"""Group the questions asked on one slide with Gemini (proposal Section 3.1, Learn step)."""

import time

import httpx2
from google import genai
from google.genai import errors, types
from pydantic import BaseModel

PROMPT = """You group student questions sent during one lecture slide in a data science course.
The questions are informal Indonesian, sometimes mixed with English, with abbreviations and typos.

Rules:
- Put two questions in the same group only if one answer would answer both (the same confusion),
  even when they use different words or do not name the function.
- Questions that share words but ask about different things go in different groups.
- A question about the lecture that is too vague to group (for example "ini maksudnya apa?") gets its own group.
- Questions that are not about the lecture content (deadlines, LMS, attendance, recordings, exams, sharing files)
  go to off_topic_ids, not to a group.
- Every question id appears exactly once.
- label: a short Indonesian summary of the shared confusion, at most 8 words.

Questions (id: text):
{questions}"""
RETRY_CODES = (500, 503, 504)
WAITS = (10, 20, 40, 60, 60)


class Group(BaseModel):
    label: str
    question_ids: list[str]


class SlideGrouping(BaseModel):
    groups: list[Group]
    off_topic_ids: list[str]


def group_slide(client: genai.Client, model: str, questions: list[dict]) -> SlideGrouping:
    """Ask Gemini to group the questions of one slide, retrying while the model is busy.

    Args:
        client: Gemini client.
        model: Model id, e.g. "gemini-3.1-flash-lite".
        questions: Questions of one slide, each with "id" and "text".

    Returns:
        The grouping, cleaned so that every question id appears exactly once.
    """
    listing = "\n".join(f"{q['id']}: {q['text']}" for q in questions)
    config = types.GenerateContentConfig(response_mime_type="application/json", response_schema=SlideGrouping,
                                         thinking_config=types.ThinkingConfig(thinking_level="low"))
    for wait in (*WAITS, None):
        try:
            reply = client.models.generate_content(model=model, contents=PROMPT.format(questions=listing), config=config)
            return clean(SlideGrouping.model_validate_json(reply.text), [q["id"] for q in questions])
        except (errors.APIError, httpx2.TransportError) as err:
            if wait is None or (isinstance(err, errors.APIError) and err.code not in RETRY_CODES):
                raise
            print(f"  Gemini busy or disconnected ({type(err).__name__}), retrying in {wait} s", flush=True)
            time.sleep(wait)
    raise AssertionError("unreachable")


def clean(grouping: SlideGrouping, ids: list[str]) -> SlideGrouping:
    """Drop unknown or repeated ids and give every missing id its own group.

    Args:
        grouping: Raw grouping from Gemini.
        ids: All question ids of the slide.

    Returns:
        A grouping where each id appears exactly once.
    """
    seen: set[str] = set()

    def take(candidates: list[str]) -> list[str]:
        kept = [i for i in dict.fromkeys(candidates) if i in ids and i not in seen]
        seen.update(kept)
        return kept

    off_topic = take(grouping.off_topic_ids)
    groups = []
    for g in grouping.groups:
        members = take(g.question_ids)
        if members:
            groups.append(Group(label=g.label, question_ids=members))
    groups += [Group(label="(missing in reply)", question_ids=[i]) for i in ids if i not in seen]
    return SlideGrouping(groups=groups, off_topic_ids=off_topic)
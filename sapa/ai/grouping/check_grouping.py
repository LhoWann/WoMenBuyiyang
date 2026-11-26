"""Run Gemini grouping on the team's sample questions and score it against the team's labels (proposal 6.1).

Pass criterion, fixed before the first run (data/README.md): at least 80% of same-slide question pairs agree on
"same group" or "different group", and Gemini sets aside at least 5 of the 6 off-topic questions.

Usage: python check_grouping.py [--model gemini-3.1-flash-lite]
"""

import argparse
import itertools
import json
import os
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types

from grouping import SlideGrouping, group_slide

HERE = Path(__file__).parent
DATA = HERE.parent / "data" / "sample_questions.jsonl"
PAIR_PASS = 0.80
OFF_TOPIC_PASS = 5
OFF = "off_topic"


def load_slides(path: Path) -> dict[tuple[int, int], list[dict]]:
    """Read the questions and split them by (meeting, page).

    Args:
        path: JSON lines file with id, meeting, page, text, group, writer.

    Returns:
        Questions per slide, in file order.
    """
    slides: dict[tuple[int, int], list[dict]] = defaultdict(list)
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            q = json.loads(line)
            slides[(q["meeting"], q["page"])].append(q)
    return dict(slides)


def score_slide(questions: list[dict], grouping: SlideGrouping) -> dict:
    """Compare Gemini's grouping of one slide with the team's labels.

    Pairs are counted only between questions the team marked on-topic. A question Gemini sets aside as off-topic is
    treated as a group of its own.

    Args:
        questions: Questions of one slide with the team's "group".
        grouping: Gemini's grouping of the same questions.

    Returns:
        Counts: agreeing pairs, total pairs, off-topic caught, off-topic total, on-topic wrongly set aside.
    """
    gemini = {i: f"{OFF}:{i}" for i in grouping.off_topic_ids}
    gemini |= {i: f"g{n}" for n, g in enumerate(grouping.groups) for i in g.question_ids}
    team = {q["id"]: q["group"] for q in questions}
    on_topic = [i for i, g in team.items() if g != OFF]
    pairs = list(itertools.combinations(on_topic, 2))
    agree = sum((team[a] == team[b]) == (gemini[a] == gemini[b]) for a, b in pairs)
    team_off = {i for i, g in team.items() if g == OFF}
    gemini_off = set(grouping.off_topic_ids)
    return {"agree": agree, "pairs": len(pairs), "off_caught": len(team_off & gemini_off), "off_total": len(team_off),
            "wrongly_off": len(gemini_off - team_off)}


def main() -> None:
    """Group every slide, print the score per slide and overall, and save the raw groupings."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--model", default=None, help="Gemini model id (default: GEMINI_MODEL from .env)")
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    load_dotenv(HERE.parent / ".env")
    model = args.model or os.environ["GEMINI_MODEL"]
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"], http_options=types.HttpOptions(timeout=120_000))

    totals = defaultdict(int)
    saved = []
    for (meeting, page), questions in load_slides(DATA).items():
        grouping = group_slide(client, model, questions)
        score = score_slide(questions, grouping)
        for key, value in score.items():
            totals[key] += value
        saved.append({"meeting": meeting, "page": page, "score": score, "grouping": grouping.model_dump()})
        print(f"M{meeting} p{page}: pairs {score['agree']}/{score['pairs']}, off-topic {score['off_caught']}/"
              f"{score['off_total']}, wrongly set aside {score['wrongly_off']}", flush=True)

    share = totals["agree"] / totals["pairs"]
    passed = share >= PAIR_PASS and totals["off_caught"] >= OFF_TOPIC_PASS
    print(f"\nModel {model}: pairs agree {totals['agree']}/{totals['pairs']} ({share:.0%}), off-topic caught "
          f"{totals['off_caught']}/{totals['off_total']}, wrongly set aside {totals['wrongly_off']} -> "
          f"{'PASS' if passed else 'FAIL'}")
    out = HERE / "results" / f"run_{datetime.now():%Y%m%d_%H%M%S}.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps({"model": model, "totals": totals, "passed": passed, "slides": saved}, indent=1,
                              ensure_ascii=False), encoding="utf-8")
    print(f"Saved {out}")


if __name__ == "__main__":
    main()
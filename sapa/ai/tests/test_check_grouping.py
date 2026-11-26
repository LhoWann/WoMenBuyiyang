import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "grouping"))

from check_grouping import DATA, load_slides, score_slide

from grouping import Group, SlideGrouping, clean

QUESTIONS = [
    {"id": "a", "group": "loc"}, {"id": "b", "group": "loc"}, {"id": "c", "group": "reset"},
    {"id": "d", "group": "off_topic"},
]


def test_perfect_grouping_scores_all_pairs_and_off_topic() -> None:
    g = SlideGrouping(groups=[Group(label="x", question_ids=["a", "b"]), Group(label="y", question_ids=["c"])],
                      off_topic_ids=["d"])
    score = score_slide(QUESTIONS, g)
    if score != {"agree": 3, "pairs": 3, "off_caught": 1, "off_total": 1, "wrongly_off": 0}:
        raise AssertionError(score)


def test_merging_everything_and_missing_off_topic_is_penalised() -> None:
    g = SlideGrouping(groups=[Group(label="x", question_ids=["a", "b", "c", "d"])], off_topic_ids=[])
    score = score_slide(QUESTIONS, g)
    if (score["agree"], score["off_caught"]) != (1, 0):
        raise AssertionError(score)


def test_on_topic_question_set_aside_counts_as_its_own_group() -> None:
    g = SlideGrouping(groups=[Group(label="x", question_ids=["a", "c"])], off_topic_ids=["b", "d"])
    score = score_slide(QUESTIONS, g)
    if (score["agree"], score["wrongly_off"]) != (1, 1):
        raise AssertionError(score)


def test_clean_removes_unknown_and_repeated_ids_and_adds_missing() -> None:
    raw = SlideGrouping(groups=[Group(label="x", question_ids=["a", "a", "zz"]), Group(label="y", question_ids=["a"])],
                        off_topic_ids=["d"])
    got = clean(raw, ["a", "b", "c", "d"])
    ids = [i for g in got.groups for i in g.question_ids] + got.off_topic_ids
    if sorted(ids) != ["a", "b", "c", "d"] or len(got.groups) != 3:
        raise AssertionError(got)


def test_sample_file_has_50_questions_on_10_slides() -> None:
    slides = load_slides(DATA)
    if (sum(len(v) for v in slides.values()), len(slides)) != (50, 10):
        raise AssertionError({k: len(v) for k, v in slides.items()})
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from qlc_demo import SAMPLE, questions


def test_sample_gets_declaration_question_with_one_correct_option() -> None:
    found = questions(SAMPLE.read_text(encoding="utf-8"), "class_means(5.0)")
    types = {q["type"] for q in found}
    if "VariableDeclaration" not in types:
        raise AssertionError(f"expected a VariableDeclaration question, got {types}")
    for q in found:
        if not any(opt["correct"] for opt in q["options"]):
            raise AssertionError(f"question without a correct option: {q['question']}")
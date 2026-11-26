"""Generate qlcpy questions for a sample program, as in proposal Section 4.3."""

import sys
from pathlib import Path

from qlcpy import QLCRequest, generate

SAMPLE = Path(__file__).parent / "samples" / "class_means.py"
STRUCTURE_TYPES = ["VariableNames", "ParameterNames", "VariableDeclaration", "LoopEnd", "LoopCount", "VariableTrace"]


def questions(src: str, call: str, count: int = 6) -> list[dict]:
    """Return qlcpy questions about the program, one per question type.

    Args:
        src: Python source of the program.
        call: Call to run, e.g. "class_means(5.0)", so value-based types can trace it.
        count: Maximum number of questions.

    Returns:
        Questions as dicts with "type", "question" and "options" (each option has "answer" and "correct").
    """
    found = generate(src, [QLCRequest(count, types=STRUCTURE_TYPES, unique_types=True)], call=call)
    return [qlc.to_dict() for qlc in found]


def main() -> None:
    """Print the questions for the sample with the correct options marked."""
    sys.stdout.reconfigure(encoding="utf-8")
    for q in questions(SAMPLE.read_text(encoding="utf-8"), "class_means(5.0)"):
        print(f"[{q['type']}] {q['question']}")
        for opt in q["options"]:
            print(f"  {'*' if opt['correct'] else ' '} {opt['answer']}")


if __name__ == "__main__":
    main()
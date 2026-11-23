# Scratch Space

Use `agent_space/` (git-ignored, at repo root) for temporary scripts, scratch files, and throwaway experiments. Do not commit files from this directory.

# Environment

If any tool you're trying to use (pip, python, etc) is missing, check for a `.venv` directory in the project root or its parent directory. If found, activate it and retry. If no `.venv` is found, stop and ask the user if an environment is needed. Do NOT try to find alternatives or install these tools.

# Asserts

Never silence ruff S101 with a noqa. Rewrite the assert as `if not cond: raise AssertionError(msg)`, since plain `assert` is stripped by `python -O`.

# Coding Style

- Minimize comments; code should be self-explanatory. Comments only for non-obvious global context. ASCII only in new comments.
- No trivial (1-2 LOC) helpers used only once unless it clearly improves readability.
- Explicit state: define all members in the class, no dynamic `setattr`/`getattr`.
- Match existing code style and architectural patterns. If uncertain, choose the simpler, more concise implementation.
- Line length 120. 4-space indents. PEP484 annotations on function signatures. Google-style docstrings (do not repeat types/defaults).
- Imports: standard library, then third-party, then local.
- Naming: snake_case functions, PascalCase classes.
- Catch specific exceptions only.
- Prefer one line over ruff-split lines; shorten names or use local variables.

# Research Rules

- Every component must have a call path from the training/eval entry point and a test. No dead code.
- Cite only papers verified from a primary source (arXiv/venue page). Never invent references.
- No newline blank space: no file may end with an empty line. If the content ends at line 77, there is no blank line 78 (no trailing newline at end of file). Applies to every file (code, Markdown, YAML, TOML, txt). For this reason ruff W292 is ignored in `pyproject.toml`, and `ruff format` is not used because it re-adds the final newline.

# Skill
- Always use skill from .agents\skills
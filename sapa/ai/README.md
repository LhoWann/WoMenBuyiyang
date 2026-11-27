# SAPA AI part

Three jobs, matching proposal Sections 3.1 and 4.3. Run everything with the repo venv:
`D:\GDGoC26\.venv\Scripts\python.exe` (it already has qlcpy, pandas, scikit-learn and pytest).

| Folder | Job | Runs where | Check before real students use it |
| --- | --- | --- | --- |
| `grouping/` | Gemini groups similar questions per slide and sets aside off-topic ones | Cloud Function | 50 sample questions written by the team: share placed in the same group as a team member would (proposal 6.1) |
| `drafts/` | Gemini drafts lecture quiz questions from slides a student marked "I'm lost" | Cloud Function | Lecturer approves every draft |
| `templates/` | Practicum questions about the student's own code: qlcpy for structure, our templates for values | Browser (Pyodide) | qlcpy runs inside Pyodide: done 27 Nov, `pyodide_check/` (needs Pyodide 0.29, Python 3.13) |

`samples/` holds code the team writes for demos and tests. Never put real student work here.

## Start

```bash
cd D:/GDGoC26/sapa/ai
../../.venv/Scripts/python.exe qlc_demo.py        # questions for samples/class_means.py, as in proposal 4.3
../../.venv/Scripts/python.exe -m pytest tests -q
cd pyodide_check && npm install && node check_qlcpy.mjs   # qlcpy inside Pyodide, answer keys checked
```

For Gemini work, copy `.env.example` to `.env`, put the key from Google AI Studio in it, and install the SDK into the
repo venv with `../../.venv/Scripts/python.exe -m pip install -r requirements.txt`.

## Next steps

1. Done 27 Nov: qlcpy runs inside Pyodide 0.29.5 (`pyodide_check/`). Pyodide 314.x (Python 3.14) fails because qlcpy
   imports `ast.Num`; Dani's runner must use the same 0.29 version.
2. Value templates in `templates/`: questions such as "How many rows does `long_ones` have?" with keys from running
   the code. Use only the standard library (`ast`) so they also run in Pyodide.
3. Grouping prompt in `grouping/`, tested on the team's 50 sample questions in `data/` (JSON lines:
   `{"slide": 7, "text": "...", "group": "..."}`, where `group` is the team member's label).
# SAPA

SAPA is a web app that a lecturer sets up for one course. Students ask about a slide anonymously or tap "I'm lost",
get a short quiz about the slides they marked and about their own practicum notebook, and book a help session with an
assistant who already sees the missed concept. Built for STACK 2026 (GDGoC ITB), Case 1: Smarter Campus and Learning.

## Folders

| Folder | Owner | Contents |
| --- | --- | --- |
| `ai/` | Ridwan | Gemini question grouping, lecture question drafts, practicum question templates (qlcpy and our own) |
| `web/` | Dani | React app: student, assistant and lecturer screens, notebook upload, Pyodide runner (not created yet) |
| `functions/` | Naufal | Firebase Cloud Functions that call Gemini and keep its key (not created yet) |

Create `web/` with `npm create vite@latest web -- --template react` and `functions/` with `firebase init functions`
when that work starts. Designs (Annisa) live outside the repo until they are exported as images.

## Rules for this repository

- No real student files, names or code. Demos and tests use notebooks the team writes.
- Never commit API keys. Put them in a local `.env` (git-ignored); see `ai/.env.example`.

## AI assistance

The handbook asks that material AI assistance be disclosed in the product README. Update this list as tools are used.

| Tool | Role | What the team did |
| --- | --- | --- |
| Claude Code (Anthropic) | Coding assistant | Team members review and test all code before committing |
| Antigravity (Google) | Coding assistant | Team members review and test all code before committing |
| Gemini API (Google) | Part of the product: groups questions and drafts lecture questions | The lecturer approves drafts before students see them |
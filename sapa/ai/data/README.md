# Sample questions for the grouping check

Proposal 6.1 promises a check on 50 sample questions written by the team: we compare how Gemini groups them with how
a team member groups them. These questions stand in for what students type during a lecture, so they must look like
real student messages, but they must be written by us.

## Rules

- Write every question yourselves. You may rewrite, in your own words, a question you remember a student asking
  (the current file mixes invented and recalled questions), but do not paste real chat messages or the lecturer's
  quiz questions.
- No real names, NIM or class names in the text.
- Use the lecturer's slides (Materi_IPSD.zip, kept outside the repo) only to know what each slide is about.

## What to write (50 questions)

| Part | Count | Why |
| --- | --- | --- |
| Meetings | 3 (for example M2 Pengolahan Data, M3 Eksplorasi Data, M6 or M7 Klasifikasi) | Different topics |
| Slides | About 10 in total, 3 or 4 per meeting | Grouping happens per slide |
| Questions per slide | About 4 or 5 | Enough to form groups |
| Groups per slide | 2 or 3 groups of 2 to 3 questions, plus 1 question alone | Tests merging and keeping apart |
| Off-topic | About 6 in total (deadlines, LMS, "slide-nya dishare?") | Gemini should set these aside |
| Vague | About 3 ("ini maksudnya apa?") | Hard case; label them `vague` |

Inside a group, change the wording, not the confusion: one question uses the function name, another describes the
problem in everyday words. Also add at least 2 "traps": questions that share words but are different confusions,
which must go to different groups.

Style: informal Indonesian like students write in chat, English terms mixed in, short forms (yg, gmn, knp, kak), a few
typos, 3 to 25 words. One or two questions in English are fine.

Split the writing: two or three members write about 17 each, so the styles differ. After writing, one other member
reads the group labels and fixes any that are unclear.

## Format

One question per line in `sample_questions.jsonl`:

```
{"id": "q01", "meeting": 2, "page": 35, "text": "...", "group": "dropna_vs_fillna", "writer": "R"}
```

- `page`: page number in the slide PDF (this is what SAPA shows), not the number printed on the slide.
- `group`: a short snake_case label for the confusion, unique within the slide. Use `off_topic` and `vague` for those
  two kinds.
- `writer`: the writer's initial, to check that the styles are mixed.

## Pass criterion (fix it before running Gemini)

For every pair of questions on the same slide, check whether Gemini and the team agree on "same group" or "different
group". Pass if at least 80% of pairs agree and Gemini sets aside at least 5 of the 6 off-topic questions.
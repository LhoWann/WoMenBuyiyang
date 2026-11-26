"""Print aggregate counts for the SAPA survey export. Open-text answers are counted, never printed.

Usage: python -I analyze_survey.py "Survei Pengalaman Kuliah dan Praktikum.csv"
"""

import collections
import csv
import sys

MULTI = {
    2: ["Screenshot kode di laporan", "Link Google Colab", "File notebook (.ipynb)"],
    5: [
        "Saya tulis sendiri dari awal",
        "Saya ubah dari contoh di modul",
        "Bantuan atau contoh dari teman",
        "Dibuat atau dibantu AI (ChatGPT, Gemini, dll.)",
        "Dari internet (StackOverflow, blog, dll.)",
    ],
    7: [
        "Malu atau takut dianggap tidak paham",
        "Bingung cara merumuskan pertanyaan",
        "Tidak mau mengganggu jalannya kelas",
        "Menunggu bertanya ke teman setelah kelas",
        "Materinya terlalu cepat",
    ],
    9: ["Bertanya langsung saat praktikum", "Chat asprak lewat WhatsApp", "Bertanya ke teman saja", "Tidak meminta bantuan"],
}
OPEN_TEXT = (14, 15)


def main(path: str) -> None:
    """Print response count, then counts per answer for every closed question.

    Args:
        path: CSV exported from Google Forms.
    """
    sys.stdout.reconfigure(encoding="utf-8")
    with open(path, encoding="utf-8-sig") as f:
        header, *rows = list(csv.reader(f))
    print(f"responses {len(rows)} | first {min(r[0] for r in rows)} | last {max(r[0] for r in rows)}")
    for j in range(1, len(header)):
        answers = [r[j] for r in rows if r[j].strip()]
        print(f"== {header[j][:60]} (answered {len(answers)})")
        if j in OPEN_TEXT:
            continue
        if j not in MULTI:
            for value, n in sorted(collections.Counter(answers).items()):
                print(f"   {n:3d}  {value}")
            continue
        counts, other = collections.Counter(), 0
        for answer in answers:
            rest = answer
            for option in MULTI[j]:
                if option in rest:
                    counts[option] += 1
                    rest = rest.replace(option, "")
            other += bool(rest.strip(" ,;"))
        for option in MULTI[j]:
            print(f"   {counts[option]:3d}  {option}")
        print(f"   {other:3d}  (other text, not shown)")


if __name__ == "__main__":
    main(sys.argv[1])
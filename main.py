"""Doing main things."""

from __future__ import annotations

from typing import Dict
from typing import List
from pathlib import Path

BOOKS_DIR = Path("books")

def word_count(s: str) -> int:
    """Return total word count for a string."""
    return len(s.split())

def char_count(s: str) -> List[Dict[str, str | int]]:
    """Return a dict of the frequency of each char found."""
    cc = {}
    for c in s:
        c = c.lower()
        cc[c] = cc.get(c, 0) + 1

    cc_list = [{"char": char, "count": count} for char, count in cc.items()]
    cc_list.sort(reverse=True, key=lambda x: x["count"])
    return cc_list


def report(book_path: Path) -> str:
    """Return a report of the input book."""
    with open(book_path, "r") as f:
        contents = f.read()
    wc = word_count(contents)
    cc = char_count(contents)

    report_lines = [f"--- Begin report of {book_path} ---"]
    report_lines.append(f"{wc} words found in the document\n")
    for x in cc:
        char, count = x["char"], x["count"]
        if char.isalpha():
            report_lines.append(f"The '{char}' character was found {count} times")

    report_lines.append("--- End report ---")
    
    return "\n".join(report_lines)


def main() -> None:
    """Doing main things"""
    frankenstein_path = BOOKS_DIR / "frankenstein.txt"
    print(report(frankenstein_path))

if __name__ == "__main__":
    main()
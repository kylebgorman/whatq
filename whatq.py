#!/usr/bin/env python

import argparse
import collections
import lzma

from typing import TextIO


# Taxonomy based on:
# https://en.wikipedia.org/wiki/Quotation_mark#Summary_table
# We list the smartquote types but don't assume they'll be done consistently.
QUOTE_TYPES = {
    # American English-like.
    # Apparently Hebrew doesn't use smartquotes.
    # Apparently Bosnian, Finnish, and Swedish only use the right smartquote.
    "Double quotation marks": ["“", "”", '"'],
    # German-like.
    "Lower-upper double quotation marks": ["„", "“"],
    # British Isles-like.
    "Single quotation marks": ["‘", "’", "'"],
    # French-like.
    # Apparently Danish uses »...«.
    # Apparently Finnish and Swedish sometimes use »...».
    "Guillemets": ["«", "»"],
    # North Korean, Mongolian, Tibetan, etc.
    "Double angle brackets": ["《", "》"],
    # Chinese and Japanese.
    "Corner brackets": ["「", "」"],
}


def _open(path: str, xz: bool) -> TextIO:
    return lzma.open(path, "rt") if xz else open(path, "r")


def main(args: argparse.ArgumentParser) -> None:
    # Collects the counts.
    qt_counts = collections.Counter()
    for path in args.path:
        with _open(path, args.xz) as source:
            for line in source:
                line = line.rstrip()
                if not line:
                    continue
                for qt, qt_chars in QUOTE_TYPES.items():
                    qt_count = 0
                    for char in line:
                        if char in qt_chars:
                            qt_count += 1
                    if qt_count:
                        qt_counts[qt] += qt_count
    # Logs the counts.
    for qt, count in qt_counts.most_common(1):
        qt_chars = QUOTE_TYPES[qt]
        print(f"{qt}\t({' '.join(qt_chars)})\t{count:,}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--xz", action="store_true", default=False, help="decompress .xz data"
    )
    parser.add_argument("path", nargs="+", help="one or more input files")
    main(parser.parse_args())

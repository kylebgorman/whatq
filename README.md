Quotation mark style
====================

This repository uses [CC-100](https://data.statmt.org/cc-100/) data to determine
the most common [quotation mark
style](https://en.wikipedia.org/wiki/Quotation_mark#Summary_table) in a variety
of languages and writing systems

The code is found in [`whatq.py`](whatq.py) and [`cc-100.sh`](cc-100.sh).

The most common quotation mark style for each language and writing system is
found in [`cc-100.tsv`](cc-100.tsv).

Our method finds that single quotes are most common in English (`en`), even
though these are not commonly used for quotations in American English. This
might reflect British style, or the use of apostrophe `'` for contractions and
possessives may have swamped other patterns. We're not sure yet. A more
sophisticated method ought to be able to tease this out.

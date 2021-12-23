[![Github CI Status](https://github.com/iwsfutcmd/unicodedataplus/workflows/Tests/badge.svg)](https://github.com/iwsfutcmd/unicodedataplus/actions?query=workflow%3A%22Tests%22)
[![PyPI](https://img.shields.io/pypi/v/unicodedataplus.svg)](https://pypi.org/project/unicodedataplus/)

unicodedataplus
============

Drop-in replacement for `unicodedata` with extensions for additional Unicode properties.

Currently supported additional Unicode properties:

* Script: `script(chr)`
* Script Extensions: `script_extensions(chr)`
* Block: `block(chr)`
* Indic Positional Category: `indic_positional_category(chr)`
* Indic Syllabic Category: `indic_syllabic_category(chr)`
* Grapheme Cluster Break: `grapheme_cluster_break(chr)`
* Total Strokes (CJK): `total_strokes(chr)`

Additionally, two dictionaries (`property_value_aliases` and `property_value_by_alias`) are provided for Property Value Alias lookup.

The versions of this package match unicode versions, so unicodedataplus==14.0.0 is data from unicode 14.0.0.

Forked from https://github.com/mikekap/unicodedata2

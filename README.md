[![Github CI Status](https://github.com/iwsfutcmd/unicodedataplus/workflows/Tests/badge.svg)](https://github.com/iwsfutcmd/unicodedataplus/actions?query=workflow%3A%22Tests%22)
[![PyPI](https://img.shields.io/pypi/v/unicodedataplus.svg)](https://pypi.org/project/unicodedataplus/)

unicodedataplus
============

Drop-in replacement for `unicodedata` with extensions for additional Unicode properties.

Currently supported additional Unicode properties:

* Script: `script(chr)`
* Script Extensions: `script_extensions(chr)`
* Block: `block(chr)`
* Indic Conjunct Break: `indic_conjunct_break(chr)`
* Indic Positional Category: `indic_positional_category(chr)`
* Indic Syllabic Category: `indic_syllabic_category(chr)`
* Grapheme Cluster Break: `grapheme_cluster_break(chr)`
* Word Break: `word_break(chr)`
* Sentence Break: `sentence_break(chr)`
* Line Break: `line_break(chr)`
* Vertical Orientation: `vertical_orientation(chr)`
* Age: `age(chr)`
* Total Strokes (CJK): `total_strokes(chr, source='G')`
  * source='G' = Simplified stroke count. source='T' = Traditional stroke count.
* Emoji: `is_emoji(chr)`
* Emoji Presentation: `is_emoji_presentation(chr)`
* Emoji Modifier: `is_emoji_modifier(chr)`
* Emoji Modifier Base: `is_emoji_modifier_base(chr)`
* Emoji Component: `is_emoji_component(chr)`
* Extended Pictographic: `is_extended_pictographic(chr)`

Additionally, two dictionaries (`property_value_aliases` and `property_value_by_alias`) are provided for Property Value Alias lookup.

The versions of this package match unicode versions, so unicodedataplus==16.0.0 is data from unicode 16.0.0.

Forked from https://github.com/mikekap/unicodedata2

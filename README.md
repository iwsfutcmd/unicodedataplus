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

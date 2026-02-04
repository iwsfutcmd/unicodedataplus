""" Tests for the unicodedataplus module.

    Written by Marc-Andre Lemburg (mal@lemburg.com).

    (c) Copyright CNRI, All Rights Reserved. NO WARRANTY.

"""

from functools import partial
import hashlib
from http.client import HTTPException
import sys
import unicodedataplus as unicodedata
import unittest

def iterallchars():
    maxunicode = sys.maxunicode
    return map(chr, range(maxunicode + 1))


class UnicodeFunctionsTest(unittest.TestCase):
    db = unicodedata
    old = False


    # Update this if the database changes. Make sure to do a full rebuild
    # (e.g. 'make distclean && make') to get the correct checksum.
    expectedchecksum = 'bb5984673c5b4158a615fd6e2bd2e32c786ed095'

    def test_function_checksum(self):
        db = self.db
        data = []
        h = hashlib.sha1()

        for char in iterallchars():
            data = "%.12g%.12g%.12g%s%s%s%s%s%s%s" % (
                # Properties
                db.digit(char, -1),
                db.numeric(char, -1),
                db.decimal(char, -1),
                db.category(char),
                db.bidirectional(char),
                db.decomposition(char),
                db.mirrored(char),
                db.combining(char),
                db.east_asian_width(char),
                db.name(char, ""),
            )
            h.update(data.encode("ascii"))
        result = h.hexdigest()
        self.assertEqual(result, self.expectedchecksum)

    def test_name_inverse_lookup(self):
        for char in iterallchars():
            looked_name = self.db.name(char, None)
            if looked_name is not None:
                self.assertEqual(self.db.lookup(looked_name), char)

    def test_no_names_in_pua(self):
        puas = [*range(0xe000, 0xf8ff),
                *range(0xf0000, 0xfffff),
                *range(0x100000, 0x10ffff)]
        for i in puas:
            char = chr(i)
            self.assertRaises(ValueError, self.db.name, char)

    def test_lookup_nonexistant(self):
        # just make sure that lookup can fail
        for nonexistent in [
            "LATIN SMLL LETR A",
            "OPEN HANDS SIGHS",
            "DREGS",
            "HANDBUG",
            "MODIFIER LETTER CYRILLIC SMALL QUESTION MARK",
            "???",
        ]:
            self.assertRaises(KeyError, self.db.lookup, nonexistent)

    def test_digit(self):
        self.assertEqual(self.db.digit('A', None), None)
        self.assertEqual(self.db.digit('9'), 9)
        self.assertEqual(self.db.digit('\u215b', None), None)
        self.assertEqual(self.db.digit('\u2468'), 9)
        self.assertEqual(self.db.digit('\U00020000', None), None)
        self.assertEqual(self.db.digit('\U0001D7FD'), 7)

        # New in 13.0.0
        self.assertEqual(self.db.digit('\U0001fbf9', None), 9)
        # New in 14.0.0
        self.assertEqual(self.db.digit('\U00016ac9', None), 9)
        # New in 15.0.0
        self.assertEqual(self.db.digit('\U0001e4f9', None), 9)

        # unicodedataplus tests
        self.assertEqual(self.db.digit('\U00016AC3'), 3)
        self.assertEqual(self.db.digit('\U0001E4F4'), 4)
        self.assertEqual(self.db.digit('\U00010D42'), 2)

        self.assertRaises(TypeError, self.db.digit)
        self.assertRaises(TypeError, self.db.digit, 'xx')
        self.assertRaises(ValueError, self.db.digit, 'x')

    def test_numeric(self):
        self.assertEqual(self.db.numeric('A',None), None)
        self.assertEqual(self.db.numeric('9'), 9)
        self.assertEqual(self.db.numeric('\u215b'), 0.125)
        self.assertEqual(self.db.numeric('\u2468'), 9.0)
        self.assertEqual(self.db.numeric('\U00020000', None), None)

        # New in 4.1.0
        self.assertEqual(self.db.numeric('\U0001012A', None), None if self.old else 9000)
        # New in 5.0.0
        self.assertEqual(self.db.numeric('\u07c0', None), None if self.old else 0.0)
        # New in 5.1.0
        self.assertEqual(self.db.numeric('\ua627', None), None if self.old else 7.0)
        # New in 6.0.0
        self.assertEqual(self.db.numeric('\u0b72', None), None if self.old else 0.25)
        # New in 12.0.0
        self.assertEqual(self.db.numeric('\U0001ed3c', None), None if self.old else 0.5)
        # New in 13.0.0
        self.assertEqual(self.db.numeric('\U0001fbf9', None), None if self.old else 9)
        # New in 14.0.0
        self.assertEqual(self.db.numeric('\U00016ac9', None), None if self.old else 9)
        # New in 15.0.0
        self.assertEqual(self.db.numeric('\U0001e4f9', None), None if self.old else 9)

        # unicodedataplus tests
        self.assertEqual(self.db.numeric('\ua627'), 7.0)
        self.assertEqual(self.db.numeric('\U0001012A'), 9000)
        self.assertEqual(self.db.numeric('\U0001D2D1'), 17)
        self.assertEqual(self.db.numeric('\U0001E5F7'), 6.0)

        self.assertRaises(TypeError, self.db.numeric)
        self.assertRaises(TypeError, self.db.numeric, 'xx')
        self.assertRaises(ValueError, self.db.numeric, 'x')

    def test_decimal(self):
        self.assertEqual(self.db.decimal('A',None), None)
        self.assertEqual(self.db.decimal('9'), 9)
        self.assertEqual(self.db.decimal('\u215b', None), None)
        self.assertEqual(self.db.decimal('\u2468', None), None)
        self.assertEqual(self.db.decimal('\U00020000', None), None)
        self.assertEqual(self.db.decimal('\U0001D7FD'), 7)

        # New in 4.1.0
        self.assertEqual(self.db.decimal('\xb2', None), 2 if self.old else None)
        self.assertEqual(self.db.decimal('\u1369', None), 1 if self.old else None)
        # New in 5.0.0
        self.assertEqual(self.db.decimal('\u07c0', None), None if self.old else 0)
        # New in 13.0.0
        self.assertEqual(self.db.decimal('\U0001fbf9', None), None if self.old else 9)
        # New in 14.0.0
        self.assertEqual(self.db.decimal('\U00016ac9', None), None if self.old else 9)
        # New in 15.0.0
        self.assertEqual(self.db.decimal('\U0001e4f9', None), None if self.old else 9)

        # unicodedataplus tests
        self.assertEqual(self.db.decimal('\U00016139'), 9)
        self.assertEqual(self.db.decimal('\U00016AC3'), 3)

        self.assertRaises(TypeError, self.db.decimal)
        self.assertRaises(TypeError, self.db.decimal, 'xx')
        self.assertRaises(ValueError, self.db.decimal, 'x')

    def test_category(self):
        self.assertEqual(self.db.category('\uFFFE'), 'Cn')
        self.assertEqual(self.db.category('a'), 'Ll')
        self.assertEqual(self.db.category('A'), 'Lu')
        self.assertEqual(self.db.category('\U00020000'), 'Lo')

        # New in 4.1.0
        self.assertEqual(self.db.category('\U0001012A'), 'Cn' if self.old else 'No')
        self.assertEqual(self.db.category('\U000e01ef'), 'Cn' if self.old else 'Mn')
        # New in 5.1.0
        self.assertEqual(self.db.category('\u0374'), 'Sk' if self.old else 'Lm')
        # Changed in 13.0.0
        self.assertEqual(self.db.category('\u0b55'), 'Cn' if self.old else 'Mn')
        self.assertEqual(self.db.category('\U0003134a'), 'Cn' if self.old else 'Lo')
        # Changed in 14.0.0
        self.assertEqual(self.db.category('\u061d'), 'Cn' if self.old else 'Po')
        self.assertEqual(self.db.category('\U0002b738'), 'Cn' if self.old else 'Lo')
        # Changed in 15.0.0
        self.assertEqual(self.db.category('\u0cf3'), 'Cn' if self.old else 'Mc')
        self.assertEqual(self.db.category('\U000323af'), 'Cn' if self.old else 'Lo')

        # unicodedataplus tests
        self.assertEqual(self.db.category('\U0001012A'), 'No')
        self.assertEqual(self.db.category('\U000110C2'), 'Mn')
        self.assertEqual(self.db.category('\U0001F7D9'), 'So')
        self.assertEqual(self.db.category('\U00011F5A'), 'Mn')

        self.assertRaises(TypeError, self.db.category)
        self.assertRaises(TypeError, self.db.category, 'xx')

    def test_bidirectional(self):
        self.assertEqual(self.db.bidirectional('\uFFFE'), '')
        self.assertEqual(self.db.bidirectional(' '), 'WS')
        self.assertEqual(self.db.bidirectional('A'), 'L')
        self.assertEqual(self.db.bidirectional('\U00020000'), 'L')

        # New in 4.1.0
        self.assertEqual(self.db.bidirectional('+'), 'ET' if self.old else 'ES')
        self.assertEqual(self.db.bidirectional('\u0221'), '' if self.old else 'L')
        self.assertEqual(self.db.bidirectional('\U000e01ef'), '' if self.old else 'NSM')
        # New in 13.0.0
        self.assertEqual(self.db.bidirectional('\u0b55'), '' if self.old else 'NSM')
        self.assertEqual(self.db.bidirectional('\U0003134a'), '' if self.old else 'L')
        # New in 14.0.0
        self.assertEqual(self.db.bidirectional('\u061d'), '' if self.old else 'AL')
        self.assertEqual(self.db.bidirectional('\U0002b738'), '' if self.old else 'L')
        # New in 15.0.0
        self.assertEqual(self.db.bidirectional('\u0cf3'), '' if self.old else 'L')
        self.assertEqual(self.db.bidirectional('\U000323af'), '' if self.old else 'L')
        # New in 16.0.0
        self.assertEqual(self.db.bidirectional('\u0897'), '' if self.old else 'NSM')
        self.assertEqual(self.db.bidirectional('\U0001fbef'), '' if self.old else 'ON')

        # unicodedataplus tests
        self.assertEqual(self.db.bidirectional('\u0876'), 'AL')
        self.assertEqual(self.db.bidirectional('\U00010EFE'), 'NSM')
        self.assertEqual(self.db.bidirectional('\U00010EFE'), 'NSM')
        self.assertEqual(self.db.bidirectional('\U0001FABE'), 'ON')

        self.assertRaises(TypeError, self.db.bidirectional)
        self.assertRaises(TypeError, self.db.bidirectional, 'xx')

    def test_decomposition(self):
        self.assertEqual(self.db.decomposition('\uFFFE'),'')
        self.assertEqual(self.db.decomposition('\u00bc'), '<fraction> 0031 2044 0034')

        self.assertRaises(TypeError, self.db.decomposition)
        self.assertRaises(TypeError, self.db.decomposition, 'xx')

    def test_mirrored(self):
        self.assertEqual(self.db.mirrored('\uFFFE'), 0)
        self.assertEqual(self.db.mirrored('a'), 0)
        self.assertEqual(self.db.mirrored('\u2201'), 1)
        self.assertEqual(self.db.mirrored('\U00020000'), 0)

        # New in 5.0.0
        self.assertEqual(self.db.mirrored('\u0f3a'), 0 if self.old else 1)
        self.assertEqual(self.db.mirrored('\U0001d7c3'), 0 if self.old else 1)
        # New in 11.0.0
        self.assertEqual(self.db.mirrored('\u29a1'), 1 if self.old else 0)
        # New in 14.0.0
        self.assertEqual(self.db.mirrored('\u2e5c'), 0 if self.old else 1)
        # New in 16.0.0
        self.assertEqual(self.db.mirrored('\u226D'), 0 if self.old else 1)

        # unicodedataplus tests
        self.assertEqual(self.db.mirrored('\U00010EFE'), 0)

        self.assertRaises(TypeError, self.db.mirrored)
        self.assertRaises(TypeError, self.db.mirrored, 'xx')

    def test_combining(self):
        self.assertEqual(self.db.combining('\uFFFE'), 0)
        self.assertEqual(self.db.combining('a'), 0)
        self.assertEqual(self.db.combining('\u20e1'), 230)
        self.assertEqual(self.db.combining('\U00020000'), 0)

        # New in 4.1.0
        self.assertEqual(self.db.combining('\u0350'), 0 if self.old else 230)
        # New in 9.0.0
        self.assertEqual(self.db.combining('\U0001e94a'), 0 if self.old else 7)
        # New in 13.0.0
        self.assertEqual(self.db.combining('\u1abf'), 0 if self.old else 220)
        self.assertEqual(self.db.combining('\U00016ff1'), 0 if self.old else 6)
        # New in 14.0.0
        self.assertEqual(self.db.combining('\u0c3c'), 0 if self.old else 7)
        self.assertEqual(self.db.combining('\U0001e2ae'), 0 if self.old else 230)
        # New in 15.0.0
        self.assertEqual(self.db.combining('\U00010efd'), 0 if self.old else 220)
        # New in 16.0.0
        self.assertEqual(self.db.combining('\u0897'), 0 if self.old else 230)

        # unicodedataplus tests
        self.assertEqual(self.db.combining('\U00010EFE'), 220)
        self.assertEqual(self.db.combining('\u0897'), 230)

        self.assertRaises(TypeError, self.db.combining)
        self.assertRaises(TypeError, self.db.combining, 'xx')

    def test_normalization(self):
        # Test normalize() and is_normalized()
        def check(ch, expected):
            if isinstance(expected, str):
                expected = [expected]*4
            forms = ('NFC', 'NFD', 'NFKC', 'NFKD')
            result = [self.db.normalize(form, ch) for form in forms]
            self.assertEqual(ascii(result), ascii(list(expected)))
            self.assertEqual([self.db.is_normalized(form, ch) for form in forms],
                             [ch == y for x, y in zip(result, expected)])

        check('', '')
        check('A', 'A')
        check(' ', ' ')
        check('\U0010ffff', '\U0010ffff')
        check('abc', 'abc')
        # Broken in 4.0.0
        check('\u0340', '\u0300')
        check('\u0300', '\u0300')
        check('\U0002fa1d', '\U0002a600')
        check('\U0002a600', '\U0002a600')
        check('\u0344', '\u0308\u0301')
        check('\u0308\u0301', '\u0308\u0301')
        # Broken in 4.0.0 and 4.0.1
        check('\U0001d1bc', '\U0001d1ba\U0001d165')
        check('\U0001d1ba\U0001d165', '\U0001d1ba\U0001d165')
        check('\ufb2c', '\u05e9\u05bc\u05c1')
        check('\u05e9\u05bc\u05c1', '\u05e9\u05bc\u05c1')
        check('\U0001d1c0', '\U0001d1ba\U0001d165\U0001d16f')
        check('\U0001d1ba\U0001d165\U0001d16f', '\U0001d1ba\U0001d165\U0001d16f')

        # Broken in 4.0.0
        check('\xa0', ['\xa0', '\xa0', ' ', ' '])
        check('\u2003', ['\u2003', '\u2003', ' ', ' '])
        check('\U0001d7ff', ['\U0001d7ff', '\U0001d7ff', '9', '9'])

        check('\xa8', ['\xa8', '\xa8', ' \u0308', ' \u0308'])
        check(' \u0308', ' \u0308')

        check('\xc0', ['\xc0', 'A\u0300']*2)
        check('A\u0300', ['\xc0', 'A\u0300']*2)

        check('\ud7a3', ['\ud7a3', '\u1112\u1175\u11c2']*2)
        check('\u1112\u1175\u11c2', ['\ud7a3', '\u1112\u1175\u11c2']*2)

        check('\xb4', ['\xb4', '\xb4', ' \u0301', ' \u0301'])
        check('\u1ffd', ['\xb4', '\xb4', ' \u0301', ' \u0301'])
        check(' \u0301', ' \u0301')

        check('\xc5', ['\xc5', 'A\u030a']*2)
        check('\u212b', ['\xc5', 'A\u030a']*2)
        check('A\u030a', ['\xc5', 'A\u030a']*2)

        check('\u1f71', ['\u03ac', '\u03b1\u0301']*2)
        check('\u03ac', ['\u03ac', '\u03b1\u0301']*2)
        check('\u03b1\u0301', ['\u03ac', '\u03b1\u0301']*2)

        check('\u01c4', ['\u01c4', '\u01c4', 'D\u017d', 'DZ\u030c'])
        check('D\u017d', ['D\u017d', 'DZ\u030c']*2)
        check('DZ\u030c', ['D\u017d', 'DZ\u030c']*2)

        check('\u1fed', ['\u1fed', '\xa8\u0300', ' \u0308\u0300', ' \u0308\u0300'])
        check('\xa8\u0300', ['\u1fed', '\xa8\u0300', ' \u0308\u0300', ' \u0308\u0300'])
        check(' \u0308\u0300', ' \u0308\u0300')

        check('\u326e', ['\u326e', '\u326e', '\uac00', '\u1100\u1161'])
        check('\u320e', ['\u320e', '\u320e', '(\uac00)', '(\u1100\u1161)'])
        check('(\uac00)', ['(\uac00)', '(\u1100\u1161)']*2)
        check('(\u1100\u1161)', ['(\uac00)', '(\u1100\u1161)']*2)

        check('\u0385', ['\u0385', '\xa8\u0301', ' \u0308\u0301', ' \u0308\u0301'])
        check('\u1fee', ['\u0385', '\xa8\u0301', ' \u0308\u0301', ' \u0308\u0301'])
        check('\xa8\u0301', ['\u0385', '\xa8\u0301', ' \u0308\u0301', ' \u0308\u0301'])
        check(' \u0308\u0301', ' \u0308\u0301')

        check('\u1fdf', ['\u1fdf', '\u1ffe\u0342', ' \u0314\u0342', ' \u0314\u0342'])
        check('\u1ffe\u0342', ['\u1fdf', '\u1ffe\u0342', ' \u0314\u0342', ' \u0314\u0342'])
        check('\u1ffe', ['\u1ffe', '\u1ffe', ' \u0314', ' \u0314'])
        check(' \u0314\u0342', ' \u0314\u0342')

        check('\u03d3', ['\u03d3', '\u03d2\u0301', '\u038e', '\u03a5\u0301'])
        check('\u03d2\u0301', ['\u03d3', '\u03d2\u0301', '\u038e', '\u03a5\u0301'])
        check('\u038e', ['\u038e', '\u03a5\u0301']*2)
        check('\u1feb', ['\u038e', '\u03a5\u0301']*2)
        check('\u03a5\u0301', ['\u038e', '\u03a5\u0301']*2)

        check('\u0626', ['\u0626', '\u064a\u0654']*2)
        check('\u064a\u0654', ['\u0626', '\u064a\u0654']*2)
        check('\ufe89', ['\ufe89', '\ufe89', '\u0626', '\u064a\u0654'])
        check('\ufe8a', ['\ufe8a', '\ufe8a', '\u0626', '\u064a\u0654'])
        check('\ufe8b', ['\ufe8b', '\ufe8b', '\u0626', '\u064a\u0654'])
        check('\ufe8c', ['\ufe8c', '\ufe8c', '\u0626', '\u064a\u0654'])

        check('\ufef9', ['\ufef9', '\ufef9', '\u0644\u0625', '\u0644\u0627\u0655'])
        check('\ufefa', ['\ufefa', '\ufefa', '\u0644\u0625', '\u0644\u0627\u0655'])
        check('\ufefb', ['\ufefb', '\ufefb', '\u0644\u0627', '\u0644\u0627'])
        check('\ufefc', ['\ufefc', '\ufefc', '\u0644\u0627', '\u0644\u0627'])
        check('\u0644\u0625', ['\u0644\u0625', '\u0644\u0627\u0655']*2)
        check('\u0644\u0627\u0655', ['\u0644\u0625', '\u0644\u0627\u0655']*2)
        check('\u0644\u0627', '\u0644\u0627')

        # Broken in 4.0.0
        check('\u327c', '\u327c' if self.old else
              ['\u327c', '\u327c', '\ucc38\uace0', '\u110e\u1161\u11b7\u1100\u1169'])
        check('\ucc38\uace0', ['\ucc38\uace0', '\u110e\u1161\u11b7\u1100\u1169']*2)
        check('\ucc38', ['\ucc38', '\u110e\u1161\u11b7']*2)
        check('\u110e\u1161\u11b7\u1100\u1169',
              ['\ucc38\uace0', '\u110e\u1161\u11b7\u1100\u1169']*2)
        check('\u110e\u1161\u11b7\u1100',
              ['\ucc38\u1100', '\u110e\u1161\u11b7\u1100']*2)
        check('\u110e\u1161\u11b7',
              ['\ucc38', '\u110e\u1161\u11b7']*2)
        check('\u110e\u1161',
              ['\ucc28', '\u110e\u1161']*2)
        check('\u110e', '\u110e')
        # Broken in 4.0.0-12.0.0
        check('\U00011938', '\U00011938' if self.old else
              ['\U00011938', '\U00011935\U00011930']*2)
        check('\U00011935\U00011930', ['\U00011938', '\U00011935\U00011930']*2)
        # New in 4.0.1
        check('\u321d', '\u321d' if self.old else
              ['\u321d', '\u321d', '(\uc624\uc804)', '(\u110b\u1169\u110c\u1165\u11ab)'])
        check('(\uc624\uc804)',
              ['(\uc624\uc804)', '(\u110b\u1169\u110c\u1165\u11ab)']*2)
        check('(\u110b\u1169\u110c\u1165\u11ab)',
              ['(\uc624\uc804)', '(\u110b\u1169\u110c\u1165\u11ab)']*2)
        check('\u4d57', '\u4d57')
        check('\u45d7', '\u45d7' if self.old else '\u45d7')
        check('\U0002f9bf', '\u4d57' if self.old else '\u45d7')
        # New in 4.1.0
        check('\u03a3', '\u03a3')
        check('\u03f9', '\u03f9' if self.old else
              ['\u03f9', '\u03f9', '\u03a3', '\u03a3'])
        # New in 5.0.0
        check('\u1b06', '\u1b06' if self.old else ['\u1b06', '\u1b05\u1b35']*2)
        # New in 5.2.0
        check('\U0001f213', '\U0001f213' if self.old else
                ['\U0001f213', '\U0001f213', '\u30c7', '\u30c6\u3099'])
        # New in 6.1.0
        check('\ufa2e', '\ufa2e' if self.old else '\u90de')
        # New in 13.0.0
        check('\U00011938', '\U00011938' if self.old else
                ['\U00011938', '\U00011935\U00011930', '\U00011938', '\U00011935\U00011930'])
        check('\U0001fbf9', '\U0001fbf9' if self.old else
                ['\U0001fbf9', '\U0001fbf9', '9', '9'])
        # New in 14.0.0
        check('\U000107ba', '\U000107ba' if self.old else
                ['\U000107ba', '\U000107ba', '\U0001df1e', '\U0001df1e'])
        # New in 15.0.0
        check('\U0001e06d', '\U0001e06d' if self.old else
                ['\U0001e06d', '\U0001e06d', '\u04b1', '\u04b1'])
        # New in 16.0.0
        check('\U0001ccd6', '\U0001ccd6' if self.old else
              ['\U0001ccd6', '\U0001ccd6', 'A', 'A'])

        self.assertRaises(TypeError, self.db.normalize)
        self.assertRaises(TypeError, self.db.normalize, 'NFC')
        self.assertRaises(ValueError, self.db.normalize, 'SPAM', 'A')

        self.assertRaises(TypeError, self.db.is_normalized)
        self.assertRaises(TypeError, self.db.is_normalized, 'NFC')
        self.assertRaises(ValueError, self.db.is_normalized, 'SPAM', 'A')

    def test_pr29(self):
        # https://www.unicode.org/review/pr-29.html
        # See issues #1054943 and #10254.
        composed = ("\u0b47\u0300\u0b3e", "\u1100\u0300\u1161",
                    'Li\u030dt-s\u1e73\u0301',
                    '\u092e\u093e\u0930\u094d\u0915 \u091c\u093c'
                    + '\u0941\u0915\u0947\u0930\u092c\u0930\u094d\u0917',
                    '\u0915\u093f\u0930\u094d\u0917\u093f\u091c\u093c'
                    + '\u0938\u094d\u0924\u093e\u0928')
        for text in composed:
            self.assertEqual(self.db.normalize('NFC', text), text)

    def test_issue10254(self):
        # Crash reported in #10254
        # New in 4.1.0
        a = 'C\u0338' * 20  + 'C\u0327'
        b = 'C\u0338' * 20  + '\xC7'
        self.assertEqual(self.db.normalize('NFC', a), b)

    def test_issue29456(self):
        # Fix #29456
        u1176_str_a = '\u1100\u1176\u11a8'
        u1176_str_b = '\u1100\u1176\u11a8'
        u11a7_str_a = '\u1100\u1175\u11a7'
        u11a7_str_b = '\uae30\u11a7'
        u11c3_str_a = '\u1100\u1175\u11c3'
        u11c3_str_b = '\uae30\u11c3'
        self.assertEqual(self.db.normalize('NFC', u1176_str_a), u1176_str_b)
        # New in 4.1.0
        self.assertEqual(self.db.normalize('NFC', u11a7_str_a), u11a7_str_b)
        self.assertEqual(self.db.normalize('NFC', u11c3_str_a), u11c3_str_b)

    def test_east_asian_width(self):
        eaw = self.db.east_asian_width
        self.assertRaises(TypeError, eaw, b'a')
        self.assertRaises(TypeError, eaw, bytearray())
        self.assertRaises(TypeError, eaw, '')
        self.assertRaises(TypeError, eaw, 'ra')
        self.assertEqual(eaw('\x1e'), 'N')
        self.assertEqual(eaw('\x20'), 'Na')
        self.assertEqual(eaw('\uC894'), 'W')
        self.assertEqual(eaw('\uFF66'), 'H')
        self.assertEqual(eaw('\uFF1F'), 'F')
        self.assertEqual(eaw('\u2010'), 'A')
        self.assertEqual(eaw('\U00020000'), 'W')
        # New in 4.1.0
        self.assertEqual(eaw('\u0350'), 'N' if self.old else 'A')
        self.assertEqual(eaw('\U000e01ef'), 'N' if self.old else 'A')
        # New in 5.2.0
        self.assertEqual(eaw('\u115a'), 'N' if self.old else 'W')
        # New in 9.0.0
        self.assertEqual(eaw('\u231a'), 'N' if self.old else 'W')
        self.assertEqual(eaw('\u2614'), 'N' if self.old else 'W')
        self.assertEqual(eaw('\U0001f19a'), 'N' if self.old else 'W')
        self.assertEqual(eaw('\U0001f991'), 'N' if self.old else 'W')
        self.assertEqual(eaw('\U0001f9c0'), 'N' if self.old else 'W')
        # New in 12.0.0
        self.assertEqual(eaw('\u32ff'), 'N' if self.old else 'W')
        self.assertEqual(eaw('\U0001fa95'), 'N' if self.old else 'W')
        # New in 13.0.0
        self.assertEqual(eaw('\u31bb'), 'N' if self.old else 'W')
        self.assertEqual(eaw('\U0003134a'), 'N' if self.old else 'W')
        # New in 14.0.0
        self.assertEqual(eaw('\u9ffd'), 'N' if self.old else 'W')
        self.assertEqual(eaw('\U0002b738'), 'N' if self.old else 'W')
        # New in 15.0.0
        self.assertEqual(eaw('\U000323af'), 'N' if self.old else 'W')
        # New in 16.0.0
        self.assertEqual(eaw('\u2630'), 'N' if self.old else 'W')
        self.assertEqual(eaw('\U0001FAE9'), 'N' if self.old else 'W')

        # unicodedataplus tests
        self.assertEqual(eaw('\U0002B737'), 'W')
        self.assertEqual(eaw('\U00031414'), 'W')
        self.assertEqual(eaw('\U0002ECCA'), 'W')
        self.assertEqual(eaw('\U00018CFF'), 'W')

    def test_east_asian_width_unassigned(self):
        eaw = self.db.east_asian_width
        # unassigned
        for char in '\u0530\u0ecf\u10c6\u20fc\uaaca\U000107bd\U000115f2':
            self.assertEqual(eaw(char), 'N')
            self.assertIs(self.db.name(char, None), None)

        # unassigned but reserved for CJK
        for char in ('\U0002A6E0\U0002FA20\U0003134B\U0003FFFD'
                     '\uFA6E\uFADA'): # New in 5.2.0
            self.assertEqual(eaw(char), 'W')
            self.assertIs(self.db.name(char, None), None)

        # private use areas
        for char in '\uE000\uF800\U000F0000\U000FFFEE\U00100000\U0010FFF0':
            self.assertEqual(eaw(char), 'A')
            self.assertIs(self.db.name(char, None), None)

    def test_east_asian_width_9_0_changes(self):
        self.assertEqual(self.db.ucd_3_2_0.east_asian_width('\u231a'), 'N')
        self.assertEqual(self.db.east_asian_width('\u231a'), 'W')

    def test_script(self):
        self.assertEqual(self.db.script('P'), 'Latin')
        self.assertEqual(self.db.script('\u0628'), 'Arabic')
        self.assertEqual(self.db.script('\U00011013'), 'Brahmi')
        self.assertEqual(self.db.script('\U00010583'), 'Vithkuqi')
        self.assertEqual(self.db.script('\U0001E4E0'), 'Nag_Mundari')
        self.assertEqual(self.db.script('\U00016D5A'), 'Kirat_Rai')
        self.assertEqual(self.db.script('\U0002EB01'), 'Han')
        self.assertEqual(self.db.script('\u1AFF'), 'Unknown')

    def test_block(self):
        self.assertEqual(self.db.block('P'), 'Basic Latin')
        self.assertEqual(self.db.block('\u03E2'), 'Greek and Coptic')
        self.assertEqual(self.db.block('\U00010107'), 'Aegean Numbers')
        self.assertEqual(self.db.block('\U00010D77'), 'Garay')
        self.assertEqual(self.db.block('\U00012FE4'), 'Cypro-Minoan')
        self.assertEqual(self.db.block('\U0001D2C2'), 'Kaktovik Numerals')
        self.assertEqual(self.db.block('\U0002ED32'), 'CJK Unified Ideographs Extension I')
        self.assertEqual(self.db.block('\u1AFF'), 'No_Block')

    def test_script_extensions(self):
        self.assertEqual(self.db.script_extensions('P'), ['Latn'])
        self.assertEqual(self.db.script_extensions('\u0640'), ['Adlm', 'Arab', 'Mand', 'Mani', 'Ougr', 'Phlp', 'Rohg', 'Sogd', 'Syrc'])
        self.assertEqual(self.db.script_extensions('\u1AFF'), ['Zzzz'])
        self.assertEqual(self.db.script_extensions('\u31EF'), ['Hani', 'Tang'])
        self.assertEqual(self.db.script_extensions('\U0001E290'), ['Toto'])
        self.assertEqual(self.db.script_extensions('\U0002EE11'), ['Hani'])

    def test_indic_conjunct_break(self):
        self.assertEqual(self.db.indic_conjunct_break('P'), 'None')
        self.assertEqual(self.db.indic_conjunct_break('\u0B4D'), 'Linker')
        self.assertEqual(self.db.indic_conjunct_break('\u0AB7'), 'Consonant')
        self.assertEqual(self.db.indic_conjunct_break('\u089C'), 'Extend')
        self.assertEqual(self.db.indic_conjunct_break('\U000113C5'), 'Extend')

    def test_indic_positional(self):
        self.assertEqual(self.db.indic_positional_category('P'), 'NA')
        self.assertEqual(self.db.indic_positional_category('\u0EC3'), 'Visual_Order_Left')
        self.assertEqual(self.db.indic_positional_category('\u1734'), 'Right')
        self.assertEqual(self.db.indic_positional_category('\U00011C39'), 'Top')
        self.assertEqual(self.db.indic_positional_category('\u1AFF'), 'NA')
        self.assertEqual(self.db.indic_positional_category('\U00076EFA'), 'NA')
        self.assertEqual(self.db.indic_positional_category('\U00011F03'), 'Right')
        self.assertEqual(self.db.indic_positional_category('\U0001612E'), 'Bottom')

    def test_indic_syllabic(self):
        self.assertEqual(self.db.indic_syllabic_category('P'), 'Other')
        self.assertEqual(self.db.indic_syllabic_category('\u0EC3'), 'Vowel_Dependent')
        self.assertEqual(self.db.indic_syllabic_category('\uA982'), 'Consonant_Final')
        self.assertEqual(self.db.indic_syllabic_category('\U00011839'), 'Virama')
        self.assertEqual(self.db.indic_syllabic_category('\u1AFF'), 'Other')
        self.assertEqual(self.db.indic_syllabic_category('\U00076EFA'), 'Other')
        self.assertEqual(self.db.indic_syllabic_category('\U00011241'), 'Vowel_Dependent')
        self.assertEqual(self.db.indic_syllabic_category('\U000113CE'), 'Pure_Killer')

    def test_grapheme_cluster_break(self):
        self.assertEqual(self.db.grapheme_cluster_break('\U000110CD'), 'Prepend')
        self.assertEqual(self.db.grapheme_cluster_break('\u000D'), 'CR')
        self.assertEqual(self.db.grapheme_cluster_break('\u000A'), 'LF')
        self.assertEqual(self.db.grapheme_cluster_break('\u200B'), 'Control')
        self.assertEqual(self.db.grapheme_cluster_break('\u09BE'), 'Extend')
        self.assertEqual(self.db.grapheme_cluster_break('\U0001F1F0'), 'Regional_Indicator')
        self.assertEqual(self.db.grapheme_cluster_break('\U00011445'), 'SpacingMark')
        self.assertEqual(self.db.grapheme_cluster_break('\U00011720'), 'Other')
        self.assertEqual(self.db.grapheme_cluster_break('\u115A'), 'L')
        self.assertEqual(self.db.grapheme_cluster_break('\u11FA'), 'T')
        self.assertEqual(self.db.grapheme_cluster_break('\uB300'), 'LV')
        self.assertEqual(self.db.grapheme_cluster_break('\u200D'), 'ZWJ')
        self.assertEqual(self.db.grapheme_cluster_break('\U00013440'), 'Extend')
        self.assertEqual(self.db.grapheme_cluster_break('\U00016D69'), 'V')

    def test_word_break(self):
        self.assertEqual(self.db.word_break('\u0041'), 'ALetter')
        self.assertEqual(self.db.word_break('\U000145AD'), 'ALetter')
        self.assertEqual(self.db.word_break('\u000D'), 'CR')
        self.assertEqual(self.db.word_break('\u0022'), 'Double_Quote')
        self.assertEqual(self.db.word_break('\u032C'), 'Extend')
        self.assertEqual(self.db.word_break('\U00011C3C'), 'Extend')
        self.assertEqual(self.db.word_break('\u005F'), 'ExtendNumLet')
        self.assertEqual(self.db.word_break('\u200E'), 'Format')
        self.assertEqual(self.db.word_break('\U00013432'), 'Format')
        self.assertEqual(self.db.word_break('\u30AB'), 'Katakana')
        self.assertEqual(self.db.word_break('\U0001B121'), 'Katakana')
        self.assertEqual(self.db.word_break('\u05D0'), 'Hebrew_Letter')
        self.assertEqual(self.db.word_break('\u000A'), 'LF')
        self.assertEqual(self.db.word_break('\u003A'), 'MidLetter')
        self.assertEqual(self.db.word_break('\u07F8'), 'MidNum')
        self.assertEqual(self.db.word_break('\uFE52'), 'MidNumLet')
        self.assertEqual(self.db.word_break('\u000B'), 'Newline')
        self.assertEqual(self.db.word_break('\u0660'), 'Numeric')
        self.assertEqual(self.db.word_break('\u2A54'), 'Other')
        self.assertEqual(self.db.word_break('\U0001F4CB'), 'Other')
        self.assertEqual(self.db.word_break('\uA95E'), 'Other')
        self.assertEqual(self.db.word_break('\U0001F1EF'), 'Regional_Indicator')
        self.assertEqual(self.db.word_break('\u0027'), 'Single_Quote')
        self.assertEqual(self.db.word_break('\u2008'), 'WSegSpace')
        self.assertEqual(self.db.word_break('\u200D'), 'ZWJ')

    def test_sentence_break(self):
        self.assertEqual(self.db.sentence_break('\u002E'), 'ATerm')
        self.assertEqual(self.db.sentence_break('\u232A'), 'Close')
        self.assertEqual(self.db.sentence_break('\U0001F676'), 'Close')
        self.assertEqual(self.db.sentence_break('\u000D'), 'CR')
        self.assertEqual(self.db.sentence_break('\u0310'), 'Extend')
        self.assertEqual(self.db.sentence_break('\U000112DF'), 'Extend')
        self.assertEqual(self.db.sentence_break('\u00AD'), 'Format')
        self.assertEqual(self.db.sentence_break('\U00013436'), 'Format')
        self.assertEqual(self.db.sentence_break('\u000A'), 'LF')
        self.assertEqual(self.db.sentence_break('\u014B'), 'Lower')
        self.assertEqual(self.db.sentence_break('\U0001DF19'), 'Lower')
        self.assertEqual(self.db.sentence_break('\u0664'), 'Numeric')
        self.assertEqual(self.db.sentence_break('\U00011F57'), 'Numeric')
        self.assertEqual(self.db.sentence_break('\u01C0'), 'OLetter')
        self.assertEqual(self.db.sentence_break('\U00018B10'), 'OLetter')
        self.assertEqual(self.db.sentence_break('\u0A0E'), 'Other')
        self.assertEqual(self.db.sentence_break('\U0001F775'), 'Other')
        self.assertEqual(self.db.sentence_break('\u002C'), 'SContinue')
        self.assertEqual(self.db.sentence_break('\u2028'), 'Sep')
        self.assertEqual(self.db.sentence_break('\u00A0'), 'Sp')
        self.assertEqual(self.db.sentence_break('\u0964'), 'STerm')
        self.assertEqual(self.db.sentence_break('\U0001144B'), 'STerm')
        self.assertEqual(self.db.sentence_break('\u0410'), 'Upper')
        self.assertEqual(self.db.sentence_break('\U00016E43'), 'Upper')

    def test_line_break(self):
        self.assertEqual(self.db.line_break('\uA994'), 'AK')
        self.assertEqual(self.db.line_break('\U00011F04'), 'AK')
        self.assertEqual(self.db.line_break('\U00011003'), 'AP')
        self.assertEqual(self.db.line_break('\u1BC0'), 'AS')
        self.assertEqual(self.db.line_break('\U00011350'), 'AS')
        self.assertEqual(self.db.line_break('\u0041'), 'AL')
        self.assertEqual(self.db.line_break('\U0001D418'), 'AL')
        self.assertEqual(self.db.line_break('\u00B6'), 'AI')
        self.assertEqual(self.db.line_break('\U0001F173'), 'AI')
        self.assertEqual(self.db.line_break('\u30E7'), 'CJ')
        self.assertEqual(self.db.line_break('\U0001B132'), 'CJ')
        self.assertEqual(self.db.line_break('\uA015'), 'NS')
        self.assertEqual(self.db.line_break('\U00016FE0'), 'NS')
        self.assertEqual(self.db.line_break('\u275B'), 'QU')
        self.assertEqual(self.db.line_break('\U0001F676'), 'QU')
        self.assertEqual(self.db.line_break('\u0530'), 'XX')
        self.assertEqual(self.db.line_break('\U000E0080'), 'XX')

    def test_vertical_orientation(self):
        self.assertEqual(self.db.vertical_orientation('\u0040'), 'R')
        self.assertEqual(self.db.vertical_orientation('\u00A9'), 'U')
        self.assertEqual(self.db.vertical_orientation('\u2329'), 'Tr')
        self.assertEqual(self.db.vertical_orientation('\u3083'), 'Tu')
        self.assertEqual(self.db.vertical_orientation('\U000143F1'), 'U')
        self.assertEqual(self.db.vertical_orientation('\U0001B000'), 'U')
        self.assertEqual(self.db.vertical_orientation('\U0001E040'), 'R')
        self.assertEqual(self.db.vertical_orientation('\U0001F200'), 'Tu')

    def test_age(self):
        self.assertEqual(self.db.age('\u03DA'), '1.1')
        self.assertEqual(self.db.age('\u20AB'), '2.0')
        self.assertEqual(self.db.age('\u20AC'), '2.1')
        self.assertEqual(self.db.age('\u058A'), '3.0')
        self.assertEqual(self.db.age('\U00010423'), '3.1')
        self.assertEqual(self.db.age('\u07B1'), '3.2')
        self.assertEqual(self.db.age('\U00010083'), '4.0')
        self.assertEqual(self.db.age('\u131F'), '4.1')
        self.assertEqual(self.db.age('\U0001D363'), '5.0')
        self.assertEqual(self.db.age('\uA95F'), '5.1')
        self.assertEqual(self.db.age('\u0C34'), '7.0')
        self.assertEqual(self.db.age('\U0001F6F8'), '10.0')
        self.assertEqual(self.db.age('\u0EAC'), '12.0')
        self.assertEqual(self.db.age('\U0002A6D9'), '13.0')
        self.assertEqual(self.db.age('\u170D'), '14.0')
        self.assertEqual(self.db.age('\U0002EBF9'), '15.1')
        self.assertEqual(self.db.age('\U0001CC52'), '16.0')

    def test_total_strokes(self):
        self.assertEqual(self.db.total_strokes('P'), 0)
        self.assertEqual(self.db.total_strokes('\u694A'), 13)
        self.assertEqual(self.db.total_strokes('\u694A', source='G'), 13)
        self.assertEqual(self.db.total_strokes('\u8303', source='G'), 9)
        self.assertEqual(self.db.total_strokes('\u8303', source='T'), 9)
        self.assertRaises(ValueError, self.db.total_strokes, '\u8303', source='U')
        self.assertEqual(self.db.total_strokes('\U0002003E'), 10)
        self.assertEqual(self.db.total_strokes('\U0002B736'), 16)
        self.assertEqual(self.db.total_strokes('\U0003137B'), 6)
        self.assertEqual(self.db.total_strokes('\U0002ED6B'), 8)

    def test_emoji(self):
        self.assertEqual(self.db.is_emoji('\u00A9'), True)
        self.assertEqual(self.db.is_emoji('\U0001F9C1'), True)
        self.assertEqual(self.db.is_emoji('\u2188'), False)
        self.assertEqual(self.db.is_emoji('\U0001F4FE'), False)
        self.assertEqual(self.db.is_emoji('\U0001FAAF'), True)
        self.assertEqual(self.db.is_emoji('\U0001FADC'), True)
        self.assertEqual(self.db.is_emoji_presentation('\u2795'), True)
        self.assertEqual(self.db.is_emoji_presentation('\U0001F32F'), True)
        self.assertEqual(self.db.is_emoji_presentation('\u00A9'), False)
        self.assertEqual(self.db.is_emoji_presentation('\U0001219A'), False)
        self.assertEqual(self.db.is_emoji_presentation('\U0001FACE'), True)
        self.assertEqual(self.db.is_emoji_presentation('\U0001FAE9'), True)
        self.assertEqual(self.db.is_emoji_modifier('\U0001F3FC'), True)
        self.assertEqual(self.db.is_emoji_modifier('Q'), False)
        self.assertEqual(self.db.is_emoji_modifier_base('\U0001F47C'), True)
        self.assertEqual(self.db.is_emoji_modifier_base('\u3312'), False)
        self.assertEqual(self.db.is_emoji_modifier_base('\U0001FAF7'), True)
        self.assertEqual(self.db.is_emoji_component('\u0039'), True)
        self.assertEqual(self.db.is_emoji_component('\u200D'), True)
        self.assertEqual(self.db.is_emoji_component('\U000E0021'), True)
        self.assertEqual(self.db.is_emoji_component('k'), False)
        self.assertEqual(self.db.is_emoji_component('\U00012122'), False)
        self.assertEqual(self.db.is_extended_pictographic('\U0001FA80'), True)
        self.assertEqual(self.db.is_extended_pictographic('\u03E2'), False)
        self.assertEqual(self.db.is_extended_pictographic('\U0001FADA'), True)
        self.assertEqual(self.db.is_extended_pictographic('\U0001F8B4'), False)

class UnicodeMiscTest(unittest.TestCase):
    db = unicodedata


    def test_decimal_numeric_consistent(self):
        # Test that decimal and numeric are consistent,
        # i.e. if a character has a decimal value,
        # its numeric value should be the same.
        count = 0
        for c in iterallchars():
            dec = self.db.decimal(c, -1)
            if dec != -1:
                self.assertEqual(dec, self.db.numeric(c))
                count += 1
        self.assertTrue(count >= 10, count) # should have tested at least the ASCII digits

    def test_digit_numeric_consistent(self):
        # Test that digit and numeric are consistent,
        # i.e. if a character has a digit value,
        # its numeric value should be the same.
        count = 0
        for c in iterallchars():
            dec = self.db.digit(c, -1)
            if dec != -1:
                self.assertEqual(dec, self.db.numeric(c))
                count += 1
        self.assertTrue(count >= 10, count) # should have tested at least the ASCII digits

    def test_normalize_consistent(self):
        allchars = list(iterallchars())
        for form in ('NFC', 'NFD', 'NFKC', 'NFKD'):
            for c in allchars:
                norm = self.db.normalize(form, c)
                self.assertEqual(self.db.is_normalized(form, c), norm == c)
                if norm != c:
                    self.assertEqual(self.db.normalize(form, norm), norm)
                    self.assertTrue(self.db.is_normalized(form, norm))

    def test_bug_1704793(self):
        self.assertEqual(self.db.lookup("GOTHIC LETTER FAIHU"), '\U00010346')

    def test_ucd_510(self):
        import unicodedataplus as unicodedata
        # In UCD 5.1.0, a mirrored property changed wrt. UCD 3.2.0
        self.assertTrue(unicodedata.mirrored("\u0f3a"))
        self.assertTrue(not unicodedata.ucd_3_2_0.mirrored("\u0f3a"))
        # Also, we now have two ways of representing
        # the upper-case mapping: as delta, or as absolute value
        self.assertTrue("a".upper()=='A')
        self.assertTrue("\u1d79".upper()=='\ua77d')
        self.assertTrue(".".upper()=='.')

    def test_bug_5828(self):
        self.assertEqual("\u1d79".lower(), "\u1d79")
        # Only U+0000 should have U+0000 as its upper/lower/titlecase variant
        self.assertEqual(
            [
                c for c in iterallchars()
                if "\x00" in (c.lower(), c.upper(), c.title())
            ],
            ["\x00"]
        )

    def test_bug_4971(self):
        # LETTER DZ WITH CARON: DZ, Dz, dz
        self.assertEqual("\u01c4".title(), "\u01c5")
        self.assertEqual("\u01c5".title(), "\u01c5")
        self.assertEqual("\u01c6".title(), "\u01c5")

    def test_linebreak_7643(self):
        for c in iterallchars():
            lines = (c + 'A').splitlines()
            if c in ('\x0a', '\x0b', '\x0c', '\x0d', '\x85',
                     '\x1c', '\x1d', '\x1e', '\u2028', '\u2029'):
                self.assertEqual(len(lines), 2,
                                 r"%a should be a linebreak" % c)
            else:
                self.assertEqual(len(lines), 1,
                                 r"%a should not be a linebreak" % c)


class NormalizationTest(unittest.TestCase):
    @staticmethod
    def check_version(testfile):
        hdr = testfile.readline()
        return unicodedata.unidata_version in hdr

    @staticmethod
    def unistr(data):
        data = [int(x, 16) for x in data.split(" ")]
        return "".join([chr(x) for x in data])

    # @requires_resource('network')
    # def test_normalization(self):
        # TESTDATAFILE = "NormalizationTest.txt"
        # TESTDATAURL = f"http://www.pythontest.net/unicode/{unicodedata.unidata_version}/{TESTDATAFILE}"
# 
        # # Hit the exception early
        # try:
            # testdata = open_urlresource(TESTDATAURL, encoding="utf-8",
                                        # check=self.check_version)
        # except PermissionError:
            # self.skipTest(f"Permission error when downloading {TESTDATAURL} "
                          # f"into the test data directory")
        # except (OSError, HTTPException):
            # self.fail(f"Could not retrieve {TESTDATAURL}")
# 
        # with testdata:
            # self.run_normalization_tests(testdata)

    def run_normalization_tests(self, testdata, ucd):
        part = None
        part1_data = set()

        NFC = partial(ucd.normalize, "NFC")
        NFKC = partial(ucd.normalize, "NFKC")
        NFD = partial(ucd.normalize, "NFD")
        NFKD = partial(ucd.normalize, "NFKD")
        is_normalized = ucd.is_normalized

        for line in testdata:
            if '#' in line:
                line = line.split('#')[0]
            line = line.strip()
            if not line:
                continue
            if line.startswith("@Part"):
                part = line.split()[0]
                continue
            c1,c2,c3,c4,c5 = [self.unistr(x) for x in line.split(';')[:-1]]

            # Perform tests
            self.assertTrue(c2 ==  NFC(c1) ==  NFC(c2) ==  NFC(c3), line)
            self.assertTrue(c4 ==  NFC(c4) ==  NFC(c5), line)
            self.assertTrue(c3 ==  NFD(c1) ==  NFD(c2) ==  NFD(c3), line)
            self.assertTrue(c5 ==  NFD(c4) ==  NFD(c5), line)
            self.assertTrue(c4 == NFKC(c1) == NFKC(c2) == \
                            NFKC(c3) == NFKC(c4) == NFKC(c5),
                            line)
            self.assertTrue(c5 == NFKD(c1) == NFKD(c2) == \
                            NFKD(c3) == NFKD(c4) == NFKD(c5),
                            line)

            self.assertTrue(is_normalized("NFC", c2))
            self.assertTrue(is_normalized("NFC", c4))

            self.assertTrue(is_normalized("NFD", c3))
            self.assertTrue(is_normalized("NFD", c5))

            self.assertTrue(is_normalized("NFKC", c4))
            self.assertTrue(is_normalized("NFKD", c5))

            # Record part 1 data
            if part == "@Part1":
                part1_data.add(c1)

        # Perform tests for all other data
        for X in iterallchars():
            if X in part1_data:
                continue
            self.assertTrue(X == NFC(X) == NFD(X) == NFKC(X) == NFKD(X), ord(X))

    def test_edge_cases(self):
        self.assertRaises(TypeError, unicodedata.normalize)
        self.assertRaises(ValueError, unicodedata.normalize, 'unknown', 'xx')
        self.assertEqual(unicodedata.normalize('NFKC', ''), '')

    def test_bug_834676(self):
        # Check for bug 834676
        unicodedata.normalize('NFC', '\ud55c\uae00')

    def test_normalize_return_type(self):
        # gh-129569: normalize() return type must always be str
        normalize = unicodedata.normalize

        class MyStr(str):
            pass

        normalization_forms = ("NFC", "NFKC", "NFD", "NFKD")
        input_strings = (
            # normalized strings
            "",
            "ascii",
            # unnormalized strings
            "\u1e0b\u0323",
            "\u0071\u0307\u0323",
        )

        for form in normalization_forms:
            for input_str in input_strings:
                with self.subTest(form=form, input_str=input_str):
                    self.assertIs(type(normalize(form, input_str)), str)
                    self.assertIs(type(normalize(form, MyStr(input_str))), str)


if __name__ == "__main__":
    unittest.main()

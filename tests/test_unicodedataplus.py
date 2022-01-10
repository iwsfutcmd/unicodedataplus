""" Tests for the unicodedataplus module.

    Written by Marc-Andre Lemburg (mal@lemburg.com).

    (c) Copyright CNRI, All Rights Reserved. NO WARRANTY.

"""

import hashlib
from http.client import HTTPException
import sys
import unicodedataplus as unicodedata
import unittest
from os import makedirs
# from test.support import open_urlresource, requires_resource, script_helper
# import test.support
# test.support.TEST_DATA_DIR = "tests/data"
# makedirs(test.support.TEST_DATA_DIR, exist_ok=True)

# class UnicodeMethodsTest(unittest.TestCase):

#     # update this, if the database changes
#     expectedchecksum = 'fbdf8106a3c7c242086b0a9efa03ad4d30d5b85d'

#     @requires_resource('cpu')
#     def test_method_checksum(self):
#         h = hashlib.sha1()
#         for i in range(sys.maxunicode + 1):
#             char = chr(i)
#             data = [
#                 # Predicates (single char)
#                 "01"[char.isalnum()],
#                 "01"[char.isalpha()],
#                 "01"[char.isdecimal()],
#                 "01"[char.isdigit()],
#                 "01"[char.islower()],
#                 "01"[char.isnumeric()],
#                 "01"[char.isspace()],
#                 "01"[char.istitle()],
#                 "01"[char.isupper()],

#                 # Predicates (multiple chars)
#                 "01"[(char + 'abc').isalnum()],
#                 "01"[(char + 'abc').isalpha()],
#                 "01"[(char + '123').isdecimal()],
#                 "01"[(char + '123').isdigit()],
#                 "01"[(char + 'abc').islower()],
#                 "01"[(char + '123').isnumeric()],
#                 "01"[(char + ' \t').isspace()],
#                 "01"[(char + 'abc').istitle()],
#                 "01"[(char + 'ABC').isupper()],

#                 # Mappings (single char)
#                 char.lower(),
#                 char.upper(),
#                 char.title(),

#                 # Mappings (multiple chars)
#                 (char + 'abc').lower(),
#                 (char + 'ABC').upper(),
#                 (char + 'abc').title(),
#                 (char + 'ABC').title(),

#                 ]
#             h.update(''.join(data).encode('utf-8', 'surrogatepass'))
#         result = h.hexdigest()
#         self.assertEqual(result, self.expectedchecksum)

class UnicodeDatabaseTest(unittest.TestCase):
    db = unicodedata

class UnicodeFunctionsTest(UnicodeDatabaseTest):

    # Update this if the database changes. Make sure to do a full rebuild
    # (e.g. 'make distclean && make') to get the correct checksum.
    expectedchecksum = '98d602e1f69d5c5bb8a5910c40bbbad4e18e8370'
    
    # @requires_resource('cpu')
    def test_function_checksum(self):
        data = []
        h = hashlib.sha1()

        for i in range(sys.maxunicode + 1):
            char = chr(i)
            data = [
                # Properties
                format(self.db.digit(char, -1), '.12g'),
                format(self.db.numeric(char, -1), '.12g'),
                format(self.db.decimal(char, -1), '.12g'),
                self.db.category(char),
                self.db.bidirectional(char),
                self.db.decomposition(char),
                str(self.db.mirrored(char)),
                str(self.db.combining(char)),
            ]
            h.update(''.join(data).encode("ascii"))
        result = h.hexdigest()
        self.assertEqual(result, self.expectedchecksum)

    def test_digit(self):
        self.assertEqual(self.db.digit('A', None), None)
        self.assertEqual(self.db.digit('9'), 9)
        self.assertEqual(self.db.digit('\u215b', None), None)
        self.assertEqual(self.db.digit('\u2468'), 9)
        self.assertEqual(self.db.digit('\U00020000', None), None)
        self.assertEqual(self.db.digit('\U00016AC3'), 3)
        self.assertEqual(self.db.digit('\U0001D7FD'), 7)

        self.assertRaises(TypeError, self.db.digit)
        self.assertRaises(TypeError, self.db.digit, 'xx')
        self.assertRaises(ValueError, self.db.digit, 'x')

    def test_numeric(self):
        self.assertEqual(self.db.numeric('A',None), None)
        self.assertEqual(self.db.numeric('9'), 9)
        self.assertEqual(self.db.numeric('\u215b'), 0.125)
        self.assertEqual(self.db.numeric('\u2468'), 9.0)
        self.assertEqual(self.db.numeric('\ua627'), 7.0)
        self.assertEqual(self.db.numeric('\U00020000', None), None)
        self.assertEqual(self.db.numeric('\U0001012A'), 9000)

        self.assertRaises(TypeError, self.db.numeric)
        self.assertRaises(TypeError, self.db.numeric, 'xx')
        self.assertRaises(ValueError, self.db.numeric, 'x')

    def test_decimal(self):
        self.assertEqual(self.db.decimal('A',None), None)
        self.assertEqual(self.db.decimal('9'), 9)
        self.assertEqual(self.db.decimal('\u215b', None), None)
        self.assertEqual(self.db.decimal('\u2468', None), None)
        self.assertEqual(self.db.decimal('\U00020000', None), None)
        self.assertEqual(self.db.decimal('\U00016AC3'), 3)
        self.assertEqual(self.db.decimal('\U0001D7FD'), 7)

        self.assertRaises(TypeError, self.db.decimal)
        self.assertRaises(TypeError, self.db.decimal, 'xx')
        self.assertRaises(ValueError, self.db.decimal, 'x')

    def test_category(self):
        self.assertEqual(self.db.category('\uFFFE'), 'Cn')
        self.assertEqual(self.db.category('a'), 'Ll')
        self.assertEqual(self.db.category('A'), 'Lu')
        self.assertEqual(self.db.category('\U00020000'), 'Lo')
        self.assertEqual(self.db.category('\U0001012A'), 'No')
        self.assertEqual(self.db.category('\U000110C2'), 'Mn')

        self.assertRaises(TypeError, self.db.category)
        self.assertRaises(TypeError, self.db.category, 'xx')

    def test_bidirectional(self):
        self.assertEqual(self.db.bidirectional('\uFFFE'), '')
        self.assertEqual(self.db.bidirectional(' '), 'WS')
        self.assertEqual(self.db.bidirectional('A'), 'L')
        self.assertEqual(self.db.bidirectional('\u0876'), 'AL')
        self.assertEqual(self.db.bidirectional('\U00020000'), 'L')

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

        self.assertRaises(TypeError, self.db.mirrored)
        self.assertRaises(TypeError, self.db.mirrored, 'xx')

    def test_combining(self):
        self.assertEqual(self.db.combining('\uFFFE'), 0)
        self.assertEqual(self.db.combining('a'), 0)
        self.assertEqual(self.db.combining('\u20e1'), 230)
        self.assertEqual(self.db.combining('\U00020000'), 0)

        self.assertRaises(TypeError, self.db.combining)
        self.assertRaises(TypeError, self.db.combining, 'xx')

    def test_normalize(self):
        self.assertRaises(TypeError, self.db.normalize)
        self.assertRaises(ValueError, self.db.normalize, 'unknown', 'xx')
        self.assertEqual(self.db.normalize('NFKC', ''), '')
        # The rest can be found in test_normalization.py
        # which requires an external file.

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
        self.assertEqual(eaw('\U0002B737'), 'W')

    def test_east_asian_width_9_0_changes(self):
        self.assertEqual(self.db.ucd_3_2_0.east_asian_width('\u231a'), 'N')
        self.assertEqual(self.db.east_asian_width('\u231a'), 'W')

    def test_script(self):
        self.assertEqual(self.db.script('P'), 'Latin')
        self.assertEqual(self.db.script('\u0628'), 'Arabic')
        self.assertEqual(self.db.script('\U00011013'), 'Brahmi')
        self.assertEqual(self.db.script('\U00010583'), 'Vithkuqi')
        self.assertEqual(self.db.script('\u1AFF'), 'Unknown')

    def test_block(self):
        self.assertEqual(self.db.block('P'), 'Basic Latin')
        self.assertEqual(self.db.block('\u03E2'), 'Greek and Coptic')
        self.assertEqual(self.db.block('\U00010107'), 'Aegean Numbers')
        self.assertEqual(self.db.block('\U00012FE4'), 'Cypro-Minoan')
        self.assertEqual(self.db.block('\u1AFF'), 'No_Block')

    def test_script_extensions(self):
        self.assertEqual(self.db.script_extensions('P'), ['Latn'])
        self.assertEqual(self.db.script_extensions('\u0640'), ['Adlm', 'Arab', 'Mand', 'Mani', 'Ougr', 'Phlp', 'Rohg', 'Sogd', 'Syrc'])
        self.assertEqual(self.db.script_extensions('\u1AFF'), ['Zzzz'])
        self.assertEqual(self.db.script_extensions('\U0001E290'), ['Toto'])

    def test_indic_positional(self):
        self.assertEqual(self.db.indic_positional_category('P'), 'NA')
        self.assertEqual(self.db.indic_positional_category('\u0EC3'), 'Visual_Order_Left')
        self.assertEqual(self.db.indic_positional_category('\u1734'), 'Right')
        self.assertEqual(self.db.indic_positional_category('\U00011C39'), 'Top')
        self.assertEqual(self.db.indic_positional_category('\u1AFF'), 'NA')
        self.assertEqual(self.db.indic_positional_category('\U00076EFA'), 'NA')

    def test_indic_syllabic(self):
        self.assertEqual(self.db.indic_syllabic_category('P'), 'Other')
        self.assertEqual(self.db.indic_syllabic_category('\u0EC3'), 'Vowel_Dependent')
        self.assertEqual(self.db.indic_syllabic_category('\uA982'), 'Consonant_Final')
        self.assertEqual(self.db.indic_syllabic_category('\U00011839'), 'Virama')
        self.assertEqual(self.db.indic_syllabic_category('\u1AFF'), 'Other')
        self.assertEqual(self.db.indic_syllabic_category('\U00076EFA'), 'Other')

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

    def test_total_strokes(self):
        self.assertEqual(self.db.total_strokes('P'), 0)
        self.assertEqual(self.db.total_strokes('\u694A'), 13)
        self.assertEqual(self.db.total_strokes('\U0002003E'), 10)
        self.assertEqual(self.db.total_strokes('\U0002B736'), 16)

    def test_emoji(self):
        self.assertEqual(self.db.is_emoji('\u00A9'), True)
        self.assertEqual(self.db.is_emoji('\U0001F9C1'), True)
        self.assertEqual(self.db.is_emoji('\u2188'), False)
        self.assertEqual(self.db.is_emoji('\U0001F4FE'), False)
        self.assertEqual(self.db.is_emoji_presentation('\u2795'), True)
        self.assertEqual(self.db.is_emoji_presentation('\U0001F32F'), True)
        self.assertEqual(self.db.is_emoji_presentation('\u00A9'), False)
        self.assertEqual(self.db.is_emoji_presentation('\U0001219A'), False)
        self.assertEqual(self.db.is_emoji_modifier('\U0001F3FC'), True)
        self.assertEqual(self.db.is_emoji_modifier('Q'), False)
        self.assertEqual(self.db.is_emoji_modifier_base('\U0001F47C'), True)
        self.assertEqual(self.db.is_emoji_modifier_base('\u3312'), False)
        self.assertEqual(self.db.is_emoji_component('\u0039'), True)
        self.assertEqual(self.db.is_emoji_component('\u200D'), True)
        self.assertEqual(self.db.is_emoji_component('\U000E0021'), True)
        self.assertEqual(self.db.is_emoji_component('k'), False)
        self.assertEqual(self.db.is_emoji_component('\U00012122'), False)
        self.assertEqual(self.db.is_extended_pictographic('\U0001FA80'), True)
        self.assertEqual(self.db.is_extended_pictographic('\u03E2'), False)

class UnicodeMiscTest(UnicodeDatabaseTest):

    # def test_failed_import_during_compiling(self):
        # # Issue 4367
        # # Decoding \N escapes requires the unicodedata module. If it can't be
        # # imported, we shouldn't segfault.
# 
        # # This program should raise a SyntaxError in the eval.
        # code = "import sys;" \
            # "sys.modules['unicodedata'] = None;" \
            # """eval("'\\\\N{SOFT HYPHEN}'")"""
        # # We use a separate process because the unicodedata module may already
        # # have been loaded in this process.
        # result = script_helper.assert_python_failure("-c", code)
        # error = "SyntaxError: (unicode error) \\N escapes not supported " \
            # "(can't load unicodedata module)"
        # self.assertIn(error, result.err.decode("ascii"))
    
    def test_decimal_numeric_consistent(self):
        # Test that decimal and numeric are consistent,
        # i.e. if a character has a decimal value,
        # its numeric value should be the same.
        count = 0
        for i in range(0x10000):
            c = chr(i)
            dec = self.db.decimal(c, -1)
            if dec != -1:
                self.assertEqual(dec, self.db.numeric(c))
                count += 1
        self.assertTrue(count >= 10) # should have tested at least the ASCII digits

    def test_digit_numeric_consistent(self):
        # Test that digit and numeric are consistent,
        # i.e. if a character has a digit value,
        # its numeric value should be the same.
        count = 0
        for i in range(0x10000):
            c = chr(i)
            dec = self.db.digit(c, -1)
            if dec != -1:
                self.assertEqual(dec, self.db.numeric(c))
                count += 1
        self.assertTrue(count >= 10) # should have tested at least the ASCII digits

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
                c for c in range(sys.maxunicode+1)
                if "\x00" in chr(c).lower()+chr(c).upper()+chr(c).title()
            ],
            [0]
        )

    def test_bug_4971(self):
        # LETTER DZ WITH CARON: DZ, Dz, dz
        self.assertEqual("\u01c4".title(), "\u01c5")
        self.assertEqual("\u01c5".title(), "\u01c5")
        self.assertEqual("\u01c6".title(), "\u01c5")

    def test_linebreak_7643(self):
        for i in range(0x10000):
            lines = (chr(i) + 'A').splitlines()
            if i in (0x0a, 0x0b, 0x0c, 0x0d, 0x85,
                     0x1c, 0x1d, 0x1e, 0x2028, 0x2029):
                self.assertEqual(len(lines), 2,
                                 r"\u%.4x should be a linebreak" % i)
            else:
                self.assertEqual(len(lines), 1,
                                 r"\u%.4x should not be a linebreak" % i)

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

    def run_normalization_tests(self, testdata):
        part = None
        part1_data = {}

        def NFC(str):
            return unicodedata.normalize("NFC", str)

        def NFKC(str):
            return unicodedata.normalize("NFKC", str)

        def NFD(str):
            return unicodedata.normalize("NFD", str)

        def NFKD(str):
            return unicodedata.normalize("NFKD", str)

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

            self.assertTrue(unicodedata.is_normalized("NFC", c2))
            self.assertTrue(unicodedata.is_normalized("NFC", c4))

            self.assertTrue(unicodedata.is_normalized("NFD", c3))
            self.assertTrue(unicodedata.is_normalized("NFD", c5))

            self.assertTrue(unicodedata.is_normalized("NFKC", c4))
            self.assertTrue(unicodedata.is_normalized("NFKD", c5))

            # Record part 1 data
            if part == "@Part1":
                part1_data[c1] = 1

        # Perform tests for all other data
        for c in range(sys.maxunicode+1):
            X = chr(c)
            if X in part1_data:
                continue
            self.assertTrue(X == NFC(X) == NFD(X) == NFKC(X) == NFKD(X), c)

    def test_edge_cases(self):
        self.assertRaises(TypeError, unicodedata.normalize)
        self.assertRaises(ValueError, unicodedata.normalize, 'unknown', 'xx')
        self.assertEqual(unicodedata.normalize('NFKC', ''), '')

    def test_bug_834676(self):
        # Check for bug 834676
        unicodedata.normalize('NFC', '\ud55c\uae00')


if __name__ == "__main__":
    unittest.main()

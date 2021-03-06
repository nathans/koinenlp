#! /usr/bin/env python3
#
# Unit tests for koinenlp.py

import json
import unittest

import koinenlp


class KoinenlpTest(unittest.TestCase):
    tests_input = "tests.json"

    def setUp(self):
        tests_file = open(self.tests_input)
        tests_text = tests_file.read()
        tests_file.close()
        self.tests = {}
        self.tests.update(json.loads(tests_text))

    def test_simplify_tag_1(self):
        case = koinenlp.simplify_tag("VAI-AAI3S")
        self.assertEqual(case, "VAI")

    # Second test to ensure that already-simple tags don't get mangled
    def test_simplify_tag_2(self):
        case = koinenlp.simplify_tag("C")
        self.assertEqual(case, "C")

    def test_strip_diacritics(self):
        case = koinenlp.strip_diacritics(
            self.tests["strip_diacritics"]["case"])
        self.assertEqual(case, self.tests["strip_diacritics"]["result"])

    def test_unicode_normalize(self):
        case = koinenlp.unicode_normalize(
            self.tests["unicode_normalize"]["case"])
        self.assertEqual(case, self.tests["unicode_normalize"]["result"])

    def test_final_sigma(self):
        case = koinenlp.final_sigma(self.tests["final_sigma"]["case"])
        self.assertEqual(case, self.tests["final_sigma"]["result"])

    def test_lowercase(self):
        case = koinenlp.lowercase(self.tests["lowercase"]["case"])
        self.assertEqual(case, self.tests["lowercase"]["result"])

    # Distinguish between types of elision: apostrophe
    def test_remove_elision_1(self):
        case = koinenlp.remove_elision(self.tests["remove_elision_1"]["case"])
        self.assertEqual(case, self.tests["remove_elision_1"]["result"])

    # Elision with \u2019
    def test_remove_elision_2(self):
        case = koinenlp.remove_elision(self.tests["remove_elision_2"]["case"])
        self.assertEqual(case, self.tests["remove_elision_2"]["result"])

    # Elision when input has diacritics
    def test_remove_elision_3(self):
        case = koinenlp.remove_elision(self.tests["remove_elision_3"]["case"],
                                       diacritics=True)
        self.assertEqual(case, self.tests["remove_elision_3"]["result"])

    def test_remove_punctuation(self):
        case = koinenlp.remove_punctuation(
            self.tests["remove_punctuation"]["case"])
        self.assertEqual(case, self.tests["remove_punctuation"]["result"])

    def test_normalize(self):
        case = koinenlp.normalize(self.tests["normalize"]["case"])
        self.assertEqual(case, self.tests["normalize"]["result"])

    def tearDown(self):
        self.tests.clear()


if __name__ == '__main__':
    unittest.main()

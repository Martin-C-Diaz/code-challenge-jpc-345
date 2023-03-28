import unittest

from app.utils import parse_and_transform


class TestParseSentence(unittest.TestCase):
    def test_one_word(self):
        self.assertEqual(parse_and_transform("Smooth"), "S3h")

    def test_multiple_words(self):
        self.assertEqual(parse_and_transform("Space separated"), "S3e s5d")
        self.assertEqual(parse_and_transform("Dash-separated"), "D2h-s5d")

    def test_word_with_number(self):
        self.assertEqual(parse_and_transform("Number2separated"), "N4r2s5d")

    def test_word_with_non_alpha_char(self):
        self.assertEqual(parse_and_transform("Non-alpha,separated"), "N1n-a3a,s5d")

    def test_sentence_with_multiple_separators(self):
        self.assertEqual(
            parse_and_transform("Multiple-separators!in@one#sentence"),
            "M5e-s6s!i0n@o1e#s4e",
        )

    def test_sentence_with_numbers(self):
        self.assertEqual(parse_and_transform("The answer is 42"), "T1e a4r i0s 42")

    def test_empty_sentence(self):
        self.assertEqual(parse_and_transform(""), "")


if __name__ == "__main__":
    unittest.main()

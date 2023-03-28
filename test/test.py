import unittest

from app.main import parse_and_transform


class TestParseSentence(unittest.TestCase):
    def test_one_word(self):
        self.assertEqual(parse_and_transform("Smooth"), "S3h")

    def test_multiple_words(self):
        self.assertEqual(parse_and_transform("Space separated"), "S3e s5d")
        self.assertEqual(parse_and_transform("Dash-separated"), "D2h-s5d")

    def test_word_with_number(self):
        self.assertEqual(parse_and_transform("Number2separated"), "N4r2s5d")

    def test_word_with_non_alpha_char(self):
        self.assertEqual(parse_and_transform("Non-alpha,separated"), "N4a,-s5d")

    def test_sentence_with_multiple_separators(self):
        self.assertEqual(
            parse_and_transform("Multiple-separators!in@one#sentence"),
            "M7e-s9s!i1n@o2e#s7e",
        )

    def test_empty_sentence(self):
        self.assertEqual(parse_and_transform(""), "")


if __name__ == "__main__":
    unittest.main()

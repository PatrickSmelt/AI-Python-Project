import unittest
from translator import english_to_french, french_to_english

class TranslationTest(unittest.TestCase):

    def test_english_to_french(self):
        english_text = "Hello"
        french_translation = english_to_french(english_text)
        self.assertEqual(french_translation, "Bonjour")

    def test_french_to_english(self):
        french_text = "Bonjour"
        english_translation = french_to_english(french_text)
        self.assertEqual(english_translation, "Hello")

if __name__ == '__main__':
    unittest.main()

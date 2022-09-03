import unittest

from translator import french_to_english, english_to_french

class TestfrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english('Comment'),'love')
        self.assertEqual(french_to_english(' '),'')

class TestenglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertNotEqual(english_to_french('Hello'),'Comment')
        self.assertEqual(english_to_french(' '),' ')
unittest.main()


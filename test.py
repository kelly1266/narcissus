import unittest
from helper_functions import parse_name, parse_notif_from_tesseract


class TestParseName(unittest.TestCase):
    def test_exiled(self):
        """
        Tests that
        :return:
        """
        input_str = 'You exiled playername'
        expected = ['playername']
        result = parse_name(input_str)
        self.assertEqual(result, expected)

    def test_disrupted(self):
        """

        :return:
        """
        input_str = 'You disrupted playername'
        expected = ['playername']
        result = parse_name(input_str)
        self.assertEqual(result, expected)

    def test_assist(self):
        """

        :return:
        """
        input_str = 'You assisted in exiling playername'
        expected = ['playername']
        result = parse_name(input_str)
        self.assertEqual(result, expected)


class TestParseTesseract(unittest.TestCase):
    def test_exile_notif(self):
        input_str = """YOU EXILED COACHLEMONS
♀"""
        expected = 'you exiled coachlemons'
        result = parse_notif_from_tesseract(input_str)
        self.assertEqual(result, expected)

    def test_disrupted_notif(self):
        input_str = """YOU DISRUPTED MEELMAJOR wil rg
7 ra = » ..


♀"""
        expected = 'you disrupted meelmajor'
        result = parse_notif_from_tesseract(input_str)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

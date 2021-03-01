import unittest
from helper_functions import parse_name


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

if __name__ == '__main__':
    unittest.main()

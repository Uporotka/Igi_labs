import unittest
from Task_1 import  *


# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here


class TestCountSentences(unittest.TestCase):
    def test_empty_text(self):
        expected = 0
        actual = amount_of_sentences('')
        self.assertEqual(actual, expected,
                         'Empty text test: result isn\'t ' + str(expected))

    def test_abbreviations(self):
        text = 'Hello, Mr. Derek. Sample text i.e. and more Ph.D. - it\'s greate text!!'
        expected = 3
        actual = amount_of_sentences(text)
        self.assertEqual(actual, expected,
                         'Abbreviations test: number of sentences not ' + str(expected))

    def test_sample_text(self):
        text = 'Oh!!! Thats good idea; Oh no... I forgot my keys in the car. '
        expected = 3
        actual = amount_of_sentences(text)
        self.assertEqual(actual, expected,
                         'Sample text test: number of sentences not ' + str(expected))


class TestCountNonDeclarativeSentences(unittest.TestCase):
    def test_empty_text(self):
        expected = 0
        actual = amount_non_decl('')
        self.assertEqual(actual, expected,
                         'Empty text test: result isn\'t ' + str(expected))

    def test_abbreviations(self):
        text = 'Hello, Mr. Derek. Sample text i.e. and more Ph.D. - it\'s greate text!!'
        expected = 1
        actual = amount_non_decl(text)
        self.assertEqual(actual, expected,
                         'Abbreviations test: number of non decl. sentences not' + str(expected))

    def test_sample_text(self):
        text = 'Oh!!! Thats good idea; Oh no... I forgot my keys in the car. '
        expected = 1
        actual = amount_non_decl(text)
        self.assertEqual(actual, expected,
                         'Sample text test: number of non decl. sentences not ' + str(expected))


class TestGetAverageSentenceLength(unittest.TestCase):
    def test_empty_text(self):
        expected = 0
        actual = average_len_sent('')
        self.assertEqual(actual, expected,
                         'Empty text test: result isn\'t ' + str(expected))

    def test_abbreviations(self):
        text = 'Hello, Mr. Derek. Sample text i.e. and more Ph.D. - it\'s greate text!!'
        expected = 47 / 3
        actual = average_len_sent(text)
        self.assertEqual(actual, expected,
                         'Average len with abbreviations test: result isn\'t ' + str(expected))

    def test_text_with_numbers(self):
        text = 'Oh!!! 4 Heloo aaaa. asd6laa, 777; word?'
        expected = 22 / 3
        actual = average_len_sent(text)
        self.assertEqual(actual, expected,
                         'Average len with numbers test: result isn\'t ' + str(expected))


class TestAvgWordLength(unittest.TestCase):
    def test_empty_text(self):
        expected = 0
        actual = average_len_word('')
        self.assertEqual(actual, expected,
                         'Empty text test: result isn\'t ' + str(expected))

    def test_abbreviations(self):
        text = 'Hello, Mr. Derek. Sample text i.e. and more Ph.D. - its greate text!!'
        expected = 47 / 14
        actual = average_len_word(text)
        self.assertEqual(actual, expected,
                         'Average len with abbreviations test: result isn\'t ' + str(expected))

    def test_text_with_numbers(self):
        text = 'Oh!!! 4 Heloo aaaa. asd6laa, 777; word?'
        expected = round(22 / 5, 2)
        actual = average_len_word(text)
        self.assertEqual(actual, expected,
                         'Average len with numbers test: result isn\'t ' + str(expected))


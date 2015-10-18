from unittest import TestCase
from median import find_median

__author__ = 'Denis'


class TestMedian(TestCase):
    def test_1(self):
        list_one = [1, 2, 3, 4]
        list_two = [1, 4, 5, 6]
        self.assertEqual(find_median(list_one, list_two), 3.5, "Good")

    def test_2(self):
        list_one = []
        list_two = []
        self.assertEqual(find_median(list_one, list_two), 0.0, "Good")

    def test_3(self):
        list_one = [1]
        list_two = [1]
        self.assertEqual(find_median(list_one, list_two), 1, "Good")

    def test_4(self):
        list_one = [1]
        list_two = [1, 4]
        self.assertEqual(find_median(list_one, list_two), 0.0, "Good")

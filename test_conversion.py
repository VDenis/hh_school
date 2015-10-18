from unittest import TestCase
from conversion import find_count_conversions

__author__ = 'Denis'


class TestConversion(TestCase):
    def test_1(self):
        n = 5
        m = 13
        self.assertEqual(find_count_conversions(n, m), 3, "Good")

    def test_2(self):
        n = 5
        m = 100
        self.assertEqual(find_count_conversions(n, m), 14, "Good")

    def test_3(self):
        n = 5
        m = 101
        self.assertEqual(find_count_conversions(n, m), 15, "Good")

    def test_4(self):
        n = 2
        m = 128
        self.assertEqual(find_count_conversions(n, m), 6, "Good")

    def test_5(self):
        n = 4
        m = 3
        self.assertEqual(find_count_conversions(n, m), None, "Good")

    def test_6(self):
        n = -2
        m = -1
        self.assertEqual(find_count_conversions(n, m), None, "Good")

"""Tests for app.backend.word_vectors"""

import unittest
from analogies.backend import word_vectors as wv


class TestModel(unittest.TestCase):
    """
        Model tests
    """

    def test_load_failed(self):
        """
            ensures model raises Error on incorrect paths
        """
        with self.assertRaises(FileNotFoundError):
            wv.Model("bullshit")

    def test_load_passes(self):
        try:
            wv.Model("analogies/backend/brown-20171221.vec")
        except:
            raise AssertionError("Failed to load existing model")

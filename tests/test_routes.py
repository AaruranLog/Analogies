import os
import unittest
from analogies import app

class AnalogiesTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_blank(self):
        url_list = ["/", "/index", "/source-code", "/predict",
                    "/brown/word"]

        for url in url_list:
            try:
                output = self.client.get(url)
            except Exception:
                raise AssertionError(f"Failed to get from URL: {url}")

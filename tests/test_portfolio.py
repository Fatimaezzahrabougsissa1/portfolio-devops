import unittest
import os

class TestPortfolio(unittest.TestCase):
    def test_index_exists(self):
        self.assertTrue(os.path.exists("index.html") or os.path.exists("../index.html"), "Le fichier index.html doit exister")

if __name__ == "__main__":
    unittest.main()

# tests/test_testatolibrary.py

import unittest
from testatolibrary import saludar

class TestTestatolibrary(unittest.TestCase):
    def test_saludar(self):
        self.assertEqual(saludar(), "Hola desde testatolibrary!")

if __name__ == "__main__":
    unittest.main()

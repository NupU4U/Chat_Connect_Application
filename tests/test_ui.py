import unittest
from ui import ChatApp

class TestUI(unittest.TestCase):
    def test_ui_load(self):
        app = ChatApp()
        self.assertIsNotNone(app.build())

if __name__ == "__main__":
    unittest.main()

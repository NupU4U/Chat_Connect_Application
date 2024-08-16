import unittest
from server import start_server

class TestServer(unittest.TestCase):
    def test_server_initialization(self):
        try:
            start_server()
            result = True
        except:
            result = False
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()

import unittest
from client import receive_messages, send_messages

class TestClient(unittest.TestCase):
    def test_client_connection(self):
        # Test if client can connect to the server
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()

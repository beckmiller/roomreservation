import unittest
from main import send_email


class TestSendMail(unittest.TestCase):
    
    def test_types(self):
        self.assertRaises(TypeError, send_email, 4)
        self.assertRaises(TypeError, send_email, 3.0)
        self.assertRaises(TypeError, send_email, "3")
        self.assertRaises(TypeError, send_email, False)
        self.assertRaises(TypeError, send_email, [1, 2])

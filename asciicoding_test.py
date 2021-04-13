import unittest 
from asciicoding import encoding_string
from asciicoding import decoding_string


class TestEncodingString(unittest.TestCase):
    def test_encoding(self):
        self.assertEqual(encoding_string("hello",2),list("jgnnq"))
        self.assertEqual(encoding_string("123",2),list("345"))

        
    def test_decoding(self):
        self.assertEqual(decoding_string("jgnnq",2),list("hello"))
        self.assertEqual(decoding_string("345",2),list("123"))

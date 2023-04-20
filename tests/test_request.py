import unittest
from unittest import TestCase


class TestSignatureValidity(TestCase):
    @unittest.skip("Not implemented")
    def test_valid_signature(self):
        pass

    @unittest.skip("Not implemented")
    def test_signature_does_not_match(self):
        pass

    @unittest.skip("Not implemented")
    def test_signature_content_is_empty(self):
        pass

    @unittest.skip("Not implemented")
    def test_no_x_grd_header(self):
        pass

    @unittest.skip("Not implemented")
    def test_signature_content_is_not_hmac_hashed(self):
        pass


class TestMessageBody(TestCase):
    @unittest.skip("Not implemented")
    def test_message_is_valid(self):
        pass

    @unittest.skip("Not implemented")
    def test_empty_message(self):
        pass

    @unittest.skip("Not implemented")
    def test_message_is_not_protobuf_encoded(self):
        pass

    @unittest.skip("Not implemented")
    def test_message_is_not_according_to_schema(self):
        pass

    @unittest.skip("Not implemented")
    def test_message_is_binary_but_not_protobuf(self):
        pass

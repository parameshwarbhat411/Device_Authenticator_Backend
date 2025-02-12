import unittest
from datetime import datetime
from services.token_factory import TokenFactory
from database import delete_token, find_token_by_email_and_device


class TestTokenFactory(unittest.TestCase):

    def setUp(self):
        self.email = "test@example.com"
        self.device_id = "device123"
        self.token, self.expires_at = TokenFactory.create_and_persist_token(self.email, self.device_id)

    def test_generate_token(self):
        token = TokenFactory.generate_token()
        self.assertIsNotNone(token)
        self.assertEqual(len(token), 43)

    def test_cleanUp_token(self):
        TokenFactory.cleanUp_token(self.email, self.device_id)
        token = find_token_by_email_and_device(self.email, self.device_id)
        self.assertIsNone(token)

    def test_create_and_persist_token(self):
        token, expires_at = TokenFactory.create_and_persist_token(self.email, self.device_id)
        self.assertIsNotNone(token)
        self.assertIsInstance(expires_at, datetime)
        self.assertGreater(expires_at, datetime.now())

    def test_validate_device_token(self):
        self.assertTrue(TokenFactory.validate_device_token(self.token, self.device_id))
        self.assertFalse(TokenFactory.validate_device_token("invalid_token", self.device_id))
        self.assertFalse(TokenFactory.validate_device_token(self.token, "invalid_device_id"))

    def tearDown(self):
        delete_token(self.token)


if __name__ == '__main__':
    unittest.main()

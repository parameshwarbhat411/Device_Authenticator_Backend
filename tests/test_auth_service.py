import unittest
from datetime import datetime, timedelta
from services.auth_service import AuthService
from services.token_factory import TokenFactory
from database import store_token, delete_token, get_token


class TestAuthService(unittest.TestCase):

    def setUp(self):
        self.email = "test@example.com"
        self.device_id = "device123"
        self.token, self.expires_at = TokenFactory.create_and_persist_token(self.email, self.device_id)

    def test_verify_email_and_generateToken(self):
        token, expires_at = AuthService.verify_email_and_generateToken(self.email, self.device_id)
        self.assertIsNotNone(token)
        self.assertIsInstance(expires_at, datetime)

    def test_validate_device_token(self):
        self.assertTrue(AuthService.validate_device_token(self.token, self.device_id))
        self.assertFalse(AuthService.validate_device_token("invalid_token", self.device_id))
        self.assertFalse(AuthService.validate_device_token(self.token, "invalid_device_id"))

    def tearDown(self):
        delete_token(self.token)


if __name__ == '__main__':
    unittest.main()

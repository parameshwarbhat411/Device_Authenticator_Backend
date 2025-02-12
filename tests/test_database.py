import unittest
from datetime import datetime, timedelta
from database import store_token, get_token, delete_token, find_token_by_email_and_device


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.token = "test_token"
        self.email = "test@example.com"
        self.device_id = "device123"
        self.expires_at = datetime.now() + timedelta(minutes=30)
        store_token(self.token, self.email, self.device_id, self.expires_at)

    def test_store_token(self):
        stored_token = get_token(self.token)
        self.assertIsNotNone(stored_token)
        self.assertEqual(stored_token["email"], self.email)
        self.assertEqual(stored_token["device_id"], self.device_id)
        self.assertEqual(stored_token["expires_at"], self.expires_at)

    def test_get_token(self):
        token_data = get_token(self.token)
        self.assertIsNotNone(token_data)
        self.assertEqual(token_data["email"], self.email)
        self.assertEqual(token_data["device_id"], self.device_id)
        self.assertEqual(token_data["expires_at"], self.expires_at)

    def test_delete_token(self):
        delete_token(self.token)
        token_data = get_token(self.token)
        self.assertIsNone(token_data)

    def test_find_token_by_email_and_device(self):
        found_token = find_token_by_email_and_device(self.email, self.device_id)
        self.assertEqual(found_token, self.token)

    def tearDown(self):
        delete_token(self.token)


if __name__ == '__main__':
    unittest.main()

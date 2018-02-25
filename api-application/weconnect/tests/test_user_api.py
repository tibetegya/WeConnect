import unittest
from app.user_api import User, users

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.my_user = User()
        self.test_info = {
                    'id': 1,
                    'user_name': 'tibetegyaGeorge',
                    'password': 'tibetegya',
                    'email_address': 'tibetegya@andela.com',
                    'user_avatar': 'pic.png',
                    'business_owned': ['business1', 'business2']
                    }

    def test_get(self):
        self.assertEqual(self.my_user.get('user1'), self.test_info , msg='Could not read from dictionary' )



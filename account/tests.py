from django.test import TestCase
from account.services.activate import longpoll_get_new_admin
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from parameterized import parameterized
from unittest.mock import patch
User = get_user_model()

# Create your tests here.
class LongPollTestCase(TestCase):
    def test_longpoll_get_new_admin_no_unactivated_users(self):
        user = User.objects.create(username='test_user')
        result = longpoll_get_new_admin(user)
        self.assertEqual(result, [])

    @parameterized.expand([
        ([{'username': 'user1', 'nickname': 'nickname1', 'sended': []}], [{'username': 'user1', 'nickname': 'nickname1', 'sended': ['test_user']}], [{'username': 'user1', 'nickname': 'nickname1'}]),
        ([{'username': 'user2', 'nickname': 'nickname2', 'sended': ['test_user']}], [], [])
    ])
    def test_longpoll_get_new_admin_unactivated_users(self, data, expected_data, expected_result):
        user = User.objects.create(username='test_user')
        user2 = User.objects.create(username='user1', nickname='nickname1', is_active=False)
        with patch('module.get_data', return_value=data), patch.object(User.objects, 'get', return_value=user2):
            result = longpoll_get_new_admin(user)
        self.assertEqual(result, expected_result)
        self.assertEqual(data, expected_data)

    def test_longpoll_get_new_admin_user_not_found(self):
        user = User.objects.create(username='test_user')
        data = [{'username': 'user1', 'nickname': 'nickname1', 'sended': []}]
        with patch('module.get_data', return_value=data), patch.object(User.objects, 'get', side_effect=ObjectDoesNotExist):
            result = longpoll_get_new_admin(user)
        self.assertEqual(result, [])
        self.assertEqual(data, [])

    def test_longpoll_get_new_admin_timeout(self):
        user = User.objects.create(username='test_user')
        with patch('module.wait', side_effect=TimeoutError):
            result = longpoll_get_new_admin(user)
        self.assertFalse(result, "Result should be False")

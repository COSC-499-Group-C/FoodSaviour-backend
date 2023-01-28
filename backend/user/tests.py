import json
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .serializers import UserSerializer


class UserTest(APITestCase):

    def setUp(self):
        '''
        Set up a Client API and create a test user.
        '''
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', email='testuser@test.com', password='testing')
        self.user.save()

    def _require_login(self):
        '''
        Login and authenticate the created test user.
        '''
        self.client.login(username='testuser', password='testing')

    def test_get_all_users(self):
        """
        Confirm that the Get All Users API endpoint is correct.
        """
        self._require_login()
        response = self.client.get('http://127.0.0.1:8000/users/')
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_user(self):
        """
        Confirm that the User Instance API endpoint is correct.
        """
        self._require_login()
        user = User.objects.order_by('id').first()
        response = self.client.get(f'http://127.0.0.1:8000/users/{user.id}/')
        serializer = UserSerializer(user, many=False)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        """
        Test the update User API
        """

    def test_update_user(self):
        self._require_login()
        user = User.objects.first()
        response = self.client.patch(f'http://127.0.0.1:8000/users/{user.id}/', {'username': 'test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """
    Test the add User API
    """
    def test_add_user(self):
        self._require_login()
        request = self.client.post('http://127.0.0.1:8000/users/', {'username': 'TestUser2', 'password': 'testing123'})
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    """
    Test the delete User API
    """

    def test_destroy_user(self):
        self._require_login()
        user = User.objects.first()
        request = self.client.delete(f'http://127.0.0.1:8000/users/{user.id}/')
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)

    """
    Test the update User API
    """

    def test_update_user(self):
        self._require_login()
        user = User.objects.first()
        request = self.client.patch(f'http://127.0.0.1:8000/users/{user.id}/', {'username': 'DummyUser'})
        self.assertEqual(request.status_code, status.HTTP_200_OK)

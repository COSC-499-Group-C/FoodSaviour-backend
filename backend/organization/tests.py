from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import OrgName, OrgGroup
from .serializers import OrgNameSerializer


class OrgNameTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user('testuser', email='testuser@test.com', password='testing')
        self.user.save()
        self.orgName = OrgName(name='Test Company 1')
        self.orgName.save()

    def _require_login(self):
        self.client.login(username='testuser', password='testing')

    def test_get_all_Org(self):
        self._require_login()
        response = self.client.get('https://127.0.0.1:8000/orgName/')
        org = OrgName.objects.all()
        serializer = OrgNameSerializer(org, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_Org(self):
        self._require_login()
        response = self.client.get(f'https://127.0.0.1:8000/orgName/{1}')
        org = OrgName.objects.first()
        serializer = OrgNameSerializer(org, many=False)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_org(self):
        self._require_login()
        response = self.client.post('https://127.0.0.1:8000/orgName/', {'name': 'test company 2'})
        self.assertEqual(response.status, status.HTTP_201_CREATED)
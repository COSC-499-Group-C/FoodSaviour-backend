from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import OrgName, OrgGroup
from .serializers import OrgNameSerializer, OrgGroupSerializer


class OrgNameTest(APITestCase):

    """
    Setting up test database
    """
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user('testuser', email='testuser@test.com', password='testing')
        self.user.save()
        self.orgName = OrgName(name='Test Company')
        self.orgName.save()
        self.orgGroup = OrgGroup(group_id=self.orgName.id, user_id=self.user.id)
        self.orgGroup.save()

    """
    Getting User to login
    """

    def _require_login(self):
        self.client.login(username='testuser', password='testing')

    """
    Test get all Organization
    """

    def test_get_all_Org(self):
        self._require_login()
        response = self.client.get('https://127.0.0.1:8000/orgName/')
        org = OrgName.objects.all()
        serializer = OrgNameSerializer(org, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """
    Test getting one organization
    """

    def test_get_one_Org(self):
        self._require_login()
        org = OrgName.objects.first()
        response = self.client.get(f'https://127.0.0.1:8000/orgName/{org.id}/')
        serializer = OrgNameSerializer(org, many=False)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """
    Test add Organization API
    """

    def test_add_org(self):
        self._require_login()
        response = self.client.post('https://127.0.0.1:8000/orgName/', {'name': 'test company 2'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_org(self):
        self._require_login()
        org = OrgName.objects.first()
        response = self.client.patch(f'https://127.0.0.1/orgName/{org.id}/', {'name': 'Test Company 1'})
        self.assertEqual(response.data, OrgNameSerializer(OrgName.objects.first()).data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_org(self):
        self._require_login()
        org = OrgName.objects.first()
        response = self.client.delete(f'https://127.0.0.1/orgName/{org.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_all_orgGroup(self):
        self._require_login()
        orgGroup = OrgGroup.objects.all()
        response = self.client.get('https://127.0.0.1/orgGroup/')
        self.assertEqual(response.data, OrgGroupSerializer(orgGroup, many=True).data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_orgGroup(self):
        self._require_login()
        orgGroup = OrgGroup.objects.first()
        response = self.client.get(f'https://127.0.0.1/orgGroup/{orgGroup.id}/')
        self.assertEqual(response.data, OrgGroupSerializer(orgGroup, many=False).data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

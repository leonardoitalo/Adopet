from rest_framework.test import APITestCase
from django.contrib.auth.models import User 
from django.urls import reverse
from rest_framework import status
from adopet.models import Shelter

class SheltersTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Shelters-list')
        self.client.force_authenticate(user=self.user)
        self.shelter_01 = Shelter.objects.create(
            name = 'Teste Shelter Um'
        )
        self.shelter_02 = Shelter.objects.create(
            name = 'Teste Shelter Um'
        )
            
    def test_request_get_list_shelters(self):
        """Teste de requisição GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
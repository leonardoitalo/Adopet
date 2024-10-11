from django.urls import reverse
from rest_framework import status
from adopet.tests.base_test import APIBaseTestCase
from adopet.serializers import ShelterSerializer

class SheltersTestCase(APIBaseTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('Shelters-list')
        self.shelter = self.create_shelter()
            
    def test_request_get_list_shelters(self):
        """Teste de requisição GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_request_get_list_one_shelter(self):
        """Teste de requisição GET para listar um shelter"""
        response = self.client.get(f'{self.url}{self.shelter.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_data = self.get_serialized_data(self.shelter, ShelterSerializer)
        self.assertEqual(response.data, serialized_data)
        
    def test_request_post_shelter(self):
        """Teste de requisição POST para um shelter"""
        datas = {
            'name': 'Test Post Shelter',
        }

        response = self.client.post(self.url, datas)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_request_delete_shelter(self):
        """Teste de requisição DELETE para um shelter"""
        response = self.client.delete(f'{self.url}{self.shelter.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_request_put_shelter(self):
        """Teste de requisição PUT para um shelter"""
        datas = {
            'name': 'Test Put Shelter'
        }

        response = self.client.put(f'{self.url}{self.shelter.id}/', datas)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
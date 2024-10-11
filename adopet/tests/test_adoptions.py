from django.urls import reverse
from rest_framework import status
from adopet.tests.base_test import APIBaseTestCase
from adopet.serializers import AdoptionSerializer

class AdoptionsTestCase(APIBaseTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('Adoptions-list')
        self.tutor = self.create_tutor()
        self.shelter = self.create_shelter()
        self.pet = self.create_pet(shelter=self.shelter)
        self.adoption = self.create_adoption(self.tutor, self.pet)
        
    def test_request_get_list_adoptions(self):
        """Teste de requisição GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_request_get_list_one_adoption(self):
        """Teste de requisição GET para listar um adoption"""
        response = self.client.get(f'{self.url}{self.adoption.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_data = self.get_serialized_data(self.adoption, AdoptionSerializer)
        self.assertEqual(response.data, serialized_data)

    def test_request_post_adoption(self):
        """Teste de requisição POST para um adoption"""
        datas = {
            'pet': self.pet.pk,
            'tutor': self.tutor.pk
        }
        response = self.client.post(self.url, datas)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_request_delete_adoption(self):
        """Teste de requisição DELETE para um adoption"""
        response = self.client.delete(f'{self.url}{self.adoption.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_request_put_adoption(self):
        """Teste de requisição PUT para um adoption"""
        self.shelter_put = self.create_shelter('Test Put Shelter')
        self.pet_put = self.create_pet(shelter=self.shelter_put)
        self.tutor_put = self.create_tutor('Test Put Tutor', 'tutor@put.com', '12345678')
         
        datas = {
            'pet': self.pet_put.pk,
            'tutor': self.tutor_put.pk
        }

        response = self.client.put(f'{self.url}{self.adoption.id}/', datas)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
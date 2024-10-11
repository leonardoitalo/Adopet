from django.urls import reverse
from rest_framework import status
from adopet.tests.base_test import APIBaseTestCase
from adopet.serializers import PetSerializer

class PetsTestCase(APIBaseTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('Pets-list')
        self.shelter = self.create_shelter()
        self.pet = self.create_pet(shelter=self.shelter)
        
    def test_request_get_list_pets(self):
        """Teste de requisição GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_request_get_list_one_pet(self):
        """Teste de requisição GET para listar um pet"""
        response = self.client.get(f'{self.url}{self.pet.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_data = self.get_serialized_data(self.pet, PetSerializer)
        self.assertEqual(response.data, serialized_data)
        
    def test_request_post_pet(self):
        """Teste de requisição POST para um pet"""
        datas = {
            'name': 'Test Post Pet',
            'age': '1 ano',
            'size': 'pequeno',
            'description': 'Alegre',
            'address': 'São Paulo (SP)',
            'adopted': False,
            'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQktXg5_v8-L9AslphhrFvphE12SWkGl-_Jig&usqp=CAU',
            'shelter': self.shelter.id
        }

        response = self.client.post(self.url, datas)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
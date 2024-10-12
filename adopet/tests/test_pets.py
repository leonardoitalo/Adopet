from django.urls import reverse
from rest_framework import status
from adopet.tests.base_test import APIBaseTestCase
from adopet.serializers import PetSerializer
from adopet.models import Pet, Shelter
from django.contrib.auth.models import User 

class PetsTestCase(APIBaseTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('Pets-list')
        self.shelter = Shelter.objects.get(pk=3)
        self.user_shelter = User.objects.get(id=2)
        self.pet = Pet.objects.get(pk=2)
        
    def test_request_get_list_pets(self):
        """Teste de requisição GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_request_get_list_one_pet(self):
        """Teste de requisição GET para listar um pet"""
        response = self.client.get(f'{self.url}{self.pet.pk}/')
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
            'shelter': self.shelter.pk
        }

        response = self.client.post(self.url, datas)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_check_shelter_can_post_pet(self):
        """Teste para verificar se um abrigo consegue criar um pet"""
        datas = {
            'name': 'Test Post Pet',
            'age': '1 ano',
            'size': 'pequeno',
            'description': 'Alegre',
            'address': 'São Paulo (SP)',
            'adopted': False,
            'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQktXg5_v8-L9AslphhrFvphE12SWkGl-_Jig&usqp=CAU',
            'shelter': self.shelter.pk
        }

        self.client.force_authenticate(user=self.user_shelter)
        response = self.client.post(self.url, datas)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_request_delete_pet(self):
        """Teste de requisição DELETE para um pet"""
        response = self.client.delete(f'{self.url}{self.pet.pk}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_check_shelter_can_delete_pet(self):
        """Teste para verificar se um abrigo consegue deletar uma adoção"""
        self.client.force_authenticate(user=self.user_shelter)
        response = self.client.delete(f'{self.url}{self.pet.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_request_put_shelter(self):
        """Teste de requisição PUT para um pet"""
        datas = {
            'name': 'Test Put Pet',
            'age': '2 meses',
            'size': 'médio',
            'description': 'Carinhoso',
            'address': 'Rio de Janeiro (RJ)',
            'adopted': False,
            'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQktXg5_v8-L9AslphhrFvphE12SWkGl-_Jig&usqp=CAU',
            'shelter': self.shelter.pk
        }

        response = self.client.put(f'{self.url}{self.pet.pk}/', datas)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_check_shelter_can_put_pet(self):
        """Teste para verificar se um abrigo consegue alterar um pet"""
        datas = {
            'name': 'Test Put Pet',
            'age': '2 meses',
            'size': 'médio',
            'description': 'Carinhoso',
            'address': 'Rio de Janeiro (RJ)',
            'adopted': False,
            'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQktXg5_v8-L9AslphhrFvphE12SWkGl-_Jig&usqp=CAU',
            'shelter': self.shelter.pk
        }
        
        self.client.force_authenticate(user=self.user_shelter)
        response = self.client.put(f'{self.url}{self.pet.pk}/', datas)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
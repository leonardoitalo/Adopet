from rest_framework.test import APITestCase
from django.contrib.auth.models import User 
from django.urls import reverse
from rest_framework import status
from adopet.models import Pet, Shelter

class PetsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Pets-list')
        self.client.force_authenticate(user=self.user)
        self.shelter = Shelter.objects.create(
            name = 'Teste Shelter Um'
        )
        self.pet_01 = Pet.objects.create(
            name = 'Pet teste Um',
            age = '1 ano',
            size = 'pequeno',
            description = 'Agradavel e alegre',
            address = 'Rio de janeiro (RJ)',
            adopted = False,
            image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQktXg5_v8-L9AslphhrFvphE12SWkGl-_Jig&usqp=CAU',
            shelter = self.shelter
        )

        
    def test_request_get_list_pets(self):
        """Teste de requisição GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
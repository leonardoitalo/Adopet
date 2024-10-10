from rest_framework.test import APITestCase
from django.contrib.auth.models import User 
from django.urls import reverse
from rest_framework import status
from adopet.models import Adoption, Pet, Shelter, Tutor
import datetime

class AdoptionsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Tutors-list')
        self.client.force_authenticate(user=self.user)
        self.tutor_01 = Tutor.objects.create(
            name = 'Teste tutor Um',
            email = 'tutor01@test.com',
            password = '12345678'
        )
        self.shelter_01 = Shelter.objects.create(
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
            shelter = self.shelter_01
        )
        self.adoption = Adoption.objects.create(
            date = datetime.date.today(), 
            pet = self.pet_01,
            tutor = self.tutor_01,
        )
        
    def test_request_get_list_pets(self):
        """Teste de requisição GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
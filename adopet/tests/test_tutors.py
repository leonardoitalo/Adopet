from rest_framework.test import APITestCase
from django.contrib.auth.models import User 
from django.urls import reverse
from rest_framework import status
from adopet.models import Tutor

class TutorsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Tutors-list')
        self.client.force_authenticate(user=self.user)
        self.tutor_01 = Tutor.objects.create(
            name = 'Teste tutor Um',
            email = 'tutor01@test.com',
            password = '12345678'
        )
        self.tutor_02 = Tutor.objects.create(
            name = 'Teste tutor Dois',
            email = 'tutor02@test.com',
            password = '12345678'
        )
        
    def test_request_get_list_tutors(self):
        """Teste de requisição GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
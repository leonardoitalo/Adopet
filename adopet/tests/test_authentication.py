from rest_framework.test import APITestCase
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status
from adopet.models import Tutor

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='admin')
        self.tutor = Tutor.objects.create(name='Tutor Test')
        self.url = reverse('Tutors-list')
    
    def test_authenticate_user_credencials(self):
        """Teste que vefifica a autenticação de um user com as credenciais corretas"""
        user = authenticate(username = 'admin', password='admin')
        self.assertTrue((user is not None) and user.is_authenticated)
        
    def test_authenticate_user_incorrect_username(self):
        """Teste que verifica a autenticação com username incorreto"""
        user = authenticate(username = 'admn', password='admin')
        self.assertFalse((user is not None) and user.is_authenticated)
        
    def test_authenticate_user_incorrect_password(self):
        """Teste que verifica a autenticação com senha incorreta"""
        user = authenticate(username = 'admin', password='adm')
        self.assertFalse((user is not None) and user.is_authenticated)
  
    def test_request_get_authorized(self):
        """Teste que verifica uma requisição GET autorizada"""
        self.client.force_authenticate(self.user)   
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_request_get_not_authorized(self):
        """Teste que verifica uma requisição GET não autorizada"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    

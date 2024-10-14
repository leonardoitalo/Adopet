from rest_framework.test import APITestCase
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status
from adopet.models import Tutor

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.user = Tutor.objects.create_user(email='admin@example.com', name='Admin', password='admin')
        self.url = reverse('Tutors-list')
    
    def test_authenticate_user_credencials(self):
        """Teste que vefifica a autenticação de um user com as credenciais corretas"""
        user = authenticate(email='admin@example.com', password='admin')
        self.assertTrue((user is not None) and self.user.is_authenticated)
        
    def test_authenticate_user_incorrect_email(self):
        """Teste que verifica a autenticação com email incorreto"""
        user = authenticate(email='admn@example.com', password='admin')
        self.assertFalse((user is not None) and user.is_authenticated)
        
    def test_authenticate_user_incorrect_password(self):
        """Teste que verifica a autenticação com senha incorreta"""
        user = authenticate(username = 'admin@example.com', password='adm')
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
        
    

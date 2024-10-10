from django.contrib.auth.models import User 
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='admin')
    
    def test_authenticate_user_credencials(self):
        """Teste que vefifica a autenticação de um user com as credenciais corretas"""
        user = authenticate(username = 'admin', password='admin')
        self.assertTrue((user is not None) and user.is_authenticated)
        
    def test_authenticate_user_incorrect_username(self):
        """Teste que verifica a autenticação de com username incorreto"""
        user = authenticate(username = 'admn', password='admin')
        self.assertFalse((user is not None) and user.is_authenticated)
        
    def test_authenticate_user_incorrect_password(self):
        """Teste que verifica a autenticação de com senha incorreta"""
        user = authenticate(username = 'admin', password='adm')
        self.assertFalse((user is not None) and user.is_authenticated)
        
    

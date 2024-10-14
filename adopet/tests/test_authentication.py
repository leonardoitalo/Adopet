from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status
from adopet.models import Tutor


class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.user = Tutor.objects.create_user(
            email="admin@example.com", name="Admin", password="admin"
        )
        self.url = reverse("Tutors-list")

    def test_authenticate_user_credencials(self):
        """Teste que vefifica a autenticação de um user com as credenciais corretas"""
        user = authenticate(email="admin@example.com", password="admin")
        self.assertTrue((user is not None) and self.user.is_authenticated)

    def test_authenticate_user_incorrect_email(self):
        """Teste que verifica a autenticação com email incorreto"""
        user = authenticate(email="admn@example.com", password="admin")
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_authenticate_user_incorrect_password(self):
        """Teste que verifica a autenticação com senha incorreta"""
        user = authenticate(username="admin@example.com", password="adm")
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


class UserRegistrationTest(APITestCase):
    def setUp(self):
        self.url = reverse("register_tutor")

    def test_register_user(self):
        """Teste que verifica o registro de um novo usuário"""
        data = {
            "email": "newuser@example.com",
            "name": "New User",
            "password": "ValidPassword123",
        }

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user_exists = Tutor.objects.filter(email="newuser@example.com").exists()
        self.assertTrue(user_exists)


class UserLoginTest(APITestCase):
    def setUp(self):
        # Criar um usuário no banco de dados antes do teste
        self.user = Tutor.objects.create_user(
            email="user@example.com", name="Test User", password="ValidPassword123"
        )
        self.url = reverse(
            "token_obtain_pair"
        )  # Defina o nome da URL para obter o token de autenticação

    def test_login_user(self):
        """Teste que verifica o login com credenciais corretas"""
        data = {"email": "user@example.com", "password": "ValidPassword123"}

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_login_invalid_credentials(self):
        """Teste que verifica o login com credenciais inválidas"""
        data = {"email": "user@example.com", "password": "WrongPassword123"}

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["detail"][0], "Senha incorreta.")

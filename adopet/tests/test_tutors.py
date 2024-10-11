from django.urls import reverse
from rest_framework import status
from adopet.tests.base_test import APIBaseTestCase
from adopet.serializers import TutorSerializer

class TutorsTestCase(APIBaseTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('Tutors-list')
        self.tutor = self.create_tutor()
        
    def test_request_get_list_tutors(self):
        """Teste de requisição GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_request_get_list_one_tutor(self):
        """Teste de requisição GET para listar um tutor"""
        response = self.client.get(f'{self.url}{self.tutor.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_data = self.get_serialized_data(self.tutor, TutorSerializer)
        self.assertEqual(response.data, serialized_data)
        
    def test_request_post_tutor(self):
        """Teste de requisição POST para um tutor"""
        datas = {
            'name': 'Test Post Tutor',
            'email': 'test@post.com',
            'password': 'test_post_password'
        }

        response = self.client.post(self.url, datas)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_request_delete_tutor(self):
        """Teste de requisição DELETE para um tutor"""
        response = self.client.delete(f'{self.url}{self.tutor.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_request_put_tutor(self):
        """Teste de requisição PUT para um tutor"""
        datas = {
            'name': 'Test Put Tutor',
            'email': 'test@put.com',
            'password': 'test_put_password'
        }

        response = self.client.put(f'{self.url}{self.tutor.id}/', datas)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
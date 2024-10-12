from django.urls import reverse
from rest_framework import status
from adopet.tests.base_test import APIBaseTestCase

class ThrottilingTestCase(APIBaseTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('Shelters-list')
            
    def test_rate_limiting_for_authenticated_user(self):
        for i in range(100): 
            response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_rate_limiting_for_authenticated_user_exceeded(self):
        for i in range(1000): 
            response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)
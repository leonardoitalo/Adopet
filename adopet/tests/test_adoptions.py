from django.urls import reverse
from rest_framework import status
from adopet.tests.base_test import APIBaseTestCase
from adopet.serializers import AdoptionSerializer
from adopet.models import Tutor, Pet, Adoption


class AdoptionsTestCase(APIBaseTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse("Adoptions-list")
        self.adoption = Adoption.objects.get(pk=1)
        self.pet = Pet.objects.get(pk=5)
        self.tutor = Tutor.objects.get(pk=5)
        self.user_shelter = Tutor.objects.get(id=2)

    def test_request_get_list_adoptions(self):
        """Teste de requisição GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_get_list_one_adoption(self):
        """Teste de requisição GET para listar um adoption"""
        response = self.client.get(f"{self.url}{self.adoption.pk}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_data = self.get_serialized_data(self.adoption, AdoptionSerializer)
        self.assertEqual(response.data, serialized_data)

    def test_request_post_adoption(self):
        """Teste de requisição POST para um adoption"""
        datas = {"pet": self.pet.pk, "tutor": self.tutor.pk}

        response = self.client.post(self.url, datas)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_check_shelter_can_post_adoption(self):
        """Teste para verificar se um abrigo consegue realizar uma adoção"""
        datas = {"pet": self.pet.pk, "tutor": self.tutor.pk}

        self.client.force_authenticate(user=self.user_shelter)
        response = self.client.post(self.url, datas)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_request_delete_adoption(self):
        """Teste de requisição DELETE para um adoption"""
        response = self.client.delete(f"{self.url}{self.adoption.pk}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_check_shelter_can_delete_adoption(self):
        """Teste para verificar se um abrigo consegue deletar uma adoção"""
        self.client.force_authenticate(user=self.user_shelter)
        response = self.client.delete(f"{self.url}{self.adoption.pk}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_put_adoption(self):
        """Teste de requisição PUT para um adoption"""
        datas = {"pet": self.pet.pk, "tutor": self.tutor.pk}

        response = self.client.put(f"{self.url}{self.adoption.pk}/", datas)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_check_shelter_can_put_pet(self):
        """Teste para verificar se um abrigo consegue alterar uma adoção"""
        datas = {"pet": self.pet.pk, "tutor": self.tutor.pk}

        self.client.force_authenticate(user=self.user_shelter)
        response = self.client.put(f"{self.url}{self.adoption.pk}/", datas)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

from rest_framework.test import APITestCase
from adopet.models import Tutor
from django.core.cache import cache


class APIBaseTestCase(APITestCase):
    fixtures = ["prototype_db", "prototype_users_db"]

    def setUp(self):
        self.user = Tutor.objects.create(
            email="", name="Admin", password="admin"
        )
        self.client.force_authenticate(user=self.user)
        cache.clear()

    def get_serialized_data(self, obj, serializer_class):
        serializer = serializer_class(obj)
        return serializer.data

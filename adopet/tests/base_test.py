from rest_framework.test import APITestCase
from django.contrib.auth.models import User 
from adopet.models import Tutor, Shelter, Pet, Adoption
import datetime

class APIBaseTestCase(APITestCase):
    datas_tutor = Tutor.objects
    
    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='admin')
        self.client.force_authenticate(user=self.user)
        
    def get_serialized_data(self, instace: object, serializer_class):
        return serializer_class(instance=instace).data

    def create_tutor(self, name='Teste tutor Um', email='tutor@test.com', password='12345678'):
        return Tutor.objects.create(name=name, email=email, password=password)
    
    def create_shelter(self, name='Teste Shelter Um'):
        return Shelter.objects.create(name=name)

    def create_pet(self, name='Pet teste', shelter=None):
        if shelter is None:
            shelter = self.create_shelter()
        return Pet.objects.create(
            name=name,
            age='1 ano',
            size='pequeno',
            description='Agradavel e alegre',
            address='Rio de Janeiro (RJ)',
            adopted=False,
            image='https://example.com/image.jpg',
            shelter=shelter
        )

    def create_adoption(self, tutor=None, pet=None):
        if tutor is None:
            tutor = self.create_tutor()
        if pet is None:
            pet = self.create_pet()
        return Adoption.objects.create(
            date=datetime.date.today(),
            pet=pet,
            tutor=tutor
        )
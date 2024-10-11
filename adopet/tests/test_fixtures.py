from django.test import TestCase
from adopet.models import Tutor, Shelter, Pet

class FixturesTesTCase(TestCase):
    fixtures = ['prototype_db']
    
    def test_load_fixtures(self):
        """Teste que verifica o carregamento das fixtures"""
        tutor = Tutor.objects.get(pk=1)
        shelter = Shelter.objects.get(pk=1)
        pet = Pet.objects.get(pk=3)
        self.assertEqual(tutor.password, '+zLtqAMCK2')
        self.assertEqual(shelter.name, 'Costa')
        self.assertEqual(pet.shelter, Shelter.objects.get(pk=3))
from django.test import TestCase
from adopet.models import Tutor, Shelter, Pet, Adoption
import datetime

class ModelTutorTestCase(TestCase):
    def setUp(self):
        self.tutor = Tutor.objects.create(
            name = 'Teste de Modelo Tutor',
            email = 'tutor@teste.com',
            password = '12345678'
        )
        self.shelter = Shelter.objects.create(
            name = 'Teste de Modelo Shelter',
        )
        self.pet = Pet.objects.create(
            name = 'Teste de Modelo Pet',
            age = '1 ano',
            size = 'SM',
            description = 'Adoravel e alegre',
            adopted = False,
            image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQktXg5_v8-L9AslphhrFvphE12SWkGl-_Jig&usqp=CAU',
            shelter = self.shelter
        )
        self.pet_adopted = Pet.objects.create(
            name = 'Teste de Modelo Pet que ira ser adotado',
            age = '1 ano',
            size = 'SM',
            description = 'Adoravel e alegre',
            adopted = False,
            image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQktXg5_v8-L9AslphhrFvphE12SWkGl-_Jig&usqp=CAU',
            shelter = self.shelter
        )
        self.adoption = Adoption.objects.create(
            data = datetime.date.today(),
            pet = self.pet_adopted,
            tutor = self.tutor
        )
    
    def test_check_tutor_attributes(self):
        """Teste que verifica os atributos do modelo de Tutor"""
        self.assertEqual(self.tutor.name, 'Teste de Modelo Tutor')
        self.assertEqual(self.tutor.email, 'tutor@teste.com')
        self.assertEqual(self.tutor.password, '12345678')
        
    def test_check_shelter_attributes(self):
        """Teste que verifica os atributos do modelo de Shelter"""
        self.assertEqual(self.shelter.name, 'Teste de Modelo Shelter')
        
    def test_check_pet_attributes(self):
        """Teste que verifica os atributos do modelo de Pet"""
        self.assertEqual(self.pet.name, 'Teste de Modelo Pet')
        self.assertEqual(self.pet.age, '1 ano')
        self.assertEqual(self.pet.size, 'SM')
        self.assertEqual(self.pet.description, 'Adoravel e alegre')
        self.assertEqual(self.pet.adopted, False)
        self.assertEqual(self.pet.image, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQktXg5_v8-L9AslphhrFvphE12SWkGl-_Jig&usqp=CAU')
        self.assertEqual(self.pet.shelter, self.shelter)
    
    def test_check_adoption_attributes(self):
        """Teste que verifica os atributos do modelo de Adoption"""
        self.assertEqual(self.adoption.data, datetime.date.today()),
        self.assertEqual(self.adoption.pet, self.pet_adopted),
        self.assertEqual(self.adoption.tutor, self.tutor),
        
        
from django.test import TestCase
from adopet.models import Tutor, Shelter, Pet, Adoption
from adopet.serializers import TutorSerializer, ShelterSerializer, PetSerializer, AdoptionSerializer

class SerializerTutorTestCase(TestCase):
    def setUp(self):
        self.tutor = Tutor(
            name = 'Teste de Modelo Tutor',
            email = 'tutor@teste.com',
            password = '12345678'
        )
        self.shelter = Shelter(
            name = 'Teste de Modelo Shelter',
        )
        self.pet = Pet(
            name = 'Teste de Modelo Pet',
            age = '1 ano',
            size = 'SM',
            description = 'Adoravel e alegre',
            adopted = False,
            image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQktXg5_v8-L9AslphhrFvphE12SWkGl-_Jig&usqp=CAU',
            shelter = self.shelter
        )
        self.adoption = Adoption(
            data = '2024-10-9',
            pet = self.pet,
            tutor = self.tutor
        )
        
        self.tutor_serializer = TutorSerializer(instance=self.tutor)
        self.shelter_serializer = ShelterSerializer(instance=self.shelter)
        self.pet_serializer = PetSerializer(instance=self.pet)
        self.adoption_serializer = AdoptionSerializer(instance=self.adoption)
        
    def test_check_serializers_fields_tutor(self):
        """Teste que verifica os campos que estão sendo serializados de tutor"""
        datas = self.tutor_serializer.data  
        self.assertEqual(set(datas.keys()), set([
            'id', 'name', 'email', 'password'   
        ]))
    def test_check_serializers_fields_content_tutor(self):
        """Teste que verifica o conteúdo dos campos que estão sendo serializados de tutor"""
        datas = self.tutor_serializer.data
        self.assertEqual(datas['name'], self.tutor.name)
        self.assertEqual(datas['email'], self.tutor.email)
        self.assertEqual(datas['password'], self.tutor.password)
        
    def test_check_serializers_fields_shelter(self):
        """Teste que verifica os campos que estão sendo serializados de shelter"""
        datas = self.shelter_serializer.data
        self.assertEqual(set(datas.keys()), set([
            'id', 'name'
        ]))
    def test_check_serializers_fields_content_shelter(self):
        """Teste que verifica o conteúdo dos campos que estão sendo serializados de shelter"""
        datas = self.shelter_serializer.data
        self.assertEqual(datas['name'], self.shelter.name)
        
    def test_check_serializers_fields_pet(self):
        """Teste que verifica os campos que estão sendo serializados de pet"""
        datas = self.pet_serializer.data
        self.assertEqual(set(datas.keys()), set([
            'id', 
            'name', 
            'age', 
            'size', 
            'description', 
            'address',
            'adopted',
            'image',
            'shelter' 
        ]))
    def test_check_serializers_fields_content_pet(self):
        """Teste que verifica o conteúdo dos campos que estão sendo serializados de pet"""
        datas = self.pet_serializer.data
        self.assertEqual(datas['name'], self.pet.name)
        self.assertEqual(datas['age'], self.pet.age)
        self.assertEqual(datas['size'], self.pet.size)
        self.assertEqual(datas['description'], self.pet.description)
        self.assertEqual(datas['address'], self.pet.address)
        self.assertEqual(datas['adopted'], self.pet.adopted)
        self.assertEqual(datas['image'], self.pet.image)
        self.assertEqual(datas['shelter'], self.pet.shelter.id)
        
    def test_check_serializers_fields_adoption(self):
        """Teste que verifica os campos que estão sendo serializados de adoption"""
        datas = self.adoption_serializer.data
        self.assertEqual(set(datas.keys()), set([
            'id', 'data', 'pet', 'tutor'
        ]))
    def test_check_serializers_fields_content_adoption(self):
        """Teste que verifica o conteúdo dos campos que estão sendo serializados de adoption"""
        datas = self.adoption_serializer.data
        self.assertEqual(datas['data'], self.adoption.data)
        self.assertEqual(datas['pet'], self.adoption.pet.id)
        self.assertEqual(datas['tutor'], self.adoption.tutor.id)
        
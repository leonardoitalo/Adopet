from rest_framework import serializers
from adopet.models import Tutor, Shelter, Pet

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ['id', 'name', 'email', 'password']

class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelter
        fields = ['name']
        
class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'
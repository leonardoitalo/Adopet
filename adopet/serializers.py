import re
from rest_framework import serializers
from adopet.models import Tutor, Shelter, Pet, Adoption
from .validators import invalid_name, invalid_age

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ['id', 'name', 'email', 'password']
    
    def validate(self, datas):
        if invalid_name(datas['name']):
            raise serializers.ValidationError({'name': 'O nome só pode conter letras'})

class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelter
        fields = ['id', 'name']
        
class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'
    
    def validate(self, datas): 
        if invalid_age(datas['age']):
            raise serializers.ValidationError(
                {'age': 'A idade deve estar no formato "X dias", "X meses" ou "X anos", onde X é um número.'}
            )

class AdoptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adoption
        fields = '__all__'
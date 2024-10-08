import re
from rest_framework import serializers
from adopet.models import Tutor, Shelter, Pet, Adoption

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ['id', 'name', 'email', 'password']
    
    def validate_name(self, name: str):
        if not name.isalpha():
            raise serializers.ValidationError('O nome só pode conter letras')

class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelter
        fields = ['id', 'name']
        
class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'
    
    def validate_age(self, age):
        pattern = r'^\d+\s+(dias|meses|anos)$'  
        if not re.match(pattern, age):
            raise serializers.ValidationError(
                'A idade deve estar no formato "X dias", "X meses" ou "X anos", onde X é um número.'
            )

class AdoptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adoption
        fields = '__all__'
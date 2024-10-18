from rest_framework import serializers
from adopet.models import Tutor, Shelter, Pet, Adoption
from .validators import invalid_name, invalid_age
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ["id", "name", "email", "password"]

    def validate(self, datas):
        if invalid_name(datas["name"]):
            raise serializers.ValidationError({"name": "O nome só pode conter letras"})
        return datas

    def create(self, validated_data):
        # Usa o TutorManager para criar o tutor com senha hashada
        return Tutor.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"],
        )


class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelter
        fields = ["id", "name"]


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = "__all__"

    def validate(self, datas):
        if invalid_age(datas["age"]):
            raise serializers.ValidationError(
                {
                    "age": 'A idade deve estar no formato "X dia(s)", "X mes(es)" ou "X ano(s)", onde X é um número.'
                }
            )
        return datas


class AdoptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adoption
        fields = "__all__"


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    # Substituímos o comportamento padrão
    def validate(self, attrs):
        # Remove a dependência do campo 'username' e usa 'email' para autenticação
        email = attrs.get("email")
        password = attrs.get("password")

        # Verifica se o tutor existe com o email fornecido
        if email and password:
            try:
                user = Tutor.objects.get(email=email)
            except Tutor.DoesNotExist:
                raise serializers.ValidationError(
                    {"error": "Usuário com esse email não encontrado."}
                )

            # Verifica se a senha está correta
            if not user.check_password(password):
                raise serializers.ValidationError({"detail": "Senha incorreta."})

            # Se passar, faz a autenticação padrão do JWT
            attrs["username"] = user.email
            return super().validate(attrs)
        else:
            raise serializers.ValidationError(
                {"error": "É necessário fornecer email e senha."}
            )

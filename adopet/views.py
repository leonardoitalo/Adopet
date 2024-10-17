from adopet.models import Tutor, Shelter, Pet, Adoption
from adopet.serializers import (
    TutorSerializer,
    ShelterSerializer,
    PetSerializer,
    AdoptionSerializer,
)
from rest_framework import viewsets, status, filters, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import ShelterPermissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer


class TutorsViewSet(viewsets.ModelViewSet):
    """View para listar os tutores"""

    queryset = Tutor.objects.all().order_by("id")
    serializer_class = TutorSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["name"]
    search_fields = ["name"]

    def list(self, request, *args, **kwargs):
        tutors = self.get_queryset()
        if not tutors.exists():
            return Response(
                {"detail": "No tutors found"}, status=status.HTTP_404_NOT_FOUND
            )

        return super().list(request, *args, **kwargs)


class RegisterTutorView(generics.CreateAPIView):
    """View para registrar novos tutores"""

    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer


class SheltersViewSet(viewsets.ModelViewSet):
    """View para listar os abrigos"""

    queryset = Shelter.objects.all().order_by("id")
    serializer_class = ShelterSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["name"]
    search_fields = ["name"]

    def list(self, request, *args, **kwargs):
        shelters = self.get_queryset()
        if not shelters.exists():
            return Response(
                {"detail": "No shelters found"}, status=status.HTTP_404_NOT_FOUND
            )

        return super().list(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        try:
            shelter = self.get_object()
            shelter.delete()
            return Response(
                {"detail": "Shelter deleted with success"}, status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {"detail": "Shelter not deleted"}, status=status.HTTP_400_BAD_REQUEST
            )


class PetsViewSet(viewsets.ModelViewSet):
    """
    View para listar pets

    Descrição do metodo POST:
    - pet: Somente um abrigo(shelter) pode criar uma pet
    """

    queryset = Pet.objects.filter(adopted=False).order_by("id")
    serializer_class = PetSerializer
    permission_classes = [ShelterPermissions, IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["name"]
    search_fields = ["name"]

    def list(self, request, *args, **kwargs):
        pets = self.get_queryset()
        if not pets.exists():
            return Response(
                {"detail": "No pets found"}, status=status.HTTP_404_NOT_FOUND
            )

        return super().list(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        try:
            pet = self.get_object()
            pet.delete()
            return Response(
                {"detail": "Pet deleted with success"}, status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {"detail": "Pet not deleted"}, status=status.HTTP_400_BAD_REQUEST
            )


class AdoptionsViewSet(viewsets.ModelViewSet):
    """
    View para listar as adoções
    """

    queryset = Adoption.objects.all().order_by("id")
    serializer_class = AdoptionSerializer
    permission_classes = [ShelterPermissions, IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["data"]
    search_fields = ["id"]

    def destroy(self, request, *args, **kwargs):
        """
        Descrição do metodo DELETE:
        - adoption: Somente um abrigo(shelter) pode deletar uma adoção(adoption)
        """
        try:
            adoption = self.get_object()
            adoption.delete()
            return Response(
                {"detail": "Adoption deleted with success"}, status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {"detail": "Pet not deleted"}, status=status.HTTP_400_BAD_REQUEST
            )


class CustomTokenObtainPairView(TokenObtainPairView):
    """View para obter um Token"""

    serializer_class = CustomTokenObtainPairSerializer

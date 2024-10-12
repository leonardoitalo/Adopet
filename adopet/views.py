from adopet.models import Tutor, Shelter, Pet, Adoption
from adopet.serializers import TutorSerializer, ShelterSerializer, PetSerializer, AdoptionSerializer
from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework import filters
from .permissions import ShelterPermissions
from django_filters.rest_framework import DjangoFilterBackend

class TutorsViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all().order_by('id')
    serializer_class = TutorSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name']
    
    def list(self, request, *args, **kwargs):
        tutors = self.get_queryset()
        if not tutors.exists():
            return Response({"detail": "No tutors found"}, status=status.HTTP_404_NOT_FOUND)

        return super().list(request, *args, **kwargs)
    
class SheltersViewSet(viewsets.ModelViewSet):
    queryset = Shelter.objects.all().order_by('id')
    serializer_class = ShelterSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name']
    
    def list(self, request, *args, **kwargs):
        shelters = self.get_queryset()
        if not shelters.exists():
            return Response({"detail": "No shelters found"}, status=status.HTTP_404_NOT_FOUND)

        return super().list(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        try:     
            shelter = self.get_object()
            shelter.delete()
            return Response({"detail": "Shelter deleted with success"}, status=status.HTTP_200_OK)
        except:
            return Response({'detail': "Shelter not deleted"}, status=status.HTTP_400_BAD_REQUEST)

class PetsViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.filter(adopted=False).order_by('id')
    serializer_class = PetSerializer
    permission_classes = [ShelterPermissions]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name']

    def list(self, request, *args, **kwargs):
        pets = self.get_queryset()
        if not pets.exists():
            return Response({"detail": "No pets found"}, status=status.HTTP_404_NOT_FOUND)

        return super().list(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        try:     
            pet = self.get_object()
            pet.delete()
            return Response({"detail": "Pet deleted with success"}, status=status.HTTP_200_OK)
        except:
            return Response({'detail': "Pet not deleted"}, status=status.HTTP_400_BAD_REQUEST)

class AdoptionsViewSet(viewsets.ModelViewSet):
    queryset = Adoption.objects.all().order_by('id')
    serializer_class = AdoptionSerializer
    permission_classes = [ShelterPermissions]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['data']
    search_fields = ['id']
    
    def destroy(self, request, *args, **kwargs):
        try:     
            adoption = self.get_object()
            adoption.delete()
            return Response({"detail": "Adoption deleted with success"}, status=status.HTTP_200_OK)
        except:
            return Response({'detail': "Pet not deleted"}, status=status.HTTP_400_BAD_REQUEST)
        
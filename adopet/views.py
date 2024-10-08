from adopet.models import Tutor, Shelter, Pet, Adoption
from adopet.serializers import TutorSerializer, ShelterSerializer, PetSerializer, AdoptionSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from .permissions import IsShelterAndCanDeleteAdoption

class TutorsViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
    
class SheltersViewSet(viewsets.ModelViewSet):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer
    
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
    queryset = Pet.objects.filter(adopted=False)
    serializer_class = PetSerializer

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
    queryset = Adoption.objects.all()
    serializer_class = AdoptionSerializer
    permission_classes = [IsShelterAndCanDeleteAdoption]
    
    def destroy(self, request, *args, **kwargs):
        try:     
            adoption = self.get_object()
            adoption.delete()
            return Response({"detail": "Adoption deleted with success"}, status=status.HTTP_200_OK)
        except:
            return Response({'detail': "Pet not deleted"}, status=status.HTTP_400_BAD_REQUEST)
        
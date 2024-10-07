from adopet.models import Tutor
from adopet.serializers import TutorSerializer
from rest_framework import viewsets

class TutorsViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer

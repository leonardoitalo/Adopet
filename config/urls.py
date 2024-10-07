from django.contrib import admin
from django.urls import path, include
from adopet.views import TutorsViewSet, SheltersViewSet, PetsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tutors', TutorsViewSet, basename='Tutors')
router.register('shelters', SheltersViewSet, basename='Shelters')
router.register('pets', PetsViewSet, basename='Pets')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

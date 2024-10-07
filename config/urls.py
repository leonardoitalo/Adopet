from django.contrib import admin
from django.urls import path, include
from adopet.views import TutorsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tutors', TutorsViewSet, basename='Tutors')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

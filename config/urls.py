from django.contrib import admin
from django.urls import path, include
from adopet.views import TutorsViewSet, SheltersViewSet, PetsViewSet, AdoptionsViewSet, CustomTokenObtainPairView, RegisterTutorView
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

router = routers.DefaultRouter()
router.register('tutors', TutorsViewSet, basename='Tutors')
router.register('shelters', SheltersViewSet, basename='Shelters')
router.register('pets', PetsViewSet, basename='Pets')
router.register('adoptions', AdoptionsViewSet, basename='Adoptions')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterTutorView.as_view(), name='register_tutor'),  # Rota de registro de tutor
]

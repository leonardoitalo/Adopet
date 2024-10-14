from django.contrib import admin
from django.urls import path, include
from adopet.views import (
    TutorsViewSet,
    SheltersViewSet,
    PetsViewSet,
    AdoptionsViewSet,
    CustomTokenObtainPairView,
    RegisterTutorView,
)
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Documentação da API",
        default_version="v1",
        description="Documentação da API Adopet",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

router = routers.DefaultRouter()
router.register("tutors", TutorsViewSet, basename="Tutors")
router.register("shelters", SheltersViewSet, basename="Shelters")
router.register("pets", PetsViewSet, basename="Pets")
router.register("adoptions", AdoptionsViewSet, basename="Adoptions")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
    path("api/token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/register/", RegisterTutorView.as_view(), name="register_tutor"),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

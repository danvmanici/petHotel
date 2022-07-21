from django.urls import include, path

# from . import views
from .views import (
    SpeciesViewSet,
    TreatViewSet,
    OwnerViewSet,
    PetViewSet,
    PetTreatViewSet,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("owners", OwnerViewSet, basename="owners")
router.register("species", SpeciesViewSet, basename="species")
router.register("pets", PetViewSet, basename="pets")
router.register("treats", TreatViewSet, basename="treats")
router.register("pet-treats", PetTreatViewSet, basename="pet-treats")

urlpatterns = [
    path("", include(router.urls)),
]

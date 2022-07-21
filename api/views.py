from .serializers import (
    SpeciesSerializer,
    TreatSerializer,
    OwnerSerializer,
    OwnerFullNameSerializer,
    PetSerializer,
    PetTreatSerializer,
)
from .models import Owner, PetTreat, Species, Pet, Treat
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render, HttpResponse


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["id", "last_name"]
    search_fields = ["^last_name"]
    ordering = ["last_name"]

    @action(detail=False)
    def cat(self, request):
        return HttpResponse("We love cats!")

    @action(detail=False)
    def fullname(self, request):
        full_name = Owner.objects.raw("SELECT id, first_name, last_name FROM api_owner")
        serializer = OwnerFullNameSerializer(full_name, many=True)
        return Response(serializer.data)


class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["id", "name"]
    search_fields = ["=name"]

    @action(detail=False)
    def funNames(self, request):
        pets = Pet.objects.get_fun_names()
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data)


class TreatViewSet(viewsets.ModelViewSet):
    queryset = Treat.objects.all()
    serializer_class = TreatSerializer


class PetTreatViewSet(viewsets.ModelViewSet):
    queryset = PetTreat.objects.all()
    serializer_class = PetTreatSerializer

from dataclasses import fields
from rest_framework import serializers
from .models import Owner, Species, Pet, Treat, PetTreat


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = "__all__"

    # fa un serializer in care implementezi creat-ul


class OwnerFullNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ["id", "first_name", "last_name"]


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = "__all__"


class PetSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(read_only=True)
    species = SpeciesSerializer(read_only=True)

    class Meta:
        model = Pet
        fields = ["name", "birth_date", "owner", "species"]


class TreatSerializer(serializers.ModelSerializer):
    pet_treats = PetSerializer(read_only=True, many=True)

    class Meta:
        model = Treat
        fields = "__all__"


class PetTreatSerializer(serializers.ModelSerializer):
    pet = PetSerializer(read_only=True)
    treat = TreatSerializer(read_only=True)

    class Meta:
        model = PetTreat
        fields = "__all__"

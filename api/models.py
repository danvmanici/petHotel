from enum import unique
from django.db import models
from django.forms import ValidationError
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.core.validators import MinLengthValidator


def validate_pretty_name(pretty_name):
    lowerCaseName = pretty_name.lower()
    if lowerCaseName == "bob":
        raise ValidationError("Your pet name isn't pretty!")


class Owner(models.Model):
    first_name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mobile = PhoneNumberField(null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True, unique=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Species(models.Model):
    CAT = "CAT"
    DOG = "DOG"
    EXOTIC = "EXO"
    AVAILABLE_SPECIES = [(CAT, "Cat"), (DOG, "Dog"), (EXOTIC, "Exotic")]
    species_name = models.CharField(
        max_length=3, choices=AVAILABLE_SPECIES, default=CAT, unique=True
    )

    def __str__(self):
        return self.species_name


class PetManager(models.Manager):
    def get_fun_names(self):
        return self.filter(name__contains="rory")


class Pet(models.Model):
    name = models.CharField(max_length=100, validators=[validate_pretty_name])
    birth_date = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    species = models.ForeignKey(
        Species, on_delete=models.SET_NULL, null=True, related_name="pets"
    )
    objects = PetManager()

    class Meta:
        unique_together = ("name", "birth_date")
        constraints = [
            models.CheckConstraint(
                check=models.Q(birth_date__lte=timezone.now()), name="birth_date_lte"
            ),
        ]

    def __str__(self):
        return self.name


class Treat(models.Model):
    name = models.CharField(max_length=100, unique=True)
    pet_treats = models.ManyToManyField(
        Pet, through="PetTreat", through_fields=("treat", "pet")
    )  # first element of tuple is the foreign_key of table PetTreat to the table where many_to_many relationship is defined

    def __str__(self):
        return self.name


class PetTreat(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    treat = models.ForeignKey(Treat, on_delete=models.CASCADE)
    db_table = "pet_treat"

    def __str__(self):
        return " pet + treat"

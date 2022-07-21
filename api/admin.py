from django.contrib import admin

from . import models


@admin.register(models.Pet)
class PetModel(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(models.Owner)
class OwnerModel(admin.ModelAdmin):
    list_display = ("last_name",)


@admin.register(models.PetTreat)
class OwnerModel(admin.ModelAdmin):
    pass


@admin.register(models.Treat)
class OwnerModel(admin.ModelAdmin):
    pass

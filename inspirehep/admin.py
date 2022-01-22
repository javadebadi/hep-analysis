from atexit import register
from operator import mod
from django.contrib import admin
from .models import (
    Country,
)
# Register your models here.

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    model = Country
    list_display = ('id', 'name', 'iso2', 'iso3')
    search_fields = ('name', 'iso2', 'iso3') 
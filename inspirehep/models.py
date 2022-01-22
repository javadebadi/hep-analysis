from tabnanny import verbose
from django.db import models

# Create your models here.
class Country(models.Model):
    """
    Django Model for Countries.

    Attributes:
        name (models.CharField): name of the country.
        iso2 (models.CharField): two letters codes of the country.
        iso3 (models.CharField): three letters codes of the country.
    """

    name = models.CharField(
        max_length=64,
    )

    iso2 = models.CharField(
        max_length=2,
        unique=True,
    )

    iso3 = models.CharField(
        max_length=3,
        unique=True,
    )

    def __str__(self) -> str:
        return self.name
    class Meta:
        db_table = 'country'
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        ordering = ('name',)
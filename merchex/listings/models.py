from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Band(models.Model):
    global Genre

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2022)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)


class Listings(models.Model):
    class ListingType(models.TextChoices):
        RECORDS = "R"
        CLOTHING = "C"
        POSTERS = "P"
        MISC = "M"

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=True)
    year = models.fields.IntegerField(
        null=True,
        validators=[MinValueValidator(1900), MaxValueValidator(2022)]
    )
    type = models.fields.CharField(max_length=5, choices=ListingType.choices)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    like_new = models.fields.BooleanField(default=True)



from email.policy import default
from pyexpat import model
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
# https://docs.djangoproject.com/fr/3.2/ref/validators/

class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP='HH'
        SYNTH_POP='SP'
        ALTERNATIVE='AR'
    name= models.fields.CharField(max_length=100)
    genre= models.fields.CharField(default="",choices=Genre.choices,max_length=5)
    biography= models.fields.CharField(default="",max_length=1000)
    year_formed= models.fields.IntegerField(default=2022,
        validators=[MinValueValidator(1900),MaxValueValidator(2022)])
    active= models.fields.BooleanField(default=True)
    official_homepage= models.fields.URLField(default="",null=True,blank=True)
    #like_new= models.fields.BooleanField(default=False)
    def __str__(self):
        return f'{self.name}'


class Titre(models.Model):
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    titre= models.fields.CharField(max_length=100)
    year_created= models.fields.IntegerField(default=2022,
        validators=[MinValueValidator(1900),MaxValueValidator(2022)])
    def __str__(self):
        return f'{self.titre}'

class releve_Ville(models.Model):
    data= models.JSONField()

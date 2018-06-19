from django.db import models
from colorfield.fields import ColorField
from datetime import datetime
import geocoder
import json


class Entry(models.Model):

    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    published_date = models.DateTimeField(blank=True, null=True)
    adresse =  models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    published_date = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    Sante = models.BooleanField(default=False)
    Environnement = models.BooleanField(default=False)
    Travail = models.BooleanField(default=False)
    Solidarite = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def geo_address(self):
        g = geocoder.google(self.adresse)
        g = g.json
        latlng = g.LatLng
        return latlng





class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=35)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.name

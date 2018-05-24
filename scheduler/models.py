from django.db import models
from colorfield.fields import ColorField
import datetime 



class Entry(models.Model):

    name = models.CharField(max_length=30)
    date_start = models.DateTimeField(default=datetime.datetime.now())
    date_end = models.DateTimeField(default=datetime.datetime.now())
    description = models.TextField()
    address = models.TextField(default='')
    inscription = models.TextField(default='')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    Theme = models.ForeignKey('Theme', on_delete=models.CASCADE)
    #Sante = models.BooleanField(default=False)
    #Environnement = models.BooleanField(default=False)
    #Travail = models.BooleanField(default=False)
    #Solidarite = models.BooleanField(default=False)
 

    def __str__(self):
        return f'{self.name} {self.date_start}'



class Category(models.Model):
    class Meta:
       verbose_name_plural = 'categories'

    name = models.CharField(max_length=35)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.name


class Theme(models.Model):
    class Meta:
       verbose_name_plural = 'thematiques'

    name = models.CharField(max_length=35)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.name


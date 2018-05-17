from django.db import models
from colorfield.fields import ColorField



class Entry(models.Model):

    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=35)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.name

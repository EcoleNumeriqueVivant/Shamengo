from django.db import models
from django.utils import timezone

class Entry(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

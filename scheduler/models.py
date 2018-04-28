from django.db import models

class Entry(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.DateTimeField(auto_now_add=True)
    

from django.db import models

class Entry(models.Model):
	name = models.CharField(max_length=100)
	date = models.DateTimeField()
	description = models.TextField()
	
	def __str__(self):
		return f'{self.name} {self.date}'

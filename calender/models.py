from django.db import models

class Entry(models.Model):
	name = models.CharField(max_length=20)
	date = models.DateTimeField()
	description = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	Sante = models.BooleanField(default=False)
	Environnement = models.BooleanField(default=False)
	Travail = models.BooleanField(default=False)
	Solidarite = models.BooleanField(default=False)
	
	def __str__(self):
		return f'{self.name} {self.date}'



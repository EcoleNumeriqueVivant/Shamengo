from django.db import models


class Entry(models.Model):

    CATEGORY = (
        ("A", "atelier"),
        ("Co", "cocktail"),
        ("C", "conference"),
        ("E", "evenement"),
        ("M", "meetup"),
        ("P", "projection"),
        ("R", "reunion"),
    )
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField()
    category = models.CharField(max_length=2 , choices=CATEGORY)
    created = models.DateTimeField(auto_now_add=True)

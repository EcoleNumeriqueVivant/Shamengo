# Generated by Django 2.0.4 on 2018-05-08 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='category',
            field=models.CharField(choices=[('A', 'atelier'), ('Co', 'cocktail'), ('C', 'conference'), ('E', 'evenement'), ('M', 'meetup'), ('P', 'projection'), ('R', 'reunion')], max_length=2),
        ),
    ]

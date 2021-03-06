# Generated by Django 3.2.3 on 2021-06-09 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaceManager', '0007_alter_astronauta_genere'),
    ]

    operations = [
        migrations.AlterField(
            model_name='astronauta',
            name='genere',
            field=models.CharField(choices=[('H', 'Home'), ('D', 'Dona'), ('?', 'Altre')], max_length=1),
        ),
        migrations.AlterField(
            model_name='astronauta',
            name='grup_sanguini',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=3),
        ),
    ]

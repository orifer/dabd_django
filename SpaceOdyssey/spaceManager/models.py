# https://docs.djangoproject.com/en/3.2/topics/db/models/

from django.db import models
from django.utils import timezone


class Agencia(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Missio(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    descripcio = models.CharField(max_length=200)
    data_finalitzacio = models.DateTimeField(default=timezone.now)
    agencia = models.ForeignKey(Agencia, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nom


class Nau(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    capacitat = models.IntegerField()
    agencia = models.ForeignKey(Agencia, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nom

from django.db import models

class Agencia(models.Model):
    nom = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.nom

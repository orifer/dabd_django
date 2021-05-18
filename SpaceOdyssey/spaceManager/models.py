from django.db import models

class Agencia(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=200)

    def __str__(self):
        return self.nom

from django.db import models

# Create your models here.
class State(models.Model):
    unidadeFederativa = models.CharField(max_length=60)
    abreviacao = models.CharField(max_length=2)
    capital = models.CharField(max_length=60)
    area = models.DecimalField(max_digits=19, decimal_places=2)
    populacao = models.BigIntegerField()
    pib = models.BigIntegerField()

    def __str__(self):
        return self.unidadeFederativa

from django.db import models


class Endereco(models.Model):
    logradouro = models.CharField(max_length=150)
    complemento = models.CharField(max_length=150, null=True, blank=True)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        endereco = self.logradouro
        if self.complemento:
            endereco += ', {}'.format(self.complemento)
        endereco += ', {}, {}, {}'.format(self.cidade, self.estado, self.pais)

        return endereco

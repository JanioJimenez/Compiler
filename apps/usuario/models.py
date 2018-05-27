from django.db import models

from django.contrib.auth.models import User


class Usuario(models.Model):

    usuario  = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    edad     = models.IntegerField()
    ciudad   = models.CharField(max_length = 70)

    pais     = models.CharField(max_length = 70)
    lenguaje = models.CharField(max_length = 70)

    def __str__(self):
        return '{} {}'.format(self.ciudad, self.pais)
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

class Concentra(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    naoh = models.FloatField()
    T20 = models.FloatField()
    T30 = models.FloatField()

    def __str__(self):
        return str(self.naoh)

class Consulta(models.Model):

    temp = (
        ('20ºC', '20ºC'),
        ('30ºC', '30ºC'),
        ('40ºC', '40ºC'),
        ('50ºC', '50ºC'),
        ('60ºC', '60ºC'),
        ('70ºC', '70ºC'),
        ('80ºC', '80ºC'),
        ('90ºC', '90ºC'),
        ('100ºC', '100ºC'),
        ('110ºC', '110ºC'),
    )
    concentra = models.FloatField(default=0)
    temperatura = models.CharField(max_length=5, choices=temp)
    densidade = models.FloatField()
    fator = models.FloatField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default= 0)
    created = models.DateTimeField(auto_now_add=True)


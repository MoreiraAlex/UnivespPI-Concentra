from django.db import models
from django.contrib.auth.models import User

class Consulta(models.Model):

    temp = (
        ('20', '20ºC'),
        ('30', '30ºC'),
        ('40', '40ºC'),
        ('50', '50ºC'),
        ('60', '60ºC'),
        ('70', '70ºC'),
        ('80', '80ºC'),
        ('90', '90ºC'),
        ('100', '100ºC'),
        ('110', '110ºC'),
    )
    concentra = models.FloatField(default=0)
    temperatura = models.CharField(max_length=5, choices=temp)
    densidade = models.FloatField()
    fator = models.FloatField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default= 0)
    created = models.DateTimeField(auto_now_add=True)


from django.db import models
from django.contrib.auth.models import User

class Consulta(models.Model):
    temp = (
        ('20', '20ºC'),('22', '22ºC'),('24', '24ºC'),('26', '26ºC'),('28', '28ºC'),
        ('30', '30ºC'),('32', '32ºC'),('34', '34ºC'),('36', '36ºC'),('38', '38ºC'),
        ('40', '40ºC'),('42', '42ºC'),('44', '44ºC'),('46', '46ºC'),('48', '48ºC'),
        ('50', '50ºC'),('52', '52ºC'),('54', '54ºC'),('56', '56ºC'),('58', '58ºC'),
        ('60', '60ºC'),('62', '62ºC'),('64', '64ºC'),('66', '66ºC'),('68', '68ºC'),
        ('70', '70ºC'),('72', '72ºC'),('74', '74ºC'),('76', '76ºC'),('78', '78ºC'),
        ('80', '80ºC'),('82', '82ºC'),('84', '84ºC'),('86', '86ºC'),('88', '88ºC'),
        ('90', '90ºC'),('92', '92ºC'),('94', '94ºC'),('96', '96ºC'),('98', '98ºC'),
        ('100', '100ºC'),('102', '102ºC'),('104', '104ºC'),
        ('106', '106ºC'),('108', '108ºC'),('110', '110ºC'),
    )
    concentra = models.FloatField()
    temperatura = models.CharField(max_length=5, choices=temp)
    densidade = models.FloatField()
    fator = models.FloatField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


# Generated by Django 3.2.9 on 2021-12-01 22:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='teste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concentra', models.FloatField()),
                ('temperatura', models.CharField(choices=[('20', '20ºC'), ('22', '22ºC'), ('30', '30ºC'), ('40', '40ºC'), ('50', '50ºC'), ('60', '60ºC'), ('70', '70ºC'), ('80', '80ºC'), ('90', '90ºC'), ('100', '100ºC'), ('110', '110ºC')], max_length=5)),
                ('densidade', models.FloatField()),
                ('fator', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

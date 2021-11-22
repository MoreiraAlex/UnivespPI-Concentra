from django.shortcuts import render
from .models import Consulta

def consulta(request):
    consultas = Consulta.objects.all()
    return render(request, 'base.html', {'consultas': consultas})


def historico(request):
    return render(request, 'concentra/historico.html')

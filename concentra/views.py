from django.shortcuts import render

def consulta(request):
    return render(request, 'concentra/consulta.html')

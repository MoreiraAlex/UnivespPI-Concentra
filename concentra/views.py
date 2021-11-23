from django.shortcuts import get_object_or_404, redirect, render
from .models import Consulta
from .forms import ConsultaForm

def consulta(request):    
    if request.method == 'POST':
        form = ConsultaForm(request.POST)

        if form.is_valid():
            consulta = form.save(commit=False)
            consulta.densidade = consulta.densidade + consulta.fator
            consulta.concentra = 1
            consulta.save()
            return redirect('/')
        else:
            print('Consulta nao foi registrada')
            return redirect('/')
            
    else:
        consultas = Consulta.objects.all().order_by('-created')
        form = ConsultaForm()
        return render(request, 'base.html', {'consultas': consultas, 'form': form})


def editConsulta(request, id):
    consultaEdit = get_object_or_404(Consulta, pk=id)
    form = ConsultaForm(instance=consultaEdit)

    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consultaEdit)

        if form.is_valid():
            consultaEdit = form.save(commit=False)
            consultaEdit.densidade = consultaEdit.densidade + consultaEdit.fator
            consultaEdit.concentra = 1
            consultaEdit.save()
            return redirect('/')
        else:
            print('Consulta nao foi editada')
            return redirect('/')

    else:
        return redirect('/', {'form': form, 'consultaEdit':consultaEdit})
    
    

def deleteConsulta(request, id):
    consulta = get_object_or_404(Consulta, pk=id)
    consulta.delete()
    return redirect('/')
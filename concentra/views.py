from django.shortcuts import get_object_or_404, redirect, render
from .models import Consulta
from .forms import ConsultaForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def consulta(request):    
    if request.method == 'POST':
        form = ConsultaForm(request.POST)

        if form.is_valid():
            consulta = form.save(commit=False)
            consulta.densidade = consulta.densidade + consulta.fator
            consulta.concentra = 1
            consulta.save()
            messages.info(request, 'Aferição de numero ' + str(consulta.id) + ' registrada.')
            return redirect('/')
        else:
            messages.info(request, 'Aferição nao foi registrada!')
            return redirect('/')
            
    else:
        consulta_list = Consulta.objects.all().order_by('-created')

        paginator = Paginator(consulta_list, 4)
        page = request.GET.get('page')
        consultas = paginator.get_page(page)

        form = ConsultaForm()
        return render(request, 'index.html', {'consultas': consultas, 'form': form})

@login_required
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
            messages.info(request, 'Aferição de numero ' + str(consulta.id) + ' editada com sucesso.')
            return redirect('/')
        else:
            messages.info(request, 'Aferição nao foi editada!')
            return redirect('/')

    else:
        return redirect('/', {'form': form, 'consultaEdit':consultaEdit})
    
    
@login_required
def deleteConsulta(request, id):
    consulta = get_object_or_404(Consulta, pk=id)
    consulta.delete()

    messages.info(request, 'Aferição deletada com sucesso.')

    return redirect('/')
from django.shortcuts import get_object_or_404, redirect, render
from .models import Consulta
from .forms import ConsultaForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
import pandas as pd
import numpy as np

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


def consulta(request): 
    dados = pd.read_csv('tb.xlsx') 
    if request.method == 'POST':
        form = ConsultaForm(request.POST)

        if form.is_valid():
            consulta = form.save(commit=False)
            consulta.author = request.user
            consulta.densidade = consulta.densidade + consulta.fator
            linha = concent(consulta.temperatura, consulta.densidade)
            consulta.concentra = dados.loc[linha, 'NaOH']
            print(consulta.concentra)
            consulta.save()
            messages.info(request, 'Aferição de numero ' + str(consulta.id) + ' registrada.')
            return redirect('/')
        else:
            messages.info(request, 'Aferição nao foi registrada!')
            return redirect('/')
            
    else:
        consulta_list = Consulta.objects.all().order_by('-created')

        paginator = Paginator(consulta_list, 5)
        page = request.GET.get('page')
        consultas = paginator.get_page(page)

        form = ConsultaForm()
        return render(request, 'index.html', {'consultas': consultas, 'form': form}) 


@login_required
def deleteConsulta(request, id):
    consulta = get_object_or_404(Consulta, pk=id)
    consulta.delete()

    messages.info(request, 'Aferição deletada com sucesso.')

    return redirect('/')


def about(request):
    return render(request,'about.html')


def concent(temperatura, densidade):
    tb = pd.read_csv('tb.xlsx')  

    concentra = tb[temperatura]
    resultado = getnearpos(concentra, densidade)
    return resultado


def getnearpos(array, value):
    idx = (np.abs(array-value)).idxmin()
    return idx

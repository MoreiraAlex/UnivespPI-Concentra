from django import forms
from django.forms import fields
from .models import Consulta

class ConsultaForm(forms.ModelForm):

    class Meta:
        model = Consulta
        fields = ('temperatura', 'densidade', 'fator')
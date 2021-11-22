from django.urls import path
from . import views

urlpatterns = [
    path('', views.consulta, name='consulta'),
    path('historico', views.historico, name='historico')
]

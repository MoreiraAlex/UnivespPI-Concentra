from django.urls import path
from . import views

urlpatterns = [
    path('/', views.consulta, name='consulta'),
    path('edit/<int:id>', views.editConsulta, name='edit-consulta'),
    path('delete/<int:id>', views.deleteConsulta, name='delete-consulta'),
]

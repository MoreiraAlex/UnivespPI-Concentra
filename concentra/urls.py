from django.urls import path
from django.urls.conf import include, include
from . import views

urlpatterns = [
    path('', views.consulta, name='consulta'),
    path('edit/<int:id>', views.editConsulta, name='edit-consulta'),
    path('delete/<int:id>', views.deleteConsulta, name='delete-consulta'),
    path('accounts/', views.SignUp.as_view(), name='registro'),
    path('accounts/', include('django.contrib.auth.urls')),    
]

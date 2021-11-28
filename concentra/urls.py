from django.urls import path
from django.urls.conf import include, include
from . import views

urlpatterns = [
    path('', views.consulta, name='consulta'),
    path('delete/<int:id>', views.deleteConsulta, name='delete-consulta'),
    path('accounts/', views.SignUp.as_view(), name='registro'),
    path('accounts/', include('django.contrib.auth.urls')),  
    path('about', views.about, name='about'),  
]

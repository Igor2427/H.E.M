"""HEM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appHEM import views

urlpatterns = [
    path('', views.login, name="login"),
    path('esqueceu-senha/', views.esqueceu_senha, name="esqueceu_senha"),
    path('pre-registro/', views.pre_registro, name="pre_registro"),
    path('registro-paciente/', views.registro_paciente, name="registro_paciente"),
    path('registro-medic/', views.registro_medico, name="registro_medico"),
    path('home-medico/', views.home_medico, name='home_medico'),
    path('admin/',admin.site.urls)
]

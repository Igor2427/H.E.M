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
    path('registro-medico/', views.registro_medico, name="registro_medico"),
    path('home-medico/', views.home_medico, name='home_medico'),
    path('home-paciente/', views.medicos, name='home_paciente'),
    path('registro-med/', views.registro_med, name='registro_med'),
    path('registro-pac/', views.registro_pac, name='registro_pac'),
    path('perfil-medico/', views.dados_med, name='perfil_medico'),
    path('edit-medico/', views.edit_medico, name='edit_medico'),
    path('perfil-paciente/', views.dados_pac, name='perfil_paciente'),
    path('edit-paciente/', views.edit_paciente, name='edit_paciente'),
    path('mensagens-paciente/', views.mensagens_pac, name='mensagens_paciente'),
    path('mensagens-medico/', views.mensagens_med, name='mensagens_medico'),
    path('chats-paciente/', views.chats_pac, name='chats_paciente'),
    path('chats-medico/', views.chats_med, name='chats_medico'),
    path('login/', views.login, name="login"),
    path('admin/',admin.site.urls),
]

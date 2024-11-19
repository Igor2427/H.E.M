from django.shortcuts import render, redirect
from .models import Medico, Paciente
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def login(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')

        if Medico.objects.filter(cpf=cpf, senha=senha).first():
            return redirect('home_medico')
        elif Paciente.objects.filter(cpf=cpf, senha=senha).first():
            return redirect('home_paciente')
        else:
            messages.error(request, 'Usuário não encontrado ou senha incorreta!')
            return render(request, 'login.html')
    return render(request, 'login.html')

def esqueceu_senha(request):
    return render(request, 'esqueceu_senha.html')

def pre_registro(request):
    return render(request, 'pre_registro.html')

def registro_paciente(request):
    return render(request, 'registro_paciente.html')

def registro_medico(request):
    return render(request, 'registro_medico.html')

def home_medico(request):
    return render(request, 'home_medico.html')

def registro_med(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        crm = request.POST.get('crm')
        especialidade = request.POST.get('especialidade')

        medico = Medico(cpf=cpf, email=email, nome=nome, senha=senha, crm=crm, especialidade=especialidade)
        medico.save()

        return redirect('login')
    return render(request, 'registro_paciente.html')

def registro_pac(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        

        paciente = Paciente(cpf=cpf, email=email, nome=nome, senha=senha)
        paciente.save()

        return redirect('login')
    return render(request, 'registro_paciente.html')

def medicos(request):
    medicos = Medico.objects.all().values()
    if request.method=='GET' and request.GET.get('opcoes') != None:
        esp = request.GET.get('opcoes')
        if esp != '':
            medicos = Medico.objects.filter(especialidade=esp).values()
    elif  request.method=='GET' and request.GET.get('busca') != None:
        nom = request.GET.get('busca')
        if nom != '':
            medicos = Medico.objects.filter(nome__icontains=nom).values()        
    template = loader.get_template('home_paciente.html')
    context = {
        'medicos': medicos,
    }
    return HttpResponse(template.render(context, request))

def dados_pac(request):
    cpf_logged = request.session.get('cpf_logged')
    pac = Paciente.objects.get(cpf=cpf_logged)
    print(pac)
    template = loader.get_template('perfil_paciente.html')
    context = {
        'pac': pac,
    }
    return HttpResponse(template.render(context, request))

def dados_med(request):
    # pegando os dados para por no perfil
    cpf_logged = request.session.get('cpf_logged')
    med = Medico.objects.get(cpf=cpf_logged)
    template = loader.get_template('perfil_medico.html')
    context = {
        'med': med,
    }
    # dando update na descricao
    if request.method=='POST':        
        descri = request.POST.get('desc')
        med.descricao = descri
        med.save()
        
    return HttpResponse(template.render(context, request))


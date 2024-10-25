from django.shortcuts import render, redirect
from .models import Medico, Paciente

# Create your views here.
def login(request):
    if request.method == 'POST':
        cpf = request.POST['cpf']

        if Medico.objects.filter(cpf=cpf).exists():
            return redirect('home_medico')
        elif Paciente.objects.filter(cpf=cpf).exists():
            return redirect('home_paciente')
        else:
            return render(request, 'login.html', {'erro': 'Usuário não encontrado!'})
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

def registro(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if 'paciente' in request.POST:
            paciente = Paciente()
            paciente = Paciente(cpf=cpf, nome=nome, email=email, senha=senha)
            paciente.save()
        
        elif 'medico' in request.POST:
            medico = Medico()
            especialidade = request.POST.get('especialidade')
            crm = request.POST.get('crm')
            medico = Medico(cpf=cpf, nome=nome, email=email, especialidade=especialidade, crm=crm, senha=senha)
            medico.save()


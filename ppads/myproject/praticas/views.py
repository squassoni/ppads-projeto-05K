from django.shortcuts import render, redirect

from .forms import NewPacienteForm
from .models import Usuario


def home(request):
    # boards = Usuario.objects.all()
    return render(request, 'home.html')


def cadastro_paciente(request):
    if request.method == 'POST':
        form = NewPacienteForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.save()
            return redirect('home')
    else:
        form = NewPacienteForm()
    return render(request, 'cadastro_paciente.html', {'form': form})

def lista_paciente(request):
    pacientes = Usuario.objects.all()
    return render(request, "lista_paciente.html", {'pacientes': pacientes})

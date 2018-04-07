from django import forms

from .models import Usuario


class NewPacienteForm(forms.ModelForm):
    class Meta:  # Next, we have class Meta, where we tell Django which model should be used to create this form (model = Paciente).
        model = Usuario
        fields = ('nome', 'sobrenome', 'endereco', 'cpf', 'email', 'telefone',)

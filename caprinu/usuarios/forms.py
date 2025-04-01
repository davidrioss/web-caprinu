from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.hashers import make_password
from .models import Usuario

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

class UsuarioChangeForm(UserChangeForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False, label="Nova Senha")
    
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'password', 'cpfUsuario', 'dataNascimentoUsuario', 'phoneUsuario', 'funcaoUsuario', 'associacao', 'endereco.rua', 'endereco.numero', 'endereco.bairro', 'endereco.cidade', 'endereco.estado', 'endereco.cep']
   
    def save(self, commit=True):
        usuario = super().save(commit=False)
        if self.cleaned_data['password']:  # Verifica se a senha foi fornecida
            usuario.set_password(self.cleaned_data['password'])  # Define a nova senha
        if commit:
            usuario.save()
        return usuario


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=100)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)
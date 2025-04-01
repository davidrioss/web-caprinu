from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from .models import Usuario, Endereco
from .forms import LoginForm, UsuarioChangeForm
from .forms import UsuarioCreationForm, UsuarioChangeForm, LoginForm


def custom_login(request):
    """
    View para autenticação de usuários.
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('inicio')
            else:
                messages.error(request, 'Usuário ou senha incorretos.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def custom_logout(request):
    """
    View para logout de usuários.
    """
    logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('login')

@login_required
def perfil_usuario(request):
    """
    View para exibir e editar o perfil do usuário logado.
    """
    usuario = request.user
    if request.method == 'POST':
        form = UsuarioChangeForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('perfil_usuario')
    else:
        form = UsuarioChangeForm(instance=usuario)
    return render(request, 'perfil.html', {'form': form})
import random
import string
from django.shortcuts import render
from .forms import UsuarioForm
from .models import Usuario

def gerar_senha():
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(caracteres) for _ in range(15))

def cadastrar_usuario(request):
    mensagem = None
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.senha = gerar_senha()
            usuario.save()
            
            mensagem = {
                'nome': usuario.nome,
                'email': usuario.email,
                'telefone': usuario.telefone,
                'area': usuario.area,
                'senha': usuario.senha,
            }

            # send_mail(
            #     subject='Dados de Cadastro e Senha',
            #     message=f"Olá {usuario.nome},\n\nSua senha é: {usuario.senha}",
            #     from_email='seu_email@dominio.com',  # Configure no settings.py
            #     recipient_list=[usuario.email],  # Envia para o e-mail do usuário
            #     fail_silently=False,
            # )

    else:
        form = UsuarioForm()
    return render(request, 'cadastro/formulario.html', {'form': form, 'mensagem': mensagem})


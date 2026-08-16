from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Classe de Login customizada
class CustomLoginView(LoginView):
    template_name = 'app/login.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        form.fields['password'].widget.attrs.update({'placeholder': 'Password'})
        return form

# Formulário customizado para cadastro sem regras restritas de senha
class SimpleUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Remove o texto de ajuda sobre o formato do nome de usuário
        if 'username' in self.fields:
            self.fields['username'].help_text = ""
            
        # Remove o texto de ajuda da senha
        if 'password1' in self.fields:
            self.fields['password1'].help_text = ""
            
        # Adiciona os placeholders
        self.fields['username'].widget.attrs.update({'placeholder': 'Usuário'})
        if 'password1' in self.fields:
            self.fields['password1'].widget.attrs.update({'placeholder': 'Senha'})
        if 'password2' in self.fields:
            self.fields['password2'].widget.attrs.update({'placeholder': 'Confirmar Senha'})

# View Home (Redireciona para clientes se logado, ou para o login se deslogado)
def home(request):
    if request.user.is_authenticated:
        return redirect('clientes')
    return redirect('login')

# View de Cadastro
def cadastrar(request):
    if request.method == 'POST':
        form = SimpleUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso! Faça o login.')
            return redirect('login')
    else:
        form = SimpleUserCreationForm()
    
    return render(request, 'app/cadastrar.html', {'form': form})

# View protegida de clientes
@login_required
def clientes(request):
    return render(request, 'app/clientes.html')
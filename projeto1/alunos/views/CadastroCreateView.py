from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from alunos.forms import UserRegistrationForm
from alunos.models import CustomUser

class CustomLoginView(LoginView):
    template_name = 'Login.html'
    success_url = reverse_lazy('alunosHome')

class CadastroView(CreateView):
    model = CustomUser
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'Cadastro.html'

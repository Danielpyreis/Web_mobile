from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from alunos.views.CadastroCreateView import CustomLoginView, CadastroView
from alunos.views.HomeListView import HomeListView
from alunos.views.MatriculaListView import MatriculaListView
from alunos.views.MatriculasCreateView import MatriculasCreateView
from alunos.views.AlunoUpdateView import AlunoUpdateView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),  # URL de login como a raiz
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('alunos/lista/', login_required(MatriculaListView.as_view()), name='alunosLista'),
    path('alunos/matricula/', login_required(MatriculasCreateView.as_view()), name='alunosMatricula'),
    path('alunos/situacao/<int:pk>/', login_required(AlunoUpdateView.as_view()), name='alunosSituacao'),
    path('home/', login_required(HomeListView.as_view()), name='alunosHome'), 
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
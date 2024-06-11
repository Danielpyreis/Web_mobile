from django.views.generic import ListView
from alunos.models import Vinculacao
from django.contrib.auth.mixins import LoginRequiredMixin

class MatriculaListView(LoginRequiredMixin, ListView ):
    model = Vinculacao
    template_name = 'MatriculaListView.html'
    
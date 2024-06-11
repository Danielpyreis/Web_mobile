from django.views.generic import CreateView
from alunos.models import Vinculacao
from alunos.forms import MatriculaForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class MatriculasCreateView(LoginRequiredMixin, CreateView):
    model = Vinculacao
    form_class = MatriculaForm
    template_name='MatriculasCreateView.html'
    def get_success_url(self):
        return reverse('alunosLista')   
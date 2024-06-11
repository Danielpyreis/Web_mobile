from django.views.generic import UpdateView
from alunos.models import Vinculacao
from alunos.forms import SituacaoForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse

class AlunoUpdateView(LoginRequiredMixin ,UpdateView):
    model = Vinculacao
    form_class = SituacaoForm  
    template_name = 'Situacao.html' 
     
    def get_success_url(self):
        return reverse('alunosLista')
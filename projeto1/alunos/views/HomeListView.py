from django.views.generic import ListView
from alunos.models import Vinculacao, Campus
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeListView(LoginRequiredMixin, ListView):
    model = Vinculacao
    template_name = 'Home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Contar o número de alunos em cada situação
        alunosJubilados = Vinculacao.objects.filter(situacao='Jubilado').count()
        alunosFormados = Vinculacao.objects.filter(situacao='Formado').count()
        alunosEvadidos = Vinculacao.objects.filter(situacao='Evadido').count()
        alunosVinculados = Vinculacao.objects.filter(situacao='Vinculado').count()
          
        # Total de cada situação
        context['alunos_jubilados'] = alunosJubilados
        context['alunos_formados'] = alunosFormados
        context['alunos_evadidos'] = alunosEvadidos
        context['alunos_vinculados'] = alunosVinculados
        
        alunosPorCampus = {}
        campusList = Campus.objects.annotate(numAlunos=Count('curso__vinculacao'))

        for campus in campusList:
            alunosPorCampus[campus.nome] = campus.numAlunos

        context['alunos_por_campus'] = alunosPorCampus
        
        return context
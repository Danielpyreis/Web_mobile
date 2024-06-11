from django.contrib import admin
from alunos.models import Campus, Curso, Vinculacao, CustomUser

class VinculacaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'matricula', 'email', 'dataNascimento', 'curso', 'ingresso']
    search_fields = ['nome', 'matricula', 'email', 'dataNascimento', 'curso__nome']  #
    list_filter = ['curso']

admin.site.register(Vinculacao, VinculacaoAdmin)
admin.site.register(Campus)
admin.site.register(Curso)
admin.site.register(CustomUser)


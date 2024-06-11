from django.db import models
from alunos.models.Campus import Campus

class Curso(models.Model):
    nome = models.CharField('Nome do Curso',max_length=50)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Curso"

    def __str__(self):
        return f"{self.nome} - {self.campus.nome}"
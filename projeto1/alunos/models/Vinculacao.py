from django.db import models
from datetime import datetime
from alunos.models.Curso import Curso


INGRESSO_CHOICES = (
        ("SISU", "SISU"),
        ("Vestibular", "Vestibular"),
        ("PSEnem", "PSEnem"),
    )
SITUACAO_CHOICES = (
        ("Vinculado", "Vinculado"),
        ("Formado", "Formado"),
        ("Evadido", "Evadido"),
        ("Jubilado", "Jubilado"),
    )

class Vinculacao(models.Model):
    ##pessoa
    nome = models.CharField('Nome',max_length=255, help_text="Nome completo")
    cpf = models.CharField('CPF',max_length=11, unique=True, help_text="Dígitos 11 numeros sem traços")
    dataNascimento = models.DateField("Data Nascimento")
    foto = models.ImageField('Foto',upload_to='uploads/', help_text='Envie apenas imagens')
    ## aluno
    matricula = models.CharField('Matrícula',max_length=9, unique=True, blank=True, help_text='Gerada automaticamente')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    ingresso = models.CharField('Forma de ingresso',max_length=10, choices=INGRESSO_CHOICES, blank=False, null=False)
    situacao = models.CharField('Situação',max_length=20, choices=SITUACAO_CHOICES, default="Vinculado")

    ## contao
    email = models.EmailField('Email',max_length=254, help_text='user@mail.com')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Vinculação"

    def gerarMatricula(self):
        anoAtual = datetime.now().year
        mesAtual = datetime.now().month
        semestre_atual = 1 if mesAtual <= 6 else 2
        
        # Formata a matrícula
        semestre = f"{anoAtual}{semestre_atual}"
        ultima_matricula = Vinculacao.objects.filter(matricula__startswith=semestre).order_by('-matricula').first()
        if ultima_matricula:
            sequencia = int(ultima_matricula.matricula[-4:]) + 1
        else:
            sequencia = 1
        self.matricula = f"{semestre}{sequencia:04d}"

    def save(self, *args, **kwargs):
        if not self.matricula:
            self.gerarMatricula()
        super().save(*args, **kwargs)


  


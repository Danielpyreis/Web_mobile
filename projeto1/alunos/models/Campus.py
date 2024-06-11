from django.db import models

class Campus(models.Model):
    nome = models.CharField('Campus',max_length=50, unique=True)
    
    class Meta:
        verbose_name_plural = "Campus"
    
    def __str__(self):
        return self.nome

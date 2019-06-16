from django.db import models

class Morador(models.Model):

    nome = models.CharField(max_length=100)
    condominio = models.CharField(max_length=50)
    apartamento = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Nome do Morador'
        verbose_name_plural = 'Moradores'




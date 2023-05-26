from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=30, blank=False, null=False)
    rg = models.CharField(max_length=9, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=11, default='')

    def __str__(self):
        return self.nome
    

class Curso(models.Model):

    NIVEL_CURSO = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )

    codigo_curso = models.CharField(max_length=10, blank=False, null=False)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL_CURSO, blank=False, null=False, default='B')

    def __str__(self):
        return self.descricao
    

class Matricula(models.Model):

    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    )

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo_curso = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')
from rest_framework import viewsets, generics

from escola.models import *
from escola.serializers import *


class AlunosViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os alunos'''
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os cursos'''
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculasViewSet(viewsets.ModelViewSet):
    '''Exibinfo todas as matriculas'''
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class ListaMatriculasAluno(generics.ListAPIView):
    '''Exibindo as matrículas de um aluno'''
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer


class ListaAlunosMatriculados(generics.ListAPIView):
    '''Exibindo alunos matriculados em um curso'''
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer

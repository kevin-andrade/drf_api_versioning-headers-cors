from rest_framework import viewsets, generics
from rest_framework import status
from rest_framework.response import Response

from escola.models import *
from escola.serializers import *


class AlunosViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os alunos'''
    queryset = Aluno.objects.all()
    # (/?version=V2)
    def get_serializer_class(self):
        if self.request.version == 'V2':
            return AlunoSerializerV2
        else:
            return AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os cursos'''
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
            return response


class MatriculasViewSet(viewsets.ModelViewSet):
    '''Exibinfo todas as matriculas'''
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    http_method_names = ['get', 'post', 'put', 'path']


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
    http_method_names = ['get', 'post', 'put', 'path']

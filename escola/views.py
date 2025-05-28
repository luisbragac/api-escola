from rest_framework import viewsets, generics
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, MatriculaPorEstudanteSerializer, MatriculaPorCursoSerializer
from escola.models import Estudante, Curso, Matricula

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class MatriculaPorEstudante(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id = self.kwargs['pk'])
        return queryset
    serializer_class = MatriculaPorEstudanteSerializer

class MatriculaPorCurso(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk'])
        return queryset
    serializer_class = MatriculaPorCursoSerializer
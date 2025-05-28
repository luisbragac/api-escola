from rest_framework import viewsets
from escola.serializers import EstudanteSerializer, CursoSerializer
from escola.models import Estudante, Curso

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
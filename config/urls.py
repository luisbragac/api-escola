from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, MatriculaPorEstudante, MatriculaPorCurso

router = routers.DefaultRouter()

router.register('estudantes', EstudanteViewSet, basename='Estudantes')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('estudantes/<int:pk>/matriculas/', MatriculaPorEstudante.as_view()),
    path('cursos/<int:pk>/matriculas/', MatriculaPorCurso.as_view())
]

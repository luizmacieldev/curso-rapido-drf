from rest_framework import viewsets
from estudante.models import Estudante
from .serializers import EstudanteSerializer

class EstudanteViewSet(viewsets.ModelViewSet):
	queryset = Estudante.objects.all()
	serializer_class = EstudanteSerializer


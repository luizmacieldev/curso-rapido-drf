from rest_framework import serializers
from estudante.models import Estudante

class EstudanteSerializer(serializers.ModelSerializer):
	class Meta:
		model 	= Estudante
		fields 	= ('id','primeiro_nome','segundo_nome','data_matricula')
		
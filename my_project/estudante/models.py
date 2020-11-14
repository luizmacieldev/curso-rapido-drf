from django.db import models

# Create your models here.
class Estudante(models.Model):
    primeiro_nome 	= models.CharField(max_length=200)
    segundo_nome 	= models.CharField(max_length=200)
    data_matricula  = models.DateField(blank=True,null=True)

    def __str__(self):
    	return self.primeiro_nome + ' ' + self.segundo_nome
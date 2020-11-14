from django.urls import path,include
from .views import EstudanteViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('estudante',EstudanteViewSet)

urlpatterns = [
	path('',include(router.urls))
]

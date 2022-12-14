
from django.urls import path
from .views import encontrar_jobs, aceitar_job, perfil, enviar_projeto

urlpatterns = [
    path('encontrar_jobs/', encontrar_jobs, name="encontrar_jobs"),
    path('aceitar_job/<int:id>/', aceitar_job, name="aceitar_job"),
    path('perfil/', perfil, name="perfil"),
    path('enviar_projeto/', enviar_projeto, name="enviar_projeto"),
]

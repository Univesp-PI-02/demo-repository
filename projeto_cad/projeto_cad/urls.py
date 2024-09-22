from django.contrib import admin
from django.urls import path
from app_cad_clientes import views

urlpatterns = [
    # roda, view responsável, nome de referencia
    path('',views.home,name='home'),
    path('clientes/', views.clientes,name='listagem_clientes'),
    path('cadastro/', views.cadastro,name='cadastro')

]

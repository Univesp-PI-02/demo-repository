from django.contrib import admin
from django.urls import path
from app_cad_clientes import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clientes/', views.clientes, name='listagem_clientes'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('excluir/<int:id>/', views.excluir_cliente, name='excluir_cliente'),
]
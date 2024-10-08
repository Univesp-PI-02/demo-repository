from django.contrib import admin
from django.urls import path
from app_cad_clientes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.clientes, name='listagem_clientes'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('excluir/<int:id>/', views.excluir_cliente, name='excluir_cliente'),
    path('editar_observacao/<int:id_observacao>/', views.editar_observacao, name='editar_observacao'),
    path('excluir_observacao/<int:id_observacao>/', views.excluir_observacao, name='excluir_observacao'),
    path('adicionar_observacao/<int:id_cliente>/', views.adicionar_observacao, name='adicionar_observacao'),
]
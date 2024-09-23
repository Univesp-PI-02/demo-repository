from django.shortcuts import render, redirect, get_object_or_404
from .models import Clientes
from datetime import date

def home(request):
    hoje = date.today()
    clientes_hoje = Clientes.objects.filter(prox_contato=hoje)
    context = {
        'clientes_hoje': clientes_hoje
    }
    return render(request, 'clientes/home.html', context)

def cadastro(request):
    if request.method == 'POST':
        novo_cliente = Clientes(
            empresa=request.POST.get('empresa'),
            segmento=request.POST.get('segmento'),
            contato=request.POST.get('contato'),
            telefone=request.POST.get('telefone'),
            cidade=request.POST.get('cidade'),
            estado=request.POST.get('estado'),
            email=request.POST.get('email'),
            instagram=request.POST.get('instagram'),
            cnpj=request.POST.get('cnpj'),
            qtd_lojas=request.POST.get('qtd_lojas'),
            observacoes=request.POST.get('observacoes'),
            prox_contato=request.POST.get('prox_contato')
        )
        novo_cliente.save() 
        return redirect('listagem_clientes') 
    return render(request, 'clientes/cadastro.html')

def clientes(request):
    clientes = {
        'clientes': Clientes.objects.all()
    }
    return render(request, 'clientes/busca.html', clientes)

def editar_cliente(request, id):
    cliente = get_object_or_404(Clientes, id_cliente=id)

    if request.method == 'POST':
        cliente.empresa = request.POST.get('empresa')
        cliente.segmento = request.POST.get('segmento')
        cliente.contato = request.POST.get('contato')
        cliente.telefone = request.POST.get('telefone')
        cliente.cidade = request.POST.get('cidade')
        cliente.estado = request.POST.get('estado')
        cliente.email = request.POST.get('email')
        cliente.instagram = request.POST.get('instagram')
        cliente.cnpj = request.POST.get('cnpj')
        cliente.qtd_lojas = request.POST.get('qtd_lojas')
        cliente.observacoes = request.POST.get('observacoes')
        cliente.prox_contato = request.POST.get('prox_contato')
        cliente.save()
        return redirect('listagem_clientes')
    return render(request, 'clientes/editar.html', {'cliente': cliente})

def excluir_cliente(request, id):
    cliente = get_object_or_404(Clientes, id_cliente=id)
    cliente.delete()
    return redirect('listagem_clientes')
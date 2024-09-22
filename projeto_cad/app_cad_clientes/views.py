from django.shortcuts import render
from .models import Clientes

# Create your views here.
def home(request):
    return render(request,'clientes/home.html')

def cadastro(request):
    return render(request,'clientes/cadastro.html')

def clientes(request):
    if request.method == 'POST':
        # Salvar novo cliente se o método for POST
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

    clientes = {
        'clientes': Clientes.objects.all()
    }
    return render(request, 'clientes/busca.html', clientes)
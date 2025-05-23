from django.shortcuts import render, redirect, get_object_or_404
from .models import Clientes, Observacoes
from django.utils import timezone
from datetime import date
from django.http import JsonResponse
from django.db.models.functions import TruncMonth, TruncYear
from django.db.models import Count
import csv
from django.http import HttpResponse

def index(request):
    hoje = timezone.now()
    clientes_hoje = Clientes.objects.filter(
        prox_contato__date=hoje
    )
    context = {
        'clientes_hoje': clientes_hoje
    }
    return render(request, 'clientes/index.html', context)


def cadastro(request):
    if request.method == 'POST':
        novo_cliente = Clientes(
            empresa=request.POST.get('empresa'),
            status=request.POST.get('status'),
            segmento=request.POST.get('segmento'),
            contato=request.POST.get('contato'),
            telefone=request.POST.get('telefone'),
            telefone_2=request.POST.get('telefone_2'),
            cidade=request.POST.get('cidade'),
            estado=request.POST.get('estado'),
            email=request.POST.get('email'),
            instagram=request.POST.get('instagram'),
            cnpj=request.POST.get('cnpj'),
            qtd_lojas=request.POST.get('qtd_lojas'),
            cep=request.POST.get('cep'), 
            rua=request.POST.get('rua'),
            numero_end=request.POST.get('numero_end'),
            bairro=request.POST.get('bairro'),
            complemento=request.POST.get('complemento'),
            primeiro_contato=request.POST.get('primeiro_contato'),
            prox_contato=request.POST.get('prox_contato')
        )
        novo_cliente.save()

        observacoes_texto = request.POST.get('observacoes')
        if observacoes_texto: 
            nova_observacao = Observacoes(
                id_cliente=novo_cliente, 
                descricao=observacoes_texto
            )
            nova_observacao.save()
        
        return redirect('listagem_clientes')
    return render(request, 'clientes/cadastro.html')

def clientes(request):
    clientes = {
        'clientes': Clientes.objects.all()
    }
    return render(request, 'clientes/busca.html', clientes)

def editar_cliente(request, id):
    cliente = get_object_or_404(Clientes, id_cliente=id)
    observacoes_cliente = Observacoes.objects.filter(id_cliente=cliente)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'salvar_cliente':
            cliente.empresa = request.POST.get('empresa')
            cliente.status = request.POST.get('status')
            cliente.segmento = request.POST.get('segmento')
            cliente.contato = request.POST.get('contato')
            cliente.telefone = request.POST.get('telefone')
            cliente.telefone_2 = request.POST.get('telefone_2')
            cliente.cidade = request.POST.get('cidade')
            cliente.estado = request.POST.get('estado')
            cliente.email = request.POST.get('email')
            cliente.instagram = request.POST.get('instagram')
            cliente.cnpj = request.POST.get('cnpj')
            cliente.qtd_lojas = request.POST.get('qtd_lojas')
            cliente.cep = request.POST.get('cep')
            cliente.rua = request.POST.get('rua')
            cliente.numero_end = request.POST.get('numero_end')
            cliente.bairro = request.POST.get('bairro')
            cliente.complemento = request.POST.get('complemento')
            cliente.primeiro_contato = request.POST.get('primeiro_contato')
            cliente.prox_contato = request.POST.get('prox_contato')
            cliente.save()

            return redirect('listagem_clientes')
    return render(request, 'clientes/editar.html', {'cliente': cliente, 'observacoes_cliente': observacoes_cliente})

def adicionar_observacao(request, id_cliente):
    if request.method == 'POST':
        cliente = get_object_or_404(Clientes, pk=id_cliente)
        nova_observacao_texto = request.POST.get('nova_observacao_texto')

        if nova_observacao_texto:
            observacao = Observacoes(id_cliente=cliente, descricao=nova_observacao_texto)
            observacao.save()

    return redirect('editar_cliente', id=id_cliente)

def excluir_cliente(request, id):
    cliente = get_object_or_404(Clientes, id_cliente=id)
    cliente.delete()
    return redirect('listagem_clientes')

def editar_observacao(request, id_observacao):
    observacao = get_object_or_404(Observacoes, id_observacao=id_observacao)
    
    if request.method == 'POST':
        nova_descricao = request.POST.get('descricao')
        if nova_descricao:
            observacao.descricao = nova_descricao
            observacao.save()
        return redirect('editar_cliente', observacao.id_cliente.id_cliente)

def excluir_observacao(request, id_observacao):
    observacao = get_object_or_404(Observacoes, id_observacao=id_observacao)
    cliente_id = observacao.id_cliente.id_cliente
    observacao.delete()
    return redirect('editar_cliente', cliente_id)

# Dashboard
def dashboard(request):
    return render(request, 'clientes/dashboard.html')

def dados_grafico(request):
    dados = Clientes.objects.annotate(
        ano=TruncYear('prox_contato'),
        mes=TruncMonth('prox_contato')
    ).values('ano', 'mes').annotate(total=Count('id_cliente')).order_by('ano', 'mes')

    return JsonResponse({
        "anos": [d["ano"].year for d in dados],
        "meses": [d["mes"].month for d in dados],
        "totais": [d["total"] for d in dados]
    })

# Filtro de clientes
def busca_clientes(request):
    # Obtém os parâmetros de busca
    empresa = request.GET.get('empresa', '')
    cidade = request.GET.get('cidade', '')

    # Filtra os clientes com base nos parâmetros
    clientes = Clientes.objects.all()
    if empresa:
        clientes = clientes.filter(empresa__icontains=empresa)
    if cidade:
        clientes = clientes.filter(cidade__icontains=cidade)

    # Renderiza o template com os resultados
    context = {'clientes': clientes}
    return render(request, 'clientes/busca.html', context)


# Gerar Arquivos CSV

def exportar_clientes_csv(request):
    # Filtra os clientes com base nos parâmetros de busca (se aplicável)
    empresa = request.GET.get('empresa', '')
    cidade = request.GET.get('cidade', '')

    clientes = Clientes.objects.all()
    if empresa:
        clientes = clientes.filter(empresa__icontains=empresa)
    if cidade:
        clientes = clientes.filter(cidade__icontains=cidade)

    # Cria a resposta HTTP com o tipo de conteúdo CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="clientes.csv"'

    # Escreve os dados no arquivo CSV
    writer = csv.writer(response)
    writer.writerow(['Empresa', 'Status', 'Segmento', 'Contato', 'Telefone', 'Cidade', 'Estado', 'Email', 'Instagram', 'CNPJ', 'Nº Lojas', 'Próximo Contato'])
    for cliente in clientes:
        writer.writerow([
            cliente.empresa, cliente.status, cliente.segmento, cliente.contato,
            cliente.telefone, cliente.cidade, cliente.estado, cliente.email,
            cliente.instagram, cliente.cnpj, cliente.qtd_lojas, cliente.prox_contato
        ])

    return response

import requests
from django.shortcuts import render, redirect
from .models import Pagamento, Feedback, Reserva
from .models import Sala
from django.utils import timezone

def listar_salas(request):
    salas = Sala.objects.all()
    return render(request, 'reservas/listar_salas.html', {'salas': salas})

def reservar_sala(request, sala_id):
    sala = Sala.objects.get(id=sala_id)
    if request.method == 'POST':
        data_inicio = request.POST.get('data_inicio')
        data_fim = request.POST.get('data_fim')
        nova_reserva = Reserva(usuario=request.user, sala=sala, data_inicio=data_inicio, data_fim=data_fim)
        nova_reserva.save()
        return redirect('listar_salas')
    return render(request, 'reservas/reservar_sala.html', {'sala': sala})


# Função para gerar o boleto via PagSeguro
def gerar_boleto_pagseguro(request):
    if request.method == 'POST':
        usuario = request.user
        quantia = request.POST.get('amount')
        
        # Informações do PagSeguro
        pagseguro_email = 'SEU_EMAIL@EMAIL.COM'
        pagseguro_token = 'SEU_TOKEN'

        url = 'https://ws.pagseguro.uol.com.br/v2/checkout'
        cabecalhos = {'Content-Type': 'application/x-www-form-urlencoded; charset=ISO-8859-1'}
        
        data = {
            'email': pagseguro_email,
            'token': pagseguro_token,
            'currency': 'BRL',
            'itemId1': '001',
            'itemDescrição1': 'Reserva de Sala de Coworking',
            'itemvalor1': f'{quantia:.2f}',
            'itemQuantidade1': '1',
            'referencia': 'REF1234',
            'remetenteNome': usuario.username,
            'remetenteE-mail': usuario.email,
            'metodoPagamento': 'boleto',
        }

        # Solicitação para gerar o boleto
        resposta = requests.post(url, data=data, cabecalhos=cabecalhos)

        if resposta.status_code == 200:
            checkout_resposta = resposta.text
            boleto_url = checkout_resposta.split('redirectURL')[1].split('<![CDATA[')[1].split(']]>')[0]

            # Criar o registro no banco de dados
            Pagamento.objects.create(
                usuario=usuario,
                quantia=quantia,
                metodo_pagamento='boleto',
                boleto_url=boleto_url
            )
            return redirect(boleto_url)  # Redireciona para o boleto gerado
        else:
            return render(request, 'erro_pagamento.html')

    return render(request, 'pagina_de_pagamento.html')

# Função para pagamentos por transferência bancária ou PIX
def transferencia_pix(request):
    if request.method == 'POST':
        usuario = request.usuario
        quantia = request.POST.get('quantia')
        pix_info = "Chave PIX: 12345678900 (Copie e cole no seu banco)"

        # Salvar os detalhes do pagamento no banco de dados
        Pagamento.objects.create(
            usuario=usuario,
            quantia=quantia,
            metodo_pagamento='pix',
            pix_info=pix_info
        )

        # Exibir instruções de pagamento por PIX/Transferência
        return render(request, 'confirmacao_pix.html', {'pix_info': pix_info, 'quantia': quantia})
    
    return render(request, 'pagina_de_pagamento.html')

# Função para pagamento via Cartão de Crédito PagSeguro
def pagamento_cartao(request):
    if request.method == 'POST':
        usuario = request.usuario
        quantia = request.POST.get('quantia')

        # Aqui você deve implementar a lógica para processar o pagamento via Cartão de Crédito.
        # A implementação varia conforme a documentação do PagSeguro.

        # Simulação de registro de pagamento, aqui você deve adicionar a lógica real
        Pagamento.objects.create(
            usuario=usuario,
            quantia=quantia,
            metodo_pagamento='cartao',
            esta_pago=True  # Ajuste de acordo com a lógica de pagamento
        )

        return render(request, 'confirmacao_cartao.html')

    return render(request, 'pagina_de_pagamento.html')

# Função para adicionar feedback
def adicionar_feedback(request):
    if request.method == 'POST':
        usuario = request.usuario
        mensagem = request.POST.get('mensagem')

        Feedback.objects.create(
            usuario=usuario,
            mensagem=mensagem
        )

        return render(request, 'confirmacao_feedback.html')

    return render(request, 'pagina_de_feedback.html')

# Função para criar uma reserva
def criar_reserva(request):
    if request.method == 'POST':
        usuario = request.usuario
        data = request.POST.get('data')
        duracao = request.POST.get('duracao')

        Reserva.objects.create(
            usuario=usuario,
            data=data,
            duracao=duracao
        )

        return render(request, 'confirmacao_reserva.html')

    return render(request, 'pagina_de_reserva.html')

def sucesso(request):
    return render(request, 'reservas/sucesso.html')

def cancelar(request):
    return render(request, 'reservas/cancelar.html')

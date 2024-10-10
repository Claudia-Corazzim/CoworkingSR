from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('salas/', views.listar_salas, name='listar_salas'),
    path('salas/<int:sala_id>/reservar/', views.reservar_sala, name='reservar_sala'),
    path('pagamento/boleto/', views.gerar_boleto_pagseguro, name='pagamento_boleto'),
    path('pagamento/pix/', views.transferencia_pix, name='pagamento_pix'),
    path('pagamento/cartao/', views.pagamento_cartao, name='pagamento_cartao'),
    path('feedback/', views.adicionar_feedback, name='adicionar_feedback'),
    path('reserva/', views.criar_reserva, name='criar_reserva'),
    path('admin/', admin.site.urls),
    path('reservas/', include('reservas.urls')),  # Inclui as URLs do aplicativo reservas
    path('reservas/<int:reserva_id>/pagar/', views.pagar_reserva, name='pagar_reserva'),
    path('sucesso/', views.sucesso, name='sucesso'),
    path('cancelar/', views.cancelar, name='cancelar'),
]
from django.contrib import admin
from .models import Sala, Reserva, Pagamento, Feedback

admin.site.register(Reserva)
admin.site.register(Pagamento)
admin.site.register(Feedback)

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'capacidade', 'descricao', 'imagem')  # Adiciona a imagem à lista
    search_fields = ('nome',)
    list_filter = ('capacidade',)
    
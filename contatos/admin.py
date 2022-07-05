from django.contrib import admin
from .models import Categoria, Contato


# Para mostrar mais dados na tela admin
class ContatoAdmin(admin.ModelAdmin):
    # Mostra os outros dados de models:
    list_display = (
        'id', 'nome', 'sobrenome', 'telefone',
        'email', 'data_criacao', 'categoria', 'mostrar')
    # Transforma em links:
    list_display_links = ('id', 'nome', 'sobrenome')
    # Adiciona um filtro
    # list_filter = ('nome', 'sobrenome')
    # Quantos itens serão exibidos por página:
    list_per_page = 5
    # Campo de pesquisa:
    search_fields = ('nome', 'sobrenome', 'id')
    # Tornar campos editáveis
    list_editable = ('telefone', 'mostrar')


# Registra os apps na tela admin
admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)

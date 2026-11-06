from django.contrib import admin
from .models import Categoria, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco', 'disponivel')
    list_editable = ('preco', 'disponivel')   # edita direto na listagem
    list_filter = ('categoria', 'disponivel')
    search_fields = ('nome', 'descricao')
    list_per_page = 25

from django.contrib.auth.models import Group, Permission

# Gerente: pode tudo em produtos e categorias
gerente, _ = Group.objects.get_or_create(name='Gerente')
gerente.permissions.set(
    Permission.objects.filter(content_type__app_label='cardapio')
)

# Atendente: só visualiza e altera produtos (ex.: marcar indisponível)
atendente, _ = Group.objects.get_or_create(name='Atendente')
atendente.permissions.set(
    Permission.objects.filter(
        content_type__app_label='cardapio',
        codename__in=['view_produto', 'change_produto', 'view_categoria'],
    )
)

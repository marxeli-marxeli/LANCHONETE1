from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=80, unique=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=120)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='produtos')
    descricao = models.TextField(blank=True)
    preco = models.DecimalField('Preço (R$)', max_digits=8, decimal_places=2)
    disponivel = models.BooleanField('Disponível', default=True)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['categoria', 'nome']

    def __str__(self):
        return f'{self.nome} - R$ {self.preco}'


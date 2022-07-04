from django.db import models
from django.utils import timezone

# Na base de dados serão criadas as tabalas contatos_contato
# e contatos_categoria


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Contato(models.Model):

    def __str__(self):
        return self.nome

    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    # Aqui ele referencia a classe acima. Se o contato for apagado,
    # não será excluido as informações desta classe
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

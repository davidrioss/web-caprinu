from django.db import models
from django.contrib.auth.models import AbstractUser

class Endereco(models.Model):
    rua = models.CharField(max_length=255, verbose_name="Rua")
    numero = models.CharField(max_length=10, verbose_name="Número")
    bairro = models.CharField(max_length=100, verbose_name="Bairro")
    cidade = models.CharField(max_length=100, verbose_name="Cidade")
    estado = models.CharField(max_length=2, verbose_name="Estado")
    cep = models.CharField(max_length=10, verbose_name="CEP")

    def __str__(self):
        return f"{self.rua}, {self.numero}, {self.bairro}, {self.cidade}, {self.estado}, {self.cep}"
    
class Usuario(AbstractUser):
    first_name = models.CharField(max_length=100, verbose_name="Nome")
    last_name = models.CharField(max_length=100, verbose_name="Sobrenome")
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    cpfUsuario = models.IntegerField(unique=True, null=True, verbose_name="CPF")
    dataNascimentoUsuario = models.DateField(null=True, verbose_name="Data de Nascimento")
    email = models.EmailField(unique=True, verbose_name="Email")
    phoneUsuario = models.IntegerField(verbose_name="Telefone")
    funcaoUsuario = models.CharField(null=True, max_length=100, verbose_name="Função/Ocupação")
    associacao = models.CharField(null=True, max_length=100, verbose_name="Associação")
    
    def __str__(self):
        return self.first_name
    

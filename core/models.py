from django.db import models

class Cpf(models.Model):
    NUM_CPF = models.CharField(max_length=11, primary_key=True)
    NOME = models.CharField(max_length=500, blank=True, null=True)
    DATA_NASCIMENTO = models.CharField(max_length=12, blank=True, null=True)
    IND_SEXO = models.CharField(max_length=2, blank=True, null=True)
    NOME_MAE = models.CharField(max_length=500, blank=True, null=True)
    NUM_TITULO_ELEITOR = models.CharField(max_length=12, blank=True, null=True)
    TIPO_LOGRADOURO = models.CharField(max_length=50, blank=True, null=True)
    DESCR_LOGRADOURO = models.CharField(max_length=100, blank=True, null=True)
    NUM_LOGRADOURO = models.CharField(max_length=50, blank=True, null=True)
    DESCR_COMPLEMENTO_LOGRADOURO = models.CharField(max_length=800, blank=True, null=True)
    NOME_BAIRRO = models.CharField(max_length=500, blank=True, null=True)
    NUM_CEP = models.CharField(max_length=50, blank=True, null=True)
    NOME_MUNICIPIO = models.CharField(max_length=200, blank=True, null=True)
    SIGLA_UF = models.CharField(max_length=50, blank=True, null=True)
    NUM_DDD = models.CharField(max_length=50, blank=True, null=True)
    NUM_TELEFONE = models.CharField(max_length=50, blank=True, null=True)
    NUM_FAX = models.CharField(max_length=50, blank=True, null=True)
    SE_ESTRANGEIRO = models.CharField(max_length=2, blank=True, null=True)
    NOME_PAIS_NACIONALIDADE = models.CharField(max_length=500, blank=True, null=True)
    COD_SITUACAO_CADASTRAL = models.CharField(max_length=2, blank=True, null=True)
    DESCR_SITUACAO_CADASTRAL = models.CharField(max_length=50, blank=True, null=True)
    DATA_SITUACAO_CADASTRAL = models.CharField(max_length=12, blank=True, null=True)
    DATA_INSCRICAO = models.CharField(max_length=12, blank=True, null=True)
    ANO_OBITO = models.CharField(max_length=10, blank=True, null=True)
    ANO_ULTIMA_ENTREGA_DECLARACAO = models.CharField(max_length=10, blank=True, null=True)
    DATA_BASE = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self):
        return self.NOME
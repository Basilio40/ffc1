from django.db import models
from django.conf import settings
from django_cpf_cnpj.fields import CPFField, CNPJField
from django.contrib.auth.models import User

class Dashboard(models.Model):
    pass



class Usuarios(models.Model):
    pass



class Perfis(models.Model):
    pass



class TbaxTipoContato(models.Model):
    descricao = models.CharField(max_length=250)



class Tbcontato(models.Model):
    STATUS_USUARIO = [
        ('Ativo','Ativo'),
        ('Inativo','Inativo'),
        ('Implantacao','Implantacao'),
    ]
    nome = models.CharField(max_length=40, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='criado_por')
    modificado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modificado_por')
    status = models.CharField(max_length=20,choices=STATUS_USUARIO)
    razao_social = models.CharField(max_length=255,blank=True, null=True)
    data_criacao = models.DateField(auto_now=True)
    data_modificação = models.DateField(auto_now_add=True)
    avatar = models.ImageField(upload_to='avatar', blank=True, null=True)
    
    def __str__(self):
        return self.nome



class TbCliente(models.Model):
    TIPO_CLIENTES = [
      ('Varejista', 'Varejista'),
      ('Cooperativa', 'Cooperativa'),
      ('Financeira', 'Financeira'),
      ('Outros', 'Outros'),
    ]

    STATUS_CLIENTE = [
        ('Ativo','Ativo'),
        ('Inativo','Inativo'),
        ('Implantacao','Implantacao'),
    ]
    nome = models.CharField(max_length=40)
    nome_curto = models.CharField( max_length=40)
    cep = models.CharField(max_length=40, blank=True, null=True)
    bairro = models.CharField(max_length=40, blank=True, null=True)
    cidade = models.CharField(max_length=40, blank=True, null=True)
    logradouro = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=50,choices=TIPO_CLIENTES)
    cnpj = CNPJField(masked=True)
    razaosocial = models.CharField(max_length=128,blank=True, null=True)  
    fkcontatoprimario = models.CharField(max_length=250, blank=True, null=True)  
    fkcontatotecnico = models.CharField(max_length=250, blank=True, null=True)  
    clientestatus = models.CharField(choices=STATUS_CLIENTE, max_length=300)
    data_criacao = models.DateField(auto_now=True)
    data_modificação = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CLIENTE)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return self.nome
    
    def clientes_ativos(self):
        cliente = self.id
        return cliente
    
 
        




class Seguradora(models.Model):
    STATUS_SEGURADORA = [
        ('Ativo','Ativo'),
        ('Inativo','Inativo'),
        ('Implantacao','Implantacao'),
    ]
    nome = models.CharField(max_length=100)
    nomecurto = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_SEGURADORA)


    class Meta:
        verbose_name = 'Seguradora'
        verbose_name_plural = 'Seguradoras'


class Operacao(models.Model):
    STATUS_OP = [
        ('Em processo de Implantacao','Em processo de Implantacao'),
        ('Implantado', 'Implantado'),
        ('Não implantado', 'Não implantado'),
        ('Operação suspensa','Operação suspensa'),
        ('Operação encerrada', 'Operação encerrada' ),
        ('Operação com gestao conjunta', 'Operação com gestao conjunta'),
        ('Operação em run-off', 'Operação em run-off'),
        ('Não defenido', 'Não defenido'),
        ('Dados em homologacao sem auxiliares', 'Dados em homologacao sem auxiliares'),
        ('Dados em homologacao', 'Dados em homologacao'),
        ('Operacao sem gestao FFC','Operacao sem gestao FFC')
    ]
    
    fkcliente = models.ForeignKey(TbCliente,on_delete=models.CASCADE)
    descricao = models.TextField(max_length=250)
    nome = models.CharField(max_length=50, blank=True, null=True)
    data_criacao = models.DateField()
    datainicio = models.DateField()
    dataencerramento = models.DateField()
    fkseguradora = models.ForeignKey(Seguradora,on_delete=models.CASCADE)
    fkfarmer = models.ForeignKey(Tbcontato,on_delete=models.CASCADE)
    operacaostatus = models.CharField(max_length=300,choices=STATUS_OP)

    class Meta:
        verbose_name = 'Operacao'
        verbose_name_plural = 'Operacoes'



class Contratos(models.Model):
    pass



class Farol(models.Model):
    pass



class Reembolso(models.Model):
    pass



class Servicos(models.Model):
    pass



class Budget(models.Model):
    pass



class Contabilidade(models.Model):
    pass



class Auxiliares(models.Model):
    pass


class TbaxTipoCliente(models.Model):
    tipocliente = models.CharField(max_length=50, db_column='TipoCliente')



class TbaxTipoOperacao(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=250)



class TbaxStatusCliente(models.Model):
    descricao = models.CharField(max_length=250)



class TbaxStatusOperacao(models.Model):
    descricao = models.CharField(max_length=250)




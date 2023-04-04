from django.contrib import admin
from .models import Dashboard, Usuarios, Perfis, Contratos, TbCliente, Tbcontato, Operacao, Seguradora, Farol, Servicos
from .models import TbaxStatusCliente, TbaxTipoCliente, TbaxTipoContato, TbaxTipoOperacao, TbaxStatusOperacao


admin.site.register(Dashboard)
admin.site.register(Usuarios)
admin.site.register(Perfis)
admin.site.register(Contratos)
admin.site.register(Servicos)
admin.site.register(TbCliente)
admin.site.register(Tbcontato)
admin.site.register(Operacao)
admin.site.register(Seguradora)
admin.site.register(TbaxStatusCliente)
admin.site.register(TbaxTipoCliente)
admin.site.register(TbaxTipoContato)
admin.site.register(TbaxStatusOperacao)
admin.site.register(TbaxTipoOperacao)
admin.site.register(Farol)



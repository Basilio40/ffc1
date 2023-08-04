from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('usuario/',views.criar_usuario,name='usuario'),
    path('login/', views.login, name='login'),
    path('forgot-password/', views.forgot_password, name='forgot-password'),

    path('servicos/', views.servicos, name='servicos'),
    path('operacoes-monitoramento/', views.operacoes_monitoramento, name='operacoes-monitoramento'),
    path('recebimento-de-dados/', views.recebimento_de_dados, name='recebimento-de-dados'),

    path('contatos/', views.contatos, name='contatos'),
    path('clientes/', views.clientes, name='clientes'),
    path('teste_cliente/',views.teste_cliente,name='teste'),
    path('seguradoras/', views.seguradoras, name='seguradoras'),
    path('contratos/', views.contratos, name='contratos'),
    path('operacoes-cadastros/', views.operacoes_cadastros, name='operacoes-cadastros'),
    path('auxiliares/', views.auxiliares, name='auxiliares'),

    path('notas-fiscais/', views.notas_fiscais, name='notas-fiscais'),
    path('faturamento/', views.faturamento, name='faturamento'),
    path('reembolso/', views.reembolso, name='reembolso'),
    path('budget/', views.budget, name='budget'),

    path('usuarios/', views.usuarios, name='usuarios'),
    path('perfis/', views.perfis, name='perfis'),
    path('modal',views.modal, name='modal'),
    path('modalview',views.modal, name='modalview'),
    path('cliente_form/',views.cliente_form,name='cliente_form'),
    path('clientevisual/<str:id>',views.clientevisualiz,name='clientevisual'),
]

# Formularios
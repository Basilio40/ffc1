from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from PIL import Image
from django.contrib.auth.models import User
from .models import TbCliente,Tbcontato, Seguradora
from rolepermissions.roles import assign_role, get_user_roles
from rolepermissions.permissions import revoke_permission, grant_permission
from rolepermissions.decorators import has_role_decorator , has_permission_decorator
from .forms import ClientesForm , SeguradorasForm,ContatosForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required

@login_required
def index(request): 
    # print(get_user_roles(request.user))
    return render(request, 'dashboard/index.html')

def criar_usuario(request):
    user = User.objects.create_user(username="farmer",password="1234")
    user.save()
    assign_role(user, 'farmer')
    return HttpResponse('Usuario salvo com sucesso')

# Auth
def login(request):
    if request.method == "GET":
        return render(request, 'dashboard/login.html')
    elif request.method == "POST":
        username = request.POST.get('email')
        senha = request.POST.get('pass')
        
        usuario = auth.authenticate(username=username, password=senha)
        if not usuario:
            return redirect('login')
        else:
            auth.login(request, usuario)
            return redirect('/')
        
        
def forgot_password(request): 
    return render(request, 'dashboard/forgot-password.html')


# Monitoramento
# @has_permission_decorator('criar_metas')
def servicos(request):
    return render(request, 'dashboard/servicos.html')

def operacoes_monitoramento(request):
    return render(request, 'dashboard/operacoes_monitoramento.html')

def recebimento_de_dados(request):
    return render(request, 'dashboard/recebimento_de_dados.html')


# Cadastros
def contatos(request):
    ativos = Tbcontato.objects.filter(status='Ativo').count()
    inativos = Tbcontato.objects.filter(status='Inativo').count()
    implantacao = Tbcontato.objects.filter(status='Implantacao').count()
    total = ativos + inativos + implantacao
    lista_contatos = Tbcontato.objects.all()
    context = {
        'contatos':lista_contatos,
        'ativos':ativos,
        'inativos':inativos,
        'implantacao':implantacao,
        'total':total
    }
    return render(request, 'dashboard/contatos.html',context)

def clientes(request):
    ativos = TbCliente.objects.filter(status='Ativo').count()
    inativos = TbCliente.objects.filter(status='Inativo').count()
    implantacao = TbCliente.objects.filter(status='Implantacao').count()
    total = ativos + inativos + implantacao
    lista_clientes = TbCliente.objects.all()
    cliente=TbCliente.objects.all()
    cliente_filtro = TbCliente.objects.filter()

    context = {
        'clientes':lista_clientes,
        'ativos':ativos,
        'inativos':inativos,
        'implantacao':implantacao,
        'total':total,
        'cliente':cliente,
        'cliente_filtro':cliente_filtro,
    }
    return render(request, 'dashboard/clientes.html',context)

def clientevisualiz(request,id):
    cliente = TbCliente.objects.filter(id=id)
    return render(request,'dashboard/clientevisual.html',{'cliente':cliente,})

def teste_cliente(request):
    cliente_ativo = TbCliente.objects.all()
    cliente_inativo = TbCliente.objects.all()
    if cliente_ativo:
        cliente=TbCliente.objects.filter(status='Ativo').count()
        if cliente_inativo:
            cliente_inat=TbCliente.objects.filter(status='Inativo').count()
    return HttpResponse(f'{cliente},{cliente_inat}')
    
    
        # cliente_ativo = cliente.values('status').count()
    

def modal(request):    
    return render(request, 'hx/modal.html')

def modalview(request):
    return render(request, 'hx/modalview.html')

def seguradoras(request):
    ativos = Seguradora.objects.filter(status='Ativo').count()
    inativos = Seguradora.objects.filter(status='Inativo').count()
    implantacao = Seguradora.objects.filter(status='Implantacao').count()
    total = ativos + inativos + implantacao
    lista_seguradoras = Seguradora.objects.all()
    context = {
        'seguradoras':lista_seguradoras,
        'ativos':ativos,
        'inativos':inativos,
        'implantacao':implantacao,
        'total':total
    }
    return render(request, 'dashboard/seguradoras.html',context)

def contratos(request):
    return render(request, 'dashboard/contratos.html')

def operacoes_cadastros(request):
    return render(request, 'dashboard/operacoes_cadastros.html')

def auxiliares(request):
    return render(request, 'dashboard/auxiliares.html')


# Financeiro
def notas_fiscais(request):
    return render(request, 'dashboard/notas_fiscais.html')

def faturamento(request):
    return render(request, 'dashboard/faturamento.html')

def reembolso(request):
    return render(request, 'dashboard/reembolso.html')

def budget(request):
    return render(request, 'dashboard/budget.html')


# Admin Sistema
def usuarios(request):
    return render(request, 'dashboard/usuarios.html')

def perfis(request):
    return render(request, 'dashboard/perfis.html')

# Formularios

def cliente_form(request):
    context = {
        'form':ClientesForm(),
    }
   
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard/clientes.html')
    return render(request, 'dashboard/cliente_form.html', context)

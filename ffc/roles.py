from rolepermissions.roles import AbstractUserRole

class Sup(AbstractUserRole):
    available_permissions = {
        'ver_contato': True,
        'ver_perfis': True,
        'ver_contratos': True,
        'ver_dashboard': True,
        'ver_servicos': True,
        'ver_operacoes': True,
        'ver_clientes': True,
        'ver_seguradoras': True,
        'ver_auxiliares': True,
        'ver_contabiliade': True,
        'ver_budget': True,
        'ver_farol': True,
        'ver_reembolso': True,
        'ver_usuarios': True,
    }

class Cliente(AbstractUserRole):
    available_permissions = {
        'ver_operacoes': True,
        'ver_dashboard': True,
        'ver_contatos': True,
        
    }

class Sys(AbstractUserRole):
    available_permissions = {
        'ver_contato': True,
        'ver_perfis': True,
        'ver_contratos': True,
        'ver_dashboard': True,
        'ver_servicos': True,
        'ver_operacoes': True,
        'ver_clientes': True,
        'ver_seguradoras': True,
        'ver_auxiliares': True,
        'ver_contabiliade': True,
        'ver_budget': True,
        'ver_farol': True,
        'ver_reembolso': True,
        'ver_usuarios': True,
    }

class Fin(AbstractUserRole):
    available_permissions = {
        'ver_contato': True,
        'ver_contratos': True,
        'ver_dashboard': True,
        'ver_clientes': True,
        'ver_seguradoras': True,
        'ver_contabiliade': True,
        'ver_budget': True,
    }

class Implantador(AbstractUserRole):
    available_permissions = {
        'ver_contato': True,
        'ver_contratos': True,
        'ver_dashboard': True,
        'ver_operacoes': True,
        'ver_clientes': True,
        'ver_seguradoras': True,
        'ver_farol': True,
        'ver_reembolso': True,
    }
    
class Farmer(AbstractUserRole):
    available_permissions = {
        'ver_contato': True,
        'ver_contratos': True,
        'ver_dashboard': True,
        'ver_operacoes': True,
        'ver_clientes': True,
        'ver_seguradoras': True,
        'ver_farol': True,
        'ver_reembolso': True,
        'ver_budget': True,
    }
    

from django import forms
from .models import TbCliente,Tbcontato, Seguradora

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ClientesForm(forms.ModelForm):
    class Meta:
        model = TbCliente
        fields ='__all__'
        
class SeguradorasForm(forms.ModelForm):
    class Meta:
        model = Seguradora
        fields ='__all__'
        
class ContatosForm(forms.ModelForm):
    class Meta:
        model = Tbcontato
        fields = '__all__'
        

# class CustomUserCreationForm(UserCreationForm):
#         model = User
#         fields = ['username',"first_name", "last_name", "email", "password1", "password2"]
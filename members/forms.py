from django.forms import ModelForm
from members.models import Usuario 

class UsuarioForms(ModelForm):
    class Meta:
        model= Usuario
        fields= ['email', 'senha']


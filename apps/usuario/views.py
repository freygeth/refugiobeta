#from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from usuario.forms import RegistroForm

class RegistroUsuario(CreateView):
	model = User
	template_name = "usuario/registrar.html"
	#form_class = UserCreationForm lo cambiamos por RegistroUsuario(se uso anterior)
	form_class = RegistroForm
	success_url = reverse_lazy('mascota:mascota_listar')
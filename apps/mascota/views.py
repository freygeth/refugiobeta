from django.shortcuts import render, redirect
from mascota.forms import MascotaForm
from mascota.models import Mascota
#from django.http import HttpResponse
# Create your views here.
#estamos trabajando en vistas basadas en funciones, con clases es menos codigo
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

#vistas por funciones:
def index(request):
	return render(request,"mascota/index.html")
	#return HttpResponse("texto index para mascota")


def mascota_view(request):
	if request.method == 'POST':
		form = MascotaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('mascota:mascota_listar')
	else:
		form = MascotaForm()
	return render(request, 'mascota/mascota_form.html', {'form':form})			

def mascota_list(request):
	mascota = Mascota.objects.all().order_by('id')
	contexto = {'mascotas':mascota}
	return render(request, 'mascota/mascota_list.html', contexto)

def mascota_edit(request, id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == 'GET':
		form = MascotaForm(instance=mascota)
	else:
		form = MascotaForm(request.POST, instance=mascota)
		if form.is_valid():
			form.save()
		return redirect('mascota:mascota_listar')
	return render(request, 'mascota/mascota_form.html', {'form':form})	

def mascota_delete(request, id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == 'POST':
		mascota.delete()
		return redirect('mascota:mascota_listar')
	return render(request, 'mascota/mascota_delete.html', {'mascota':mascota})				

###### vistas por clases
class MascotaList(ListView):
	model = Mascota
	template_name = 'mascota/mascota_list.html'

class MascotaCreate(CreateView):
	model = Mascota
	form_class = MascotaForm
	template_name = 'mascota/mascota_form.html'
	success_url = reverse_lazy('mascota:mascota_listar')
#success_url = reverse_lazy('mascota:mascota_listar') para enviarme a la lista de mascotas	

class MascotaUpdate(UpdateView):
	model = Mascota
	form_class = MascotaForm
	template_name = 'mascota/mascota_form.html'
	success_url = reverse_lazy('mascota:mascota_listar')
# vemos que en mascota_edit() le pasabamos el id, ahora ese id en MascotaUpdate estara como pk en urls.py	

class MascotaDelete(DeleteView):
	model = Mascota
	template_name = 'mascota/mascota_delete.html'
	success_url = reverse_lazy('mascota:mascota_listar')
	
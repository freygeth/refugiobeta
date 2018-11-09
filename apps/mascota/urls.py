from django.conf.urls import url
from . import views
#from mascota.views import index  no me funciona porque lo hice la estructura como la doc.oficial
#from mascota.views import mascota_view ya lo uso con la linea 2
#from mascota.views import mascota_list ya lo uso con la linea 2
##añadi para importa la class MascotaList
from django.contrib.auth.decorators import login_required
#####con clases:
from mascota.views import MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete
urlpatterns = [
	url(r'^$', views.index, name='index'),
	#url(r'^$', index), no me fuciono, en el video si.
	url(r'^nuevo$', login_required(MascotaCreate.as_view()), name='mascota_crear'),
	url(r'^listar$', login_required(MascotaList.as_view()), name='mascota_listar'),
	url(r'^editar/(?P<pk>\d+)/$', login_required(MascotaUpdate.as_view()), name='mascota_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', login_required(MascotaDelete.as_view()), name='mascota_eliminar'),
]

#cuando se haga peticion al url ,como MascotaList es una clase se añade .as_view() para ejecutarse como vista
#####version anterior:
"""
urlpatterns = [
	url(r'^$', views.index, name='index'),
	#url(r'^$', index), no me fuciono, en el video si.
	url(r'^nuevo$', views.mascota_view, name='mascota_crear'),
	url(r'^listar$', views.mascota_list, name='mascota_listar'),
	url(r'^editar/(?P<id_mascota>BARRAINVERTIDAd+)/$', views.mascota_edit, name='mascota_editar'),
	url(r'^eliminar/(?P<id_mascota>BARRAINVERTIDAd+)/$', views.mascota_delete, name='mascota_eliminar'),
]
"""
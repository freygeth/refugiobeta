from django.conf.urls import url
from . import views
#from mascota.views import index  no me funciona porque lo hice la estructura como la doc.oficial
from adopcion.views import index_adopcion, SolicitudList, SolicitudCreate,SolicitudUpdate, SolicitudDelete
#from adopcion.views import index_adopcion, SolicitudList

"""
urlpatterns = [
	url(r'^$', views.index, name='index'),

]
"""
###trabajaremos con clases
urlpatterns = [
	url(r'^$', index_adopcion),
	url(r'^solicitud/listar$', SolicitudList.as_view() , name='solicitud_listar'),
	url(r'^solicitud/nueva$', SolicitudCreate.as_view() , name='solicitud_crear'),
	url(r'^solicitud/editar/(?P<pk>\d+)$', SolicitudUpdate.as_view() , name='solicitud_editar'),
	url(r'^solicitud/eliminar/(?P<pk>\d+)$', SolicitudDelete.as_view() , name='solicitud_eliminar'),
]
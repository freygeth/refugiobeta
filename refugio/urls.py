"""refugio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login
""" version sin modificacion disponible para user
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^mascota/', include('mascota.urls', namespace='mascota')),
    url(r'^adopcion/', include('adopcion.urls', namespace='adopcion')),
    url(r'^usuario/', include('usuario.urls', namespace='usuario')),
    url(r'^$', login, {'template_name':'index.html'}, name='login')
]
"""
# vista basada en funcion(es propia de django):
#url(r'^', login, {'template_name':'index.html'}, name='login')

##################################################################

####### Era para que el user modifique su pass:
from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^mascota/', include('mascota.urls', namespace='mascota')),
    url(r'^adopcion/', include('adopcion.urls', namespace='adopcion')),
    url(r'^usuario/', include('usuario.urls', namespace='usuario')),
    url(r'^accounts/login/$', login, {'template_name':'index.html'}, name='login'),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^reset/password_reset', password_reset, 
        {'template_name':'registration/password_reset_form.html',
        'email_template_name': 'registration/password_reset_email.html'}, 
        name='password_reset'), 
    url(r'^password_reset_done', password_reset_done, 
        {'template_name': 'registration/password_reset_done.html'}, 
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, 
        {'template_name': 'registration/password_reset_confirm.html'},
        name='password_reset_confirm'
        ),
    url(r'^reset/done', password_reset_complete, {'template_name': 'registration/password_reset_complete.html'},
        name='password_reset_complete'),
]
"""
- luego de realizar el bloqueo para que los que no son usuarios no puedan ingresar
 a links solo para usuarios. al intentar entrar a uno de esos links me envia error 404 con 
 el link http://localhost:8000/accounts/login/?next=/mascota/listar
 Para que nos envie al login real añadimos accounts/login/ al url que tiene este archivo login(index.html)
-luego de ya poder navegar en el navbar, añadimos el logout_then_login(importacion) y el url logout aqui.
En base.html tambien y el link goout, asi como en refugio/setting.py
"""
################################################################



"""lpc_tarefas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from tastypie.api import Api
from django.contrib import admin
from tarefas.api.resources import *
from tarefas.views import *

v1_api = Api(api_name='v1')
v1_api.register(UsuarioResource())
v1_api.register(ProjetoResource())
v1_api.register(TarefaResource())
v1_api.register(ProjetoUsuarioResource())

urlpatterns = [
    url(r'^api/', include(v1_api.urls)),
    url(r'^$', index, name='index'),
    url(r'^tarefas/', listaTarefas, name='listaTarefas'),
    url(r'^tarefa/([0-9]{1})', tarefaId, name='tarefaId'),
    url(r'^usuarios/', listaUsuarios, name='usuarios'),
    url(r'^usuario/([0-9]{1})/', usuarioId, name='usuarioId'),
    url(r'^projetos/', listaProjetos, name='listaProjetos'),
    url(r'^api/', include(v1_api.urls)),
]

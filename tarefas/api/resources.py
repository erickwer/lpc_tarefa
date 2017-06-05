from tastypie.resources import ModelResource
from tastypie import fields, utils
from tastypie.authorization import Authorization
from tarefas.models import *
from django.contrib.auth.models import User
from tastypie.exceptions import Unauthorized

class UsuarioResource(ModelResource):
    def obj_delete_list(self,bundle,**kwargs):
        raise Unauthorized('Você não pode deletar essa lista');

    class Meta:
        queryset = Usuario.objects.all()
        allowed_methods = ['get','post','put','delete']
        filtering = {
            "nome": ('exact', 'startswith',)
        }
        authorization = Authorization()

class ProjetoResource(ModelResource):
    def obj_delete_list(self,bundle,**kwargs):
        raise Unauthorized('Você não pode deletar essa lista');

    class Meta:
        queryset = Projeto.objects.all()
        allowed_methods = ['get','post','put','delete']
        filtering = {
            "nome": ('exact', 'startswith',)
        }
        authorization = Authorization()

class TarefaResource(ModelResource):
    def obj_create(self, bundle, **kwargs):

        nomeTarefa = bundle.data['nomeTarefa']
        usuario = bundle.data['usuario'].split("/")
        projeto = bundle.data['projeto'].split("/")

        if not Tarefa.objects.filter(nomeTarefa=nomeTarefa):
            tipo = Tarefa()
            tipo.nomeTarefa = bundle.data['nomeTarefa']
            tipo.usuario = Usuario.objects.get(pk=usuario[4])
            tipo.projeto = Projeto.objects.get(pk=projeto[4])
            tipo.save()
            bundle.obj = tipo
            return bundle
        else:
            raise Unauthorized('Esta tarefa ja está associada a um projeto!');



    def obj_delete_list(self,bundle,**kwargs):
        raise Unauthorized('Você não pode deletar essa lista');

    class Meta:
        queryset = Tarefa.objects.all()
        allowed_methods = ['get','post','put','delete']
        filtering = {
            "nome": ('exact', 'startswith',)
        }
        authorization = Authorization()

class ProjetoUsuarioResource(ModelResource):
    def obj_delete_list(self,bundle,**kwargs):
        raise Unauthorized('Você não pode deletar essa lista');

    class Meta:
        queryset = ProjetoUsuario.objects.all()
        allowed_methods = ['get','post','put','delete']
        filtering = {
            "nome": ('exact', 'startswith',)
        }
authorization = Authorization()

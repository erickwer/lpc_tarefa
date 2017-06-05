from django.contrib import admin

# Register your models here.

from tarefas.models import *

admin.site.register(Usuario)
admin.site.register(Projeto)
admin.site.register(Tarefa)
admin.site.register(ProjetoUsuario)

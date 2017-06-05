from django.http import HttpResponse
from .models import *

def index(request):
    html = """<h1>Opções</h1>
                <ul>
                    <li><a href='/projetos'>Projetos</a></li>
                    <li><a href='/tarefas'>Tarefas</a></li>
                    <li><a href='/usuarios'>Usuarios</a></li>
                </ul>
            """
    return HttpResponse(html)

def listaProjetos(request):
    html = "<h1>Lista de Projetos</h1>"
    listaProjeto = Projeto.objects.all()
    for projeto in listaProjeto:
        html += '<li><strong>Nome: {}</strong></li>'.format(projeto.nome)
        html += '<ul><li>Tarefas : {}</li>'.format(projeto.tarefa)
        #html += '<li>Usuarios: {}/{}</li>'.format(projeto.usuario)
    return HttpResponse(html)

def projetoId(request, id):
    pj = Projeto.objects.get(pk=id)
    return HttpResponse("<h2> Informações Projeto #" + str(pj.id) + "</h2>" + "<strong>Nome:</strong> " + str(pj.nome) + "<strong>Tarefa: </strong> " + str(pj.tarefa)  + "<strong>Usuario: </strong> " + str(pj.usuario) )

def listaUsuarios(request):
    html = "<h1>Lista de Usuarios</h1>"
    listaUsuarios = Usuario.objects.all()
    for usuario in listaUsuarios:
        html += '<li><strong>Nome: {}</strong></li>'.format(usuario.nome)
        html += '<li>email: {}</li>'.format(usuario.email)
        html += '<li>Senha : {}</li>'.format(usuario.senha) + '<br>'
    return HttpResponse(html)

def usuarioId(request, id):
    user= Usuario.objects.get(pk=id)
    return HttpResponse("<h2> Informações Usuario #" + str(user.id) + "</h2>" + "<strong>Nome:</strong> " + str(user.nome)  + "<br>" + "<strong>Email:</strong> " + str(user.email)  + "<br>" + "<strong>Senha:</strong> " + str(user.senha) + "<br>")

def listaTarefas(request):
    html = "<h1>Lista de tarefas</h1>"
    lt = Tarefa.objects.all()
    for tarefa in lt:
        html += '<li><strong> Nome: {}</strong></li>'.format(tarefa.nome)
        html += '<ul><li>Data e Hora Inicio: {}</li></ul>'.format(tarefa.dataEHoraInicio)
    return HttpResponse(html)

def tarefaId(request, id):
    tf = Tarefa.objects.get(pk=id)
    return HttpResponse("<h2> Informações tarefa #" + str(tf.id) + "</h2>" + "<strong>Nome:</strong> " + str(tf.nome)  + "<br>" + "<strong> Data e Hora Inicio:</strong> " + str(tf.dataEHoraInicio))

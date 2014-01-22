# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from aluno.model import Aluno
from curso.model import Curso, Matricula
from zen import router


def index(_write_tmpl):
    query = Curso.query_cursos_ordenados_asc()
    lista_de_cursos = query.fetch()
    url = router.to_path(form)
    values = {'curso_form_url': url,
              'lista_de_cursos': lista_de_cursos,
              'matricula_url': router.to_path(matriculas)}
    _write_tmpl('templates/curso_home.html', values)


def form(_write_tmpl):
    url = router.to_path(salvar)
    values = {'curso_salvar_url': url}
    _write_tmpl('templates/curso_form.html', values)


def salvar(_handler, nome):
    curso = Curso(nome=nome)
    curso.put()
    home = router.to_path(index)
    _handler.redirect(home)


def matriculas(_write_tmpl, curso_id):
    # Lista de todos alunos do BD
    alunos = Aluno.query_alunos_ordenados_asc().fetch()
    #Construção da chave baseado no id do curso
    curso_key = ndb.Key(Curso, int(curso_id))

    lista_de_matriculas = Matricula.query_matriculas_do_curso(curso_key).fetch()

    # Filtrando apenas chaves dos alunos matriculados
    chaves_alunos_matriculados = [m.aluno for m in lista_de_matriculas]

    #montando lista de alunos matriculados e disponiveis
    alunos_matriculados = []
    alunos_disponiveis = []
    for aluno in alunos:
        if aluno.key in chaves_alunos_matriculados:
            alunos_matriculados.append(aluno)
        else:
            alunos_disponiveis.append(aluno)
    # buscando curso do BD. Usa memcache (NDB)
    curso = curso_key.get()

    #Montagem dos parametros do template
    values = {'curso': curso,
              'matricula_salvar_url': router.to_path(salvar_matricula),
              'lista_de_alunos_matriculados': alunos_matriculados,
              'lista_de_alunos_disponiveis': alunos_disponiveis}
    _write_tmpl('templates/matricula.html', values)


def salvar_matricula(_handler,curso_id, aluno_id):
    curso_key=ndb.Key(Curso,int(curso_id))
    aluno_key=ndb.Key(Aluno,int(aluno_id))
    Matricula(curso=curso_key,aluno=aluno_key).put()

    url=router.to_path(matriculas,curso_id)
    _handler.redirect(url)


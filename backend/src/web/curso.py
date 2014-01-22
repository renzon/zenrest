# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from curso.model import Curso
from zen import router


def index(_write_tmpl):
    query = Curso.query_cursos_ordenados_asc()
    lista_de_cursos = query.fetch()
    url = router.to_path(form)
    values = {'curso_form_url': url,
              'lista_de_cursos': lista_de_cursos}
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

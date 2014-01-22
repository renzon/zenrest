# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from aluno.model import Aluno
from zen import router


def index(_write_tmpl):
    url = router.to_path(form)
    values = {'aluno_form_url': url}
    _write_tmpl('templates/aluno_home.html', values)


def form(_write_tmpl):
    url = router.to_path(salvar)
    values = {'aluno_salvar_url': url}
    _write_tmpl('templates/aluno_form.html', values)


def salvar(_handler, nome):
    aluno=Aluno(nome=nome)
    aluno.put()
    home=router.to_path(index)
    _handler.redirect(home)

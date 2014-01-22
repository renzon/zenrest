# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from zen import router


def index(_write_tmpl):
    url = router.to_path(form)
    values = {'aluno_form_url': url}
    _write_tmpl('templates/aluno_home.html', values)


def form():
    pass
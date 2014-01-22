# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from web import aluno
from zen import router


def index(_write_tmpl):
    url = router.to_path(aluno.index)
    values = {'aluno_home_url': url}
    _write_tmpl('templates/home.html', values)

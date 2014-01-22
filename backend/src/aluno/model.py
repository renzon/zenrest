# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb


class Aluno(ndb.Model):
    nome = ndb.StringProperty(required=True)

    @classmethod
    def query_alunos_ordenados_asc(cls):
        return cls.query().order(cls.nome)


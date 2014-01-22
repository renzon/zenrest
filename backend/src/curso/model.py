# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb


class Curso(ndb.Model):
    nome=ndb.StringProperty(required=True)

    @classmethod
    def query_cursos_ordenados_asc(cls):
        return cls.query().order(cls.nome)


# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from aluno.model import Aluno


class Curso(ndb.Model):
    nome = ndb.StringProperty(required=True)

    @classmethod
    def query_cursos_ordenados_asc(cls):
        return cls.query().order(cls.nome)


class Matricula(ndb.Model):
    criacao=ndb.DateTimeProperty(auto_now_add=True)
    curso=ndb.KeyProperty(Curso,required=True)
    aluno=ndb.KeyProperty(Aluno,required=True)

    @classmethod
    def query_matriculas_do_curso(cls, curso_key):
        return cls.query(cls.curso==curso_key)


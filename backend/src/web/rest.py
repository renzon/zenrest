# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from google.appengine.ext import ndb
from curso.model import Curso, Matricula


def matriculas(_resp,curso_id):
    #Construção da chave baseado no id do curso
    curso_key = ndb.Key(Curso, int(curso_id))

    lista_de_matriculas = Matricula.query_matriculas_do_curso(curso_key).fetch()

    # Filtrando apenas chaves dos alunos matriculados
    chaves_alunos_matriculados = [m.aluno for m in lista_de_matriculas]

    #Buscando alunos matrículados no BD
    matriculados=ndb.get_multi(chaves_alunos_matriculados)

    #Transformando propriedade em dicionario

    def to_dict(entidade):
        dct=entidade.to_dict()
        dct['id']=str(entidade.key.id())
        return dct

    matriculados_dcts=[to_dict(aluno) for aluno in matriculados]
    js=json.dumps(matriculados_dcts)
    _resp.write(js)

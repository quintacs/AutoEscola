from flask_openapi3 import  OpenAPI,Info, Tag
from flask_cors import CORS
from flask import redirect

from sqlalchemy.exc import IntegrityError
from urllib.parse import unquote

from schemas import *

from logger import logger

from modelo import Session, Aluno, Instrutor


info = Info(title = "Minha API", version = "1.0.0" )
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(name="Documentacao", description="Selecao de documentacao: swagger, redoc ou rapidoc")
aluno_tag = Tag(name="Aluno", description="Adicao, visualizacao e remocao de alunos da base")
instrutor_tag = Tag(name="Instrutor", description="Adicao, visualizacao e remocao de instrutores")

@app.get('/', tags=[home_tag])
def home():
    return redirect('/openapi')

@app.post('/aluno',tags=[aluno_tag],
          responses={"200":AlunoViewSchema, "409":ErrorSchema, "400":ErrorSchema})
def add_aluno(form:AlunoSchema):
    aluno = Aluno(
        nome = form.nome,
        idade = form.idade,
        endereco = form.endereco,
        telefone = form.telefone,
        data_nascimento = form.data_nascimento,
        matricula = form.matricula
    )
    logger.debug(f"Adicionando aluno: '{aluno.nome}'")
    try:
        session = Session()
        session.add(aluno)
        session.commit()
        logger.debug(f"Aluno cadastrado com sucesso '{aluno.nome}'")
        return apresenta_aluno(aluno),200

    except IntegrityError as e:
        error_msg = "Erro ao adicionar o aluno:/ "
        logger.warning(f"Erro ao adicionar o aluno '{aluno.nome}','{error_msg}' ")
        return{"message":error_msg}, 409

    except Exception as e:
        error_msg = "Erro ao adicionar o aluno:/ "
        logger.warning(f"Erro ao adicionar o aluno '{aluno.nome}','{error_msg}' ")
        return {"message": error_msg}, 400

@app.get('/alunos',tags=[aluno_tag],
         responses={"200":ListagemAlunosSchema,"404":ErrorSchema})
def get_alunos():
    logger.debug(f"Coletando alunos")

    session= Session()
    alunos = session.query(Aluno).all()
    if not alunos:
        return {"alunos ":[]},200
    else:
        logger.debug(f"%d alunos encontrados "%len(alunos))
        print(alunos)
        return  apresenta_alunos(alunos),200

@app.get('/aluno', tags=[aluno_tag],
         responses={"200": AlunoViewSchema, "404": ErrorSchema})
def get_aluno(query: AlunoBuscaSchema):
    id = query.id
    logger.debug(f"Coletando dados sobre o aluno #{id}")
    session = Session()
    aluno = session.query(Aluno).filter(Aluno.id == id).first()

    if not aluno:
        error_msg = "Aluno não encontrado na base :/"
        logger.warning(f"Erro ao buscar aluno '{id}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Aluno econtrado: '{aluno.nome}'")
        return apresenta_aluno(aluno), 200

@app.delete('/aluno', tags=[aluno_tag],
            responses={"200": AlunoDelSchema, "404": ErrorSchema})
def del_aluno(query: AlunoBuscaSchema):

    aluno_nome = unquote(unquote(query.nome))
    print(aluno_nome)
    logger.debug(f"Deletando dados sobre o aluno #{aluno_nome}")

    session = Session()
    count = session.query(Aluno).filter(Aluno.nome == aluno_nome).delete()
    session.commit()

    if count:
        logger.debug(f"Deletado produto #{aluno_nome}")
        return {"mesage": "Produto removido", "id": aluno_nome}
    else:
        error_msg = "Aluno não encontrado na base :/"
        logger.warning(f"Erro ao deletar aluno #'{aluno_nome}', {error_msg}")
        return {"mesage": error_msg}, 404

#***************************************************************************


@app.post('/instrutor',tags=[instrutor_tag],
          responses={"200":InstrutorSchema, "409":ErrorSchema, "400":ErrorSchema})
def add_instrutor(form:InstrutorSchema):
    instrutor = Instrutor(
        nome = form.nome,
        idade = form.idade,
        endereco = form.endereco,
        telefone = form.telefone,
        data_nascimento = form.data_nascimento,
        agenda = form.agenda
    )
    logger.debug(f"Adicionando instrutor: '{instrutor.nome}'")
    try:
        session = Session()
        session.add(instrutor)
        session.commit()
        logger.debug(f"Instrutor cadastrado com sucesso '{instrutor.nome}'")
        return apresenta_instrutor(instrutor),200

    except IntegrityError as e:
        error_msg = "Erro ao adicionar o instrutor:/ "
        logger.warning(f"Erro ao adicionar o instrutor '{instrutor.nome}','{error_msg}' ")
        return{"message":error_msg}, 409

    except Exception as e:
        error_msg = "Erro ao adicionar o instrutor:/ "
        logger.warning(f"Erro ao adicionar o instrutor '{instrutor.nome}','{error_msg}' ")
        return {"message": error_msg}, 400

@app.get('/instrutores',tags=[instrutor_tag],
         responses={"200":ListagemInstrutorSchema,"404":ErrorSchema})
def get_instrutores():
    logger.debug(f"Coletando instrutores")

    session= Session()
    instrutores = session.query(Instrutor).all()
    if not instrutores:
        return {"instrutores ":[]},200
    else:
        logger.debug(f"%d instrutores encontrados "%len(instrutores))
        print(instrutores)
        return  apresenta_instrutores(instrutores) ,200

@app.get('/instrutor', tags=[instrutor_tag],
         responses={"200": InstrutorViewSchema, "404": ErrorSchema})
def get_instrutor(query: InstrutorBuscaSchema):
    id = query.id
    logger.debug(f"Coletando dados sobre o instrutor #{id}")
    session = Session()
    instrutor = session.query(Instrutor).filter(Instrutor.id == id).first()

    if not instrutor:
        error_msg = "Instrutor não encontrado na base :/"
        logger.warning(f"Erro ao buscar instrutor '{id}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Instrutor econtrado: '{instrutor.nome}'")
        return apresenta_aluno(instrutor), 200

@app.delete('/instrutor', tags=[instrutor_tag],
            responses={"200": InstrutorDelSchema, "404": ErrorSchema})
def del_instrutor(query: InstrutorBuscaSchema):

    instrutor_nome = unquote(unquote(query.nome))
    print(instrutor_nome)
    logger.debug(f"Deletando dados sobre o instrutor #{instrutor_nome}")

    session = Session()
    count = session.query(Instrutor).filter(Instrutor.nome == instrutor_nome).delete()
    session.commit()

    if count:
        logger.debug(f"Deletado o instrutor #{instrutor_nome}")
        return {"mesage": "Instrutor removido", "nome ": instrutor_nome}
    else:
        error_msg = "Instrutor não encontrado na base :/"
        logger.warning(f"Erro ao deletar instrutor #'{instrutor_nome}', {error_msg}")
        return {"mesage": error_msg}, 404

#if __name__ == '__main__':
#    SERVER_HOST = environ.get('SERVER_HOST','localhost')
#    app.run(host=SERVER_HOST,port=5500, debug=(not environ.get('ENV') == 'PRODUCTION'),threaded=True)




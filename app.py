from flask_openapi3 import  OpenAPI,Info, Tag
from flask_cors import CORS
from flask import redirect

from sqlalchemy.exc import IntegrityError
from urllib.parse import unquote

from schemas import *

from logger import logger

from modelo import Session, Aluno, Instrutor

from datetime import datetime

from utils import util

info = Info(title = "Minha API", version = "1.0.0" )
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(name="Documentacao", description="Selecao de documentacao: swagger Api Auto Escola")
aluno_tag = Tag(name="Aluno", description="Adicao, visualizacao e remocao de alunos da base")
instrutor_tag = Tag(name="Instrutor", description="Adicao, visualizacao e remocao de instrutores")

@app.get('/', tags=[home_tag])
def home():
    return redirect('/openapi')

#***************
#Adiciona Aluno
#***************
@app.post('/AdicionaAluno',tags=[aluno_tag],
          responses={"200":AlunoSchema, "409":ErrorSchema, "400":ErrorSchema})
def add_aluno(form:AlunoSchema):

   # date_format = '%d/%m/%Y'
    #data_nascimento_formatada = datetime.strptime(form.data_nascimento,date_format)
    
    #data = datetime.strptime(form.data_nascimento,'%d/%m/%Y') #util.formata_data(form.data_nascimento)

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

#***************
#Atualiza Aluno
#***************
@app.put('/AtualizaAluno/<int:id>', tags=[aluno_tag], 
          responses={"200":AlunoViewSchema, "409":ErrorSchema, "400":ErrorSchema})
def merge_aluno(path:AlunoBuscaSchema ,form:AlunoSchema): 
   
   # date_format = '%d/%m/%Y'
    #data_nascimento_formatada = datetime.strptime(form.data_nascimento,date_format)
    
    #util = Util()
    #data = util.formata_data(form.data_nascimento).date()
    #id = query.id

    aluno = Aluno(
        nome = form.nome,
        idade = form.idade,
        endereco = form.endereco,
        telefone = form.telefone,
        data_nascimento = form.data_nascimento,
        matricula = form.matricula
    )
    logger.debug(f"Atualizando aluno: '{aluno.nome}'")
    try:
        session = Session()
        #session.query(Aluno).filter(Aluno.id == path.id).update({Aluno.nome:aluno.nome,
        #                                                    Aluno.idade:aluno.idade,
        #                                                    Aluno.endereco:aluno.endereco,
        #                                                    Aluno.telefone:aluno.telefone,
        #                                                    Aluno.data_nascimento:aluno.data_nascimento,
        #                                                    Aluno.matricula:aluno.matricula}, synchronize_session=False)
        
        alunoTemp = session.query(Aluno).get(path.id)
        alunoTemp.nome = aluno.nome
        alunoTemp.idade = aluno.idade
        alunoTemp.endereco = aluno.endereco
        alunoTemp.telefone = aluno.telefone
        alunoTemp.data_nascimento = aluno.data_nascimento
        alunoTemp.matricula = aluno.matricula
        
        session.commit()
        logger.debug(f"Aluno atualizado com sucesso '{aluno.nome}'")
        ""
        return apresenta_aluno(aluno),200

    except IntegrityError as e:
        error_msg = "Erro ao atualizar o aluno:/ "
        logger.warning(f"Erro ao atualizar o aluno '{aluno.nome}','{error_msg}' ")
        return{"message":error_msg}, 409

    except Exception as e:
        error_msg = "Erro ao atualizar o aluno:/ "
        logger.warning(f"Erro ao atualizar o aluno '{aluno.nome}','{error_msg}' ")
        return {"message": error_msg}, 400



#***************
#Lista Alunos
#***************
@app.get('/ListaAlunos',tags=[aluno_tag],
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

#***************
#Busca Aluno
#***************
@app.get('/BuscaAluno', tags=[aluno_tag],
         responses={"200": AlunoViewSchema, "404": ErrorSchema})
def get_aluno(query: AlunoBuscaSchema):
    id = query.id
    
    logger.debug(f"Coletando dados sobre o aluno id: #{id}")
    session = Session()
    aluno = session.query(Aluno).filter(Aluno.id == id).first()

    if not aluno:
        error_msg = f"Aluno não encontrado na base :'{id}'"
        logger.warning(f"Erro ao buscar aluno '{id}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Aluno econtrado: '{aluno.nome}'")
        return apresenta_aluno(aluno), 200

#***************
#Deleta Aluno
#***************
@app.delete('/DeletaAluno', tags=[aluno_tag],
            responses={"200": AlunoDelSchema, "404": ErrorSchema})
def del_aluno(query: AlunoBuscaSchemaNome):

    aluno_nome = unquote(unquote(query.nome))
    print(aluno_nome)
    logger.debug(f"Deletando dados sobre o aluno #{aluno_nome}")

    session = Session()
    count = True #session.query(Aluno).filter(Aluno.nome == aluno_nome).delete()
    session.commit()

    if count:
        logger.debug(f"Deletado produto #{aluno_nome}")
        return {"mesage": "Produto removido", "id": aluno_nome}
    else:
        error_msg = "Aluno não encontrado na base :/"
        logger.warning(f"Erro ao deletar aluno #'{aluno_nome}', {error_msg}")
        return {"mesage": error_msg}, 404

#***************************************************************************


#*********************
#Adiciona Instrutor
#*********************
@app.post('/AdicionaInstrutor',tags=[instrutor_tag],
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


#*********************
#Atualiza Instrutor
#*********************
@app.put('/AtualizaInstrutor/<int:id>', tags=[instrutor_tag], 
          responses={"200":InstrutorSchema, "409":ErrorSchema, "400":ErrorSchema})
def merge_instrutor(path:InstrutorBuscaSchema ,form:InstrutorSchema): 
   
   # date_format = '%d/%m/%Y'
    #data_nascimento_formatada = datetime.strptime(form.data_nascimento,date_format)
    
    #util = Util()
    #data = util.formata_data(form.data_nascimento).date()
    #id = query.id

    print(form)

    instrutor = Instrutor(
        nome = form.nome,
        idade = form.idade,
        endereco = form.endereco,
        telefone = form.telefone,
        data_nascimento = form.data_nascimento,
        agenda = form.agenda
    )
    logger.debug(f"Atualizando instrutor: '{instrutor.nome}'")
    try:
        session = Session()
        #session.query(Instrutor).filter(Instrutor.id == path.id).update({Instrutor.nome:instrutor.nome,
        #                                                    Instrutor.idade:instrutor.idade,
        #                                                    Instrutor.endereco:instrutor.endereco,
        #                                                    Instrutor.telefone:instrutor.telefone,
        #                                                    Instrutor.data_nascimento:instrutor.data_nascimento,
        #                                                    Instrutor.agenda:instrutor.agenda}, synchronize_session=False)
        
        instrutorTemp = session.query(Instrutor).get(path.id)
        instrutorTemp.nome = instrutor.nome
        instrutorTemp.idade = instrutor.idade
        instrutorTemp.endereco = instrutor.endereco
        instrutorTemp.telefone = instrutor.telefone
        instrutorTemp.data_nascimento = instrutor.data_nascimento
        instrutorTemp.agenda = instrutor.agenda
        
        session.commit()
        logger.debug(f"Instrutor atualizado com sucesso '{instrutor.nome}'")
        return apresenta_instrutor(instrutor),200

    except IntegrityError as e:
        error_msg = f"Erro ao atualizar o instrutor: '{e._message}'"
        logger.warning(f"Erro: '{instrutor.nome}','{error_msg}' ")
        return{"message":error_msg}, 409

    except Exception as er:
        error_msg = f"Erro ao atualizar o instrutor: '{er.__str__}'"
        logger.warning(f"Erro ao atualizar o instrutor '{instrutor.nome}','{error_msg}' ")
        return {"message": error_msg}, 400

#*********************
#Lista Instrutor
#*********************
@app.get('/ListaInstrutores',tags=[instrutor_tag],
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

#*********************
#Busca Instrutor
#*********************
@app.get('/BuscaInstrutor', tags=[instrutor_tag],
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

#*********************
#Deleta Instrutor
#*********************
@app.delete('/DeletaInstrutor', tags=[instrutor_tag],
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




from pydantic import BaseModel
from typing import List
from modelo import Aluno

class AlunoSchema(BaseModel):
    """ Define como um novo aluno a ser inserido deve ser representado
    """

    nome: str = "Teste"
    idade: int = 0
    endereco: str = "rua teste"
    telefone: str = "(00) 0000-0000"
    data_nascimento:  str = "00/00/0000"
    matricula:str ="000000"


class AlunoViewSchema(BaseModel):
    """ Define como um aluno será retornado.
    """
    id: int = 0
    nome: str = "Teste"
    idade: int = 0
    endereco: str = "rua teste"
    telefone: str = "(00) 0000-0000"
    data_nascimento:  str = "00/00/0000"
    matricula: str = "000000"


class AlunoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no id do aluno.
    """
    id: int = 0



class AlunoBuscaSchemaNome(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do aluno.
    """
    nome: str = "Teste"



class ListagemAlunoViewSchema(BaseModel):
    """ Define como uma listagem de alunos será retornada.
    """
    AlunosViewSchema:List[AlunoViewSchema]
    #alunos:List[AlunoSchema]
    

def apresenta_alunosViewSchem(AlunosViewSchema: List[AlunoViewSchema]):
    """ Retorna uma representação do aluno seguindo o schema definido em
        AlunoViewSchema.
    """
    result = []
    for aluno in AlunosViewSchema:
        result.append({
            "id":aluno.id,
            "nome":aluno.nome,
            "idade":aluno.idade,
            "endereco": aluno.endereco,
            "telefone":aluno.telefone,
            "data_nascimento":aluno.data_nascimento ,
            "matricula" :aluno.matricula
        })

    return {"alunos": result}


class ListagemAlunosSchema(BaseModel):
    """ Define como uma listagem de alunos será retornada.
    """
    alunos:List[AlunoSchema]

def apresenta_alunos(alunos: List[Aluno]):
    """ Retorna uma representação do aluno seguindo o schema definido em
        AlunoViewSchema.
    """
    result = []
    for aluno in alunos:
        result.append({
            "id":aluno.id,
            "nome":aluno.nome,
            "idade":aluno.idade,
            "endereco": aluno.endereco,
            "telefone":aluno.telefone,
            "data_nascimento":aluno.data_nascimento ,
            "matricula" :aluno.matricula
        })

    return {"alunos": result}


class AlunoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do aluno retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_aluno(aluno: Aluno):
    """ Retorna uma representação do aluno seguindo o schema definido em
        AlunoViewSchema.
    """
    return {
            "id":aluno.id,
            "nome":aluno.nome,
            "idade":aluno.idade,
            "endereco": aluno.endereco,
            "telefone":aluno.telefone,
            "data_nascimento":aluno.data_nascimento ,
            "matricula" :aluno.matricula
    }

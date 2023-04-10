from pydantic import BaseModel
from sqlalchemy import Date
from typing import List
from modelo import Aluno

class AlunoSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """

    nome: str = "Teste"
    idade: int = 0
    endereco: str = "rua teste"
    telefone: str = "(00) 0000-0000"
    data_nascimento: Date
    matricula:str ="000000"


class AlunoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    nome: str = "Teste"


class ListagemAlunosSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    alunos:List[AlunoSchema]


def apresenta_alunos(alunos: List[Aluno]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for aluno in alunos:
        result.append({
            "nome":aluno.nome,
            "idade":aluno.idade,
            "endereco": aluno.endereco,
            "telefone":aluno.telefone,
            "data_nascimento":aluno.data_nascimento ,
            "matricula" :aluno.matricula
        })

    return {"alunos": result}


class AlunoViewSchema(BaseModel):
    """ Define como um produto será retornado: produto + comentários.
    """
    id: int = 1
    nome: str = "Teste"
    idade: int = 0
    endereco: str = "rua teste"
    telefone: str = "(00) 0000-0000"
    data_nascimento: Date
    matricula: str = "000000"


class AlunoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_aluno(aluno: Aluno):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
            "id":id,
            "nome":aluno.nome,
            "idade":aluno.idade,
            "endereco": aluno.endereco,
            "telefone":aluno.telefone,
            "data_nascimento":aluno.data_nascimento ,
            "matricula" :aluno.matricula
    }

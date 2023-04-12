from sqlalchemy import Column,String,Integer,ForeignKey

from modelo import Pessoa, Base

class Aluno(Pessoa, Base):

    __tablename__='aluno'

    id = Column("id_aluno", Integer,primary_key=True)
    #nome = Column(String(140))
    #idade = Column(Integer)
    #endereco = Column(String(200))
    #telefone = Column(String(20))
    #data_nascimento = Column(Date)
    matricula = Column(String(20))

    pessoa =  Column(Integer, ForeignKey("pessoa.id_pessoa"),nullable=False)

    def __int__(self, nome, idade, endereco, telefone, data_nascimento, matricula):
        super().__int__(nome, idade, endereco, telefone, data_nascimento)
        self.matricula = matricula


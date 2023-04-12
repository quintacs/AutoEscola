from sqlalchemy import Column, String, Integer,DateTime
from modelo import Base

class Pessoa(Base):

    __tablename__='pessoa'

    id = Column("id_pessoa", Integer, primary_key=True)
    nome = Column(String(140))
    idade = Column(Integer)
    endereco = Column(String(200))
    telefone = Column(String(20))
    data_nascimento = Column(String(20))

    def __int__(self, nome, idade, endereco, telefone, data_nascimento):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone
        self.data_nascimento = data_nascimento


   



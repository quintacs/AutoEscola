from sqlalchemy import Column,Integer,ForeignKey,Date

from modelo import Pessoa, Base

class Instrutor(Pessoa, Base):

    __tablename__='instrutor'

    id = Column("id_instrutor", Integer,primary_key=True)
    #nome = Column(String(140))
    #idade = Column(Integer)
    #endereco = Column(String(200))
    #telefone = Column(String(20))
    #data_nascimento = Column(Date)
    agenda = Column(Date)

    pessoa =  Column(Integer, ForeignKey("pessoa.id_pessoa"),nullable=False)

    def __int__(self, nome, idade, endereco, telefone, data_nascimento, agenda):
        super().__int__( nome, idade, endereco, telefone, data_nascimento)
        self.agenda = agenda


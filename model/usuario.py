from sqlalchemy import Integer, Column, String

from model.conexao import Base, engine

class usuario (Base):
    __tablename__="usuario"
    id = Column(Integer, primary_key=True,  autoincrement=True)
    nome = Column(Integer,nullable=False)
    data =Column(String,nullable=False)

    def __init(self,nome,data):
        self.nome = nome
        self.data = data

    def to_dict(self):
        return{
            "id": self.id,
            "nome" : self.nome,
            "data" : self.data
        }

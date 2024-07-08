from db.database import Base
from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    preco = Column(Float)
    quantidade = Column(Integer)
    fornecedor_id = Column(Integer, ForeignKey("fornecedores.id"))
    

    fornecedores = relationship("Fornecedor", back_populates="produtos")

    def __init__(self, nome, preco, quantidade, fornecedor_id):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.fornecedor_id = fornecedor_id

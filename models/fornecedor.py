from db.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Fornecedor(Base):
    __tablename__ = "fornecedores"

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    contato = Column(String)

    produtos = relationship("Produto", back_populates="fornecedores")

    def __init__(self, nome, contato):
        self.nome = nome
        self.contato = contato

from db.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

class Movimentacao(Base):
    __tablename__ = 'movimentacoes'

    id = Column(Integer, primary_key=True)
    produto_id = Column(Integer, ForeignKey("produtos.id"))
    quantidade = Column(Integer)
    tipo = Column(String)
    data = Column(DateTime, server_default=func.now())

    produto = relationship("Produto")

    def __init__(self, produto_id, quantidade, tipo, data=None):
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.tipo = tipo
        self.data = data
        
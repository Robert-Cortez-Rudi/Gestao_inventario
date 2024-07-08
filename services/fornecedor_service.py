from sqlalchemy.orm import Session
from db.database import SessionLocal
from models.fornecedor import Fornecedor

class Fornecedor_Service:
    def __init__(self):
        self.db: Session = SessionLocal

    def adicionar_fornecedor(self, nome, contato):
        novo_fornecedor = Fornecedor(
            nome = nome,
            contato = contato
        )
        self.db.add(novo_fornecedor)
        self.db.commit()
        self.db.refresh(novo_fornecedor)
        return novo_fornecedor

    def listar_fornecedores(self):
        return self.db.query(Fornecedor).all()
    
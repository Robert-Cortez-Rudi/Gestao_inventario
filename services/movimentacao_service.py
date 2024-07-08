from sqlalchemy.orm import Session
from db.database import SessionLocal
from models.movimentacao import Movimentacao

class Movimentacao_Service:
    def __init__(self):
        self.db: Session = SessionLocal

    def registrar_movimento(self, produto_id, quantidade, tipo):
        nova_movimentacao = Movimentacao(
            produto_id = produto_id,
            quantidade = quantidade,
            tipo = tipo
        )
        self.db.add(nova_movimentacao)
        self.db.commit()
        self.db.refresh(nova_movimentacao)
        print("Registro realizado!")
        return nova_movimentacao


    def excluir_movimentacoes_por_produto(self, produto_id):
        movimentacoes = self.db.query(Movimentacao).filter(Movimentacao.produto_id == produto_id).all()
        for movimentacao in movimentacoes:
            self.db.delete(movimentacao)
        self.db.commit()
        print("Movimentações retiradas!")
        
from sqlalchemy.orm import Session
from db.database import SessionLocal
from models.produto import Produto
from services.movimentacao_service import Movimentacao_Service


class Produto_Service:
    def __init__(self):
        self.db: Session = SessionLocal
        self.movimentacao_service: Session = Movimentacao_Service()


    def adicionar_produto(self, nome, preco, quantidade, fornecedor_id):
        novo_produto = Produto(
            nome = nome, 
            preco = preco,
            quantidade = quantidade,
            fornecedor_id = fornecedor_id,
        )
        self.db.add(novo_produto)
        self.db.commit()
        self.db.refresh(novo_produto)
        print("Produto registrado no banco de dados!")
        self.movimentacao_service.registrar_movimento(novo_produto.id, quantidade, "Entrada")
        return novo_produto
    

    def atualizar_quantidade(self, produto_id, quantidade):
        produto = self.db.query(Produto).filter(Produto.id == produto_id).first()
        if produto:
            produto.quantidade += quantidade
            self.db.commit()
            self.db.refresh(produto)
            print("Atualização de estoque feita com sucesso!")
            self.movimentacao_service.registrar_movimento(produto.id, quantidade, "Atualização de Estoque")
            return produto
        else:
            print(f"Produto com ID {produto_id} não encontrado.")


    def mostrar_produtos(self):
        produtos = self.db.query(Produto).all()
        print("Produtos cadastrados:")
        for produto in produtos:
            print(f"ID {produto.id} - Produto: {produto.nome} - Preço: {produto.preco} - Quantidade: {produto.quantidade}")
        

    def remover_produto(self, produto_id):
        produto = self.db.query(Produto).filter(Produto.id == produto_id).first()
        if produto:
            self.db.delete(produto)
            self.db.commit()
            print("Produto removido!")
        else:
            print(f"Produto com ID {produto_id} não encontrado.")
    
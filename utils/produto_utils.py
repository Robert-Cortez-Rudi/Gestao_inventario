from services import Produto_Service, Movimentacao_Service
from utils.fornecedor_utils import listar_fornecedores, adicionar_fornecedor


def adicionar_produto(nome, preco, quantidade):
    produto_service = Produto_Service()

    listar_fornecedores()
    fornecedor_id = input("\nDigite o ID do fornecedor para o produto (ou 'NOVO' para adicionar novo fornecedor): ")
    if fornecedor_id.upper() == "NOVO":
        adicionar_fornecedor()
        listar_fornecedores()
        fornecedor_id = int(input("Digite o ID do fornecedor recém-adicionado: "))
    else:
        fornecedor_id = int(fornecedor_id)
    
    produto_service.adicionar_produto(nome, preco, quantidade, fornecedor_id)


def atualizar_quantidade(produto_id, quantidade):
    produto_service = Produto_Service()
    produto_service.atualizar_quantidade(produto_id, quantidade)


def mostrar_produtos():
    produto_service = Produto_Service()
    produto_service.mostrar_produtos()


def remover_produto(produto_id):
    produto_service = Produto_Service()
    movimentacao_service = Movimentacao_Service()
    movimentacao_service.excluir_movimentacoes_por_produto(produto_id)
    produto_service.remover_produto(produto_id)


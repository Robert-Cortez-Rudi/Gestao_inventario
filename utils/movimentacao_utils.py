from services import Movimentacao_Service

def adicionar_movimentacao(produto_id, quantidade, tipo):
    movimentacao_service = Movimentacao_Service()
    movimentacao_service.registrar_movimento(produto_id, quantidade, tipo)

def remover_movimentacoes(produto_id):
    movimentacao_service = Movimentacao_Service()
    movimentacao_service.remover_movimentacoes(produto_id)
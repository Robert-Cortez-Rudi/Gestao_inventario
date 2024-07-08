from services import Fornecedor_Service

def listar_fornecedores():
    fornecedores_service = Fornecedor_Service()
    fornecedores = fornecedores_service.listar_fornecedores()
    if fornecedores:
        print("\nFornecedores cadastrados:")
        for fornecedor in fornecedores:
            print(f"{fornecedor.id} - {fornecedor.nome} - {fornecedor.contato}")
    else:
        print("Não há fornecedores cadastrados\n")

def adicionar_fornecedor(nome_fornecedor, contato_fornecedor):
    fornecedor_service = Fornecedor_Service()
    fornecedor_service.adicionar_fornecedor(nome_fornecedor, contato_fornecedor)
    print(f"Contato: {nome_fornecedor} adicionado com sucesso!\n")

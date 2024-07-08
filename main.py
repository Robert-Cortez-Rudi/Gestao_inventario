from db import init_db
from utils import adicionar_produto, atualizar_quantidade, mostrar_produtos, remover_produto
from utils import adicionar_fornecedor, listar_fornecedores
from utils import adicionar_movimentacao
import os


if __name__ == "__main__":    
    init_db()
    while True:
        print("\n--- Sistema de Inventário ---")
        print("1 - Adicionar produto")
        print("2 - Atualizar quantidade de um produto")
        print("3 - Remover produto")
        print("4 - Mostrar todos os produtos cadastrados")
        print("5 - Adicionar fornecedor")
        print("6 - Listar fornecedores")
        print("7 - Adicionar movimentação")
        print("8 - Sair")
        opcao = input("Digite a opção desejada: ")
        os.system("cls")
        
        if opcao == "1":
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Qual será a quantidade de produtos: "))
            adicionar_produto(nome, preco, quantidade)
        
        elif opcao == "2":
            mostrar_produtos()
            id_produto = int(input("Digite o ID do produto que deseja fazer a alteração do estoque: "))
            quantidade = int(input("Qual será a quantidade de produtos que será alterada (digite negativo para retirar): "))
            atualizar_quantidade(id_produto, quantidade)

        elif opcao == "3":
            mostrar_produtos()
            produto_id = int(input("\nDigite o ID do produto que deseja remover: "))
            remover_produto(produto_id)
        
        elif opcao == "4":
            mostrar_produtos()
            
        elif opcao == "5":
            nome = input("Digite o nome do fornecedor: ")
            contato = input("Digite o contato do fornecedor: ")
            adicionar_fornecedor(nome, contato)
        
        elif opcao == "6":
            listar_fornecedores()

        elif opcao == "7":
            mostrar_produtos()
            produto_id = int(input("\nQual o ID do produto que deseja realizar um movimento: "))
            quantidade = int(input("Qual a quantidade que deseja realizar um movimento: "))
            tipo = input("Qual o tipo do movimento: ")
            adicionar_movimentacao(produto_id, quantidade, tipo)

        elif opcao == "8":
            break
        
        elif ValueError:
            print("Insira um valor válido!")

        continuar = input("\nDeseja continuar ou sair do sistema (S/N) ?: ")
        
        if continuar.upper() == "N":
            break
        else:
            continue

print("Sistema encerrado!!!")

# Gestão de Inventário 📋

Este projeto é um sistema de gerenciamento de estoque desenvolvido em Python, utilizando Programação Orientada a Objetos (POO) e SQLAlchemy para interagir com um banco de dados PostgreSQL. O sistema permite gerenciar produtos, fornecedores e registrar movimentações de estoque, facilitando o controle e a administração do inventário

## Funcionalidades do Sistema ⚙️

- **Adicionar Fornecedor:** Insere novos fornecedores no banco de dados.

- **Listar Fornecedores:** Exibe todos os fornecedores cadastrados.

- **Adicionar Produto:** Adiciona produtos vinculados a fornecedores.

- **Remover Produto:** Exclui produtos e registra a saída no estoque.

- **Atualizar Produto:** Modifica a quantidade de produtos e registra a atualização no estoque.

- **Registrar Movimentação Manual:** Adiciona movimentações no banco de dados manualmente.



## Tecnologias Utilizadas 👨‍💻

- **Python**: Linguagem de programação utilizada para desenvolver o sistema.

- **SQLAlchemy**: Biblioteca ORM (Object-Relational Mapping) que facilita a interação com o banco de dados PostgreSQL.

- **psycopg2-binary**: Adaptador de banco de dados PostgreSQL para Python, necessário para que o SQLAlchemy possa se conectar ao PostgreSQL.

- **PostgreSQL**: Sistema de gerenciamento de banco de dados relacional utilizado para armazenar os dados do sistema.

## Como utilizar o sistema 📑


1. Clone o repositório do projeto para o seu ambiente local:

```bash
git clone https://github.com/Robert-Cortez-Rudi/Gestao_inventario.git
cd Gestao_inventario
``` 

2. Instale as dependências listadas no arquivo requirements.txt:

```bash
pip install -r requirements.txt
```

3. Configurar o banco de dados:
    - Crie um banco de dados no PostgreSQL com o nome desejado.

    - Abra o arquivo **inventario_loja/db/database.py** e configure a URL do banco de dados com seu nome de usuário, senha e nome do banco de dados:

    ```bash
    user = "postgres" # Seu usuario
    password = "sua_senha" # Sua senha
    host = "localhost"
    database = "Inventario_loja" # Nome do banco de dados
    ```
    Substitua **username**, **password** e **database** pelas suas credenciais e nome do banco de dados.


4. Inicializar o Banco de Dados:
    - inicialize o banco de dados para criar todas as tabelas necessárias. Execute o script main.py para inicializar o banco de dados:


    ```bash
    python main.py
    ``` 

## Observações 👀

- Certifique-se de ter um banco de dados PostgreSQL em execução e configurado corretamente.

- Ajuste as variáveis de conexão do banco de dados no arquivo database.py de acordo com suas configurações locais.

- Este projeto poderá ter extensões futuramente para incluir funcionalidades adicionais, como relatórios mais detalhados, interface gráfica, entre outros.

## Formas de contribuir no projeto 📈

Por ser um projeto com diversas funcionalidades, possa ser que em alguns momentos o projeto tenha algumas irregularidades. Para ajudar no projeto, seja encontrando formas de tornar o código melhor elaborado ou uma forma de refatora-lo, além de opiniões para novas implementações, serão bem-vindas ao projeto!

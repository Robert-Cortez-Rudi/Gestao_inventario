from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Configuração do banco de dados

user = "postgres" # Seu usuario
password = "sua_senha" # Sua senha
host = "localhost"
database = "Inventario_loja" # Nome do banco de dados

DATABASE_URI = f"postgresql://{user}:{password}@{host}/{database}"

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)

SessionLocal = Session()

Base = declarative_base()


# Inicia o banco de dados
def init_db():
    inpsector = inspect(engine)

    # Faz a busca para saber se as tabelas ja existem no database
    tables = inpsector.get_table_names()
    if tables:
        pass
    else:
        try:
            # Cria as tabelas no banco de dados
            Base.metadata.create_all(engine)
            print("Tabelas criadas no banco de dados!")
        except Exception as e:
            print(f"Ocorreu um erro ao criar as tabelas do banco de dados: {e}")
        
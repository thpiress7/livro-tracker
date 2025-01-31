from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

# Engine do Banco de Dados
engine = create_engine("sqlite:///database.db")

# Configuração da Sessão
Session = sessionmaker(engine)

# Criando a base da tabela
Base = declarative_base()

class Livro(Base):
    __tablename__ = 'Biblioteca'
    id = Column(Integer, primary_key=True)  # ID do Livro
    nome = Column(String, nullable=False)  # Nome do Livro, não pode ser nulo
    autor = Column(String, nullable=False)  # Nome do Autor, não pode ser nulo
    ano_publicacao = Column(Integer, nullable=False)  # Ano de Publicação, não pode ser nulo

def insert_livro(name, author, year):  # Função para inserir livro no banco de dados
    session = Session()
    try:
        if all([name, author, year]):
            novo_livro = Livro(nome=name, autor=author, ano_publicacao=year)
            session.add(novo_livro)  # Adicionando o livro no banco
            session.commit()  # Confirmando a alteração no banco
            print(f"Livro '{name}' adicionado com sucesso!")  # Mensagem de sucesso
        else:
            print('É obrigatório preencher nome, nome do autor e o ano de publicação.')
    except Exception as e:
        session.rollback()  # Em caso de erro, desfaz qualquer alteração
        print(f'Erro ao tentar cadastrar o livro: {name}. Erro: {e}')
    finally:
        session.close()  # Fechando a conexão com o banco de dados

def select_name(name):
    session = Session()
    try:
        if name:  # Verifica se o nome foi fornecido
            livros = session.query(Livro).filter(Livro.nome == name).all()
            if livros:
                for i in livros:
                    print(f"\n{i.nome} - {i.autor} - ({i.ano_publicacao})")
            else:
                print('Nenhum livro encontrado com esse nome.')
        else:
            print('Nome não fornecido.')
    except Exception as e:
        print(f"Erro ao listar os livros: {e}")
    finally:
        session.close()

def select_author(author):
    session = Session()
    try:
        if author:  # Verifica se o nome do autor foi fornecido
            livros = session.query(Livro).filter(Livro.autor == author).all()
            if livros:
                for i in livros:
                    print(f"\n{i.nome} - {i.autor} - ({i.ano_publicacao})")
            else:
                print('Nenhum livro encontrado com esse autor.')
        else:
            print('Nome do autor não fornecido.')
    except Exception as e:
        print(f'Erro ao listar os livros: {e}')
    finally:
        session.close()

def select_all():
    session = Session()
    try:
        dados = session.query(Livro).all()
        if dados:
            for i in dados:
                print(f"\n{i.nome} - {i.autor} - ({i.ano_publicacao})")
        else:
            print('Nenhum livro encontrado.')
    except Exception as e:
        print(f'Erro ao listar os livros: {e}')
    finally:
        session.close()

def update_book(id, name, author, year):
    session = Session()
    try:
        if all([id, name, author, year]):
            livro = session.query(Livro).filter(Livro.id == id).first()
            if livro:
                livro.nome = name
                livro.autor = author
                livro.ano_publicacao = int(year)
                session.commit()
                print(f'Livro com ID {id} atualizado com sucesso!')
            else:
                print(f'Nenhum livro encontrado com o ID {id}.')
        else:
            print('É obrigatório informar o ID, o nome, o autor e o ano de publicação do livro para ser atualizado.')
    except Exception as e:
        session.rollback()
        print(f"Erro ao atualizar livro: {e}")
    finally:
        session.close()

def delete_book(id):
    session = Session()
    try:
        if id:
            livro = session.query(Livro).filter(Livro.id == id).first()
            if livro:
                session.delete(livro)
                session.commit()
                print(f'Livro com ID {id} deletado com sucesso!')
            else:
                print(f'Nenhum livro encontrado com o ID {id}.')
        else:
            print('É obrigatório informar o ID do livro a ser deletado.')
    except Exception as e:
        session.rollback()
        print(f'Erro ao tentar deletar livro com ID {id}: {e}')
    finally:
        session.close()

def menu():
    while True:
        print("\nMenu:")
        print("1 - Adicionar livro")
        print("2 - Listar livros por nome")
        print("3 - Listar livros por autor")
        print("4 - Listar todos os livros")
        print("5 - Deletar livro")
        print("6 - Atualizar livro")
        print("7 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            name = input("Digite o nome do livro: ")
            author = input("Digite o nome do autor: ")
            year = input("Digite o ano de publicação: ")
            insert_livro(name, author, year)
        elif opcao == '2':
            name = input("Digite o nome do livro: ")
            select_name(name)
        elif opcao == '3':
            author = input("Digite o nome do autor: ")
            select_author(author)
        elif opcao == '4':
            select_all()
        elif opcao == '5':
            id = input("Digite o ID do livro que deseja deletar: ")
            delete_book(id)
        elif opcao == '6':
            id = int(input("Digite o ID do livro que deseja atualizar: "))
            name = input("Digite o novo nome do livro: ")
            author = input("Digite o novo autor: ")
            year = input("Digite o novo ano de publicação: ")
            update_book(id, name, author, year)
        elif opcao == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == '__main__':
    Base.metadata.create_all(engine)  # Criando tabela no banco de dados
    menu()

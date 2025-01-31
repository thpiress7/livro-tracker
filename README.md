# LivroTracker

**LivroTracker** é uma aplicação de gerenciamento de biblioteca pessoal, projetada para armazenar, organizar e manipular informações sobre livros. Desenvolvido em Python, o projeto utiliza a biblioteca SQLAlchemy para interagir com um banco de dados SQLite, proporcionando uma interface simples para realizar operações como adicionar, atualizar, listar e deletar livros.

## Funcionalidades

O **LivroTracker** permite aos usuários gerenciar sua coleção de livros de maneira eficiente, oferecendo as seguintes funcionalidades:

- **Adicionar Livro**: Permite ao usuário adicionar um novo livro à biblioteca, com informações sobre nome, autor e ano de publicação.
- **Listar Livros por Nome**: Realiza a busca por nome do livro e exibe os livros encontrados.
- **Listar Livros por Autor**: Realiza a busca por autor e exibe os livros encontrados.
- **Listar Todos os Livros**: Exibe todos os livros registrados na base de dados.
- **Atualizar Livro**: Permite atualizar as informações de um livro existente, incluindo nome, autor e ano de publicação.
- **Deletar Livro**: Permite a exclusão de um livro da biblioteca.

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação principal utilizada para o desenvolvimento do projeto.
- **SQLAlchemy**: Biblioteca de ORM (Object Relational Mapper) para interação com o banco de dados SQLite.
- **SQLite**: Banco de dados relacional leve utilizado para armazenar informações sobre os livros.

## Requisitos

- Python 3.6 ou superior
- [Poetry](https://python-poetry.org/) (gerenciador de dependências recomendado)
- SQLite (será automaticamente configurado durante a execução)

## Instalação

### 1. Clonando o repositório:

Primeiro, clone o repositório para sua máquina local:

```bash
git clone https://github.com/SEU_USUARIO/LivroTracker.git
cd LivroTracker

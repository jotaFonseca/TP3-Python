import re

# Função para formatar o nome e sobrenome com iniciais em maiúsculo
def format_name():
    nome = input("Digite seu nome e sobrenome: ")
    nome_sobrenome = nome.split()
    nome_formatado = [nome.capitalize() for nome in nome_sobrenome]
    return nome_formatado

# Função para verificar se o email é válido
def is_valid_email(email):
    regex = r'^[a-zA-Z]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

# Função para solicitar um email válido
def get_valid_email():
    while True:
        email = input("Digite seu endereço de email: ")
        if is_valid_email(email):
            return email
        else:
            opcao = input("O endereço de email inserido é inválido. Deseja tentar novamente? (S/N): ")
            if opcao.lower() != 's':
                return False

# Função para realizar busca por nome ou sobrenome
def search_name_or_lastname(database, search_term, search_lastname=False):
    resultados = []
    for i, registro in enumerate(database):
        if search_lastname:
            if search_term.capitalize() == registro[1]:
                resultados.append((i, registro))
        else:
            if search_term.capitalize() == registro[0]:
                resultados.append((i, registro))
    return resultados

# Função para cadastrar usuário
def cadastrar_usuario(database):
    nome = format_name()
    email = get_valid_email()
    if email:
        database.append([nome[0], nome[1], email])
        print("Usuário cadastrado com sucesso!")
    else:
        print("Cadastro cancelado.")
    return database

# Função para pesquisar no banco de dados
def pesquisar(database):
    termo = input("Digite o nome ou sobrenome que deseja pesquisar: ")
    opcao = input("Você está pesquisando pelo nome (N) ou sobrenome (S)? ")
    search_lastname = True if opcao.lower() == 's' else False
    resultados = search_name_or_lastname(database, termo, search_lastname)
    if resultados:
        print("Resultados encontrados:")
        for i, (idx, registro) in enumerate(resultados):
            print(f"ID: {idx + 1}, Nome: {registro[0]} {registro[1]}, Email: {registro[2]}")
    else:
        print("Nenhum resultado encontrado.")

# Função para listar os usuários cadastrados com seus índices
def listar_usuarios(database):
    print("Usuários cadastrados:")
    for i, usuario in enumerate(database):
        print(f"{i + 1}: {usuario[0]} {usuario[1]} - {usuario[2]}")

# Função para exibir o menu de opções
def menu(database):
    while True:
        print("\n--- Menu ---")
        print("1. Cadastrar novo usuário")
        print("2. Listar usuários cadastrados")
        print("3. Pesquisar usuário")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_usuario(database)
        elif opcao == '2':
            listar_usuarios(database)
        elif opcao == '3':
            pesquisar(database)
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Banco de dados de exemplo
banco_de_dados = []

# Exemplo de uso:
menu(banco_de_dados)

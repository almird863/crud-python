import sqlite3
cx = sqlite3.connect('Database.db')
cs = cx.cursor()

menu = "0"
##################################
#            Funções
##################################


def criar_banco():
    cs.execute(f'''
                CREATE TABLE IF NOT EXISTS Filmes (
                    Id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Nome TEXT NOT NULL,
                    Genero TEXT,
                    Duracao REAL,
                    Diretor TEXT,
                    Avaliacao INTEGER )
                    ''')
    cx.commit()
    print("\nTabela criada com sucesso.")


def adicionar_registro():
    nome = input("\nDigite o nome do filme:\n> ").title()
    while nome == "" or nome.isspace() == True:
        print("\nO nome precisa ser válido.")
        nome = input("\nDigite o nome do filme:\n> ").title()

    genero = input("\nDigite o gênero do filme:\n> ").capitalize()
    while genero == "" or genero.isspace() == True:
        print("\nO nome precisa ser válido.")
        genero = input("\nDigite o gênero do filme:\n> ").title()

    duracao = ""
    while duracao == "":
        try:
            duracao = float(
                input("\nDigite a duração do filme (Exemplo: horas.minutos):\n> "))
        except ValueError:
            print("\nA duração do filme precisa ser um valor numérico.")
            duracao = ""

    diretor = input("\nDigite o nome do diretor:\n> ")
    while diretor == "" or diretor.isspace() == True:
        print("\nO nome precisa ser válido.")
        diretor = input("\nDigite o diretor do filme:\n> ").title()

    avaliacao = ""
    while avaliacao == "":
        try:
            avaliacao = int(
                input("\nDigite a avaliação do filme (1 a 10):\n> "))
        except ValueError:
            print("\nA avaliação do filme precisa ser um valor numérico.")
            avaliacao = ""

    if nome != "":
        cs.execute(f'''
                INSERT INTO Filmes (Nome, Genero, Duracao, Diretor, Avaliacao)
                VALUES ('{nome}', '{genero}', '{duracao}', '{diretor}', '{avaliacao}')
                ''')
        cx.commit()
        print(
            f"\n\33[32mFilme {nome} foi inserido no banco de dados com sucesso.\33[0m\n")


def atualizar_registro():
    print()
    print("Escolha o que deseja atualizar:")
    print("1 - Genero")
    print("2 - Duração")
    print("3 - Diretor")
    print("4 - Avaliação")
    menu_interno = input("> ")

    if menu_interno == '1':
        resultados = listar_filmes()

        if resultados != []:
            print()
            for i in resultados:
                print(f"ID: {i[0]} || Nome: {i[1]} || Gênero: {i[2]}")

            id = ""
            while id == "":
                try:
                    id = int(input("\nConfirme o ID do filme que quer atualizar:\n> "))
                except ValueError:
                    print("O ID precisa ser um valor numérico.")

            genero = input(f"\nDigite o novo gênero do filme:\n> ").capitalize()

            if genero != "":
                cs.execute(f'''
                            update or replace Filmes set Genero = '{genero}' where Id = '{id}'
                            ''')
                cx.commit()

                print(
                    f"\n\33[32mO filme foi atualizado com o gênero '{genero}'\33[0m\n")

            else:
                print("\nO campo não pode estar vazio.")
                atualizar_registro()
        else:
            print("Não há filmes com esse nome")

    if menu_interno == '2':
        resultados = listar_filmes()

        if resultados != []:
            print()
            for i in resultados:
                print(f"ID: {i[0]} || Nome: {i[1]} || Duração: {i[3]}")

            id = ""
            while id == "":
                try:
                    id = int(input("\nConfirme o ID do filme que quer atualizar:\n> "))
                except ValueError:
                    print("O ID precisa ser um valor numérico.")

            duracao = input(f"\nDigite a nova duração do filme:\n> ")

            if duracao != "":
                cs.execute(f'''
                            update or replace Filmes set Duracao = '{duracao}' where Id = '{id}'
                            ''')
                cx.commit()

                print(f"\n\33[32mO filme foi atualizado com a duração: '{duracao}'\n\33[0m")

            else:
                print("\nO campo não pode estar vazio.")
                atualizar_registro()

        else:
            print("Não há filmes com esse nome")

    if menu_interno == '3':
        resultados = listar_filmes()

        if resultados != []:
            print()
            for i in resultados:
                print(f"ID: {i[0]} || Nome: {i[1]} || Diretor: {i[4]}")

            id = ""
            while id == "":
                try:
                    id = int(input("\nConfirme o ID do filme que quer atualizar:\n> "))
                except ValueError:
                    print("O ID precisa ser um valor numérico.")

            diretor = input(
                f"\nDigite o novo diretor do filme:\n> ")

            if diretor != "":
                cs.execute(f'''
                            update or replace Filmes set Diretor = '{diretor}' where Id = '{id}'
                            ''')
                cx.commit()

                print(
                    f"\n\33[32mO filme foi atualizado com o diretor: '{diretor}'\33[0m\n")

            else:
                print("\nO campo não pode estar vazio.")
                atualizar_registro()

        else:
            print("Não há filmes com esse nome")

    if menu_interno == '4':
        resultados = listar_filmes()

        if resultados != []:
            print()
            for i in resultados:
                print(f"ID: {i[0]} || Nome: {i[1]} || Avaliação: {i[5]}")

            id = ""
            while id == "":
                try:
                    id = int(input("\nConfirme o ID do filme que quer atualizar:\n> "))
                except ValueError:
                    print("O ID precisa ser um valor numérico.")

            avaliacao = float(input(f"\nDigite a nova avaliação do filme:\n> "))

            if avaliacao != "":
                cs.execute(f'''
                            update or replace Filmes set Avaliacao = '{avaliacao}' where Id = '{id}'
                            ''')
                cx.commit()

                print(f"\n\33[32mO filme foi atualizado com a avaliação: '{avaliacao}'\33[0m\n")

            else:
                print("\nO campo não pode estar vazio.")
                atualizar_registro()

        else:
            print("Não há filmes com esse nome")


def deletar_registro():
    resultados = listar_filmes()

    if resultados != []:
        print()
        for i in resultados:
            print(f"ID: {i[0]} || Nome: {i[1]} || Genero: {i[2]} || Duração: {i[3]}")

        id = ""
        while id == "":
            try:
                id = int(input("\nConfirme o ID do filme que quer DELETAR:\n> "))
            except ValueError:
                print("O ID precisa ser um valor numérico.")

    cs.execute(f'''
            delete from Filmes where Id = {id}
            ''')
    cx.commit()

    print("\n\33[31mRegistro excluido com sucesso.\33[0m\n")


def listar_filmes():
    nome = input("\nDigite o nome do filme para listar: (digite '*' para listar todos)\n> ").title()
    if nome == "" or nome.isspace() == True:
        print("\nDigite um nome válido.\n")
        return
    else:
        if nome == '*':
            cs.execute(f'''
                    select * from Filmes
                    ''')
            cx.commit()
            return cs.fetchall()
        else:
            cs.execute(f'''
                    select * from Filmes where Nome = '{nome}'
                    ''')
            cx.commit()
            return cs.fetchall()


##########################################
#                CÓDIGO
##########################################


while menu != "6":
    print("Escolha uma opção:")
    print("\33[32m1\33[0m - Criar tabela no banco de dados")
    print("\33[32m2\33[0m - Listar Filmes")
    print("\33[32m3\33[0m - \33[32mInserir registro\33[0m")
    print("\33[32m4\33[0m - \33[33mAtualizar registro\33[0m")
    print("\33[32m5\33[0m - \33[31mDeletar registro\33[0m")
    print("\33[32m6\33[0m - Fechar programa")
    menu = input("> ")

    if menu == "1":
        criar_banco()
    if menu == "2":
        resultados = listar_filmes()
        try:
            if resultados != []:
                print()
                for i in resultados:
                    print(
                        f"ID: {i[0]} || Nome: {i[1]} || Genero: {i[2]} || Duração: {i[3]}")
                print()
            else:
                print("Não há filmes com esse nome")
        except Exception as e:
            print("Erro ao procurar filme.\n")

    if menu == "3":
        adicionar_registro()
    if menu == "4":
        atualizar_registro()
    if menu == "5":
        deletar_registro()
    if menu == "6":
        print("Fechando programa......................")

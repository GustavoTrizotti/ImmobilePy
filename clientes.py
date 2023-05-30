# Bibliotecas
# ------------------------------------------------------------------------------------------

from auxiliares import *

# ------------------------------------------------------------------------------------------
# FUNÇÕES - CLIENTES
# ------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------
#                                           Existe Cliente
# ------------------------------------------------------------------------------------------

def existeCliente(dic, chave):
    if chave in dic.keys():
        return True
    else:
        return False
# ------------------------------------------------------------------------------------------
#                                               Inserir
# ------------------------------------------------------------------------------------------

def inserir_clientes(dic):
    print("--" * 15)
    CPF = input("Digite o CPF: ")
    if existeCliente(dic, CPF):
        print("Esta pessoa já está cadastrada!")
        pausa()
    else:
        nome = input("Nome: ")
        data = input("Data de Nascimento: ")
        salario = float(input("Salário: "))
        email = input("E-mail: ")
        telefone = input("Telefone: ")

        dic[CPF] = (nome, data, salario, email, telefone)
        print("\nDados inseridos com sucesso!")
        pausa()

# ------------------------------------------------------------------------------------------
#                                               Exibir
# ------------------------------------------------------------------------------------------

def exibir_clientes(dic, chave):
    if existeCliente(dic, chave):
        dados = dic[chave]
        print()
        print(f"Nome: {dados[0]}")
        print(f"Data de Nascimento: {dados[1]}")
        print(f"Salário: {dados[2]}")
        print(f"E-mail: {dados[3]}")
        print(f"Telefone: {dados[4]}")
    else:
        print("Cadastro não existente!")
        pausa()

# ------------------------------------------------------------------------------------------
#                                               Alterar
# ------------------------------------------------------------------------------------------

def alterar_clientes(dic, chave):
    if existeCliente(dic, chave):
        exibir_clientes(dic, chave)
        print("--" * 15)
        confirma = input("Deseja alterar os dados? S/N: ").upper()
        if confirma == "S":
            print()
            nome = input("Nome: ")
            data = input("Data de Nascimento: ")
            salario = float(input("Salário: "))
            email = input("E-mail: ")
            telefone = input("Telefone: ")
            dic[chave] = (nome, data, salario, email, telefone)
            print("Alteração concluída com sucesso!")
            pausa()
        else:
            print("Alteração cancelada.")
            pausa()
    else:
        print("Cadastro não existente!")
        pausa()

# ------------------------------------------------------------------------------------------
#                                             Remover
# ------------------------------------------------------------------------------------------

def remover_clientes(dic, chave):
    if existeCliente(dic, chave):
        exibir_clientes(dic, chave)
        confirma = input("Deseja remover os dados? S/N: ").upper()
        if confirma == "S":
            del dic[chave]
            print("Dados removidos com sucesso!")
            pausa()
        else:
            print("Remoção cancelada.")
    else:
        print("Cadastro não existente!")
        pausa()

# ------------------------------------------------------------------------------------------
#                                           Exibir Todos
# ------------------------------------------------------------------------------------------

def exibir_todos_clientes(dic):
    print("--" * 15)
    print("Relatório - Clientes")
    print()
    print("CPF - Nome - Endereço - Salário - Data Nascimento - Telefone\n")
    for CPF in dic:
        tupla = dic[CPF]
        string = CPF + " - " + tupla[0] + " - " + tupla[1] + " - " + str(tupla[2]) + " - " + tupla[3] + " - " + tupla[4]
        print(string)
    print()
    pausa()

# ------------------------------------------------------------------------------------------
#                                              Gravar
# ------------------------------------------------------------------------------------------

def grava_clientes(dic):
    arq = open("clientes.txt", "w")
    for CPF in dic:
        tupla = dic[CPF]
        linha = CPF + ";" + tupla[0] + ";" + tupla[1] + ";" + str(tupla[2]) + ";" + tupla[3] + ";" + tupla[4] + "\n"
        arq.write(linha)
    arq.close()

# ------------------------------------------------------------------------------------------
#                                             Recuperar
# ------------------------------------------------------------------------------------------

def recupera_clientes(dic):
    if existe_arquivo("clientes.txt"):
        arq = open("clientes.txt", "r")
        for linha in arq:
            linha = linha[:len(linha)-1]
            lista = linha.split(";")
            CPF = lista[0]
            nome = lista[1]
            endereco = lista[2]
            renda = float(lista[3])
            data = lista[4]
            telefone = lista[5]
            dic[CPF] = (nome, endereco, renda, data, telefone)

# ------------------------------------------------------------------------------------------
#                                           Menu - Clientes
# ------------------------------------------------------------------------------------------

def menu_clientes(dic):
    c = 0
    while c < 6:
        print("--" * 15)
        print("Gerenciamento - Pessoas")
        print("--" * 15)
        print("1 - Inserir")
        print("2 - Alterar")
        print("3 - Remover")
        print("4 - Exibir Cliente")
        print("5 - Exibir todos Clientes")
        print("6 - Voltar para o Menu")
        print("--" * 15)

        c = int(input("\nOpção: "))
        print()
        if c < 1 or c > 6:
            print("Opção Inválida")
        else:
            if c == 1:
                inserir_clientes(dic)
            elif c == 2:
                CPF = input("Digite o CPF para Alterar: ")
                alterar_clientes(dic, CPF)
            elif c == 3:
                CPF = input("Digite o CPF para Remover: ")
                remover_clientes(dic, CPF)
            elif c == 4:
                CPF = input("Digite o CPF para Exibir: ")
                exibir_clientes(dic, CPF)
            elif c == 5:
                exibir_todos_clientes(dic)
            elif c == 6:
                grava_clientes(dic)

# ------------------------------------------------------------------------------------------

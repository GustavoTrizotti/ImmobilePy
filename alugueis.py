# ------------------------------------------------------------------------------------------
# Bibliotecas
# ------------------------------------------------------------------------------------------

from datetime import *
from auxiliares import *
from clientes import *
from imoveis import *

# ------------------------------------------------------------------------------------------
# FUNÇÕES
# ------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------
#                                           Existe Aluguel
# ------------------------------------------------------------------------------------------

def existeAluguel(dic, chave):
    if chave in dic.keys():
        return True
    else:
        return False

# ------------------------------------------------------------------------------------------
#                                               Inserir
# ------------------------------------------------------------------------------------------

def insere_aluguel(dicC, dicI, dicA):
    CPF = input("Digite o CPF: ")
    if existeAluguel(dicC, CPF):
        codigo = input("Digite o Código do Imóvel: ")
        if existeAluguel(dicI, codigo):
            data = input("Data de Entrada: ")
            chave = (CPF, codigo, data)
            if existeAluguel(dicA, chave):
                print("Este aluguél já existe!")
                pausa()
            else:
                nomes_moradores = []
                nome = input("Nome Morador: ")
                while nome != "":
                    nomes_moradores.append(nome)
                    nome = input("Nome Morador: ")

                if len(nomes_moradores) == 0:
                    nomes_moradores.append("Este aluguél não tem moradores")

                valor = float(input("Valor Mensal: R$ "))
                    
                dicA[chave] = (nomes_moradores, valor)
        else:
            print("Este imóvel não existe!")
            pausa()
    else:
        print("Este CPF não existe!")
        pausa()

# ------------------------------------------------------------------------------------------
#                                               Exibir
# ------------------------------------------------------------------------------------------

def exibir_aluguel(dicC, dicI, dicA, CPF, codigo, data):
    chave = (CPF, codigo, data)
    if existeAluguel(dicA, chave):
        dados = dicA[chave]
        print("--" * 15)
        print("Dados - Aluguéis")
        print()
        # Dados Cliente
        print("--" * 15)
        print("Cliente: ")
        exibir_clientes(dicC, CPF)
        # Dados Imovel
        print("--" * 15)
        print("Imóvel: ")
        exibir_imoveis(dicI, codigo)
        # Dados Aluguel
        print("--" * 15)
        print("Aluguel: ")
        print()
        nomes_moradores = " - ".join(dados[0])
        print(f"Nomes Moradores: {nomes_moradores}")
        print(f"Valor Mensal: {dados[1]}")
        print()
    else:
        print("Este aluguél não existe!")
        pausa()

# ------------------------------------------------------------------------------------------
#                                               Alterar
# ------------------------------------------------------------------------------------------

def alterar_aluguel(dicC, dicI, dicA, CPF, codigo, data):
    chave = (CPF, codigo, data)
    if existeAluguel(dicA, chave):
        exibir_aluguel(dicC, dicI, dicA, CPF, codigo, data)
        confirma = input("Deseja alterar? (S/N)").upper()
        if confirma == "S":
            nomes_moradores = []
            nome = input("Nome Morador: ")
            while nome != "":
                nomes_moradores.append(nome)
                nome = input("Nome Morador: ")

            if len(nomes_moradores) == 0:
                nomes_moradores.append("Este aluguél não tem moradores")

            valor = float(input("Valor Mensal: R$ "))
            tupla = (nomes_moradores, valor)
            dicA[chave] = tupla
            pausa()
        else:
            print("Operação cancelada!")
            pausa()
    else:
        print("Este aluguél não existe!")
        pausa()

# ------------------------------------------------------------------------------------------
#                                               Remover
# ------------------------------------------------------------------------------------------

def remover_aluguel(dicC, dicI, dicA, CPF, codigo, data):
    chave = (CPF, codigo, data)
    if existeAluguel(dicA, chave):
        exibir_aluguel(dicC, dicI, dicA, CPF, codigo, data)
        confirma = input("Deseja remover? (S/N): ").upper()
        if confirma == "S":
            del dicA[chave]
            pausa()
        else:
            print("Operação cancelada!")
            pausa()
    else:
        print("Este aluguél não existe!")
        pausa()

# ------------------------------------------------------------------------------------------
#                                              Exibir Todos
# ------------------------------------------------------------------------------------------

def exibir_todos_alugueis(dicC, dicI, dicA):
    for chave in dicA:
        CPF = chave[0]
        codigo = chave[1]
        data = chave[2]
        exibir_aluguel(dicC, dicI, dicA, CPF, codigo, data)
    print()
    pausa()

# ------------------------------------------------------------------------------------------
#                                               Gravar
# ------------------------------------------------------------------------------------------

def grava_alugueis(dic):
    arq = open("aluguel.txt", "w")
    for chave in dic:
        CPF = chave[0]
        codigo = chave[1]
        data = chave[2]
        tupla = dic[chave]
        nomes_moradores = " - ".join(tupla[0])
        valor = tupla[1]
        linha = CPF + ";" + codigo + ";" + data + ";" + nomes_moradores + ";" + str(valor)
        arq.write(linha)
    arq.close()

# ------------------------------------------------------------------------------------------
#                                             Recuperar
# ------------------------------------------------------------------------------------------

def recupera_alugueis(dic):
    if existe_arquivo("aluguel.txt"):
        arq = open("aluguel.txt", "r")
        for linha in arq:
            linha = linha[:len(linha)-1]
            lista = linha.split(";")
            CPF = lista[0]
            codigo = lista[1]
            data = lista[2]
            nomes = lista[3]
            nomes_moradores = nomes.split(" - ")
            valor = float(lista[4])
            chave = (CPF, codigo, data)
            dic[chave] = (nomes_moradores, valor)

# ------------------------------------------------------------------------------------------
#                                           Menu - Aluguéis
# ------------------------------------------------------------------------------------------

def menu_alugueis(dicC, dicI, dicA):
    c = 0
    while c < 6:
        print("--" * 15)
        print("Gerenciamento - Aluguéis")
        print("--" * 15)
        print("1 - Inserir")
        print("2 - Alterar")
        print("3 - Remover")
        print("4 - Exibir Aluguel")
        print("5 - Exibir todos Alugéis")
        print("6 - Voltar para o Menu")
        print("--" * 15)

        c = int(input("\nOpção: "))
        print()
        if c < 1 or c > 6:
            print("Opção Inválida")
            pausa()
        else:
            if c == 1:
                insere_aluguel(dicC, dicI, dicA)
            elif c == 2:
                CPF = input("Digite o CPF: ")
                codigo = input("Digite o Código: ")
                data = input("Digite a Data de Entrada: ")
                alterar_aluguel(dicC, dicI, dicA, CPF, codigo, data)
            elif c == 3:
                CPF = input("Digite o CPF: ")
                codigo = input("Digite o Código: ")
                data = input("Digite a Data de Entrada: ")
                remover_aluguel(dicC, dicI, dicA, CPF, codigo, data)
            elif c == 4:
                CPF = input("Digite o CPF: ")
                codigo = input("Digite o Código: ")
                data = input("Digite a Data de Entrada: ")
                exibir_aluguel(dicC, dicI, dicA, CPF, codigo, data)
            elif c == 5:
                exibir_todos_alugueis(dicC, dicI, dicA)
            elif c == 6:
                grava_alugueis(dicA)

# ------------------------------------------------------------------------------------------
#                                             Relatório
# ------------------------------------------------------------------------------------------

def relatorio(dicC, dicI, dicA, X, Y):
    print(f"Relatório - Aluguéis com Data de Entrada entre {X} e {Y}.")
    print()
    for chave in dicA:
        # Chave - ('111', '11', '29/11/2021')
        data = chave[2]
        data_entrada = datetime.strptime(data, '%d/%m/%Y')
        if len(X) > 4 and len(Y) > 4:
            xDate = datetime.strptime(X, '%d/%m/%Y')
            yDate = datetime.strptime(Y, '%d/%m/%Y')
            if data_entrada >= xDate and data_entrada <= yDate:
                CPF = chave[0]
                codigo = chave[1]
                exibir_aluguel(dicC, dicI, dicA, CPF, codigo, data)
                print()
            else:
                print("Nenhum cadastro detectado nas datas informadas!")
                pausa()
        else:
            dataX = X
            dataY = Y
            anoX = datetime.strptime(dataX, '%Y')
            anoY = datetime.strptime(dataY, '%Y')
            if data_entrada >= anoX and data_entrada <= anoY:
                CPF = chave[0]
                codigo = chave[1]
                exibir_aluguel(dicC, dicI, dicA, CPF, codigo, data)
                print()
            else:
                print("Nenhum cadastro detectado nas datas informadas!")
                pausa()

# ------------------------------------------------------------------------------------------

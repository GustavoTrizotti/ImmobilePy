# ---------------------------------------------------------------------------------
#                                    Bibliotecas
# ---------------------------------------------------------------------------------

from auxiliares import *

# BD = {}
# [Código] = (Descrição, Endereço, Tipo, Valor alguel)

# ---------------------------------------------------------------------------------
#                                    Existe Imóvel
# ---------------------------------------------------------------------------------

def existeImovel(dic, chave):
    if chave in dic.keys():
        return True
    else:
        return False

# ---------------------------------------------------------------------------------
#                                      Inserir
# ---------------------------------------------------------------------------------

def inserir_imoveis(dic):
    codigo = input("Digite o Código: ")
    if existeImovel(dic, codigo):
        print("Imóvel já cadastrado!")
        pausa()
    else:
        descricao = input("Descrição: ")
        endereco = input("Endereço: ")
        tipo = input("Tipo Imóvel: ")
        valor = float(input("Valor Aluguél: "))

        dic[codigo] = (descricao, endereco, tipo, valor)
        print("Dados inseridos com sucesso!")
        pausa()

# ---------------------------------------------------------------------------------
#                                      Exibir
# ---------------------------------------------------------------------------------

def exibir_imoveis(dic, chave):
    if existeImovel(dic, chave):
        dados = dic[chave]
        print()
        print(f"Descrição: {dados[0]}")
        print(f"Endereço: {dados[1]}")
        print(f"Tipo do Imóvel: {dados[2]}")
        print(f"Valor Aluguél: {dados[3]}")
    else:
        print("Cadastro não existente!")
        pausa()

# ---------------------------------------------------------------------------------
#                                      Alterar
# ---------------------------------------------------------------------------------

def alterar_imoveis(dic, chave):
    if existeImovel(dic, chave):
        exibir_imoveis(dic, chave)
        confirma = input("Deseja alterar os dados? S/N: ").upper()
        if confirma == "S":
            print()
            descricao = input("Descrição: ")
            endereco = input("Endereço: ")
            tipo = input("Tipo Imóvel: ")
            valor = float(input("Valor Aluguél: "))
            print()
            dic[chave] = (descricao, endereco, tipo, valor)
            print("Dados Alterados com sucesso!") 
            pausa()
        else:
            print("Alteração cancelada.")
            pausa()
    else:
        print("Cadastro não existente!")
        pausa()

# ---------------------------------------------------------------------------------
#                                      Remover
# ---------------------------------------------------------------------------------

def remover_imoveis(dic, chave):
    if existeImovel(dic, chave):
        exibir_imoveis(dic, chave)
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

# ---------------------------------------------------------------------------------
#                                     Exibir Todos
# ---------------------------------------------------------------------------------

def exibir_todos_imoveis(dic):
    print("--" * 15)
    print("Relatório - Imóveis")
    print()
    print("Código - Descrição - Endereço - Tipo - Valor do Aluguél\n")
    for codigo in dic:
        tupla = dic[codigo]
        string = codigo + " - " + tupla[0] + " - " + tupla[1] + " - " + tupla[2] + " - " + str(tupla[3])
        print(string)
    print()
    pausa()

# ---------------------------------------------------------------------------------
#                                        Gravar
# ---------------------------------------------------------------------------------

def grava_imoveis(dic):
    arq = open("imoveis.txt", "w")
    for codigo in dic:
        tupla = dic[codigo]
        linha = codigo + ";" + tupla[0] + ";" + tupla[1] + ";" + tupla[2] + ";" + str(tupla[3]) + "\n"
        arq.write(linha)
    arq.close()

# ---------------------------------------------------------------------------------
#                                      Recuperar
# ---------------------------------------------------------------------------------

def recupera_imoveis(dic):
    if existe_arquivo("imoveis.txt"):
        arq = open("imoveis.txt", "r")
        for linha in arq:
            linha = linha[:len(linha)-1]
            lista = linha.split(";")
            codigo = lista[0]
            descricao = lista[1]
            endereco = lista[2]
            tipo = lista[3]
            valor = lista[4]
            dic[codigo] = (descricao, endereco, tipo, valor)

# ---------------------------------------------------------------------------------
#                                     Menu Imóveis
# ---------------------------------------------------------------------------------

def menu_imoveis(dic):
    c = 0
    while c < 6:
        print("--" * 15)
        print("Gerenciamento - Imóveis")
        print("--" * 15)
        print("1 - Inserir")
        print("2 - Alterar")
        print("3 - Remover")
        print("4 - Exibir Imóvel")
        print("5 - Exibir todos Imóveis")
        print("6 - Voltar para o Menu")
        print("--" * 15)

        c = int(input("\nOpção: "))
        print()
        if c < 1 or c > 6:
            print("Opção Inválida")
        else:
            if c == 1:
                inserir_imoveis(dic)
            elif c == 2:
                codigo = input("Digite o Código para Alterar: ")
                alterar_imoveis(dic, codigo)
            elif c == 3:
                codigo = input("Digite o Código para Remover: ")
                remover_imoveis(dic, codigo)
            elif c == 4:
                codigo = input("Digite o Código para Exibir: ")
                exibir_imoveis(dic, codigo)
            elif c == 5:
                exibir_todos_imoveis(dic)
            elif c == 6:
                grava_imoveis(dic)

# ---------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Bibliotecas
# ------------------------------------------------------------------------------

from clientes import *
from imoveis import *
from alugueis import *
from auxiliares import *

# ------------------------------------------------------------------------------
# Banco de Dados
# ------------------------------------------------------------------------------

BD_clientes = {}
BD_imoveis = {}
BD_alugueis = {}

# ------------------------------------------------------------------------------
# Recuperando Arquivos
# ------------------------------------------------------------------------------

recupera_clientes(BD_clientes)
recupera_imoveis(BD_imoveis)
recupera_alugueis(BD_alugueis)

# ------------------------------------------------------------------------------
# Menu Principal
# ------------------------------------------------------------------------------

c = 0
while c < 5:
    print("--" * 15)
    print("Menu")
    print("--" * 15)
    print("1 - Submenu de Clientes")
    print("2 - Submenu de Imóveis")
    print("3 - Submenu de Aluguéis")
    print("4 - Relatório")
    print("5 - Sair")
    print("--" * 15)

    c = int(input("\nOpção: "))
    print()
    if c == 1:
        menu_clientes(BD_clientes)
        print("\nVoltando para o menu...\n")
    elif c == 2:
        menu_imoveis(BD_imoveis)
        print("\nVoltando para o menu...\n")
    elif c == 3:
        menu_alugueis(BD_clientes, BD_imoveis, BD_alugueis)
        print("\nVoltando para o menu...\n")
    elif c == 4:
        X = input("Data Inicial: ")
        Y = input("Data Final: ")
        relatorio(BD_clientes, BD_imoveis, BD_alugueis, X, Y)
print("Fim do programa.")

# ------------------------------------------------------------------------------
# Fim do Programa
# ------------------------------------------------------------------------------

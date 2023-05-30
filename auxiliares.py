# Funções Auxiliares
# ----------------------------

def existe_arquivo(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False
    
def pausa():
    input("Aperte <enter> para continuar...")
    print()

# Implemente uma função que altere uma lista,
# de forma que os valores positivos fiquem negativos e os 
# negativos fiquem positivos. Esta função deve ter o protótipo:

class no:
    def __init__(self, item):
        self.item = item
        self.proximo = None

def lista_altera(lst):
    atual = lst
    while atual is not None:
        atual.item = -atual.item
        atual = atual.proximo
    return lst

def inserirItem(lista, item):
    novoItem = no(item)
    novoItem.proximo = lista
    lista = novoItem
    return lista

def listarItens(lista):
    atual = lista
    while atual is not None:
        print(atual.item)
        atual = atual.proximo

def main():
    lista = None
    lista = inserirItem(lista, 10)
    lista = inserirItem(lista, -20)
    lista = inserirItem(lista, 30)
    lista = inserirItem(lista, -40)
    lista = inserirItem(lista, 50)
    print("Lista original:")
    listarItens(lista)
    lista_altera(lista)
    print("Lista alterada:")
    listarItens(lista)
main()
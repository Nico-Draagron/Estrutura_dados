# Implemente uma função que insira elementos sempre ao 
# final da lista. Esta função deve ter o protótipo:

class no:
    def __init__(self, item):
        self.item = item
        self.proximo = None

def lista_insere_final(lst, valor):
    novo_no = no(valor)
    if lst is None:
        return novo_no
    atual = lst
    while atual.proximo is not None:
        atual = atual.proximo
    atual.proximo = novo_no
    return lst

def listarItens(lista):
    atual = lista
    while atual is not None:
        print(atual.item)
        atual = atual.proximo

def inserirItem(lista, item):
    novoItem = no(item)
    novoItem.proximo = lista
    lista = novoItem
    return lista

def main():
    lista = None
    lista = inserirItem(lista, 10)
    lista = inserirItem(lista, 20)
    lista = inserirItem(lista, 5) 
    lista = lista_insere_final(lista, 1)
    lista = inserirItem(lista, 15)
    lista = lista_insere_final(lista, 25)
    listarItens(lista)

main()
        

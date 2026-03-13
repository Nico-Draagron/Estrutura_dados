# Implemente uma função que tenha como valor de retorno a referência
# do último nó de uma lista encadeada. Esta função deve obedecer ao 
# protótipo:

class No:
    def __init__(self, item):
        self.item = item
        self.proximo = None
def inserirItem(lista, item):
    novoItem = No(item)
    novoItem.proximo = lista
    lista = novoItem
    return lista

def ultimo(lista):
    if lista is None:
        return None
    atual = lista
    while atual.proximo is not None:
        atual = atual.proximo
        print(f"Visitando nó com valor: {atual.item}")
    return atual

def main():
    lista = None
    lista = inserirItem(lista, 10)
    lista = inserirItem(lista, 20)
    lista = inserirItem(lista, 30)
    ultimoNo = ultimo(lista)
    if ultimoNo is not None:
        print(f"O último nó contém o valor: {ultimoNo.item}")
    else:
        print("A lista está vazia.")

main()



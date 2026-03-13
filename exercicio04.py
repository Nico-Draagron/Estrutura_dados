# Implemente uma função que receba duas listas encadeadas de valores 
# inteiros e retorne a lista resultante da concatenação 
# das duas listas recebidas como parâmetros, isto é, 
# após a concatenação, o último elemento da primeira lista 
# deve apontar para o primeiro elemento da segunda lista.
# Esta função deve obedecer ao protótipo:

class No:
    def __init__(self, item):
        self.item = item
        self.proximo = None

def inserirItem(lista, item):
    novoItem = No(item)
    novoItem.proximo = lista
    lista = novoItem
    return lista

def concatena(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    atual = l1
    while atual.proximo is not None:
        atual = atual.proximo
    atual.proximo = l2
    return l1
def listarItens(lista):
    atual = lista
    while atual is not None:
        print(atual.item)
        atual = atual.proximo

def main():
    l1 = None
    l2 = None
    l1 = inserirItem(l1, 10)
    l1 = inserirItem(l1, 20)
    l1 = inserirItem(l1, 30)
    l2 = inserirItem(l2, 40)
    l2 = inserirItem(l2, 50)
    l2 = inserirItem(l2, 60)
    resultado = concatena(l1, l2)
    listarItens(resultado)

main()
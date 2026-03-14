# Implemente uma função que calcule a média
# aritmética dos valores armazenados. Esta função deve ter o protótipo:

class no:
    def __init__(self, item):
        self.item = item
        self.proximo = None

def lista_calcula_media(lst):
    if lst is None:
        return 0
    soma =0
    count =0
    atual = lst
    while atual is not None:
        soma += atual.item
        count +=1
        atual = atual.proximo
    media = soma / count
    return media

def inserirItem(lista, item):
    novoItem = no(item)
    novoItem.proximo = lista
    lista = novoItem
    return lista

def main():
    lista = None
    lista = inserirItem(lista, 10)
    lista = inserirItem(lista, 20)
    lista = inserirItem(lista, 30)
    media = lista_calcula_media(lista)
    print(f"A média dos valores na lista é: {media}")

main()
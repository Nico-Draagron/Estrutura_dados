# Considere listas encadeadas de valores inteiros e implemente uma função para retornar o número de nós da lista que possuem o campo info com valores maiores do que n (informado pelo usuário).
# Esta função deve obedecer ao protótipo:

class No:
    def __init__(self, item):
        self.item = item
        self.proximo = None

def maiores(lst, n):
    count = 0
    atual = lst
    while atual is not None:
        if atual.item > n:
            count += 1
            print(f"Valor {atual.item} é maior que {n}.")
        atual = atual.proximo
    return count
def inserirItem(lista, item):
    novoItem = No(item)
    novoItem.proximo = lista
    lista = novoItem
    return lista


# Exemplo de uso
lista = None
lista = inserirItem(lista, 10)
lista = inserirItem(lista, 20)
lista = inserirItem(lista, 30)
n = int(input("Digite um número: "))
resultado = maiores(lista, n)
print(f"Número de nós com valor maior que {n}: {resultado}")
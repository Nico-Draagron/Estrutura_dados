class No:
    def __init__(self, item):
        self.item = item
        self.proximo = None
    

def inserirItem(lista, item):
    novoItem = No(item)
    novoItem.proximo = lista
    lista = novoItem
    return lista

def listarItens(lista):
    atual = lista
    while atual is not None:
        print(atual.item)
        atual = atual.proximo

# Exemplo de uso
lista = None
lista = inserirItem(lista, 10)
lista = inserirItem(lista, 20)
lista = inserirItem(lista, 30)
listarItens(lista)

def menu():
    print("1. Inserir item")
    print("2. Listar itens")
    print("3. Remover item")
    print("4. Sair")
    opc = int(input("Escolha uma opção: "))
    return opc


def removerItem(lista, item):
    atual = lista
    anterior = None
    while atual is not None:
        if atual.item == item:
            if anterior is None:
                lista = atual.proximo
            else:
                anterior.proximo = atual.proximo
            return lista
        anterior = atual
        atual = atual.proximo
    print("Item não encontrado.")
    return lista


def main():
    lista = None
    while True:
        opc = menu()
        if opc == 1:
            item = int(input("Digite o item a ser inserido: "))
            lista = inserirItem(lista, item)
        elif opc == 2:
            listarItens(lista)
        elif opc == 3:
            item = int(input("Digite o item a ser removido: "))
            lista = removerItem(lista, item)
        elif opc == 4:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    main()

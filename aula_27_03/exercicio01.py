# Crie uma lista circular onde cada nó representa um atleta de um time.
# Cada atleta possui um bastao e uma variável que representa se estão ou não com o bastao (True ou False)
# Implemente funções para adicionar e remover atletas.
# Faça uma simulação onde o bastao é passado de atleta para atleta (percorra a lista circular algumas vezes, mostrando quem tem o bastao em cada turno).


class No:
    def __init__(self, item):
        self.item = item
        self.bastao = None
        self.proximo = None
        self.anterior = None

def menu():
    print("1. Inserir elemento")
    print("2. Listar elementos")
    print("3. Remover elemento")
    print("4. Passar bastão para o próximo atleta")
    print("5. Sair")
    try:
        return int(input("Escolha uma opção: "))
    except ValueError:
        print("Opção inválida  seu animal, legume.")
        return 0

def insert(lista, item, bastao=None):
    novo = No(item)
    novo.bastao = bastao
    if lista is None:
        novo.proximo = novo
        novo.anterior = novo
        lista = novo
        return lista
    ultimo = lista.anterior
    ultimo.proximo = novo
    novo.anterior = ultimo
    novo.proximo = lista
    lista.anterior = novo
    return lista

def listar(lista):
    if lista is None:
        print("vazio")
        return

    aux = lista
    while True:
        print(f'Atleta: {aux.item}, Bastão: {"Sim" if aux.bastao else "Não"}')
        aux = aux.proximo
        if aux == lista:
            break
def passar_bastao(lista):
    if lista is None:
        print("Lista vazia.")
        return
    atual = lista
    while True:
        if atual.bastao:
            atual.bastao = False
            atual.proximo.bastao = True
            print(f'Bastão passado para: {atual.proximo.item}')
            break
        atual = atual.proximo
        if atual == lista:
            print("Nenhum atleta com bastão encontrado.")
            break
def remover(lista, item):
    if lista is None:
        return None
    aux = lista
    while True:
        if aux.item == item:
            removido_tinha_bastao = aux.bastao is True
            proximo_no = aux.proximo
            if aux.proximo == aux:  # Único elemento na lista
                return None
            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior
            if removido_tinha_bastao:
                proximo_no.bastao = True
            if aux == lista:  # Removendo o primeiro elemento
                lista = aux.proximo
            return lista
        aux = aux.proximo
        if aux == lista:
            break  # Elemento não encontrado
    return lista

def main():
    atletas = [("Pontel", True), ("Cassol", False)]
    lista = None
    for atleta, bastao in atletas:
        lista = insert(lista, atleta, bastao)
    while True:
        opcao = menu()
        if opcao == 1:
            nome = input("Digite o nome do atleta: ")
            lista = insert(lista, nome)
        elif opcao == 2:
            listar(lista)
        elif opcao == 3:
            nome = input("Digite o nome do atleta a ser removido: ")
            lista = remover(lista, nome)
        elif opcao == 4:
            passar_bastao(lista)
        elif opcao == 5:
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Ta querendo ser QA ou o que?")

main()

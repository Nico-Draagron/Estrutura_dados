# Um ônibus urbano segue sempre o mesmo trajeto circular.
# Cada nó da lista representa uma parada de ônibus.
# Implemente funções para adicionar uma nova parada, remover uma parada e simular o percurso, imprimindo as paradas em sequência.

class No:
    def __init__(self, item):
        self.item = item
        self.proximo = None
        self.anterior = None
        self.parada = False
        
def menu():
    print("1. Inserir parada")
    print("2. Remover parada")
    print("3. Ver paradas")
    print("4. Exibir rota atual")
    print("5. Seguir para próxima parada")
    print("6. Sair")
    try:
        return int(input("Escolha uma opção: "))
    except ValueError:
        print("Opção inválida  seu animal, legume.")
        return 0


def adicionar(lista, item):
    novo = No(item)
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

def verificar_paradas(lista):
    if lista is None:
        print("Lista vazia.")
        return
    aux = lista
    while True:
        print(f'Parada: {aux.item}')
        aux = aux.proximo
        if aux == lista:
            break

def remover(lista, item):
    if lista is None:
        return None
    aux = lista
    while True:
        if aux.item == item:
            if aux.proximo == aux:  # Único elemento na lista
                return None
            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior
            if aux == lista:  # Removendo o primeiro elemento
                lista = aux.proximo
            return lista
        aux = aux.proximo
        if aux == lista:
            break  # Elemento não encontrado
    return lista

def exibir_rota(lista):
    """Exibe parada anterior, atual e próxima"""
    if lista is None:
        print("Nenhuma parada atual.")
        return
    aux = lista
    while True:
        if aux.parada:
            anterior = aux.anterior
            proximo = aux.proximo
            print(f"Parada Anterior: {anterior.item}")
            print(f"Parada Atual: {aux.item}")
            print(f"Próxima Parada: {proximo.item}")
            return
        aux = aux.proximo
        if aux == lista:
            print("Nenhuma parada marcada como atual.")
            return

def seguir(lista):
    """Move para a próxima parada no trajeto circular"""
    if lista is None:
        return lista
    aux = lista
    while True:
        if aux.parada:
            aux.parada = False
            aux.proximo.parada = True
            print(f"Ônibus saiu de {aux.item} e chegou em {aux.proximo.item}")
            return lista
        aux = aux.proximo
        if aux == lista:
            return lista

def main():
    paradas = ["Cachoeira do Sul", "Novo Cabrais", "Paraiso do Sul", "Agudo", "Recanto Maestro"]
    lista = None
    for parada in paradas:
        lista = adicionar(lista, parada)
    
    # Marcar Cachoeira do Sul como parada atual -OBS: Melhor cidade por que eu  vim de lá 
    if lista:
        lista.parada = True
    
    while True:
        opcao = menu()
        if opcao == 1:
            nome = input("Digite o nome da parada: ")
            lista = adicionar(lista, nome)
            print("Parada adicionada com sucesso.")
        elif opcao == 2:
            nome = input("Digite o nome da parada a ser removida: ")
            lista = remover(lista, nome)
            if lista is None:
                print("Lista vazia.")
            else:
                print("Parada removida com sucesso.")
        elif opcao == 3:
            verificar_paradas(lista)
        elif opcao == 4:
            exibir_rota(lista)
        elif opcao == 5:
            lista = seguir(lista)
        elif opcao == 6:
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()


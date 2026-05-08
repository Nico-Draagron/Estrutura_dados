import random


class satelite:
    def __init__(self,id, altitude, integridade):
        self.id = id
        self.altituide = altitude
        self.integridade = 100
        self.proximo = None
        self.anterior = None

class No:
    def __init__(self, valor):
        self.valor = valor

class lista_duplamente_encadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
    
    def cadastrar_satelite(self, id, altitude):
        novo_satelite = satelite(id, altitude, 100)
        if self.cabeca is None:
            self.cabeca = novo_satelite
            self.cauda = novo_satelite
        else:
            self.cauda.proximo = novo_satelite
            novo_satelite.anterior = self.cauda
            self.cauda = novo_satelite
    def listar_satelites(self):
        if self.cabeca is None:
            print("seu animal de duas patas, a lista esta vazia")
            return
        atual = self.cabeca
        while atual is not None:
            print(f"ID: {atual.id}, Altitude: {atual.altituide}, Integridade: {atual.integridade}%")
            atual = atual.proximo
    
    def remover_satelite(self, id):
        atual = self.cabeca
        while atual is not None:
            if atual.id == id:
                if atual == self.cabeca:
                    self.cabeca = atual.proximo
                    if self.cabeca is not None:
                        self.cabeca.anterior = None
                elif atual == self.cauda:
                    self.cauda = atual.anterior
                    if self.cauda is not None:
                        self.cauda.proximo = None
                else:
                    atual.anterior.proximo = atual.proximo
                    atual.proximo.anterior = atual.anterior
                return
            atual = atual.proximo

    def simular_orbita(self):
        for volta in range(3):
            print(f"--- Volta {volta + 1} ---")
            satelites = []
            atual = self.cabeca
            while atual is not None:
                satelites.append(atual)
                atual = atual.proximo

            if not satelites:
                print("Nenhum satelite restante para simular.")
                break

            quantidade = min(2, len(satelites))
            selecionados = random.sample(satelites, quantidade)

            for satelite_atual in selecionados:
                satelite_atual.integridade -= 20
                if satelite_atual.integridade <= 0:
                    print(f"Satelite {satelite_atual.id} perdeu toda a integridade e será removido.")
                    self.remover_satelite(satelite_atual.id)
                else:
                    print(f"Satelite {satelite_atual.id} tem integridade de {satelite_atual.integridade}%")

def main():
    lista = lista_duplamente_encadeada()
    lista.cadastrar_satelite("SAT-001", 500)
    lista.cadastrar_satelite("SAT-002", 600)
    lista.cadastrar_satelite("SAT-003", 700)

    print("--- Lista de Satélites Cadastrados ---")
    lista.listar_satelites()

    print("\nSimulando órbita...")
    lista.simular_orbita()

    print("\nLista de Satélites após simulação:")
    lista.listar_satelites()

main()

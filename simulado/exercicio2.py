class Satelite:
    def __init__(self, nome, pais_origem):
        self.nome = nome
        self.pais_origem = pais_origem
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def inserir_satelite(self, nome, pais_origem):
        novo_satelite = Satelite(nome, pais_origem)
        if self.cabeca is None:
            self.cabeca = novo_satelite
        else:
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_satelite
        
    def listar_satelites(self):
        if self.cabeca is None:
            return
        atual = self.cabeca
        while atual is not None:
            print(f"Nome: {atual.nome}, pais de origem: {atual.pais_origem} ")
            atual = atual.proximo
    
    def remover_satelite(self, nome):
        atual = self.cabeca
        anterior = None
        while atual is not None:
            if atual.nome == nome:
                if anterior is None: # O elemento a remover é a cabeça
                    self.cabeca = atual.proximo
                else: # O elemento está no meio ou fim
                    anterior.proximo = atual.proximo
                return True # Sucesso na remoção
            anterior = atual
            atual = atual.proximo
            return False
def main():
    lista = ListaEncadeada()
    
    
    lista.inserir_satelite("Hubble", "Estados Unidos")
    lista.inserir_satelite("James Webb", "Reino unido")
    lista.inserir_satelite("Amazônia-1", "Brasil")

    
   
    print("--- Lista de Satélites ---")
    lista.listar_satelites()
    
 
    print("\nRemovendo satélite 'Hubble'...")
    lista.remover_satelite("Hubble")
    print("\nLista de Satélites após remoção:")
    lista.listar_satelites()

main()

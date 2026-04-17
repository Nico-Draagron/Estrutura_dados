# Modifique a classe Pilha do exercício anterior para incluir os métodos topo()
# que retorna o elemento do topo sem removê-lo e esta_vazia() que informa se a pilha está vazia.
# Teste a funcionalidade empilhando elementos e verificando o topo antes e depois de desempilhar.

class Pilha:
    def __init__(self):
        self.elementos = []
    
    def empilhar(self, dado):
        self.elementos.append(dado)
    
    def desempilhar(self):
        if not self.elementos:
            print("Pilha vazia")
            return None
        return self.elementos.pop()
    
    def percorrer(self):
        if not self.elementos:
            print("Pilha vazia")
            return None

        print("Elementos da pilha:")
        for elemento in self.elementos:
            print(elemento)
    def topo(self):
        if not self.elementos:
            print("Pilha vazia")
            return None
        return self.elementos[-1]
    def esta_vazia(self):
        return len(self.elementos) == 0
    def tamanho(self):
        return len(self.elementos)
    def media(self):
        contador = 0
        soma = 0
        for elemento in self.elementos:
            if isinstance(elemento, (int, float)):
                soma += elemento
                contador += 1
        if contador == 0:
            return 0
        return soma / contador
    
def main():
    pilha = Pilha()
    pilha.empilhar(10)
    pilha.empilhar(20)
    pilha.empilhar(30)

    print("Topo da pilha:", pilha.topo())
    print("Pilha vazia?", pilha.esta_vazia())
    print("Tamanho da pilha:", pilha.tamanho())
    print("Média dos elementos:", pilha.media())

    pilha.desempilhar()
    print("Topo da pilha após desempilhar:", pilha.topo())

main()
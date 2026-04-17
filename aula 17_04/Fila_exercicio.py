# Crie uma classe Fila em Python utilizando uma lista para armazenar os elementos. 
# Implemente os métodos enfileirar(dado) para adicionar um elemento ao final da fila,
# desenfileirar() para remover o elemento do início e percorrer() para exibir todos 
# os elementos da fila na ordem em que estão.
# Adicione alguns elementos, remova um deles e mostre o conteúdo final da fila.

class Fila:
    def __init__(self):
        self.elementos = []
    
    def enfileirar(self, dado):
        self.elementos.append(dado)
    
    def desenfileirar(self):
        if not self.elementos:
            print("Fila  vazia")
            return None
        return self.elementos.pop(0)
    
    def percorrer(self):
        if not self.elementos:
            print("Fila vazia")
            return None

        print("Elementos da fila:")
        for elemento in self.elementos:
            print(elemento)
    def frente(self):
        if not self.elementos:
            print("Fila vazia")
            return None
        return self.elementos[0]
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
    fila = Fila()
    fila.enfileirar(10)
    fila.enfileirar(20)
    fila.enfileirar(30)

    print("Frente da fila:", fila.frente())
    print("Fila vazia?", fila.esta_vazia())
    print("Tamanho da fila:", fila.tamanho())
    print("Média dos elementos:", fila.media())

    fila.desenfileirar()
    print("Frente da fila após desenfileirar:", fila.frente())

main()
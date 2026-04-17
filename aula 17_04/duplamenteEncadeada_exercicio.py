# Crie uma classe NoDuplo para uma lista duplamente encadeada, contendo dado, anterior e proximo.
#  Implemente uma classe ListaDuplamenteEncadeada com um método para adicionar um nó no início 
# (adicionar_inicio) e um método para percorrer a lista do início ao fim (percorrer_frente).
#  Adicione elementos e demonstre o percurso.
# Adicione à classe ListaDuplamenteEncadeada do exercício anterior um método percorrer_tras() 
# que percorre a lista do fim ao início. Teste a funcionalidade após adicionar alguns elementos.

class NoDuplo:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None
    
class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def adicionar_inicio(self, dado):
        novo_no = NoDuplo(dado)
        if self.inicio is None:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            novo_no.proximo = self.inicio
            self.inicio.anterior = novo_no
            self.inicio = novo_no
    
    def percorrer_frente(self):
        atual = self.inicio
        while atual is not None:
            print(atual.dado)
            atual = atual.proximo
    
    def percorrer_tras(self):
        atual = self.fim
        while atual is not None:
            print(atual.dado)
            atual = atual.anterior

def main():
    lista = ListaDuplamenteEncadeada()
    lista.adicionar_inicio(10)
    lista.adicionar_inicio(20)
    lista.adicionar_inicio(30)

    print("Percorrendo do início ao fim:")
    lista.percorrer_frente()

    print("Percorrendo do fim ao início:")
    lista.percorrer_tras()

main()  
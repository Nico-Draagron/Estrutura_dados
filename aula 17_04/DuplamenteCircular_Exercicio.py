
class NoDuploCircular:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None 

class ListaDuplamenteEncadeadaCircular:
    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def adicionar_inicio(self, dado):
        novo_no = NoDuploCircular(dado)
        if self.inicio is None:
            self.inicio = novo_no
            self.fim = novo_no
            novo_no.proximo = novo_no
            novo_no.anterior = novo_no
        else:
            novo_no.proximo = self.inicio
            novo_no.anterior = self.fim
            self.inicio.anterior = novo_no
            self.fim.proximo = novo_no
            self.inicio = novo_no
    
    def adicionar_final(self, dado):
        novo_no = NoDuploCircular(dado)
        if self.inicio is None:
            self.inicio = novo_no
            self.fim = novo_no
            novo_no.proximo = novo_no
            novo_no.anterior = novo_no
        else:
            novo_no.proximo = self.inicio
            novo_no.anterior = self.fim
            self.fim.proximo = novo_no
            self.inicio.anterior = novo_no
            self.fim = novo_no
    
    def percorrer_frente(self, quantidade):
        atual = self.inicio
        for _ in range(quantidade):
            print(atual.dado)
            atual = atual.proximo
    
    def percorrer_tras(self, quantidade):
        atual = self.fim
        for _ in range(quantidade):
            print(atual.dado)
            atual = atual.anterior
    def remover(self, dado):
        if self.inicio is None:
            return
        
        atual = self.inicio
        while True:
            if atual.dado == dado:
                if atual == self.inicio and atual == self.fim:
                    self.inicio = None
                    self.fim = None
                else:
                    atual.anterior.proximo = atual.proximo
                    atual.proximo.anterior = atual.anterior
                    if atual == self.inicio:
                        self.inicio = atual.proximo
                    if atual == self.fim:
                        self.fim = atual.anterior
                return
            
            atual = atual.proximo
            if atual == self.inicio:
                break
def main():
    lista = ListaDuplamenteEncadeadaCircular()
    lista.adicionar_inicio(10)
    lista.adicionar_inicio(20)
    lista.adicionar_inicio(30)

    print("Percorrendo do início ao fim:")
    lista.percorrer_frente(6)

    print("Percorrendo do fim ao início:")
    lista.percorrer_tras(6)

    print("Removendo o elemento 20:")
    lista.remover(20)

    print("Percorrendo do início ao fim após remoção:")
    lista.percorrer_frente(6)

main()
class No:
    def __init__(self, dado):
        self.dado= dado
        self.proximo = None
        self.anterior = None
    

class Deque:
    def __init__(self):
        self.inicio = None
        self.fim = None

    
    def inserirInicio(self, dado):
        novo = No(dado)

        if self.inicio== None:
            self.inicio = novo
            self.fim = novo

        else:
            self.inicio.anterior= novo
            novo.proximo = self.inicio
            self.inicio = novo
        print(dado, "inserir no deque")
    
    def inserirFIm(self, dado):
        novo = No(dado)

        if self.inicio== None:
            self.inicio = novo
            self.fim = novo

        else:
            self.fim.proximo= novo
            novo.anterior = self.fim
            self.fim = novo
        print(dado, "inserir no deque")

    
    def ListarChamados(self):
        aux = self.inicio
        if aux == None:   
            print(" lista vazia")

        while aux != None:
            print("Item:", aux.dado)
            aux = aux.proximo

    def removerInicio(self):

        if self.inicio is None: 
            print("fila vazia, ebaaaaaa")
            return
        
        if  self.inicio.proximo == None:
            self.inicio = self.fim  = None
        
        else:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None
        
    def removerFim(self):
        if self.fim is None: 
            print("fila vazia, ebaaaaaa")
            return
        
        if  self.fim == self.inicio:
            self.fim = self.inicio = None

        else:
            self.fim = self.fim.anterior
            self.fim.proximo = None

def main():
    
    deque = Deque()

    opcao= 0

    while opcao !=6:
        opcao = int(input("Digite a opção"))

        if opcao ==1:
            print("Adicionar o chamado no final da fila")
            dado = int(input("inserir no final"))
            deque.inserirFIm(dado)

        elif opcao ==2:
            print("Inserir o chamado no inicio da fila, seu furao")
            dado = int(input("inserir no inicio"))
            deque.inserirInicio(dado)
        elif opcao ==3:
            print("Atender o primeiro chamado da fila")
            print(f" o primeiro chamado da fila {deque.inicio.dado} foi atendio")
            deque.removerInicio()
      
        elif opcao ==4:
            print("Atender o ultimo chamado da fila")
            print(f" o ultimo chamado da fila: {deque.fim.dado} foi atendido")
            deque.removerFim()
    
        elif opcao ==5:
            print("LIstando todos os chamados da fila")
            deque.ListarChamados()
        elif opcao ==6:
            print("Adeus, e não se esqueça de abrir a droga do chamado quando precisar")
            break
        else:
            print("Digite uma opção valida seu mamaco")
            return
         
main()

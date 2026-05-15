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

        if aux is None:
            print("Fila vazia")
            return

        print("\nORDEM ATUAL DE ATENDIMENTO:")

        while aux is not None:
            print(aux.dado)
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
        

def main():
    
    deque = Deque()

    

    while True:
        print("1-adicionar cliente")
        print("2-atender clientes")
        print("3-listar clientes")
        print("4-fechar")
        opcao = int(input("Escolha: "))

        if opcao == 1:

            while True:

                print("\n1 - Cliente comum")
                print("2 - Cliente VIP")
                print("3 - Voltar")
                
                tipo = int(input("Tipo do cliente: "))

                if tipo == 1:

                    dado= input("Nome do cliente comum: ")

                    deque.inserirFIm(dado)

                    print("Cliente comum adicionado no final.")

                    deque.ListarChamados()

                elif tipo == 2:

                    dado = input("Nome do cliente VIP: ")

                    deque.inserirInicio(dado)

                    print("Cliente VIP adicionado no início.")

                    deque.ListarChamados()

                elif tipo == 3:
                    break

                else:
                    print("Opção inválida")
        elif opcao == 2:
            
            print(f"Cliente atendido {deque.inicio.dado}")
            deque.removerInicio()
            deque.ListarChamados()
        
        elif opcao == 3:

            print("listar os chamados")
            deque.ListarChamados()

        elif opcao ==4:
            print("tchauuuu ")
            break

        else:
            print("digita algo certo ai")

main()
            

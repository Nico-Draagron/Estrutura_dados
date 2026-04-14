# Implemente um programa que simule o funcionamento de operações matemáticas armazenadas em uma pilha. O menu deve conter as opções:

# Inserir operação na pilha (ex: “5+3”, “7*2”)
# Retirar última operação (POP)
# Mostrar última operação inserida (topo)
# Mostrar todas as operações pendentes
# Sair



def calcular(operacao):
    for simbolo in ['+', '-', '*', '/']:
        if simbolo in operacao:
            partes = operacao.split(simbolo)
            if len(partes) == 2:
                a = float(partes[0])
                b = float(partes[1])
                if simbolo == '+':
                    resultado = a + b
                elif simbolo == '-':
                    resultado = a - b
                elif simbolo == '*':
                    resultado = a * b
                elif simbolo == '/':
                    if b == 0:
                        return "Erro: divisão por zero"
                    resultado = a / b
                if resultado == int(resultado):
                    return int(resultado)
                return resultado
    return None

def menu():
    print("1. Inserir operação na pilha")
    print("2. Retirar última operação (POP)")
    print("3. Mostrar última operação inserida (topo)")
    print("4. Mostrar todas as operações pendentes")
    print("5. Sair")
    try:
        return int(input("Escolha uma opção: "))
    except ValueError:
        print("Opção inválida, tente novamente.")
        return 0

def main():
    pilha = []
    while True:
        choice = menu()
        if choice == 1:
            operacao = input("Digite a operação (ex: 5+3): ")
            pilha.append(operacao)
            resultado = calcular(operacao)
            if resultado is not None:
                print(f'Resultado: {operacao} = {resultado}')
            else:
                print("Operação inválida, mas foi adicionada à pilha.")
        elif choice == 2:
            if pilha:
                op = pilha.pop()
                print(f'Operação removida: {op} = {calcular(op)}')
            else:
                print("Pilha vazia.")
        elif choice == 3:
            if pilha:
                op = pilha[-1]
                print(f'Última operação inserida: {op} = {calcular(op)}')
            else:
                print("Pilha vazia.")
        elif choice == 4:
            if pilha:
                print("Operações pendentes:")
                for op in reversed(pilha):
                    print(f'  {op} = {calcular(op)}')
            else:
                print("Pilha vazia.")
        elif choice == 5:
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()

# Os carros entram em uma garagem em fila indiana (um atrás do outro).
# Para um carro sair, é necessário retirar todos os que entraram depois dele (LIFO).
# Cadastrar 20 carros, pedir qual deseja tirar e mostrar todos os retirados.

def menu():
    print('\n--- GARAGEM ---')
    print('1. Ver carros na garagem')
    print('2. Retirar um carro')
    print('3. Sair')
    try:
        return int(input('Escolha uma opção: '))
    except ValueError:
        return 0

def main():
    garagem = []
    for i in range(1, 21):
        garagem.append(f'carro{i}')

    while True:
        opcao = menu()

        if opcao == 1:
            if garagem:
                print('\nCarros na garagem (do primeiro ao último que entrou):')
                for i in range(len(garagem)):
                    print(f'  {i + 1}. {garagem[i]}')
            else:
                print('\nGaragem vazia.')

        elif opcao == 2:
            if not garagem:
                print('\nGaragem vazia, nenhum carro para retirar.')
                continue

            print('\nCarros disponíveis:')
            for i in range(len(garagem)):
                print(f'  {i + 1}. {garagem[i]}')

            try:
                numero = int(input('\nDigite o número do carro que deseja retirar: '))
            except ValueError:
                print('Número inválido.')
                continue

            if numero < 1 or numero > len(garagem):
                print('Número inválido.')
                continue

            posicao = numero - 1
            carro_desejado = garagem[posicao]
            retirados = []

            while len(garagem) > posicao:
                retirados.append(garagem.pop())

            print(f'\nCarros retirados para liberar o {carro_desejado}:')
            for carro in retirados:
                print(f'  {carro}')

            print(f'\nTotal de carros retirados: {len(retirados)}')
            print(f'Carros que permaneceram na garagem: {len(garagem)}')

        elif opcao == 3:
            print('Saindo...')
            break
        else:
            print('Opção inválida.')

if __name__ == '__main__':
    main()

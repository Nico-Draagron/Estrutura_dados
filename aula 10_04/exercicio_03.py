# Simular uma sala de partidas em que jogadores entram numa fila.
# A cada rodada, o jogador da frente participa da partida e volta para o fim da fila.

def menu():
    print('\n--- SALA DE PARTIDAS ---')
    print('1. Adicionar jogador ao final da fila')
    print('2. Remover jogador específico')
    print('3. Simular 1 rodada')
    print('4. Simular N rodadas')
    print('5. Mostrar fila')
    print('6. Mostrar próximo a jogar')
    print('7. Limpar fila')
    print('8. Sair')
    try:
        return int(input('Escolha uma opção: '))
    except ValueError:
        return 0

def mostrar_fila(fila):
    if fila:
        print('Fila atual:')
        for i in range(len(fila)):
            print(f'  {i + 1}. {fila[i]}')
    else:
        print('Fila vazia.')

def simular_rodada(fila):
    if not fila:
        print('Fila vazia, não é possível simular.')
        return
    jogador = fila.pop(0)
    print(f'Jogador da vez: {jogador}')
    fila.append(jogador)

def main():
    fila = []

    while True:
        opcao = menu()

        if opcao == 1:
            nome = input('Nome do jogador: ').strip()
            if nome:
                fila.append(nome)
                print(f'{nome} entrou na fila.')
            else:
                print('Nome inválido.')

        elif opcao == 2:
            if not fila:
                print('Fila vazia.')
                continue
            mostrar_fila(fila)
            nome = input('Nome do jogador para remover: ').strip()
            if nome in fila:
                fila.remove(nome)
                print(f'{nome} foi removido da fila.')
            else:
                print('Jogador não encontrado.')

        elif opcao == 3:
            simular_rodada(fila)

        elif opcao == 4:
            if not fila:
                print('Fila vazia.')
                continue
            try:
                n = int(input('Quantas rodadas? '))
            except ValueError:
                print('Número inválido.')
                continue
            for r in range(1, n + 1):
                print(f'\n-- Rodada {r} --')
                simular_rodada(fila)
                mostrar_fila(fila)

        elif opcao == 5:
            mostrar_fila(fila)

        elif opcao == 6:
            if fila:
                print(f'Próximo a jogar: {fila[0]}')
            else:
                print('Fila vazia.')

        elif opcao == 7:
            fila.clear()
            print('Fila limpa.')

        elif opcao == 8:
            print('Saindo...')
            break

        else:
            print('Opção inválida.')

if __name__ == '__main__':
    main()

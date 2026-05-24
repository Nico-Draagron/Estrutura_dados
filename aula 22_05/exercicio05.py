# Uma empresa empilha caixas em uma torre. 
# Crie uma função recursiva 
# que exiba os números das caixas do topo até a base.

def exibir_caixas(n):
    if n < 1:
        return
    print(f"Caixa número: {n}")
    exibir_caixas(n - 1)

def main():
    n = int(input("Digite o numero de caixas ate a base:"))
    exibir_caixas(n)

main()

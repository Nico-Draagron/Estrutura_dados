
def contagem_regressiva(n):
    if n < 1:
        return
    print(f"Contagem regressiva em: {n}...")
    contagem_regressiva(n - 1)
    if n == 1:
        print("ACABOU O KAOOOO, O GENERAL CHEGOU, O GENERAL CHEGOU OUOUOU")

def imprimir_pares(n):
    if n < 0:
        return
    if n % 2 ==0:
        print(f"Par: {n}")
    imprimir_pares(n - 1)
    
    
def soma_impares(n):
    if n < 1:
        return 0
    if n % 2 == 1:
        print(f"Ímpar: {n}") 
        return n + soma_impares(n - 1)
 
    else:
        return soma_impares(n - 1)
   
    
def main():
    n = int(input("digite um numero para ver tudo isso aqui: contagem regressiva, pares e soma de impares: "))
    contagem_regressiva(n)
    imprimir_pares(n)
    resultado = soma_impares(n)
    print(f"A soma dos números ímpares de 1 até {n} é: {resultado}")

main()

# Uma estação meteorológica armazenou temperaturas em um vetor.
#  Faça uma função recursiva que retorne a 
# média das temperaturas armazenadas.

def media(temperaturas, n):
    if n == 0: #Se n for zero, nao ha temperaturas para calcular a media
        return 0
    if n == 1: #Se n for um, a media é a unica temperatura
        return temperaturas[0]
    #Soma a temperatura atual com a media das temperaturas anteriores
    #Primeiro calcula a media das temperaturas anteriores
    #depois multiplica pela quantidade de temperaturas anteriores para obter a soma total
    #Por fim, dividimos pela quantidade total de temperaturas, obtendo  a media
    return (temperaturas[n - 1] + media(temperaturas, n - 1) * (n - 1)) / n

def main():
    temperaturas = [20.5, 22.0, 19.8, 21.3, 23.1]
    n = len(temperaturas)
    resultado = media(temperaturas, n)
    print(f"A média das temperaturas é: {resultado:.2f}")

main()  

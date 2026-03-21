# FizzBuzz: Percorra os números de 1 a 100.
#  Para múltiplos de 3, imprima "Fizz". Para múltiplos de 5, imprima "Buzz". 
# Para múltiplos de ambos, imprima "FizzBuzz".

def fizz_buzz():
    for i in range (1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    

fizz_buzz()
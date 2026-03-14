# Crie uma classe Livro com os atributos: título, autor e número de páginas.
# Implemente um método que informe se o livro é "curto" ou "longo", considerando:
# até 100 páginas = curto
# mais de 100 páginas = longo

# Crie dois objetos e mostre o resultado do método para cada um.

class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def tipo_livro(self):
        if self.num_paginas <= 100:
            return "curto"
        else:
            return "longo"

def main():
    livro1 = Livro("os 3 leitoes e um lobo pidao", "Cassol azevedo", 96)
    livro2 = Livro("A arte da guerra", "Tsu Ghain", 1225)

    print(f"Livro: {livro1.titulo}, autor: {livro1.autor}, numero de paginas: {livro1.num_paginas}, tipo: {livro1.tipo_livro()}")
    print(f"Livro: {livro2.titulo}, autor: {livro2.autor}, numero de paginas: {livro2.num_paginas}, tipo: {livro2.tipo_livro()}")

main()
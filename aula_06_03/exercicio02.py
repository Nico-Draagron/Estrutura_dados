# Crie uma classe chamada Produto com os atributos: nome, 
# preco e quantidade.
# Use o método __init__ para inicializar esses atributos.
# Depois, crie dois produtos diferentes e imprima seus dados.

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

def main():
    produto1 = Produto("notebook", 2500.00, 10)
    produto2 = Produto("smartphone", 1500.00, 20)

    print(f"Produto: {produto1.nome}, preço: R${produto1.preco}, quantidade em estoque: {produto1.quantidade}")
    print(f"Produto: {produto2.nome}, preço: R${produto2.preco}, quantidade em estoque: {produto2.quantidade}")

main()
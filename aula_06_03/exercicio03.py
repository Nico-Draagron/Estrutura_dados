# Crie uma classe chamada Produto, que tenha os atributos:
# nome, preço e quantidade em estoque.
# Implemente um método atualizar_estoque() que recebe um valor
# e soma à quantidade atual.
# Crie dois objetos e atualize o estoque de cada um, mostrando
# os dados antes e depois da atualização.

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def atualizar_estoque(self, valor):
        self.quantidade += valor

def main():
    produto1 = Produto("notebook", 2500.00, 10)
    produto2 = Produto("smartphone", 1500.00, 20)

    print(f"Produto: {produto1.nome}, preço: R${produto1.preco}, quantidade em estoque: {produto1.quantidade}")
    print(f"Produto: {produto2.nome}, preço: R${produto2.preco}, quantidade em estoque: {produto2.quantidade}")

    produto1.atualizar_estoque(5)
    produto2.atualizar_estoque(-3)

    print("\nApós atualização do estoque:")
    print(f"Produto: {produto1.nome}, preço: R${produto1.preco}, quantidade em estoque: {produto1.quantidade}")
    print(f"Produto: {produto2.nome}, preço: R${produto2.preco}, quantidade em estoque: {produto2.quantidade}")


main()
    
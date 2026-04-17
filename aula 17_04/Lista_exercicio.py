class No:
	def __init__(self, dado):
		self.dado = dado
		self.proximo = None


class ListaEncadeada:
	def __init__(self):
		self.inicio = None

	def adicionar_inicio(self, dado):
		novo_no = No(dado)
		novo_no.proximo = self.inicio
		self.inicio = novo_no

	def adicionar_final(self, dado):
		novo_no = No(dado)

		if self.inicio is None:
			self.inicio = novo_no
			return

		atual = self.inicio
		while atual.proximo is not None:
			atual = atual.proximo
		atual.proximo = novo_no

	def percorrer(self):
		atual = self.inicio
		while atual is not None:
			print(atual.dado)
			atual = atual.proximo

	def media_dados(self):
		if self.inicio is None:
			return 0

		soma = 0
		quantidade = 0
		atual = self.inicio

		while atual is not None:
			soma += atual.dado
			quantidade += 1
			atual = atual.proximo

		return soma / quantidade


def main():
	lista = ListaEncadeada()

	lista.adicionar_inicio(20)
	lista.adicionar_inicio(10)

	lista.adicionar_final(30)
	lista.adicionar_final(40)

	print("Elementos da lista:")
	lista.percorrer()

	print(f"Média dos dados: {lista.media_dados():.2f}")


main()

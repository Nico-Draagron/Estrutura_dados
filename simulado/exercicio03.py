class No:
	def __init__(self, nome, altitude, combustivel, ativo=True):
		self.nome = nome
		self.altitude = altitude
		self.combustivel = combustivel
		self.ativo = ativo
		self.proximo = None
		self.anterior = None


def mostrar_no(no):
	status = "Ativo" if no.ativo else "Desativado"
	print(
		f"Nome: {no.nome}, Altitude: {no.altitude} km, "
		f"Combustivel: {no.combustivel}%, Status: {status}"
	)


def adicionar_satelite(cabeca, nome, altitude, combustivel):
	if altitude < 300:
		print(f"Nao foi possivel adicionar {nome}: altitude menor que 300 km.")
		return cabeca

	if combustivel < 0:
		combustivel = 0
	if combustivel > 100:
		combustivel = 100

	novo = No(nome, altitude, combustivel, True)

	if cabeca is None:
		novo.proximo = novo
		novo.anterior = novo
		return novo

	cauda = cabeca.anterior
	cauda.proximo = novo
	novo.anterior = cauda
	novo.proximo = cabeca
	cabeca.anterior = novo
	return cabeca


def remover_satelite(cabeca, nome):
	if cabeca is None:
		return cabeca

	atual = cabeca
	while True:
		if atual.nome == nome:
			if atual.combustivel != 0:
				print(f"{nome} nao pode ser removido: combustivel ainda maior que 0.")
				return cabeca

			if atual.proximo == atual:
				return None

			atual.anterior.proximo = atual.proximo
			atual.proximo.anterior = atual.anterior

			if atual == cabeca:
				cabeca = atual.proximo
			return cabeca

		atual = atual.proximo
		if atual == cabeca:
			break

	return cabeca


def desativar_satelite(cabeca, nome):
	if cabeca is None:
		return

	atual = cabeca
	while True:
		if atual.nome == nome:
			atual.ativo = False
			return
		atual = atual.proximo
		if atual == cabeca:
			break


def ativar_satelite(cabeca, nome):
	if cabeca is None:
		return

	atual = cabeca
	while True:
		if atual.nome == nome:
			if atual.combustivel > 0:
				atual.ativo = True
			return
		atual = atual.proximo
		if atual == cabeca:
			break


def reposicionar_satelite(cabeca, nome, nova_altitude):
	if cabeca is None:
		return

	if nova_altitude < 300:
		print(f"Nao foi possivel reposicionar {nome}: altitude menor que 300 km.")
		return

	atual = cabeca
	while True:
		if atual.nome == nome:
			atual.altitude = nova_altitude
			return
		atual = atual.proximo
		if atual == cabeca:
			break


def simular_orbita(cabeca, consumo_por_volta):
	if cabeca is None:
		return cabeca

	atual = cabeca
	while True:
		if atual.ativo:
			atual.combustivel -= consumo_por_volta
			if atual.combustivel < 0:
				atual.combustivel = 0

			if atual.combustivel == 0:
				atual.ativo = False

		atual = atual.proximo
		if atual == cabeca:
			break

	return cabeca


def percorrer_horario(cabeca):
	print("\n--- Orbita em sentido horario ---")
	if cabeca is None:
		print("Lista vazia.")
		return

	atual = cabeca
	while True:
		mostrar_no(atual)
		atual = atual.proximo
		if atual == cabeca:
			break


def percorrer_antihorario(cabeca):
	print("\n--- Orbita em sentido anti-horario ---")
	if cabeca is None:
		print("Lista vazia.")
		return

	atual = cabeca
	while True:
		mostrar_no(atual)
		atual = atual.anterior
		if atual == cabeca:
			break


def mostrar_ativados(cabeca):
	print("\n--- Satelites ativados ---")
	if cabeca is None:
		print("Lista vazia.")
		return

	atual = cabeca
	achou = False
	while True:
		if atual.ativo:
			mostrar_no(atual)
			achou = True
		atual = atual.proximo
		if atual == cabeca:
			break

	if not achou:
		print("Nenhum satelite ativado.")


def mostrar_desativados(cabeca):
	print("\n--- Satelites desativados ---")
	if cabeca is None:
		print("Lista vazia.")
		return

	atual = cabeca
	achou = False
	while True:
		if not atual.ativo:
			mostrar_no(atual)
			achou = True
		atual = atual.proximo
		if atual == cabeca:
			break

	if not achou:
		print("Nenhum satelite desativado.")


def remover_todos_com_combustivel_zero(cabeca):
	if cabeca is None:
		return cabeca

	nomes_para_remover = []
	atual = cabeca
	while True:
		if atual.combustivel == 0:
			nomes_para_remover.append(atual.nome)
		atual = atual.proximo
		if atual == cabeca:
			break

	for nome in nomes_para_remover:
		cabeca = remover_satelite(cabeca, nome)

	return cabeca


cabeca = None

cabeca = adicionar_satelite(cabeca, "Hubble", 540, 40)
cabeca = adicionar_satelite(cabeca, "James Webb", 1500, 65)
cabeca = adicionar_satelite(cabeca, "Amazonia-1", 752, 20)
cabeca = adicionar_satelite(cabeca, "CBERS-4A", 778, 90)

percorrer_horario(cabeca)
percorrer_antihorario(cabeca)

reposicionar_satelite(cabeca, "James Webb", 1550)
desativar_satelite(cabeca, "CBERS-4A")

cabeca = simular_orbita(cabeca, 25)

mostrar_ativados(cabeca)
mostrar_desativados(cabeca)

cabeca = remover_todos_com_combustivel_zero(cabeca)

print("\n--- Orbita final (apos remover combustivel 0) ---")
percorrer_horario(cabeca)

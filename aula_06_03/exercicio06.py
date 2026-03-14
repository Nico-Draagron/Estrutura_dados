# Crie uma classe Funcionario com os atributos: nome, salário e cargo.
# Implemente um método calcular_bonus() que retorne:
# 10% de bônus para o cargo "Gerente"
# 5% de bônus para os demais cargos

# Instancie dois funcionários e exiba o salário com bônus de cada um.

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    
    def calcular_bonus(self):
        if self.cargo.capitalize() == "Gerente":
            return self.salario * 0.10
        else:
            return self.salario * 0.05

def main():
    funcionario1 = Funcionario("Carlos", 5000.00, "gerente")
    funcionario2 = Funcionario("Ana", 3000.00, "analista")

    print(f"Funcionário: {funcionario1.nome}, cargo: {funcionario1.cargo}, salario: R${funcionario1.salario}, bonus: R${funcionario1.calcular_bonus()}")
    print(f"Funcionário: {funcionario2.nome}, cargo: {funcionario2.cargo}, salario: R${funcionario2.salario}, bonus: R${funcionario2.calcular_bonus()}")

main()
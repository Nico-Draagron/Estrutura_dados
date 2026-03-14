# Crie uma classe Aluno que receba nome e uma lista com três notas.
# Implemente um método calcular_media() que retorne a média das notas.
# Implemente também um método verificar_aprovacao(), que retorne "Aprovado" se a média for maior ou igual a 7, ou "Reprovado" caso contrário.
# Teste a classe com dois alunos e mostre os resultados.

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
    
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    
    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media >= 7:
            return "Aprovado"
        else:
            return "Reprovado"

def main():
    aluno1 = Aluno("yuri", [8, 7, 9])
    aluno2 = Aluno("maria", [6, 5, 7])

    print(f"Aluno: {aluno1.nome}, media: {aluno1.calcular_media()}, situacao: {aluno1.verificar_aprovacao()}")
    print(f"Aluno: {aluno2.nome}, media: {aluno2.calcular_media()}, situacao: {aluno2.verificar_aprovacao()}")

main()
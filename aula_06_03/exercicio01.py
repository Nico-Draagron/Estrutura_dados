# Crie uma classe “aluno” com nome, frequência e média geral, e logo após crie e imprima 2 objetos com essas características:
# Joao(76, 7.8) e Maria(80, 8.5)

class Aluno:
    def __init__(self, nome, frequencia, media):
        self.nome = nome
        self.frequencia = frequencia
        self.media = media

def main():
    aluno1 = Aluno("Joao", 76, 7.8)
    aluno2 = Aluno("Maria", 80, 8.5)

    print(f"Aluno: {aluno1.nome}, Frequência: {aluno1.frequencia}%, Média: {aluno1.media}")
    print(f"Aluno: {aluno2.nome}, Frequência: {aluno2.frequencia}%, Média: {aluno2.media}")

main()
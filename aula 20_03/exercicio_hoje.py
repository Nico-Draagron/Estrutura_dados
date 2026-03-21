# Faça um algoritmo que utilize lista duplamente encadeada para armazenar informações de alunos. Cada nó deve conter:
# Identificador (ID)
# Nome do aluno
# Nota final
# O algoritmo deve apresentar o seguinte menu principal:
# Inserir aluno
# Listar alunos
# Remover aluno
# Mostrar situação dos alunos
# Listar todos os alunos classificados como:
# Aprovado (nota ≥ 7,0)
# Exame (nota entre 4,0 e 6,9)
# Reprovado (nota < 4,0)
# Sair

class Node:
    def __init__(self, id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, id, name, grade):
        new_node = Node(id, name, grade)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def list_students(self):
        current = self.head
        while current:
            print(f'ID: {current.id}, Name: {current.name}, Grade: {current.grade}')
            current = current.next

    def remove_student(self, id):
        current = self.head
        while current:
            if current.id == id:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True
            current = current.next
        return False

    def show_status(self):
        current = self.head
        while current:
            status = "Aprovado" if current.grade >= 7.0 else "Exame" if 4.0 <= current.grade < 7.0 else "Reprovado"
            print(f'ID: {current.id}, Name: {current.name}, Grade: {current.grade}, Status: {status}')
            current = current.next
def main():
    students = DoublyLinkedList()
  
    students.insert("1", "Joao", 7.8)
    students.insert("2", "Maria", 8.5)
    students.insert("3", "Carlos", 5.5)
    students.insert("4", "Ana", 3.0)
    
    while True:
        print("\nMenu:")
        print("1. Inserir aluno")
        print("2. Listar alunos")
        print("3. Remover aluno")
        print("4. Mostrar situação dos alunos")
        print("5. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            id = input("ID do aluno: ")
            name = input("Nome do aluno: ")
            grade = float(input("Nota final do aluno: "))
            students.insert(id, name, grade)
        elif choice == '2':
            students.list_students()
        elif choice == '3':
            id = input("ID do aluno a remover: ")
            if students.remove_student(id):
                print("Aluno removido com sucesso.")
            else:
                print("Aluno não encontrado.")
        elif choice == '4':
            students.show_status()
        elif choice == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")



main()
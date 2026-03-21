# Faça um algoritmo que possua uma lista duplamente encadeada e apresente o seguinte menu:
# Inserir no
# Listar no’s
# Remover no’s
# Verificar se no existe
# Neste caso deve-se apresentar um novo menu e verificar se o usuário quer buscar por nome ou identificador.
# Sair

# Cada nó deve armazenar o nome e um identificador.

class node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, id, name):
        new_node = node(id, name)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def list_nodes(self):
        current = self.head
        while current:
            print(f'ID: {current.id}, Name: {current.name}')
            current = current.next

    def remove_node(self, id):
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

    def find_node(self, id=None, name=None):
        current = self.head
        while current:
            if (id is not None and current.id == id) or (name is not None and current.name == name):
                return f'Node found: ID: {current.id}, Name: {current.name}'
            current = current.next
        return 'Node not found'
    
def main():
    students = DoublyLinkedList()
  
    students.insert("1", "Joao")
    students.insert("2", "Maria")
    students.insert("3", "Pedro")

    print("List of nodes:")
    students.list_nodes()

    print("\nRemoving node with ID '2':")
    if students.remove_node("2"):
        print("Node removed successfully.")
    else:
        print("Node not found.")

    print("\nList of nodes after removal:")
    students.list_nodes()

    print("\nFinding node by ID '1':")
    print(students.find_node(id="1"))

    print("\nFinding node by name 'Pedro':")
    print(students.find_node(name="Pedro"))

main()
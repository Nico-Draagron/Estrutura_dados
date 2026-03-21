# Implemente um algoritmo com lista duplamente encadeada para gerenciar uma playlist de músicas. Cada nó deve armazenar:
# ID da música
# Nome da música
# Artista
# Duração (em minutos)
# O menu deve conter as seguintes opções:
# Adicionar música na playlist
# Listar todas as músicas
# Remover música
# Buscar música (por nome ou por artista)
# Mostrar a duração total da playlist
# Avançar para a próxima música / Voltar para a música anterior 
# (usando os ponteiros da lista)
# Sair

class Node:
    def __init__(self, id, name, artist, duration):
        self.id = id
        self.name = name
        self.artist = artist
        self.duration = duration
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self, id, name,artist, duration):
        new_node = Node(id,name,artist,duration)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    def list_songs(self):
        current = self.head
        while current:
            print(f'id: {current.id}, nome: {current.name}, artista: {current.artist}, duracao: {current.duration} minutos')
            current = current.next
    
    def remove_song(self, id):
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
    
    def find_song(self, name=None, artist=None):
        current = self.head
        while current:
            if (name is not None and current.name == name) or (artist is not None and current.artist == artist):
                return f'musica encontrada: id: {current.id}, nome: {current.name}, artista: {current.artist}, duracao: {current.duration} minutos'
            current = current.next
        return 'musica nao encontrada'
    
    def total_duration(self):
        total = 0
        current = self.head
        while current:
            total += current.duration
            current = current.next
        return total
def main():
    playlist = DoublyLinkedList()
    playlist.insert("1", "Song A", "Artist A", 3.5)
    playlist.insert("2", "Song B", "Artist B", 4.0)
    playlist.insert("3", "Song C", "Artist A", 2.5)

    menu = """
    1. adicionar musica na playlist
    2. listar todas as musicas
    3. remover musica
    4. buscar musica (por nome ou artista)
    5. mostrar duracao total da playlist
    6. sair
    """
    while True:
        print(menu)
        choice = input("escolha uma opcao: ")
        if choice == "1":
            id = input("digite o id da musica: ")
            name = input("digite o nome da musica: ")
            artist = input("digite o nome do artista: ")
            duration = float(input("digite a duracao da musica (em minutos): "))
            playlist.insert(id, name, artist, duration)
        elif choice == "2":
            playlist.list_songs()
        elif choice == "3":
            id = input("digite o id da musica para remover: ")
            if playlist.remove_song(id):
                print("musica removida com sucesso.")
            else:
                print("musica nao encontrada.")
        elif choice == "4":
            search_choice = input("buscar por (1) nome ou (2) artista? ")
            if search_choice == "1":
                name = input("digite o nome da musica para buscar: ")
                print(playlist.find_song(name=name))
            elif search_choice == "2":
                artist = input("digite o nome do artista para buscar: ")
                print(playlist.find_song(artist=artist))
        elif choice == "5":
            print(f'duracao total da playlist: {playlist.total_duration()} minutos')
        elif choice == "6":
            break
        else:
            print("opcao invalida. tente novamente.")
main()
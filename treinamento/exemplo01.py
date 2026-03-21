# Inversão de String: Crie uma função que inverta
# uma string sem usar funções prontas de reversão (como .reverse()).

def reverse_string(s):
    reversed_string = ""
    for i in range(len(s) - 1, -1, -1 ):
        reversed_string += s[i]
    return reversed_string


input_string = "Hello, World!"
reversed_result = reverse_string(input_string)
print(reversed_result)
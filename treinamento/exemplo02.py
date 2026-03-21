# Verifique se uma palavra ou 
# frase é igual quando lida de trás para frente (ignorando espaços e pontuação).

def is_palindrome(s):
    cleaned_string = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned_string == cleaned_string[::-1]
input_string = "A man, a plan, a canal: Panama"
input_string = "Hello, World!"

if is_palindrome(input_string):
    print(f'"{input_string}" é um palíndromo.')
else:
    print(f'"{input_string}" não é um palíndromo.')

    


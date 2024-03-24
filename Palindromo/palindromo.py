# Ejercicio: Palíndromo

# Autor: Daniel Jaeger

# Fecha: 2024/03/24

# Escribe una función que reciba un texto y  retorne True o False
# según sean palindromo o no.

# Preguntamos al usuario por un texto

string = input('Introduce un texto: ')

string = string.lower()

# Se define la función palindromo

def palindromo(string):
    string = string.replace(' ', '')
    return string == string[::-1]

# Se define la función main

def main():
    if palindromo(string):
        print('El texto es un palíndromo')
    else:
        print('El texto no es un palíndromo')

# Se llama a la función main

if __name__ == '__main__':
    main()

# Ejercicio 2 ¿Es un anagrama?

# Autor: Daniel Jaeger

# Fecha: 2024/03/11

# Escribe una función que reciba dos palabras (String) y retorne
# verdadero o falso (Bool) según sean o no anagramas.
# - Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
# - NO hace falta comprobar que ambas palabras existan.
# - Dos palabras exactamente iguales no son anagrama.

#  Metodología:

# def obtener_entrada(): Nos permite hablar con el usuario
# def anagrama(string1, string2) compara ambos stirngs.
# while True: nos permite crear un bucle infinito.
# input() nos permite "hablar" con el usuario.
# if : nos permite comparar dos strings.
# return: nos permite devolver un valor.
# else : nos permite imprimir un mensaje si la condición no se cumple.
# isalpha() es un metodo que nos garantiza que el string solo contiene letras.
# sorted() ordena los caracteres de un string.
# print() nos permite imprimir un mensaje de True que nos pedía el enunciado.

# Pedimos al usuario que introduzca una palabra
# Si la palabra contiene solo letras, la devolvemos en minúsculas
# Si no, le pedimos que introduzca solo letras
def obtener_entrada():
    while True:
        string = input('Ingrese una palabra: ')
        if string.isalpha():
            return string.lower()
        else:
            print("Por favor, introduzca solo letras.")

# Función para comprobar si es un anagrama
# Primero ordena las cadenas de caracteres y las compara
def anagrama(string1, string2):
    return sorted(string1) == sorted(string2)

#
string1 = obtener_entrada()
string2 = obtener_entrada()

print(anagrama(string1, string2))
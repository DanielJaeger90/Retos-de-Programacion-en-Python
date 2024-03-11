# Ejercicio 7 Invritiendo Cadenas

# Autor: Daniel Jaeger

# Fecha: 2024/03/11

# Metodología:

# Usamos un procedimiento nuevo: [::-1]
# que nos permite invertir el orden de una cadena de texto
# Desde la posición 0 hasta la última posición, de uno en uno.
# Si cambiasemos el -1 por un -2, invertiríamos la cadena desde
# la segunda posición empezando desde el final.
'''
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
'''
def invertir_cadena():
    string = input('Ingrese una palabra: ')
    print(string[::-1])

invertir_cadena()


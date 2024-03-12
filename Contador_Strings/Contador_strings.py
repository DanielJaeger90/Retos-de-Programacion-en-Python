# Ejercicio 8 Contando Palabras

# Autor: Daniel Jaeger

# Fecha 2024/04/12
'''
/*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */
'''
def contatar_palabras():
    string = input('Ingrese una frase: ')
    string = string.lower()
    signos_puntuacion = [",", ".", "!", "?", ";", ":"]
    for signo in signos_puntuacion:
        string = string.replace(signo, "")
    string = string.split()
    diccionario = {}
    total = 0
    for palabra in string:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
        total += 1
    print(diccionario)
    print("Total de palabras: ", total)

contatar_palabras()
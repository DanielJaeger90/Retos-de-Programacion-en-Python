# Ejercicio 8 Cambiando a binario

# Autor: Daniel Jaeger

# Fecha 2024/04/12

'''/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 *  Para convertir un numero decimal en binario.
 * - Dividimos el número entre 2.
 * - El resultado de la división entera es el primer dígito del número binario.
 * - El residuo de la división es el segundo dígito del número binario.
 * - Repetimos el proceso con el cociente de la división.
 * - El número binario es el residuo de la última división seguido de los residuos de las divisiones anteriores.
 * - Si le pasamos 10 nos retornaría 1010
 */
'''
def transformar_binario():
    while True:
        try:
            num = int(input('Ingrese un número: '))
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    binario = ''
    while num > 0:
        binario = str(num % 2) + binario
        num = num // 2
    print(binario)

transformar_binario()
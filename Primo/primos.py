# Ejercio 4
# Autor: Daniel Iturralde
# Fecha: 2024/03/11

# Escribe un programa:
# 1- Una interfaz que permita al usuario introducir un númoero y la funcion comprobará si es primo o no.
# 2- Que imprima los primeros 100 números primos.

# Notas: Importamos math para poder usar el metodo isqrt
# Esto nos permite calcular la raíz cuadrada entera de un número
# y así poder comprobar si es primo o no.

import math

num = int(input("Introduce un número: "))

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

if es_primo(num):
    print("Es primo")
else:
    print("No es primo")

def primeros_primos(n):
    contador = 0
    numero = 2
    while contador < n:
        if es_primo(numero):
            print(numero)
            contador += 1
        numero += 1

primeros_primos(100)
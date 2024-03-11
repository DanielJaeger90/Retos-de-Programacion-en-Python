# Ejercicio FizzFuzz

# Autor: Daniel Jaeger

# Fecha: 2024/03/11

#Variable
n = 0

# Se define la función fizzfuzz
def fizzbuzz(n):
    while n <= 100:
        n += 1
        if n % 3 == 0 and n % 5 == 0:
            print('FizzBuzz')
        elif n  % 3 == 0:
            print ('Fizz')
        elif n % 5 == 0:
            print ('Buzz')

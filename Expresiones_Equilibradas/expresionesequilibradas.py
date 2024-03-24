# Ejercicio Expresiones Equilibradas

# Autor: Daniel Jaeger

# Fechas: 2024/03/24

# Crea un programa que comprueba si los paréntesis, llaves y corchetes
# de una expresión están equilibrados.
# Equilibrado significa que estos delimitadores se abren y cieran
# en orden y de forma correcta.
# Paréntesis, llaves y corchetes son igual de prioritarios.
# No hay uno más importante que otro.
# Expresión balanceada: { [ a * ( c + d ) ] - 5 }
# Expresión no balanceada: { a * ( c + d ) ] - 5 }

# Se define la función expresionesequilibradas

def expresionesequilibradas(expresion):
    pila = []
    for caracter in expresion:
        if caracter in '({[':
            pila.append(caracter)
        elif caracter in ')}]':
            if not pila:
                return False
            tope = pila.pop()
            if (tope == '(' and caracter != ')') or \
               (tope == '[' and caracter != ']') or \
               (tope == '{' and caracter != '}'):
                return False
    return not pila

# Se define la función main
def main():
    expresion = input('Introduce la expresión a evaluar: ')
    if expresionesequilibradas(expresion):
        print('La expresión está equilibrada')
    else:
        print('La expresión no está equilibrada')

# Se llama a la función main
if __name__ == '__main__':
    main()

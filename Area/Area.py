# Ejercicio 5 Area de un polígono

# Autor: Daniel Jaeger

# Fecha: 2024/03/11

'''
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
'''

# Polígonos

def calcular_area():
    polígono = input("Introduce el polígono: triangulo, cuadrado, rectangulo: ")

    if polígono == "triangulo":
        base = float(input("Introduce la base: "))
        altura = float(input("Introduce la altura: "))
        area = (base * altura) / 2
    elif polígono == "cuadrado":
        longitud = float(input("Introduce la longitud: "))
        area = longitud ** 2
    elif polígono == "rectangulo":
        base = float(input("Introduce la base: "))
        altura = float(input("Introduce la altura: "))
        area = base * altura
    else:
        print("Polígono no válido")
        return

    print(f"El área del {polígono} es: {area}")

calcular_area()
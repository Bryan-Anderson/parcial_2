import math

def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def formas():
    print("1. Circulo | 2. Rectangulo | 3. Triangulo")

def programa():
    while True:
        formas()
        opcion = input("Elije una figura (1/2/3 para salir): ")

        if opcion == '1':
            radio = float(input("Introduce el radio del círculo: "))
            area = calcular_area_circulo(radio)
            print(f"El área del círculo con radio {radio} es: {area:.2f}")
        elif opcion == '2':
            base = float(input("Introduce la base del rectángulo: "))
            altura = float(input("Introduce la altura del rectángulo: "))
            area = calcular_area_rectangulo(base, altura)
            print(f"El área del rectángulo con base {base} y altura {altura} es: {area:.2f}")
        elif opcion == '3':
            base = float(input("Introduce la base del triángulo: "))
            altura = float(input("Introduce la altura del triángulo: "))
            area = calcular_area_triangulo(base, altura)
            print(f"El área del triángulo con base {base} y altura {altura} es: {area:.2f}")
        elif opcion == 'q':
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

programa()

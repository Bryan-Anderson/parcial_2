def mostrar_mensaje(mensaje):
    print("****************************")
    print(mensaje)  # Aquí utilizamos el argumento 'mensaje'
    print("****************************")

def cargar_suma(): 
    valor1 = int(input("ingrese el primer valor: "))
    valor2 = int(input("ingrese el segundo valor: "))
    suma = valor1 + valor2
    print(f"La suma es: {suma}")

# programa principal

mostrar_mensaje("el programa calcula la suma de dos valores ingresados por teclado")
cargar_suma()

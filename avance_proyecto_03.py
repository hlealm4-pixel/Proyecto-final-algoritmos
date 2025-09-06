# Menu
def mostrar_menu():
    print("\n========== MENU PRINCIPAL ==========")
    print("| 1. Ingresar notas                |")
    print("| 2. Registrar un nuevo curso      |")
    print("| 3. Registrar un nuevo estudiante |")
    print("| 4. Ver datos de un estudiante    |")
    print("| 5. Salir                         |")
    print("====================================")

def instrucciones_ingresar_notas():
    print("\n\n====================================== INGRESAR NOTAS ======================================")
    print("\nINSTRUCCIONES\n")
    print(" - Las notas que se ingresen deben estar en el rango entre 0 y 100.")
    print(" - Si termino de ingresar notas, escriba stop y finalizara el bucle.\n")

def calcular_promedio(total, cantidad_notas):
    if cantidad_notas == 0:
        return 0
    return total / cantidad_notas

def imprimir_promedio(promedio, cantidad_notas):
    if cantidad_notas == 0:
        print("\nNo se ingreso ninguna nota")
    else:
        print(f"\nSe ingresaron {cantidad_notas} nota(s)")
        print(f"El promedio de las notas ingresadas es de: {promedio}")

def ingresar_notas():
    instrucciones_ingresar_notas()
    total = 0
    cant_notas = 0
    while True:
        nota = input("Ingrese la nota: ")
        try:
            nota = float(nota)
        except ValueError:
            if "stop" in nota.lower():
                break
        if nota < 0 or nota > 100:
            print("Nota incorrecta, la nota debe estar en el rango entre 0 y 100")
            continue
        total += nota
        cant_notas += 1
    promedio = calcular_promedio(total, cant_notas)
    imprimir_promedio(promedio, cant_notas)

# Muestra el menu principal
mostrar_menu()

# Inicia un bucle infinito para seleccionar opciones
while True:
    opcion = int(input("Seleccione una opcion: "))
    if opcion == 1:
        ingresar_notas()
        mostrar_menu()
    elif opcion == 2:
        continue
    elif opcion == 3:
        continue
    elif opcion == 4:
        continue
    elif opcion == 5:
        break
    else:
        print("Esta opcion no existe, intente nuevamente")

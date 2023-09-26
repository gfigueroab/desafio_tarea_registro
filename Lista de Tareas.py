tareas = []

def agregar_tarea():
    tarea = input("Ingresa una nueva tarea:")
    tareas.append(tarea)
    print("Tarea agragada con éxito")


def eliminar_tarea():
    tarea = int(input("Ingresa la tarea que deseas eliminar:"))-1
    if tarea < len(tareas):
        tareas.pop(tarea)
        print("Tarea eliminada con éxito")
    else:
        print("La tarea no éxiste en la lista")


def mostrar_tareas():
    if tareas:
        print("Lista de tareas:")
        for i, tarea in enumerate(tareas,1):
            print(f"{i}, {tarea}")

def main():
    opcion = 0

    while opcion ≠ 4:
        print("\n --- Lista de Tareas ---")
        print("1. Agrear tarea")
        print("2. Eliminar Tarea")
        print("3. Mostrar Tarea")
        print("4. Salir")

        opcion = int(input("Seleccione una opcion:"))

        if opcion == 1:
            agregar_tarea()
        elif opcion == 2:
            eliminar_tarea()
        elif opcion == 3:
            mostrar_tareas()
        elif opcion == 4:
            print("Hasta luego!!!")
        else:
            print("Opcion no válida")


if __name__ == "__main__":
    main()



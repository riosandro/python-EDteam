"""
Vamos a crear un programa de hacer tareas, que nos pida la tarea a hacer y que podamos marcar una tarea completada
Los puntos a relizar son los siguientes.
1: Crear la funcion principal y punto de entrada.
2: Crear el menu de opciones del ToDo.
3: Mostrar listado de tareas.
4: Agregar una tarea a la lista.
5: Marcar una tarea como realizada.
5: Eliminar una tarea de la lista.
"""
import os
runProgram = True # Siempre iniciamos el programa en True
todolist = [] # creamos una lista vacia la cual iremos llenando a medida que el usuario valla creando mas tareas

# Función para mostrar las opciones del menu
def showMenuOptions():
    print("")
    print("")
    print("Por favor seleccione una opción:")
    print("")
    print("")
    print("1. Crear un tarea")
    print("2. Marcar como realizada una tarea")
    # print("3. Actualizar una tarea")
    print("4. Borrar una tarea")
    print("5. Salir")

# Función para mostrar todas las tareas
def showTodoList():
    global todolist
    print()
    print()
    print("************************************")
    for todo in todolist: #Con este for recorremos la lista y mostramos las tareas disponibles.
        print("Tarea",f"{todolist.index(todo) + 1}. {todo}")
    print("************************************")
    print()
    print() 
 
# Función para guardar las tareas en la variable "todolist"
def createTodo():
    os.system("cls") # Mac => os.system("clear") Con esto se limpia la consola al crear una nueva tarea
    global todolist
    print("Crear un nueva tarea")
    todo = input("Por favor ingrese el nombre de la tarea: ")  # Aqui recibimos la tarea ingresada por el usuario y la guardamos en la variable todo
    todolist.append(todo)  # Aqui agregamos una tarea la la lista
    # Mostrar la lista de tareas
    showTodoList()

# Función para marcar una tarea como realizada
def madeTodo():
    global todolist
    print("Actualizar una tarea")
    todoId = int(input("Ingrese el número de la tarea que quiere marcar como hecha: "))
    todolist[todoId - 1] = todolist[todoId - 1] + "✅"
    showTodoList()

# # Función para marcar una tarea como realizada
# def updateTodo():
#     global todolist
#     print("Actualizar una tarea")
#     updateId = int(input("Ingrese el número de la tarea que quiere actualizar: "))
#     todolist[updateId - 1]
#     showTodoList()


# Función que nos permite borrar una tarea
def deleteTodo():
    global todolist
    print("Borrar una tarea")
    todoId = int(input("Ingrese el número de la tarea que quiere borrar: "))
    del todolist[todoId - 1]
    showTodoList()
# Esta es la funcion principal, cuando el usuario escoge una de las opciones invocamos su funcion por medio del Match
def main():
    global runProgram
    print(".: WELCOME TO A PYTHON TO DO LIST :.")
    flag = True

    while runProgram:
        while flag:
            showMenuOptions() # aquí invocamos la función para mostrar las opciones del menu.
            option = int(input("Ingresa el número de la opción: "))

            match option:
                case 1:
                    createTodo()
                case 2:
                    madeTodo()
                # case 3:
                #     updateTodo()
                case 4:
                    deleteTodo()
                case 5:
                    print("Hasta Luego!!!")
                    runProgram = False
                    flag = False
                case _:
                    print("Opción no reconocida. Ingrese una opción válida.")
if __name__ == "__main__":
    main()        
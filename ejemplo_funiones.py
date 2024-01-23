"""
EJEMPLO DE QUE FUNCION SE EJECUTA PRIMERO EN UN CODIGO
"""
def funcion_uno ():
    print("Esta es la funcion uno")
def funcion_dos ():
    print("Esta es la funcion dos")
def funcion_tres ():
    print("Esta es la funcion tres")
def funcion_cuatro ():
    print("Esta es la funcion cuatro")
def funcion_cinco ():
    print("Esta es la funcion cinco")

if __name__ == "__main__":
    funcion_cinco ()
    funcion_uno () 
    funcion_tres ()
    funcion_cuatro ()
    funcion_dos ()
        
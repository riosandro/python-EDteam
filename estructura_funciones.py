# ESTRUCTURA DE UNA FUNCION
# Las funciones nos permiten ejecutar varias porciones de codigo
def fibonacci (n): # Creamos una funcion y le pasamos un elemento por parametro
    # Creamos dos variables una con valor cero y la otra con valor 1
    a, b = 0, 1
    # Creamos un bucle while para recorrer el parametro de la funcion
    while a < n:
        print(a, end=" ")
        # Ahora pasamos el valor de b para a y a b le ponemos como valor el resultado de la suma de a mas b
        a, b = b, a + b
    print("")
fibonacci(1000) # Le damos un valor al parametro de la funcion
fibonacci(3000) # Le damos un valor al parametro de la funcion
fibonacci(4500) # Le damos un valor al parametro de la funcion
fibonacci(2100) # Le damos un valor al parametro de la funcion
# Como es una funcion la puedo ejecutar las veses que yo quiera
"""
NOTA: Para que podamos ver el resultado de forma horizontal debemos de uvicar bien la indentacion en los print
"""
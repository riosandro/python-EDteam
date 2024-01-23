# Las funciones siempre retornan un valor, si nosotros no definimos un valor a la funcion, esta siempre va adevolver
# un valor "None"
# Forma de retornar uno o varios argumentos d euna funcion
def suma(num1, num2):
    resul = num1 + num2
    return resul
print(suma(25, 30))

# Esto da el mismo resultado que lo de arriba
def suma(num1, num2):
    resul = num1 + num2
    print(resul)
suma(25, 30)

# Podemos crear un diccionario para invocar nuestra funcion
def operaciopnesMatematicas(nume1, nume2):
    resultados = dict(sumas = nume1 + nume2, rest = nume1 - nume2, mult = nume1 * nume2, divi = nume1 / nume2
    )
    print(resultados)
operaciopnesMatematicas(5, 10)    

# Otra forma de hacer lo mismo de arriba
def operaciopnesMatematicas(nume1, nume2):
    sumas = nume1 + nume2
    rest = nume1 - nume2
    multi = nume1 * nume2
    divi = nume1 / nume2
    return sumas, rest, multi, divi
sum, res, mul, div = operaciopnesMatematicas(5, 10)
print(sum)
print(res)
print(mul)
print(div)

# Si queremos usar una variable global dentro de una funcion o dentro de metodo usamos la palabra recerbada
# de python que es "global" segida del nombre d ela variable, veamos un ejemplo.

name = "Jose" # Variable global

def usuario():
    global name # Invocamos la variable global
    name = name + " Rios" # Usamos una variable locak con el mismo nombre de la variable global, le podemos poner cualquier nombre

    print(name) # Aqui llamamos a la variable local.
usuario()# Siempre debemos de llamar a la funcion     

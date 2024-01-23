# Sets
# Los sets a diferencia  elos diccionarios, no reciben una llave, valor ino que solo
# reciben el valor y cuano lo llamamosa nos devuelve los datos en forma desordenada y si hay algun dato repetido
# este dato se reemplaza o no se muestra, por eso si queremos usar sets tenemos que especificar bien los datos para que no
# hallan repetidos. Y al igual que los diccionarios los sets se crean usando brakets.

names = {"Jose", 12345, 10.34,"Danny", "Danny", True, 1, False, 0}
# PARA TENER EN CUENTA: Cuando usamos la palabra False y True y a la ves usamos los numeros 1 y 0 solo se muestra True
# y False y los numeros 1 y 0 no se muestran ya que en systema el numero 1 es igual a True y el numero 0 es igual a False
# Por lo tanto si los usamos juntos estariamos repitiendo los datos.
print(names) #Impriminos esto y nos muestra todo en desorden y solo me muestra un solo "Danny"

# Otra forma de crear sets
name =set(("Jose", 12345, 10.34,"Danny", "Danny", True, 1, False, 0)) # Como podemos ver aqui creamos una tupla dentro del set
# Y el resultado es el mismo
print(name)

# CURIOSIDAD
texto = ("El mundo es un citio donde los seres humanos nos creemos los duenos de todo")
print (set(texto)) # En esta ocacion imprimimos un texto y nos muestra un set de letras separadas por coma y ninguna se repite.

var = None # Por defecto
var = "pepito"
print(var)
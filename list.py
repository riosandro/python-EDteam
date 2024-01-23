# LIST (Listas)
cosas = ["Manzanas", 12345, "Pears", "Moras", 102.09, "Naranja", "Pinas"] # Creamos una lista, las listas pueden ser
# de solo enteros, flotantes, strings, o combinadas como en este ejemplo.
print(cosas[1]) # Accedemos a un elemento d ela lista
print(len(cosas))# Accedemos a la longitud de la lista
print(cosas[-1])# Accedemos al ultimo elemento de la lista
print(cosas[2:5])# Accedemos a un rango de elementos en este caso accedemos desde el elemento 2 hasta el elemento 4,
# aunque el numero es 5 el elemento que me muestra es el que esta en la posicion 4 contando desde cero, si queremos
# que muestre el numero deceado ponemos un numero mas grande o ponemos +1 'print(cosas[2:6])', 'print(cosas[2:5+1])'
cosas [2] = "peras" # Modificamos o remplazamos un elemento d ela lista, en este caso modificamso el elemento d ela poscion 2
print(cosas)

cosas [1:4] = [54321, "Mangos", "Papayas",] #Cambiamos  o modificamos los elementos en un rango
print(cosas)
nuevas_cosas = cosas[1:4]#Extraemos elementos desde un rango espesifico.
print(nuevas_cosas)
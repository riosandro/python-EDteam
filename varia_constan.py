# name = input("Ingresa tu nombre: ")
# apellido = input("Ingresa tu apellodo: ")
# edad = int(input("Ingresa tu edad: "))
# print("Mi nombre completo es: " + name + " " + apellido + " y mi edad es: " +str(edad))

# CONSTANTES
# Las constantes en py no existen en realidad, osea si creamos una constante esta puede cambiar a lo largo del 
# nuestro proyecto, en py las constants no funcionan como en otros lenguages de programacion
# donde las constantes tienen un valor fijo y estas no cambia a lo largo del proyecto.
# Cuando creamos una constante en py debemos de ponerle nombre sinificativo y en mayusculas y es mejor comentar
# que esa es una constante por ejemplo: PI = 3.1416 esa es una constante que es fija ya que el numero pi no 
# puede cambiar pero tenemos que tener cuidado ya que esta constante a lo largo del proyecto puede cambiar de valor.

# Constantes
PI = 3.1416 # PI es numero fijo
SECONDS_IN_ONE_HOUR = 3600 # La cantidad de segundos en una hora no cambia

PI = 5.1234 # El numero de pi cambia ya que las constantes en py en realidad no son constantes

number1 = 100
number2 = number1
print(id(number1)) #la palabra recervada id se usa para saber el id de el espacio que tiene recervado una 
# variable en el systema, no hace ninguna funcion en especial en nuestro proyecto
print(id(number2))
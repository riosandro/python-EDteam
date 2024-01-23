# TIPOS DE DATOS
# NUMERICON
# int (tipos de datos enteros)=> 10, 345, 90, 876
# float(tipos de datos flotantes o decimales)=> 10.3, 12.34, 100,32
# complex (numeros conplejos, veremos esto maa a profundidad en un futuro)=> 1 + 4j, 4

# STRINGS
# str (string o cadena d etexto)=>"Hola Mundo!"

# BOOLEANOS
# bool(Tipos de datos falso o verdadero)=> false, true
# Podemos utilizar la palabra recervada 'type' para saver que tipo de dato es un dato que estemos usando
entero = 12345
flotante = 35.678
cadena = "Hola mundo!" #Si queremos crear un parafo grande y concervar los saltos de linea debemos d eutilizar comillas
# triples cadena = """El mumdo es una locura, con todo sus seres estan acabando con
# el planeta y sus habitantes! """ A la hora de imprimir sus saltos de linea se conservaran.
print(cadena[5:9+1]) #De esta forma podemos extraer un pedazo de la cadena o un solo caracter si ponemos un solo 
# numero quiere decir que vamos a extraer el caracter que se encuentra en esa posicion. Si ponemos un numero
# separado por dos puntos quiere decir que el primer numero sera desde donde empieza la cadena que queremos extraer
# y el segundo numero es hasta donde vamos a cortar la cadena le ponemos un +1 para que no la de completa
print(len(cadena))#De esta forma sabremos la longitud de una cadena de texto.

booleanos = entero == flotante
complejo = 4 + 1j
millon_flotante = 1e6 # Usamos esta simplisidad para no escribir todos los ceros en un numero redonde largo como lo es
# el numero millon, con el 1 le decios que ese sera el primer numero co  la e le decimos que va a cer un numero largo 
# y con el 6 le decimos la cantidad de ceros que nececitamos, al final nos mostrara un umero flotante 1000000.0

print(entero)
print(entero)
print(entero)
print(entero)
print(flotante)
print(cadena)
print(booleanos)
print(complejo)
print(millon_flotante)

print(type(entero))
print(type(flotante))
print(type(cadena))
print(type(booleanos))
print(type(complejo))
print(type(millon_flotante))

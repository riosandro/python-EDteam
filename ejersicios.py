# 1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
# (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
# def max(num1, num2):
#     if num1 < num2:
#         print(num2)
#     else:
#         print(num1)
# max(5, 8)

# 2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
# def maxtres(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#         print(num1)
#     elif num2 > num1 and num2 > num3:
#         print(num2)
#     # elif num3 > num1 and num3 > num2:
#     #     print(num3)
#     # else:
#     #     print("Son iguales!") 
#     else:
#         print(num3) 
# maxtres(18,14,16)

# 3 - Definir una función que calcule la longitud de una lista o una cadena dada. 
# (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta 
#  un muy buen ejercicio.
# def long(cadena):
#     coun = 0
#     for x in cadena: 
#       coun += 1
#     return coun
# print (long(["Manzana", "Uvas", "Mango", "Peras", "Mora", 123456]))

# 4 - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False
# def vocales(vocal):
#     if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
#             print(True)
#     elif vocal == "A" or vocal == "E" or vocal == "I" or vocal == "O" or vocal == "U":
#             print(True)      
#     else:
#             print(False)
# vocales("m")

# 5 - Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números
# de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
# def sum(suma):
#     resul = 0
#     for i in suma:
#         resul +=i
#     return resul
# print(sum([1,2,3,4])) 

# def mult(multipli):
#     resul = 1 # No pongo 0 porque todo numero multiplicado por 0 es igual a cero
#     for i in multipli:
#         resul *=i
#     return resul
# print(mult([1,2,3,4]))    

# 6 - Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena 
# "Hola Mundo" debería devolver la cadena "!odnuM aloH"  
# def inversa (cadena):
#      invertida = ""
#      cont = len(cadena)
#      indice = -1
#      while cont >= 1:
#          invertida += cadena[indice]
#          indice = indice + (-1)
#          cont -= 1
#      return invertida      
# print(inversa("Hola Mundo!"))

# 7 - Definir una función es_palindromo() que reconoce palíndromos 
# (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") 
# tendría que devolver True.

def es_palindromo (cadena2):
    cadena1=["radar"]
    palabra_invertida =  cadena1
    indice = 0
    cont = 0
    for i in range (len(cadena2)):
        if palabra_invertida[indice] == cadena2[indice]:
            indice += 1
            cont += 1
        else:
            print ("No es palindromo")
            break
    if cont == len(cadena2): #Si el contador = a la cantidad de letras de la cadena
        print ("Es palindromo")
print(es_palindromo("radares"))
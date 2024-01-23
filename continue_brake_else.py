# CONTINUE => lo que hace continue es que cuando encuentra una coincidencia dada el programa salta esa coincidencia
# y continua con el programa.

# BREAK =>lo que hace breakes que cuando encuentra una coincidencia dada el programa termina la ejecucion del programa

# ELSE => lo que hace else es que cuando una condicion no se cumple, else ejecuta una centencia.

# Para estos ejemplos vamos a crear una lista.
# frutas = ["Mango", "Pera",12.56, "Naranja", "Manzana", 1369, ]
# for x in frutas: # Por medio de un for vamos a recorrer nuestra lista
#      if x == "Pera": # por medio de un condicional vamos a evaluar si un elemento se encuentra en la lista
#          print("X es pera")
#          print(x)
# Con lo anterior el programa nos muestra el mensaje y la fruta Pera 
        
# Para estos ejemplos vamos a crear una lista.
# frutas = ["Mango", "Pera",12.56, "Naranja", "Manzana", 1369, ]
# for x in frutas: # Por medio de un for vamos a recorrer nuestra lista
#     if x == "Pera": # por medio de un condicional vamos a evaluar si un elemento se encuentra en la lista
#         print("X es pera")
#         continue
#     print(x) 
#Con lo anterior usamos continue para que el programa continue con su ejecucion y no muestra el elemento elegido en este caso [Pera]    

# # Para estos ejemplos vamos a crear una lista.
# frutas = ["Mango", "Pera",12.56, "Naranja", "Manzana", 1369, ]
# for x in frutas: # Por medio de un for vamos a recorrer nuestra lista
#     if x == "Pera": # por medio de un condicional vamos a evaluar si un elemento se encuentra en la lista
#         print("X es pera")
#         break
#     print(x) 
# #Con lo anterior usamos break para que el programa rompa con su ejecucion y no muestra el resto de los elemento de la lista   

# Para estos ejemplos vamos a crear una lista.
frutas = ["Mango", "Pera",12.56, "Naranja", "Manzana", 1369, ]
for x in frutas: # Por medio de un for vamos a recorrer nuestra lista
    if x == "Pera": # por medio de un condicional vamos a evaluar si un elemento se encuentra en la lista
        print("X es pera")
    print(x)
else:       
    print("Fin del ciclo!") 
#Con lo anterior usamos break para que el programa rompa con su ejecucion y no muestra el resto de los elemento de la lista   
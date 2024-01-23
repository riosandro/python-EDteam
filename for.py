# FOR
# for x in range(10):
#      print(x)

# for i in range(2, 10, 3): # Empieza desde 2 y va de 3 en 3
#      print(i)

# numero = input("Ingresa u numero: ")
# for i in range(1, int (numero)+1): # Empieza desde 1 y va hasta el numero que ingresa el usuario y le sumamos 1 para que de los numeros completos
#      print(i)

# Podemos recorrer una lista
# frutas = ["Mango", "Naranja", 'Pera', "Uva"]
# for s in frutas:
#      print(s)

# Podemos validar si un elemnto esta o no en una lista
# frutas = ["Mango", "Naranja", 'Pera', "Uva"]
# for s in frutas:
#     if s == "Pera":
#         print(s)

# num = 5
# for x in range(1, 10 + 1):  # Le pongo +1 para que me muestre hasta el 10
#     resu = num*x
#     print(x, " X ", num, " = ", resu)


num1 = 3
sum = 0

for num1 in range(1000):

    if num1 % 3 == 0 or num1 % 5 == 0:
        sum += num1
print(sum)

#  Fivonashi Secuence
# prev, cur = 0, 1
# total = 0
# while True:
#     prev, cur = cur, prev + cur
#     if cur >= 4000000:
#         break
#     if cur % 2 == 0:
#         total += cur
# print(total)

# num = 13195
# resul1 = 0
# i = 3
# for i in range(num):
# #     resul1 = 1319 - 5*2
#     if num % i == 0:
#         print("El numero no es primo!")
#     i += 2
#     num = num / i
# print("Es primo")
# print(num)


# def es_primo(num):
num = 600851475143

for n in range(2,   num):
    if num % n == 0:
        print("No es primo", n, "es divisor")
          #   return False

print("Es primo")
#     return True

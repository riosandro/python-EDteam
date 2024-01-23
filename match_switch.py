# MATCH (SWITCH)
"""
Match es igual a switch donde evaluamos una condicion y si esta se cumple se ejecuta un pedazo de codigo

"""
# Creamos una condicion
mes = "Marz"
match mes:
    case "Enero":
        print("El mes es correcto 1: ")
    case "Febrero":
        print("El mes es correcto: 2")
    case "Marzo":
        print("El mes es correcto: 3")
    case "Abril":
        print("El mes es correcto: 4")
    case "Mayo":
        print("El mes es correcto: 5")
    case "Junio":
        print("El mes es correcto: 6")
    case "Julio":
        print("El mes es correcto: 7")
    case "Agosto":
        print("El mes es correcto: 8")
    case "Septiembre":
        print("El mes es correcto: 9")
    case "Octubre":
        print("El mes es correcto: 10")
    case "Noviembre":
        print("El mes es correcto: 11")
    case "Diciembre":
        print("El mes es correcto: 12")
    case _:
        print("El mes no existe")
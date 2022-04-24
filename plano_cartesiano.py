""" PROGRAMA 8 
ENCONTRAR EL CUADRANTE DE UN PUNTO EN EL PLANO CARTESIANO """

print(" -------------------------------- ")
print(" ----PUNTOS Y SUS CUADRANTES----- ")
print(" -------------------------------- ")

# input

x = int(input("DIgite el valor de x: "))
y = int(input("Digite el valor de y: "))

# processing

if x > 0 and y == 0:
    msj = "se encuentra en el eje x "

if x < 0 and y == 0:
    msj = "se encuentra en el eje x "

if x == 0 and y < 0:
    msj = "se encuentra en el eje y "

if x == 0 and y > 0:
    msj = "se encuentra en el eje y "

if x > 0 and y > 0:
    msj = "se encuentra en el cuadrante No 1. "

if x < 0 and y > 0:
    msj = "se encuentra en el cuadrante No 2."

if x < 0 and y < 0:
    msj = "se encuentra en el cuadrante No 3 "

if x > 0 and y < 0:
    msj = "se encuentra en el cuadrante No 4"

# output

print(" el punto con esas coordenadas " + msj)


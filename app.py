# TP 4 - Estructuras Repetitivas
# Alumno: Enrique Alejandro Juarez Alvarez
# Tecnicatura Universitaria en Programación - UTN A Distancia

# 1. Números del 0 al 100
for i in range(101):
    print(i)

# 2. Contar dígitos de un número
numero = input("Ingresá un número entero: ")
print("Cantidad de dígitos:", len(numero))

# 3. Sumar números entre dos valores dados (sin incluirlos)
inicio = int(input("Primer número: "))
fin = int(input("Segundo número: "))

suma = 0
for i in range(inicio + 1, fin):
    suma += i

print("La suma entre ellos es:", suma)

# 4. Sumar números hasta que se ingrese 0
total = 0
while True:
    num = int(input("Ingresá un número (0 para salir): "))
    if num == 0:
        break
    total += num

print("Suma total:", total)

# 5. Juego de adivinar un número
import random
secreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adiviná el número (0 al 9): "))
    intentos += 1
    if intento == secreto:
        print("¡Acertaste! Lo lograste en", intentos, "intentos")
        break
    else:
        print("No es, seguí intentando...")

# 6. Números pares del 100 al 0 (orden decreciente)
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# 7. Sumar números desde 0 hasta uno indicado
hasta = int(input("Sumar desde 0 hasta: "))
total = 0
for i in range(hasta + 1):
    total += i

print("La suma total es:", total)

# 8. Contar pares, impares, positivos y negativos de 100 números
pares = impares = positivos = negativos = 0

for _ in range(100):  # cambiar a un número menor para pruebas
    n = int(input("Ingresá un número: "))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    if n >= 0:
        positivos += 1
    else:
        negativos += 1

print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

# 9. Calcular la media de 100 números
total = 0
for _ in range(100):  # se puede cambiar a un número menor para testear
    num = int(input("Número: "))
    total += num

print("Media:", total / 100)

# 10. Invertir los dígitos de un número
numero = input("Ingresá un número: ")
invertido = numero[::-1]
print("Invertido:", invertido)

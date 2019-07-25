#Cada término en la serie de Fibonacci es generado a partir de la suma de los dos términos previos, empezando de 1 y 2, los diez primeros términos serán: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, … Considerando los términos de la serie de Fibonacci que son impares, y por debajo de un millón encuentre la suma de dichos términos.

suma = 0
a = 1
b = 1
c = 0

while c <= 1000000:
    if c % 2 != 0:
        suma += c
    a = b
    b = c
    c = a + b

print(suma)


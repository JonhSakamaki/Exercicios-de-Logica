import math

print("Medindo a area de um circulo com base no tamanho do raio...")
r = float(input("DIgite o tamanho do raio: "))

ar = math.pi * (r ** 2)
print("A área do raio com tamanho de {}, é igual a {:.2f}".format(r, ar))
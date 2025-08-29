n1 = int(input("Digite o primeiro numero sendo INTEIRO: "))
n2 = int(input("Digite o segundo numero sendo INTEIRO: "))
n3 = float(input("Digite o terceiro numero sendo REAL "))

p1 = (n1 * 2) + (n2 / 2)
p2 = (n1 * 3) + n3
p3 = n3 ** 3 

print("o produto do dobro de {}  com metade de {} é igual a {}".format(n1, n2, p1))
print("a soma do triplo de {:.2f} com {:.2f} é igual a {:.2f}.".format(n1, n3, p2))
print("Sendo {:.2f} elevado ao cubo e igual a {:.2f} ".format(n3, p3))
import math

ar = float(input("Qual o tamnaho da area em M² voce deseja pintar: "))

ln = ar / 3
qtl = math.ceil(ln / 18)
ptot = qtl * 80

print("Com base nos dados adiquiros, para pintar o espaço de {:.2f}m², serão nescessarios {} latas de tintas, oque custará R${:.2f}".format(ar, qtl, ptot))
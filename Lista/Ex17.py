import math

m = float(input("Quantos M²(metros quadrados) você deseja pintar: "))
tp = input("Escolha o tipo de compra (lata / galao / os dois): ").lower()

lt = m / 6 * 1.10
qtl = math.ceil(lt/18) * 80
qtg = math.ceil(lt/3.6) * 25


latas = int(lt // 18)
resto = lt - (latas * 18)
galoes = math.ceil(resto / 3.6)
ptot = (latas * 80) + (galoes * 25)

if tp.lower() == "lata":
    print("Como você escolheu lata para pintar {}M², você irá gastar R${} ".format(m, qtl))
elif tp.lower() == "galao":
    print("Como você escolheu galoes para pintar os {}M², você irá gastar R$ {}".format(m, qtg))
else:
    print("Por escolher misturar entre latas e galoes para pintar os {}M², você irá gastar um total de {} latas e {} galões, custando um total de R${}".format(m, latas, galoes, ptot))
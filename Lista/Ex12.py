print("Boa Noite! Agora iremos calcular seu peso ideal!")

alt = float(input("Por favor, Digite sua altura: "))

imc = 22

psid = imc * (alt ** 2)

print("Feito! De acordo com sua altura {:.2f}cm, seu peso ideal é {:.2f}kgs".format(alt, psid))
sh = float(input("Digite quanto voce ganha por hora trabalhada: "))
hm = int(input("Agora digite as horas trabalhada no mês: "))

vst = sh * hm

print("Com base nos dados informados, ao receber R${:.2f} por hora, com um total de {} horas trabalhadas no mês, voce está recebendo R${:.2f} mensalmente.".format(sh, hm, vst))
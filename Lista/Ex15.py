sl = float(input("Quanto ganha por hora: "))
hr = float(input("Quantas horas voce trabalha no mês: "))

sb = sl * hr
ir = sb * 0.11
inss = sb * 0.08
sd = sb * 0.05
desc = inss + sd + ir
sq = sb - desc

print("Sabendo que voce recebe {:.2f} por hora e trabalha {:.2f} horas por mes, seu salario bruto é de {:.2f}".format(sl, hr, sb))
print("Sabendo q voce tera os descontos de IR {:.2f}, INSS {:.2f}, e Sindicato {:.2f}, sendo um total de {:.2f}, seu Salario liquido sera de {:.2f} ".format(ir, inss, sd, desc, sq))
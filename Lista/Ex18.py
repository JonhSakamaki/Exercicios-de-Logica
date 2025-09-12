tm = float(input("DIgite o tamanho do arquivo(em MB): "))
vl = float(input("Digite a velocidade da internet(em MBps): "))

tmb = tm * 8

ts = tmb / vl

tm = ts / 60

print("O tempo aproximado ate o fim do download é de {:.2f} minutos.".format(tm))
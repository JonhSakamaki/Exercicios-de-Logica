print("=-=Caulculando media bimestral=-=")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

m = ((n1 + n2 )+ (n3 + n4)) // 4

print("Apos calcular as notas do aluno, sua media bimestral é de {}".format(m))
sx = str(input("Qual Seu Sexo(F/M)? ")).lower()

if sx.lower() == "f":
    print("Seu Sexo é FEMININO!")
elif sx.lower() == "m":
    print("Seu Sexo é MASCULINO!")
else:
    print("Opção INVÁLIDA!")
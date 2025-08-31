
def psid(Altura_m: float, sexo: str) -> float:
    sexo = sexo.strip().lower()
    if sexo == "homem":
        return (72.7 * alt) - 58
    elif sexo == "mulher":
        return (62.1 * alt) - 44.7
    else:
        raise ValueError ("Sexo Invalido, tente novamente!")
    

try:
    print("Olá, agora com base em suas informações iremos medir seu peso ideal!")    
    sx = str(input("Qual o seu Sexo(homem/mulher): "))
    alt = float(input("Qual a sua altura: "))
    ideal = psid(alt, sx)
    print("Sabendo que você é {} e sual altura é {} seu peso ideal é {:.2f}".format(sx, alt, ideal))
except ValueError as e:
    print("Erro", e)        
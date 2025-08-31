print("Bom dia! Espero que tenha tido uma ótima pescaria.")
print("Lembrando que o limite de peso da pesca é de 50kgs, passar dele terá de pagar 4,00 por kilo acima do limite")
kg = float(input("Quantos kilos de peixe voce pescou hoje: "))

ps = (kg - 50) * 4

if kg > 50:
    print("Você passou do peso permitido pelo regulamento de pesca, sua multa sera de R${:.2f}".format(ps))
else:
    print("Você pescou {:.2f}kgs dessa vez, pode ficar tranquilo que nao passou do peso permitido!".format(kg))
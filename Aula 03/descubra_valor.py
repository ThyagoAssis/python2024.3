print(25*"#")
print("Descubra o numero secreto")
print(25*"#")
print("")
print(43*"#")
print("Você é capaz de descobrir o numero secreto?")
print(43*"#")

secreto_num = 12
fichas = int(input("Quantas fichas? "))
contador = 0

while contador < fichas:
    palpite = int(input("Informe seu palpite: "))
    print("Seu palpite é: {}".format(palpite))

    if (secreto_num == palpite):
        print("Você acertou miseravi")
    else:
        print("Você errou miseravi")
    contador += 1
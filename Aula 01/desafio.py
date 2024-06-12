'''
    Solicitar ao usuario a cor da camisa e salvar a resposata
    dentro de uma variável

    Ao final exiba a cor da camisa
'''

#A função input recebe uma informação que vem de fora
nome = "Thyago"
cor_camisa = input("Qual a cor da sua camisa? ")

#Saida da informação
#Primeira forma de exibir
print("Primeria - A cor da camisa é: ", cor_camisa, nome)

#Segunda forma de exibir
print(f"Segunda - A cor da camisa é {cor_camisa} {nome}")

#Terceira Forma
print("Terceira - A cor da camisa é: {} {}".format(cor_camisa,nome ))


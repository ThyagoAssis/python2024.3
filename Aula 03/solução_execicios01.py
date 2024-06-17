'''
Desafio 01
Elabore um programa em python para ler um valor
inteiro e informar, através de uma mensagem
se este valor é um número par ou ímpar.
'''
# A função int() converte para inteiros
#A função float() converte para fracionarios
valor = int(input("Informe um valor: "))
print(type(valor))

resto = valor % 2
if resto == 0:
    print("O valor é par")
else:
    print("O valor é impar")


'''
Desafio 02
Implemente um programa que solicite ao usuário dois valores, 
em seguida verifica se o primeiro é múltiplo do segundo,  
seu programa deverá exibir a mensagem: 
“São múltiplos” ou “Não são múltiplos”

'''
valor_um = int(input("Informe o primeiro valor: "))
valor_dois = int(input("Informe o segundo valor: "))
modulo = valor_um % valor_dois

if modulo == 0:
    print("Os valores são multiplos!")
else:
    print("Os valores não são multiplos!")


'''
Desafio 03
Desenvolva um programa para ler um valor inteiro e apresentar
     *  a. Exibir a mensagem “número negativo” se n < 0.
     *  b. Exibir a mensagem “zero” se n = 0.
     *  c. Exibir a mensagem “número positivo” se n > 0.
'''
numero = int(input("Informe um numero: "))

if numero == 0:
    print("O numero é zero")
elif numero > 0:
    print("O numero é positivo")
elif numero < 0:
    print("O numero é negativo")
else:
    print("Opção invalida!")

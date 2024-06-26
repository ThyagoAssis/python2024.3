'''
1 – Construa um algoritmo em Python que leia 20 valores inteiros
e calcule seu somatório.

soma = 0
for contar in range(20):
    soma = soma + contar
    print(f"Valor de contar:  {contar}, Valor de soma: {soma}")
'''
'''
2 – Construa um programa em python que solicite ao usuário um  
valor entre 10 e 100,  
caso o usuário digite  um valor menor que 10 ou maior que 100,   
envie uma mensagem informando que os valores são inválidos  
caso contrário conte de zero até o numero digitado pelo usuário
'''
valor = int(input("Informe um valor entre 10 e 100: "))
#and - as duas condições devem ser verdadeiras
#or - basta que uma condição seja verdadeira
if valor < 10 or valor > 100:
    print("Valor Invalido!")
else:
    for contador in range(valor+1):
        print(contador)
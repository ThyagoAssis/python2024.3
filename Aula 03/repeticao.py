'''
O que é um loop (Repetição)?
    É algo que acontece rotineiramente, ou seja, é algo que se repete

    Estruturas de repetição basica
        >while (Enquanto)
        >for (Ler uma lista)
'''

print("Repetição com while")
# Para o while funcionar ele precisa de um contador
# O contador é quem informa ao while quando deve parar
# O contador é um variavel que a gente cria
# Ele pode ser incrementado ou decrementado

# controla o while
contador = 0

#Sintaxe do while
while contador < 10:
    print(f"Volta ao mundo: {contador}")
    #Conta a volta ao mundo
    contador = contador + 1 #incremento

print(30*"#")
print("Repetição while com else")

contar = int(input("Informe um valor: "))

while contar <= 10:
    print("O valor de contar é: {}".format(contar))
    #contar = contar + 1
    #Forma simplificada
    contar += 1
else:
    print("Só sei contar ate 10")

print(30*"#")
print("Repetição simples com for")
for contar_for in range(0,10):
    print("Contagem do for: ", contar_for)

print("For com array")
caixa_frutas = ["Banana","Maçã","Uva"]
for fruta in caixa_frutas:
    print(f"A fruta é: {fruta}")
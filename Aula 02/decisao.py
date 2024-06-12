'''
Estruturas de decisão - Serve para que nossa APP tome um decisão
    Baseada em uma condição

    Classificações
        >Simples - Somente um única resposta
        >Composta - Duas respostas
        >Encadeada - Possui varias respostas
        >Aninhada - Uma resposata dentro da outra
'''

#Decisão simples
print("Decisão Simples")
idade = 18

if ( idade >= 18 ):
    print("Você é maior de idade")

#Decisao composta
print("Decisão Composta")

idade_dois = 15

if ( idade_dois >= 18 ):
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

#Decisao encadeada
print("Decisão encadeada")
fruta = "Laranja"

if fruta == "banana":
    print("Fica bom com Mel")
elif fruta == "Laranja":
    print("A melhor fruta")
elif fruta == "Maracuja":
    print("Fica em mousse")
else:
    print("Não tenho resposta")

#Decisão aninhada
print("Decisão aninhada")

idade_tres = 8
tem_ingresso = True

if ( idade_tres >= 18 ):
    # Condição para verificar se o usuario tem_ingresso
    if ( tem_ingresso == True ):
        print("Pode entrar na festa!")
    else:
        print("Não pode entrar na festa")
else:
    print("Você é menor de idade")

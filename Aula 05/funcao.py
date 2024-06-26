'''
O que é função?
    -> A s funções são blocos de código que realizam uma tarefa.
    -> Ajudam a organizar o código
    -> ajuda a não repetir codigos desnecessariamente
'''

#Sintaxe (Escrita) da função
def nome_funcao():
    '''
    #Corpo da função
    #comandos da função
    '''

#def - Palavra chave para definir a função
#nome_funcao - Nome que identifica a função

print("Função simples")
#Criando a função
def saudacao():
    print("Ola!. Boa noite. Ass: Bonner")

#Chamando nosssa função saudacao
saudacao()

print(20*"-") #Aparece 20 tracinhos na tela para separar uma função
print("Função com parametros")

#def saudacao_turma(nome, sobrenome, idade):

def saudacao_turma(nome):
    print(f"Boa noite {nome}")

#Chama a função
#saudacao_turma("João")

#Direto na função com input
#saudacao_turma(input("Seu nome: "))

#Utilizando variáveis para passar parametro para a função
#nome_aluno = input("Seu nome: ")
#saudacao_turma(nome_aluno)

print(20*"-") #Aparece 20 tracinhos na tela para separar uma função
print("Função com retorno")

def soma():
    return 2 + 2

#Chama a função
print(soma())

def multiplicar():
    multi = 2 * 3
    return multi
    #return 2 * 3

print(multiplicar())

def multiplicar_dois(valor_um,valor_dois):
    multi = valor_um * valor_dois
    return multi

numero_um = int(input("Informe o primeiro valor: "))
numero_dois = int(input("Informe o segundo valor: "))

resultado = multiplicar_dois(numero_um,numero_dois)

print(f"{numero_um} x {numero_dois} = {resultado}")
#A POO - Representa objetos de um mundo real através de um classe
#Toda classe pode ser consireda um molde

#Atibutos - São caracteristicas de um objeto(Nome, cpf,)
#Podemos dizer que na prática os atributos são variveis metidas

#Métodos são ações executadas por um objeto
#Podemos dizer que na pratica metodos são funções

class Pessoa:
    #No python os atributos precisão ser contruidos
    #Toda classe possui um metodo contrutor chamado __init__
    def __init__(self,nome,cpf,altura):
        self.nome = nome
        self.cpf = cpf
        self.altura = altura

    #Nossos metodos
    def falar(self):
        print("Estou falando!")

    def dizer_nome(self):
        print(f"Meu nome é: {self.nome}")
#Fim da classe


#Usando o molde (Instanciar da classe)
pessoa_um = Pessoa("João","6666655555",1.75)
pessoa_um.falar()
pessoa_um.dizer_nome()

#Segunda pessoa
pessoa_dois = Pessoa("Maria","99999999",1.60)
pessoa_dois.dizer_nome()
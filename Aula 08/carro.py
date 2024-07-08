class Carro:
    def __init__(self,modelo,ano,marca,cor):
        self.modelo = modelo
        self.ano = ano
        self.marca = marca
        self.cor = cor

    def exibir_carro(self):
        print(f"O modelo é: {self.modelo}\nAno: {self.ano}\nMarca: {self.marca}\nCor: {self.cor}")

#Fim da classe carro

#Usando a classe carro
carro_um = Carro("320 I", "2017","BMW", "Branca")

carro_um.exibir_carro()
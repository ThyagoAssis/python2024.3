class Conta_corrente:
    def __init__(self,agencia,conta,cliente):
        self.agencia = agencia
        self.conta = conta
        self.cliente = cliente
        #Atributo privado é aquele que não pode ser manipulado diretamente
        #No python o atributo privado é determinando pelo __ ex: __saldo
        self.__saldo = 0


    #Metodos sacar
    def sacar(self, saque):
        if self.__saldo <= 0:
            print("Saldo INSUFICIENTE!!!")
        else:
            self.__saldo = self.__saldo - saque
            return self.__saldo

    #Metodo de deposito
    def depositar(self, valor_deposito):
        if valor_deposito <= 0:
            print("Deposito não realizado")
        else:
            self.__saldo = self.__saldo + valor_deposito
            return self.__saldo

    #Metodo de consulta
    def consulta_saldo(self):
        return self.__saldo

cliente_um = Conta_corrente(255,98989,"José Maria")
cliente_um.depositar(1000)
cliente_um.sacar(0)

print(f"Agencia: {cliente_um.agencia},\nConta: {cliente_um.conta},\nCliente: {cliente_um.cliente}")
print(f"Saldo atual: {cliente_um.consulta_saldo()}")

print(20*"-")
print("")
cliente_dois = Conta_corrente(255,98978,"Rafaela")
cliente_dois.depositar(2500)
cliente_dois.sacar(555)

print(f"Agencia: {cliente_dois.agencia},\nConta: {cliente_dois.conta},\nCliente: {cliente_dois.cliente}")
print(f"Saldo atual: {cliente_dois.consulta_saldo()}")

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    def extrato(self):
        print("Saldo de R${} do Titular {}".format(self.__saldo, self.__titular))
        
    def deposita(self, valor):
        if valor > 0:
            self.__saldo += valor
            print("{} Você depositou R${}. Você tem R${} disponível em sua conta".format(self.__titular, valor, self.__saldo))
        else:
            print("Não foi possível depositar este valor")
            
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_para_saque = (self.__saldo + self.__limite)
        return valor_a_sacar <= valor_disponivel_para_saque
    
    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            print("{} Você sacou R${}! Seu saldo atual é de R${}".format(self.__titular, valor, self.__saldo))    
        else:
            print("{}, não foi possível sacar R${} da sua conta. Você tem R${} disponível para saque ".format(self.__titular, valor, self.__saldo)) 
    
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    
    @property
    def saldo(self):
        return(self.__saldo)
    
    @property
    def limite(self):
        return(self.__limite)
    
    @property
    def get_titular(self):
        return(self.__titular)

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
                
    @staticmethod        
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
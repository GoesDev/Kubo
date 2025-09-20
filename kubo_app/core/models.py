from .constants import TIPO_CONTA

class Conta():

    def __init__(self, nome, saldo, tipo):
        
        self.nome = nome
        self.saldo = saldo
        self.tipo = TIPO_CONTA[tipo]
    
    def conta(self):
        print(self.nome, self.saldo, self.tipo)
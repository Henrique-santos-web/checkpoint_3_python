import os
import time
tempo = 4

class Conta():
    def __init__(self):
        self._saldo = 0.0
        # self.conta = conta
    
    #* Depositar e Sacar
    def get_saldo(self):
        return self._saldo
    

    def sacar(self, valor):
        while True:
            try:
                if valor > self._saldo or valor <= 0.0:
                    print("Verificando Saldo...")
                    time.sleep(2)
                    os.system('cls' if 'nt' else 'clear')
                    print("⚠️ ERRO: Apenas Saques acima de 0,01 são autorizados!")
                    time.sleep(2)
                    os.system('cls' if 'nt' else 'clear')
                    continue
                else:
                    print("Verificando Saldo...")
                    time.sleep(2)
                    os.system('cls' if 'nt' else 'clear')
                    self._saldo -= valor
                    print(f"Tranferência no valor de: {valor} realizada com sucesso!")
                    time.sleep(2)
                    os.system('cls' if 'nt' else 'clear')
                    break
            except ValueError:
                print("Apenas números são permitidos!")
                time.sleep(2)
                os.system('cls' if 'nt' else 'clear')
                continue


    def depositar(self, valor):
        while True:
            try:
                if valor < 0.0:
                    print("⚠️ ERRO: Apenas depositos acima de 0,01")
                    time.sleep(2)
                    os.system('cls' if 'nt' else 'clear')
                    continue
                else:
                    print("Verificando Saldo...")
                    time.sleep(2)
                    os.system('cls' if 'nt' else 'clear')
                    self._saldo += valor
                    print(f"Tranferência no valor de: {valor} realizada com sucesso!")
                    break
            except ValueError:
                print("Apenas números são permitidos!")
                time.sleep(2)   
                os.system('cls' if 'nt' else 'clear')
                continue
from Conta import Conta

class ContaCorrente(Conta):
    def __init__(self):
        super().__init__()#* Esse super() é a mãe. esse __init__ é o método da mãe. O def __init__(self) vai pegar esse método da class mãe

    def sacar(self, valor):
        super().sacar(valor + 1) #* Na minha classe sacar, o saldo é subtraído pelo valor, e como tem uma taxa de R$ 1,00, adicionamos +1 ao valor. Taxa cobrada!
        #* importar levar em consideração que: O que mostra ao python qual método ele vai executar é o que vem após o super, que neste caso é o "sacar"


#? Mas por que criar um método novo? Porque estamos adicionando uma nova função a ela: A adição da taxa

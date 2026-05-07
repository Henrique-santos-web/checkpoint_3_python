from Conta import Conta

class ContaPoupanca(Conta):
    def __init__(self):
        super().__init__()

    def render_juros(self):
        print("Parece um absurdo, né? Mas a sua conta Poupança está rendendo 1,01 ao dia")
        self._saldo = self._saldo * 1.01
from Conta import Conta

class ContaPoupanca(Conta):
    def __init__(self):
        super().__init__()

    def render_juros(self):
        self._saldo = self._saldo * 1.01
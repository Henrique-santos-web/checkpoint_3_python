class Cliente():
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def validar_usuario(self, nome_digitado, cpf_digitado):
        if self.nome == nome_digitado and self.cpf == cpf_digitado:
            return True
        else:
            return False
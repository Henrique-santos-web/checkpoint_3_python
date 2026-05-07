from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca
from Cliente import Cliente
from Conta import Conta
import os, time
TEMPO = 3


def exibir_menu():

    print("\n" + "="*45)
    print("🏦BANCO CENTRAL🏦".center(45))
    print("="*45)
    print("[ 1 ] Ver Saldo")
    print("[ 2 ] Depositar")
    print("[ 3 ] Sacar")
    print("[ 0 ] Sair do Sistema")
    print("="*45)

def main():

    saldo_atual = Conta()
    conta_corrente = ContaCorrente()
    conta_poupanca = ContaPoupanca()

    print("\n 🏦BEM-VINDO AO BANCO🏦")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        match opcao:
            case "1":
                print(f"Saldo Atual: {saldo_atual.get_saldo()}")
                print(f"Saldo Conta Corrente: {conta_corrente.get_saldo()}")
                print(f"Saldo Conta Poupança: {conta_poupanca.get_saldo()}")
                time.sleep(TEMPO)
                os.system('cls' if os.name == 'nt' else 'clear')
                pass

            case "2":
                saldo_saque = input("Quanto você deseja sacar? ")


                time.sleep(TEMPO)
                os.system('cls' if os.name == 'nt' else 'clear')
                pass

            case "3":
                time.sleep(TEMPO)
                os.system('cls' if os.name == 'nt' else 'clear')
                pass

            case "0":
                time.sleep(TEMPO)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Encerrando sistema. Bye 👋")

            case _:
                print("\n⚠️ Erro: Opção inválida! Por favor, escolha um número de 0 a 3")
                time.sleep(TEMPO)
                os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
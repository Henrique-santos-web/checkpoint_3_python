from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca
# from Cliente import Cliente
from Conta import Conta
import os, time
TEMPO = 3
saldo_atual = Conta()
conta_corrente = ContaCorrente()
conta_poupanca = ContaPoupanca()
#cliente_login = Cliente()

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

    print("\nBEM-VINDO AO BANCO")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        match opcao:
            case "1":
                print(f"Saldo Conta Corrente: {conta_corrente.get_saldo()}")
                print(f"Saldo Conta Poupança: {conta_poupanca.get_saldo()}")
                time.sleep(TEMPO)
                os.system('cls' if os.name == 'nt' else 'clear')
                
            case "2":
                print("[ 1 ] Conta Corrente\n[ 2 ] Conta Poupança", "\n" + "-"*30)
                opcao_deposito = input("\nEscolha uma opção: ")
                if opcao_deposito == "1":
                    saldo_deposito = float(input("Quanto você deseja depositar? "))
                    conta_corrente.depositar(saldo_deposito)
                elif opcao_deposito == "2":
                    saldo_deposito = float(input("Quanto você deseja depositar? "))
                    conta_poupanca.depositar(saldo_deposito)
                time.sleep(TEMPO)
                os.system('cls' if os.name == 'nt' else 'clear')
                
            case "3":
                print("[ 1 ] Conta Corrente\n[ 2 ] Conta Poupança", "\n" + "-"*30)
                opcao_saque = input("\nEscolha uma opção: ")
                if opcao_saque == "1":
                    saldo_saque = float(input("Quanto você deseja sacar? "))
                    conta_corrente.sacar(saldo_saque)
                elif opcao_saque == "2":
                    saldo_saque = float(input("Quanto você deseja sacar? "))
                    conta_poupanca.sacar(saldo_saque)
                time.sleep(TEMPO)
                os.system('cls' if os.name == 'nt' else 'clear')
                
            case "0":
                print("Encerrando sistema. Bye 👋")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                break

            case _:
                print("\n⚠️ Erro: Opção inválida! Por favor, escolha um número de 0 a 3")
                time.sleep(TEMPO)
                os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
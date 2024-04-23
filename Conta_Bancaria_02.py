menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def func_depositar(saldo, extrato):
    valor_deposito = float(input("Insira o valor do depósito: "))
    if valor_deposito > 0: 
        saldo += valor_deposito 
        extrato += f"Depósito: R${valor_deposito:.2f}\n"
        print("Depósito efetuado com sucesso!")
        return saldo, extrato
    else:
        print("Depósito não efetuado, valor inválido!")

def func_sacar(*, saldo, extrato, limite, numero_saques):
    valor_saque = float(input("Insira o valor do saque: "))
    if valor_saque > 0 and valor_saque <= limite:
        if numero_saques == LIMITE_SAQUES:
            print("Limite de saques diários atingido!")
        elif valor_saque > saldo or saldo <= 0: 
            print("Saque não efetuado, saldo insuficiente.")
        else:
            saldo -= valor_saque 
            extrato += f"Saque: R${valor_saque}\n"
            numero_saques += 1 
            print("Saque efetuado com sucesso!")
            return saldo, extrato
    else:
        print("Valor de saque inválido!")

def func_extrato(saldo, /, *, extrato):
    print("\n############### EXTRATO ###############\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R${saldo:.2f}") 
    print("\n#######################################")

while True:
    opcao = input(menu)

    if opcao == "d":
        saldo, extrato = func_depositar(saldo, extrato)
    elif opcao == "s":
        saldo, extrato = func_sacar(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques)
    elif opcao == "e":
        func_extrato(saldo, extrato=extrato)
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

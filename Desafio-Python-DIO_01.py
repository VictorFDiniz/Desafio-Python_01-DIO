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

while True:
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Insira o valor do depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            print("Depósito efetuado com sucesso!")
        else:
            print("Depósito não efetuado, valor inválido!")

    elif opcao == "s":
        valor_saque = float(input("Insira o valor do saque: "))
        if valor_saque > 0 and valor_saque <= limite:
            if numero_saques == LIMITE_SAQUES:
                print("Limite de saques diários atingido!")
            elif valor_saque > saldo or saldo <= 0:
                print("Saque não efetuado, saldo insuficiente.")
            else:
                saldo -= valor_saque
                numero_saques += 1
                print("Saque efetuado com sucesso!")
        else:
            print("Valor de saque inválido!")

    elif opcao == "e":
        print("Extrato")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

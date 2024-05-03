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

    if opcao == "d":  # Opção para depósito
        valor_deposito = float(input("Insira o valor do depósito: ")) 
        if valor_deposito > 0:  # Verifica se o valor do depósito é positivo
            saldo += valor_deposito  # Adiciona o valor do depósito ao saldo
            extrato += f"Depósito: R${valor_deposito:.2f}\n"  # Adiciona a transação ao extrato
            print("Depósito efetuado com sucesso!")
        else:
            print("Depósito não efetuado, valor inválido!")
    elif opcao == "s":  # Opção para saque
        valor_saque = float(input("Insira o valor do saque: "))
        if valor_saque > 0 and valor_saque <= limite:  # Verifica se o valor do saque é válido
            if numero_saques == LIMITE_SAQUES:  # Verifica se o limite de saques diários foi atingido
                print("Limite de saques diários atingido!")
            elif valor_saque > saldo or saldo <= 0:  # Verifica se há saldo suficiente para o saque
                print("Saque não efetuado, saldo insuficiente.")
            else:
                saldo -= valor_saque  # Subtrai o valor do saque do saldo
                extrato += f"Saque: R${valor_saque}\n"  # Adiciona a transação ao extrato
                numero_saques += 1  # Incrementa o número de saques realizados
                print("Saque efetuado com sucesso!")
        else:
            print("Valor de saque inválido!")
    elif opcao == "e":  # Opção para extrato
        print("\n############### EXTRATO ###############\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)  # Exibe o extrato ou mensagem de ausência de movimentações
        print(f"\nSaldo atual: R${saldo:.2f}")  # Exibe o saldo atual
        print("\n#######################################")
    elif opcao == "q":  # Opção para sair do programa
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

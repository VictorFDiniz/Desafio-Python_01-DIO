
usuarios = []  # Lista para armazenar informações dos usuários
contas = []  # Lista para armazenar informações das contas
saldo = 0  # Variável para armazenar o saldo total
limite = 500  # Limite de saldo para saques
extrato = ""  # Variável para armazenar o extrato das transações
contas_cadastradas = ""  # Variável para armazenar o histórico das contas criadas
numero_saques = 0  # Variável para controlar o número de saques diários
LIMITE_SAQUES = 3


# Função para realizar um depósito na conta
def func_depositar(saldo, extrato):
    valor_deposito = float(input("Insira o valor do depósito: "))
    if valor_deposito > 0: 
        saldo += valor_deposito 
        extrato += f"Depósito: R${valor_deposito:.2f}\n"
        print("Depósito efetuado com sucesso!")
        return saldo, extrato
    else:
        print("Depósito não efetuado, valor inválido!")

# Função para realizar um saque na conta
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

# Função para exibir o extrato da conta
def func_extrato():
    print("\n############### EXTRATO ###############\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R${saldo:.2f}") 
    print("\n#######################################")

# Função para listar todas as contas criadas
def listar_contas():
    print("\n############### CONTAS ###############\n")
    print("Nenhuma conta foi encontrada." if not contas_cadastradas else contas_cadastradas)
    print("\n#######################################")

# Função para criar um novo usuário
def criar_usuario(lista_usuarios):
    nome = str(input("Digite seu nome: "))
    data_nascimento = str(input("Digite sua data de nascimento (DD-MM-AAAA): "))
    cpf = int(input("Digite seu número de CPF: "))
    for usuario in lista_usuarios:
        if usuario[2] == cpf:
            print("\nErro: CPF já cadastrado!")
            return
    endereco = str(input("Digite seu endereço no formato formato(rua, número - bairro - cidade/abreviação do estado): "))
    lista_usuarios.append([nome, data_nascimento, cpf, endereco])
    print("\nNovo usuário criado com sucesso!")

# Função para criar uma nova conta
def criar_conta(lista_contas, lista_usuarios):
    global contas_cadastradas
    cpf = int(input("Digite o CPF do usuário: "))
    for usuario in lista_usuarios:
        if usuario[2] == cpf:
            break
    else:
        print("\nErro: Usuario não encontrado!")
        return
    numero_da_conta = len(lista_contas) + 1
    lista_contas.append({"agência": "0001", "número da conta": numero_da_conta, "usuário": usuario[0]})
    contas_cadastradas += f"nome: {usuario[0]} - número da conta: {numero_da_conta} - agência: 0001\n"
    print("\nConta criada com sucesso!")

# Loop principal do programa

def main():

    menu = """

[u] Novo usuário
[c] Nova conta
[d] Depositar
[s] Sacar
[e] Extrato
[l] Listar contas
[q] Sair
=> """

    while True:
        opcao = input(menu)

        if opcao == "u":
            criar_usuario(usuarios)
        elif opcao == "c":
            criar_conta(contas, usuarios)
        elif opcao == "d":
            saldo, extrato = func_depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato = func_sacar(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques)
        elif opcao == "e":
            func_extrato(saldo, extrato=extrato)
        elif opcao == "l":
            listar_contas()
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
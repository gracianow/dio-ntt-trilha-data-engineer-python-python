import textwrap

def menu():
    menu = """\n
    [d]\tDepositar
    [s]\tSacar
    [e]\tExibir extrato
    [nc]\tCriar conta
    [nu]\tCriar usuário
    [fu]\tFiltrar usuários
    [lu]\tListar usuários
    [lc]\tListar contas
    [q]\tSair
    ==>"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"===Depósito de R$ {valor:.2f} realizado com sucesso!===")
    else:
        print("\n@@@ Falha ao realizar depósito! Valor inválido! @@@\n")
    return saldo, extrato  

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite_saque = valor > limite
    excedeu_saque = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Falha ao realizar saque! Saldo insuficiente! @@@\n")
    elif excedeu_limite_saque:
        print("\n@@@ Falha ao realizar saque! Limite de saque excedido! @@@\n")
    elif excedeu_saque:
        print("\n@@@ Falha ao realizar saque! Limite de saques diários excedido! @@@\n")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"===Saque de R$ {valor:.2f} realizado com sucesso!===")
    return saldo, extrato

def exibir_extrato(saldo, /, extrato):
    print(f"Saldo: R$ {saldo:.2f}")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF: ")
    usuario = filtrar_usuarios(cpf, usuarios)  

    if usuarios:
        print("=== Usuário cadastrado com sucesso ===")
        return {"agencia": agencia, "conta": numero_conta, "usuario": usuario}
    else
        print("@@@ Usuário não cadastrado @@@")
        return {}

def criar_usuario(usuarios):
    cpf = input("Digite o CPF: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("@@@ Usuário já cadastrado @@@")
        return
    nome = input("Digite o nome: ")
    data_nascimento = input("Digite a data de nascimento: ")
    endereco = input("Digite o endereço: ")
    telefone = input("Digite o telefone: ")

    usuarios.append({
        "cpf": cpf,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco,
        "telefone": telefone
    })

    print("=== Usuário cadastrado com sucesso ===")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = list(filter(lambda usuario: usuario["cpf"] == cpf, usuarios))
    return usuarios_filtrados

def listar_usuarios():
    print("Listar usuários")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
                Agência: {conta['agencia']}
                Conta: {conta['conta']}
                Titular: {conta['usuario']['nome']}
                Saldo: {conta['saldo']}
            """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():

    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    contas = []
    usuarios = []
    numero_saques = 0

    while True:
        opcao = menu()
        if opcao == "d":
            valor = float(input("Digite o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Digite o valor do saque: "))
            saldo, extrato = sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUE)
        elif opcao == "e":
            extrato(saldo, extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            conta = len(contas) + 1
            conta = criar_conta(AGENCIA, conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)     
        elif opcao == "q":
            break
        else:
            print("@@@ Opção inválida, tente novamente! @@@")


main()            

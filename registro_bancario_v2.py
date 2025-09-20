def menu():
    tela = """\n
    ------------------- MENU ------------------
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo Usuário
    [5]\tNova Conta
    [6]\tListar Contas
    [0]\tSair
    => """
    return input(tela)

def depositar(saldo, extrato, deposito, /):
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"
        print("Depósito realizado com sucesso.")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, saque, extrato, limite, numero_saques, LIMITE_SAQUES):
    if saque > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif saque > limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques diários excedido.")

    elif saque > 0:
        saldo -= saque
        extrato += f"Saque: R$ {saque:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso.")

    else:
        print("Operação falhou! O valor informado é invalido.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n======================= EXTRATO =====================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=======================================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado, opção de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)


def main():
    agencia = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []


    while True:
        tela = menu()


        if tela == "1":
            deposito = float(input("Informe o valor do deposito: "))

            saldo, extrato = depositar(saldo, extrato, deposito)


        elif tela == "2":
            saque = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                saque=saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,
            )


        elif tela == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif tela == "4":
            criar_usuario(usuarios)

        elif tela == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)
            
        elif tela == "6":
            listar_contas(contas)

        elif tela == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
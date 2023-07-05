"""
    OBJETIVO GERAL:
    
    - Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária
    
    
    SAQUE:
    
     A função saque deve receber os argumentos por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, número_saques, limite_saques.
     Sugestão de retorno: saldo e extrato
     
    DEPOSITO:
    
     A função depósito deve receber argumentos apenas por posição (position only). Sugestão de argumentos: saldo, valor, extrato
     Sugestão de retorno: salo e extrato
     
    EXTRATO:
    
     A função extrato deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato
     
    CRIAR USUÁRIO:
    
     O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato
     logradouro, numero - bairro - cidade/sigla estado. Deve ser armazenado somentes os números do CPF. não podemos cadastrar 2 usuários com os mesmo CPF.
     
     Para vincular um usuário a uma conta filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista
     
    CRIAR CONTA CORRENTE:
     
     O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1.
     O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence somente um usuário 
     
     

"""

proxima_conta = 1
usuarios = []
contas = []


def criar_usuario(nome, data_nascimento, cpf, endereco):
    
    # Verificar se o CPF já existe na lista de usuários
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Usuário já cadastrado.")
            return
    
    # Se o CPF não existir, adicionar um novo usuário a lista de usuários
    
    usuarios.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    })
    
    print('Usuário cadastrado com sucesso.')


def criar_contaCorrente(agencia, numero_conta, cpf):
    
    # Verificar se o CPF pertence a um usuário existente
    usuario_encontrado = None
    
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuario_encontrado = usuario
            break
    
    if usuario_encontrado is None:
        print('Usuário não encontrado. Não foi possível cadastrar a conta.')
        return

    
    # Se o CPF existir, criar uma nova conta bancaria
    
    nova_conta = {
        'agencia': agencia,
        'numero_conta': numero_conta,
        'usuario': usuario_encontrado
    }
    
    # Incrementar a variável 'proxima_conta' para obter o próximo número de conta disponível
    global proxima_conta
    proxima_conta += 1
    
    # Vincular a nova conta ao usuário correspondente
    contas.append(nova_conta)
    
    print('Conta cadastrada com sucesso.')

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    # Verificar se o valor do saque é válido
    if valor > saldo:
        print('Saldo insuficiente. Saque não pode ser realizado.')
        return saldo, extrato
    
    # Verificar se o número de saques ainda está dentro do limite
    if numero_saques >= limite_saques:
        print('Limite diário de saques atingido.')
        return saldo, extrato
    
    # Atualizar saldo, extrato e contador de saques diários
    saldo -= valor
    extrato += f"Saque: R$ {valor:.2f}\n"
    numero_saques += 1
    
    # Retornar saldo e extrato atualizados
    return saldo, extrato


def deposito(saldo, valor, extrato):
    
    # Verificar se o valor do depósito é valido
    if valor <= 0:
        print('Valor inválido para depósito.')
        return saldo, extrato
    
    # Atualiazr saldo e extrato
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    
    # Retornar saldo e extrato atualiados
    return saldo, extrato

def exibir_extrato(saldo, *, extrato):
    
    # Imprimir o extrato das transações e o saldo atual
    print("================ EXTRATO ================")
    if extrato:
        print(extrato)
    else:
        print("Não foram realizadas movimentações.")
    print(f"Saldo: R$ {saldo:.2f}")
    print("=========================================")
    
    
    
def exibir_contas():
    print("================= LISTA DE CONTAS =================")
    for conta in contas:
        print(f"Agência: {conta['agencia']}")
        print(f"Número da Conta: {conta['numero_conta']}")
        print(f"Usuário: {conta['usuario']['nome']}")
        print("-------------------------------------------")
    print("==================================================")


def exibir_usuarios():
    print("================= LISTA DE USUÁRIOS =================")
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}")
        print(f"Data de Nascimento: {usuario['data_nascimento']}")
        print(f"CPF: {usuario['cpf']}")
        print(f"Endereço: {usuario['endereco']}")
        print("-------------------------------------------")
    print("===================================================")
    
    

# Testes

# Cadastrar um usuário
criar_usuario("João Silva", "01/01/1990", "12345678900", "Rua A, 123 - Centro - Cidade/UF")

# Cadastrar uma conta para o usuário
criar_contaCorrente("0001", proxima_conta, "12345678900")


# Realizar saques
saldo = 1000.0
extrato_transacoes = ""
limite_diario = 1000.0
numero_saques = 0
limite_saques = 3

saldo, extrato_transacoes = saque(saldo=saldo, valor=200.0, extrato=extrato_transacoes, limite=limite_diario, numero_saques=numero_saques, limite_saques=limite_saques)
saldo, extrato_transacoes = saque(saldo=saldo, valor=500.0, extrato=extrato_transacoes, limite=limite_diario, numero_saques=numero_saques, limite_saques=limite_saques)
saldo, extrato_transacoes = saque(saldo=saldo, valor=300.0, extrato=extrato_transacoes, limite=limite_diario, numero_saques=numero_saques, limite_saques=limite_saques)

# Realizar depósitos
saldo, extrato_transacoes = deposito(saldo=saldo, valor=1500.0, extrato=extrato_transacoes)
saldo, extrato_transacoes = deposito(saldo=saldo, valor=800.0, extrato=extrato_transacoes)

# Visualizar o extrato
exibir_extrato(saldo=saldo, extrato=extrato_transacoes)

# Exibir contas
exibir_contas()

# Exibir usuarios
exibir_usuarios()
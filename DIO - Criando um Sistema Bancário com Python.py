menu = ('Que operação você quer realizar? '
                 '\n 1 - DEPOSITO \t 2 - SAQUE \t 3 - EXTRATO \t 4 - SAIR'
                 '\n= ')

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    operacao = input(menu)

    if operacao == '1':
        valor = float(input('Informe o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print('Operação falhou! Valor informado inválido')

    elif operacao == '2':
        valor = float(input('Qual valor para saque?:'))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou! Você não tem saldo suficiente')
        elif excedeu_limite:
            print('Operação falhou! O valor do saque excede o limite')
        elif excedeu_saques:
            print('Operação falhou! Número máximo de saques excedido')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques -= 1
        else:
            print('Operação falhou! O valor informado é inválido!')

    elif operacao == '3':
        print('\n ============== EXTRATO ==============')
        print('Não foram realizadas movimentações' if not extrato else extrato)
        print(f'\n Saldo: R$ {saldo:.2f}')
        print('============================')

    elif operacao == '4':
        break
    else:
        print('Operação Inválida, por favor selecione novamente a operçaão defejada')


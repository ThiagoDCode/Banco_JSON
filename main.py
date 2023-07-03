from random import choice
from complementos import menu, erro_cor


class Banco:
    def __init__(self, cliente, cpf, conta, saldo):
        self.__cliente = cliente
        self.__cpf = cpf
        self.__conta = conta
        self.__saldo = saldo

    def info_cliente(self):
        print(f'\n|> INFORMAÇÕES DA CONTA <|\n'
              f'CLIENTE: {self.__cliente}   CPF: {self.__cpf}   CONTA: {self.__conta}\n'
              f'SALDO: R${self.__saldo:.2f}')

    def depositar(self, valor_deposito):
        if valor_deposito > 0:
            self.__saldo += valor_deposito
            print(f'\nDEPÓSITO EFETUADO COM SUCESSO! R$+{valor_deposito:.2f}\n'
                  f'SALDO: R${self.__saldo:.2f}')
        else:
            print(erro_cor('ERRO! Valores negativos não é válido para depósito'))

    def sacar(self, valor_saque):
        if valor_saque <= self.__saldo:
            self.__saldo -= valor_saque
            print(f'\nSAQUE EFETUADO COM SUCESSO! R$-{valor_saque:.2f}\n'
                  f'SALDO: R${self.__saldo:.2f}')
        else:
            print(erro_cor('ERRO! Saldo insuficiente'))


contas_clientes = {}
while True:
    options = menu('Criar Conta', 'Acessar Conta', 'Encerrar Sessão')

    if options == 3:
        print('\nObrigado por escolher o Dalla$ Bank')
        break

    elif options == 1:
        nome_cliente = input('Nome do Cliente: ').strip().title()
        cpf_cliente = input('CPF do Cliente (ex: 000.000.000-00): ')
        deposito_inicial = float(input('Valor de Depósito: R$'))
        num_conta = str(choice(range(1000, 9999)))

        contas_clientes[num_conta] = Banco(nome_cliente, cpf_cliente, num_conta, deposito_inicial)
        print(f'\n|> CONTA CRIADA COM SUCESSO! <|\n'
              f'CLIENTE: {nome_cliente}    CPF: {cpf_cliente}   CONTA: {num_conta}\n'
              f'DEPÓSITO: R${deposito_inicial:.2f}')

    elif options == 2:
        buscar = input('Número da Conta: ')

        try:
            contas_clientes[buscar].info_cliente()
        except KeyError:
            print(erro_cor('ERRO! Desculpe, conta não encontrada'))

        else:
            while True:
                saque_deposito = menu('Sacar', 'Depositar', 'Voltar')

                if saque_deposito == 3:
                    break
                elif saque_deposito == 1:
                    contas_clientes[buscar].sacar(
                        float(input('Valor a Sacar: R$'))
                    )
                elif saque_deposito == 2:
                    contas_clientes[buscar].depositar(
                        float(input('Valor a Depositar: R$'))
                    )

from extras import *
from random import choice
import os


class Banco:
    def __init__(self, cliente, cpf, senha, conta, saldo):
        self.cliente = cliente
        self.cpf = cpf
        self.senha = senha
        self.conta = conta
        self.saldo = saldo

    def info_cliente(self):
        os.system('cls')

        name_exclusions = ['DA', 'DAS', 'DE', 'DO', 'DOS']
        if self.cliente[1] not in name_exclusions:
            name = f'{self.cliente[0]} {self.cliente[1]}'
        else:
            name = self.cliente[0]

        # PRINT ------------------------------------------------------------------------
        print(f'<< INFORMAÇÕES DA CONTA >>'.center(32, '='))
        print(f'Olá, {cor(1, name.title())}'
              f'\nCPF: {cor(1, self.cpf)}  Conta: {cor(1, self.conta)}'
              f'\nSaldo: {cor(1, f"{self.saldo:.2f}")}\n')
        # ------------------------------------------------------------------------ PRINT

    def depositar(self):
        try:
            valor_deposito = float(input('Valor do depósito: R$'))
            if valor_deposito > 0:
                self.saldo += valor_deposito
                print(f'\nDEPÓSITO EFETUADO COM SUCESSO!\n'
                      f'SALDO: R${self.saldo:.2f}\n')
            else:
                print(error('ERRO! Valores negativos não é válido para depósito\n'))
        except ValueError:
            print(error('ERRO! Valor de depósito inválido\n'))

    def sacar(self):
        try:
            valor_saque = float(input('Valor do saque: R$'))
            if valor_saque <= self.saldo:
                self.saldo -= valor_saque if valor_saque > 0 else (-valor_saque)  # TODO: vê melhor forma de converter
                print(f'\nSAQUE EFETUADO COM SUCESSO!\n'
                      f'SALDO: R${self.saldo:.2f}\n')
            else:
                print(error('ERRO! Saldo insuficiente\n'))
        except ValueError:
            print(error('ERRO! Valor de saque inválido\n'))

    def check_pass(self, senha):
        try:
            if int(senha) == self.senha:
                return True
            raise Exception()
        except ValueError:
            print(error('ERRO! A senha é formada por 4 dígitos, tente novamente...\n'))
        os.system('pause')


def create_acc(dict_objs):
    while True:
        acc = str(choice(range(1000, 10000)))

        if not dict_objs.get(acc):
            return acc

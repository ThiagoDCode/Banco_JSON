from lib_def import *
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

        nome = f'{self.cliente[0]} {self.cliente[1]}' if 'DE' != self.cliente[1] != 'DA' else self.cliente[0]

        print(f'<< INFORMAÇÕES DA CONTA >>'.center(32, '='))
        print(f'Olá, {cor(1, nome.title())}'
              f'\nCPF: {cor(1, self.cpf)}  Conta: {cor(1, self.conta)}'
              f'\nSaldo: {cor(1, f"{self.saldo:.2f}")}\n')

    def depositar(self):
        try:
            valor_deposito = float(input('Valor do depósito: R$'))
            if valor_deposito > 0:
                self.saldo += valor_deposito
                print(f'\nDEPÓSITO EFETUADO COM SUCESSO!\n'
                      f'SALDO: R${self.saldo:.2f}\n')
            else:
                print(erro_cor('ERRO! Valores negativos não é válido para depósito\n'))
        except ValueError:
            print(erro_cor('ERRO! Valor de depósito inválido\n'))

    def sacar(self):
        try:
            valor_saque = float(input('Valor do saque: R$'))
            if valor_saque <= self.saldo:
                self.saldo -= valor_saque if valor_saque > 0 else (-valor_saque)  # TODO: vê melhor forma de converter
                print(f'\nSAQUE EFETUADO COM SUCESSO!\n'
                      f'SALDO: R${self.saldo:.2f}\n')
            else:
                print(erro_cor('ERRO! Saldo insuficiente\n'))
        except ValueError:
            print(erro_cor('ERRO! Valor de saque inválido\n'))

    def check_pass(self):
        try:
            senha_entrada = int(input('Digite a senha: '))
            if senha_entrada == self.senha:
                return True
            else:
                print(erro_cor('Senha incorreta\n'))
        except ValueError:
            print(erro_cor('Senha incorreta\n'))
        os.system('pause')

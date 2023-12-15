from extras import *
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

        # PRINT ------------------------------------------------------------------------
        print(f'<< INFORMAÇÕES DA CONTA >>'.center(32, '='))
        print(f'{cor(1, self.cliente)}'
              f'\nCPF: {cor(1, self.cpf)}  Conta: {cor(1, self.conta)}'
              f'\nSaldo: {cor(1, f"R${self.saldo:.2f}")}\n')
        # ------------------------------------------------------------------------ PRINT

    def depositar(self):
        try:
            valor_deposito = float(input('Valor do depósito: R$'))
            if valor_deposito > 0:
                self.saldo += valor_deposito
                print(f'\nDEPÓSITO EFETUADO COM SUCESSO!\n'
                      f'SALDO: R${self.saldo:.2f}\n')
           
            else:
                print(erro('ERRO! Valores negativos não é válido para depósito\n'))
        except ValueError:
            print(erro('ERRO! Valor de depósito inválido\n'))

    def sacar(self):
        try:
            valor_saque = float(input('Valor do saque: R$'))
            if valor_saque <= self.saldo:
                self.saldo -= valor_saque if valor_saque > 0 else (-valor_saque)  # TODO: vê melhor forma de converter
                print(f'\nSAQUE EFETUADO COM SUCESSO!\n'
                      f'SALDO: R${self.saldo:.2f}\n')
            
            else:
                print(erro('ERRO! Saldo insuficiente\n'))
        except ValueError:
            print(erro('ERRO! Valor de saque inválido\n'))

    def check_pass(self, senha):
        try:
            if int(senha) == self.senha:
                return True
            raise Exception()
        
        except ValueError:
            print(erro('ERRO! A senha é formada por 4 dígitos, tente novamente...\n'))
        os.system('pause')

    def transferir(self, conta_destino):
        try:
            valor_trans = float(input('Valor da Transferência: R$'))
            if valor_trans <= self.saldo:
                self.saldo -= valor_trans
                conta_destino.saldo += valor_trans
                print(f"\nTransferência de {cor(1, f'R${valor_trans}')} para "
                      f"{cor(1, conta_destino.cliente)} realizada com sucesso! \n")
            
            else:
                print(erro('Saldo insuficiente!\n'))
        except ValueError:
            print(erro('ERRO! Valor para transferência inválido\n'))

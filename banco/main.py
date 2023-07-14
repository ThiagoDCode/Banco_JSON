from random import choice
from dados_json import *
from lib_def import *
import os
from time import sleep


# Armazena todos os objetos da classe Banco
contas_clientes = {}

while True:
    os.system('cls')
    match menu('ABRIR CONTA', 'ACESSAR CONTA', 'ENCERRAR SESSÃO'):

        case 3:
            print('\nObrigado por escolher o Dalla$$ Bank')
            break

        case 1:
            os.system('cls')

            # TODO: Criar uma interrupção "Esc" caso usuário queira não mas prosseguir com o cadastro
            nome_cliente = name_check('Nome do Cliente: ')
            cpf_cliente = verify_cpf('CPF do Cliente: ')
            senha_cliente = verify_pass('Senha de 4 dígitos: ')
            num_conta = str(choice(range(1000, 9999)))
            deposito_inicial = verify_num('Valor de Depósito: R$')

            conta = Banco(nome_cliente, cpf_cliente, senha_cliente, num_conta, deposito_inicial)
            # Converte o Objeto em uma Lista de Dicionários e salva no JSON
            save_dados('arquivos_banco.json', conta)
            contas_clientes[num_conta] = conta

        case 2:
            os.system('cls')
            # Faz o carregamento dos arquivos
            if not acc_account('arquivos_banco.json', contas_clientes):
                continue

            buscar = input('Número da Conta: ')
            if buscar == '':
                continue
            try:
                if contas_clientes[buscar].check_pass():
                    while True:
                        contas_clientes[buscar].info_cliente()
                        match menu('SACAR', 'DEPOSITAR', 'SAIR DA CONTA'):
                            case 3:
                                os.system('cls')
                                save_changes('arquivos_banco.json', contas_clientes)
                                print('\n>>> SAINDO DA CONTA...')
                                sleep(3)
                                break
                            case 1:
                                os.system('cls')
                                contas_clientes[buscar].sacar()
                            case 2:
                                os.system('cls')
                                contas_clientes[buscar].depositar()
                        os.system('pause')
            except KeyError:
                print(erro_cor('ERRO! Desculpe, conta não encontrada\n'))
                os.system('pause')

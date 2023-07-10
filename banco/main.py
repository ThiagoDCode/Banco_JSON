from random import choice
from dados_json import *
import os
from time import sleep


# ARMAZENARÁ TODOS OS OBJETOS DA CLASSE BANCO
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
            nome_cliente = verify_name('Nome do Cliente: ')
            cpf_cliente = verify_cpf('CPF do Cliente: ')
            senha_cliente = verify_pass('Senha de 4 dígitos: ')
            num_conta = str(choice(range(1000, 9999)))
            deposito_inicial = verify_num('Valor de Depósito: R$')

            conta = Banco(nome_cliente, cpf_cliente, senha_cliente, num_conta, deposito_inicial)
            # CONVERTE O OBJETO EM UMA LISTA DE DICIONÁRIOS E SALVA NO JSON
            save_dados('arquivos_banco.json', conta)

            contas_clientes[num_conta] = conta

            # TODO: Colocar esse print no 'save_dados()', junto com uma verificação de arquivo salvo
            print(f'\n|> CONTA CRIADA COM SUCESSO!\n'
                  f'CLIENTE: {nome_cliente}    CPF: {cpf_cliente}   CONTA: {num_conta}\n'
                  f'DEPÓSITO: R${deposito_inicial:.2f}\n')
            os.system('pause')

        case 2:
            os.system('cls')
            # VAI FAZER O CARREGAMENTO DOS ARQUIVOS
            acc_account('arquivos_banco.json', contas_clientes)

            buscar = input('Número da Conta: ')
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

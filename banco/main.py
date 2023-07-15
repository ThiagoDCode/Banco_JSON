from dados_json import *
from extras import *
import check_lib as ck
import os
from time import sleep


# Armazena todos os objetos da classe Banco
contas_clientes = {}

# Recupera e re-instância os Objetos (se existir), assim que o programa é rodado
if os.path.exists('arquivos_banco.json'):
    acc_account('arquivos_banco.json', contas_clientes)


while True:
    os.system('cls')
    match menu('ABRIR CONTA', 'ACESSAR CONTA', 'ENCERRAR SESSÃO'):

        case 3:
            print('\nObrigado por escolher o Dalla$$ Bank')
            break

        case 1:
            os.system('cls')

            nome_cliente = ck.name_check('Nome do Cliente: ')
            if not nome_cliente:
                continue
            cpf_cliente = ck.verify_cpf('CPF do Cliente: ')
            senha_cliente = ck.verify_pass('Senha de 4 dígitos: ')
            num_conta = create_acc(contas_clientes)
            deposito_inicial = ck.verify_num('Valor de Depósito: R$')

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
                print(error('ERRO! Desculpe, conta não encontrada\n'))
                os.system('pause')

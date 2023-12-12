from dados_json import *
from extras import *
import check_lib as ck
import os
from time import sleep


# Recupera e re-instância os Objetos (se existir), assim que o programa é rodado
if os.path.exists('arquivos_banco.json'):
    acc_account('arquivos_banco.json', contas_clientes)


while True:
    os.system('cls')
    match menu('ABRIR CONTA', 'ACESSAR CONTA', 'ENCERRAR SESSÃO'):

        case 3:  # ENCERRAR SESSÃO
            print('\nObrigado por escolher o DALLA$$ BANK\n')
            break

        case 1:  # ABRIR CONTA
            os.system('cls')
            
            try:
                nome_cliente = ck.name_validation()
                cpf_cliente = ck.cpf_validation(contas_clientes)
                senha_cliente = ck.password_check('Senha de 4 dígitos: ')
                deposito_inicial = ck.number_check('Valor de Depósito: R$')
            except Exception:
                print(cor(3,'\nCancelado!!\n'))
                sleep(1.5)
            else:
                create_acc(nome_cliente, cpf_cliente, senha_cliente, deposito_inicial)

        case 2:  # ACESSAR CONTA
            os.system('cls')
            
            buscar_conta = input('Número da Conta: ')
            if buscar_conta == '':
                continue
            buscar_senha = input('Digite a Senha: ')

            try:
                if contas_clientes[buscar_conta].check_pass(buscar_senha):
                    while True:
                        contas_clientes[buscar_conta].info_cliente()
                        match menu('SACAR', 'DEPOSITAR', 'TRANSFERIR', 'SAIR DA CONTA'):

                            case 4:  # SAIR DA CONTA
                                os.system('cls')
                                save_changes('arquivos_banco.json', contas_clientes)
                                print('\n>>> SAINDO DA CONTA...')
                                sleep(1.5)
                                break

                            case 1:  # SACAR VALOR
                                os.system('cls')
                                contas_clientes[buscar_conta].sacar()

                            case 2:  # DEPOSITAR VALOR
                                os.system('cls')
                                contas_clientes[buscar_conta].depositar()

                            case 3:  # TRANSFERIR VALOR
                                os.system('cls')
                                conta_destino = input('Número da Conta Destinatária: ')
                                if contas_clientes.get(conta_destino):
                                    contas_clientes[buscar_conta].transferir(contas_clientes[conta_destino])
                                else:
                                    print(erro('ERRO! Conta destinatária não encontrada\n'))

                        os.system('pause')
            
            except (KeyError, Exception):
                print(erro('ERRO! Conta ou Senha inválida\n'))
                if input('Esqueceu? Deseja recuperar Conta/Senha ("S")? ').strip().upper() == 'S':
                    try:
                        if recover('arquivos_banco.json', contas_clientes):
                            print(cor(2, '\nDADOS ATUALIZADOS COM SUCESSO!\n'))
                            sleep(1.5)
                    except Exception:
                        print(cor(3, "\nCancelado!!"))
                        sleep(1.5)

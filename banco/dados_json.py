import check_lib as ck
import banco
from extras import *
from time import sleep
import json
import os


# Armazena todos os Objetos da Classe 'Banco'
contas_clientes = {}


def create_acc(nome, cpf, senha, deposito):
    conta_validated = banco.validate_acc(contas_clientes)

    conta_cliente = banco.Banco(nome, cpf, senha, conta_validated, deposito)
    # Converte o Objeto em uma Lista de Dicionários e salva no JSON
    save_dados('arquivos_banco.json', conta_cliente)
    contas_clientes[conta_validated] = conta_cliente


def save_dados(arquivo, dados):
    """ Converte o Objeto e uma lista de dicionários e os salva em arquivo JSON

    :param arquivo: Nome do arquivo de dados
    :param dados: Objeto que será convertido e salvo
    """
    try:
        if not os.path.exists(arquivo):
            # O primeiro dado será salvo como uma lista de dicionários (por isso: [.__dict__])
            dados_iniciais = [dados.__dict__]
            with open(arquivo, 'w', encoding='UTF-8') as save:
                save.write(json.dumps(dados_iniciais, ensure_ascii=False, indent=4))
        else:
            with open(arquivo, 'r', encoding='UTF-8') as file:
                nova_entrada = json.load(file)
                file.close()

            # Os dados posteriores serão adicionados como dicionários, na lista criada inicialmente
            nova_entrada.append(dados.__dict__)
            with open(arquivo, 'w', encoding='UTF-8') as save:
                save.write(json.dumps(nova_entrada, ensure_ascii=False, indent=4))
    except FileNotFoundError:
        print(erro('\nERRO! Ocorreu um problema no acesso ao banco de dados'))
        os.system('pause')
    else:
        print('\n=====<< CONTA CRIADA COM SUCESSO! >>=====')
        sleep(1.5)


def acc_account(arquivo, dict_objects):
    """ Re-instância os dados JSON na class Banco

    :param arquivo: Arquivo JSON
    :param dict_objects: Dicionário onde será armazenado os objetos re-instanciados
    :return: Retorna o Dict
    """
    try:
        with open(arquivo, 'r', encoding='UTF-8') as file:
            re_instance = json.load(file)
            file.close()

        for obj in re_instance:
            dict_objects[obj['conta']] = banco.Banco(
                obj['cliente'], obj['cpf'], obj['senha'], obj['conta'], obj['saldo']
            )
    except FileNotFoundError:
        print(erro('ERRO! Arquivo de dados não encontrado\n'))
        os.system('pause')
        return False
    else:
        return dict_objects


def save_changes(arquivo, dict_objetos):
    """ Salva modificações feitas no Objeto no arquivo JSON

    Args:
        dict_objetos (dict): Dicionário dos objetos modificados
        arquivo (.json): Arquivo JSON
    """
    update = []
    for cliente in dict_objetos.keys():
        update.append(dict_objetos[cliente].__dict__)

    with open(arquivo, 'w', encoding='UTF-8') as save:
        save.write(json.dumps(update, ensure_ascii=False, indent=4))


def recover(arquivo, dict_objects):
    os.system('cls')

    while True:
        cpf_busca = ck.cpf_validation(dict_objects, recover=True)

        for conta in dict_objects.values():
            if conta.cpf == cpf_busca:
                os.system('cls')
                # PRINT --------------------------------------------------------------
                print('=' * 35)
                print(cor(1, conta.cliente))
                print(f'CPF: {cor(1, conta.cpf)}   Conta: {cor(1, conta.conta)} \n'
                      f'{"=" * 35}')
                # -------------------------------------------------------------- PRINT

                new_pass = ck.password_check('Digite a nova senha: ')
                conta.senha = new_pass
                save_changes(arquivo, dict_objects)
                return True

        print(erro('ERRO! CPF não encontrado\n'))
        os.system('pause')
        break

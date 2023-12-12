import check_lib as ck
import banco
from extras import *
from time import sleep
import json
import os
from random import choice


# Armazena todos os Objetos da classe 'Banco' em uma lista/dicionário temporário
contas_clientes = {}


def create_account(dict_objects, nome, cpf, senha, deposito):
    """ Cria e válida a conta do cliente, armazenando em um dicionário temporário.

    Args:
        dict_objects (dict): Dicionário de Objetos (arquivo de dados de clientes)
        nome (str): Nome do Cliente
        cpf (str): CPF do cliente
        senha (int): Senha do Cliente
        deposito (float): Deposito do Cliente
    """
    
    # Define um número único de 4 dígitos para a conta do cliente
    while True:
        num_conta = str(choice(range(1000, 10000)))

        if not dict_objects.get(num_conta):       # Verifica se a conta já existe
            dados_cliente = banco.Banco(nome, cpf, senha, num_conta, deposito)
            break

    contas_clientes[num_conta] = dados_cliente    # Salva os dados na lista de clientes
    
    if save_dados(dados_cliente):                 # Salva os dados no arquivo JSON
        os.system("cls")
        # PRINT --------------------------------------------------------------
        print("=====<< CONTA CRIADA COM SUCESSO! >>=====")
        print(cor(1, nome))
        print(f'CPF: {cor(1, cpf)}       Conta: [ {cor(3, num_conta)} ] \n'
            f'Saldo: {cor(1, f"R${deposito:.2f}")} \n'
            f'{"=" * 41}\n')
        # -------------------------------------------------------------- PRINT
        os.system("pause")


def save_dados(nova_conta):
    """ Salva os dados em um arquivo JSON no formato de Lista de Dicionários.

    Args:
        nova_conta (_object): Objeto da Classe Banco (dados do novo cliente)
    """
    
    try:
        # O primeiro arquivo é convertido e salvo como uma lista de dicionários (por isso o: [.__dict__])
        if not os.path.exists("arquivos_banco.json"):
            dados = [nova_conta.__dict__]
        
        # Se o arquivo já existe, os dados são recuperados e é adicionado os novos dados
        else:
            with open("arquivos_banco.json", "r", encoding="UTF-8") as file:
                dados = json.load(file)
                dados.append(nova_conta.__dict__)
                file.close()

        # Salva os dados atualizados no arquivo JSON
        with open("arquivos_banco.json", "w", encoding="UTF-8") as save:
            save.write(json.dumps(dados, ensure_ascii=False, indent=4))

    except FileNotFoundError:
        print(erro("\nERRO! Ocorreu um problema no acesso ao Bando de Dados..."))
        os.system("pause")

    else:
        return True


def reInstance_dados(arquivo, dict_objects):
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
    """ Recupera os dados de um usuário, e redefinindo sua senha.

    Args:
        arquivo (json): Arquivo JSON com os dados
        dict_objects (dict): Dicionário com a lista de clientes

    Returns:
        bool: Retorna True caso a recuperação tenha tido sucesso
    """
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

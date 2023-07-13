from banco import *
from time import sleep
import json
import os


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
    except :
        print(erro_cor('\nERRO! Ocorreu um problema no acesso ao banco de dados'))
        os.system('pause')
    else:
        print('\n=====<< CONTA CRIADA COM SUCESSO! >>=====')
        sleep(1.5)


def acc_account(arquivo, dict_objetos):
    """ Re-instância os dados JSON na class Banco

    :param arquivo: Arquivo JSON
    :param dict_objetos: Dicionário onde será armazenado os objetos re-instanciados
    :return: Retorna o Dict
    """
    try:
        with open(arquivo, 'r', encoding='UTF-8') as file:
            re_instance = json.load(file)
            file.close()

        for obj in re_instance:
            dict_objetos[obj['conta']] = Banco(
                obj['cliente'], obj['cpf'], obj['senha'], obj['conta'], obj['saldo']
            )
    except FileNotFoundError:
        print(erro_cor('ERRO! Arquivo de dados não encontrado\n'))
        os.system('pause')
        return False
    else:
        return dict_objetos


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

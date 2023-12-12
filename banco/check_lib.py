from extras import *


def name_validation():
    while True:
        name_entry = input("Nome Completo: ").strip()
        
        if name_entry == '':
            raise Exception()  # ENTER com campo de nome vazio > cancela a criação de conta
        elif not name_entry.replace(' ', '').isalpha():
            print(erro('ERRO! Nome inválido, tente novamente...\n'))
        else:
            return name_entry.upper()


def cpf_validation(dict_objects: dict, recover=False) -> str:
    """ Verifica se o CPF contém 11 números e o convertendo para o padrão de CPF Brasileiro (ex: 000.000.000-00). E faz a busca nos 
    arquivos de dados de clientes para garantir que não haja CPFs duplicados.

    :param dict_objects: Dicionário de Objetos (arquivo com os dados dos clientes)
    :param recover: True, ignora a verificação de CPF duplicado.
    :return: Retorna o número CPF (verificado e formatado)
    """
    
    while True:
        cpf_entry = input("CPF: ").replace('.', '').replace('-', '').replace(' ', '')
        if cpf_entry == '':
            raise Exception()  # ENTER com campo de CPF vazio -> cancela a criação de conta

        if len(cpf_entry) != 11 or not cpf_entry.isdigit():
            print(erro('CPF INVÁLIDO! Número CPF requer 11 números (ex: 000.000.000-00)\n'))
            continue
        
        cpf = f'{cpf_entry[:3]}.{cpf_entry[3:6]}.{cpf_entry[6:9]}-{cpf_entry[9:]}'    # Formatação para padrão (000.000.000-00)
        
        if not recover and busca_cpf(dict_objects, cpf):
            print(erro('ERRO! CPF já cadastrado\n'))
        else:
            return cpf


def busca_cpf(dict_objects: dict, cpf_busca: str) -> bool:
    """ Verifica se o CPF informado já existe nos arquivos de dados.

    :param dict_objects: Dicionário de Objetos (arquivo com dados dos clientes)
    :param cpf_busca: CPF a ser buscado nos arquivos de dados
    :return: True, caso CPF seja encontrado nos arquivos de dados
    """
    
    for cliente in dict_objects.values():
        if cliente.cpf == cpf_busca:
            return True


def password_check(txt_user: str) -> int:
    """ Tratamento de entrada de senhas

    Args:
        txt_user (str): Texto exibido ao usuário

    Returns:
        int.: Retorna a senha
    """
    while True:
        senha = input(txt_user)
        if senha == '':
            raise Exception()

        if len(senha) == 4 and senha.isdigit():
            return int(senha)
        else:
            print(erro('ERRO! A senha deve conter apenas e exatos 4 dígitos\n'))


def number_check(txt_user: str) -> float:
    """ Tratamento de entrada de números INT/FLOAT

    Args:
        txt_user (str): Texto exibido ao usuário

    Returns:
        float: Retorna o valor
    """
    while True:
        valor = input(txt_user)
        if valor == '':
            raise Exception()

        try:
            if float(valor):
                return float(valor)
        except ValueError:
            print(erro('ERRO! Valor inserido inválido\n'))


def remove_item(my_list: list, *args) -> list:
    """ Remove todos os elementos de uma lista passados como argumentos

    :param my_list: Lista principal
    :param args: Elementos que deverão ser removidos da lista principal
    :return: Retorna a lista principal com os elementos removidos
    """
    remove = list(args)

    for item in remove:
        while item in my_list:
            my_list.remove(item)

    return my_list

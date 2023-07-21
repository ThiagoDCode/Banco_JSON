import extras as ex


def name_check(txt: str):
    while True:
        name_entry = input(txt).strip().upper()
        if name_entry == '':
            return False

        if not name_entry.replace(' ', '').isalpha():
            print(ex.error('\nERRO! Nome inválido'))
        else:
            name_entry = name_entry.split(' ')

            return remove_item(name_entry, ' ', '')


def validate_cpf(txt_user: str, dict_objects: dict, recover=False) -> str:
    """ Verifica se o CPF contém 11 números e, converte o número para
    o padrão CPF do Brazil (ex: 000.000.000-00)

    :param txt_user: Texto exibido ao usuário
    :param dict_objects: Dicionário de Objetos (Com as contas dos Clientes do Banco)
    :param recover: Se True, retorna apenas o CPF formatado
    :return: Retorna o número CPF (verificado e formatado)
    """
    while True:
        cpf_entrada = input(txt_user).replace('.', '').replace('-', '').replace(' ', '')

        if len(cpf_entrada) != 11 or not cpf_entrada.isdigit():
            print(ex.error('CPF INVÁLIDO! Número CPF requer 11 números (ex: 000.000.000-00)\n'))
            continue

        cpf = f'{cpf_entrada[:3]}.{cpf_entrada[3:6]}.{cpf_entrada[6:9]}-{cpf_entrada[9:]}'
        if recover:
            return cpf

        if busca_cpf(dict_objects, cpf):
            print(ex.error('ERRO! CPF já cadastrado\n'))
        else:
            return cpf


def busca_cpf(dict_objects: dict, cpf_busca: str) -> bool:
    """ Verifica se o CPF informado já existe nos arquivos de dados.

    :param dict_objects: Dicionário de Objetos (Com as contas dos Clientes do Banco)
    :param cpf_busca: CPF a ser buscado nos arquivos de dados
    :return: True, caso CPF seja encontrado nos arquivos de dados
    """
    for cliente in dict_objects.values():
        if cliente.cpf == cpf_busca:
            return True


def verify_pass(txt: str) -> int:
    """ Tratamento de entrada de senhas

    Args:
        txt (str): Texto exibido ao usuário

    Returns:
        int.: Retorna a senha
    """
    while True:
        try:
            senha = int(input(txt))
            if len(str(senha)) != 4:
                print(ex.error('ERRO! A senha deve conter exatos 4 dígitos\n'))
                continue
            return senha
        except ValueError:
            print(ex.error('ERRO! A senha deve conter apenas dígitos\n'))


def verify_num(txt: str) -> float:
    """ Tratamento de entrada de números INT/FLOAT

    Args:
        txt (str): Texto exibido ao usuário

    Returns:
        float: Retorna o valor
    """
    while True:
        try:
            valor = float(input(txt))
            if valor < 100:
                print(ex.error('O depósito mínimo é de R$100,00\n'))
                continue
            return valor
        except ValueError:
            print(ex.error('ERRO! Valor inserido inválido\n'))


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


def menu(*options):
    print(f'+{"=" * 30}+')
    print(f'|{"<< Dalla$$ Bank >>":=^30}|')
    print(f'+{"-" * 30}+')
    for n, opt in enumerate(options):
        print(f'|{f" [{n+1}] - {opt}":30}|')
    print(f'+{"=" * 30}+')

    while True:
        try:
            resposta = int(input('|> '))
            if 0 < resposta <= len(options):
                return resposta
            else:
                print(erro_cor('ERRO! Opção inválida, tente novamente...'))
        except (ValueError, Exception):
            print(erro_cor('ERRO! Opção inválida, tente novamente...'))


def erro_cor(txt):
    return '\033[1;31m' + txt + '\033[m'


def verify_cpf(texto: str) -> str:
    """ Verifica se o CPF contém 11 números e, converte o número para
    o padrão CPF do Brazil (ex: 000.000.000-00)

    :param texto: Texto de exibição para o usuário
    :return: Retorna o número CPF (formato padrão)
    """

    while True:
        cpf_entrada = input(texto).replace('.', '').replace('-', '').replace(' ', '')

        if len(cpf_entrada) != 11 or not cpf_entrada.isdigit():
            print(erro_cor(erro_cor('\nCPF INVÁLIDO! Número CPF requer 11 números (ex: 000.000.000-00)')))
        else:
            cpf = f'{cpf_entrada[:3]}.{cpf_entrada[3:6]}.{cpf_entrada[6:9]}-{cpf_entrada[9:]}'
            return cpf


def name_check(txt: str):
    while True:
        name_entry = input(txt).strip().upper()
        if name_entry == '':
            return False

        if not name_entry.replace(' ', '').isalpha():
            print(erro_cor('\nERRO! Nome inválido'))
        else:
            name_entry = name_entry.split(' ')

            return remove_item(name_entry, ' ', '')


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
                print(erro_cor('ERRO! O depósito mínimo é de R$100,00\n'))
                continue
            return valor
        except ValueError:
            print(erro_cor('ERRO! Valor inserido inválido\n'))


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
                print(erro_cor('ERRO! A senha deve conter exatos 4 dígitos\n'))
                continue
            return senha
        except ValueError:
            print(erro_cor('ERRO! A senha deve conter apenas dígitos\n'))


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


def cor(cor=0, txt=''):
    """ Colore uma string.

    :param cor: Número da cor
    :param txt: String que será colorida
    :return: Retorna a string colorida
    """
    cores = {
        0: '\033[m',     # Neutro
        1: '\033[34m',   # Azul
        2: '\033[32m',   # Verde
        3: '\033[93m',   # Amarelo
    }

    return cores[cor] + str(txt) + cores[0]

def menu(*options):
    print(f'+{"=" * 30}+')
    print(f'|{"<<< Dalla$$ Bank >>>":=^30}|')
    print(f'+{"-" * 30}+')
    for n, opt in enumerate(options):
        print(f'|{f" {n+1} - {opt}":30}|')
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
            print(erro_cor('\nCPF INVÁLIDO! Número CPF requer 11 números (ex: 000.000.000-00)'))
        else:
            cpf = f'{cpf_entrada[:3]}.{cpf_entrada[3:6]}.{cpf_entrada[6:9]}-{cpf_entrada[9:]}'
            return cpf


def verify_name(txt: str) -> str:
    """ Tratamento de entrada de nome

    Args:
        txt (str): Texto exibido ao usuário

    Returns:
        str: Retorna o nome formatado
    """

    while True:
        name = input('Nome: ').strip()
        if not name.replace(' ', '').isalpha():
            print('\nERRO! Nome inválido\n')
        else:
            return name.title()


def verify_num(txt: str) -> float:
    """ Tratamento de entrada de números INT/FLOAT

    Args:
        txt (str): Texto exibido ao usuário

    Returns:
        float: Retorna o valor
    """

    while True:
        try:
            valor = float(input('Valor: '))
            if valor < 100:
                print('ERRO! O depósito mínimo é de R$100,00\n')
                continue
            return valor
        except ValueError:
            print('ERRO! Valor inserido inválido\n')


if __name__ == '__main__':
    deposito = verify_num('Valor: R$')
    print(deposito)

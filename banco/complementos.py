

def menu(*options):
    print(f'+{"=" * 30}+')
    print(f'|{"MENU":^30}|')
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

        if len(cpf_entrada) < 11:
            print('\nCPF INVÁLIDO! Número CPF requer no mínimo 11 números (ex: 000.000.000-00)')
        else:
            cpf = f'{cpf_entrada[:3]}.{cpf_entrada[3:6]}.{cpf_entrada[6:9]}-{cpf_entrada[9:]}'
            return cpf

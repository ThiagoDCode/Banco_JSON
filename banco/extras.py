
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
                print(error('ERRO! Opção inválida, tente novamente...'))
        except (ValueError, Exception):
            print(error('ERRO! Opção inválida, tente novamente...'))


def error(txt):
    return '\033[1;31m' + txt + '\033[m'


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

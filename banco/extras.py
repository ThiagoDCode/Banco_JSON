
def menu(*options) -> int:
    """ Usa os argumentos passados para criar um Menu dinamicamente

        Args:
            options: Opções do Menu

        Raises:
            Exception: Exibe erro caso entrada não corresponda ao range das opções

        Returns:
            Retorna o valor de entrada na resposta
        """
    tamanho = 30
    # PRINT -------------------------------------------------------
    print(f'+{"=" * tamanho}+ \n'
          f'|{"DALLA$$ Bank":^{tamanho}}| \n'
          f'+{"=" * tamanho}+')
    for n, opt in enumerate(options):
        print(f'|{f" [{n + 1}] - {opt}":{tamanho}}!')
    print(f'+{"=" * tamanho}+')
    # ------------------------------------------------------- PRINT

    while True:
        try:
            resposta = int(input('|> '))
            if 0 < resposta <= len(options):
                return resposta
            raise Exception()
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

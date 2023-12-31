
def menu(*options) -> int:
    """ Usa os argumentos passados para criar um Menu dinamicamente

        Args:
            options: Opções do Menu

        Raises:
            Exception: Exibe erro caso entrada não corresponda ao range das opções

        Returns:
            Retorna o valor de entrada na resposta
        """

    # PRINT -------------------------------------------------------
    print("=============================")
    print("|        DALLA$ BANK        |")
    print("=============================")
    for num, opt in enumerate(options):
        print(f"| {f'[{num + 1}] - {opt}':{26}}|")
    print("=============================")
    # ------------------------------------------------------- PRINT

    while True:
        try:
            resposta = int(input('|> '))
            if 0 < resposta <= len(options):
                return resposta
            raise Exception()  # Qualquer valor diferente dos que esperados, cai no 'except Exception' (opção inválida)
        except (ValueError, Exception):
            print(cor(4, "ERRO! Opção inválida, tente novamente..."))


def cor(cor_txt=0, txt=''):
    """ Colore uma string.

    :param cor_txt: Número da cor
    :param txt: String que será colorida
    :return: Retorna a string colorida
    """
    cores = {
        0: '\033[m',     # Neutro
        1: '\033[34m',   # Azul
        2: '\033[32m',   # Verde
        3: '\033[93m',   # Amarelo
    }

    if cor_txt == 4:  # Destaque de ERRO
        return '\033[1;31m' + txt + '\033[m'
    return cores[cor_txt] + str(txt) + cores[0]

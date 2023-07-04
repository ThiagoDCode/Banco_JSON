
def menu(*options):
    tamanho = 30

    print()
    print(f'+{"=" * tamanho}+')
    print(f'|{"MENU":^{tamanho}}|')
    print(f'+{"-" * tamanho}+')

    for c, op in enumerate(options):
        print(f'|{f" {c+1} - {op}":{tamanho}}|')
    print(f'+{"=" * tamanho}+')

    while True:
        try:
            resposta = int(input('|> '))
        except ValueError:
            print(erro_cor('ERRO! Digite apenas um número INTEIRO...'))
        else:
            if 0 < resposta <= len(options):
                return resposta
            else:
                print(erro_cor('ERRO! Opção inválida, tente novamente...'))


# Destaque de cor para erros
def erro_cor(txt):
    return '\033[1;31m' + txt + '\033[m'

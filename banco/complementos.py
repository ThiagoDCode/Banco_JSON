

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

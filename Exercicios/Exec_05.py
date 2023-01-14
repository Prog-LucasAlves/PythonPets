# Faça um programa que leia 5 notas de um determinado aluno(matemática, física, química, biologia e geografia)
# e imprima a média final do aluno na tela.

BLUE = "\033[1;34m"
RED = "\033[0;31m"
RESET = "\033[0;0m"

MATERIAS = ['matemática', 'física', 'química', 'biologia', 'geografia']


def verifica_input(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def input_valores(string):
    while True:
        valor = input(f'{string}').replace(',', '.')
        if verifica_input(valor):
            break
        else:
            print(f'## Você não digitou um formato válido - |{valor}| ##')
    return float(valor)


def valores():
    notas_ = []
    for MATERIA in MATERIAS:
        notas = input_valores(f'## Qual a nota de {MATERIA}: ')
        notas_.append(notas)
        media_notas = sum(notas_) / len(notas_)

    return media_notas


def verifica_media():
    media_notas = valores()
    if media_notas < 6.0:
        print('##')
        print(
            f'Sua nota foi {RED}{media_notas}{RESET} - Abaixo da média que é: 6.0')
    else:
        print('##')
        print(
            f'Sua nota foi {BLUE}{media_notas}{RESET} - Acima da média que é: 6.0')


if __name__ == '__main__':
    verifica_media()

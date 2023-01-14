# Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.

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
            print(f'## Você não digitou um formato válido - {valor}. ##')
    return float(valor)


def conversao():
    resultado = input_valores('Digite a quantidade de metros: ')
    conversao = resultado * 100
    print(f'{resultado:.2f} metro(s) são {conversao:.0f} milímitros')


if __name__ == '__main__':
    conversao()

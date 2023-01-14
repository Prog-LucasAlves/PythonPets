# Faça um programa que peça dois números inteiros.
# Imprima a soma deles na tela

def verifica_input(string):
    """
    Função
    """
    try:
        int(string)
        return True
    except ValueError:
        return False


def input_valores(string):
    while True:
        valor = input(f'{string}')
        if verifica_input(valor):
            break
        else:
            print('## Você não digitou um número inteiro. ##')
    return int(valor)


def qtd_valores():
    lista_numeros = []
    print('-----')
    qtd = input_valores('Quantos números seram somados: ')
    print('-----')
    for i in range(qtd):
        numero = input_valores(f'Digite o {i+1}º número: ')
        lista_numeros.append(numero)

    return lista_numeros


def soma():
    numeros = sum(qtd_valores())
    print('-----')
    return print(f'A Soma dos números é: {numeros} \n-----')


if __name__ == '__main__':
    soma()

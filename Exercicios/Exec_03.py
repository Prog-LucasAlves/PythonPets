# Faça um programa que calcule o aumento de um salário.
# O programa deve solicitar o valor do salário e a porcentagem de aumento.
# Exiba o valor do aumento de do novo salário


RED = "\033[1;31m"
RESET = "\033[0;0m"


def verifica_input(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def input_valores(string):
    while True:
        valor = input(f'{string}')
        if verifica_input(valor):
            break
        else:
            print(
                f'## Você não digitou um formato válido - |{valor}| - |Formato 1000.00|. ##')
    return float(valor)


def salario():
    print('###############################')
    print('##### .|Formato 1000.00|. #####')
    print('###############################')
    salario = input_valores('Informe o seu salário: ')
    porcentagem = input_valores('Informe a (%) de aumento: ')

    aumento = salario * porcentagem / 100
    novo_salario = f'{salario + aumento:,.2f}'.replace(
        ',', '_').replace('.', ','). replace('_', '.')
    aumento_str = f'{aumento:,.2f}'.replace(
        ',', '_').replace('.', ','). replace('_', '.')

    print('###############################')
    print(
        f'O aumento foi de {RED}R${aumento_str}{RESET} - e o valor do novo salário e de {RED}R${novo_salario}{RESET}')
    print('###############################')


if __name__ == '__main__':
    salario()

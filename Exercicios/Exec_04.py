# Escreva um programa que pergunta a quantidade de km percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado

RED = "\033[0;31m"
RESET = "\033[0;0m"


def verifica_input(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def input_valores(string):
    while True:
        valor = int(round(float(input(f'{string}').replace(',', '.'))))
        if verifica_input(valor):
            break
        else:
            print(f'## Você não digitou um formato válido - |{valor}| ##')
    return int(valor)


def valores():
    print('#####')
    print(f'{RED}Frações de km(s)[0-1-2-3-4-5] Serão arredondadas para baixo.')
    print(f'Frações de km(s)[6-7-8-9] Serão arredondadas para cima{RESET}.')
    print('#####')
    km_percorridos = input_valores('Isira a quantidade de km(s) percorridos: ')
    qtd_dias = input_valores(
        'Insira a Quantidade de dias com o carro alugado: ')

    return km_percorridos, qtd_dias


def calculo():
    PRECO_POR_DIA = 60
    PRECO_POR_KM = 0.15

    km_percorridos, qtd_dias = valores()
    total = km_percorridos * PRECO_POR_KM + qtd_dias * PRECO_POR_DIA

    print('#####')
    print(f'O Total a ser pago e: R${total:,.2f}')


if __name__ == '__main__':
    calculo()

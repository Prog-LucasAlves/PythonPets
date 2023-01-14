# Operações matemáticas

def operacoes_matematicas(num1:float, num2:float) -> dict[str, int|float]:
    soma = num1 + num2
    diferenca = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2

    print(f'A Soma de {num1} com {num2}: {soma}')
    print(f'A Diferença de {num1} com {num2}: {diferenca}')
    print(f'A Multiplicação de {num1} com {num2}: {multiplicacao}')
    print(f'A Divisão de {num1} com {num2}: {divisao}')

    resultado = {
        'soma':soma, 'diferenca':diferenca, 'mi':multiplicacao
    }

    return resultado

if __name__ == '__main__':
    print(operacoes_matematicas(5.5, 5))

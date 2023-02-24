## Agenda ##

# Incluir contato
# Alterar contato
# Excluir contato
# Mostrar contatos
# Pesquisar contato

import csv

BLUE = "\033[0;34m"
GREEN = "\033[0;32m"
RED = "\033[0;31m"
RESET = "\033[0;0m"

def inicia_agenda() -> int:
    print('#######################################')
    print('------- BEM VINDO A SUA AGENDA --------')
    print('#######################################')
    print('####### Escolha uma das opções ########')
    print('---------------------------------------')
    print('######## |1| - Criar Contato ##########')
    print('######## |2| - Alterar Contato ########')
    print('######## |3| - Excluir Contato ########')
    print('######## |4| - Pesquisar Contato ######')
    print('######## |5| - Mostrar Contatos #######')
    print('#######################################')


    opcao_escolhida = input('\nDigite o número da opção desejada: ')
    opcao_escolhida_valida = opcao_escolhida.isdecimal() \
                        and int(opcao_escolhida) <= 5 \
                        and int(opcao_escolhida) > 0

    while not opcao_escolhida_valida:
        print('#######################################')
        print(f'\n{RED}##### Opção Digitada Inválida -> [{opcao_escolhida}] ##{RESET}')
        print('#######################################')
        print('####### Escolha uma das opções ########')
        print('---------------------------------------')
        print('######## |1| - Criar Contato ##########')
        print('######## |2| - Alterar Contato ########')
        print('######## |3| - Excluir Contato ########')
        print('######## |4| - Pesquisar Contato ######')
        print('######## |5| - Mostrar Contatos #######')
        print('#######################################')
        opcao_escolhida = input('\nDigite o número da opção desejada: ')
        opcao_escolhida_valida = opcao_escolhida.isdecimal() \
                        and int(opcao_escolhida) <= 5 \
                        and int(opcao_escolhida) > 0       
    return int(opcao_escolhida)

def opcao_escolhida() -> list:
    contato = []
    escolha = inicia_agenda()
    if escolha == 1:
        print('\n#######################################')
        print(f'######## {BLUE}Opção |1| Selecionada{RESET} ########')
        print('---------------------------------------')
        print(f'######## {GREEN}Cadastro de um novo contato{RESET} ##')
        nome = input('Digite o nome: ')
        nome_valido = any(nome.isdigit() for nome in nome)
        print(nome_valido)
        nome = nome.capitalize()
        while nome_valido:
            print(f'####### {RED}Nome Digitado Inválido ->|{nome}|{RESET} ###')
            nome = input('Digite o nome: ')
            nome_valido = any(nome.isdigit() for nome in nome)
            nome = nome.capitalize()

        sobrenome = input('Digite o nome: ')
        telefone = input('Digite o nome: ')
        contato.append(nome)
        contato.append(sobrenome)
        contato.append(telefone)
        print(contato)

        with open('./contatos.csv', 'a', newline='\n') as csvfile:
            write = csv.writer(csvfile, quoting=csv.QUOTE_ALL,delimiter=';')
            write.writerow(contato)
    
if __name__ == '__main__':
    opcao_escolhida()
    
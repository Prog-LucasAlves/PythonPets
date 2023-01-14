
# Vacinação (Segunda dose):

# 1. Ser maior de 21 Anos
# 2. Ter tomado a primeira dose da vacina
# 3. Ter mais de 6 meses que tomou a primeira dose

BLUE = "\033[0;34m"
GREEN = "\033[0;32m"
RED = "\033[0;31m"
RESET = "\033[0;0m"

idade = input(f'{BLUE}Qual a sua idade:{RESET} ')
idade_valida = idade.isdecimal() and int(idade) > 0

while not idade_valida:
    print(f'\n{RED}###!! Idade Inválida! Por Favor Digite uma Idade Válida. !!###{RESET}')
    idade = input(f'{BLUE}Digite sua idade novamente, por favor!:{RESET} ')
    idade_valida = idade.isdecimal() and int(idade) > 0

idade = int(idade)

maior_idade = idade < 21

if maior_idade:
    print(f'\n{RED}###!! Você não pode tomar a vacina só pessoas acima de 21 anos. !!###{RESET}')

else:
    segunda_dose = input(f'{BLUE}Tomou a primeira dose da vacina (S/N):{RESET} ')
    informacao_dose_valida = segunda_dose.lower() == 'n' or segunda_dose.lower() == 's'

    while not informacao_dose_valida:
        print(f'\n{RED}###!! Você Digitou uma informação incorreta. !!###{RESET}')
        segunda_dose = input(F'{BLUE}Informe Por Favor se Já Tomou a Primeira Dose da Vacina (S/N):{RESET} ')
        informacao_dose_valida = segunda_dose.lower() == 'n' or segunda_dose.lower() == 's'

    tomou_segunda_dose = segunda_dose == 'n'

    if tomou_segunda_dose:
        print(f'\n{RED}###!! Você não pode tomar a segunda dose da vacina. !!###{RESET}')
        print(f'\n{RED}###!! Procure um Posto de Saúde Aonde Esteja Aplicando a 1º Dose da Vacina. !!###{RESET}')

    else:
        meses = input(f'{BLUE}Faz quantos meses que você tomou a primeira dose:{RESET} ')
        informacao_mes_valida = meses.isdecimal() and int(meses) >= 0

        while not informacao_mes_valida:
            print(f'\n{RED}###!! Mês Inválido! Por Favor Digite um Mês Válido. !!###{RESET}')
            meses = input(f'{BLUE}Faz quantos meses que tomou a primeira dose:{RESET} ')
            informacao_mes_valida = meses.isdecimal() and int(meses) >= 0
        
        meses = int(meses)

        meses_correto = meses <= 6
            
        if meses_correto:
            print(f'\n{RED}###!! Voce não tem o tempo suficiente para tomar a segunda dose da vacina. !!###{RESET}')
            print(f'{RED}###!! AGUARDE O TEMPO NECESSÁRIO DE 6 MESES. !!###{RESET}')
            
        else:
            print(f'\n{GREEN}Siga a fila para tomar a segunda dose da vacina.{RESET}')


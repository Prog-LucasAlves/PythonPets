# Vacinação (Segunda dose):

# 1. Ser maior de 21 Anos
# 2. Ter tomado a primeira dose da vacina
# 3. Ter mais de 6 meses que tomou a primeira dose

idade =  int(input('Qual a sua idade: '))
maior_idade = idade < 21

if idade < maior_idade:
    print('Você não pode tomar a vacina só pessoas acima de 21 anos.')

else:
    segunda_dose = input('Tomou a primeira dose da vacina (S/N): ')
    tomou_segunda_dose = segunda_dose.lower() == 'n'

    if tomou_segunda_dose:
        print('Você não pode tomar a segunda dose da vacina.')

    else:
        meses = int(input('Faz quantos meses que tomou a primeira dose: '))
        meses_correto = meses <= 6
            
        if meses <= meses_correto:
            print('Voce não tem o tempo suficiente para tomar a segunda dose da vacina.')
            
        else:
            print('Siga a fila para tomar a segunda dose da vacina.')

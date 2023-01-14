# %%

frase = 'O importante não é vencer todos os dias, mas lutar sempre'

for posicao, letra in enumerate(frase, start=1):
    print(f'A letra {letra} esta na posição -> {posicao}')

# %%

estado_sigla = {
    'rio de janeiro': 'rj',
    'sao paulo': 'sp',
    'minas gerais': 'mg'
}

for posicao, estado in enumerate(estado_sigla.values()):
    print(posicao, estado)
# %%

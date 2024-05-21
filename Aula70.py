frase = 'Python é uma linguagem de programação criado por Guido Van Rossum de tipagem dinâmica'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]
    qtd_letras = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if qtd_apareceu_mais_vezes < qtd_letras:
        qtd_apareceu_mais_vezes = qtd_letras
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print('A letra que apareceu mais vezes foi a letra "{}" {} vezes'.format(letra_apareceu_mais_vezes,qtd_apareceu_mais_vezes))

    
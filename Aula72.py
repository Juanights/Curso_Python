
texto = 'python'
novo_texto = ''
for letra in texto:   # for significa "para". Nesse bloco de código significa que para cada letra dentro do texto ele vai printar. Fazendo uma iteração(repetição) indo para cada uma das letras dentro da nossa variavel texto
    novo_texto += f'*{letra}'
    
print (novo_texto + '*')
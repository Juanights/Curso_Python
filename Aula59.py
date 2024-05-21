"""condicao = True

while condicao: # while siginifica 'enquanto'. Nesse curto bloco de código significa que enquando minha variavel 'condicao' for True meu bloco de código será executado
    print(1)
    print(2)
    print(3) 

    input('') # Input para não gerar um looping infinito.
"""
condicao = True
while condicao:
    nome = input('Digite seu nome: ')  
    print('Seu nome é {}'.format(nome)) 

    if nome == 'sair':
        break  # Usamos o break para freiar ou parar a execução do nosso código, nesse caso usei junto com um if, então se caso o nome digitado foi sair meu código da um break e para de ser executado.
print('Acabou!!')    


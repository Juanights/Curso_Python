"""
Iterando strings com while
"""
#       012345678910
nome = input('Digite seu nome: ') # Iteráveis
#      1110987654321

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += ('-{}'.format(letra))
    indice += 1 
novo_nome += '-'    
print(novo_nome)
    

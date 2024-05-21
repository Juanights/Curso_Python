"""Podemos criar um while dentro de outro while como se fosse uma engrenagem pequena dentro de uma engrenagem maior. nesse caso iremos criar uma tabela com 5 linhas e 5 colunas para cada linha, totalizando 25 colunas"""

qtd_linhas = 5
qtd_colunas = 5

linha = 1
coluna = 1
while linha <= qtd_linhas:
    coluna = 1
    
    while coluna <= qtd_colunas:
        print(linha, coluna)
        coluna += 1
        
    linha += 1
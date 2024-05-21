
import os
# Faça um jogo para o usuário adivinhar qual a palavra secreta.

# - Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
palavra_secreta = ('Python').lower() # Variavel da nossa palavr secreta
letra_certa = ''
tentativas = 0

while True: # vamos deixar o nosso codigo dentro do while para se repetir
    letra_digitada = input('Tente descobrir a palavra secreta, digite uma letra: ') # Input para o usuario digitar a letra
    tentativas += 1

    if len(letra_digitada) > 1: # A função len faz a contagem das letras dentro da nossa variavel - se a quantidade que digitamos for maior que 1 nosso codigo vai exibir a mensagem abaixo
        print('Digite somente uma letra')
        continue 
    if letra_digitada.isalpha() == False:
        print('não é aceito numeros, digite apenas uma letra')
        continue


    if letra_digitada in palavra_secreta: # se a nossa letra digitada estiver dentro da palavra secreta ela vai...
        letra_certa += letra_digitada # Ela vai pegar a nossa letra certa e guardar na variavel letra_certa

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_certa:   
            palavra_formada += letra_secreta  
        else:
            palavra_formada += '*'
    print(palavra_formada)

    if palavra_formada == palavra_secreta: 
        os.system('cls')      
        print(palavra_formada)    
        print(f'PARABÉNS VOCÊ ACERTOU A PALAVRA SECRETA QUE É {palavra_secreta}, em {tentativas} tentativas')
        letra_certa = ''
        tentativas = 0        

    


   
    #  Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    # Se a letra digitada estiver na palavra secreta; exiba a letra;

    # Se a letra digitada não estiver na palavra secreta; exiba *.
    # Faça a contagem de tentativas do seu usuário.
# Uso da palavra continue = Usamos para pular o bloco de códigos

contador = 0

while contador <= 100:
    contador += 1
    

    if contador == 6:
        print('Não vou mostrar o 6') # Muito cuidado como montar nossa estrutura, uma posição do print ou do continue pode afetar a execução do código
        continue # -> nosso bloco de código vai pular quando nosso contador for o numero 6

    if contador >=10 and contador <=25:
        print('Não vou mostrar', contador)
        continue
    
    print(contador)

    if contador == 50:
        print('Vou parar no numero 50')
        break

print('Acabou') 
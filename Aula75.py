for i in range(10):
    if i == 2:
        print('i é igual a 2')
        continue

    if i == 8:
        print('Seu else não será executado')
        break

    for j in range(1,3):
        print(i,j)
else:
    print('Comando executado com sucesso')        
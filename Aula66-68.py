while True:

    numero1 = input('Digite o primeiro numero: ')
    numero2 = input('Digite o segundo numero: ')
    operador = input('Digite um operador (+,-,*,/): ')
    numero1_f = 0
    numero2_f = 0
    numeros_validos = None
    try:
        numero1_f = float(numero1)
        numero2_f = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Por favor Digite apenas Numeros!')  
        continue      

    operadores_permitidos = '+-*/'    

    if operador not in operadores_permitidos:
        print('Operador invalido!')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue


    
    if operador == '+':
        resultado =  numero1_f + numero2_f
        print('{:.0f} + {:.0f} = {:.0f}'.format(numero1_f,numero2_f,resultado))
    if operador == '-':
        resultado = numero1_f - numero2_f
        print('{:.0f} - {:.0f} = {:.0f}'.format(numero1_f,numero2_f,resultado))
    if operador == '*':
        resultado = numero1_f * numero2_f
        print('{:.0f} * {:.0f} = {:.0f}'.format(numero1_f,numero2_f,resultado))
    elif operador =='/':
        resultado = numero1_f / numero2_f
        print('{:.0f} / {:.0f} = {}'.format(numero1_f,numero2_f,resultado))     


    sair = input('Deseja sair? [s]im: ').lower().startswith('s')
        
    if sair is True:
        break


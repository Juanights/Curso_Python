# lista = [1,2,3,4]
# print(lista[2])

# lista[1] = 50
# print(lista)

# lista.append(55)
# lista.append(70)
# lista.append(58)
# print(lista)
# lista.pop()
# ultimo_valor = lista.pop()
# print(ultimo_valor)

lista = [10,20,30,40]
print(lista)
lista.append('Juan')
nome = lista.pop()
print(lista, nome)
lista.append(50)

del lista[-1]
lista.insert(1,200)
print(lista)

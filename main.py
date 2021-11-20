x = int(input('digite um numero: '))
y = int(input('digite um numero maior que o anterior: '))
total = 0
numeros = []

if x >= y:
    print('ERROR: primeiro numero maior ou igual a o segundo!')
else:
    while x < y:
        if x%2 == 1:
            numeros.append(x)
            total += x
        x += 1
    print('''
          entre x e y tiveram {} numeros impares
          que foram os numeros {}
          e a soma desses numeros é igual a {}'''.format(len(numeros),numeros,total))

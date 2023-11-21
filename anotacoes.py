# Separador de milhares ======================================================


# Este
num = 10000000000


# é igual a este:
num = 10_000_000_000




# zip =========================================================================


capitais = ('São Paulo', 'Curitiba', 'Natal', 'Campo Grande', 'Manaus')
estados = ('SP', 'PR', 'RN', 'MS', 'AM')
regioes = ('Sudeste', 'Sul', 'Nordeste', 'Centro Oeste', 'Norte')

for capital, estado, regiao in zip(capitais, estados, regioes):
    print(f'{capital} - {estado}: {regiao}')

'''
São Paulo - SP: Sudeste
Curitiba - PR: Sul
Natal - RN: Nordeste
Campo Grande - MS: Centro Oeste
Manaus - AM: Norte
''' 


# Unpack values ==============================================================

x, y = (7, 9)

print(x)
7

print(y)
9

# Caso queira descartar algum valor
x, _ = (7, 9)

print(x)
7



x, y, *z = (1, 2, 3, 4, 5)

print(x)                                                                                                                                                                                                   
1

print(y)                                                                                                                                                                                                   
2

print(z)                                                                                                                                                                                                   
[3, 4, 5]



x, *y, z = (1, 2, 3, 4, 5)

print(x)                                                                                                                                                                                                   
1

print(y)                                                                                                                                                                                                  
[2, 3, 4]

print(z)                                                                                                                                                                                                  
5


*x, y, z = (1, 2, 3, 4, 5)                                                                                                                                                                                

print(x)                                                                                                                                                                                                  
[1, 2, 3]

print(y)                                                                                                                                                                                                  
4

print(z)                                                                                                                                                                                                  
5



# Descartando valores
*_, y, z = (1, 2, 3, 4, 5)                                                                                                                                                                                

print(y)                                                                                                                                                                                                  
4

print(z)                                                                                                                                                                                                  
5

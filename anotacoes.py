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
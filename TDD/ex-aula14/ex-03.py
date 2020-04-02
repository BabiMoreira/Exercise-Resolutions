def calcular_area(raio):
    area = 3.14*raio**2
    return area

def calcular_comprimento(raio):
    comprimento= 2*3.14*raio
    return comprimento
# 

askRaio= float(input('Digite o valor do raio: '))

area = calcular_area(askRaio)
comprimento = calcular_comprimento(askRaio)

print('a circuferência do raio {} é de {}'.format(askRaio, area))
print('O raio de {} tem o comprimento de {}'.format(askRaio,comprimento))


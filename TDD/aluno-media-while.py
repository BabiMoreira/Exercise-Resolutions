contador = 0
lista_media = []

while contador <4:
    lista_media.append(float(input('Digite uma Nota: ')))
    contador = contador + 1

media = (lista_media[0]+lista_media[1]+lista_media[2]+lista_media[3]) /4

if media >7:
    print('Parabéns , você foi aprovado. Sua média é de {}. '. format( media))
elif (media <7) and (media >5.5):
    print('Otimo , você não fez mais que a sua obrigação. Sua média é de {}.'.format( media))
else:
    print('Uauu , hoje não. Sua média é de {}.'.format( media))

lista = [2, 0, 8, 4, 10, 0, 2, 89, 1, 75, 25, 11, 3]
lista_ordenada = sorted(lista)
lista_decrescente = sorted(lista, reverse=True)
pergunta = input('Deseja a lista na ordem crescente ou decrescente ? ')

if pergunta == 'crescente' or pergunta == 'c':
    print(lista_ordenada)
elif pergunta == 'decrescente' or pergunta == 'd':
    print(lista_decrescente)
else:
   print('não encontrado')

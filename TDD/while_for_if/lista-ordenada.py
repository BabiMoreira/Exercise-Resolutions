# lista = [2, 0, 8, 4, 10, 0, 2, 89, 1, 75, 25, 11, 3]
# print('Essa é a lista a ser ordenada {}'.format(lista))
# lista.sort()
# print('Essa é a lista em ordem crescente {}'.format(lista))
# lista.sort(reverse=True)
# print('Essa é a lista em ordem decrescente {}'.format(lista))

number_list = []
number = input('Digite um número: ')
question = input('Deseja adicionar mais números: ')

while True:
    number_list.append(number)
    if question == 'sim' or question == 's':
        number = input('Digite um número: ')
        question = input('Deseja adicionar mais números: ')
    elif question == 'nao' or question =='n':
        print('Lista Ordenada: {}'.format(sorted(number_list, key=int)))
        break
    else:
        print('alguma coisa')
        break
print('Lista não ordenada: {}'.format(number_list))


 
        


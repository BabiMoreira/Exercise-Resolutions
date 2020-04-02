lista_palavras = []
question_one = input('Digite uma palavra: ')
question_two = input('Você quer continuar? ')

while True:
    lista_palavras.append(question_one)
    if question_two == 'sim' or question_two == 'yes':
        question_one = input('Digite uma palavra: ')
        lista_palavras.append(question_one)
    elif question_two == 'não' or question_two == 'nao':
        print('O questionário esta encerrado')
        break
    else:
        print('abobrinha')
    print(lista_palavras)
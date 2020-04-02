print('Vamos começar o teste ')

while True:
    resposta_usuario = input('Você é um Gato? ')
    if resposta_usuario == "sim" or resposta_usuario == 'yes':
        print(' Uauu que bacana ')
        break
    elif resposta_usuario == 'não' or resposta_usuario == 'no':
        print('Que triste, esperava mais de você ')
        break
    else:
        print('Digite sim ou não ')
        break


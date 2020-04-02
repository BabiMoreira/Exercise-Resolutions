nome_aluno = input('Digite o nome do aluno: ')
nota1 = float(input('Entre com a nota um: '))
nota2 = float(input('Entre com a nota dois: '))
nota3 = float(input('Entre com a nota tres: '))
nota4 = float(input('Entre com a nota quatro: '))
media = (nota1 + nota2 + nota3 + nota4) / 4

if media >7:
    print('Parabéns {}, você foi aprovado. Sua média é de {}. '. format(nome_aluno, media))
elif (media <7) and (media >5.5):
    print('Otimo {}, você não fez mais que a sua obrigação. Sua média é de {}.'.format(nome_aluno, media))
else:
    print('Uauu {}, hoje não. Sua média é de {}.'.format(nome_aluno, media))

def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media
# função responsavel por calcular a media do aluno , recebendo dois parametros, nota1 e nota2 
# que são calculadas dentro de uma variavel.

def verificar_media(nota1, nota2):
    
    media_aluno= calcular_media(nota1, nota2)
    
    if media_aluno >= 6:
        print('Parabéns! você foi aprovado')
    else:
        print('Não foi dessa vez, você foi reprovado')

# A  função verificar_media é responsavel por verificar se o aluno passou ou não de ano com as condições propostas. Logo no inicio 
# criei uma variavel chamada media_aluno que recebe a função calcular_media com os parametros nota1 e nota2, que irão receber o valor do proprio usuario.


nota1 = float(input('Digite a nota um: '))
nota2 = float(input('Digite a nota dois: '))
# variaveis criadas para receber o valor do usuário, nota-se que os nomes das variaveis são os mesmo que os parametros passados para a função calcular_media em media_aluno.

verificar_media(nota1, nota2)




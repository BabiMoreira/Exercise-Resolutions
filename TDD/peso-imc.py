
peso = int(input('Digite seu peso atual:'))
altura = float(input('Digite sua altura:'))
calculo_imc = round(peso/(altura*altura), 2)
dados_usuario = print('\nINFORMAÇÕES PESSOAIS \nPeso: {}kg \nAltura: {} \nIMC: {}'.format(peso, altura, calculo_imc))

if calculo_imc <18.5:
    print('Você esta abaixo do peso ideal')
elif calculo_imc <=24.9:
    print('Parabéns você está em seu peso normal')
elif calculo_imc <=30:
    print('Você está acima de seu peso')
elif calculo_imc >30:
    print('Você está Obeso')

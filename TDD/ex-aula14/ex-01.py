def numeroPar(numero):
    if numero % 2 == 0:
        print('o número {} é par'.format(numero))
    else:
        print('o númeor {} é impar'.format(numero))

# Na função numeroPar estou passando um parametro chamado numero, em que vou utilizar
# nas minhas condições. Se o numero digitado pelo usuario for par ou impar ele vai imprimir
# a  mensagem referente a sua condição.

askUser = int(input('Digite um Número: '))
# Aqui criei uma variavel que irá pegar o valor do usuario

resultado = numeroPar(askUser)
# a variavel resultado esta sendo utilizada para chamar a função
# numeroPar e passar a variavel que o usuario digitou o valor.


carrinho= int(input('Quantos produtos você tem no carrinho ?'))
contador = 0

while contador < carrinho:
    nome_produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o valor por unidade do produto: '))
    quantidade = int(input('Quantidade de {}: '.format(nome_produto)))
    valor = preco*quantidade
    contador = contador + 1
    print('\nRECIBO \nQuant. Produto Preço \n{} {} {}'.format(quantidade, nome_produto, valor) )
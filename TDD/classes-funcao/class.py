# a class é a forma do nosso objeto

class Carro:
    def __init__(self, proprietario, modelo, cor, placa, preco, marca):
        # o self é a referencia para os meus atributos 
        self.proprietario = proprietario
        self.modelo = modelo
        self.cor = cor
        self.placa = placa
        self.preco = preco
        self.marca = marca

    # a função def str esta convertendo o objeto Carro em string possibilitando a visualização(print)
    # para o usuario.

    def __str__(self):
        return f"Olá {self.proprietario}, o seu carro é {self.modelo} da marca {self.marca}, {self.cor}, no preço de {self.preco}"

# a variavel foi criada com  o intuito de chamar o objeto Carro e atribuir valor para os seus argumentos(parametros)

veiculo= Carro(
    proprietario = 'Mario Gomez',
    modelo = 'Fusca',
    cor= 'Preto',
    placa = 'TDD-0083',
    marca = 'Wolgs',
    preco= 30000
)

print(veiculo)
class Funcionario:
    def __init__(self, nome, email, rg, idade, salario):
        self.nome = nome
        self.email = email
        self.rg = rg
        self.idade = idade
        self.salario = salario

    def __str__(self):
        return f'Olá {self.nome}, você foi cadastrado com sucesso'

    def aumentar_salario(self, aumento):
        return self.salario+aumento

dados_funcionario = Funcionario(
    nome = 'José',
    email = 'josealmeida@gmail.com',
    rg = '35078787689',
    idade = 20,
    salario = 2000
)

print(dados_funcionario)
print(dados_funcionario.aumentar_salario(2000))
print(dados_funcionario.aumentar_salario(float(input('Digite o valor do aumento: '))))
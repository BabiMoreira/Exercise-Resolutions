class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Pet(Cliente):
    def __init__(self, nome, idade, nome_pet, idade_pet ):
        super().__init__(nome, idade)
        self.nome_pet = nome_pet
        self.idade_pet = idade_pet

cliente = Cliente('Tobias Oliveira,', '20 anos')
pet = Pet( 'nome' ,'idade',' Chewie', '7 anos')

print('O {} ' 'é dono do {} de {}' .format(cliente.nome, pet.nome_pet, pet.idade_pet))
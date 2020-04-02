# lista_nomes = ['Bárbara', 'Moreira', 'Jessica', 'Joao']
# #
# for nome in lista_nomes:
#     print(nome)
# else:
#     print('Esta terminado')

estudantes = []
i=0
while i < 4:
     estudantes.insert(i, input("Digite o nome do aluno: "))  
     i+=1
i=0    
while i < len(estudantes):
     print("Aluno {}: {}".format(i, estudantes[i]))
     i+=1

#
# i = 0
#
# while i < len(lista_nomes):
#     print(lista_nomes[i])
#     i+= 1

# degraus = int(input('Digite um numero de degraus '))
# for item in range (0, degraus):
#     print(item)
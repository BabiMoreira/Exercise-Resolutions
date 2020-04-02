palavras = ['amanda', 'aline', 'anderson', 'ana paula', 'barbara', 'bianca', 'beatriz', 'carlos', 'camila', 'debora', 'diego', 'thiago', 'helio', 'leonardo']
pergunta = input('Digite uma letra a ser filtrada: ')


def filtrarLetras(letra):
    return letra.startswith(pergunta)
print(list(filter(filtrarLetras, palavras)))

def trocar_vogais(letras):
    # vogais = "aeiou"
    vogais = {
        'a': '@',
        'e': '&',
        'i': '!',
        'o': '#',
        'u': '*'
    }
    for letra in vogais:
        letras = letras.replace(letra, vogais[letra])
    
    print (letras)
    return letras
    

print(trocar_vogais('luar')) 
# imprime l*@r

print(trocar_vogais('bocejo')) 
# imprime b#c&j#

print(trocar_vogais('tranquilo')) 
# imprime tr@nq*!l#

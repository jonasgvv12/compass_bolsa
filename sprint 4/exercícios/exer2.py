def conta_vogais(texto:str)-> int:
    vogais = 'AEIOUaeiou'
    return len(list(filter(lambda x: x in vogais, texto)))
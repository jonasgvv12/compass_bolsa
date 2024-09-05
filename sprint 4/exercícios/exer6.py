def maiores_que_media(conteudo:dict)->list:
    media = sum(conteudo.values()) / len(conteudo)
    acima_da_media = filter(lambda item: item[1] > media, conteudo.items())
    return sorted(acima_da_media, key=lambda item: item[1])
def funcao(*n_nomeado, **parametro_nomeado):
    for n_nomeados in n_nomeado:
        print(n_nomeados)
    for primeiro, segundo in parametro_nomeado.items():
        print(f"{primeiro} = {segundo}")

funcao(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
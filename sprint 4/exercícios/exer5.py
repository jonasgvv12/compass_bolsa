import csv

def processar_notas(arquivo_csv):
    estudantes = []
    with open(arquivo_csv, newline='', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile)
        
        for linha in leitor:
            nome = linha[0]
            notas = list(map(float, linha[1:]))
            tres_maiores_notas = sorted(notas, reverse=True)[:3]
            media = round(sum(tres_maiores_notas) / 3, 2)
            estudantes.append((nome, tres_maiores_notas, media))

    ordenados = sorted(estudantes, key=lambda x: x[0])

    for estudante in ordenados:
        nome, notas, media = estudante
        notas_formatadas = ', '.join(map(str, notas))
        print(f"Nome: {nome} Notas: [{notas_formatadas}] Média: {media:.2f}")
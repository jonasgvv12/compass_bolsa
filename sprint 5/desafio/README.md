### Documentação

*CONSULTAS*
1. [Primeira_Consulta](consulta1.sql)
2. [Segunda_Consulta](consulta2.sql)
3. [Terceira_Consulta](consulta3.sql)
4. [Quarta_Consulta](consulta4.sql)
5. [Quinta_Consulta](consulta5.sql)

Durante o desafio, utilizei somente o S3 Select dentro da própria da plataforma da AWS, testei implementações em python utilizando o Boto3, optei pela utilização do Console, tive alguns problemas com a implementação em Python, mas depois de alguns testes funcionou, apenas optei pela implementação via console mesmo.

Na primeira consulta, acessei a tabela "vl_despesa", utilizando da função CASE para dividir em grupos por valor gasto na despesa total. No grupo 1, somente os projetos que tiveram despesas menores que 2500 reais, no grupo 2, somente os projetos que tiveram despesas acima de 2500 reais. Durante a consulta, apesar dos valores da tabela "vl_despesa" já estarem em valores FLOAT, transformei os valores no CAST para garantir que não houvesse equívocos no resultado da query.

Na segunda consulta, acessei a tabela "tx_justificativa", única tabela dentro da minha base de dados que continha valores em strings. Para essa consulta, utilizei a função "CHAR_LENGTH" para retornar apenas as strings maiores que 25 caracteres.

Na terceira consulta, acessei as tabelas "id_projeto", "id_despesa" e "vl_unitario", na qual utilizei o CAST para transformar os valores float para valores inteiros. A query retornava o ID do projeto e o ID da despesa onde os valores unitários eram maiores do que 100. 

Na quarta consulta, acessei as tabelas "Id_projeto", "vl_despesa" e "CD_IDENTIFICADOR_RUBRICA", para retornar uma query que me informasse o ID do projeto e o valor da despesa dos quais os valores "339033" e "339018" da tabela "cd_identificador_rubrica" haviam participado. Também utilizei o LIMIT 20 ao final para não criar uma consulta muito pesada, visto que haviam vários projetos nos quais esses 2 haviam participado.

Na quinta e última consulta, acessei a tabela "vl_despesa" novamente, agora com uma função AVG, que retornava esse valor em uma nova tabela "Media_despesa" para descobrir a média da despesa do identificador "339033" dentro de todos os projetos/palestras/eventos que ele havia participado.

*AS EVIDÊNCIAS E PRINTS DE EXECUÇÃO ESTÃO TODAS DENTRO DO README DA SPRINT E DA PASTA EVIDÊNCIAS.*
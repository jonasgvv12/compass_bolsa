### DOCUMENTAÇÃO

- [CODIGOS LAMBDA](/sprint%207/Desafio/consultas_lambda)

Durante o desenvolvimento do desafio, foi somente utilizado a API do TMDB, pois estou analisando apenas filmes. Durante a ingestão de dados, procurei dentro da API dados de filmes do mesmo gênero que a saga crepúsculo (Saga que está por trás da análise), armazenando seus dados comuns (ID, Rating, Popularidade, Runtime, etc...) para responder uma das perguntas do meu desafio: "Como a saga se compara a produções de gêneros parecidos?". Uma pergunta em específico tem que ser mudada: "Como a popularidade dos atores principais evoluiu ao longo da saga?" pois o TMDB não armazena a popularidade de um ator em um período/data específica, apenas a popularidade atual. Da minha ingestão de dados pela API, os dados dos filmes semelhantes, e alguns que disputaram bilheteria com os filmes da saga crepúsculo perto da sua data de lançamento (Toy Story 3, Mamma Mia, The Avengers) foram os mais valiosos que consegui coletar, pois contribuem diretamente para resposta de uma das perguntas citadas acima. Pretendo fazer uma ingestão maior de dados usando outras APIS, considerando que estou fazendo sobre uma saga específica.

Os dados foram todos armazenados persistidos na camada RAW e respeitando as condições impostas de PATH. Segue evidência:

- [ARMAZENAMENTO NO BUCKET/JSONS](/sprint%207/evidências/evidencia_armazenamento.png)

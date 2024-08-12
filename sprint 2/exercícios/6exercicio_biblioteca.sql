SELECT
    a.codautor,
    a.nome,
    COUNT(l.cod) AS quantidade_publicacoes
FROM
    autor a
JOIN
    livro l ON a.codautor = l.autor
GROUP BY
    a.codautor, a.nome
ORDER BY
    quantidade_publicacoes DESC
LIMIT 1;
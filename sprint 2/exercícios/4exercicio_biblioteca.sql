SELECT
    a.codautor,
    a.nome,
    a.nascimento,
    COUNT(l.cod) AS quantidade
FROM
    autor a
LEFT JOIN
    livro l ON a.codautor = l.autor
GROUP BY
    a.codautor, a.nome, a.nascimento
ORDER BY
    a.nome ASC;
SELECT
    a.nome
FROM
    autor a
LEFT JOIN
    livro l ON a.codautor = l.autor
WHERE
    l.autor IS NULL
ORDER BY
    a.nome ASC;
SELECT
    COUNT(l.cod) AS quantidade,
    e.nome,
    en.estado,
    en.cidade
FROM
    livro l
JOIN
    editora e ON l.editora = e.codeditora
JOIN
    endereco en ON e.endereco = en.codendereco
GROUP BY
    e.codeditora, e.nome, en.estado, en.cidade
ORDER BY
    quantidade DESC
LIMIT 5;
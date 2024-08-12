SELECT
    cdpro,
    nmpro
FROM
    tbvendas
WHERE
    status = 'Concluído'
    AND dtven BETWEEN '2014-02-03' AND '2018-02-02'
GROUP BY
    cdpro, nmpro
ORDER BY
    SUM(qtd) DESC
LIMIT 1;
SELECT
    cdcli,
    nmcli,
    ROUND(SUM(qtd * vrunt), 2) AS gasto
FROM
    tbvendas
WHERE
    status = 'Concluído'
GROUP BY
    cdcli, nmcli
ORDER BY
    gasto DESC
LIMIT 1;

SELECT
    v.cdvdd,
    v.nmvdd
FROM
    tbvendedor v
JOIN
    tbvendas ve ON v.cdvdd = ve.cdvdd
WHERE
    ve.status = 'Concluído'
GROUP BY
    v.cdvdd, v.nmvdd
ORDER BY
    COUNT(ve.cdven) DESC
LIMIT 1;

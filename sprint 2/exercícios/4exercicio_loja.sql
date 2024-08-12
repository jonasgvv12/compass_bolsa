WITH VendasPorVendedor AS (
    SELECT
        v.cdvdd,
        ROUND(SUM(v.qtd * v.vrunt), 2) AS valor_total_vendas
    FROM
        tbvendas v
    WHERE
        v.status = 'Concluído'
    GROUP BY
        v.cdvdd
    HAVING
        valor_total_vendas > 0
),
VendedorMenorValor AS (
    SELECT
        cdvdd
    FROM
        VendasPorVendedor
    ORDER BY
        valor_total_vendas ASC
    LIMIT 1
)
SELECT
    d.cddep,
    d.nmdep,
    d.dtnasc,
    ROUND(SUM(v.qtd * v.vrunt), 2) AS valor_total_vendas
FROM
    tbdependente d
JOIN
    tbvendas v ON d.cdvdd = v.cdvdd
JOIN
    VendedorMenorValor vmv ON v.cdvdd = vmv.cdvdd
WHERE
    v.status = 'Concluído'
GROUP BY
    d.cddep, d.nmdep, d.dtnasc;

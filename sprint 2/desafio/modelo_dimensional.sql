CREATE VIEW LocacaoCliente AS
SELECT 
    C.idCliente AS ClienteID,
    C.nomeCliente AS NomeCliente,
    COUNT(L.idLocacao) AS TotalLocacoes,
    SUM(L.vlrDiaria * L.qtdDiaria) AS ValorTotalLocacoes
FROM Locacao L
JOIN Cliente_cons C ON L.idCliente = C.idCliente
GROUP BY C.idCliente, C.nomeCliente;

SELECT *
FROM LocacaoCliente

CREATE VIEW LocacaoCarro AS
SELECT 
    D.idCarro AS CarroID,
    D.marcaCarro AS MarcaCarro,
    D.modeloCarro AS ModeloCarro,
    D.anoCarro AS AnoCarro,
    COUNT(L.idLocacao) AS TotalLocacoes,
    SUM(L.vlrDiaria * L.qtdDiaria) AS ValorTotalLocacoes
FROM Locacao L
JOIN Info_carro D ON L.idCarro = D.idCarro
GROUP BY D.idCarro, D.marcaCarro, D.modeloCarro, D.anoCarro;

SELECT *
FROM LocacaoCarro

CREATE VIEW LocacaoVendedor AS
SELECT 
    V.idVendedor AS VendedorID,
    V.nomeVendedor AS NomeVendedor,
    V.estadoVendedor AS EstadoVendedor,
    COUNT(L.idLocacao) AS TotalLocacoes,
    SUM(L.vlrDiaria * L.qtdDiaria) AS ValorTotalLocacoes
FROM Locacao L
JOIN Info_Vendedor V ON L.idVendedor = V.idVendedor
GROUP BY V.idVendedor, V.nomeVendedor, V.estadoVendedor;

SELECT *
FROM locacaoVendedor

CREATE VIEW LocacaoGeral AS
SELECT 
    L.idLocacao AS LocacaoID,
    C.nomeCliente AS NomeCliente,
    C.cidadeCliente AS CidadeCliente,
    C.paisCliente AS PaisCliente,
    C.idCliente AS ClienteID,
    D.marcaCarro AS MarcaCarro,
    D.modeloCarro AS ModeloCarro,
    D.anoCarro AS AnoCarro,
    F.tipoCombustivel AS TipoCombustivel,
    L.dataLocacao AS DataLocacao,
    L.horaLocacao AS HoraLocacao,
    L.qtdDiaria AS QuantidadeDiarias,
    L.vlrDiaria AS ValorDiaria,
    L.dataEntrega AS DataEntrega,
    L.horaEntrega AS HoraEntrega,
    V.nomeVendedor AS NomeVendedor,
    V.estadoVendedor AS EstadoVendedor
FROM Locacao L
JOIN Cliente_cons C ON L.idCliente = C.idCliente
JOIN Info_carro D ON L.idCarro = D.idCarro
JOIN Info_Combustivel F ON D.idCombustivel = F.idCombustivel
JOIN Info_Vendedor V ON L.idVendedor = V.idVendedor;

SELECT *
FROM locacaogeral
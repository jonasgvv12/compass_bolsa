-- normalização - fiz a divisão e a normalização das tabelas identificando uma chave primária e atributos que pertencam a aquela e somente a aquela tabela
-- após isso, verifiquei se não haviam atributos multi-valorados que necessitavam ser divididos em uma tabela própria 
-- verifiquei a depêndencia dos atributos, para caso houvesse algum que dependesse não apenas da chave primária



CREATE TABLE Cliente_cons(
idCliente int PRIMARY KEY,
nomeCliente varchar(100),
cidadeCliente varchar(40),
paisCliente varchar(40)
);

CREATE TABLE Info_carro(
idCarro int PRIMARY KEY, 
kmCarro int, 
classiCarro varchar(50),
marcaCarro varchar(80),
modeloCarro varchar(80),
anoCarro int, 
idCombustivel int,
FOREIGN KEY (idCombustivel) REFERENCES Info_Combustivel(idCombustivel)
);

CREATE TABLE Info_Combustivel(
idCombustivel int PRIMARY KEY,
tipoCombustivel varchar(20)
);

CREATE TABLE Info_Vendedor(
idVendedor int PRIMARY KEY,
nomeVendedor varchar(15),
sexoVendedor smallint,
estadoVendedor varchar(40)
);

CREATE TABLE Locacao(
idLocacao int PRIMARY KEY,
idCliente int,
idCarro int,
dataLocacao datetime,
horaLocacao time, 
qtdDiaria int,
vlrDiaria decimal(18,2),
dataEntrega date,
horaEntrega time, 
idVendedor int,
FOREIGN KEY (idCliente) REFERENCES Cliente_cons(idCliente),
FOREIGN KEY (idCarro) REFERENCES Info_carro(idCarro),
FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor)
);

-- documentar a fim de identificar qual a tabela inicial que gerou todas as outras
ALTER TABLE tb_locacao RENAME TO tb_locacao_base;

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
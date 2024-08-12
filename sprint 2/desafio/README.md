### Etapas

**Normalização e código fonte:**[Normalização](desafio_sprint2_jonas.sql)

**Modelo Entidade Relacionamento:**[Modelo ER](modeloER_SPRINT2.png)

**Modelo Dimensional:**[Modelo Dimensional](modelo_dimensional.sql)

## **Normalização**

Para a normalização, as tabelas foram abordadas até a 3NF.
 
Primeiro, fiz a divisão das tabelas, totalizando 5. (Cliente_cons, Info_carro, Info_Combustivel, Info_Vendedor e Locacao)
Após isso, verifiquei se as tabelas ja estavam na 1NF, para que as colunas tivessem nomes únicos e valores do mesmo tipo, além de armazenarem valores únicos.
Depois, fiz a verificação para a 2NF, para que os atributos dependessem única e exclusivamente da chave primária da tabela, e nada além.
Finalizando, fiz a verificação das dependências transitivas para a 3NF, checando caso houvesse atributos que dependessem de outro atributo que depende da chave primária.
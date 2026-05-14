-- ==========================================================
-- EXERCÍCIO 04 - CRIAÇÃO DAS TABELAS (DDL)
-- ==========================================================

CREATE TABLE Laboratorio (
  id int(11) NOT NULL AUTO_INCREMENT,
  cnpj varchar(20) NOT NULL,
  nomeFantasia varchar(60) NOT NULL,
  idAntigo int(11),
  PRIMARY KEY (id)
);

CREATE TABLE Representante (
  idRepr int(11) NOT NULL AUTO_INCREMENT,
  nome varchar(30) NOT NULL,
  cpf char(14) NOT NULL,
  regiaoAtuacao varchar(20) DEFAULT NULL,
  telefone varchar(15) DEFAULT NULL,
  PRIMARY KEY (idRepr),
  UNIQUE KEY (cpf)
);

CREATE TABLE Farmacia (
  idFarmacia int(11) NOT NULL AUTO_INCREMENT,
  cnpj char(20) NOT NULL,
  responsavelTecnico varchar(30) DEFAULT NULL,
  tipo varchar(20) DEFAULT NULL,
  condicoesEspeciais varchar(60) DEFAULT NULL,
  PRIMARY KEY (idFarmacia),
  UNIQUE KEY (cnpj)
);

CREATE TABLE PrincipioAtivo (
  idPrincipio int(11) NOT NULL AUTO_INCREMENT,
  nomeSubstancia varchar(40) NOT NULL,
  restricoes varchar(30) Default NULL,
  PRIMARY KEY (idPrincipio)
);

CREATE TABLE Medicamento (
  idProduto int(11) NOT NULL AUTO_INCREMENT,
  idLab int(11) NOT NULL,
  descricao varchar(60) NOT NULL,
  marca varchar(20) NOT NULL,
  linhaMedicamento varchar(30) NOT NULL,
  valor decimal(10,2) DEFAULT NULL,
  formaFarmaceutica varchar(30) NOT NULL,
  PRIMARY KEY (idProduto),1
  FOREIGN KEY (idLab) REFERENCES Laboratorio(id)
);

CREATE TABLE Teste (
  TESTE
)
CREATE TABLE Composicao (
  idComposicao int(11) NOT NULL AUTO_INCREMENT,
  idProduto int(11) NOT NULL,
  idPrincipio int(11) NOT NULL,
  concentracao varchar(20),
  PRIMARY KEY (idComposicao),
  FOREIGN KEY (idProduto) REFERENCES Medicamento(idProduto),
  FOREIGN KEY (idPrincipio) REFERENCES PrincipioAtivo(idPrincipio)
);

CREATE TABLE Pedido (
  idPedido int(11) NOT NULL AUTO_INCREMENT,
  idFarmacia int(11) NOT NULL,
  idRepresentante int(11) NOT NULL,
  dataEmissao date DEFAULT NULL,
  valorTotal decimal(10,2) NOT NULL,
  PRIMARY KEY (idPedido),
  FOREIGN KEY (idFarmacia) REFERENCES Farmacia(idFarmacia),
  FOREIGN KEY (idRepresentante) REFERENCES Representante(idRepr)
);

CREATE TABLE ItensPedido (
  idItensPedido int(11) NOT NULL AUTO_INCREMENT,
  idPedido int(11) NOT NULL,
  idProduto int(11) NOT NULL,
  quantidade int(11) DEFAULT NULL,
  valorUnitario decimal(10,2) NOT NULL,
  PRIMARY KEY (idItensPedido),
  FOREIGN KEY (idPedido) REFERENCES Pedido(idPedido),
  FOREIGN KEY (idProduto) REFERENCES Medicamento(idProduto)
);

-- ==========================================================
-- EXERCÍCIO 05 - POVOAR TABELAS (INSERTS)
-- ==========================================================

INSERT INTO Laboratorio (cnpj, nomeFantasia, idAntigo) VALUES
('11.111.111/0001-01', 'Pfizer', 1001),
('22.222.222/0001-02', 'Medley', 1002),
('33.333.333/0001-03', 'EMS', 1003),
('44.444.444/0001-04', 'Eurofarma', 2004),
('55.555.555/0001-05', 'Neo Química', 2040),
('66.666.666/0001-06', 'Bayer', 3005),
('77.777.777/0001-07', 'Novartis', 3010),
('88.888.888/0001-08', 'Sanofi', NULL),
('99.999.999/0001-09', 'Aché', 4001),
('10.101.010/0001-10', 'Teuto', 4020);

INSERT INTO Representante (nome, cpf, regiaoAtuacao, telefone) VALUES
('João Silva', '111.111.111-11', 'Sul', '(41) 99999-0001'),
('Maria Oliveira', '222.222.222-22', 'Sudeste', '(11) 99999-0002'),
('Carlos Souza', '333.333.333-33', 'Norte', '(92) 99999-0003'),
('Ana Pereira', '444.444.444-44', 'Nordeste', '(71) 99999-0004'),
('Roberto Santos', '555.555.555-55', 'Centro-Oeste', '(61) 99999-0005'),
('Fernanda Lima', '666.666.666-66', 'Sudeste', '(21) 99999-0006'),
('Paulo Mendes', '777.777.777-77', 'Sul', '(48) 99999-0007'),
('Juliana Costa', '888.888.888-88', 'Nordeste', '(81) 99999-0008'),
('Marcos Rocha', '999.999.999-99', 'Sudeste', '(31) 99999-0009'),
('Luciana Alves', '101.010.101-01', 'Centro-Oeste', '(62) 99999-0010');

INSERT INTO Farmacia (cnpj, responsavelTecnico, tipo, condicoesEspeciais) VALUES
('12.345.678/0001-01', 'Dr. Pedro', 'Convencional', 'Prazo 30 dias'),
('23.456.789/0001-02', 'Dra. Carla', 'Manipulação', 'À vista 5% desc'),
('34.567.890/0001-03', 'Dr. Lucas', 'Convencional', 'Boleto 60 dias'),
('45.678.901/0001-04', 'Dra. Amanda', 'Convencional', 'Sem desconto'),
('56.789.012/0001-05', 'Dr. Bruno', 'Manipulação', 'Entrega Grátis'),
('67.890.123/0001-06', 'Dra. Vanessa', 'Convencional', 'Prazo 45 dias'),
('78.901.234/0001-07', 'Dr. Ricardo', 'Convencional', 'Bonificação 10%'),
('89.012.345/0001-08', 'Dra. Bianca', 'Manipulação', 'À vista'),
('90.123.456/0001-09', 'Dr. Felipe', 'Convencional', 'Boleto 30/60'),
('01.234.567/0001-10', 'Dra. Camila', 'Manipulação', 'Desconto Fidelidade');

INSERT INTO PrincipioAtivo (nomeSubstancia, restricoes) VALUES
('Paracetamol', 'Venda Livre'),
('Dipirona Sódica', 'Venda Livre'),
('Amoxicilina', 'Retenção de Receita'),
('Ibuprofeno', 'Uso Adulto'),
('Loratadina', 'Venda Livre'),
('Clonazepam', 'Receita Azul'),
('Omeprazol', 'Jejum obrigatório'),
('Simeticona', 'Venda Livre'),
('Azitromicina', 'Retenção de Receita'),
('Acido Ascorbico', 'Suplemento');

INSERT INTO Medicamento (idLab, descricao, marca, linhaMedicamento, valor, formaFarmaceutica) VALUES
(1, 'Viagra 50mg', 'Viagra', 'Saúde Masculina', 50.00, 'Comprimido'),
(2, 'Dipirona 500mg', 'Genérico', 'Analgésico', 5.50, 'Gotas'),
(3, 'Amoxil 500mg', 'Amoxil', 'Antibiótico', 35.90, 'Cápsula'),
(4, 'Ibuprofeno 600mg', 'Advil', 'Anti-inflamatório', 12.00, 'Cápsula Gel'),
(5, 'Loratadina 10mg', 'Claritin', 'Antialérgico', 18.50, 'Comprimido'),
(6, 'Aspirina Prevent', 'Aspirina', 'Cardiológico', 9.90, 'Comprimido'),
(7, 'Ritalina 10mg', 'Ritalina', 'Psicotrópico', 45.00, 'Comprimido'),
(8, 'Novalgina 1g', 'Novalgina', 'Analgésico', 15.00, 'Efervescente'),
(9, 'Buscopan Composto', 'Buscopan', 'Antiespasmódico', 11.20, 'Drágea'),
(10, 'Cewin 500mg', 'Cewin', 'Vitamínico', 8.50, 'Gotas');

INSERT INTO Composicao (idProduto, idPrincipio, concentracao) VALUES
(2, 2, '500mg'),
(3, 3, '500mg'),
(4, 4, '600mg'),
(5, 5, '10mg'),
(8, 2, '1g'),
(10, 10, '500mg'),
(7, 6, '10mg'),
(9, 2, '250mg'),
(1, 1, '50mg'),
(6, 1, '100mg');

INSERT INTO Pedido (idFarmacia, idRepresentante, dataEmissao, valorTotal) VALUES
(1, 1, '2023-10-01', 500.00),
(2, 2, '2023-10-02', 1200.50),
(3, 1, '2023-10-03', 350.00),
(4, 3, '2023-10-04', 800.00),
(5, 4, '2023-10-05', 150.00),
(6, 2, '2023-10-06', 2000.00),
(7, 5, '2023-10-07', 450.00),
(8, 6, '2023-10-08', 3000.00),
(9, 7, '2023-10-09', 100.00),
(10, 8, '2023-10-10', 750.00);

INSERT INTO ItensPedido (idPedido, idProduto, quantidade, valorUnitario) VALUES
(1, 1, 10, 48.00), 
(1, 2, 20, 5.00),  
(2, 3, 5, 30.00),   
(2, 4, 10, 10.00),
(3, 5, 15, 15.00),
(4, 6, 50, 8.00),
(5, 7, 2, 45.00),
(6, 8, 100, 12.00),
(7, 9, 30, 10.00),
(8, 10, 20, 8.00);

-- ==========================================================
-- EXERCÍCIO 06 - ALTER TABLE (NOVAS COLUNAS)
-- ==========================================================

ALTER TABLE Laboratorio ADD COLUMN site varchar(100) DEFAULT NULL;
ALTER TABLE Laboratorio ADD COLUMN emailComercial varchar(80) DEFAULT NULL;

ALTER TABLE Farmacia ADD COLUMN bairro varchar(50) DEFAULT NULL;
ALTER TABLE Farmacia ADD COLUMN dataFundacao date DEFAULT NULL;

ALTER TABLE Medicamento ADD COLUMN codigoBarras varchar(20) DEFAULT NULL;
ALTER TABLE Medicamento ADD COLUMN temperaturaArmazenagem varchar(30) DEFAULT NULL;

ALTER TABLE Representante ADD COLUMN rg varchar(12) DEFAULT NULL;
ALTER TABLE Pedido ADD COLUMN observacao varchar(100) Default NULL;

-- ==========================================================
-- EXERCÍCIO 07 - SELECTS
-- ==========================================================

-- 7.A (Simples)
SELECT * FROM Representante;

-- 7.B (Com Where)
SELECT * FROM Medicamento WHERE valor > 20.00;

-- 7.C (Agregação)
SELECT 
    COUNT(*) AS Qtd_Medicamentos, 
    AVG(valor) AS Media_Preco 
FROM Medicamento;

-- 7.D (Junção 2 tabelas)
SELECT 
    m.descricao AS Medicamento, 
    p.nomeSubstancia AS Principio_Ativo,
    c.concentracao
FROM Medicamento m
INNER JOIN Composicao c ON m.idProduto = c.idProduto
INNER JOIN PrincipioAtivo p ON c.idPrincipio = p.idPrincipio;

-- 7.E (Junção 3 tabelas)
SELECT 
    p.idPedido,
    p.dataEmissao,
    f.responsavelTecnico AS Farmacia_Resp,
    r.nome AS Representante,
    p.valorTotal
FROM Pedido AS p
INNER JOIN Farmacia AS f ON p.idFarmacia = f.idFarmacia
INNER JOIN Representante AS r ON p.idRepresentante = r.idRepr;

-- ==========================================================
-- EXERCÍCIO 08 - UPDATE (ATUALIZAR 3 REGISTROS)
-- ==========================================================

UPDATE Laboratorio 
SET emailComercial = 'contato@pfizer.com.br', site = 'www.pfizer.com.br' 
WHERE id = 1;

UPDATE Farmacia 
SET bairro = 'Centro', responsavelTecnico = 'Dr. Lucas Martins' 
WHERE idFarmacia = 3;

UPDATE Medicamento 
SET valor = 22.90, temperaturaArmazenagem = '15°C a 30°C' 
WHERE idProduto = 5;

-- ==========================================================
-- EXERCÍCIO 09 - DELETE (APAGAR EM 3 TABELAS)
-- ==========================================================

DELETE FROM ItensPedido WHERE idItensPedido = 1;

INSERT INTO Representante (nome, cpf, regiaoAtuacao, telefone, rg) 
VALUES ('Para Deletar', '000.000.000-00', 'X', '0000', '000');
DELETE FROM Representante WHERE cpf = '000.000.000-00';

DELETE FROM Composicao WHERE idProduto = 1;

-- ==========================================================
-- EXERCÍCIO 10 - DROP TABLE (EXCLUIR TABELA)
-- ==========================================================

DROP TABLE Composicao;
DROP TABLE PrincipioAtivo;
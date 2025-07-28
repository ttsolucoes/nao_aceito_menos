CREATE TABLE jogadores (
    id_jogador INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha_hash VARCHAR(255) NOT NULL,
    data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    ultimo_login DATETIME,
    jornada_escolhida ENUM('jornada1', 'jornada2', 'jornada3', 'jornada4')
);

CREATE TABLE progresso_jogador (
    id_progresso INT PRIMARY KEY AUTO_INCREMENT,
    id_jogador INT NOT NULL,
    capitulo_atual INT NOT NULL DEFAULT 1,
    estado_alma ENUM('ceu', 'purgatorio', 'inferno', 'em_jornada') DEFAULT 'em_jornada',
    pontos_fe INT NOT NULL DEFAULT 0,
    pontos_esperanca INT NOT NULL DEFAULT 0,
    pontos_caridade INT NOT NULL DEFAULT 0,
    decisoes_chave JSON,
    data_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (id_jogador) REFERENCES jogadores(id_jogador)
);

CREATE TABLE capitulos (
    id_capitulo INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(100) NOT NULL,
    descricao TEXT,
    ordem INT NOT NULL UNIQUE,
    jornada ENUM('comum', 'jornada1', 'jornada2', 'jornada3', 'jornada4') DEFAULT 'comum'
);

CREATE TABLE decisoes (
    id_decisao INT PRIMARY KEY AUTO_INCREMENT,
    id_capitulo INT NOT NULL,
    texto_decisao TEXT NOT NULL,
    efeito_fe INT DEFAULT 0,
    efeito_esperanca INT DEFAULT 0,
    efeito_caridade INT DEFAULT 0,
    FOREIGN KEY (id_capitulo) REFERENCES capitulos(id_capitulo)
);

CREATE TABLE ramificacoes (
    id_ramificacao INT PRIMARY KEY AUTO_INCREMENT,
    id_decisao_anterior INT NOT NULL,
    id_capitulo_destino INT,
    condicao TEXT,
    FOREIGN KEY (id_decisao_anterior) REFERENCES decisoes(id_decisao),
    FOREIGN KEY (id_capitulo_destino) REFERENCES capitulos(id_capitulo)
);

CREATE TABLE estados_alma (
    id_estado INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL UNIQUE,
    descricao TEXT NOT NULL,
    min_fe INT NOT NULL,
    min_esperanca INT NOT NULL,
    min_caridade INT NOT NULL,
    resultado_final ENUM('ceu', 'purgatorio', 'inferno') NOT NULL
);

CREATE TABLE mudancas_estado (
    id_mudanca INT PRIMARY KEY AUTO_INCREMENT,
    id_jogador INT NOT NULL,
    id_estado_anterior INT,
    id_estado_novo INT NOT NULL,
    id_decisao INT,
    data_mudanca DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_jogador) REFERENCES jogadores(id_jogador),
    FOREIGN KEY (id_estado_anterior) REFERENCES estados_alma(id_estado),
    FOREIGN KEY (id_estado_novo) REFERENCES estados_alma(id_estado),
    FOREIGN KEY (id_decisao) REFERENCES decisoes(id_decisao)
);

CREATE TABLE textos_capitulos (
    id_texto INT PRIMARY KEY AUTO_INCREMENT,
    id_capitulo INT NOT NULL,
    ordem_texto INT NOT NULL,
    tipo ENUM('narrativa', 'dialogo', 'descricao', 'evento') NOT NULL,
    conteudo TEXT NOT NULL,
    personagem VARCHAR(50),
    FOREIGN KEY (id_capitulo) REFERENCES capitulos(id_capitulo),
    UNIQUE KEY (id_capitulo, ordem_texto)
);

CREATE TABLE cenas (
    id_cena INT PRIMARY KEY AUTO_INCREMENT,
    id_capitulo INT NOT NULL,
    titulo VARCHAR(100) NOT NULL,
    background VARCHAR(255),
    musica VARCHAR(255),
    FOREIGN KEY (id_capitulo) REFERENCES capitulos(id_capitulo)
);

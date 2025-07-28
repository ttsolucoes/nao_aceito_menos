# Não Aceito Menos: A Jornada da Alma Peregrina

## Visão Geral do Projeto

"Não Aceito Menos" é um jogo de RPG narrativo com temática católica, onde o jogador assume o papel de uma alma peregrina em sua jornada terrena. O objetivo é guiar a alma através de escolhas morais e espirituais que afetam seu estado e o mundo ao redor, culminando em um dos três destinos eternos: Céu, Purgatório ou Inferno. O jogo é desenvolvido em colaboração com um movimento de evangelização catequética, utilizando o conhecimento teológico e o Catecismo da Igreja Católica como fontes principais.

A ideia central é que "Se Deus me criou em completude, então quem sou eu pra aceitar menos que o céu?".

## Estrutura do Projeto

A arquitetura do projeto `mmorpg_catolico` é organizada para separar as responsabilidades entre a lógica de backend (API), a interface do usuário (App), configurações, dados e utilitários.

```
├───api
│   ├───modules
│   └───routes
├───app
│   ├───routes
│   ├───static
│   │   ├───css
│   │   │   ├───components
│   │   │   └───pages
│   │   │       └───public
│   │   ├───images
│   │   │   └───home
│   │   ├───js
│   │   │   └───modules
│   │   │       └───public
│   │   ├───json
│   │   └───midias
│   │       ├───capitulo1
│   │       ├───capitulo2amor
│   │       ├───capitulo2medo
│   │       ├───capitulo3estocolmo
│   │       ├───capitulo3roma
│   │       ├───capitulo3sao_paulo
│   │       ├───capitulo3sevilha
│   │       ├───ceu
│   │       ├───inferno
│   │       ├───julgamento-ceu
│   │       ├───julgamento-inferno
│   │       ├───julgamento-purgatorio
│   │       ├───perdicao
│   │       └───purgatorio
│   ├───templates
│   │   ├───components
│   │   ├───macros
│   │   └───pages
│   │       ├───private
│   │       └───public
│   └───utils
├───config
│   ├───auth
│   ├───database
│   │   ├───config
│   │   └───queries
│   └───models
├───data
│   ├───base
│   ├───entrada
│   └───saida
├───logs
├───temp
├───tests
└───utils
    └───modules
        └───usuarios
```

## Como o Jogo Funciona (Fluxo Central)

O coração da narrativa e da progressão do jogo reside no dicionário `jogo_jornada`, localizado em `app/utils/midia_jogo`. Este dicionário centraliza a definição de todas as cenas, diálogos, escolhas, descrições de imagem e áudio para cada capítulo e jornada.

### Fluxo de Jogo Simplificado:

1.  **Capítulo 1 (Envio):**
    *   A alma é apresentada a Deus em uma câmara celeste.
    *   Deus narra a história da salvação e a missão da alma.
    *   **Escolha:** A alma decide aceitar a missão "com amor" ou "com medo", ou "recusar".
    *   **Consequência da Recusa:** A alma entra em um estado de "bolha de fogo em um vácuo", exigindo o reinício do jogo.
2.  **Capítulo 2 (Escolha da Jornada):**
    *   **Capítulo 2.1 (Origem: Fé + Amor):** Deus apresenta as Jornadas 1 (Sevilha) e 3 (Estocolmo). O jogador escolhe uma delas.
    *   **Capítulo 2.2 (Origem: Fé + Medo):** Deus apresenta as Jornadas 2 (São Paulo) e 4 (Roma). O jogador escolhe uma delas.
3.  **Capítulo 3 (Nascimento e Infância):**
    *   A alma encarna na cidade e contexto escolhidos.
    *   São apresentados os primeiros desafios e a introdução ao Dom da Sabedoria.
    *   A primeira escolha consciente da alma é feita, impactando seu estado espiritual.
4.  **Capítulos Posteriores:** (A serem desenvolvidos) Seguirão a progressão da vida da alma (adolescência, juventude, vida adulta, velhice), com novos desafios, Dons do Espírito Santo em foco e escolhas morais.
5.  **Capítulo Final (Morte e Juízo):**
    *   A morte da alma encarnada.
    *   O Juízo Particular diante de Cristo, onde todas as escolhas são reveladas.
    *   O destino final da alma: Céu, Purgatório ou Inferno, determinado pelo acúmulo das decisões ao longo da jornada.

## Desenvolvimento e Colaboração

### Pré-requisitos

- Navegador
- Python

### Instalação

1.  Clone o repositório:

https://github.com/ttsolucoes/nao_aceito_menos.git

2. Baixe dependêcias:

pip install -r requirements.txt

3. Rode:

python run.py

## Contribuição
Contribuições são muito bem-vindas! Se você deseja colaborar, por favor:

- Faça um fork do repositório.
- Crie uma nova branch para sua feature (git checkout -b feature/sua-feature).
- Faça suas alterações e commit (git commit -m 'feat: Adiciona nova funcionalidade X').
- Envie para sua branch (git push origin feature/sua-feature).
- Abra um Pull Request.

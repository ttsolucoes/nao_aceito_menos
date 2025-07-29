document.addEventListener("DOMContentLoaded", function () {
    let indiceAtual = 0;
    const container = document.getElementById("jogo-container");
    const audioFundo = document.getElementById("audio-fundo");
    let historicoEscolhas = [];
    let faixaVisivel = true;

    function tocarNarracao(cena) {
        const existente = document.getElementById("audio-narracao");
        if (existente) existente.remove();

        const audio = document.createElement("audio");
        audio.id = "audio-narracao";
        audio.autoplay = true;
        audio.innerHTML = `<source src="/static/midias/${pasta}/${cena.audio}.mp3" type="audio/mp3">`;
        container.appendChild(audio);

        audio.addEventListener("ended", () => {
            const botaoProximo = document.getElementById("botao-proximo");
            if (botaoProximo) botaoProximo.classList.add("pulsando");
        });
    }

    function atualizarAudioFundo(novoAudio) {
        audioFundo.pause();
        audioFundo.innerHTML = `
            <source src="/static/midias/${pasta}/${novoAudio}.mp3" type="audio/mp3">
        `;
        audioFundo.load();
        audioFundo.play();
    }

    function mostrarCena(indice) {
        const cena = cenas[indice];
        if (!cena) return;

        let html = `
            <img class="imagem-fundo" src="/static/midias/${pasta}/${cena.imagem_principal}.png">
            <div class="faixa-dialogo">
                ${cena.personagem ? `<div class="personagem">${cena.personagem}</div>` : ''}
                <div class="texto">${cena.texto || ''}</div>
            </div>
        `;

        if (cena.opcoes) {
            html += `
                <div class="bloco-opcoes">
                    ${cena.opcoes.map(op => `<button class="botao-opcao">${op}</button>`).join('')}
                </div>
            `;
        } else if (cena.template === "dialogo") {
            html += `<button id="botao-proximo" title="continuar jornada"> >> </button>`;
        }

        if (cena.template === "finalizacao") {
            html += `
                <div class="bloco-score">
                    <h2>Sua Jornada</h2>
                    <ul>
                        ${historicoEscolhas.map(item => `<li><strong>${item.capitulo}</strong>: ${item.escolha}</li>`).join('')}
                    </ul>
                    <div class="acoes-finais">
                        <button id="botao-reiniciar">Reiniciar Jornada</button>
                        <button id="botao-sair">Sair</button>
                    </div>
                </div>
            `;
        }

        container.innerHTML = html;
        tocarNarracao(cena);

        // Aplicar visibilidade da faixa de diálogo (manter o estado)
        const faixa = document.querySelector(".faixa-dialogo");
        if (faixa) {
            faixa.style.display = faixaVisivel ? "block" : "none";
        }

        if (cena.opcoes) {
            document.querySelectorAll(".botao-opcao").forEach(botao => {
                botao.addEventListener("click", () => {
                    const escolha = botao.textContent.trim();
                    historicoEscolhas.push({ capitulo: pasta, escolha });

                    fetch("/escolher", {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({ escolha, capitulo: pasta })
                    })
                    .then(res => res.json())
                    .then(data => {
                        if (data.capitulo && data.dados && data.dados.cenas) {
                            pasta = data.capitulo;
                            cenas = data.dados.cenas;
                            indiceAtual = 0;
                            mostrarCena(indiceAtual);

                            if (data.dados.audio_fundo) {
                                atualizarAudioFundo(data.dados.audio_fundo);
                            }
                        }
                    })
                    .catch(err => console.error("Erro ao enviar escolha:", err));
                });
            });
        } else if (cena.template === "dialogo") {
            const botaoProximo = document.getElementById("botao-proximo");
            if (botaoProximo) {
                botaoProximo.classList.remove("pulsando");
                botaoProximo.addEventListener("click", (e) => {
                    e.stopPropagation(); // impede conflito com clique fora da faixa
                    indiceAtual++;
                    mostrarCena(indiceAtual);
                });
            }
        } else if (cena.template === "finalizacao") {
            const reiniciar = document.getElementById("botao-reiniciar");
            const sair = document.getElementById("botao-sair");

            if (reiniciar) {
                reiniciar.addEventListener("click", () => {
                    indiceAtual = 0;
                    historicoEscolhas = [];
                    location.reload();
                });
            }

            if (sair) {
                sair.addEventListener("click", () => {
                    window.location.href = "/index";
                });
            }
        }
    }

    mostrarCena(indiceAtual);

    // Clique fora da faixa para alternar visibilidade
    document.addEventListener("click", function toggleFaixa(e) {
        const faixa = document.querySelector(".faixa-dialogo");
        const opcoes = document.querySelector(".bloco-opcoes");
        const botao = document.getElementById("botao-proximo");

        if (!faixa || faixa.contains(e.target) || (opcoes && opcoes.contains(e.target)) || (botao && botao.contains(e.target))) return;

        faixaVisivel = faixa.style.display === "none";
        faixa.style.display = faixaVisivel ? "block" : "none";
    });

    // Avançar com tecla espaço
    document.addEventListener("keydown", function (e) {
        const cena = cenas[indiceAtual];
        if (e.code === "Space" && cena.template === "dialogo") {
            e.preventDefault();
            indiceAtual++;
            mostrarCena(indiceAtual);
        }
    });
});

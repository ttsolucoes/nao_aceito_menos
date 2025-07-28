from app import app
from flask import request, render_template, jsonify
from config import secret_key
from app.utils import jogo_jornada

usuarios_temp = {}
app.secret_key = secret_key

@app.route("/jogo")
def jogo():
    capitulo = request.args.get('capitulo', default='capitulo1', type=str)
    dados_capitulo = jogo_jornada.get(capitulo)

    if not dados_capitulo:
        dados_capitulo = jogo_jornada.get('ceu')  # capítulo final, se aplicável

    return render_template(
        'pages/public/jogos.html',
        capitulo=capitulo,
        audio_fundo=dados_capitulo.get('audio_fundo', ''),
        cenas=dados_capitulo['cenas']
    )

@app.route("/escolher", methods=["POST"])
def escolher():
    escolha = request.json.get("escolha")
    capitulo = request.json.get("capitulo")

    roteamento = jogo_jornada[capitulo].get("roteamento", {})
    proximo = roteamento.get(escolha, 'ceu')
    dados = jogo_jornada.get(proximo, jogo_jornada['ceu'])

    return jsonify({
        'capitulo': proximo,
        'dados': {
            'audio_fundo': dados.get('audio_fundo', ''),
            'cenas': dados.get('cenas', [])
        }
    })

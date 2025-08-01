jogo_jornada = {
    'capitulo1': {
        'audio_fundo': 'fundo_capitulo1',
        'cenas': [
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Eu Sou. Antes de tudo o que existe, Eu Sou. Do Meu Amor, do Meu Verbo, do Meu Espírito, Eu criei tudo do nada. Contemplei a vastidão do universo, as galáxias girando em danças cósmicas, os sóis ardentes e os planetas em sua órbita perfeita. E então, criei a vida, em suas formas mais simples e complexas, até chegar à sua espécie. Eu os criei à Minha imagem e semelhança, com a capacidade de amar, de conhecer, de escolher. Entreguei a vocês um jardim, um paraíso de comunhão, onde a vida era plena e a morte não existia. Tudo era dado, tudo era graça.',
                'audio': 'narracao1_capitulo1',
                'imagem_principal': 'imagem_deus'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Mas sua espécie quis mais. Quis ser como Eu, sem Mim. Escolheu a sombra em vez da luz, a desobediência em vez da confiança. E assim, a harmonia se quebrou, e a morte entrou no mundo. A beleza que Eu havia plantado foi manchada, e a comunhão, ferida.',
                'audio': 'narracao2_capitulo1',
                'imagem_principal': 'alma_peregrina'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Mesmo assim, Meu Amor não se apagou. Eu os chamei de volta, uma e outra vez. Enviei patriarcas, homens de fé que Me buscaram em meio à escuridão. Enviei profetas, vozes que clamavam no deserto, anunciando Minha vontade e Minha misericórdia. Eu lhes dei leis, alianças, promessas. Mas, por mais que Eu estendesse Minha mão, a humanidade, em sua liberdade, muitas vezes Me virou as costas, escolhendo seus próprios caminhos, suas próprias idolatrias, suas próprias feridas.',
                'audio': 'narracao3_capitulo1',
                'imagem_principal': 'profetas_patriarcas'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Então, em um ato de Amor que transcende toda compreensão, Eu enviei Meu Filho Unigênito. Ele, que é a Minha própria Palavra, Minha própria Luz, veio ao mundo que Eu criei, assumiu a sua carne, viveu entre vocês, ensinou o Caminho, a Verdade e a Vida. Ele curou, perdoou, amou sem medida. Ele se entregou por vocês, para que pudessem ser reconciliados Comigo, para que a comunhão fosse restaurada. Mas, em sua cegueira e medo, a humanidade O condenou e O matou, pregando Ele em uma cruz.',
                'audio': 'narracao4_capitulo1',
                'imagem_principal': 'jesus_cristo'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Mesmo diante de tal rejeição, Meu Amor não diminuiu. Pelo contrário, daquela cruz brotou a salvação, e Meu Filho ressuscitou, vencendo a morte e abrindo as portas do Céu. E Ele enviou Meu Espírito, o Espírito Santo, para habitar em vocês, para ser a força que os guia, a luz que os ilumina, o fogo que os purifica.',
                'audio': 'narracao5_capitulo1',
                'imagem_principal': 'espirito_santo_paraclito'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Agora, Eu envio você. Você, alma, que está diante de Mim, em Minha Presença. Você já está no Céu, em Minha glória, neste momento eterno. Mas Eu o envio a um mundo que ainda clama por redenção, um mundo onde Minha Luz precisa ser levada, onde o Amor precisa ser vivido. Você carregará em si a centelha do Meu Espírito, a memória de sua origem divina.',
                'audio': 'narracao6_capitulo1',
                'imagem_principal': 'alma_peregrina'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Sua missão será peregrinar, aprender, cair e levantar, até reencontrar o sentido original: o Céu. Se você viver sua vida em Mim, buscando a verdade, praticando o amor, perdoando e se sacrificando, se você não aceitar menos que a dignidade que Eu lhe dei, então, ao final de sua jornada, você retornará a Mim, a este lugar de plenitude, para morar Comigo para sempre. Esta é a Minha promessa, a promessa da salvação, que se cumpre em cada alma que Me busca de coração.',
                'audio': 'narracao7_capitulo1',
                'imagem_principal': 'alma_peregrina'
            },
            {
                'template': 'escolha',
                'personagem': 'Deus',
                'texto': 'Você aceita esta missão?',
                'audio': 'narracao8_capitulo1',
                'imagem_principal': 'imagem_deus',
                'opcoes': ['Aceita a missão com amor', 'Aceita com medo', 'Recusa a missão']
            }
        ],
        'roteamento': {
            'Aceita a missão com amor': 'capitulo2amor',
            'Aceita com medo': 'capitulo2medo',
            'Recusa a missão': 'perdicao'
        }
    },
    'capitulo2amor': {
        'audio_fundo': 'fundo_capitulo2amor',  
        'cenas': [
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Olá, Alma que Me aceitou com amor, sua fé e esperança resplandecem em Minha Presença. Sua disposição é um bálsamo para o Meu Coração. Você escolheu o caminho da entrega, e por isso, grandes graças o aguardam, e grandes desafios também.',
                'imagem_principal': 'parte1_capitulo2amor',
                'audio': 'narracao1_capitulo2amor'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Contemple agora um dos caminhos que se abrem para você. Uma terra de fé antiga e vibrante, onde o catolicismo pulsa em cada rua, em cada celebração. Você nascerá em Sevilha, Espanha, em uma família abastada e profundamente religiosa. A fé será o ar que você respira, a tradição, seu berço. Seus recursos serão vastos, e a Igreja, uma presença constante.',
                'imagem_principal': 'parte2_capitulo2amor',
                'audio': 'narracao2_capitulo2amor'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Agora, veja outro caminho, igualmente preparado para sua missão. Uma terra de razão e progresso, onde a fé é uma voz sussurrante em meio ao clamor do mundo. Você nascerá em Estocolmo, Suécia, em uma família de intelectuais que buscam a verdade na ciência e na lógica, sem Me reconhecer. Sua busca por Mim será solitária, mas sua fé, se cultivada, brilhará como uma estrela no inverno.',
                'imagem_principal': 'parte3_capitulo2amor',
                'audio': 'narracao3_capitulo2amor'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Ambas as jornadas são caminhos de amor, preparados para que sua alma cresça e Me encontre. Em uma, a fé é um rio caudaloso, mas a tentação pode ser a complacência. Na outra, a fé é uma nascente oculta, mas a busca será pura e ardente. Sua missão é a mesma: não aceitar menos que o Céu. Agora, escolha o ambiente onde sua luz brilhará.',
                'imagem_principal': 'parte4_capitulo2amor',
                'audio': 'narracao4_capitulo2amor'
            },
            {
                'template': 'escolha',
                'personagem': 'Deus',
                'texto': 'E então, cara alma. Para onde deseja ir? Estocolmo ou Sevilha?',
                'imagem_principal': 'parte4_capitulo2amor',
                'audio': 'narracao5_capitulo2amor',
		        'opcoes': ['Sevilha - Espanha', 'Estocolmo - Suécia']
            }  
        ],
        'roteamento': {
            'Sevilha - Espanha': 'capitulo3sevilha',
            'Estocolmo - Suécia': 'capitulo3estocolmo'
        }
    },
    'capitulo2medo': {
        'audio_fundo': 'fundo_capitulo2medo',
        'cenas': [
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Alma que Me aceitou com medo, Eu conheço as profundezas de seu coração. Sua fé é verdadeira, mas a apreensão ainda o envolve. Não tema, pois Minha graça é suficiente para você. Sua jornada será um caminho para que o amor perfeito expulse todo o medo, e sua confiança em Mim se torne inabalável.',
                'imagem_principal': 'parte1_capitulo2medo',
                'audio': 'narracao1_capitulo2medo'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Contemple agora um dos caminhos que se abrem para você. Uma terra de fé vibrante e diversidade, onde Minha Igreja coexiste com muitos outros caminhos. Você nascerá em São Paulo, Brasil, em uma família de outra religião. Sua fé será testada pela lealdade familiar e pela busca da verdade em meio a diferentes vozes. Sua coragem será forjada no discernimento.',
                'imagem_principal': 'parte2_capitulo2medo',
                'audio': 'narracao2_capitulo2medo'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Agora, veja outro caminho, igualmente preparado para sua missão. Uma terra de fé milenar, o coração de Minha Igreja, mas onde você nascerá sem conhecer seus pais. Em Roma, Itália, sua busca por um lar e por amor será profunda. Sua fé será o alicerce para superar o abandono, e Minha Igreja, sua verdadeira família. Sua confiança em Mim será sua maior conquista.',
                'imagem_principal': 'parte3_capitulo2medo',
                'audio': 'narracao3_capitulo2medo'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Ambas as jornadas são caminhos de crescimento, preparados para que sua alma supere o medo e encontre a plenitude em Mim. Em uma, sua fé será forjada na diversidade. Na outra, seu coração encontrará um lar em Minha Igreja. Sua missão é a mesma: não aceitar menos que o Céu. Agora, escolha o ambiente onde sua confiança florescerá.',
                'imagem_principal': 'parte4_capitulo2medo',
                'audio': 'narracao4_capitulo2medo'
            },
            {
                'template': 'escolha',
                'personagem': 'Deus',
                'texto': 'E então, cara alma. Para onde deseja ir? São Paulo ou Roma?',
                'imagem_principal': 'parte4_capitulo2medo',
                'audio': 'narracao5_capitulo2medo',
		        'opcoes': ['São Paulo - Brasil', 'Roma - Itália']
            },
        ],
        'roteamento': {
            'Roma - Itália': 'capitulo3roma',
            'São Paulo - Brasil': 'capitulo3sao_paulo'
        },
    },
    'capitulo3roma': {
        'audio_fundo': 'fundo_global',
        'cenas': [
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Em Roma, a Cidade Eterna, sua jornada se inicia, alma. O portal se fechou, e você, Giulia, nasceu. Mas o mundo, em sua fragilidade, já lhe impôs a primeira ferida. O amor materno, brevemente sentido, se esvaiu com o último suspiro de sua mãe. E o pai, em seu próprio desespero, a deixou, uma pequena vida entregue ao cuidado de estranhos. O medo que você trouxe consigo, agora encontra sua primeira prova.',
                'imagem_principal': 'parte1_capitulo3roma',
                'audio': 'narracao1_capitulo3roma'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Os primeiros anos de Giulia se desenrolam entre as paredes de um orfanato em Roma. Ali, em meio a outras crianças e ao cuidado das Irmãs, você busca um toque, um olhar, um sinal de pertencimento. A presença de Minha Igreja é constante, através das mãos que a alimentam e das vozes que rezam. Mas o vazio da ausência de pais é uma sombra que acompanha cada dia, e o medo de não ser amada, uma constante.',
                'imagem_principal': 'parte2_capitulo3roma',
                'audio': 'narracao2_capitulo3roma'
            },
            {
                'template': 'dialogo',
                'personagem': 'Giulia',
                'texto': 'Por que não tenho pais? Por que sou diferente? Eu só queria alguém para me abraçar, para me chamar de "filha". As Irmãs são boas, mas... é diferente. Sinto um vazio aqui dentro.',
                'imagem_principal': 'parte3_capitulo3roma',
                'audio': 'narracao3_capitulo3roma'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Giulia, agora com três anos, você encontra um brinquedo quebrado, um pequeno cavalo de madeira. Outra criança, que o quebrou, o escondeu e agora o acusa de ter sido você. A Irmã se aproxima, buscando a verdade. Seu coração, ainda tão jovem, é confrontado com a primeira escolha consciente: a verdade ou a segurança, a justiça ou o medo da punição.',
                'imagem_principal': 'parte4_capitulo3roma',
                'audio': 'narracao4_capitulo3roma'
            },
            {
                'template': 'escolha',
                'personagem': 'Irmã do Orfanato',
                'texto': 'Giulia, você sabe o que aconteceu com o cavalo? Quem o quebrou?',
                'imagem_principal': 'parte4_capitulo3roma',
                'audio': 'narracao5_capitulo3roma',
		'opcoes': ['Eu não quebrei. Sabrina o quebrou e o escondeu.', 'Eu não sei. Não fui eu.', 'Eu quebrei, mas não foi por querer. Eu só queria brincar com ele.'],
            }  
        ],
        'roteamento': {
            'Eu não quebrei. Sabrina o quebrou e o escondeu.': 'julgamento-ceu',
            'Eu não sei. Não fui eu.': 'julgamento-purgatorio',
            'Eu quebrei, mas não foi por querer. Eu só queria brincar com ele.': 'julgamento-inferno'
        }
    },
    'capitulo3sao_paulo': {
        'audio_fundo': 'fundo_global',
        'cenas': [
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Em São Paulo, a metrópole que nunca dorme, sua jornada se inicia, alma. O portal se fechou, e você, Mateus, nasceu. No ventre de uma mulher que Me busca com sinceridade, embora por caminhos diferentes. Seu choro é acolhido por braços que Me invocam com fervor, mas que ainda não Me enxergam em Minha totalidade. O medo que você trouxe consigo, agora encontra seu primeiro lar na lealdade familiar.',
                'imagem_principal': 'parte1',
                'audio': 'narracao1_cap3sp'
            },
            {
                'template': 'dialogo',
                'personagem': 'Jeferson - pai do Mateus',
                'texto': 'Senhor, consagramos este filho a Ti! Que ele cresça em Tua Palavra, longe das idolatrias e dos enganos do mundo. Que ele seja fiel à nossa fé, e que nada o desvie do Teu verdadeiro caminho!',
                'imagem_principal': 'parte2',
                'audio': 'narracao2_cap3sp' 
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Desde o berço, o Nome de Deus será familiar aos seus ouvidos. Mas não o Meu Corpo. A Cruz será símbolo, mas não Sacramento. A fé será viva, mas limitada pelo medo do engano. Você crescerá sendo amado e instruído na retidão, mas também na desconfiança do que é diferente. E Eu estarei lá. Sempre.',
                'imagem_principal': 'parte3',
                'audio': 'narracao3_cap3sp'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Mateus, desde cedo você perceberá que há algo mais. Nos silêncios entre os hinos, nas perguntas que ninguém sabe responder, nas imagens que dizem ser ídolos, mas que tocarão seu coração... Meu Espírito sussurrará ao seu interior: "Procure por Mim em toda parte, pois Eu sou maior do que esses limites". E esse chamado, alma, será o início da sua coragem, um convite a superar o medo que o prende.',
                'imagem_principal': 'parte4',
                'audio': 'narracao4_cap3sp'
            },
            {
                'template': 'dialogo',
                'personagem': 'Mateus',
                'texto': 'Professora... por que minha igreja diz que Maria não pode aparecer? Mas ela parece tão... boa...',
                'imagem_principal': 'parte5',
                'audio': 'narracao5_cap3sp'
            },
            {
                'template': 'dialogo',
                'personagem': 'Professora - Yvone',
                'texto': 'Ah, Mateus... bem, algumas igrejas têm diferentes formas de expressar a fé. Mas o importante é o amor a Jesus, não é?',
                'imagem_principal': 'parte6',
                'audio': 'narracao6_cap3sp'
            },
            {
                'template': 'dialogo',
                'personagem': 'Colega - Junior',
                'texto': 'Isso aí é coisa de católico. Minha mãe disse que a gente não pode acreditar nessas imagens. Que é pecado!',
                'imagem_principal': 'parte7',
                'audio': 'narracao7_cap3sp'
            },
            {
                'template': 'dialogo',
                'personagem': 'Leticia - mãe do Mateus',
                'texto': 'Filho, você sabe que a gente não acredita nessas coisas. Só Jesus, tá bem? Só Ele é suficiente.',
                'imagem_principal': 'parte8',
                'audio': 'narracao8_cap3sp'
            },
            {
                'template': 'dialogo',
                'personagem': 'Mateus',
                'texto': 'Meu pai... eu não sei se isso é certo ou errado. Mas parece bom. Eu gosto de ouvir falar do Senhor. Só... só não entendo por que tem tanta coisa que dizem que é errada. Se for o Senhor mesmo... então, por que tanta divisão?',
                'imagem_principal': 'parte9',
                'audio': 'narracao9_cap3sp'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': '...',
                'imagem_principal': 'parte9',
                'audio': 'fundo_global'
            },
            {
                'template': 'dialogo',
                'personagem': 'Mateus',
                'texto': 'Se o Senhor quiser me mostrar... pode mostrar. Eu quero aprender. Mas... não quero machucar ninguém. Nem minha mãe.',
                'imagem_principal': 'parte9',
                'audio': 'narracao10_cap3sp'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': '...',
                'imagem_principal': 'parte9',
                'audio': 'fundo_global'
            },
            {
                'template': 'dialogo',
                'personagem': 'Professora - Yvone',
                'texto': 'A turma vai ensaiar na igreja católica do bairro, ok? É o lugar com mais espaço. Vai ser lindo. Quem tiver algum problema, me avisa.',
                'imagem_principal': 'opcao_final',
                'audio': 'narracao11_cap3sp',
            },
            {
                'template': 'opcao',
                'personagem': 'Professora - Yvone',
                'texto': 'Mateus, você quer participar da visita à igreja para o ensaio?',
                'imagem_principal': 'opcao_final',
                'audio': 'narracaofinal_cap3sp',
                'opcoes': ['Sim, professora. Eu quero ir.', 'Não, professora. Prefiro não participar.', 'Não sei, professora. Talvez seja melhor não ir.'],
            },
        ],
        'roteamento': {
            'Sim, professora. Eu quero ir.': 'julgamento-ceu',
            'Não, professora. Prefiro não participar.': 'julgamento-inferno',
            'Não sei, professora. Talvez seja melhor não ir.': 'julgamento-purgatorio'
        }
    },
    'capitulo3estocolmo': {
        'audio_fundo': 'fundo_global',
        'cenas': [
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Alma enviada com amor, sua jornada se inicia. Neste país de invernos longos e palavras contidas, você nasceu. Linnea Karlsson, filha de mentes brilhantes, mas de corações que Me desconhecem. Aqueles que agora te seguram foram formados pela razão, pela lógica, pela ciência que Eu mesmo criei, mas que agora tentam usar para Me negar. Eles te amarão como puderem, mas não saberão te ensinar sobre Mim. Não por maldade, mas por ignorância. Aqui, o amor é medido, e a fé, uma superstição esquecida.',
                'imagem_principal': 'parte1',
                'audio': 'narracao1_cap3e'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Mesmo entre livros e teorias, seu coração sente que algo falta. Você ouve sobre o Big Bang, mas pergunta quem acendeu o fósforo. Você aprende sobre evolução, mas sente que há mais beleza no mundo do que o acaso pode criar. É o Meu sopro, Linnea. Ele já ressoa em você.',
                'imagem_principal': 'parte2',
                'audio': 'narracao2_cap3e'
            },
            {
                'template': 'dialogo',
                'personagem': 'Linnea',
                'texto': 'O que é isso?',
                'imagem_principal': 'parte3',
                'audio': 'narracao3_cap3e'
            },
            {
                'template': 'dialogo',
                'personagem': 'Senhora idosa',
                'texto': 'É um terço... uma oração.',
                'imagem_principal': 'parte3',
                'audio': 'narracao4_cap3e'
            },
            {
                'template': 'dialogo',
                'personagem': 'Linnea',
                'texto': 'Oração?',
                'imagem_principal': 'parte3',
                'audio': 'narracao5_cap3e'
            },
            {
                'template': 'dialogo',
                'personagem': 'Senhora idosa',
                'texto': 'É quando falamos com Deus. Você nunca falou com Ele?',
                'imagem_principal': 'parte3',
                'audio': 'narracao6_cap3e'
            },
            {
                'template': 'dialogo',
                'personagem': 'Linnea',
                'texto': '...',
                'imagem_principal': 'parte3',
                'audio': 'fundo_global'
            },
            {
                'template': 'dialogo',
                'personagem': 'Linnea',
                'texto': 'Não. Não sei se Ele existe.',
                'imagem_principal': 'parte3',
                'audio': 'narracao7_cap3e'
            },
            {
                'template': 'dialogo',
                'personagem': 'Senhora idosa',
                'texto': 'Talvez você não saiba ainda. Mas Ele já está te ouvindo.',
                'imagem_principal': 'parte3',
                'audio': 'narracao8_cap3e'
            },
            {
                'template': 'dialogo',
                'personagem': 'Linnea',
                'texto': 'Deus... você está me ouvindo?',
                'imagem_principal': 'parte4',
                'audio': 'narracao9_cap3e'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': '...',
                'imagem_principal': 'parte4',
                'audio': 'fundo_global'
            },
            {
                'template': 'dialogo',
                'personagem': 'Linnea',
                'texto': 'Deus... você está me ouvindo?',
                'imagem_principal': 'parte4',
                'audio': 'narracao9_cap3e'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': '...',
                'imagem_principal': 'parte4',
                'audio': 'fundo_global'
            },
            {
                'template': 'dialogo',
                'personagem': 'Linnea',
                'texto': 'Deus... você está me ouvindo?',
                'imagem_principal': 'parte4',
                'audio': 'narracao9_cap3e'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': '...',
                'imagem_principal': 'parte4',
                'audio': 'fundo_global'
            },
            {
                'template': 'dialogo',
                'personagem': 'Linnea',
                'texto': 'Mãe, existe Deus?',
                'imagem_principal': 'parte5',
                'audio': 'narracao10_cap3e'
            },
            {
                'template': 'dialogo',
                'personagem': 'Joana - mãe de Linnea',
                'texto': 'Ah, meu amor... algumas pessoas acreditam nisso. Mas nós acreditamos na razão. A vida é maravilhosa por si só. E é só isso que temos.',
                'imagem_principal': 'parte5',
                'audio': 'narracao11_cap3e'
            },
            {
                'template': 'dialogo',
                'personagem': 'Linnea',
                'texto': 'Mas... e se for mais?',
                'imagem_principal': 'parte5',
                'audio': 'narracao12_cap3e'
            },
            {
                'template': 'dialogo',
                'personagem': 'João - pai de Linnea',
                'texto': 'Linnea, isso é papo de igreja. Não precisamos disso para sermos boas pessoas. Está bem?',
                'imagem_principal': 'parte5',
                'audio': 'narracao13_cap3e'
            },
            {
                'template': 'dialogo',
                'personagem': 'Linnea',
                'texto': '...',
                'imagem_principal': 'parte5',
                'audio': 'fundo_global'
            },
            {
                'template': 'dialogo',
                'personagem': 'Linnea',
                'texto': 'Que biblioteca rica! Olha esses livros antigos! E esse aqui... Parece interessante. Eu nunca ouvi falar disso na escola.',
                'imagem_principal': 'parte5',
                'audio': 'narracao14_cap3e'
            },
            {
                'template': 'dialogo',
                'personagem': 'Linnea',
                'texto': '...',
                'imagem_principal': 'parte5',
                'audio': 'fundo_global'
            },
            {
                'template': 'opcao',
                'personagem': 'Bibliotecária',
                'texto': 'Quer levar esse livro, querida?',
                'imagem_principal': 'parte6',
                'audio': 'narracao15_cap3e',
                'opcoes': ['Sim... posso levar?', 'Não... meus pais não gostam dessas coisas.', 'Não sei... talvez seja melhor não levar agora. Eu não sei se posso ler isso.'],
            },
        ],
        'roteamento': {
            'Sim... posso levar?': 'julgamento-ceu',
            'Não... meus pais não gostam dessas coisas.': 'julgamento-inferno',
            'Não sei... talvez seja melhor não levar agora. Eu não sei se posso ler isso.': 'julgamento-purgatorio'
        }
    },
    'capitulo3sevilha': {
        'audio_fundo': 'fundo_global',
        'cenas': [
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Em Sevilha, a cidade da luz e da devoção, sua jornada se inicia, alma. O portal se fechou, e você, Isabella, nasce. O sol da Andaluzia banha as ruas históricas, e o ar é perfumado com incenso e flores. Você nasceu em uma das mais tradicionais e abastadas famílias, onde a fé católica é um legado, e a riqueza, uma herança. Seu choro é acolhido por braços que Me invocam com fervor e que Me enxergam em Minha totalidade. O amor que você trouxe consigo, agora encontra seu primeiro lar na tradição e na prosperidade.',
                'imagem_principal': 'parte1',
                'audio': 'narracao1_cap3s'
            },
            {
                'template': 'dialogo',
                'personagem': 'Francisco - pai da Isabella',
                'texto': 'Senhor, consagramos esta filha a Ti! Que ela seja digna de nossa fé e de nosso nome. Que ela cresça na retidão e na caridade, e que sua vida seja um testemunho de nossa devoção e de nossa posição na sociedade!',
                'imagem_principal': 'parte1',
                'audio': 'narracao2_cap3s'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Desde o berço, o Nome de Deus será familiar aos seus ouvidos. O Meu Corpo, a Cruz, o Sacramento, tudo será parte de sua vida. A fé será viva, mas a tentação da complacência e do orgulho espiritual espreitará. Você crescerá sendo amada e instruída na retidão, mas também na expectativa de manter as aparências e o status. E Eu estarei lá. Sempre.',
                'imagem_principal': 'parte1',
                'audio': 'narracao3_cap3s'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Isabella, desde cedo você demonstrará uma sensibilidade incomum. Em meio ao luxo e às formalidades, seu coração sentirá que há algo mais profundo. Você observará a caridade de sua família, mas perguntará se ela é feita por amor verdadeiro ou por reconhecimento. Você aprenderá sobre os santos, mas sentirá que a santidade é mais do que títulos e aparências. É o Meu sopro, Isabella. Ele já ressoa em você, uma sede inata pela autenticidade e pela verdade que transcende as convenções sociais.',
                'imagem_principal': 'parte1',
                'audio': 'narracao4_cap3s'
            },
            {
                'template': 'dialogo',
                'personagem': 'Isabella',
                'texto': 'Mãe... por que eles não têm brinquedos bonitos como os meus? E por que eles parecem... tão diferentes?',
                'imagem_principal': 'parte2',
                'audio': 'narracao5_cap3s'
            },
            {
                'template': 'dialogo',
                'personagem': 'Maria - mãe da Isabella',
                'texto': 'Ah, meu amor... são crianças menos afortunadas. Nós as ajudamos com a caridade da família. É importante que saibam que somos generosos e que Deus nos abençoou para isso.',
                'imagem_principal': 'parte2',
                'audio': 'narracao6_cap3s'
            },
            {
                'template': 'dialogo',
                'personagem': 'Criança no evento',
                'texto': '...',
                'imagem_principal': 'parte3',
                'audio': 'fundo_global'
            },
            {
                'template': 'dialogo',
                'personagem': 'Isabella',
                'texto': '...',
                'imagem_principal': 'parte3',
                'audio': 'fundo_global'
            },
            {
                'template': 'opcao',
                'personagem': 'Criança no evento',
                'texto': 'Que boneca linda, eu posso brincar?',
                'imagem_principal': 'parte3',
                'audio': 'narracao7_cap3s',
                'opcoes': ['Quer brincar com ela? Pode ficar com ela.', 'Sim, mas só se você prometer que vai cuidar muito bem dela e me devolver depois.', 'Podemos brincar juntas. o que acha?'],
            },
        ],
        'roteamento': {
            'Sim, mas só se você prometer que vai cuidar muito bem dela e me devolver depois.': 'julgamento-inferno',
            'Quer brincar com ela? Pode ficar com ela.': 'julgamento-ceu',
            'Podemos brincar juntas. o que acha?': 'julgamento-purgatorio'
        }
    },
    'julgamento-ceu': {
        'audio_fundo': 'fundo_global',
        'cenas': [
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'A jornada terrena chegou ao seu fim. O corpo, templo da alma, cessa sua respiração. A vida, que Eu soprei em você, agora se retira. A alma, livre de suas amarras terrenas, se desprende, leve e consciente, pronta para o encontro que a aguarda.',
                'imagem_principal': 'parte1',
                'audio': 'narracao1_julgamento'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Imediatamente após a morte, cada alma se apresenta diante de Mim, em um Juízo Particular. Não há mais tempo para escolhas, apenas para a verdade. Todas as suas ações, pensamentos e omissões, cada ato de amor e cada recusa, são revelados em um instante. Sua vida, alma, é posta diante de Cristo, o Juiz dos vivos e dos mortos.',
                'imagem_principal': 'parte2',
                'audio': 'narracao2_julgamento'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'O momento da verdade chegou. Com base em todas as suas escolhas, na sua busca por Mim, na sua capacidade de discernir Meus caminhos e de amar como Eu amo, seu destino eterno é revelado.',
                'imagem_principal': 'parte2',
                'audio': 'narracao3_julgamento'
            },
            {
                'template': 'opcao',
                'personagem': 'Deus',
                'texto': 'Vinde, bendito de Meu Pai! Recebeis em herança o Reino preparado para vós desde a criação do mundo. Sua vida foi um hino de amor e verdade. Entre na alegria de seu Senhor!',
                'imagem_principal': 'parte2',
                'audio': 'narracao4_julgamento',
                'opcoes': ['Aceitar destino']
            }
        ],
        'roteamento': {
            'Aceitar destino': 'ceu'
        }
    },
    'julgamento-inferno': {
        'audio_fundo': 'fundo_global',
        'cenas': [
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'A jornada terrena chegou ao seu fim. O corpo, templo da alma, cessa sua respiração. A vida, que Eu soprei em você, agora se retira. A alma, livre de suas amarras terrenas, se desprende, leve e consciente, pronta para o encontro que a aguarda.',
                'imagem_principal': 'parte1',
                'audio': 'narracao1_julgamento'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Imediatamente após a morte, cada alma se apresenta diante de Mim, em um Juízo Particular. Não há mais tempo para escolhas, apenas para a verdade. Todas as suas ações, pensamentos e omissões, cada ato de amor e cada recusa, são revelados em um instante. Sua vida, alma, é posta diante de Cristo, o Juiz dos vivos e dos mortos.',
                'imagem_principal': 'parte2',
                'audio': 'narracao2_julgamento'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'O momento da verdade chegou. Com base em todas as suas escolhas, na sua busca por Mim, na sua capacidade de discernir Meus caminhos e de amar como Eu amo, seu destino eterno é revelado.',
                'imagem_principal': 'parte2',
                'audio': 'narracao3_julgamento'
            },
            {
                'template': 'opcao',
                'personagem': 'Deus',
                'texto': 'Afasta-te de Mim, alma que Me rejeitou. Sua escolha foi a separação, e sua vontade, a de viver sem Mim. Você não aceitou Minha graça, e agora, a consequência de sua liberdade é a ausência de Minha Luz. Vá para a escuridão eterna, onde sua escolha se consuma.',
                'imagem_principal': 'parte2',
                'audio': 'narracao4_julgamento',
                'opcoes': ['Aceitar destino']
            }
        ],
        'roteamento': {
            'Aceitar destino': 'inferno'
        }
    },
    'julgamento-purgatorio': {
        'audio_fundo': 'fundo_global',
        'cenas': [
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'A jornada terrena chegou ao seu fim. O corpo, templo da alma, cessa sua respiração. A vida, que Eu soprei em você, agora se retira. A alma, livre de suas amarras terrenas, se desprende, leve e consciente, pronta para o encontro que a aguarda.',
                'imagem_principal': 'parte1',
                'audio': 'narracao1_julgamento'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'Imediatamente após a morte, cada alma se apresenta diante de Mim, em um Juízo Particular. Não há mais tempo para escolhas, apenas para a verdade. Todas as suas ações, pensamentos e omissões, cada ato de amor e cada recusa, são revelados em um instante. Sua vida, alma, é posta diante de Cristo, o Juiz dos vivos e dos mortos.',
                'imagem_principal': 'parte2',
                'audio': 'narracao2_julgamento'
            },
            {
                'template': 'dialogo',
                'personagem': 'Deus',
                'texto': 'O momento da verdade chegou. Com base em todas as suas escolhas, na sua busca por Mim, na sua capacidade de discernir Meus caminhos e de amar como Eu amo, seu destino eterno é revelado.',
                'imagem_principal': 'parte2',
                'audio': 'narracao3_julgamento'
            },
            {
                'template': 'opcao',
                'personagem': 'Deus',
                'texto': 'Alma amada, você Me buscou com sinceridade, mas ainda há apegos e imperfeições que precisam ser purificados. Vá para o Purgatório, onde o fogo do Meu Amor o refinará, até que esteja pronto para a plenitude da Minha Presença. Sua esperança é certa, e sua entrada no Céu, garantida.',
                'imagem_principal': 'parte2',
                'audio': 'narracao4-julgamento',
                'opcoes': ['Aceitar destino']
            }
        ],
        'roteamento': {
            'Aceitar destino': 'purgatorio'
        }
    },
    'ceu': {
        'audio_fundo': 'som_ceu',
        'cenas': [
            {
                'template': 'finalizacao',
                'personagem': 'Deus',
                'texto': 'Você chegou ao Céu! O lugar de plenitude e alegria eterna. Aqui, não há dor, não há lágrimas, não há separação. Aqui, você está em Minha Presença, rodeado pelo Meu Amor infinito.',
                'imagem_principal': 'o_ceu',
                'audio': 'narracao_final_ceu'
            }
        ]
    },
    'inferno': {
        'audio_fundo': 'som_inferno',
        'cenas': [
            {
                'template': 'finalizacao',
                'personagem': 'Deus',
                'texto': 'Você escolheu o caminho da desobediência e do egoísmo. Aqui, você está separado de Mim, em um lugar de dor e arrependimento. Lembre-se, eu criei esse espaço para o Demônio e seus anjos, mas você escolheu estar aqui!',
                'imagem_principal': 'o_inferno',
                'audio': 'narracao_final_inferno'
            }
        ]
    },
    'purgatorio': {
        'audio_fundo': 'som_purgatorio',
        'cenas': [
            {
                'template': 'finalizacao',
                'personagem': 'Deus',
                'texto': 'Você está no Purgatório, um lugar de purificação. Aqui, você se prepara para entrar no Céu, passando pelo fogo do Meu Amor que purifica e transforma. Sua jornada não acabou, mas a esperança de redenção permanece.',
                'imagem_principal': 'o_purgatorio',
                'audio': 'narracao_final_purgatorio'
            }
        ]    
    },
    'perdicao': {
        'audio_fundo': 'som_ceu',
        'cenas': [
            {
                'template': 'finalizacao',
                'personagem': 'Deus',
                'texto': 'Infelizmente, você rejeitou a missão. Você escolheu o caminho da desobediência e do egoísmo. Mas, tudo bem! Eu te espero na eternidade, em uma nova oportunidade de redenção. Lembre-se, Meu Amor por você nunca acaba!',
                'imagem_principal': 'perdicao',
                'audio': 'narracao_final_perdicao'
            }
        ]
    }
}
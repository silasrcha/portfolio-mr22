# Traduções do portfólio MR 22. Chave = texto exato em português na página (nó de texto ou atributo).
# Gera en.html e es.html a partir de index.html:  py -3 i18n.py
import re, html as H

T = {
"Estudo de caso de Silas na campanha MR 22: direção de arte, automação com IA e produção em escala com identidade intacta.":
 ("Case study by Silas on the MR 22 campaign: art direction, AI-powered automation and production at scale with the identity intact.",
  "Caso de estudio de Silas en la campaña MR 22: dirección de arte, automatización con IA y producción a escala con la identidad intacta."),
"Alta demanda, identidade intacta · Silas": ("High demand, identity intact · Silas", "Alta demanda, identidad intacta · Silas"),
"Portfólio Campanha MR 22": ("MR 22 Campaign Portfolio", "Portfolio Campaña MR 22"),
"Seções": ("Sections", "Secciones"),
"Idioma": ("Language", "Idioma"),
"Perfil": ("Profile", "Perfil"),
"Debates": ("Debates", "Debates"),
"Tráfego": ("Paid media", "Pauta paga"),
"· Portfólio MR 22": ("· Portfolio MR 22", "· Portfolio MR 22"),
"Estúdios": ("Studios", "Estudios"),
"IA": ("AI", "IA"),
"Linha do tempo": ("Timeline", "Línea de tiempo"),
"Primeira lâmina do carrossel de biografia, fixado no perfil": ("First slide of the biography carousel, pinned to the profile", "Primera lámina del carrusel de biografía, fijado en el perfil"),
"Carrossel da biografia · lâmina 01 · fixado no perfil · 08/09": ("Biography carousel · slide 01 · pinned to profile · Sep 8", "Carrusel de biografía · lámina 01 · fijado en el perfil · 08/09"),
"Índice": ("Index", "Índice"),
"Estudos de caso": ("Case studies", "Casos de estudio"),
"001 Campanha MR 22": ("001 MR 22 Campaign", "001 Campaña MR 22"),
"Alta demanda, identidade intacta.": ("High demand, identity intact.", "Alta demanda, identidad intacta."),
"Eleições 2026 · Governo de Rondônia": ("2026 Elections · Governor of Rondônia, Brazil", "Elecciones 2026 · Gobernación de Rondônia, Brasil"),
"Entrei na campanha de Marcos Rogério (22) ao Governo de Rondônia como diretor de arte, para desdobrar a identidade para o digital. A partir dela, usei inteligência artificial para construir ferramentas e automatizar a produção: cards de debate em tempo real, peças para os 52 municípios e a mobilização saíram rápido, sem trabalho repetitivo para a equipe e sem perder a identidade. A campanha venceu no primeiro turno, em 4 de outubro de 2026.":
 ("I joined Marcos Rogério’s (22) campaign for Governor of Rondônia as art director, to extend the identity into digital. Building on it, I used artificial intelligence to create tools and automate production: real-time debate cards, pieces for all 52 municipalities and grassroots mobilization went out fast, with no repetitive work for the team and no loss of identity. The campaign won in the first round, on October 4, 2026.",
  "Entré a la campaña de Marcos Rogério (22) a la Gobernación de Rondônia como director de arte, para desplegar la identidad en lo digital. A partir de ella, usé inteligencia artificial para crear herramientas y automatizar la producción: cards de debate en tiempo real, piezas para los 52 municipios y la movilización salieron rápido, sin trabajo repetitivo para el equipo y sin perder la identidad. La campaña ganó en primera vuelta, el 4 de octubre de 2026."),
"Cliente": ("Client", "Cliente"),
"Campanha Marcos Rogério 22, Governo de Rondônia": ("Marcos Rogério 22 campaign, Governor of Rondônia", "Campaña Marcos Rogério 22, Gobernación de Rondônia"),
"Minha função": ("My role", "Mi rol"),
"Direção de arte do digital: linguagem, curadoria das fotos, peças e ferramentas": ("Digital art direction: visual language, photo curation, pieces and tools", "Dirección de arte digital: lenguaje, curaduría de fotos, piezas y herramientas"),
"Ponto de partida": ("Starting point", "Punto de partida"),
"Logotipo, tipografia, paleta e grafismos de outro diretor de arte": ("Logo, typography, palette and graphic elements by another art director", "Logotipo, tipografía, paleta y gráficos de otro director de arte"),
"Ferramentas": ("Tools", "Herramientas"),
"Photoshop, Figma (auto layout e API), Claude Code, Python, GitHub Pages, Vercel": ("Photoshop, Figma (auto layout and API), Claude Code, Python, GitHub Pages, Vercel", "Photoshop, Figma (auto layout y API), Claude Code, Python, GitHub Pages, Vercel"),
"Diretor de arte": ("Art director", "Director de arte"),
"Designer gráfico": ("Graphic designer", "Diseñador gráfico"),
"Ver os números": ("See the numbers", "Ver los números"),
"Números da campanha": ("Campaign numbers", "Números de la campaña"),
"Produção em lote": ("Batch production", "Producción en lote"),
"peças geradas em lote a partir dos meus modelos: 495 lâminas de carrossel, 104 peças por município e 208 adesivos. Fora isso, os cards que saíram dos estúdios.":
 ("pieces batch-generated from my templates: 495 carousel slides, 104 per-municipality pieces and 208 stickers. Plus the cards made in the studios.",
  "piezas generadas en lote a partir de mis plantillas: 495 láminas de carrusel, 104 piezas por municipio y 208 stickers. Además, los cards que salieron de los estudios."),
"Linhas de código": ("Lines of code", "Líneas de código"),
"~20 mil": ("~20k", "~20 mil"),
"linhas de código nas ferramentas, escritas com IA a partir das minhas especificações": ("lines of code across the tools, written with AI from my specifications", "líneas de código en las herramientas, escritas con IA a partir de mis especificaciones"),
"Estúdios web": ("Web studios", "Estudios web"),
"estúdios web que automatizam cards da campanha: a equipe digita o texto, escolhe a foto e baixa a peça pronta": ("web studios that automate campaign cards: the team types the text, picks the photo and downloads the finished piece", "estudios web que automatizan cards de la campaña: el equipo escribe el texto, elige la foto y descarga la pieza lista"),
"Trabalho manual evitado": ("Manual work saved", "Trabajo manual evitado"),
"de trabalho manual absorvidas pela produção em lote, só nas 807 peças. Os cards dos estúdios somam mais: cada um levava cerca de 8 minutos à mão.":
 ("of manual work absorbed by batch production, on the 807 pieces alone. Studio cards add more: each one took about 8 minutes by hand.",
  "de trabajo manual absorbidas por la producción en lote, solo en las 807 piezas. Los cards de los estudios suman más: cada uno llevaba unos 8 minutos a mano."),
"IA generativa nas peças": ("Generative AI in the pieces", "IA generativa en las piezas"),
"imagens ou elementos gráficos gerados por IA nas peças que assinei: a IA ficou na engenharia, a criação ficou comigo":
 ("AI-generated images or graphic elements in the pieces I signed: AI stayed in the engineering, the creative work stayed with me",
  "imágenes o elementos gráficos generados por IA en las piezas que firmé: la IA quedó en la ingeniería, la creación quedó conmigo"),
"Do 1º post à vitória": ("From first post to victory", "Del 1.er post a la victoria"),
"54 dias": ("54 days", "54 días"),
"entre o primeiro carrossel publicado, em 11/08, e a vitória no primeiro turno": ("between the first carousel published, on Aug 11, and the first-round victory", "entre el primer carrusel publicado, el 11/08, y la victoria en primera vuelta"),
"807 peças · ~20 mil linhas · 9 estúdios · ~45 h": ("807 pieces · ~20k lines · 9 studios · ~45 h", "807 piezas · ~20 mil líneas · 9 estudios · ~45 h"),
"Ver a conta →": ("See the math →", "Ver el cálculo →"),
"Uma identidade pronta, e uma campanha que precisava falar a língua das redes.": ("An identity already in place, and a campaign that needed to speak the language of social media.", "Una identidad ya definida, y una campaña que necesitaba hablar el idioma de las redes."),
"Cheguei com a base da identidade já definida por outro diretor de arte: logotipo, tipografia, paleta e grafismos. Minha missão era desdobrar esse sistema para o digital, onde a campanha precisava de outro ritmo e de mais proximidade.":
 ("I arrived with the identity foundation already set by another art director: logo, typography, palette and graphic elements. My mission was to extend that system into digital, where the campaign needed a different pace and more closeness.",
  "Llegué con la base de la identidad ya definida por otro director de arte: logotipo, tipografía, paleta y gráficos. Mi misión era desplegar ese sistema en lo digital, donde la campaña necesitaba otro ritmo y más cercanía."),
"Linguagem": ("Visual language", "Lenguaje"),
"Para as redes, optei por uma linguagem mais crua, leve e humana, que transmitisse sentimento e mostrasse o candidato do jeito que o eleitor ainda não tinha visto.":
 ("For social media, I chose a rawer, lighter and more human language, one that conveyed feeling and showed the candidate in a way voters had not seen before.",
  "Para las redes, opté por un lenguaje más crudo, liviano y humano, que transmitiera sentimiento y mostrara al candidato como el votante todavía no lo había visto."),
"Estratégia documental": ("Documentary approach", "Estrategia documental"),
"Em vez de distribuir santinhos, mostrar a trajetória de perto.": ("Instead of handing out flyers, show the journey up close.", "En vez de repartir volantes, mostrar el recorrido de cerca."),
"Mantive os elementos da marca e mudei o tratamento. A linha passou a ser documental: em cada foto e em cada carrossel, quem acompanhava o perfil estava ali com o candidato, nas cidades, com as pessoas. A escolha das fotos, a edição e o tratamento ficaram sob a minha direção, do avatar aos carrosséis.":
 ("I kept the brand elements and changed the treatment. The line became documentary: in every photo and every carousel, followers were right there with the candidate, in the towns, with the people. Photo selection, editing and treatment were under my direction, from the avatar to the carousels.",
  "Mantuve los elementos de la marca y cambié el tratamiento. La línea pasó a ser documental: en cada foto y en cada carrusel, quien seguía el perfil estaba ahí con el candidato, en las ciudades, con la gente. La elección de las fotos, la edición y el tratamiento quedaron bajo mi dirección, del avatar a los carruseles."),
"Frente 01 / Perfil oficial": ("Workstream 01 / Official profile", "Frente 01 / Perfil oficial"),
"A linguagem aplicada: enxoval, carrosséis e cards.": ("The language in use: profile kits, carousels and cards.", "El lenguaje aplicado: kits de perfil, carruseles y cards."),
"As peças do perfil foram feitas no Photoshop. Nelas, a foto conduz e a identidade de campanha entra para assinar.": ("The profile pieces were made in Photoshop. In them, the photo leads and the campaign identity comes in as the signature.", "Las piezas del perfil se hicieron en Photoshop. En ellas, la foto conduce y la identidad de campaña entra como firma."),
"Enxoval do perfil": ("Profile kit", "Kit de perfil"),
"avatar, capas, destaques e fixados": ("avatar, covers, highlights and pinned posts", "avatar, portadas, destacadas y fijados"),
"Avatar do lançamento da campanha": ("Campaign launch avatar", "Avatar del lanzamiento de la campaña"),
"001 / Ago · 15–18/08": ("001 / Aug · 15–18", "001 / Ago · 15–18/08"),
"Lançamento": ("Launch", "Lanzamiento"),
"Enxoval completo para a estreia: avatar, capas de Facebook, YouTube e X, destaques do Instagram.": ("Full kit for the debut: avatar, Facebook, YouTube and X covers, Instagram highlights.", "Kit completo para el estreno: avatar, portadas de Facebook, YouTube y X, destacadas de Instagram."),
"Destaques do lançamento": ("Launch highlights", "Destacadas del lanzamiento"),
"Segundo avatar, com reforço do número 22": ("Second avatar, reinforcing the number 22", "Segundo avatar, reforzando el número 22"),
"002 / Set · 20–25/09": ("002 / Sep · 20–25", "002 / Sep · 20–25/09"),
"Segundo enxoval": ("Second kit", "Segundo kit"),
"Nova foto e reforço do número do candidato em todo o perfil, com destaques refeitos.": ("New photo and the candidate’s number reinforced across the profile, with redone highlights.", "Foto nueva y refuerzo del número del candidato en todo el perfil, con destacadas rehechas."),
"Destaques do segundo enxoval": ("Second kit highlights", "Destacadas del segundo kit"),
"Novo ícone de perfil, da reta final": ("New profile picture for the final stretch", "Nuevo ícono de perfil, de la recta final"),
"003 / Set · 29/09": ("003 / Sep · 29", "003 / Sep · 29/09"),
"Reta final": ("Final stretch", "Recta final"),
"Novo ícone de perfil, também com reforço do número, para a última semana. Os destaques do segundo enxoval continuaram.": ("New profile picture, also reinforcing the number, for the last week. The second kit’s highlights stayed.", "Nuevo ícono de perfil, también con refuerzo del número, para la última semana. Las destacadas del segundo kit se mantuvieron."),
"Destaques mantidos do segundo enxoval": ("Highlights kept from the second kit", "Destacadas mantenidas del segundo kit"),
"Foto oficial do governador eleito": ("Official photo of the governor-elect", "Foto oficial del gobernador electo"),
"004 / Out · 05/10": ("004 / Oct · 5", "004 / Oct · 05/10"),
"Governador eleito": ("Governor-elect", "Gobernador electo"),
"Quarto enxoval, já com a foto oficial e destaques novos, feito no dia seguinte à vitória.": ("Fourth kit, with the official photo and new highlights, made the day after the victory.", "Cuarto kit, ya con la foto oficial y destacadas nuevas, hecho al día siguiente de la victoria."),
"Destaques do governador eleito": ("Governor-elect highlights", "Destacadas del gobernador electo"),
"Carrosséis": ("Carousels", "Carruseles"),
"1080 × 1440 · feed 3:4 · role cada tira para o lado": ("1080 × 1440 · 3:4 feed · scroll each strip sideways", "1080 × 1440 · feed 3:4 · desplazá cada tira hacia el costado"),
"Cards": ("Cards", "Cards"),
"peças únicas · 1080 × 1440": ("single pieces · 1080 × 1440", "piezas únicas · 1080 × 1440"),
"Card da pesquisa CNN": ("CNN poll card", "Card de la encuesta CNN"),
"Pesquisa CNN · 12/09": ("CNN poll · Sep 12", "Encuesta CNN · 12/09"),
"Card Quem vota 22 vota 22": ("“Who votes 22 votes 22” card", "Card “Quien vota 22 vota 22”"),
"Quem vota Flávio · 25/09": ("Quem vota Flávio · Sep 25", "Quem vota Flávio · 25/09"),
"Card Eu voto por": ("“I vote for” card", "Card “Yo voto por”"),
"Direcionamentos · Eu voto por · 26/09": ("Messaging · Eu voto por · Sep 26", "Direccionamientos · Eu voto por · 26/09"),
"Card governador que conhece Rondônia": ("“A governor who knows Rondônia” card", "Card “Un gobernador que conoce Rondônia”"),
"Gov que conhece Rondônia · 02/10": ("Gov que conhece Rondônia · Oct 2", "Gov que conhece Rondônia · 02/10"),
"Colinha 22, card Passa a cola": ("Colinha 22, the ballot cheat-sheet card", "Colinha 22, el card machete para votar"),
"Passa a cola · Colinha 22 · 03/10": ("Passa a cola · Colinha 22 · Oct 3", "Passa a cola · Colinha 22 · 03/10"),
"Card da vitória no primeiro turno": ("First-round victory card", "Card de la victoria en primera vuelta"),
"Vitória no 1º turno · 04/10": ("First-round victory · Oct 4", "Victoria en 1.ª vuelta · 04/10"),
"Frente 02 / Página de apoiadores": ("Workstream 02 / Supporters page", "Frente 02 / Página de simpatizantes"),
"Uma identidade à parte, para reforçar a mensagem.": ("A separate identity, to reinforce the message.", "Una identidad aparte, para reforzar el mensaje."),
"Além do perfil oficial, fiz os cards da página de apoiadores. Ela tinha identidade própria e funcionava como reforço: repercutia pesquisas, debates e chamadas de mobilização com outra voz, sem repetir o visual do candidato.":
 ("Beyond the official profile, I made the cards for the supporters page. It had its own identity and worked as reinforcement: it echoed polls, debates and mobilization calls in a different voice, without repeating the candidate’s look.",
  "Además del perfil oficial, hice los cards de la página de simpatizantes. Tenía identidad propia y funcionaba como refuerzo: amplificaba encuestas, debates y convocatorias con otra voz, sin repetir la estética del candidato."),
"Card de apoiadores: debate encerrado": ("Supporters card: debate closed", "Card de simpatizantes: debate terminado"),
"Debate encerrado": ("Debate encerrado", "Debate encerrado"),
"Card de apoiadores: Veritá confirma": ("Supporters card: Veritá poll confirms", "Card de simpatizantes: Veritá confirma"),
"Veritá confirma": ("Veritá confirma", "Veritá confirma"),
"Card de apoiadores 10": ("Supporters card 10", "Card de simpatizantes 10"),
"Apoiadores · 10": ("Supporters · 10", "Simpatizantes · 10"),
"Card de apoiadores 11": ("Supporters card 11", "Card de simpatizantes 11"),
"Apoiadores · 11": ("Supporters · 11", "Simpatizantes · 11"),
"Card de apoiadores 8": ("Supporters card 8", "Card de simpatizantes 8"),
"Apoiadores · 08": ("Supporters · 08", "Simpatizantes · 08"),
"Card de apoiadores 2": ("Supporters card 2", "Card de simpatizantes 2"),
"Apoiadores · 02": ("Supporters · 02", "Simpatizantes · 02"),
"Como escalar sem diluir": ("How to scale without diluting", "Cómo escalar sin diluir"),
"Separar o que é decisão de design do que é repetição.": ("Separate design decisions from repetition.", "Separar lo que es decisión de diseño de lo que es repetición."),
"O perfil oficial foi trabalhado peça por peça. Já a": ("The official profile was crafted piece by piece.", "El perfil oficial se trabajó pieza por pieza. En cambio, la"),
"mobilização": ("Mobilization", "movilización"),
"e o": ("and", "y la"),
"tráfego pago": ("paid media", "pauta paga"),
"pediam volume. A mobilização era disparada por WhatsApp: cards de agenda, adesivaço, caminhada e outros, com pauta mudando de hora em hora. No tráfego, o mesmo recado chegava aos 52 municípios: os carrosséis em formato de feed e as demais peças em 9:16, com a informação blocada na área 1:1, para funcionar em qualquer corte. Somavam-se os cards de debate, que precisavam sair em tempo real. Nesse ritmo, os riscos são três: a peça chegar tarde, a equipe se desgastar em trabalho repetitivo e a identidade se desfazer a cada nova versão. Para essas duas frentes, organizei a produção em três camadas:":
 ("demanded volume. Mobilization went out over WhatsApp: cards for the agenda, sticker drives, campaign walks and more, with the schedule changing by the hour. In paid media, the same message reached all 52 municipalities: carousels in feed format and every other piece in 9:16, with the information locked inside the 1:1 area so it works under any crop. On top of that came the debate cards, which had to go out in real time. At that pace there are three risks: the piece arriving late, the team burning out on repetitive work, and the identity coming apart with each new version. For these two workstreams, I organized production in three layers:",
  "pedían volumen. La movilización se enviaba por WhatsApp: cards de agenda, jornadas de stickers, caminatas y otros, con la agenda cambiando hora a hora. En la pauta paga, el mismo mensaje llegaba a los 52 municipios: los carruseles en formato feed y las demás piezas en 9:16, con la información contenida en el área 1:1, para funcionar con cualquier recorte. A eso se sumaban los cards de debate, que tenían que salir en tiempo real. A ese ritmo, los riesgos son tres: que la pieza llegue tarde, que el equipo se desgaste en trabajo repetitivo y que la identidad se desarme en cada nueva versión. Para estos dos frentes, organicé la producción en tres capas:"),
"01 · Desenho": ("01 · Design", "01 · Diseño"),
"A peça nasce no Figma ou no Photoshop": ("The piece is born in Figma or Photoshop", "La pieza nace en Figma o en Photoshop"),
"Grid, tipografia, cor, foto e hierarquia são decididos por mim, na ferramenta de design.": ("Grid, type, color, photo and hierarchy are decided by me, in the design tool.", "Grilla, tipografía, color, foto y jerarquía los decido yo, en la herramienta de diseño."),
"02 · Regra": ("02 · Rule", "02 · Regla"),
"Cada decisão vira medida": ("Every decision becomes a measurement", "Cada decisión se vuelve medida"),
"Margens, entreletra, onde a linha quebra, o que cresce e para que lado. O auto layout guarda essas regras.": ("Margins, tracking, where the line breaks, what grows and in which direction. Auto layout holds these rules.", "Márgenes, interletrado, dónde corta la línea, qué crece y hacia dónde. El auto layout guarda esas reglas."),
"03 · Ferramenta": ("03 · Tool", "03 · Herramienta"),
"A equipe preenche só o que muda": ("The team fills in only what changes", "El equipo completa solo lo que cambia"),
"Texto, foto, cidade, data. A ferramenta trava a identidade e abre os campos variáveis.": ("Text, photo, town, date. The tool locks the identity and opens the variable fields.", "Texto, foto, ciudad, fecha. La herramienta bloquea la identidad y abre los campos variables."),
"Sobre IA": ("On AI", "Sobre la IA"),
"Da minha parte, nunca houve a decisão de usar IA para gerar imagem ou elemento gráfico nas peças. A IA entrou como par de programação (Claude Code), para escrever as ferramentas e os scripts de produção em lote, e em tarefas mecânicas como recortar a pessoa do fundo da foto.":
 ("On my part, there was never a decision to use AI to generate images or graphic elements in the pieces. AI came in as a programming partner (Claude Code), to write the tools and the batch-production scripts, and for mechanical tasks such as cutting the person out of the photo background.",
  "De mi parte, nunca hubo la decisión de usar IA para generar imágenes o elementos gráficos en las piezas. La IA entró como compañera de programación (Claude Code), para escribir las herramientas y los scripts de producción en lote, y en tareas mecánicas como recortar a la persona del fondo de la foto."),
"Frente 03 / Real time de debates": ("Workstream 03 / Real-time debate coverage", "Frente 03 / Debates en tiempo real"),
"Um estúdio de citação para cada emissora.": ("A quote studio for each broadcaster.", "Un estudio de citas para cada canal."),
"Para cada emissora fiz uma moldura própria no Figma e um estúdio web que a reproduz número por número. Durante a transmissão, o designer cola a frase, escolhe foto e modelo e baixa o card pronto em dois formatos: feed 3:4 e story 9:16. Os cards abaixo foram publicados nas próprias noites de debate, entre 19h e 22h30.":
 ("For each broadcaster I designed a dedicated frame in Figma and a web studio that reproduces it measurement by measurement. During the broadcast, the designer pastes the quote, picks a photo and template, and downloads the finished card in two formats: 3:4 feed and 9:16 story. The cards below were published on the debate nights themselves, between 7 and 10:30 pm.",
  "Para cada canal hice un marco propio en Figma y un estudio web que lo reproduce medida por medida. Durante la transmisión, el diseñador pega la frase, elige foto y plantilla y descarga el card listo en dos formatos: feed 3:4 y story 9:16. Los cards de abajo se publicaron en las mismas noches de debate, entre las 19:00 y las 22:30."),
"A quebra de linha precisa sair igual à do Figma. Por isso o estúdio aplica a mesma tipografia (Work Sans 30 sobre 40, entreletra −4%): sem a entreletra, a frase quebra em outro lugar e o card perde o desenho.":
 ("Line breaks must match Figma exactly. That is why the studio applies the same typography (Work Sans 30 on 40, −4% tracking): without the tracking, the sentence breaks elsewhere and the card loses its shape.",
  "El corte de línea tiene que salir igual que en Figma. Por eso el estudio aplica la misma tipografía (Work Sans 30 sobre 40, interletrado −4%): sin el interletrado, la frase corta en otro lugar y el card pierde su forma."),
"Rondoniaovivotv · 18/09": ("Rondoniaovivotv · Sep 18", "Rondoniaovivotv · 18/09"),
"Azul, azul escuro e branco.": ("Blue, dark blue and white.", "Azul, azul oscuro y blanco."),
"SIC TV | Record · 21/09": ("SIC TV | Record · Sep 21", "SIC TV | Record · 21/09"),
"Layout invertido, texto em cima e bico de balão. Histórico dos últimos 20 cards para reabrir e corrigir.": ("Inverted layout, text on top and a speech-bubble tail. History of the last 20 cards to reopen and fix.", "Layout invertido, texto arriba y pico de globo. Historial de los últimos 20 cards para reabrir y corregir."),
"Rede Amazônica | Globo · 29/09": ("Rede Amazônica | Globo · Sep 29", "Rede Amazônica | Globo · 29/09"),
"Canto de 125 px e adereço no topo, legenda eleitoral já com sombra.": ("125 px corner and a top ornament, electoral caption with a built-in shadow.", "Esquina de 125 px y adorno arriba, leyenda electoral ya con sombra."),
"Grupo SGC · 01/10": ("Grupo SGC · Oct 1", "Grupo SGC · 01/10"),
"Cantos de 50 px na diagonal e aspas em amarelo ou azul, nas quatro combinações.": ("50 px diagonal corners and yellow or blue quotation marks, in all four combinations.", "Esquinas de 50 px en diagonal y comillas en amarillo o azul, en las cuatro combinaciones."),
"Prévia": ("Preview", "Vista previa"),
"A rolagem dá zoom na foto em volta do cursor e o card arrasta na vertical, com um ímã na posição padrão.": ("Scrolling zooms the photo around the cursor and the card drags vertically, snapping to its default position.", "El scroll hace zoom en la foto alrededor del cursor y el card se arrastra en vertical, con imán en la posición estándar."),
"Card de citação publicado no debate de 1º de setembro": ("Quote card published during the September 1 debate", "Card de cita publicado en el debate del 1 de septiembre"),
"01/09 · Estúdio Aspas Debate · publicado 22h25": ("Sep 1 · Aspas Debate studio · posted 10:25 pm", "01/09 · Estudio Aspas Debate · publicado 22:25"),
"Card de citação do debate Rondoniaovivotv": ("Quote card from the Rondoniaovivotv debate", "Card de cita del debate Rondoniaovivotv"),
"18/09 · Rondoniaovivotv · publicado 21h22": ("Sep 18 · Rondoniaovivotv · posted 9:22 pm", "18/09 · Rondoniaovivotv · publicado 21:22"),
"Card de citação do debate SIC TV Record": ("Quote card from the SIC TV Record debate", "Card de cita del debate SIC TV Record"),
"21/09 · SIC TV | Record · publicado 22h25": ("Sep 21 · SIC TV | Record · posted 10:25 pm", "21/09 · SIC TV | Record · publicado 22:25"),
"Card de citação do debate Rede Amazônica Globo": ("Quote card from the Rede Amazônica Globo debate", "Card de cita del debate Rede Amazônica Globo"),
"29/09 · Rede Amazônica | Globo · publicado 22h30": ("Sep 29 · Rede Amazônica | Globo · posted 10:30 pm", "29/09 · Rede Amazônica | Globo · publicado 22:30"),
"Card de citação do debate Grupo SGC": ("Quote card from the Grupo SGC debate", "Card de cita del debate Grupo SGC"),
"01/10 · Grupo SGC · publicado 19h09": ("Oct 1 · Grupo SGC · posted 7:09 pm", "01/10 · Grupo SGC · publicado 19:09"),
"Interface do Estúdio Aspas Rede Amazônica no ar": ("Interface of the live Aspas Rede Amazônica studio", "Interfaz del Estudio Aspas Rede Amazônica online"),
"Estúdio Aspas Rede Amazônica, no ar no GitHub Pages": ("Aspas Rede Amazônica studio, live on GitHub Pages", "Estudio Aspas Rede Amazônica, online en GitHub Pages"),
"Painel que reúne todos os estúdios": ("Dashboard gathering all the studios", "Panel que reúne todos los estudios"),
"Painel dos Estúdios: um endereço para a equipe abrir qualquer ferramenta": ("Studios dashboard: one address for the team to open any tool", "Panel de Estudios: una sola dirección para que el equipo abra cualquier herramienta"),
"Frente 04 / Tráfego pago por município": ("Workstream 04 / Paid media by municipality", "Frente 04 / Pauta paga por municipio"),
"Um modelo, 52 cidades, 495 lâminas.": ("One template, 52 towns, 495 slides.", "Una plantilla, 52 ciudades, 495 láminas."),
"O tráfego pago teve várias frentes ao longo da campanha. A de maior escala foi a regionalização: cada município ganhou um carrossel de até dez lâminas com obras e propostas da cidade. Desenhei um modelo no Figma com auto layout, e as 52 versões saíram dele por edição pela API, conferidas peça por peça.":
 ("Paid media had several workstreams throughout the campaign. The largest in scale was regionalization: each municipality got a carousel of up to ten slides with the town’s projects and proposals. I designed one template in Figma with auto layout, and the 52 versions came out of it through API editing, checked piece by piece.",
  "La pauta paga tuvo varios frentes a lo largo de la campaña. El de mayor escala fue la regionalización: cada municipio recibió un carrusel de hasta diez láminas con obras y propuestas de la ciudad. Diseñé una plantilla en Figma con auto layout, y las 52 versiones salieron de ella por edición vía API, revisadas pieza por pieza."),
"A mesma lógica gerou duas séries por cidade para tráfego em todas as redes (Instagram, Facebook e as demais):": ("The same logic produced two series per town for paid media on every network (Instagram, Facebook and the rest):", "La misma lógica generó dos series por ciudad para pauta en todas las redes (Instagram, Facebook y las demás):"),
"Conheça meu trabalho em {cidade}": ("Conheça meu trabalho em {cidade} (“See my work in {town}”)", "Conheça meu trabalho em {cidade} (“Conocé mi trabajo en {ciudad}”)"),
"e a série Saúde,": ("and the Health series,", "y la serie Salud,"),
"{cidade} merece ser atendida em {cidade}": ("{cidade} merece ser atendida em {cidade} (“{town} deserves care in {town}”)", "{cidade} merece ser atendida em {cidade} (“{ciudad} merece ser atendida en {ciudad}”)"),
". São mais 104 peças, desenhadas em 9:16 com a informação sempre centrada na área 1:1, para resistir a qualquer corte que a plataforma fizesse.": (". That is 104 more pieces, designed in 9:16 with the information always centered in the 1:1 area, to survive any crop the platform applied.", ". Son 104 piezas más, diseñadas en 9:16 con la información siempre centrada en el área 1:1, para resistir cualquier recorte que hiciera la plataforma."),
"Nas séries por município, o bloco do título cresce para cima, preso acima da faixa azul. Nome longo empurra o topo e nunca invade o rodapé.": ("In the per-municipality series, the title block grows upward, anchored above the blue band. A long name pushes the top and never invades the footer.", "En las series por municipio, el bloque del título crece hacia arriba, anclado sobre la franja azul. Un nombre largo empuja el borde superior y nunca invade el pie."),
"Leading trim na altura das maiúsculas: o espaço que o auto layout mede é o espaço que se vê na arte.": ("Leading trim at cap height: the space auto layout measures is the space you see in the artwork.", "Leading trim a la altura de las mayúsculas: el espacio que mide el auto layout es el que se ve en la pieza."),
"Entrelinha e entreletra do nome da cidade em %, para escalar junto com a fonte.": ("Line height and tracking of the town name in %, so they scale with the font.", "Interlineado e interletrado del nombre de la ciudad en %, para escalar junto con la fuente."),
"Largura máxima de 1012 px no nome, para quebrar a linha em vez de sair da peça.": ("1012 px max width on the name, so it breaks the line instead of overflowing the piece.", "Ancho máximo de 1012 px en el nombre, para cortar la línea en vez de salirse de la pieza."),
"Na série Saúde, a largura da fonte (do Condensed ao Expanded) foi escolhida cidade a cidade: menos linhas, sem partir o nome.": ("In the Health series, the font width (from Condensed to Expanded) was chosen town by town: fewer lines, without splitting the name.", "En la serie Salud, el ancho de la fuente (de Condensed a Expanded) se eligió ciudad por ciudad: menos líneas, sin partir el nombre."),
"Jaru, as dez lâminas": ("Jaru, all ten slides", "Jaru, las diez láminas"),
"1080 × 1440 cada · 1 de 52": ("1080 × 1440 each · 1 of 52", "1080 × 1440 cada una · 1 de 52"),
"As 52 capas": ("The 52 covers", "Las 52 portadas"),
"ordem alfabética · Alta Floresta D’Oeste → Vilhena": ("alphabetical · Alta Floresta D’Oeste → Vilhena", "orden alfabético · Alta Floresta D’Oeste → Vilhena"),
"Frente 05 / Mobilização da carreata": ("Workstream 05 / Motorcade mobilization", "Frente 05 / Movilización de la caravana"),
"208 adesivos digitais na véspera da eleição.": ("208 digital stickers on the eve of the election.", "208 stickers digitales en la víspera de la elección."),
"Para a carreata final, cada cidade recebeu quatro adesivos de story:": ("For the final motorcade, each town got four story stickers:", "Para la caravana final, cada ciudad recibió cuatro stickers de story:"),
"Tá fechada com o 22": ("Tá fechada com o 22 (“locked in with 22”)", "Tá fechada com o 22 (“cerrada con el 22”)"),
"Destrava": ("Destrava (“unlock”)", "Destrava (“destrabá”)"),
"Botar pra funcionar": ("Botar pra funcionar (“make it work”)", "Botar pra funcionar (“ponerla a funcionar”)"),
"e": ("and", "y"),
"É Marcos Rogério 22": ("É Marcos Rogério 22 (“it’s Marcos Rogério 22”)", "É Marcos Rogério 22 (“es Marcos Rogério 22”)"),
". Fiz três modelos à mão para cada série, medi as regras deles e o resto foi montado em auto layout em uma manhã.": (". I made three templates by hand for each series, measured their rules, and the rest was assembled in auto layout in one morning.", ". Hice tres modelos a mano para cada serie, medí sus reglas y el resto se armó en auto layout en una mañana."),
"Cada série tem regras próprias, porque o nome da cidade muda tudo: de Jaru, que cabe numa palavra, a Nova Brasilândia D’Oeste.": ("Each series has its own rules, because the town name changes everything: from Jaru, a single word, to Nova Brasilândia D’Oeste.", "Cada serie tiene sus propias reglas, porque el nombre de la ciudad lo cambia todo: de Jaru, que entra en una palabra, a Nova Brasilândia D’Oeste."),
"Faixas de 131 px que abraçam o texto; quebra de linha sem deixar DE, DO ou DA no fim da linha.": ("131 px bands that hug the text; line breaks never leave DE, DO or DA at the end of a line.", "Franjas de 131 px que abrazan el texto; corte de línea sin dejar DE, DO o DA al final de la línea."),
"Nome de uma linha só:": ("Single-line name:", "Nombre de una sola línea:"),
"lado a lado quando a primeira linha passa de 763 px.": ("side by side when the first line exceeds 763 px.", "lado a lado cuando la primera línea supera los 763 px."),
"Grafia dos nomes como no restante do material da cidade.": ("Name spelling matches the rest of each town’s material.", "Grafía de los nombres igual que en el resto del material de la ciudad."),
"A palavra em fonte de pincel é uma fonte local, que a API não carrega: foi clonada do modelo, nunca redigitada.": ("The brush-script word uses a local font the API cannot load: it was cloned from the template, never retyped.", "La palabra en tipografía de pincel es una fuente local que la API no carga: se clonó del modelo, nunca se reescribió."),
"Fundo transparente calculado a partir de duas versões de cada adesivo, sobre preto e sobre branco.": ("Transparent background computed from two versions of each sticker, on black and on white.", "Fondo transparente calculado a partir de dos versiones de cada sticker, sobre negro y sobre blanco."),
"Ji-Paraná, as quatro séries": ("Ji-Paraná, all four series", "Ji-Paraná, las cuatro series"),
"PNG transparente · story sobre foto": ("transparent PNG · story over photo", "PNG transparente · story sobre foto"),
"Adesivo Ji-Paraná tá fechada com o 22": ("Ji-Paraná “locked in with 22” sticker", "Sticker Ji-Paraná cerrada con el 22"),
"Adesivo destrava Ji-Paraná": ("“Unlock Ji-Paraná” sticker", "Sticker destrabá Ji-Paraná"),
"Adesivo botar Ji-Paraná pra funcionar": ("“Make Ji-Paraná work” sticker", "Sticker poner Ji-Paraná a funcionar"),
"Adesivo Ji-Paraná é Marcos Rogério 22": ("“Ji-Paraná is Marcos Rogério 22” sticker", "Sticker Ji-Paraná es Marcos Rogério 22"),
"Série Tá fechada com o 22, 52 cidades": ("“Tá fechada com o 22” series, 52 towns", "Serie Tá fechada com o 22, 52 ciudades"),
"Frente 06 / Ferramentas para a equipe": ("Workstream 06 / Tools for the team", "Frente 06 / Herramientas para el equipo"),
"Nove estúdios web, uma regra: a identidade não abre.": ("Nine web studios, one rule: the identity stays locked.", "Nueve estudios web, una regla: la identidad no se abre."),
"Cada estúdio reproduz em canvas um card que desenhei no Figma, com as medidas tiradas do auto layout. O designer da equipe trabalha no navegador, sem abrir arquivo de design, e só mexe no que pode mudar. Onde não havia custo de servidor, publiquei no GitHub Pages, aberto e fora dos buscadores; onde havia API paga, na Vercel, com senha.":
 ("Each studio reproduces on canvas a card I designed in Figma, with measurements taken from auto layout. Team designers work in the browser, without opening a design file, and only touch what is allowed to change. Where there was no server cost, I published on GitHub Pages, open and hidden from search engines; where there was a paid API, on Vercel, behind a password.",
  "Cada estudio reproduce en canvas un card que diseñé en Figma, con las medidas tomadas del auto layout. El diseñador del equipo trabaja en el navegador, sin abrir archivos de diseño, y solo toca lo que puede cambiar. Donde no había costo de servidor, publiqué en GitHub Pages, abierto y fuera de los buscadores; donde había una API paga, en Vercel, con contraseña."),
"Agenda Rádio e TV": ("Radio & TV agenda", "Agenda Radio y TV"),
"Recorte automático da pessoa e quatro camadas: fundo desfocado, foto nítida, elementos e o recorte por cima, no mesmo registro.": ("Automatic person cutout and four layers: blurred background, sharp photo, elements and the cutout on top, all in register.", "Recorte automático de la persona y cuatro capas: fondo desenfocado, foto nítida, elementos y el recorte encima, en el mismo registro."),
"Saiu na Mídia": ("Saiu na Mídia (in the news)", "Saiu na Mídia (salió en los medios)"),
"O print da notícia entra num card de largura fixa e a altura vem da imagem. Seis modelos.": ("The news screenshot goes into a fixed-width card and the height follows the image. Six templates.", "La captura de la noticia entra en un card de ancho fijo y la altura sale de la imagen. Seis plantillas."),
"Aspas · 5 versões": ("Quotes · 5 versions", "Citas · 5 versiones"),
"Uma para debate geral e uma para cada emissora, com histórico, zoom e arraste na prévia.": ("One for general debates and one per broadcaster, with history, zoom and drag in the preview.", "Una para debates en general y una por canal, con historial, zoom y arrastre en la vista previa."),
"Caminhadas": ("Campaign walks", "Caminatas"),
"Cidade, data e horário da caminhada sobre foto, com histórico dos cards já feitos.": ("Town, date and time of the walk over a photo, with a history of cards already made.", "Ciudad, fecha y horario de la caminata sobre foto, con historial de los cards ya hechos."),
"Adesivaços": ("Sticker drives", "Jornadas de stickers"),
"O bloco de informação cresce para cima a partir do rodapé fixo. Dia, data e horário mudam de cor juntos.": ("The info block grows upward from a fixed footer. Day, date and time change color together.", "El bloque de información crece hacia arriba desde el pie fijo. Día, fecha y horario cambian de color juntos."),
"Painel": ("Dashboard", "Panel"),
"Um endereço só, que lista e abre todos os estúdios. Acrescentar um novo é um item na configuração.": ("A single address that lists and opens every studio. Adding a new one is one item in the config.", "Una sola dirección que lista y abre todos los estudios. Sumar uno nuevo es un ítem en la configuración."),
"Interface do Estúdio de Adesivaços": ("Sticker-drive studio interface", "Interfaz del Estudio de Jornadas de stickers"),
"Estúdio de Adesivaços · card 1080 × 1920 com a guia do corte 3:4 do feed": ("Sticker-drive studio · 1080 × 1920 card with the 3:4 feed crop guide", "Estudio de Jornadas de stickers · card 1080 × 1920 con la guía de recorte 3:4 del feed"),
"Estúdio de Cards da agenda, com o histórico da equipe aberto": ("Agenda card studio, with the team history open", "Estudio de cards de agenda, con el historial del equipo abierto"),
"Estúdio de Agenda Rádio e TV · histórico da equipe com os cards salvos": ("Radio & TV agenda studio · team history with saved cards", "Estudio de Agenda Radio y TV · historial del equipo con los cards guardados"),
"Frente 07 / Revisão e aprovação": ("Workstream 07 / Review and approval", "Frente 07 / Revisión y aprobación"),
"Ver a peça como o público vai ver, antes de postar.": ("See the piece the way the audience will, before posting.", "Ver la pieza como la va a ver el público, antes de publicar."),
"Nuvem de carrosséis": ("Carousel cloud", "Nube de carruseles"),
"Biblioteca no computador que publica cada carrossel num link fixo. Quem recebe abre no celular, sem login; republicar troca o conteúdo e mantém o link.": ("A desktop library that publishes each carousel to a fixed link. Recipients open it on their phone, no login; republishing swaps the content and keeps the link.", "Biblioteca en la computadora que publica cada carrusel en un link fijo. Quien lo recibe lo abre en el celular, sin login; republicar cambia el contenido y mantiene el link."),
"13 carrosséis publicados, 106 lâminas, incluindo vídeo.": ("13 carousels published, 106 slides, including video.", "13 carruseles publicados, 106 láminas, incluido video."),
"Vídeo convertido para H.264 sem perder resolução nem fps, porque o HEVC original ficava preto no Chrome do Android.": ("Video converted to H.264 with no loss of resolution or fps, because the original HEVC showed black in Chrome on Android.", "Video convertido a H.264 sin perder resolución ni fps, porque el HEVC original quedaba negro en Chrome de Android."),
"Miniatura leve para o link chegar com imagem no WhatsApp.": ("Lightweight thumbnail so the link arrives with an image on WhatsApp.", "Miniatura liviana para que el link llegue con imagen en WhatsApp."),
"Simulação fiel ao app": ("True-to-app simulation", "Simulación fiel a la app"),
"O visualizador segue as regras do Instagram: todas as lâminas na proporção da primeira, avanço depois de 28% da largura, encaixe sem efeito de mola.": ("The viewer follows Instagram’s rules: every slide in the first one’s ratio, advance after 28% of the width, snapping with no spring effect.", "El visor sigue las reglas de Instagram: todas las láminas en la proporción de la primera, avance después del 28% del ancho, encastre sin efecto rebote."),
"Preview do perfil no Figma, conferido com print do app: grade 3:4, tema claro e escuro ligados por variáveis. Foi onde os enxovais foram testados antes de ir ao ar.": ("Profile preview in Figma, checked against an app screenshot: 3:4 grid, light and dark themes linked by variables. That is where the profile kits were tested before going live.", "Vista previa del perfil en Figma, comparada con una captura de la app: grilla 3:4, tema claro y oscuro vinculados por variables. Ahí se probaron los kits de perfil antes de salir al aire."),
"Espelho do Photoshop: a peça que está aberta aparece no celular em cerca de meio segundo, sem travar o programa.": ("Photoshop mirror: the open piece shows up on the phone in about half a second, without slowing the app down.", "Espejo de Photoshop: la pieza abierta aparece en el celular en cerca de medio segundo, sin trabar el programa."),
"Uso de inteligência artificial": ("Use of artificial intelligence", "Uso de inteligencia artificial"),
"Onde a IA entrou, e o que ficou comigo.": ("Where AI came in, and what stayed with me.", "Dónde entró la IA, y qué quedó conmigo."),
"Frente": ("Area", "Frente"),
"O que a IA fez": ("What AI did", "Qué hizo la IA"),
"O que ficou com a direção de arte": ("What stayed with art direction", "Qué quedó en la dirección de arte"),
"Linguagem e peças": ("Language and pieces", "Lenguaje y piezas"),
"Nada.": ("Nothing.", "Nada."),
"Estratégia visual, escolha e edição das fotos, enxovais, carrosséis, cards.": ("Visual strategy, photo selection and editing, profile kits, carousels, cards.", "Estrategia visual, elección y edición de fotos, kits de perfil, carruseles, cards."),
"Escreveu o código a partir das medidas e do comportamento que especifiquei.": ("Wrote the code from the measurements and behavior I specified.", "Escribió el código a partir de las medidas y el comportamiento que especifiqué."),
"Layout, tipografia, cor, o que pode e o que não pode mudar, teste com a equipe.": ("Layout, type, color, what can and cannot change, testing with the team.", "Layout, tipografía, color, qué puede y qué no puede cambiar, pruebas con el equipo."),
"Produção em lote no Figma": ("Batch production in Figma", "Producción en lote en Figma"),
"Clonou modelos, trocou textos e montou auto layout pela API.": ("Cloned templates, swapped text and built auto layout via the API.", "Clonó plantillas, cambió textos y armó auto layout vía API."),
"Os modelos, as regras de quebra e de grafia, a conferência de cada peça.": ("The templates, the line-break and spelling rules, checking every piece.", "Las plantillas, las reglas de corte y de grafía, la revisión de cada pieza."),
"Foto nos estúdios": ("Photos in the studios", "Fotos en los estudios"),
"Recortou a pessoa do fundo.": ("Cut the person out of the background.", "Recortó a la persona del fondo."),
"Escolha da foto, enquadramento e composição.": ("Photo choice, framing and composition.", "Elección de la foto, encuadre y composición."),
"Ferramentas no ar": ("Tools in production", "Herramientas online"),
"Versionamento, deploy dos estúdios, conversão de vídeo e miniaturas da nuvem de carrosséis.": ("Versioning, studio deploys, video conversion and thumbnails for the carousel cloud.", "Versionado, deploy de los estudios, conversión de video y miniaturas de la nube de carruseles."),
"Onde cada ferramenta fica hospedada, quem acessa e o que segue para revisão.": ("Where each tool is hosted, who has access and what goes to review.", "Dónde se aloja cada herramienta, quién accede y qué pasa a revisión."),
"Linha do tempo · datas dos arquivos": ("Timeline · file dates (day/month)", "Línea de tiempo · fechas de los archivos"),
"Agosto a outubro.": ("August to October.", "De agosto a octubre."),
"Primeiros carrosséis no perfil: Dia do Estudante e Rota 22.": ("First carousels on the profile: Student’s Day and Rota 22.", "Primeros carruseles en el perfil: Día del Estudiante y Rota 22."),
"Enxoval de lançamento: avatar, capas e destaques. Modelo do carrossel por município começa a ser desenhado.": ("Launch kit: avatar, covers and highlights. Design starts on the per-municipality carousel template.", "Kit de lanzamiento: avatar, portadas y destacadas. Empieza el diseño de la plantilla de carrusel por municipio."),
"Nuvem de carrosséis e simulador no celular.": ("Carousel cloud and phone simulator.", "Nube de carruseles y simulador en el celular."),
"Estúdios de Agenda, Saiu na Mídia, Adesivaços e Aspas; painel único.": ("Agenda, Saiu na Mídia, Sticker-drive and Quote studios; single dashboard.", "Estudios de Agenda, Saiu na Mídia, Jornadas de stickers y Citas; panel único."),
"Primeiro debate com cards em tempo real.": ("First debate with real-time cards.", "Primer debate con cards en tiempo real."),
"Carrosséis Rondônia é 22 e Parceria com os 52 municípios; fixados da biografia e das propostas.": ("“Rondônia é 22” and “Partnership with the 52 municipalities” carousels; pinned biography and proposals.", "Carruseles Rondônia é 22 y Alianza con los 52 municipios; fijados de biografía y propuestas."),
"Séries por município para tráfego: Conheça meu trabalho e Saúde.": ("Per-municipality paid series: “See my work” and Health.", "Series por municipio para pauta: Conocé mi trabajo y Salud."),
"Debate Rondoniaovivotv, com estúdio próprio.": ("Rondoniaovivotv debate, with its own studio.", "Debate Rondoniaovivotv, con estudio propio."),
"Segundo enxoval, com reforço do número.": ("Second profile kit, reinforcing the number.", "Segundo kit de perfil, con refuerzo del número."),
"Debate SIC TV | Record.": ("SIC TV | Record debate.", "Debate SIC TV | Record."),
"Debate Rede Amazônica | Globo. Novo ícone de perfil.": ("Rede Amazônica | Globo debate. New profile picture.", "Debate Rede Amazônica | Globo. Nuevo ícono de perfil."),
"Debate Grupo SGC.": ("Grupo SGC debate.", "Debate Grupo SGC."),
"208 adesivos da carreata final, em uma manhã.": ("208 stickers for the final motorcade, in one morning.", "208 stickers para la caravana final, en una mañana."),
"Eleição. Vitória no primeiro turno.": ("Election. First-round victory.", "Elección. Victoria en primera vuelta."),
"Enxoval de governador eleito: foto oficial e destaques novos.": ("Governor-elect kit: official photo and new highlights.", "Kit de gobernador electo: foto oficial y destacadas nuevas."),
"Competências": ("Skills", "Competencias"),
"O que este trabalho mostra.": ("What this work shows.", "Lo que muestra este trabajo."),
"Direção de arte": ("Art direction", "Dirección de arte"),
"Desdobrar uma identidade existente para o digital e conduzir foto, edição e peças numa linha documental, mais leve e mais humana.": ("Extending an existing identity into digital and leading photography, editing and pieces in a lighter, more human documentary line.", "Desplegar una identidad existente en lo digital y conducir foto, edición y piezas en una línea documental, más liviana y más humana."),
"Design gráfico": ("Graphic design", "Diseño gráfico"),
"Enxovais, carrosséis e cards no Photoshop; cards da página de apoiadores; adesivos com regras por cidade.": ("Profile kits, carousels and cards in Photoshop; supporters page cards; stickers with per-town rules.", "Kits de perfil, carruseles y cards en Photoshop; cards de la página de simpatizantes; stickers con reglas por ciudad."),
"Transformar regras de design em ferramentas e automações com IA: estúdios web, produção em lote no Figma, publicação e revisão no celular.": ("Turning design rules into AI-powered tools and automations: web studios, batch production in Figma, publishing and review on the phone.", "Convertir reglas de diseño en herramientas y automatizaciones con IA: estudios web, producción en lote en Figma, publicación y revisión en el celular."),
"Produção em escala": ("Production at scale", "Producción a escala"),
"Peças por município para tráfego, cards no ritmo dos debates e da mobilização, ferramentas que a equipe usa sem treinamento.": ("Per-municipality paid pieces, cards at the pace of debates and mobilization, tools the team uses without training.", "Piezas por municipio para pauta, cards al ritmo de los debates y de la movilización, herramientas que el equipo usa sin capacitación."),
"Números contados nos arquivos de trabalho em 8 de outubro de 2026: backup do Google Drive, pasta de Photoshop, arquivo do Figma e repositórios das ferramentas. Datas vêm dos arquivos; os horários dos cards de debate vêm do registro de publicação no Instagram.":
 ("Numbers counted from the working files on October 8, 2026: Google Drive backup, Photoshop folder, Figma file and the tools’ repositories. Dates come from the files (shown as day/month); debate card times come from Instagram’s publishing record (Rondônia time).",
  "Números contados en los archivos de trabajo el 8 de octubre de 2026: backup de Google Drive, carpeta de Photoshop, archivo de Figma y repositorios de las herramientas. Las fechas vienen de los archivos (día/mes); los horarios de los cards de debate vienen del registro de publicación de Instagram (hora de Rondônia)."),
"As horas de trabalho manual são uma estimativa feita com os meus tempos de referência para adaptar cada peça à mão: capa do carrossel 5 min, lâminas 2 e 3 5 min cada, demais lâminas 2 min, peça por município e adesivo 3 a 5 min. Total de 2.394 a 3.018 minutos.":
 ("The manual-work hours are an estimate based on my reference times for adapting each piece by hand: carousel cover 5 min, slides 2 and 3 5 min each, other slides 2 min, per-municipality piece and sticker 3 to 5 min. Total of 2,394 to 3,018 minutes.",
  "Las horas de trabajo manual son una estimación hecha con mis tiempos de referencia para adaptar cada pieza a mano: portada del carrusel 5 min, láminas 2 y 3 5 min cada una, demás láminas 2 min, pieza por municipio y sticker 3 a 5 min. Total de 2.394 a 3.018 minutos."),
}

# textos dentro do script (carrosséis e textos alternativos gerados)
JS = [
 ('"Propostas"', ('"Proposals"', '"Propuestas"')),
 ('"fixado no perfil · 08/09"', ('"pinned to profile · Sep 8"', '"fijado en el perfil · 08/09"')),
 ('"Biografia"', ('"Biography"', '"Biografía"')),
 ('"Parceria com os 52 municípios"', ('"Partnership with the 52 municipalities"', '"Alianza con los 52 municipios"')),
 ('"Rondônia é 22"', ('"Rondônia é 22"', '"Rondônia é 22"')),
 ('"06/09"', ('"Sep 6"', '"06/09"')),
 ('"05/09"', ('"Sep 5"', '"05/09"')),
 ('" lâminas"', ('" slides"', '" láminas"')),
 ('" em vídeo, mostradas pelo primeiro quadro"', ('" in video, shown by their first frame"', '" en video, mostradas por su primer cuadro"')),
 ('", lâmina "', ('", slide "', '", lámina "')),
 ('"VÍDEO"', ('"VIDEO"', '"VIDEO"')),
 ('"Jaru, lâmina "', ('"Jaru, slide "', '"Jaru, lámina "')),
 ('"Capa do carrossel de "', ('"Carousel cover for "', '"Portada del carrusel de "')),
 ('" tá fechada com o 22"', ('" locked in with 22"', '" cerrada con el 22"')),
]

LANG = {"en": 0, "es": 1}
SITE = "https://silasrcha.github.io/portfolio-mr22/"

def build(lang):
    k = LANG[lang]
    s = open("index.html", encoding="utf-8").read()
    head_end = s.index("<script>")
    doc, script = s[:head_end], s[head_end:]
    faltando = []
    def tr(txt):
        key = txt.strip()
        if key in T:
            return txt.replace(key, T[key][k])
        return None
    # nós de texto
    def sub_text(m):
        inner = m.group(1)
        if not inner.strip() or not re.search(r"[A-Za-zÀ-ú]", inner):
            return m.group(0)
        out = tr(H.unescape(inner))
        if out is None:
            faltando.append(inner.strip()); return m.group(0)
        return ">" + H.escape(out, quote=False) + "<"
    body_start = doc.index("</style>")
    top, rest = doc[:body_start], doc[body_start:]
    rest = re.sub(r">([^<>]+)<", sub_text, rest)
    # atributos
    def sub_attr(m):
        name, val = m.group(1), m.group(2)
        out = tr(H.unescape(val))
        if out is None:
            if re.search(r"[A-Za-zÀ-ú]{3}", val) and name != "content": faltando.append(val)
            return m.group(0)
        return f'{name}="{H.escape(out, quote=True)}"'
    top = re.sub(r'\b(content|alt|aria-label|title)="([^"]+)"', sub_attr, top)
    rest = re.sub(r'\b(alt|aria-label|title)="([^"]+)"', sub_attr, rest)
    top = re.sub(r">([^<>]+)</title>", lambda m: ">" + (tr(m.group(1)) or m.group(1)) + "</title>", top)
    for a, b in JS:
        assert a in script, a
        script = script.replace(a, b[k])
    out = top + rest + script
    out = out.replace('<html lang="pt-BR">', f'<html lang="{"en" if lang=="en" else "es"}">')
    out = out.replace(f'<meta property="og:url" content="{SITE}">', f'<meta property="og:url" content="{SITE}{lang}.html">')
    out = out.replace('og:locale" content="pt_BR"', f'og:locale" content="{"en_US" if lang=="en" else "es_AR"}"')
    out = out.replace('<a href="./" aria-current="page">PT</a>', '<a href="./">PT</a>')
    out = out.replace(f'<a href="{lang}.html">{lang.upper()}</a>', f'<a href="{lang}.html" aria-current="page">{lang.upper()}</a>')
    out = out.replace("img/og.jpg", f"img/og-{lang}.jpg")
    open(f"{lang}.html", "w", encoding="utf-8").write(out)
    return sorted(set(faltando))

if __name__ == "__main__":
    for lang in ("en", "es"):
        f = build(lang)
        print(lang, "sem tradução:", f)

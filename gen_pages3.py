#!/usr/bin/env python3
"""Generate info pages (foundations, about, faq, contact, booking) + product pages for EN/ES/DE/PT/IT."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gen_pages import (head, nav_full, footer_html, cookie, COMMON_JS, BASE_CSS, NAV_CSS,
                        STRIPE, SYSTEME_CONTACT, SYSTEME_BOOKING, HREFLANG, PROD_DIR, PROD_FILES,
                        PROD_NAMES, write, FONT_LINK, SITE_URL, NAV_LABELS, hreflang)

INFO_CSS = BASE_CSS + NAV_CSS + """
  .page-hero { padding:clamp(6rem,12vw,10rem) 0 clamp(3rem,5vw,4rem); position:relative; overflow:hidden; }
  .page-hero-bg { position:absolute; inset:0; background:radial-gradient(ellipse 60% 60% at 70% 50%, rgba(198,161,110,0.04), transparent); }
  .page-hero-inner { position:relative; z-index:1; max-width:700px; }
  .page-hero .label { display:block; margin-bottom:1.5rem; }
  .page-hero h1 { color:var(--gold); margin-bottom:1.5rem; }
  .page-hero p { color:var(--muted); font-size:clamp(0.95rem,1.6vw,1.1rem); line-height:1.95; }
  .content-section { max-width:800px; }
  .content-section h2 { font-family:var(--serif); font-size:clamp(1.6rem,3vw,2.4rem); color:var(--gold); margin-bottom:1.2rem; }
  .content-section p { color:var(--muted); font-size:clamp(0.88rem,1.4vw,1rem); line-height:1.95; margin-bottom:1.2rem; }
  .content-section .highlight { font-family:var(--serif); font-size:clamp(1.1rem,2vw,1.5rem); color:var(--white); line-height:1.5; font-style:italic; margin:2.5rem 0; padding:1.5rem 2rem; border-left:2px solid var(--gold); background:rgba(198,161,110,0.03); }
  .pillars-grid { display:grid; grid-template-columns:repeat(2,1fr); gap:1px; border:1px solid var(--border2); }
  .pillar-card { padding:2.4rem 2rem; background:var(--black); transition:background 0.3s; }
  .pillar-card:hover { background:rgba(198,161,110,0.02); }
  .pillar-num { font-family:var(--serif); font-size:2.5rem; color:rgba(198,161,110,0.15); line-height:1; margin-bottom:0.8rem; }
  .pillar-card h3 { font-family:var(--serif); font-size:1.25rem; color:var(--gold); margin-bottom:0.7rem; }
  .pillar-card p { font-size:0.85rem; color:var(--muted); line-height:1.8; }
  .team-section { display:grid; grid-template-columns:280px 1fr; gap:5rem; align-items:start; }
  .team-img { width:100%; aspect-ratio:3/4; object-fit:cover; filter:grayscale(20%); }
  .values-list { list-style:none; display:flex; flex-direction:column; gap:0; border:1px solid var(--border2); }
  .values-list li { padding:1.4rem 2rem; border-bottom:1px solid var(--border2); display:flex; align-items:flex-start; gap:1.2rem; transition:background 0.3s; }
  .values-list li:last-child { border-bottom:none; }
  .values-list li:hover { background:rgba(198,161,110,0.02); }
  .values-list li strong { font-family:var(--serif); font-size:1.1rem; color:var(--gold); min-width:180px; flex-shrink:0; }
  .values-list li span { font-size:0.85rem; color:var(--muted); line-height:1.75; }
  .faq-list { max-width:800px; }
  .faq-item { border-bottom:1px solid var(--border2); }
  .faq-item:first-child { border-top:1px solid var(--border2); }
  .faq-q { width:100%; background:transparent; border:none; text-align:left; padding:1.6rem 0; display:flex; align-items:center; justify-content:space-between; gap:1.5rem; cursor:pointer; color:var(--white); font-family:var(--serif); font-size:clamp(1rem,1.8vw,1.25rem); line-height:1.35; }
  .faq-q:hover { color:var(--gold); }
  .faq-icon { flex-shrink:0; width:32px; height:32px; border:1px solid var(--border); display:flex; align-items:center; justify-content:center; transition:transform 0.3s, border-color 0.3s; }
  .faq-icon svg { width:14px; height:14px; stroke:var(--gold); fill:none; stroke-width:1.5; transition:transform 0.3s; }
  .faq-item.open .faq-icon { border-color:var(--gold); }
  .faq-item.open .faq-icon svg { transform:rotate(45deg); }
  .faq-a { max-height:0; overflow:hidden; transition:max-height 0.4s ease; }
  .faq-a-inner { padding:0 0 1.6rem; font-size:0.88rem; color:var(--muted); line-height:1.9; }
  .contact-grid { display:grid; grid-template-columns:1fr 1fr; gap:4rem; }
  .contact-form label { display:block; font-size:0.68rem; letter-spacing:0.16em; text-transform:uppercase; color:var(--gold); margin-bottom:0.5rem; margin-top:1.4rem; }
  .contact-form label:first-of-type { margin-top:0; }
  .contact-form input, .contact-form textarea, .contact-form select { width:100%; background:rgba(255,255,255,0.03); border:1px solid var(--border); color:var(--white); font-family:var(--sans); font-size:0.88rem; font-weight:300; padding:0.9rem 1.1rem; outline:none; transition:border-color 0.3s; }
  .contact-form input:focus, .contact-form textarea:focus { border-color:var(--gold); }
  .contact-form textarea { min-height:140px; resize:vertical; }
  .contact-info { display:flex; flex-direction:column; gap:2rem; }
  .contact-info-item h3 { font-family:var(--sans); font-size:0.72rem; font-weight:500; letter-spacing:0.18em; text-transform:uppercase; color:var(--gold); margin-bottom:0.5rem; }
  .contact-info-item p { color:var(--muted); font-size:0.88rem; line-height:1.75; }
  .booking-section { max-width:700px; margin:0 auto; text-align:center; }
  .booking-section h2 { color:var(--gold); margin-bottom:1.2rem; }
  .booking-section p { color:var(--muted); line-height:1.9; margin-bottom:0.8rem; }
  .booking-steps { display:flex; flex-direction:column; gap:1px; border:1px solid var(--border2); margin:3rem 0; text-align:left; }
  .booking-step { padding:1.5rem 2rem; background:var(--black); display:flex; align-items:center; gap:1.5rem; }
  .booking-step-num { font-family:var(--serif); font-size:2rem; color:rgba(198,161,110,0.2); line-height:1; flex-shrink:0; min-width:2rem; }
  .booking-step-body h3 { font-family:var(--sans); font-size:0.78rem; letter-spacing:0.14em; text-transform:uppercase; color:var(--white); font-weight:400; margin-bottom:0.3rem; }
  .booking-step-body p { font-size:0.82rem; color:var(--muted); line-height:1.7; }
  @media (max-width:768px) {
    .pillars-grid { grid-template-columns:1fr; }
    .team-section { grid-template-columns:1fr; }
    .team-img { max-width:300px; }
    .contact-grid { grid-template-columns:1fr; }
    .values-list li { flex-direction:column; gap:0.5rem; }
    .values-list li strong { min-width:auto; }
  }
"""

def nav_js():
    return """<script>function toggleMobileNav(){var btn=document.getElementById('navToggle');var menu=document.getElementById('navMobile');btn.classList.toggle('open');menu.classList.toggle('open');btn.setAttribute('aria-expanded',menu.classList.contains('open'));}</script>"""

# ─────────────────────────────────────────────────────────────────────────────
# FOUNDATIONS PAGE
# ─────────────────────────────────────────────────────────────────────────────

FOND_CONTENT = {
    "en": {
        "slug":"foundations.html","title":"Foundations","label":"Foundations",
        "h1":"The foundations of an AI-driven business",
        "intro":"Before you automate, you must understand. Before you scale, you must build. Kemora Agency's Foundations introduce you to the principles that guide every system, every resource, every strategy we develop.",
        "s1_h":"Why AI changes everything","s1_p":"Artificial intelligence is not just a new tool — it is a new paradigm. The businesses that will thrive in the next decade are those that have understood this now, and have built their systems accordingly. Not by following trends, but by adopting a fundamentally different way of thinking about growth, time and leverage.",
        "quote":"The question is not whether to use AI. It is whether your business is designed to benefit from it.",
        "s2_h":"The Kemora approach",
        "p1_title":"Mental clarity","p1_p":"Everything begins with posture. Your ability to make effective decisions, build coherent systems and scale without burning out depends on how you think — before you act.",
        "p2_title":"Intentional execution","p2_p":"A strategy only has value when it is executed. We give you the frameworks, protocols and templates to move from idea to action in a structured, repeatable and measurable way.",
        "p3_title":"Intelligent automation","p3_p":"Delegate to AI what can be delegated. Build systems that generate results for you — day and night, without direct intervention from you at every step.",
        "p4_title":"A scalable ecosystem","p4_p":"Assemble everything into a coherent whole. An operating system for your business that grows with you, without requiring you to work harder — only smarter.",
        "s3_h":"Our commitment",
        "s3_p1":"Kemora Agency was not created to add complexity to your life. Every resource, every system, every programme we create responds to a simple standard: does it produce measurable results for the person who uses it?",
        "s3_p2":"No superfluous theory. No vague advice. Tools that work, applied by people who have thought through every detail.",
    },
    "es": {
        "slug":"fundaciones.html","title":"Fundaciones","label":"Fundaciones",
        "h1":"Las fundaciones de un negocio orientado a la IA",
        "intro":"Antes de automatizar, hay que comprender. Antes de escalar, hay que construir. Las Fundaciones de Kemora Agency le introducen a los principios que guían cada sistema, cada recurso y cada estrategia que desarrollamos.",
        "s1_h":"Por qué la IA lo cambia todo","s1_p":"La inteligencia artificial no es simplemente una nueva herramienta — es un nuevo paradigma. Los negocios que prosperarán en la próxima década son los que han comprendido esto ahora y han construido sus sistemas en consecuencia. No siguiendo tendencias, sino adoptando una forma fundamentalmente diferente de pensar sobre el crecimiento, el tiempo y el apalancamiento.",
        "quote":"La pregunta no es si usar la IA. Es si su negocio está diseñado para beneficiarse de ella.",
        "s2_h":"El enfoque Kemora",
        "p1_title":"Claridad mental","p1_p":"Todo comienza con la postura. Su capacidad para tomar decisiones efectivas, construir sistemas coherentes y escalar sin agotarse depende de cómo piensa — antes de actuar.",
        "p2_title":"Ejecución intencional","p2_p":"Una estrategia solo tiene valor cuando se ejecuta. Le proporcionamos los marcos, protocolos y plantillas para pasar de la idea a la acción de forma estructurada, repetible y medible.",
        "p3_title":"Automatización inteligente","p3_p":"Delegar a la IA lo que puede ser delegado. Construir sistemas que generen resultados para usted — día y noche, sin intervención directa suya en cada paso.",
        "p4_title":"Un ecosistema escalable","p4_p":"Ensamblar todo en un conjunto coherente. Un sistema operativo para su negocio que crece con usted, sin requerir que trabaje más — solo con más inteligencia.",
        "s3_h":"Nuestro compromiso",
        "s3_p1":"Kemora Agency no fue creado para añadir complejidad a su vida. Cada recurso, cada sistema, cada programa que creamos responde a un estándar simple: ¿produce resultados medibles para la persona que lo usa?",
        "s3_p2":"Sin teoría superflua. Sin consejos vagos. Herramientas que funcionan, aplicadas por personas que han pensado en cada detalle.",
    },
    "de": {
        "slug":"grundlagen.html","title":"Grundlagen","label":"Grundlagen",
        "h1":"Die Grundlagen eines KI-gesteuerten Unternehmens",
        "intro":"Bevor Sie automatisieren, müssen Sie verstehen. Bevor Sie skalieren, müssen Sie aufbauen. Die Grundlagen von Kemora Agency führen Sie in die Prinzipien ein, die jedes System, jede Ressource und jede Strategie, die wir entwickeln, leiten.",
        "s1_h":"Warum KI alles verändert","s1_p":"Künstliche Intelligenz ist nicht nur ein neues Werkzeug — sie ist ein neues Paradigma. Die Unternehmen, die im nächsten Jahrzehnt erfolgreich sein werden, sind diejenigen, die dies jetzt verstanden haben und ihre Systeme entsprechend aufgebaut haben. Nicht durch das Verfolgen von Trends, sondern durch die Übernahme einer grundlegend anderen Denkweise über Wachstum, Zeit und Hebelwirkung.",
        "quote":"Die Frage ist nicht, ob man KI einsetzen soll. Sondern ob Ihr Unternehmen darauf ausgerichtet ist, davon zu profitieren.",
        "s2_h":"Der Kemora-Ansatz",
        "p1_title":"Mentale Klarheit","p1_p":"Alles beginnt mit der Haltung. Ihre Fähigkeit, effektive Entscheidungen zu treffen, kohärente Systeme aufzubauen und zu skalieren, ohne auszubrennen, hängt davon ab, wie Sie denken — bevor Sie handeln.",
        "p2_title":"Intentionale Ausführung","p2_p":"Eine Strategie hat nur dann Wert, wenn sie ausgeführt wird. Wir geben Ihnen die Frameworks, Protokolle und Templates, um von der Idee zur Aktion zu gelangen — strukturiert, wiederholbar und messbar.",
        "p3_title":"Intelligente Automatisierung","p3_p":"Delegieren Sie an KI, was delegiert werden kann. Bauen Sie Systeme auf, die für Sie Ergebnisse generieren — Tag und Nacht, ohne Ihr direktes Eingreifen bei jedem Schritt.",
        "p4_title":"Ein skalierbares Ökosystem","p4_p":"Alles zu einem kohärenten Ganzen zusammenfügen. Ein Betriebssystem für Ihr Unternehmen, das mit Ihnen wächst, ohne dass Sie härter arbeiten müssen — nur intelligenter.",
        "s3_h":"Unser Engagement",
        "s3_p1":"Kemora Agency wurde nicht gegründet, um Ihr Leben komplexer zu machen. Jede Ressource, jedes System, jedes Programm, das wir erstellen, entspricht einem einfachen Standard: Erzeugt es messbare Ergebnisse für die Person, die es nutzt?",
        "s3_p2":"Keine überflüssige Theorie. Kein vager Rat. Tools, die funktionieren, angewendet von Menschen, die jeden Detail durchdacht haben.",
    },
    "pt": {
        "slug":"fundacoes.html","title":"Fundações","label":"Fundações",
        "h1":"As fundações de um negócio orientado pela IA",
        "intro":"Antes de automatizar, é preciso compreender. Antes de escalar, é preciso construir. As Fundações da Kemora Agency introduzem-no nos princípios que guiam cada sistema, cada recurso e cada estratégia que desenvolvemos.",
        "s1_h":"Por que a IA muda tudo","s1_p":"A inteligência artificial não é apenas uma nova ferramenta — é um novo paradigma. Os negócios que prosperarão na próxima década são os que compreenderam isso agora e construíram os seus sistemas em conformidade. Não seguindo tendências, mas adotando uma forma fundamentalmente diferente de pensar sobre crescimento, tempo e alavancagem.",
        "quote":"A questão não é se deve usar a IA. É se o seu negócio está concebido para beneficiar dela.",
        "s2_h":"A abordagem Kemora",
        "p1_title":"Clareza mental","p1_p":"Tudo começa com a postura. A sua capacidade de tomar decisões eficazes, construir sistemas coerentes e escalar sem se esgotar depende de como pensa — antes de agir.",
        "p2_title":"Execução intencional","p2_p":"Uma estratégia só tem valor quando é executada. Fornecemos os frameworks, protocolos e templates para passar da ideia à ação de forma estruturada, repetível e mensurável.",
        "p3_title":"Automatização inteligente","p3_p":"Delegar à IA o que pode ser delegado. Construir sistemas que gerem resultados para si — dia e noite, sem a sua intervenção direta em cada passo.",
        "p4_title":"Um ecossistema escalável","p4_p":"Reunir tudo num conjunto coerente. Um sistema operacional para o seu negócio que cresce consigo, sem exigir que trabalhe mais — apenas com mais inteligência.",
        "s3_h":"O nosso compromisso",
        "s3_p1":"A Kemora Agency não foi criada para adicionar complexidade à sua vida. Cada recurso, cada sistema, cada programa que criamos responde a um padrão simples: produz resultados mensuráveis para a pessoa que o utiliza?",
        "s3_p2":"Sem teoria supérflua. Sem conselhos vagos. Ferramentas que funcionam, aplicadas por pessoas que pensaram em cada detalhe.",
    },
    "it": {
        "slug":"fondamenta.html","title":"Fondamenta","label":"Fondamenta",
        "h1":"Le fondamenta di un'attività orientata all'IA",
        "intro":"Prima di automatizzare, bisogna comprendere. Prima di scalare, bisogna costruire. Le Fondamenta di Kemora Agency La introducono ai principi che guidano ogni sistema, ogni risorsa e ogni strategia che sviluppiamo.",
        "s1_h":"Perché l'IA cambia tutto","s1_p":"L'intelligenza artificiale non è semplicemente un nuovo strumento — è un nuovo paradigma. Le attività che prospereranno nel prossimo decennio sono quelle che hanno compreso questo ora e hanno costruito i propri sistemi di conseguenza. Non seguendo le tendenze, ma adottando un modo fondamentalmente diverso di pensare alla crescita, al tempo e alla leva.",
        "quote":"La domanda non è se usare l'IA. È se la Sua attività è progettata per trarne vantaggio.",
        "s2_h":"L'approccio Kemora",
        "p1_title":"Chiarezza mentale","p1_p":"Tutto inizia con la postura. La Sua capacità di prendere decisioni efficaci, costruire sistemi coerenti e scalare senza esaurirsi dipende da come pensa — prima di agire.",
        "p2_title":"Esecuzione intenzionale","p2_p":"Una strategia ha valore solo quando viene eseguita. Le forniamo i framework, i protocolli e i template per passare dall'idea all'azione in modo strutturato, ripetibile e misurabile.",
        "p3_title":"Automatizzazione intelligente","p3_p":"Delegare all'IA ciò che può essere delegato. Costruire sistemi che generino risultati per Lei — giorno e notte, senza il Suo intervento diretto a ogni passo.",
        "p4_title":"Un ecosistema scalabile","p4_p":"Assemblare tutto in un insieme coerente. Un sistema operativo per la Sua attività che cresce con Lei, senza richiedere di lavorare di più — solo in modo più intelligente.",
        "s3_h":"Il nostro impegno",
        "s3_p1":"Kemora Agency non è stata creata per aggiungere complessità alla Sua vita. Ogni risorsa, ogni sistema, ogni programma che creiamo risponde a uno standard semplice: produce risultati misurabili per la persona che lo utilizza?",
        "s3_p2":"Nessuna teoria superflua. Nessun consiglio vago. Strumenti che funzionano, applicati da persone che hanno pensato a ogni dettaglio.",
    },
}

def make_fondations(lang):
    c = FOND_CONTENT[lang]
    nav = nav_full(lang, "fondations")
    html = head(lang, c["title"], c["intro"][:160], c["slug"], "fondations")
    html += f"\n<style>\n{INFO_CSS}\n</style>\n</head>\n<body id=\"main\">\n{nav}\n"
    html += f"""
<section class="page-hero">
  <div class="page-hero-bg"></div>
  <div class="container">
    <div class="page-hero-inner">
      <span class="label reveal">{c["label"]}</span>
      <h1 class="reveal reveal-delay-1">{c["h1"]}</h1>
      <p class="reveal reveal-delay-2">{c["intro"]}</p>
    </div>
  </div>
</section>
<div class="divider-h container"></div>
<section class="section">
  <div class="container">
    <div class="content-section">
      <h2 class="reveal">{c["s1_h"]}</h2>
      <p class="reveal reveal-delay-1">{c["s1_p"]}</p>
      <blockquote class="highlight reveal reveal-delay-2">{c["quote"]}</blockquote>
    </div>
  </div>
</section>
<div class="divider-h container"></div>
<section class="section" style="background:var(--black2);">
  <div class="container">
    <h2 class="reveal" style="text-align:center;max-width:600px;margin:0 auto 3.5rem;">{c["s2_h"]}</h2>
    <div class="pillars-grid">
      <div class="pillar-card reveal"><div class="pillar-num">01</div><h3>{c["p1_title"]}</h3><p>{c["p1_p"]}</p></div>
      <div class="pillar-card reveal reveal-delay-1"><div class="pillar-num">02</div><h3>{c["p2_title"]}</h3><p>{c["p2_p"]}</p></div>
      <div class="pillar-card reveal reveal-delay-2"><div class="pillar-num">03</div><h3>{c["p3_title"]}</h3><p>{c["p3_p"]}</p></div>
      <div class="pillar-card reveal reveal-delay-3"><div class="pillar-num">04</div><h3>{c["p4_title"]}</h3><p>{c["p4_p"]}</p></div>
    </div>
  </div>
</section>
<div class="divider-h container"></div>
<section class="section">
  <div class="container">
    <div class="content-section">
      <h2 class="reveal">{c["s3_h"]}</h2>
      <p class="reveal reveal-delay-1">{c["s3_p1"]}</p>
      <p class="reveal reveal-delay-2">{c["s3_p2"]}</p>
    </div>
  </div>
</section>
{footer_html(lang)}
{cookie(lang)}
{COMMON_JS}
{nav_js()}
</body></html>"""
    return html, c["slug"]

# ─────────────────────────────────────────────────────────────────────────────
# ABOUT PAGE
# ─────────────────────────────────────────────────────────────────────────────

ABOUT_CONTENT = {
    "en": {
        "slug":"about.html","title":"About","label":"About Kemora Agency",
        "h1":"A vision.<br>An <em>ecosystem</em>.",
        "intro":"Kemora Agency was born from a simple observation: most entrepreneurs have everything it takes to build a remarkable business — except the systems that would allow them to fully leverage it.",
        "s1_h":"Our story",
        "s1_p1":"The digital world evolves at a pace that makes it difficult to stay relevant without a rigorous approach. AI has changed the rules. Those who understand this early will have a structural advantage that only grows over time.",
        "s1_p2":"Kemora Agency was created to give entrepreneurs this advantage — through premium training, turnkey AI systems, and a clear methodology that goes from mental posture to full automation.",
        "s2_h":"Our values",
        "v1_t":"Excellence","v1_p":"Every resource, every system, every word is designed with the same level of requirement. We do not deliver work that does not meet our standard.",
        "v2_t":"Clarity","v2_p":"Complexity is the enemy of execution. We make every concept accessible, every tool usable, every strategy applicable — without simplifying what must remain rigorous.",
        "v3_t":"Integrity","v3_p":"We only recommend what we apply ourselves. No empty promises, no inflated claims. We speak in results.",
        "v4_t":"Long-term impact","v4_p":"We are not interested in short-term tactics. We build systems designed to generate value over time — regardless of trends.",
        "s3_h":"Our mission",
        "s3_p":"Give every entrepreneur the tools, methods and systems to build a business that truly works for them — not against them.",
    },
    "es": {
        "slug":"sobre-nosotros.html","title":"Sobre Nosotros","label":"Sobre Kemora Agency",
        "h1":"Una visión.<br>Un <em>ecosistema</em>.",
        "intro":"Kemora Agency nació de una observación simple: la mayoría de los emprendedores tienen todo lo necesario para construir un negocio notable — excepto los sistemas que les permitirían aprovecharlo plenamente.",
        "s1_h":"Nuestra historia",
        "s1_p1":"El mundo digital evoluciona a un ritmo que hace difícil mantenerse relevante sin un enfoque riguroso. La IA ha cambiado las reglas. Los que comprendan esto temprano tendrán una ventaja estructural que solo crece con el tiempo.",
        "s1_p2":"Kemora Agency fue creado para dar a los emprendedores esta ventaja — a través de formaciones premium, sistemas IA listos para usar y una metodología clara que va de la postura mental a la automatización completa.",
        "s2_h":"Nuestros valores",
        "v1_t":"Excelencia","v1_p":"Cada recurso, cada sistema, cada palabra está diseñado con el mismo nivel de exigencia. No entregamos un trabajo que no cumpla con nuestro estándar.",
        "v2_t":"Claridad","v2_p":"La complejidad es el enemigo de la ejecución. Hacemos que cada concepto sea accesible, cada herramienta utilizable, cada estrategia aplicable — sin simplificar lo que debe seguir siendo riguroso.",
        "v3_t":"Integridad","v3_p":"Solo recomendamos lo que aplicamos nosotros mismos. Sin promesas vacías, sin afirmaciones exageradas. Hablamos en resultados.",
        "v4_t":"Impacto a largo plazo","v4_p":"No nos interesan las tácticas a corto plazo. Construimos sistemas diseñados para generar valor con el tiempo — independientemente de las tendencias.",
        "s3_h":"Nuestra misión",
        "s3_p":"Dar a cada emprendedor las herramientas, métodos y sistemas para construir un negocio que realmente trabaje para ellos — no en su contra.",
    },
    "de": {
        "slug":"ueber-uns.html","title":"Über Uns","label":"Über Kemora Agency",
        "h1":"Eine Vision.<br>Ein <em>Ökosystem</em>.",
        "intro":"Kemora Agency entstand aus einer einfachen Beobachtung: Die meisten Unternehmer haben alles, was es braucht, um ein bemerkenswertes Unternehmen aufzubauen — außer den Systemen, die es ihnen ermöglichen würden, es vollständig zu nutzen.",
        "s1_h":"Unsere Geschichte",
        "s1_p1":"Die digitale Welt entwickelt sich so schnell, dass es schwierig ist, ohne einen rigorosen Ansatz relevant zu bleiben. KI hat die Regeln verändert. Wer dies frühzeitig versteht, wird einen strukturellen Vorteil haben, der mit der Zeit nur wächst.",
        "s1_p2":"Kemora Agency wurde gegründet, um Unternehmern diesen Vorteil zu verschaffen — durch Premium-Schulungen, schlüsselfertige KI-Systeme und eine klare Methodik, die von der mentalen Haltung bis zur vollständigen Automatisierung reicht.",
        "s2_h":"Unsere Werte",
        "v1_t":"Exzellenz","v1_p":"Jede Ressource, jedes System, jedes Wort ist mit demselben Anspruchsniveau gestaltet. Wir liefern keine Arbeit ab, die unserem Standard nicht entspricht.",
        "v2_t":"Klarheit","v2_p":"Komplexität ist der Feind der Ausführung. Wir machen jeden Begriff zugänglich, jedes Werkzeug nutzbar, jede Strategie anwendbar — ohne zu vereinfachen, was rigoros bleiben muss.",
        "v3_t":"Integrität","v3_p":"Wir empfehlen nur, was wir selbst anwenden. Keine leeren Versprechen, keine aufgeblähten Behauptungen. Wir sprechen in Ergebnissen.",
        "v4_t":"Langfristiger Einfluss","v4_p":"Wir interessieren uns nicht für kurzfristige Taktiken. Wir bauen Systeme auf, die darauf ausgelegt sind, über die Zeit Wert zu generieren — unabhängig von Trends.",
        "s3_h":"Unsere Mission",
        "s3_p":"Jedem Unternehmer die Werkzeuge, Methoden und Systeme geben, um ein Unternehmen aufzubauen, das wirklich für ihn arbeitet — nicht gegen ihn.",
    },
    "pt": {
        "slug":"sobre-nos.html","title":"Sobre Nós","label":"Sobre a Kemora Agency",
        "h1":"Uma visão.<br>Um <em>ecossistema</em>.",
        "intro":"A Kemora Agency nasceu de uma observação simples: a maioria dos empreendedores tem tudo o que é necessário para construir um negócio notável — exceto os sistemas que lhes permitiriam aproveitá-lo plenamente.",
        "s1_h":"A nossa história",
        "s1_p1":"O mundo digital evolui a um ritmo que torna difícil manter-se relevante sem uma abordagem rigorosa. A IA mudou as regras. Os que compreenderem isso cedo terão uma vantagem estrutural que só cresce com o tempo.",
        "s1_p2":"A Kemora Agency foi criada para dar aos empreendedores esta vantagem — através de formações premium, sistemas de IA prontos a usar e uma metodologia clara que vai da postura mental à automatização completa.",
        "s2_h":"Os nossos valores",
        "v1_t":"Excelência","v1_p":"Cada recurso, cada sistema, cada palavra é concebido com o mesmo nível de exigência. Não entregamos trabalho que não corresponda ao nosso padrão.",
        "v2_t":"Clareza","v2_p":"A complexidade é a inimiga da execução. Tornamos cada conceito acessível, cada ferramenta utilizável, cada estratégia aplicável — sem simplificar o que deve permanecer rigoroso.",
        "v3_t":"Integridade","v3_p":"Só recomendamos o que aplicamos nós mesmos. Sem promessas vazias, sem afirmações exageradas. Falamos em resultados.",
        "v4_t":"Impacto a longo prazo","v4_p":"Não nos interessam as táticas a curto prazo. Construímos sistemas concebidos para gerar valor ao longo do tempo — independentemente das tendências.",
        "s3_h":"A nossa missão",
        "s3_p":"Dar a cada empreendedor as ferramentas, métodos e sistemas para construir um negócio que realmente trabalhe para ele — não contra ele.",
    },
    "it": {
        "slug":"chi-siamo.html","title":"Chi Siamo","label":"Chi è Kemora Agency",
        "h1":"Una visione.<br>Un <em>ecosistema</em>.",
        "intro":"Kemora Agency è nata da una semplice osservazione: la maggior parte degli imprenditori ha tutto il necessario per costruire un'attività notevole — tranne i sistemi che gli permetterebbero di sfruttarla appieno.",
        "s1_h":"La nostra storia",
        "s1_p1":"Il mondo digitale evolve a un ritmo che rende difficile rimanere rilevanti senza un approccio rigoroso. L'IA ha cambiato le regole. Chi lo capisce prima avrà un vantaggio strutturale che cresce solo nel tempo.",
        "s1_p2":"Kemora Agency è stata creata per dare agli imprenditori questo vantaggio — attraverso formazioni premium, sistemi IA chiavi in mano e una metodologia chiara che va dalla postura mentale all'automatizzazione completa.",
        "s2_h":"I nostri valori",
        "v1_t":"Eccellenza","v1_p":"Ogni risorsa, ogni sistema, ogni parola è progettata con lo stesso livello di esigenza. Non consegniamo lavoro che non soddisfi il nostro standard.",
        "v2_t":"Chiarezza","v2_p":"La complessità è nemica dell'esecuzione. Rendiamo ogni concetto accessibile, ogni strumento utilizzabile, ogni strategia applicabile — senza semplificare ciò che deve rimanere rigoroso.",
        "v3_t":"Integrità","v3_p":"Consigliamo solo ciò che applichiamo noi stessi. Nessuna promessa vuota, nessuna affermazione gonfiata. Parliamo in risultati.",
        "v4_t":"Impatto a lungo termine","v4_p":"Non ci interessano le tattiche a breve termine. Costruiamo sistemi progettati per generare valore nel tempo — indipendentemente dalle tendenze.",
        "s3_h":"La nostra missione",
        "s3_p":"Dare ad ogni imprenditore gli strumenti, i metodi e i sistemi per costruire un'attività che lavori davvero per lui — non contro di lui.",
    },
}

def make_about(lang):
    c = ABOUT_CONTENT[lang]
    nav = nav_full(lang, "about")
    html = head(lang, c["title"], c["intro"][:160], c["slug"], "about")
    html += f"\n<style>\n{INFO_CSS}\n</style>\n</head>\n<body id=\"main\">\n{nav}\n"
    html += f"""
<section class="page-hero">
  <div class="page-hero-bg"></div>
  <div class="container">
    <div class="page-hero-inner">
      <span class="label reveal">{c["label"]}</span>
      <h1 class="reveal reveal-delay-1">{c["h1"]}</h1>
      <p class="reveal reveal-delay-2">{c["intro"]}</p>
    </div>
  </div>
</section>
<div class="divider-h container"></div>
<section class="section">
  <div class="container">
    <div class="content-section">
      <h2 class="reveal">{c["s1_h"]}</h2>
      <p class="reveal reveal-delay-1">{c["s1_p1"]}</p>
      <p class="reveal reveal-delay-2">{c["s1_p2"]}</p>
    </div>
  </div>
</section>
<div class="divider-h container"></div>
<section class="section" style="background:var(--black2);">
  <div class="container">
    <h2 class="reveal" style="margin-bottom:2.5rem;">{c["s2_h"]}</h2>
    <ul class="values-list">
      <li class="reveal"><strong>{c["v1_t"]}</strong><span>{c["v1_p"]}</span></li>
      <li class="reveal reveal-delay-1"><strong>{c["v2_t"]}</strong><span>{c["v2_p"]}</span></li>
      <li class="reveal reveal-delay-2"><strong>{c["v3_t"]}</strong><span>{c["v3_p"]}</span></li>
      <li class="reveal reveal-delay-3"><strong>{c["v4_t"]}</strong><span>{c["v4_p"]}</span></li>
    </ul>
  </div>
</section>
<div class="divider-h container"></div>
<section class="section">
  <div class="container">
    <div class="content-section">
      <h2 class="reveal">{c["s3_h"]}</h2>
      <p class="reveal reveal-delay-1" style="font-family:var(--serif);font-size:clamp(1.1rem,2vw,1.5rem);font-style:italic;color:var(--gold);">{c["s3_p"]}</p>
    </div>
  </div>
</section>
{footer_html(lang)}
{cookie(lang)}
{COMMON_JS}
{nav_js()}
</body></html>"""
    return html, c["slug"]

# ─────────────────────────────────────────────────────────────────────────────
# FAQ PAGE
# ─────────────────────────────────────────────────────────────────────────────

FAQ_CONTENT = {
    "en": {
        "slug":"faq.html","title":"FAQ","label":"Frequently Asked Questions",
        "h1":"Frequently Asked Questions",
        "intro":"Everything you need to know before taking the plunge.",
        "faqs":[
            ("Who are Kemora Agency's resources for?","For any entrepreneur, freelancer or manager who wants to use AI to make their business more efficient, scalable and autonomous — regardless of their current level of technical knowledge."),
            ("Do I need to be technically proficient to benefit from the resources?","No. Each resource is designed to be applicable immediately, whatever your level. The AI tools we recommend require no specific technical knowledge."),
            ("What is the difference between the products?","Each product corresponds to a stage in the Kemora progression — from mental posture (Le Cadre Mental) to the complete ecosystem (Kemora OS IA). You can start where you are and progress at your own pace."),
            ("How do I access the resources after purchase?","Immediately after payment, you receive an e-mail containing access to your resource. Access is immediate and does not expire."),
            ("Is there a satisfaction guarantee?","Each product is designed to produce results. If you have applied the method and see no results, contact us — we will find a solution together."),
            ("Can I purchase multiple products?","Yes. The products are designed as a coherent progression. Each product purchased also provides a preferential offer for the next step."),
            ("What does a strategic call consist of?","A 30-45 minute call to identify your situation, your objectives and the starting point most suited to your journey. There is no commitment on your part."),
            ("In what languages are the resources available?","The resources are produced and delivered in French. The website is available in 6 languages for your convenience."),
        ]
    },
    "es": {
        "slug":"preguntas-frecuentes.html","title":"Preguntas Frecuentes","label":"Preguntas Frecuentes",
        "h1":"Preguntas Frecuentes",
        "intro":"Todo lo que necesita saber antes de dar el paso.",
        "faqs":[
            ("¿A quién van dirigidos los recursos de Kemora Agency?","A cualquier emprendedor, freelance o directivo que desee utilizar la IA para hacer su negocio más eficiente, escalable y autónomo — independientemente de su nivel técnico actual."),
            ("¿Necesito conocimientos técnicos para beneficiarme de los recursos?","No. Cada recurso está diseñado para ser aplicable de forma inmediata, cualquiera que sea su nivel. Las herramientas de IA que recomendamos no requieren conocimientos técnicos específicos."),
            ("¿Cuál es la diferencia entre los productos?","Cada producto corresponde a una etapa de la progresión Kemora — desde la postura mental (Le Cadre Mental) hasta el ecosistema completo (Kemora OS IA). Puede empezar donde está y progresar a su propio ritmo."),
            ("¿Cómo accedo a los recursos después de la compra?","Inmediatamente después del pago, recibirá un correo electrónico con acceso a su recurso. El acceso es inmediato y no caduca."),
            ("¿Hay alguna garantía de satisfacción?","Cada producto está diseñado para producir resultados. Si ha aplicado el método y no ve ningún resultado, contáctenos — encontraremos una solución juntos."),
            ("¿Puedo adquirir varios productos?","Sí. Los productos están diseñados como una progresión coherente. Cada producto adquirido proporciona también una oferta preferencial para el siguiente paso."),
            ("¿En qué consiste una llamada estratégica?","Una llamada de 30-45 minutos para identificar su situación, sus objetivos y el punto de partida más adecuado para su trayectoria. Sin compromiso de su parte."),
            ("¿En qué idiomas están disponibles los recursos?","Los recursos se producen y entregan en francés. El sitio web está disponible en 6 idiomas para su comodidad."),
        ]
    },
    "de": {
        "slug":"haeufige-fragen.html","title":"Häufige Fragen","label":"Häufig gestellte Fragen",
        "h1":"Häufig gestellte Fragen",
        "intro":"Alles, was Sie wissen müssen, bevor Sie den Schritt wagen.",
        "faqs":[
            ("Für wen sind die Ressourcen von Kemora Agency?","Für jeden Unternehmer, Freiberufler oder Manager, der KI nutzen möchte, um sein Unternehmen effizienter, skalierbarer und autonomer zu machen — unabhängig von seinem aktuellen technischen Kenntnisstand."),
            ("Muss ich technisch versiert sein, um von den Ressourcen zu profitieren?","Nein. Jede Ressource ist so konzipiert, dass sie sofort anwendbar ist, egal auf welchem Niveau Sie sind. Die von uns empfohlenen KI-Tools erfordern keine spezifischen technischen Kenntnisse."),
            ("Was ist der Unterschied zwischen den Produkten?","Jedes Produkt entspricht einer Stufe in der Kemora-Progression — von der mentalen Haltung (Le Cadre Mental) bis zum vollständigen Ökosystem (Kemora OS IA). Sie können dort beginnen, wo Sie sind, und in Ihrem eigenen Tempo voranschreiten."),
            ("Wie greife ich nach dem Kauf auf die Ressourcen zu?","Unmittelbar nach der Zahlung erhalten Sie eine E-Mail mit dem Zugang zu Ihrer Ressource. Der Zugang ist sofort und läuft nicht ab."),
            ("Gibt es eine Zufriedenheitsgarantie?","Jedes Produkt ist darauf ausgelegt, Ergebnisse zu erzielen. Wenn Sie die Methode angewendet haben und keine Ergebnisse sehen, kontaktieren Sie uns — wir finden gemeinsam eine Lösung."),
            ("Kann ich mehrere Produkte kaufen?","Ja. Die Produkte sind als kohärente Progression konzipiert. Jedes gekaufte Produkt bietet auch ein Vorzugsangebot für den nächsten Schritt."),
            ("Woraus besteht ein Strategiegespräch?","Ein 30-45-minütiges Gespräch, um Ihre Situation, Ihre Ziele und den am besten geeigneten Ausgangspunkt für Ihren Weg zu identifizieren. Ohne Verpflichtung Ihrerseits."),
            ("In welchen Sprachen sind die Ressourcen verfügbar?","Die Ressourcen werden auf Französisch produziert und geliefert. Die Website ist zur Ihrer Bequemlichkeit in 6 Sprachen verfügbar."),
        ]
    },
    "pt": {
        "slug":"perguntas-frequentes.html","title":"Perguntas Frequentes","label":"Perguntas Frequentes",
        "h1":"Perguntas Frequentes",
        "intro":"Tudo o que precisa de saber antes de dar o passo.",
        "faqs":[
            ("A quem se destinam os recursos da Kemora Agency?","A qualquer empreendedor, freelancer ou gestor que queira utilizar a IA para tornar o seu negócio mais eficiente, escalável e autónomo — independentemente do seu nível técnico atual."),
            ("Preciso de ter competências técnicas para beneficiar dos recursos?","Não. Cada recurso é concebido para ser aplicável imediatamente, qualquer que seja o seu nível. As ferramentas de IA que recomendamos não requerem conhecimentos técnicos específicos."),
            ("Qual é a diferença entre os produtos?","Cada produto corresponde a uma etapa da progressão Kemora — desde a postura mental (Le Cadre Mental) até ao ecossistema completo (Kemora OS IA). Pode começar onde está e progredir ao seu próprio ritmo."),
            ("Como acedo aos recursos após a compra?","Imediatamente após o pagamento, receberá um e-mail com acesso ao seu recurso. O acesso é imediato e não expira."),
            ("Existe uma garantia de satisfação?","Cada produto é concebido para produzir resultados. Se tiver aplicado o método e não vir resultados, contacte-nos — encontraremos uma solução juntos."),
            ("Posso adquirir vários produtos?","Sim. Os produtos são concebidos como uma progressão coerente. Cada produto adquirido também fornece uma oferta preferencial para o passo seguinte."),
            ("Em que consiste uma chamada estratégica?","Uma chamada de 30-45 minutos para identificar a sua situação, os seus objetivos e o ponto de partida mais adequado ao seu percurso. Sem compromisso da sua parte."),
            ("Em que idiomas estão disponíveis os recursos?","Os recursos são produzidos e entregues em francês. O site está disponível em 6 idiomas para a sua conveniência."),
        ]
    },
    "it": {
        "slug":"domande-frequenti.html","title":"Domande Frequenti","label":"Domande Frequenti",
        "h1":"Domande Frequenti",
        "intro":"Tutto quello che deve sapere prima di fare il passo.",
        "faqs":[
            ("A chi sono destinati le risorse di Kemora Agency?","A qualsiasi imprenditore, libero professionista o manager che voglia utilizzare l'IA per rendere la propria attività più efficiente, scalabile e autonoma — indipendentemente dal suo livello tecnico attuale."),
            ("Ho bisogno di competenze tecniche per beneficiare delle risorse?","No. Ogni risorsa è progettata per essere applicabile immediatamente, qualunque sia il suo livello. Gli strumenti IA che raccomandiamo non richiedono conoscenze tecniche specifiche."),
            ("Qual è la differenza tra i prodotti?","Ogni prodotto corrisponde a una tappa della progressione Kemora — dalla postura mentale (Le Cadre Mental) all'ecosistema completo (Kemora OS IA). Può iniziare dove si trova e progredire al proprio ritmo."),
            ("Come accedo alle risorse dopo l'acquisto?","Immediatamente dopo il pagamento, riceverà un'e-mail contenente l'accesso alla Sua risorsa. L'accesso è immediato e non scade."),
            ("C'è una garanzia di soddisfazione?","Ogni prodotto è progettato per produrre risultati. Se ha applicato il metodo e non vede risultati, ci contatti — troveremo insieme una soluzione."),
            ("Posso acquistare più prodotti?","Sì. I prodotti sono progettati come una progressione coerente. Ogni prodotto acquistato fornisce anche un'offerta preferenziale per il passo successivo."),
            ("In cosa consiste una chiamata strategica?","Una chiamata di 30-45 minuti per identificare la Sua situazione, i Suoi obiettivi e il punto di partenza più adatto al Suo percorso. Senza impegno da parte Sua."),
            ("In quali lingue sono disponibili le risorse?","Le risorse vengono prodotte e consegnate in francese. Il sito è disponibile in 6 lingue per la Sua comodità."),
        ]
    },
}

def make_faq(lang):
    c = FAQ_CONTENT[lang]
    nav = nav_full(lang, "faq")
    faq_items = ""
    for i,(q,a) in enumerate(c["faqs"]):
        faq_items += f'<div class="faq-item reveal"><button class="faq-q" onclick="toggleFaq(this)"><span>{q}</span><span class="faq-icon"><svg viewBox="0 0 14 14"><line x1="7" y1="1" x2="7" y2="13"/><line x1="1" y1="7" x2="13" y2="7"/></svg></span></button><div class="faq-a"><div class="faq-a-inner">{a}</div></div></div>\n'
    faq_schema = '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[' + ','.join([f'{{"@type":"Question","name":"{q.replace(chr(34),chr(39))}","acceptedAnswer":{{"@type":"Answer","text":"{a.replace(chr(34),chr(39))}"}}}}'for q,a in c["faqs"]]) + ']}'
    html = head(lang, c["title"], c["intro"], c["slug"], "faq")
    html += f'\n<script type="application/ld+json">{faq_schema}</script>\n'
    html += f"\n<style>\n{INFO_CSS}\n</style>\n</head>\n<body id=\"main\">\n{nav}\n"
    html += f"""
<section class="page-hero">
  <div class="page-hero-bg"></div>
  <div class="container">
    <div class="page-hero-inner">
      <span class="label reveal">{c["label"]}</span>
      <h1 class="reveal reveal-delay-1">{c["h1"]}</h1>
      <p class="reveal reveal-delay-2">{c["intro"]}</p>
    </div>
  </div>
</section>
<div class="divider-h container"></div>
<section class="section">
  <div class="container">
    <div class="faq-list">{faq_items}</div>
  </div>
</section>
{footer_html(lang)}
{cookie(lang)}
{COMMON_JS}
{nav_js()}
<script>
function toggleFaq(btn){{
  var item=btn.closest('.faq-item');
  var ans=item.querySelector('.faq-a');
  var wasOpen=item.classList.contains('open');
  document.querySelectorAll('.faq-item.open').forEach(function(el){{el.classList.remove('open');el.querySelector('.faq-a').style.maxHeight='0';}});
  if(!wasOpen){{item.classList.add('open');ans.style.maxHeight=ans.scrollHeight+40+'px';}}
}}
</script>
</body></html>"""
    return html, c["slug"]

# ─────────────────────────────────────────────────────────────────────────────
# CONTACT PAGE
# ─────────────────────────────────────────────────────────────────────────────

CONTACT_CONTENT = {
    "en":{"slug":"contact.html","title":"Contact","label":"Contact us","h1":"Get in <em>touch</em>","intro":"A question, a project, a specific need? We read every message and respond personally.","name_l":"Full name","email_l":"Email address","subject_l":"Subject","msg_l":"Your message","send_l":"Send message","info1_h":"Response time","info1_p":"We respond to every message within 24 to 48 hours on business days.","info2_h":"A strategic call?","info2_p":"If you prefer to discuss directly, book a call — it is free and without commitment.","info2_btn":"Book a Call"},
    "es":{"slug":"contacto.html","title":"Contacto","label":"Contáctenos","h1":"Póngase en <em>contacto</em>","intro":"¿Una pregunta, un proyecto, una necesidad específica? Leemos cada mensaje y respondemos personalmente.","name_l":"Nombre completo","email_l":"Dirección de correo electrónico","subject_l":"Asunto","msg_l":"Su mensaje","send_l":"Enviar mensaje","info1_h":"Tiempo de respuesta","info1_p":"Respondemos a cada mensaje en un plazo de 24 a 48 horas en días hábiles.","info2_h":"¿Una llamada estratégica?","info2_p":"Si prefiere hablar directamente, reserve una llamada — es gratuita y sin compromiso.","info2_btn":"Reservar Llamada"},
    "de":{"slug":"kontakt.html","title":"Kontakt","label":"Kontaktieren Sie uns","h1":"Nehmen Sie <em>Kontakt</em> auf","intro":"Eine Frage, ein Projekt, ein spezifisches Anliegen? Wir lesen jede Nachricht und antworten persönlich.","name_l":"Vollständiger Name","email_l":"E-Mail-Adresse","subject_l":"Betreff","msg_l":"Ihre Nachricht","send_l":"Nachricht senden","info1_h":"Antwortzeit","info1_p":"Wir antworten auf jede Nachricht innerhalb von 24 bis 48 Stunden an Werktagen.","info2_h":"Ein Strategiegespräch?","info2_p":"Wenn Sie lieber direkt sprechen möchten, buchen Sie einen Anruf — kostenlos und unverbindlich.","info2_btn":"Anruf Buchen"},
    "pt":{"slug":"contato.html","title":"Contato","label":"Contacte-nos","h1":"Entre em <em>contacto</em>","intro":"Uma questão, um projeto, uma necessidade específica? Lemos cada mensagem e respondemos pessoalmente.","name_l":"Nome completo","email_l":"Endereço de e-mail","subject_l":"Assunto","msg_l":"A sua mensagem","send_l":"Enviar mensagem","info1_h":"Tempo de resposta","info1_p":"Respondemos a cada mensagem em 24 a 48 horas em dias úteis.","info2_h":"Uma chamada estratégica?","info2_p":"Se preferir falar diretamente, reserve uma chamada — é gratuita e sem compromisso.","info2_btn":"Reservar Chamada"},
    "it":{"slug":"contatto.html","title":"Contatto","label":"Contattaci","h1":"Mettetevi in <em>contatto</em>","intro":"Una domanda, un progetto, un'esigenza specifica? Leggiamo ogni messaggio e rispondiamo personalmente.","name_l":"Nome completo","email_l":"Indirizzo e-mail","subject_l":"Oggetto","msg_l":"Il Suo messaggio","send_l":"Invia messaggio","info1_h":"Tempo di risposta","info1_p":"Rispondiamo a ogni messaggio entro 24-48 ore nei giorni lavorativi.","info2_h":"Una chiamata strategica?","info2_p":"Se preferisce parlare direttamente, prenoti una chiamata — è gratuita e senza impegno.","info2_btn":"Prenota una Chiamata"},
}
# Fix DE dict key typo
CONTACT_CONTENT["de"]["h1"] = "Nehmen Sie <em>Kontakt</em> auf"

def make_contact(lang):
    c = CONTACT_CONTENT[lang]
    nav = nav_full(lang, "contact")
    booking_file = HREFLANG["booking"].get(lang,"").replace(lang+"/","")
    html = head(lang, c["title"], c["intro"], c["slug"], "contact")
    html += f"\n<style>\n{INFO_CSS}\n</style>\n</head>\n<body id=\"main\">\n{nav}\n"
    html += f"""
<section class="page-hero">
  <div class="page-hero-bg"></div>
  <div class="container">
    <div class="page-hero-inner">
      <span class="label reveal">{c["label"]}</span>
      <h1 class="reveal reveal-delay-1">{c["h1"]}</h1>
      <p class="reveal reveal-delay-2">{c["intro"]}</p>
    </div>
  </div>
</section>
<div class="divider-h container"></div>
<section class="section">
  <div class="container">
    <div class="contact-grid">
      <form class="contact-form reveal" method="post" action="{SYSTEME_CONTACT}">
        <label for="name">{c["name_l"]}</label>
        <input type="text" id="name" name="contact[name]" required autocomplete="name">
        <label for="email">{c["email_l"]}</label>
        <input type="email" id="email" name="contact[email]" required autocomplete="email">
        <label for="subject">{c["subject_l"]}</label>
        <input type="text" id="subject" name="contact[fields][subject]">
        <label for="msg">{c["msg_l"]}</label>
        <textarea id="msg" name="contact[fields][message]" required></textarea>
        <div style="margin-top:1.8rem;">
          <button type="submit" class="btn-gold">{c["send_l"]}</button>
        </div>
      </form>
      <div class="contact-info reveal reveal-delay-1">
        <div class="contact-info-item">
          <h3>{c["info1_h"]}</h3>
          <p>{c["info1_p"]}</p>
        </div>
        <div class="contact-info-item">
          <h3>{c["info2_h"]}</h3>
          <p>{c["info2_p"]}</p>
          <div style="margin-top:1rem;">
            <a href="/{lang}/{booking_file}" class="btn-outline">{c["info2_btn"]}</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
{footer_html(lang)}
{cookie(lang)}
{COMMON_JS}
{nav_js()}
</body></html>"""
    return html, c["slug"]

# ─────────────────────────────────────────────────────────────────────────────
# BOOKING PAGE
# ─────────────────────────────────────────────────────────────────────────────

BOOKING_CONTENT = {
    "en":{"slug":"book-a-call.html","title":"Book a Call","label":"Strategic Call","h1":"Let's talk about<br>your <em>project</em>","intro":"A 30-45 minute call to understand your situation, your objectives and identify together the starting point most suited to your journey. Free, without commitment.","s1":"Complete the form","s1_p":"A few pieces of information so we can best prepare for our exchange.","s2":"Receive a confirmation","s2_p":"You will receive an e-mail with the date and details of the call.","s3":"Our exchange","s3_p":"30-45 minutes of strategic discussion — honest, concrete, without sales pressure.","name_l":"Full name","email_l":"Email address","project_l":"Describe your project or objective","activity_l":"Your current activity","send_l":"Request a call"},
    "es":{"slug":"reservar-llamada.html","title":"Reservar Llamada","label":"Llamada Estratégica","h1":"Hablemos de<br>su <em>proyecto</em>","intro":"Una llamada de 30-45 minutos para comprender su situación, sus objetivos e identificar juntos el punto de partida más adecuado para su trayectoria. Gratuita, sin compromiso.","s1":"Complete el formulario","s1_p":"Algunos datos para preparar mejor nuestro intercambio.","s2":"Reciba una confirmación","s2_p":"Recibirá un correo electrónico con la fecha y los detalles de la llamada.","s3":"Nuestro intercambio","s3_p":"30-45 minutos de conversación estratégica — honesta, concreta, sin presión de venta.","name_l":"Nombre completo","email_l":"Dirección de correo electrónico","project_l":"Describa su proyecto u objetivo","activity_l":"Su actividad actual","send_l":"Solicitar una llamada"},
    "de":{"slug":"anruf-buchen.html","title":"Anruf Buchen","label":"Strategiegespräch","h1":"Reden wir über<br>Ihr <em>Projekt</em>","intro":"Ein 30-45-minütiges Gespräch, um Ihre Situation und Ihre Ziele zu verstehen und gemeinsam den geeignetsten Ausgangspunkt für Ihren Weg zu identifizieren. Kostenlos, unverbindlich.","s1":"Formular ausfüllen","s1_p":"Einige Angaben, damit wir unser Gespräch optimal vorbereiten können.","s2":"Bestätigung erhalten","s2_p":"Sie erhalten eine E-Mail mit Datum und Details des Gesprächs.","s3":"Unser Gespräch","s3_p":"30-45 Minuten strategische Unterhaltung — ehrlich, konkret, ohne Verkaufsdruck.","name_l":"Vollständiger Name","email_l":"E-Mail-Adresse","project_l":"Beschreiben Sie Ihr Projekt oder Ziel","activity_l":"Ihre aktuelle Tätigkeit","send_l":"Anruf anfragen"},
    "pt":{"slug":"reservar-chamada.html","title":"Reservar Chamada","label":"Chamada Estratégica","h1":"Vamos falar sobre<br>o seu <em>projeto</em>","intro":"Uma chamada de 30-45 minutos para compreender a sua situação, os seus objetivos e identificar juntos o ponto de partida mais adequado ao seu percurso. Gratuita, sem compromisso.","s1":"Preencha o formulário","s1_p":"Algumas informações para melhor preparar a nossa troca.","s2":"Receba uma confirmação","s2_p":"Receberá um e-mail com a data e os detalhes da chamada.","s3":"A nossa troca","s3_p":"30-45 minutos de conversa estratégica — honesta, concreta, sem pressão de venda.","name_l":"Nome completo","email_l":"Endereço de e-mail","project_l":"Descreva o seu projeto ou objetivo","activity_l":"A sua atividade atual","send_l":"Solicitar uma chamada"},
    "it":{"slug":"prenota-chiamata.html","title":"Prenota una Chiamata","label":"Chiamata Strategica","h1":"Parliamo del<br>Suo <em>progetto</em>","intro":"Una chiamata di 30-45 minuti per comprendere la Sua situazione, i Suoi obiettivi e identificare insieme il punto di partenza più adatto al Suo percorso. Gratuita, senza impegno.","s1":"Compilare il modulo","s1_p":"Alcune informazioni per preparare al meglio il nostro scambio.","s2":"Ricevere una conferma","s2_p":"Riceverà un'e-mail con la data e i dettagli della chiamata.","s3":"Il nostro scambio","s3_p":"30-45 minuti di conversazione strategica — onesta, concreta, senza pressione di vendita.","name_l":"Nome completo","email_l":"Indirizzo e-mail","project_l":"Descriva il Suo progetto o obiettivo","activity_l":"La Sua attività attuale","send_l":"Richiedere una chiamata"},
}

def make_booking(lang):
    c = BOOKING_CONTENT[lang]
    nav = nav_full(lang, "booking")
    html = head(lang, c["title"], c["intro"][:160], c["slug"], "booking")
    html += f"\n<style>\n{INFO_CSS}\n</style>\n</head>\n<body id=\"main\">\n{nav}\n"
    html += f"""
<section class="page-hero">
  <div class="page-hero-bg"></div>
  <div class="container">
    <div class="page-hero-inner">
      <span class="label reveal">{c["label"]}</span>
      <h1 class="reveal reveal-delay-1">{c["h1"]}</h1>
      <p class="reveal reveal-delay-2">{c["intro"]}</p>
    </div>
  </div>
</section>
<div class="divider-h container"></div>
<section class="section" style="background:var(--black2);">
  <div class="container">
    <div class="booking-steps reveal">
      <div class="booking-step"><span class="booking-step-num">01</span><div class="booking-step-body"><h3>{c["s1"]}</h3><p>{c["s1_p"]}</p></div></div>
      <div class="booking-step"><span class="booking-step-num">02</span><div class="booking-step-body"><h3>{c["s2"]}</h3><p>{c["s2_p"]}</p></div></div>
      <div class="booking-step"><span class="booking-step-num">03</span><div class="booking-step-body"><h3>{c["s3"]}</h3><p>{c["s3_p"]}</p></div></div>
    </div>
  </div>
</section>
<div class="divider-h container"></div>
<section class="section">
  <div class="container" style="max-width:640px;">
    <form class="contact-form reveal" method="post" action="{SYSTEME_BOOKING}">
      <label for="b-name">{c["name_l"]}</label>
      <input type="text" id="b-name" name="contact[name]" required autocomplete="name">
      <label for="b-email">{c["email_l"]}</label>
      <input type="email" id="b-email" name="contact[email]" required autocomplete="email">
      <label for="b-activity">{c["activity_l"]}</label>
      <input type="text" id="b-activity" name="contact[fields][activity]">
      <label for="b-project">{c["project_l"]}</label>
      <textarea id="b-project" name="contact[fields][project]" style="min-height:160px;"></textarea>
      <div style="margin-top:1.8rem;">
        <button type="submit" class="btn-gold">{c["send_l"]}</button>
      </div>
    </form>
  </div>
</section>
{footer_html(lang)}
{cookie(lang)}
{COMMON_JS}
{nav_js()}
</body></html>"""
    return html, c["slug"]

# ─────────────────────────────────────────────────────────────────────────────
# PRODUCT PAGES (translated landing pages)
# ─────────────────────────────────────────────────────────────────────────────

PROD_CSS = BASE_CSS + NAV_CSS + """
  .prod-hero { min-height:90vh; display:grid; grid-template-columns:1fr 1fr; padding-top:72px; position:relative; overflow:hidden; }
  .prod-hero-left { display:flex; align-items:center; padding:clamp(3rem,6vw,6rem) clamp(1.5rem,4vw,5rem) clamp(3rem,6vw,6rem) clamp(1.5rem,5vw,5rem); position:relative; z-index:2; }
  .prod-hero-left-inner { max-width:540px; }
  .prod-hero-left .label { display:block; margin-bottom:1.5rem; }
  .prod-hero-left h1 { color:var(--gold); margin-bottom:1.5rem; }
  .prod-hero-left .subtitle { color:var(--muted); font-size:clamp(0.9rem,1.5vw,1.05rem); line-height:1.95; margin-bottom:2.5rem; }
  .prod-price-row { display:flex; align-items:center; gap:1.5rem; margin-bottom:2.2rem; flex-wrap:wrap; }
  .prod-price { font-family:var(--serif); font-size:3rem; color:var(--gold); line-height:1; }
  .prod-price-note { font-size:0.72rem; letter-spacing:0.1em; text-transform:uppercase; color:var(--muted); }
  .prod-hero-right { position:relative; overflow:hidden; }
  .prod-hero-right img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; }
  .prod-hero-right::after { content:''; position:absolute; inset:0; background:linear-gradient(to right,var(--black) 0%,rgba(5,5,5,0.1) 50%,transparent 100%),linear-gradient(to top,rgba(5,5,5,0.4) 0%,transparent 40%); }
  .prod-section { max-width:800px; }
  .prod-section h2 { font-family:var(--serif); font-size:clamp(1.6rem,3vw,2.4rem); color:var(--gold); margin-bottom:1.2rem; }
  .prod-section p { color:var(--muted); font-size:clamp(0.88rem,1.4vw,1rem); line-height:1.95; margin-bottom:1.2rem; }
  .prod-section ul { list-style:none; display:flex; flex-direction:column; gap:0.7rem; margin-bottom:1.5rem; }
  .prod-section ul li { display:flex; align-items:flex-start; gap:0.8rem; font-size:0.88rem; color:var(--muted); line-height:1.7; }
  .prod-section ul li::before { content:''; width:5px; height:5px; border-radius:50%; background:var(--gold); flex-shrink:0; margin-top:0.5rem; }
  .prod-includes { border:1px solid var(--border); }
  .prod-include-item { padding:1.3rem 1.8rem; border-bottom:1px solid var(--border2); display:flex; align-items:center; gap:1rem; transition:background 0.3s; }
  .prod-include-item:last-child { border-bottom:none; }
  .prod-include-item:hover { background:rgba(198,161,110,0.02); }
  .prod-include-icon { width:8px; height:8px; border-radius:50%; background:var(--gold); flex-shrink:0; }
  .prod-include-item span { font-size:0.85rem; color:var(--muted); line-height:1.6; }
  .prod-cta { text-align:center; padding:clamp(4rem,8vw,7rem) 0; }
  .prod-cta h2 { color:var(--gold); margin-bottom:1rem; max-width:600px; margin-left:auto; margin-right:auto; }
  .prod-cta p { color:var(--muted); max-width:480px; margin:0 auto 2.5rem; line-height:1.9; }
  @media (max-width:960px) { .prod-hero { grid-template-columns:1fr; } .prod-hero-right { height:50vw; min-height:260px; } }
"""

PROD_CONTENT = {
    "en": {
        "cadre": {
            "label":"Foundation Level", "h1":"Le Cadre Mental", "subtitle":"Adopt the posture and the architecture of thought that precede any lasting transformation. The foundation before all foundations.",
            "img":"/assets/images/le_cadremental.webp", "price":"37 €", "price_note":"one-time access",
            "s1_h":"What you will discover",
            "s1_items":["The 4 mental levers that determine the quality of your decisions","How to structure your thinking to eliminate mental noise","The posture adopted by high-performing entrepreneurs","A complete framework to think about your business differently","Applicable immediately — no prior knowledge required"],
            "s2_h":"For whom?",
            "s2_p":"For any entrepreneur, freelancer or manager who feels that their thinking is the limiting factor — not their skills, not their market, not their resources. For those who want to build a solid foundation before automating anything.",
            "includes_h":"What is included",
            "includes":["Complete digital resource in PDF format","Practical framework with immediate application","Self-assessment tools and decision matrices","Full lifetime access"],
            "cta_h":"Ready to change<br>your <em>posture</em>?",
            "cta_p":"Adopt the mental framework that precedes every transformation.",
        },
        "exec": {
            "label":"Action Level", "h1":"L'Exécution", "subtitle":"The systems to move from intention to action — in a structured, repeatable and effective way. Execution is the only strategy that counts.",
            "img":"/assets/images/lexecution.webp", "price":"37 €", "price_note":"one-time access",
            "s1_h":"What you will discover",
            "s1_items":["The 7 high-velocity execution systems","The project launch protocol in under 24 hours","The friction-free prioritisation method","Operational thinking templates ready to use","A complete anti-procrastination system"],
            "s2_h":"For whom?",
            "s2_p":"For those who have ideas but struggle to execute them consistently. For those who want to move from inspiration to action without losing momentum or energy along the way.",
            "includes_h":"What is included",
            "includes":["Complete digital resource in PDF format","7 execution systems with templates","Implementation protocols for immediate use","Full lifetime access"],
            "cta_h":"Ready to execute<br>at a different <em>level</em>?",
            "cta_p":"The systems that transform intention into concrete results.",
        },
        "core": {
            "label":"Beginner Level", "h1":"CORE OS IA", "subtitle":"The foundations of an automated business: essential AI tools, 5 structural pillars and a 7-day action plan to launch your transformation.",
            "img":"/assets/images/coreosia.webp", "price":"97 €", "price_note":"one-time access",
            "s1_h":"What you will discover",
            "s1_items":["The 5 pillars of an automated business","The 12 essential AI tools explained step by step","A 7-day operational action plan","Ready-to-use templates for each pillar","How to delegate your first tasks to AI"],
            "s2_h":"For whom?",
            "s2_p":"For entrepreneurs starting their AI journey who want a structured, complete and immediately applicable foundation to automate their business.",
            "includes_h":"What is included",
            "includes":["Complete digital resource in multiple formats","5 structural modules","7-day action plan with daily tasks","Tool library and ready-to-use templates","Full lifetime access"],
            "cta_h":"Start building your<br><em>automated</em> business",
            "cta_p":"The complete foundations for a business that works for you.",
        },
        "biz": {
            "label":"Advanced Level", "h1":"Business OS IA", "subtitle":"Advanced strategy, monetisation systems and deep automation for a solid, scalable business that no longer depends on your direct time.",
            "img":"/assets/images/businessosia.webp", "price":"230 €", "price_note":"one-time access",
            "s1_h":"What you will discover",
            "s1_items":["Advanced AI strategy for entrepreneurs at scale","Automated monetisation systems","Deep delegation techniques to AI","Scaling methods without time dependency","Full business automation framework"],
            "s2_h":"For whom?",
            "s2_p":"For entrepreneurs who have already mastered the basics and want to go further — to build a system that generates results independently of their direct involvement.",
            "includes_h":"What is included",
            "includes":["Advanced strategy module","Monetisation and scaling systems","Deep automation protocols","Premium templates and frameworks","Full lifetime access"],
            "cta_h":"Build a business that<br>works for <em>you</em>",
            "cta_p":"Advanced strategy and deep automation for true scalability.",
        },
        "kemora": {
            "label":"Signature Level", "h1":"Kemora OS IA", "subtitle":"The complete ecosystem — the most comprehensive version of our method for a business entirely orchestrated by AI. Everything. In one place.",
            "img":"/assets/images/kemoraosia.webp", "price":"347 €", "price_note":"one-time access",
            "s1_h":"What is included",
            "s1_items":["The complete Kemora method from foundation to full ecosystem","All systems, templates and operational protocols","The complete AI orchestration protocol","Exclusive scaling and monetisation methods","Lifetime access and all future updates"],
            "s2_h":"For whom?",
            "s2_p":"For ambitious entrepreneurs who want the complete method — to build a business entirely orchestrated by AI, structured for the long term, and capable of scaling without depending on their time.",
            "includes_h":"The complete ecosystem",
            "includes":["Le Cadre Mental — Foundation","L'Exécution — Action systems","CORE OS IA — AI automation foundations","Business OS IA — Advanced strategy","The complete Kemora OS IA framework","All updates, forever"],
            "cta_h":"The complete method<br>for an <em>intelligent</em> business",
            "cta_p":"Everything you need to build a business orchestrated by AI.",
        },
    },
    "es": {
        "cadre": {"label":"Nivel Fundación","h1":"Le Cadre Mental","subtitle":"Adopte la postura y la arquitectura del pensamiento que preceden a toda transformación duradera. La fundación antes de todas las fundaciones.","img":"/assets/images/le_cadremental.webp","price":"37 €","price_note":"acceso único","s1_h":"Lo que descubrirá","s1_items":["Los 4 palancas mentales que determinan la calidad de sus decisiones","Cómo estructurar su pensamiento para eliminar el ruido mental","La postura adoptada por los emprendedores de alto rendimiento","Un framework completo para pensar su negocio diferente","Aplicable de forma inmediata — sin conocimientos previos necesarios"],"s2_h":"¿Para quién?","s2_p":"Para cualquier emprendedor, freelance o directivo que sienta que su forma de pensar es el factor limitante — no sus habilidades, no su mercado, no sus recursos. Para quienes quieren construir una base sólida antes de automatizar cualquier cosa.","includes_h":"Qué está incluido","includes":["Recurso digital completo en formato PDF","Framework práctico con aplicación inmediata","Herramientas de autoevaluación y matrices de decisión","Acceso completo de por vida"],"cta_h":"¿Listo para cambiar<br>su <em>postura</em>?","cta_p":"Adopte el marco mental que precede a toda transformación."},
        "exec": {"label":"Nivel Acción","h1":"L'Exécution","subtitle":"Los sistemas para pasar de la intención a la acción — de forma estructurada, repetible y eficaz. La ejecución es la única estrategia que cuenta.","img":"/assets/images/lexecution.webp","price":"37 €","price_note":"acceso único","s1_h":"Lo que descubrirá","s1_items":["Los 7 sistemas de ejecución de alta velocidad","El protocolo de lanzamiento de proyecto en menos de 24h","El método de priorización sin fricción","Plantillas de reflexión operacional listas para usar","Un sistema completo anti-procrastinación"],"s2_h":"¿Para quién?","s2_p":"Para quienes tienen ideas pero tienen dificultades para ejecutarlas de forma constante. Para quienes quieren pasar de la inspiración a la acción sin perder impulso ni energía en el camino.","includes_h":"Qué está incluido","includes":["Recurso digital completo en formato PDF","7 sistemas de ejecución con plantillas","Protocolos de implementación para uso inmediato","Acceso completo de por vida"],"cta_h":"¿Listo para ejecutar<br>a un <em>nivel</em> diferente?","cta_p":"Los sistemas que transforman la intención en resultados concretos."},
        "core": {"label":"Nivel Principiante","h1":"CORE OS IA","subtitle":"Los fundamentos de un negocio automatizado: herramientas IA esenciales, 5 pilares estructurales y un plan de acción de 7 días para lanzar su transformación.","img":"/assets/images/coreosia.webp","price":"97 €","price_note":"acceso único","s1_h":"Lo que descubrirá","s1_items":["Los 5 pilares de un negocio automatizado","Las 12 herramientas IA esenciales explicadas paso a paso","Un plan de acción operacional de 7 días","Plantillas listas para usar para cada pilar","Cómo delegar sus primeras tareas a la IA"],"s2_h":"¿Para quién?","s2_p":"Para emprendedores que comienzan su camino con la IA y quieren una base estructurada, completa e inmediatamente aplicable para automatizar su negocio.","includes_h":"Qué está incluido","includes":["Recurso digital completo en varios formatos","5 módulos estructurales","Plan de acción de 7 días con tareas diarias","Biblioteca de herramientas y plantillas listas para usar","Acceso completo de por vida"],"cta_h":"Empiece a construir su<br>negocio <em>automatizado</em>","cta_p":"Los fundamentos completos para un negocio que trabaja para usted."},
        "biz": {"label":"Nivel Avanzado","h1":"Business OS IA","subtitle":"Estrategia avanzada, sistemas de monetización y automatización profunda para un negocio sólido y escalable que ya no depende de su tiempo directo.","img":"/assets/images/businessosia.webp","price":"230 €","price_note":"acceso único","s1_h":"Lo que descubrirá","s1_items":["Estrategia IA avanzada para emprendedores en escala","Sistemas de monetización automatizados","Técnicas de delegación profunda a la IA","Métodos de scaling sin dependencia de tiempo","Framework completo de automatización del negocio"],"s2_h":"¿Para quién?","s2_p":"Para emprendedores que ya dominan los fundamentos y quieren ir más lejos — para construir un sistema que genere resultados independientemente de su implicación directa.","includes_h":"Qué está incluido","includes":["Módulo de estrategia avanzada","Sistemas de monetización y scaling","Protocolos de automatización profunda","Plantillas y frameworks premium","Acceso completo de por vida"],"cta_h":"Construya un negocio que<br>trabaje para <em>usted</em>","cta_p":"Estrategia avanzada y automatización profunda para una escalabilidad real."},
        "kemora": {"label":"Nivel Firma","h1":"Kemora OS IA","subtitle":"El ecosistema completo — la versión más completa de nuestro método para un negocio enteramente orquestado por la IA. Todo. En un solo lugar.","img":"/assets/images/kemoraosia.webp","price":"347 €","price_note":"acceso único","s1_h":"Qué está incluido","s1_items":["El método Kemora completo de la fundación al ecosistema completo","Todos los sistemas, plantillas y protocolos operacionales","El protocolo de orquestación IA completa","Métodos exclusivos de scaling y monetización","Acceso de por vida y todas las actualizaciones futuras"],"s2_h":"¿Para quién?","s2_p":"Para emprendedores ambiciosos que quieren el método completo — para construir un negocio enteramente orquestado por la IA, estructurado a largo plazo y capaz de escalar sin depender de su tiempo.","includes_h":"El ecosistema completo","includes":["Le Cadre Mental — Fundación","L'Exécution — Sistemas de acción","CORE OS IA — Fundamentos de automatización IA","Business OS IA — Estrategia avanzada","El framework completo Kemora OS IA","Todas las actualizaciones, para siempre"],"cta_h":"El método completo<br>para un negocio <em>inteligente</em>","cta_p":"Todo lo que necesita para construir un negocio orquestado por la IA."},
    },
    "de": {
        "cadre": {"label":"Fundament-Ebene","h1":"Le Cadre Mental","subtitle":"Nehmen Sie die Haltung und Gedankenarchitektur an, die jeder dauerhaften Transformation vorausgehen. Das Fundament vor allen Fundamenten.","img":"/assets/images/le_cadremental.webp","price":"37 €","price_note":"Einmalzugang","s1_h":"Was Sie entdecken werden","s1_items":["Die 4 mentalen Hebel, die die Qualität Ihrer Entscheidungen bestimmen","Wie man sein Denken strukturiert, um mentales Rauschen zu eliminieren","Die Haltung, die Hochleistungsunternehmer einnehmen","Ein vollständiges Framework, um Ihr Unternehmen anders zu denken","Sofort anwendbar — keine Vorkenntnisse erforderlich"],"s2_h":"Für wen?","s2_p":"Für jeden Unternehmer, Freiberufler oder Manager, der das Gefühl hat, dass sein Denken der begrenzende Faktor ist — nicht seine Fähigkeiten, nicht sein Markt, nicht seine Ressourcen. Für diejenigen, die ein solides Fundament aufbauen möchten, bevor sie irgendetwas automatisieren.","includes_h":"Was ist enthalten","includes":["Vollständige digitale Ressource im PDF-Format","Praktisches Framework mit sofortiger Anwendung","Selbstbewertungstools und Entscheidungsmatrizen","Vollständiger lebenslanger Zugang"],"cta_h":"Bereit, Ihre<br><em>Haltung</em> zu ändern?","cta_p":"Nehmen Sie den mentalen Rahmen an, der jeder Transformation vorausgeht."},
        "exec": {"label":"Aktions-Ebene","h1":"L'Exécution","subtitle":"Die Systeme, um von der Absicht zur Aktion überzugehen — strukturiert, wiederholbar und effektiv. Ausführung ist die einzige Strategie, die zählt.","img":"/assets/images/lexecution.webp","price":"37 €","price_note":"Einmalzugang","s1_h":"Was Sie entdecken werden","s1_items":["Die 7 Hochgeschwindigkeits-Ausführungssysteme","Das Projektstart-Protokoll in unter 24 Stunden","Die reibungsfreie Priorisierungsmethode","Operative Denktemplates zur sofortigen Verwendung","Ein vollständiges Anti-Prokrastinations-System"],"s2_h":"Für wen?","s2_p":"Für diejenigen, die Ideen haben, aber Schwierigkeiten haben, sie konsequent umzusetzen. Für diejenigen, die von der Inspiration zur Aktion gelangen möchten, ohne unterwegs Schwung oder Energie zu verlieren.","includes_h":"Was ist enthalten","includes":["Vollständige digitale Ressource im PDF-Format","7 Ausführungssysteme mit Templates","Implementierungsprotokolle zur sofortigen Verwendung","Vollständiger lebenslanger Zugang"],"cta_h":"Bereit, auf einem anderen<br><em>Niveau</em> auszuführen?","cta_p":"Die Systeme, die Absicht in konkrete Ergebnisse verwandeln."},
        "core": {"label":"Einsteiger-Ebene","h1":"CORE OS IA","subtitle":"Die Grundlagen eines automatisierten Unternehmens: wesentliche KI-Tools, 5 Struktursäulen und ein 7-Tage-Aktionsplan, um Ihre Transformation zu starten.","img":"/assets/images/coreosia.webp","price":"97 €","price_note":"Einmalzugang","s1_h":"Was Sie entdecken werden","s1_items":["Die 5 Säulen eines automatisierten Unternehmens","Die 12 wesentlichen KI-Tools Schritt für Schritt erklärt","Ein 7-Tage-Operationsaktionsplan","Gebrauchsfertige Templates für jede Säule","Wie Sie Ihre ersten Aufgaben an KI delegieren"],"s2_h":"Für wen?","s2_p":"Für Unternehmer, die ihre KI-Reise beginnen und eine strukturierte, vollständige und sofort anwendbare Grundlage für die Automatisierung ihres Unternehmens wünschen.","includes_h":"Was ist enthalten","includes":["Vollständige digitale Ressource in mehreren Formaten","5 Strukturmodule","7-Tage-Aktionsplan mit täglichen Aufgaben","Tool-Bibliothek und gebrauchsfertige Templates","Vollständiger lebenslanger Zugang"],"cta_h":"Beginnen Sie, Ihr<br><em>automatisiertes</em> Unternehmen aufzubauen","cta_p":"Die vollständigen Grundlagen für ein Unternehmen, das für Sie arbeitet."},
        "biz": {"label":"Fortgeschrittene Ebene","h1":"Business OS IA","subtitle":"Fortgeschrittene Strategie, Monetarisierungssysteme und tiefgreifende Automatisierung für ein solides, skalierbares Unternehmen, das nicht mehr von Ihrer direkten Zeit abhängt.","img":"/assets/images/businessosia.webp","price":"230 €","price_note":"Einmalzugang","s1_h":"Was Sie entdecken werden","s1_items":["Fortgeschrittene KI-Strategie für skalierte Unternehmer","Automatisierte Monetarisierungssysteme","Tiefe Delegationstechniken an KI","Skalierungsmethoden ohne Zeitabhängigkeit","Vollständiges Business-Automatisierungs-Framework"],"s2_h":"Für wen?","s2_p":"Für Unternehmer, die die Grundlagen bereits beherrschen und weiter gehen möchten — um ein System aufzubauen, das unabhängig von ihrer direkten Beteiligung Ergebnisse generiert.","includes_h":"Was ist enthalten","includes":["Modul für fortgeschrittene Strategie","Monetarisierungs- und Skalierungssysteme","Tiefe Automatisierungsprotokolle","Premium-Templates und Frameworks","Vollständiger lebenslanger Zugang"],"cta_h":"Bauen Sie ein Unternehmen auf,<br>das für <em>Sie</em> arbeitet","cta_p":"Fortgeschrittene Strategie und tiefe Automatisierung für echte Skalierbarkeit."},
        "kemora": {"label":"Signatur-Ebene","h1":"Kemora OS IA","subtitle":"Das vollständige Ökosystem — die umfassendste Version unserer Methode für ein vollständig von KI orchestriertes Unternehmen. Alles. An einem Ort.","img":"/assets/images/kemoraosia.webp","price":"347 €","price_note":"Einmalzugang","s1_h":"Was ist enthalten","s1_items":["Die vollständige Kemora-Methode vom Fundament bis zum vollständigen Ökosystem","Alle Systeme, Templates und Betriebsprotokolle","Das vollständige KI-Orchestrierungsprotokoll","Exklusive Skalierungs- und Monetarisierungsmethoden","Lebenslanger Zugang und alle zukünftigen Updates"],"s2_h":"Für wen?","s2_p":"Für ambitionierte Unternehmer, die die vollständige Methode wünschen — um ein vollständig von KI orchestriertes Unternehmen aufzubauen, das langfristig strukturiert ist und ohne Zeitabhängigkeit skalieren kann.","includes_h":"Das vollständige Ökosystem","includes":["Le Cadre Mental — Fundament","L'Exécution — Aktionssysteme","CORE OS IA — KI-Automatisierungsgrundlagen","Business OS IA — Fortgeschrittene Strategie","Das vollständige Kemora OS IA Framework","Alle Updates, für immer"],"cta_h":"Die vollständige Methode<br>für ein <em>intelligentes</em> Unternehmen","cta_p":"Alles, was Sie brauchen, um ein von KI orchestriertes Unternehmen aufzubauen."},
    },
    "pt": {
        "cadre": {"label":"Nível Fundação","h1":"Le Cadre Mental","subtitle":"Adote a postura e a arquitetura do pensamento que precedem qualquer transformação duradoura. A fundação antes de todas as fundações.","img":"/assets/images/le_cadremental.webp","price":"37 €","price_note":"acesso único","s1_h":"O que irá descobrir","s1_items":["As 4 alavancas mentais que determinam a qualidade das suas decisões","Como estruturar o seu pensamento para eliminar o ruído mental","A postura adotada pelos empreendedores de alto desempenho","Um framework completo para pensar o seu negócio de forma diferente","Aplicável imediatamente — sem conhecimentos prévios necessários"],"s2_h":"Para quem?","s2_p":"Para qualquer empreendedor, freelancer ou gestor que sinta que a sua forma de pensar é o fator limitante — não as suas competências, não o seu mercado, não os seus recursos. Para aqueles que querem construir uma base sólida antes de automatizar qualquer coisa.","includes_h":"O que está incluído","includes":["Recurso digital completo em formato PDF","Framework prático com aplicação imediata","Ferramentas de autoavaliação e matrizes de decisão","Acesso completo vitalício"],"cta_h":"Pronto para mudar<br>a sua <em>postura</em>?","cta_p":"Adote o quadro mental que precede toda a transformação."},
        "exec": {"label":"Nível Ação","h1":"L'Exécution","subtitle":"Os sistemas para passar da intenção à ação — de forma estruturada, repetível e eficaz. A execução é a única estratégia que conta.","img":"/assets/images/lexecution.webp","price":"37 €","price_note":"acesso único","s1_h":"O que irá descobrir","s1_items":["Os 7 sistemas de execução de alta velocidade","O protocolo de arranque de projeto em menos de 24h","O método de priorização sem fricção","Templates de reflexão operacional prontos a usar","Um sistema completo anti-procrastinação"],"s2_h":"Para quem?","s2_p":"Para aqueles que têm ideias mas têm dificuldade em executá-las de forma consistente. Para quem quer passar da inspiração à ação sem perder o impulso ou energia ao longo do caminho.","includes_h":"O que está incluído","includes":["Recurso digital completo em formato PDF","7 sistemas de execução com templates","Protocolos de implementação para uso imediato","Acesso completo vitalício"],"cta_h":"Pronto para executar<br>a um <em>nível</em> diferente?","cta_p":"Os sistemas que transformam a intenção em resultados concretos."},
        "core": {"label":"Nível Iniciante","h1":"CORE OS IA","subtitle":"Os alicerces de um negócio automatizado: ferramentas de IA essenciais, 5 pilares estruturais e um plano de ação de 7 dias para lançar a sua transformação.","img":"/assets/images/coreosia.webp","price":"97 €","price_note":"acesso único","s1_h":"O que irá descobrir","s1_items":["Os 5 pilares de um negócio automatizado","As 12 ferramentas de IA essenciais explicadas passo a passo","Um plano de ação operacional de 7 dias","Templates prontos a usar para cada pilar","Como delegar as suas primeiras tarefas à IA"],"s2_h":"Para quem?","s2_p":"Para empreendedores que estão a iniciar a sua jornada com a IA e que querem uma base estruturada, completa e imediatamente aplicável para automatizar o seu negócio.","includes_h":"O que está incluído","includes":["Recurso digital completo em vários formatos","5 módulos estruturais","Plano de ação de 7 dias com tarefas diárias","Biblioteca de ferramentas e templates prontos a usar","Acesso completo vitalício"],"cta_h":"Comece a construir o seu<br>negócio <em>automatizado</em>","cta_p":"Os alicerces completos para um negócio que trabalha para si."},
        "biz": {"label":"Nível Avançado","h1":"Business OS IA","subtitle":"Estratégia avançada, sistemas de monetização e automatização aprofundada para um negócio sólido e escalável que já não depende do seu tempo direto.","img":"/assets/images/businessosia.webp","price":"230 €","price_note":"acesso único","s1_h":"O que irá descobrir","s1_items":["Estratégia IA avançada para empreendedores em escala","Sistemas de monetização automatizados","Técnicas de delegação aprofundada à IA","Métodos de scaling sem dependência de tempo","Framework completo de automatização do negócio"],"s2_h":"Para quem?","s2_p":"Para empreendedores que já dominam os fundamentos e querem ir mais longe — para construir um sistema que gere resultados independentemente da sua participação direta.","includes_h":"O que está incluído","includes":["Módulo de estratégia avançada","Sistemas de monetização e scaling","Protocolos de automatização aprofundada","Templates e frameworks premium","Acesso completo vitalício"],"cta_h":"Construa um negócio que<br>trabalhe para <em>si</em>","cta_p":"Estratégia avançada e automatização aprofundada para uma escalabilidade real."},
        "kemora": {"label":"Nível Assinatura","h1":"Kemora OS IA","subtitle":"O ecossistema completo — a versão mais completa do nosso método para uma atividade inteiramente orquestrada pela IA. Tudo. Num só lugar.","img":"/assets/images/kemoraosia.webp","price":"347 €","price_note":"acesso único","s1_h":"O que está incluído","s1_items":["O método Kemora completo da fundação ao ecossistema completo","Todos os sistemas, templates e protocolos operacionais","O protocolo de orquestração IA completa","Métodos exclusivos de scaling e monetização","Acesso vitalício e todas as atualizações futuras"],"s2_h":"Para quem?","s2_p":"Para empreendedores ambiciosos que querem o método completo — para construir uma atividade inteiramente orquestrada pela IA, estruturada a longo prazo e capaz de escalar sem depender do seu tempo.","includes_h":"O ecossistema completo","includes":["Le Cadre Mental — Fundação","L'Exécution — Sistemas de ação","CORE OS IA — Fundamentos de automatização IA","Business OS IA — Estratégia avançada","O framework completo Kemora OS IA","Todas as atualizações, para sempre"],"cta_h":"O método completo<br>para uma atividade <em>inteligente</em>","cta_p":"Tudo o que precisa para construir uma atividade orquestrada pela IA."},
    },
    "it": {
        "cadre": {"label":"Livello Fondazione","h1":"Le Cadre Mental","subtitle":"Adotti la postura e l'architettura del pensiero che precedono qualsiasi trasformazione duratura. La fondamenta prima di tutte le fondamenta.","img":"/assets/images/le_cadremental.webp","price":"37 €","price_note":"accesso unico","s1_h":"Cosa scoprirà","s1_items":["Le 4 leve mentali che determinano la qualità delle Sue decisioni","Come strutturare il Suo pensiero per eliminare il rumore mentale","La postura adottata dagli imprenditori ad alte prestazioni","Un framework completo per pensare la Sua attività in modo diverso","Applicabile immediatamente — nessuna conoscenza pregressa richiesta"],"s2_h":"Per chi?","s2_p":"Per qualsiasi imprenditore, libero professionista o manager che sente che il suo modo di pensare è il fattore limitante — non le sue competenze, non il suo mercato, non le sue risorse. Per chi vuole costruire una base solida prima di automatizzare qualsiasi cosa.","includes_h":"Cosa è incluso","includes":["Risorsa digitale completa in formato PDF","Framework pratico con applicazione immediata","Strumenti di autovalutazione e matrici decisionali","Accesso completo a vita"],"cta_h":"Pronto a cambiare<br>la Sua <em>postura</em>?","cta_p":"Adotti il quadro mentale che precede ogni trasformazione."},
        "exec": {"label":"Livello Azione","h1":"L'Exécution","subtitle":"I sistemi per passare dall'intenzione all'azione — in modo strutturato, ripetibile ed efficace. L'esecuzione è l'unica strategia che conta.","img":"/assets/images/lexecution.webp","price":"37 €","price_note":"accesso unico","s1_h":"Cosa scoprirà","s1_items":["I 7 sistemi di esecuzione ad alta velocità","Il protocollo di avvio progetto in meno di 24 ore","Il metodo di prioritizzazione senza attrito","Template di riflessione operativa pronti all'uso","Un sistema completo anti-procrastinazione"],"s2_h":"Per chi?","s2_p":"Per chi ha idee ma fatica ad eseguirle in modo coerente. Per chi vuole passare dall'ispirazione all'azione senza perdere slancio o energia lungo la strada.","includes_h":"Cosa è incluso","includes":["Risorsa digitale completa in formato PDF","7 sistemi di esecuzione con template","Protocolli di implementazione per uso immediato","Accesso completo a vita"],"cta_h":"Pronto a eseguire<br>a un <em>livello</em> diverso?","cta_p":"I sistemi che trasformano l'intenzione in risultati concreti."},
        "core": {"label":"Livello Principiante","h1":"CORE OS IA","subtitle":"Le fondamenta di un'attività automatizzata: strumenti IA essenziali, 5 pilastri strutturali e un piano d'azione di 7 giorni per avviare la Sua trasformazione.","img":"/assets/images/coreosia.webp","price":"97 €","price_note":"accesso unico","s1_h":"Cosa scoprirà","s1_items":["I 5 pilastri di un'attività automatizzata","I 12 strumenti IA essenziali spiegati passo dopo passo","Un piano d'azione operativo di 7 giorni","Template pronti all'uso per ogni pilastro","Come delegare all'IA i Suoi primi compiti"],"s2_h":"Per chi?","s2_p":"Per imprenditori che iniziano il loro percorso con l'IA e vogliono una base strutturata, completa e immediatamente applicabile per automatizzare la propria attività.","includes_h":"Cosa è incluso","includes":["Risorsa digitale completa in più formati","5 moduli strutturali","Piano d'azione di 7 giorni con attività quotidiane","Libreria di strumenti e template pronti all'uso","Accesso completo a vita"],"cta_h":"Inizia a costruire la Sua<br>attività <em>automatizzata</em>","cta_p":"Le fondamenta complete per un'attività che lavora per Lei."},
        "biz": {"label":"Livello Avanzato","h1":"Business OS IA","subtitle":"Strategia avanzata, sistemi di monetizzazione e automatizzazione approfondita per un'attività solida e scalabile che non dipende più dal Suo tempo diretto.","img":"/assets/images/businessosia.webp","price":"230 €","price_note":"accesso unico","s1_h":"Cosa scoprirà","s1_items":["Strategia IA avanzata per imprenditori in scala","Sistemi di monetizzazione automatizzati","Tecniche di delega approfondita all'IA","Metodi di scaling senza dipendenza di tempo","Framework completo di automatizzazione dell'attività"],"s2_h":"Per chi?","s2_p":"Per imprenditori che hanno già padroneggiato le basi e vogliono andare oltre — per costruire un sistema che generi risultati indipendentemente dal loro coinvolgimento diretto.","includes_h":"Cosa è incluso","includes":["Modulo di strategia avanzata","Sistemi di monetizzazione e scaling","Protocolli di automatizzazione approfondita","Template e framework premium","Accesso completo a vita"],"cta_h":"Costruisca un'attività che<br>lavori per <em>Lei</em>","cta_p":"Strategia avanzata e automatizzazione approfondita per una vera scalabilità."},
        "kemora": {"label":"Livello Firma","h1":"Kemora OS IA","subtitle":"L'ecosistema completo — la versione più completa del nostro metodo per un'attività interamente orchestrata dall'IA. Tutto. In un unico posto.","img":"/assets/images/kemoraosia.webp","price":"347 €","price_note":"accesso unico","s1_h":"Cosa è incluso","s1_items":["Il metodo Kemora completo dalla fondazione all'ecosistema completo","Tutti i sistemi, i template e i protocolli operativi","Il protocollo completo di orchestrazione IA","Metodi esclusivi di scaling e monetizzazione","Accesso a vita e tutti gli aggiornamenti futuri"],"s2_h":"Per chi?","s2_p":"Per imprenditori ambiziosi che vogliono il metodo completo — per costruire un'attività interamente orchestrata dall'IA, strutturata a lungo termine e capace di scalare senza dipendere dal loro tempo.","includes_h":"L'ecosistema completo","includes":["Le Cadre Mental — Fondazione","L'Exécution — Sistemi di azione","CORE OS IA — Fondamenta di automatizzazione IA","Business OS IA — Strategia avanzata","Il framework completo Kemora OS IA","Tutti gli aggiornamenti, per sempre"],"cta_h":"Il metodo completo<br>per un'attività <em>intelligente</em>","cta_p":"Tutto ciò di cui ha bisogno per costruire un'attività orchestrata dall'IA."},
    },
}

PROD_KEYS = {"cadre":"prod_cadre","exec":"prod_exec","core":"prod_core","biz":"prod_biz","kemora":"prod_kemora"}
STRIPE_KEYS = {"cadre":"cadre-mental","exec":"execution","core":"core-os-ia","biz":"business-os-ia","kemora":"kemora-os-ia"}

def make_product(lang, prod_key):
    c = PROD_CONTENT[lang][prod_key]
    hk = PROD_KEYS[prod_key]
    nav = nav_full(lang, hk)
    slug = PROD_FILES[lang][prod_key]
    stripe_url = STRIPE[STRIPE_KEYS[prod_key]]
    buy_labels = {"fr":"Accéder maintenant","en":"Access now","es":"Acceder ahora","de":"Jetzt zugreifen","pt":"Acessar agora","it":"Accedi ora"}
    disc_labels = {"fr":"Tout inclus. Une seule fois.","en":"All-inclusive. One time.","es":"Todo incluido. Una sola vez.","de":"Alles inklusive. Einmalig.","pt":"Tudo incluído. Uma única vez.","it":"Tutto incluso. Una sola volta."}

    items_html = "".join(f"<li>{item}</li>" for item in c["s1_items"])
    inc_html = "".join(f'<div class="prod-include-item"><span class="prod-include-icon"></span><span>{inc}</span></div>' for inc in c["includes"])

    prod_schema = '{"@context":"https://schema.org","@type":"Product","name":"' + c["h1"] + '","description":"' + c["subtitle"].replace('"',"'") + '","brand":{"@type":"Brand","name":"Kemora Agency"},"offers":{"@type":"Offer","priceCurrency":"EUR","price":"' + c["price"].replace(" €","") + '","availability":"https://schema.org/InStock"}}'

    html = head(lang, c["h1"], c["subtitle"][:160], slug, hk, c["img"])
    html += f'\n<script type="application/ld+json">{prod_schema}</script>\n'
    html += f"\n<style>\n{PROD_CSS}\n</style>\n</head>\n<body id=\"main\">\n{nav}\n"
    html += f"""
<section class="prod-hero">
  <div class="prod-hero-left">
    <div class="prod-hero-left-inner">
      <span class="label reveal">{c["label"]}</span>
      <h1 class="reveal reveal-delay-1">{c["h1"]}</h1>
      <p class="subtitle reveal reveal-delay-2">{c["subtitle"]}</p>
      <div class="prod-price-row reveal reveal-delay-2">
        <span class="prod-price">{c["price"]}</span>
        <span class="prod-price-note">{c["price_note"]}</span>
      </div>
      <div class="reveal reveal-delay-3">
        <a href="{stripe_url}" class="btn-gold">{buy_labels[lang]}</a>
      </div>
    </div>
  </div>
  <div class="prod-hero-right">
    <img src="{c["img"]}" alt="{c["h1"]} — Kemora Agency" fetchpriority="high" width="960" height="1080">
  </div>
</section>
<div class="divider-h container"></div>
<section class="section">
  <div class="container">
    <div class="prod-section">
      <h2 class="reveal">{c["s1_h"]}</h2>
      <ul class="reveal reveal-delay-1">{items_html}</ul>
    </div>
  </div>
</section>
<div class="divider-h container"></div>
<section class="section" style="background:var(--black2);">
  <div class="container">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:start;" class="reveal">
      <div>
        <h2 class="reveal">{c["s2_h"]}</h2>
        <p class="reveal reveal-delay-1">{c["s2_p"]}</p>
      </div>
      <div>
        <h3 class="reveal" style="font-family:var(--sans);font-size:0.72rem;letter-spacing:0.18em;text-transform:uppercase;color:var(--gold);margin-bottom:1.5rem;">{c["includes_h"]}</h3>
        <div class="prod-includes reveal reveal-delay-1">{inc_html}</div>
      </div>
    </div>
  </div>
</section>
<section class="prod-cta">
  <div class="container">
    <h2 class="reveal">{c["cta_h"]}</h2>
    <p class="reveal reveal-delay-1">{c["cta_p"]}</p>
    <div class="reveal reveal-delay-2">
      <a href="{stripe_url}" class="btn-gold" style="margin-right:1rem;">{buy_labels[lang]}</a>
      <span style="font-size:0.72rem;color:var(--muted);letter-spacing:0.1em;text-transform:uppercase;">{disc_labels[lang]}</span>
    </div>
  </div>
</section>
{footer_html(lang)}
{cookie(lang)}
{COMMON_JS}
{nav_js()}
<script>
document.querySelectorAll('.prod-section ul li, .prod-includes .prod-include-item').forEach(function(el,i){{
  el.classList.add('reveal');
  if(i%3===1)el.classList.add('reveal-delay-1');
  if(i%3===2)el.classList.add('reveal-delay-2');
}});
</script>
</body></html>"""
    return html, slug

# ─────────────────────────────────────────────────────────────────────────────
# WRITE ALL PAGES
# ─────────────────────────────────────────────────────────────────────────────

for lang in ["en","es","de","pt","it"]:
    print(f"Writing {lang.upper()} info pages...")
    html, slug = make_fondations(lang)
    write(f"{lang}/{slug}", html)
    html, slug = make_about(lang)
    write(f"{lang}/{slug}", html)
    html, slug = make_faq(lang)
    write(f"{lang}/{slug}", html)
    html, slug = make_contact(lang)
    write(f"{lang}/{slug}", html)
    html, slug = make_booking(lang)
    write(f"{lang}/{slug}", html)

print("Writing product pages...")
for lang in ["en","es","de","pt","it"]:
    d = PROD_DIR[lang]
    os.makedirs(f"{lang}/{d}", exist_ok=True)
    for pk in ["cadre","exec","core","biz","kemora"]:
        html, slug = make_product(lang, pk)
        write(f"{lang}/{d}/{slug}", html)

print("All info + product pages done.")

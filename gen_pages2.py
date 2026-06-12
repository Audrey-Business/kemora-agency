#!/usr/bin/env python3
"""Generate FR new pages + info pages (legal, privacy, faq, about, contact, booking, foundations) all languages."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gen_pages import (head, nav_full, nav_back, footer_html, cookie, COMMON_JS, BASE_CSS, NAV_CSS,
                        STRIPE, SYSTEME_CONTACT, SYSTEME_BOOKING, HREFLANG, PROD_DIR, PROD_FILES,
                        PROD_NAMES, write, FONT_LINK, SITE_URL)

# ─────────────────────────────────────────────────────────────────────────────
# MERCI (THANK-YOU) PAGES — FR
# ─────────────────────────────────────────────────────────────────────────────

MERCI_CSS = BASE_CSS + NAV_CSS + """
  .merci-hero { min-height:100vh; display:flex; align-items:center; padding-top:72px; position:relative; overflow:hidden; }
  .merci-hero-bg { position:absolute; inset:0; background:radial-gradient(ellipse 70% 70% at 50% 40%, rgba(198,161,110,0.05), transparent); pointer-events:none; }
  .merci-hero-inner { position:relative; z-index:1; max-width:720px; margin:0 auto; text-align:center; padding:clamp(4rem,10vw,8rem) clamp(1.5rem,5vw,4rem); }
  .merci-check { width:72px; height:72px; border:1px solid var(--border); border-radius:50%; display:flex; align-items:center; justify-content:center; margin:0 auto 2.5rem; animation:scaleIn 0.6s var(--ease) 0.3s both; }
  .merci-check svg { width:28px; height:28px; stroke:var(--gold); fill:none; stroke-width:1.5; }
  @keyframes scaleIn { from { opacity:0; transform:scale(0.6); } to { opacity:1; transform:scale(1); } }
  .merci-hero h1 { margin-bottom:1.5rem; color:var(--gold); animation:heroFadeUp 0.7s var(--ease) 0.4s both; }
  .merci-hero p { color:var(--muted); font-size:clamp(0.9rem,1.5vw,1.05rem); line-height:1.95; margin-bottom:0.6rem; animation:heroFadeUp 0.7s var(--ease) 0.55s both; }
  @keyframes heroFadeUp { from { opacity:0; transform:translateY(20px); } to { opacity:1; transform:translateY(0); } }
  .upsell-section { background:var(--black2); }
  .upsell-card { border:1px solid var(--border); max-width:680px; margin:0 auto; overflow:hidden; }
  .upsell-card-header { background:linear-gradient(135deg, rgba(198,161,110,0.08), rgba(198,161,110,0.02)); padding:2.5rem; border-bottom:1px solid var(--border2); display:flex; align-items:flex-start; gap:2rem; }
  .upsell-card-header-text .label { display:block; margin-bottom:0.8rem; }
  .upsell-card-header-text h2 { font-size:clamp(1.6rem,3vw,2.4rem); color:var(--gold); margin-bottom:0.8rem; }
  .upsell-card-header-text p { color:var(--muted); font-size:0.9rem; line-height:1.85; }
  .upsell-card-body { padding:2.5rem; }
  .upsell-features { list-style:none; margin-bottom:2rem; display:flex; flex-direction:column; gap:0.9rem; }
  .upsell-features li { display:flex; align-items:flex-start; gap:0.8rem; font-size:0.85rem; color:var(--muted); line-height:1.65; }
  .upsell-features li::before { content:''; width:6px; height:6px; border-radius:50%; background:var(--gold); flex-shrink:0; margin-top:0.45rem; }
  .upsell-price { display:flex; align-items:baseline; gap:0.5rem; margin-bottom:1.5rem; }
  .upsell-price-num { font-family:var(--serif); font-size:2.4rem; color:var(--gold); }
  .upsell-price-note { font-size:0.72rem; letter-spacing:0.1em; text-transform:uppercase; color:var(--muted); }
  .upsell-card-footer { padding:0 2.5rem 2.5rem; }
  .no-upsell-section { text-align:center; max-width:600px; margin:0 auto; }
  .no-upsell-section .label { display:block; margin-bottom:1.5rem; }
  .no-upsell-section h2 { color:var(--gold); margin-bottom:1.2rem; }
  .no-upsell-section p { color:var(--muted); line-height:1.95; margin-bottom:2.5rem; }
  .btn-row { display:flex; gap:1rem; flex-wrap:wrap; justify-content:center; }
"""

def merci_page(lang, prod_key, h1, sub_p, upsell_prod_key=None, upsell_h2=None, upsell_label=None, upsell_desc=None, upsell_features=None, upsell_price=None, upsell_price_note=None):
    """Generate a thank-you page. If upsell_prod_key is None, render celebration-only version."""
    # page-specific slug & hreflang key for this lang
    merci_slugs = {
        ("fr","cadre"):   "merci-cadre-mental.html",
        ("fr","exec"):    "merci-execution.html",
        ("fr","core"):    "merci-core-os-ia.html",
        ("fr","biz"):     "merci-business-os-ia.html",
        ("fr","kemora"):  "merci-kemora-os-ia.html",
        ("en","cadre"):   "thank-you-mental-framework.html",
        ("en","exec"):    "thank-you-execution.html",
        ("en","core"):    "thank-you-core-os-ai.html",
        ("en","biz"):     "thank-you-business-os-ai.html",
        ("en","kemora"):  "thank-you-kemora-os-ai.html",
        ("es","cadre"):   "gracias-marco-mental.html",
        ("es","exec"):    "gracias-ejecucion.html",
        ("es","core"):    "gracias-core-os-ia.html",
        ("es","biz"):     "gracias-business-os-ia.html",
        ("es","kemora"):  "gracias-kemora-os-ia.html",
        ("de","cadre"):   "danke-mentaler-rahmen.html",
        ("de","exec"):    "danke-ausfuehrung.html",
        ("de","core"):    "danke-core-os-ki.html",
        ("de","biz"):     "danke-business-os-ki.html",
        ("de","kemora"):  "danke-kemora-os-ki.html",
        ("pt","cadre"):   "obrigado-quadro-mental.html",
        ("pt","exec"):    "obrigado-execucao.html",
        ("pt","core"):    "obrigado-core-os-ia.html",
        ("pt","biz"):     "obrigado-business-os-ia.html",
        ("pt","kemora"):  "obrigado-kemora-os-ia.html",
        ("it","cadre"):   "grazie-quadro-mentale.html",
        ("it","exec"):    "grazie-esecuzione.html",
        ("it","core"):    "grazie-core-os-ia.html",
        ("it","biz"):     "grazie-business-os-ia.html",
        ("it","kemora"):  "grazie-kemora-os-ia.html",
    }
    slug = merci_slugs.get((lang, prod_key), "merci.html")
    prod_name = PROD_NAMES[prod_key]
    titles = {"fr":"Merci pour votre achat","en":"Thank you for your purchase","es":"Gracias por su compra","de":"Danke für Ihren Kauf","pt":"Obrigado pela sua compra","it":"Grazie per il Suo acquisto"}
    descs = {"fr":f"Merci pour votre achat de {prod_name}. Votre transformation commence maintenant.",
             "en":f"Thank you for purchasing {prod_name}. Your transformation begins now.",
             "es":f"Gracias por adquirir {prod_name}. Su transformación comienza ahora.",
             "de":f"Danke für Ihren Kauf von {prod_name}. Ihre Transformation beginnt jetzt.",
             "pt":f"Obrigado pela compra de {prod_name}. A sua transformação começa agora.",
             "it":f"Grazie per aver acquistato {prod_name}. La Sua trasformazione inizia ora."}

    title = titles[lang]
    desc = descs[lang]
    nav = nav_back(lang, "index")
    check_svg = '<svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>'

    html = head(lang, title, desc, slug, "index")
    html += f"\n<style>\n{MERCI_CSS}\n</style>\n</head>\n<body id=\"main\">\n{nav}\n"
    html += f"""
<section class="merci-hero">
  <div class="merci-hero-bg"></div>
  <div class="merci-hero-inner">
    <div class="merci-check">{check_svg}</div>
    <h1>{h1}</h1>
    {sub_p}
  </div>
</section>
"""
    if upsell_prod_key:
        d = PROD_DIR[lang]
        pf = PROD_FILES[lang]
        stripe_url = STRIPE[upsell_prod_key if upsell_prod_key in STRIPE else "cadre-mental"]
        disc_labels = {"fr":"Découvrir","en":"Discover","es":"Descubrir","de":"Entdecken","pt":"Descobrir","it":"Scoprire"}
        buy_labels = {"fr":"Accéder maintenant","en":"Access now","es":"Acceder ahora","de":"Jetzt zugreifen","pt":"Acessar agora","it":"Accedi ora"}
        features_html = "".join(f"<li>{f}</li>" for f in (upsell_features or []))
        html += f"""
<section class="section upsell-section">
  <div class="container">
    <div class="upsell-card reveal">
      <div class="upsell-card-header">
        <div class="upsell-card-header-text">
          <span class="label">{upsell_label}</span>
          <h2>{upsell_h2}</h2>
          <p>{upsell_desc}</p>
        </div>
      </div>
      <div class="upsell-card-body">
        <ul class="upsell-features">{features_html}</ul>
        <div class="upsell-price">
          <span class="upsell-price-num">{upsell_price}</span>
          <span class="upsell-price-note">{upsell_price_note}</span>
        </div>
      </div>
      <div class="upsell-card-footer">
        <a href="{stripe_url}" class="btn-gold" style="width:100%;justify-content:center;">{buy_labels[lang]}</a>
      </div>
    </div>
  </div>
</section>
"""
    else:
        # No upsell — celebration
        no_upsell_c = {
            "fr":("Votre écosystème complet","Vous avez accès à l'ensemble de la méthode Kemora. C'est le point de départ d'une activité orchestrée par l'intelligence artificielle — à votre rythme, avec votre vision.","Découvrir tous nos produits","Réserver un appel stratégique"),
            "en":("Your complete ecosystem","You now have access to the entire Kemora method. This is the starting point of an AI-orchestrated business — at your pace, with your vision.","Explore all our products","Book a strategic call"),
            "es":("Su ecosistema completo","Ahora tiene acceso a todo el método Kemora. Este es el punto de partida de un negocio orquestado por IA — a su ritmo, con su visión.","Explorar todos nuestros productos","Reservar una llamada estratégica"),
            "de":("Ihr vollständiges Ökosystem","Sie haben nun Zugang zur gesamten Kemora-Methode. Dies ist der Ausgangspunkt eines von KI orchestrierten Unternehmens — in Ihrem Tempo, mit Ihrer Vision.","Alle Produkte erkunden","Strategischen Anruf buchen"),
            "pt":("O seu ecossistema completo","Agora tem acesso a todo o método Kemora. Este é o ponto de partida de um negócio orquestrado pela IA — ao seu ritmo, com a sua visão.","Explorar todos os nossos produtos","Reservar uma chamada estratégica"),
            "it":("Il Suo ecosistema completo","Ha ora accesso all'intero metodo Kemora. Questo è il punto di partenza di un'attività orchestrata dall'IA — al Suo ritmo, con la Sua visione.","Esplora tutti i nostri prodotti","Prenota una chiamata strategica"),
        }[lang]
        ix = "index.html"
        booking_file = HREFLANG["booking"].get(lang,"").replace(lang+"/","")
        html += f"""
<section class="section">
  <div class="container">
    <div class="no-upsell-section">
      <span class="label reveal">Kemora OS IA</span>
      <h2 class="reveal reveal-delay-1">{no_upsell_c[0]}</h2>
      <p class="reveal reveal-delay-2">{no_upsell_c[1]}</p>
      <div class="btn-row reveal reveal-delay-3">
        <a href="/{lang}/{ix}#offre" class="btn-gold">{no_upsell_c[2]}</a>
        <a href="/{lang}/{booking_file}" class="btn-outline">{no_upsell_c[3]}</a>
      </div>
    </div>
  </div>
</section>
"""

    html += f"\n{footer_html(lang)}\n{cookie(lang)}\n{COMMON_JS}\n"
    html += "<script>function toggleMobileNav(){}</script>\n</body>\n</html>"
    return html, slug


# ─────────────────────────────────────────────────────────────────────────────
# LEGAL / PRIVACY PAGES
# ─────────────────────────────────────────────────────────────────────────────

LEGAL_CSS = BASE_CSS + NAV_CSS + """
  .legal-hero { padding:clamp(6rem,12vw,10rem) 0 clamp(3rem,5vw,5rem); }
  .legal-hero h1 { color:var(--gold); margin-bottom:1rem; }
  .legal-hero .label { display:block; margin-bottom:1.5rem; }
  .legal-content { max-width:800px; }
  .legal-content h2 { font-family:var(--sans); font-size:0.78rem; font-weight:500; letter-spacing:0.18em; text-transform:uppercase; color:var(--gold); margin:3rem 0 1rem; padding-top:2rem; border-top:1px solid var(--border2); }
  .legal-content h2:first-of-type { border-top:none; padding-top:0; }
  .legal-content p { color:var(--muted); font-size:0.88rem; line-height:1.9; margin-bottom:1rem; }
  .legal-content a { color:var(--gold); text-decoration:underline; text-underline-offset:3px; }
  .legal-content ul { list-style:none; padding:0; margin-bottom:1rem; }
  .legal-content ul li { color:var(--muted); font-size:0.88rem; line-height:1.9; padding-left:1.2rem; position:relative; }
  .legal-content ul li::before { content:'—'; position:absolute; left:0; color:var(--gold); }
"""

def legal_page(lang):
    CONTENT = {
        "fr": {
            "slug": "mentions-legales.html",
            "title": "Mentions légales",
            "h1": "Mentions légales",
            "label": "Informations légales",
            "body": """
<h2>Éditeur du site</h2>
<p>Le site kemora-agency.com est édité par Kemora Agency, entreprise individuelle.<br>
Adresse : France<br>
Contact : <a href="mailto:contact@kemora-agency.com">contact@kemora-agency.com</a></p>

<h2>Hébergement</h2>
<p>Le site est hébergé par Vercel Inc., 340 Pine Street, Suite 701, San Francisco, CA 94104, États-Unis.<br>
Site : <a href="https://vercel.com" rel="noopener noreferrer">vercel.com</a></p>

<h2>Propriété intellectuelle</h2>
<p>L'ensemble du contenu présent sur ce site (textes, images, visuels, structure, code) est la propriété exclusive de Kemora Agency et est protégé par les lois françaises et internationales relatives à la propriété intellectuelle.</p>
<p>Toute reproduction, représentation, modification, publication, transmission ou dénaturation de ce contenu, sans l'autorisation préalable et écrite de Kemora Agency, est strictement interdite.</p>

<h2>Responsabilité</h2>
<p>Kemora Agency s'efforce de fournir des informations exactes et à jour sur ce site. Toutefois, elle ne peut garantir l'exactitude, la complétude ou l'actualité des informations diffusées. L'utilisateur reconnaît utiliser ces informations sous sa responsabilité exclusive.</p>

<h2>Liens hypertextes</h2>
<p>Le site peut contenir des liens vers des sites tiers. Kemora Agency n'exerce aucun contrôle sur ces sites et décline toute responsabilité quant à leur contenu ou leurs pratiques.</p>

<h2>Droit applicable</h2>
<p>Le présent site et ses mentions légales sont soumis au droit français. En cas de litige, les tribunaux français seront seuls compétents.</p>

<h2>Contact</h2>
<p>Pour toute question relative aux présentes mentions légales, vous pouvez nous contacter à l'adresse suivante : <a href="mailto:contact@kemora-agency.com">contact@kemora-agency.com</a></p>
"""
        },
        "en": {
            "slug": "legal-notice.html",
            "title": "Legal Notice",
            "h1": "Legal Notice",
            "label": "Legal information",
            "body": """
<h2>Publisher</h2>
<p>The website kemora-agency.com is published by Kemora Agency, a sole proprietorship.<br>
Address: France<br>
Contact: <a href="mailto:contact@kemora-agency.com">contact@kemora-agency.com</a></p>

<h2>Hosting</h2>
<p>The website is hosted by Vercel Inc., 340 Pine Street, Suite 701, San Francisco, CA 94104, United States.<br>
Website: <a href="https://vercel.com" rel="noopener noreferrer">vercel.com</a></p>

<h2>Intellectual property</h2>
<p>All content on this website (texts, images, visuals, structure, code) is the exclusive property of Kemora Agency and is protected by French and international intellectual property laws.</p>
<p>Any reproduction, representation, modification, publication, transmission or distortion of this content, without the prior written authorisation of Kemora Agency, is strictly prohibited.</p>

<h2>Liability</h2>
<p>Kemora Agency strives to provide accurate and up-to-date information on this website. However, it cannot guarantee the accuracy, completeness or currency of the information provided. The user acknowledges using this information under their sole responsibility.</p>

<h2>Hyperlinks</h2>
<p>The website may contain links to third-party websites. Kemora Agency has no control over these websites and accepts no responsibility for their content or practices.</p>

<h2>Applicable law</h2>
<p>This website and its legal notices are subject to French law. In the event of a dispute, French courts shall have sole jurisdiction.</p>

<h2>Contact</h2>
<p>For any question regarding this legal notice, you may contact us at: <a href="mailto:contact@kemora-agency.com">contact@kemora-agency.com</a></p>
"""
        },
        "es": {
            "slug": "menciones-legales.html",
            "title": "Menciones Legales",
            "h1": "Menciones Legales",
            "label": "Información legal",
            "body": """
<h2>Editor del sitio</h2>
<p>El sitio web kemora-agency.com está editado por Kemora Agency, empresa individual.<br>
Dirección: Francia<br>
Contacto: <a href="mailto:contact@kemora-agency.com">contact@kemora-agency.com</a></p>

<h2>Alojamiento</h2>
<p>El sitio está alojado por Vercel Inc., 340 Pine Street, Suite 701, San Francisco, CA 94104, Estados Unidos.<br>
Sitio web: <a href="https://vercel.com" rel="noopener noreferrer">vercel.com</a></p>

<h2>Propiedad intelectual</h2>
<p>Todo el contenido presente en este sitio (textos, imágenes, visuales, estructura, código) es propiedad exclusiva de Kemora Agency y está protegido por las leyes francesas e internacionales relativas a la propiedad intelectual.</p>
<p>Cualquier reproducción, representación, modificación, publicación, transmisión o desnaturalización de este contenido, sin la autorización previa y escrita de Kemora Agency, está estrictamente prohibida.</p>

<h2>Responsabilidad</h2>
<p>Kemora Agency se esfuerza por proporcionar información precisa y actualizada en este sitio. Sin embargo, no puede garantizar la exactitud, integridad o actualidad de la información difundida. El usuario reconoce utilizar esta información bajo su exclusiva responsabilidad.</p>

<h2>Hipervínculos</h2>
<p>El sitio puede contener enlaces a sitios de terceros. Kemora Agency no ejerce ningún control sobre estos sitios y declina toda responsabilidad en cuanto a su contenido o prácticas.</p>

<h2>Ley aplicable</h2>
<p>El presente sitio y sus menciones legales están sujetos al derecho francés. En caso de litigio, los tribunales franceses serán los únicos competentes.</p>

<h2>Contacto</h2>
<p>Para cualquier pregunta relativa a las presentes menciones legales, puede contactarnos en: <a href="mailto:contact@kemora-agency.com">contact@kemora-agency.com</a></p>
"""
        },
        "de": {
            "slug": "impressum.html",
            "title": "Impressum",
            "h1": "Impressum",
            "label": "Rechtliche Angaben",
            "body": """
<h2>Herausgeber</h2>
<p>Die Website kemora-agency.com wird von Kemora Agency, einem Einzelunternehmen, herausgegeben.<br>
Adresse: Frankreich<br>
Kontakt: <a href="mailto:contact@kemora-agency.com">contact@kemora-agency.com</a></p>

<h2>Hosting</h2>
<p>Die Website wird von Vercel Inc., 340 Pine Street, Suite 701, San Francisco, CA 94104, Vereinigte Staaten, gehostet.<br>
Website: <a href="https://vercel.com" rel="noopener noreferrer">vercel.com</a></p>

<h2>Geistiges Eigentum</h2>
<p>Alle Inhalte dieser Website (Texte, Bilder, Grafiken, Struktur, Code) sind ausschließliches Eigentum von Kemora Agency und durch französisches und internationales Urheberrecht geschützt.</p>
<p>Jede Vervielfältigung, Darstellung, Änderung, Veröffentlichung, Übertragung oder Entstellung dieser Inhalte ohne vorherige schriftliche Genehmigung von Kemora Agency ist streng untersagt.</p>

<h2>Haftung</h2>
<p>Kemora Agency bemüht sich, genaue und aktuelle Informationen auf dieser Website bereitzustellen. Es kann jedoch keine Garantie für die Richtigkeit, Vollständigkeit oder Aktualität der bereitgestellten Informationen übernommen werden. Der Nutzer bestätigt, diese Informationen auf eigene Verantwortung zu verwenden.</p>

<h2>Hyperlinks</h2>
<p>Die Website kann Links zu Drittanbieter-Websites enthalten. Kemora Agency hat keine Kontrolle über diese Websites und übernimmt keine Verantwortung für deren Inhalt oder Praktiken.</p>

<h2>Anwendbares Recht</h2>
<p>Diese Website und ihre rechtlichen Angaben unterliegen französischem Recht. Bei Streitigkeiten sind ausschließlich französische Gerichte zuständig.</p>

<h2>Kontakt</h2>
<p>Bei Fragen zu diesem Impressum können Sie uns kontaktieren unter: <a href="mailto:contact@kemora-agency.com">contact@kemora-agency.com</a></p>
"""
        },
        "pt": {
            "slug": "mencoes-legais.html",
            "title": "Menções Legais",
            "h1": "Menções Legais",
            "label": "Informação legal",
            "body": """
<h2>Editor do site</h2>
<p>O site kemora-agency.com é editado pela Kemora Agency, empresa individual.<br>
Endereço: França<br>
Contacto: <a href="mailto:contact@kemora-agency.com">contact@kemora-agency.com</a></p>

<h2>Alojamento</h2>
<p>O site é alojado pela Vercel Inc., 340 Pine Street, Suite 701, San Francisco, CA 94104, Estados Unidos.<br>
Site: <a href="https://vercel.com" rel="noopener noreferrer">vercel.com</a></p>

<h2>Propriedade intelectual</h2>
<p>Todo o conteúdo presente neste site (textos, imagens, visuais, estrutura, código) é propriedade exclusiva da Kemora Agency e está protegido pelas leis francesas e internacionais relativas à propriedade intelectual.</p>
<p>Qualquer reprodução, representação, modificação, publicação, transmissão ou desnaturação deste conteúdo, sem a autorização prévia e escrita da Kemora Agency, é estritamente proibida.</p>

<h2>Responsabilidade</h2>
<p>A Kemora Agency esforça-se por fornecer informações precisas e atualizadas neste site. No entanto, não pode garantir a exatidão, integridade ou atualidade das informações difundidas. O utilizador reconhece utilizar estas informações sob a sua exclusiva responsabilidade.</p>

<h2>Hiperligações</h2>
<p>O site pode conter ligações para sites de terceiros. A Kemora Agency não exerce qualquer controlo sobre estes sites e declina toda a responsabilidade quanto ao seu conteúdo ou práticas.</p>

<h2>Lei aplicável</h2>
<p>O presente site e as suas menções legais estão sujeitos ao direito francês. Em caso de litígio, os tribunais franceses serão os únicos competentes.</p>

<h2>Contacto</h2>
<p>Para qualquer questão relativa às presentes menções legais, pode contactar-nos em: <a href="mailto:contact@kemora-agency.com">contact@kemora-agency.com</a></p>
"""
        },
        "it": {
            "slug": "note-legali.html",
            "title": "Note Legali",
            "h1": "Note Legali",
            "label": "Informazioni legali",
            "body": """
<h2>Editore del sito</h2>
<p>Il sito kemora-agency.com è pubblicato da Kemora Agency, impresa individuale.<br>
Indirizzo: Francia<br>
Contatto: <a href="mailto:contact@kemora-agency.com">contact@kemora-agency.com</a></p>

<h2>Hosting</h2>
<p>Il sito è ospitato da Vercel Inc., 340 Pine Street, Suite 701, San Francisco, CA 94104, Stati Uniti.<br>
Sito web: <a href="https://vercel.com" rel="noopener noreferrer">vercel.com</a></p>

<h2>Proprietà intellettuale</h2>
<p>Tutti i contenuti presenti su questo sito (testi, immagini, visuali, struttura, codice) sono di proprietà esclusiva di Kemora Agency e sono protetti dalle leggi francesi e internazionali relative alla proprietà intellettuale.</p>
<p>Qualsiasi riproduzione, rappresentazione, modifica, pubblicazione, trasmissione o alterazione di questi contenuti, senza la preventiva autorizzazione scritta di Kemora Agency, è severamente vietata.</p>

<h2>Responsabilità</h2>
<p>Kemora Agency si adopera per fornire informazioni accurate e aggiornate su questo sito. Tuttavia, non può garantire l'esattezza, la completezza o l'attualità delle informazioni diffuse. L'utente riconosce di utilizzare tali informazioni sotto la propria esclusiva responsabilità.</p>

<h2>Hyperlink</h2>
<p>Il sito può contenere link a siti di terze parti. Kemora Agency non esercita alcun controllo su questi siti e declina ogni responsabilità in merito al loro contenuto o pratiche.</p>

<h2>Legge applicabile</h2>
<p>Il presente sito e le sue note legali sono soggetti al diritto francese. In caso di controversia, i tribunali francesi saranno gli unici competenti.</p>

<h2>Contatto</h2>
<p>Per qualsiasi domanda relativa alle presenti note legali, può contattarci a: <a href="mailto:contact@kemora-agency.com">contact@kemora-agency.com</a></p>
"""
        },
    }
    c = CONTENT[lang]
    nav = nav_back(lang, "legal")
    html = head(lang, c["title"], c["title"] + " — Kemora Agency", c["slug"], "legal")
    html += f"\n<style>\n{LEGAL_CSS}\n</style>\n</head>\n<body id=\"main\">\n{nav}\n"
    html += f"""
<section class="legal-hero section">
  <div class="container">
    <span class="label">{c["label"]}</span>
    <h1>{c["h1"]}</h1>
  </div>
</section>
<div class="divider-h container"></div>
<section class="section">
  <div class="container">
    <div class="legal-content">{c["body"]}</div>
  </div>
</section>
"""
    html += f"\n{footer_html(lang)}\n{cookie(lang)}\n{COMMON_JS}\n"
    html += "<script>function toggleMobileNav(){}</script>\n</body>\n</html>"
    return html, c["slug"]


def privacy_page(lang):
    CONTENT = {
        "fr": {
            "slug": "politique-confidentialite.html",
            "title": "Politique de confidentialité",
            "h1": "Politique de confidentialité",
            "label": "Protection des données",
            "body": """
<h2>Responsable du traitement</h2>
<p>Kemora Agency est responsable du traitement de vos données personnelles collectées via le site kemora-agency.com.</p>

<h2>Données collectées</h2>
<p>Nous collectons uniquement les données que vous nous transmettez volontairement via nos formulaires de contact et de réservation :</p>
<ul>
  <li>Nom et prénom</li>
  <li>Adresse e-mail</li>
  <li>Informations relatives à votre activité (si renseignées)</li>
</ul>

<h2>Finalités du traitement</h2>
<p>Vos données sont utilisées exclusivement pour :</p>
<ul>
  <li>Répondre à vos demandes de contact</li>
  <li>Organiser les appels stratégiques réservés</li>
  <li>Vous envoyer les ressources commandées</li>
  <li>Vous adresser des communications relatives à nos offres (si vous y avez consenti)</li>
</ul>

<h2>Base légale</h2>
<p>Le traitement est fondé sur votre consentement explicite (article 6.1.a du RGPD) et sur l'exécution du contrat lorsque vous procédez à un achat (article 6.1.b du RGPD).</p>

<h2>Durée de conservation</h2>
<p>Vos données sont conservées pour une durée maximale de 3 ans à compter de votre dernière interaction avec nous, sauf obligation légale contraire.</p>

<h2>Partage des données</h2>
<p>Vos données ne sont jamais vendues à des tiers. Elles peuvent être partagées avec nos prestataires de services (Systeme.io pour la gestion des formulaires, Stripe pour les paiements) dans la stricte limite de leurs missions.</p>

<h2>Vos droits</h2>
<p>Conformément au RGPD, vous disposez des droits suivants :</p>
<ul>
  <li>Droit d'accès à vos données</li>
  <li>Droit de rectification</li>
  <li>Droit à l'effacement (« droit à l'oubli »)</li>
  <li>Droit à la limitation du traitement</li>
  <li>Droit à la portabilité</li>
  <li>Droit d'opposition</li>
</ul>
<p>Pour exercer ces droits, contactez-nous à : <a href="mailto:contact@kemora-agency.com">contact@kemora-agency.com</a></p>

<h2>Cookies et traceurs</h2>
<p>Le site utilise Plausible Analytics, un outil d'analyse respectueux de la vie privée, sans dépôt de cookie, activé uniquement après votre consentement explicite. Aucun cookie publicitaire ou de profilage n'est utilisé.</p>

<h2>Sécurité</h2>
<p>Nous mettons en œuvre des mesures techniques et organisationnelles appropriées pour protéger vos données contre tout accès non autorisé, perte ou divulgation.</p>

<h2>Contact et réclamation</h2>
<p>Pour toute question, contactez-nous à : <a href="mailto:contact@kemora-agency.com">contact@kemora-agency.com</a><br>
Vous avez également le droit d'introduire une réclamation auprès de la CNIL (www.cnil.fr).</p>
"""
        },
        "en": {
            "slug": "privacy-policy.html",
            "title": "Privacy Policy",
            "h1": "Privacy Policy",
            "label": "Data protection",
            "body": """
<h2>Data controller</h2>
<p>Kemora Agency is the data controller for personal data collected through the website kemora-agency.com.</p>

<h2>Data collected</h2>
<p>We only collect the data you voluntarily provide through our contact and booking forms:</p>
<ul>
  <li>First and last name</li>
  <li>Email address</li>
  <li>Information about your business (if provided)</li>
</ul>

<h2>Purposes of processing</h2>
<p>Your data is used exclusively to:</p>
<ul>
  <li>Respond to your contact requests</li>
  <li>Schedule booked strategic calls</li>
  <li>Send you the resources you ordered</li>
  <li>Send you communications about our offers (if you have consented)</li>
</ul>

<h2>Legal basis</h2>
<p>Processing is based on your explicit consent (Article 6.1.a of GDPR) and on the performance of a contract when you make a purchase (Article 6.1.b of GDPR).</p>

<h2>Retention period</h2>
<p>Your data is kept for a maximum of 3 years from your last interaction with us, unless required by law.</p>

<h2>Data sharing</h2>
<p>Your data is never sold to third parties. It may be shared with our service providers (Systeme.io for form management, Stripe for payments) strictly within the scope of their services.</p>

<h2>Your rights</h2>
<p>In accordance with GDPR, you have the following rights:</p>
<ul>
  <li>Right of access to your data</li>
  <li>Right to rectification</li>
  <li>Right to erasure ("right to be forgotten")</li>
  <li>Right to restriction of processing</li>
  <li>Right to data portability</li>
  <li>Right to object</li>
</ul>
<p>To exercise these rights, contact us at: <a href="mailto:contact@kemora-agency.com">contact@kemora-agency.com</a></p>

<h2>Cookies and trackers</h2>
<p>The website uses Plausible Analytics, a privacy-respecting analytics tool, with no cookies, activated only after your explicit consent. No advertising or profiling cookies are used.</p>

<h2>Security</h2>
<p>We implement appropriate technical and organisational measures to protect your data against unauthorised access, loss or disclosure.</p>

<h2>Contact and complaints</h2>
<p>For any questions, contact us at: <a href="mailto:contact@kemora-agency.com">contact@kemora-agency.com</a><br>
You also have the right to lodge a complaint with the relevant data protection authority.</p>
"""
        },
        "es": {
            "slug": "politica-privacidad.html",
            "title": "Política de Privacidad",
            "h1": "Política de Privacidad",
            "label": "Protección de datos",
            "body": """
<h2>Responsable del tratamiento</h2>
<p>Kemora Agency es responsable del tratamiento de sus datos personales recopilados a través del sitio kemora-agency.com.</p>

<h2>Datos recopilados</h2>
<p>Solo recopilamos los datos que usted nos transmite voluntariamente a través de nuestros formularios de contacto y reserva:</p>
<ul>
  <li>Nombre y apellidos</li>
  <li>Dirección de correo electrónico</li>
  <li>Información sobre su actividad (si se facilita)</li>
</ul>

<h2>Finalidades del tratamiento</h2>
<p>Sus datos se utilizan exclusivamente para:</p>
<ul>
  <li>Responder a sus solicitudes de contacto</li>
  <li>Organizar las llamadas estratégicas reservadas</li>
  <li>Enviarle los recursos solicitados</li>
  <li>Enviarle comunicaciones sobre nuestras ofertas (si ha prestado su consentimiento)</li>
</ul>

<h2>Base jurídica</h2>
<p>El tratamiento se basa en su consentimiento explícito (artículo 6.1.a del RGPD) y en la ejecución del contrato cuando realiza una compra (artículo 6.1.b del RGPD).</p>

<h2>Período de conservación</h2>
<p>Sus datos se conservan durante un máximo de 3 años desde su última interacción con nosotros, salvo obligación legal contraria.</p>

<h2>Compartición de datos</h2>
<p>Sus datos nunca se venden a terceros. Pueden compartirse con nuestros proveedores de servicios (Systeme.io para la gestión de formularios, Stripe para los pagos) en los estrictos límites de sus funciones.</p>

<h2>Sus derechos</h2>
<p>De conformidad con el RGPD, usted dispone de los siguientes derechos:</p>
<ul>
  <li>Derecho de acceso a sus datos</li>
  <li>Derecho de rectificación</li>
  <li>Derecho de supresión («derecho al olvido»)</li>
  <li>Derecho a la limitación del tratamiento</li>
  <li>Derecho a la portabilidad</li>
  <li>Derecho de oposición</li>
</ul>
<p>Para ejercer estos derechos, contáctenos en: <a href="mailto:contact@kemora-agency.com">contact@kemora-agency.com</a></p>

<h2>Cookies y rastreadores</h2>
<p>El sitio utiliza Plausible Analytics, una herramienta de análisis respetuosa con la privacidad, sin cookies, activada solo tras su consentimiento explícito. No se utilizan cookies publicitarias ni de perfilado.</p>

<h2>Seguridad</h2>
<p>Implementamos las medidas técnicas y organizativas adecuadas para proteger sus datos contra el acceso no autorizado, la pérdida o la divulgación.</p>

<h2>Contacto y reclamaciones</h2>
<p>Para cualquier consulta, contáctenos en: <a href="mailto:contact@kemora-agency.com">contact@kemora-agency.com</a><br>
También tiene derecho a presentar una reclamación ante la autoridad de protección de datos competente.</p>
"""
        },
        "de": {
            "slug": "datenschutz.html",
            "title": "Datenschutzerklärung",
            "h1": "Datenschutzerklärung",
            "label": "Datenschutz",
            "body": """
<h2>Verantwortlicher</h2>
<p>Kemora Agency ist Verantwortlicher für die Verarbeitung der über kemora-agency.com erhobenen personenbezogenen Daten.</p>

<h2>Erhobene Daten</h2>
<p>Wir erheben ausschließlich die Daten, die Sie uns freiwillig über unsere Kontakt- und Buchungsformulare mitteilen:</p>
<ul>
  <li>Vor- und Nachname</li>
  <li>E-Mail-Adresse</li>
  <li>Angaben zu Ihrer Tätigkeit (falls angegeben)</li>
</ul>

<h2>Verarbeitungszwecke</h2>
<p>Ihre Daten werden ausschließlich verwendet für:</p>
<ul>
  <li>Beantwortung Ihrer Kontaktanfragen</li>
  <li>Organisation der gebuchten Strategiegespräche</li>
  <li>Zusendung der bestellten Ressourcen</li>
  <li>Zusendung von Mitteilungen zu unseren Angeboten (sofern Sie eingewilligt haben)</li>
</ul>

<h2>Rechtsgrundlage</h2>
<p>Die Verarbeitung erfolgt auf Grundlage Ihrer ausdrücklichen Einwilligung (Art. 6 Abs. 1 lit. a DSGVO) und bei Käufen zur Vertragserfüllung (Art. 6 Abs. 1 lit. b DSGVO).</p>

<h2>Speicherdauer</h2>
<p>Ihre Daten werden für maximal 3 Jahre ab Ihrem letzten Kontakt mit uns gespeichert, sofern keine gesetzliche Aufbewahrungspflicht besteht.</p>

<h2>Datenweitergabe</h2>
<p>Ihre Daten werden niemals an Dritte verkauft. Sie können an unsere Dienstleister (Systeme.io für die Formularverwaltung, Stripe für Zahlungen) ausschließlich im Rahmen ihrer Aufgaben weitergegeben werden.</p>

<h2>Ihre Rechte</h2>
<p>Gemäß DSGVO haben Sie folgende Rechte:</p>
<ul>
  <li>Auskunftsrecht</li>
  <li>Berichtigungsrecht</li>
  <li>Löschungsrecht ("Recht auf Vergessenwerden")</li>
  <li>Recht auf Einschränkung der Verarbeitung</li>
  <li>Recht auf Datenübertragbarkeit</li>
  <li>Widerspruchsrecht</li>
</ul>
<p>Um diese Rechte auszuüben, kontaktieren Sie uns unter: <a href="mailto:contact@kemora-agency.com">contact@kemora-agency.com</a></p>

<h2>Cookies und Tracker</h2>
<p>Die Website verwendet Plausible Analytics, ein datenschutzkonformes Analysetool ohne Cookies, das erst nach Ihrer ausdrücklichen Einwilligung aktiviert wird. Es werden keine Werbe- oder Profiling-Cookies verwendet.</p>

<h2>Sicherheit</h2>
<p>Wir treffen geeignete technische und organisatorische Maßnahmen zum Schutz Ihrer Daten vor unbefugtem Zugriff, Verlust oder Offenlegung.</p>

<h2>Kontakt und Beschwerden</h2>
<p>Bei Fragen kontaktieren Sie uns unter: <a href="mailto:contact@kemora-agency.com">contact@kemora-agency.com</a><br>
Sie haben auch das Recht, eine Beschwerde bei der zuständigen Datenschutzaufsichtsbehörde einzureichen.</p>
"""
        },
        "pt": {
            "slug": "politica-privacidade.html",
            "title": "Política de Privacidade",
            "h1": "Política de Privacidade",
            "label": "Proteção de dados",
            "body": """
<h2>Responsável pelo tratamento</h2>
<p>A Kemora Agency é responsável pelo tratamento dos dados pessoais recolhidos através do site kemora-agency.com.</p>

<h2>Dados recolhidos</h2>
<p>Recolhemos apenas os dados que nos transmite voluntariamente através dos nossos formulários de contacto e reserva:</p>
<ul>
  <li>Nome e apelido</li>
  <li>Endereço de e-mail</li>
  <li>Informações sobre a sua atividade (se fornecidas)</li>
</ul>

<h2>Finalidades do tratamento</h2>
<p>Os seus dados são utilizados exclusivamente para:</p>
<ul>
  <li>Responder aos seus pedidos de contacto</li>
  <li>Organizar as chamadas estratégicas reservadas</li>
  <li>Enviar-lhe os recursos encomendados</li>
  <li>Enviar-lhe comunicações sobre as nossas ofertas (se tiver dado o seu consentimento)</li>
</ul>

<h2>Base legal</h2>
<p>O tratamento baseia-se no seu consentimento explícito (artigo 6.º, n.º 1, alínea a) do RGPD) e na execução do contrato quando realiza uma compra (artigo 6.º, n.º 1, alínea b) do RGPD).</p>

<h2>Período de conservação</h2>
<p>Os seus dados são conservados por um máximo de 3 anos a partir da sua última interação connosco, salvo obrigação legal em contrário.</p>

<h2>Partilha de dados</h2>
<p>Os seus dados nunca são vendidos a terceiros. Podem ser partilhados com os nossos prestadores de serviços (Systeme.io para gestão de formulários, Stripe para pagamentos) estritamente no âmbito das suas funções.</p>

<h2>Os seus direitos</h2>
<p>Em conformidade com o RGPD, tem os seguintes direitos:</p>
<ul>
  <li>Direito de acesso aos seus dados</li>
  <li>Direito de retificação</li>
  <li>Direito ao apagamento («direito a ser esquecido»)</li>
  <li>Direito à limitação do tratamento</li>
  <li>Direito à portabilidade</li>
  <li>Direito de oposição</li>
</ul>
<p>Para exercer estes direitos, contacte-nos em: <a href="mailto:contact@kemora-agency.com">contact@kemora-agency.com</a></p>

<h2>Cookies e rastreadores</h2>
<p>O site utiliza o Plausible Analytics, uma ferramenta de análise que respeita a privacidade, sem cookies, ativada apenas após o seu consentimento explícito. Não são utilizados cookies publicitários ou de perfilagem.</p>

<h2>Segurança</h2>
<p>Implementamos medidas técnicas e organizativas adequadas para proteger os seus dados contra acesso não autorizado, perda ou divulgação.</p>

<h2>Contacto e reclamações</h2>
<p>Para qualquer questão, contacte-nos em: <a href="mailto:contact@kemora-agency.com">contact@kemora-agency.com</a><br>
Tem também o direito de apresentar uma reclamação à autoridade de proteção de dados competente.</p>
"""
        },
        "it": {
            "slug": "politica-privacy.html",
            "title": "Politica sulla Privacy",
            "h1": "Politica sulla Privacy",
            "label": "Protezione dei dati",
            "body": """
<h2>Titolare del trattamento</h2>
<p>Kemora Agency è titolare del trattamento dei dati personali raccolti tramite il sito kemora-agency.com.</p>

<h2>Dati raccolti</h2>
<p>Raccogliamo esclusivamente i dati che ci trasmette volontariamente attraverso i nostri moduli di contatto e prenotazione:</p>
<ul>
  <li>Nome e cognome</li>
  <li>Indirizzo e-mail</li>
  <li>Informazioni sulla Sua attività (se fornite)</li>
</ul>

<h2>Finalità del trattamento</h2>
<p>I Suoi dati vengono utilizzati esclusivamente per:</p>
<ul>
  <li>Rispondere alle Sue richieste di contatto</li>
  <li>Organizzare le chiamate strategiche prenotate</li>
  <li>Inviarle le risorse ordinate</li>
  <li>Inviarle comunicazioni relative alle nostre offerte (se ha prestato il consenso)</li>
</ul>

<h2>Base giuridica</h2>
<p>Il trattamento si basa sul Suo consenso esplicito (art. 6, par. 1, lett. a del RGPD) e sull'esecuzione del contratto quando effettua un acquisto (art. 6, par. 1, lett. b del RGPD).</p>

<h2>Periodo di conservazione</h2>
<p>I Suoi dati vengono conservati per un massimo di 3 anni dall'ultima interazione con noi, salvo obbligo di legge contrario.</p>

<h2>Condivisione dei dati</h2>
<p>I Suoi dati non vengono mai venduti a terzi. Possono essere condivisi con i nostri fornitori di servizi (Systeme.io per la gestione dei moduli, Stripe per i pagamenti) strettamente nei limiti dei loro incarichi.</p>

<h2>I Suoi diritti</h2>
<p>In conformità con il RGPD, Lei dispone dei seguenti diritti:</p>
<ul>
  <li>Diritto di accesso ai Suoi dati</li>
  <li>Diritto di rettifica</li>
  <li>Diritto alla cancellazione («diritto all'oblio»)</li>
  <li>Diritto alla limitazione del trattamento</li>
  <li>Diritto alla portabilità</li>
  <li>Diritto di opposizione</li>
</ul>
<p>Per esercitare questi diritti, ci contatti a: <a href="mailto:contact@kemora-agency.com">contact@kemora-agency.com</a></p>

<h2>Cookie e tracker</h2>
<p>Il sito utilizza Plausible Analytics, uno strumento di analisi rispettoso della privacy, senza cookie, attivato solo dopo il Suo consenso esplicito. Non vengono utilizzati cookie pubblicitari o di profilazione.</p>

<h2>Sicurezza</h2>
<p>Implementiamo misure tecniche e organizzative appropriate per proteggere i Suoi dati da accessi non autorizzati, perdite o divulgazioni.</p>

<h2>Contatto e reclami</h2>
<p>Per qualsiasi domanda, ci contatti a: <a href="mailto:contact@kemora-agency.com">contact@kemora-agency.com</a><br>
Ha anche il diritto di presentare un reclamo all'autorità di protezione dei dati competente.</p>
"""
        },
    }
    c = CONTENT[lang]
    nav = nav_back(lang, "privacy")
    html = head(lang, c["title"], c["title"] + " — Kemora Agency", c["slug"], "privacy")
    html += f"\n<style>\n{LEGAL_CSS}\n</style>\n</head>\n<body id=\"main\">\n{nav}\n"
    html += f"""
<section class="legal-hero section">
  <div class="container">
    <span class="label">{c["label"]}</span>
    <h1>{c["h1"]}</h1>
  </div>
</section>
<div class="divider-h container"></div>
<section class="section">
  <div class="container">
    <div class="legal-content">{c["body"]}</div>
  </div>
</section>
"""
    html += f"\n{footer_html(lang)}\n{cookie(lang)}\n{COMMON_JS}\n"
    html += "<script>function toggleMobileNav(){}</script>\n</body>\n</html>"
    return html, c["slug"]


# ─────────────────────────────────────────────────────────────────────────────
# GENERATE ALL PAGES
# ─────────────────────────────────────────────────────────────────────────────

# FR merci pages
MERCI_DATA_FR = [
    # (prod_key, h1, sub_p, upsell_prod_key, upsell_h2, upsell_label, upsell_desc, upsell_features, upsell_price, upsell_price_note)
    ("cadre",
     "Bienvenue dans<br>Le Cadre Mental",
     '<p>Votre accès est en route. Vous avez pris la première décision — <em>la plus déterminante</em>.<br>Ce qui suit commence ici.</p>',
     "execution",
     "Passez à l'étape suivante",
     "Offre complémentaire",
     "Vous avez posé les fondations. Maintenant, construisez les systèmes qui vont transformer votre vision en réalité concrète.",
     ["Les 7 systèmes d'exécution à haute vélocité","Le protocole de démarrage de projet en moins de 24h","La méthode de priorisation sans friction","Les templates de réflexion opérationnelle","Accès immédiat — format numérique"],
     "37 €", "accès unique"),
    ("exec",
     "Bienvenue dans<br>L'Exécution",
     '<p>Votre accès est en cours d\'envoi. Vous êtes passé à l\'action — c\'est <em>exactement ça</em> l\'exécution.<br>La prochaine étape : structurer votre activité avec l\'IA.</p>',
     "core-os-ia",
     "Structurez votre activité avec l'IA",
     "Offre complémentaire",
     "Vous savez comment vous mettre en mouvement. Maintenant, automatisez ce mouvement — avec les bons systèmes.",
     ["Les 5 piliers d'un business automatisé","Les outils IA essentiels, expliqués pas à pas","Un plan d'action opérationnel sur 7 jours","Des templates prêts à l'emploi","Accès immédiat — format numérique"],
     "97 €", "accès unique"),
    ("core",
     "Bienvenue dans<br>CORE OS IA",
     '<p>Vos accès sont en préparation. Vous venez de prendre une décision <em>structurante</em> pour votre activité.<br>La prochaine étape : aller plus loin.</p>',
     "business-os-ia",
     "Passez au niveau supérieur",
     "Offre complémentaire",
     "Les bases sont posées. Pour aller plus loin — stratégie avancée, systèmes de monétisation et automatisation profonde.",
     ["Stratégie IA avancée pour entrepreneurs","Systèmes de monétisation automatisés","Délégation profonde à l'IA","Méthodes de scaling sans dépendre de votre temps","Accès immédiat — format numérique"],
     "230 €", "accès unique"),
    ("biz",
     "Bienvenue dans<br>Business OS IA",
     '<p>Vos accès arrivent. Vous avez fait le choix de construire quelque chose de <em>solide</em>.<br>Une dernière étape est possible — la plus complète.</p>',
     "kemora-os-ia",
     "L'écosystème complet",
     "Offre signature",
     "Business OS IA est puissant. Kemora OS IA est l'intégralité de la méthode — pour une activité entièrement orchestrée par l'IA.",
     ["L'ensemble des formations et systèmes Kemora","Le protocole d'orchestration IA complète","Les méthodes exclusives de scaling","Un accompagnement à vie sur les mises à jour","Accès immédiat — format numérique"],
     "347 €", "accès unique"),
    ("kemora",
     "Bienvenue dans<br>Kemora OS IA",
     '<p>Vous avez accès à l\'<em>écosystème complet</em>.<br>C\'est le point de départ d\'une activité orchestrée par l\'intelligence artificielle — entièrement, selon votre vision.</p>',
     None, None, None, None, None, None, None),
]

MERCI_DATA_OTHER = {
    "en": [
        ("cadre",
         "Welcome to<br>Le Cadre Mental",
         "<p>Your access is on its way. You've made the first decision — <em>the most decisive one</em>.<br>What follows begins here.</p>",
         "execution",
         "Take the next step",
         "Complementary offer",
         "You've laid the foundations. Now build the systems that will turn your vision into concrete reality.",
         ["7 high-velocity execution systems","Project start protocol in under 24h","Friction-free prioritisation method","Operational thinking templates","Immediate access — digital format"],
         "37 €", "one-time access"),
        ("exec",
         "Welcome to<br>L'Exécution",
         "<p>Your access is being sent. You took action — that <em>is</em> execution.<br>The next step: structure your business with AI.</p>",
         "core-os-ia",
         "Structure your business with AI",
         "Complementary offer",
         "You know how to get moving. Now automate that movement — with the right systems.",
         ["The 5 pillars of an automated business","Essential AI tools, explained step by step","A 7-day operational action plan","Ready-to-use templates","Immediate access — digital format"],
         "97 €", "one-time access"),
        ("core",
         "Welcome to<br>CORE OS IA",
         "<p>Your access is being prepared. You just made a <em>structuring decision</em> for your business.<br>The next step: go further.</p>",
         "business-os-ia",
         "Level up",
         "Complementary offer",
         "The foundations are in place. To go further — advanced strategy, monetisation systems and deep automation.",
         ["Advanced AI strategy for entrepreneurs","Automated monetisation systems","Deep delegation to AI","Scaling methods without depending on your time","Immediate access — digital format"],
         "230 €", "one-time access"),
        ("biz",
         "Welcome to<br>Business OS IA",
         "<p>Your access is arriving. You chose to build something <em>solid</em>.<br>One last step is possible — the most complete one.</p>",
         "kemora-os-ia",
         "The complete ecosystem",
         "Signature offer",
         "Business OS IA is powerful. Kemora OS IA is the complete method — for a business entirely orchestrated by AI.",
         ["All Kemora training and systems","The complete AI orchestration protocol","Exclusive scaling methods","Lifetime access to updates","Immediate access — digital format"],
         "347 €", "one-time access"),
        ("kemora",
         "Welcome to<br>Kemora OS IA",
         "<p>You have access to the <em>complete ecosystem</em>.<br>This is the starting point of a business entirely orchestrated by artificial intelligence — according to your vision.</p>",
         None, None, None, None, None, None, None),
    ],
    "es": [
        ("cadre",
         "Bienvenido a<br>Le Cadre Mental",
         "<p>Su acceso está en camino. Ha tomado la primera decisión — <em>la más determinante</em>.<br>Lo que sigue comienza aquí.</p>",
         "execution",
         "Pase al siguiente paso",
         "Oferta complementaria",
         "Ha puesto los cimientos. Ahora construya los sistemas que convertirán su visión en realidad concreta.",
         ["7 sistemas de ejecución de alta velocidad","Protocolo de inicio de proyecto en menos de 24h","Método de priorización sin fricción","Plantillas de reflexión operacional","Acceso inmediato — formato digital"],
         "37 €", "acceso único"),
        ("exec",
         "Bienvenido a<br>L'Exécution",
         "<p>Su acceso está siendo enviado. Pasó a la acción — <em>eso es</em> la ejecución.<br>El siguiente paso: estructure su actividad con IA.</p>",
         "core-os-ia",
         "Estructure su actividad con IA",
         "Oferta complementaria",
         "Sabe cómo ponerse en movimiento. Ahora automatice ese movimiento — con los sistemas correctos.",
         ["Los 5 pilares de un negocio automatizado","Herramientas IA esenciales, explicadas paso a paso","Un plan de acción operacional de 7 días","Plantillas listas para usar","Acceso inmediato — formato digital"],
         "97 €", "acceso único"),
        ("core",
         "Bienvenido a<br>CORE OS IA",
         "<p>Sus accesos están en preparación. Acaba de tomar una decisión <em>estructurante</em> para su actividad.<br>El siguiente paso: ir más lejos.</p>",
         "business-os-ia",
         "Pase al siguiente nivel",
         "Oferta complementaria",
         "Las bases están puestas. Para ir más lejos — estrategia avanzada, sistemas de monetización y automatización profunda.",
         ["Estrategia IA avanzada para emprendedores","Sistemas de monetización automatizados","Delegación profunda a la IA","Métodos de scaling sin depender de su tiempo","Acceso inmediato — formato digital"],
         "230 €", "acceso único"),
        ("biz",
         "Bienvenido a<br>Business OS IA",
         "<p>Sus accesos llegan. Eligió construir algo <em>sólido</em>.<br>Un último paso es posible — el más completo.</p>",
         "kemora-os-ia",
         "El ecosistema completo",
         "Oferta firma",
         "Business OS IA es poderoso. Kemora OS IA es la totalidad del método — para un negocio completamente orquestado por IA.",
         ["El conjunto de formaciones y sistemas Kemora","El protocolo de orquestación IA completa","Los métodos exclusivos de scaling","Acceso de por vida a las actualizaciones","Acceso inmediato — formato digital"],
         "347 €", "acceso único"),
        ("kemora",
         "Bienvenido a<br>Kemora OS IA",
         "<p>Tiene acceso al <em>ecosistema completo</em>.<br>Este es el punto de partida de un negocio enteramente orquestado por inteligencia artificial — según su visión.</p>",
         None, None, None, None, None, None, None),
    ],
    "de": [
        ("cadre",
         "Willkommen bei<br>Le Cadre Mental",
         "<p>Ihr Zugang ist unterwegs. Sie haben die erste Entscheidung getroffen — <em>die entscheidendste</em>.<br>Was folgt, beginnt hier.</p>",
         "execution",
         "Nächsten Schritt machen",
         "Ergänzendes Angebot",
         "Sie haben das Fundament gelegt. Jetzt bauen Sie die Systeme, die Ihre Vision in konkrete Realität verwandeln.",
         ["7 Hochgeschwindigkeits-Ausführungssysteme","Projektstart-Protokoll in unter 24h","Reibungsfreie Priorisierungsmethode","Operative Denktemplates","Sofortiger Zugang — digitales Format"],
         "37 €", "Einmalzugang"),
        ("exec",
         "Willkommen bei<br>L'Exécution",
         "<p>Ihr Zugang wird gesendet. Sie haben gehandelt — das <em>ist</em> Ausführung.<br>Der nächste Schritt: Ihr Unternehmen mit KI strukturieren.</p>",
         "core-os-ia",
         "Strukturieren Sie Ihr Unternehmen mit KI",
         "Ergänzendes Angebot",
         "Sie wissen, wie Sie in Bewegung kommen. Jetzt automatisieren Sie diese Bewegung — mit den richtigen Systemen.",
         ["Die 5 Säulen eines automatisierten Unternehmens","Wesentliche KI-Tools, Schritt für Schritt erklärt","Ein 7-Tage-Operationsaktionsplan","Gebrauchsfertige Templates","Sofortiger Zugang — digitales Format"],
         "97 €", "Einmalzugang"),
        ("core",
         "Willkommen bei<br>CORE OS IA",
         "<p>Ihr Zugang wird vorbereitet. Sie haben gerade eine <em>strukturierende Entscheidung</em> für Ihr Unternehmen getroffen.<br>Der nächste Schritt: Weiter gehen.</p>",
         "business-os-ia",
         "Nächstes Level erreichen",
         "Ergänzendes Angebot",
         "Das Fundament ist gelegt. Um weiter zu gehen — fortgeschrittene Strategie, Monetarisierungssysteme und tiefgreifende Automatisierung.",
         ["Fortgeschrittene KI-Strategie für Unternehmer","Automatisierte Monetarisierungssysteme","Tiefe Delegation an KI","Skalierungsmethoden ohne Zeitabhängigkeit","Sofortiger Zugang — digitales Format"],
         "230 €", "Einmalzugang"),
        ("biz",
         "Willkommen bei<br>Business OS IA",
         "<p>Ihr Zugang kommt. Sie haben sich entschieden, etwas <em>Solides</em> aufzubauen.<br>Ein letzter Schritt ist möglich — der vollständigste.</p>",
         "kemora-os-ia",
         "Das vollständige Ökosystem",
         "Signatur-Angebot",
         "Business OS IA ist leistungsstark. Kemora OS IA ist die vollständige Methode — für ein vollständig von KI orchestriertes Unternehmen.",
         ["Alle Kemora-Schulungen und -Systeme","Das vollständige KI-Orchestrierungsprotokoll","Exklusive Skalierungsmethoden","Lebenslanger Zugang zu Updates","Sofortiger Zugang — digitales Format"],
         "347 €", "Einmalzugang"),
        ("kemora",
         "Willkommen bei<br>Kemora OS IA",
         "<p>Sie haben Zugang zum <em>vollständigen Ökosystem</em>.<br>Dies ist der Ausgangspunkt eines vollständig von künstlicher Intelligenz orchestrierten Unternehmens — gemäß Ihrer Vision.</p>",
         None, None, None, None, None, None, None),
    ],
    "pt": [
        ("cadre",
         "Bem-vindo ao<br>Le Cadre Mental",
         "<p>O seu acesso está a caminho. Tomou a primeira decisão — <em>a mais determinante</em>.<br>O que se segue começa aqui.</p>",
         "execution",
         "Avance para o próximo passo",
         "Oferta complementar",
         "Estabeleceu as fundações. Agora construa os sistemas que vão transformar a sua visão em realidade concreta.",
         ["7 sistemas de execução de alta velocidade","Protocolo de início de projeto em menos de 24h","Método de priorização sem fricção","Templates de reflexão operacional","Acesso imediato — formato digital"],
         "37 €", "acesso único"),
        ("exec",
         "Bem-vindo ao<br>L'Exécution",
         "<p>O seu acesso está a ser enviado. Passou à ação — <em>isso é</em> a execução.<br>O próximo passo: estruture a sua atividade com IA.</p>",
         "core-os-ia",
         "Estruture a sua atividade com IA",
         "Oferta complementar",
         "Sabe como se pôr em movimento. Agora automatize esse movimento — com os sistemas certos.",
         ["Os 5 pilares de um negócio automatizado","Ferramentas IA essenciais, explicadas passo a passo","Um plano de ação operacional de 7 dias","Templates prontos a usar","Acesso imediato — formato digital"],
         "97 €", "acesso único"),
        ("core",
         "Bem-vindo ao<br>CORE OS IA",
         "<p>Os seus acessos estão em preparação. Acabou de tomar uma decisão <em>estruturante</em> para a sua atividade.<br>O próximo passo: ir mais longe.</p>",
         "business-os-ia",
         "Avance para o nível seguinte",
         "Oferta complementar",
         "As bases estão estabelecidas. Para ir mais longe — estratégia avançada, sistemas de monetização e automatização aprofundada.",
         ["Estratégia IA avançada para empreendedores","Sistemas de monetização automatizados","Delegação profunda à IA","Métodos de scaling sem depender do seu tempo","Acesso imediato — formato digital"],
         "230 €", "acesso único"),
        ("biz",
         "Bem-vindo ao<br>Business OS IA",
         "<p>Os seus acessos estão a chegar. Escolheu construir algo <em>sólido</em>.<br>Um último passo é possível — o mais completo.</p>",
         "kemora-os-ia",
         "O ecossistema completo",
         "Oferta assinatura",
         "O Business OS IA é poderoso. O Kemora OS IA é a totalidade do método — para uma atividade inteiramente orquestrada pela IA.",
         ["O conjunto de formações e sistemas Kemora","O protocolo de orquestração IA completa","Os métodos exclusivos de scaling","Acesso vitalício às atualizações","Acesso imediato — formato digital"],
         "347 €", "acesso único"),
        ("kemora",
         "Bem-vindo ao<br>Kemora OS IA",
         "<p>Tem acesso ao <em>ecossistema completo</em>.<br>Este é o ponto de partida de uma atividade inteiramente orquestrada pela inteligência artificial — segundo a sua visão.</p>",
         None, None, None, None, None, None, None),
    ],
    "it": [
        ("cadre",
         "Benvenuto in<br>Le Cadre Mental",
         "<p>Il Suo accesso è in arrivo. Ha preso la prima decisione — <em>la più determinante</em>.<br>Ciò che segue inizia qui.</p>",
         "execution",
         "Passi al passo successivo",
         "Offerta complementare",
         "Ha posto le fondamenta. Ora costruisca i sistemi che trasformeranno la Sua visione in realtà concreta.",
         ["7 sistemi di esecuzione ad alta velocità","Protocollo di avvio progetto in meno di 24h","Metodo di prioritizzazione senza attrito","Template di riflessione operativa","Accesso immediato — formato digitale"],
         "37 €", "accesso unico"),
        ("exec",
         "Benvenuto in<br>L'Exécution",
         "<p>Il Suo accesso è in fase di invio. Ha agito — <em>è proprio questo</em> l'esecuzione.<br>Il passo successivo: strutturare la Sua attività con l'IA.</p>",
         "core-os-ia",
         "Strutturi la Sua attività con l'IA",
         "Offerta complementare",
         "Sa come mettersi in moto. Ora automatizzi quel movimento — con i sistemi giusti.",
         ["I 5 pilastri di un'attività automatizzata","Strumenti IA essenziali, spiegati passo dopo passo","Un piano d'azione operativo di 7 giorni","Template pronti all'uso","Accesso immediato — formato digitale"],
         "97 €", "accesso unico"),
        ("core",
         "Benvenuto in<br>CORE OS IA",
         "<p>I Suoi accessi sono in preparazione. Ha appena preso una decisione <em>strutturante</em> per la Sua attività.<br>Il passo successivo: andare oltre.</p>",
         "business-os-ia",
         "Passi al livello superiore",
         "Offerta complementare",
         "Le fondamenta sono poste. Per andare oltre — strategia avanzata, sistemi di monetizzazione e automatizzazione approfondita.",
         ["Strategia IA avanzata per imprenditori","Sistemi di monetizzazione automatizzati","Delega approfondita all'IA","Metodi di scaling senza dipendere dal Suo tempo","Accesso immediato — formato digitale"],
         "230 €", "accesso unico"),
        ("biz",
         "Benvenuto in<br>Business OS IA",
         "<p>I Suoi accessi stanno arrivando. Ha scelto di costruire qualcosa di <em>solido</em>.<br>Un ultimo passo è possibile — il più completo.</p>",
         "kemora-os-ia",
         "L'ecosistema completo",
         "Offerta firma",
         "Business OS IA è potente. Kemora OS IA è la totalità del metodo — per un'attività interamente orchestrata dall'IA.",
         ["L'insieme delle formazioni e sistemi Kemora","Il protocollo di orchestrazione IA completa","I metodi esclusivi di scaling","Accesso a vita agli aggiornamenti","Accesso immediato — formato digitale"],
         "347 €", "accesso unico"),
        ("kemora",
         "Benvenuto in<br>Kemora OS IA",
         "<p>Ha accesso all'<em>ecosistema completo</em>.<br>Questo è il punto di partenza di un'attività interamente orchestrata dall'intelligenza artificiale — secondo la Sua visione.</p>",
         None, None, None, None, None, None, None),
    ],
}

# Write FR merci
print("Writing FR merci pages...")
for data in MERCI_DATA_FR:
    html, slug = merci_page("fr", *data)
    write(f"fr/{slug}", html)

# Write merci pages for other langs
for lang, data_list in MERCI_DATA_OTHER.items():
    print(f"Writing {lang.upper()} merci pages...")
    for data in data_list:
        html, slug = merci_page(lang, *data)
        write(f"{lang}/{slug}", html)

# Write legal + privacy pages all langs
print("Writing legal/privacy pages...")
for lang in ["fr","en","es","de","pt","it"]:
    html, slug = legal_page(lang)
    write(f"{lang}/{slug}", html)
    html, slug = privacy_page(lang)
    write(f"{lang}/{slug}", html)

print("Done.")

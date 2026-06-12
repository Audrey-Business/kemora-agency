#!/usr/bin/env python3
"""Full site generator for Kemora Agency."""

import os, re

SITE_URL = "https://kemora-agency.com"

STRIPE = {
    "cadre-mental":   "https://buy.stripe.com/bJe14p84heDCepVbFUcMM00",
    "execution":      "https://buy.stripe.com/dRmbJ3doBfHGepV11gcMM01",
    "core-os-ia":     "https://buy.stripe.com/8x2dRb84hfHG3LhdO2cMM02",
    "business-os-ia": "https://buy.stripe.com/5kQfZj0BP0MMgy3h0ecMM03",
    "kemora-os-ia":   "https://buy.stripe.com/28EdRb1FT0MM4Pl4dscMM04",
}
SYSTEME_CONTACT = "https://go.kemora-agency.com/f6f64125"
SYSTEME_BOOKING = "https://go.kemora-agency.com/4c191075"

HREFLANG = {
    "index":      {"fr":"fr/index.html","en":"en/index.html","es":"es/index.html","de":"de/index.html","pt":"pt/index.html","it":"it/index.html"},
    "fondations": {"fr":"fr/fondations.html","en":"en/foundations.html","es":"es/fundaciones.html","de":"de/grundlagen.html","pt":"pt/fundacoes.html","it":"it/fondamenta.html"},
    "about":      {"fr":"fr/a-propos.html","en":"en/about.html","es":"es/sobre-nosotros.html","de":"de/ueber-uns.html","pt":"pt/sobre-nos.html","it":"it/chi-siamo.html"},
    "faq":        {"fr":"fr/faq.html","en":"en/faq.html","es":"es/preguntas-frecuentes.html","de":"de/haeufige-fragen.html","pt":"pt/perguntas-frequentes.html","it":"it/domande-frequenti.html"},
    "contact":    {"fr":"fr/contact.html","en":"en/contact.html","es":"es/contacto.html","de":"de/kontakt.html","pt":"pt/contato.html","it":"it/contatto.html"},
    "booking":    {"fr":"fr/reserver-appel.html","en":"en/book-a-call.html","es":"es/reservar-llamada.html","de":"de/anruf-buchen.html","pt":"pt/reservar-chamada.html","it":"it/prenota-chiamata.html"},
    "prod_cadre": {"fr":"fr/produits/le-cadre-mental.html","en":"en/products/the-mental-framework.html","es":"es/productos/el-marco-mental.html","de":"de/produkte/der-mentale-rahmen.html","pt":"pt/produtos/o-quadro-mental.html","it":"it/prodotti/il-quadro-mentale.html"},
    "prod_exec":  {"fr":"fr/produits/lexecution.html","en":"en/products/execution.html","es":"es/productos/la-ejecucion.html","de":"de/produkte/die-ausfuehrung.html","pt":"pt/produtos/a-execucao.html","it":"it/prodotti/lesecuzione.html"},
    "prod_core":  {"fr":"fr/produits/core-os-ia.html","en":"en/products/core-os-ai.html","es":"es/productos/core-os-ia.html","de":"de/produkte/core-os-ki.html","pt":"pt/produtos/core-os-ia.html","it":"it/prodotti/core-os-ia.html"},
    "prod_biz":   {"fr":"fr/produits/business-os-ia.html","en":"en/products/business-os-ai.html","es":"es/productos/business-os-ia.html","de":"de/produkte/business-os-ki.html","pt":"pt/produtos/business-os-ia.html","it":"it/prodotti/business-os-ia.html"},
    "prod_kemora":{"fr":"fr/produits/kemora-os-ia.html","en":"en/products/kemora-os-ai.html","es":"es/productos/kemora-os-ia.html","de":"de/produkte/kemora-os-ki.html","pt":"pt/produtos/kemora-os-ia.html","it":"it/prodotti/kemora-os-ia.html"},
}

LANGS_META = {
    "fr":{"locale":"fr_FR","flag":"🇫🇷","label":"FR"},
    "en":{"locale":"en_GB","flag":"🇬🇧","label":"EN"},
    "es":{"locale":"es_ES","flag":"🇪🇸","label":"ES"},
    "de":{"locale":"de_DE","flag":"🇩🇪","label":"DE"},
    "pt":{"locale":"pt_PT","flag":"🇵🇹","label":"PT"},
    "it":{"locale":"it_IT","flag":"🇮🇹","label":"IT"},
}

COOKIE = {
    "fr":{"text":"Nous utilisons des outils d'analyse respectueux de votre vie privée pour améliorer votre expérience.","accept":"Accepter","decline":"Refuser"},
    "en":{"text":"We use privacy-respecting analytics tools to improve your experience.","accept":"Accept","decline":"Decline"},
    "es":{"text":"Utilizamos herramientas de análisis respetuosas con su privacidad para mejorar su experiencia.","accept":"Aceptar","decline":"Rechazar"},
    "de":{"text":"Wir verwenden datenschutzkonforme Analysetools, um Ihre Erfahrung zu verbessern.","accept":"Akzeptieren","decline":"Ablehnen"},
    "pt":{"text":"Utilizamos ferramentas de análise que respeitam a sua privacidade para melhorar a sua experiência.","accept":"Aceitar","decline":"Recusar"},
    "it":{"text":"Utilizziamo strumenti di analisi rispettosi della Sua privacy per migliorare la Sua esperienza.","accept":"Accettare","decline":"Rifiutare"},
}

SKIP_LINK = {
    "fr":"Aller au contenu principal","en":"Skip to main content","es":"Ir al contenido principal",
    "de":"Zum Hauptinhalt springen","pt":"Ir para o conteúdo principal","it":"Vai al contenuto principale",
}

BACK_HOME = {
    "fr":"Retour à l'accueil","en":"Back to home","es":"Volver al inicio",
    "de":"Zurück zur Startseite","pt":"Voltar ao início","it":"Torna alla home",
}

# ─── COMMON HTML SNIPPETS ─────────────────────────────────────────────────────

LANG_SWITCHER_CSS = """
  /* LANGUAGE SWITCHER */
  .lang-switcher{position:relative;margin-left:1rem;}
  .lang-btn{display:flex;align-items:center;gap:0.4rem;font-family:var(--sans);font-size:0.68rem;font-weight:500;letter-spacing:0.14em;text-transform:uppercase;color:var(--gold);background:transparent;border:1px solid var(--border);padding:0.35rem 0.75rem;cursor:pointer;transition:all 0.3s;white-space:nowrap;}
  .lang-btn:hover{border-color:var(--gold);}
  .lang-btn svg{width:10px;height:10px;transition:transform 0.3s;}
  .lang-switcher.open .lang-btn svg{transform:rotate(180deg);}
  .lang-menu{position:absolute;top:calc(100% + 0.6rem);right:0;background:var(--black2);border:1px solid var(--border);min-width:160px;padding:0.4rem 0;opacity:0;pointer-events:none;transform:translateY(-6px);transition:opacity 0.25s,transform 0.25s;z-index:300;box-shadow:0 20px 50px rgba(0,0,0,0.7);}
  .lang-switcher.open .lang-menu{opacity:1;pointer-events:all;transform:translateY(0);}
  .lang-menu a{display:flex;align-items:center;gap:0.6rem;padding:0.6rem 1rem;font-family:var(--sans);font-size:0.68rem;letter-spacing:0.12em;text-transform:uppercase;color:var(--muted);text-decoration:none;transition:color 0.2s,background 0.2s;}
  .lang-menu a:hover,.lang-menu a.active{color:var(--gold);background:rgba(198,161,110,0.04);}
  .lang-mobile-wrap{margin-top:1.2rem;padding-top:1.2rem;border-top:1px solid var(--border2);display:flex;flex-wrap:wrap;gap:0.6rem;}
  .lang-mobile-wrap a{font-family:var(--sans);font-size:0.68rem;letter-spacing:0.14em;text-transform:uppercase;color:var(--muted);text-decoration:none;border:1px solid var(--border2);padding:0.4rem 0.8rem;transition:color 0.3s,border-color 0.3s;}
  .lang-mobile-wrap a:hover,.lang-mobile-wrap a.active{color:var(--gold);border-color:var(--gold);}"""

def hreflang_tags(key):
    links = HREFLANG.get(key, {})
    tags = [f'<link rel="alternate" hreflang="{l}" href="{SITE_URL}/{p}">' for l,p in links.items()]
    tags.append(f'<link rel="alternate" hreflang="x-default" href="{SITE_URL}/fr/index.html">')
    return "\n".join(tags)

def seo_meta(lang, title, desc, slug, hreflang_key, image="/assets/images/Accueil.webp"):
    locale = LANGS_META[lang]["locale"]
    canonical = f"{SITE_URL}/{lang}/{slug}"
    og_img = f"{SITE_URL}{image}"
    preload = f'<link rel="preload" as="image" href="{image}">'
    return f"""<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Kemora Agency</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title} — Kemora Agency">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:type" content="website">
<meta property="og:locale" content="{locale}">
<meta property="og:site_name" content="Kemora Agency">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title} — Kemora Agency">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{og_img}">
{hreflang_tags(hreflang_key)}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{preload}
<link rel="icon" href="/assets/favicon/favicon.ico">
<link rel="apple-touch-icon" href="/assets/favicon/apple-touch-icon.png">
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#C6A16E">"""

def lang_switcher_widget(lang, hreflang_key):
    m = LANGS_META[lang]
    links = HREFLANG.get(hreflang_key, {})
    items = []
    mob_items = []
    for l in ["fr","en","es","de","pt","it"]:
        lm = LANGS_META[l]
        path = links.get(l, f"{l}/index.html")
        ac = ' class="active"' if l==lang else ''
        items.append(f'<a href="/{path}" data-lang="{l}"{ac}>{lm["flag"]} {lm["label"]}</a>')
        mob_items.append(f'<a href="/{path}" data-lang="{l}"{ac}>{lm["flag"]} {lm["label"]}</a>')
    widget = f'''<div class="lang-switcher" id="langSwitcher">
    <button class="lang-btn" onclick="toggleLang(event)" aria-label="Language" aria-haspopup="true" aria-expanded="false">
      {m["flag"]} {m["label"]} <svg viewBox="0 0 10 6" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M1 1l4 4 4-4"/></svg>
    </button>
    <div class="lang-menu">{"".join(items)}</div>
  </div>'''
    mob_widget = f'<div class="lang-mobile-wrap">{"".join(mob_items)}</div>'
    return widget, mob_widget

def cookie_banner(lang):
    c = COOKIE[lang]
    return f'''<div id="cookieBanner" style="display:none;position:fixed;bottom:0;left:0;right:0;z-index:10000;background:var(--black2);border-top:1px solid var(--border);padding:1.2rem clamp(1.5rem,5vw,4rem);display:flex;align-items:center;justify-content:space-between;gap:1.5rem;flex-wrap:wrap;">
  <p style="font-size:0.78rem;color:var(--muted);line-height:1.6;max-width:600px;">{c["text"]}</p>
  <div style="display:flex;gap:0.8rem;flex-shrink:0;">
    <button onclick="acceptCookies()" style="background:var(--gold);color:var(--black);border:none;padding:0.6rem 1.4rem;font-family:var(--sans);font-size:0.72rem;font-weight:500;letter-spacing:0.12em;text-transform:uppercase;cursor:pointer;">{c["accept"]}</button>
    <button onclick="declineCookies()" style="background:transparent;color:var(--muted);border:1px solid var(--border);padding:0.6rem 1.4rem;font-family:var(--sans);font-size:0.72rem;letter-spacing:0.12em;text-transform:uppercase;cursor:pointer;">{c["decline"]}</button>
  </div>
</div>'''

COMMON_SCRIPT = """<script>
(function(){var c=localStorage.getItem('kemora-cookies');if(!c){var b=document.getElementById('cookieBanner');if(b){b.style.display='flex';}}else if(c==='accepted'){loadAnalytics();}})();
function acceptCookies(){localStorage.setItem('kemora-cookies','accepted');var b=document.getElementById('cookieBanner');if(b)b.style.display='none';loadAnalytics();}
function declineCookies(){localStorage.setItem('kemora-cookies','declined');var b=document.getElementById('cookieBanner');if(b)b.style.display='none';}
function loadAnalytics(){if(window._al)return;window._al=true;var s=document.createElement('script');s.defer=true;s.setAttribute('data-domain','kemora-agency.com');s.src='https://plausible.io/js/script.js';document.head.appendChild(s);}
function toggleLang(e){e.stopPropagation();var s=document.getElementById('langSwitcher');if(s){s.classList.toggle('open');var b=s.querySelector('.lang-btn');if(b)b.setAttribute('aria-expanded',s.classList.contains('open'));}}
document.addEventListener('click',function(e){var s=document.getElementById('langSwitcher');if(s&&!s.contains(e.target))s.classList.remove('open');});
document.querySelectorAll('[data-lang]').forEach(function(a){a.addEventListener('click',function(){localStorage.setItem('kemora-lang',this.getAttribute('data-lang'));});});
if('serviceWorker' in navigator){navigator.serviceWorker.register('/sw.js');}
</script>"""

ORG_SCHEMA = '{"@context":"https://schema.org","@type":"Organization","name":"Kemora Agency","url":"https://kemora-agency.com","description":"Écosystème digital premium dédié à l\'IA, l\'automatisation et les systèmes de croissance intelligents.","logo":"https://kemora-agency.com/assets/favicon/apple-touch-icon.png","sameAs":[]}'

def product_schema(name, desc, price, url):
    return f'{{"@context":"https://schema.org","@type":"Product","name":"{name}","description":"{desc}","offers":{{"@type":"Offer","price":"{price}","priceCurrency":"EUR","availability":"https://schema.org/InStock","url":"{url}"}}}}'

def breadcrumb_schema(lang, prod_name, prod_url):
    our_offer = {"fr":"Notre offre","en":"Our Offer","es":"Nuestra Oferta","de":"Unser Angebot","pt":"Nossa Oferta","it":"La Nostra Offerta"}
    return f'{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Kemora Agency","item":"{SITE_URL}"}},{{"@type":"ListItem","position":2,"name":"{our_offer.get(lang,"Notre offre")}","item":"{SITE_URL}/{lang}/index.html#offre"}},{{"@type":"ListItem","position":3,"name":"{prod_name}","item":"{SITE_URL}/{prod_url}"}}]}}'

def breadcrumb_html(lang, prod_name):
    sep = '<span style="color:var(--gold-dim);margin:0 0.5rem;">›</span>'
    our_offer_label = {"fr":"Notre offre","en":"Our Offer","es":"Nuestra Oferta","de":"Unser Angebot","pt":"Nossa Oferta","it":"La Nostra Offerta"}
    index_files = {"fr":"index.html","en":"index.html","es":"index.html","de":"index.html","pt":"index.html","it":"index.html"}
    return f'<nav aria-label="breadcrumb" style="padding:0.8rem 0;margin-bottom:1.5rem;"><span style="font-family:var(--sans);font-size:0.7rem;letter-spacing:0.1em;color:var(--muted);"><a href="/'+lang+'/'+index_files[lang]+'" style="color:var(--muted);text-decoration:none;transition:color 0.3s;" onmouseover="this.style.color=\'var(--gold)\'" onmouseout="this.style.color=\'var(--muted)\'">Kemora Agency</a>'+sep+'<a href="/'+lang+'/'+index_files[lang]+'#offre" style="color:var(--muted);text-decoration:none;transition:color 0.3s;" onmouseover="this.style.color=\'var(--gold)\'" onmouseout="this.style.color=\'var(--muted)\'">'+our_offer_label.get(lang,"Notre offre")+'</a>'+sep+'<span style="color:var(--gold);">'+prod_name+'</span></span></nav>'

# ─── PROCESS FR FILES ─────────────────────────────────────────────────────────

FR_FILE_META = {
    "fr/index.html": {
        "title":"Kemora Agency — Maîtrisez l'IA. Automatisez. Libérez votre potentiel.",
        "desc":"Écosystème digital premium dédié à l'IA, l'automatisation et les systèmes de croissance intelligents. Cinq ressources pour transformer votre activité.",
        "slug":"index.html","hreflang_key":"index","image":"/assets/images/Accueil.webp",
        "schema": f'<script type="application/ld+json">{ORG_SCHEMA}</script>',
    },
    "fr/fondations.html": {
        "title":"Fondations — Les principes de Kemora Agency",
        "desc":"Découvrez les fondations intellectuelles et stratégiques qui sous-tendent l'approche Kemora Agency. IA, automatisation, systèmes de croissance.",
        "slug":"fondations.html","hreflang_key":"fondations","image":"/assets/images/fondations.webp","schema":"",
    },
    "fr/a-propos.html": {
        "title":"À propos — La mission de Kemora Agency",
        "desc":"Kemora Agency : un écosystème digital conçu pour aider les entrepreneurs à exploiter pleinement le potentiel de l'intelligence artificielle.",
        "slug":"a-propos.html","hreflang_key":"about","image":"/assets/images/apropos.webp",
        "schema": f'<script type="application/ld+json">{ORG_SCHEMA}</script>',
    },
    "fr/faq.html": {
        "title":"Questions fréquentes — Kemora Agency",
        "desc":"Toutes les réponses aux questions les plus fréquentes sur Kemora Agency, ses ressources, l'IA et l'automatisation.",
        "slug":"faq.html","hreflang_key":"faq","image":"/assets/images/faq.webp",
        "schema":'<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"À qui s\'adresse Kemora Agency ?","acceptedAnswer":{"@type":"Answer","text":"Kemora Agency s\'adresse aux entrepreneurs, créateurs et freelances qui souhaitent utiliser l\'IA pour structurer et automatiser leur activité."}},{"@type":"Question","name":"Faut-il avoir des connaissances en IA ?","acceptedAnswer":{"@type":"Answer","text":"Non. Les ressources sont accessibles même aux débutants. L\'objectif est d\'utiliser l\'IA comme levier, pas de devenir expert technique."}},{"@type":"Question","name":"Que se passe-t-il après l\'achat ?","acceptedAnswer":{"@type":"Answer","text":"Vous recevez toutes les informations pour accéder à votre contenu et pouvez avancer à votre propre rythme."}}]}</script>',
    },
    "fr/contact.html": {
        "title":"Contact — Échangeons sur votre projet",
        "desc":"Prenez contact avec Kemora Agency pour toute question sur nos ressources, notre accompagnement ou votre projet digital et IA.",
        "slug":"contact.html","hreflang_key":"contact","image":"/assets/images/contact.webp","schema":"",
    },
    "fr/reserver-appel.html": {
        "title":"Réserver un appel — Kemora Agency",
        "desc":"Réservez un appel stratégique avec Kemora Agency. Échangeons sur votre situation, vos objectifs et la ressource qui vous correspond.",
        "slug":"reserver-appel.html","hreflang_key":"booking","image":"/assets/images/contact.webp","schema":"",
    },
    "fr/produits/le-cadre-mental.html": {
        "title":"Le Cadre Mental — Kemora Agency",
        "desc":"Adoptez la posture et l'architecture de pensée qui précèdent toute transformation durable. Le Cadre Mental — 37 €.",
        "slug":"produits/le-cadre-mental.html","hreflang_key":"prod_cadre","image":"/assets/images/le_cadremental.webp",
        "schema": (
            '<script type="application/ld+json">' +
            product_schema("Le Cadre Mental","Posture et architecture de pensee pour toute transformation durable.","37",SITE_URL+"/fr/produits/le-cadre-mental.html") +
            '</script>\n<script type="application/ld+json">' +
            breadcrumb_schema("fr","Le Cadre Mental","fr/produits/le-cadre-mental.html") +
            '</script>'
        ),
        "stripe": STRIPE["cadre-mental"],
    },
    "fr/produits/lexecution.html": {
        "title":"L'Execution — Kemora Agency",
        "desc":"Les systemes pour passer de l'intention a l'action de facon structuree, repetable et efficace. 37 €.",
        "slug":"produits/lexecution.html","hreflang_key":"prod_exec","image":"/assets/images/lexecution.webp",
        "schema": (
            '<script type="application/ld+json">' +
            product_schema("L'Execution","Les systemes pour passer de l'intention a l'action de facon structuree.","37",SITE_URL+"/fr/produits/lexecution.html") +
            '</script>\n<script type="application/ld+json">' +
            breadcrumb_schema("fr","L'Execution","fr/produits/lexecution.html") +
            '</script>'
        ),
        "stripe": STRIPE["execution"],
    },
    "fr/produits/core-os-ia.html": {
        "title":"CORE OS IA — Kemora Agency",
        "desc":"Les fondations d'un business automatise : outils IA essentiels, 5 piliers et plan d'action sur 7 jours. CORE OS IA — 97 €.",
        "slug":"produits/core-os-ia.html","hreflang_key":"prod_core","image":"/assets/images/coreosia.webp",
        "schema": (
            '<script type="application/ld+json">' +
            product_schema("CORE OS IA","Les fondations d'un business automatise : outils IA essentiels, 5 piliers et plan d'action sur 7 jours.","97",SITE_URL+"/fr/produits/core-os-ia.html") +
            '</script>\n<script type="application/ld+json">' +
            breadcrumb_schema("fr","CORE OS IA","fr/produits/core-os-ia.html") +
            '</script>'
        ),
        "stripe": STRIPE["core-os-ia"],
    },
    "fr/produits/business-os-ia.html": {
        "title":"Business OS IA — Kemora Agency",
        "desc":"Strategie avancee, monetisation et automatisation pour un business solide et scalable. Business OS IA — 230 €.",
        "slug":"produits/business-os-ia.html","hreflang_key":"prod_biz","image":"/assets/images/businessosia.webp",
        "schema": (
            '<script type="application/ld+json">' +
            product_schema("Business OS IA","Strategie avancee, systemes de monetisation et automatisation approfondie.","230",SITE_URL+"/fr/produits/business-os-ia.html") +
            '</script>\n<script type="application/ld+json">' +
            breadcrumb_schema("fr","Business OS IA","fr/produits/business-os-ia.html") +
            '</script>'
        ),
        "stripe": STRIPE["business-os-ia"],
    },
    "fr/produits/kemora-os-ia.html": {
        "title":"Kemora OS IA — L'ecosysteme complet",
        "desc":"L'ecosysteme IA complet — la methode Kemora dans sa version la plus aboutie pour un business orchestre par l'IA. 347 €.",
        "slug":"produits/kemora-os-ia.html","hreflang_key":"prod_kemora","image":"/assets/images/kemoraosia.webp",
        "schema": (
            '<script type="application/ld+json">' +
            product_schema("Kemora OS IA","L'ecosysteme IA complet pour un business entierement orchestre par l'intelligence artificielle.","347",SITE_URL+"/fr/produits/kemora-os-ia.html") +
            '</script>\n<script type="application/ld+json">' +
            breadcrumb_schema("fr","Kemora OS IA","fr/produits/kemora-os-ia.html") +
            '</script>'
        ),
        "stripe": STRIPE["kemora-os-ia"],
    },
}

FR_LINK_MAP = {
    'href="index.html"':         'href="/fr/index.html"',
    "href='index.html'":         "href='/fr/index.html'",
    'href="fondations.html"':    'href="/fr/fondations.html"',
    'href="a-propos.html"':      'href="/fr/a-propos.html"',
    'href="faq.html"':           'href="/fr/faq.html"',
    'href="contact.html"':       'href="/fr/contact.html"',
    'href="reserver-appel.html"':'href="/fr/reserver-appel.html"',
    'href="produits/le-cadre-mental.html"':'href="/fr/produits/le-cadre-mental.html"',
    'href="produits/lexecution.html"':'href="/fr/produits/lexecution.html"',
    'href="produits/core-os-ia.html"':'href="/fr/produits/core-os-ia.html"',
    'href="produits/business-os-ia.html"':'href="/fr/produits/business-os-ia.html"',
    'href="produits/kemora-os-ia.html"':'href="/fr/produits/kemora-os-ia.html"',
    'href="index.html#offre"':   'href="/fr/index.html#offre"',
    'href="../index.html"':      'href="/fr/index.html"',
    'href="../contact.html"':    'href="/fr/contact.html"',
    'href="../faq.html"':        'href="/fr/faq.html"',
    'href="../reserver-appel.html"':'href="/fr/reserver-appel.html"',
    'href="#"':                  'href="/fr/mentions-legales.html"',
    'src="assets/':              'src="/assets/',
    "src='assets/":              "src='/assets/",
    'href="assets/':             'href="/assets/',
    'url("assets/':              'url("/assets/',
}

FULL_NAV_LINKS_FR = """  <ul class="nav-links">
    <li><a href="/fr/fondations.html">Fondations</a></li>
    <li><a href="/fr/a-propos.html">À propos</a></li>
    <li class="nav-dropdown">
      <a href="/fr/index.html#offre" aria-haspopup="true">
        Notre offre
        <svg viewBox="0 0 10 6" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M1 1l4 4 4-4"/></svg>
      </a>
      <div class="dropdown-menu">
        <a href="/fr/produits/le-cadre-mental.html">Le Cadre Mental</a>
        <a href="/fr/produits/lexecution.html">L'Exécution</a>
        <a href="/fr/produits/core-os-ia.html">CORE OS IA</a>
        <a href="/fr/produits/business-os-ia.html">Business OS IA</a>
        <a href="/fr/produits/kemora-os-ia.html">Kemora OS IA</a>
      </div>
    </li>
    <li><a href="/fr/faq.html">FAQ</a></li>
    <li><a href="/fr/contact.html">Contact</a></li>
    <li><a href="/fr/reserver-appel.html" class="nav-cta">Réserver un appel</a></li>
  </ul>"""

FULL_MOBILE_NAV_FR = """  <a href="/fr/fondations.html">Fondations</a>
  <a href="/fr/a-propos.html">À propos</a>
  <a href="/fr/produits/le-cadre-mental.html">Le Cadre Mental</a>
  <a href="/fr/produits/lexecution.html">L'Exécution</a>
  <a href="/fr/produits/core-os-ia.html">CORE OS IA</a>
  <a href="/fr/produits/business-os-ia.html">Business OS IA</a>
  <a href="/fr/produits/kemora-os-ia.html">Kemora OS IA</a>
  <a href="/fr/faq.html">FAQ</a>
  <a href="/fr/contact.html">Contact</a>
  <a href="/fr/reserver-appel.html" class="mobile-cta">Réserver un appel</a>"""

def process_fr_file(filepath):
    meta = FR_FILE_META.get(filepath)
    if not meta:
        print(f"  SKIP (no meta): {filepath}")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    lang = "fr"
    title = meta["title"]
    desc = meta["desc"]
    slug = meta["slug"]
    hk = meta["hreflang_key"]
    image = meta.get("image", "/assets/images/Accueil.webp")
    schema = meta.get("schema", "")
    stripe_url = meta.get("stripe", "")

    # 1. Fix path references
    for old, new in FR_LINK_MAP.items():
        html = html.replace(old, new)

    # Fix footer legal links more carefully - only href="#" that aren't already fixed
    html = re.sub(r'href="#"(?=[^>]*>Mentions légales)', 'href="/fr/mentions-legales.html"', html)
    html = re.sub(r'href="#"(?=[^>]*>Politique de confidentialité)', 'href="/fr/politique-confidentialite.html"', html)

    # 2. Fix image case issue: Accueil.webp
    html = html.replace('/assets/images/accueil.webp', '/assets/images/Accueil.webp')
    html = html.replace('src="/assets/images/accueil.webp"', 'src="/assets/images/Accueil.webp"')

    # 3. Replace <html lang="fr"> with proper opener
    html = re.sub(r'<html\s+lang="fr">', '<html lang="fr">', html)

    # 4. Replace old <head> opening / meta charset block with full SEO block
    seo_block = seo_meta(lang, title, desc, slug, hk, image)
    html = re.sub(
        r'<meta charset="UTF-8">\s*<meta name="viewport"[^>]*>\s*<title>[^<]*</title>',
        seo_block,
        html
    )

    # 5. Add schema.org after <title> closing if provided
    if schema:
        html = html.replace('</head>', schema + '\n</head>', 1)

    # 6. Add lang switcher CSS before </style>
    if 'lang-switcher' not in html:
        html = html.replace('</style>', LANG_SWITCHER_CSS + '\n</style>', 1)

    # 7. Add lang switcher widget to nav
    switcher_widget, mobile_items = lang_switcher_widget(lang, hk)
    # Find nav-links or nav-back and insert after nav CTA
    if 'nav-cta' in html and 'langSwitcher' not in html:
        # For pages with full nav (index, fondations etc)
        html = html.replace('</ul>\n  <button class="nav-toggle"',
                            '</ul>\n  ' + switcher_widget + '\n  <button class="nav-toggle"')
        # Also update mobile nav with lang switcher
        html = re.sub(r'(class="mobile-cta">[^<]*</a>\s*</div>)',
                      r'\1', html)
        # Add mobile lang switcher before closing nav-mobile div
        if 'nav-mobile' in html:
            html = re.sub(r'(class="mobile-cta"[^<]*</a>)\s*(</div>)',
                         r'\1\n  ' + mobile_items + r'\n\2', html)

    elif 'nav-back' in html and 'langSwitcher' not in html:
        # For pages with back nav (contact, booking, faq, product pages)
        html = re.sub(r'(class="nav-back"[^>]*>.*?</a>)\s*(</nav>)',
                      r'\1\n  ' + switcher_widget + r'\n\2', html, flags=re.DOTALL)

    # 8. Replace form actions for contact/booking pages
    if 'contactForm' in html or 'callForm' in html:
        if 'contactForm' in html:
            html = html.replace('action="#" method="POST" onsubmit="return handleSubmit(event)"',
                               f'action="{SYSTEME_CONTACT}" method="POST" onsubmit="return handleSubmit(event)"')
        if 'callForm' in html:
            html = html.replace('action="#" method="POST" onsubmit="return handleSubmit(event)"',
                               f'action="{SYSTEME_BOOKING}" method="POST" onsubmit="return handleSubmit(event)"')

    # 9. Connect Stripe buttons (replace href="#" or placeholder Stripe on CTA buttons)
    if stripe_url:
        # Replace payment button placeholders
        html = re.sub(r'href="https://buy\.stripe\.com/[^"]*"', f'href="{stripe_url}"', html)
        # Also fix any button that leads to checkout
        html = re.sub(r'(btn-gold[^>]*href=")#"', f'\\1{stripe_url}"', html)

    # 10. Add cookie banner before </body>
    if 'cookieBanner' not in html:
        html = html.replace('</body>', cookie_banner(lang) + '\n' + COMMON_SCRIPT + '\n</body>')

    # 11. Add skip-to-content link after <body>
    skip = SKIP_LINK.get(lang, 'Aller au contenu principal')
    if 'skip-link' not in html:
        html = html.replace('<body>\n', f'<body>\n<a href="#main" class="skip-link" style="position:absolute;top:-40px;left:0;padding:0.5rem 1rem;background:var(--gold);color:var(--black);font-family:var(--sans);font-size:0.75rem;z-index:9999;transition:top 0.3s;" onfocus="this.style.top=\'0\'" onblur="this.style.top=\'-40px\'">{skip}</a>\n')

    # 12. Add loading="lazy" to non-hero images and fetchpriority to hero
    # Hero images: first <img> in hero section
    def add_lazy(m):
        tag = m.group(0)
        if 'loading=' in tag:
            return tag
        return tag.replace('<img ', '<img loading="lazy" ')
    # Apply lazy to all imgs except those in #hero
    parts = re.split(r'(<section[^>]*id="hero"[^>]*>.*?</section>)', html, flags=re.DOTALL)
    new_parts = []
    for i, part in enumerate(parts):
        if i % 2 == 1:  # hero section
            new_parts.append(re.sub(r'<img (?!.*fetchpriority)', '<img fetchpriority="high" ', part, count=1))
        else:
            new_parts.append(re.sub(r'<img (?!.*loading=)', add_lazy, part))
    html = ''.join(new_parts)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  OK: {filepath}")

# Process all FR files
print("\n=== Processing FR files ===")
fr_files = list(FR_FILE_META.keys())
for fp in fr_files:
    if os.path.exists(fp):
        process_fr_file(fp)
    else:
        print(f"  MISSING: {fp}")

print("\nFR files processed.")

#!/usr/bin/env python3
"""Build script for Kemora Agency multilingual site."""

import os
import re
import shutil

# ─── CONSTANTS ───────────────────────────────────────────────────────────────

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

# ─── LANGUAGE CONFIGS ────────────────────────────────────────────────────────

LANGS = {
    "fr": {
        "locale": "fr_FR",
        "flag": "🇫🇷",
        "label": "FR",
        "name": "Français",
        "dir": "fr",
        "pages": {
            "index": "index.html",
            "fondations": "fondations.html",
            "about": "a-propos.html",
            "faq": "faq.html",
            "contact": "contact.html",
            "booking": "reserver-appel.html",
            "prod_cadre": "produits/le-cadre-mental.html",
            "prod_exec": "produits/lexecution.html",
            "prod_core": "produits/core-os-ia.html",
            "prod_biz": "produits/business-os-ia.html",
            "prod_kemora": "produits/kemora-os-ia.html",
        },
        "nav": {
            "fondations": "Fondations",
            "about": "À propos",
            "offre": "Notre offre",
            "faq": "FAQ",
            "contact": "Contact",
            "booking": "Réserver un appel",
        },
        "success": "Votre message a bien été envoyé.",
        "skip": "Aller au contenu principal",
        "cookie_text": "Nous utilisons des outils d'analyse respectueux de votre vie privée pour améliorer votre expérience.",
        "cookie_accept": "Accepter",
        "cookie_decline": "Refuser",
        "back_home": "Retour à l'accueil",
    },
    "en": {
        "locale": "en_GB",
        "flag": "🇬🇧",
        "label": "EN",
        "name": "English",
        "dir": "en",
        "pages": {
            "index": "index.html",
            "fondations": "foundations.html",
            "about": "about.html",
            "faq": "faq.html",
            "contact": "contact.html",
            "booking": "book-a-call.html",
            "prod_cadre": "products/the-mental-framework.html",
            "prod_exec": "products/execution.html",
            "prod_core": "products/core-os-ai.html",
            "prod_biz": "products/business-os-ai.html",
            "prod_kemora": "products/kemora-os-ai.html",
        },
        "nav": {
            "fondations": "Foundations",
            "about": "About",
            "offre": "Our Offer",
            "faq": "FAQ",
            "contact": "Contact",
            "booking": "Book a Call",
        },
        "success": "Your message has been sent successfully.",
        "skip": "Skip to main content",
        "cookie_text": "We use privacy-respecting analytics tools to improve your experience.",
        "cookie_accept": "Accept",
        "cookie_decline": "Decline",
        "back_home": "Back to home",
    },
    "es": {
        "locale": "es_ES",
        "flag": "🇪🇸",
        "label": "ES",
        "name": "Español",
        "dir": "es",
        "pages": {
            "index": "index.html",
            "fondations": "fundaciones.html",
            "about": "sobre-nosotros.html",
            "faq": "preguntas-frecuentes.html",
            "contact": "contacto.html",
            "booking": "reservar-llamada.html",
            "prod_cadre": "productos/el-marco-mental.html",
            "prod_exec": "productos/la-ejecucion.html",
            "prod_core": "productos/core-os-ia.html",
            "prod_biz": "productos/business-os-ia.html",
            "prod_kemora": "productos/kemora-os-ia.html",
        },
        "nav": {
            "fondations": "Fundaciones",
            "about": "Sobre Nosotros",
            "offre": "Nuestra Oferta",
            "faq": "FAQ",
            "contact": "Contacto",
            "booking": "Reservar Llamada",
        },
        "success": "Su mensaje ha sido enviado correctamente.",
        "skip": "Ir al contenido principal",
        "cookie_text": "Utilizamos herramientas de análisis respetuosas con su privacidad para mejorar su experiencia.",
        "cookie_accept": "Aceptar",
        "cookie_decline": "Rechazar",
        "back_home": "Volver al inicio",
    },
    "de": {
        "locale": "de_DE",
        "flag": "🇩🇪",
        "label": "DE",
        "name": "Deutsch",
        "dir": "de",
        "pages": {
            "index": "index.html",
            "fondations": "grundlagen.html",
            "about": "ueber-uns.html",
            "faq": "haeufige-fragen.html",
            "contact": "kontakt.html",
            "booking": "anruf-buchen.html",
            "prod_cadre": "produkte/der-mentale-rahmen.html",
            "prod_exec": "produkte/die-ausfuehrung.html",
            "prod_core": "produkte/core-os-ki.html",
            "prod_biz": "produkte/business-os-ki.html",
            "prod_kemora": "produkte/kemora-os-ki.html",
        },
        "nav": {
            "fondations": "Grundlagen",
            "about": "Über Uns",
            "offre": "Unser Angebot",
            "faq": "FAQ",
            "contact": "Kontakt",
            "booking": "Anruf Buchen",
        },
        "success": "Ihre Nachricht wurde erfolgreich gesendet.",
        "skip": "Zum Hauptinhalt springen",
        "cookie_text": "Wir verwenden datenschutzkonforme Analysetools, um Ihre Erfahrung zu verbessern.",
        "cookie_accept": "Akzeptieren",
        "cookie_decline": "Ablehnen",
        "back_home": "Zurück zur Startseite",
    },
    "pt": {
        "locale": "pt_PT",
        "flag": "🇵🇹",
        "label": "PT",
        "name": "Português",
        "dir": "pt",
        "pages": {
            "index": "index.html",
            "fondations": "fundacoes.html",
            "about": "sobre-nos.html",
            "faq": "perguntas-frequentes.html",
            "contact": "contato.html",
            "booking": "reservar-chamada.html",
            "prod_cadre": "produtos/o-quadro-mental.html",
            "prod_exec": "produtos/a-execucao.html",
            "prod_core": "produtos/core-os-ia.html",
            "prod_biz": "produtos/business-os-ia.html",
            "prod_kemora": "produtos/kemora-os-ia.html",
        },
        "nav": {
            "fondations": "Fundações",
            "about": "Sobre Nós",
            "offre": "Nossa Oferta",
            "faq": "FAQ",
            "contact": "Contato",
            "booking": "Reservar Chamada",
        },
        "success": "A sua mensagem foi enviada com sucesso.",
        "skip": "Ir para o conteúdo principal",
        "cookie_text": "Utilizamos ferramentas de análise que respeitam a sua privacidade para melhorar a sua experiência.",
        "cookie_accept": "Aceitar",
        "cookie_decline": "Recusar",
        "back_home": "Voltar ao início",
    },
    "it": {
        "locale": "it_IT",
        "flag": "🇮🇹",
        "label": "IT",
        "name": "Italiano",
        "dir": "it",
        "pages": {
            "index": "index.html",
            "fondations": "fondamenta.html",
            "about": "chi-siamo.html",
            "faq": "domande-frequenti.html",
            "contact": "contatto.html",
            "booking": "prenota-chiamata.html",
            "prod_cadre": "prodotti/il-quadro-mentale.html",
            "prod_exec": "prodotti/lesecuzione.html",
            "prod_core": "prodotti/core-os-ia.html",
            "prod_biz": "prodotti/business-os-ia.html",
            "prod_kemora": "prodotti/kemora-os-ia.html",
        },
        "nav": {
            "fondations": "Fondamenta",
            "about": "Chi Siamo",
            "offre": "La Nostra Offerta",
            "faq": "FAQ",
            "contact": "Contatto",
            "booking": "Prenota una Chiamata",
        },
        "success": "Il Suo messaggio è stato inviato con successo.",
        "skip": "Vai al contenuto principale",
        "cookie_text": "Utilizziamo strumenti di analisi rispettosi della Sua privacy per migliorare la Sua esperienza.",
        "cookie_accept": "Accettare",
        "cookie_decline": "Rifiutare",
        "back_home": "Torna alla home",
    },
}

# ─── SEO DATA PER PAGE PER LANG ──────────────────────────────────────────────

SEO = {
    "fr": {
        "index": {
            "title": "Kemora Agency — Maîtrisez l'IA. Automatisez. Libérez votre potentiel.",
            "desc": "Écosystème digital premium dédié à l'IA, l'automatisation et les systèmes de croissance intelligents. Cinq ressources pour transformer votre activité.",
            "slug": "index.html",
            "hreflang_key": "index",
            "schema": "org",
            "image": "/assets/images/Accueil.webp",
        },
        "fondations.html": {
            "title": "Fondations — Les principes de Kemora Agency",
            "desc": "Découvrez les fondations intellectuelles et stratégiques qui sous-tendent l'approche Kemora Agency. IA, automatisation, systèmes de croissance.",
            "slug": "fondations.html",
            "hreflang_key": "fondations",
            "schema": None,
            "image": "/assets/images/fondations.webp",
        },
        "a-propos.html": {
            "title": "À propos — La mission de Kemora Agency",
            "desc": "Kemora Agency : un écosystème digital conçu pour aider les entrepreneurs à exploiter pleinement le potentiel de l'intelligence artificielle.",
            "slug": "a-propos.html",
            "hreflang_key": "about",
            "schema": "org",
            "image": "/assets/images/apropos.webp",
        },
        "faq.html": {
            "title": "Questions fréquentes — Kemora Agency",
            "desc": "Toutes les réponses aux questions les plus fréquentes sur Kemora Agency, ses ressources, l'IA et l'automatisation. Clarté avant décision.",
            "slug": "faq.html",
            "hreflang_key": "faq",
            "schema": "faq",
            "image": "/assets/images/faq.webp",
        },
        "contact.html": {
            "title": "Contact — Échangeons sur votre projet",
            "desc": "Prenez contact avec Kemora Agency pour toute question sur nos ressources, notre accompagnement ou votre projet digital et IA.",
            "slug": "contact.html",
            "hreflang_key": "contact",
            "schema": None,
            "image": "/assets/images/contact.webp",
        },
        "reserver-appel.html": {
            "title": "Réserver un appel — Kemora Agency",
            "desc": "Réservez un appel stratégique avec Kemora Agency. Échangeons sur votre situation, vos objectifs et la ressource qui vous correspond.",
            "slug": "reserver-appel.html",
            "hreflang_key": "booking",
            "schema": None,
            "image": "/assets/images/contact.webp",
        },
        "produits/le-cadre-mental.html": {
            "title": "Le Cadre Mental — Kemora Agency | 37 €",
            "desc": "Adoptez la posture et l'architecture de pensée qui précèdent toute transformation durable. Le Cadre Mental par Kemora Agency — 37 €.",
            "slug": "produits/le-cadre-mental.html",
            "hreflang_key": "prod_cadre",
            "schema": "product",
            "product": {"name": "Le Cadre Mental", "price": "37", "stripe": STRIPE["cadre-mental"]},
            "image": "/assets/images/le_cadremental.webp",
        },
        "produits/lexecution.html": {
            "title": "L'Exécution — Kemora Agency | 37 €",
            "desc": "Les systèmes pour passer de l'intention à l'action — de façon structurée, répétable et efficace. L'Exécution par Kemora Agency — 37 €.",
            "slug": "produits/lexecution.html",
            "hreflang_key": "prod_exec",
            "schema": "product",
            "product": {"name": "L'Exécution", "price": "37", "stripe": STRIPE["execution"]},
            "image": "/assets/images/lexecution.webp",
        },
        "produits/core-os-ia.html": {
            "title": "CORE OS IA — Kemora Agency | 97 €",
            "desc": "Les fondations d'un business automatisé : outils IA essentiels, 5 piliers et plan d'action sur 7 jours. CORE OS IA — 97 €.",
            "slug": "produits/core-os-ia.html",
            "hreflang_key": "prod_core",
            "schema": "product",
            "product": {"name": "CORE OS IA", "price": "97", "stripe": STRIPE["core-os-ia"]},
            "image": "/assets/images/coreosia.webp",
        },
        "produits/business-os-ia.html": {
            "title": "Business OS IA — Kemora Agency | 230 €",
            "desc": "Stratégie avancée, monétisation et automatisation pour un business solide et scalable. Business OS IA par Kemora Agency — 230 €.",
            "slug": "produits/business-os-ia.html",
            "hreflang_key": "prod_biz",
            "schema": "product",
            "product": {"name": "Business OS IA", "price": "230", "stripe": STRIPE["business-os-ia"]},
            "image": "/assets/images/businessosia.webp",
        },
        "produits/kemora-os-ia.html": {
            "title": "Kemora OS IA — L'écosystème complet | 347 €",
            "desc": "L'écosystème IA complet — la méthode Kemora dans sa version la plus aboutie pour un business entièrement orchestré par l'IA. 347 €.",
            "slug": "produits/kemora-os-ia.html",
            "hreflang_key": "prod_kemora",
            "schema": "product",
            "product": {"name": "Kemora OS IA", "price": "347", "stripe": STRIPE["kemora-os-ia"]},
            "image": "/assets/images/kemoraosia.webp",
        },
    }
}

# ─── HREFLANG MAP ─────────────────────────────────────────────────────────────

HREFLANG = {
    "index": {"fr": "fr/index.html", "en": "en/index.html", "es": "es/index.html", "de": "de/index.html", "pt": "pt/index.html", "it": "it/index.html"},
    "fondations": {"fr": "fr/fondations.html", "en": "en/foundations.html", "es": "es/fundaciones.html", "de": "de/grundlagen.html", "pt": "pt/fundacoes.html", "it": "it/fondamenta.html"},
    "about": {"fr": "fr/a-propos.html", "en": "en/about.html", "es": "es/sobre-nosotros.html", "de": "de/ueber-uns.html", "pt": "pt/sobre-nos.html", "it": "it/chi-siamo.html"},
    "faq": {"fr": "fr/faq.html", "en": "en/faq.html", "es": "es/preguntas-frecuentes.html", "de": "de/haeufige-fragen.html", "pt": "pt/perguntas-frequentes.html", "it": "it/domande-frequenti.html"},
    "contact": {"fr": "fr/contact.html", "en": "en/contact.html", "es": "es/contacto.html", "de": "de/kontakt.html", "pt": "pt/contato.html", "it": "it/contatto.html"},
    "booking": {"fr": "fr/reserver-appel.html", "en": "en/book-a-call.html", "es": "es/reservar-llamada.html", "de": "de/anruf-buchen.html", "pt": "pt/reservar-chamada.html", "it": "it/prenota-chiamata.html"},
    "prod_cadre": {"fr": "fr/produits/le-cadre-mental.html", "en": "en/products/the-mental-framework.html", "es": "es/productos/el-marco-mental.html", "de": "de/produkte/der-mentale-rahmen.html", "pt": "pt/produtos/o-quadro-mental.html", "it": "it/prodotti/il-quadro-mentale.html"},
    "prod_exec": {"fr": "fr/produits/lexecution.html", "en": "en/products/execution.html", "es": "es/productos/la-ejecucion.html", "de": "de/produkte/die-ausfuehrung.html", "pt": "pt/produtos/a-execucao.html", "it": "it/prodotti/lesecuzione.html"},
    "prod_core": {"fr": "fr/produits/core-os-ia.html", "en": "en/products/core-os-ai.html", "es": "es/productos/core-os-ia.html", "de": "de/produkte/core-os-ki.html", "pt": "pt/produtos/core-os-ia.html", "it": "it/prodotti/core-os-ia.html"},
    "prod_biz": {"fr": "fr/produits/business-os-ia.html", "en": "en/products/business-os-ai.html", "es": "es/productos/business-os-ia.html", "de": "de/produkte/business-os-ki.html", "pt": "pt/produtos/business-os-ia.html", "it": "it/prodotti/business-os-ia.html"},
    "prod_kemora": {"fr": "fr/produits/kemora-os-ia.html", "en": "en/products/kemora-os-ai.html", "es": "es/productos/kemora-os-ia.html", "de": "de/produkte/kemora-os-ki.html", "pt": "pt/produtos/kemora-os-ia.html", "it": "it/prodotti/kemora-os-ia.html"},
}

def hreflang_tags(key):
    links = HREFLANG.get(key, {})
    tags = []
    for lang, path in links.items():
        tags.append(f'<link rel="alternate" hreflang="{lang}" href="{SITE_URL}/{path}">')
    tags.append(f'<link rel="alternate" hreflang="x-default" href="{SITE_URL}/fr/index.html">')
    return "\n".join(tags)

def seo_head(lang, slug, title=None, desc=None, hreflang_key=None, image=None, product=None, schema_type=None):
    cfg = LANGS[lang]
    locale = cfg["locale"]
    if not title:
        seo_data = SEO.get("fr", {}).get(slug, {})
        title = seo_data.get("title", f"Kemora Agency")
        desc = seo_data.get("desc", "Écosystème digital premium dédié à l'IA.")
        hreflang_key = seo_data.get("hreflang_key", "index")
        image = seo_data.get("image", "/assets/images/Accueil.webp")

    canonical = f"{SITE_URL}/{lang}/{slug}"
    og_image = f"{SITE_URL}{image}" if image and not image.startswith("http") else (image or f"{SITE_URL}/assets/images/Accueil.webp")

    hreflang = hreflang_tags(hreflang_key) if hreflang_key else ""

    head = f"""<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Kemora Agency</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title} — Kemora Agency">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:type" content="website">
<meta property="og:locale" content="{locale}">
<meta property="og:site_name" content="Kemora Agency">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title} — Kemora Agency">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{og_image}">
{hreflang}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<meta name="theme-color" content="#C6A16E">
<link rel="icon" href="/assets/favicon/favicon.ico">
<link rel="apple-touch-icon" href="/assets/favicon/apple-touch-icon.png">
<link rel="manifest" href="/manifest.json">"""
    return head

def lang_switcher_css():
    return """
  /* ─── LANGUAGE SWITCHER ─── */
  .lang-switcher { position: relative; margin-left: 1.2rem; }
  .lang-btn { display: flex; align-items: center; gap: 0.4rem; font-family: var(--sans); font-size: 0.68rem; font-weight: 500; letter-spacing: 0.14em; text-transform: uppercase; color: var(--gold); background: transparent; border: 1px solid var(--border); padding: 0.35rem 0.75rem; cursor: pointer; transition: all 0.3s; white-space: nowrap; }
  .lang-btn:hover { border-color: var(--gold); }
  .lang-btn svg { width: 10px; height: 10px; transition: transform 0.3s; }
  .lang-switcher.open .lang-btn svg { transform: rotate(180deg); }
  .lang-menu { position: absolute; top: calc(100% + 0.6rem); right: 0; background: var(--black2); border: 1px solid var(--border); min-width: 160px; padding: 0.4rem 0; opacity: 0; pointer-events: none; transform: translateY(-6px); transition: opacity 0.25s, transform 0.25s; z-index: 300; box-shadow: 0 20px 50px rgba(0,0,0,0.7); }
  .lang-switcher.open .lang-menu { opacity: 1; pointer-events: all; transform: translateY(0); }
  .lang-menu a { display: flex; align-items: center; gap: 0.6rem; padding: 0.6rem 1rem; font-family: var(--sans); font-size: 0.68rem; letter-spacing: 0.12em; text-transform: uppercase; color: var(--muted); text-decoration: none; transition: color 0.2s, background 0.2s; }
  .lang-menu a:hover { color: var(--gold); background: rgba(198,161,110,0.04); }
  .lang-menu a.active { color: var(--gold); }
  /* Mobile lang */
  .nav-mobile .lang-mobile { margin-top: 1.2rem; padding-top: 1.2rem; border-top: 1px solid var(--border2); display: flex; flex-wrap: wrap; gap: 0.6rem; }
  .nav-mobile .lang-mobile a { font-family: var(--sans); font-size: 0.68rem; letter-spacing: 0.14em; text-transform: uppercase; color: var(--muted); text-decoration: none; border: 1px solid var(--border2); padding: 0.4rem 0.8rem; transition: color 0.3s, border-color 0.3s; }
  .nav-mobile .lang-mobile a:hover, .nav-mobile .lang-mobile a.active { color: var(--gold); border-color: var(--gold); }"""

def lang_switcher_html(current_lang, page_key):
    cfg = LANGS[current_lang]
    links = HREFLANG.get(page_key, {})
    items = []
    for lang in ["fr", "en", "es", "de", "pt", "it"]:
        lc = LANGS[lang]
        path = links.get(lang, f"{lang}/index.html")
        active = ' class="active"' if lang == current_lang else ''
        items.append(f'<a href="/{path}" data-lang="{lang}"{active}>{lc["flag"]} {lc["label"]}</a>')

    mobile_items = []
    for lang in ["fr", "en", "es", "de", "pt", "it"]:
        lc = LANGS[lang]
        path = links.get(lang, f"{lang}/index.html")
        active = ' class="active"' if lang == current_lang else ''
        mobile_items.append(f'<a href="/{path}" data-lang="{lang}"{active}>{lc["flag"]} {lc["label"]}</a>')

    switcher = f"""<div class="lang-switcher" id="langSwitcher">
    <button class="lang-btn" onclick="toggleLang()" aria-label="Choisir la langue" aria-haspopup="true" aria-expanded="false">
      {cfg["flag"]} {cfg["label"]}
      <svg viewBox="0 0 10 6" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M1 1l4 4 4-4"/></svg>
    </button>
    <div class="lang-menu">
      {"".join(items)}
    </div>
  </div>"""
    return switcher, "\n".join([f'  {i}' for i in mobile_items])

def cookie_banner_html(lang):
    cfg = LANGS[lang]
    return f"""
<!-- COOKIE BANNER -->
<div id="cookieBanner" style="display:none;position:fixed;bottom:0;left:0;right:0;z-index:1000;background:var(--black2);border-top:1px solid var(--border);padding:1.2rem clamp(1.5rem,5vw,4rem);display:flex;align-items:center;justify-content:space-between;gap:1.5rem;flex-wrap:wrap;">
  <p style="font-size:0.78rem;color:var(--muted);line-height:1.6;max-width:600px;">{cfg["cookie_text"]}</p>
  <div style="display:flex;gap:0.8rem;flex-shrink:0;">
    <button onclick="acceptCookies()" style="background:var(--gold);color:var(--black);border:none;padding:0.6rem 1.4rem;font-family:var(--sans);font-size:0.72rem;font-weight:500;letter-spacing:0.12em;text-transform:uppercase;cursor:pointer;">{cfg["cookie_accept"]}</button>
    <button onclick="declineCookies()" style="background:transparent;color:var(--muted);border:1px solid var(--border);padding:0.6rem 1.4rem;font-family:var(--sans);font-size:0.72rem;letter-spacing:0.12em;text-transform:uppercase;cursor:pointer;">{cfg["cookie_decline"]}</button>
  </div>
</div>"""

def cookie_script():
    return """
<script>
(function(){
  var consent = localStorage.getItem('kemora-cookies');
  if(!consent){ var b=document.getElementById('cookieBanner'); if(b) b.style.display='flex'; }
  else if(consent==='accepted'){ loadAnalytics(); }
})();
function acceptCookies(){ localStorage.setItem('kemora-cookies','accepted'); var b=document.getElementById('cookieBanner'); if(b) b.style.display='none'; loadAnalytics(); }
function declineCookies(){ localStorage.setItem('kemora-cookies','declined'); var b=document.getElementById('cookieBanner'); if(b) b.style.display='none'; }
function loadAnalytics(){ if(window._analyticsLoaded) return; window._analyticsLoaded=true; var s=document.createElement('script'); s.defer=true; s.setAttribute('data-domain','kemora-agency.com'); s.src='https://plausible.io/js/script.js'; document.head.appendChild(s); }
function toggleLang(){ var s=document.getElementById('langSwitcher'); if(s){ s.classList.toggle('open'); var b=s.querySelector('.lang-btn'); if(b) b.setAttribute('aria-expanded', s.classList.contains('open')); } }
document.addEventListener('click', function(e){ var s=document.getElementById('langSwitcher'); if(s && !s.contains(e.target)) s.classList.remove('open'); });
document.querySelectorAll('[data-lang]').forEach(function(a){ a.addEventListener('click', function(){ localStorage.setItem('kemora-lang', this.getAttribute('data-lang')); }); });
</script>"""

def sw_script():
    return '<script>if("serviceWorker" in navigator){navigator.serviceWorker.register("/sw.js");}</script>'

print("Build configuration loaded successfully.")
print(f"Languages: {list(LANGS.keys())}")
print(f"Total pages planned: 84+")

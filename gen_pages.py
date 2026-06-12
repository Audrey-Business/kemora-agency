#!/usr/bin/env python3
"""Generate all remaining pages for Kemora Agency multilingual site."""
import os

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
    "index":       {"fr":"fr/index.html","en":"en/index.html","es":"es/index.html","de":"de/index.html","pt":"pt/index.html","it":"it/index.html"},
    "fondations":  {"fr":"fr/fondations.html","en":"en/foundations.html","es":"es/fundaciones.html","de":"de/grundlagen.html","pt":"pt/fundacoes.html","it":"it/fondamenta.html"},
    "about":       {"fr":"fr/a-propos.html","en":"en/about.html","es":"es/sobre-nosotros.html","de":"de/ueber-uns.html","pt":"pt/sobre-nos.html","it":"it/chi-siamo.html"},
    "faq":         {"fr":"fr/faq.html","en":"en/faq.html","es":"es/preguntas-frecuentes.html","de":"de/haeufige-fragen.html","pt":"pt/perguntas-frequentes.html","it":"it/domande-frequenti.html"},
    "contact":     {"fr":"fr/contact.html","en":"en/contact.html","es":"es/contacto.html","de":"de/kontakt.html","pt":"pt/contato.html","it":"it/contatto.html"},
    "booking":     {"fr":"fr/reserver-appel.html","en":"en/book-a-call.html","es":"es/reservar-llamada.html","de":"de/anruf-buchen.html","pt":"pt/reservar-chamada.html","it":"it/prenota-chiamata.html"},
    "legal":       {"fr":"fr/mentions-legales.html","en":"en/legal-notice.html","es":"es/menciones-legales.html","de":"de/impressum.html","pt":"pt/mencoes-legais.html","it":"it/note-legali.html"},
    "privacy":     {"fr":"fr/politique-confidentialite.html","en":"en/privacy-policy.html","es":"es/politica-privacidad.html","de":"de/datenschutz.html","pt":"pt/politica-privacidade.html","it":"it/politica-privacy.html"},
    "prod_cadre":  {"fr":"fr/produits/le-cadre-mental.html","en":"en/products/the-mental-framework.html","es":"es/productos/el-marco-mental.html","de":"de/produkte/der-mentale-rahmen.html","pt":"pt/produtos/o-quadro-mental.html","it":"it/prodotti/il-quadro-mentale.html"},
    "prod_exec":   {"fr":"fr/produits/lexecution.html","en":"en/products/execution.html","es":"es/productos/la-ejecucion.html","de":"de/produkte/die-ausfuehrung.html","pt":"pt/produtos/a-execucao.html","it":"it/prodotti/lesecuzione.html"},
    "prod_core":   {"fr":"fr/produits/core-os-ia.html","en":"en/products/core-os-ai.html","es":"es/productos/core-os-ia.html","de":"de/produkte/core-os-ki.html","pt":"pt/produtos/core-os-ia.html","it":"it/prodotti/core-os-ia.html"},
    "prod_biz":    {"fr":"fr/produits/business-os-ia.html","en":"en/products/business-os-ai.html","es":"es/productos/business-os-ia.html","de":"de/produkte/business-os-ki.html","pt":"pt/produtos/business-os-ia.html","it":"it/prodotti/business-os-ia.html"},
    "prod_kemora": {"fr":"fr/produits/kemora-os-ia.html","en":"en/products/kemora-os-ai.html","es":"es/productos/kemora-os-ia.html","de":"de/produkte/kemora-os-ki.html","pt":"pt/produtos/kemora-os-ia.html","it":"it/prodotti/kemora-os-ia.html"},
}

LANGS_META = {
    "fr":{"locale":"fr_FR","flag":"🇫🇷","lbl":"FR"},
    "en":{"locale":"en_GB","flag":"🇬🇧","lbl":"EN"},
    "es":{"locale":"es_ES","flag":"🇪🇸","lbl":"ES"},
    "de":{"locale":"de_DE","flag":"🇩🇪","lbl":"DE"},
    "pt":{"locale":"pt_PT","flag":"🇵🇹","lbl":"PT"},
    "it":{"locale":"it_IT","flag":"🇮🇹","lbl":"IT"},
}

COOKIE = {
    "fr":("Nous utilisons des outils d'analyse respectueux de votre vie privée pour améliorer votre expérience.","Accepter","Refuser"),
    "en":("We use privacy-respecting analytics tools to improve your experience.","Accept","Decline"),
    "es":("Utilizamos herramientas de análisis respetuosas con su privacidad para mejorar su experiencia.","Aceptar","Rechazar"),
    "de":("Wir verwenden datenschutzkonforme Analysetools, um Ihre Erfahrung zu verbessern.","Akzeptieren","Ablehnen"),
    "pt":("Utilizamos ferramentas de análise que respeitam a sua privacidade para melhorar a sua experiência.","Aceitar","Recusar"),
    "it":("Utilizziamo strumenti di analisi rispettosi della Sua privacy per migliorare la Sua esperienza.","Accettare","Rifiutare"),
}

NAV_LABELS = {
    "fr":{"fond":"Fondations","about":"À propos","offre":"Notre offre","faq":"FAQ","contact":"Contact","booking":"Réserver un appel","back":"Retour à l'accueil"},
    "en":{"fond":"Foundations","about":"About","offre":"Our Offer","faq":"FAQ","contact":"Contact","booking":"Book a Call","back":"Back to home"},
    "es":{"fond":"Fundaciones","about":"Sobre Nosotros","offre":"Nuestra Oferta","faq":"FAQ","contact":"Contacto","booking":"Reservar Llamada","back":"Volver al inicio"},
    "de":{"fond":"Grundlagen","about":"Über Uns","offre":"Unser Angebot","faq":"FAQ","contact":"Kontakt","booking":"Anruf Buchen","back":"Zurück zur Startseite"},
    "pt":{"fond":"Fundações","about":"Sobre Nós","offre":"Nossa Oferta","faq":"FAQ","contact":"Contato","booking":"Reservar Chamada","back":"Voltar ao início"},
    "it":{"fond":"Fondamenta","about":"Chi Siamo","offre":"La Nostra Offerta","faq":"FAQ","contact":"Contatto","booking":"Prenota una Chiamata","back":"Torna alla home"},
}

PROD_NAMES = {
    "cadre": "Le Cadre Mental",
    "exec":  "L'Exécution",
    "core":  "CORE OS IA",
    "biz":   "Business OS IA",
    "kemora":"Kemora OS IA",
}

PROD_DIR = {"fr":"produits","en":"products","es":"productos","de":"produkte","pt":"produtos","it":"prodotti"}

PROD_FILES = {
    "fr":   {"cadre":"le-cadre-mental.html","exec":"lexecution.html","core":"core-os-ia.html","biz":"business-os-ia.html","kemora":"kemora-os-ia.html"},
    "en":   {"cadre":"the-mental-framework.html","exec":"execution.html","core":"core-os-ai.html","biz":"business-os-ai.html","kemora":"kemora-os-ai.html"},
    "es":   {"cadre":"el-marco-mental.html","exec":"la-ejecucion.html","core":"core-os-ia.html","biz":"business-os-ia.html","kemora":"kemora-os-ia.html"},
    "de":   {"cadre":"der-mentale-rahmen.html","exec":"die-ausfuehrung.html","core":"core-os-ki.html","biz":"business-os-ki.html","kemora":"kemora-os-ki.html"},
    "pt":   {"cadre":"o-quadro-mental.html","exec":"a-execucao.html","core":"core-os-ia.html","biz":"business-os-ia.html","kemora":"kemora-os-ia.html"},
    "it":   {"cadre":"il-quadro-mentale.html","exec":"lesecuzione.html","core":"core-os-ia.html","biz":"business-os-ia.html","kemora":"kemora-os-ia.html"},
}

INDEX_FILES = {"fr":"index.html","en":"index.html","es":"index.html","de":"index.html","pt":"index.html","it":"index.html"}

GRAIN = "url(\"data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E\")"

BASE_CSS = """  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  :root {
    --black:#050505; --black2:#0a0a0a; --black3:#111111;
    --gold:#C6A16E; --gold-dim:#8a6e49; --white:#f5f0e8;
    --muted:rgba(245,240,232,0.45); --border:rgba(198,161,110,0.18); --border2:rgba(198,161,110,0.08);
    --serif:'Cormorant Garamond',Georgia,'Times New Roman',serif;
    --sans:'Jost',system-ui,-apple-system,BlinkMacSystemFont,sans-serif;
    --ease:cubic-bezier(0.25,0.46,0.45,0.94);
  }
  html { scroll-behavior: smooth; }
  body { background:var(--black); color:var(--white); font-family:var(--sans); font-weight:300; line-height:1.7; overflow-x:hidden; -webkit-font-smoothing:antialiased; }
  body::before { content:''; position:fixed; inset:0; background-image:""" + GRAIN + """; pointer-events:none; z-index:9999; opacity:0.5; }
  h1,h2,h3 { font-family:var(--serif); font-weight:400; }
  h1 { font-size:clamp(2.6rem,6vw,5rem); line-height:1.08; letter-spacing:-0.02em; }
  h2 { font-size:clamp(2rem,4.5vw,3.4rem); line-height:1.12; letter-spacing:-0.01em; }
  h3 { font-size:clamp(1.25rem,2.2vw,1.7rem); line-height:1.2; }
  p  { font-size:clamp(0.88rem,1.4vw,1rem); }
  em { font-style:italic; color:var(--gold); }
  .label { font-family:var(--sans); font-size:0.68rem; font-weight:500; letter-spacing:0.22em; text-transform:uppercase; color:var(--gold); }
  .container { max-width:1100px; margin:0 auto; padding:0 clamp(1.5rem,5vw,4rem); }
  .section { padding:clamp(5rem,10vw,9rem) 0; }
  .divider-h { height:1px; background:linear-gradient(to right,transparent,var(--border),transparent); }
  .btn-gold { display:inline-flex; align-items:center; gap:0.6rem; background:var(--gold); color:var(--black); font-family:var(--sans); font-size:0.78rem; font-weight:500; letter-spacing:0.14em; text-transform:uppercase; padding:1rem 2.4rem; border:none; cursor:pointer; text-decoration:none; transition:all 0.3s var(--ease); position:relative; overflow:hidden; white-space:nowrap; }
  .btn-gold::after { content:''; position:absolute; inset:0; background:rgba(255,255,255,0.12); opacity:0; transition:opacity 0.3s; }
  .btn-gold:hover::after { opacity:1; }
  .btn-gold:hover { transform:translateY(-2px); box-shadow:0 12px 40px rgba(198,161,110,0.3); }
  .btn-outline { display:inline-flex; align-items:center; gap:0.6rem; background:transparent; color:var(--gold); font-family:var(--sans); font-size:0.78rem; font-weight:400; letter-spacing:0.14em; text-transform:uppercase; padding:0.95rem 2.2rem; border:1px solid var(--border); cursor:pointer; text-decoration:none; transition:all 0.3s var(--ease); white-space:nowrap; }
  .btn-outline:hover { border-color:var(--gold); background:rgba(198,161,110,0.06); }
  .reveal { opacity:0; transform:translateY(24px); transition:opacity 0.75s var(--ease),transform 0.75s var(--ease); }
  .reveal.visible { opacity:1; transform:translateY(0); }
  .reveal-delay-1 { transition-delay:0.12s; }
  .reveal-delay-2 { transition-delay:0.24s; }
  .reveal-delay-3 { transition-delay:0.36s; }
  @media (prefers-reduced-motion:reduce) { .reveal { opacity:1; transform:none; transition:none; } }"""

NAV_CSS = """
  nav { position:fixed; top:0; left:0; right:0; z-index:200; padding:0 clamp(1.5rem,5vw,4rem); height:72px; display:flex; align-items:center; justify-content:space-between; background:rgba(5,5,5,0.88); backdrop-filter:blur(22px); border-bottom:1px solid var(--border2); transition:border-color 0.3s; }
  .nav-brand { font-family:var(--serif); font-size:1rem; letter-spacing:0.12em; text-transform:uppercase; color:var(--white); text-decoration:none; flex-shrink:0; margin-right:1rem; }
  .nav-links { display:flex; align-items:center; gap:2.2rem; list-style:none; }
  .nav-links a { font-family:var(--sans); font-size:0.7rem; letter-spacing:0.14em; text-transform:uppercase; color:var(--muted); text-decoration:none; transition:color 0.3s; white-space:nowrap; }
  .nav-links a:hover { color:var(--gold); }
  .nav-dropdown { position:relative; }
  .nav-dropdown > a { display:flex; align-items:center; gap:0.35rem; }
  .nav-dropdown > a svg { width:10px; height:10px; transition:transform 0.3s; }
  .nav-dropdown:hover > a svg { transform:rotate(180deg); }
  .nav-dropdown:hover > a { color:var(--gold); }
  .dropdown-menu { position:absolute; top:calc(100% + 1.2rem); left:50%; transform:translateX(-50%) translateY(-6px); background:var(--black2); border:1px solid var(--border); min-width:230px; padding:0.6rem 0; opacity:0; pointer-events:none; transition:opacity 0.25s var(--ease),transform 0.25s var(--ease); box-shadow:0 24px 60px rgba(0,0,0,0.7); }
  .nav-dropdown:hover .dropdown-menu { opacity:1; pointer-events:all; transform:translateX(-50%) translateY(0); }
  .dropdown-menu a { display:block; padding:0.7rem 1.4rem; font-size:0.7rem; letter-spacing:0.14em; text-transform:uppercase; color:var(--muted); text-decoration:none; transition:color 0.2s,background 0.2s; border-left:2px solid transparent; }
  .dropdown-menu a:hover { color:var(--gold); background:rgba(198,161,110,0.04); border-left-color:var(--gold); }
  .nav-cta { font-family:var(--sans); font-size:0.68rem; font-weight:500; letter-spacing:0.14em; text-transform:uppercase; color:var(--black) !important; background:var(--gold); padding:0.38rem 1rem; text-decoration:none; transition:all 0.3s; white-space:nowrap; }
  .nav-cta:hover { background:var(--white); }
  .nav-toggle { display:none; flex-direction:column; gap:5px; cursor:pointer; padding:4px; background:transparent; border:none; min-width:44px; min-height:44px; align-items:center; justify-content:center; }
  .nav-toggle span { display:block; width:22px; height:1px; background:var(--gold); transition:all 0.3s; }
  .nav-toggle.open span:nth-child(1) { transform:translateY(6px) rotate(45deg); }
  .nav-toggle.open span:nth-child(2) { opacity:0; }
  .nav-toggle.open span:nth-child(3) { transform:translateY(-6px) rotate(-45deg); }
  .nav-mobile { display:none; position:fixed; top:72px; left:0; right:0; background:var(--black2); border-bottom:1px solid var(--border); z-index:199; padding:2rem clamp(1.5rem,5vw,4rem); overflow-y:auto; max-height:calc(100vh - 72px); }
  .nav-mobile.open { display:block; }
  .nav-mobile a { display:block; font-family:var(--sans); font-size:0.78rem; letter-spacing:0.16em; text-transform:uppercase; color:var(--muted); text-decoration:none; padding:0.85rem 0; border-bottom:1px solid var(--border2); transition:color 0.3s; min-height:44px; display:flex; align-items:center; }
  .nav-mobile a:hover { color:var(--gold); }
  .nav-mobile a.mobile-cta { color:var(--gold); border:1px solid var(--border); text-align:center; padding:0.9rem; margin-top:1.2rem; justify-content:center; }
  .lang-switcher { position:relative; margin-left:1rem; }
  .lang-btn { display:flex; align-items:center; gap:0.4rem; font-family:var(--sans); font-size:0.68rem; font-weight:500; letter-spacing:0.14em; text-transform:uppercase; color:var(--gold); background:transparent; border:1px solid var(--border); padding:0.35rem 0.75rem; cursor:pointer; transition:all 0.3s; white-space:nowrap; min-height:44px; }
  .lang-btn:hover { border-color:var(--gold); }
  .lang-btn svg { width:10px; height:10px; transition:transform 0.3s; }
  .lang-switcher.open .lang-btn svg { transform:rotate(180deg); }
  .lang-menu { position:absolute; top:calc(100% + 0.6rem); right:0; background:var(--black2); border:1px solid var(--border); min-width:160px; padding:0.4rem 0; opacity:0; pointer-events:none; transform:translateY(-6px); transition:opacity 0.25s,transform 0.25s; z-index:300; box-shadow:0 20px 50px rgba(0,0,0,0.7); }
  .lang-switcher.open .lang-menu { opacity:1; pointer-events:all; transform:translateY(0); }
  .lang-menu a { display:flex; align-items:center; gap:0.6rem; padding:0.6rem 1rem; font-family:var(--sans); font-size:0.68rem; letter-spacing:0.12em; text-transform:uppercase; color:var(--muted); text-decoration:none; transition:color 0.2s,background 0.2s; min-height:44px; }
  .lang-menu a:hover,.lang-menu a.active { color:var(--gold); background:rgba(198,161,110,0.04); }
  .lang-mobile-wrap { margin-top:1.2rem; padding-top:1.2rem; border-top:1px solid var(--border2); display:flex; flex-wrap:wrap; gap:0.6rem; }
  .lang-mobile-wrap a { font-family:var(--sans); font-size:0.68rem; letter-spacing:0.14em; text-transform:uppercase; color:var(--muted); text-decoration:none; border:1px solid var(--border2); padding:0.4rem 0.8rem; transition:color 0.3s,border-color 0.3s; min-height:44px; display:flex; align-items:center; }
  .lang-mobile-wrap a:hover,.lang-mobile-wrap a.active { color:var(--gold); border-color:var(--gold); }
  footer { padding:3rem clamp(1.5rem,5vw,4rem); border-top:1px solid var(--border2); }
  .footer-inner { display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:1.5rem; }
  .footer-brand { font-family:var(--serif); font-size:0.95rem; letter-spacing:0.12em; text-transform:uppercase; }
  .footer-links { display:flex; gap:2rem; flex-wrap:wrap; }
  .footer-links a { font-size:0.72rem; letter-spacing:0.12em; text-transform:uppercase; color:var(--muted); text-decoration:none; transition:color 0.3s; }
  .footer-links a:hover { color:var(--gold); }
  .footer-copy { font-size:0.65rem; letter-spacing:0.1em; color:rgba(245,240,232,0.25); width:100%; text-align:center; margin-top:1.2rem; padding-top:1.2rem; border-top:1px solid var(--border2); }
  @media (max-width:960px) { .nav-links { display:none; } .nav-toggle { display:flex; } }
  @media (max-width:600px) { .footer-inner { flex-direction:column; align-items:flex-start; } }"""

FONT_LINK = '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=Jost:wght@200;300;400;500&display=swap" rel="stylesheet">'

COMMON_JS = """<script>
(function(){
  var c=localStorage.getItem('kemora-cookies');
  if(!c){var b=document.getElementById('cookieBanner');if(b)b.style.display='flex';}
  else if(c==='accepted'){loadAnalytics();}
})();
function acceptCookies(){localStorage.setItem('kemora-cookies','accepted');var b=document.getElementById('cookieBanner');if(b)b.style.display='none';loadAnalytics();}
function declineCookies(){localStorage.setItem('kemora-cookies','declined');var b=document.getElementById('cookieBanner');if(b)b.style.display='none';}
function loadAnalytics(){if(window._al)return;window._al=true;var s=document.createElement('script');s.defer=true;s.setAttribute('data-domain','kemora-agency.com');s.src='https://plausible.io/js/script.js';document.head.appendChild(s);}
function toggleLang(e){e.stopPropagation();var s=document.getElementById('langSwitcher');if(s){s.classList.toggle('open');var b=s.querySelector('.lang-btn');if(b)b.setAttribute('aria-expanded',s.classList.contains('open'));}}
document.addEventListener('click',function(e){var s=document.getElementById('langSwitcher');if(s&&!s.contains(e.target))s.classList.remove('open');});
document.querySelectorAll('[data-lang]').forEach(function(a){a.addEventListener('click',function(){localStorage.setItem('kemora-lang',this.getAttribute('data-lang'));});});
if('serviceWorker' in navigator){navigator.serviceWorker.register('/sw.js');}
var _obs=new IntersectionObserver(function(entries){entries.forEach(function(e){if(e.isIntersecting){e.target.classList.add('visible');_obs.unobserve(e.target);}});},{threshold:0.1});
document.querySelectorAll('.reveal').forEach(function(el){_obs.observe(el);});
window.addEventListener('scroll',function(){var nav=document.getElementById('mainNav');if(nav)nav.style.borderBottomColor=window.scrollY>50?'rgba(198,161,110,0.15)':'rgba(198,161,110,0.06)';});
</script>"""

def hreflang(key):
    links = HREFLANG.get(key, {})
    return "\n".join([f'<link rel="alternate" hreflang="{l}" href="{SITE_URL}/{p}">' for l,p in links.items()]) + f'\n<link rel="alternate" hreflang="x-default" href="{SITE_URL}/fr/index.html">'

def head(lang, title, desc, slug, hk, image="/assets/images/Accueil.webp"):
    locale = LANGS_META[lang]["locale"]
    canon = f"{SITE_URL}/{lang}/{slug}"
    ogimg = f"{SITE_URL}{image}"
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Kemora Agency</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{title} — Kemora Agency">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{ogimg}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:type" content="website">
<meta property="og:locale" content="{locale}">
<meta property="og:site_name" content="Kemora Agency">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title} — Kemora Agency">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{ogimg}">
{hreflang(hk)}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="image" href="{image}">
<link rel="icon" href="/assets/favicon/favicon.ico">
<link rel="apple-touch-icon" href="/assets/favicon/apple-touch-icon.png">
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#C6A16E">
{FONT_LINK}"""

def lang_widget(lang, hk):
    links = HREFLANG.get(hk, {})
    m = LANGS_META[lang]
    items = ""
    mob = ""
    for l in ["fr","en","es","de","pt","it"]:
        lm = LANGS_META[l]
        path = links.get(l, f"{l}/index.html")
        ac = ' class="active"' if l==lang else ''
        items += f'<a href="/{path}" data-lang="{l}"{ac}>{lm["flag"]} {lm["lbl"]}</a>'
        mob += f'<a href="/{path}" data-lang="{l}"{ac}>{lm["flag"]} {lm["lbl"]}</a>'
    return (
        f'<div class="lang-switcher" id="langSwitcher"><button class="lang-btn" onclick="toggleLang(event)" aria-label="Language" aria-haspopup="true" aria-expanded="false">{m["flag"]} {m["lbl"]} <svg viewBox="0 0 10 6" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M1 1l4 4 4-4"/></svg></button><div class="lang-menu">{items}</div></div>',
        f'<div class="lang-mobile-wrap">{mob}</div>'
    )

def cookie(lang):
    txt, acc, dec = COOKIE[lang]
    return f"""<div id="cookieBanner" style="display:none;position:fixed;bottom:0;left:0;right:0;z-index:10000;background:var(--black2);border-top:1px solid var(--border);padding:1.2rem clamp(1.5rem,5vw,4rem);display:flex;align-items:center;justify-content:space-between;gap:1.5rem;flex-wrap:wrap;">
  <p style="font-size:0.78rem;color:var(--muted);line-height:1.6;max-width:600px;">{txt}</p>
  <div style="display:flex;gap:0.8rem;flex-shrink:0;">
    <button onclick="acceptCookies()" style="background:var(--gold);color:var(--black);border:none;padding:0.6rem 1.4rem;font-family:var(--sans);font-size:0.72rem;font-weight:500;letter-spacing:0.12em;text-transform:uppercase;cursor:pointer;min-height:44px;">{acc}</button>
    <button onclick="declineCookies()" style="background:transparent;color:var(--muted);border:1px solid var(--border);padding:0.6rem 1.4rem;font-family:var(--sans);font-size:0.72rem;letter-spacing:0.12em;text-transform:uppercase;cursor:pointer;min-height:44px;">{dec}</button>
  </div>
</div>"""

def nav_full(lang, hk):
    nl = NAV_LABELS[lang]
    sw, mob_sw = lang_widget(lang, hk)
    d = PROD_DIR[lang]
    pf = PROD_FILES[lang]
    ix = INDEX_FILES[lang]
    fond_file = HREFLANG["fondations"].get(lang,"").replace(lang+"/","")
    about_file = HREFLANG["about"].get(lang,"").replace(lang+"/","")
    faq_file = HREFLANG["faq"].get(lang,"").replace(lang+"/","")
    contact_file = HREFLANG["contact"].get(lang,"").replace(lang+"/","")
    booking_file = HREFLANG["booking"].get(lang,"").replace(lang+"/","")
    skip = {"fr":"Aller au contenu principal","en":"Skip to main content","es":"Ir al contenido principal","de":"Zum Hauptinhalt springen","pt":"Ir para o conteúdo principal","it":"Vai al contenuto principale"}[lang]
    return f"""<a href="#main" class="skip-link" style="position:absolute;top:-40px;left:0;padding:0.5rem 1rem;background:var(--gold);color:var(--black);font-family:var(--sans);font-size:0.75rem;z-index:9999;transition:top 0.3s;" onfocus="this.style.top='0'" onblur="this.style.top='-40px'">{skip}</a>
<nav id="mainNav" role="navigation" aria-label="Navigation principale">
  <a href="/{lang}/{ix}" class="nav-brand">Kemora Agency</a>
  <ul class="nav-links">
    <li><a href="/{lang}/{fond_file}">{nl['fond']}</a></li>
    <li><a href="/{lang}/{about_file}">{nl['about']}</a></li>
    <li class="nav-dropdown">
      <a href="/{lang}/{ix}#offre" aria-haspopup="true">
        {nl['offre']} <svg viewBox="0 0 10 6" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M1 1l4 4 4-4"/></svg>
      </a>
      <div class="dropdown-menu">
        <a href="/{lang}/{d}/{pf['cadre']}">{PROD_NAMES['cadre']}</a>
        <a href="/{lang}/{d}/{pf['exec']}">{PROD_NAMES['exec']}</a>
        <a href="/{lang}/{d}/{pf['core']}">{PROD_NAMES['core']}</a>
        <a href="/{lang}/{d}/{pf['biz']}">{PROD_NAMES['biz']}</a>
        <a href="/{lang}/{d}/{pf['kemora']}">{PROD_NAMES['kemora']}</a>
      </div>
    </li>
    <li><a href="/{lang}/{faq_file}">{nl['faq']}</a></li>
    <li><a href="/{lang}/{contact_file}">{nl['contact']}</a></li>
    <li><a href="/{lang}/{booking_file}" class="nav-cta">{nl['booking']}</a></li>
  </ul>
  {sw}
  <button class="nav-toggle" id="navToggle" aria-label="{nl['fond']}" aria-expanded="false" onclick="toggleMobileNav()">
    <span></span><span></span><span></span>
  </button>
</nav>
<div class="nav-mobile" id="navMobile">
  <a href="/{lang}/{fond_file}">{nl['fond']}</a>
  <a href="/{lang}/{about_file}">{nl['about']}</a>
  <a href="/{lang}/{d}/{pf['cadre']}">{PROD_NAMES['cadre']}</a>
  <a href="/{lang}/{d}/{pf['exec']}">{PROD_NAMES['exec']}</a>
  <a href="/{lang}/{d}/{pf['core']}">{PROD_NAMES['core']}</a>
  <a href="/{lang}/{d}/{pf['biz']}">{PROD_NAMES['biz']}</a>
  <a href="/{lang}/{d}/{pf['kemora']}">{PROD_NAMES['kemora']}</a>
  <a href="/{lang}/{faq_file}">{nl['faq']}</a>
  <a href="/{lang}/{contact_file}">{nl['contact']}</a>
  <a href="/{lang}/{booking_file}" class="mobile-cta">{nl['booking']}</a>
  {mob_sw}
</div>"""

def nav_back(lang, hk):
    nl = NAV_LABELS[lang]
    sw, _ = lang_widget(lang, hk)
    ix = INDEX_FILES[lang]
    skip = {"fr":"Aller au contenu principal","en":"Skip to main content","es":"Ir al contenido principal","de":"Zum Hauptinhalt springen","pt":"Ir para o conteúdo principal","it":"Vai al contenuto principale"}[lang]
    return f"""<a href="#main" class="skip-link" style="position:absolute;top:-40px;left:0;padding:0.5rem 1rem;background:var(--gold);color:var(--black);font-family:var(--sans);font-size:0.75rem;z-index:9999;transition:top 0.3s;" onfocus="this.style.top='0'" onblur="this.style.top='-40px'">{skip}</a>
<nav id="mainNav" role="navigation" aria-label="Navigation">
  <a href="/{lang}/{ix}" class="nav-brand">Kemora Agency</a>
  <a href="/{lang}/{ix}" class="nav-back" style="font-family:var(--sans);font-size:0.72rem;letter-spacing:0.16em;text-transform:uppercase;color:var(--muted);text-decoration:none;display:flex;align-items:center;gap:0.5rem;transition:color 0.3s;" onmouseover="this.style.color='var(--gold)'" onmouseout="this.style.color='var(--muted)'">
    <svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M10 12L6 8l4-4"/></svg>
    {nl['back']}
  </a>
  {sw}
</nav>"""

def footer_html(lang):
    legal_file = HREFLANG["legal"].get(lang,"").replace(lang+"/","")
    privacy_file = HREFLANG["privacy"].get(lang,"").replace(lang+"/","")
    contact_file = HREFLANG["contact"].get(lang,"").replace(lang+"/","")
    labels = {"fr":("Mentions légales","Politique de confidentialité","Contact"),
              "en":("Legal Notice","Privacy Policy","Contact"),
              "es":("Menciones Legales","Política de Privacidad","Contacto"),
              "de":("Impressum","Datenschutz","Kontakt"),
              "pt":("Menções Legais","Política de Privacidade","Contato"),
              "it":("Note Legali","Politica Privacy","Contatto")}[lang]
    return f"""<footer>
  <div class="footer-inner">
    <div class="footer-brand">Kemora Agency</div>
    <div class="footer-links">
      <a href="/{lang}/{legal_file}">{labels[0]}</a>
      <a href="/{lang}/{privacy_file}">{labels[1]}</a>
      <a href="/{lang}/{contact_file}">{labels[2]}</a>
    </div>
  </div>
  <div class="footer-copy">© 2026 Kemora Agency</div>
</footer>"""

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(path) else None
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  WROTE: {path}")

# ─────────────────────────────────────────────────────────────────────────────
# HOMEPAGE GENERATOR
# ─────────────────────────────────────────────────────────────────────────────

HOME_CONTENT = {
    "en": {
        "title": "Kemora Agency — Master AI. Automate. Unleash Your Potential.",
        "desc": "A premium digital ecosystem dedicated to AI, automation and intelligent growth systems. Five resources to transform your business.",
        "eyebrow": "AI Ecosystem",
        "h1": "Master AI and build a business that truly <em>frees you</em>",
        "sub": "Automate the ordinary. Build the extraordinary.",
        "cta1": "Book a Call", "cta2": "Discover Our Offer",
        "stat1_n":"5","stat1_l":"Resources in the ecosystem",
        "stat2_n":"100%","stat2_l":"Results-oriented",
        "stat3_n":"AI","stat3_l":"At the heart of every system",
        "stat4_n":"∞","stat4_l":"Scalability potential",
        "pres_label":"Kemora Agency",
        "pres_h2":"A premium <em>digital</em> ecosystem",
        "pres_p1":"Kemora Agency was created to answer a simple question: how to help entrepreneurs fully harness the potential of artificial intelligence — without getting lost in complexity, without wasting energy, and without waiting months to see real results.",
        "pres_p2":"Every resource, every system, every strategy is designed to produce real impact. No superfluous theory. Actionable tools.",
        "f1_h":"Premium training","f1_p":"Rigorous programmes on AI, automation and digital strategy — from foundation to expertise.",
        "f2_h":"Operational systems","f2_p":"Turn-key AI operating systems to structure your activity, automate processes and scale without depending on your time.",
        "f3_h":"Strategic support","f3_p":"An expert outside perspective to identify your growth levers and activate them as quickly as possible.",
        "f4_h":"Concrete, lasting impact","f4_p":"Every element is designed to generate measurable results — no vague promises, systems that work.",
        "meth_label":"The Kemora progression",
        "meth_h2":"Four pillars for an <em>intelligent</em> business",
        "meth_p":"A structured progression — from mental framework to the complete ecosystem — to build something that grows with you.",
        "m1_step":"Pillar 01","m1_h":"The mental framework","m1_p":"Before automating anything, you must adopt the right posture. Clarity, intention and architecture of thought — the foundations of everything that follows.",
        "m2_step":"Pillar 02","m2_h":"Execution","m2_p":"Strategies without execution are philosophy. We give you the systems to move from idea to action — in a repeatable way.",
        "m3_step":"Pillar 03","m3_h":"Automation","m3_p":"Delegate to AI what can be delegated. Build systems that work for you — day and night, without friction, without wasted energy.",
        "m4_step":"Pillar 04","m4_h":"The ecosystem","m4_p":"Assemble everything into a coherent, scalable system — a true operating system for your activity, designed to grow without exhausting you.",
        "offre_label":"The complete ecosystem",
        "offre_h2":"Five resources to <em>transform</em> your activity",
        "offre_p":"From first awareness to a fully structured AI ecosystem — a progression designed for every stage of your journey.",
        "c1_label":"Foundation level","c1_desc":"Adopt the posture and architecture of thought that precede any lasting transformation.",
        "c2_label":"Action level","c2_desc":"The systems to move from intention to action — in a structured, repeatable and effective way.",
        "c3_label":"Beginner level","c3_desc":"The foundations of an automated business: essential AI tools, 5 pillars and a 7-day action plan.",
        "c4_label":"Advanced level","c4_desc":"Advanced strategy, monetisation systems and deep automation for a solid and scalable business.",
        "c5_label":"Signature level","c5_desc":"The complete ecosystem — the most complete version of our method for a business entirely orchestrated by AI.",
        "c_disc":"Discover",
        "manifeste_text":'Artificial intelligence does not replace your ambition —<br>it <em>amplifies</em> what you have already decided to build.',
        "manifeste_author":"Kemora Agency — Manifesto",
        "cta_label":"Take action",
        "cta_h2":"Your business will not grow<br>because you work <em>harder</em>.",
        "cta_p":"It will grow because you will have built something capable of growing with you. Book a call to identify together the starting point that corresponds to your situation.",
        "cta_btn1":"Book a Call","cta_btn2":"Explore Our Offer",
        "featured_badge":"Signature",
    },
    "es": {
        "title": "Kemora Agency — Domine la IA. Automatice. Libere su potencial.",
        "desc": "Ecosistema digital premium dedicado a la IA, la automatización y los sistemas de crecimiento inteligentes. Cinco recursos para transformar su actividad.",
        "eyebrow": "Ecosistema IA",
        "h1": "Domine la IA y construya un negocio que le <em>libere</em>",
        "sub": "Automatice lo ordinario. Construya lo extraordinario.",
        "cta1": "Reservar Llamada", "cta2": "Descubrir la Oferta",
        "stat1_n":"5","stat1_l":"Recursos en el ecosistema",
        "stat2_n":"100%","stat2_l":"Orientado a resultados",
        "stat3_n":"IA","stat3_l":"En el corazón de cada sistema",
        "stat4_n":"∞","stat4_l":"Potencial de escalabilidad",
        "pres_label":"Kemora Agency",
        "pres_h2":"Un ecosistema digital <em>premium</em>",
        "pres_p1":"Kemora Agency fue creado para responder a una pregunta simple: cómo ayudar a los emprendedores a aprovechar al máximo el potencial de la inteligencia artificial — sin perderse en la complejidad, sin desperdiciar energía, y sin esperar meses para ver resultados concretos.",
        "pres_p2":"Cada recurso, cada sistema, cada estrategia está pensado para producir un impacto real. Sin teoría superflua. Herramientas accionables.",
        "f1_h":"Formaciones premium","f1_p":"Programas rigurosos sobre IA, automatización y estrategia digital — desde la fundación hasta la experiencia.",
        "f2_h":"Sistemas operativos","f2_p":"Sistemas operativos IA listos para usar que estructuran su actividad, automatizan procesos y escalan sin depender de su tiempo.",
        "f3_h":"Acompañamiento estratégico","f3_p":"Una perspectiva experta externa para identificar sus palancas de crecimiento y activarlas lo antes posible.",
        "f4_h":"Impacto concreto y duradero","f4_p":"Cada elemento está diseñado para generar resultados medibles — sin promesas vagas, sistemas que funcionan.",
        "meth_label":"La progresión Kemora",
        "meth_h2":"Cuatro pilares para un negocio <em>inteligente</em>",
        "meth_p":"Una progresión estructurada — del marco mental al ecosistema completo — para construir algo que crezca con usted.",
        "m1_step":"Pilar 01","m1_h":"El marco mental","m1_p":"Antes de automatizar cualquier cosa, debe adoptar la postura correcta. Claridad, intención y arquitectura del pensamiento — las bases de todo lo que sigue.",
        "m2_step":"Pilar 02","m2_h":"La ejecución","m2_p":"Las estrategias sin ejecución son filosofía. Le proporcionamos los sistemas para pasar de la idea a la acción — de forma repetible.",
        "m3_step":"Pilar 03","m3_h":"La automatización","m3_p":"Delegar en la IA lo que se pueda delegar. Construir sistemas que trabajen para usted — día y noche, sin fricción, sin pérdida de energía.",
        "m4_step":"Pilar 04","m4_h":"El ecosistema","m4_p":"Ensamblar todo en un sistema coherente y escalable — un verdadero sistema operativo de su actividad, diseñado para crecer sin agotarle.",
        "offre_label":"El ecosistema completo",
        "offre_h2":"Cinco recursos para <em>transformar</em> su actividad",
        "offre_p":"Desde la primera toma de conciencia hasta el ecosistema IA completamente estructurado — una progresión pensada para cada etapa de su camino.",
        "c1_label":"Nivel fundación","c1_desc":"Adopte la postura y la arquitectura del pensamiento que preceden a toda transformación duradera.",
        "c2_label":"Nivel acción","c2_desc":"Los sistemas para pasar de la intención a la acción — de forma estructurada, repetible y eficaz.",
        "c3_label":"Nivel principiante","c3_desc":"Los fundamentos de un negocio automatizado: herramientas IA esenciales, 5 pilares y un plan de acción de 7 días.",
        "c4_label":"Nivel avanzado","c4_desc":"Estrategia avanzada, sistemas de monetización y automatización profunda para un negocio sólido y escalable.",
        "c5_label":"Nivel firma","c5_desc":"El ecosistema completo — la versión más desarrollada de nuestro método para un negocio enteramente orquestado por la IA.",
        "c_disc":"Descubrir",
        "manifeste_text":'La inteligencia artificial no reemplaza su ambición —<br>la <em>amplifica</em> en lo que usted ya ha decidido construir.',
        "manifeste_author":"Kemora Agency — Manifiesto",
        "cta_label":"Pasar a la acción",
        "cta_h2":"Su negocio no crecerá<br>porque trabaje <em>más</em>.",
        "cta_p":"Crecerá porque habrá construido algo capaz de crecer con usted. Reserve una llamada para identificar juntos el punto de partida que corresponde a su situación.",
        "cta_btn1":"Reservar Llamada","cta_btn2":"Explorar la Oferta",
        "featured_badge":"Firma",
    },
    "de": {
        "title": "Kemora Agency — Beherrschen Sie KI. Automatisieren Sie. Entfalten Sie Ihr Potenzial.",
        "desc": "Ein erstklassiges digitales Ökosystem für KI, Automatisierung und intelligente Wachstumssysteme. Fünf Ressourcen, um Ihr Unternehmen zu transformieren.",
        "eyebrow": "KI-Ökosystem",
        "h1": "Beherrschen Sie KI und bauen Sie ein Unternehmen, das Sie <em>befreit</em>",
        "sub": "Automatisieren Sie das Gewöhnliche. Bauen Sie das Außergewöhnliche.",
        "cta1": "Anruf Buchen", "cta2": "Angebot Entdecken",
        "stat1_n":"5","stat1_l":"Ressourcen im Ökosystem",
        "stat2_n":"100%","stat2_l":"Ergebnisorientiert",
        "stat3_n":"KI","stat3_l":"Im Herzen jedes Systems",
        "stat4_n":"∞","stat4_l":"Skalierungspotenzial",
        "pres_label":"Kemora Agency",
        "pres_h2":"Ein erstklassiges digitales <em>Ökosystem</em>",
        "pres_p1":"Kemora Agency wurde entwickelt, um eine einfache Frage zu beantworten: Wie können Unternehmer das volle Potenzial der künstlichen Intelligenz nutzen — ohne sich in der Komplexität zu verlieren, ohne Energie zu verschwenden und ohne monatelang auf konkrete Ergebnisse zu warten.",
        "pres_p2":"Jede Ressource, jedes System, jede Strategie ist darauf ausgerichtet, echte Wirkung zu erzielen. Keine überflüssige Theorie. Umsetzbare Werkzeuge.",
        "f1_h":"Premium-Schulungen","f1_p":"Rigorose Programme zu KI, Automatisierung und digitaler Strategie — von den Grundlagen bis zur Expertise.",
        "f2_h":"Operative Systeme","f2_p":"Schlüsselfertige KI-Betriebssysteme zur Strukturierung Ihrer Tätigkeit, Automatisierung von Prozessen und Skalierung ohne Zeitabhängigkeit.",
        "f3_h":"Strategische Begleitung","f3_p":"Ein externer Expertenblick, um Ihre Wachstumshebel zu identifizieren und so schnell wie möglich zu aktivieren.",
        "f4_h":"Konkreter und dauerhafter Einfluss","f4_p":"Jedes Element ist darauf ausgelegt, messbare Ergebnisse zu erzielen — keine vagen Versprechen, Systeme die funktionieren.",
        "meth_label":"Die Kemora-Progression",
        "meth_h2":"Vier Säulen für ein <em>intelligentes</em> Unternehmen",
        "meth_p":"Eine strukturierte Progression — vom mentalen Rahmen bis zum vollständigen Ökosystem — um etwas aufzubauen, das mit Ihnen wächst.",
        "m1_step":"Säule 01","m1_h":"Der mentale Rahmen","m1_p":"Bevor Sie irgendetwas automatisieren, müssen Sie die richtige Haltung einnehmen. Klarheit, Absicht und Gedankenarchitektur — das Fundament für alles, was folgt.",
        "m2_step":"Säule 02","m2_h":"Die Ausführung","m2_p":"Strategien ohne Ausführung sind Philosophie. Wir geben Ihnen die Systeme, um von der Idee zur Aktion überzugehen — auf wiederholbare Weise.",
        "m3_step":"Säule 03","m3_h":"Die Automatisierung","m3_p":"Delegieren Sie an KI, was delegiert werden kann. Bauen Sie Systeme auf, die für Sie arbeiten — Tag und Nacht, ohne Reibung, ohne Energieverlust.",
        "m4_step":"Säule 04","m4_h":"Das Ökosystem","m4_p":"Alles zu einem kohärenten, skalierbaren System zusammenführen — ein echtes Betriebssystem für Ihre Tätigkeit, das wächst, ohne Sie zu erschöpfen.",
        "offre_label":"Das vollständige Ökosystem",
        "offre_h2":"Fünf Ressourcen, um Ihr Unternehmen zu <em>transformieren</em>",
        "offre_p":"Von der ersten Bewusstseinsbildung bis zum vollständig strukturierten KI-Ökosystem — eine Progression für jede Etappe Ihres Weges.",
        "c1_label":"Fundament-Ebene","c1_desc":"Nehmen Sie die Haltung und Gedankenarchitektur an, die jeder dauerhaften Transformation vorausgehen.",
        "c2_label":"Aktions-Ebene","c2_desc":"Die Systeme, um von der Absicht zur Aktion überzugehen — strukturiert, wiederholbar und effektiv.",
        "c3_label":"Einsteiger-Ebene","c3_desc":"Die Grundlagen eines automatisierten Unternehmens: wesentliche KI-Werkzeuge, 5 Säulen und ein 7-Tage-Aktionsplan.",
        "c4_label":"Fortgeschrittene Ebene","c4_desc":"Fortgeschrittene Strategie, Monetarisierungssysteme und tiefgehende Automatisierung für ein solides und skalierbares Unternehmen.",
        "c5_label":"Signatur-Ebene","c5_desc":"Das vollständige Ökosystem — die ausgefeilteste Version unserer Methode für ein vollständig von KI orchestriertes Unternehmen.",
        "c_disc":"Entdecken",
        "manifeste_text":'Künstliche Intelligenz ersetzt nicht Ihren Ehrgeiz —<br>sie <em>verstärkt</em>, was Sie bereits beschlossen haben aufzubauen.',
        "manifeste_author":"Kemora Agency — Manifest",
        "cta_label":"Handeln Sie jetzt",
        "cta_h2":"Ihr Unternehmen wird nicht wachsen,<br>weil Sie <em>mehr</em> arbeiten.",
        "cta_p":"Es wird wachsen, weil Sie etwas aufgebaut haben, das mit Ihnen wächst. Buchen Sie einen Anruf, um gemeinsam den Ausgangspunkt zu finden, der zu Ihrer Situation passt.",
        "cta_btn1":"Anruf Buchen","cta_btn2":"Angebot Erkunden",
        "featured_badge":"Signatur",
    },
    "pt": {
        "title": "Kemora Agency — Domine a IA. Automatize. Liberte o seu potencial.",
        "desc": "Ecossistema digital premium dedicado à IA, à automatização e aos sistemas de crescimento inteligentes. Cinco recursos para transformar a sua atividade.",
        "eyebrow": "Ecossistema IA",
        "h1": "Domine a IA e construa um negócio que o <em>liberte</em>",
        "sub": "Automatize o ordinário. Construa o extraordinário.",
        "cta1": "Reservar Chamada", "cta2": "Descobrir a Oferta",
        "stat1_n":"5","stat1_l":"Recursos no ecossistema",
        "stat2_n":"100%","stat2_l":"Orientado para resultados",
        "stat3_n":"IA","stat3_l":"No coração de cada sistema",
        "stat4_n":"∞","stat4_l":"Potencial de escalabilidade",
        "pres_label":"Kemora Agency",
        "pres_h2":"Um ecossistema digital <em>premium</em>",
        "pres_p1":"A Kemora Agency foi criada para responder a uma pergunta simples: como ajudar os empreendedores a aproveitar plenamente o potencial da inteligência artificial — sem se perderem na complexidade, sem desperdiçar energia, e sem esperar meses para ver resultados concretos.",
        "pres_p2":"Cada recurso, cada sistema, cada estratégia é concebido para produzir um impacto real. Sem teoria supérflua. Ferramentas acionáveis.",
        "f1_h":"Formações premium","f1_p":"Programas rigorosos sobre IA, automatização e estratégia digital — da fundação à especialização.",
        "f2_h":"Sistemas operacionais","f2_p":"Sistemas operacionais de IA prontos a usar para estruturar a sua atividade, automatizar processos e escalar sem depender do seu tempo.",
        "f3_h":"Acompanhamento estratégico","f3_p":"Um olhar externo especializado para identificar as suas alavancas de crescimento e ativá-las no menor prazo possível.",
        "f4_h":"Impacto concreto e duradouro","f4_p":"Cada elemento é concebido para gerar resultados mensuráveis — sem promessas vagas, sistemas que funcionam.",
        "meth_label":"A progressão Kemora",
        "meth_h2":"Quatro pilares para um negócio <em>inteligente</em>",
        "meth_p":"Uma progressão estruturada — do quadro mental ao ecossistema completo — para construir algo que cresce consigo.",
        "m1_step":"Pilar 01","m1_h":"O quadro mental","m1_p":"Antes de automatizar qualquer coisa, é preciso adotar a postura correta. Clareza, intenção e arquitetura do pensamento — os alicerces de tudo o que se segue.",
        "m2_step":"Pilar 02","m2_h":"A execução","m2_p":"As estratégias sem execução são filosofia. Fornecemos os sistemas para passar da ideia à ação — de forma repetível.",
        "m3_step":"Pilar 03","m3_h":"A automatização","m3_p":"Delegar à IA o que pode ser delegado. Construir sistemas que trabalhem por si — dia e noite, sem fricção, sem perda de energia.",
        "m4_step":"Pilar 04","m4_h":"O ecossistema","m4_p":"Reunir tudo num sistema coerente e escalável — um verdadeiro sistema operacional da sua atividade, concebido para crescer sem o esgotar.",
        "offre_label":"O ecossistema completo",
        "offre_h2":"Cinco recursos para <em>transformar</em> a sua atividade",
        "offre_p":"Desde a primeira tomada de consciência até ao ecossistema de IA completamente estruturado — uma progressão pensada para cada etapa do seu percurso.",
        "c1_label":"Nível fundação","c1_desc":"Adote a postura e a arquitetura do pensamento que precedem qualquer transformação duradoura.",
        "c2_label":"Nível ação","c2_desc":"Os sistemas para passar da intenção à ação — de forma estruturada, repetível e eficaz.",
        "c3_label":"Nível iniciante","c3_desc":"Os alicerces de um negócio automatizado: ferramentas de IA essenciais, 5 pilares e um plano de ação de 7 dias.",
        "c4_label":"Nível avançado","c4_desc":"Estratégia avançada, sistemas de monetização e automatização aprofundada para um negócio sólido e escalável.",
        "c5_label":"Nível assinatura","c5_desc":"O ecossistema completo — a versão mais desenvolvida do nosso método para um negócio inteiramente orquestrado pela IA.",
        "c_disc":"Descobrir",
        "manifeste_text":'A inteligência artificial não substitui a sua ambição —<br>ela <em>amplifica</em> o que você já decidiu construir.',
        "manifeste_author":"Kemora Agency — Manifesto",
        "cta_label":"Agir agora",
        "cta_h2":"O seu negócio não irá crescer<br>porque trabalha <em>mais</em>.",
        "cta_p":"Crescerá porque terá construído algo capaz de crescer consigo. Reserve uma chamada para identificar juntos o ponto de partida que corresponde à sua situação.",
        "cta_btn1":"Reservar Chamada","cta_btn2":"Explorar a Oferta",
        "featured_badge":"Assinatura",
    },
    "it": {
        "title": "Kemora Agency — Padroneggi l'IA. Automatizzi. Liberi il suo potenziale.",
        "desc": "Ecosistema digitale premium dedicato all'IA, all'automatizzazione e ai sistemi di crescita intelligenti. Cinque risorse per trasformare la Sua attività.",
        "eyebrow": "Ecosistema IA",
        "h1": "Padroneggi l'IA e costruisca un'attività che la <em>liberi</em>",
        "sub": "Automatizzi l'ordinario. Costruisca lo straordinario.",
        "cta1": "Prenota una Chiamata", "cta2": "Scopri l'Offerta",
        "stat1_n":"5","stat1_l":"Risorse nell'ecosistema",
        "stat2_n":"100%","stat2_l":"Orientato ai risultati",
        "stat3_n":"IA","stat3_l":"Al cuore di ogni sistema",
        "stat4_n":"∞","stat4_l":"Potenziale di scalabilità",
        "pres_label":"Kemora Agency",
        "pres_h2":"Un ecosistema digitale <em>premium</em>",
        "pres_p1":"Kemora Agency è stata concepita per rispondere a una domanda semplice: come aiutare gli imprenditori a sfruttare appieno il potenziale dell'intelligenza artificiale — senza perdersi nella complessità, senza sprecare energia, e senza aspettare mesi per vedere risultati concreti.",
        "pres_p2":"Ogni risorsa, ogni sistema, ogni strategia è pensato per produrre un impatto reale. Nessuna teoria superflua. Strumenti pratici e applicabili.",
        "f1_h":"Formazioni premium","f1_p":"Programmi rigorosi su IA, automatizzazione e strategia digitale — dalle fondamenta all'expertise.",
        "f2_h":"Sistemi operativi","f2_p":"Sistemi operativi IA chiavi in mano per strutturare la Sua attività, automatizzare i processi e scalare senza dipendere dal Suo tempo.",
        "f3_h":"Accompagnamento strategico","f3_p":"Uno sguardo esperto esterno per identificare le Sue leve di crescita e attivarle nei tempi migliori.",
        "f4_h":"Impatto concreto e duraturo","f4_p":"Ogni elemento è progettato per generare risultati misurabili — nessuna promessa vaga, sistemi che funzionano.",
        "meth_label":"La progressione Kemora",
        "meth_h2":"Quattro pilastri per un'attività <em>intelligente</em>",
        "meth_p":"Una progressione strutturata — dal quadro mentale all'ecosistema completo — per costruire qualcosa che cresca con Lei.",
        "m1_step":"Pilastro 01","m1_h":"Il quadro mentale","m1_p":"Prima di automatizzare qualsiasi cosa, bisogna adottare la postura giusta. Chiarezza, intenzione e architettura del pensiero — le fondamenta di tutto ciò che segue.",
        "m2_step":"Pilastro 02","m2_h":"L'esecuzione","m2_p":"Le strategie senza esecuzione sono filosofia. Le forniamo i sistemi per passare dall'idea all'azione — in modo ripetibile.",
        "m3_step":"Pilastro 03","m3_h":"L'automatizzazione","m3_p":"Delegare all'IA ciò che può essere delegato. Costruire sistemi che lavorino per Lei — giorno e notte, senza attrito, senza perdita di energia.",
        "m4_step":"Pilastro 04","m4_h":"L'ecosistema","m4_p":"Assemblare tutto in un sistema coerente e scalabile — un vero sistema operativo della Sua attività, progettato per crescere senza esaurirla.",
        "offre_label":"L'ecosistema completo",
        "offre_h2":"Cinque risorse per <em>trasformare</em> la Sua attività",
        "offre_p":"Dalla prima presa di coscienza all'ecosistema IA completamente strutturato — una progressione pensata per ogni tappa del Suo percorso.",
        "c1_label":"Livello fondazione","c1_desc":"Adotti la postura e l'architettura del pensiero che precedono qualsiasi trasformazione duratura.",
        "c2_label":"Livello azione","c2_desc":"I sistemi per passare dall'intenzione all'azione — in modo strutturato, ripetibile ed efficace.",
        "c3_label":"Livello principiante","c3_desc":"Le fondamenta di un'attività automatizzata: strumenti IA essenziali, 5 pilastri e un piano d'azione di 7 giorni.",
        "c4_label":"Livello avanzato","c4_desc":"Strategia avanzata, sistemi di monetizzazione e automatizzazione approfondita per un'attività solida e scalabile.",
        "c5_label":"Livello firma","c5_desc":"L'ecosistema completo — la versione più compiuta del nostro metodo per un'attività interamente orchestrata dall'IA.",
        "c_disc":"Scoprire",
        "manifeste_text":"L'intelligenza artificiale non sostituisce la Sua ambizione —<br>la <em>amplifica</em> in ciò che ha già deciso di costruire.",
        "manifeste_author":"Kemora Agency — Manifesto",
        "cta_label":"Passare all'azione",
        "cta_h2":"La Sua attività non crescerà<br>perché lavora <em>di più</em>.",
        "cta_p":"Crescerà perché avrà costruito qualcosa capace di crescere con Lei. Prenoti una chiamata per identificare insieme il punto di partenza che corrisponde alla Sua situazione.",
        "cta_btn1":"Prenota una Chiamata","cta_btn2":"Esplora l'Offerta",
        "featured_badge":"Firma",
    },
}

def make_homepage(lang):
    c = HOME_CONTENT[lang]
    nl = NAV_LABELS[lang]
    d = PROD_DIR[lang]
    pf = PROD_FILES[lang]
    booking_file = HREFLANG["booking"].get(lang,"").replace(lang+"/","")
    nav = nav_full(lang, "index")
    sw_widget, _ = lang_widget(lang, "index")

    svg_arrow = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>'
    org_schema = '{"@context":"https://schema.org","@type":"Organization","name":"Kemora Agency","url":"https://kemora-agency.com","description":"Premium digital ecosystem dedicated to AI, automation and intelligent growth systems.","logo":"https://kemora-agency.com/assets/favicon/apple-touch-icon.png","sameAs":[]}'

    html = head(lang, c["title"], c["desc"], "index.html", "index", "/assets/images/Accueil.webp")
    html += f"""
<style>
{BASE_CSS}
{NAV_CSS}
  #hero {{ min-height:100vh; display:grid; grid-template-columns:1fr 1fr; padding-top:72px; position:relative; overflow:hidden; }}
  .hero-left {{ display:flex; align-items:center; padding:clamp(3rem,8vw,6rem) clamp(1.5rem,4vw,5rem) clamp(3rem,8vw,6rem) clamp(1.5rem,5vw,5rem); position:relative; z-index:2; }}
  .hero-left-inner {{ max-width:520px; }}
  .hero-eyebrow {{ display:flex; align-items:center; gap:1rem; margin-bottom:2rem; animation:heroFadeUp 0.8s var(--ease) 0.2s both; }}
  .hero-eyebrow-line {{ width:36px; height:1px; background:var(--gold); flex-shrink:0; }}
  .hero-title {{ margin-bottom:1.8rem; color:var(--white); animation:heroFadeUp 0.8s var(--ease) 0.35s both; }}
  .hero-subtitle {{ color:var(--muted); font-size:clamp(0.9rem,1.5vw,1.05rem); margin-bottom:2.8rem; line-height:1.9; animation:heroFadeUp 0.8s var(--ease) 0.5s both; }}
  .hero-cta {{ display:flex; align-items:center; gap:1.2rem; flex-wrap:wrap; animation:heroFadeUp 0.8s var(--ease) 0.65s both; }}
  .hero-right {{ position:relative; overflow:hidden; }}
  .hero-right img {{ position:absolute; inset:0; width:100%; height:100%; object-fit:cover; }}
  .hero-right::after {{ content:''; position:absolute; inset:0; background:linear-gradient(to right,var(--black) 0%,rgba(5,5,5,0.15) 40%,transparent 100%),linear-gradient(to top,rgba(5,5,5,0.5) 0%,transparent 40%); }}
  .hero-right::before {{ content:''; position:absolute; inset:0; background:rgba(5,5,5,0.3); z-index:1; }}
  .hero-bg-glow {{ position:absolute; left:-200px; top:50%; transform:translateY(-50%); width:600px; height:600px; background:radial-gradient(ellipse,rgba(198,161,110,0.05) 0%,transparent 65%); pointer-events:none; }}
  @keyframes heroFadeUp {{ from {{ opacity:0; transform:translateY(32px); }} to {{ opacity:1; transform:translateY(0); }} }}
  #stats {{ padding:2.8rem 0; background:var(--black2); border-top:1px solid var(--border2); border-bottom:1px solid var(--border2); }}
  .stats-grid {{ display:grid; grid-template-columns:repeat(4,1fr); gap:1px; }}
  .stat-item {{ text-align:center; padding:1.2rem 1rem; position:relative; }}
  .stat-item:not(:last-child)::after {{ content:''; position:absolute; right:0; top:20%; bottom:20%; width:1px; background:var(--border2); }}
  .stat-num {{ font-family:var(--serif); font-size:clamp(2rem,3.5vw,2.8rem); font-weight:300; color:var(--gold); line-height:1; }}
  .stat-label {{ font-size:0.65rem; letter-spacing:0.2em; text-transform:uppercase; color:var(--muted); margin-top:0.4rem; }}
  #presentation {{ position:relative; }}
  .pres-bg {{ position:absolute; inset:0; background:radial-gradient(ellipse 55% 55% at 80% 50%,rgba(198,161,110,0.04),transparent); pointer-events:none; }}
  .pres-grid {{ display:grid; grid-template-columns:0.9fr 1.1fr; gap:6rem; align-items:center; position:relative; z-index:1; }}
  .pres-left .label {{ display:block; margin-bottom:1.5rem; }}
  .pres-left h2 {{ margin-bottom:2rem; color:var(--gold); }}
  .pres-left .pres-line {{ width:48px; height:1px; background:var(--gold); margin-bottom:2rem; }}
  .pres-left p {{ color:var(--muted); line-height:1.95; font-size:clamp(0.9rem,1.4vw,1.02rem); }}
  .pres-right {{ display:flex; flex-direction:column; gap:0; border:1px solid var(--border2); }}
  .pres-feature {{ padding:1.8rem 2rem; border-bottom:1px solid var(--border2); transition:background 0.3s; display:flex; align-items:flex-start; gap:1.4rem; }}
  .pres-feature:last-child {{ border-bottom:none; }}
  .pres-feature:hover {{ background:rgba(198,161,110,0.02); }}
  .pres-feature-num {{ font-family:var(--serif); font-size:1.8rem; font-weight:300; color:rgba(198,161,110,0.2); line-height:1; flex-shrink:0; min-width:2rem; }}
  .pres-feature-body h3 {{ font-family:var(--sans); font-size:0.78rem; letter-spacing:0.14em; text-transform:uppercase; color:var(--white); font-weight:400; margin-bottom:0.35rem; }}
  .pres-feature-body p {{ font-size:0.82rem; color:var(--muted); line-height:1.75; }}
  #methode {{ background:var(--black2); }}
  .methode-header {{ text-align:center; max-width:620px; margin:0 auto 4.5rem; }}
  .methode-header .label {{ display:block; margin-bottom:1.2rem; }}
  .methode-header h2 {{ margin-bottom:1.2rem; color:var(--gold); }}
  .methode-header p {{ color:var(--muted); }}
  .methode-grid {{ display:grid; grid-template-columns:repeat(4,1fr); gap:1px; border:1px solid var(--border2); }}
  .methode-card {{ padding:2.8rem 2rem; background:var(--black); position:relative; overflow:hidden; transition:background 0.3s; }}
  .methode-card::before {{ content:''; position:absolute; top:0; left:0; right:0; height:2px; background:linear-gradient(to right,var(--gold-dim),var(--gold)); transform:scaleX(0); transform-origin:left; transition:transform 0.4s var(--ease); }}
  .methode-card:hover {{ background:rgba(198,161,110,0.015); }}
  .methode-card:hover::before {{ transform:scaleX(1); }}
  .methode-icon {{ width:44px; height:44px; border:1px solid var(--border); display:flex; align-items:center; justify-content:center; margin-bottom:1.8rem; }}
  .methode-icon svg {{ width:20px; height:20px; color:var(--gold); stroke:currentColor; fill:none; stroke-width:1.2; }}
  .methode-step {{ font-size:0.58rem; letter-spacing:0.2em; text-transform:uppercase; color:var(--gold); margin-bottom:0.8rem; }}
  .methode-card h3 {{ font-family:var(--serif); font-size:1.3rem; color:var(--white); margin-bottom:0.8rem; }}
  .methode-card p {{ font-size:0.82rem; color:var(--muted); line-height:1.8; }}
  #offre {{ position:relative; }}
  .offre-header {{ text-align:center; max-width:620px; margin:0 auto 4.5rem; }}
  .offre-header .label {{ display:block; margin-bottom:1.2rem; }}
  .offre-header h2 {{ margin-bottom:1.2rem; color:var(--gold); }}
  .offre-header p {{ color:var(--muted); }}
  .offre-grid {{ display:grid; grid-template-columns:repeat(3,1fr); gap:1px; border:1px solid var(--border2); }}
  .offre-grid .offre-card:nth-child(4) {{ grid-column:1/2; }}
  .offre-grid .offre-card:nth-child(5) {{ grid-column:2/3; }}
  .offre-card {{ background:var(--black); position:relative; overflow:hidden; display:flex; flex-direction:column; transition:background 0.4s; cursor:pointer; text-decoration:none; }}
  .offre-card:hover {{ background:rgba(198,161,110,0.02); }}
  .offre-card-img {{ width:100%; height:220px; overflow:hidden; position:relative; }}
  .offre-card-img img {{ width:100%; height:100%; object-fit:cover; transition:transform 0.6s var(--ease); filter:brightness(0.75) saturate(0.8); }}
  .offre-card:hover .offre-card-img img {{ transform:scale(1.04); filter:brightness(0.85) saturate(1); }}
  .offre-card-img::after {{ content:''; position:absolute; inset:0; background:linear-gradient(to bottom,transparent 40%,rgba(5,5,5,0.8) 100%); }}
  .offre-card-body {{ padding:1.8rem; flex:1; display:flex; flex-direction:column; gap:0.6rem; border-top:1px solid var(--border2); }}
  .offre-card-label {{ font-size:0.58rem; letter-spacing:0.2em; text-transform:uppercase; color:var(--gold); }}
  .offre-card-title {{ font-family:var(--serif); font-size:1.35rem; color:var(--gold); line-height:1.2; }}
  .offre-card-desc {{ font-size:0.8rem; color:var(--muted); line-height:1.75; flex:1; }}
  .offre-card-footer {{ display:flex; align-items:center; justify-content:space-between; padding-top:1rem; border-top:1px solid var(--border2); margin-top:auto; }}
  .offre-card-price {{ font-family:var(--serif); font-size:1.5rem; color:var(--gold); }}
  .offre-card-arrow {{ font-size:0.65rem; letter-spacing:0.16em; text-transform:uppercase; color:var(--muted); display:flex; align-items:center; gap:0.5rem; transition:color 0.3s; }}
  .offre-card:hover .offre-card-arrow {{ color:var(--gold); }}
  .offre-card-arrow svg {{ width:14px; height:14px; stroke:currentColor; fill:none; stroke-width:1.5; }}
  .offre-card.featured .offre-card-img::before {{ content:'{c["featured_badge"]}'; position:absolute; top:1rem; right:1rem; z-index:2; font-size:0.58rem; letter-spacing:0.18em; text-transform:uppercase; color:var(--black); background:var(--gold); padding:0.25rem 0.7rem; }}
  #manifeste {{ background:var(--black2); position:relative; overflow:hidden; }}
  .manifeste-bg {{ position:absolute; inset:0; background:radial-gradient(ellipse 70% 70% at 50% 50%,rgba(198,161,110,0.04),transparent); }}
  .manifeste-inner {{ position:relative; z-index:1; max-width:820px; margin:0 auto; text-align:center; }}
  .manifeste-mark {{ font-family:var(--serif); font-size:clamp(5rem,10vw,8rem); color:rgba(198,161,110,0.1); line-height:0.8; }}
  .manifeste-text {{ font-family:var(--serif); font-size:clamp(1.5rem,3.5vw,2.4rem); font-weight:300; line-height:1.45; color:var(--gold); margin-top:-0.5rem; }}
  .manifeste-author {{ margin-top:2.5rem; font-size:0.68rem; letter-spacing:0.22em; text-transform:uppercase; color:var(--muted); }}
  #cta-final {{ position:relative; overflow:hidden; text-align:center; }}
  .cta-final-bg {{ position:absolute; inset:0; background:radial-gradient(ellipse 60% 70% at 50% 50%,rgba(198,161,110,0.05),transparent); }}
  .cta-final-inner {{ position:relative; z-index:1; max-width:680px; margin:0 auto; }}
  .cta-final-inner .label {{ display:block; margin-bottom:1.5rem; }}
  .cta-final-inner h2 {{ margin-bottom:1.5rem; color:var(--gold); }}
  .cta-final-inner p {{ color:var(--muted); margin-bottom:2.8rem; line-height:1.9; font-size:clamp(0.9rem,1.5vw,1.05rem); }}
  .cta-final-buttons {{ display:flex; gap:1.2rem; justify-content:center; flex-wrap:wrap; }}
  @media (max-width:960px) {{
    #hero {{ grid-template-columns:1fr; }}
    .hero-right {{ height:45vw; min-height:260px; }}
    .stats-grid {{ grid-template-columns:repeat(2,1fr); }}
    .stat-item:nth-child(2)::after {{ display:none; }}
    .pres-grid {{ grid-template-columns:1fr; gap:3rem; }}
    .methode-grid {{ grid-template-columns:repeat(2,1fr); }}
    .offre-grid {{ grid-template-columns:1fr; }}
    .offre-grid .offre-card:nth-child(4),.offre-grid .offre-card:nth-child(5) {{ grid-column:auto; }}
  }}
  @media (max-width:600px) {{
    .stats-grid {{ grid-template-columns:1fr 1fr; }}
    .methode-grid {{ grid-template-columns:1fr; }}
  }}
</style>
<script type="application/ld+json">{org_schema}</script>
</head>
<body id="main">
{nav}

<section id="hero">
  <div class="hero-bg-glow"></div>
  <div class="hero-left">
    <div class="hero-left-inner">
      <div class="hero-eyebrow">
        <div class="hero-eyebrow-line"></div>
        <span class="label">{c["eyebrow"]}</span>
      </div>
      <h1 class="hero-title">{c["h1"]}</h1>
      <p class="hero-subtitle">{c["sub"]}</p>
      <div class="hero-cta">
        <a href="/{lang}/{booking_file}" class="btn-gold">{c["cta1"]}</a>
        <a href="#offre" class="btn-outline">{c["cta2"]}</a>
      </div>
    </div>
  </div>
  <div class="hero-right">
    <img src="/assets/images/Accueil.webp" alt="Kemora Agency — workspace" fetchpriority="high" width="960" height="1080">
  </div>
</section>

<div id="stats">
  <div class="container">
    <div class="stats-grid">
      <div class="stat-item reveal"><div class="stat-num">{c["stat1_n"]}</div><div class="stat-label">{c["stat1_l"]}</div></div>
      <div class="stat-item reveal reveal-delay-1"><div class="stat-num">{c["stat2_n"]}</div><div class="stat-label">{c["stat2_l"]}</div></div>
      <div class="stat-item reveal reveal-delay-2"><div class="stat-num">{c["stat3_n"]}</div><div class="stat-label">{c["stat3_l"]}</div></div>
      <div class="stat-item reveal reveal-delay-3"><div class="stat-num">{c["stat4_n"]}</div><div class="stat-label">{c["stat4_l"]}</div></div>
    </div>
  </div>
</div>

<section id="presentation" class="section">
  <div class="pres-bg"></div>
  <div class="container">
    <div class="pres-grid">
      <div class="pres-left">
        <span class="label reveal">{c["pres_label"]}</span>
        <h2 class="reveal reveal-delay-1">{c["pres_h2"]}</h2>
        <div class="pres-line reveal reveal-delay-1"></div>
        <p class="reveal reveal-delay-2">{c["pres_p1"]}</p>
        <p class="reveal reveal-delay-2" style="margin-top:1.2rem">{c["pres_p2"]}</p>
      </div>
      <div class="pres-right reveal reveal-delay-1">
        <div class="pres-feature"><span class="pres-feature-num">01</span><div class="pres-feature-body"><h3>{c["f1_h"]}</h3><p>{c["f1_p"]}</p></div></div>
        <div class="pres-feature"><span class="pres-feature-num">02</span><div class="pres-feature-body"><h3>{c["f2_h"]}</h3><p>{c["f2_p"]}</p></div></div>
        <div class="pres-feature"><span class="pres-feature-num">03</span><div class="pres-feature-body"><h3>{c["f3_h"]}</h3><p>{c["f3_p"]}</p></div></div>
        <div class="pres-feature"><span class="pres-feature-num">04</span><div class="pres-feature-body"><h3>{c["f4_h"]}</h3><p>{c["f4_p"]}</p></div></div>
      </div>
    </div>
  </div>
</section>

<div class="divider-h container"></div>

<section id="methode" class="section">
  <div class="container">
    <div class="methode-header">
      <span class="label reveal">{c["meth_label"]}</span>
      <h2 class="reveal reveal-delay-1">{c["meth_h2"]}</h2>
      <p class="reveal reveal-delay-2">{c["meth_p"]}</p>
    </div>
    <div class="methode-grid">
      <div class="methode-card reveal">
        <div class="methode-icon"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M12 1v4M12 19v4M4.22 4.22l2.83 2.83M16.95 16.95l2.83 2.83M1 12h4M19 12h4M4.22 19.78l2.83-2.83M16.95 7.05l2.83-2.83"/></svg></div>
        <div class="methode-step">{c["m1_step"]}</div><h3>{c["m1_h"]}</h3><p>{c["m1_p"]}</p>
      </div>
      <div class="methode-card reveal reveal-delay-1">
        <div class="methode-icon"><svg viewBox="0 0 24 24"><polyline points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg></div>
        <div class="methode-step">{c["m2_step"]}</div><h3>{c["m2_h"]}</h3><p>{c["m2_p"]}</p>
      </div>
      <div class="methode-card reveal reveal-delay-2">
        <div class="methode-icon"><svg viewBox="0 0 24 24"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg></div>
        <div class="methode-step">{c["m3_step"]}</div><h3>{c["m3_h"]}</h3><p>{c["m3_p"]}</p>
      </div>
      <div class="methode-card reveal reveal-delay-3">
        <div class="methode-icon"><svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
        <div class="methode-step">{c["m4_step"]}</div><h3>{c["m4_h"]}</h3><p>{c["m4_p"]}</p>
      </div>
    </div>
  </div>
</section>

<section id="offre" class="section">
  <div class="container">
    <div class="offre-header">
      <span class="label reveal">{c["offre_label"]}</span>
      <h2 class="reveal reveal-delay-1">{c["offre_h2"]}</h2>
      <p class="reveal reveal-delay-2">{c["offre_p"]}</p>
    </div>
    <div class="offre-grid">
      <a href="/{lang}/{d}/{pf['cadre']}" class="offre-card reveal">
        <div class="offre-card-img"><img src="/assets/images/le_cadremental.webp" alt="{PROD_NAMES['cadre']}" loading="lazy" width="400" height="220"></div>
        <div class="offre-card-body">
          <span class="offre-card-label">{c["c1_label"]}</span>
          <div class="offre-card-title">{PROD_NAMES['cadre']}</div>
          <p class="offre-card-desc">{c["c1_desc"]}</p>
          <div class="offre-card-footer"><span class="offre-card-price">37 €</span><span class="offre-card-arrow">{c["c_disc"]} {svg_arrow}</span></div>
        </div>
      </a>
      <a href="/{lang}/{d}/{pf['exec']}" class="offre-card reveal reveal-delay-1">
        <div class="offre-card-img"><img src="/assets/images/lexecution.webp" alt="{PROD_NAMES['exec']}" loading="lazy" width="400" height="220"></div>
        <div class="offre-card-body">
          <span class="offre-card-label">{c["c2_label"]}</span>
          <div class="offre-card-title">{PROD_NAMES['exec']}</div>
          <p class="offre-card-desc">{c["c2_desc"]}</p>
          <div class="offre-card-footer"><span class="offre-card-price">37 €</span><span class="offre-card-arrow">{c["c_disc"]} {svg_arrow}</span></div>
        </div>
      </a>
      <a href="/{lang}/{d}/{pf['core']}" class="offre-card reveal reveal-delay-2">
        <div class="offre-card-img"><img src="/assets/images/coreosia.webp" alt="{PROD_NAMES['core']}" loading="lazy" width="400" height="220"></div>
        <div class="offre-card-body">
          <span class="offre-card-label">{c["c3_label"]}</span>
          <div class="offre-card-title">{PROD_NAMES['core']}</div>
          <p class="offre-card-desc">{c["c3_desc"]}</p>
          <div class="offre-card-footer"><span class="offre-card-price">97 €</span><span class="offre-card-arrow">{c["c_disc"]} {svg_arrow}</span></div>
        </div>
      </a>
      <a href="/{lang}/{d}/{pf['biz']}" class="offre-card reveal reveal-delay-1">
        <div class="offre-card-img"><img src="/assets/images/businessosia.webp" alt="{PROD_NAMES['biz']}" loading="lazy" width="400" height="220"></div>
        <div class="offre-card-body">
          <span class="offre-card-label">{c["c4_label"]}</span>
          <div class="offre-card-title">{PROD_NAMES['biz']}</div>
          <p class="offre-card-desc">{c["c4_desc"]}</p>
          <div class="offre-card-footer"><span class="offre-card-price">230 €</span><span class="offre-card-arrow">{c["c_disc"]} {svg_arrow}</span></div>
        </div>
      </a>
      <a href="/{lang}/{d}/{pf['kemora']}" class="offre-card featured reveal reveal-delay-2">
        <div class="offre-card-img"><img src="/assets/images/kemoraosia.webp" alt="{PROD_NAMES['kemora']}" loading="lazy" width="400" height="220"></div>
        <div class="offre-card-body">
          <span class="offre-card-label">{c["c5_label"]}</span>
          <div class="offre-card-title">{PROD_NAMES['kemora']}</div>
          <p class="offre-card-desc">{c["c5_desc"]}</p>
          <div class="offre-card-footer"><span class="offre-card-price">347 €</span><span class="offre-card-arrow">{c["c_disc"]} {svg_arrow}</span></div>
        </div>
      </a>
    </div>
  </div>
</section>

<section id="manifeste" class="section">
  <div class="manifeste-bg"></div>
  <div class="container">
    <div class="manifeste-inner">
      <div class="manifeste-mark reveal">&ldquo;</div>
      <div class="manifeste-text reveal reveal-delay-1">{c["manifeste_text"]}</div>
      <div class="manifeste-author reveal reveal-delay-2">{c["manifeste_author"]}</div>
    </div>
  </div>
</section>

<section id="cta-final" class="section">
  <div class="cta-final-bg"></div>
  <div class="container">
    <div class="cta-final-inner">
      <span class="label reveal">{c["cta_label"]}</span>
      <h2 class="reveal reveal-delay-1">{c["cta_h2"]}</h2>
      <p class="reveal reveal-delay-2">{c["cta_p"]}</p>
      <div class="cta-final-buttons reveal reveal-delay-3">
        <a href="/{lang}/{booking_file}" class="btn-gold">{c["cta_btn1"]}</a>
        <a href="#offre" class="btn-outline">{c["cta_btn2"]}</a>
      </div>
    </div>
  </div>
</section>

{footer_html(lang)}
{cookie(lang)}
{COMMON_JS}
<script>
function toggleMobileNav(){{var btn=document.getElementById('navToggle');var menu=document.getElementById('navMobile');btn.classList.toggle('open');menu.classList.toggle('open');btn.setAttribute('aria-expanded',menu.classList.contains('open'));}}
document.querySelectorAll('a[href^="#"]').forEach(function(a){{a.addEventListener('click',function(e){{var t=document.querySelector(a.getAttribute('href'));if(t){{e.preventDefault();t.scrollIntoView({{behavior:'smooth'}});document.getElementById('navToggle').classList.remove('open');document.getElementById('navMobile').classList.remove('open');}}}});}});
</script>
</body>
</html>"""
    return html

# Write homepages
for lang in ["en","es","de","pt","it"]:
    write(f"{lang}/index.html", make_homepage(lang))

print("Homepages done.")

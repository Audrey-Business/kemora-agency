#!/usr/bin/env python3
"""Generate sitemap-index.xml + per-language sitemaps."""
import os
from datetime import date

SITE_URL = "https://kemora-agency.com"
TODAY = date.today().isoformat()

PAGES = {
    "fr": [
        "fr/index.html","fr/fondations.html","fr/a-propos.html","fr/faq.html",
        "fr/contact.html","fr/reserver-appel.html","fr/mentions-legales.html",
        "fr/politique-confidentialite.html","fr/merci-cadre-mental.html","fr/merci-execution.html",
        "fr/merci-core-os-ia.html","fr/merci-business-os-ia.html","fr/merci-kemora-os-ia.html",
        "fr/produits/le-cadre-mental.html","fr/produits/lexecution.html",
        "fr/produits/core-os-ia.html","fr/produits/business-os-ia.html","fr/produits/kemora-os-ia.html",
    ],
    "en": [
        "en/index.html","en/foundations.html","en/about.html","en/faq.html",
        "en/contact.html","en/book-a-call.html","en/legal-notice.html","en/privacy-policy.html",
        "en/thank-you-mental-framework.html","en/thank-you-execution.html",
        "en/thank-you-core-os-ai.html","en/thank-you-business-os-ai.html","en/thank-you-kemora-os-ai.html",
        "en/products/the-mental-framework.html","en/products/execution.html",
        "en/products/core-os-ai.html","en/products/business-os-ai.html","en/products/kemora-os-ai.html",
    ],
    "es": [
        "es/index.html","es/fundaciones.html","es/sobre-nosotros.html","es/preguntas-frecuentes.html",
        "es/contacto.html","es/reservar-llamada.html","es/menciones-legales.html","es/politica-privacidad.html",
        "es/gracias-marco-mental.html","es/gracias-ejecucion.html",
        "es/gracias-core-os-ia.html","es/gracias-business-os-ia.html","es/gracias-kemora-os-ia.html",
        "es/productos/el-marco-mental.html","es/productos/la-ejecucion.html",
        "es/productos/core-os-ia.html","es/productos/business-os-ia.html","es/productos/kemora-os-ia.html",
    ],
    "de": [
        "de/index.html","de/grundlagen.html","de/ueber-uns.html","de/haeufige-fragen.html",
        "de/kontakt.html","de/anruf-buchen.html","de/impressum.html","de/datenschutz.html",
        "de/danke-mentaler-rahmen.html","de/danke-ausfuehrung.html",
        "de/danke-core-os-ki.html","de/danke-business-os-ki.html","de/danke-kemora-os-ki.html",
        "de/produkte/der-mentale-rahmen.html","de/produkte/die-ausfuehrung.html",
        "de/produkte/core-os-ki.html","de/produkte/business-os-ki.html","de/produkte/kemora-os-ki.html",
    ],
    "pt": [
        "pt/index.html","pt/fundacoes.html","pt/sobre-nos.html","pt/perguntas-frequentes.html",
        "pt/contato.html","pt/reservar-chamada.html","pt/mencoes-legais.html","pt/politica-privacidade.html",
        "pt/obrigado-quadro-mental.html","pt/obrigado-execucao.html",
        "pt/obrigado-core-os-ia.html","pt/obrigado-business-os-ia.html","pt/obrigado-kemora-os-ia.html",
        "pt/produtos/o-quadro-mental.html","pt/produtos/a-execucao.html",
        "pt/produtos/core-os-ia.html","pt/produtos/business-os-ia.html","pt/produtos/kemora-os-ia.html",
    ],
    "it": [
        "it/index.html","it/fondamenta.html","it/chi-siamo.html","it/domande-frequenti.html",
        "it/contatto.html","it/prenota-chiamata.html","it/note-legali.html","it/politica-privacy.html",
        "it/grazie-quadro-mentale.html","it/grazie-esecuzione.html",
        "it/grazie-core-os-ia.html","it/grazie-business-os-ia.html","it/grazie-kemora-os-ia.html",
        "it/prodotti/il-quadro-mentale.html","it/prodotti/lesecuzione.html",
        "it/prodotti/core-os-ia.html","it/prodotti/business-os-ia.html","it/prodotti/kemora-os-ia.html",
    ],
}

PRIORITY = {
    "index.html":"1.0",
    "le-cadre-mental.html":"0.9","lexecution.html":"0.9","core-os-ia.html":"0.9",
    "business-os-ia.html":"0.9","kemora-os-ia.html":"0.9",
    "the-mental-framework.html":"0.9","execution.html":"0.9","core-os-ai.html":"0.9",
    "business-os-ai.html":"0.9","kemora-os-ai.html":"0.9",
}

def get_priority(path):
    fname = path.split("/")[-1]
    if "merci" in fname or "thank-you" in fname or "gracias" in fname or "danke" in fname or "obrigado" in fname or "grazie" in fname:
        return "0.2"
    if "legal" in fname or "mentions" in fname or "impressum" in fname or "privacy" in fname or "confidentialite" in fname or "datenschutz" in fname or "privacidad" in fname or "privacidade" in fname or "privacy" in fname or "mencoes" in fname or "menciones" in fname or "note-legali" in fname:
        return "0.3"
    return PRIORITY.get(fname, "0.7")

def lang_sitemap(lang, pages):
    urls = ""
    for p in pages:
        prio = get_priority(p)
        change = "monthly" if float(prio) < 0.5 else "weekly"
        urls += f"""  <url>
    <loc>{SITE_URL}/{p}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>{change}</changefreq>
    <priority>{prio}</priority>
  </url>\n"""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
{urls}</urlset>"""

def sitemap_index():
    sitemaps = ""
    for lang in ["fr","en","es","de","pt","it"]:
        sitemaps += f"""  <sitemap>
    <loc>{SITE_URL}/sitemap-{lang}.xml</loc>
    <lastmod>{TODAY}</lastmod>
  </sitemap>\n"""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{sitemaps}</sitemapindex>"""

with open("sitemap-index.xml", "w") as f:
    f.write(sitemap_index())
print("WROTE: sitemap-index.xml")

for lang, pages in PAGES.items():
    with open(f"sitemap-{lang}.xml", "w") as f:
        f.write(lang_sitemap(lang, pages))
    print(f"WROTE: sitemap-{lang}.xml")

print("Done.")

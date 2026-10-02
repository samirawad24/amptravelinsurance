# -*- coding: utf-8 -*-
"""Builds every page of the AMP Insurance Assistance site.

    python _src/build.py

Copy lives in content.py (site pages) and legal.py (legal pages).
Shared styles: assets/site.css. Shared behavior: assets/site.js.
Folders starting with "_" are not published by GitHub Pages.
"""
import io, os, json, html, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import BRAND, OWNER, BROKER, TRAVEL_PARTNER, COMMON, LINES, LINE_URL, LINE_ICON, LINE_IMG, CARD, HOME, PAGES, PAGE_GREETING
from legal import LEGAL, LEGAL_ORDER, UPDATED

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://samirawad24.github.io/amptravelinsurance/"   # change when the custom domain is live
SITE = {"whatsapp": "19545341345", "phoneDisplay": "+1 (954) 534-1345",
        "email": "anamariapalacios1608@gmail.com", "instagram": "amptravelinsurance"}
OG_IMAGE = BASE + "assets/og-share.jpg"
LOGO = "assets/amp-logo-128.png"
EN, ES = COMMON["en"], COMMON["es"]

def e(s):  # escape text for HTML
    return html.escape(s, quote=True)

def tx(key, d=None):  # default (English) text for a data-i18n key
    d = d or EN
    return e(d[key])

def i18n_json(d):
    return json.dumps(d, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

# ============================================================ HEAD
def head(title, desc, url, schema=None, preload_img=None):
    s = [f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}" />
<link rel="canonical" href="{url}" />
<meta name="robots" content="index, follow, max-image-preview:large" />
<meta name="author" content="{OWNER}" />
<meta name="theme-color" content="#26324a" />
<meta name="color-scheme" content="light dark" />
<link rel="icon" href="{LOGO}" type="image/png" />
<link rel="apple-touch-icon" href="assets/amp-logo-512.png" />
<meta property="og:type" content="website" />
<meta property="og:site_name" content="{BRAND}" />
<meta property="og:title" content="{e(title)}" />
<meta property="og:description" content="{e(desc)}" />
<meta property="og:url" content="{url}" />
<meta property="og:image" content="{OG_IMAGE}" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:image:alt" content="{BRAND} logo" />
<meta property="og:locale" content="en_US" />
<meta property="og:locale:alternate" content="es_US" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{e(title)}" />
<meta name="twitter:description" content="{e(desc)}" />
<meta name="twitter:image" content="{OG_IMAGE}" />
<link rel="preload" href="assets/fonts/geist-latin.woff2" as="font" type="font/woff2" crossorigin />''']
    if preload_img:
        s.append(f'<link rel="preload" as="image" href="{preload_img}" fetchpriority="high" />')
    s.append('<link rel="stylesheet" href="assets/fonts/fonts.css" />\n<link rel="stylesheet" href="assets/site.css" />')
    if schema:
        s.append('<script type="application/ld+json">\n' + json.dumps(schema, ensure_ascii=False, indent=1) + '\n</script>')
    s.append('</head>\n<body>')
    return "\n".join(s)

# ============================================================ HEADER / FOOTER
def header(current, quote_href):
    links = "".join(
        f'<li><a href="{LINE_URL[l]}"' + (' aria-current="page"' if l == current else '') + f' data-i18n="nav_{l}">{tx("nav_"+l)}</a></li>'
        for l in LINES)
    panel = "".join(
        f'<li><a href="{LINE_URL[l]}"' + (' aria-current="page"' if l == current else '') +
        f'><i class="ph ph-{LINE_ICON[l]}" aria-hidden="true"></i><span data-i18n="nav_{l}">{tx("nav_"+l)}</span></a></li>'
        for l in LINES)
    return f'''<a class="skip" href="#main" data-i18n="skip">{tx("skip")}</a>
<div id="top-sentinel" style="position:absolute;top:0;height:1px;width:1px"></div>
<header class="nav" id="nav">
  <div class="wrap nav-in">
    <a class="brand" href="./" aria-label="{BRAND}, {e(EN["nav_home_page"])}">
      <img src="{LOGO}" alt="" width="42" height="42" />
      <span class="brand-txt"><b>{BRAND}</b><small>{OWNER}</small></span>
    </a>
    <nav aria-label="Insurance"><ul class="nav-links">{links}</ul></nav>
    <div class="nav-r">
      <div class="lang" role="group" aria-label="Language / Idioma">
        <button type="button" data-lang="en" aria-pressed="true" aria-label="English">EN</button>
        <button type="button" data-lang="es" aria-pressed="false" aria-label="Español">ES</button>
      </div>
      <a class="btn btn-primary" href="{quote_href}" data-i18n="cta_quote">{tx("cta_quote")}</a>
      <button type="button" class="menu-btn" id="menuBtn" aria-expanded="false" aria-controls="menuPanel" aria-label="{tx("menu_open")}" data-i18n-aria="menu_open"><i class="ph ph-list" aria-hidden="true"></i></button>
    </div>
  </div>
  <div class="menu-panel" id="menuPanel" hidden>
    <ul>{panel}</ul>
    <a class="btn btn-primary" href="{quote_href}" data-i18n="cta_quote">{tx("cta_quote")}</a>
  </div>
</header>'''

def footer(mbar_quote_href=None):
    ins = "".join(f'<li><a href="{LINE_URL[l]}" data-i18n="nav_{l}">{tx("nav_"+l)}</a></li>' for l in LINES)
    legal = "".join(f'<li><a href="{LEGAL[k]["file"]}" data-i18n="l_{k}">{tx("l_"+k)}</a></li>' for k in LEGAL_ORDER)
    mbar = ""
    if mbar_quote_href:
        mbar = f'''
<div class="mbar" id="mbar" aria-hidden="true">
  <a class="btn btn-primary" href="{mbar_quote_href}" tabindex="-1" data-i18n="cta_quote">{tx("cta_quote")}</a>
  <a class="btn btn-ghost wa" data-wa-link href="#" target="_blank" rel="noopener" tabindex="-1" aria-label="{tx("cta_whatsapp")}" data-i18n-aria="cta_whatsapp"><i class="ph-fill ph-whatsapp-logo" aria-hidden="true"></i></a>
</div>'''
    return f'''<footer class="foot">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <a class="brand" href="./" aria-label="{BRAND}, {e(EN["nav_home_page"])}">
          <img src="{LOGO}" alt="" width="42" height="42" loading="lazy" />
          <span><b>{BRAND}</b><small>{OWNER}</small></span>
        </a>
        <p data-i18n="foot_tag">{tx("foot_tag")}</p>
      </div>
      <div>
        <h2 class="fh" data-i18n="foot_contact">{tx("foot_contact")}</h2>
        <ul>
          <li><a data-wa-link href="#" target="_blank" rel="noopener"><i class="ph ph-whatsapp-logo" aria-hidden="true"></i>WhatsApp</a></li>
          <li><a class="js-tel" href="tel:+19545341345"><i class="ph ph-phone" aria-hidden="true"></i><span class="js-phone">{SITE["phoneDisplay"]}</span></a></li>
          <li><a class="js-mail" href="mailto:{SITE["email"]}"><i class="ph ph-envelope-simple" aria-hidden="true"></i><span class="js-email">{SITE["email"]}</span></a></li>
          <li><a class="js-ig" href="https://instagram.com/{SITE["instagram"]}" target="_blank" rel="noopener"><i class="ph ph-instagram-logo" aria-hidden="true"></i>@{SITE["instagram"]}</a></li>
        </ul>
      </div>
      <div>
        <h2 class="fh" data-i18n="foot_ins">{tx("foot_ins")}</h2>
        <ul>{ins}</ul>
      </div>
      <div>
        <h2 class="fh" data-i18n="foot_legal_h">{tx("foot_legal_h")}</h2>
        <ul>{legal}</ul>
      </div>
    </div>
    <div class="foot-bottom">
      <p>© <span class="js-year">2026</span> {BRAND} · {OWNER}. <span data-i18n="foot_legal">{tx("foot_legal")}</span></p>
    </div>
  </div>
</footer>{mbar}'''

def scripts(i18n):
    return f'''<script>window.SITE={json.dumps(SITE)};window.I18N={i18n_json(i18n)};</script>
<script src="assets/site.js"></script>
</body>
</html>
'''

# ============================================================ QUOTE FORM
def opt_tag():
    return f' <span class="opt" data-i18n="opt">{tx("opt")}</span>'

def fld(fid, label, *, typ="text", req=True, wa=None, wa_label=None, v=None, err="err_required", ph=None,
        opt=False, digits=None, ac=None, auto="off", inputmode=None, maxtoday=False, mintoday=False, after=None, cls=""):
    if v in ("zip", "year") and err == "err_required":
        err = "err_" + v   # empty and invalid share one clear message
    a = [f'id="{fid}"', f'name="{fid}"', f'type="{typ}"']
    if req: a.append("required")
    if wa: a.append(f'data-wa="{wa}"')
    if wa_label: a.append(f'data-wa-label="{wa_label}"')
    if v: a.append(f'data-v="{v}"')
    if req: a.append(f'data-err="{err}"')
    if ph: a.append(f'data-i18n-ph="{ph}" placeholder="{tx(ph)}"')
    if digits: a.append(f'data-digits="{digits}"')
    if ac: a.append(f'data-ac="{ac}"')
    a.append(f'autocomplete="{auto}"')
    if inputmode: a.append(f'inputmode="{inputmode}"')
    if maxtoday: a.append('data-max-today="1" min="1900-01-01"')
    if mintoday: a.append('data-min-today="1"')
    if after: a.append(f'data-v="after" data-after="{after}"')
    errdiv = f'<div class="err" data-i18n="{err}">{tx(err)}</div>' if (req or v) else ""
    if v == "email": errdiv = f'<div class="err" data-i18n="err_email">{tx("err_email")}</div>'
    if v == "zip": errdiv = f'<div class="err" data-i18n="err_zip">{tx("err_zip")}</div>'
    if v == "year": errdiv = f'<div class="err" data-i18n="err_year">{tx("err_year")}</div>'
    if after: errdiv = f'<div class="err" data-i18n="err_ret">{tx("err_ret")}</div>'
    return (f'<div class="field {cls}"><label for="{fid}"><span data-i18n="{label}">{tx(label)}</span>' + (opt_tag() if opt else "") +
            f'</label><input {" ".join(a)} />{errdiv}</div>')

def chips(name, label, options, *, radio=True, req=False, wa=None, opt=False):
    kind = "radio" if radio else "checkbox"
    role = 'role="radiogroup"' if radio else 'role="group"'
    items = "".join(
        f'<label class="chip"><input type="{kind}" name="{name}" value="{val}" /><span class="chip-face"><i class="ph ph-check" aria-hidden="true"></i><span data-i18n="{key}">{tx(key)}</span></span></label>'
        for val, key in options)
    err = f'<div class="err" data-i18n="err_choose">{tx("err_choose")}</div>' if req else ""
    return (f'<div class="chip-group"' + (f' data-wa="{wa}"' if wa else "") + (' data-required="1"' if req else "") +
            f'><span class="flabel" id="{name}-lbl"><span data-i18n="{label}">{tx(label)}</span>' + (opt_tag() if opt else "") +
            f'</span><div class="chips" {role} aria-labelledby="{name}-lbl">{items}</div>{err}</div>')

def repeater(rep, title, add, max_n, wa, fields_html, join=None):
    return (f'<div class="rep" data-rep="{rep}" data-title="{title}" data-max="{max_n}" data-wa="{wa}"' + (f' data-join="{join}"' if join else "") +
            f'><div class="rep-list"></div><template>{fields_html}</template>'
            f'<button type="button" class="rep-add"><i class="ph ph-plus" aria-hidden="true"></i><span data-i18n="{add}">{tx(add)}</span></button></div>')

def person_fields(prefix):
    return ('<div class="grid-2">' +
            fld(f"__ID__-name", "f_name", err="err_name", ph="ph_name", auto="off") +
            fld(f"__ID__-dob", "f_dob", typ="date", v="dob", err="err_dob", wa_label="wa_dob", maxtoday=True) +
            '</div>')

def sec(t, inner):
    return (f'<fieldset class="fgroup qsec" data-for="{t}" hidden disabled><legend><span class="num">2</span>'
            f'<span data-i18n="q_details">{tx("q_details")}</span></legend>{inner}</fieldset>')

def quote_form(preset=""):
    types = "".join(
        f'<label class="type"><input type="radio" name="qtype" value="{l}" /><span class="type-face"><i class="ph ph-{LINE_ICON[l]}" aria-hidden="true"></i><span data-i18n="t_{l}">{tx("t_"+l)}</span></span></label>'
        for l in LINES)
    auto = (fld("a-zip", "a_zip", v="zip", ph="ph_zip", wa="wa_zip", digits=5, inputmode="numeric", auto="postal-code", cls="field-sm") +
            repeater("drivers", "driver", "add_driver", 6, "wa_drivers", person_fields("d")) +
            repeater("vehicles", "vehicle", "add_vehicle", 6, "wa_vehicles",
                     '<div class="grid-3">' +
                     fld("__ID__-year", "f_year", v="year", digits=4, inputmode="numeric") +
                     fld("__ID__-make", "f_make", ph="ph_make") +
                     fld("__ID__-model", "f_model", ph="ph_model") + '</div>', join="space") +
            chips("a-cov", "a_cov", [("min", "a_cov_min"), ("full", "a_cov_full"), ("unsure", "a_cov_unsure")], wa="wa_cov", opt=True) +
            fld("a-current", "f_current", req=False, opt=True, wa="wa_current"))
    home = (chips("h-ptype", "h_ptype", [("house", "h_house"), ("condo", "h_condo"), ("town", "h_town"), ("mobile", "h_mobile"), ("rental", "h_rental")], req=True, wa="wa_ptype") +
            '<div class="grid-2">' +
            fld("h-zip", "h_zip", v="zip", ph="ph_zip", wa="wa_zip", digits=5, inputmode="numeric", auto="postal-code") +
            fld("h-built", "h_built", req=False, opt=True, v="year", digits=4, inputmode="numeric", wa="wa_built") +
            '</div><div class="grid-2">' +
            fld("h-owner", "h_owner", err="err_name", ph="ph_name", wa="wa_owner", auto="name") +
            fld("h-owner-dob", "h_owner_dob", typ="date", v="dob", err="err_dob", wa="wa_owner_dob", maxtoday=True) +
            '</div>' +
            fld("h-current", "f_current", req=False, opt=True, wa="wa_current") +
            chips("h-extra", "h_extra", [("flood", "h_flood"), ("umbrella", "h_umbrella")], radio=False, wa="wa_extra", opt=True))
    renters = (fld("r-zip", "r_zip", v="zip", ph="ph_zip", wa="wa_zip", digits=5, inputmode="numeric", auto="postal-code", cls="field-sm") +
               '<div class="grid-2">' +
               fld("r-name", "r_name", err="err_name", ph="ph_name", wa="wa_name", auto="name") +
               fld("r-dob", "r_dob", typ="date", v="dob", err="err_dob", wa="wa_dob", maxtoday=True) +
               '</div>' +
               fld("r-move", "r_move", typ="date", req=False, opt=True, wa="wa_move", cls="field-sm") +
               chips("r-value", "r_value", [("v1", "r_v1"), ("v2", "r_v2"), ("v3", "r_v3"), ("v4", "r_v4"), ("v5", "r_v5")], wa="wa_value", opt=True))
    travel = (repeater("travelers", "traveler", "add_traveler", 10, "wa_travelers", person_fields("t")) +
              '<div class="grid-2">' +
              fld("origin", "tr_from", ph="ph_city", wa="wa_from", ac="places") +
              fld("destination", "tr_to", ph="ph_city", wa="wa_to", ac="places") +
              '</div>' +
              fld("residence", "tr_res", ph="ph_country", wa="wa_res", ac="countries") +
              '<div class="grid-2">' +
              fld("depart", "tr_dep", typ="date", req=False, opt=True, wa="wa_dep", mintoday=True) +
              fld("ret", "tr_ret", typ="date", req=False, opt=True, wa="wa_ret", after="depart") +
              '</div>' +
              chips("tr-purpose", "tr_purpose", [("vacation", "p_vacation"), ("business", "p_business"), ("study", "p_study"), ("family", "p_family")], wa="wa_purpose", opt=True) +
              chips("tr-prio", "tr_prio", [("medical", "c_medical"), ("cancel", "c_cancel"), ("baggage", "c_baggage"), ("delays", "c_delays")], radio=False, wa="wa_prio", opt=True))
    business = ('<div class="grid-2">' +
                fld("b-name", "b_name", wa="wa_bname", auto="organization") +
                fld("b-zip", "b_zip", v="zip", ph="ph_zip", wa="wa_zip", digits=5, inputmode="numeric", auto="postal-code") +
                '</div>' +
                fld("b-what", "b_what", ph="ph_what", wa="wa_bwhat") +
                fld("b-owner", "b_owner", err="err_name", ph="ph_name", wa="wa_name", auto="name") +
                '<div class="grid-2">' +
                fld("b-years", "b_years", req=False, opt=True, digits=3, inputmode="numeric", wa="wa_years") +
                fld("b-emps", "b_emps", req=False, opt=True, digits=5, inputmode="numeric", wa="wa_emps") +
                '</div>' +
                chips("b-cov", "b_cov", [("gl", "b_gl"), ("prop", "b_prop"), ("auto", "b_auto"), ("wc", "b_wc"), ("pro", "b_pro"), ("unsure", "b_unsure")], radio=False, wa="wa_bcov", opt=True))
    contact = ('<div class="grid-2">' +
               fld("waNumber", "f_wa", typ="tel", req=False, opt=True, wa="wa_contact_wa", auto="tel", inputmode="tel") +
               fld("email", "f_email", typ="email", req=False, opt=True, v="email", wa="wa_contact_email", auto="email", inputmode="email") +
               '</div>' +
               f'''<div class="consent"><input type="checkbox" id="consent" required aria-describedby="consentErr" /><label for="consent"><span data-i18n="consent">{tx("consent")}</span> <a href="privacy.html" data-i18n="consent_link">{tx("consent_link")}</a>.</label></div>
<div class="err consent-err" id="consentErr" data-i18n="err_consent">{tx("err_consent")}</div>''')
    return f'''<div class="card form-card" data-reveal>
  <form id="quoteForm" novalidate data-preset="{preset}">
    <fieldset class="fgroup"><legend><span class="num">1</span><span data-i18n="q_type">{tx("q_type")}</span></legend>
      <div class="types">{types}</div>
      <div class="err type-err" id="typeErr" data-i18n="err_type">{tx("err_type")}</div>
    </fieldset>
    {sec("auto", auto)}
    {sec("home", home)}
    {sec("renters", renters)}
    {sec("travel", travel)}
    {sec("business", business)}
    <fieldset class="fgroup" id="qcontact" hidden disabled><legend><span class="num">3</span><span data-i18n="q_contact">{tx("q_contact")}</span></legend>{contact}</fieldset>
    <div class="submit-row" id="qsubmit" hidden>
      <button type="submit" class="btn btn-primary btn-block"><i class="ph-fill ph-whatsapp-logo" aria-hidden="true"></i><span data-i18n="submit">{tx("submit")}</span></button>
      <p class="form-note" data-i18n="form_note">{tx("form_note")}</p>
    </div>
  </form>
  <div class="success" id="success" role="status" aria-live="polite" tabindex="-1">
    <div class="chk"><i class="ph ph-check" aria-hidden="true"></i></div>
    <h3 data-i18n="s_h">{tx("s_h")}</h3>
    <p data-i18n="s_p">{tx("s_p")}</p>
    <div class="copy-box" id="copyBox"></div>
    <div class="acts">
      <a class="btn btn-primary" id="successWa" href="#" target="_blank" rel="noopener"><i class="ph-fill ph-whatsapp-logo" aria-hidden="true"></i><span data-i18n="s_open">{tx("s_open")}</span></a>
      <button type="button" class="btn btn-ghost" id="copyBtn"><i class="ph ph-copy" aria-hidden="true"></i><span data-i18n="s_copy">{tx("s_copy")}</span></button>
      <button type="button" class="btn btn-ghost" id="editBtn"><i class="ph ph-pencil-simple" aria-hidden="true"></i><span data-i18n="s_edit">{tx("s_edit")}</span></button>
    </div>
  </div>
</div>'''

def quote_section(preset=""):
    return f'''<section class="sec" id="quote">
  <div class="wrap quote-grid">
    <div class="quote-side" data-reveal>
      <span class="eyebrow"><i class="ph ph-paper-plane-tilt" aria-hidden="true"></i><span data-i18n="quote_eyebrow">{tx("quote_eyebrow")}</span></span>
      <h2 style="margin-top:14px" data-i18n="quote_h2">{tx("quote_h2")}</h2>
      <p class="lede" data-i18n="quote_sub">{tx("quote_sub")}</p>
      <ul class="assure">
        <li><i class="ph ph-user-circle" aria-hidden="true"></i><span data-i18n="assure_1">{tx("assure_1")}</span></li>
        <li><i class="ph ph-lock-simple" aria-hidden="true"></i><span data-i18n="assure_2">{tx("assure_2")}</span></li>
        <li><i class="ph ph-check" aria-hidden="true"></i><span data-i18n="assure_3">{tx("assure_3")}</span></li>
      </ul>
      <div class="side-contact">
        <img src="assets/ana-headshot.jpg" width="52" height="52" loading="lazy" alt="" />
        <span><b>{OWNER}</b><span class="js-phone">{SITE["phoneDisplay"]}</span></span>
      </div>
    </div>
    {quote_form(preset)}
  </div>
</section>'''

def faq_section(faq_en):
    return f'''<section class="sec faq" id="faq">
  <div class="wrap faq-in">
    <h2 data-reveal data-i18n="faq_h2">{tx("faq_h2")}</h2>
    <div class="faq-list" id="faqList" data-reveal>''' + "".join(
        f'<details class="faq-item"><summary>{e(f["q"])}<i class="ph ph-caret-down" aria-hidden="true"></i></summary><div class="ans">{e(f["a"])}</div></details>'
        for f in faq_en) + f'''</div>
    <div class="faq-more" data-reveal>
      <b data-i18n="faq_more">{tx("faq_more")}</b>
      <a class="btn btn-primary" data-wa-link href="#" target="_blank" rel="noopener"><i class="ph-fill ph-whatsapp-logo" aria-hidden="true"></i><span data-i18n="cta_whatsapp">{tx("cta_whatsapp")}</span></a>
    </div>
  </div>
</section>'''

def trust_band():
    return f'''<section class="trust" id="broker" aria-label="{BROKER}, {TRAVEL_PARTNER}">
  <div class="wrap trust-in" data-reveal>
    <div class="trust-brk">
      <div class="partner">
        <img src="assets/agb-insurance-logo.png" alt="{BROKER}" width="385" height="159" />
        <p><b data-i18n="broker_t">{tx("broker_t")}</b><span data-i18n="broker_p">{tx("broker_p")}</span></p>
      </div>
      <div class="partner">
        <img class="bta" src="assets/best-travel-assistance-logo.svg" alt="{TRAVEL_PARTNER}" width="424" height="133" />
        <p><b data-i18n="travel_t">{tx("travel_t")}</b><span data-i18n="travel_p">{tx("travel_p")}</span></p>
      </div>
    </div>
    <ul class="facts">
      <li><i class="ph ph-user-circle" aria-hidden="true"></i><span data-i18n="fact_1">{tx("fact_1")}</span></li>
      <li><i class="ph ph-currency-circle-dollar" aria-hidden="true"></i><span data-i18n="fact_2">{tx("fact_2")}</span></li>
      <li><i class="ph ph-translate" aria-hidden="true"></i><span data-i18n="fact_3">{tx("fact_3")}</span></li>
    </ul>
  </div>
</section>'''

# ============================================================ SCHEMA
BIZ_ID = BASE + "#business"
PERSON_ID = BASE + "#person"
def biz_schema():
    return {
        "@type": ["InsuranceAgency", "LocalBusiness"], "@id": BIZ_ID, "name": BRAND,
        "description": "Bilingual (English and Spanish) insurance help from Ana María Palacios for auto, home, renters, travel, and business insurance, through AGB Insurance and, for travel plans, Best Travel Assistance.",
        "url": BASE, "logo": BASE + "assets/amp-logo-512.png", "image": BASE + "assets/ana-headshot.jpg",
        "telephone": "+19545341345", "email": SITE["email"],
        "address": {"@type": "PostalAddress", "addressCountry": "US"},
        "areaServed": {"@type": "Country", "name": "United States"},
        "knowsLanguage": ["en", "es"],
        "sameAs": ["https://www.instagram.com/" + SITE["instagram"], "https://wa.me/" + SITE["whatsapp"]],
        "founder": {"@id": PERSON_ID},
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Insurance quotes", "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": CARD["en"][l][0] + " insurance", "url": BASE + LINE_URL[l]}} for l in LINES]},
    }
def person_schema():
    return {"@type": "Person", "@id": PERSON_ID, "name": OWNER,
            "jobTitle": "Travel insurance agent and insurance advisor",
            "image": BASE + "assets/ana-headshot.jpg", "knowsLanguage": ["en", "es"],
            "worksFor": {"@id": BIZ_ID}, "sameAs": ["https://www.instagram.com/" + SITE["instagram"]]}
def faq_schema(url, faq):
    return {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
        {"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in faq]}

# ============================================================ PAGES
def write(name, text):
    io.open(os.path.join(ROOT, name), "w", encoding="utf-8", newline="\n").write(text)
    print("wrote", name, len(text))

def build_home():
    P = HOME
    title, desc = P["meta"]["en"]
    i18n = {L: dict(COMMON[L], **P[L], meta_title=P["meta"][L][0]) for L in ("en", "es")}
    for L in ("en", "es"):
        for l in LINES:
            i18n[L]["card_" + l + "_t"], i18n[L]["card_" + l + "_d"] = CARD[L][l]
    H = P["en"]
    schema = {"@context": "https://schema.org", "@graph": [biz_schema(), person_schema(),
              {"@type": "WebSite", "@id": BASE + "#website", "url": BASE, "name": BRAND, "inLanguage": ["en", "es"], "publisher": {"@id": BIZ_ID}},
              faq_schema(BASE, H["faq"])]}
    cards = "".join(f'''<article class="line-card">
        <div class="lc-img"><img src="{LINE_IMG[l]}" width="1200" height="800" loading="lazy" decoding="async" alt="" /></div>
        <div class="lc-body">
          <h3><i class="ph ph-{LINE_ICON[l]}" aria-hidden="true"></i><span data-i18n="card_{l}_t">{e(CARD["en"][l][0])}</span></h3>
          <p data-i18n="card_{l}_d">{e(CARD["en"][l][1])}</p>
          <span class="lc-go" aria-hidden="true"><span data-i18n="learn_more">{tx("learn_more")}</span><i class="ph ph-arrow-right"></i></span>
        </div>
        <a class="cover" href="{LINE_URL[l]}"><span class="sr" data-i18n="card_{l}_t">{e(CARD["en"][l][0])}</span></a>
      </article>''' for l in LINES)
    body = f'''{head(title, desc, BASE, schema, "assets/ana-headshot.jpg")}
{header(None, "#quote")}
<main id="main" tabindex="-1">
<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <span class="eyebrow" data-enter="1"><i class="ph ph-translate" aria-hidden="true"></i><span data-i18n="hero_eyebrow">{e(H["hero_eyebrow"])}</span></span>
      <h1 data-enter="2" data-i18n="hero_h1" data-html>{H["hero_h1"]}</h1>
      <p class="lede" data-enter="3" data-i18n="hero_sub">{e(H["hero_sub"])}</p>
      <div class="hero-cta" data-enter="4">
        <a class="btn btn-primary" href="#quote"><span data-i18n="cta_quote">{tx("cta_quote")}</span><i class="ph ph-arrow-right" aria-hidden="true"></i></a>
        <a class="btn btn-ghost" data-wa-link href="#" target="_blank" rel="noopener"><i class="ph ph-whatsapp-logo" aria-hidden="true"></i><span data-i18n="cta_whatsapp">{tx("cta_whatsapp")}</span></a>
      </div>
    </div>
    <figure class="hero-media" data-enter="5">
      <div class="frame"><img src="assets/ana-headshot.jpg" width="960" height="1200" fetchpriority="high" decoding="async" alt="{OWNER}" /></div>
      <figcaption class="hero-id"><span><b>{OWNER}</b><span data-i18n="hero_role">{e(H["hero_role"])}</span></span></figcaption>
    </figure>
  </div>
</section>
{trust_band()}
<section class="sec" id="lines">
  <div class="wrap">
    <div data-reveal>
      <h2 data-i18n="lines_h2">{e(H["lines_h2"])}</h2>
      <p class="lede" data-i18n="lines_sub">{e(H["lines_sub"])}</p>
    </div>
    <div class="lines" data-reveal>{cards}</div>
  </div>
</section>
<section class="sec how" id="how">
  <div class="wrap">
    <h2 data-reveal data-i18n="how_h2">{e(H["how_h2"])}</h2>
    <ol class="steps" data-reveal>
      <li><span class="step-ico"><i class="ph ph-paper-plane-tilt" aria-hidden="true"></i></span><h3 data-i18n="how_1_t">{e(H["how_1_t"])}</h3><p data-i18n="how_1_d">{e(H["how_1_d"])}</p></li>
      <li><span class="step-ico"><i class="ph ph-list-checks" aria-hidden="true"></i></span><h3 data-i18n="how_2_t">{e(H["how_2_t"])}</h3><p data-i18n="how_2_d">{e(H["how_2_d"])}</p></li>
      <li><span class="step-ico"><i class="ph ph-shield-check" aria-hidden="true"></i></span><h3 data-i18n="how_3_t">{e(H["how_3_t"])}</h3><p data-i18n="how_3_d">{e(H["how_3_d"])}</p></li>
    </ol>
  </div>
</section>
{quote_section("")}
<section class="sec" id="about">
  <div class="wrap about-in" data-reveal>
    <img class="avatar" src="assets/ana-headshot.jpg" width="132" height="132" loading="lazy" decoding="async" alt="{OWNER}" />
    <h2 data-i18n="about_h2">{e(H["about_h2"])}</h2>
    <p data-i18n="about_p1">{e(H["about_p1"])}</p>
    <p data-i18n="about_p2">{e(H["about_p2"])}</p>
    <div class="about-links"><a class="btn btn-ghost js-ig" href="https://instagram.com/{SITE["instagram"]}" target="_blank" rel="noopener"><i class="ph ph-instagram-logo" aria-hidden="true"></i>@{SITE["instagram"]}</a></div>
  </div>
</section>
{faq_section(H["faq"])}
</main>
{footer("#quote")}
{scripts(i18n)}'''
    write(P["file"], body)

def build_line(l):
    P = PAGES[l]
    url = BASE + LINE_URL[l]
    title, desc = P["meta"]["en"]
    i18n = {}
    for L in ("en", "es"):
        d = dict(COMMON[L]); d.update(P[L]); d["meta_title"] = P["meta"][L][0]; d["wa_greeting"] = PAGE_GREETING[l][L]
        for i, (_, t_, p_) in enumerate(P[L]["items"]):
            d[f"cov_{i}_t"], d[f"cov_{i}_d"] = t_, p_
        for o in LINES:
            d["card_" + o + "_t"] = CARD[L][o][0]
        d.pop("items")
        i18n[L] = d
    H = P["en"]
    note_h, note_p = ("agent_h", "agent_p") if l == "travel" else ("adv_h", "adv_p")
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "Service", "@id": url + "#service", "name": CARD["en"][l][0] + " insurance quotes", "serviceType": CARD["en"][l][0] + " insurance",
         "description": desc, "url": url, "provider": {"@id": BIZ_ID}, "areaServed": {"@type": "Country", "name": "United States"},
         "availableLanguage": ["en", "es"]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": BRAND, "item": BASE},
            {"@type": "ListItem", "position": 2, "name": CARD["en"][l][0] + " insurance", "item": url}]},
        faq_schema(url, H["faq"])]}
    items = "".join(
        f'<li><span class="cov-ico"><i class="ph ph-{ico}" aria-hidden="true"></i></span><div><h3 data-i18n="cov_{i}_t">{e(t_)}</h3><p data-i18n="cov_{i}_d">{e(p_)}</p></div></li>'
        for i, (ico, t_, p_) in enumerate(H["items"]))
    others = "".join(
        f'<a class="chip" href="{LINE_URL[o]}"><span class="chip-face"><i class="ph ph-{LINE_ICON[o]}" aria-hidden="true" style="display:inline"></i><span data-i18n="card_{o}_t">{e(CARD["en"][o][0])}</span></span></a>'
        for o in LINES if o != l)
    body = f'''{head(title, desc, url, schema, LINE_IMG[l])}
{header(l, "#quote")}
<main id="main" tabindex="-1">
<section class="lhero">
  <div class="wrap">
    <a class="crumb" href="./#lines"><i class="ph ph-arrow-left" aria-hidden="true"></i><span data-i18n="back_home">{tx("back_home")}</span></a>
    <div class="lhero-grid">
      <div>
        <span class="eyebrow"><i class="ph ph-{LINE_ICON[l]}" aria-hidden="true"></i><span data-i18n="eyebrow">{e(H["eyebrow"])}</span></span>
        <h1 data-i18n="h1" data-html>{H["h1"]}</h1>
        <p class="lede" data-i18n="sub">{e(H["sub"])}</p>
        <div class="hero-cta" style="margin-top:28px">
          <a class="btn btn-primary" href="#quote"><span data-i18n="cta_quote">{tx("cta_quote")}</span><i class="ph ph-arrow-right" aria-hidden="true"></i></a>
          <a class="btn btn-ghost" data-wa-link href="#" target="_blank" rel="noopener"><i class="ph ph-whatsapp-logo" aria-hidden="true"></i><span data-i18n="cta_whatsapp">{tx("cta_whatsapp")}</span></a>
        </div>
      </div>
      <div class="lhero-img"><img src="{LINE_IMG[l]}" width="1200" height="800" fetchpriority="high" decoding="async" alt="" /></div>
    </div>
  </div>
</section>
<section class="advise">
  <div class="wrap"><div class="advise-in" data-reveal>
    <img src="assets/ana-headshot.jpg" width="64" height="64" loading="lazy" alt="" />
    <div><h2 data-i18n="{note_h}">{tx(note_h)}</h2><p data-i18n="{note_p}">{tx(note_p)}</p></div>
  </div></div>
</section>
<section class="sec" id="coverage">
  <div class="wrap">
    <h2 data-reveal data-i18n="cov_h2">{e(H["cov_h2"])}</h2>
    <ul class="covlist" data-reveal>{items}</ul>
    <p class="fine" data-i18n="cov_fine">{tx("cov_fine")}</p>
  </div>
</section>
{quote_section(l)}
{faq_section(H["faq"])}
<section class="sec more">
  <div class="wrap">
    <h2 class="more-h" data-i18n="more_h">{tx("more_h")}</h2>
    <div class="chips more-chips">{others}</div>
  </div>
</section>
</main>
{footer("#quote")}
{scripts(i18n)}'''
    write(LINE_URL[l], body)

def build_legal(k):
    P = LEGAL[k]
    url = BASE + P["file"]
    def block(item):
        if isinstance(item, tuple) and item[0] == "ul":
            return "<ul>" + "".join(f"<li>{li}</li>" for li in item[1]) + "</ul>"
        return f"<p>{item}</p>"
    blocks = ""
    for L in ("en", "es"):
        blocks += (f'<div lang="{L}" data-lang-block="{L}"' + ("" if L == "en" else " hidden") + ">" +
                   f'<h1>{P["title"][L]}</h1><p class="upd">{UPDATED[L]}</p><p class="intro">{P["intro"][L]}</p>' +
                   "".join(f'<section><h2>{h}</h2>' + "".join(block(i) for i in items) + '</section>' for h, items in P["sections"][L]) +
                   "</div>")
    i18n = {L: dict(COMMON[L], meta_title=P["title"][L] + " | " + BRAND) for L in ("en", "es")}
    body = f'''{head(P["title"]["en"] + " | " + BRAND, P["desc"]["en"], url)}
{header(None, "./#quote")}
<main id="main" tabindex="-1">
<div class="doc">
  <a class="back" href="./"><i class="ph ph-arrow-left" aria-hidden="true"></i><span data-i18n="nav_home_page">{tx("nav_home_page")}</span></a>
  {blocks}
</div>
</main>
{footer(None)}
{scripts(i18n)}'''
    write(P["file"], body)

if __name__ == "__main__":
    build_home()
    for l in LINES:
        build_line(l)
    for k in LEGAL_ORDER:
        build_legal(k)

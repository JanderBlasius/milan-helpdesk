#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Erzeugt die statische Helpdesk-Seite aus content_a.py / content_b.py.
Aufruf (im Repository-Hauptordner):  python3 tools/build_site.py
Keine externen Pakete nötig."""
import html, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from content_b import PAGES
from content_a import SECTIONS

STAND = "12.10.2026"
TITEL = "Milan Helpdesk"
UNTER = "Anleitungen für Helferinnen und Helfer · Milan Materialmanagement"
OUT = os.path.join(ROOT, "anleitungen")

CSP = ("default-src 'none'; img-src 'self'; style-src 'self'; script-src 'self'; "
       "base-uri 'none'; form-action 'none'")
by_id = {p["id"]: p for p in PAGES}
for i, p in enumerate(PAGES):
    p["_i"] = i

def mk(t):  # {1} -> Markierung
    return re.sub(r"\{(\d)\}", r'<span class="marker" aria-label="Markierung \1">\1</span>', t)

def link(pid, root):  # relativer Link auf Leitfaden
    return f'{root}anleitungen/{pid}.html' if root == "" else f'{pid}.html'

def head(title, root, desc):
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="{CSP}">
<meta name="referrer" content="no-referrer">
<meta name="robots" content="noindex, nofollow">
<meta name="description" content="{html.escape(desc)}">
<title>{html.escape(title)} – {TITEL}</title>
<link rel="icon" type="image/png" href="{root}assets/img/favicon.png">
<link rel="stylesheet" href="{root}assets/style.css">
</head>
"""

def sidebar(root, active):
    s = ['<nav class="sidebar" id="sidebar" aria-label="Seitennavigation">',
         '<div class="sidebar-search"><input id="navSearch" type="search" placeholder="Suchen, z. B. „Passwort“ oder „auffüllen“" aria-label="Anleitungen durchsuchen" autocomplete="off"></div>',
         '<ul class="search-results" id="searchResults" hidden></ul>',
         '<div id="navList"><div class="sidebar-title">Inhalt</div><ul class="nav-list">']
    s.append(f'<li class="nav-section"><a href="{root}index.html"{" class=\"active\"" if active=="start" else ""}>Startseite</a></li>')
    for n, sec in SECTIONS.items():
        a = f' class="active"' if active == f"sec{n}" else ""
        s.append(f'<li class="nav-section"><a href="{root}anleitungen/abschnitt-{n}.html"{a}>{n}. {html.escape(sec["title"])}</a></li>')
        for p in PAGES:
            if p["sec"] == n:
                a = ' active' if active == p["id"] else ""
                s.append(f'<li><a class="sub{a}" href="{root}anleitungen/{p["id"]}.html">{p["num"]} {html.escape(p["title"])}</a></li>')
    s.append('</ul></div></nav>')
    return "\n".join(s)

def top(root):
    return f"""<body data-root="{root}">
<div class="top-bar">
  <div class="brand">
    <button class="menu-toggle" id="menuToggle" aria-label="Menü öffnen" aria-expanded="false" aria-controls="sidebar"><span></span><span></span><span></span></button>
    <a class="logo" href="{root}index.html" aria-label="Zur Startseite des Milan Helpdesk"><img class="brand-mark" src="{root}assets/img/milan-logo.png" alt="Milan Materialmanagement"></a>
    <div><div class="brand-text">{TITEL}</div><span class="brand-sub">{UNTER}</span></div>
  </div>
</div>
<div class="overlay" id="overlay"></div>
<div class="layout">
"""

def foot(root):
    return f"""</div>
<footer class="site">{TITEL} · Anleitungen für Helferinnen und Helfer · Stand {STAND}. Die Anleitungen zeigen Beispieldaten. Deine Ansicht kann je nach Einstellung leicht abweichen.</footer>
<script src="{root}assets/search-index.js"></script>
<script src="{root}assets/site.js"></script>
</body>
</html>
"""

def block(b, root):
    k = b[0]
    if k == "h": return f'<h3>{mk(b[1])}</h3>'
    if k == "p": return f'<p>{mk(b[1])}</p>'
    if k == "list": return '<ul class="content-list">' + "".join(f"<li>{mk(x)}</li>" for x in b[1]) + "</ul>"
    if k in ("note", "warn", "stop", "ok"):
        cls = "" if k == "note" else f" {k}"
        return f'<div class="box{cls}"><strong class="t">{html.escape(b[1])}</strong>{mk(b[2])}</div>'
    if k == "table":
        th = "".join(f"<th>{html.escape(h)}</th>" for h in b[1])
        rows = "".join("<tr>" + "".join(f"<td>{mk(c)}</td>" for c in r) + "</tr>" for r in b[2])
        return f'<div class="table-wrap"><table class="t"><thead><tr>{th}</tr></thead><tbody>{rows}</tbody></table></div>'
    if k == "faq":
        return "".join(f'<details class="faq"><summary>{html.escape(q)}</summary><div class="a">{mk(a)}</div></details>' for q, a in b[1])
    if k == "flow":
        return '<div class="flow">' + "".join(f'<div class="f{" alt" if alt else ""}"><b>{html.escape(t)}</b><small>{html.escape(d)}</small></div>' for t, d, alt in b[1]) + "</div>"
    if k == "tiles":
        return '<div class="tiles">' + "".join(f'<a class="tile" href="{pid}.html"><span class="q">{html.escape(t)}</span><span class="d">{html.escape(d)}</span><span class="go">Zur Anleitung →</span></a>' for t, d, pid in b[1]) + "</div>"
    if k == "steps":
        out = ['<ol class="steps">']
        for s in b[1]:
            out.append(f'<li><div class="step-text">{mk(s["t"])}</div>')
            if s.get("img"):
                out.append(f'<figure class="shot"><img src="../assets/img/{s["img"]}.png" alt="{html.escape(s["alt"])}" loading="lazy" width="585" height="1266"><figcaption>{mk(s["cap"])}</figcaption></figure>')
            out.append("</li>")
        out.append("</ol>")
        return "".join(out)
    raise ValueError(k)

def page_html(p):
    root = "../"
    prev_p = PAGES[p["_i"] - 1] if p["_i"] > 0 else None
    next_p = PAGES[p["_i"] + 1] if p["_i"] < len(PAGES) - 1 else None
    h = head(f'{p["num"]} {p["title"]}', root, p["kurz"])
    h += top(root) + sidebar(root, p["id"]) + '<main class="content">\n'
    sec = SECTIONS[p["sec"]]
    h += f'<div class="crumbs"><a href="{root}index.html">Start</a> › <a href="abschnitt-{p["sec"]}.html">{p["sec"]}. {html.escape(sec["title"])}</a></div>\n'
    h += f'<div class="page-intro"><span class="status-tag">Anleitung {p["num"]}</span><h1><span class="h1-num">{p["num"]}</span>{html.escape(p["title"])}</h1>'
    if p.get("wann"): h += f'<p><b>Wann brauchst du das?</b> {mk(p["wann"])}</p>'
    h += '</div>\n'
    h += f'<div class="tldr"><strong class="t">Kurz gesagt</strong>{mk(p["kurz"])}</div>\n'
    if p.get("vorher"):
        h += '<h2 class="sec"><span class="n">✔</span>Das brauchst du vorher</h2><ul class="content-list">' + "".join(f"<li>{mk(x)}</li>" for x in p["vorher"]) + "</ul>\n"
    first = True
    for b in p["blocks"]:
        if first and b[0] == "steps":
            h += '<h2 class="sec"><span class="n">→</span>So geht’s</h2>\n'
        first = False
        h += block(b, root) + "\n"
    if p.get("weiter"):
        h += '<div class="next"><h3>Wie geht’s weiter?</h3><ul>' + "".join(f'<li><a href="{w}.html">{by_id[w]["num"]} {html.escape(by_id[w]["title"])}</a></li>' for w in p["weiter"]) + "</ul></div>\n"
    h += '<div class="pager">'
    h += f'<a href="{prev_p["id"]}.html">← {prev_p["num"]} {html.escape(prev_p["title"])}</a>' if prev_p else "<span></span>"
    h += f'<a href="{next_p["id"]}.html">{next_p["num"]} {html.escape(next_p["title"])} →</a>' if next_p else ""
    h += "</div>\n</main>\n" + foot(root)
    return h

def section_html(n):
    sec = SECTIONS[n]; root = "../"
    h = head(f"{n}. {sec['title']}", root, sec["lead"]) + top(root) + sidebar(root, f"sec{n}") + '<main class="content">\n'
    h += f'<div class="crumbs"><a href="{root}index.html">Start</a> › {n}. {html.escape(sec["title"])}</div>'
    h += f'<div class="page-intro"><span class="status-tag">Abschnitt {n}</span><h1><span class="h1-num">{n}</span>{html.escape(sec["title"])}</h1><p>{html.escape(sec["lead"])}</p></div>'
    h += '<div class="tiles">' + "".join(
        f'<a class="tile" href="{p["id"]}.html"><span class="q">{p["num"]} {html.escape(p["title"])}</span><span class="d">{html.escape(re.sub(r"<[^>]+>","",re.sub(r"\{\d\}","",p["kurz"])))}</span><span class="go">Öffnen →</span></a>'
        for p in PAGES if p["sec"] == n) + "</div></main>\n" + foot(root)
    return h

START_TILES = [
 ("Ich habe bei einem Dienst Material verbraucht", "Eintragen, was verbraucht wurde, und später auffüllen.", "verbrauch-ueberblick", False),
 ("Ich will Material nach dem Auffüllen bestätigen", "Offene Auffüllungen abhaken, Verfallsdaten eintragen.", "auffuellen", False),
 ("Ich kontrolliere ein Fahrzeug, einen Rucksack oder Koffer", "Zustand, Anzahl und Verfallsdatum melden.", "ep-kontrolle", False),
 ("Etwas fehlt oder ist kaputt", "Einen Fehler melden oder einen Auftrag anlegen.", "ep-fehler-melden", True),
 ("Ich will ein ganzes Modul auf einmal erfassen", "Massenscan: jede Packung einzeln scannen.", "massenscan", False),
 ("Ich will einen Code scannen", "Etikett mit der Kamera lesen. Und was hilft, wenn es nicht klappt.", "scan-button", False),
 ("Ich will etwas nachschlagen", "Produkte, Bestand, Lagerorte, Veranstaltungen ansehen.", "nachschlagen-produkte", True),
 ("Ich kann mich nicht anmelden", "Anmelden, Passwort ändern, abmelden.", "anmelden", True),
 ("Ich verstehe ein Wort nicht", "Begriffe einfach erklärt.", "glossar", True),
]

def index_html():
    root = ""
    h = head("Startseite", root, "Anleitungen für Helferinnen und Helfer zur Nutzung von Milan Materialmanagement") + top(root) + sidebar(root, "start") + '<main class="content">\n'
    h += f'<div class="hero"><span class="status-tag">Stand {STAND}</span><h1>Willkommen beim {TITEL}</h1><p>Hier findest du Schritt-für-Schritt-Anleitungen für alles, was du als Helferin oder Helfer in Milan selbst erledigen kannst. Du brauchst keine Vorkenntnisse.</p></div>\n'
    h += '<h2 class="sec"><span class="n">?</span>Was möchtest du tun?</h2>\n<div class="tiles">'
    for q, d, pid, alt in START_TILES:
        h += f'<a class="tile{" alt" if alt else ""}" href="anleitungen/{pid}.html"><span class="q">{html.escape(q)}</span><span class="d">{html.escape(d)}</span><span class="go">Zur Anleitung →</span></a>'
    h += '</div>\n'
    h += '<h2 class="sec"><span class="n">★</span>Schnellstart: Verbrauch nach einem Dienst</h2>\n<ol class="steps">'
    for t in ["Menü öffnen → <b>Verbrauchsportal</b> → bei deiner Veranstaltung auf <b>Erfassen</b> tippen.",
              "Produkt suchen, Menge einstellen, <b>Austragen</b> tippen, Objekt und Position bestätigen.",
              "Später im Lager: Reiter <b>Offene Auffüllungen</b> → bei der Position <b>Auffüllen</b> tippen und bestätigen."]:
        h += f'<li><div class="step-text">{t}</div></li>'
    h += '</ol><p>Ausführlich mit Bildern: <a href="anleitungen/verbrauch-ueberblick.html">2.1 Verbrauch dokumentieren: der Überblick</a>.</p>\n'
    h += '<h2 class="sec"><span class="n">☰</span>Alle Abschnitte</h2><div class="tiles">'
    for n, sec in SECTIONS.items():
        h += f'<a class="tile" href="anleitungen/abschnitt-{n}.html"><span class="q">{n}. {html.escape(sec["title"])}</span><span class="d">{html.escape(sec["lead"])}</span><span class="go">Öffnen →</span></a>'
    h += '</div>\n'
    h += '<div class="box"><strong class="t">Hinweise zu dieser Seite</strong><p>Die Bilder stammen aus einer Testumgebung mit Beispieldaten. Die orangen Nummern in den Bildern findest du im Text wieder. Tippe ein Bild an, um es zu vergrößern.</p><p>Adresse und Zugangsdaten für Milan bekommst du von deinem Materialwart. Gib sie nicht weiter.</p></div>\n'
    h += "</main>\n" + foot(root)
    return h

def strip(t):
    return re.sub(r"<[^>]+>", " ", re.sub(r"\{\d\}", "", t))

def build():
    os.makedirs(OUT, exist_ok=True)
    for f in os.listdir(OUT):
        if f.endswith(".html"): os.remove(os.path.join(OUT, f))
    for p in PAGES:
        open(os.path.join(OUT, p["id"] + ".html"), "w", encoding="utf-8").write(page_html(p))
    for n in SECTIONS:
        open(os.path.join(OUT, f"abschnitt-{n}.html"), "w", encoding="utf-8").write(section_html(n))
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(index_html())
    idx = []
    for p in PAGES:
        txt = [p.get("kw", ""), p["kurz"], p.get("wann", "")]
        for b in p["blocks"]:
            if b[0] == "steps": txt += [s["t"] for s in b[1]]
            elif b[0] == "faq": txt += [q for q, a in b[1]]
            elif b[0] in ("h", "p"): txt.append(b[1])
        idx.append({"n": p["num"], "t": p["title"], "u": f'anleitungen/{p["id"]}.html', "k": strip(" ".join(txt))[:900]})
    open(os.path.join(ROOT, "assets", "search-index.js"), "w", encoding="utf-8").write("window.MILAN_INDEX=" + json.dumps(idx, ensure_ascii=False) + ";\n")
    open(os.path.join(ROOT, ".nojekyll"), "w").close()
    print(f"{len(PAGES)} Leitfäden, {len(SECTIONS)} Abschnitte, Startseite und Suchindex erzeugt.")

if __name__ == "__main__":
    build()

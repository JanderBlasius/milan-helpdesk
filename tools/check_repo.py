#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prüft das Repository vor jeder Veröffentlichung. Rückgabewert 0 = alles in Ordnung.
Aufruf: python3 tools/check_repo.py
Prüft: 1) keine sicherheitsrelevanten Inhalte, 2) Links und Bilder, 3) Aufbau der Leitfäden,
4) ob die erzeugten Seiten zum Inhalt passen."""
import html.parser, os, re, sys, tempfile, shutil, subprocess, filecmp

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
fehler, warn = [], []
TEXT_EXT = {".html", ".css", ".js", ".md", ".py", ".yml", ".yaml", ".json", ".txt", ".svg"}

# ---------- 1. sensible Inhalte ----------
VERBOTEN = [
 (r"https?://", "URL im Text (keine Adressen ins Repository)"),
 (r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", "IP-Adresse"),
 (r"\b(localhost|127\.0\.0\.1|0\.0\.0\.0)\b", "lokale Adresse"),
 (r"\.(synology\.me|local|lan|internal|intranet)\b", "interner Hostname"),
 (r"[\w.+-]+@[\w-]+\.[\w.-]+", "E-Mail-Adresse"),
 (r"(?i)\b(docker|synology|postgres(ql)?|uvicorn|fastapi|sqlalchemy|nginx|reverse[- ]?proxy|ddns|portweiterleitung|\.env)\b", "Technik-/Infrastrukturbegriff"),
 (r"(?i)\b(session_secret|secret_key|api[_-]?key|bearer|private[_ ]key|mvs_session|samesite|httponly)\b", "Geheimnis-/Sicherheitsbegriff"),
 (r"(?i)/api/[a-z]", "API-Pfad"),
 (r"(?i)\b(passwort|password|kennwort|pw|pwd)\s*[:=]\s*[^\s<\"']{3,}", "Zugangsdaten-Zuweisung"),
 (r"(?i)(demo|admin|helfer)_demo|Demo-(Admin|Helfer)-Passwort", "Demo-Zugangsdaten"),
 (r"\b(?=[A-Za-z0-9]*\d)(?=[A-Za-z0-9]*[A-Za-z])[A-Za-z0-9]{32,}\b", "lange Zeichenfolge (Schlüssel/Token?)"),
 (r"(?i)\b(ssh|sftp|rsync)\b|\bport\s*\d{2,5}\b", "Zugriffs-/Portangabe"),
 (r"(?<!\d)(\+49|0049|0\d{3,5})[\s/-]?\d{3,}", "Telefonnummer"),
 (r"(?i)\b(ghp_|github_pat_|AKIA|xox[bap]-)", "Token-Präfix"),
]
AUSNAHMEN = {"tools/check_repo.py", "docs/INHALTSREGELN.md", "README.md", ".github/workflows/pruefung.yml"}
def texte():
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in (".git", "__pycache__")]
        for f in fn:
            p = os.path.join(dp, f)
            if os.path.splitext(f)[1].lower() in TEXT_EXT: yield p
for p in texte():
    rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
    if rel in AUSNAHMEN: continue
    src = open(p, encoding="utf-8", errors="replace").read()
    if rel == "assets/search-index.js": pass
    for pat, grund in VERBOTEN:
        for m in re.finditer(pat, src):
            # CSP-Zeile und Bildnamen enthalten harmlose Muster
            line = src[max(0, src.rfind("\n", 0, m.start())):src.find("\n", m.end())]
            if "Content-Security-Policy" in line or "w3.org" in m.group(0): continue
            fehler.append(f"{rel}: {grund}: „{m.group(0)[:60]}“")
# Bildmetadaten (EXIF/Text-Chunks) dürfen nichts enthalten
try:
    from PIL import Image
    for f in sorted(os.listdir(os.path.join(ROOT, "assets", "img"))):
        im = Image.open(os.path.join(ROOT, "assets", "img", f))
        meta = {k: v for k, v in im.info.items() if k in ("exif", "Software", "Comment", "Description", "Author", "Title", "XML:com.adobe.xmp")}
        if meta: fehler.append(f"assets/img/{f}: enthält Metadaten {list(meta)}")
except ImportError:
    warn.append("Pillow fehlt: Bildmetadaten nicht geprüft (pip install pillow)")

# ---------- 2. Links und Bilder ----------
class L(html.parser.HTMLParser):
    def __init__(s): super().__init__(); s.refs = []; s.imgs = []; s.ids = set(); s.title = ""; s._t = False
    def handle_starttag(s, t, a):
        a = dict(a)
        if "id" in a: s.ids.add(a["id"])
        if t in ("a", "link") and a.get("href"): s.refs.append(a["href"])
        if t in ("img", "script") and a.get("src"): s.refs.append(a["src"])
        if t == "img": s.imgs.append(a)
        if t == "title": s._t = True
    def handle_data(s, d):
        if s._t: s.title += d
    def handle_endtag(s, t):
        if t == "title": s._t = False
html_files = []
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d not in (".git", "__pycache__")]
    html_files += [os.path.join(dp, f) for f in fn if f.endswith(".html")]
benutzt = set(); erreichbar = set()
for p in html_files:
    rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
    pr = L(); pr.feed(open(p, encoding="utf-8").read())
    if not pr.title.strip(): fehler.append(f"{rel}: kein Titel")
    for r in pr.refs:
        if r.startswith(("#", "mailto:", "tel:")): continue
        if re.match(r"^[a-z]+:", r) or r.startswith("//"): fehler.append(f"{rel}: externer Verweis {r}"); continue
        t = os.path.normpath(os.path.join(os.path.dirname(p), r.split("#")[0]))
        if not os.path.exists(t): fehler.append(f"{rel}: toter Verweis {r}")
        else:
            benutzt.add(os.path.relpath(t, ROOT).replace(os.sep, "/")); erreichbar.add(os.path.relpath(t, ROOT).replace(os.sep, "/"))
    for im in pr.imgs:
        if not im.get("alt", "").strip(): fehler.append(f"{rel}: Bild ohne Alternativtext {im.get('src')}")
for f in os.listdir(os.path.join(ROOT, "assets", "img")):
    if f"assets/img/{f}" not in benutzt: warn.append(f"ungenutztes Bild: assets/img/{f}")
for p in html_files:
    rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
    if rel != "index.html" and rel not in erreichbar: fehler.append(f"{rel}: von keiner Seite verlinkt")

# ---------- 3. Aufbau der Leitfäden ----------
from content_b import PAGES
from content_a import SECTIONS
ids = {p["id"] for p in PAGES}
for p in PAGES:
    w = p["id"]
    if p["sec"] not in SECTIONS: fehler.append(f"{w}: Abschnitt unbekannt")
    if len(p.get("kurz", "")) < 40: fehler.append(f"{w}: Kurzfassung fehlt oder zu kurz")
    kinds = [b[0] for b in p["blocks"]]
    if not set(kinds) & {"steps", "table", "list", "flow", "tiles", "faq"}: fehler.append(f"{w}: kein Inhaltsbaustein (Schritte/Tabelle/Liste)")
    if not p.get("weiter"): fehler.append(f"{w}: kein „Wie geht’s weiter?“")
    for x in p.get("weiter", []):
        if x not in ids: fehler.append(f"{w}: weiter → unbekannte Seite {x}")
    if "faq" not in kinds and p["sec"] in (1, 2, 3, 4, 5) and not any(b[0] in ("note", "warn", "stop") for b in p["blocks"]):
        warn.append(f"{w}: weder Problemhilfe noch Hinweis")
    for b in p["blocks"]:
        if b[0] == "steps":
            for s in b[1]:
                if s.get("img") and (not s.get("alt") or not s.get("cap")): fehler.append(f"{w}: Bild ohne alt/Bildunterschrift")
                # Markierungen im Schritttext müssen in der Bildunterschrift erklärt sein
                if s.get("img"):
                    marks = set(re.findall(r"\{(\d)\}", s["t"]))
                    if marks and not marks <= set(re.findall(r"\{(\d)\}", s["cap"])):
                        fehler.append(f"{w}: Markierung im Text, aber nicht in der Bildunterschrift erklärt ({s['img']})")
    txt = repr(p)
    if re.search(r"\bTODO|\bXXX|Platzhalter-?text|Lorem", txt): fehler.append(f"{w}: Platzhaltertext")

# ---------- 4. erzeugte Seiten aktuell? ----------
tmp = tempfile.mkdtemp()
try:
    for d in ("tools", "assets"): shutil.copytree(os.path.join(ROOT, d), os.path.join(tmp, d))
    subprocess.run([sys.executable, os.path.join(tmp, "tools", "build_site.py")], check=True, capture_output=True)
    for rel in ["index.html"] + ["anleitungen/" + f for f in sorted(os.listdir(os.path.join(tmp, "anleitungen")))]:
        a, b = os.path.join(tmp, rel), os.path.join(ROOT, rel)
        if not os.path.exists(b) or not filecmp.cmp(a, b, shallow=False): fehler.append(f"{rel}: nicht aktuell (tools/build_site.py ausführen)")
    for f in os.listdir(os.path.join(ROOT, "anleitungen")):
        if f.endswith(".html") and not os.path.exists(os.path.join(tmp, "anleitungen", f)): fehler.append(f"anleitungen/{f}: Überbleibsel")
finally:
    shutil.rmtree(tmp, ignore_errors=True)

warn = list(dict.fromkeys(warn)); fehler = list(dict.fromkeys(fehler))
for w in warn: print("WARNUNG:", w)
for f in fehler[:80]: print("FEHLER :", f)
if len(fehler) > 80: print(f"... und {len(fehler) - 80} weitere")
print(f"\n{len(html_files)} HTML-Seiten, {len(PAGES)} Leitfäden geprüft: {len(fehler)} Fehler, {len(warn)} Warnungen.")
sys.exit(1 if fehler else 0)

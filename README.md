# Milan Helpdesk

Anleitungen für Helferinnen und Helfer zur Nutzung von **Milan Materialmanagement**.
Ziel: Helfer finden die richtige Anleitung ohne Hilfe und können die Schritte ohne Vorkenntnisse selbst ausführen.

Die Seite ist eine statische Webseite (nur HTML, CSS und etwas JavaScript, keine externen Dienste, keine Cookies).

## Inhalt

| Abschnitt | Themen |
|---|---|
| 1 Erste Schritte | Anmelden, Passwort ändern, Aufbau der App |
| 2 Verbrauch dokumentieren | Veranstaltung wählen, Austragen, Korrigieren, Auffüllen, Bericht |
| 3 Einsatzmittel kontrollieren | Position finden, EP-Kontrolle, Fehler melden, Chargen, Verlauf |
| 4 Massenscan | Wann und warum, Durchführung |
| 5 Scannen | Codes scannen, wenn der Scanner nicht funktioniert |
| 6 Aufträge | Ansehen, anlegen, bearbeiten |
| 7 Nachschlagen | Produkte, Lagerbestand und Lagerorte, Veranstaltungen |
| 8 Hilfe und Begriffe | Häufige Fragen, Begriffe, Rechte |

Einstieg: `index.html` (Startseite mit der Frage „Was möchtest du tun?“).

## Aufbau des Repositorys

```
index.html            Startseite
anleitungen/          erzeugte Seiten (nicht von Hand bearbeiten)
assets/               Gestaltung, Skripte, Bilder (assets/img)
tools/
  content_a.py        Inhalte Abschnitt 1–3
  content_b.py        Inhalte Abschnitt 4–8 (und Zusammenführung)
  build_site.py       erzeugt die Seiten aus den Inhalten
  check_repo.py       Sicherheits-, Link- und Strukturprüfung
docs/INHALTSREGELN.md Regeln: was nicht ins Repository darf, Stil, Screenshots
```

## Inhalte ändern

1. Text in `tools/content_a.py` oder `tools/content_b.py` ändern. Jeder Eintrag ist ein Leitfaden (`P(id=…, title=…, kurz=…, blocks=[…])`).
2. Seiten neu erzeugen: `python3 tools/build_site.py`
3. Prüfen: `python3 tools/check_repo.py` (muss **0 Fehler** melden, benötigt `pillow`)
4. Änderungen einchecken. Die Prüfung läuft zusätzlich automatisch bei jedem Push.

Bausteine in `blocks`: `("h", …)`, `("p", …)`, `("list", […])`, `("steps", […])` mit Bild und Markierungen, `("note"|"warn"|"stop", Titel, Text)`, `("table", Kopf, Zeilen)`, `("faq", […])`, `("flow", …)`, `("tiles", …)`.
Markierungen `{1}`, `{2}` … im Text entsprechen den orangen Nummern im Bild.

## Screenshots erneuern

Wenn sich die Oberfläche von Milan ändert, müssen die Bilder in `assets/img` neu aufgenommen werden, in einer **Testumgebung mit erfundenen Daten** (siehe `docs/INHALTSREGELN.md`). Bildformat: Hochformat, 390 × 844 Pixel Fensterbreite, auf 585 Pixel Breite verkleinert, mit orangen nummerierten Rahmen als Markierung (`#E8590C`).

## Veröffentlichen (GitHub Pages)

Im Repository unter „Settings → Pages“ den Branch `main` und den Ordner `/ (root)` wählen. Die Seiten sind so gebaut, dass sie ohne Zusatzdienste laufen (`.nojekyll` liegt bei). Die Seiten sind mit „noindex“ markiert und sollen nicht in Suchmaschinen erscheinen.

## Wichtig: keine sicherheitsrelevanten Inhalte

In diesem Repository stehen **keine** Adresse von Milan, keine Zugangsdaten, keine Angaben zu Server oder Netzwerk und keine echten Daten. Adresse und Zugang bekommen Helfer von ihrem Materialwart. Details: `docs/INHALTSREGELN.md`.

# Inhaltsregeln für dieses Repository

Dieses Repository ist öffentlich lesbar (bzw. wird als öffentliche Seite ausgeliefert). Deshalb gilt:

## Was niemals ins Repository darf

| Kategorie | Beispiele |
|---|---|
| Adressen | URL oder Adresse der Milan-Installation, IP-Adressen, Hostnamen, Ports, DDNS-Namen |
| Zugangsdaten | Benutzernamen echter Konten, Passwörter, Passwortbeispiele, Tokens, Schlüssel |
| Infrastruktur | Angaben zu Server, Netzwerk, Container, Datenbank, Backup, Firewall, Schutzmaßnahmen |
| Schnittstellen | API-Pfade, interne Funktionsnamen, Fehlertexte aus Protokollen |
| Personen | Echte Namen, Telefonnummern, E-Mail-Adressen, Dienstkürzel, Fotos von Personen |
| Verwaltungsabläufe | Wie Konten, Rechte oder Freigaben vergeben oder umgangen werden |
| Echte Daten | Screenshots mit echten Veranstaltungen, Beständen, Personen oder Chargen |

Stattdessen schreiben wir: „Adresse und Zugangsdaten bekommst du von deinem Materialwart.“

## Screenshots

* Nur aus einer Testumgebung mit **erfundenen** Daten aufnehmen (zum Beispiel „RTW 1 (Demo)“, „Max Muster“).
* Vor dem Einchecken prüfen: Adressleiste, Benutzerliste, Passwortfelder und Hinweisbanner dürfen nichts Echtes zeigen.
* Orange nummerierte Markierungen gehören zu den Nummern im Text. Bildunterschrift und Text müssen dieselben Nummern erklären.
* Bilder ohne Metadaten speichern (kein EXIF, keine Programmkommentare).

## Schreibstil

* Du-Form, kurze Sätze, ein Handgriff pro Schritt, Bezeichnungen **genau so** wie in Milan.
* Jede Anleitung hat: Kurzfassung, „Wann brauchst du das?“, Voraussetzungen (falls nötig), nummerierte Schritte, „Wenn etwas nicht klappt“ oder einen Hinweis, „Wie geht’s weiter?“.
* Keine Fachbegriffe der Technik. Wenn ein Wort aus Milan erklärt werden muss, ins Glossar aufnehmen.
* Nichts erklären, was Helfer nicht tun dürfen. Stattdessen auf die Materialverwaltung verweisen.

## Vor jeder Veröffentlichung

```bash
python3 tools/build_site.py     # Seiten aus den Inhalten neu erzeugen
python3 tools/check_repo.py     # Sicherheits-, Link- und Strukturprüfung (muss 0 Fehler melden)
```

Die gleiche Prüfung läuft automatisch bei jedem Push (siehe `.github/workflows/pruefung.yml`).

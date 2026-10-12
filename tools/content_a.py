# -*- coding: utf-8 -*-
"""Inhalte Abschnitt 1-3. Nur Anleitungstexte, keine Zugangsdaten, keine Adressen, keine Technikdetails."""

SECTIONS = {
 1: dict(title="Erste Schritte", lead="Anmelden, Passwort ändern und sich in Milan zurechtfinden. Das brauchst du einmal – danach nie wieder."),
 2: dict(title="Verbrauch dokumentieren", lead="Nach einem Dienst oder Einsatz: was verbraucht wurde eintragen und das Material später wieder auffüllen."),
 3: dict(title="Einsatzmittel kontrollieren", lead="Fahrzeug, Rucksack oder Koffer prüfen: ist alles da, ist alles in Ordnung, ist nichts abgelaufen?"),
 4: dict(title="Massenscan", lead="Ein ganzes Modul auf einmal erfassen, indem jede Packung einzeln gescannt wird."),
 5: dict(title="Scannen", lead="Codes mit der Handykamera lesen, damit du nicht tippen musst."),
 6: dict(title="Aufträge", lead="Aufgaben und Meldungen: etwas ansehen, melden oder abhaken."),
 7: dict(title="Nachschlagen", lead="Wo liegt etwas? Wie viel ist da? Was läuft gerade? Hier darfst du alles ansehen."),
 8: dict(title="Hilfe und Begriffe", lead="Häufige Fragen, Begriffe einfach erklärt und was du nicht selbst machen musst."),
}

PAGES = []
def P(**k): PAGES.append(k)

# ---------------------------------------------------------------- 1
P(id="anmelden", sec=1, num="1.1", title="Anmelden und Abmelden",
  kw="login anmelden einloggen abmelden ausloggen benutzername passwort sitzung",
  kurz="Mit Benutzername und Passwort anmelden. Danach immer über das Profil-Symbol oben rechts abmelden, besonders auf fremden oder gemeinsam genutzten Geräten.",
  wann="Du öffnest Milan zum ersten Mal oder wurdest automatisch abgemeldet.",
  vorher=["Die Adresse von Milan, dein Benutzername und dein Passwort. Die bekommst du von deinem Materialwart oder der Administration.",
          "Ein Handy, Tablet oder Computer mit Internet."],
  blocks=[
   ("steps",[
     dict(t="Öffne Milan im Browser. Tipp: Speichere die Seite als Lesezeichen oder lege sie auf deinen Startbildschirm, dann findest du sie schnell wieder.", img=None),
     dict(t="Tippe in das Feld Benutzername {1} und gib deinen Benutzernamen ein. Tippe dann in das Feld Passwort {2} und gib dein Passwort ein.", img="login", alt="Anmeldeseite von Milan mit den Feldern Benutzername und Passwort sowie dem Button Anmelden", cap="Die Anmeldeseite: {1} Benutzername, {2} Passwort, {3} Anmelden. Die Felder sind hier absichtlich leer."),
     dict(t="Tippe auf Anmelden {3}.", img=None),
     dict(t="Du siehst jetzt das Dashboard (die Startseite). Du bist angemeldet.", img=None),
   ]),
   ("h","Abmelden"),
   ("steps",[
     dict(t="Tippe oben rechts auf das Profil-Symbol (Kreis mit Person).", img=None),
     dict(t="Im Menü steht oben dein Name. Bei {1} siehst du, wie lange es bis zur automatischen Abmeldung dauert (Anzeige „Abmeldung in“). Tippe auf Abmelden {3}.", img="profilmenue", alt="Geöffnetes Profil-Menü mit Namen, Abmelde-Countdown, Passwort ändern und Abmelden", cap="Das Profil-Menü. {1} Countdown, {2} Passwort ändern, {3} Abmelden."),
   ]),
   ("warn","Auf fremden Geräten","<p>Melde dich immer ab, wenn du ein Gerät mit anderen teilst. Gib dein Passwort nie weiter. Alles, was unter deinem Namen erfasst wird, ist dir zugeordnet.</p>"),
   ("note","Automatische Abmeldung","<p>Wenn du eine Zeit lang nichts machst, meldet Milan dich aus Sicherheitsgründen automatisch ab. Das ist normal. Melde dich einfach neu an. Bereits gespeicherte Eingaben bleiben erhalten.</p>"),
   ("faq",[
     ("Ich habe mein Passwort vergessen.","<p>Wende dich an deinen Materialwart oder die Administration. Dort kann ein neues Passwort vergeben werden. Du kannst es danach selbst ändern (siehe <a href=\"passwort-aendern.html\">Passwort ändern</a>).</p>"),
     ("Die Anmeldung klappt nicht.","<p>Prüfe Groß- und Kleinschreibung und ob die Feststelltaste aktiv ist. Klappt es weiterhin nicht, melde dich bei deinem Materialwart. Probiere nicht viele Varianten durch.</p>"),
     ("Ich sehe die Meldung, dass meine Sitzung abgelaufen ist.","<p>Das ist die automatische Abmeldung. Melde dich einfach neu an.</p>"),
   ]),
  ],
  weiter=["passwort-aendern","app-ueberblick"])

P(id="passwort-aendern", sec=1, num="1.2", title="Passwort ändern",
  kw="passwort ändern kennwort wechseln sicher",
  kurz="Profil-Symbol oben rechts → Passwort ändern → altes und neues Passwort eingeben → Speichern.",
  wann="Du hast ein Startpasswort bekommen, oder du möchtest dein Passwort aus Sicherheitsgründen wechseln.",
  vorher=["Du bist angemeldet und kennst dein aktuelles Passwort."],
  blocks=[
   ("steps",[
     dict(t="Tippe oben rechts auf das Profil-Symbol und dann auf Passwort ändern {2}.", img="profilmenue", alt="Profil-Menü mit der Schaltfläche Passwort ändern", cap="Passwort ändern findest du im Profil-Menü ({2})."),
     dict(t="Gib bei {1} dein aktuelles Passwort ein und bei {2} dein neues Passwort.", img="passwort-dialog", alt="Dialog Passwort ändern mit den Feldern Aktuelles Passwort und Neues Passwort", cap="{1} Aktuelles Passwort, {2} Neues Passwort, {3} Speichern."),
     dict(t="Tippe auf Speichern {3}.", img=None),
   ]),
   ("h","So wird ein gutes Passwort"),
   ("list",["<strong>Lang statt kompliziert:</strong> Mehrere zusammenhanglose Wörter hintereinander sind besser als ein kurzes Wort mit Sonderzeichen.",
            "<strong>Nur für Milan:</strong> Verwende es nirgendwo anders.",
            "<strong>Nicht weitergeben:</strong> Auch nicht an Kolleginnen und Kollegen. Wer Zugang braucht, bekommt einen eigenen.",
            "<strong>Nicht auf Zettel am Gerät.</strong>"]),
   ("faq",[("Es kommt eine Fehlermeldung beim Speichern.","<p>Meist stimmt das aktuelle Passwort nicht, oder das neue ist zu kurz. Prüfe beides und versuche es erneut. Sonst frage deinen Materialwart.</p>")]),
  ],
  weiter=["app-ueberblick"])

P(id="app-ueberblick", sec=1, num="1.3", title="Die App im Überblick",
  kw="menü navigation dashboard startseite scan button profil überblick wo finde ich",
  kurz="Oben links das Menü, oben rechts dein Profil, unten rechts der Scan-Button. Für dich sind vor allem Verbrauchsportal, Einsatzpositionen und Aufträge wichtig.",
  wann="Du willst wissen, wo in Milan was zu finden ist.",
  blocks=[
   ("steps",[
     dict(t="Nach der Anmeldung siehst du das Dashboard. Es zeigt Kennzahlen wie „Offene Aufträge“ oder „Laufende Veranstaltungen“. Tippe auf eine aufklappbare Zeile wie „Kritische Verfallsdaten“, um Einzelheiten zu sehen.", img="start-uebersicht", alt="Dashboard mit drei markierten Bedienelementen: Menü-Symbol, Profil-Symbol und Scan-Button", cap="{1} Menü öffnen, {2} Profil, {3} Scan-Button."),
     dict(t="Tippe auf das Menü-Symbol {1} (drei Striche). Das Menü hat drei Gruppen: Material, Organisation und Veranstaltungen. Tippe auf eine Gruppe, um sie auf- oder zuzuklappen.", img="menue-organisation", alt="Geöffnetes Menü mit aufgeklappten Gruppen Organisation und Veranstaltungen", cap="Hier: {1} Aufträge, {2} Veranstaltungen, {3} Verbrauchsportal."),
     dict(t="In der Gruppe Material findest du Einsatzpositionen, Produkte und Lagerbestand.", img="menue-material", alt="Menü mit aufgeklappter Gruppe Material", cap="{1} Einsatzpositionen, {2} Produkte, {3} Lagerbestand."),
     dict(t="Das Milan-Logo oben im Menü bringt dich jederzeit zurück zum Dashboard.", img=None),
     dict(t="Der runde blaue Scan-Button {3} unten rechts ist auf fast jeder Seite da. Damit liest du Codes mit der Kamera (siehe <a href=\"scan-button.html\">Scannen</a>).", img=None),
   ]),
   ("h","Welche Menüpunkte sind für dich?"),
   ("p","Milan zeigt dir mehr Menüpunkte, als du brauchst. Manche sind für den Materialwart oder die Administration gedacht. Das ist kein Fehler. Diese Übersicht hilft dir:"),
   ("table",["Menüpunkt","Für dich?","Wofür"],[
     ["Verbrauchsportal","<span class='pill yes'>Ja</span>","Verbrauch eintragen und Material auffüllen"],
     ["Einsatzpositionen","<span class='pill yes'>Ja</span>","Einsatzmittel kontrollieren, Massenscan"],
     ["Aufträge","<span class='pill yes'>Ja</span>","Aufgaben ansehen, melden, abhaken"],
     ["Veranstaltungen","<span class='pill view'>Ansehen</span>","Berichte und Stand der Auffüllungen"],
     ["Produkte, Lagerbestand, Lagerorte, Objekte","<span class='pill view'>Ansehen</span>","Nachschlagen"],
     ["Personal, Personalausleihen","<span class='pill view'>Ansehen</span>","Nur Übersicht, Änderungen macht die Verwaltung"],
     ["Bestellungen, Einkaufsstandards, Zulieferer","<span class='pill view'>Ansehen</span>","Einkauf, wird von der Materialverwaltung gepflegt"],
     ["Protokollapp-Sync, HiOrg-Integration, Analoge Erfassung, Verbrauchsbericht Import","<span class='pill no'>Nicht für dich</span>","Verwaltungsaufgaben. Bei dir funktionieren sie nicht."],
   ]),
   ("note","Gesperrte Knöpfe","<p>Siehst du einen Knopf, der bei dir eine Fehlermeldung wie „Keine Berechtigung“ auslöst? Dann ist die Funktion für Materialwart oder Administration vorgesehen. Gib einfach Bescheid, wenn du sie brauchst.</p>"),
   ("note","Profil","<p>Über das Profil-Symbol änderst du dein Passwort und meldest dich ab (siehe <a href=\"anmelden.html\">Anmelden und Abmelden</a>).</p>"),
  ],
  weiter=["verbrauch-ueberblick","ep-finden","scan-button"])

# ---------------------------------------------------------------- 2
P(id="verbrauch-ueberblick", sec=2, num="2.1", title="Verbrauch dokumentieren: der Überblick",
  kw="verbrauch verbrauchsportal austragen auffüllen ablauf überblick sanitätsdienst veranstaltung",
  kurz="Zwei Schritte: 1) Austragen, was verbraucht wurde. 2) Später das Material auffüllen und bestätigen. Beides machst du im Verbrauchsportal.",
  wann="Du warst bei einer Veranstaltung oder einem Dienst und hast Material verbraucht.",
  blocks=[
   ("p","Das Verbrauchsportal ist der wichtigste Ort für dich. Dort hält Milan fest, was bei einer Veranstaltung aus welchem Fahrzeug, Rucksack oder Koffer verbraucht wurde und ob es schon wieder aufgefüllt ist."),
   ("flow",[("1 · Veranstaltung wählen","Du suchst die laufende Veranstaltung aus.",False),
            ("2 · Austragen","Du trägst ein, was verbraucht wurde, am besten direkt nach dem Dienst.",False),
            ("3 · Auffüllen","Später im Lager: Material auffüllen und in Milan bestätigen.",False),
            ("4 · Abschluss","Das erledigt der Materialwart. Du musst nichts tun.",True)]),
   ("h","Wichtig zu wissen"),
   ("list",["<strong>Austragen und Auffüllen müssen nicht dieselbe Person machen.</strong> Unter „Offene Auffüllungen“ siehst du alles, was noch fehlt, auch von anderen.",
            "<strong>Du siehst nur laufende Veranstaltungen.</strong> Ist die Veranstaltung beendet, melde dich beim Materialwart.",
            "<strong>Nach dem Auffüllen ist ein Eintrag gesperrt.</strong> Er lässt sich dann nicht mehr ändern. Prüfe also vorher.",
            "<strong>Die Auswahl der Veranstaltung bleibt aktiv,</strong> solange du angemeldet bist, auch wenn du zwischendurch andere Seiten öffnest."]),
   ("note","Nicht sicher, was zu tun ist?","<p>Lieber kurz beim Materialwart nachfragen, als etwas Falsches einzutragen. Eingaben lassen sich nur eingeschränkt zurücknehmen.</p>"),
   ("h","Los geht’s"),
   ("tiles",[("Veranstaltung wählen","Der erste Schritt","veranstaltung-waehlen"),
             ("Material austragen","Eintragen, was verbraucht wurde","austragen"),
             ("Material auffüllen","Auffüllen bestätigen","auffuellen")]),
  ],
  weiter=["veranstaltung-waehlen"])

P(id="veranstaltung-waehlen", sec=2, num="2.2", title="Veranstaltung wählen",
  kw="veranstaltung wählen erfassen auswahl sitzung verbrauchsportal öffnen laufend",
  kurz="Menü → Verbrauchsportal → bei deiner Veranstaltung auf Erfassen tippen. Prüfe den Titel, bevor du loslegst.",
  wann="Du willst Verbrauch eintragen oder Material auffüllen.",
  vorher=["Die Veranstaltung muss in Milan angelegt sein und laufen. Das macht die Materialverwaltung."],
  blocks=[
   ("steps",[
     dict(t="Tippe auf das Menü-Symbol, öffne die Gruppe Veranstaltungen und tippe auf Verbrauchsportal.", img="menue-organisation", alt="Menü mit Gruppe Veranstaltungen und Eintrag Verbrauchsportal", cap="Das Verbrauchsportal findest du in der Gruppe Veranstaltungen ({3})."),
     dict(t="Du siehst die Liste der laufenden Veranstaltungen. Suche deine Veranstaltung. Mit dem Suchfeld oben findest du sie nach Titel oder Kurztitel. Tippe bei ihr auf Erfassen {1}.", img="vp-01-auswahl", alt="Verbrauchsportal mit der Liste der laufenden Veranstaltungen und dem Button Erfassen", cap="{1} Erfassen. Die Veranstaltung ist hier ein Beispiel."),
     dict(t="Jetzt öffnet sich die Erfassungsansicht. Oben bei {1} steht die gewählte Veranstaltung. Bei {2} siehst du die drei Reiter Austragen, Offene Auffüllungen und Bericht. Bei {3} wählst du, wie du Material findest.", img="vp-02-erfassung", alt="Erfassungsansicht mit Veranstaltung, Reitern und Auswahl Über Produkte oder Über Einsatzpositionen", cap="{1} Veranstaltung, {2} Reiter, {3} Weg zur Auswahl."),
   ]),
   ("warn","Richtige Veranstaltung?","<p>Lies den Titel oben genau. Verwechsle nicht ähnliche Veranstaltungen. Eine falsche Zuordnung fällt erst später auf. Im Zweifel vergleiche mit der Nummer oder dem Namen aus deiner Dienstplanung.</p>"),
   ("faq",[
     ("Meine Veranstaltung steht nicht in der Liste.","<p>Es werden nur laufende Veranstaltungen angezeigt. Ist deine nicht dabei, wurde sie noch nicht angelegt oder ist schon beendet. Melde dich beim Materialwart.</p>"),
     ("Es steht „Aktuell läuft keine Veranstaltung“.","<p>Dann gibt es gerade keine laufende Veranstaltung in Milan. Frage beim Materialwart nach.</p>"),
     ("Wie wechsle ich zu einer anderen Veranstaltung?","<p>Tippe in der Erfassungsansicht auf Sitzung beenden. Danach kannst du eine andere wählen (siehe <a href=\"verbrauch-bericht.html\">Bericht und Sitzung beenden</a>).</p>"),
   ]),
  ],
  weiter=["austragen"])

P(id="austragen", sec=2, num="2.3", title="Material austragen",
  kw="austragen verbrauch eintragen verbraucht menge produkt einsatzposition objekt nochmal",
  kurz="Im Reiter Austragen das Produkt suchen, Menge einstellen, Austragen tippen, Objekt und Position bestätigen. Fertig.",
  wann="Du hast bei einer Veranstaltung Material aus einem Fahrzeug, Rucksack oder Koffer verbraucht.",
  vorher=["Du hast die Veranstaltung gewählt (siehe <a href=\"veranstaltung-waehlen.html\">Veranstaltung wählen</a>).",
          "Du weißt, was verbraucht wurde, wie viel und aus welchem Fahrzeug oder Rucksack (das „Objekt“)."],
  blocks=[
   ("h","Weg A: Über Produkte (der schnellste Weg)"),
   ("steps",[
     dict(t="Bleibe im Reiter Austragen und wähle Über Produkte. Suche das Produkt, entweder mit dem Suchfeld oder durch Blättern. Zuletzt ausgetragene Produkte stehen oben unter „Zuletzt in dieser Sitzung ausgetragen“. Dort kannst du mit Nochmal austragen schnell wiederholen.", img=None),
     dict(t="Stelle bei dem Produkt die Menge ein. Mit + und − {1} zählst du hoch und runter, du kannst die Zahl auch direkt eintippen. Tippe dann auf Austragen {2}.", img="vp-03-menge", alt="Produktkarte Verbandpäckchen groß mit Mengenfeld und Button Austragen", cap="{1} Menge, {2} Austragen."),
     dict(t="Es öffnet sich ein Dialog mit drei Schritten. Schritt 1: Tippe das Objekt an, aus dem das Material kam {1}. Das ist dein Fahrzeug, Rucksack oder Koffer.", img="vp-04-dialog-objekt", alt="Dialog Austragen, Schritt 1 Objekt wählen", cap="Schritt 1: {1} Objekt wählen."),
     dict(t="Schritt 2: Milan zeigt die passende Einsatzposition. Bei nur einer Möglichkeit steht „bitte bestätigen“. Tippe sie an {2}. Schritt 3: Prüfe die Menge {3} und tippe auf Austragen {4}.", img="vp-05-dialog-ep", alt="Dialog Austragen mit gewählter Einsatzposition, Menge und Button Austragen", cap="{2} Position, {3} Menge, {4} Austragen."),
     dict(t="Unten erscheint kurz „Ausgetragen.“. Der Eintrag ist gespeichert. Er taucht jetzt im Reiter Offene Auffüllungen auf.", img="vp-06-ausgetragen", alt="Bestätigung Ausgetragen am unteren Bildrand", cap="Die Bestätigung verschwindet nach wenigen Sekunden von selbst."),
   ]),
   ("h","Weg B: Über Einsatzpositionen"),
   ("p","Dieser Weg passt, wenn du genau weißt, aus welchem Fahrzeug oder Rucksack das Material kam. Du wählst zuerst den Ort, dann das Produkt."),
   ("steps",[
     dict(t="Tippe auf Über Einsatzpositionen {1}. Die Liste ist nach Objekten sortiert {2}. Mit dem Suchfeld findest du eine Position auch über Produktnamen oder Pfad.", img="vp-07-ueber-ep", alt="Liste der Einsatzpositionen nach Objekt gruppiert mit Button Verbrauch erfassen", cap="{1} Weg wählen, {2} Gruppe nach Objekt."),
     dict(t="Tippe bei der richtigen Position auf Verbrauch erfassen. Weil Ort und Produkt schon feststehen, musst du nur noch die Menge {1} prüfen und auf Austragen {2} tippen.", img="vp-07b-ep-dialog", alt="Dialog mit Menge und Button Austragen für eine bereits gewählte Position", cap="{1} Menge, {2} Austragen."),
   ]),
   ("h","Weg C: Per Scan"),
   ("p","Tippe auf Position/Modul scannen und halte die Kamera auf das Etikett des Moduls oder der Position. Milan wählt dann den richtigen Eintrag. Wie das Scannen funktioniert, steht unter <a href=\"scan-button.html\">Scannen</a>."),
   ("warn","Wenn du den Ort nicht kennst","<p>In der Objektliste gibt es den Eintrag „999 – Unbekannt / Platzhalter“. Wähle ihn nur, wenn du wirklich nicht weißt, woher das Material stammt. Sage danach dem Materialwart Bescheid, damit er es zuordnen kann.</p>"),
   ("faq",[
     ("Ich habe die falsche Menge eingetragen.","<p>Das lässt sich korrigieren, solange noch nicht aufgefüllt wurde. Siehe <a href=\"austragen-korrigieren.html\">Eintrag korrigieren oder entfernen</a>.</p>"),
     ("Das Produkt finde ich nicht.","<p>Probiere einen kürzeren Suchbegriff oder die Kategorie. Findest du es trotzdem nicht, ist es nicht in Milan angelegt. Melde das dem Materialwart.</p>"),
     ("Muss ich dazu im Fahrzeug sein?","<p>Nein. Du kannst das von überall tun, wo du Milan öffnen kannst.</p>"),
   ]),
  ],
  weiter=["austragen-korrigieren","auffuellen"])

P(id="austragen-korrigieren", sec=2, num="2.4", title="Eintrag korrigieren oder entfernen",
  kw="korrigieren ändern menge entfernen löschen falsch alle positionen verbrauch rückgängig",
  kurz="Unten auf Alle Positionen tippen. Dort kannst du die Menge ändern oder den Eintrag entfernen, solange er noch nicht aufgefüllt ist.",
  wann="Du hast eine falsche Menge oder das falsche Produkt eingetragen.",
  vorher=["Der Eintrag ist noch nicht als aufgefüllt bestätigt."],
  blocks=[
   ("steps",[
     dict(t="Scrolle in der Erfassungsansicht nach unten. Dort siehst du eine dunkle Leiste mit den Zahlen „ausgetragen“, „aufgefüllt“ und „offen“. Tippe auf Alle Positionen.", img="vp-09b-alle-positionen-knopf", alt="Reiter Offene Auffüllungen mit der dunklen Kennzahlen-Leiste und dem markierten Button Alle Positionen", cap="{1} Alle Positionen."),
     dict(t="Du siehst alle Einträge dieser Veranstaltung. Mit − und + {1} änderst du die Menge. Mit Entfernen {2} löschst du einen Eintrag, der gar nicht hätte angelegt werden sollen. Zur Sicherheit fragt Milan eventuell noch einmal nach. Graue Einträge mit dem Vermerk „aufgefüllt“ sind schon bestätigt und lassen sich nicht mehr ändern.", img="vp-08-alle-positionen", alt="Dialog Alle Positionen dieser Veranstaltung mit Mengenfeldern, Entfernen und zwei bereits aufgefüllten, grauen Einträgen", cap="{1} Menge ändern, {2} Entfernen, {3} Schließen."),
     dict(t="Tippe unten auf Schließen {3}. Fertig.", img=None),
   ]),
   ("note","Falsch erfasst nach dem Auffüllen?","<p>Einträge, die bereits aufgefüllt sind, sind schreibgeschützt. Das ist Absicht, damit dokumentierte Materialbewegungen nicht heimlich verändert werden. Wende dich in diesem Fall an deinen Materialwart.</p>"),
   ("note","Nur diese Veranstaltung","<p>Du kannst nur Einträge der Veranstaltung ändern, die du gerade gewählt hast.</p>"),
  ],
  weiter=["auffuellen"])

P(id="auffuellen", sec=2, num="2.5", title="Material auffüllen",
  kw="auffüllen aufgefüllt offene auffüllungen verfallsdatum charge bestätigen nachfüllen ablaufdatum",
  kurz="Reiter Offene Auffüllungen → bei der Position auf Auffüllen tippen. Bei Produkten mit Verfallsdatum trägst du Datum und Menge ein, sonst bestätigst du nur.",
  wann="Du hast verbrauchtes Material wieder in das Fahrzeug, den Rucksack oder den Koffer gelegt.",
  vorher=["Das Material ist wirklich schon aufgefüllt. Bestätige erst, wenn es physisch da ist.",
          "Bei Produkten mit Verfallsdatum: Die Packungen liegen vor dir, damit du das Datum ablesen kannst."],
  blocks=[
   ("steps",[
     dict(t="Öffne das Verbrauchsportal und wähle deine Veranstaltung. Tippe auf den Reiter Offene Auffüllungen {1}.", img="vp-09-offen", alt="Reiter Offene Auffüllungen mit zwei offenen Positionen und Auffüllen-Buttons", cap="{1} Reiter, {2} Auffüllen. Hier siehst du auch Positionen anderer Personen."),
     dict(t="Suche die Position, die du aufgefüllt hast, und tippe auf Auffüllen {2}. Steht unter der Position „kein Verfallsprodukt“, ist es ein Produkt ohne Verfallsdatum (Fall 1). Sonst ist es ein Produkt mit Verfallsdatum (Fall 2).", img=None),
   ]),
   ("h","Fall 1: Produkt ohne Verfallsdatum"),
   ("steps",[
     dict(t="Es erscheint eine Rückfrage, ob die Position als aufgefüllt markiert werden soll. Bestätige mit OK. Dabei musst du nichts eintragen.", img=None),
   ]),
   ("h","Fall 2: Produkt mit Verfallsdatum"),
   ("steps",[
     dict(t="Der Dialog Auffüllung bestätigen öffnet sich. Oben bei {1} siehst du Produkt, Menge und Ziel.", img="vp-11-auffuellen-charge", alt="Dialog Auffüllung bestätigen mit Verfallsdatum, Mengenfeld und Button Bestätigen", cap="{1} Produkt und Menge, {2} Verfallsdatum, {3} Menge dieser Charge, {4} Bestätigen."),
     dict(t="Trage bei {2} das Verfallsdatum ein, das auf der Packung steht. Bei {3} steht die Menge mit diesem Datum.", img=None),
     dict(t="Haben nicht alle Packungen dasselbe Datum? Tippe auf + Weiteres Verfallsdatum und trage das nächste Datum samt Menge ein. Die Summe muss genau zur aufzufüllenden Menge passen. Darunter erscheint „vollständig“, wenn alles stimmt.", img=None),
     dict(t="Tippe auf Bestätigen {4}.", img=None),
   ]),
   ("steps",[
     dict(t="Die Position verschwindet aus der Liste. Sind alle erledigt, steht dort „Keine offenen Auffüllungen – alles erledigt.“", img="vp-11b-alles-aufgefuellt", alt="Reiter Offene Auffüllungen mit dem Hinweis, dass alles erledigt ist", cap="Alles aufgefüllt."),
   ]),
   ("warn","Danach ist der Eintrag gesperrt","<p>Nach dem Bestätigen kannst du den Eintrag nicht mehr ändern. Prüfe Datum und Menge vorher in Ruhe.</p>"),
   ("note","Nur Monat und Jahr auf der Packung?","<p>Milan verlangt ein volles Datum. Steht auf der Packung nur Monat und Jahr, richte dich nach der Regel deiner Organisation und frage im Zweifel deinen Materialwart.</p>"),
   ("faq",[
     ("Die Summe stimmt nicht, ich kann nicht bestätigen.","<p>Die Mengen aller Zeilen zusammen müssen genau der aufzufüllenden Menge entsprechen. Passe die Zahlen an oder füge eine Zeile hinzu.</p>"),
     ("Ich habe versehentlich falsch bestätigt.","<p>Das kann nur die Administration zurücknehmen. Melde dich beim Materialwart.</p>"),
     ("Ich sehe die Option „Chargenerfassung übergehen“.","<p>Diese Option ist nur für Materialwarte gedacht. Trage bitte immer die Verfallsdaten ein, wenn du sie hast.</p>"),
   ]),
  ],
  weiter=["verbrauch-bericht"])

P(id="verbrauch-bericht", sec=2, num="2.6", title="Bericht ansehen und Sitzung beenden",
  kw="bericht pdf sitzung beenden zusammenfassung abschluss veranstaltung abschließen",
  kurz="Im Reiter Bericht siehst du, was ausgetragen und aufgefüllt wurde. Mit Sitzung beenden verlässt du die Veranstaltung. Abgeschlossen wird sie vom Materialwart.",
  wann="Du willst prüfen, ob alles erfasst ist, oder zu einer anderen Veranstaltung wechseln.",
  blocks=[
   ("steps",[
     dict(t="Tippe auf den Reiter Bericht {1}. Oben siehst du die Zahl der Positionen und wie viele davon aufgefüllt oder noch offen sind.", img="vp-12-bericht", alt="Reiter Bericht mit Kennzahlen und Zusammenfassung je Produkt", cap="{1} Reiter Bericht. Darunter: Zusammenfassung je Produkt und Einzelpositionen."),
     dict(t="Scrolle nach unten für die Einzelpositionen. Mit den Filtern „alle“, „nur offene“ und „nur aufgefüllte“ grenzt du die Liste ein. Über Als PDF exportieren erhältst du den Bericht als Datei.", img=None),
     dict(t="Möchtest du die Veranstaltung wechseln oder bist du fertig, tippe oben auf Sitzung beenden {1}. Deine Daten bleiben dabei gespeichert.", img="vp-13-sitzung-beenden", alt="Erfassungsansicht mit markiertem Button Sitzung beenden", cap="{1} Sitzung beenden."),
   ]),
   ("note","Abschluss der Veranstaltung","<p>Eine Veranstaltung kann erst abgeschlossen werden, wenn nichts mehr offen ist. Das macht der Materialwart. In der Veranstaltungsliste siehst du, ob noch Auffüllungen offen sind (siehe <a href=\"nachschlagen-veranstaltungen.html\">Veranstaltungen ansehen</a>).</p>"),
  ],
  weiter=["nachschlagen-veranstaltungen","ep-finden"])

# ---------------------------------------------------------------- 3
P(id="ep-finden", sec=3, num="3.1", title="Einsatzposition finden",
  kw="einsatzposition finden suchen baum tabelle modul objekt pfad fahrzeug rucksack koffer record id",
  kurz="Menü → Einsatzpositionen. Im Baum das Objekt (Fahrzeug, Rucksack) öffnen, dann den Fachbereich, dann die Position. Oder oben suchen oder scannen.",
  wann="Du willst Material in einem Fahrzeug, Rucksack oder Koffer prüfen.",
  blocks=[
   ("h","Kurz erklärt: so ist Milan aufgebaut"),
   ("list",["<strong>Objekt:</strong> dein Fahrzeug, Rucksack oder Koffer.",
            "<strong>Pfad:</strong> wo darin etwas liegt (zum Beispiel „Seitenfach links“).",
            "<strong>Modul:</strong> alle Positionen, die im selben Fach liegen. Module bekommen eine Nummer und ein Etikett zum Scannen.",
            "<strong>Einsatzposition (EP):</strong> ein Produkt an einem bestimmten Platz mit Sollbestand, zum Beispiel „Verbandpäckchen groß, Seitenfach links, Soll 5“."]),
   ("steps",[
     dict(t="Tippe im Menü auf Einsatzpositionen. Oben siehst du ein Suchfeld {1}, den Schalter Tabelle/Baum {2} und die Reiter Einsatzpositionen/Module {3}.", img="ep-01-uebersicht", alt="Übersicht der Einsatzpositionen mit Suchfeld, Schalter Tabelle und Baum und dem Reiter Module", cap="{1} Suche, {2} Ansicht, {3} Module."),
     dict(t="Im Baum tippst du auf ein Objekt, dann auf einen Fachbereich {1}, dann auf die Position {2}.", img="ep-02-baum", alt="Baumansicht mit aufgeklapptem Objekt, Fachbereich und markierter Einsatzposition", cap="{1} Fachbereich, {2} Position."),
     dict(t="Die Detailansicht öffnet sich. Oben siehst du den Namen des Produkts, darunter Status und Modul. Mit den Pfeilen ‹ › wechselst du zur nächsten oder vorherigen Position, mit ☰ Positionen öffnest du die Liste.", img="ep-03-detail", alt="Detailansicht einer Einsatzposition mit Button EP-Kontrolle erfassen und Statusanzeige", cap="{1} EP-Kontrolle erfassen, {2} Status."),
   ]),
   ("h","Was die Zahlen im Baum bedeuten"),
   ("p","Hinter jedem Objekt und Fach stehen drei Zahlen und eine Balkenanzeige, zum Beispiel „1/0/4“. Die Zahlen zeigen, wie viele Positionen in Ordnung (grün), in Vorwarnung (gelb) oder mit Fehlermeldung bzw. abgelaufen (rot) sind. Die fett gedruckte Zahl daneben ist die Gesamtzahl der Positionen."),
   ("h","Weitere Wege"),
   ("list",["<strong>Suchen:</strong> Gib Produktnamen, Pfad oder die RecordID ein.","<strong>Scannen:</strong> Tippe auf Referenz scannen und halte die Kamera auf das Etikett (siehe <a href=\"scan-button.html\">Scannen</a>).","<strong>Reiter Module:</strong> zeigt alle Fächer mit Nummer, Anzahl der Positionen und davon in Ordnung."]),
   ("faq",[
     ("Ich finde mein Fahrzeug oder meinen Rucksack nicht.","<p>Prüfe die Suche und ob ein Filter gesetzt ist (Objekt-ID, Produkt-ID, „Nur ohne Produkt zugewiesen“). Entferne Filter, die du nicht brauchst. Ist das Objekt nicht angelegt, sage dem Materialwart Bescheid.</p>"),
     ("Was ist „999 – Unbekannt“?","<p>Ein Sammelplatz für Einträge, die keinem Objekt zugeordnet werden konnten. Dort musst du nichts tun.</p>"),
   ]),
  ],
  weiter=["ep-kontrolle","massenscan"])

P(id="ep-kontrolle", sec=3, num="3.2", title="EP-Kontrolle erfassen",
  kw="ep kontrolle erfassen zustand ok anzahl verfallsdatum druck sauerstoff prüfen einsatzposition kontrolle",
  kurz="Position öffnen → + EP-Kontrolle erfassen → Zustand wählen, nur Neues eintragen → Erfassen. Vorher unter „Aktuelle Chargen“ nachsehen, was schon eingetragen ist!",
  wann="Du kontrollierst ein Fahrzeug, einen Rucksack oder Koffer und meldest den Zustand.",
  vorher=["Du hast die Einsatzposition geöffnet (siehe <a href=\"ep-finden.html\">Einsatzposition finden</a>).",
          "Du hast das Material vor dir und kannst zählen und Daten ablesen."],
  blocks=[
   ("stop","Wichtig, bitte zuerst lesen","<p>Jede Kontrolle mit einer <b>Anzahl</b> legt einen <b>neuen</b> Eintrag an. Sie ersetzt keinen alten. Trägst du dieselbe Charge zweimal ein, zählt Milan sie doppelt.</p><p>Schaue deshalb immer erst unter <b>Aktuelle Chargen</b> nach: Steht die Charge dort schon mit der richtigen Zahl, melde nur den Zustand und lasse die Anzahl leer. Stimmt die Zahl nicht, korrigiere sie dort mit + und − (siehe <a href=\"ep-chargen.html\">Chargen korrigieren</a>).</p>"),
   ("steps",[
     dict(t="Tippe in der Detailansicht auf + EP-Kontrolle erfassen {1}.", img="ep-03-detail", alt="Detailansicht mit markiertem Button EP-Kontrolle erfassen", cap="{1} EP-Kontrolle erfassen."),
     dict(t="Wähle bei {1} den Zustand: Zustand ok, wenn alles in Ordnung ist, sonst Fehlermeldung (siehe <a href=\"ep-fehler-melden.html\">Fehler melden</a>).", img="ep-04-kontrolle-dialog", alt="Dialog EP-Kontrolle erfassen mit Zustand, Anzahl, Verfallsdatum und Erfassen", cap="{1} Zustand, {2} Anzahl, {3} Verfallsdatum, {4} Erfassen."),
     dict(t="Trage bei {2} Anzahl die Stückzahl ein, die du <b>neu</b> meldest. Bei einer reinen Zustandsmeldung lässt du das Feld leer.", img=None),
     dict(t="Bei Produkten mit Verfallsdatum erscheint {3} Verfallsdatum. Trage das Datum von der Packung ein. Haben deine Packungen verschiedene Daten, melde jedes Datum einzeln: eine Kontrolle pro Datum.", img=None),
     dict(t="Tippe auf Erfassen {4}. Unten erscheint „EP-Kontrolle erfasst.“", img=None),
   ]),
   ("h","Sonderfall Sauerstoff"),
   ("steps",[
     dict(t="Bei Sauerstoffflaschen gibt es zusätzlich das Feld Druck {2}. Trage die Anzahl {1}, den Flaschendruck, den das Manometer zeigt {2}, und das Verfallsdatum {3} ein. Druck und Verfallsdatum gehören immer zu einer Anzahl.", img="ep-08-sauerstoff", alt="Dialog EP-Kontrolle erfassen für ein Sauerstoffprodukt mit Feldern für Anzahl, Druck und Verfallsdatum", cap="{1} Anzahl, {2} Druck, {3} Verfallsdatum."),
   ]),
   ("note","Feld „SecurPharm-Code scannen“","<p>Bei manchen Arzneimitteln erscheint dieses Feld. Wenn die Packung einen SecurPharm-Code (2D-Code) trägt, scanne ihn oder füge ihn ein und tippe auf Übernehmen. Milan trägt das Verfallsdatum dann selbst ein. Kein Code, kein Problem: Datum einfach selbst eintragen.</p>"),
   ("table",["Du siehst …","Das bedeutet"],[
     ["Feld Verfallsdatum","Das Produkt hat ein Verfallsdatum. Eintragen ist Pflicht, sobald du eine Anzahl größer als 0 meldest."],
     ["Feld Druck","Nur bei Sauerstoff."],
     ["Weder Datum noch Druck","Das Produkt hat kein Verfallsdatum. Es zählt nur Zustand und Anzahl."],
   ]),
   ("faq",[
     ("Ich habe „Bitte Status und/oder Anzahl angeben“ gesehen.","<p>Wähle entweder Zustand ok oder Fehlermeldung, trage eine Anzahl ein, oder beides. Ganz leer geht nicht.</p>"),
     ("Ich habe eine Charge doppelt eingetragen.","<p>Öffne Aktuelle Chargen. Die doppelte Zeile kannst du mit „Als verbraucht markieren“ aus der aktuellen Liste nehmen. Sage dem Materialwart danach kurz Bescheid.</p>"),
     ("Das Verfallsdatum ist schon abgelaufen.","<p>Melde es trotzdem ehrlich. Milan zeigt abgelaufenes Material mit Warnung an. Tausche die Ware aus und melde die neue Charge.</p>"),
   ]),
  ],
  weiter=["ep-fehler-melden","ep-chargen"])

P(id="ep-fehler-melden", sec=3, num="3.3", title="Einen Fehler melden",
  kw="fehlermeldung fehler melden defekt beschädigt fehlt zustand nicht ok anmerkung auftrag",
  kurz="Bei der EP-Kontrolle Fehlermeldung wählen und in der Anmerkung kurz beschreiben, was los ist. Milan legt dafür automatisch einen Auftrag an.",
  wann="Etwas fehlt, ist kaputt, beschädigt oder nicht einsatzfähig.",
  blocks=[
   ("steps",[
     dict(t="Öffne die Einsatzposition und tippe auf + EP-Kontrolle erfassen.", img=None),
     dict(t="Tippe auf Fehlermeldung {1}. Der Knopf wird rot.", img="ep-07-fehlermeldung", alt="Dialog EP-Kontrolle mit gewählter Fehlermeldung und Textfeld Anmerkung", cap="{1} Fehlermeldung, {2} Anmerkung, {3} Erfassen."),
     dict(t="Schreibe bei Anmerkung {2} kurz und konkret, was nicht stimmt, zum Beispiel was beschädigt ist oder wie viele fehlen.", img=None),
     dict(t="Trage die Anzahl ein, die du tatsächlich vorfindest, wenn sie noch nicht unter Aktuelle Chargen steht. Tippe auf Erfassen {3}.", img=None),
   ]),
   ("note","Was dann passiert","<p>Die Einsatzposition erscheint mit Fehlerstatus. Milan legt automatisch einen Auftrag an, damit sich jemand kümmert. Du findest ihn unter <a href=\"auftraege-ansehen.html\">Aufträge</a>. Ist die Position später wieder in Ordnung, schließt sich dieser Auftrag nach einer neuen, positiven Kontrolle von selbst.</p>"),
   ("note","Löschen","<p>Eine Kontrolle lässt sich nicht löschen. Meldest du die Position später als in Ordnung, gilt wieder der neue Status. Die alte Fehlermeldung bleibt in der Historie sichtbar.</p>"),
   ("faq",[("Ich möchte noch etwas ergänzen, das nicht zur Position passt.","<p>Lege einen Auftrag mit eigenem Text an (siehe <a href=\"auftrag-anlegen.html\">Auftrag anlegen</a>).</p>")]),
  ],
  weiter=["auftraege-ansehen","ep-chargen"])

P(id="ep-chargen", sec=3, num="3.4", title="Chargen korrigieren und als verbraucht markieren",
  kw="chargen aktuelle charge anzahl korrigieren plus minus verbraucht markieren abgelaufen",
  kurz="Unter Aktuelle Chargen siehst du jede Charge mit Menge und Verfallsdatum. Mit + und − korrigierst du die Menge, mit Als verbraucht markieren nimmst du eine leere Charge heraus.",
  wann="Eine Menge stimmt nicht, oder eine Charge ist aufgebraucht, abgelaufen oder entsorgt.",
  blocks=[
   ("steps",[
     dict(t="Öffne die Einsatzposition und scrolle zum Reiter Aktuelle Chargen. Jede Charge hat eine eigene Karte.", img=None),
     dict(t="Mit − und + {1} änderst du die Menge der Charge um je 1.", img="ep-05-chargen", alt="Aktuelle Chargen mit Mengenbuttons und dem Button Als verbraucht markieren", cap="{1} Menge anpassen, {2} Als verbraucht markieren."),
     dict(t="Ist eine Charge komplett verbraucht, abgelaufen oder aussortiert, tippe auf Als verbraucht markieren {2}. Sie verschwindet aus der aktuellen Liste, bleibt aber in der Historie.", img=None),
   ]),
   ("note","Was „aktuell“ heißt","<p>„Aktuell“ bedeutet: noch nicht verbraucht. Es können gleichzeitig mehrere Chargen aktuell sein, zum Beispiel zwei Packungen mit verschiedenen Verfallsdaten. Das ist richtig so.</p>"),
  ],
  weiter=["ep-historie","ep-kontrolle"])

P(id="ep-historie", sec=3, num="3.5", title="Verlauf einer Position ansehen",
  kw="historie verlauf nachverfolgen wer wann kontrolle eintrag",
  kurz="In der Detailansicht auf den Reiter Historie tippen. Dort steht jede Kontrolle mit Datum, Zustand, Anzahl und Anmerkung.",
  wann="Du willst wissen, wer wann zuletzt kontrolliert hat oder was gemeldet wurde.",
  blocks=[
   ("steps",[
     dict(t="Öffne die Einsatzposition und tippe auf den Reiter Historie {1}.", img="ep-06-historie", alt="Reiter Historie einer Einsatzposition mit einem Kontrolleintrag", cap="{1} Reiter Historie."),
     dict(t="Scrolle durch die Einträge. Neue stehen oben. Der Status „Aktuell“ zeigt, dass die Charge noch nicht verbraucht ist.", img=None),
   ]),
   ("faq",[("Die Historie ist leer.","<p>Für diese Position wurde noch keine Kontrolle erfasst. Das ist bei neuen Positionen normal.</p>"),
           ("Ich sehe einen Eintrag, den ich nicht kenne.","<p>Jede Kontrolle wird mit Datum gespeichert. Frage im Zweifel deinen Materialwart, wer die Position zuletzt geprüft hat.</p>")]),
  ],
  weiter=["ep-kontrolle"])

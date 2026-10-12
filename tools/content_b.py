# -*- coding: utf-8 -*-
from content_a import PAGES
def P(**k): PAGES.append(k)

# ---------------------------------------------------------------- 4
P(id="massenscan", sec=4, num="4.1", title="Massenscan: wann und warum",
  kw="massenscan modul scannen packung einzeln entwurf wann nutzen",
  kurz="Beim Massenscan scannst du jede Packung eines Moduls einzeln. Erst mit „Massenscan abschließen“ werden die Bestände wirklich geändert. Alles, was du nicht neu scannst, wird entfernt.",
  wann="Du willst ein ganzes Fach oder Modul in einem Rutsch neu erfassen, zum Beispiel nach dem Auffüllen.",
  blocks=[
   ("stop","Das musst du wissen","<p>Der Massenscan ist eine <b>komplette Neuaufnahme</b> des Moduls. Chargen, die bisher in Milan standen und die du nicht neu scannst, werden beim Abschluss <b>entfernt</b>. Scanne deshalb alles, was wirklich im Modul liegt.</p>"),
   ("h","Wann passt der Massenscan?"),
   ("list",["Das Modul enthält Produkte mit Verfallsdatum, die per Code gescannt werden können.",
            "Du hast alle Packungen des Moduls vor dir.",
            "Du hast Zeit, jede Packung einzeln vor die Kamera zu halten. Das geht wie an der Supermarktkasse."]),
   ("h","Wann nicht?"),
   ("list",["Du willst nur eine einzelne Position prüfen: nutze die <a href=\"ep-kontrolle.html\">EP-Kontrolle</a>.",
            "Der Knopf Massenscan ist grau: Dann ist das Modul dafür nicht freigegeben. Frage deinen Materialwart.",
            "Das Modul wird gerade von jemand anderem gescannt. Dann zeigt Milan, wer es bearbeitet. Warte oder sprich mit der Person."]),
   ("note","Entwurf","<p>Bis zum Abschluss ist alles nur ein Entwurf. Wenn du abbrichst oder später weitermachst, ändert sich am Bestand nichts. Ein Entwurf bleibt bis zu 24 Stunden erhalten.</p>"),
  ],
  weiter=["massenscan-durchfuehren","scan-button"])

P(id="massenscan-durchfuehren", sec=4, num="4.2", title="Massenscan durchführen",
  kw="massenscan durchführen scannen starten abschließen ohne scan fortsetzen neu beginnen verfallsdatum",
  kurz="Reiter Module → beim Modul auf Massenscan → Hinweis lesen → Scannen starten → alle Packungen scannen → Massenscan abschließen → Vorschau prüfen → Abschließen.",
  wann="Du hast die Hinweise unter „Massenscan: wann und warum“ gelesen und alle Packungen des Moduls vor dir.",
  vorher=["Die Kamera ist erlaubt (siehe <a href=\"scan-probleme.html\">Wenn der Scanner nicht funktioniert</a>).","Gute Beleuchtung und alle Packungen griffbereit."],
  blocks=[
   ("steps",[
     dict(t="Öffne Einsatzpositionen und tippe auf den Reiter Module. Suche das Modul mit seiner Nummer und tippe auf Massenscan {1}.", img="ms-01-modul", alt="Reiter Module mit einer Modulkarte und dem Button Massenscan", cap="{1} Massenscan. Ist er grau, ist das Modul nicht freigegeben."),
     dict(t="Gibt es noch einen unfertigen Entwurf, fragt Milan nach. Fortsetzen übernimmt den bisherigen Stand {1}, Neu beginnen verwirft ihn {2}.", img="ms-02a-unfertig", alt="Dialog Unfertige Sitzung gefunden mit den Buttons Fortsetzen und Neu beginnen", cap="{1} Fortsetzen, {2} Neu beginnen."),
     dict(t="Lies die kurze Erklärung und tippe auf Verstanden, scannen {1}. Wenn du den Hinweis nicht mehr sehen willst, setze vorher den Haken.", img="ms-02-hinweis", alt="Dialog Massenscan kurz erklärt mit fünf Hinweisen", cap="{1} Verstanden, scannen."),
     dict(t="Du siehst die Liste der Positionen des Moduls mit „gescannt / Soll“. Tippe auf Scannen starten {1}.", img="ms-03-liste", alt="Massenscan-Liste eines Moduls mit Fortschrittsbalken und Buttons Scannen starten und Massenscan abschließen", cap="{1} Scannen starten, {2} Abschließen, {3} Später fortsetzen."),
     dict(t="Die Kamera bleibt an. Halte nacheinander jede Packung mit ihrem Code in den Rahmen. Milan ordnet sie der richtigen Position zu und zählt hoch.", img="scan-01-scanner", alt="Scan-Fenster mit Kamerabild und Rahmen", cap="Das Scan-Fenster. Im Beispiel zeigt eine Testkamera nur ein Muster, bei dir siehst du das Kamerabild."),
   ]),
   ("h","Wenn etwas nicht automatisch klappt"),
   ("table",["Situation","Was du tust"],[
     ["Der Code enthält kein Verfallsdatum","Milan fragt bei jedem Scan nach Datum und Anzahl. Trage beides ein und tippe auf Übernehmen."],
     ["„Code nicht erkannt“","Wähle selbst aus der Liste, zu welcher Position die Packung gehört, oder verwirf den Scan."],
     ["Packung hat gar keinen Code","Tippe bei der Position auf Ohne Scan bestätigen und trage Anzahl und Datum von Hand ein."],
     ["„Sollbestand bereits erreicht“","Es liegen mehr Stück im Modul als vorgesehen. Milan fragt, welche Packungen im Modul bleiben und welche als Rückläufer zurück ins Lager gehen. Ordne sie zu und tippe auf Fertig."],
     ["Mengen müssen korrigiert werden","Mit − und + bei der jeweiligen Charge in der Liste."],
   ]),
   ("h","Abschließen"),
   ("steps",[
     dict(t="Sind alle Packungen gescannt, tippe auf Massenscan abschließen {2}. Milan zeigt eine Vorschau „Vor dem Abschluss prüfen“.", img=None),
     dict(t="Prüfe die Vorschau. Nicht gewollte Änderungen kannst du abwählen. Tippe dann auf Abschließen. Erst jetzt ändert sich der Bestand.", img=None),
     dict(t="Hast du Rückläufer, fragt Milan, ob sie ins Lager eingebucht werden sollen. Wähle die Packungen aus und tippe auf Einbuchen, oder überspringe den Schritt.", img=None),
   ]),
   ("warn","Zwischendurch unterbrechen","<p>Mit Später fortsetzen {3} verlässt du den Massenscan. Der Entwurf bleibt erhalten, der Bestand ändert sich nicht. Mit Massenscan abbrechen verwirfst du alles.</p>"),
   ("faq",[
     ("Ich habe versehentlich eine Packung doppelt gescannt.","<p>Korrigiere die Menge der Charge in der Liste mit −. Bemerkst du es erst in der Vorschau, wähle die Änderung ab oder gehe zurück.</p>"),
     ("Die Kamera startet nicht.","<p>Siehe <a href=\"scan-probleme.html\">Wenn der Scanner nicht funktioniert</a>.</p>"),
     ("Ich habe etwas vergessen zu scannen und schon abgeschlossen.","<p>Melde dich beim Materialwart. Nicht gescannte Chargen wurden mit dem Abschluss entfernt und müssen neu erfasst werden.</p>"),
   ]),
  ],
  weiter=["ep-kontrolle"])

# ---------------------------------------------------------------- 5
P(id="scan-button", sec=5, num="5.1", title="Codes scannen",
  kw="scannen scan button kamera barcode qr code etikett modul position produkt lagerort referenz",
  kurz="Auf den runden blauen Scan-Button unten rechts tippen, Kamera erlauben, Etikett in den Rahmen halten. Milan öffnet dann das passende Ziel.",
  wann="Du willst ein Etikett lesen, statt Namen oder Nummern zu tippen.",
  blocks=[
   ("steps",[
     dict(t="Tippe auf den runden blauen Scan-Button {3} unten rechts. Er ist auf fast jeder Seite da. In manchen Listen gibt es zusätzlich Knöpfe wie Referenz scannen oder Position/Modul scannen.", img="start-uebersicht", alt="Dashboard mit dem Scan-Button unten rechts", cap="{3} Scan-Button."),
     dict(t="Beim ersten Mal fragt dein Handy, ob Milan die Kamera benutzen darf. Tippe auf Erlauben.", img=None),
     dict(t="Das Scan-Fenster öffnet sich. Halte das Etikett so in den Rahmen {1}, dass der Code ganz zu sehen ist. Ruhig halten, nicht zu nah und nicht zu weit weg.", img="scan-01-scanner", alt="Scan-Fenster mit Kamerabild, Rahmen, Diagnose-Knopf und Scanner schließen", cap="{1} Rahmen, {2} Scanner schließen, {3} Diagnose. Das Kamerabild ist hier ein Testmuster."),
     dict(t="Sobald der Code erkannt ist, schließt sich das Fenster, und Milan öffnet das passende Ziel.", img=None),
   ]),
   ("h","Was passiert bei welchem Etikett?"),
   ("table",["Etikett","Ergebnis"],[
     ["Modul (Fach)","Milan zeigt alle Einsatzpositionen des Moduls zur Kontrolle."],
     ["Einsatzposition","Die Detailansicht der Position öffnet sich."],
     ["Produkt","Die Produktseite öffnet sich."],
     ["Lagerort","In einem geöffneten Buchungsformular wird das Lagerort-Feld gefüllt, sonst öffnet sich die Seite Lagerorte."],
     ["Veranstaltung","Die Veranstaltungsdetails öffnen sich."],
     ["Anderer Barcode (zum Beispiel auf einer Packung)","Milan sucht den Code und zeigt Suchergebnisse. Gibt es Treffer, wähle den passenden."],
   ]),
   ("note","Handscanner","<p>Hat dein Team einen Bluetooth-Handscanner? Tippe in das gewünschte Eingabefeld, sodass der Cursor blinkt, und löse den Scanner aus. Der Code wird wie getippt eingetragen. Fragen zur Kopplung beantwortet dein Materialwart.</p>"),
  ],
  weiter=["scan-probleme"])

P(id="scan-probleme", sec=5, num="5.2", title="Wenn der Scanner nicht funktioniert",
  kw="scanner funktioniert nicht kamera keine kamera berechtigung diagnose dunkel unscharf code nicht erkannt",
  kurz="Kamera erlauben, Licht verbessern, ruhig halten. Hilft nichts, tippe auf Diagnose anzeigen und schicke ein Foto davon an deinen Materialwart.",
  wann="Die Kamera bleibt schwarz, es erscheint „Keine Kamera gefunden“ oder der Code wird nicht erkannt.",
  blocks=[
   ("table",["Problem","Lösung"],[
     ["Kamera bleibt schwarz oder „Keine Kamera gefunden“","Erlaube den Kamerazugriff für den Browser in den Einstellungen deines Handys. Schließe andere Apps, die die Kamera nutzen. Lade Milan neu."],
     ["Der Code wird nicht erkannt","Mehr Licht, Handy ruhig halten, Abstand verändern (ca. eine Handbreit), Etikett glatt halten. Reinige die Kameralinse."],
     ["Das Etikett ist beschädigt oder verschmutzt","Gib stattdessen Namen oder Nummer von Hand ein oder nutze die Suche."],
     ["Es dauert lange, bis etwas passiert","Halte das Handy ruhig vor den Code. Auf älteren Handys kann das Erkennen länger dauern."],
   ]),
   ("steps",[
     dict(t="Tippe im Scan-Fenster auf Diagnose anzeigen {3}. Milan zeigt eine kurze Liste, was bei der Kamera funktioniert und was nicht.", img="scan-01-scanner", alt="Scan-Fenster mit Diagnose-Knopf", cap="{3} Diagnose anzeigen."),
     dict(t="Mache einen Screenshot davon und schicke ihn deinem Materialwart. Damit lässt sich die Ursache schnell eingrenzen.", img=None),
     dict(t="Mit Scanner schließen {2} kehrst du zurück und kannst von Hand weitermachen.", img=None),
   ]),
   ("note","Immer möglich","<p>Alles, was du scannen kannst, kannst du auch tippen oder suchen. Der Scan spart nur Zeit.</p>"),
  ],
  weiter=["haeufige-fragen"])

# ---------------------------------------------------------------- 6
P(id="auftraege-ansehen", sec=6, num="6.1", title="Aufträge ansehen",
  kw="aufträge liste status offen erledigt filter aufgaben meldungen",
  kurz="Menü → Aufträge. Dort siehst du alle Aufgaben mit Status. Tippe eine Zeile an, um Einzelheiten zu sehen.",
  wann="Du willst wissen, was noch zu tun ist, oder eine Meldung nachverfolgen.",
  blocks=[
   ("p","Ein Auftrag ist eine Aufgabe, zum Beispiel „Rettungsdecken nachbestellen“ oder „Sauerstoffflasche prüfen“. Aufträge entstehen von Hand oder automatisch, etwa wenn eine EP-Kontrolle einen Fehler meldet."),
   ("steps",[
     dict(t="Öffne im Menü, Gruppe Organisation, den Eintrag Aufträge.", img="menue-organisation", alt="Menü mit dem Eintrag Aufträge", cap="Aufträge ({1})."),
     dict(t="Oben filterst du nach Status (Alle Status, Offen, In Bearbeitung, Erledigt, Abgebrochen). „Erledigte ausblenden“ hält die Liste übersichtlich. Tippe auf einen Auftrag, um ihn zu öffnen.", img="au-03-liste", alt="Auftragsliste mit Statusfilter, Button Neuer Auftrag und einem Auftrag", cap="Die Liste. Jeder Auftrag zeigt Text, Art, Status, Bearbeiter und Verlinkung."),
   ]),
   ("table",["Status","Bedeutung"],[
     ["Offen","Noch niemand hat angefangen."],
     ["In Bearbeitung","Jemand kümmert sich darum."],
     ["Erledigt","Fertig."],
     ["Abgebrochen","Wird nicht mehr gebraucht."],
   ]),
  ],
  weiter=["auftrag-anlegen","auftrag-bearbeiten"])

P(id="auftrag-anlegen", sec=6, num="6.2", title="Auftrag anlegen",
  kw="auftrag anlegen neu melden aufgabe bestellen nachbestellen verlinkt record id",
  kurz="Aufträge → + Neuer Auftrag → Art und Text eintragen → bei Bedarf mit einer Position verlinken → Anlegen.",
  wann="Etwas muss erledigt werden, das nicht zu einer EP-Kontrolle passt, oder du willst jemandem etwas melden.",
  blocks=[
   ("steps",[
     dict(t="Öffne Aufträge und tippe auf + Neuer Auftrag.", img="au-01-liste-leer", alt="Leere Auftragsliste mit Button Neuer Auftrag", cap="{1} Neuer Auftrag."),
     dict(t="Wähle die Auftragsart {1} (zum Beispiel Sonstige) und schreibe bei {2} kurz und verständlich, worum es geht. Nenne Ort, Produkt und Menge.", img="au-02-neu", alt="Dialog Neuer Auftrag mit Auftragsart, Auftragstext, Bearbeiter, Verlinkung und Anlegen", cap="{1} Art, {2} Text, {3} Bezug, {4} ID, {5} Anlegen."),
     dict(t="Möchtest du den Auftrag mit etwas verknüpfen, wähle bei {3} „Verlinkt mit“, zum Beispiel Einsatzposition, und trage bei {4} die Nummer ein. Die RecordID einer Position steht in ihrer Detailansicht. Das ist optional.", img=None),
     dict(t="Tippe auf Anlegen {5}. Unten steht „Auftrag angelegt.“", img=None),
   ]),
   ("note","Bearbeiter","<p>Du kannst eine Person als Bearbeiter wählen. Wenn du unsicher bist, lasse „nicht zugewiesen“ stehen.</p>"),
  ],
  weiter=["auftrag-bearbeiten"])

P(id="auftrag-bearbeiten", sec=6, num="6.3", title="Auftrag bearbeiten und abhaken",
  kw="auftrag status ändern abhaken erledigt kommentar bearbeiter verlinkung",
  kurz="Auftrag öffnen → Status wählen → Übernehmen (Abhaken). Mit einem Kommentar hältst du fest, was du getan hast.",
  wann="Du hast einen Auftrag begonnen oder erledigt.",
  blocks=[
   ("steps",[
     dict(t="Öffne den Auftrag aus der Liste. Oben bei {1} wählst du den neuen Status, zum Beispiel Erledigt. Tippe dann auf Übernehmen (Abhaken) {2}.", img="au-04-detail", alt="Auftragsdetail mit Statusauswahl und Button Übernehmen", cap="{1} Status, {2} Übernehmen (Abhaken)."),
     dict(t="Scrolle nach unten. Bei {1} schreibst du einen kurzen Kommentar, zum Beispiel „Nachbestellt, kommt Freitag“. Tippe auf Kommentar hinzufügen {2}. Unter Verlauf siehst du, was bisher passiert ist.", img="au-05-kommentar", alt="Kommentarfeld unter dem Auftragsverlauf mit Button Kommentar hinzufügen", cap="{1} Kommentarfeld, {2} Kommentar hinzufügen."),
   ]),
   ("note","Automatische Aufträge","<p>Aufträge, die Milan selbst angelegt hat (zum Beispiel nach einer Fehlermeldung), schließen sich oft von selbst, sobald die Position wieder in Ordnung ist. Du musst sie dann nicht abhaken.</p>"),
  ],
  weiter=["auftraege-ansehen"])

# ---------------------------------------------------------------- 7
P(id="nachschlagen-produkte", sec=7, num="7.1", title="Produkte und Bestand ansehen",
  kw="produkte bestand mindestbestand verfallsdatum aa bb cc suche produktdetail bund bedarfsbericht",
  kurz="Menü → Produkte. Suchen, ein Produkt antippen und im Reiter Bestand sehen, wie viel da ist und wie lange es hält. Hier kannst du nur ansehen.",
  wann="Du willst wissen, wie viel von einem Produkt vorhanden ist, oder wann es abläuft.",
  blocks=[
   ("steps",[
     dict(t="Öffne im Menü, Gruppe Material, den Eintrag Produkte. Suche oben {1} nach Namen, Synonym oder Kategorie.", img="nl-01-produkte", alt="Produktliste mit Suchfeld und Karten je Produkt", cap="{1} Suche. Jede Karte zeigt Bestand, Mindestbestand und Status."),
     dict(t="Tippe ein Produkt an. Die Reiter Stammdaten, Bestand, Verbrauch, Verfallsdaten, Einsatzpositionen, Einkaufsstandards und Barcodes zeigen Einzelheiten.", img="nl-02-produkt-detail", alt="Produktdetail mit Reitern und Stammdaten", cap="Produktdetail."),
   ]),
   ("h","Die Bestandsanzeige AA / BB / CC"),
   ("table",["Anzeige","Farbe","Bedeutung"],[
     ["AA","grün","Kein Verfallsdatum oder mehr als 150 Tage haltbar"],
     ["BB","gelb","20 bis 150 Tage bis zum Verfall"],
     ["CC","rot","20 Tage oder weniger, oder abgelaufen"],
     ["GES","–","Gesamtbestand"],
   ]),
   ("note","Bund-Bedarfsbericht","<p>Über den Knopf Bund-Bedarfsbericht (PDF) erhältst du eine Übersicht der vom Bund gestellten Positionen, die nicht in Ordnung sind. Für diese müsste beim Bund Bedarf angemeldet werden. Der Bericht ist rein informativ und löst keine Bestellung aus.</p>"),
   ("note","Nur ansehen","<p>Produkte anlegen, ändern oder bestellen kann nur die Materialverwaltung.</p>"),
  ],
  weiter=["nachschlagen-lager"])

P(id="nachschlagen-lager", sec=7, num="7.2", title="Lagerbestand und Lagerorte",
  kw="lagerbestand lagerort lager regal fach wo liegt charge verfallsdatum hauptlager",
  kurz="Im Lagerbestand wählst du ein Produkt und siehst, in welchen Lagerorten welche Chargen liegen. Die Lagerorte zeigen, wie das Lager aufgebaut ist.",
  wann="Du suchst Ware im Lager oder willst wissen, was wo liegt.",
  blocks=[
   ("steps",[
     dict(t="Öffne im Menü, Gruppe Material, Lagerbestand. Gib die Produktnummer ein oder tippe auf Produkt suchen. Tippe dann auf Bestand laden.", img="nl-03-lagerbestand", alt="Seite Lagerbestand mit Eingabefeld Produkt-ID und Button Bestand laden", cap="Lagerbestand je Produkt."),
     dict(t="Die Lagerorte findest du unter Organisation → Lagerorte. Sie sind verschachtelt, zum Beispiel Hauptlager → Regal → Fach. „Blatt“ bedeutet: ganz unten, dort liegt tatsächlich Ware.", img="nl-04-lagerorte", alt="Baumansicht der Lagerorte mit Hauptlager, Regal und zwei Fächern", cap="Lagerorte als Baum."),
   ]),
   ("note","Buchen","<p>Wareneingang, Umlagern und Korrekturen bucht die Materialverwaltung. Bei Fehlern im Bestand sprich bitte deinen Materialwart an.</p>"),
  ],
  weiter=["nachschlagen-veranstaltungen"])

P(id="nachschlagen-veranstaltungen", sec=7, num="7.3", title="Veranstaltungen ansehen",
  kw="veranstaltungen liste status auffüllungen offen bericht pdf detail abgeschlossen",
  kurz="Menü → Veranstaltungen. Dort siehst du Status und ob noch Auffüllungen offen sind. Ein Tipp auf die Veranstaltung zeigt den Bericht.",
  wann="Du willst wissen, ob noch etwas aufzufüllen ist, oder einen Bericht ansehen.",
  blocks=[
   ("steps",[
     dict(t="Öffne im Menü, Gruppe Veranstaltungen, den Eintrag Veranstaltungen. Jede Veranstaltung zeigt Beginn, Status (zum Beispiel Laufend) und ob die Auffüllungen vollständig sind oder noch etwas offen ist.", img="nl-05-veranstaltungen", alt="Liste der Veranstaltungen mit Status und Auffüllungsstand", cap="Die Veranstaltungsliste."),
     dict(t="Tippe auf eine Veranstaltung. Du siehst Zeiten, Status und darunter alle Verbrauchsberichte. Mit Verbrauchsportal ansehen oder PDF-Bericht öffnest du den Bericht.", img="nl-06-veranstaltung-detail", alt="Detailansicht einer Veranstaltung mit Zeiten, Status und Verbrauchsberichten", cap="Veranstaltungsdetail."),
   ]),
   ("note","Abschluss","<p>Abschließen, Ausblenden und Anlegen von Veranstaltungen übernimmt die Materialverwaltung.</p>"),
  ],
  weiter=["verbrauch-ueberblick"])

# ---------------------------------------------------------------- 8
P(id="haeufige-fragen", sec=8, num="8.1", title="Häufige Fragen",
  kw="fragen faq hilfe problem fehler wer ansprechen internet seite lädt nicht",
  kurz="Schnelle Antworten auf die häufigsten Fragen. Findest du deine Frage nicht, wende dich an deinen Materialwart.",
  blocks=[
   ("faq",[
     ("Ich weiß nicht, wo ich anfangen soll.","<p>Nach einem Einsatz: <a href=\"verbrauch-ueberblick.html\">Verbrauch dokumentieren</a>. Beim Kontrollieren: <a href=\"ep-finden.html\">Einsatzposition finden</a>. Sonst die Suche oben links nutzen.</p>"),
     ("Die Seite lädt nicht oder bleibt leer.","<p>Prüfe deine Internetverbindung, lade die Seite neu und melde dich bei Bedarf neu an. Hilft das nicht, frage deinen Materialwart, ob Milan gerade gewartet wird.</p>"),
     ("Habe ich Daten verloren, wenn ich abgemeldet wurde?","<p>Nein. Was du mit Speichern, Austragen, Erfassen oder Bestätigen abgeschickt hast, ist gespeichert. Nur nicht abgeschickte Eingaben in offenen Dialogen gehen verloren.</p>"),
     ("Kann ich etwas löschen oder rückgängig machen?","<p>Austragungen kannst du entfernen, solange sie nicht aufgefüllt sind. Kontrollen und bestätigte Auffüllungen bleiben bewusst erhalten, damit alles nachvollziehbar ist. Melde Fehler deinem Materialwart.</p>"),
     ("Wer sieht, was ich eingebe?","<p>Eingaben werden mit deinem Namen gespeichert. Das hilft bei Rückfragen und bei der Abrechnung.</p>"),
     ("Ich sehe einen Knopf, der bei mir nicht geht.","<p>Manche Funktionen sind der Materialverwaltung vorbehalten. Siehe <a href=\"rechte.html\">Was du nicht selbst machen musst</a>.</p>"),
     ("Ich habe einen Fehler in Milan gefunden.","<p>Notiere, was du getan hast und was angezeigt wurde, und mache wenn möglich einen Screenshot. Gib beides deinem Materialwart, ohne dein Passwort zu nennen.</p>"),
   ]),
  ],
  weiter=["glossar","rechte"])

P(id="glossar", sec=8, num="8.2", title="Begriffe einfach erklärt",
  kw="glossar begriffe erklärung ep modul objekt charge pfad verfallsprodukt sollbestand mindestbestand sitzung veranstaltung",
  kurz="Die wichtigsten Wörter in Milan, kurz und ohne Fachsprache.",
  blocks=[
   ("table",["Begriff","Bedeutung"],[
     ["Objekt","Ein Fahrzeug, Rucksack, Koffer oder Standort, in dem Material liegt."],
     ["Pfad","Wo im Objekt etwas liegt, zum Beispiel „Seitenfach links“."],
     ["Modul","Alle Positionen im selben Fach. Hat eine eigene Nummer und ein Etikett."],
     ["Einsatzposition (EP)","Ein Produkt an einem Platz in einem Objekt, mit Soll-Menge."],
     ["RecordID","Die Nummer einer Einsatzposition."],
     ["Produkt","Ein Artikel im Katalog, zum Beispiel „Einmalhandschuhe M“."],
     ["Verfallsprodukt","Ein Produkt mit Haltbarkeitsdatum. Dafür trägst du das Datum ein."],
     ["Charge","Eine Gruppe gleicher Packungen mit demselben Verfallsdatum."],
     ["Sollbestand","So viele Stück sollen in der Position liegen."],
     ["Mindestbestand","Darunter schlägt Milan Alarm."],
     ["EP-Kontrolle","Die Prüfung einer Position: Zustand, Anzahl, Datum."],
     ["Fehlermeldung","Eine Kontrolle, bei der etwas nicht in Ordnung ist."],
     ["Austragen","Eintragen, dass Material verbraucht wurde."],
     ["Auffüllen","Bestätigen, dass verbrauchtes Material wieder aufgefüllt ist."],
     ["Sitzung","Die gewählte Veranstaltung im Verbrauchsportal, bis du sie beendest oder dich abmeldest."],
     ["Materialwart / Materialverwaltung","Die Personen, die Stammdaten und Bestände pflegen und Veranstaltungen abschließen."],
     ["Auftrag","Eine Aufgabe oder Meldung mit Status."],
   ]),
  ],
  weiter=["haeufige-fragen"])

P(id="rechte", sec=8, num="8.3", title="Was du nicht selbst machen musst",
  kw="rechte berechtigung rollen materialwart admin darf nicht keine berechtigung gesperrt",
  kurz="Du kannst eintragen, kontrollieren, scannen und nachschlagen. Anlegen und Ändern von Stammdaten, Buchen und Abschließen machen Materialwart oder Administration.",
  blocks=[
   ("p","Milan unterscheidet drei Rollen. Du hast die Basis-Rolle. Das ist Absicht: So ist geschützt, was andere eingetragen haben."),
   ("table",["Aufgabe","Du","Materialwart","Admin"],[
     ["Verbrauch austragen und auffüllen","<span class='pill yes'>Ja</span>","Ja","Ja"],
     ["EP-Kontrolle, Fehler melden","<span class='pill yes'>Ja</span>","Ja","Ja"],
     ["Massenscan, Scannen","<span class='pill yes'>Ja</span>","Ja","Ja"],
     ["Aufträge anlegen und bearbeiten","<span class='pill yes'>Ja</span>","Ja","Ja"],
     ["Nachschlagen (Produkte, Lager, Veranstaltungen)","<span class='pill view'>Ansehen</span>","Ja","Ja"],
     ["Produkte, Objekte, Lagerorte anlegen und ändern","<span class='pill no'>Nein</span>","Ja","Ja"],
     ["Bestand buchen, umlagern, bestellen","<span class='pill no'>Nein</span>","Ja","Ja"],
     ["Veranstaltung anlegen und abschließen","<span class='pill no'>Nein</span>","Ja","Ja"],
     ["Bestätigte Auffüllung zurücknehmen","<span class='pill no'>Nein</span>","Nein","Ja"],
     ["Konten und Personal verwalten","<span class='pill no'>Nein</span>","Nein","Ja"],
   ]),
   ("note","Wenn du mehr brauchst","<p>Sprich mit deinem Materialwart. Rechte werden nicht über diese Seite, sondern persönlich vergeben.</p>"),
  ],
  weiter=["haeufige-fragen"])

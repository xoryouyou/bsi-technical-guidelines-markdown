## Nachweise für die Konformitätsprüfung gemäß BSI TR-03138 Ersetzendes Scannen 

enthält Testcases der BSI TR-03138 Anlage P in der Version: 1.4.1 09.09.2021 

## Änderungshistorie 

|Version|Datum|Name|Beschreibung|
|---|---|---|---|
|1.0|23.04.2020|BSI|Finale Fassung|
|1.1|09.09.2021|BSI|Umstellung auf MS<br>Word,|



Tabelle 1: Änderungshistorie 

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn Tel.: +49 22899 9582-0 E-Mail: resiscan@bsi.bund.de Internet: https://www.bsi.bund.de © Bundesamt für Sicherheit in der Informationstechnik 2021 

Inhalt 

## Inhalt 

Nachweise für die Konformitätsprüfung gemäß BSI TR-03138 Ersetzendes Scannen ................................................ 4 P.1 Grundlegendes ................................................................................................................................................................................ 4 P.2 Basismodul ....................................................................................................................................................................................... 4 P.2.1 Grundlegende Anforderungen ........................................................................................................................................ 5 P.2.2 Organisatorische Maßnahmen ........................................................................................................................................ 6 P.2.3 Personelle Maßnahmen .................................................................................................................................................... 11 P.2.4 Technische Maßnahmen .................................................................................................................................................. 13 P.2.5 Sicherheitsmaßnahmen bei der Dokumentenvorbereitung ............................................................................ 15 P.2.6 Sicherheitsmaßnahmen beim Scannen ..................................................................................................................... 18 P.2.7 Sicherheitsmaßnahmen bei der Nachbearbeitung ............................................................................................... 24 P.2.8 Sicherheitsmaßnahmen bei der Integritätssicherung ......................................................................................... 26 P.3 Aufbaumodule .............................................................................................................................................................................. 27 P.3.1 Generelle Maßnahmen bei erhöhtem Schutzbedarf ............................................................................................ 27 P.3.2 Zusätzliche Maßnahmen bei hohen Integritätsanforderungen ...................................................................... 28 P.3.3 Zusätzliche Maßnahmen bei sehr hohen Integritätsanforderungen ............................................................ 32 P.3.4 Zusätzliche Maßnahmen bei hohen Vertraulichkeitsanforderungen .......................................................... 34 P.3.5 Zusätzliche Maßnahmen bei sehr hohen Vertraulichkeitsanforderungen ................................................ 36 P.3.6 Zusätzliche Maßnahmen bei hohen Verfügbarkeitsanforderungen ............................................................. 37 P.3.7 Zusätzliche Maßnahmen bei sehr hohen Verfügbarkeitsanforderungen ................................................... 39 P4. Weitere Ausführungen .............................................................................................................................................................. 40 Literaturverzeichnis ............................................................................................................................................................................... 43 

Bundesamt für Sicherheit in der Informationstechnik 

3 

## Nachweise für die Konformitätsprüfung gemäß BSI TR-03138 Ersetzendes Scannen 

## P.1 Grundlegendes 

Bei Beantragung der Zertifizierung gemäß BSI TRProzess der Prüfung und Zertifizierung effizient zu gestalten. 


![](markdown/tr/TR-03138-Anlage-P_V1_4_Formularfelder/TR-03138-Anlage-P_V1_4_Formularfelder.pdf-0004-03.png)



![](markdown/tr/TR-03138-Anlage-P_V1_4_Formularfelder/TR-03138-Anlage-P_V1_4_Formularfelder.pdf-0004-04.png)


iben bzw. auf das/die Referenzdokument/e (inkl. 

Dokumenten-bezeichnung, Kapitel, Seite und ggf. Abschnitt) verweisen. 


![](markdown/tr/TR-03138-Anlage-P_V1_4_Formularfelder/TR-03138-Anlage-P_V1_4_Formularfelder.pdf-0004-07.png)


Ausführungen genutzt werden. 

## P.2 Basismodul 

|ID|Anforderung|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|---|
|-||||Strukturanalyse|
||Die Strukturanalyse identifiziert die relevanten||||
||a|Datenobjekte|MUSS||
||b|IT-Systeme und Anwendungen|MUSS||
||c|Kommunikationsverbindungen (Netze)|MUSS||
||Bereinigter Netzplan liegt vor||MUSS||
|-||||Schutzbedarfsanalyse|
||Der Schutzbedarf der weiteren Datenobjekte<br>ergibt sich aus dem Schutzbedarf der||||



Bundesamt für Sicherheit in der Informationstechnik 

|ID|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|
||Papieroriginale.|||
||Der Schutzbedarf der Datenobjekte muss<br>hinsichtlich der Grundwerte Integrität,<br>Vertraulichkeit und Verfügbarkeit bestimmt werden.|MUSS||
||Bei der Bestimmung des Schutzbedarfs empfiehlt<br>sich die Klassifizierung und Zusammenfassung<br>gleichartiger Dokumente.|SOLL||



## P.2.1 Grundlegende Anforderungen 

|ID|Anforderung|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|---|
|A.G.1|||Verfahrensdokumentation||
||Die Verfahrensdokumentation muss die<br>folgenden Aspekte umfassen:||||
||a|Art der verarbeiteten Dokumente|MUSS||
|||Regelungen für nicht verarbeitete Dokumente|||
|||Festlegung der Verantwortlichkeiten im<br>Scanprozess|||
|||Festlegung der Abläufe im Scanprozess|||
|||Festlegung der Aufgaben im Scanprozess|||
||b||MUSS||



Bundesamt für Sicherheit in der Informationstechnik 

5 

|ID||Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|---|
|||Festlegung von Maßnahmen zur Qualifizierung<br>und Sensibilisierung der Mitarbeiter|||
||c|Beschreibung der dem Schutzbedarf<br>entsprechender Anforderungen an Räume, IT-<br>Systeme, Anwendungen und Sicherungsmittel|MUSS||
||d|Regelungen für die Administration und<br>Wartung der IT-Systeme und Anwendungen|MUSS||
||e|Festlegung von Sicherheitsanforderungen für<br>IT-Systeme, Netze und Anwendungen|MUSS||



## P.2.2 Organisatorische Maßnahmen 

|ID|Anforderung|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|---|
|A.O.1|Festlegung von Verantwortlichkeiten, Abläufen und Aufgaben im Scanprozess||||
||Verantwortlichkeiten, Abläufe und Aufgaben<br>müssen festgelegt sein. Dies umfasst<br>insbesondere:||||
||a|Welche Schritte werden durch wen ausgeführt<br>und wie ist dabei im Einzelnen vorzugehen?|MUSS||
||b|Welche Dokumente werden gescannt und<br>welche Daten werden hierbei erzeugt?|MUSS||
||c|Welche Qualitätskontrollen werden durch wen<br>in welchen Zeitabständen und nach welchen<br>Kriterien durchgeführt?|MUSS||
||d|Welche Sicherungsdaten oder<br>Sicherungssysteme sind für den Schutz der<br>Integrität dieser Daten vorgesehen?|MUSS||



Bundesamt für Sicherheit in der Informationstechnik 

6 

|ID||Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|---|
||e|Qualitätskontrollen müssen mindestens<br>stichprobenartig erfolgen.|MUSS||
|||Qualitätskontrollen sollen regelmäßig durch<br>Mitarbeiter durchgeführt werden, die nicht mit<br>der operativen Durchführung des zu<br>kontrollierenden Arbeitsschritts betraut sind.|SOLL||
||f|Für die in den Scanprozess involvierten<br>Datenobjekte sowie die genutzten IT-Systeme<br>und Anwendungen sollen Verantwortliche<br>benannt werden.|SOLL||
||g|Bei der Zuweisung des Personals zu den<br>operativen Aufgaben im Scanprozess müssen<br>potenzielle Interessenkonflikte berücksichtigt<br>werden.|MUSS||
|||Bei der Zuweisung des Personals zu den<br>operativen Aufgaben im Scanprozess sollen<br>potenzielle Interessenkonflikte nach<br>Möglichkeit vermieden werden|SOLL||
||h|Typische Fehlerquellen müssen berücksichtigt<br>werden.|MUSS||
|||Für typische Fehlerquellen sollen<br>entsprechende Vorsichtsmaßnahmen<br>festgelegt werden.|SOLL||
||i|Es muss festgelegt werden, unter welchen<br>Umständen und ab welchem Zeitpunkt das<br>Originaldokument vernichtet werden darf.|MUSS||
||j|Es muss ein Verfahren zur Klärung von|MUSS||



Bundesamt für Sicherheit in der Informationstechnik 

7 

|ID|Anforderung|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|---|
||k|Es wird empfohlen das Scannen vor der<br>Vorgangsbearbeitung durchzuführen (frühes<br>Scannen).|SOLL||
|A.O.2|Regelungen für Wartungs- und Reparaturarbeiten||||
||Es sollen Regelungen für die Wartung und die<br>Reparatur der eingesetzten IT-Systeme und<br>Anwendungen getroffen werden. Dies umfasst<br>insbesondere:||||
||a|Festlegung der Verantwortlichkeit für die<br>Beauftragung, Durchführung und Kontrolle<br>von Wartungs- und Reparaturarbeiten|SOLL||
||b|Verfahren für die regelmäßige Bereitstellung<br>und Anwendung von sicherheitsrelevanten<br>Updates|SOLL||
||c|Regelung zur Authentisierung und zum<br>Nachweis der Autorisierung des<br>Wartungspersonals|SOLL||
||d|Regelungen zum Schutz personenbezogener<br>oder anderweitig besonders schützenswerter<br>Daten (z. B. Betriebsgeheimnisse) auf den zu<br>wartenden IT-Systemen|SOLL||
||e|Dokumentation von sicherheitsrelevanten<br>Veränderungen an den involvierten IT-<br>Systemen und Anwendungen|SOLL||
||f|Dokumentation der erfolgreichen<br>Durchführung der Maßnahmen zur<br>Qualitätskontrolle und Freigabe vor<br>Wiederaufnahme des regulären Betriebs|SOLL||



Bundesamt für Sicherheit in der Informationstechnik 

8 

|ID|Anforderung|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|---|
|A.O.3|Abnahme- und Freigabe-Verfahren für Hardware und Software||||
||Es muss ein Verfahren für die Abnahme und<br>Freigabe der eingesetzten Hard- und Software<br>etabliert werden; dies umfasst Scanner, Scan-<br>Workstation und Scan-Cache.||MUSS||
||Neben der initialen Inbetriebnahme ist dieses<br>Abnahmeverfahren auch bei der Wiederaufnahme<br>des Betriebs nach Wartungs- und<br>Reparaturarbeiten durchzuführen.||MUSS||
|A.O.4|Aufrechterhaltung der Informationssicherheit||||
||In angemessenen Abständen soll eine Überprüfung<br>der Wirksamkeit und Vollständigkeit der für die<br>Informationssicherheit beim ersetzenden Scannen<br>vorgesehenen Maßnahmen durchgeführt werden<br>(in Bundesbehörden min. alle drei Jahre).||SOLL||
||In diesen Audits muss geprüft werden:||||
||a|ob Prozesse und Sicherheitsmaßnahmen<br>korrekt implementiert wurden und wirksam<br>sind.|MUSS||
||b|ob die Sicherheitsmaßnahmen ausreichend vor<br>den potenziellen Bedrohungen schützen oder<br>ob zusätzliche oder korrigierte<br>Sicherheitsmaßnahmen notwendig sind.|MUSS||
||Audits sollen von unabhängigen Personen<br>durchgeführt werden.||SOLL||
||Die Ergebnisse der Audits sollen schriftlich<br>dokumentiert werden.||SOLL||



Bundesamt für Sicherheit in der Informationstechnik 

9 

|ID|Anforderung|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|---|
||Aus identifizierten Sicherheitslücken oder<br>Probleme müssen Korrekturmaßnahmen<br>abgeleitet werden.||MUSS||
||Für die Umsetzung von Korrekturmaßnahmen<br>muss ein Zeitplan mit Verantwortlichkeiten<br>definiert werden.||MUSS||
||Die Umsetzung der Maßnahmen muss durch die<br>Verantwortlichen verfolgt und überprüft werden.||MUSS||
|A.O.5|Anforderungen beim Outsourcing des Scanprozesses||||
||Wird der Scanprozess von spezialisierten<br>Scandienstleistern durchgeführt, sind die<br>Anforderungen der TR-RESISCAN umzusetzen.||MUSS||
||Darüber hinaus gelten folgende Anforderungen:||||
||a|Organisatorische und technische Schnittstellen<br>zwischen Auftraggeber und Auftragnehmer<br>müssen in der Verfahrensdokumentation<br>explizit dargestellt werden. (Übertragungswege,<br>Datenablageorte, beteiligte Akteure,<br>Rückfallverfahren, Maßnahmen zur<br>Integritäts- und Vollständigkeitskontrolle etc.)|MUSS||
||b|Der Auftragnehmer muss zur Einhaltung der<br>vom Auftraggeber definierten<br>Sicherheitsmaßnahmen verpflichtet werden.|MUSS||
||c|Es soll eine Analyse der durch die<br>Aufgabenteilung zusätzlich entstehenden<br>Risiken erfolgen.|SOLL||



Bundesamt für Sicherheit in der Informationstechnik 

10 

|ID||Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|---|
||d|Zusätzlich zur regelmäßigen Auditierung<br>sollen unangemeldete Stichproben<br>durchgeführt werden.|SOLL||



## P.2.3 Personelle Maßnahmen 

|ID|Anforderung|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|---|
|A.P.1|Sensibilisierung der Mitarbeiter für Informationssicherheit||||
||Mitarbeiter sollen bzgl. der Sicherheitsmaßnahmen<br>und der sicherheitsbewussten Handhabung von<br>Dokumenten, Daten und IT-Systemen sowie der<br>ergreifenden Vorsichtsmaßnahmen sensibilisiert<br>werden.||SOLL||
|A.P.2|Verpflichtung der Mitarbeiter zur Einhaltung einschlägiger Gesetze, Vorschriften und Regelungen und der Verfahrensanweisung||||
||Die im Rahmen der Schutzbedarfsanalyse<br>identifizierten rechtlichen Rahmenbedingungen<br>sollen den Mitarbeitern zur Kenntnis gebracht<br>werden.||SOLL||
||Mitarbeiter sollen zur Einhaltung der einschlägigen<br>Gesetze, Vorschriften, Regelungen und der<br>Verfahrensanweisung verpflichtet werden.||SOLL||
|A.P.3|Einweisung zur ordnungsgemäßen Bedienung des Scansystems||||
||Mitarbeiter, die den Scanvorgang durchführen,<br>müssen hinsichtlich der eingesetzten Geräte,<br>Anwendungen und Abläufe geschult werden.<br>Dies umfasst insbesondere:||||
||a|die grundsätzlichen Abläufe im Scanprozess<br>einschließlich der Dokumentenvorbereitung,|MUSS||



Bundesamt für Sicherheit in der Informationstechnik 

11 

|ID|Anforderung|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|---|
|||dem Scannen, der Indexierung, der zulässigen<br>Nachbearbeitung, und der Integritätssicherung|||
||b|die Konfiguration und Nutzung des Scanners<br>und der Scan-Workstation|MUSS||
||c|die Anforderungen hinsichtlich der<br>Qualitätssicherung|MUSS||
||d|die Abläufe und Anforderungen bei der<br>Erstellung des Transfervermerks|MUSS||
||e|die Konfiguration und Nutzung der Systeme<br>zur Integritätssicherung|MUSS||
||f|das Verhalten im Fehlerfall|MUSS||
|A.P.4|Schulung zu Sicherheitsmaßnahmen im Scanprozess||||
||Mitarbeiter, die den Scanprozess durchführen<br>oder verantworten, müssen hinsichtlich der umzusetzenden<br>sowie der implementierten Sicherheitsmaßnahmen geschult<br>werden.<br>Dies umfasst insbesondere:||||
||a|die grundsätzliche Sensibilisierung der<br>Mitarbeiter für Informationssicherheit|MUSS||
||b|Personenbezogene Sicherheitsmaßnahmen im<br>Scanprozess|MUSS||
||c|System-bezogene Sicherheitsmaßnahmen im<br>Scanprozess|MUSS||
||d|Verhalten beim Auftreten von Schadsoftware|MUSS||
||e|Bedeutung der Datensicherung und deren<br>Durchführung|MUSS||



Bundesamt für Sicherheit in der Informationstechnik 

12 

|ID|Anforderung|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|---|
||f|Umgang mit personenbezogenen und anderen<br>sensiblen Daten|MUSS||
||g|Einweisung in Notfallmaßnahmen|MUSS||
|A.P.5|Schulung des Wartungs- und Administrationspersonals||||
||Das Wartungs- und Administrationspersonal<br>soll soweit geschult werden, dass:||||
||a|alltägliche Administrationsaufgaben selbst<br>durchgeführt werden können.|SOLL||
||b|einfache Fehler selbst erkannt und behoben<br>werden können.|SOLL||
||c|Datensicherungen regelmäßig selbsttätig<br>durchgeführt werden können.|SOLL||
||d|Eingriffe von externem Wartungspersonal<br>nachvollzogen werden können.|SOLL||
||e|Manipulationsversuche oder unbefugte<br>Zugriffe auf die Systeme erkannt und zügig<br>behoben werden können.|SOLL||



## P.2.4 Technische Maßnahmen 

|ID|Anforderung|||
|---|---|---|---|
|||M / S|Referenzen / Umsetzung|
|||||
|A.T.1|Grundlegende Sicherheitsmaßnahmen für IT-Systeme im Scanprozess|||



Bundesamt für Sicherheit in der Informationstechnik 

13 

|ID|Anforderung||Referenzen / Umsetzung|
|---|---|---|---|
|||M / S||
|||||
||Basierend auf den Ergebnissen der Schutzbedarfs-<br>/Strukturanalyse SOLLEN für ALLE in den<br>Scanprozess involvierten IT-Systeme (z.B. Client-,<br>Server- und Netzwerkkomponenten) die<br>relevanten Sicherheitsanforderungen (Bausteine)<br>aus dem BSI Grundschutz-Kompendium [BSI-GSK]<br>umgesetzt werden.<br>Für die Prüfung sind vom Auditor hiervon fünf<br>Bausteine Risiko-orientiert auszuwählen; in<br>begründeten Fällen kann der Auditor den<br>Prüfumfang auf zusätzliche Bausteine ausweiten.<br>Der Prüfumfang ist vor dem Audit mit dem BSI<br>abzustimmen.<br>Eine bestehende Zertifizierung nach IT-<br>Grundschutz oder ISO/IEC 27001 nativ, deren<br>Geltungsbereich den zu zertifizierenden<br>Scanprozess abdeckt, KANN die Bausteinprüfung<br>ersetzen.1Die Gültigkeit des jeweiligen Zertifikates<br>MUSS hierbei mindestens noch 12 Monate<br>betragen.|SOLL||
|A.T.2|Festlegung der zulässigen Kommunikationsverbindungen|||
||Sofern die für das Scannen eingesetzten IT-Systeme<br>über ein Netzwerk verbunden sind, müssen in<br>diesem Netzwerk sowie auf den IT-Systemen selbst<br>die zulässigen Kommunikationsverbindungen<br>effektiv vor Zugriffen außerhalb des Netzwerks<br>geschützt werden (Firewall).|MUSS||



1Für den Abgleich des Geltungsbereiches ist dem Auditor Einsicht in die entsprechenden Auditberichte/ -ergebnisse zu gewähren. Fällt der zu zertifizierende Scanprozess nicht in den Geltungsbereich der bestehenden Zertifizierung, muss die Bausteinprüfung erfolgen. 

Bundesamt für Sicherheit in der Informationstechnik 

14 

|ID|Anforderung|Anforderung|||
|---|---|---|---|---|
||||M / S|Referenzen / Umsetzung|
||||||
|A.T.3|||Schutz vor Schadprogrammen||
||Zum Schutz vor Schadprogrammen MÜSSEN<br>für alle relevanten IT-Systeme folgende<br>Maßnahmen umgesetzt werden:||||
||a|Auswahl eines geeigneten Viren-<br>Schutzprogramms|MUSS||
||b|Meldung von Schadprogramm-Infektionen|MUSS||
||c|Aktualisierung der eingesetzten Viren-<br>Schutzprogramme und Signaturen|MUSS||
||d|Regelmäßige Datensicherung|MUSS||
|A.T.4|||Zuverlässige Speicherung||
||Die für die beweiswerterhaltende Aufbewahrung<br>der Scanprodukte und Metadaten verwendeten<br>Speichermedien, Verfahren (z. B. zur<br>Datensicherung) und Konfigurationen müssen für<br>die notwendige Aufbewahrungsdauer bzw. bis zur<br>zuverlässigen Übergabe an einen geeigneten<br>Langzeitspeicher eine Verfügbarkeit gewährleisten,<br>die dem Schutzbedarf der Datenobjekte<br>angemessen ist.||MUSS||



## P.2.5 Sicherheitsmaßnahmen bei der Dokumentenvorbereitung 

|ID|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|
|A.DV.1|Sorgfältige Vorbereitung der Papierdokumente|||



Bundesamt für Sicherheit in der Informationstechnik 

15 

|ID|Anforderung|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|---|
||Um eine zuverlässige und sorgfältige<br>Erfassung zu gewährleisten, müssen<br>Papierdokumente sorgfältig auf das Scannen<br>vorbereitet werden. Dies umfasst folgende<br>Aspekte:||||
||a|Sorgfältige Brieföffnung|MUSS||
|||Prüfung, ob das Dokument offensichtlich<br>manipuliert wurde oder es sich um eine<br>Kopie handelt.|MUSS||
|||Zuordnung zu einer bestimmten<br>Dokumentenklasse, um die entsprechende<br>Vorsortierung zu ermöglichen.|MUSS||
|||Prüfung, ob die Dokumente grundsätzlich für<br>die Erfassung vorgesehen sind.|MUSS||
||b|Prüfung, dass die zu scannenden Dokumente<br>geeignet sind, mit den beim Scannen<br>verwendeten Geräten, Verfahren und<br>Einstellungen fehlerfrei verarbeitet werden<br>zu können.|SOLL||
||c|Maßnahmen für die Bewahrung des<br>logischen Kontextes der zu erfassenden<br>Dokumente|MUSS||
|||Bewahrung der Zugehörigkeit der<br>eingescannten Seiten zu einem Dokument|MUSS||
||d|Die korrekte Orientierung der erfassten<br>Blätter muss erhalten bleiben (Drehung, leere<br>Rückseite)|MUSS||



Bundesamt für Sicherheit in der Informationstechnik 

16 

|ID||Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|---|
|||Ist dies nicht möglich, muss beidseitig erfasst<br>werden.|MUSS||
||e|Bewahrung der korrekten Reihenfolge von<br>Blättern bei mehrseitigen Dokumenten|MUSS||
||f|Zuverlässige Trennung von unabhängigen<br>Dokumenten|MUSS||
||g|Entfernen von Klammern, Knicken und nicht<br>relevanten Klebezetteln|MUSS||
|||Sofern der Inhalt eines Klebezettels relevant<br>ist, muss dieser in geeigneter Weise gescannt<br>werden.|MUSS||
||h|Sofern im Rahmen des Scanprozesses ein<br>Umkopieren notwendig ist, ist darauf zu<br>achten, dass die Kopie alle relevanten<br>Informationen enthält.|MUSS||
|A.DV.2|||Vorbereitung der Vollständigkeitsprüfung||
||Bei automatisierter Erfassung müssen<br>Maßnahmen für die Sicherstellung der<br>Vollständigkeit getroffen werden.||MUSS||
||Damit eine Vollständigkeitsprüfung im Rahmen<br>der Nachbereitung durchgeführt werden kann,<br>sollen entsprechende Vorbereitungen getroffen<br>werden (bei Bedarf).||SOLL||



Bundesamt für Sicherheit in der Informationstechnik 

17 

## P.2.6 Sicherheitsmaßnahmen beim Scannen 

|ID|Anforderung|Anforderung|||
|---|---|---|---|---|
||||M / S|Referenzen / Umsetzung|
||||||
|A.SC.1|||Auswahl und Beschaffung geeigneter Scanner||
||Bei der Auswahl und Beschaffung geeigneter<br>Scanner sollen folgende Kriterien auf ihre<br>Relevanz geprüft und berücksichtigt werden:||||
||a|ausreichender Durchsatz|SOLL||
||b|Unterstützung geeigneter Datenformate|SOLL||
||c|Unterstützung von Patch- und/oder<br>Barcodes zur Dokumententrennung und<br>Übergabe von Meta-Informationen|SOLL||
||d|ausreichende Qualität der Scanprodukte|SOLL||
||e|ausreichende Flexibilität der Konfiguration|SOLL||
||f|Zuverlässiger und leistungsfähiger<br>automatischer Seiteneinzug|SOLL||
||g|Möglichkeit zum Scannen gebundener<br>Dokumente, Überlängen, zum Scannen von<br>Farbe oder von Durchlichtdokumenten (bei<br>Bedarf)|SOLL||
||h|Geeignete Schnittstellen für die<br>Übermittlung des Scanprodukts in<br>DMS/VBS/Archive/Fachanwendungen|SOLL||
||i|Möglichkeit der Absicherung der<br>Administrationsschnittstelle|SOLL||
||j|Nutzung eines internen Datenspeichers|SOLL||



Bundesamt für Sicherheit in der Informationstechnik 

18 

|ID|Anforderung|Anforderung|||
|---|---|---|---|---|
||||M / S|Referenzen / Umsetzung|
||||||
||k|Möglichkeit zum sicheren Löschen oder<br>verschlüsselter Speicherung von<br>Scanprodukten auf dem internen<br>Datenspeicher|SOLL||
||l|ausreichender Support|SOLL||
|A.SC.2|||Zugangs- und Zugriffskontrollen für Scanner||
||Personen, die keinen Zugriff auf Originale,<br>Scanpro-dukte und Scansystem haben dürfen,<br>sollen keinen unbeaufsichtigten Zugang zum<br>Scansystem erhalten.||SOLL||
||Es sollen geeignete Zugangskontrollen und<br>Besucherregelungen vorgesehen werden.||SOLL||
||Um einen hohen Schutz gegen Manipulationen<br>des Scannen bzw. der Konfigurationen, der<br>Dokumente beim Scannen, oder gegen das<br>nachträgliche Auslesen von Scanprodukten vom<br>internen Datenträger des Scanners zu erreichen,<br>soll der Zugang zum Scanner generell auf ein<br>Minimum beschränkt werden.||SOLL||
||Die Administration des Scanners bzw. die<br>Konfiguration der<br>Kommunikationsschnittstellen bei<br>netzwerkfähigen Scannern soll durch ein<br>geeignetes Authentisierungsverfahren geschützt<br>werden.||SOLL||
||Der Zugriff auf die Administrationsschnittstelle<br>soll durch eine geeignete Netzwerk-||SOLL||



Bundesamt für Sicherheit in der Informationstechnik 

19 

|ID|Anforderung|||
|---|---|---|---|
|||M / S|Referenzen / Umsetzung|
|||||
||Konfiguration auf die notwendigen Systeme<br>eingeschränkt werden.|||
|A.SC.3|Änderung voreingestellte Passwörter|||
||Voreingestellte Passwörter müssen nach der<br>Installation des Scanners/Scansystems geändert<br>werden.|MUSS||
||Basis für die Vergabe der Passwörter SOLLEN<br>explizit formulierte interne<br>Sicherheitsrichtlinien unter Berücksichtigung<br>der Empfehlungen aus BSI-Grundschutz (siehe<br>ORP.4.A8) sein.|SOLL||
|A.SC.4|Sorgfältige Durchführung von Konfigurationsänderungen|||
||Bei der Durchführung von<br>Konfigurationsänderungen muss sorgfältig<br>vorgegangen werden.|MUSS||
||Die alte Konfiguration soll zuvor gesichert<br>werden.|SOLL||
||Änderungen sollen von einem Kollegen<br>überprüft werden, bevor diese in den Echtbetrieb<br>übernommen werden.|SOLL||
|A.SC.5||Geeignete Benutzung des Scanners||
||Der eingesetzte Scanner muss gemäß den<br>Vorgaben des Herstellers gepflegt werden.|MUSS||
||Die Dokumente müssen entsprechend den<br>Vorgaben der Produkthandbücher und gemäß<br>der physikalischen Struktur de Dokumente dem<br>Scanner übergeben werden.|MUSS||



Bundesamt für Sicherheit in der Informationstechnik 

20 

|ID|Anforderung|||
|---|---|---|---|
|||M / S|Referenzen / Umsetzung|
|||||
||Für Dokumente, die nicht für den automatischen<br>Einzug geeignet sind, müssen in der<br>Verfahrensdokumentation geeignete Verfahren<br>beschrieben werden.|MUSS||
|A.SC.6||Geeignete Scan-Einstellungen||
||Die Scan-Einstellungen müssen für die<br>jeweiligen Dokumente geeignet gewählt werden.|MUSS||
||Für die Dokumententypen sollen geeignete<br>Profile definiert, getestet und freigegeben<br>werden.|SOLL||
||Spätestens beim Scannen soll geprüft werden,<br>dass geeignete Scan-Einstellungen genutzt<br>werden.|SOLL||
|A.SC.7||Geeignete Erfassung von Metainformationen||
||Index- und Metadaten sollen in geeigneter Weise<br>übergeben werden.|SOLL||
||Hierbei soll eine zuverlässige Konfiguration der<br>Applikation bzgl. der Erkennung und Gültigkeit<br>der ausgelesenen Werte sowie eine sorgfältige<br>manuelle Qualitätssicherung und<br>Nachbearbeitung erfolgen.|SOLL||
|A.SC.8||Qualitätssicherung der Scanprodukte||
||Zur Erkennung mangelhafter Scanvorgänge<br>muss eine geeignete Qualitätskontrolle erfolgen.|MUSS||
||Die Ausgestaltung der Qualitätssicherung soll<br>sich am Scan-Durchsatz und dem Schutzbedarf<br>der verarbeiteten Dokumente orientieren.|SOLL||



Bundesamt für Sicherheit in der Informationstechnik 

21 

|ID|Anforderung|||
|---|---|---|---|
|||M / S|Referenzen / Umsetzung|
|||||
||Die Größe der Stichprobe soll abhängig vom<br>Schutzbedarf der Dokumente und der<br>Zuverlässigkeit des Scansystems bestimmt<br>werden.|SOLL||
||Bei automatisierten Qualitätskontrollen soll eine<br>manuelle Prüfung der automatisch<br>identifizierten Probleme erfolgen.|SOLL||
||Die Vernichtung der Originaldokumente darf<br>nicht vor Abschluss der Qualitätskontrolle<br>erfolgen.|MUSS||
|A.SC.9|Sichere Außerbetriebnahme von Scannern|||
||Bei Außerbetriebnahme müssen alle<br>sicherheitsrelevanten Informationen von den<br>Geräten gelöscht werden.|MUSS||
||Authentisierungsinformationen und<br>gespeicherte Informationen im Scan-Cache<br>müssen gelöscht werden.|MUSS||
||Spezifische Konfigurationsinformationen, die<br>Rückschlüsse auf die Netzwerkstrukturen liefern<br>können, sollen gelöscht werden.|SOLL||
|A.SC.10|Informationsschutz und Zugriffsbeschränkung bei netzwerkfähigen Scannern|||
||Bei Scannern, die über ein Netzwerk<br>angesprochen werden, sollen geeignete<br>Maßnahmen zur Zugriffsbeschränkung und für<br>den Schutz der über das Netzwerk übertragenen<br>Informationen vorgesehen werden.|SOLL||



Bundesamt für Sicherheit in der Informationstechnik 

22 

|ID|Anforderung|Anforderung|||
|---|---|---|---|---|
||||M / S|Referenzen / Umsetzung|
||||||
||Werden Netzlaufwerke für die Ablage von<br>Zwischenergebnissen oder Scanprodukten<br>genutzt, muss der Zugriff auf diese<br>Netzlaufwerke auf das notwendige Minimum<br>eingeschränkt werden.||MUSS||
||Bei Multifunktionsgeräten, die Scan2Mail oder<br>Scan2Fax unterstützen, muss der Versand an<br>ungewünschte Empfängerkreise verhindert<br>werden.||MUSS||
||verarbeitet werden, sollen geeignete<br>kryptographische Mechanismen gemäß BSI TR-<br>02102 oder BSI TR-03116 für die gesicherte<br>Übertragung der Informationen und die<br>Realisierung des Zugriffsschutzes eingesetzt<br>werden.||SOLL||
|A.SC.11|Protokollierung beim Scannen||||
||Für die Sicherstellung der Nachvollziehbarkeit<br>des Scanprozesses soll eine geeignete und in der<br>Verfahrensanweisung näher geregelte Protokollierung<br>erfolgen. Dies soll<br>insbesondere folgende Punkte umfassen:||||
||a|Änderung von kritischen<br>Konfigurationsparametern sowie<br>Authentisierungs- und<br>Berechtigungsfunktionen|SOLL||



Bundesamt für Sicherheit in der Informationstechnik 

23 

|ID|Anforderung|Anforderung|||
|---|---|---|---|---|
||||M / S|Referenzen / Umsetzung|
||||||
||b|Informationen wer das Scansystem wann<br>und in welcher Weise genutzt hat|SOLL||
||c|Informationen ob eine manuelle<br>Nachbearbeitung des Scanprodukts<br>stattgefunden hat|SOLL||
||d|Fehlgeschlagene Authentisierungsvorgänge<br>und sonstige aufgetretene Fehler|SOLL||
||Protokolldaten müssen gemäß den geltenden<br>datenschutzrechtlichen Bestimmungen<br>verarbeitet und vor unautorisiertem Zugriff<br>geschützt werden.||MUSS||
|A.SC.12|Auswahl geeigneter Bildkompressionsverfahren||||
||Es muss auf die Auswahl geeigneter<br>Bildkompressionsverfahren geachtet werden.||MUSS||



## P.2.7 Sicherheitsmaßnahmen bei der Nachbearbeitung 

|ID|||Referenzen / Umsetzung|
|---|---|---|---|
||Anforderung|M / S||
|||||
|A.NB.1|Geeignete und nachvollziehbare Nachbearbeitung|||
||Die Nachbearbeitung des Scanproduktes (z. B.<br>Veränderung des Kontrastes/Helligkeit,<br>Farbreduktion, Beschneiden,<br>Rauschunterdrückung) darf nicht erfolgen, außer<br>sie zielt auf die Erhöhung der Lesbarkeit ab.|MUSS||



Bundesamt für Sicherheit in der Informationstechnik 

24 

|ID|Anforderung|||
|---|---|---|---|
|||M / S|Referenzen / Umsetzung|
|||||
||Die Nachbearbeitung muss sorgfältig<br>durchgeführt werden, damit keine potenziell<br>relevanten Informationen zerstört werden.|MUSS||
||Es muss ausgeschlossen werden (z. B.<br>Protokollierung), dass Inhalte unbemerkt<br>verfälscht werden können.|MUSS||
||Welche Form der Nachbearbeitung in welchen<br>Fällen zulässig ist, soll in der<br>Verfahrensanweisung geregelt werden.|SOLL||
|A.NB.2|Qualitätssicherung der nachbearbeiteten Scanprodukte|||
||Sofern eine Nachbearbeitung erfolgt, muss für die<br>durchgeführten Operationen eine<br>Qualitätssicherung erfolgen.|MUSS||
||Die ursprünglichen Scanprodukte dürfen nicht<br>vor Abschluss der Qualitätssicherung gelöscht<br>werden.|MUSS||
|A.NB.3||Durchführung der Vollständigkeitsprüfung||
||In einem automatisierten Prozess müssen<br>geeignete Maßnahmen zur Sicherstellung der<br>Vollständigkeit getroffen werden.<br>Im Rahmen des Audits werden die getroffenen<br>Maßnahmen zur Vollständigkeitsprüfung erfasst<br>und vom Auditor hinsichtlich der Eignung<br>bewertet.|MUSS||
|A.NB.4|||Transfervermerk|
||Für jedes Scanprodukt soll ein Transfervermerk<br>erstellt werden.|SOLL||



Bundesamt für Sicherheit in der Informationstechnik 

25 

|ID|Anforderung|Anforderung||Referenzen / Umsetzung|
|---|---|---|---|---|
||||M / S||
||||||
||Der Transfervermerk soll insbesondere<br>folgende Aspekte dokumentieren||||
||a|Ersteller des Scanprodukts|SOLL||
||b|Technisches und organisatorisches Umfeld<br>des Erfassungsvorgangs|SOLL||
||c|Etwaige Auffälligkeiten während des<br>Scanprozesses|SOLL||
||d|Zeitpunkt der Erfassung|SOLL||
||e|Ergebnis der Qualitätssicherung|SOLL||
||f|die Tatsache, dass es sich um ein Scanprodukt<br>handelt, das bildlich und inhaltlich mit dem<br>Papierdokument übereinstimmt.|SOLL||
||Der Transfervermerk muss mit dem Scanprodukt<br>logisch verknüpft oder in das Scanprodukt<br>integriert werden.||MUSS||
||Der Transfervermerk muss entsprechend dem<br>Schutzbedarf der verarbeiteten Dokumente<br>geschützt werden.||MUSS||



## P.2.8 Sicherheitsmaßnahmen bei der Integritätssicherung 

|ID|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|
|A.IS.1|Nutzung geeigneter Dienste und Systeme für den Integritätsschutz|||
||Um eine unerkannte nachträgliche Manipulation<br>der während des Scanprozesses entstehenden<br>Datenobjekte (Scanprodukt, Transfervermerk,|MUSS||



Bundesamt für Sicherheit in der Informationstechnik 

26 

|ID|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|
||Index-<br>verhindern, müssen geeignete Mechanismen zum<br>Schutz deren Integrität eingesetzt werden.|||
||Die Widerstandsfähigkeit der Mechanismen muss<br>sich am Schutzbedarf (hinsichtlich der Integrität) der<br>verarbeiteten Datenobjekte orientieren.|MUSS||
||Zum Schutz der Datenobjekte gegen zufällige<br>Änderungen oder aufgrund von Systemfehlern<br>sollen diese jedoch mit einem geeigneten<br>Datensicherungsverfahren gesichert werden.|SOLL||



## P.3 Aufbaumodule 

## P.3.1 Generelle Maßnahmen bei erhöhtem Schutzbedarf 

|ID|Anforderung|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|---|
|A.AM.G.1|Beschränkung des Zugriffs auf sensible Papierdokumente||||
||Bei der Verarbeitung von Dokumenten mit<br>der Integrität, Vertraulichkeit oder<br>Verfügbarkeit sollen während des<br>Scanvorgangs keine unbefugten Personen<br>Zugriff auf die Papierdokumente erhalten.||SOLL||
||Es sollen geeignete Maßnahmen für die<br>Beschränkung des Zugriffs auf die sensiblen<br>Papierdokumente getroffen werden. Dies umfasst:||||
||a|Zugangsbeschränkung zu den<br>Räumlichkeiten in denen die Dokumente<br>verarbeitet werden.|SOLL||



Bundesamt für Sicherheit in der Informationstechnik 

27 

|ID|Anforderung|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|---|
||b|Eine Aufbewahrung, die Schutz vor<br>unbefugtem Zugriff, Einsichtnahme oder<br>Beschädigung bietet.|SOLL||
||c|Die Verpflichtung der Mitarbeiter zur<br>sorgfältigen Handhabung der Dokumente<br>(z. B. kein unbeaufsichtigtes Liegenlassen,<br>keine Weitergabe ohne Prüfung der<br>Autorisierung)|SOLL||
||Sofern nicht bereits generelle Regelungen für<br>den Zugriff auf sensible Papierdokumente<br>existieren, müssen im Rahmen des ersetzenden<br>Scannens entsprechende Regelungen<br>geschaffen werden.||MUSS||
|A.AM.G.2|||Pflicht zur Protokollierung beim Scannen||
||Die in A.SC.11 empfohlene Protokollierung<br>muss erfolgen.||MUSS||
|A.AM.G.3|||Pflicht zur regelmäßigen Auditierung||
||Die in A.O.4 empfohlene Überprüfung der<br>Wirksamkeit und Vollständigkeit der für die<br>Informations-sicherheit beim ersetzenden<br>Scannen vorgesehenen Maßnahmen muss<br>mindestens alle drei Jahre erfolgen.||MUSS||



## P.3.2 Zusätzliche Maßnahmen bei hohen Integritätsanforderungen 

|ID|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|
|A.AM.IN.H.1|Einsatz kryptographischer Mechanismen zum Integritätsschutz|||
||Bei der Verarbeitung von Dokumenten mit|SOLL||



Bundesamt für Sicherheit in der Informationstechnik 

28 

|ID|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|
||bezüglich der Integrität sollen geeignete<br>kryptographische Mechanismen in Form<br>von fortgeschrittenen elektronischen<br>Signaturen, fortgeschrittenen<br>elektronischen Siegeln und/ oder<br>elektronischen Zeitstempeln zum Einsatz<br>kommen.|||
||Sofern keine kryptographischen<br>Mechanismen in Form von<br>fortgeschrittenen elektronischen<br>Signaturen, fortgeschrittenen<br>elektronischen Siegeln und/oder<br>elektronischen Zeitstempeln eingesetzt<br>werden, Andernfalls muss ein schriftlicher<br>Nachweis erbracht werden, dass der für den<br>Integritätsschutz eingesetzte Mechanismus<br>ausreichend widerstandsfähig (siehe<br>Fußnote 31 in A.IS.1) ist.|MUSS||
||Für den Integritätsschutz des<br>dokumentierten Zeitpunktes des Scan-<br>Vorgangs (als Meta-Datum) sollen<br>(qualifizierte) Zeitstempel (Art. 3 Nr. 34<br>eIDAS) verwendet werden.|SOLL||
|A.AM.IN.H.2|Geeignetes Schlüsselmanagement|||
||Sofern schlüsselbasierte kryptographische<br>Mechanismen eingesetzt werden, müssen<br>geeignete Verfahren zum<br>Schlüsselmanagement vorgesehen werden.|MUSS||
||Dabei muss insbesondere über den vor-<br>gesehenen Aufbewahrungszeitraum der|||



Bundesamt für Sicherheit in der Informationstechnik 

29 

|ID|Anforderung|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|---|
||Scanprodukte hin sichergestellt werden, dass||||
||a|die Vertraulichkeit, Integrität und<br>Authentizität der Schlüssel gewahrt<br>bleibt.|MUSS||
||b|private und geheime Schlüssel nicht<br>unbefugt verwendet werden können.|MUSS||
||c|die zur Prüfung der Integritätssicherung<br>erforderlichen Schlüssel und Zertifikate<br>verfügbar bleiben.|MUSS||
||Hierbei sollen die einschlägigen<br>Empfehlungen aus dem IT-Grundschutz-<br>Kompendium des BSI (CON.1,<br>Kryptokonzept), NIST-800-57-1/2, NIST-<br>800-133 und BSI TR-03145 bei der<br>Verwaltung des  Schlüsselmaterials<br>berücksichtigt oder  vertrauenswürdige<br>Dienstleister für das Schlüsselmanagement<br>genutzt werden.||SOLL||
|A.AM.IN.H.3|Auswahl eines geeigneten kryptographischen Verfahrens||||
||Sofern kryptographische Verfahren<br>eingesetzt werden, müssen diese für den<br>jeweiligen Zweck geeignet sein.||MUSS||
||Hierbei sollen Verfahren gemäß BSI TR-<br>02102 oder BSI TR-03116 eingesetzt werden.||SOLL||
||Sofern andere kryptographische Verfahren<br>eingesetzt werden, Andernfalls muss ein<br>schriftlicher Nachweis erbracht werden,<br>dass der eingesetzte Mechanismus||MUSS||



Bundesamt für Sicherheit in der Informationstechnik 

30 

|ID|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|
||ausreichend widerstandsfähig (siehe<br>Fußnote 31 in A.IS.1) ist.|||
|A.AM.IN.H.4|Auswahl eines geeigneten kryptographischen Produktes|||
||Zur Integritätssicherung müssen geeignete<br>Produkte hinsichtlich Funktionalität (insb.<br>Stärke und Widerstandsfähigkeit der<br>Sicherheitsmechanismen) und<br>Vertrauenswürdigkeit (z. B. Einsatz<br>veröffentlichter Algorithmen, Prüfung nach<br>anerkannten Sicherheitsstandards wie CC,<br>FIPS-140) eingesetzt werden.|MUSS||
||Da sich die Sicherheitseignung der<br>kryptographischen Algorithmen ändern<br>kann, soll auf eine leichte Austauschbarkeit<br>der entsprechenden Komponenten geachtet<br>werden.|SOLL||
||Um eine sichere Nutzung der<br>kryptographischen Produkte zu<br>gewährleisten, müssen die notwendigen<br>Einsatzbedingungen und sonstigen<br>Empfehlungen des Herstellers<br>berücksichtigt werden.|MUSS||
|A.AM.IN.H.5|Langfristige Datensicherung bei Einsatz kryptographischer Verfahren|||
||Für die eingesetzten kryptographischen<br>Verfahren soll die Eignung der verwendeten<br>Algorithmen und Parameter regelmäßig<br>evaluiert werden.|SOLL||
||Sofern der Beweiswert von qualifiziert<br>signierten, gesiegelten oder|MUSS||



Bundesamt für Sicherheit in der Informationstechnik 

31 

|ID|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|
||zeitgestempelten Daten über längere<br>Zeiträume erhalten bleiben soll, muss<br>rechtzeitig vor Ablauf der Eignung der<br>kryptographischen Verfahren eine<br>Nachsignatur erfolgen.|||
||Für den Erhalt der Beweiskraft<br>kryptographisch signierter Daten wird der<br>Einsatz der in der BSI TR-03125<br>spezifizierten Verfahren empfohlen.|SOLL||
|A.AM.IN.H.6||Verhinderung ungesicherter Netzzugänge||
||Sofern die für das Scannen eingesetzten IT-<br>Systeme über ein Netzwerk verbunden sind,<br>muss ein ungesicherter Zugang zu diesem<br>Netzwerksegment verhindert werden.|MUSS||
||Ein Zugriff aus dem Internet auf dieses<br>Netzwerk-segment darf nur entkoppelt<br>(Proxy/Gateway) und nur bei Initiierung<br>von innen möglich sein.|MUSS||



## P.3.3 Zusätzliche Maßnahmen bei sehr hohen Integritätsanforderungen 

|ID|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|
|A.AM.IN.SH.1|||4-Augen-Prinzip|
||der Integrität muss im Rahmen der<br>Aufgabenteilung (siehe A.O.1)<br>sichergestellt werden, dass die Erstellung<br>und Qualitätssicherung des Scanproduktes<br>von unterschiedlichen Personen|MUSS||



Bundesamt für Sicherheit in der Informationstechnik 

32 

|ID|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|
||durchgeführt werden. ein 4-Augen-Prinzip<br>umgesetzt werden.|||
|A.AM.IN.SH.2|Einsatz qualifizierter elektronischer Signaturen oder Siegel und Zeitstempel|||
||Sofern Datenobjekte<br>bzgl. der Integrität verarbeitet werden,<br>für Datenobjekte die Verkehrsfähigkeit<br>gefordert ist und<br>die im Rahmen des Scanprozesses<br>entstandenen Datenobjekte (Scanprodukt,<br>Transfervermerk, Index- und Metadaten,<br>Protokolldaten) voraussichtlich als<br>Beweismittel genutzt werden,<br>sollen für die Integritätssicherung des<br>Scanproduktes bzw. des Transfervermerks<br>qualifizierte elektronische Signaturen oder<br>qualifizierte elektronische Siegel und<br>qualifizierte Zeitstempel eingesetzt<br>werden.|SOLL||
||Sofern in diesem Fall andere<br>Sicherheitsmechanismen für die<br>Integritätssicherung eingesetzt werden,<br>Andernfalls muss ein schriftlicher<br>Nachweis erbracht werden, dass der für<br>den Integritätsschutz eingesetzte<br>Mechanismus ausreichend<br>widerstandsfähig (siehe Fußnote 31 in<br>A.IS.1) ist.|MUSS||
|A.AM.IN.SH.3|Eigenständiges Netzsegment|||



Bundesamt für Sicherheit in der Informationstechnik 

33 

|ID|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|
||Bei einem Schutzbedarf der Datenobjekte<br>bzgl. Vertraulichkeit oder Integrität von<br>eingesetzten IT-Systeme in einem<br>eigenständigen Netzsegment eingebunden<br>sein.|MUSS||
||Der Zugriff auf dieses Netzsegment aus<br>anderen Netzsegmenten darf nicht<br>erfolgen, es sei denn die Kommunikation<br>wird über einen Proxy oder ein Gateway<br>vermittelt und der Verbindungsaufbau<br>erfolgt von innen.|MUSS||
|A.AM.IN.SH.4||Kennzeichnung der Dokumente bzgl. Sensitivität||
||Dokumente, die einen Schutzbedarf von<br>sollen als solche gekennzeichnet werden.|SOLL||
||Die Kennzeichnung soll deutlich sichtbar<br>angebracht werden.|SOLL||



## P.3.4 Zusätzliche Maßnahmen bei hohen Vertraulichkeitsanforderungen 

|ID|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|
|A.AM.VT.H.1||Sensibilisierung und Verpflichtung der Mitarbeiter||
||Bei der Verarbeitung von Dokumenten mit<br>einem Schutzbedarf hinsichtlich der<br>müssen die Mitarbeiter bzgl. der<br>Sicherheitsmaßnahmen und der<br>sicherheitsbewussten Handhabung von|MUSS||



Bundesamt für Sicherheit in der Informationstechnik 

34 

|ID|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|
||Dokumenten, Daten und IT-Systemen und<br>der zu ergreifenden Vorsichtsmaßnahmen<br>sensibilisiert und geschult werden.|||
||Mitarbeiter müssen durch eine explizite<br>Verfahrensanweisung auf die Einhaltung<br>der einschlägigen Gesetze, Vorschriften<br>und Regelungen verpflichtet werden.|MUSS||
|A.AM.VT.H.2||Verhinderung ungesicherter Netzzugänge||
||Sofern die für das Scannen eingesetzten IT-<br>Systeme über ein Netzwerk verbunden<br>sind, muss ein ungesicherter Zugang zu<br>diesem Netzwerksegment verhindert<br>werden.|MUSS||
||Ein Zugriff aus dem Internet auf dieses<br>Netzwerksegment darf nur entkoppelt<br>(Proxy/Gateway) und nur bei Initiierung<br>von innen möglich sein.|MUSS||
|A.AM.VT.H.3||Löschen von Zwischenergebnissen||
||Bei der Verarbeitung von Dokumenten mit<br>einem Schutzbedarf hinsichtlich der<br>Vertraulichkeit von<br>müssen die in der Verarbeitung<br>entstehenden Zwischenergebnisse (z. B.<br>rohe Scanprodukte, Daten im Scan-Cache)<br>zuverlässig gelöscht werden.|MUSS||



Bundesamt für Sicherheit in der Informationstechnik 

35 

## P.3.5 Zusätzliche Maßnahmen bei sehr hohen Vertraulichkeitsanforderungen 

|ID|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|
|-|Bei der Verarbeitung von<br>Verschlusssachen müssen die<br>Anforderungen der VSA berücksichtigt<br>werden.|MUSS||
|A.AM.VT.SH.1|Kennzeichnung der Dokumente bzgl. Sensitivität|||
||Dokumente, die einen Schutzbedarf von<br>Vertraulichkeit<br>besitzen, sollen als solche gekennzeichnet<br>werden.|SOLL||
||Die Kennzeichnung soll deutlich sichtbar<br>angebracht werden.|SOLL||
|A.AM.VT.SH.2|Ordnungsgemäße Entsorgung von schützenswerten Betriebsmitteln|||
||Sofern der Scanner einen internen<br>Speicher besitzt und Dokumente gescannt<br>werden, die einen Schutzbedarf bzgl. der<br>muss der Datenträger vor der Entsorgung<br>des Scanners zuverlässig gelöscht werden.|MUSS||
||Sofern möglich soll der Datenträger<br>ausgebaut und mit einem geeigneten<br>Verfahren zuverlässig gelöscht oder<br>zerstört werden.|SOLL||
||Kryptographische Schlüssel, die im zu<br>entsorgenden Scanner vorgehalten<br>werden, müssen zuverlässig gelöscht oder<br>deaktiviert werden.|MUSS||
|A.AM.VT.SH.3|Besondere Zuverlässigkeit und Vertrauenswürdigkeit der Mitarbeiter|||



Bundesamt für Sicherheit in der Informationstechnik 

36 

|ID|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|
||Sofern Dokumente gescannt werden,<br>deren Schutzbedarf hinsichtlich der<br>sichergestellt werden, dass die Mitarbeiter,<br>die für den Scanprozess verantwortlich<br>sind und den Prozess durchführen<br>besonders zuverlässig und<br>vertrauenswürdig sind.|SOLL||
|A.AM.VT.SH.4|Verschlüsselte Datenübertragung innerhalb des Scansystems|||
||Bei der Verarbeitung von Datenobjekten<br>bzgl. der Vertraulichkeit soll die<br>Datenübertragung zwischen Scanner,<br>Scan-Workstation, Scan-Cache und<br>anderen damit zusammenhängenden<br>Systemen durch geeignete<br>Verschlüsselungsverfahren gemäß BSI TR-<br>02102 oder BSI TR-03116 erfolgen.|SOLL||
||Andernfalls muss ein geeigneter Nachweis<br>erbracht werden, dass diese<br>Kommunikationsverbindungen durch<br>alternative Maßnahmen ausreichend<br>geschützt sind.|MUSS||



## P.3.6 Zusätzliche Maßnahmen bei hohen Verfügbarkeitsanforderungen 

|ID|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|
|A.AM.VF.H.1||Erweiterte Qualitätssicherung der Scanprodukte||
||Bei einem Schutzbedarf der Datenobjekte|SOLL||



Bundesamt für Sicherheit in der Informationstechnik 

37 

|ID|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|
||die Qualitätskontrolle der Scanprodukte<br>durch eine vollständige Sichtkontrolle<br>erfolgen.<br>Bei einem sehr hohen Durchsatz KANN die<br>Sichtkontrolle sukzessive auf regelmäßig<br>durchgeführte Stichproben reduziert<br>werden, wobei deren Größe den<br>Stichprobenumfang der Sichtkontrolle des<br>Schutzbedarfs<br>übertreffen MUSS. In regelmäßigen<br>zeitlichen Abständen MUSS die<br>Qualitätssicherung durch eine vollständige<br>Sichtkontrolle erfolgen|||
||Falls keine vollständige Sichtkontrolle<br>realisiert wird, SOLLEN automatische<br>Mechanismen zur Qualitätskontrolle<br>eingesetzt werden, wie z.B. eine<br>automatische Erkennung von Leerseiten,<br>von unzureichender Bildqualität oder die<br>Prüfung der Seitenzahl (z.B. gegen die auf<br>Vorblättern angegebenen Meta-Daten).|SOLL||
||Beim Einsatz automatisierter Mechanismen<br>MUSS eine manuelle Prüfung der<br>identifizierten Probleme und<br>Auffälligkeiten erfolgen.|MUSS||
|A.AM.VF.H.2|Fehlertolerante Protokolle und redundante Datenhaltung|||
||Verfügbarkeit wird die Verwendung eines<br>fehlertoleranten Übertragungsprotokolls<br>sowie eine redundante Datenhaltung<br>empfohlen.|SOLL||



Bundesamt für Sicherheit in der Informationstechnik 

38 

## P.3.7 Zusätzliche Maßnahmen bei sehr hohen Verfügbarkeitsanforderungen 

|ID|Anforderung|M / S|Referenzen / Umsetzung|
|---|---|---|---|
|A.AM.VF.SH.1|Vollständige Sichtkontrolle zur Qualitätssicherung der Scanprodukte|||
||Bei einem Schutzbedarf der Datenobjekte<br>bzgl. der Verfügbarkeit<br>soll die Qualitätskontrolle der<br>Scanprodukte durch eine vollständige<br>Sichtkontrolle erfolgen.|SOLL||
|A.AM.VF.SH.2|Test der Geräte und Einstellungen mit ähnlichen Dokumenten|||
||Bei Datenobjekten mit einem<br>bzgl. der<br>Verfügbarkeit muss die Eignung der<br>verwendeten Geräte, Verfahren und<br>Einstellungen vorher mit physikalisch<br>ähnlichen Dokumenten, die selbst keinen<br>hohen Schutzbedarf bzgl. der<br>Verfügbarkeit haben, getestet und das<br>Prüfergebnis dokumentiert werden.|MUSS||



Bundesamt für Sicherheit in der Informationstechnik 

39 

## P4. Weitere Ausführungen 

Bundesamt für Sicherheit in der Informationstechnik 

40 


![](markdown/tr/TR-03138-Anlage-P_V1_4_Formularfelder/TR-03138-Anlage-P_V1_4_Formularfelder.pdf-0041-00.png)


Bundesamt für Sicherheit in der Informationstechnik 

41 


![](markdown/tr/TR-03138-Anlage-P_V1_4_Formularfelder/TR-03138-Anlage-P_V1_4_Formularfelder.pdf-0042-00.png)


Bundesamt für Sicherheit in der Informationstechnik 

42 

Literaturverzeichnis 

## Literaturverzeichnis 

[BSI-TR03138] 

[BSI-TR03138-R] 

Bundesamt für Sicherheit in der Informationstechnik (BSI): Ersetzendes Scannen, Technische Richtlinie (TR) des BSI Nr. 03138 (TR RESISCAN), Version 1.4, 2019 

Bundesamt für Sicherheit in der Informationstechnik (BSI): Ersetzendes Scannen - Anwendungshinweis R: Unverbindliche rechtliche Hinweise, Anwendungshinweis R, Version 1.2, 2018, Technische Richtlinie (TR) des BSI Nr. 03138 (TR RESISCAN), Version 1.2, 2018 

Bundesamt für Sicherheit in der Informationstechnik 

43 


## BSI Technische Richtlinie 03138 Ersetzendes Scannen 

Bezeichnung: Ersetzendes Scannen (RESISCAN) Anlage P – Prüfspezifikation Kürzel: BSI TR-03138-P Version: 1.5 Datum: 21.11.2024 

Bundesamt für Sicherheit in der Informationstechnik 

2 

Anlage P – Prüfspezifikation (normativ) 

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn Tel.: +49 22899 9582-0 E-Mail:  resiscan@bsi.bund.de Internet: https://www.bsi.bund.de © Bundesamt für Sicherheit in der Informationstechnik 2024 

Bundesamt für Sicherheit in der Informationstechnik 

3 

## Inhaltsverzeichnis 

Anlage P – Prüfspezifikation (normativ) .......................................................................................................................................... 5 P.1 Grundlegendes zur Konformitätsprüfung .......................................................................................................................... 5 P.1.1 Konkretisierung des Prüfgegenstandes ....................................................................................................................... 5 P.1.2 Verweis auf Referenzdokumente ................................................................................................................................... 5 P.2 Basismodul ....................................................................................................................................................................................... 6 P.2.1 Grundlegende Anforderungen ........................................................................................................................................ 7 P.2.2 Organisatorische Maßnahmen ........................................................................................................................................ 8 P.2.3 Personelle Maßnahmen .................................................................................................................................................... 12 P.2.4 Technische Maßnahmen .................................................................................................................................................. 14 P.2.5 Sicherheitsmaßnahmen bei der Dokumentenvorbereitung ............................................................................ 16 P.2.6 Sicherheitsmaßnahmen beim Scannen ..................................................................................................................... 18 P.2.7 Sicherheitsmaßnahmen bei der Nachbearbeitung ............................................................................................... 24 P.2.8 Sicherheitsmaßnahmen bei der Integritätssicherung ......................................................................................... 26 P.3 Aufbaumodule .............................................................................................................................................................................. 27 P.3.1 Generelle Maßnahmen bei erhöhtem Schutzbedarf ............................................................................................ 27 P.3.2 Zusätzliche Maßnahmen bei hohen Integritätsanforderungen ...................................................................... 28 P.3.3 Zusätzliche Maßnahmen bei sehr hohen Integritätsanforderungen ............................................................ 33 P.3.4 Zusätzliche Maßnahmen bei hohen Vertraulichkeitsanforderungen .......................................................... 35 P.3.5 Zusätzliche Maßnahmen bei sehr hohen Vertraulichkeitsanforderungen ................................................ 36 P.3.6 Zusätzliche Maßnahmen bei hohen Verfügbarkeitsanforderungen ............................................................. 38 P.3.7 Zusätzliche Maßnahmen bei sehr hohen Verfügbarkeitsanforderungen ................................................... 38 P.4 Besonderheiten beim mobilen ersetzenden Scannen .................................................................................................. 39 P.4.1 Einführung in das mobile Scannen ............................................................................................................................. 39 P.4.2 Basismodul mobiles Scannen ......................................................................................................................................... 39 P.4.3 Aufbaumodule ...................................................................................................................................................................... 48 Referenzen .................................................................................................................................................................................................. 51 

Bundesamt für Sicherheit in der Informationstechnik 

4 

Anlage P – Prüfspezifikation (normativ) 

## Anlage P – Prüfspezifikation (normativ) 

## P.1 Grundlegendes zur Konformitätsprüfung 

Im Rahmen der Konformitätsprüfung für die vorliegende Richtlinie wird verifiziert, ob die in [BSI-TR03138] (Abschnitte 3, 4 und 5)[1] definierten Anforderungen vom betrachteten Scansystem erfüllt werden. Hierzu wird sowohl die Verfahrensdokumentation als auch das implementierte Scansystem mit den praktizierten Prozessen geprüft. 

## P.1.1 Konkretisierung des Prüfgegenstandes 

Prüfgrundlage für Konformitätsprüfungen und Audits nach [BSI-TR03138] ist ausschließlich die BSI TR-03138 mit der zugehörigen Prüfspezifikation Anlage P. Ein TRRESISCAN-Audit umfasst ausschließlich die Prüfung der Testfälle gemäß Anlage P (Basismodule + Aufbaumodule in Abhängigkeit des ermittelten Schutzbedarfs)[2] : Eine Zertifizierung gemäß [ISO/IEC 27001] nativ oder BSI-Grundschutz ist keine Voraussetzung oder Erfordernis für eine Zertifizierung nach [BSI-TR03138][3] : Auch die Anwendung der Vorgehensweise nach BSI-Grundschutz oder die Nutzung bzw. Umsetzung von BSI-Grundschutz oder anderer BSI-Standards ist keine Voraussetzung für eine Zertifizierung nach [BSI-TR03138]. 

## P.1.2 Verweis auf Referenzdokumente 

Um den Prozess der Prüfung und Zertifizierung effizient zu gestalten, SOLL der Antragsteller im Rahmen der Beantragung der Zertifizierung das Dokument „Nachweise für die Konformitätsprüfung gemäß BSI TR-03138 Ersetzendes Scannen“ ausgefüllt einreichen. 

- 1  Abschnitt 5 ist optional zu berücksichtigen, wenn das mobile Scannen betrachtet werden soll im Rahmen der Zertifizierung 

- 2 Alle übrigen formalen Verfahrensgrundlagen zur Zertifizierung nach Technischen Richtlinien (allgemein) - d.h. Verfahrensbeschreibung etc. - sind unter https://www.bsi.bund.de/zertifizierungtr  veröffentlicht. 

- 3  Disclaimer: Aus Gründen der Übersichtlichkeit und Lesbarkeit wird im Folgenden nur vom BSI-Grundschutz gesprochen. Alle diesbezüglichen Ausführungen gelten synonym auch für die Nutzung von ISO/IEC 27001 (inkl. ISO/IEC 27002 ff.) nativ oder BSI-Grundschutz. 

Bundesamt für Sicherheit in der Informationstechnik 

5 

## P.2 Basismodul 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|---|
|01|15|3.1|-|**Strukturanalyse**||||||
|||||Die Strukturanalyse identifiziert die relevanten||||||
|||||a|Datenobjekte|MUSS||||
|||||b|IT-Systeme und Anwendungen|MUSS||||
|||||c|Kommunikationsverbindungen (Netze)|MUSS||||
|||||Netzplan liegt vor.||MUSS||||
|02|19|4.2.1.2|A.G.2|**Schutzbedarfsanalyse**||||||
|||||Der Schutzbedarf der weiteren Datenobjekte ergibt sich aus dem Schutzbedarf der<br>Papieroriginale.||||||
|||||Der Schutzbedarf der Datenobjekte muss hinsichtlich der Schutzziele<br>Integrität, Vertraulichkeit und Verfügbarkeit bestimmt werden.||MUSS||||



Bundesamt für Sicherheit in der Informationstechnik 

6 

Anlage P – Prüfspezifikation (normativ) 

## P.2.1 Grundlegende Anforderungen 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|---|
|03|18|4.2.1.1|A.G.1|**Verfahrensdokumentation**||||||
|||||Die Verfahrensdokumentation muss die folgenden Aspekte umfassen:||||||
|||||a|Art der verarbeiteten Dokumente|MUSS||||
||||||Regelungen für nicht verarbeitete Dokumente|||||
||||||Festlegung der Verantwortlichkeiten im Scanprozess|||||
||||||Festlegung der Abläufe im Scanprozess|||||
||||||Festlegung der Aufgaben im Scanprozess|||||
|||||b|Festlegung von Maßnahmen zur Qualifizierung und Sensibilisierung der<br>Mitarbeiterinnen und Mitarbeiter|MUSS||||
|||||c|Beschreibung der dem Schutzbedarf entsprechender Anforderungen an<br>Räume, IT-Systeme, Anwendungen und Sicherungsmittel|MUSS||||
|||||d|Regelungen für die Administration und Wartung der IT-Systeme und<br>Anwendungen|MUSS||||
|||||e|Festlegung von Sicherheitsanforderungen für IT-Systeme, Netze und<br>Anwendungen|SOLLTE||||
|||||f|Beschreibung der Umsetzung der Sicherheitsmaßnahmen entsprechend<br>dem definierten Schutzbedarf anhand des tatsächlich implementierten<br>Scanprozesses|MUSS||||
|||||g|Verfahrensanweisung, für die am Scanprozess beteiligten Personen|MUSS||||



Bundesamt für Sicherheit in der Informationstechnik 

7 

## P.2.2 Organisatorische Maßnahmen 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|---|
|04|19|4.2.2.1|A.O.1|**Festlegung von Verantwortlichkeiten, Abläufen und Aufgaben im Scanprozess**||||||
|||||Verantwortlichkeiten, Abläufe und Aufgaben müssen festgelegt sein. Dies umfasst<br>insbesondere:||||||
|||||a|Welche Schritte werden durch wen ausgeführt und wie ist dabei im<br>Einzelnen vorzugehen?|MUSS||||
|||||b|Welche Dokumente werden gescannt und welche Daten werden hierbei<br>erzeugt?|MUSS||||
|||||c|Welche Qualitätskontrollen werden durch wen in welchen Zeitabständen<br>und nach welchen Kriterien durchgeführt?|MUSS||||
|||||d|Welche Sicherungsdaten oder Sicherungssysteme sind für den Schutz der<br>Integrität dieser Daten vorgesehen?|MUSS||||
|||||e|Qualitätskontrollen müssen mindestens stichprobenartig erfolgen.|MUSS||||
||||||Qualitätskontrollen sollten regelmäßig durch Mitarbeiterinnen und<br>Mitarbeiter durchgeführt werden, die nicht mit der operativen<br>Durchführung des zu kontrollierenden Arbeitsschritts betraut sind.|SOLLTE||||
|||||f|Für die in den Scanprozess involvierten Datenobjekte sowie die genutzten<br>IT-Systeme und Anwendungen sollten Verantwortliche benannt werden.|SOLLTE||||
|||||g|Bei der Zuweisung des Personals zu den operativen Aufgaben im<br>Scanprozess müssen potenzielle Interessenkonflikte berücksichtigt werden.|MUSS||||



Bundesamt für Sicherheit in der Informationstechnik 

8 

Anlage P – Prüfspezifikation (normativ) 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|---|
||||||Bei der Zuweisung des Personals zu den operativen Aufgaben im<br>Scanprozess sollten potenzielle Interessenkonflikte nach Möglichkeit<br>vermieden werden.|SOLLTE||||
|||||h|Typische Fehlerquellen müssen berücksichtigt werden.|MUSS||||
||||||Für typische Fehlerquellen sollten entsprechende Vorsichtsmaßnahmen<br>festgelegt werden.|SOLLTE||||
|||||i|Es muss festgelegt werden, unter welchen Umständen und ab welchem<br>Zeitpunkt das Originaldokument vernichtet werden darf.|MUSS||||
|||||j|Es muss ein Verfahren zur Klärung von „Zweifelsfragen“ etabliert werden.|MUSS||||
|05|20|4.2.2.2|A.O.2|**Regelungen für Wartungs- und Reparaturarbeiten**||||||
|||||Es sollten Regelungen für die Wartung und die Reparatur der eingesetzten IT-Systeme<br>und Anwendungen getroffen werden. Dies umfasst insbesondere:||||||
|||||a|Festlegung der Verantwortlichkeit für die Beauftragung, Durchführung und<br>Kontrolle von Wartungs- und Reparaturarbeiten|SOLLTE||||
|||||b|Verfahren für die regelmäßige Bereitstellung und Anwendung von<br>sicherheitsrelevanten Updates|SOLLTE||||
|||||c|Regelung zur Authentisierung und zum Nachweis der Autorisierung des<br>Wartungspersonals|SOLLTE||||
|||||d|Regelungen zum Schutz personenbezogener oder anderweitig besonders<br>schützenswerter Daten (z. B. Betriebsgeheimnisse) auf den zu wartenden IT-<br>Systemen|SOLLTE||||



Bundesamt für Sicherheit in der Informationstechnik 

9 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|---|
|||||e|Dokumentation von sicherheitsrelevanten Veränderungen an den<br>involvierten IT-Systemen und Anwendungen|SOLLTE||||
|||||f|Dokumentation der erfolgreichen Durchführung der Maßnahmen zur<br>Qualitätskontrolle und Freigabe vor Wiederaufnahme des regulären<br>Betriebs|SOLLTE||||
|06|20|4.2.2.3|A.O.3|**Abnahme- und Freigabe-Verfahren für Hardware und Software**||||||
|||||Es muss ein Verfahren für die Abnahme und Freigabe der eingesetzten Hard-<br>und Software etabliert werden; dies umfasst Scanner, Scan-Workstation und<br>Scan-Cache.||MUSS||||
|||||Neben der initialen Inbetriebnahme ist dieses Abnahmeverfahren auch bei der<br>Wiederaufnahme des Betriebs nach Wartungs- und Reparaturarbeiten<br>durchzuführen.||MUSS||||
|07|21|4.2.2.4|A.O.4|**Aufrechterhaltung der Informationssicherheit**||||||
|||||In angemessenen zeitlichen Abständen muss eine Überprüfung der<br>Wirksamkeit und Vollständigkeit der für die Informationssicherheit beim<br>ersetzenden Scannen vorgesehenen Maßnahmen durchgeführt werden.||MUSS||||
|||||In diesen Audits muss geprüft werden:||||||
|||||a|Ob Prozesse und Sicherheitsmaßnahmen korrekt implementiert wurden<br>und wirksam sind.|MUSS||||
|||||b|Ob die Sicherheitsmaßnahmen ausreichend vor den potenziellen<br>Bedrohungen schützen oder ob zusätzliche oder korrigierte<br>Sicherheitsmaßnahmen notwendig sind.|MUSS||||
|||||Audits sollten von unabhängigen Personen durchgeführt werden.||SOLLTE||||



Bundesamt für Sicherheit in der Informationstechnik 

10 

Anlage P – Prüfspezifikation (normativ) 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|---|
|||||Die Ergebnisse der Audits sollten schriftlich dokumentiert werden.||SOLLTE||||
|||||Aus identifizierten Sicherheitslücken oder Probleme müssen<br>Korrekturmaßnahmen abgeleitet werden.||MUSS||||
|||||Für die Umsetzung von Korrekturmaßnahmen muss ein Zeitplan mit<br>Verantwortlichkeiten definiert werden.||MUSS||||
|||||Die Umsetzung der Maßnahmen muss durch die Verantwortlichen verfolgt<br>und überprüft werden.||MUSS||||
|08|21|4.2.2.5|A.O.5|**Anforderungen beim Outsourcing des Scanprozesses**||||||
|||||Wird der Scanprozess von spezialisierten Scandienstleistern durchgeführt, sind<br>die Anforderungen der TR-RESISCAN umzusetzen.||MUSS||||
|||||Darüber hinaus gelten folgende Anforderungen:||||||
|||||a|Organisatorische und technische Schnittstellen zwischen Auftraggebenden<br>und Auftragnehmenden müssen in der Verfahrensdokumentation explizit<br>dargestellt werden. (Übertragungswege, Datenablageorte, beteiligte Akteure,<br>Rückfallverfahren, Maßnahmen zur Integritäts- und<br>Vollständigkeitskontrolle etc.)|MUSS||||
|||||b|Der Auftragnehmende muss zur Einhaltung der vom Auftraggebenden<br>definierten Sicherheitsmaßnahmen verpflichtet werden.|MUSS||||
|||||c|Es sollte eine Analyse der durch die Aufgabenteilung zusätzlich<br>entstehenden Risiken erfolgen.|SOLLTE||||
|||||d|Zusätzlich zur regelmäßigen Auditierung sollten unangemeldete<br>Stichproben durchgeführt werden.|SOLLTE||||



Bundesamt für Sicherheit in der Informationstechnik 

11 

## P.2.3 Personelle Maßnahmen 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|---|
|09|22|4.2.3.1|A.P.1.|**Verpflichtung der Mitarbeiter zur Einhaltung einschlägiger Gesetze, Vorschriften und Regelungen und der Verfahrensanweisung**||||||
|||||Die im Rahmen der Schutzbedarfsanalyse identifizierten rechtlichen<br>Rahmenbedingungen sollten den Mitarbeiterinnen und Mitarbeitern zur<br>Kenntnis gebracht werden.||SOLLTE||||
|||||Mitarbeiterinnen und Mitarbeitern sollten zur Einhaltung der einschlägigen<br>Gesetze, Vorschriften, Regelungen und der Verfahrensanweisung verpflichtet<br>werden.||SOLLTE||||
|10|22|4.2.3.2|A.P.2|**Einweisung zur ordnungsgemäßen Bedienung des Scansystems**||||||
|||||Mitarbeiterinnen und Mitarbeiter, die den Scanvorgang durchführen, müssen<br>hinsichtlich der eingesetzten Geräte, Anwendungen und Abläufe geschult werden. Dies<br>umfasst insbesondere:||||||
|||||a|Die grundsätzlichen Abläufe im Scanprozess einschließlich der<br>Dokumentenvorbereitung, dem Scannen, der Indexierung, der zulässigen<br>Nachbearbeitung, und der Integritätssicherung|MUSS||||
|||||b|Die Konfiguration und Nutzung des Scanners und der Scan-Workstation|MUSS||||
|||||c|Die Anforderungen hinsichtlich der Qualitätssicherung|MUSS||||
|||||d|Die Abläufe und Anforderungen beider Erstellung des Transfervermerks|MUSS||||
|||||e|Die Konfiguration und Nutzung der Systeme zur Integritätssicherung|MUSS||||
|||||f|Das Verhalten im Fehlerfall|MUSS||||
|11|22|4.2.3.3|A.P.3|**Schulung zu Sicherheitsmaßnahmen im Scanprozess**||||||



Bundesamt für Sicherheit in der Informationstechnik 

12 

Anlage P – Prüfspezifikation (normativ) 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|---|
|||||Mitarbeiterinnen und Mitarbeiter, die den Scanprozess durchführen oder verantworten,<br>müssen hinsichtlich der umzusetzenden sowie der implementierten<br>Sicherheitsmaßnahmen geschult werden. Dies umfasst insbesondere:||||||
|||||a|Die grundsätzliche Sensibilisierung der Mitarbeiterinnen und Mitarbeiter<br>für Informationssicherheit|MUSS||||
|||||b|Personenbezogene Sicherheitsmaßnahmen im Scanprozess|MUSS||||
|||||c|Systembezogene Sicherheitsmaßnahmen im Scanprozess|MUSS||||
|||||d|Verhalten beim Auftreten von Schadsoftware|MUSS||||
|||||e|Bedeutung der Datensicherung und deren Durchführung|MUSS||||
|||||f|Umgang mit personenbezogenen und anderen sensiblen Daten|MUSS||||
|||||g|Einweisung in Notfallmaßnahmen|MUSS||||
|12|23|4.2.3.4|A.P.4|**Schulung des Wartungs- und Administrationspersonals**||||||
|||||Das Wartungs- und Administrationspersonal sollte soweit geschult werden, dass:||||||
|||||a|Alltägliche Administrationsaufgaben selbst durchgeführt werden können.|SOLLTE||||
|||||b|Einfache Fehler selbst erkannt und behoben werden können.|SOLLTE||||
|||||c|Datensicherungen regelmäßig selbsttätig durchgeführt werden können.|SOLLTE||||
|||||d|Eingriffe von externem Wartungspersonal nachvollzogen werden können.|SOLLTE||||
|||||e|Manipulationsversuche oder unbefugte Zugriffe auf die Systeme erkannt<br>und zügig behoben werden können.|SOLLTE||||



Bundesamt für Sicherheit in der Informationstechnik 

13 

## P.2.4 Technische Maßnahmen 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|13|23|4.2.4.1|A.T.1|**Grundlegende Sicherheitsmaßnahmen für IT-Systeme im Scanprozess**|||||
|||||Basierend auf den Ergebnissen der Schutzbedarfs-/Strukturanalyse müssen für<br>ALLE in den Scanprozess involvierten IT-Systeme (z.B. Client-, Server- und<br>Netzwerkkomponenten) die relevanten Sicherheitsanforderungen (Bausteine)<br>aus dem BSI Grundschutz-Kompendium [BSI-GSK] oder entsprechende<br>äquivalente Maßnahmen auf Basis [ISO27001] [ISO27002] umgesetzt werden.<br>Für die Prüfung nach BSI Grundschutz-Kompendium [BSI-GSK] sind vom<br>Auditor hiervon fünf Bausteine Risiko-orientiert auszuwählen; in begründeten<br>Fällen kann der Auditor den Prüfumfang auf zusätzliche Bausteine ausweiten.<br>Der Prüfumfang ist vor dem Audit mit dem BSI abzustimmen.<br>Eine bestehende Zertifizierung nach IT-Grundschutz oder [ISO/IEC 27001]<br>nativ, deren Geltungsbereich den zu zertifizierenden Scanprozess abdeckt,<br>kann die Bausteinprüfung ersetzen. Die Gültigkeit des jeweiligen Zertifikates<br>muss hierbei mindestens noch 12 Monate betragen.4|MUSS||||
|14|23|4.2.4.2|A.T.2|**Festlegung der zulässigen Kommunikationsverbindungen**|||||



- 4 Für den Abgleich des Geltungsbereiches ist dem Auditor Einsicht in die entsprechenden Auditberichte/ -ergebnisse zu gewähren. Fällt der zu zertifizierende Scanprozess nicht in den Geltungsbereich der bestehenden Zertifizierung, muss die Bausteinprüfung erfolgen. 

Bundesamt für Sicherheit in der Informationstechnik 

14 

Anlage P – Prüfspezifikation (normativ) 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|---|
|||||Sofern die für das Scannen eingesetzten IT-Systeme über ein Netzwerk<br>verbunden sind, müssen in diesem Netzwerk sowie auf den IT-Systemen selbst<br>die zulässigen Kommunikationsverbindungen effektiv vor Zugriffen außerhalb<br>des Netzwerks geschützt werden (Firewall).<br>Bei der Festlegung der zulässigen Kommunikationsverbindungen müssen die<br>jeweiligen Anforderungen der [TR-02102-1] bezogen auf das eingesetzte und in<br>der Strukturanalyse beschriebene Scansystem beachtet werden.<br>Dies kann durch eine zugehörige Erklärung der Organisation sichergestellt<br>werden.||MUSS||||
|15|24|4.2.4.3|A.T.3|**Schutz vor Schadprogrammen**||||||
|||||Zum Schutz vor Schadprogrammen MÜSSEN für alle relevanten IT-Systeme folgende<br>Maßnahmen umgesetzt werden:||||||
|||||a|Auswahl eines geeigneten Viren-Schutzprogramms|MUSS||||
|||||b|Meldung von Schadprogramm-Infektionen|MUSS||||
|||||c|Aktualisierung der eingesetzten Viren-Schutzprogramme und Signaturen|MUSS||||
|||||d|Regelmäßige Datensicherung.|MUSS||||
|16|24|4.2.4.4|A.T.4|**Zuverlässige Speicherung**||||||
|||||Die für die beweiswerterhaltende Aufbewahrung der Scanprodukte und<br>Metadaten verwendeten Speichermedien, Verfahren (z. B. zur Datensicherung)<br>und Konfigurationen müssen für die notwendige Aufbewahrungsdauer bzw.<br>bis zur zuverlässigen Übergabe an einen geeigneten Langzeitspeicher eine<br>Verfügbarkeit gewährleisten, die dem Schutzbedarf der Datenobjekte<br>angemessen ist.||MUSS||||



Bundesamt für Sicherheit in der Informationstechnik 

15 

## P.2.5 Sicherheitsmaßnahmen bei der Dokumentenvorbereitung 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|---|
|17|24|4.2.5.1|A.DV.1|**Sorgfältige Vorbereitung der Papierdokumente**||||||
|||||Um eine zuverlässige und sorgfältige Erfassung zu gewährleisten, müssen<br>Papierdokumente sorgfältig auf das Scannen vorbereitet werden. Dies umfasst folgende<br>Aspekte:||||||
|||||a|Sorgfältige Brieföffnung (bei Bedarf das Aufbringen von<br>Posteingangsnachweisen, z.B. Durch QR-Code auf Trennblättern etc.)|SOLLTE||||
||||||Prüfung, ob das Dokument offensichtlich manipuliert wurde oder es sich<br>um eine Kopie handelt.|SOLLTE||||
||||||Zuordnung zu einer bestimmten Dokumentenklasse, um die entsprechende<br>Vorsortierung zu ermöglichen.|SOLLTE||||
||||||Prüfung, ob die Dokumente grundsätzlich für die Erfassung vorgesehen<br>sind.|MUSS||||
|||||b|Prüfung, dass die zu scannenden Dokumente geeignet sind, mit den beim<br>Scannen verwendeten Geräten, Verfahren und Einstellungen fehlerfrei<br>verarbeitet werden zu können.|SOLLTE||||
|||||c|Maßnahmen für die Bewahrung des logischen Kontextes der zu erfassenden<br>Dokumente|SOLLTE||||
||||||Bewahrung der Zugehörigkeit der eingescannten Seiten zu einem<br>Dokument|SOLLTE||||



Bundesamt für Sicherheit in der Informationstechnik 

16 

Anlage P – Prüfspezifikation (normativ) 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|---|
|||||d|Die korrekte Orientierung der erfassten Blätter muss erhalten bleiben<br>(Drehung, leere Rückseite)<br>Ist dies nicht möglich, muss beidseitig erfasst werden.|MUSS||||
|||||e|Bewahrung der korrekten Reihenfolge von Blättern bei mehrseitigen<br>Dokumenten|SOLLTE||||
|||||f|Zuverlässige Trennung von unabhängigen Dokumenten|SOLLTE||||
|||||g|Entfernen von Klammern, Knicken und nicht relevanten Klebezetteln|SOLLTE||||
||||||Sofern der Inhalt eines Klebezettels relevant ist, muss dieser in geeigneter<br>Weise gescannt werden.|MUSS||||
|||||h|Sofern im Rahmen des Scanprozesses ein Umkopieren notwendig ist, ist<br>darauf zu achten, dass die Kopie alle relevanten Informationen enthält.|MUSS||||
|18|25|4.2.5.2|A.DV.2|**Vorbereitung der Vollständigkeitsprüfung**||||||
|||||Bei automatisierter Erfassung müssen geeignete Maßnahmen für die<br>Sicherstellung der Vollständigkeit getroffen werden.||MUSS||||
|||||Damit eine Vollständigkeitsprüfung im Rahmen der Nachbereitung<br>durchgeführt werden kann, sollten entsprechende Vorbereitungen getroffen<br>werden (bei Bedarf).||SOLLTE||||



Bundesamt für Sicherheit in der Informationstechnik 

17 

## P.2.6 Sicherheitsmaßnahmen beim Scannen 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|---|
|19|26|4.2.6.1|A.SC.1|**Auswahl und Beschaffung geeigneter Scanner**||||||
|||||Bei der Auswahl und Beschaffung geeigneter Scanner sollten folgende Kriterien auf ihre<br>Relevanz geprüft und berücksichtigt werden:||||||
|||||a|Ausreichender Durchsatz|SOLLTE||||
|||||b|Unterstützung geeigneter Datenformate|SOLLTE||||
|||||c|Unterstützung von Patch- und/oder Barcodes zur Dokumententrennung<br>und Übergabe von Meta-Informationen|SOLLTE||||
|||||d|Ausreichende Qualität der Scanprodukte|SOLLTE||||
|||||e|Ausreichende Flexibilität der Konfiguration|SOLLTE||||
|||||f|Zuverlässiger und leistungsfähiger automatischer Seiteneinzug|SOLLTE||||
|||||g|Möglichkeit zum Scannen gebundener Dokumente, Überlängen, zum<br>Scannen von Farbe oder von Durchlichtdokumenten (bei Bedarf)|SOLLTE||||
|||||h|Geeignete Schnittstellen für die Übermittlung des Scanprodukts in<br>DMS/VBS/Archive/Fachanwendungen|SOLLTE||||
|||||i|Möglichkeit der Absicherung der Administrationsschnittstelle|SOLLTE||||
|||||j|Nutzung eines internen Datenspeichers|SOLLTE||||
|||||k|Möglichkeit zum sicheren Löschen oder verschlüsselter Speicherung von<br>Scanprodukten auf dem internen Datenspeicher|SOLLTE||||



Bundesamt für Sicherheit in der Informationstechnik 

18 

Anlage P – Prüfspezifikation (normativ) 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|---|
|||||l|Ausreichender Support|SOLLTE||||
|20|27|4.2.6.2|A.SC.2|**Zugangs- und Zugriffskontrollen für Scanner**||||||
|||||Es muss sichergestellt werden, dass Personen, die keinen Zugriff auf Originale,<br>Scanprodukte und Scansystem haben dürfen, keinen unbeaufsichtigten<br>Zugang zum Scansystem erhalten.||MUSS||||
|||||Es müssen geeignete Zugangskontrollen und Besucherregelungen vorgesehen<br>werden.||MUSS||||
|||||Um einen hohen Schutz gegen Manipulationen des Scannen bzw. der<br>Konfigurationen, der Dokumente beim Scannen, oder gegen das nachträgliche<br>Auslesen von Scanprodukten vom internen Datenträger des Scanners zu<br>erreichen, muss der Zugang zum Scanner generell auf ein Minimum<br>beschränkt werden.||MUSS||||
|||||Die Administration des Scanners bzw. die Konfiguration der<br>Kommunikationsschnittstellen bei netzwerkfähigen Scannern muss durch ein<br>geeignetes Authentisierungsverfahren geschützt werden.||MUSS||||
|||||Der Zugriff auf die Administrationsschnittstelle muss durch eine geeignete<br>Netzwerk-Konfiguration auf die notwendigen Systeme eingeschränkt werden.||MUSS||||
|21|27|4.2.6.3|A.SC.3|**Änderung voreingestellte Passwörter**||||||
|||||Voreingestellte Passwörter müssen nach der Installation des<br>Scanners/Scansystems geändert werden.||MUSS||||
|||||Basis für die Passwortvergabe sollten explizit formulierte interne<br>Sicherheitsrichtlinien unter Berücksichtigung der Empfehlungen aus dem<br>[BSI-GSK] in seiner aktuellsten Fassung sein.||SOLLTE||||



Bundesamt für Sicherheit in der Informationstechnik 

19 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|22|27|4.2.6.4|A.SC.4|**Sorgfältige Durchführung von Konfigurationsänderungen**|||||
|||||Bei der Durchführung von Konfigurationsänderungen muss sorgfältig<br>vorgegangen werden.|MUSS||||
|||||Die alte Konfiguration sollte zuvor gesichert werden.|SOLLTE||||
|||||Änderungen sollten von einem Kollegen überprüft werden, bevor diese in den<br>Echtbetrieb übernommen werden.|SOLLTE||||
|23|27|4.2.6.5|A.SC.5|**Geeignete Benutzung des Scanners**|||||
|||||Der eingesetzte Scanner muss gemäß den Vorgaben des Herstellers gepflegt<br>werden.|MUSS||||
|||||Die Dokumente müssen entsprechend den Vorgaben der Produkthandbücher<br>und gemäß der physikalischen Struktur de Dokumente dem Scanner<br>übergeben werden.|MUSS||||
|||||Für Dokumente, die nicht für den automatischen Einzug geeignet sind, müssen<br>in der Verfahrensdokumentation geeignete Verfahren beschrieben werden.|MUSS||||
|24|27|4.2.6.6|A.SC.6|**Geeignete Scan-Einstellungen**|||||
|||||Die Scan-Einstellungen müssen für die jeweiligen Dokumente geeignet<br>gewählt werden.|MUSS||||
|||||Für die Dokumententypen sollten geeignete Profile definiert, getestet und<br>freigegeben werden.|SOLLTE||||
|||||Spätestens beim Scannen sollte geprüft werden, dass geeignete Scan-<br>Einstellungen genutzt werden.|SOLLTE||||



Bundesamt für Sicherheit in der Informationstechnik 

20 

Anlage P – Prüfspezifikation (normativ) 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|25|28|4.2.6.7|A.SC.7|**Geeignete Erfassung von Metainformationen**|||||
|||||Index- und Metadaten sollten in geeigneter Weise übergeben werden.|SOLLTE||||
|||||Hierbei sollte eine zuverlässige Konfiguration der Applikation bzgl. der<br>Erkennung und Gültigkeit der ausgelesenen Werte sowie eine sorgfältige<br>manuelle Qualitätssicherung und Nachbearbeitung erfolgen.|SOLLTE||||
|26|28|4.2.6.8|A.SC.8|**Qualitätssicherung der Scanprodukte**|||||
|||||Zur Erkennung mangelhafter Scanvorgänge muss eine geeignete<br>Qualitätskontrolle erfolgen.|MUSS||||
|||||Die Ausgestaltung der Qualitätssicherung sollte sich am Scan-Durchsatz und<br>dem Schutzbedarf der verarbeiteten Dokumente orientieren.|SOLLTE||||
|||||Die Größe der Stichprobe muss abhängig vom Schutzbedarf der Dokumente<br>und der Zuverlässigkeit des Scansystems bestimmt werden.|MUSS||||
|||||Bei automatisierten Qualitätskontrollen sollte eine manuelle Prüfung der<br>automatisch identifizierten Probleme erfolgen.|SOLLTE||||
|||||Die Vernichtung der Originaldokumente darf nicht vor Abschluss der<br>Qualitätskontrolle erfolgen.|MUSS||||
|27|28|4.2.6.9|A.SC.9|**Sichere Außerbetriebnahme von Scannern**|||||
|||||Bei Außerbetriebnahme müssen alle sicherheitsrelevanten Informationen von<br>den Geräten gelöscht werden.|MUSS||||
|||||Authentisierungsinformationen und gespeicherte Informationen im Scan-<br>Cache müssen gelöscht werden.|MUSS||||



Bundesamt für Sicherheit in der Informationstechnik 

21 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|---|
|||||Spezifische Konfigurationsinformationen, die Rückschlüsse auf die<br>Netzwerkstrukturen liefern können, sollten gelöscht werden.||SOLLTE||||
|28|29|4.2.6.10|A.SC.10|**Informationsschutz und Zugriffsbeschränkung bei netzwerkfähigen Scannern**||||||
|||||Bei Scannern, die über ein Netzwerk angesprochen werden, sollten geeignete<br>Maßnahmen zur Zugriffsbeschränkung und für den Schutz der über das<br>Netzwerk übertragenen Informationen vorgesehen werden.||SOLLTE||||
|||||Werden Netzlaufwerke für die Ablage von Zwischenergebnissen oder<br>Scanprodukten genutzt, muss der Zugriff auf diese Netzlaufwerke auf das<br>notwendige Minimum eingeschränkt werden.||MUSS||||
|||||Bei Multifunktionsgeräten, die Scan2Mail oder Scan2Fax unterstützen, muss<br>der Versand an ungewünschte Empfängerkreise verhindert werden.||MUSS||||
|29|29|4.2.6.11|A.SC.11|**Protokollierung beim Scannen**||||||
|||||Für die Sicherstellung der Nachvollziehbarkeit des Scanprozesses soll eine geeignete und<br>in der Verfahrensanweisung näher geregelte Protokollierung erfolgen. Dies sollte<br>insbesondere folgende Punkte umfassen:||||||
|||||a|Änderung von kritischen Konfigurationsparametern sowie<br>Authentisierungs- und Berechtigungsfunktionen|SOLLTE||||
|||||b|Informationen, wer das Scansystem wann und in welcher Weise genutzt hat.|SOLLTE||||
|||||c|Informationen, ob eine manuelle Nachbearbeitung des Scanprodukts<br>stattgefunden hat.|SOLLTE||||
|||||d|Fehlgeschlagene Authentisierungsvorgänge und sonstige aufgetretene<br>Fehler|SOLLTE||||



Bundesamt für Sicherheit in der Informationstechnik 

22 

Anlage P – Prüfspezifikation (normativ) 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|||||Protokolldaten müssen gemäß den geltenden datenschutzrechtlichen<br>Bestimmungen verarbeitet und vor unautorisiertem Zugriff geschützt werden.|MUSS||||
|30|29|4.2.6.12|A.SC.12|**Auswahl geeigneter Bildkompressionsverfahren**|||||
|||||Es muss auf die Auswahl geeigneter Bildkompressionsverfahren geachtet<br>werden.|MUSS||||
|||||Verfahren, die zur Bildkompression - das sog. „Symbol Coding“ verwenden,<br>dürfen nicht eingesetzt werden.|DARF<br>NICHT||||



Bundesamt für Sicherheit in der Informationstechnik 

23 

## P.2.7 Sicherheitsmaßnahmen bei der Nachbearbeitung 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|31|30|4.2.7.1|A.NB.1|**Geeignete und nachvollziehbare Nachbearbeitung**|||||
|||||Die Nachbearbeitung des Scanproduktes (z. B. Veränderung des<br>Kontrastes/Helligkeit, Farbreduktion, Beschneiden, Rauschunterdrückung)<br>darf nicht erfolgen, außer sie zielt auf die Erhöhung der Lesbarkeit ab.|MUSS||||
|||||Die Nachbearbeitung muss sorgfältig durchgeführt werden, damit keine<br>potenziell relevanten Informationen zerstört werden.|MUSS||||
|||||Es muss ausgeschlossen werden (z. B. Protokollierung), dass Inhalte unbemerkt<br>verfälscht werden können.|MUSS||||
|||||Welche Form der Nachbearbeitung in welchen Fällen zulässig ist, sollte in der<br>Verfahrensanweisung geregelt werden.|SOLLTE||||
|32|30|4.2.7.2|A.NB.2|**Qualitätssicherung der nachbearbeiteten Scanprodukte**|||||
|||||Sofern eine Nachbearbeitung erfolgt, muss für die durchgeführten<br>Operationen eine Qualitätssicherung erfolgen.|MUSS||||
|||||Die ursprünglichen Scanprodukte dürfen nicht vor Abschluss der<br>Qualitätssicherung gelöscht werden.|MUSS||||
|33|30|4.2.7.3|A.NB.3|**Durchführung der Vollständigkeitsprüfung**|||||



Bundesamt für Sicherheit in der Informationstechnik 

24 

Anlage P – Prüfspezifikation (normativ) 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|---|
|||||In einem automatisierten Prozess müssen geeignete Maßnahmen zur<br>Sicherstellung der Vollständigkeit getroffen werden.<br>Im Rahmen des Audits werden die getroffenen Maßnahmen zur<br>Vollständigkeits-prüfung erfasst und vom Auditor hinsichtlich der Eignung<br>bewertet.<br>Die Vollständigkeitsprüfung muss die bildliche und inhaltliche<br>Übereinstimmung von Originaldokument und Scanprodukt auf geeignete<br>Weise prüfen und im Transfervermerk dokumentieren. Hierzu muss die<br>Sachbearbeitung die Ergebnisse der Vollständigkeitsprüfung an die Scanstelle<br>weitergeben.||MUSS||||
|||||Die Größe der Stichprobe sollte abhängig vom Schutzbedarf der gescannten<br>Dokumente, der Zuverlässigkeit des Scansystems und den Ergebnissen<br>vorhergehender Stichproben bestimmt werden.||SOLLTE||||
|34|30|4.2.7.4|A.NB.4|**Transfervermerk**||||||
|||||Für jedes Scanprodukt muss ein Transfervermerk erstellt werden.||MUSS||||
|||||Der Transfervermerk soll insbesondere folgende Aspekte dokumentieren||||||
|||||a|Ersteller des Scanprodukts|MUSS||||
||||||Die ausschließliche Angabe der Organisation darf nicht erfolgen|DARF<br>NICHT||||
|||||b|Technisches und organisatorisches Umfeld des Erfassungsvorgangs|MUSS||||
|||||c|Etwaige Auffälligkeiten während des Scanprozesses|MUSS||||



Bundesamt für Sicherheit in der Informationstechnik 

25 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|---|
|||||d|Zeitpunkt der Erfassung|MUSS||||
|||||e|Ergebnis der Qualitätssicherung|MUSS||||
|||||f|Die Tatsache, dass es sich um ein Scanprodukt handelt, das bildlich und<br>inhaltlich mit dem Papierdokument übereinstimmt.|MUSS||||
|||||Der Transfervermerk muss mit dem Scanprodukt logisch verknüpft oder in das<br>Scanprodukt integriert werden.||MUSS||||
|||||Die Integrität des Transfervermerks muss entsprechend dem Schutzbedarf der<br>verarbeiteten Dokumente geschützt werden.||MUSS||||
|||||Besteht der Transfervermerk ganz oder teilweise aus entsprechenden<br>Protokollinformationen, muss die Integrität derselben entsprechend geschützt<br>werden.||MUSS||||



## P.2.8 Sicherheitsmaßnahmen bei der Integritätssicherung 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|35|31|4.2.8.1|A.IS.1|**Nutzung geeigneter Dienste und Systeme für den Integritätsschutz**|||||
|||||Um eine unerkannte nachträgliche Manipulation der während des<br>Scanprozesses entstehenden Datenobjekte (Scanprodukt, Transfervermerk,<br>Index- und Metadaten, Protokolldaten, …) zu verhindern, müssen geeignete<br>Mechanismen zum Schutz deren Integrität eingesetzt werden.|MUSS||||
|||||Die Widerstandsfähigkeit der Mechanismen muss sich am Schutzbedarf<br>(hinsichtlich der Integrität) der verarbeiteten Datenobjekte orientieren.|MUSS||||



Bundesamt für Sicherheit in der Informationstechnik 

26 

Anlage P – Prüfspezifikation (normativ) 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|||||Bei der Verarbeitung von Dokumenten mit Schutzbedarf „normal“ bezüglich<br>der|SOLLTE||||
|||||Integrität, sollten geeignete kryptographische Mechanismen in Form von<br>fortgeschrittenen elektronischen Signaturen oder fortgeschrittenen<br>elektronischen Siegeln verwendet werden.|SOLLTE||||
|||||Andernfalls muss ein schriftlicher Nachweis erbracht werden, dass der für den<br>Integritätsschutz eingesetzte Mechanismus im Sinne der obigen Festlegung<br>ausreichend widerstandsfähig ist.|MUSS||||
|||||Zum Schutz der Datenobjekte gegen zufällige Änderungen oder aufgrund von<br>Systemfehlern sollten diese jedoch mit einem geeigneten<br>Datensicherungsverfahren gesichert werden.|SOLLTE||||
|P.3 Aufbaumodule<br>P.3.1 Generelle Maßnahmen bei erhöhtem Schutzbedarf|||||||||
|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**||
|36|32|4.3.1.1|A.AM.G.1|**Beschränkung des Zugriffs auf sensible Papierdokumente**|||||
|||||Bei der Verarbeitung von Dokumenten mit Schutzbedarf von zumindest<br>„hoch“ bezüglich der Integrität, Vertraulichkeit oder Verfügbarkeit sollten<br>während des Scanvorgangs keine unbefugten Personen Zugriff auf die<br>Papierdokumente erhalten.|SOLLTE||||
|||||Es müssen geeignete Maßnahmen für die Beschränkung des Zugriffs auf die sensiblen<br>Papierdokumente getroffen werden. Dies umfasst:|||||



## P.3 Aufbaumodule 

## P.3.1 Generelle Maßnahmen bei erhöhtem Schutzbedarf 

Bundesamt für Sicherheit in der Informationstechnik 

27 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|---|
|||||a|Zugangsbeschränkung zu den Räumlichkeiten, in denen die Dokumente<br>verarbeitet werden.|MUSS||||
|||||b|Eine Aufbewahrung, die Schutz vor unbefugtem Zugriff, Einsichtnahme<br>oder Beschädigung bietet.|MUSS||||
|||||c|<br>Die Verpflichtung der Mitarbeiter zur sorgfältigen Handhabung der<br>Dokumente (z. B. kein unbeaufsichtigtes Liegenlassen, keine Weitergabe<br>ohne Prüfung der Autorisierung)|MUSS||||
|||||Sofern nicht bereits generelle Regelungen für den Zugriff auf sensible<br>Papierdokumente existieren, müssen im Rahmen des ersetzenden Scannens<br>entsprechende Regelungen geschaffen werden.||MUSS||||
|37|33|4.3.1.2|A.AM.G.2|**Pflicht zur Protokollierung beim Scannen**||||||
|||||Die in A.SC.11 empfohlene Protokollierung muss erfolgen.||MUSS||||
|38|33|4.3.1.3|A.AM.G.3|**Pflicht zur regelmäßigen Auditierung**||||||
|||||Die in A.O.4 empfohlene Überprüfung der Wirksamkeit und Vollständigkeit,<br>der für die Informationssicherheit beim ersetzenden Scannen vorgesehenen<br>Maßnahmen, muss mindestens alle drei Jahre erfolgen.||MUSS||||



## P.3.2 Zusätzliche Maßnahmen bei hohen Integritätsanforderungen 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|39|33|4.3.2.1|A.AM.IN.H.1|**Einsatz kryptographischer Mechanismen zum Integritätsschutz**|||||
|||||Bei der Verarbeitung von Datenobjekten mit einem Schutzbedarf von<br>zumindest „hoch“ bezüglich der Integrität müssen geeignete|MUSS||||



Bundesamt für Sicherheit in der Informationstechnik 

28 

Anlage P – Prüfspezifikation (normativ) 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|---|
|||||kryptographische Mechanismen in Form von qualifizierten elektronischen<br>Signaturen oder qualifizierten elektronischen Siegeln zum Einsatz kommen.||||||
|||||Die Vorgaben der [LeitLeSig] müssen eingehalten werden, sofern eine<br>anschließende langfristige Beweiswerterhaltung vorgesehen ist.||MUSS||||
|||||Um die Verkehrsfähigkeit der Datenobjekte und Sicherungsdaten<br>sicherzustellen, müssen standardisierte Formate verwendet werden.||MUSS||||
|40|34|4.3.2.2|A.AM.IN.H.2|**Geeignetes Schlüsselmanagement**||||||
|||||Sofern schlüsselbasierte kryptographische Mechanismen eingesetzt werden,<br>müssen geeignete Verfahren zum Schlüsselmanagement vorgesehen<br>werden.||MUSS||||
|||||Dabei muss insbesondere über den vorgesehenen Aufbewahrungszeitraum der<br>Scanprodukte hin sichergestellt werden, dass||||||
|||||a|die Vertraulichkeit, Integrität und Authentizität der Schlüssel gewahrt<br>bleibt.|MUSS||||
|||||b|private und geheime Schlüssel nicht unbefugt verwendet werden<br>können.|MUSS||||
|||||c|die zur Prüfung der Integritätssicherung erforderlichen Schlüssel und<br>Zertifikate verfügbar bleiben.|MUSS||||
|||||Hierbei sollten die einschlägigen Empfehlungen aus dem IT-Grundschutz-<br>Kompendium des BSI (CON.1, Kryptokonzept), [NIST-800-57-1/2], [NIST-<br>800-133] und [BSI TR-03145] bei der Verwaltung des Schlüsselmaterials<br>berücksichtigt oder vertrauenswürdige Dienstleister für das<br>Schlüsselmanagement genutzt werden.||SOLLTE||||



Bundesamt für Sicherheit in der Informationstechnik 

29 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|41|34|4.3.2.3|A.AM.IN.H.3|**Auswahl eines geeigneten kryptographischen Verfahrens**|||||
|||||Sofern kryptographische Verfahren eingesetzt werden, müssen geeignete<br>kryptographische Verfahren verwendet werden. Hierbei müssen Verfahren<br>gemäß {BSI TR-02102-1], [BSI TR-03116-4] oder [ETSI TS 119 312] eingesetzt<br>werden.|MUSS||||
|42|34|4.3.2.4|A.AM.IN.H.4|**Auswahl eines geeigneten kryptographischen Produktes**|||||
|||||Zur Integritätssicherung müssen geeignete (qualifizierte) Vertrauensdienste<br>und Produkte hinsichtlich Funktionalität und Vertrauenswürdigkeit<br>eingesetzt werden. Bei der Funktionalität ist vor allem auf eine ausreichende<br>Stärke und Widerstandsfähigkeit der eingesetzten Sicherheitsmechanismen<br>im Sinne der eIDAS-VO sowie der [LeitLeSig] zu achten.|MUSS||||
|||||Hinsichtlich der Vertrauenswürdigkeit sind der Einsatz veröffentlichter und<br>gemeinschaftlich analysierter Algorithmen (siehe A.AM.IN.H.3, oben) und<br>Quellen sowie durchgeführte Prüfungen nach einem anerkannten<br>Sicherheitsstandard wie FIPS-140, Common Criteria oder ITSEC positiv zu<br>bewerten und sollten daher primär herangezogen werden|SOLLTE||||
|||||Da sich die Sicherheitseignung der kryptographischen Algorithmen ändern<br>kann, sollte auf eine leichte Austauschbarkeit der entsprechenden<br>Komponenten geachtet werden.|SOLLTE||||
|||||Um eine sichere Nutzung der kryptographischen Produkte zu gewährleisten,<br>müssen die notwendigen Einsatzbedingungen und sonstigen Empfehlungen<br>des Herstellers berücksichtigt werden.|MUSS||||
|43|35|4.3.2.5|A.AM.IN.H.5|**Langfristige Datensicherung bei Einsatz kryptographischer Verfahren**|||||
|||||Für die eingesetzten kryptographischen Verfahren, muss die Eignung der<br>verwendeten Algorithmen und Parameter regelmäßig evaluiert werden.|MUSS||||



Bundesamt für Sicherheit in der Informationstechnik 

30 

Anlage P – Prüfspezifikation (normativ) 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|||||Sofern Bedarf für eine langfristige Beweiswerterhaltung besteht, sind nach §<br>15 VDG, qualifiziert elektronisch signierte, gesiegelte oder zeitgestempelte<br>Daten durch geeignete Maßnahmen neu zu schützen, bevor der<br>Sicherheitswert der vorhandenen Signaturen, Siegel oder Zeitstempel durch<br>Zeitablauf geringer wird.|MUSS||||
|||||Sofern Bedarf für eine langfristige Beweiswerterhaltung besteht, muss die<br>neue Sicherung nach dem Stand der Technik erfolgen. Der Stand der<br>Technik wird durch den Einsatz eines (zertifizierten) [BSI TR-03125]-<br>Produktes oder durch den Einsatz eines (qualifizierten) Bewahrungsdienstes<br>gemäß [ETSI TS 119 511] sichergestellt.|MUSS||||
|44|35|4.3.2.6|A.AM.IN.H.6|**Verhinderung ungesicherter Netzzugänge**|||||
|||||Sofern die für das Scannen eingesetzten IT-Systeme über ein Netzwerk<br>verbunden sind, muss ein ungesicherter Zugang zu diesem<br>Netzwerksegment verhindert werden.|MUSS||||
|||||Ein Zugriff aus dem Internet auf dieses Netzwerksegment darf nur<br>entkoppelt (Proxy/Gateway) und nur bei Initiierung von innen möglich sein.|MUSS||||
|45|35|4.3.2.7|A.AM.IN.H.7|**Erweiterte Qualitätssicherung der Scanprodukte**|||||
|||||Bei einem Schutzbedarf der Datenobjekte von „hoch“ bezüglich der<br>Integrität, sollte die Qualitätskontrolle der Scanprodukte (in regelmäßigen<br>zeitlichen Abständen) durch eine vollständige Sichtkontrolle erfolgen.|SOLLTE||||
|||||Bei einem sehr hohen Durchsatz kann die Sichtkontrolle sukzessive auf<br>regelmäßig durchgeführte Stichproben reduziert werden, wobei deren<br>Größe den Stichprobenumfang der Sichtkontrolle des Schutzbedarfs<br>„normal“ deutlich übertreffen muss.|MUSS||||



Bundesamt für Sicherheit in der Informationstechnik 

31 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|||||Falls keine vollständige Sichtkontrolle realisiert wird, sollten automatische<br>Mechanismen zur Qualitätskontrolle eingesetzt werden, wie z. B. eine<br>automatische Erkennung von Leerseiten, von unzureichender Bildqualität<br>oder die Prüfung der Seitenzahl.|SOLLTE||||
|||||Beim Einsatz automatisierter Mechanismen muss eine manuelle Prüfung<br>der identifizierten Probleme und Auffälligkeiten erfolgen.|MUSS||||



Bundesamt für Sicherheit in der Informationstechnik 

32 

Anlage P – Prüfspezifikation (normativ) 

## P.3.3 Zusätzliche Maßnahmen bei sehr hohen Integritätsanforderungen 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|46|36|4.3.3.1|A.AM.IN.SH.1|**4-Augen-Prinzip**|||||
|||||Bei Schutzbedarf „sehr hoch“ hinsichtlich der Integrität muss im Rahmen<br>der Aufgabenteilung (siehe A.O.1) sichergestellt werden, dass die Erstellung<br>und Qualitätssicherung des Scanproduktes von unterschiedlichen Personen<br>durchgeführt wird.|MUSS||||
|47|36|4.3.3.2|A.AM.IN.SH.2|**Einsatz qualifizierter elektronischer Signaturen oder Siegel und Zeitstempel**|||||
|||||Sofern Datenobjekte mit einem Schutzbedarf von „sehr hoch“ bezüglich der<br>Integrität verarbeitet werden, müssen für die Integritätssicherung des<br>Scanproduktes bzw. des Transfervermerkes qualifizierte elektronische<br>Signaturen oder qualifizierte elektronische Siegel und qualifizierte<br>Zeitstempel eingesetzt werden (vgl. A.AM.IN.H.1).|MUSS||||
|48|36|4.3.3.3|A.AM.IN.SH.3|**Eigenständiges Netzsegment**|||||
|||||Bei einem Schutzbedarf der Datenobjekte bzgl. Vertraulichkeit oder<br>Integrität von „sehr hoch“, müssen die für das Scannen eingesetzten IT-<br>Systeme in einem eigenständigen Netzsegment eingebunden sein.|MUSS||||
|||||Der Zugriff auf dieses Netzsegment aus anderen Netzsegmenten darf nicht<br>erfolgen, es sei denn die Kommunikation wird über einen Proxy oder ein<br>Gateway vermittelt und der Verbindungsaufbau erfolgt von innen.|MUSS||||
|49|36|4.3.3.4|A.AM.IN.SH.4|**Kennzeichnung der Dokumente bzgl. Sensitivität**|||||
|||||Dokumente, die einen Schutzbedarf von „sehr hoch“ bzgl. der Integrität<br>besitzen, sollten als solche gekennzeichnet werden, ohne das Original zu<br>manipulieren.|SOLLTE||||



Bundesamt für Sicherheit in der Informationstechnik 

33 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|||||Die Kennzeichnung sollte deutlich sichtbar angebracht werden.|SOLLTE||||
|50|36|4.3.3.5|A.AM.IN.SH.5|**Vollständige Sichtkontrolle zur Qualitätssicherung der Scanprodukte**|||||
|||||Bei einem Schutzbedarf der Datenobjekte von „sehr hoch“ bezüglich der<br>Integrität, muss die Qualitätskontrolle der Scanprodukte durch eine<br>vollständige Sichtkontrolle erfolgen.|MUSS||||



Bundesamt für Sicherheit in der Informationstechnik 

34 

Anlage P – Prüfspezifikation (normativ) 

## P.3.4 Zusätzliche Maßnahmen bei hohen Vertraulichkeitsanforderungen 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|51|37|4.3.4.1|A.AM.VT.H.1|**Sensibilisierung und Verpflichtung der Mitarbeiter**|||||
|||||Bei der Verarbeitung von Dokumenten mit einem Schutzbedarf bezüglich<br>der Vertraulichkeit von zumindest „hoch“ müssen die Mitarbeiterinnen und<br>Mitarbeiter bzgl. der Sicherheitsmaßnahmen und der sicherheitsbewussten<br>Handhabung von Dokumenten, Daten und IT-Systemen und der zu<br>ergreifenden Vorsichtsmaßnahmen sensibilisiert und geschult werden.|MUSS||||
|||||Mitarbeiter müssen durch eine explizite Verfahrensanweisung auf die<br>Einhaltung der einschlägigen Gesetze, Vorschriften und Regelungen<br>verpflichtet werden.|MUSS||||
|52|37|4.3.4.2|A.AM.VT.H.2|**Verhinderung ungesicherter Netzzugänge**|||||
|||||Siehe A.AM.IN.H.6, Abschnitt 4.3.2.|MUSS||||
|53|37|4.3.4.3|A.AM.VT.H.3|**Löschen von Zwischenergebnissen**|||||
|||||Bei der Verarbeitung von Dokumenten mit einem Schutzbedarf hinsichtlich<br>der Vertraulichkeit von zumindest „hoch“, müssen die in der Verarbeitung<br>entstehenden Zwischenergebnisse (z. B. rohe Scanprodukte, Daten im Scan-<br>Cache) zuverlässig gelöscht werden.|MUSS||||



Bundesamt für Sicherheit in der Informationstechnik 

35 

## P.3.5 Zusätzliche Maßnahmen bei sehr hohen Vertraulichkeitsanforderungen 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|54|37|4.3.5.1|A.AM.VT.SH.1|**Kennzeichnung der Dokumente bzgl. Sensitivität**|||||
|||||Dokumente, die einen Schutzbedarf von „sehr hoch“ bzgl. der<br>Vertraulichkeit besitzen, sollten als solche gekennzeichnet werden, ohne<br>das Original zu manipulieren.|SOLLTE||||
|||||Die Kennzeichnung sollte deutlich sichtbar angebracht werden.|SOLLTE||||
|55|37|4.3.5.2|A.AM.VT.SH.2|**Ordnungsgemäße Entsorgung von schützenswerten Betriebsmitteln**|||||
|||||Sofern der Scanner einen internen Speicher besitzt und Dokumente<br>gescannt werden, die einen Schutzbedarf bzgl. der Vertraulichkeit von<br>„sehr hoch“ besitzen, muss der Datenträger vor der Entsorgung des<br>Scanners zuverlässig gelöscht werden.|MUSS||||
|||||Sofern möglich, sollte der Datenträger ausgebaut und mit einem<br>geeigneten Verfahren zuverlässig gelöscht oder zerstört werden.|SOLLTE||||
|||||Kryptographische Schlüssel, die im zu entsorgenden Scanner vorgehalten<br>werden, müssen zuverlässig gelöscht oder deaktiviert werden.|MUSS||||
|||||In etwaigen Verträgen mit Dienstleistern ist darauf zu achten, dass ein<br>zuverlässiges und für die Organisation nachvollziehbares Lösch- und<br>Entsorgungsverfahren etabliert wird. Hierbei müssen die Anforderungen<br>nach CON.6 aus dem BSI-Grundschutzkompendium oder [DIN66399]<br>angewendet werden.|MUSS||||
|56|38|4.3.5.3|A.AM.VT.SH.3|**Besondere Zuverlässigkeit und Vertrauenswürdigkeit der Mitarbeiter**|||||
|||||Sofern Dokumente gescannt werden, deren Schutzbedarf hinsichtlich der<br>Vertraulichkeit „sehr hoch“ ist, sollte sichergestellt werden, dass die|SOLLTE||||



Bundesamt für Sicherheit in der Informationstechnik 

36 

Anlage P – Prüfspezifikation (normativ) 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|---|
|||||Mitarbeiter, die für den Scanprozess verantwortlich sind und den Prozess<br>durchführen besonders zuverlässig und vertrauenswürdig sind.||||||
|57|38|4.3.5.4|A.AM.VT.SH.4|**Verschlüsselte Datenübertragung innerhalb des Scansystems**||||||
|||||Bei der Verarbeitung von Datenobjekten mit einem Schutzbedarf von<br>„sehr hoch“ bzgl. der Vertraulichkeit sollte die Datenübertragung zwischen<br>Scanner, Scan-Workstation, Scan-Cache und anderen damit<br>zusammenhängenden Systemen durch geeignete<br>Verschlüsselungsverfahren gemäß [BSI TR-02102-1] oder [BSI TR-03116-4]<br>erfolgen.||SOLLTE||||
|||||Andernfalls muss ein geeigneter Nachweis erbracht werden, dass diese<br>Kommunikationsverbindungen durch alternative Maßnahmen<br>ausreichend geschützt sind.||MUSS||||
|58|39|4.3.5.5|A.AM.VT.SH.5|**Räumlichkeiten des Scan-Systems**||||||
|||||a|Die räumliche Absicherung des Scan-Systems muss dem Schutzbedarf<br>des Papieroriginals entsprechen.|MUSS||||
|||||b|Die Räumlichkeiten sollten nur von den vertrauenswürdigen<br>Mitarbeitenden zu betreten sein, in dem dies in einem geeigneten<br>Zutrittskonzept beschrieben ist.|SOLLTE||||
|||||c|Etwaige Fenster müssen mit einem lichtdurchlässigen Sichtschutz<br>versehen sein.|MUSS||||



Bundesamt für Sicherheit in der Informationstechnik 

37 

## P.3.6 Zusätzliche Maßnahmen bei hohen Verfügbarkeitsanforderungen 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|59|39|4.3.6.1|A.AM.VF.H.1|**Fehlertolerante Protokolle und redundante Datenhaltung**|||||
|||||Bei Schutzbedarf „hoch“ bzgl. der Verfügbarkeit sollte ein fehlertolerantes<br>Übertragungsprotokoll sowie eine redundante Auslegung des Scansystems<br>verwendet werden.|SOLLTE||||



## P.3.7 Zusätzliche Maßnahmen bei sehr hohen Verfügbarkeitsanforderungen 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|60|39|4.3.7.1|A.AM.VF.SH.1|**Test der Geräte und Einstellungen mit ähnlichen Dokumenten**|||||
|||||Bei Datenobjekten mit einem Schutzbedarf „sehr hoch“ bzgl. der<br>Verfügbarkeit, muss die Eignung der verwendeten Geräte, Verfahren und<br>Einstellungen vorher mit physikalisch ähnlichen Dokumenten, die selbst<br>keinen hohen Schutzbedarf bzgl. der Verfügbarkeit haben, getestet und das<br>Prüfergebnis dokumentiert werden.|MUSS||||



Bundesamt für Sicherheit in der Informationstechnik 

38 

Anlage P – Prüfspezifikation (normativ) 

## P.4 Besonderheiten beim mobilen ersetzenden Scannen 

## P.4.1 Einführung in das mobile Scannen 

Unter mobilem ersetzendem Scannen wird die ersetzende Digitalisierung von Papieroriginalen unter Nutzung mobiler Endgeräte (beispielsweise Mobiltelefon oder Tablet) unter Nutzung einer ScanApp und Übertragung von Scanprodukt, Metadaten, Transfervermerk etc. an eine zentrale Infrastruktur verstanden. Stationäre Scanstellen an verschiedenen Orten oder solche, die mittels Fahrzeugen an verschiedene Orte verbracht werden können, werden vom mobilen Scannen nicht umfasst. 

Im Folgenden werden nur die besonderen Anforderungen an das mobile ersetzende Scannen als Abweichung zum stationären ersetzenden Scannen definiert. Sofern keine Abweichung beschrieben ist, gelten die Anforderungen der TR-RESISCAN für das stationäre ersetzende Scannen (P 2 und P 3). Die spezifischen Anforderungen an das mobile Scannen werden in der Syntax [M.MaßnahmeXY.Nr. der Maßnahme] angegeben: 

## P.4.2 Basismodul mobiles Scannen 

## P.4.2.1 Organisatorische Maßnahmen 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|61|40|5.2.1.1|M.A.O.1|**Festlegung von Verantwortlichkeiten, Abläufen und Aufgaben im Scanprozess**|||||
|||||Abweichend von den organisatorischen Maßnahmen nach A.O.1 müssen<br>beim mobilen Scannen die folgenden Aspekte besonders umgesetzt<br>werden:<br>Zu a)<br>Klare Aufteilung der Verantwortlichkeiten zwischen scannender<br>Mitarbeiterin/scannendem Mitarbeiter und nachbearbeitender<br>Mitarbeiterin/nachbearbeitendem Mitarbeiter|MUSS||||
|||||Zu b)<br>Festlegung der Dokumente, die vom mobilen Scannen eingeschlossen sind<br>und die mobil nur kopierend gescannt werden dürfen.|MUSS||||



Bundesamt für Sicherheit in der Informationstechnik 

39 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|||||Zu c) und d)<br>•<br>Protokolldaten der scannenden Mitarbeiterinnen und Mitarbeiter zum<br>Prozess und Nachweise zur bildlichen und inhaltlichen<br>Übereinstimmung<br>•<br>Protokolldaten des Mobilgeräts beim Scannen der Dokumente<br>•<br>Nutzung von Hashwerten und kryptografischen Signaturen und<br>Siegeln|MUSS||||
|||||Zu e)<br>• Qualitätssicherung durch scannende Mitarbeiterin / scannendem<br>Mitarbeiter vor dem Upload.<br>• Ergänzende Qualitätssicherung durch organisationsinterne<br>Mitarbeiterin / organisationsinternen Mitarbeiter nach Upload<br>• Festlegung der Maßnahmen zur Qualitätssicherung, ausgerichtet an den<br>Möglichkeiten des Mobilgeräts<br>• Festlegung des Prozesses bei Qualitätsmängeln|MUSS||||
||||||||||
|||||Es sollten Vorgaben zu den nachfolgenden Aspekten in einer<br>organisationsweiten Richtlinie festgehalten, in die bestehenden Prozesse<br>integriert und durch die Mitarbeitenden, die am mobilen Scannen beteiligt<br>sind auf geeignete Weise bestätigt werden:<br>• Schritte zur Dokumentenvorbereitung und Digitalisierung.<br>• Welche Dokumente gescannt und welche Daten hierbei erzeugt werden,<br>respektive wie diese zu scannen sind.<br>• Notwendige Qualitätskontrollen, also z.B. die Prüfung der auf den<br>Scancache gescannte Dokumente durch die scannenden Mitarbeitenden<br>auf logische, inhaltliche und bildliche Übereinstimmung.|SOLLTE||||



Bundesamt für Sicherheit in der Informationstechnik 

40 

Anlage P – Prüfspezifikation (normativ) 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|||||• Verantwortlichkeit für die Originaldokumente und Scanprodukte bei<br>den scannenden Mitarbeitenden.|||||
|||||Die Qualitätskontrolle des Scanprodukts muss in zwei Schritten erfolgen<br>(Erstkontrolle und Freigabe zum Upload durch scannende Mitarbeitende<br>und Zweikontrolle durch Bearbeitende in der Zielinfrastruktur|MUSS||||
|||||Es müssen geeignete Kommunikationsprozesse unter Beachtung der BSI<br>TR-02102-1 zwischen scannenden Mitarbeitenden und Bearbeitenden in<br>der Zielinfrastruktur etabliert werden.|MUSS||||
|62|42|5.2.1.2|M.A.O.2<br>M.A.O.3|**Wartungs- und Reparaturarbeiten sowie Abnahme und Freigabeverfahren**|||||
|||||Wartung und Reparatur sowie Abnahme und Freigabe der zum mobilen<br>ersetzenden Scannen eingesetzten Geräte darf nur mit in der Organisation<br>geprüften Endgeräten möglich sein.|MUSS||||
|||||Für mobile Endgeräte müssen die Bausteine INF.9, SYS.2.1 und SYS.3.2 des<br>[BSI-GSK] umgesetzt werden.|MUSS||||
|63|42|5.2.1.3|M.A.O.4|**Aufrechterhaltung der Informationssicherheit**|||||
|||||Das mobile ersetzende Scannen muss in der Organisation integriert und<br>entsprechend dokumentiert sein. Die Überprüfung muss in die in der<br>Organisation etablierten Prüfprozesse für die mobilen Endgeräte integriert<br>werden.|MUSS||||



Bundesamt für Sicherheit in der Informationstechnik 

41 

## P.4.2.2 Personelle Maßnahmen 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|64|42|5.2.2.1<br>5.2.2.2|M.A.P.1<br>M.A.P.2|**Einweisung zum ordnungsgemäßen Scannen sowie Schulungen und Sensibilisierung zu Sicherheitsmaßnahmen**|||||
|||||Sowohl die Sensibilisierungen zu Sicherheitsmaßnahmen und<br>Einweisungen zum ordnungsgemäßen Scannen als auch Schulungen und<br>können aufgrund der personeller Komplexität durch elektronische<br>Verfahren der Organisation (z.B. Onlinetutorials) erfolgen. Die Teilnahme<br>muss durch die Mitarbeitenden elektronisch bestätigt und von der<br>Organisation überprüfbar nachgehalten werden.|MUSS||||
|P.4.2.|3 Technische Maßnahmen||||||||
|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**||
|65|43|5.2.3.1|M.A.T.1|**Generelle Sicherheitsmaßnahmen**|||||
|||||Entsprechend A.T.1 ist das jeweilige Scansystem zu betrachten. Neben den<br>grundsätzlichen, scanrelevanten Bausteinen des BSI-Grundschutz, müssen<br>beim mobilen Scannen folgende Teile des BSI IT-<br>Grundschutzkompendium mindestens umgesetzt werden oder<br>vergleichbare Maßnahmen nach [ISO 27001] getroffen werden:<br>•<br>APP.1.2 (Webbrowser)<br>•<br>APP.1.4 (Mobile Anwendungen (Apps))<br>•<br>SYS.2.1 (Allgemeiner Client)<br>•<br>SYS.3.3 (Mobiltelefon)<br>•<br>SYS.3.2.1 (Allgemeine Smartphones und Tablets)<br>•<br>SYS.3.2.2 (Mobile Device Management (MDM))<br>•<br>SYS.3.2.3 (iOS for Enterprise)|MUSS||||



## P.4.2.3 Technische Maßnahmen 

Bundesamt für Sicherheit in der Informationstechnik 

42 

Anlage P – Prüfspezifikation (normativ) 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|||||•<br>SYS.4.4 (Allgemeines IoT-Gerät)<br>•<br>INF.9 (Mobiler Arbeitsplatz)<br>•<br>NET.1.1 (Netzarchitektur & -design)<br>•<br>NET.3.3 (VPN)|||||
|66|43|5.2.3.2|M.A.T.2|**Festlegung der zulässigen Kommunikationsverbindungen**|||||
|||||Es gelten die Kommunikationsverbindungen nach dem generischen<br>Scansystem mit Ausnahme von K1, siehe BSITR-03138-A. Hinzu kommt die<br>Verbindung mobiles Endgerät zum Scancache. Es müssen beim mobilen<br>Scannen folgende Teile des BSI IT-Grundschutzkompendiums mindestens<br>berücksichtigt werden oder vergleichbare Maßnahmen nach ISO 27001<br>getroffen werden:<br>•<br>NET.1.1 (Netzarchitektur & -design)<br>•<br>NET.1.2 (Netzmanagement)<br>•<br>NET.3.1 (Router & Switches)<br>•<br>NET.3.2 (Firewall)<br>•<br>INF.9 (Mobiler Arbeitsplatz)<br>•<br>SYS.2.1 (Allgemeiner Client)<br>•<br>SYS.3.2 (Allgemeine Smartphone und Tablets)|MUSS||||
|67|43|5.2.3.3|M.A.T.3|**Schutz vor Schadprogrammen**|||||
|||||•<br>Es müssen beim mobilen Scannen folgende Teile des BSI IT-<br>Grundschutzkompendiums mindestens berücksichtigt werden oder<br>vergleichbare Maßnahmen nach ISO 27001 getroffen werden:<br>•<br>OPS.1.1.4 (Schutz vor Schadprogrammen)|MUSS||||



Bundesamt für Sicherheit in der Informationstechnik 

43 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|||||•<br>CON (Datensicherungskonzept)<br>•<br>INF.9 (Mobiler Arbeitsplatz)<br>•<br>SYS.2.1 (Allgemeiner Client)<br>•<br>SYS.3.2 (Allgemeine Smartphones und Tablets)|||||
|68|43|5.2.3.4|M.A.T.4|**Zuverlässige Speicherung**|||||
|||||Die dauerhafte Speicherung von Scanprodukten auf dem mobilen Endgerät<br>muss technisch ausgeschlossen sein. Eine Speicherung auf dem mobilen<br>Endgerät darf nur temporär erfolgen. Nach Übermittlung an die<br>Zielinfrastruktur muss das Scanprodukt im mobilen Endgerät automatisch<br>gelöscht werden (z.B. Funktion der ScanApp). Eine Speicherung darf nur in<br>der Zielinfrastruktur der Organisation erfolgen.|MUSS||||
|P.4.2.|4 Sicherheitsmaßnahmen zur Dokumentenvorbereitung||||||||
|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**||
|69|44|5.2.4.1|M.A.DV.1|**Sorgfältige Vorbereitung der Papierdokumente**|||||
|||||Hinsichtlich der Bewahrung des logischen Kontexts der zu erfassenden<br>Dokumente sollte beim mobilen Scannen bei den scannenden<br>Mitarbeitenden aus Gründen der Ergonomie nur eine begrenzte<br>Metadatenerfassung erfolgen.|SOLLTE||||
|||||Die Metadaten müssen so vergeben werden können, dass der logische<br>Kontext erhalten bleibt.|MUSS||||
|70|44|5.2.4.2|M.A.DV.2|**Vorbereitung der Vollständigkeitsprüfung**|||||



## P.4.2.4 Sicherheitsmaßnahmen zur Dokumentenvorbereitung 

Bundesamt für Sicherheit in der Informationstechnik 

44 

Anlage P – Prüfspezifikation (normativ) 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|||||Die Vollständigkeitsprüfung in A.NB.3 sollte auf Stichproben reduziert<br>werden.|SOLLTE||||
|P.4.2.|5 Sicherheitsmaßnahmen beim Scannen||||||||
|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**||
|71|44|5.2.5.1|M.A.SC.1|**Auswahl und Beschaffung geeigneter Scanner**|||||
|||||Als mobiles Endgerät dürfen nur in der Organisation zugelassene Geräte<br>zum Einsatz kommen. Dies muss auf geeignete Weise sichergestellt werden.|MUSS||||
|||||Für mobile Endgeräte müssen die Bausteine INF.9, SYS.2.1 und SYS.3.2 des<br>[BSI IT-GSK] erfüllt werden oder vergleichbare Maßnahmen nach ISO<br>27001 getroffen werden.|MUSS||||
|||||Dabei müssen zudem folgende Kriterien geprüft werden:<br>•<br>Bereitstellung und ausschließliche Nutzung einer in der Organisation<br>zugelassenen ScanApp auf den mobilen Endgeräten<br>•<br>Bereitstellung und Wartung der App auf einem sicheren Weg (z. B.<br>organisationseigener App-Store)<br>•<br>Softwareseitige Verhinderung einer Zwischenspeicherung des<br>Scanprodukts bei Nutzung der ScanApp<br>•<br>Verhinderung eines Zugriffs auf den Scancache ohne Nutzung der<br>zugelassenen ScanApp<br>•<br>Unterstützung geeigneter Datenformate<br>•<br>Unterstützung einer Erfassung von Minimalmetadaten am Mobilgerät<br>•<br>Ausreichende Qualität der Scanprodukte (bzgl. Auflösung,<br>Bildkompressionsverfahren, Helligkeit, Kontrast etc.)|MUSS||||



## P.4.2.5 Sicherheitsmaßnahmen beim Scannen 

Bundesamt für Sicherheit in der Informationstechnik 

45 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|||||•<br>Ausreichende Flexibilität der Konfiguration<br>•<br>Geeignete Schnittstellen zur Übertragung der Scanprodukte an den<br>Scancache (Scannen zum Scancache) sowie zum Zugriff auf eine<br>Integritätssicherungssoftware oder externen Vertrauensdienst<br>•<br>Möglichkeit zur sicheren Bestätigung/Freigabe eines Scanvorgangs<br>unter Anzeige des Scanprodukts<br>•<br>Möglichkeit zum sicheren Löschen oder zur verschlüsselten<br>Speicherung auf dem Scancache<br>•<br>Ausreichender Support|||||
|72|44|5.2.5.2|M.A.SC.2|**Zugangs- und Zugriffskontrollen für Scanner**|||||
|||||Es muss eine sichere Authentisierung der scannenden Mitarbeitenden am<br>zugelassenen mobilen Endgerät sowie der zentralen Infrastruktur<br>gewährleistet werden, um Zugriffe durch unbefugte Personen auf das<br>mobile Endgerät zu vermeiden.|MUSS||||
||||||||||
||||||||||
|||||Die Konfiguration und Administration der ScanApp muss durch<br>berechtigtes Administrationspersonal erfolgen.|MUSS||||
||||||||||
||||||||||
|73|45|5.2.5.3|M.A.SC.6|**Geeignete Scan-Einstellungen**|||||
|||||Die Scan-Einstellung muss durch die ScanApp der Organisation<br>vorgegeben und darf von der scannenden Mitarbeiterin / vom scannenden<br>Mitarbeiter nicht verändert werden.|MUSS/<br>DARF<br>NICHT||||
|74|45|5.2.5.4|M.A.SC.7|**Geeignete Erfassung von Metadaten**|||||
|||||Beim mobilen Scannen muss sichergestellt werden, dass die Erfassung<br>minimaler Metadaten am mobilen Endgerät möglich ist.|MUSS||||



Bundesamt für Sicherheit in der Informationstechnik 

46 

Anlage P – Prüfspezifikation (normativ) 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|||||Die Indexierung und umfassendere Erfassung beschreibender Information<br>sollte durch die Bearbeiterin / den Bearbeiter in der Zielinfrastruktur der<br>Organisation erfolgen.|SOLLTE||||
|75|45|5.2.5.5|M.A.SC.8|**Qualitätssicherung der Scanprodukte**|||||
|||||Die Qualitätskontrolle muss in den folgenden beiden Schritten erfolgen:<br>•<br>Qualitätssicherung durch die scannende Mitarbeiterin / dem<br>scannenden Mitarbeiter am mobilen Endgerät.<br>•<br>Qualitätssicherung durch die Bearbeiterin / den Bearbeiter in der<br>Zielinfrastruktur der Organisation gemäß A.SC.8.|MUSS||||
|76|45|5.2.5.6|M.A.SC.9|**Sichere Außerbetriebnahme von Scannern**|||||
|||||Es müssen die Bausteine INF.9 und SYS.3.2 oder vergleichbare Maßnahmen<br>nach [ISO 27001] umgesetzt werden.|MUSS||||
|77|45|5.2.5.7|M.A.SC.10|**Informationsschutz und Zugriffsbeschränkung bei netzwerkfähigen Scannern**|||||
|||||Es müssen die Bausteine INF.9 und SYS.3.2 oder vergleichbare Maßnahmen<br>nach [ISO 27001] umgesetzt werden.|MUSS||||
|78|45|5.2.5.8|M.A.SC.11|**Protokollierung beim Scannen**|||||
|||||Zusätzlich müssen Maßnahmen nach A.SC.11 auch für die ScanApp<br>umgesetzt werden.|MUSS||||



Bundesamt für Sicherheit in der Informationstechnik 

47 

## P.4.2.6 Sicherheitsmaßnahmen bei der Nachbearbeitung und Integritätssicherung 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|79|45|5.2.6|M.A.NB/IS.1|**Sicherheitsmaßnahmen bei der Nachbearbeitung und Integritätssicherung**|||||
|||||Die Nachbearbeitung, Qualitätssicherung und Vollständigkeitsprüfung<br>müssen in der Zielinfrastruktur der Organisation erfolgen.|MUSS||||
|||||Der Transfervermerk muss in der Zielinfrastruktur erzeugt werden.|MUSS||||
|||||Die Integritätssicherung muss in der Zielinfrastruktur erfolgen.|MUSS||||



## P.4.3 Aufbaumodule 

## P.4.3.1 Generelle Maßnahmen bei Schutzbedarf „hoch“ 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|80|46|5.3.1.1|M.A.AM.G.1|**Beschränkung des Zugriffs auf sensible Papierdokumente**|||||
|||||Das mobile Scannen sensibler Papierdokumente muss durch eine erhöhte<br>Sensibilisierung der Mitarbeitenden zum Umgang und Digitalisierung<br>dieser Dokumente begleitet werden, welche in einer spezifischen internen<br>Richtlinie festgehalten wird und von den Mitarbeitenden nachprüfbar<br>bestätigt wird.|MUSS||||
|81|46|5.3.1.2|M.A.AM.G.2|**Pflicht zur Protokollierung beim Scannen**|||||
|||||Alle technischen Schritte im Scanprozess (ScanApp und Komponenten in<br>der Zielinfrastruktur) müssen gemäß A.AM.G.2 protokolliert werden.|MUSS||||
|82|46|5.3.1.3|M.A.AM.G.3|**Pflicht zur regelmäßigen Auditierung**|||||



Bundesamt für Sicherheit in der Informationstechnik 

48 

Anlage P – Prüfspezifikation (normativ) 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|---|
|||||Die mobilen Endgeräte und deren Nutzung müssen in die periodische<br>Audits ebenso eingebunden werden, wie die Zielinfrastruktur.||MUSS||||
|P.4.3.|2 Zusätzliche Maßnahmen|||bei hohen Integritätsanforderungen||||||
|**Nr**|**Seite**|**Kapitel**|**ID**||**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**||
|83|46|5.3.2.1|M.A.AM.IN.H.1||**Einsatz kryptografischer Mechanismen zum Integritätsschutz**|||||
||||||Der Integritätsschutz muss in der Zielinfrastruktur gemäß den Vorgaben<br>von A.AM.IN.H.1 erfolgen.|MUSS||||
|84|46|5.3.2.2|M.A.AM.IN.H.2||**Geeignetes Schlüsselmanagement**|||||
||||||Das Schlüsselmanagement muss in der Zielinfrastruktur gemäß den<br>Vorgaben von A.AM.IN.H.2 erfolgen.|MUSS||||
|85|46|5.3.2.3|M.A.AM.IN.H.5||**Langfristige Datensicherung bei Einsatz kryptographischer Vorgaben**|||||
||||||Die langfristige Datensicherung muss in der Zielinfrastruktur gemäß den<br>Vorgaben von A.AM.IN.H.5 erfolgen.|MUSS||||
|86|46|5.3.2.4|M.A.AM.IN.H.6||**Verhinderung ungesicherter Netzzugänge**|||||
||||||Es muss ein ungesicherter Zugang zum Netzwerksegment der<br>Zielinfrastruktur unter Beachtung der [BSI TR-02102-1] verhindert<br>werden.|MUSS||||
||||||Ein Zugriff aus dem Internet auf dieses Netzsegment darf nicht erfolgen,<br>es sei denn die Kommunikation wird über einen Proxy oder ein Gateway<br>vermittelt und der Verbindungsaufbau erfolgt von innen.|MUSS||||



## P.4.3.2 Zusätzliche Maßnahmen bei hohen Integritätsanforderungen 

Bundesamt für Sicherheit in der Informationstechnik 

49 

## P.4.3.3 Zusätzliche Maßnahmen bei hohen Vertraulichkeitsanforderungen 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|87|47|5.3.3.1|M.A.AM.VT.H.1|**Sensibilisierung und Verpflichtung der Mitarbeiterinnen und Mitarbeiter**|||||
|||||Es muss eine gesonderte Sensibilisierung und nachweisbare<br>Verpflichtungen der Mitarbeitenden für das mobile Scannen erfolgen.|MUSS||||
|88|47|5.3.3.2|M.A.AM.VT.H.3|**Löschen von Zwischenergebnissen**|||||
|||||Es darf keine Speicherung von Zwischenergebnissen auf dem mobilen<br>Endgerät erfolgen.|MUSS||||



## P.4.3.4 Zusätzliche Maßnahmen bei hohen Verfügbarkeitsanforderungen 

|**Nr**|**Seite**|**Kapitel**|**ID**|**Anforderung**|**M / S**|**Referenzen / Bemerkungen**|**Ergebnis**|**Ergebnis**|
|---|---|---|---|---|---|---|---|---|
|89|48|5.3.4.1|M.A.AM.VF.H.1|**Erweiterte Qualitätssicherung der Scanprodukte**|||||
|||||Die Maßgaben von A.AM.VF.H.1 müssen in der Zielinfrastruktur<br>umgesetzt werden.|MUSS||||
|||||Die Rückkopplung zum einscannenden Mitarbeitenden muss dabei<br>berücksichtigt werden.|MUSS||||
|90|48|5.3.4.2|M.A.AM.VF.H.2|**Fehlertolerante Protokolle und redundante Datenhaltung**|||||
|||||Die Maßgaben nach A.AM.VF.H.2 müssen in der Zielinfrastruktur und<br>beim mobilen Endgerät umgesetzt werden.|MUSS||||
|||||Da im mobilen Endgerät keine Datensicherung erfolgt muss die<br>redundante Datenhaltung in der Zielinfrastruktur der Organisation<br>erfolgen.|MUSS||||



Bundesamt für Sicherheit in der Informationstechnik 

50 

Referenzen 

## Referenzen 

[BSI-GSK] Bundesamt für Sicherheit in der Informationstechnik (BSI): IT-Grundschutz- Kompendium, 2023 - - - - - - - https://www.bsi.bund.de/DE/Themen/Unternehmen und Organisationen/Standards und Zertifizierung/IT Grundschutz/IT Grundschutz - - Kompendium/it grundschutz kompendium_node.html [BSI TR-02102-1] Bundesamt für Sicherheit in der Informationstechnik (BSI): Kryptographische Verfahren: Empfehlungen und Schlüssellängen, BSI TR-02102-1, https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR02102/BSI-TR02102.pdf?__blob=publicationFile&v=10 

- [BSI TR-03116-4] Bundesamt für Sicherheit in der Informationstechnik (BSI): Kryptographische Vorgaben für Projekte der Bundesregierung, Teil: Kommunikationsverfahren und Anwendungen, BSI TR-03116-4 ,https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR03116/BSI-TR-031164.pdf?__blob=publicationFile&v=5 

- [BSI TR-03125] Bundesamt für Sicherheit in der Informationstechnik (BSI): Beweiswerterhaltung kryptographisch signierter Dokumente (TR-ESOR), BSI TR- 

- 03125, https://www.bsi.bund.de/dok/TR 03125 

- [BSI TR-03138] Bundesamt für Sicherheit in der Informationstechnik (BSI): Ersetzendes Scannen, Technische Richtlinie (TR) des BSI Nr. 03138 (TR RESISCAN) 

- [BSI TR-03138-R] Bundesamt für Sicherheit in der Informationstechnik (BSI): Ersetzendes Scannen - Anwendungshinweis R: Unverbindliche rechtliche Hinweise, Anwendungshinweis R, Technische Richtlinie (TR) des BSI Nr. 03138 (TR RESISCAN) 

- [BSI TR-03145] Bundesamt für Sicherheit in der Informationstechnik (BSI): Secure CA operation, BSI TR-03145 

- [DIN66399] DIN: DIN 66399-1-3 Büro- und Datentechnik - Vernichten von Datenträgern - Teil 1: Grundlagen und Begriffe, Vernichten von Datenträgern - Teil 2: Anforderungen an Maschinen zur Vernichtung von Datenträgern; Vernichten von Datenträgern - Teil 3: Prozess der Datenträgervernichtung. https://www.din.de/de/meta/suche/62730!search?query=66399&submit-btn=Submit 

- [ETSI TS 119 312] ETSI TS 119 312: Electronic Signatures and Infrastructures (ESI); Cryptographic Suites 

- [ETSI TS 119 511] ETSI TS 119 511: Electronic Signatures and Infrastructures (ESI); Policy and security requirements for trust service providers providing longterm preservation of digital signatures or general data using digital signature techniques 

- [ISO27001] ISO/IEC, ISO/IEC 27001: Information security, cybersecurity and privacy protection Information security management systems - requirements, International Standard, https://www.iso.org/standard/27001 

- [ISO27002] ISO/IEC, ISO/IEC 27002: Information security, cybersecurity and privacy protection — Information security controls, International Standard, https://www.iso.org/standard/75652.html 

- [LeitLeSig] Leitlinie für digitale Signatur-/ Siegel-, Zeitstempelformate sowie technische Beweisdaten (Evidence Record). Bundesamt für Sicherheit in der Informationstechnik. 

- [NIST-800-57-1] E. Barker: Recommendation for Key Management – Part 1: General, NIST Special Publication 800-57 

- [NIST-800-57-2] E. Barker, W. Barker, W. Burr, W. Polk, M. Smid: Recommendation for Key Management – Part 2: Best Practices for Key Management Organization, NIST Special Publication 800-57 

- [NIST-800-133] E. Barker, A. Roginsky: Recommendation for Cryptographic Key Generation, NIST Special Publication 800-133 

- [VDG] Vertrauensdienstegesetz vom 18. Juli 2017 (BGBl. I S. 2745), das durch Artikel 2 des Gesetzes vom 18. Juli 2017 (BGBl. I S. 2745) geändert worden ist 

Bundesamt für Sicherheit in der Informationstechnik 

51 


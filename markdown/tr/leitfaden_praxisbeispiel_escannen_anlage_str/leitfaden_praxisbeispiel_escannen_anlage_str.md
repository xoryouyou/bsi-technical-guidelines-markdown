
![](markdown/tr/leitfaden_praxisbeispiel_escannen_anlage_str/leitfaden_praxisbeispiel_escannen_anlage_str.pdf-0001-00.png)



![](markdown/tr/leitfaden_praxisbeispiel_escannen_anlage_str/leitfaden_praxisbeispiel_escannen_anlage_str.pdf-0001-01.png)


## **Leitfaden: E-Scannen für Bundesbehörden** 

**Ersetzendes Scannen gemäß EGovG und TR-RESISCAN Anlage (STR): Muster Strukturanalyse** 

## Inhaltsverzeichnis 

|1|Einleitung ....................................................................................................................... 3|
|---|---|
|2|Strukturanalyse .............................................................................................................. 3|
|2.1|IT-Systeme und Anwendungen ............................................................................... 3|
|2.2|Netze und Kommunikationsbeziehungen ................................................................ 7|
|2.3|Datenobjekte ........................................................................................................... 8|



## 1 Einleitung 

_**Hinweis:**_ Die vorliegende Anlage 1 des Leitfadens „E-Scannen für Bundesbehörden“ kann als Dokumentenvorlage für die Erstellung einer **Strukturanalyse** gemäß der TR-RESISCAN genutzt werden. 

Wie in Abschnitt 4 des Leitfadens „E-Scannen für Bundesbehörden“ näher erläutert, beginnt die Einführung des Ersetzenden Scannens mit der Strukturanalyse, in der die relevanten Bestandteile des existierenden oder geplanten Scansystems bzw. Scanprozesses identifiziert werden. Hierbei werden die folgenden Aspekte betrachtet: 

- IT-Systeme und Anwendungen (siehe Abschnitt 2.1), 

- Netze und Kommunikationsbeziehungen (siehe Abschnitt 2.2) und 

- Datenobjekte (siehe Abschnitt 2.3). 

Zielgruppe des Musters Strukturanalyse sind vorrangig 

- IT-Sicherheitsbeauftragte und 

- Mitarbeiterinnen und Mitarbeiter der IT-Abteilung. 

Eine Unterstützung durch die für den Scanprozess fachliche verantwortliche Organisationseinheit ist empfehlenswert. 

## 2 Strukturanalyse 

## 2.1 IT-Systeme und Anwendungen 

Im Zuge der Identifikation der relevanten IT-Systeme und Anwendungen des Scansystems wird ein bereinigter Netzplan (siehe Abbildung 1) erstellt, der auch Ausgangspunkt für die mögliche Auditierung und Zertifizierung des Scanprozesses ist. Das zu betrachtende Scansystem umfasst dabei die zum Scannen notwendigen Komponenten inklusive der Schnittstellen zu den angrenzenden Systemen (z.B. E- Akte-System, TR-ESOR-System). 

Das Scansystem der Behörde ist im reduzierten Netzplan in Abbildung 1 im Überblick dargestellt. Der behördenspezifische Netzplan kann auf Basis des Powerpoint-Templates zur Muster-Strukturanalyse erstellt werden. 

_**Hinweis:**_ Dieser reduzierte Netzplan muss an das konkrete Scansystem der Behörde angepasst werden und bildet die Grundlage für die weiteren Betrachtungen. 


![](markdown/tr/leitfaden_praxisbeispiel_escannen_anlage_str/leitfaden_praxisbeispiel_escannen_anlage_str.pdf-0004-00.png)


Abbildung 1: Netzplan des Scansystems der [Organisation] 

Wie in Abbildung 1 ersichtlich, umfasst das _exemplarische Scansystem_ eine Reihe von Systemen (S _x_ ) (siehe 

Tabelle 1) und darauf laufenden Anwendungen (A _y_ ) (siehe Tabelle 2). 

Die hierbei identifizierten Systeme und Anwendungen bilden die Grundlage für die Bestimmung der notwendigen Sicherheitsmaßnahmen bei der Umsetzung der Anforderung A.T.1 (siehe auch Abschnitt 6.2 des Leitfadens), welche letztlich die Implementierung der relevanten Maßnahmen aus dem Grundschutz-Kompendium des BSI [BSI-GSK] fordert. 

_**Hinweis:**_ Die nachfolgende Tabelle muss an den konkreten Netzplan des Scansystems der Behörde angepasst werden. 

|**ID**|**IT-System**|**Beschreibung**|**Ausprägung**<br>**Anwenderbehörde**|
|---|---|---|---|
|S1|Scanner|Scanner für die Erzeugung eines<br>Scanproduktes aus dem scanrelevanten<br>Papierdokument.<br>**_Hinweis:_**Dieser Scanner kann lokal (z.<br>B. über USB) oder über ein Netzwerk an<br>die Scan-Workstation (S2)<br>angeschlossen sein.||
|S2|Scan-Workstation|Bildet die Ablaufumgebung für die<br>Scan-Software (A1), die für die<br>stationäre Digitalisierung der<br>Papierdokumente genutzt wird.<br>**_Hinweis:_**In der Praxis kann die hier<br>betrachtete „Scan-Workstation“ durch<br>mehrere gleichartige Rechnersysteme<br>realisiert sein, die im Rahmen der<br>Strukturanalyse zusammen betrachtet<br>werden können.||



|**ID**|**IT-System**|**Beschreibung**|**Ausprägung**<br>**Anwenderbehörde**|
|---|---|---|---|
|S3|Qualitätssicherungs<br>(QS)-Workstation|Bildet die Ablaufumgebung für die QS-<br>Software (A2), die zur<br>Qualitätssicherung der Scanprodukte<br>und zur Erzeugung des<br>Transfervermerks eingesetzt wird.<br>**_Hinweis:_**Sofern die IT-Plattform der<br>Scan-Workstation und der QS-<br>Workstation identisch ist, können die<br>beiden IT-Systeme zusammengefasst<br>betrachtet werden.||
|S4|Scan-Server|Bildet die Ablaufumgebung für den<br>Scan-Service (A3), der für die<br>Integration der Scan- und QS-Software<br>mit den angrenzenden Zielsystemen<br>und der mobilen Scan-Appsorgt.||
|S5|Firewall|Dient der Netzwerkssegmentierung<br>innerhalb der bestehenden IT-<br>Infrastruktur und trennt das<br>scanspezifische interne Netz von den<br>anderen internen bzw. externen<br>Netzen.||
|S6|Router|Sorgt für die IP-basierte<br>Kommunikation mit den angrenzenden<br>Systemen (E-Akte- und TR-ESOR-<br>System)bzw. dem Intranet.||
|S7|Proxyserver|Server auf dem ein als Application Level<br>Gateway fungierender Apache (A4)<br>läuft, der die TLS-gesicherte<br>Übertragung von extern erzeugten<br>Scanprodukten an den auf dem Scan-<br>Server (S4) laufenden Scan-Service (A3)<br>ermöglicht.||
|S8|Smartphone|Stellt die Ablaufumgebung für die Scan-<br>App (A5) bereit, die die mobile<br>Erfassung von beleghaften Dokumenten<br>und die gesicherte Übertragung der<br>entsprechenden Scanprodukte an den<br>auf dem Scan-Server (S4) laufenden<br>Scan-Service(A3)ermöglicht.||
|S9|IS-Hardware1|Signatur-/Siegelkarte zur<br>Integritätssicherung des Scanprodukts<br>und Transfervermerks||



**Tabelle 1: IT-Systeme im Scansystem der [Organisation]** 

> 1 Besteht nur wenn Signatur/Siegel auf Basis von Signatur- oder Siegelkarte erzeugt wird. 

5 

Für die IT-Systeme und Anwendungen sollen[2] Verantwortliche definiert werden. 

_**Hinweis:**_ Die nachfolgende Tabelle muss an den konkreten Netzplan des Scansystems der Behörde angepasst werden. 

|**ID**|**Anwendung**|**Beschreibung**|**Ausprägung**<br>**Anwenderbehörde**|
|---|---|---|---|
|A1|Scan-Software|Client-Software, die auf der Scan-<br>Workstation (S2) läuft und für die<br>digitale Erfassung von<br>Papierdokumentengenutzt wird.||
|A2|QS-Software|Client-Software, die auf der QS-<br>Workstation (S3) läuft und für die<br>Qualitätssicherung der Scanprodukte<br>und zur Erzeugung des Transfervermerks<br>genutzt wird.||
|A3|Scan-Service|Dienst, der auf dem Scan-Server (S4)<br>läuft und für die Integration der Scan-<br>Software (A1) und QS-Software (A2) mit<br>den angrenzenden Systemen (E-Akte-<br>und TR-ESOR-System) und der mobilen<br>Scan-App (A5) und zur<br>Integritätssicherung genutzt wird.||
|A4|Apache|Dienst, der auf dem Proxyserver (S7) als<br>Application Level Gateway läuft und die<br>TLS-gesicherte Übertragung von extern<br>erzeugten Scanprodukten von der Scan-<br>App (A5) an den Scan-Service (A3)<br>ermöglicht.||
|A5|Scan-App|Anwendung auf dem Smartphone (S8),<br>die die mobile Erfassung von beleghaften<br>Dokumenten und die gesicherte<br>Übertragung der entsprechenden<br>Scanprodukte an den Scan-Service (A3)<br>ermöglicht.||
|A6|IS-Software|Software zur Erzeugung (qualifizierter)<br>elektronischer Signaturen/Siegel oder<br>Zeitstempel ggf. in Kommunikation mit<br>dem qualifizierten<br>Vertrauendiensteanbieter zur<br>Integritätssicherung des Scanprodukts<br>sowie Transfervermerks.||
|A7|Indexsoftware|Softwarekomponente für die<br>automatische (z. B. durch OCR) oder<br>manuelle Bereitstellung von zum<br>Scanprodukt (D2) gehörigen Index- und<br>Metadaten (D3). Diese Index-Software<br>kann wie hier dargestellt auf der Scan-||



> 2 Siehe [BSI-TR03138] (A.O.1 f)). Hinweis: Sofern beispielsweise eine bestimmte Organisationseinheit für alle IT-Systeme und Anwendungen verantwortlich ist, kann hier auf eine differenzierte Betrachtung in den Tabellen hier verzichtet werden. 

|**ID**|**Anwendung**|**Beschreibung**|**Ausprägung**<br>**Anwenderbehörde**|
|---|---|---|---|
|||Workstation, einem eigenständigen<br>Indexier-Arbeitsplatz oder innerhalb<br>einer entsprechenden Fachanwendung<br>betrieben werden||



Tabelle 2: Anwendungen im Scansystem von [Organisation] 

## 2.2 Netze und Kommunikationsbeziehungen 

Zusätzlich zur Identifikation der IT-Systeme und Anwendungen müssen[3] im Rahmen der Strukturanalyse auch die Netze und Kommunikationsbeziehungen (siehe Abbildung 2) identifiziert werden, damit später adäquate Sicherheitsmaßnahmen[4] ausgewählt und umgesetzt werden können. Die behördenspezifische Darstellung der Netze und Kommunikationsbeziehungen kann auf Basis des Powerpoint-Templates zur Muster-Strukturanalyse erstellt werden. 

_**Hinweis:**_ Die nachfolgende Abbildung muss an den konkreten Netzplan des Scansystems der Behörde angepasst werden. 


![](markdown/tr/leitfaden_praxisbeispiel_escannen_anlage_str/leitfaden_praxisbeispiel_escannen_anlage_str.pdf-0007-05.png)


Abbildung 2: Netze und Kommunikationsbeziehungen im Scansystem von [Organisation] 

|**ID**|**Netze und**<br>**Kommunikationsbeziehungen**|**Beschreibung**|**Ausprägung**<br>**Anwenderbehörde**|
|---|---|---|---|
|N1|Scan-Netz|Im Scan-Netz befinden sich der<br>Scanner (S1), die Scan-<br>Workstation (S2), die QS-<br>Workstation (S3) und der Scan-<br>Server(S4).||



> 3 Siehe [BSI-TR03138] (A.G.1, e)) 

- 4 Siehe [BSI-TR03138] (A.T.1) 

7 

|**ID**|**Netze und**<br>**Kommunikationsbeziehungen**|**Beschreibung**|**Ausprägung**<br>**Anwenderbehörde**|
|---|---|---|---|
|N2|DMZ|In der De-Militarisierten-Zone<br>(DMZ), die von den beiden<br>Firewalls (S5) umschlossen wird,<br>befindet sich der Proxyserver<br>(S7).||
|N3|Internet|Das Internet wird für die<br>Übertragung der extern<br>erzeugten Scanproduktegenutzt.||
|K1|Scan-Server-TR-ESOR-System|Über diese<br>Kommunikationsbeziehung<br>werden die am Scan-Server<br>integritätsgesicherten<br>Scanprodukte, Index- und<br>Metadaten, Transfervermerke<br>etc. an das TR-ESOR-System zur<br>langfristigen Aufbewahrung<br>übergeben.||
|K2|Smartphone-Scan-Server|Über diese<br>Kommunikationsbeziehung<br>werden die am Smartphone<br>erzeugten Scanprodukte etc. an<br>den Scan-Servergeleitet.||



**Tabelle 3: Netze und Kommunikationsbeziehungen im Scansystem von [Organisation]** 

## 2.3 Datenobjekte 

Wie in der TR-RESISCAN gefordert, müssen[5] im Rahmen der Strukturanalyse die relevanten Dokumente und Datenobjekte identifiziert werden. Außerdem sollen[6] Verantwortliche für die jeweiligen Datenobjekte festgelegt werden. Die nachfolgende Tabelle der Datenobjekte basiert auf [BSI-TR03138A] (Tabelle 1): 

|**ID**|**Datenobjekt**|**Beschreibung**|**Ausprägung**<br>**Datenobjekt**<br>**Anwenderbehörde**|**Verantwortlichkeit**|
|---|---|---|---|---|
|D0|Schriftgut aus<br>dem<br>Posteingang|Schriftgut, das per Post o. ä.<br>eingegangen ist.|||
|D1|Scanrelevantes<br>Original|Papierdokument, das durch<br>geeignete Vorbereitungsschritte<br>(z. B. durch Entfernung des<br>Kuverts, Umkopieren,<br>Entklammern etc.) aus dem<br>eingegangenen Schriftgut (D0)<br>gewonnen und dem Scanprozess<br>zugeführt wird.<br>**_Hinweis:_**Die in einem konkreten<br>Scansystem verarbeiteten und|||



> 5 Siehe [BSI-TR03138] (A.O.1 b)) 

> 6 Siehe [BSI-TR03138] (A.O.1 f)). 

|**ID**|**Datenobjekt**|**Beschreibung**|**Ausprägung**<br>**Datenobjekt**<br>**Anwenderbehörde**|**Verantwortlichkeit**|
|---|---|---|---|---|
|||nicht-verarbeitbaren<br>Dokumenttypen_7_müssen im<br>Rahmen der<br>Verfahrensdokumentation<br>explizit aufgelistet werden. Dies<br>erfolgt sinnvoller Weise in der<br>Verfahrensanweisung (siehe<br>Anlage 3).|||
||Die genau verarbeiteten Dokumente sind in<br>Abschnitt 2.3 der Verfahrensanweisungaufgeführt.||||
|D2|Scanprodukt|Elektronisches Abbild des<br>Papierdokumentes (D1). Dieses<br>wird durch den Scanner erzeugt<br>und ggf. von der Scansoftware<br>nachbearbeitet.|||
|D3|Index- und<br>Metadaten|Daten, die das Auffinden und die<br>Nutzung des später abgelegten<br>Scanproduktes ermöglichen bzw.<br>erleichtern.<br>Durch die hier manuell oder<br>automatisch durch eine<br>Formularerkennungs-Software<br>vorgeschlagenen und im Rahmen<br>der Qualitätssicherung<br>überprüften bzw. ergänzten<br>Index- und Metadaten wird die<br>eindeutige Zuordnung der<br>Dokumente zu einem<br>Geschäftsvorfall sichergestellt,<br>wodurch ein wesentliches<br>Element der Ordnungsmäßigkeit<br>gegeben ist.|||
|D4|Transfervermerk|Mit dem Transfervermerk8wird<br>dokumentiert, wann und durch<br>wen die Übertragung des<br>Papierdokumentes in ein<br>elektronisches Dokument<br>stattgefunden hat.<br>**_Hinweis:_**Im vorliegenden<br>Beispiel des exemplarischen<br>Scansystems (siehe Abbildung 1)<br>wird der Transfervermerk vom<br>Scan-Service (A3) erstellt.|||
|D5|Sicherungsdaten|Sicherungsdaten sind<br>Datenobjekte,die dem Schutz|||



> 7 Siehe [BSI-TR03138] (A.G.1 a)). 

> 8 Siehe auch [BSI-TR03138] (A.NB.4). 

9 

|**ID**|**Datenobjekt**|**Beschreibung**|**Ausprägung**<br>**Datenobjekt**<br>**Anwenderbehörde**|**Verantwortlichkeit**|
|---|---|---|---|---|
|||der Integrität und ggf.<br>Authentizität anderer<br>Datenobjekte dienen.<br>**_Hinweis:_**Im vorliegenden<br>Beispiel des exemplarischen<br>Scansystems (siehe Abbildung 1)<br>werden zur Sicherung der<br>Integrität der Scanprodukte<br>fortgeschrittene elektronische<br>Siegel_9_eingesetzt.|||
|D6|Protokolldaten|Die Protokolldaten<br>dokumentieren zusätzliche<br>sicherheitsrelevante Abläufe und<br>Ereignisse. Sie unterstützen somit<br>die Nachvollziehbarkeit der<br>Abläufe und den Nachweis der<br>Ordnungsmäßigkeit des<br>Scanprozesses.|||



**Tabelle 4: Relevante Datenobjekte und Dokumenttypen im Scansystem von [Organisation]** 

## Verzeichnisse 

## Tabellenverzeichnis 

Tabelle 1: IT-Systeme im Scansystem der [Organisation] ..................................................... 5 Tabelle 2: Anwendungen im Scansystem von [Organisation] ................................................ 7 Tabelle 3: Netze und Kommunikationsbeziehungen im Scansystem von [Organisation]........ 8 Tabelle 4: Relevante Datenobjekte und Dokumenttypen im Scansystem von [Organisation] 10 Abbildungsverzeichnis Abbildung 1: Netzplan des Scansystems der [Organisation] .................................................. 4 Abbildung 2: Netze und Kommunikationsbeziehungen im Scansystem von [Organisation] ... 7 

## Literaturverzeichnis 

|[BSI-GSK]|Bundesamt für Sicherheit in der Informationstechnik (BSI): IT-Grundschutz-|
|---|---|
||Kompendium,|
||https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzKompendi|
||um/itgrundschutzKompendium_node.html|
|[BSI-TR03138]|Bundesamt für Sicherheit in der Informationstechnik (BSI): Ersetzendes|
||Scannen (RESISCAN), BSI TR-03138|
||https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr03138/inde|
||x_htm.html|
|[BSI-TR03138-A]|Bundesamt für Sicherheit in der Informationstechnik (BSI): Ersetzendes|
||Scannen – Anwendungshinweis A: Ergebnis der Risikoanalyse, BSI TR-|
||03138-A, Version 1.2, 2018|



## **Impressum** 

## **Herausgeber** 

Der Beauftragte der Bundesregierung für Informationstechnik, 10557 Berlin 

## **Ansprechpartner** 

Programm Dienstekonsolidierung Postanschrift: Alt-Moabit 140, 10557 Berlin Hausanschrift: Englische Str. 30, 10587 Berlin Referatspostfach: DGII1@bmi.bund.de Internet: www.cio.bund.de 

## **Stand** 

27.04.2020 

## **Bildnachweis** 

James Brey/GettyImages 

Die Publikation wird kostenlos abgegeben und ist nicht zum Verkauf bestimmt. Sie darf weder von Parteien noch von Wahlwerbern oder Wahlhelfern während eines Wahlkampfes zum Zwecke der Wahlwerbung verwendet werden. 

Dies gilt für Bundestags-, Landtags- und Kommunalwahlen sowie für Wahlen zum Europäischen Parlament. Nachdruck, auch auszugsweise, ist genehmigungspflichtig. 

www.cio.bund.de 


![](markdown/tr/leitfaden_praxisbeispiel_escannen_anlage_str/leitfaden_praxisbeispiel_escannen_anlage_str.pdf-0013-01.png)


1 


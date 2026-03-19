
![](markdown/tr/TR_De_Mail_ID_FU/TR_De_Mail_ID_FU.pdf-0001-00.png)



![](markdown/tr/TR_De_Mail_ID_FU/TR_De_Mail_ID_FU.pdf-0001-01.png)


BSI – Technische Richtlinie Bezeichnung: Identitätsbestätigungsdienst Funktionalitätsspezifikation Anwendungsbereich: De-Mail Kürzel: BSI TR 01201 Teil 4.1 Version: 1.8 

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn Tel.: +49 22899 9582-0 E-Mail: de-mail@bsi.bund.de Internet: https://www.bsi.bund.de © Bundesamt für Sicherheit in der Informationstechnik 2024 

## **Inhaltsverzeichnis** 

|1|Einleitung....................................................................................................................................5|
|---|---|
|2|Gesamtüberblick.........................................................................................................................6|
|3|Funktionale Anforderungen........................................................................................................8|
|3.1|Ident-Karten.........................................................................................................................................8|
|3.2|Ident-Auftrag.......................................................................................................................................9|
|3.3|Ident-Bestätigung...............................................................................................................................10|
|3.4|Ident-Bestätigungsnachricht..............................................................................................................10|
|3.5|Meldungen.........................................................................................................................................11|
|3.6|System-Adressen...............................................................................................................................11|
|4|Ablauf des Verfahrens..............................................................................................................12|
|5|Aktivitätsdiagramm...................................................................................................................14|
|6|Funktionale Beschreibung.........................................................................................................15|
|6.1|Einbindung des ID beim SP...............................................................................................................15|
|6.2|Identitätsbestätigung erstellen...........................................................................................................15|
|7|Anhang......................................................................................................................................23|
|7.1|Legende zum Aktivitätsdiagramm.....................................................................................................23|
|7.2|Legende zu Schritten der Ablaufbeschreibung..................................................................................24|



Bundesamt für Sicherheit in der Informationstechnik 

3 

## **Abbildungsverzeichnis** 

Abbildung 1: Gesamtüberblick ID.......................................................................................................6 Abbildung 2: Funktionaler Ablauf des ID..........................................................................................12 Abbildung 3: Aktivitätsdiagramm des ID..........................................................................................14 

## **Tabellenverzeichnis** 

Tabelle 1: Liste der im ID verwendeten System-Adressen................................................................11 Tabelle 2: Ablaufbeschreibung ID.....................................................................................................13 Tabelle 3: Schritte zum Erstellen eines Ident-Auftrages....................................................................16 Tabelle 4: Schritte zum Prüfen eines Ident-Auftrages durch DMDA................................................18 Tabelle 5: Schritte zur Prüfung der Ident-Bestätigung durch den Nutzer..........................................19 Tabelle 6: Schritte zum Erstellen und Versenden der Ident-Bestätigung...........................................22 Tabelle 7: Legende zum Aktivitätsdiagramm....................................................................................24 Tabelle 8: Legende zu Schritten.........................................................................................................25 

Bundesamt für Sicherheit in der Informationstechnik 

4 

1 Einleitung 

## **1 Einleitung** 

Dieses Modul beinhaltet die funktionalen Spezifikationen des Identitätsbestätigungsdienstes und ist Bestandteil von [TR DM ID M]. 

In diesem Modul werden die zwingenden Anforderungen an den ID von De-Mail technikneutral beschrieben, sofern dieser angeboten wird. Eine Spezifikation von Protokollen und zugehörigen Parametern erfolgt nur dort, wo dies aus funktionaler Sicht explizit erforderlich ist. 

Bundesamt für Sicherheit in der Informationstechnik 

5 

2 Gesamtüberblick 

## **2 Gesamtüberblick** 

Der ID ermöglicht es allen Nutzern von De-Mail-Konten und insbesondere Service Provider (SP), wie bspw. einem Web-Shop oder Auktionsportal, zuverlässig die Identitätsdaten eines De-MailNutzers zu erhalten. Der ID übermittelt, die im De-Mail-Konto des Nutzers hinterlegten und vom Nutzer explizit für diese Zwecke freigegebenen Identitätsattribute. Der Zeitpunkt der Verifikation wird immer zusammen mit den Identitätsdaten übertragen, sodass der Empfänger entscheiden kann, ob die Aktualität der Daten für seinen Geschäftsvorfall ausreichend ist. 

Folgende Rollen sind beim ID involviert: 

- Ein Nutzer von De-Mail ist eine bei einem DMDA registrierte natürliche Person oder Institution. Wenn er seinen DMDA beauftragt, seine Identitätsdaten über den ID einem SP zu übermitteln, wird er auch als Ident-Auftraggeber bezeichnet. 

- Ein SP ist i. d. R. ein Anbieter von Produkten oder Dienstleistungen im Internet. Er ist selbst als De-Mail-Nutzer bei einem DMDA registriert. Im Zusammenhang mit dem ID treten SP in erster Linie als diejenigen auf, die den ID zur Feststellung der Identität eines anderen DeMail-Nutzers verwenden. Neben den SP können aber auch andere natürliche Personen oder Institutionen Empfänger der Identitätsdaten sein. 


![](markdown/tr/TR_De_Mail_ID_FU/TR_De_Mail_ID_FU.pdf-0006-06.png)


_Abbildung 1: Gesamtüberblick ID_ 

Im Folgenden wird die Anwendung des ID kurz beschrieben: 

Ein Nutzer will einen Dienst eines SP (linker, dunkelgrüner Pfeil in Abbildung 1) nutzen. Der SP benötigt zur Erbringung des Dienstes zuverlässige Informationen über den Nutzer, wie bspw. Name, Vorname, Adresse oder Alter. Sofern der SP eine Identifizierung des Nutzers via De-Mail 

Bundesamt für Sicherheit in der Informationstechnik 

6 

## 2 Gesamtüberblick 

akzeptiert, teilt der SP dem Nutzer mit, welche Identitätsinformationen er vom Nutzer benötigt und an welche De-Mail-Adresse diese Informationen gesendet werden sollen. 

Der Nutzer meldet sich an seinem De-Mail-Konto zwingend mit Authentisierungsniveau „hoch“ an und veranlasst einen Ident-Auftrag (rechter, roter Pfeil in Abbildung 1), mit dem er auswählt, welche Identitätsinformationen an den SP gesendet werden sollen. 

Der DMDA des Nutzers erstellt im Rahmen des Ident-Auftrags eine sogenannte Ident-Bestätigung (vgl. Abschnitt 3.3), die anschließend in einer Nachricht (Ident-Bestätigungsnachricht) über den PVD von De-Mail (siehe [TR DM PVD FU]) zum SP übermittelt wird (oberer, blauer Pfeil in Abbildung 1). Der SP prüft die erhaltene Ident-Bestätigung. 

Eine detaillierte Beschreibung des Ablaufs erfolgt in Abschnitt 4. 

Bundesamt für Sicherheit in der Informationstechnik 

7 

3 Funktionale Anforderungen 

## **3 Funktionale Anforderungen** 

Die Definition und Beschreibung der relevanten Datenstrukturen erfolgen [TR DM ID IO]. 

## **3.1 Ident-Karten** 

Bei De-Mail existiert eine Mindestanzahl an Ident-Karten, die einheitlich von allen DMDA umgesetzt werden müssen. Ident-Karten können Identitäts- oder Adresskarten sein. Jede Ident-Karte enthält unterschiedliche Identitätsattribute. Zu jedem Identitätsattribut muss das dazugehörige MetaAttribut Datum und Uhrzeit der letzten Verifikation (vgl. [TR DM ACM FU]) angegeben werden. 

Im Folgenden werden die Ident-Karten definiert, die mindestens vom DMDA umgesetzt werden müssen. Der DMDA kann weitere definieren und anbieten. 

## **3.1.1 De-Mail-Adresskarte** 

Die De-Mail-Adresskarte enthält nur die vom Nutzer verwendete De-Mail-Adresse und kann eingesetzt werden, um die De-Mail-Adresse gegenüber einem SP als valide zu bestätigen. Diese De-Mail-Adresse ist identisch zu der Adresse, die der Ident-Bestätigung durch den ID hinzugefügt wird (vgl. Abschnitt 3.3). Als De-Mail-Adresse kann hierbei auch eine Pseudonym-Adresse angegeben werden. 

## **3.1.2 Identitätskarte einer natürlichen Person** 

Die Identitätskarte beinhaltet alle Attribute, die zur vollständigen Beschreibung der Identität einer natürlichen Person erforderlich sind: 

- Name, 

- Vorname, 

- Straße, 

- Hausnummer, 

- Ort, 

- Plz, 

- Staat, 

- Geburtsdatum, 

- Geburtsort. 

## **3.1.3 Adresskarte einer natürlichen Person** 

Die Adresskarte beinhaltet alle Attribute, die zur vollständigen Beschreibung der Adresse einer natürlichen Person erforderlich sind: 

Bundesamt für Sicherheit in der Informationstechnik 

8 

## 3 Funktionale Anforderungen 

- Name, 

- Vorname, 

- Straße, 

- Hausnummer, 

- Ort, 

- Plz, 

- Staat. 

## **3.1.4 Alters-Karte einer natürlichen Person** 

Die Alters-Karte existiert in folgenden drei Ausprägungen: 

- Genaue Altersangabe in Jahren (z. B. 43 Jahre), 

- Alterskategorie 16 Jahre oder älter, 

- Alterskategorie 18 Jahre oder älter. 

Die Alterskategorie-Karten dürfen dem Nutzer im Rahmen der Ident-Auftragserstellung nur dann zur Auswahl angeboten werden, wenn das aktuelle Alter des Nutzers tatsächlich innerhalb des jeweiligen Kategorieintervalles liegt. 

Nicht bei allen natürlichen Personen ist das Geburtsdatum vollständig bekannt. Für die spezielle Funktion Alters-Karte muss in diesen Fällen das gemäß der bekannten Teildaten späteste mögliche Datum als Vergleichsdatum abgebildet werden (z. B. falls vom Geburtsdatum nur das Jahr bekannt ist der 31.12. des Jahres). So wird sichergestellt, dass auch im Falle unvollständiger Geburtsdaten eine Altersberechnung so erfolgt, dass das jüngste Alter berechnet wird. 

## **3.1.5 Adresskarte einer Institution** 

Die Adresskarte einer Institution beinhaltet alle Attribute, die zur vollständigen Beschreibung dieser erforderlich sind: 

- Name der Institution, 

- Straße, 

- Hausnummer, 

- Ort, 

- Plz, 

- Staat. 

## **3.2 Ident-Auftrag** 

Um einen Ident-Auftrag zu erteilen, ist zwingend eine Authentisierung mit Authentisierungsniveau „hoch“erforderlich. 

Bundesamt für Sicherheit in der Informationstechnik 

9 

## 3 Funktionale Anforderungen 

Für einen Ident-Auftrag ist zum einen die De-Mail-Adresse des Empfängers notwendig, an die die Ident-Bestätigung geschickt werden soll, und zum anderen die Ident-Karte, die die Identitätsattribute spezifiziert, die in der Ident-Bestätigung ausgewiesen werden sollen. 

Hat der Nutzer für Identitätsattribute, die von der ausgewählten Ident-Karte referenziert werden, verschiedene Angaben im De-Mail-Konto hinterlegt, so muss er bei der Erstellung des IdentAuftrages auswählen können, welche konkreten Daten in der Ident-Bestätigung ausgewiesen werden sollen. 

Weiterhin ist die De-Mail-Adresse des Ident-Auftraggebers erforderlich, die in der IdentBestätigung hinterlegt wird. Anstelle der primären De-Mail-Adresse, die seinen Namen im Klartext enthält (siehe [TR DM ACM FU]), kann dies auch eine Pseudonym-De-Mail-Adresse sein. In diesem Fall kann keine Ident-Karte ausgewählt werden, die einen Namen, einen Teil oder die vollständige postalische Adresse des Ident-Auftraggebers als Attribut enthält. 

Der Ident-Auftraggeber muss die Möglichkeit haben, die Inhalte der zu erstellenden IdentBestätigung zu überprüfen, bevor er den Ident-Auftrag bestätigt. 

## **3.3 Ident-Bestätigung** 

Unmittelbar nach Erhalt eines Ident-Auftrages erstellt der DMDA für die gewünschte De-MailAdresse eine Ident-Bestätigung. Dazu werden vom DMDA die auf der Ident-Karte vorgegebenen Attribute mit den konkreten Identitätsdaten des Ident-Auftraggebers ausgefüllt, um Metadaten ergänzt und anschließend mit einer qualifizierten elektronischen Signatur signiert. 

Die Ident-Bestätigung wird vom DMDA signiert, um einerseits die Korrektheit aller Daten zu bestätigen, und um andererseits zu versichern, dass der Nutzer mit Authentisierungsniveau „hoch“ an seinem De-Mail-Konto angemeldet war, als er den Ident-Auftrag gestellt hat. 

Die Ident-Bestätigung enthält neben dem Meta-Attribut „Verifikationszeitpunkt der Identitätsdaten“ für jedes Identitätsattribut (vgl. [TR DM ACM FU]) folgende Metadaten: 

- die spezifische System-Adresse für den ID, 

- die vom Ident-Auftraggeber verwendete De-Mail-Adresse, 

- die De-Mail-Adresse des Empfängers, für den die Bestätigung ausgestellt wird, 

- den Ausstellungszeitpunkt der Ident-Bestätigung. 

## **3.4 Ident-Bestätigungsnachricht** 

Die Ident-Bestätigungsnachricht ist eine Nachricht, die der DMDA ausschließlich aufgrund eines Ident-Auftrages an den angegebenen Empfänger über den PVD sendet. 

Absender der Ident-Bestätigungsnachricht ist jeweils die System-Adresse des ID. Empfänger der Nachricht ist der SP, der über seine De-Mail-Adresse adressiert wird. Der Ident-Auftraggeber wird in Kopie gesetzt. Der Betreff der Nachricht ist auf „Ident-Bestätigung“ zu setzen Und der entsprechende „Nachrichten-Typ“ zu setzen. Die Nachricht wird weiterhin mit der Versandoption „Persönlich“ versendet (vgl. [TR DM PVD FU]), um sicherzustellen, dass keine unautorisierten Personen die Identitätsattribute einsehen können. 

Bundesamt für Sicherheit in der Informationstechnik 

10 

## 3 Funktionale Anforderungen 

Die vom DMDA des Nutzers erstellte und signierte Ident-Bestätigung wird als Anhang der Nachricht über den PVD an die De-Mail-Adresse des SPs und in Kopie an den Ident-Auftraggeber zugestellt. Anhand der speziellen Absender-Adresse, die eine System-Adresse ist, kann der SP bzw. der Empfänger erkennen, ob die Nachricht tatsächlich im Rahmen eines Ident-Auftrages durch den DMDA erstellt wurde. 

Ident-Bestätigungsnachrichten müssen einen Hinweis zur Verwendung und Interpretation der Anhänge in Textform enthalten. Des Weiteren müssen diese Hinweise die wesentlichen Informationen aus der signierten Bestätigung referenzieren, wie z. B. die De-Mail-Adresse des Ident-Auftraggebers oder des SPs. 

## **3.5 Meldungen** 

Meldungen sind Informationen des ID an den Nutzer und können in Abhängigkeit der Benutzerschnittstelle, die der Nutzer verwendet, unterschiedlich dargestellt und bekannt gemacht werden. Bspw. können sie in einem Webbrowser dargestellt oder auch als Meldungsnachricht (siehe [TR DM PVD FU]) übermittelt werden. Es muss sichergestellt werden, dass der Nutzer Meldungen über die von ihm verwendete Benutzerschnittstelle unmittelbar zur Kenntnis nehmen kann. 

## **3.6 System-Adressen** 

In der nachfolgenden Tabelle werden die System-Adressen (siehe [TR DM ACM FU]) aufgelistet, die innerhalb des ID verwendet werden. 

|die innerhalb des ID verwendet werden.||
|---|---|
|**_Verwendungszweck_**|**_De-Mail-Adresse_**|
|Ident-Bestätigungen|Ident-Bestaetigung@<DMDA>|
|Meldungen|Ident-Meldung@<DMDA>|



_Tabelle 1: Liste der im ID verwendeten System-Adressen_ 

Bundesamt für Sicherheit in der Informationstechnik 

11 

4 Ablauf des Verfahrens 

## **4 Ablauf des Verfahrens** 

In der nachfolgenden Abbildung 2 ist der funktionale und zeitliche Ablauf für die Erstellung und den Versand einer Ident-Bestätigung zwischen Nutzer, d. h. dem Ident-Auftraggeber, dem SP und dem DMDA des Nutzers dargestellt. Die eigentliche Funktionalität des ID ist dabei mit einem Rahmen gekennzeichnet und wird in den nachfolgenden Abschnitten näher spezifiziert. 


![](markdown/tr/TR_De_Mail_ID_FU/TR_De_Mail_ID_FU.pdf-0012-03.png)


_Abbildung 2: Funktionaler Ablauf des ID_ 

|**_Schritt_**|**_Bezeichnung_**|**_Übermittlung_**|**_Beschreibung_**|
|---|---|---|---|
|1|Serviceanfrage|Web|Der Nutzer möchte bspw. einen Warenkorb<br>füllen und bestellen oder ein Konto beim SP<br>einrichten.|
|2|Identifizierung<br>anfordern|Web|Die dazu notwendige Identifizierung soll via<br>ID eines DMDA geschehen.|
|3|Ident-Karte und De-<br>Mail-Adresse<br>angeben|Web|Der SP nennt dem Nutzer eine De-Mail-<br>Adresse, an die der DMDA die Ident-<br>Bestätigung sendet. Ferner teilt der SP dem<br>Nutzer mit, welche Ident-Karte er benötigt.|
|4|Mit Ident-Dienst|Web|Der Benutzer verbindet sich mit dem|



Bundesamt für Sicherheit in der Informationstechnik 

12 

4 Ablauf des Verfahrens 

|**_Schritt_**|**_Bezeichnung_**|**_Übermittlung_**|**_Beschreibung_**|
|---|---|---|---|
||verbinden||Authentisierungsniveau „hoch“ mit dem ID<br>seines DMDA.|
|5|Ident-Auftrag<br>erstellen|Web|Der Nutzer veranlasst die Erstellung einer<br>Ident-Nachricht. Dabei teilt der Nutzer dem<br>DMDA die De-Mail-Adresse des SP, die zu<br>verwendende Ident-Karte und seine eigene<br>De-Mail-Adresse mit, die für die<br>Kommunikation mit dem SP verwendet wird.|
|6|Ident-Bestätigung<br>erstellen||Der ID erstellt eine Ident-Bestätigung.|
|7|Ident-Bestätigung<br>versenden|Nachricht|Der ID versendet die Ident-Bestätigung mittels<br>einer Nachricht über den PVD zum SP.<br>Eine Kopie der Nachricht erhält der Nutzer.|
|8|Ident-Bestätigung<br>empfangen|Nachricht|Der SP empfängt die Ident-Bestätigung vom<br>ID mittels des PVD.|



_Tabelle 2: Ablaufbeschreibung ID_ 

Bundesamt für Sicherheit in der Informationstechnik 

13 

5 Aktivitätsdiagramm 

## **5 Aktivitätsdiagramm** 

In Abbildung 3 wird der funktionale Ablauf des ID von der Erstellung eines Ident-Auftrages durch einen Nutzer bis zum Versenden einer Ident-Bestätigung an einen SP über den PVD (siehe [TR DM PVD FU]) in einem Aktivitätsdiagramm[1] dargestellt. Eine detaillierte technisch-funktionale Beschreibung der einzelnen Aktionen und Schritte des Aktivitätsdiagramms erfolgt in Abschnitt 6. 


![](markdown/tr/TR_De_Mail_ID_FU/TR_De_Mail_ID_FU.pdf-0014-03.png)


_Abbildung 3: Aktivitätsdiagramm des ID_ 

- 1 Eine Legende zu den Symbolen des Aktivitätsdiagramms findet sich in Abschnitt 7.1. 

Bundesamt für Sicherheit in der Informationstechnik 

14 

6 Funktionale Beschreibung 

## **6 Funktionale Beschreibung** 

Im Folgenden werden die einzelnen Schritte des Aktivitätsdiagramms aus Abschnitt 5 von der Erstellung eines Ident-Auftrages durch einen Nutzer bis zum Versenden einer Ident-Bestätigung an einen SP über den PVD von De-Mail beschrieben. Die referenzierten Funktionen des Account- und Zeitdienstes werden in [TR DM ACM FU] und in [TR DM IT-BInfra] erläutert. Eine Beschreibung, wie die einzelnen Schritte strukturiert sind, findet sich in diesem Abschnitt. 

## **6.1 Einbindung des ID beim SP** 

Der SP muss dem Nutzer im Vorfeld in geeigneter Form (z. B. auf seiner Website) eine De-MailAdresse und die geforderte Ident-Karte angeben, damit der Nutzer den Ident-Auftrag stellen kann, auf dessen Grundlage die Ident-Bestätigung vom DMDA erstellt wird. 

## **6.2 Identitätsbestätigung erstellen** 

## **6.2.1 Ident-Auftrag erstellen** 

|**Schritt 1**|**Ident-Auftrag erstellen**|
|---|---|
|Kurzbeschreibung|Der Nutzer erstellt einen Ident-Auftrag.|
|Akteure|Nutzer|
|Auslöser|Nutzer|
|Vorbedingung|**•**<br>De-Mail-Adresse vom SP erhalten<br>**•**<br>SP hat Ident-Karte mit benötigten Attributen mitgeteilt<br>**•**<br>Anmeldung am De-Mail-Konto mit Authentisierungsniveau „hoch“|
|Input|De-Mail-Adresse des SP<br>Typ der benötigten Ident-Karte|
|Ergebnis|Ident-Auftrag ist erstellt|
|Nachbedingung||
|Ablauf|**•**<br>Ident-Auftrag-Maske aufrufen<br>**•**<br>De-Mail-Adresse des SP eingeben<br>**•**<br>Ident-Karte auswählen<br>**◦**<br>ggf. Spezifikation, welche im De-Mail-Konto hinterlegten<br>Daten in der Ident-Bestätigung verwendet werden müssen (vgl.<br>Abschnitt 3.2)<br>**•**<br>Auftrag ausführen|



Bundesamt für Sicherheit in der Informationstechnik 

15 

6 Funktionale Beschreibung 

|Fehlerfälle|FC-01: Nutzer nicht am De-Mail-Konto mit Authentisierungsniveau „hoch“<br>angemeldet|
|---|---|
|**Schritt 2**|**Ident-Auftrag senden**|
|Kurzbeschreibung|Der Nutzer sendet den Ident-Auftrag zum ID.|
|Akteure|Nutzer, ID|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Ident-Auftrag|
|Ergebnis|Ident-Auftrag zum ID versendet|
|Nachbedingung||
|Ablauf|Ident-Auftrag zum ID senden|
|Fehlerfälle|FC-01: Ident-Auftrag wird nicht angenommen|



_Tabelle 3: Schritte zum Erstellen eines Ident-Auftrages_ 

## **6.2.2 Ident-Auftrag durch DMDA prüfen** 

|**Schritt 3**|**Ident-Auftrag empfangen**|
|---|---|
|Kurzbeschreibung|Der ID empfängt den Ident-Auftrag.|
|Akteure|Nutzer, ID|
|Auslöser|Nutzer|
|Vorbedingung|**•**<br>Sicherer Kanal zwischen den Kommunikationspartnern aufgebaut<br>**•**<br>Authentisierungsniveau des Nutzers „hoch“|
|Input|Ident-Auftrag|
|Ergebnis|Ident-Auftrag vom ID empfangen|
|Nachbedingung||
|Ablauf|Ident-Auftrag empfangen|
|Fehlerfälle|FC-01: Nutzer nicht am De-Mail-Konto mit Authentisierungsniveau „hoch“<br>angemeldet|
|**Schritt 4**|**Ident-Auftrag prüfen**|
|Kurzbeschreibung|Der ID prüft den Ident-Auftrag.|
|Akteure|ID, Account-Dienst|
|Auslöser|ID|
|Vorbedingung||



Bundesamt für Sicherheit in der Informationstechnik 

16 

6 Funktionale Beschreibung 

|Input|Ident-Auftrag<br>Aktuelles Authentisierungsniveau des Nutzers|
|---|---|
|Ergebnis|Ident-Auftrag geprüft|
|Nachbedingung||
|Ablauf|**•**<br>De-Mail-Adresse des SP syntaktisch prüfen<br>**•**<br>Ident-Karte prüfen, ob der Nutzer sie auswählen darf (z.B. bei<br>Alterskategorie-Karte)<br>**•**<br>Prüfen, ob explizit referenzierte Identitätsdaten für Ident-Karte<br>genutzt werden dürfen (vgl. Abschnitt 3.2)|
|Fehlerfälle|FC-01: De-Mail-Adresse des SP ist syntaktisch fehlerhaft<br>FC-02: Ident-Karte (für Nutzer) nicht vorhanden<br>FC-03: Referenzierte Identitätsdaten nicht erlaubt/nicht gültig|
|**Schritt 5**|<br>**Entscheidungsknoten: Auftrag OK?**|
|Kurzbeschreibung|Auswertung durch ID, ob der Ident-Auftrag korrekt gestellt wurde.|
|ja|Schritt 7|
|nein|Schritt 6|
|**Schritt 6**|**Fehlermeldung an Nutzer senden**|
|Kurzbeschreibung|Der ID sendet eine Fehlermeldung an den Nutzer (vgl. Abschnitt 3.4).|
|Akteure|ID|
|Auslöser|ID|
|Vorbedingung||
|Input|Fehlerfälle aus Schritt 4|
|Ergebnis|Meldung an Nutzer gesendet|
|Nachbedingung|Stopp|
|Ablauf|**•**<br>Fehlerfälle aus Schritt 4 zu einer Meldung verarbeiten<br>**•**<br>Meldung an Nutzer senden|
|Fehlerfälle|FC-01: Meldung konnte nicht abgesendet/dargestellt werden|
|**Schritt 7**|<br>**Inhalt der Ident-Bestätigung aufbereiten**|
|Kurzbeschreibung|Der ID erstellt die Inhalte der späteren Ident-Bestätigung|
|Akteure|ID, Account-Dienst, Zeitdienst|
|Auslöser|ID|
|Vorbedingung||
|Input|**•**<br>Ident-Karte|



Bundesamt für Sicherheit in der Informationstechnik 

17 

6 Funktionale Beschreibung 

||**•**<br>Nutzerkennung des Ident-Auftraggebers (De-Mail-Adresse des<br>Nutzers)<br>**•**<br>Nutzerkennung des Empfängers (De-Mail-Adresse des SP)<br>**•**<br>Nutzerkennung des Ausstellers (De-Mail-Adresse des DMDA)<br>**•**<br>Authentisierungsniveau des Nutzers<br>**•**<br>Ausstellungszeitpunkt (gesetzliche Zeit)|
|---|---|
|Ergebnis|Inhalte der Ident-Bestätigung erstellt|
|Nachbedingung||
|Ablauf|**•**<br>Anfrage an Account-Dienst (Attribute von Ident-Karte).<br>**•**<br>Identitätsdaten und deren Metadaten in die Ident-Bestätigung<br>einfügen.<br>**•**<br>Nutzerkennung des Ident-Auftraggebers (De-Mail-Adresse des<br>Nutzers) in die Ident-Bestätigung einfügen.<br>**•**<br>Nutzerkennung des Empfängers (De-Mail-Adresse des SP) in die<br>Ident-Bestätigung einfügen.<br>**•**<br>Nutzerkennung des Ausstellers (De-Mail-Adresse des DMDA) in<br>die Ident-Bestätigung einfügen.<br>**•**<br>Authentisierungsniveau des Nutzers in die Ident-Bestätigung<br>einfügen.<br>**•**<br>Ausstellungszeitpunkt in die Ident-Bestätigung einfügen.|
|Fehlerfälle|FC-01: Identitätsattribut für Nutzer nicht vorhanden|
|**Schritt 8**|**Inhalt der Ident-Bestätigung als Meldung versenden**|
|Kurzbeschreibung|Der ID erstellt eine Meldung an den Nutzer, der den Ident-Auftrag erstellt<br>hat. Die Meldung beinhaltet die Inhalte der späteren Ident-Bestätigung.|
|Akteure|ID, Nutzer|
|Auslöser|ID|
|Vorbedingung||
|Input|Inhalte der Ident-Bestätigung|
|Ergebnis|Inhalt der Ident-Bestätigung zum Nutzer versendet|
|Nachbedingung||
|Ablauf|**•**<br>Meldung mit Informationen aus Schritt 7 erstellen<br>**•**<br>Meldung zum Nutzer senden|
|Fehlerfälle|FC-01: Meldung wird nicht angenommen|



_Tabelle 4: Schritte zum Prüfen eines Ident-Auftrages durch DMDA_ 

Bundesamt für Sicherheit in der Informationstechnik 

18 

6 Funktionale Beschreibung 

## **6.2.3 Inhalte der Ident-Bestätigung durch Nutzer prüfen** 

|**Schritt 9**|**Inhalt der Ident-Bestätigung empfangen**|
|---|---|
|Kurzbeschreibung|Der Nutzer empfängt den Inhalt der (späteren) Ident-Bestätigung.|
|Akteure|ID, Nutzer|
|Auslöser|ID|
|Vorbedingung||
|Input|Ident-Auftrag|
|Ergebnis|Inhalt der Ident-Bestätigung vom ID empfangen|
|Nachbedingung||
|Ablauf|Inhalt der Ident-Bestätigung empfangen|
|Fehlerfälle||
|**Schritt 10**|**Inhalt der Ident-Bestätigung prüfen**|
|Kurzbeschreibung|Der Nutzer prüft die Richtigkeit der Inhalte der späteren Ident-Bestätigung.<br>Im Anschluss an die Prüfung kann er den Ident-Auftrag bestätigen oder<br>abbrechen.|
|Akteure|Nutzer|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Inhalt der Ident-Bestätigung|
|Ergebnis|Ident-Auftrag geprüft|
|Nachbedingung||
|Ablauf|**•**<br>Darstellung des Inhalts<br>**•**<br>Bestätigung oder Abbrechen des initiierten Ident-Auftrages|
|Fehlerfälle||
|**Schritt 11**|**Prüfergebnis senden**|
|Kurzbeschreibung|Das Prüfergebnis des Nutzers wird zum ID gesendet.|
|Akteure|Nutzer, ID|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Prüfergebnis (Bestätigung oder Abbrechen)|
|Ergebnis|Prüfergebnis zum ID versendet|
|Nachbedingung||
|Ablauf|Prüfergebnis zum ID senden|



Bundesamt für Sicherheit in der Informationstechnik 

19 

6 Funktionale Beschreibung 

Fehlerfälle FC-01: Prüfergebnis wird nicht angenommen 

_Tabelle 5: Schritte zur Prüfung der Ident-Bestätigung durch den Nutzer_ 

## **6.2.4 Ident-Bestätigung erstellen und versenden** 

|**Schritt 12**|**Prüfergebnis empfangen**|
|---|---|
|Kurzbeschreibung|Der ID empfängt das Prüfergebnis für den Ident-Auftrag.|
|Akteure|Nutzer, ID|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Prüfergebnis|
|Ergebnis|Prüfergebnis vom ID empfangen|
|Nachbedingung|Wenn kein Prüfergebnis empfangen wurde: Schritt 14.|
|Ablauf|Prüfergebnis empfangen|
|Fehlerfälle||
|**Schritt 13**|**Entscheidungsknoten: Prüfergebnis OK?**|
|Kurzbeschreibung|Auswertung, ob der Nutzer den Ident-Auftrag bestätigt (ja) oder<br>abgebrochen (nein) hat.|
|ja|Schritt 16|
|nein|Schritt 14|
|**Schritt 14**|**Inhalt der Ident-Bestätigung verwerfen**|
|Kurzbeschreibung|Der Inhalt der Ident-Bestätigung wird vom ID verworfen.|
|Akteure|ID|
|Auslöser|ID|
|Vorbedingung||
|Input|Inhalt der Ident-Bestätigung|
|Ergebnis|Inhalt der Ident-Bestätigung gelöscht|
|Nachbedingung||
|Ablauf|Löschen der Inhalte der Ident-Bestätigung|
|Fehlerfälle||
|**Schritt 15**|**Meldung mit Abbruch an Nutzer senden**|
|Kurzbeschreibung|Der ID sendet eine Meldung an den Nutzer, dass der Ident-Auftrag<br>abgebrochen wurde.|



Bundesamt für Sicherheit in der Informationstechnik 

20 

6 Funktionale Beschreibung 

|Akteure|ID|
|---|---|
|Auslöser|ID|
|Vorbedingung||
|Input||
|Ergebnis|Meldung an Nutzer gesendet|
|Nachbedingung|Stopp|
|Ablauf|Meldung mit Abbruch an Nutzer senden|
|Fehlerfälle|FC-01: Meldung konnte nicht abgesendet/dargestellt werden|
|**Schritt 16**|<br>**Ident-Bestätigung fertig stellen**|
|Kurzbeschreibung|Die in Schritt 7 erstellen Inhalte werden zur Ident-Bestätigung<br>zusammengestellt und vom ID mit einer qualifizierten elektronischen<br>Signatur signiert.|
|Akteure|ID|
|Auslöser|ID|
|Vorbedingung||
|Input|Inhalte der Ident-Bestätigung aus Schritt 7|
|Ergebnis|Ident-Bestätigung fertig erstellt|
|Nachbedingung||
|Ablauf|-<br>Inhalte der Ident-Bestätigung aus Schritt 7 in das Format für eine<br>Ident-Bestätigung strukturieren.<br>-<br>Die Ident-Bestätigung mit einer qualifizierten elektronischen Signatur<br>versehen|
|Fehlerfälle||
|**Schritt 17**|**Ident-Bestätigungsnachricht erstellen**|
|Kurzbeschreibung|Der ID erstellt eine Ident-Bestätigungsnachricht.|
|Akteure|ID|
|Auslöser|ID|
|Vorbedingung||
|Input|**•**<br>Ident-Bestätigung<br>**•**<br>Nutzerkennung des Absenders (De-Mail-Adresse des DMDA)<br>**•**<br>Nutzerkennung des Empfängers SP (De-Mail-Adresse des SP)<br>**•**<br>Nutzerkennung des Empfängers Nutzer (De-Mail-Adresse des<br>Nutzers)|
|Ergebnis|Ident-Bestätigungsnachricht erstellt|



Bundesamt für Sicherheit in der Informationstechnik 

21 

6 Funktionale Beschreibung 

|Nachbedingung||
|---|---|
|Ablauf|**•**<br>Ident-Bestätigung in Ident-Bestätigungsnachricht einfügen<br>**•**<br>Nutzerkennung des Ausstellers als Absender-Adresse der Ident-<br>Bestätigungsnachricht einfügen<br>**•**<br>Nutzerkennung des SP als Empfänger-Adresse der Ident-<br>Bestätigungsnachricht einfügen<br>**•**<br>Nutzerkennung des Ident-Auftraggebers in Kopie (Carbon Copy,<br>CC) als Empfänger-Adresse der Ident-Bestätigungsnachricht<br>einfügen<br>**•**<br>Versandoption „Persönlich“wählen|
|Fehlerfälle||
|**Schritt 18**|**Ident-Bestätigungsnachricht versenden**|
|Kurzbeschreibung|Der ID sendet die Ident-Bestätigungsnachricht über den PVD an den SP<br>und Nutzer.|
|Akteure|ID, Postfachdienst des Ausstellers|
|Auslöser|ID|
|Vorbedingung|Sicheren Kanal mit PVD aufgebaut|
|Input|Ident-Bestätigungsnachricht|
|Ergebnis|Ident-Bestätigungsnachricht an SP und Nutzer gesendet|
|Nachbedingung||
|Ablauf|Ident-Bestätigungsnachricht über den PVD versenden|
|Fehlerfälle|FC-01: Ident-Bestätigungsnachricht wurde nicht angenommen|



_Tabelle 6: Schritte zum Erstellen und Versenden der Ident-Bestätigung_ 

Bundesamt für Sicherheit in der Informationstechnik 

22 

7 Anhang 

## **7 Anhang** 

## **7.1 Legende zum Aktivitätsdiagramm** 

||**Startknoten**|Startknoten<br>Der Startknoten ist der Startpunkt eines Prozesses. Ein Prozess<br>darf mehrere Startknoten haben, in diesem Fall beginnen beim<br>Start des Prozesses mehrere Abläufe. Es ist möglich, dass ein<br>Prozess keinen Startknoten besitzt, sondern von einem Ereignis<br>angestoßen wird.|
|---|---|---|
||**Endknoten**|Endknoten<br>Der Endknoten gibt an, dass die Ausführung des Prozesses<br>abgeschlossen ist. Es kann in einem Prozessdiagramm mehrere<br>Ausgänge in Form dieser Endknoten geben. Gibt es zum<br>Zeitpunkt des Erreichens des Endknotens mehrere parallele<br>Abläufe innerhalb des Prozesses, werden beim Erreichen eines<br>Endknotens alle Abläufe gestoppt.|
||**Stopp**|Ablaufende<br>Das Ablaufende terminiert einen Ablauf. Im Unterschied zum<br>Endknoten, der einen ganzen Prozess beendet, hat das Erreichen<br>des Ablaufendes keinen Effekt auf andere parallele Abläufe, die<br>zu diesem Zeitpunkt innerhalb des Prozesses abgearbeitet<br>werden. Auf diese Weise lassen sich parallele Abläufe gezielt<br>und einzeln beenden.|
|||Kante<br>Die als Pfeile dargestellten Kanten verbinden die einzelnen<br>Komponenten des Diagramms und stellen den Kontrollfluss dar.|
||Aktion|Aktion<br>Eine Aktion ist ein einzelner Schritt innerhalb eines Prozesses,<br>der nicht mehr weiter zerlegt wird. Das bedeutet nicht<br>unbedingt, dass die Aktion in der realen Welt nicht mehr weiter<br>zerlegbar wäre, sondern dass die Aktion in diesem Diagramm<br>nicht mehr weiter verfeinert wird. Die Aktion kann Ein- und<br>Ausgabeinformationen besitzen. Der Output einer Aktion kann<br>der Input einer Folge-Aktion sein.|
||Aufruf einer<br>Aktivität|Aufruf einer Aktivität<br>Mit diesem Symbol kann aus einer Aktivität (Prozess) heraus<br>eine weitere Aktivität aufgerufen werden. Der Aufruf selbst ist<br>eine Aktion, der aufgerufene Ablauf eine weitere Aktivität.|



Bundesamt für Sicherheit in der Informationstechnik 

23 

7 Anhang 

||Ereignis<br>empfangen|Empfang eines Ereignisses<br>Diese Aktion wartet auf das Eintreten eines Ereignisses. Nach<br>dem Empfang des Ereignisses wird der im Aktivitätsdiagramm<br>definierte, von dieser Aktion ausgehende Ablauf abgearbeitet.|
|---|---|---|
||Signal senden|Senden von Signalen<br>Das Senden von Signalen bedeutet, dass ein Signal an eine<br>empfangende Aktivität gesendet wird. Die empfangende<br>Aktivität nimmt das Signal mit der Aktion „Ereignis<br>empfangen“entgegen und kann entsprechend darauf reagieren.|
||Entscheidungsknoten|Entscheidungsknoten<br>Die Raute stellt eine Verzweigung im Kontrollfluss dar. Eine<br>Verzweigung hat einen Eingang und zwei oder mehrere<br>Ausgänge. Jeder Ausgang wird mit einer Bedingung versehen.<br>Trifft eine Bedingung zu, wird am entsprechenden Ausgang<br>weiterverfahren.|
||Datenobjekt|Datenobjekt<br>Datenobjekte gehören üblicherweise nicht zum Symbolumfang<br>in UML-Aktivitätsdiagrammen. Sie sind hier jedoch eingeführt<br>worden, um an entscheidender Stelle zu verdeutlichen, welche<br>Datenobjekte, insbesondere im Fokus der Schutzbedarfsanalyse,<br>vorliegen.|



_Tabelle 7: Legende zum Aktivitätsdiagramm_ 

## **7.2 Legende zu Schritten der Ablaufbeschreibung** 

Schritte im Aktivitätsdiagramm bezeichnen im Kontrollfluss eingebundene einmalig ablaufende Aktionen, wie z. B. einen vom Nutzer erstellten Ident-Auftrag zu prüfen (Schritt 4 in Abschnitt 4). 

## Schritte werden in diesem Modul als Aktionen auf folgende Art und Weise beschrieben: 

|<br>Schritt<Nr.>|<br>Eindeutiger Name der Aktion|
|---|---|
|Kurzbeschreibung|Innerhalb der Kurzbeschreibung erfolgt eine verbale Beschreibung der<br>wesentlichen Funktionalität der Aktion.|
|Akteure|Alle Rollen bzw. Dienste, die innerhalb der Aktion in irgendeiner Weise<br>beteiligt sind, werden aufgezählt.|
|Auslöser|Der Auslöser ist ein Akteur, durch den die Aktion aufgerufen bzw.<br>initialisiert wird.|
|Vorbedingung|Unter Vorbedingungen werden die Bedingungen verstanden, die nicht aus<br>einer unmittelbar vorhergehenden Aktion folgen, sondern asynchron erzielt<br>werden müssen. Diese Aktivitäten sind nicht unbedingt in diesem Dokument<br>beschrieben, die Ergebnisse sind jedoch als Vorbedingungen für die<br>Ausführung der hier beschriebenen Aktion notwendig. Auf die Erfüllung|



Bundesamt für Sicherheit in der Informationstechnik 

24 

7 Anhang 

|Schritt<Nr.>|Eindeutiger Name der Aktion|
|---|---|
||dieser Vorbedingungen muss sich die nutzende Aktion verlassen können.|
|Input|Der Auslöser muss bei Initialisierung der Aktion die entsprechenden<br>Informationen an diese übergeben oder durch die Aktion abfragen lassen, so<br>dass eine Verarbeitung der Informationen innerhalb der Aktion erfolgen<br>kann.|
|Ergebnis|Nach Beendigung der Aktion muss eine bestimmte Information als Resultat<br>erarbeitet bzw. bereitgestellt werden.|
|Nachbedingung|Unter Nachbedingungen werden Bedingungen verstanden, die innerhalb<br>dieser Aktion nicht betrachtet werden und durch unmittelbar nachfolgende<br>Aktionen aufgegriffen und dort behandelt werden müssen.|
|Ablauf|Für die innerhalb der Aktion definierte Logik wird ein konkreter Ablauf<br>beschrieben. Die definierte Abfolge muss innerhalb der Aktion durchgeführt<br>und abgeschlossen werden.|
|Fehlerfälle|Als Fehlerfall wird ein Ergebnis einer Funktion bezeichnet, der innerhalb<br>der Funktionsspezifikation liegt, aber kein Standard-Ergebnis darstellt.<br>Die konkrete Behandlung eines Fehlerfalls ist implementierungsabhängig.<br>Je nach Fall können unterschiedliche Lösungsstrategien verwendet werden,<br>bspw. kann eine Aktion zu einem späteren Zeitpunkt wiederholt oder die<br>Aktion abgebrochen werden. Bei Abbruch einer Aktion ist der Nutzer<br>mindestens darüber zu informieren und alle bis zu diesem Schritt<br>generierten temporären Daten müssen gelöscht werden. In den<br>Beschreibungen der Fehlerfälle der Aktionen werden nur mögliche Fehler<br>beschrieben, die innerhalb der Funktionsspezifikation liegen.|



_Tabelle 8: Legende zu Schritten_ 

Bundesamt für Sicherheit in der Informationstechnik 

25 


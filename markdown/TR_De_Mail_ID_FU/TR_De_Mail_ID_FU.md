![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_2.jpeg)

# BSI – Technische Richtlinie

| Bezeichnung:       | Identitätsbestätigungsdienst<br>Funktionalitätsspezifikation |
|--------------------|--------------------------------------------------------------|
| Anwendungsbereich: | De-Mail                                                      |
| Kürzel:            | BSI TR 01201 Teil 4.1                                        |
| Version:           | 1.8                                                          |

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn Tel.: +49 22899 9582-0 E-Mail: [de-mail@bsi.bund.de](mailto:de-mail@bsi.bund.de) Internet: [https://www.bsi.bund.de](https://www.bsi.bund.de/) © Bundesamt für Sicherheit in der Informationstechnik 2024

| 1   | Einleitung5                                   |  |
|-----|-----------------------------------------------|--|
| 2   | Gesamtüberblick6                              |  |
| 3   | Funktionale Anforderungen8                    |  |
| 3.1 | Ident-Karten8                                 |  |
| 3.2 | Ident-Auftrag9                                |  |
| 3.3 | Ident-Bestätigung10                           |  |
| 3.4 | Ident-Bestätigungsnachricht10                 |  |
| 3.5 | Meldungen11                                   |  |
| 3.6 | System-Adressen11                             |  |
| 4   | Ablauf des Verfahrens12                       |  |
| 5   | Aktivitätsdiagramm14                          |  |
| 6   | Funktionale Beschreibung15                    |  |
| 6.1 | Einbindung des ID beim SP15                   |  |
| 6.2 | Identitätsbestätigung erstellen15             |  |
| 7   | Anhang23                                      |  |
| 7.1 | Legende zum Aktivitätsdiagramm23              |  |
| 7.2 | Legende zu Schritten der Ablaufbeschreibung24 |  |

### **Abbildungsverzeichnis**

| Abbildung 1: Gesamtüberblick ID6          |  |
|-------------------------------------------|--|
| Abbildung 2: Funktionaler Ablauf des ID12 |  |
| Abbildung 3: Aktivitätsdiagramm des ID14  |  |

### **Tabellenverzeichnis**

| Tabelle 1: Liste der im ID verwendeten System-Adressen11                 |  |
|--------------------------------------------------------------------------|--|
| Tabelle 2: Ablaufbeschreibung ID13                                       |  |
| Tabelle 3: Schritte zum Erstellen eines Ident-Auftrages16                |  |
| Tabelle 4: Schritte zum Prüfen eines Ident-Auftrages durch DMDA18        |  |
| Tabelle 5: Schritte zur Prüfung der Ident-Bestätigung durch den Nutzer19 |  |
| Tabelle 6: Schritte zum Erstellen und Versenden der Ident-Bestätigung22  |  |
| Tabelle 7: Legende zum Aktivitätsdiagramm24                              |  |
| Tabelle 8: Legende zu Schritten25                                        |  |

# <span id="page-4-0"></span>**1 Einleitung**

Dieses Modul beinhaltet die funktionalen Spezifikationen des Identitätsbestätigungsdienstes und ist Bestandteil von [TR DM ID M].

In diesem Modul werden die zwingenden Anforderungen an den ID von De-Mail technikneutral beschrieben, sofern dieser angeboten wird. Eine Spezifikation von Protokollen und zugehörigen Parametern erfolgt nur dort, wo dies aus funktionaler Sicht explizit erforderlich ist.

# <span id="page-5-0"></span>**2 Gesamtüberblick**

Der ID ermöglicht es allen Nutzern von De-Mail-Konten und insbesondere Service Provider (SP), wie bspw. einem Web-Shop oder Auktionsportal, zuverlässig die Identitätsdaten eines De-Mail-Nutzers zu erhalten. Der ID übermittelt, die im De-Mail-Konto des Nutzers hinterlegten und vom Nutzer explizit für diese Zwecke freigegebenen Identitätsattribute. Der Zeitpunkt der Verifikation wird immer zusammen mit den Identitätsdaten übertragen, sodass der Empfänger entscheiden kann, ob die Aktualität der Daten für seinen Geschäftsvorfall ausreichend ist.

Folgende Rollen sind beim ID involviert:

- **•** Ein Nutzer von De-Mail ist eine bei einem DMDA registrierte natürliche Person oder Institution. Wenn er seinen DMDA beauftragt, seine Identitätsdaten über den ID einem SP zu übermitteln, wird er auch als Ident-Auftraggeber bezeichnet.
- **•** Ein SP ist i. d. R. ein Anbieter von Produkten oder Dienstleistungen im Internet. Er ist selbst als De-Mail-Nutzer bei einem DMDA registriert. Im Zusammenhang mit dem ID treten SP in erster Linie als diejenigen auf, die den ID zur Feststellung der Identität eines anderen De-Mail-Nutzers verwenden. Neben den SP können aber auch andere natürliche Personen oder Institutionen Empfänger der Identitätsdaten sein.

![](_page_5_Figure_6.jpeg)

#### <span id="page-5-1"></span>*Abbildung 1: Gesamtüberblick ID*

Im Folgenden wird die Anwendung des ID kurz beschrieben:

Ein Nutzer will einen Dienst eines SP (linker, dunkelgrüner Pfeil in [Abbildung 1](#page-5-1)) nutzen. Der SP benötigt zur Erbringung des Dienstes zuverlässige Informationen über den Nutzer, wie bspw. Name, Vorname, Adresse oder Alter. Sofern der SP eine Identifizierung des Nutzers via De-Mail akzeptiert, teilt der SP dem Nutzer mit, welche Identitätsinformationen er vom Nutzer benötigt und an welche De-Mail-Adresse diese Informationen gesendet werden sollen.

Der Nutzer meldet sich an seinem De-Mail-Konto zwingend mit Authentisierungsniveau "hoch" an und veranlasst einen Ident-Auftrag (rechter, roter Pfeil in [Abbildung 1](#page-5-1)), mit dem er auswählt, welche Identitätsinformationen an den SP gesendet werden sollen.

Der DMDA des Nutzers erstellt im Rahmen des Ident-Auftrags eine sogenannte Ident-Bestätigung (vgl. Abschnitt [3.3\)](#page-9-0), die anschließend in einer Nachricht (Ident-Bestätigungsnachricht) über d[en](#page-5-1)  PVD von De-Mail (siehe [TR DM PVD FU]) zum SP übermittelt wird (oberer, blauer Pfeil in [Abbildung 1](#page-5-1)). Der SP prüft die erhaltene Ident-Bestätigung.

Eine detaillierte Beschreibung des Ablaufs erfolgt in Abschnitt [4](#page-11-0).

# <span id="page-7-0"></span>**3 Funktionale Anforderungen**

Die Definition und Beschreibung der relevanten Datenstrukturen erfolgen [TR DM ID IO].

### **3.1 Ident-Karten**

Bei De-Mail existiert eine Mindestanzahl an Ident-Karten, die einheitlich von allen DMDA umgesetzt werden müssen. Ident-Karten können Identitäts- oder Adresskarten sein. Jede Ident-Karte enthält unterschiedliche Identitätsattribute. Zu jedem Identitätsattribut muss das dazugehörige Meta-Attribut Datum und Uhrzeit der letzten Verifikation (vgl. [TR DM ACM FU]) angegeben werden.

Im Folgenden werden die Ident-Karten definiert, die mindestens vom DMDA umgesetzt werden müssen. Der DMDA kann weitere definieren und anbieten.

#### **3.1.1 De-Mail-Adresskarte**

Die De-Mail-Adresskarte enthält nur die vom Nutzer verwendete De-Mail-Adresse und kann eingesetzt werden, um die De-Mail-Adresse gegenüber einem SP als valide zu bestätigen. Diese De-Mail-Adresse ist identisch zu der Adresse, die der Ident-Bestätigung durch den ID hinzugefügt wird (vgl. Abschnitt [3.3\)](#page-9-0). Als De-Mail-Adresse kann hierbei auch eine Pseudonym-Adresse angegeben werden.

#### **3.1.2 Identitätskarte einer natürlichen Person**

Die Identitätskarte beinhaltet alle Attribute, die zur vollständigen Beschreibung der Identität einer natürlichen Person erforderlich sind:

- **•** Name,
- **•** Vorname,
- **•** Straße,
- **•** Hausnummer,
- **•** Ort,
- **•** Plz,
- **•** Staat,
- **•** Geburtsdatum,
- **•** Geburtsort.

#### **3.1.3 Adresskarte einer natürlichen Person**

Die Adresskarte beinhaltet alle Attribute, die zur vollständigen Beschreibung der Adresse einer natürlichen Person erforderlich sind:

- **•** Name,
- **•** Vorname,
- **•** Straße,
- **•** Hausnummer,
- **•** Ort,
- **•** Plz,
- **•** Staat.

#### **3.1.4 Alters-Karte einer natürlichen Person**

Die Alters-Karte existiert in folgenden drei Ausprägungen:

- **•** Genaue Altersangabe in Jahren (z. B. 43 Jahre),
- **•** Alterskategorie 16 Jahre oder älter,
- **•** Alterskategorie 18 Jahre oder älter.

Die Alterskategorie-Karten dürfen dem Nutzer im Rahmen der Ident-Auftragserstellung nur dann zur Auswahl angeboten werden, wenn das aktuelle Alter des Nutzers tatsächlich innerhalb des jeweiligen Kategorieintervalles liegt.

Nicht bei allen natürlichen Personen ist das Geburtsdatum vollständig bekannt. Für die spezielle Funktion Alters-Karte muss in diesen Fällen das gemäß der bekannten Teildaten späteste mögliche Datum als Vergleichsdatum abgebildet werden (z. B. falls vom Geburtsdatum nur das Jahr bekannt ist der 31.12. des Jahres). So wird sichergestellt, dass auch im Falle unvollständiger Geburtsdaten eine Altersberechnung so erfolgt, dass das jüngste Alter berechnet wird.

#### **3.1.5 Adresskarte einer Institution**

Die Adresskarte einer Institution beinhaltet alle Attribute, die zur vollständigen Beschreibung dieser erforderlich sind:

- **•** Name der Institution,
- **•** Straße,
- **•** Hausnummer,
- **•** Ort,
- **•** Plz,
- **•** Staat.

## <span id="page-8-0"></span>**3.2 Ident-Auftrag**

Um einen Ident-Auftrag zu erteilen, ist zwingend eine Authentisierung mit Authentisierungsniveau "hoch"erforderlich.

Für einen Ident-Auftrag ist zum einen die De-Mail-Adresse des Empfängers notwendig, an die die Ident-Bestätigung geschickt werden soll, und zum anderen die Ident-Karte, die die Identitätsattribute spezifiziert, die in der Ident-Bestätigung ausgewiesen werden sollen.

Hat der Nutzer für Identitätsattribute, die von der ausgewählten Ident-Karte referenziert werden, verschiedene Angaben im De-Mail-Konto hinterlegt, so muss er bei der Erstellung des Ident-Auftrages auswählen können, welche konkreten Daten in der Ident-Bestätigung ausgewiesen werden sollen.

Weiterhin ist die De-Mail-Adresse des Ident-Auftraggebers erforderlich, die in der Ident-Bestätigung hinterlegt wird. Anstelle der primären De-Mail-Adresse, die seinen Namen im Klartext enthält (siehe [TR DM ACM FU]), kann dies auch eine Pseudonym-De-Mail-Adresse sein. In diesem Fall kann keine Ident-Karte ausgewählt werden, die einen Namen, einen Teil oder die vollständige postalische Adresse des Ident-Auftraggebers als Attribut enthält.

Der Ident-Auftraggeber muss die Möglichkeit haben, die Inhalte der zu erstellenden Ident-Bestätigung zu überprüfen, bevor er den Ident-Auftrag bestätigt.

### <span id="page-9-0"></span>**3.3 Ident-Bestätigung**

Unmittelbar nach Erhalt eines Ident-Auftrages erstellt der DMDA für die gewünschte De-Mail-Adresse eine Ident-Bestätigung. Dazu werden vom DMDA die auf der Ident-Karte vorgegebenen Attribute mit den konkreten Identitätsdaten des Ident-Auftraggebers ausgefüllt, um Metadaten ergänzt und anschließend mit einer qualifizierten elektronischen Signatur signiert.

Die Ident-Bestätigung wird vom DMDA signiert, um einerseits die Korrektheit aller Daten zu bestätigen, und um andererseits zu versichern, dass der Nutzer mit Authentisierungsniveau "hoch" an seinem De-Mail-Konto angemeldet war, als er den Ident-Auftrag gestellt hat.

Die Ident-Bestätigung enthält neben dem Meta-Attribut "Verifikationszeitpunkt der Identitätsdaten" für jedes Identitätsattribut (vgl. [TR DM ACM FU]) folgende Metadaten:

- **•** die spezifische System-Adresse für den ID,
- **•** die vom Ident-Auftraggeber verwendete De-Mail-Adresse,
- **•** die De-Mail-Adresse des Empfängers, für den die Bestätigung ausgestellt wird,
- **•** den Ausstellungszeitpunkt der Ident-Bestätigung.

### **3.4 Ident-Bestätigungsnachricht**

Die Ident-Bestätigungsnachricht ist eine Nachricht, die der DMDA ausschließlich aufgrund eines Ident-Auftrages an den angegebenen Empfänger über den PVD sendet.

Absender der Ident-Bestätigungsnachricht ist jeweils die System-Adresse des ID. Empfänger der Nachricht ist der SP, der über seine De-Mail-Adresse adressiert wird. Der Ident-Auftraggeber wird in Kopie gesetzt. Der Betreff der Nachricht ist auf "Ident-Bestätigung" zu setzen Und der entsprechende "Nachrichten-Typ" zu setzen. Die Nachricht wird weiterhin mit der Versandoption "Persönlich" versendet (vgl. [TR DM PVD FU]), um sicherzustellen, dass keine unautorisierten Personen die Identitätsattribute einsehen können.

Die vom DMDA des Nutzers erstellte und signierte Ident-Bestätigung wird als Anhang der Nachricht über den PVD an die De-Mail-Adresse des SPs und in Kopie an den Ident-Auftraggeber zugestellt. Anhand der speziellen Absender-Adresse, die eine System-Adresse ist, kann der SP bzw. der Empfänger erkennen, ob die Nachricht tatsächlich im Rahmen eines Ident-Auftrages durch den DMDA erstellt wurde.

Ident-Bestätigungsnachrichten müssen einen Hinweis zur Verwendung und Interpretation der Anhänge in Textform enthalten. Des Weiteren müssen diese Hinweise die wesentlichen Informationen aus der signierten Bestätigung referenzieren, wie z. B. die De-Mail-Adresse des Ident-Auftraggebers oder des SPs.

### <span id="page-10-0"></span>**3.5 Meldungen**

Meldungen sind Informationen des ID an den Nutzer und können in Abhängigkeit der Benutzerschnittstelle, die der Nutzer verwendet, unterschiedlich dargestellt und bekannt gemacht werden. Bspw. können sie in einem Webbrowser dargestellt oder auch als Meldungsnachricht (siehe [TR DM PVD FU]) übermittelt werden. Es muss sichergestellt werden, dass der Nutzer Meldungen über die von ihm verwendete Benutzerschnittstelle unmittelbar zur Kenntnis nehmen kann.

### **3.6 System-Adressen**

In der nachfolgenden Tabelle werden die System-Adressen (siehe [TR DM ACM FU]) aufgelistet, die innerhalb des ID verwendet werden.

| Verwendungszweck    | De-Mail-Adresse           |
|---------------------|---------------------------|
| Ident-Bestätigungen | Ident-Bestaetigung@<DMDA> |
| Meldungen           | Ident-Meldung@<DMDA>      |

*Tabelle 1: Liste der im ID verwendeten System-Adressen*

# <span id="page-11-0"></span>**4 Ablauf des Verfahrens**

In der nachfolgenden [Abbildung 2](#page-11-1) ist der funktionale und zeitliche Ablauf für die Erstellung und den Versand einer Ident-Bestätigung zwischen Nutzer, d. h. dem Ident-Auftraggeber, dem SP und dem DMDA des Nutzers dargestellt. Die eigentliche Funktionalität des ID ist dabei mit einem Rahmen gekennzeichnet und wird in den nachfolgenden Abschnitten näher spezifiziert.

![](_page_11_Figure_3.jpeg)

<span id="page-11-1"></span>*Abbildung 2: Funktionaler Ablauf des ID*

| Schritt | Bezeichnung                                   | Übermittlung | Beschreibung                                                                                                                                                             |
|---------|-----------------------------------------------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1       | Serviceanfrage                                | Web          | Der Nutzer möchte bspw. einen Warenkorb<br>füllen und bestellen oder ein Konto beim SP<br>einrichten.                                                                    |
| 2       | Identifizierung<br>anfordern                  | Web          | Die dazu notwendige Identifizierung soll via<br>ID eines DMDA geschehen.                                                                                                 |
| 3       | Ident-Karte und De<br>Mail-Adresse<br>angeben | Web          | Der SP nennt dem Nutzer eine De-Mail<br>Adresse, an die der DMDA die Ident<br>Bestätigung sendet. Ferner teilt der SP dem<br>Nutzer mit, welche Ident-Karte er benötigt. |
| 4       | Mit Ident-Dienst                              | Web          | Der Benutzer verbindet sich mit dem                                                                                                                                      |

| Schritt | Bezeichnung                    | Übermittlung | Beschreibung                                                                                                                                                                                                                                                     |
|---------|--------------------------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         | verbinden                      |              | Authentisierungsniveau "hoch" mit dem ID<br>seines DMDA.                                                                                                                                                                                                         |
| 5       | Ident-Auftrag<br>erstellen     | Web          | Der Nutzer veranlasst die Erstellung einer<br>Ident-Nachricht. Dabei teilt der Nutzer dem<br>DMDA die De-Mail-Adresse des SP, die zu<br>verwendende Ident-Karte und seine eigene<br>De-Mail-Adresse mit, die für die<br>Kommunikation mit dem SP verwendet wird. |
| 6       | Ident-Bestätigung<br>erstellen |              | Der ID erstellt eine Ident-Bestätigung.                                                                                                                                                                                                                          |
| 7       | Ident-Bestätigung<br>versenden | Nachricht    | Der ID versendet die Ident-Bestätigung mittels<br>einer Nachricht über den PVD zum SP.<br>Eine Kopie der Nachricht erhält der Nutzer.                                                                                                                            |
| 8       | Ident-Bestätigung<br>empfangen | Nachricht    | Der SP empfängt die Ident-Bestätigung vom<br>ID mittels des PVD.                                                                                                                                                                                                 |

*Tabelle 2: Ablaufbeschreibung ID*

# <span id="page-13-0"></span>**5 Aktivitätsdiagramm**

In [Abbildung 3](#page-13-1) wird der funktionale Ablauf des ID von der Erstellung eines Ident-Auftrages durch einen Nutzer bis zum Versenden einer Ident-Bestätigung an einen SP über den PVD (siehe [TR DM PVD FU]) in einem Aktivitätsdiagramm[1](#page-13-2) dargestellt. Eine detaillierte technisch-funktionale Beschreibung der einzelnen Aktionen und Schritte des Aktivitätsdiagramms erfolgt in Abschnitt [6.](#page-14-0)

![](_page_13_Figure_3.jpeg)

<span id="page-13-1"></span>*Abbildung 3: Aktivitätsdiagramm des ID*

<span id="page-13-2"></span><sup>1</sup> Eine Legende zu den Symbolen des Aktivitätsdiagramms findet sich in Abschnitt [7.1](#page-22-1).

# <span id="page-14-0"></span>**6 Funktionale Beschreibung**

Im Folgenden werden die einzelnen Schritte des Aktivitätsdiagramms aus Abschnitt [5](#page-13-0) von der Erstellung eines Ident-Auftrages durch einen Nutzer bis zum Versenden einer Ident-Bestätigung an einen SP über den PVD von De-Mail beschrieben. Die referenzierten Funktionen des Account- und Zeitdienstes werden in [TR DM ACM FU] und in [TR DM IT-BInfra] erläutert. Eine Beschreibung, wie die einzelnen Schritte strukturiert sind, findet sich in diesem Abschnitt.

### **6.1 Einbindung des ID beim SP**

Der SP muss dem Nutzer im Vorfeld in geeigneter Form (z. B. auf seiner Website) eine De-Mail-Adresse und die geforderte Ident-Karte angeben, damit der Nutzer den Ident-Auftrag stellen kann, auf dessen Grundlage die Ident-Bestätigung vom DMDA erstellt wird.

### **6.2 Identitätsbestätigung erstellen**

|  | 6.2.1 | Ident-Auftrag erstellen |  |
|--|-------|-------------------------|--|
|--|-------|-------------------------|--|

| Schritt 1        | Ident-Auftrag erstellen                                                                                                                         |  |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|--|
| Kurzbeschreibung | Der Nutzer erstellt einen Ident-Auftrag.                                                                                                        |  |
| Akteure          | Nutzer                                                                                                                                          |  |
| Auslöser         | Nutzer                                                                                                                                          |  |
| Vorbedingung     | De-Mail-Adresse vom SP erhalten<br>•                                                                                                            |  |
|                  | SP hat Ident-Karte mit benötigten Attributen mitgeteilt<br>•                                                                                    |  |
|                  | Anmeldung am De-Mail-Konto mit Authentisierungsniveau "hoch"<br>•                                                                               |  |
| Input            | De-Mail-Adresse des SP                                                                                                                          |  |
|                  | Typ der benötigten Ident-Karte                                                                                                                  |  |
| Ergebnis         | Ident-Auftrag ist erstellt                                                                                                                      |  |
| Nachbedingung    |                                                                                                                                                 |  |
| Ablauf           | Ident-Auftrag-Maske aufrufen<br>•                                                                                                               |  |
|                  | De-Mail-Adresse des SP eingeben<br>•                                                                                                            |  |
|                  | Ident-Karte auswählen<br>•                                                                                                                      |  |
|                  | ggf. Spezifikation, welche im De-Mail-Konto hinterlegten<br>◦<br>Daten in der Ident-Bestätigung verwendet werden müssen (vgl.<br>Abschnitt 3.2) |  |
|                  | Auftrag ausführen<br>•                                                                                                                          |  |

| Fehlerfälle      | FC-01: Nutzer nicht am De-Mail-Konto mit Authentisierungsniveau "hoch"<br>angemeldet |
|------------------|--------------------------------------------------------------------------------------|
| Schritt 2        | Ident-Auftrag senden                                                                 |
| Kurzbeschreibung | Der Nutzer sendet den Ident-Auftrag zum ID.                                          |
| Akteure          | Nutzer, ID                                                                           |
| Auslöser         | Nutzer                                                                               |
| Vorbedingung     |                                                                                      |
| Input            | Ident-Auftrag                                                                        |
| Ergebnis         | Ident-Auftrag zum ID versendet                                                       |
| Nachbedingung    |                                                                                      |
| Ablauf           | Ident-Auftrag zum ID senden                                                          |
| Fehlerfälle      | FC-01: Ident-Auftrag wird nicht angenommen                                           |

*Tabelle 3: Schritte zum Erstellen eines Ident-Auftrages*

#### **6.2.2 Ident-Auftrag durch DMDA prüfen**

<span id="page-15-0"></span>

| Schritt 3        | Ident-Auftrag empfangen                                                              |
|------------------|--------------------------------------------------------------------------------------|
| Kurzbeschreibung | Der ID empfängt den Ident-Auftrag.                                                   |
| Akteure          | Nutzer, ID                                                                           |
| Auslöser         | Nutzer                                                                               |
| Vorbedingung     | Sicherer Kanal zwischen den Kommunikationspartnern aufgebaut<br>•                    |
|                  | Authentisierungsniveau des Nutzers "hoch"<br>•                                       |
| Input            | Ident-Auftrag                                                                        |
| Ergebnis         | Ident-Auftrag vom ID empfangen                                                       |
| Nachbedingung    |                                                                                      |
| Ablauf           | Ident-Auftrag empfangen                                                              |
| Fehlerfälle      | FC-01: Nutzer nicht am De-Mail-Konto mit Authentisierungsniveau "hoch"<br>angemeldet |
| Schritt 4        | Ident-Auftrag prüfen                                                                 |
| Kurzbeschreibung | Der ID prüft den Ident-Auftrag.                                                      |
| Akteure          | ID, Account-Dienst                                                                   |
| Auslöser         | ID                                                                                   |
| Vorbedingung     |                                                                                      |

<span id="page-16-1"></span><span id="page-16-0"></span>

| Input            | Ident-Auftrag                                                                                                        |
|------------------|----------------------------------------------------------------------------------------------------------------------|
|                  | Aktuelles Authentisierungsniveau des Nutzers                                                                         |
| Ergebnis         | Ident-Auftrag geprüft                                                                                                |
| Nachbedingung    |                                                                                                                      |
| Ablauf           | De-Mail-Adresse des SP syntaktisch prüfen<br>•                                                                       |
|                  | Ident-Karte prüfen, ob der Nutzer sie auswählen darf (z.B. bei<br>•<br>Alterskategorie-Karte)                        |
|                  | Prüfen, ob explizit referenzierte Identitätsdaten für Ident-Karte<br>•<br>genutzt werden dürfen (vgl. Abschnitt 3.2) |
| Fehlerfälle      | FC-01: De-Mail-Adresse des SP ist syntaktisch fehlerhaft                                                             |
|                  | FC-02: Ident-Karte (für Nutzer) nicht vorhanden                                                                      |
|                  | FC-03: Referenzierte Identitätsdaten nicht erlaubt/nicht gültig                                                      |
| Schritt 5        | Entscheidungsknoten: Auftrag OK?                                                                                     |
| Kurzbeschreibung | Auswertung durch ID, ob der Ident-Auftrag korrekt gestellt wurde.                                                    |
| ja               | Schritt 7                                                                                                            |
| nein             | Schritt 6                                                                                                            |
| Schritt 6        | Fehlermeldung an Nutzer senden                                                                                       |
| Kurzbeschreibung | Der ID sendet eine Fehlermeldung an den Nutzer (vgl. Abschnitt 3.4).                                                 |
| Akteure          | ID                                                                                                                   |
| Auslöser         | ID                                                                                                                   |
| Vorbedingung     |                                                                                                                      |
| Input            | Fehlerfälle aus Schritt 4                                                                                            |
| Ergebnis         | Meldung an Nutzer gesendet                                                                                           |
| Nachbedingung    | Stopp                                                                                                                |
| Ablauf           | Fehlerfälle aus Schritt 4 zu einer Meldung verarbeiten<br>•                                                          |
|                  | Meldung an Nutzer senden<br>•                                                                                        |
| Fehlerfälle      | FC-01: Meldung konnte nicht abgesendet/dargestellt werden                                                            |
| Schritt 7        | Inhalt der Ident-Bestätigung aufbereiten                                                                             |
| Kurzbeschreibung | Der ID erstellt die Inhalte der späteren Ident-Bestätigung                                                           |
| Akteure          | ID, Account-Dienst, Zeitdienst                                                                                       |
| Auslöser         | ID                                                                                                                   |
| Vorbedingung     |                                                                                                                      |
| Input            | Ident-Karte<br>•                                                                                                     |

| Nutzerkennung des Ident-Auftraggebers (De-Mail-Adresse des<br>•<br>Nutzers)                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nutzerkennung des Empfängers (De-Mail-Adresse des SP)<br>•                                                                                            |
| Nutzerkennung des Ausstellers (De-Mail-Adresse des DMDA)<br>•                                                                                         |
| Authentisierungsniveau des Nutzers<br>•                                                                                                               |
| Ausstellungszeitpunkt (gesetzliche Zeit)<br>•                                                                                                         |
| Inhalte der Ident-Bestätigung erstellt                                                                                                                |
|                                                                                                                                                       |
| Anfrage an Account-Dienst (Attribute von Ident-Karte).<br>•                                                                                           |
| Identitätsdaten und deren Metadaten in die Ident-Bestätigung<br>•<br>einfügen.                                                                        |
| Nutzerkennung des Ident-Auftraggebers (De-Mail-Adresse des<br>•<br>Nutzers) in die Ident-Bestätigung einfügen.                                        |
| Nutzerkennung des Empfängers (De-Mail-Adresse des SP) in die<br>•<br>Ident-Bestätigung einfügen.                                                      |
| Nutzerkennung des Ausstellers (De-Mail-Adresse des DMDA) in<br>•<br>die Ident-Bestätigung einfügen.                                                   |
| Authentisierungsniveau des Nutzers in die Ident-Bestätigung<br>•<br>einfügen.                                                                         |
| Ausstellungszeitpunkt in die Ident-Bestätigung einfügen.<br>•                                                                                         |
| FC-01: Identitätsattribut für Nutzer nicht vorhanden                                                                                                  |
| Inhalt der Ident-Bestätigung als Meldung versenden                                                                                                    |
| Der ID erstellt eine Meldung an den Nutzer, der den Ident-Auftrag erstellt<br>hat. Die Meldung beinhaltet die Inhalte der späteren Ident-Bestätigung. |
| ID, Nutzer                                                                                                                                            |
| ID                                                                                                                                                    |
|                                                                                                                                                       |
| Inhalte der Ident-Bestätigung                                                                                                                         |
| Inhalt der Ident-Bestätigung zum Nutzer versendet                                                                                                     |
|                                                                                                                                                       |
| Meldung mit Informationen aus Schritt 7 erstellen<br>•                                                                                                |
| Meldung zum Nutzer senden<br>•                                                                                                                        |
| FC-01: Meldung wird nicht angenommen                                                                                                                  |
|                                                                                                                                                       |

*Tabelle 4: Schritte zum Prüfen eines Ident-Auftrages durch DMDA*

| Schritt 9        | Inhalt der Ident-Bestätigung empfangen                                                                                                                              |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Kurzbeschreibung | Der Nutzer empfängt den Inhalt der (späteren) Ident-Bestätigung.                                                                                                    |
| Akteure          | ID, Nutzer                                                                                                                                                          |
| Auslöser         | ID                                                                                                                                                                  |
| Vorbedingung     |                                                                                                                                                                     |
| Input            | Ident-Auftrag                                                                                                                                                       |
| Ergebnis         | Inhalt der Ident-Bestätigung vom ID empfangen                                                                                                                       |
| Nachbedingung    |                                                                                                                                                                     |
| Ablauf           | Inhalt der Ident-Bestätigung empfangen                                                                                                                              |
| Fehlerfälle      |                                                                                                                                                                     |
| Schritt 10       | Inhalt der Ident-Bestätigung prüfen                                                                                                                                 |
| Kurzbeschreibung | Der Nutzer prüft die Richtigkeit der Inhalte der späteren Ident-Bestätigung.<br>Im Anschluss an die Prüfung kann er den Ident-Auftrag bestätigen oder<br>abbrechen. |
| Akteure          | Nutzer                                                                                                                                                              |
| Auslöser         | Nutzer                                                                                                                                                              |
| Vorbedingung     |                                                                                                                                                                     |
| Input            | Inhalt der Ident-Bestätigung                                                                                                                                        |
| Ergebnis         | Ident-Auftrag geprüft                                                                                                                                               |
| Nachbedingung    |                                                                                                                                                                     |
| Ablauf           | Darstellung des Inhalts<br>•                                                                                                                                        |
|                  | Bestätigung oder Abbrechen des initiierten Ident-Auftrages<br>•                                                                                                     |
| Fehlerfälle      |                                                                                                                                                                     |
| Schritt 11       | Prüfergebnis senden                                                                                                                                                 |
| Kurzbeschreibung | Das Prüfergebnis des Nutzers wird zum ID gesendet.                                                                                                                  |
| Akteure          | Nutzer, ID                                                                                                                                                          |
| Auslöser         | Nutzer                                                                                                                                                              |
| Vorbedingung     |                                                                                                                                                                     |
| Input            | Prüfergebnis (Bestätigung oder Abbrechen)                                                                                                                           |
| Ergebnis         | Prüfergebnis zum ID versendet                                                                                                                                       |
| Nachbedingung    |                                                                                                                                                                     |
| Ablauf           | Prüfergebnis zum ID senden                                                                                                                                          |

#### **6.2.3 Inhalte der Ident-Bestätigung durch Nutzer prüfen**

| Fehlerfälle | FC-01: Prüfergebnis wird nicht angenommen |
|-------------|-------------------------------------------|
|             |                                           |

*Tabelle 5: Schritte zur Prüfung der Ident-Bestätigung durch den Nutzer*

#### **6.2.4 Ident-Bestätigung erstellen und versenden**

<span id="page-19-0"></span>

| Schritt 12       | Prüfergebnis empfangen                                                                     |
|------------------|--------------------------------------------------------------------------------------------|
| Kurzbeschreibung | Der ID empfängt das Prüfergebnis für den Ident-Auftrag.                                    |
| Akteure          | Nutzer, ID                                                                                 |
| Auslöser         | Nutzer                                                                                     |
| Vorbedingung     |                                                                                            |
| Input            | Prüfergebnis                                                                               |
| Ergebnis         | Prüfergebnis vom ID empfangen                                                              |
| Nachbedingung    | Wenn kein Prüfergebnis empfangen wurde: Schritt 14.                                        |
| Ablauf           | Prüfergebnis empfangen                                                                     |
| Fehlerfälle      |                                                                                            |
| Schritt 13       | Entscheidungsknoten: Prüfergebnis OK?                                                      |
| Kurzbeschreibung | Auswertung, ob der Nutzer den Ident-Auftrag bestätigt (ja) oder<br>abgebrochen (nein) hat. |
| ja               | Schritt 16                                                                                 |
| nein             | Schritt 14                                                                                 |
| Schritt 14       | Inhalt der Ident-Bestätigung verwerfen                                                     |
| Kurzbeschreibung | Der Inhalt der Ident-Bestätigung wird vom ID verworfen.                                    |
| Akteure          | ID                                                                                         |
| Auslöser         | ID                                                                                         |
| Vorbedingung     |                                                                                            |
| Input            | Inhalt der Ident-Bestätigung                                                               |
| Ergebnis         | Inhalt der Ident-Bestätigung gelöscht                                                      |
| Nachbedingung    |                                                                                            |
| Ablauf           | Löschen der Inhalte der Ident-Bestätigung                                                  |
| Fehlerfälle      |                                                                                            |
| Schritt 15       | Meldung mit Abbruch an Nutzer senden                                                       |
| Kurzbeschreibung | Der ID sendet eine Meldung an den Nutzer, dass der Ident-Auftrag<br>abgebrochen wurde.     |

<span id="page-20-0"></span>

| Akteure          | ID                                                                                                                                                           |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Auslöser         | ID                                                                                                                                                           |
| Vorbedingung     |                                                                                                                                                              |
|                  |                                                                                                                                                              |
| Input            |                                                                                                                                                              |
| Ergebnis         | Meldung an Nutzer gesendet                                                                                                                                   |
| Nachbedingung    | Stopp                                                                                                                                                        |
| Ablauf           | Meldung mit Abbruch an Nutzer senden                                                                                                                         |
| Fehlerfälle      | FC-01: Meldung konnte nicht abgesendet/dargestellt werden                                                                                                    |
| Schritt 16       | Ident-Bestätigung fertig stellen                                                                                                                             |
| Kurzbeschreibung | Die in Schritt 7 erstellen Inhalte werden zur Ident-Bestätigung<br>zusammengestellt und vom ID mit einer qualifizierten elektronischen<br>Signatur signiert. |
| Akteure          | ID                                                                                                                                                           |
| Auslöser         | ID                                                                                                                                                           |
| Vorbedingung     |                                                                                                                                                              |
| Input            | Inhalte der Ident-Bestätigung aus Schritt 7                                                                                                                  |
| Ergebnis         | Ident-Bestätigung fertig erstellt                                                                                                                            |
| Nachbedingung    |                                                                                                                                                              |
| Ablauf           | -<br>Inhalte der Ident-Bestätigung aus Schritt 7 in das Format für eine<br>Ident-Bestätigung strukturieren.                                                  |
|                  | -<br>Die Ident-Bestätigung mit einer qualifizierten elektronischen Signatur<br>versehen                                                                      |
| Fehlerfälle      |                                                                                                                                                              |
| Schritt 17       | Ident-Bestätigungsnachricht erstellen                                                                                                                        |
| Kurzbeschreibung | Der ID erstellt eine Ident-Bestätigungsnachricht.                                                                                                            |
| Akteure          | ID                                                                                                                                                           |
| Auslöser         | ID                                                                                                                                                           |
| Vorbedingung     |                                                                                                                                                              |
| Input            | Ident-Bestätigung<br>•                                                                                                                                       |
|                  | Nutzerkennung des Absenders (De-Mail-Adresse des DMDA)<br>•                                                                                                  |
|                  | Nutzerkennung des Empfängers SP (De-Mail-Adresse des SP)<br>•                                                                                                |
|                  | Nutzerkennung des Empfängers Nutzer (De-Mail-Adresse des<br>•<br>Nutzers)                                                                                    |
| Ergebnis         | Ident-Bestätigungsnachricht erstellt                                                                                                                         |

| Nachbedingung    |                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Ablauf           | Ident-Bestätigung in Ident-Bestätigungsnachricht einfügen<br>•                                                                             |
|                  | Nutzerkennung des Ausstellers als Absender-Adresse der Ident<br>•<br>Bestätigungsnachricht einfügen                                        |
|                  | Nutzerkennung des SP als Empfänger-Adresse der Ident<br>•<br>Bestätigungsnachricht einfügen                                                |
|                  | Nutzerkennung des Ident-Auftraggebers in Kopie (Carbon Copy,<br>•<br>CC) als Empfänger-Adresse der Ident-Bestätigungsnachricht<br>einfügen |
|                  | Versandoption "Persönlich" wählen<br>•                                                                                                     |
| Fehlerfälle      |                                                                                                                                            |
| Schritt 18       | Ident-Bestätigungsnachricht versenden                                                                                                      |
| Kurzbeschreibung | Der ID sendet die Ident-Bestätigungsnachricht über den PVD an den SP<br>und Nutzer.                                                        |
| Akteure          | ID, Postfachdienst des Ausstellers                                                                                                         |
| Auslöser         | ID                                                                                                                                         |
| Vorbedingung     | Sicheren Kanal mit PVD aufgebaut                                                                                                           |
| Input            | Ident-Bestätigungsnachricht                                                                                                                |
| Ergebnis         | Ident-Bestätigungsnachricht an SP und Nutzer gesendet                                                                                      |
| Nachbedingung    |                                                                                                                                            |
| Ablauf           | Ident-Bestätigungsnachricht über den PVD versenden                                                                                         |
| Fehlerfälle      | FC-01: Ident-Bestätigungsnachricht wurde nicht angenommen                                                                                  |

*Tabelle 6: Schritte zum Erstellen und Versenden der Ident-Bestätigung*

# <span id="page-22-0"></span>**7 Anhang**

#### <span id="page-22-1"></span>**7.1 Legende zum Aktivitätsdiagramm**

|                           | Startknoten                                                                                                                                                                                                                                                                                                                                                                                                                     |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Startknoten               | Der Startknoten ist der Startpunkt eines Prozesses. Ein Prozess<br>darf mehrere Startknoten haben, in diesem Fall beginnen beim<br>Start des Prozesses mehrere Abläufe. Es ist möglich, dass ein<br>Prozess keinen Startknoten besitzt, sondern von einem Ereignis<br>angestoßen wird.                                                                                                                                          |
| Endknoten                 | Endknoten                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                           | Der Endknoten gibt an, dass die Ausführung des Prozesses<br>abgeschlossen ist. Es kann in einem Prozessdiagramm mehrere<br>Ausgänge in Form dieser Endknoten geben. Gibt es zum<br>Zeitpunkt des Erreichens des Endknotens mehrere parallele<br>Abläufe innerhalb des Prozesses, werden beim Erreichen eines<br>Endknotens alle Abläufe gestoppt.                                                                               |
|                           | Ablaufende                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Stopp                     | Das Ablaufende terminiert einen Ablauf. Im Unterschied zum<br>Endknoten, der einen ganzen Prozess beendet, hat das Erreichen<br>des Ablaufendes keinen Effekt auf andere parallele Abläufe, die<br>zu diesem Zeitpunkt innerhalb des Prozesses abgearbeitet<br>werden. Auf diese Weise lassen sich parallele Abläufe gezielt<br>und einzeln beenden.                                                                            |
|                           | Kante                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                           | Die als Pfeile dargestellten Kanten verbinden die einzelnen<br>Komponenten des Diagramms und stellen den Kontrollfluss dar.                                                                                                                                                                                                                                                                                                     |
|                           | Aktion                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Aktion                    | Eine Aktion ist ein einzelner Schritt innerhalb eines Prozesses,<br>der nicht mehr weiter zerlegt wird. Das bedeutet nicht<br>unbedingt, dass die Aktion in der realen Welt nicht mehr weiter<br>zerlegbar wäre, sondern dass die Aktion in diesem Diagramm<br>nicht mehr weiter verfeinert wird. Die Aktion kann Ein- und<br>Ausgabeinformationen besitzen. Der Output einer Aktion kann<br>der Input einer Folge-Aktion sein. |
| Aufruf einer<br>Aktivität | Aufruf einer Aktivität                                                                                                                                                                                                                                                                                                                                                                                                          |
|                           | Mit diesem Symbol kann aus einer Aktivität (Prozess) heraus<br>eine weitere Aktivität aufgerufen werden. Der Aufruf selbst ist<br>eine Aktion, der aufgerufene Ablauf eine weitere Aktivität.                                                                                                                                                                                                                                   |

| Ereignis<br>empfangen | Empfang eines Ereignisses<br>Diese Aktion wartet auf das Eintreten eines Ereignisses. Nach<br>dem Empfang des Ereignisses wird der im Aktivitätsdiagramm<br>definierte, von dieser Aktion ausgehende Ablauf abgearbeitet.                                                                |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Signal senden         | Senden von Signalen<br>Das Senden von Signalen bedeutet, dass ein Signal an eine<br>empfangende Aktivität gesendet wird. Die empfangende<br>Aktivität nimmt das Signal mit der Aktion "Ereignis<br>empfangen" entgegen und kann entsprechend darauf reagieren.                           |
| Entscheidungsknoten   | Entscheidungsknoten<br>Die Raute stellt eine Verzweigung im Kontrollfluss dar. Eine<br>Verzweigung hat einen Eingang und zwei oder mehrere<br>Ausgänge. Jeder Ausgang wird mit einer Bedingung versehen.<br>Trifft eine Bedingung zu, wird am entsprechenden Ausgang<br>weiterverfahren. |
| Datenobjekt           | Datenobjekt<br>Datenobjekte gehören üblicherweise nicht zum Symbolumfang<br>in UML-Aktivitätsdiagrammen. Sie sind hier jedoch eingeführt<br>worden, um an entscheidender Stelle zu verdeutlichen, welche<br>Datenobjekte, insbesondere im Fokus der Schutzbedarfsanalyse,<br>vorliegen.  |

*Tabelle 7: Legende zum Aktivitätsdiagramm*

# **7.2 Legende zu Schritten der Ablaufbeschreibung**

Schritte im Aktivitätsdiagramm bezeichnen im Kontrollfluss eingebundene einmalig ablaufende Aktionen, wie z. B. einen vom Nutzer erstellten Ident-Auftrag zu prüfen ([Schritt 4](#page-15-0) in Abschnitt [4\)](#page-11-0).

| Schritt <Nr.>    | Eindeutiger Name der Aktion                                                                                                                                                                                                                                                                                                                                                   |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Kurzbeschreibung | Innerhalb der Kurzbeschreibung erfolgt eine verbale Beschreibung der<br>wesentlichen Funktionalität der Aktion.                                                                                                                                                                                                                                                               |
| Akteure          | Alle Rollen bzw. Dienste, die innerhalb der Aktion in irgendeiner Weise<br>beteiligt sind, werden aufgezählt.                                                                                                                                                                                                                                                                 |
| Auslöser         | Der Auslöser ist ein Akteur, durch den die Aktion aufgerufen bzw.<br>initialisiert wird.                                                                                                                                                                                                                                                                                      |
| Vorbedingung     | Unter Vorbedingungen werden die Bedingungen verstanden, die nicht aus<br>einer unmittelbar vorhergehenden Aktion folgen, sondern asynchron erzielt<br>werden müssen. Diese Aktivitäten sind nicht unbedingt in diesem Dokument<br>beschrieben, die Ergebnisse sind jedoch als Vorbedingungen für die<br>Ausführung der hier beschriebenen Aktion notwendig. Auf die Erfüllung |

Schritte werden in diesem Modul als Aktionen auf folgende Art und Weise beschrieben:

|  | 7 Anhang |
|--|----------|
|--|----------|

| Schritt <Nr.> | Eindeutiger Name der Aktion                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|               | dieser Vorbedingungen muss sich die nutzende Aktion verlassen können.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Input         | Der Auslöser muss bei Initialisierung der Aktion die entsprechenden<br>Informationen an diese übergeben oder durch die Aktion abfragen lassen, so<br>dass eine Verarbeitung der Informationen innerhalb der Aktion erfolgen<br>kann.                                                                                                                                                                                                                                                                                                                                              |
| Ergebnis      | Nach Beendigung der Aktion muss eine bestimmte Information als Resultat<br>erarbeitet bzw. bereitgestellt werden.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Nachbedingung | Unter Nachbedingungen werden Bedingungen verstanden, die innerhalb<br>dieser Aktion nicht betrachtet werden und durch unmittelbar nachfolgende<br>Aktionen aufgegriffen und dort behandelt werden müssen.                                                                                                                                                                                                                                                                                                                                                                         |
| Ablauf        | Für die innerhalb der Aktion definierte Logik wird ein konkreter Ablauf<br>beschrieben. Die definierte Abfolge muss innerhalb der Aktion durchgeführt<br>und abgeschlossen werden.                                                                                                                                                                                                                                                                                                                                                                                                |
| Fehlerfälle   | Als Fehlerfall wird ein Ergebnis einer Funktion bezeichnet, der innerhalb<br>der Funktionsspezifikation liegt, aber kein Standard-Ergebnis darstellt.                                                                                                                                                                                                                                                                                                                                                                                                                             |
|               | Die konkrete Behandlung eines Fehlerfalls ist implementierungsabhängig.<br>Je nach Fall können unterschiedliche Lösungsstrategien verwendet werden,<br>bspw. kann eine Aktion zu einem späteren Zeitpunkt wiederholt oder die<br>Aktion abgebrochen werden. Bei Abbruch einer Aktion ist der Nutzer<br>mindestens darüber zu informieren und alle bis zu diesem Schritt<br>generierten temporären Daten müssen gelöscht werden. In den<br>Beschreibungen der Fehlerfälle der Aktionen werden nur mögliche Fehler<br>beschrieben, die innerhalb der Funktionsspezifikation liegen. |

*Tabelle 8: Legende zu Schritten*
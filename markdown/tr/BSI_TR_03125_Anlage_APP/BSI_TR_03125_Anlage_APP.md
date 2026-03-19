
![](markdown/tr/BSI_TR_03125_Anlage_APP/BSI_TR_03125_Anlage_APP.pdf-0001-00.png)


Profilierung im Rahmen der BSI Technischen Richtlinie 03125 Beweiswerterhaltung kryptographisch signierter Dokumente 

## **Anlage TR-ESOR-Profil-APP: Appendix für TR-ESOR V1.2.1 und TR-ESOR V1.2.2 - Profilierung einiger TR-ESORAssessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

Bezeichnung Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung als Appendix für TR-ESOR V1.2.1 und TR-ESOR V1.2.2 Kürzel BSI TR-ESOR-APP Version 1.2.1 und 1.2.2 (auf Basis der eIDAS-Verordnung und ETSI Preservation Standards) Datum 01.04.2021 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

## **Inhaltsverzeichnis** 

|1.|Einführung ..................................................................................................................................... 6|
|---|---|
|2.|Übersicht........................................................................................................................................ 9|
|2.1|Nutzung eines zertifizierte TR-ESOR Produktes in Kombination mit einem Bewahrungsdienst|
||eines Preservation Service Provider (PSP) .................................................................................... 9|
|2.2|Nutzung eines zertifizierte TR-ESOR Produktes (V1.2.1 und V1.2.2) in Kombination mit einem|
||Bewahrungsdienst eines Preservation Service Provider (PSP) ..................................................... 9|
|2.3|Wesentlichen Ergänzungen in diesem Appendix .......................................................................... 9|
|3.|Appendix zum TR-ESOR Hauptdokument ................................................................................. 11|
|3.1|Ergänzung zu Kapitel “4.1 Bundesarchivgesetz und Landesarchivgesetze” ............................... 11|
|3.2|Ergänzung zu Kapitel 5 „Funktionen einer Middleware zum Beweiswerterhalt“ ....................... 11|
|3.3|Ergänzung zu Kapitel „5.1.1 Bewahrung kryptographisch signierter und unsignierter Daten“ .. 11|
|3.4|Änderung in Kapitel „Ändern von bereits archivierten Daten“ ................................................... 13|
|3.5|Ergänzung zu Kapitel „5.1.5 Löschen bewahrter Daten“ ............................................................ 13|
|3.6|Ergänzung zu Kapitel “6.1 Systemtechnische Anforderungen” .................................................. 13|
|3.7|Ergänzung zu Kapitel „ArchiSig-Modul (TR-ESOR-M.3)“ ....................................................... 14|
|3.8|Ergänzung zu Kapitel “8.2.3 Maßnahmen zum Schutz der Authentizität, Integrität und|
||Verbindlichkeit” .......................................................................................................................... 14|
|3.9|Ergänzung zu Kapitel “13 Quellenverzeichnis” .......................................................................... 15|
|3.10|Ergänzung zu Kapitel “4 Grundlegende Anforderungen und Parameter” ................................... 15|
|3.11|Ergänzung zu Kapitel “5.1.2 Validierung digitaler Signaturen” ................................................. 15|
|3.12|Zeitstempel .................................................................................................................................. 16|
|4.|Appendix zu TR-ESOR-M.3 ....................................................................................................... 17|
|4.1|Ergänzung des Titels von Kap. 2.5 „Vorgehensweise beim Import_von XAIPs mit_Evidence|
||Records“ ...................................................................................................................................... 17|
|4.2|Ergänzung zu Kap. 2.7: Details zum Export-Import Prozess von ECM/Langzeitspeicher-|
||Beständen .................................................................................................................................... 17|
|4.3|Ergänzung zu Kap. 3.1 „Grundlegender Aufbau und funktionale Abgrenzung“ ........................ 18|
|4.4|Ergänzung zu Kap.4.5 „Erzeugung initialer Archivzeitstempel“ ................................................ 18|
|4.5|Ergänzung zu Kap. 5.3: Überwachung der Gültigkeitszeiträume von Algorithmen ................... 19|
|5.|Appendix zu TR-ESOR-ERS ...................................................................................................... 20|
|5.1|Ergänzung zu Kapitel 5.1: Erstellung eines Evidence Records gem. Basis-ERS-Profil ............. 20|
|6.|Appendix zu TR-ESOR-E ........................................................................................................... 22|
|6.1|Ergänzung zu Kapitel 2: Überblick ............................................................................................. 22|
|6.2|Ergänzung zu Kapitel 3, Unterkapitel 3.6.1 ArchiveDataRequest .............................................. 23|
|6.3|Ergänzung zu Kapitel 4: Funktionen der Preservation-API gemäß ETSI TS 119 512 in der|
||Profilierung [TR-ESOR-TRANS] (ab TR-ESOR V1.2.2) .......................................................... 23|
|7.|Additional Test Cases for Conformity Level 1 – Functional Conformity ................................... 25|
|7.1|Additional Tests for all products ................................................................................................. 25|
|7.1.1|A-11 – What happens to the Data at the End of the Preservation Period shall be stated in the in|
||the Preservation Evidence Policy of the TR-ESOR Product-Manufacturer ................................ 25|
|7.1.2|A-12 – The TOT shall support at least one Preservation Profile, which is publicly published and|
||can be retrieved as described in the User Manual and Preservation Evidence Policy (PEP) of the|
||TOT (TR-ESOR Product) ............................................................................................................ 27|



Bundesamt für Sicherheit in der Informationstechnik 

3 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn Tel.: +49 228 99 9582-0 E-Mail: tresor@bsi.bund.de Internet: https://www.bsi.bund.de © Bundesamt für Sicherheit in der Informationstechnik 2021 

Bundesamt für Sicherheit in der Informationstechnik 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

|7.1.3 A-13 – Each installed Preservation Profile shall contain an identifier which uniquely identifies|7.1.3 A-13 – Each installed Preservation Profile shall contain an identifier which uniquely identifies|
|---|---|
|this Preservation Profile .............................................................................................................. 30||
|7.1.4 A-14 – The Preservation Evidence Policy of the TR-ESOR-Product Manufacturer shall contain||
|the description of how the preservation evidence is created including which cryptographic||
|algorithms are used. ..................................................................................................................... 31||
|7.1.5 A-15 – The Evaluation Report of the TR-ESOR-Product, written by the Testing Body, shall||
|contain|the digital fingerprints of the relevant Programs of the TR-ESOR-Product. .................. 32|
|7.2<br>Appendix to Module 2 – Crypto-Module .................................................................................... 33||
|7.2.1 M.2-05|– Support of Hash functions ........................................................................................... 33|
|7.2.2 M.2-11|– Suitability of cryptographic algorithms should be defined by User Manual and the|
|Preservation Evidence Policy (PEP) of the TR-ESOR-Product Manufacturer, based on the BSI-||
|[TR-ESOR-PEPT] ....................................................................................................................... 35||
|7.2.3 M.2-18|– Crypto-Module supports [RFC 3161], [RFC5816], [RFC5652] and [EN 319 422] and|
|suitable|algorithms ....................................................................................................................... 36|
|7.2.4 M.2-20|– Crypto-Module shall validate digital signatures of received electronic time-stamps or|
|hash values (or another cryptographic security element) in <asic:DataObjectReference> of a||
|LXAIP according to the signature validation policy ................................................................... 39||
|7.3<br>Appendix to Module 3 – ArchiSig Module ................................................................................. 42||
|7.3.1 M.3-04|– Creation of Initial Archive Timestamps according to [RFC4998] or [RFC6283] ....... 42|
|7.3.2 M.3-13– ArchiSig-Module supports Timestamp Renewal and Hash-Tree Renewal .................. 44||
|7.3.3 M.3-14|– Timestamp Renewal .................................................................................................... 48|
|7.3.4 M.3-15|– ArchiSig-Module shall validate requested electronic time-stamps ............................. 50|
|7.3.5 M.3-16|– Time-stamps shall be verified prior to renewal ........................................................... 53|
|7.3.6 M.3-23|– The Process of requesting Export-Import package(s) and the Production Methods of|
|the Export-Import Packages shall be stated in the User Manual and in the published TR-ESOR-||
|Product|Preservation Evidence Policy (PEP) of the TOT, based on the BSI-[TR-ESOR-PEPT],|
|and is allowed for authorized clients or preservation services (TR-ESOR Product) ................... 56||
|7.3.7 M.3-24|- How the Request for an Export-Import Package can be done with standardised|
|formats, shall be stated in the User Manual and in the published TR-ESOR-Product Preservation||
|Evidence Policy (PEP) of the TOT.............................................................................................. 59||
|7.3.8 M.3-25|– The TR-ESOR middleware shall keep records of all released export-import packages|
|and shall allow only authorized clients or preservation services to request export-import||
|packages ...................................................................................................................................... 61||
|7.4<br>Interface S4 .................................................................................................................................. 63||
|7.4.1 S.4.1-05 – 13 additional Test Steps to “Archive Submission includes the validation of||
|supplemental evidence data and evidence records validation and storage of results” ................. 63||
|8.<br>Generelle Änderung von TR-ESOR-C.1 V1.2.1 seit 30.7.2019 unabhängig davon, ob der||
|Einsatzes eines TR-ESOR-Produktes in einen Bewahrungsdienst gemäß [ETSI TS 119 511]||
|angestrebt wird und die Prüferleichterungen gemäß [ASS 119 511] in Anspruch genommen||
|werden|sollen ............................................................................................................................... 73|



## **Abbildungsverzeichnis** 

Abbildung 1: Schematische Darstellung der IT-Referenzarchitektur für TR-S.4.................................... 7 Abbildung 2: Schematische Darstellung der IT-Referenzarchitektur mit TR-S.512 (ab TR-ESOR V1.2.2) ..................................................................................................................................................... 7 

## **Tabellenverzeichnis** 

Tabelle 1: Aktuell zugelassene Hashalgorithmen für die Erzeugung technische Beweisdaten (Evidence Records) _(Stand Januar.2021)_ ............................................................................................................... 21 

Bundesamt für Sicherheit in der Informationstechnik 

4 

## **Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

Tabelle 2: Aktuell zusätzlich erforderliche Hashalgorithmen für die Verifikation eines Evidence Records _(Stand Januar 2021)_ ................................................................................................................ 21 

5 

Bundesamt für Sicherheit in der Informationstechnik 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

## **1. Einführung** 

Ziel der Technischen Richtlinie „Beweiswerterhaltung kryptographisch signierter Dokumente“ ist die Spezifikation sicherheitstechnischer Anforderungen für den langfristigen Beweiswerterhalt von kryptographisch signierten elektronischen Dokumenten und Daten nebst zugehörigen elektronischen Verwaltungsdaten (Metadaten). 

Eine für diese Zwecke definierte Middleware (TR-ESOR-Middleware) im Sinn dieser Richtlinie umfasst alle diejenigen Module ( **M** ) und Schnittstellen ( **S)** , die zur Sicherung und zum Erhalt der Authentizität und zum Nachweis der Integrität der aufbewahrten Dokumente und Daten eingesetzt werden. 

Die im Hauptdokument dieser Technischen Richtlinie vorgestellte Referenzarchitektur besteht aus den nachfolgend beschriebenen Schnittstellen, Funktionen und logischen Einheiten: 

- der S.4- oder **ab TR-ESOR V1.2.2** auch die TS119512-Schnittstelle S.512 in der Profilierung [TR-ESOR-TRANS] der TR-ESOR-Middleware, die dazu dient, die TRESOR-Middleware in die bestehende IT- und Infrastrukturlandschaft einzubetten; 

- dem „ArchiSafe-Modul“ ( **[TR-ESOR-M.1]** ), welches den Informationsfluss in der Middleware regelt, die Sicherheitsanforderungen an die Schnittstellen zu den ITAnwendungen umsetzt und für eine Entkopplung von Anwendungssystemen und ECM/Langzeitspeicher sorgt; 

- dem „Krypto“-Modul ( **[TR-ESOR-M.2]** ) nebst den zugehörigen Schnittstellen S.1 und S.3, das alle erforderlichen Funktionen zur Berechnung von Hashwerten, zur Prüfung elektronischer Signaturen bzw. Siegel bzw. Zeitstempel, zur Nachprüfung elektronischer Zertifikate und zum Einholen qualifizierter Zeitstempel sowie (optional) elektronischer Signaturen bzw. Siegel für die Middleware zur Verfügung stellt. Darüber hinaus kann es Funktionen zur Ver- und Entschlüsselung von Daten und Dokumenten zur Verfügung stellen; 

- dem „ArchiSig-Modul“ ( **[TR-ESOR-M.3]** ) mit der Schnittstelle S.6, das die erforderlichen Funktionen für die Beweiswerterhaltung der digital signierten Unterlagen bereitstellt; 

- einem ECM/Langzeitspeicher mit den Schnittstellen S.2 und S.5, der die physische Archivierung/Aufbewahrung und auch das Speichern der beweiswerterhaltenden Zusatzdaten übernimmt. _Dieser ECM/Langzeitspeicher ist nicht mehr direkt Teil der Technischen Richtlinie gleichwohl werden über die beiden Schnittstellen, die noch Teil der TR-ESOR-Middleware sind, Anforderungen daran gestellt._ 

_Ebenso wenig ist die Applikationsschicht, die auch einen XML-Adapter enthalten kann, direkter Teil der Technischen Richtlinie, auch wenn dieser XML-Adapter als Teil einer Middleware implementiert werden kann._ 

Die empfohlene IT-Referenzarchitektur ist in Abbildung 1 und Abbildung 2 dargestellt und besteht im Wesentlichen aus den in ( **[TR-ESOR]** , Kap. 7) grob beschriebenen logischen Komponenten und Schnittstellen. Diese werden in Anhängen zur TR weiter detailliert. Die Grafik zeigt zudem die externen Komponenten und Systeme an, die das Bild vervollständigen. Grundsätzlich wird als obere Schnittstelle der TR-ESOR-Middleware entweder die S.4-Schnittstelle gemäß **[TR-ESOR-E]** , die in Abbildung 1 dargestellt ist, oder **ab TR-ESOR v1.2.2** auch die S.512-Schnittstelle gemäß **[ETSI TS 119512]** in der Profilierung **[TR-ESOR-TRANS]** , die in Abbildung 2 gezeigt wird, unterstützt. 

6 

Bundesamt für Sicherheit in der Informationstechnik 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 


![](markdown/tr/BSI_TR_03125_Anlage_APP/BSI_TR_03125_Anlage_APP.pdf-0007-01.png)


**Abbildung 1: Schematische Darstellung der IT-Referenzarchitektur für TR-S.4** 


![](markdown/tr/BSI_TR_03125_Anlage_APP/BSI_TR_03125_Anlage_APP.pdf-0007-03.png)


**Abbildung 2: Schematische Darstellung der IT-Referenzarchitektur mit TR-S.512 (ab TR-ESOR V1.2.2)** 

Bundesamt für Sicherheit in der Informationstechnik 

7 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

Die in Abbildung 1 bzw. Abbildung 2 dargestellte IT-Referenzarchitektur orientiert sich an der ArchiSafe Referenzarchitektur und soll die logische (funktionale) Interoperabilität künftiger Produkte mit den Zielen und Anforderungen der Technischen Richtlinie ermöglichen und unterstützen. 

Sofern der optionale XML-Adapter und/oder der optionale TR-ESOR-512-Transformator[1] vorhanden sind, können beide in folgenden Ausprägungen vorliegen: 

- Jeweils eigenständige Komponente mit Schnittstellen zur Applikation sowie zum ArchiSafeModul 

- Jeweils eigenständige Komponente, jedoch Teil der Applikation mit Schnittstelle zum ArchiSafe-Modul 

- XML-Adapter und TR-ESOR-512-Transformator als eine gemeinsame Komponente, die beide Teile enthält mit Schnittstellen zur Applikation sowie zum ArchiSafe-Modul 

- XML-Adapter und TR-ESOR-512-Transformator als eine gemeinsame Komponente, die beide Teile enthält und Teil der Applikation ist, mit Schnittstelle zum ArchiSafe-Modul. 

Der Einsatz des TR-ESOR-512-Transformators wird EMPFOHLEN, sofern das TR-ESOR-Produkt mit einer TR-S.4-Schnittstelle in Europa zum Einsatz kommt und Interoperabilität mit europäischen (qualifizierten) Bewahrungsdiensten und Bewahrungsprodukten hergestellt werden soll. 

Diese Technische Richtlinie ist modular aufgebaut und spezifiziert in einzelnen Anlagen zum Hauptdokument die funktionalen und sicherheitstechnischen Anforderungen an die erforderlichen ITKomponenten und Schnittstellen der TR-ESOR-Middleware. Die Spezifikationen sind strikt plattform, produkt-, und herstellerunabhängig. 

Das vorliegende Dokument trägt die Bezeichnung „TR-ESOR-Appendix“ [ **TR-ESOR-APP]** und stellt eine Ergänzung für **[TR-ESOR(-C.1), V1.2.1][2]** und **[TR-ESOR(-C.1), V1.2.2]** dar, um die in **[TRESOR(-C.1), V1.2.1]** und **[TR-ESOR(-C.1), V1.2.2]** fehlenden, aber in **[TR-ESOR(-C.1) V1.3]** vorhandenen notwendigen zusätzlichen Anforderungen und Testfälle gemäß **[ETSI TS 119511]** für eine TR-ESOR-Zertifizierung **[TR-ESOR V1.2.1]** bzw. **[TR-ESOR V1.2.2]** bereitzustellen, so dass die Zertifizierungserleichterungen für einen Preservation Service (deutsch auch Bewahrungsdienst genannt) gemäß **[ASS 119 511]** in Anspruch genommen werden können. 

> 1 Siehe ETSI TS 119512 TR-ESOR Transformator unter einer Open Source Lizenz, ab TR-ESOR V1.2.2 

> 2 [TR-ESOR(-C.1)] bedeutet [TR-ESOR] bzw. [TR.ESOR-C.1] 

Bundesamt für Sicherheit in der Informationstechnik 

8 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

## **2. Übersicht** 

## **2.1 Nutzung eines zertifizierte TR-ESOR Produktes in Kombination mit einem Bewahrungsdienst eines Preservation Service Provider (PSP)** 

Falls der Preservation Service Provider ein zertifiziertes **TR-ESOR Produkt [TR-ESOR] der Version V1.2.1 oder höher** nutzt, 

- nachgewiesen durch einen entsprechenden aktuellen TR-ESOR-Prüfbericht und das TRESOR-Zertifizierungs-Test-Protokoll, 

- und dieses **[TR-ESOR] z** ertifizierte Produkt in der Tat für diesen Preservation Service produktiv eingesetzt wird, 

   - nachgewiesen z.B. durch Vergleich des digitalen Fingerabdrucks der relevanten ausführbaren Dateien, 

dann kann das Prüfergebnis der äquivalenten [ **ETSI TS 119 511]** – Testfälle durch die äquivalenten TR-ESOR-Zertifizierungs-Ergebnisse ersetzt werden und diese **[ETSI TS 119 511]** - Assessment Testschritte sind zu streichen. 

## **2.2 Nutzung eines zertifizierte TR-ESOR Produktes (V1.2.1 und V1.2.2) in Kombination mit einem Bewahrungsdienst eines Preservation Service Provider (PSP)** 

Eine TR-ESOR-Zertifizierung gemäß TR-ESOR V1.2.1 bzw. TR-ESOR V1.2.2 kann auch ohne diesen optionalen Appendix **[TR-ESOR-APP]** durchgeführt werden. 

Sofern aber ein Produktionseinsatz dieses TR-ESOR-Produktes in einen Bewahrungsdienst gemäß **[ETSI TS 119 511]** angestrebt wird und die Prüferleichterungen gemäß **[ASS 119 511]** in Anspruch genommen werden sollen, dann sollten die in diesem Anhang enthaltenden Anforderungen und Testfälle die in **[TR-ESOR-C.1, V1.2.1]** bzw. **[TR-ESOR-C.1, V1.2.2]** enthaltenden Anforderungen und Testfälle ersetzen, so dass 

- die Assessment-Testschritte von **[ETSI TS 119 511]** , die gemäß [ASS 119 511] äquivalent zu TR-ESOR (ab V1.2.1 und höher) -Testschritten sind, 

entfallen können. 

Dadurch wird bei der PSP-Zertifizierung eine vollumgängliche Verringerung der Testfälle erreicht, wie im Assessment Handbuch **[ASS 119 511]** dargestellt. 

Diese unter diesen Umständen erforderlichen Änderungen und Ergänzungen der TR-ESORAnforderungen und –Testfälle sind hier in der Kopie der ursprünglichen TR-ESOR-V1.2.1/V1.2.2Texte jeweils in „ **Fettdruck und kursiv** “ in den folgenden Kapiteln dargestellt. 

In TR-ESOR V1.3 sind die hier enthaltenden Anforderungen und Testfälle als reguläre Anforderungen und Testfälle enthalten. 

## **2.3 Wesentlichen Ergänzungen in diesem Appendix** 

Neben Ergänzungen in den TR-ESOR V1.2.1/V1.2.2-Texten **müssen** gemäß **[TR 119 511]** auch das aktuelle „ **Preservation Profile** “ gemäß **[ETSI TS 119 511, Anhang 6.4]** und **[ETSI TS 119 512, Anhang 5.4.7]** , die aktuelle und historische „ **Preservation Evidence Policies** “ **[ETSI TS 119 511, Anhang 6.5]** und die „ **Signature Validation Policy** “ **[ETSI TS 119 511, Anhang 6.6** ] be- 

Bundesamt für Sicherheit in der Informationstechnik 

9 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

reitgestellt werden. Das BSI stellt hierfür den TR-ESOR-Anhang [ **TR-ESOR-PEPT]: „Preservation Evidence Policy Template for TR-ESOR (PEPT)”** zur Verfügung. 

Bundesamt für Sicherheit in der Informationstechnik 

10 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

## **3. Appendix zum TR-ESOR Hauptdokument** 

Die Änderungen und Ergänzungen sind in den folgenden Kapiteln im Fettdruck, kursiv und größer dargestellt. 

## **3.1 Ergänzung zu Kapitel “4.1 Bundesarchivgesetz und Landesarchivgesetze”** 

Auf Basis von OVR-6.1-09: Hier wird lediglich eine zusätzliche Anforderungsnummer „(A4.1-1)“ eingeführt, damit diese Anforderung geeignet referenziert werden kann. Die ergänzte Textstelle sieht dann wie folgt aus: 

_**- „(A4.1 1) Alle öffentlichen Stellen des Bundes und der Länder sind gesetzlich verpflichtet, Unterlagen, die für die Aufgabenwahrnehmung nicht mehr benötigt werden, vor ihrer Vernichtung dem Bundes- bzw. Landesarchiv zur Übernahme als Archivgut des Bundes / des Landes anzubieten (vgl. §§ 3 und 5 [BArchG] und entsprechende Landesarchivgesetze). Diese Anbietungspflicht gilt selbstverständlich auch für elektronische Unterlagen.“**_ 

## **3.2 Ergänzung zu Kapitel 5 „Funktionen einer Middleware zum Beweiswerterhalt“** 

In Hinblick auf PRP-8.1-06 wird die Anforderung am Ende ergänzt. „ 

_**(A5.1-1)**_ Der Zugriff auf die TR-ESOR-Middleware bzw. den ECM/Langzeitspeicher zu Zwecken der Ablage, des Änderns, des Abrufs der Daten oder des Abrufs von technischen Beweisdaten _**oder der Bewahrungs-Profile oder Log-Daten**_ oder auch des Löschens abgelegter Dokumente und Daten muss in jedem Falle nachweisbar (z.B. protokolliert) über definierte Schnittstellen aus den vorgelagerten IT-Anwendungen erfolgen. Diese Aktionen/Vorgänge dürfen nur von dazu autorisierten (natürlichen oder juristischen) Personen vorgenommen werden. Unberechtigte Zugriffe sind zuverlässig zu verhindern. Die Nachweisführung muss in der Middleware an geeigneter Stelle, z.B. im ArchiSafe-Modul, erfolgen _**und kann im vorhandenen Berechtigungsfall für eine vorgegebene AOID zur Verfügung gestellt werden.“**_ 

## **3.3 Ergänzung zu Kapitel „5.1.1 Bewahrung kryptographisch signierter und unsignierter Daten“** 

Im folgenden Text wird ergänzt, welche binären Datentypen erlaubt sind mit näheren Informationen zu AOID (siehe PRP-8.1-05). 

**„(A5.1-3)** _**Die Ablagen der Dokumente und Daten müssen in einem Archivinformationspaket (AIP) als ein XML-basiertes Archivdatenobjekt (XAIP) gemäß ([TR-ESOR-F], Kap. 3.1) oder als ein logisches XAIP (LXAIP) gemäß ([TR-ESOR-F], Kapitel 3.2) oder als ein ASiC-AIP gemäß ([TRESOR-F], Kapitel 3.3) erfolgen. Dieses AIP muss grundsätzlich in der Lage sein, 1-n Dokumente und Daten aufzunehmen. Das XAIP-Format gemäß Kapitel 3.1 ist das Default-Format und muss in jedem Fall unterstützt werden können. Zusätzlich kann die Ablage als ein logisches XAIP (LXAIP)[3] gemäß ([TR-ESOR-F], Kap. 3.2, oder als ein ASiC-AIP gemäß ([TR-ESOR-F], Kap. 3.3) erfolgen. Nur für die in [TR-ESOR F, Hinweis 2], angegebenen binären Datentypen CAdES, XAdES, PAdES, ASiC-E und DigestList oder bei der Nutzung eines “Upload-Requests” zusammen mit einem LXAIP ist die Ablage der Daten außerhalb eines Archivinformationspakets (AIP) möglich. Bei der Ablage der Dokumente und Daten im ECM/Langzeitspeicher muss jedem**_ 

> 3   Eine Variante des XAIP, bei dem auf extern im ECM/Langzeitspeicher abgelegte Datenobjekte verwiesen werden kann. 

Bundesamt für Sicherheit in der Informationstechnik 

11 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

_**Archivdatenobjekt (z.B. für ein XML-basiertes Archivdatenobjekt (XAIP) gemäß ([TR-ESOR-F], Kap. 3.1) oder ein logisches XAIP (LXAIP) gemäß ([TR-ESOR-F], Kap. 3.2) oder ein ASiC-AIP gemäß ([TR-ESOR-F], Kap. 3.3)) ein eindeutiger und in der Regel unveränderbarer Bezeichner (Archivdatenobjekt ID, AOID) zugewiesen werden. Durch die Übergabe eines AOID-Elementes bei der Bewahrung kryptographisch signierter und unsignierter Daten kann die AOID von der aufrufenden Anwendung vergeben werden, wie z.B. im Fall eines LXAIP. Im Regelfall eines XAIP fehlt dieses Element und die AOID wird vom aufgerufenen Modul bereitgestellt. Die AOID dient der zuverlässigen Wiederauffindbarkeit der gespeicherten Dokumente und Daten und als Schlüssel für den autorisierten Zugriff auf die im ECM/Langzeitspeicher abgelegten Archivdatenobjekte.**_ “ 

In Bezug zu OVR-9.3-01 und OVR-9.3-02 wird hier wird lediglich die folgende Ergänzung vorgenommen: “according to the signature validation policy supported by the Preservation Profile”. 

**„(A5.1-5)** Für die Aufbewahrung kryptographisch signierter Daten muss die Middleware die Möglichkeit vorsehen, die digitalen Signaturen bzw. elektronischen Zeitstempel vor der Übergabe an den ECM/Langzeitspeicher umfassend sowohl auf Basis des Schalenmodells als auch des Kettenmodells _**gemäß den in dem Bewahrungs- Profil (engl. „Preservation Profile“) referenzierten Signaturbzw. Zeitstempel-Validierungs-Richtlinien (engl. „signature validation policy“ bzw. „time-stamp validation policy“)**_ zu prüfen oder bei einem (qualifizierten) Vertrauensdiensteanbieter prüfen zu lassen und die Prüfergebnisse gemeinsam mit den kryptographisch signierten Daten abzulegen. _**Im Fall, dass die Validierungsdaten der digitalen Signaturen bzw. Zeitstempel von der IT-Anwendung nicht übergeben wurden, muss die TR-ESOR-Middleware alle Anstrengungen unternehmen, die Validierungsdaten gemäß der Signatur- bzw. Zeitstempel-Validierungs-Richtlinien zu sammeln und zu prüfen. Wenn die Middleware nicht in der Lage ist, alle Validierungsdaten gemäß der der Signaturbzw. Zeitstempel-Validierungs-Richtlinien zu sammeln und zu verifizieren, dann muss die TRESOR-Middleware eine entsprechende verständliche Fehlermeldung an die IT-Anwendung zurückgegeben und diesen Fall als Fehlerfall behandeln. In jedem Fall ist es**_ für eine Weiterverarbeitung erforderlich, dass mindestens eines der beiden Validierungsmodelle (Schalenmodell bzw. Kettenmodell) erfolgreich ist. Schlägt die Prüfung für beide Validierungsmodelle (Schalenmodell bzw. Kettenmodell) fehl, soll, ggf. auf Basis von   konfigurierbaren Optionen, wie folgt vorgegangen werden: 

- a. Im Fall XAIP oder ASiC-AIP: ArchiSafe **[TR-ESOR-M.1]** liefert eine verständliche Fehlermeldung an die Anwendung zurück und lehnt die Aufbewahrung des Objekts ab. 

- **b.** Im Fall LXAIP: Die entsprechende Fehlermeldung kommt zusammen mit allen anderen ggf. vorhandenen Prüfinformationen in die Credential-Section. Das Objekt wird danach im ECM/Langzeitspeicher abgelegt. Zusätzlich wird eine Fehlermeldung an die IT-Anwendung oder den XML-Adapter gegeben.[4] 

- _**c.**_ Im Fall eines logischen XAIP (LXAIP) ist stets der vorstehende Fall b) anzuwenden. Auf Basis von konfigurierbaren Optionen _**soll**_ die IT-Anwendung oder der XML-Adapter nach Empfang der Fehlermeldung das LXAIP und die dazugehörigen Datenobjekte im ECM/Langzeitspeicher löschen. _**Es wird empfohlen, die Datenobjekte, deren Signaturprüfung fehlschlägt, durch die Anwendung in ein dezidiertes Fehlerverzeichnis auszugeben und zu analysieren. Für nicht mehr prüfbare digitale Signaturen und Zeitstempel wird die Ablage dieser Objekte (geschützt oder nicht geschützt) in der MetaDataSection empfohlen.**_ 

> 4 Wenn mindestens eine Signaturprüfung fehlschlägt dann ist es nicht mehr „…/resultmajor#ok“. Wenn mindestens Ketteoder Schalenprüfung einer Signatur nicht fehlschlägt, sollte „…/resultmajor#warning“ und „…/resultminor/arl/XAIP_NOK_SIG“ zurückgeliefert werden. Im anderen Fall „../resultmajor#error“. 

Bundesamt für Sicherheit in der Informationstechnik 

12 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

## **3.4 Änderung in Kapitel „Ändern von bereits archivierten Daten“** 

Das Wort „soll“ wird durch „müssen ersetzt: 

„ **(A5.1-17) S** ämtliche Änderungen _**müssen**_ nachvollziehbar protokolliert werden. Soweit als möglich ist der Zeitpunkt der Änderung, der Urheber und der Inhalt der Änderung zu protokollieren.“ 

## **3.5 Ergänzung zu Kapitel „5.1.5 Löschen bewahrter Daten“** 

Gemäß _**OVR-6.1-09**_ ist es erforderlich, zu erklären, was mit den bewahrten Archivdatenobjekten nach Ablauf der Aufbewahrungspflicht passiert. 

_**„(A5.1-29)**_ Das Löschen von Daten und Dokumenten **nach Ablauf** des gesetzlich vorgeschriebenen Aufbewahrungszeitraums kann durch organisatorisch berechtigte Nutzer einer technisch berechtigten vorgelagerten IT-Anwendung angestoßen werden, oder durch einen zentralen Prozess, der diese Funktion für _**den gesamten ECM/Langzeitspeicher ausführt und entsprechend berechtigt ist. In jedem Fall muss die Middleware den Ablauf von Aufbewahrungsfristen sowie den Umgang mit den Archivdatenobjekten nach Ablauf der Aufbewahrungsfrist überwachen und dies entsprechend in der Preservation Evidence Policy des Herstellers dokumentieren.“**_ 

## **3.6 Ergänzung zu Kapitel “6.1 Systemtechnische Anforderungen”** 

Gemäß **[ETSI TS 119 511]** und **[ETSI TS 119 512]** ist es erforderlich, ein aktuelles „Preservation Profile“ gemäß **[ETSI TS 119 511, Anhang 6.4]** und **[ETSI TS 119 512, Anhang 5.4.7]** sowie eine „Preservation Evidence Policy“ gemäß **[ETSI TS 119 512, Anhang 6.5]** zu veröffentlichen. 

Siehe auch OVR-6.4-01, OVR-6.4-04a), PRP-8.1-04 und PRP-8.1-05, OVR-6.5-03, OVR-7.14-01, OVR-7.14-02, OVR-7.15-03. 

Hier werden die nachfolgenden drei neuen Anforderungen (A6.1-6), (A6.1-7), (A6.1-8) an das Ende des Kapitels 6.1 im Hauptdokument eingefügt **.** Die drei ergänzten Textstellen sehen dann wie folgt aus: 

_**„(A6.1-6) Die TR-ESOR-Middleware muss mindestens ein aktuelles „Preservation Profile“ gemäß [ETSI TS 119 512, Anhang 5.4.7] unterstützen und die vorausgegangenen „Preservation Profile“ gemäß [ETSI TS 119 512, Anhang 5.4.7] referenzieren. Diese „Preservation Profile“, aufgebaut auf Basis des BSI TR-ESOR „Preservation Profile-Templates“ (PEPT), müssen als öffentliche Dokumente auf der Webseite des TR-ESOR-Produkt-Herstellers und in der veröffentlichten Preservation Evidence Policy (PEP) des entsprechenden TR-ESOR-Produkts des TR-ESOR-ProduktHerstellers zu finden sein. Jedes Preservation Profile muss einen eindeutigen Identifikator enthalten.“**_ 

_**„(A6.1-7) Die TR-ESOR-Middleware muss mindestens eine „Preservation Evidence Policy“ (PEP) gemäß [ETSI TS 119 511, Anhang 6.5], aufbauend auf dem „Preservation Evidence Policy Template“ (PEPT) des BSI, unterstützen, die im „Preservation Profile“ des TR-ESOR-Produkt-Herstellers referenziert und auf der Webseite des TR-ESOR-Produkt-Herstellers veröffentlicht ist. Die „Preservation Evidence Policy“ muss die Beschreibung, wie der „Preservation Evidence“ erzeugt wird, und welcher kryptographische Algorithmus dabei verwendet werden, enthalten**_ . _**“**_ 

Bundesamt für Sicherheit in der Informationstechnik 

13 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

_**- „(A6.1 8) Falls einer der Algorithmen oder Parameter, die im „Preservation Evidence“ genutzt werden, droht, seine Sicherheitseignung zu verlieren oder ein relevantes Zertifikat droht, seine Gültigkeit zu verlieren, dann muss der „Preservation Evidence“ durch die TR-ESOR-Middleware gemäß einer neuen „Preservation Evidence Policy“ während der Aufbewahrungszeit „augmentiert“ werden. Diese neue „Preservation Evidence Policy“ muss für zukünftige Aufnahmen von neu zu speichernden Archivdatenobjekte vorher vom TR-ESOR-Produkt Herstellers erstellt und veröffentlicht worden sein und dann vom Bewahrungsdienst (engl. Preservation Service Provider (PSP)) im “ “ „Preservation Service Practice Statement (PSPS) neu eingefügt werden**_ . 

_**„(A6.1-9) Das Monitoring der verwendeten kryptographischen Algorithmen sollte auf Basis eines elektronischen Algorithmenkatalogs gemäß [TS119312] und [SOGIS] automatisch vorgenommen werden.“**_ 

## **3.7 Ergänzung zu Kapitel „ArchiSig-Modul (TR-ESOR-M.3)“** 

Eine neue Anforderung 

_**„(A7.4-13) Für die Aufbewahrung der Archivdatenobjekte und der kryptographischen Beweisdaten muss das ArchiSig-Modul über eine (oder mehrere) sichere und performante Schnittstelle(n) TRS.2 zu einem (oder mehreren) vertrauenswürdigen elektronischen ECM/Langzeitspeicher(n) verfügen.“**_ 

_**„ (A7.4-14) Für die Erzeugung von Hashwerten und die Anforderung, den Abruf und die Verifikation von qualifizierten Zeitstempeln muss das ArchiSig-Modul über eine sichere und performante Schnittstelle TR-S.3[5] auf ein kryptographisches Modul zugreifen können, das mindestens die in der Anlage [TR-ESOR-M.2] dieser TR beschriebenen obligatorischen Anforderungen erfüllt.**_ 

## **3.8 Ergänzung zu Kapitel “8.2.3 Maßnahmen zum Schutz der Authentizität, Integrität und Verbindlichkeit”** 

Gemäß **[ETSI TS 119 511]** ist es erforderlich, OVR-9.3-03 zu erfüllen: _“[PDS] To extend the ability to validate a digital signature and to maintain its validity status, the preservation service shall, at the minimum, provide a proof of existence of the signature and of the validation data needed to validate the signature using digital signature techniques (digital signatures, time-stamps, evidence records).”_ 

Hier wird daher die nachfolgende Anforderung (A8.2-1) entsprechend ergänzt. (A8.2-1) sieht dann wie folgt aus: 

> 5 Um einen performanten Umgang mit der Hashwertberechnung innerhalb des ArchiSig-Moduls zu ermöglichen, ist es durchaus möglich, das dafür vorgesehene Krypto-Modul über ein alternatives Binding der Schnittstelle mit dem ArchiSig-Modul zu verbinden. So könnte beispielweise durch die Verwendung eines direkten JavaBinding der Overhead der SOAP-basierten Remote-Kommunikation zwischen den ArchiSig- und KryptoModulen entfallen. Eine solche Konstellation hätte zur Folge, dass es sich innerhalb der Middleware mehr als eine Instanz (hier genau 2) des (gleichen) Krypto-Moduls befinden würden: 

1. Eine Instanz für die alleinige Benutzung durch das ArchiSig für die Berechnung der Hashwerte, angesprochen über die direkte Java Schnittstelle (In-Proc-Binding) 

2. Eine zweite Instanz für die sonstigen Aufgaben des Krypto-Moduls, erreichbar wie gewöhnlich durch einen entfernten Aufruf der SOAP-basierten Schnittstelle (HTTPS-SOAP-Binding). 

Bundesamt für Sicherheit in der Informationstechnik 

14 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

_**„(A8.2-1)**_ Um die langfristige Nachprüfbarkeit der digitalen Signaturen bzw. elektronische Zeitstempel zu gewährleisten, müssen die digitalen Signaturen bzw. elektronischen Zeitstempeln und Signaturbzw. Siegel- bzw. Zeitstempelprüfdaten (Zertifikate und Statusabfragen/-informationen) in standardisierten Datenformaten abgelegt werden. Details dazu finden sich in [TR-ESOR-F] bzw. [TR-ESORERS]. _**Um die langfristige Nachprüfbarkeit digitaler Signaturen und deren Gültigkeitsstatus sowie der signierten Daten zu erhalten, muss die TR-ESOR-Middleware einen Existenzbeweis dieser digitalen Signaturen und deren Prüfdaten, die für eine Prüfung der Signaturen erforderlich sind, sowie der signierten Daten unter Verwendung von Evidence Records gemäß (A8.2-5)erzeugen.“**_ 

## **3.9 Ergänzung zu Kapitel “13 Quellenverzeichnis”** 

Die folgenden Referenzen werden für [TR-ESOR], V1.2.1 und V1.2.2 ergänzt: 

- [TR-ESOR-APP] Profilierungen im Rahmen der BSI Technischen Richtlinie 03125 Beweiswerterhaltung kryptographisch signierter Dokumente _, Anlage TR-ESOR-Profile-APP: Appendix für TRESOR V1.2.1 und TR-ESOR V1.2.2 – Profilierung einiger Assessment-Kriterien auf Basis von ETSI TS 119 511,_ V1.2.1 und V1.2.2 

- [TR-ESOR-PEPT] BSI TR 03125: Preservation of Evidence of Cryptographically Signed Documents: _Annex TR-ESOR-PEPT: Preservation Evidence Policy Template,_ V1.2.1 and higher 

- [TR-ESOR-TRANS] BSI TR 03125 Beweiswerterhaltung kryptographisch signierter Dokumente _, Appendix zu Anlage TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-APIFrameworks – Grobkonzept ETSI TS119512 TR-ESOR Transformator,_ V1.2.1 und V1.2.2Appendix zu TR-ESOR-M.2 

## **3.10 Ergänzung zu Kapitel “4 Grundlegende Anforderungen und Parameter”** 

Hier wird eine zusätzliche Anforderungsnummer „(A4.1-1)“ eingeführt, damit diese Anforderung geeignet referenziert werden kann und der Absatz leicht überarbeitet. Siehe auch OVR-6.5-03, OVR6.5-04, OVR-7.14-03. Die ergänzte Textstelle sieht dann wie folgt aus. 

_**„(A4.0-1)**_ Diese Vorgaben _**gemäß [ETSI TS 119 312][6] und [SOG-IS][7]**_ sind für das Krypto-Modul verbindlich und müssen stets den aktuellen Empfehlungen gemäß **[ETSI TS 119 312]** und **[SOG-IS]** folgend angepasst werden. Weiterhin _**müssen**_ die allgemeinen Empfehlungen des BSI hinsichtlich der Sicherheitseignung kryptographischer Funktionen _**beachtet werden**_ ( **[TR-02102]** : Kryptographische Verfahren: Empfehlungen und Schlüssellängen). Auch hier _**muss**_ das Krypto-Modul an aktualisierte Empfehlungen laufend _**angepasst werden**_ .“ 

## **3.11 Ergänzung zu Kapitel “5.1.2 Validierung digitaler Signaturen”** 

Gemäß **[ETSI TS 119 511, Kap. 6-6]** wird die folgende Ergänzung eingefügt: **”** gemäß der in dem Bewahrungs-Profil (engl. Preservation profile) referenzierten „signature validation policy“ erfolgen und **”** 

**„(A5.1-10)** Diese Funktion muss selbst prüfen können oder durch den beauftragten Vertrauensdiensteanbieter prüfen lassen, ob das für die Erstellung der digitalen Signatur verwendete Nutzer-Zertifikat zum Zeitpunkt der Signatur- bzw. Siegelerstellung gültig war (vgl. Kapitel 5.1.3 und **[eIDAS-VO, Artikel 32 bzw. 40]** ) sowie ob die durch den Aussteller der Zertifikats gesetzte Signatur  bzw. das Siegel gültig ist und ob Zertifikatserweiterungen gemäß **[eIDAS-VO, Artikel 28 bzw. 38 Absatz 3]** 

- 6     ETSI TS 119 312:  "ETSI: Electronic Signatures and Infrastructures (ESI); Cryptographic Suites" 

- 7 SOG-IS Crypto Working Group: "SOG-IS Crypto Evaluation Scheme – Agreed Cryptographic Mechanisms", 2016, https://www.sogis.org/uk/supporting_doc_en.html 

15 

Bundesamt für Sicherheit in der Informationstechnik 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

und der Verwendungszweck des Zertifikates richtig gesetzt wurden. Die Gültigkeitsprüfung muss _**gemäß der in dem Bewahrungs-Profil (engl. Preservation profile) referenzierten „signature validation policy“ erfolgen und**_ vollständig sein, d. h. die gesamte Zertifikatskette bis hin zu einem vertrauenswürdigen Wurzel-Zertifikat umfassen. Diese Funktion des Krypto-Moduls muss bei der Prüfung ermittelte oder erhaltene zusätzliche Prüfinformationen an das aufrufende Modul zurückgeben. Diese hierbei ermittelten Prüfinformationen (Zertifikate, Sperrlisten, OCSP-Responses) sind im Archivdatenobjekt zu ergänzen oder als Prüfbericht gemäß **[OASIS-VR]** bzw. **[TR-ESOR-VR]** zurückzugeben.“ Siehe auch OVR-9.3-01. 

Eine zusätzliche Anforderung bzgl. des LXAIP: 

_**„(A5.1-14) Im Falle eines LXAIP muss das Krypto-Modul über geeignete Funktionen verfügen, die im LXAIP gem. [TR-ESOR F] enthaltenen Verweise auf die extern im ECM/Langzeitspeicher abgelegten Inhaltsdaten aufzulösen und so die Signaturprüfung vornehmen zu können. Dabei muss das Krypto-Modul über eine sichere und performante Schnittstelle auf den ECM/Langzeitspeicher zugreifen, um die signierten/gesiegelten/zeitgestempelten Daten zur Prüfung der kryptographischen Signaturen/Siegel/Zeitstempel gemäß Kap. 5.1.2, 5.1.3, 5.4.2 bzw. 5.2 abzurufen und den Hashwert bzw. das kryptographischen Sicherungsmittels in der <asic:DataObjectReference> zu prüfen.“**_ 

Zusätzlich die Angabe eines “Reason Codes” im Fall einer „Public Key Certificate“-Sperrung erforderlich: 

**„(A5.1-17)** Die Validierung der Zertifikatsgültigkeit muss auf der Basis eines Standardprotokolls erfolgen. Empfohlen wird das Protokoll: 

- OCSP – Online Certificate Status Protocol ( **[RFC6960],** vormals **[RFC2560]** ) _**mit Angabe eines “Reason Codes” im Fall einer „Public Key Certificate“-Sperrung:…**_ “ 

Siehe auch OVR-7.5-03. 

## **3.12 Zeitstempel** 

_**„(A5.4-1)**_ Das Krypto-Modul muss über eine Funktion zur Abfrage eines qualifizierten Zeitstempels verfügen. Falls die Abfrage bei einem qualifizierten Vertrauensdiensteanbieter erfolgt, muss dieser mindestens die Anforderungen nach den **[eIDAS-VO, Artikel 24],** erfüllen, in der Vertrauensliste der Europäischen Kommission gemäß Kapitel 3.3 mit dem Status „ **granted** “ gelistet sein und qualifizierte Zeitstempel gemäß **[eIDAS-VO, Artikel 42]** erzeugen. _**Darüber hinaus soll dieser qualifizierter Vertrauensdiensteanbieter konform zu ETSI EN 319 421 sein.“**_ 

Siehe auch OVR-7.5-02. 

16 

Bundesamt für Sicherheit in der Informationstechnik 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

## **4. Appendix zu TR-ESOR-M.3** 

## **4.1 Ergänzung des Titels von Kap. 2.5 „Vorgehensweise beim Import** _**von XAIPs mit**_ **Evidence Records“** 

Ergänzung: „ _**von XAIPs mit**_ ..“ 

Siehe dazu OVR-7.16-01. 

## **4.2 Ergänzung zu Kap. 2.7: Details zum Export-Import Prozess von ECM/Langzeitspeicher-Beständen** 

„ _**Im Fall einer TR-ESOR-Middleware, kombiniert mit einem ECM/Langzeitspeicher, wie in Abbildung 1 bzw. Abbildung 2 beschrieben, ist es eine wichtige Anforderung bzgl. der Interoperabilität, dass es möglich sein muss, den gesamten Datenbestand von einem Bewahrungsdienst exportieren und zu einem anderen anschließend importieren zu können.**_ 

_**Für diesen Zweck muss mindestens ein der folgenden Ansätze verfolgt werden:**_ 

- _**Mindestanforderung: Ansatz 1: Anwendung der im Kap. 2.6 dargestellten generischen Methode für die Migration der bewahrten Bestände,**_ 

- _**Optional: Ansatz 2: Export-Import der (L)XAIPs mit den dort eingebetteten reduzierten Evidence Records gemäß der Beschreibung aus dem Kap. 2.5.**_ 

_**Da Evidence Records gemäß [RFC 4998] oder [RFC 6283] nur reduzierte Hash-Bäume enthalten, die nur den Teil des Hash-Baums enthalten, der relevant ist für ein(e) spezifisches (spezifische) (Menge von) Archivdatenobjekt(en), können die konventionellen Funktionen**_ _**`ArchiveRetrieval` gemäß [TR-ESOR-E] für den Export von Archivdatenobjekten und**_ _**`ArchiveSubmission` für den Import von Archivdatenobjekts gemäß [TR-EOSR-M.3, Kap. 2.5] nicht immer für die Migration des gesamten Datenbestandes von einem Bewahrungsdienst zu einem anderen optimal geeignet sein. In solchem Fall kann der Ansatz 1 seine Anwendung finden.**_ 

_**Bezüglich des Prozesses und der Anfrage von “Export-Import Paketen” gelten die folgenden Anforderungen:**_ “ 

Siehe auch OVR-6.1-07, OVR-7.16-01, OVR-6.1-08, OVR-7.16-02. 

Daher werden bezüglich des Prozesses und der Anfrage von “Export-Import Paketen” die folgenden Anforderungen eingefügt: 

_**„(A2.7-1) Die TR-ESOR-Middleware muss eine der zwei folgenden Prozess-Alternativen für die Anfrage von einem (oder mehreren) „Export-Import-Paket(en)“ mit dem (den) Archivdatenobjekt(en) mit den beweisrelevanten Daten und technischen Beweisdaten auf Basis des Ansatzes 1 unterstützen:**_ 

   - _**a) Alternative 1a gemäß [TR-ESOR-E], Kap. 3: unter Verwendung der standardisierten Funktionen**_ _**`ArchiveRetrieval` und**_ _**`ArchiveEvidence` für den Export der Archivdatenobjekte und korrespondierenden Beweisdaten (Evidence Records),**_ _**`Verify` für die Ermittlung der Prüfprotokolle für die Beweisdaten und**_ _**`ArchiveSubmission` sowie**_ _**`ArchiveUpdate` für den Import der Daten in das Zielsystem,**_ 

   - _**b) Alternative 1b gemäß [TR-ESOR-E], Kap. 4: unter der Verwendung der standardisierten Funktionen**_ _**`RetrievePO` für den Export der Archivdatenobjekte und zugehörigen Beweisdaten,**_ _**`ValidateEvidence` für die Ermittlung der Prüfprotokolle und**_ _**`PreservePO` für den Import der Archivdatenobjekte samt Beweisdaten und Prüfprotokolle in das Zielsystem,**_ 

- _**,oder eine der zwei folgenden Prozess-Alternativen im Falle der Wahl des Ansatzes 2 verfolgen:**_ 

   - _**c) Alternative 2a gemäß [TR-ESOR-E], Kap. 3: die standardisierten Funktionen**_ _**`ArchiveRetrieval` (inklusive Evidence Records) für den Export von Archivdatenobjekten und**_ _**`Ar-`**_ 

Bundesamt für Sicherheit in der Informationstechnik 

17 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

   - _**`chiveSubmission` mit Evidence Records für den Import von den Archivdatenobjekten gemäß [TR-EOSR-M.3, Kap. 2.5],**_ 

- _**d) Alternative 2b gemäß [TR-ESOR-E], Kap. 4: die standardisierten Funktionen**_ _**`RetrievePO` für den Export von Archivdatenobjekten und**_ _**`PreservePO` für den Import von den Archivdatenobjekten gemäß [TR-ESOR-M.3], Kap. 2.5“**_ 

_**„(A2.7-2) Die TR-ESOR-Middleware muss den Ansatz 1 gemäß [TR-ESOR-M.3], Kap. 2.6 für das Erzeugen des (der) Export-Import-Pakets(e) im produktiven Betrieb wie folgt unterstützten:**_ 

- _**a) Die TR-ESOR-Produkt-Hersteller müssen den Ansatz 1 unterstützen und dabei entscheiden, ob sie Alternative 1a oder Alternative 1b unterstützen. Zusätzlich können die TRESOR-Produkt-Hersteller auch Ansatz 2 mit entweder Alternative 2a oder Alternative 2b unterstützen. Das Ergebnis ihrer Entscheidungen müssen die TR-ESOR-Produkt-Hersteller in ihre aktuelle „Preservation Evidence Policy“ (PEP) übernehmen und diese PEP veröffentlichen.**_ 

- _b)_ _**Die Datenformate des ganzen Export-Import Datenbestandes muss eine Menge von XAIPs mit reduzierten EvidenceRecords gemäß [TR-ESOR-F] sein.**_ 

- _c)_ _**Die TR-ESOR-Produkt-Hersteller müssen das Datenformat des Export-ImportDatenbestandes in ihre aktuelle „Preservation Evidence Policy“ (PEP) übernehmen und diese PEP veröffentlichen.**_ 

- d) _**Falls der „Preservation Service Provider“ (PSP) im Rahmen seines Produktionseinsatzes eines TR-ESOR-Produktes die Erleichterungen gemäß [ASS 119 511] im Rahmen seiner Bewahrungs-Konformitätsprüfung in Anspruch nehmen will, so muss er das ergänzte PEP seines TR-ESOR-Produktherstellers vervollständigen, in sein „Preservation Service Practice Statement“ (PSPS) einfügen und sein PSPS sowie sein PEP veröffentlichen. Der PSP muss den Inhalt dieses PSP in eigene allgemeine Geschäftsbedingungen aufnehmen.**_ “ 

_**„(A2.7-3) Die TR-ESOR-Middleware muss Log-Daten über alle ausgelieferten Export-Import Pakete speichern, inklusive Information über das Datum der Auslieferung und die Kriterien, auf dessen Basis die Menge der Bewahrungs-Objekte ausgewählt wurden, die in das Export-Import-Paket eingefügt wurden.“**_ 

## **4.3 Ergänzung zu Kap. 3.1 „Grundlegender Aufbau und funktionale Abgrenzung“** 

**„(A3.1-6)** _**Das ArchiSig-Modul muss eine sichere Datenablage, das Teil des ArchiSig-Moduls ist oder zum ArchiSig-Modul allokiert ist, zur Aufnahme der Archivzeitstempel und der Archivdatenobjekt ID gewährleisten (siehe Hauptdokument, Kapitel 7.1) in so einer Art und Weise, dass bzgl. der Hashbäume ein Hashwert zugehörig zu einem**_ _**`AOID` und, falls anwendbar, zu einer**_ _**`VersionID` mit absoluter Sicherheit zu jedem Zeitpunkt identifiziert werden kann.“**_ 

## **4.4 Ergänzung zu Kap.4.5 „Erzeugung initialer Archivzeitstempel“** 

Gemäß **[TS 119 511, Kap. 9.3, OVR-9.3-03]** gilt: _„[PDS] To extend the ability to validate a digital signature and to maintain its validity status, the preservation service shall, at the minimum, provide a_ 

Bundesamt für Sicherheit in der Informationstechnik 

18 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

_proof of existence of the signature and of the validation data needed to validate the signature using digital signature techniques (digital signatures, time-stamps, evidence records)_ **“.** 

Daher wir die Anforderung wie folgt ergänzt. 

**„(A4.5-3** ) Der Zeitstempel muss sämtliche Informationen tragen, die für eine Gültigkeitsprüfung des Zeitstempels einschließlich der darin enthaltenen _**digitalen Signatur erforderlich sind. Zusätzlich muss im Fall von signierten Daten in (L)XAIP sichergestellt sein, dass mindestens die digitale Signatur selbst und ihre Validierungsdaten, die notwendig sind, um die digitale Signatur zu prüfen, auch durch den Evidence Record geschützt werden**_ .“ 

Siehe auch OVR-9.3-04. 

**„(A4.5-5)** Es wird empfohlen, die Erstellung eines initialen Archivzeitstempels über neu archivierte Archivdatenobjekte bzw. (L)XAIP-Versionen wenigstens einmal pro Tag automatisch durch das ArchiSig-Modul auszuführen. _**Darüber hinaus wird empfohlen, die Evidence Records der neu archivierten Archivdatenobjekte zeitnah in dem dafür vorgesehenen Feld, z.B. in der Credential Section des korrespondierenden Archivdatenobjekts (L)XAIP, abzulegen [TR-ESOR-F].“**_ 

## **4.5 Ergänzung zu Kap. 5.3: Überwachung der Gültigkeitszeiträume von Algorithmen** 

Gemäß OVR-7.14-03: Ersetzen „oder“ durch „und“ in (A5.3-1) 

„(A5.3-1) Die Gültigkeitszeiträume von verwendeten Algorithmen und Parametern müssen überwacht und im ArchiSig-Modul verwaltet werden. Die Gültigkeitszeiträume der verwendeten Algorithmen und Parameter zur Durchführung von Erneuerungen der Zeitstempel inkl. der darin enthaltenen digitalen Signatur müssen auf _**[EN 119 312] und [SOG-IS]**_ beruhen.‘ 

Bundesamt für Sicherheit in der Informationstechnik 

19 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

## **5. Appendix zu TR-ESOR-ERS** 

## **5.1 Ergänzung zu Kapitel 5.1: Erstellung eines Evidence Records gem. Basis-ERS-Profil** 

Hier wird lediglich eine zusätzliche Anforderungsnummer „ **(A5.1-1)** “ eingeführt, damit diese Anforderung geeignet referenziert werden kann. Die ergänzte Textstelle sieht dann wie folgt aus: 

_**- (A5.1 1)**_ Die Anforderungen an die kryptographischen Algorithmen und Parameter bei der Erstellung von Evidence Records unter Einsatz von qualifizierten Zeitstempeln gemäß **[eIDAS-VO, Artikel 42]** basieren auf den Vorgaben der jeweils aktuellen Fassung des Algorithmenkataloges **[ETSI TS 119 312][8]** ~~, der auf der Webseite https://portal.etsi.org/TBSiteMap/ESI/ESIActivities.aspx veröffentlicht wird, u~~ nd der auf dem  Algorithmenkatalog **[SOG-IS]** ~~**,** veröffentlicht auf  der Webseite https://www.sogis.org/uk/supporting_doc_en.htmlwww.sogis.org,~~ basiert Diese Vorgaben sind verbindlich und müssen stets den aktuellen Vorgaben gemäß **[ETSI TS 119 312]** und **[SOG-IS][9]** _**angepasst**_ werden. 

~~Für die Erzeugung von technischen Beweisdaten (Evidence Records) gilt die Anforderung~~ ~~**(A4.3-1)** des~~ ~~**Krypto-Moduls M.2** .~~ 

_**-**_ Für die Verifikation von technischen Beweisdaten (Evidence Records) gilt die Anforderung _**(A4.0 1) und**_ **(A4.2-3)** des **Krypto-Moduls M.2** . Bei der Verifikation eines Evidence Records müssen im Bedarfsfall auch die _**weiteren**_ Hashalgorithmen ~~gemäß (vgl.~~ ~~**[ALGCAT]** , Kapitel 6)~~ unterstützt werden. Die OIDs der verwendeten Algorithmen sind **[ETSI TS 119 312]** zu entnehmen. 

Hier werden zusätzliche Anforderungsnummer und in den Tabellen zusätzliche Algorithmen oder geänderte URN eingeführt, damit diese Anforderung geeignet referenziert werden kann. Die ergänzte Textstelle sieht dann wie folgt aus: 

_**(A5.1-2)**_ Aktuell dürfen nur folgende Hashalgorithmen für die Erzeugung von technischen Beweisdaten (Evidence Records) gemäß Kap. 3 verwendet werden: 

|**Algorithmus**|**OID/URN**|**Normative Refe-**|
|---|---|---|
|||**renzen**|
|SHA-256|OID:  2.16.840.1.101.3.4.2.1|**[RFC4055]**|
||URN:http://www.w3.org/2001/04/xmlenc#sha256|**[XMLENC]**|
|SHA-384|OID:  2.16.840.1.101.3.4.2.2|**[RFC4055]**|
||URN:http://www.w3.org/2001/04/xmldsig-more#sha384|**[RFC6931]**|
|SHA-512|OID:  2.16.840.1.101.3.4.2.3|**[RFC4055]**|
||URN:http://www.w3.org/2001/04/xmlenc#sha512|**[XMLENC]**|
|**_SHA3-256_**|**_OID:  2.16.840.1.101.3.4.2.8_**|**_[FIPS202]_**|
||**_URN: http://www.w3.org/2007/05/xmldsig-more#sha3-256_**|**_[RFC6931]_**|



> 8 _**Vgl. https://portal.etsi.org/TBSiteMap/ESI/ESIActivities.aspx**_ 

> _**9 Vgl. https://www.sogis.eu/uk/supporting_doc_en.html**_ 

Bundesamt für Sicherheit in der Informationstechnik 

20 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

|**Algorithmus**|**OID/URN**|**Normative Refe-**|
|---|---|---|
|||**renzen**|
|**_SHA3-384_**|**_OID:  2.16.840.1.101.3.4.2.9_**|**_[FIPS202]_**|
||**_URN: http://www.w3.org/2007/05/xmldsig-more#sha3-384_**|**_[RFC6931]_**|
|**_SHA3-512_**|**_OID:  2.16.840.1.101.3.4.2.10_**|**_[FIPS202]_**|
||**_URN: http://www.w3.org/2007/05/xmldsig-more#sha3-512_**|**_[RFC6931]_**|



**Tabelle 1: Aktuell zugelassene Hashalgorithmen für die Erzeugung technische Beweisdaten (Evidence** 

**Records)** _**(Stand Januar.2021)**_ 

_**(A5.1-3)**_ Hier sind die Vorgaben und Empfehlungen gemäß **[ETSI TS 119 312]** und **[SOG-IS]** einzuhalten. 

_(A5.2-1)_ Für das Prüfen eines Evidence Records müssen alle Algorithmen unterstützt werden, die in diesem Evidence Record verwendet werden. Auch Hash- und Signatur- bzw. Siegel-Algorithmen, deren Sicherheitseignung abgelaufen ist, müssen weiterhin für die Validierung der Beweisdaten vom System unterstützt werden. 

Aktuell müssen im Bedarfsfall zusätzlich mindestens auch noch die folgenden Hashalgorithmen unterstützt werden. 

|**Algorithmus**|**OID/URN**|**Normative Refe-**|
|---|---|---|
|||**renzen**|
|SHA-1|OID:  1.3.14.3.2.26|**[RFC3279]**|
||URN:http://www.w3.org/2000/09/xmldsig#sha1|**[XMLENC]**|
|SHA-224|OID:  2.16.840.1.101.3.4.2.1|**[RFC4055]**|
||URN:http://www.w3.org/2001/04/xmldsig-more#sha384|**[RFC4051]**|
|RIPEMD-160|OID:  1.3.36.3.2.1|**[CRYPTO3N2]**|
||URN:http://www.w3.org/2001/04/xmlenc#ripemd160|**[XMLENC]**|



**Tabelle 2: Aktuell zusätzlich erforderliche Hashalgorithmen für die Verifikation eines Evidence Records** 

_**(Stand Januar 2021)**_ 

_(A5.2.2)_ Für die Erzeugung müssen die Vorgaben und Empfehlungen gemäß **[ETSI TS 119 312]** und **[SOG-IS]** beachtet werden. 

Darüber hinaus sollen nach aktuellem Stand bei der Prüfung auch noch die folgenden Signatur- bzw. Siegelalgorithmen unterstützt werden (vgl. Tabelle 23): 

Bundesamt für Sicherheit in der Informationstechnik 

21 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

## **6. Appendix zu TR-ESOR-E** 

## **6.1 Ergänzung zu Kapitel 2: Überblick** 

Neue Anforderung: 

_**„(A2.0-1) Als ArchiSafe-Schnittstelle muss entweder die nachfolgend spezifizierte TR-S.4Schnittstelle implementiert sein oder ab TR-ESOR V1.2.2 die TS119512-Schnittstelle gemäß [ETSI TS 119 512] in der Profilierung [TR-ESOR-TRANS].“**_ 

Neue Anforderungsnummer und Ergänzungen: 

_**„(A2.0-2) Falls die TR-S.4-Schnittstelle unterstützt wird, dann**_ müssen die im Folgenden näher aufgeführten Funktionen mit den hier beschriebenen Parameterkonstellationen unterstützt werden: 

- ArchiveSubmissionRequest und ArchiveSubmissionResponse (siehe Abschnitt 3.1) 

- ArchiveUpdateRequest und ArchiveUpdateResponse (siehe Abschnitt 3.2) 

- ArchiveRetrievalRequest und ArchiveRetrievalResponse (siehe Abschnitt 3.3) 

- ArchiveEvidenceRequest und ArchiveEvidenceResponse (siehe Abschnitt 3.4) 

- ArchiveDeletionRequest und ArchiveDeletionResponse (siehe Abschnitt 3.5) 

_**Falls die TR-S.4-Schnittstelle unterstützt wird, dann**_ sollen _in der der Schnittstelle TR-S.4_ die folgenden im vorliegenden Dokument näher aufgeführten Funktionen mit den hier beschriebenen Parameterkonstellationen unterstützt werden: 

- ArchiveDataRequest und ArchiveDataResponse (siehe Abschnitt 3.6) 

- VerifyRequest und VerifyResponse (siehe Abschnitt 3.7)“ 

Neue Anforderung: 

_**„(A2.0-3) Falls die TS119512-Schnittstelle in TR-ESOR V1.2.2 unterstützt wird, dann müssen die im Folgenden näher aufgeführten Funktionen mit den in [ETSI TS 119 512] in der Profilierung [TR-ESOR-TRANS] beschriebenen Parameterkonstellationen unterstützt werden:**_ 

- _**PreservePO und PreservePOResponse (siehe [ETSI TS 119 512, Abs. 5.3.3], [TR-ESORTRANS]** , Abs. 3.2_ _**)**_ 

- _**UpdatePOC und UpdatePOC (siehe Abschnitt [ETSI TS 119 512, Abschnitt 5.3.6], [TRESOR-TRANS]** , Abs. 3.3_ _**)**_ 

- _**RetrievePO und RetrievePOResponse (siehe Abschnitt [ETSI TS 119 512, Abschnitt 5.3.4], [TR-ESOR-TRANS]** , Abs. 3.4_ _**)**_ 

- _**DeletePO und DeletePOResponse (siehe Abschnitt [ETSI TS 119 512, Abschnitt 5.3.5], [TR-ESOR-TRANS]** , Abs. 3.5_ _**)**_ 

- _**RetrieveInfo und RetrieveInfoResponse (siehe Abschnitt [ETSI TS 119 512, Abschnitt 5.3.2], [TR-ESOR-TRANS]** , Abs. 3.1_ _**).**_ 

_**Falls die TS119512-Schnittstelle unterstützt wird, dann sollen in der der TS119512-Schnittstelle die folgenden in [ETSI TS 119 512] näher aufgeführten Funktionen mit den dort beschriebenen Parameterkonstellationen unterstützt werden:**_ 

- _**Search und SearchResponse (siehe Abschnitt [ETSI TS 119 512, Abschnitt 5.3.9], [TRESOR-TRANS]** , Abs. 3.7_ _**)**_ 

Bundesamt für Sicherheit in der Informationstechnik 

22 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

- _**ValidateEvidence und ValidateEvidenceResponse (siehe Abschnitt [ETSI TS 119 512, Abschnitt 5.3.8], [TR-ESOR-TRANS]** , Abs. 3.6_ _**)“**_ 

## **6.2 Ergänzung zu Kapitel 3, Unterkapitel 3.6.1 ArchiveDataRequest** 

Auf Basis von PRP-8.1-09: Hier wird lediglich eine zusätzliche Anforderungsnummer „(A3.6-1)“ bzgl. „ `tr:DataLocation“` eingeführt, damit diese Anforderung geeignet referenziert werden kann. Die ergänzte Textstelle sieht dann wie folgt aus: 

_„_ _**(A3.6-1)**_ Sofern der `ArchiveDataRequest` unterstützt wird, muss dieser die Details der an der Schnittstelle angebotenen Funktionalität dokumentieren.“ 

## **6.3 Ergänzung zu Kapitel 4: Funktionen der Preservation-API gemäß ETSI TS 119 512 in der Profilierung [TR-ESOR-TRANS] (ab TRESOR V1.2.2)** 

Hier wird lediglich eine zusätzliche Anforderungsnummer „ **(A4.0-1)** “ eingeführt, damit diese Anforderung geeignet referenziert werden kann. Siehe auch PRP-8.1-06, PRP-8.1-09, PRP-8.1-10, PRP-8.111, PRP-8.1-12, PRP-8.1-14. Die ergänzte Textstelle sieht dann wie folgt aus: 

_**(A4.0-1)**_ Für den Einsatz der „Preservation-API“ gemäß **[ETSI TS 119 512]** in der Profilierung **[TRESOR-TRANS]** im Rahmen der vorliegenden Technischen Richtlinie müssen die folgenden Mindestanforderungen unterstützt werden: 

- `RetrieveInfo` gemäß Abschnitt 3.1 von **[TR-ESOR-TRANS]** muss unterstützt werden. `Hierbei` muss zumindest ein Bewahrungsprofil unterstützt werden, welches das Bewahrungsschema `http://uri.etsi.org/19512/scheme/pds+pgd+aug+wst+ers` gemäß Annex F.1 von **[ETSI TS 119 512]** umsetzt. 

- `PreservePO` gemäß Abschnitt 3.2 von **[TR-ESOR-TRANS]** muss unterstützt werden, wobei zumindest eines der in **[TR-ESOR-F]** definierten Archivdatenobjekt-Formate (XAIP, LXAIP oder ASiC-AIP) unterstützt werden muss. 

- `RetrievePO` gemäß Abschnitt 3.4 von **[TR-ESOR-TRANS]** muss unterstützt werden, wobei zumindest eines der in **[TR-ESOR-F]** definierten Archivdatenobjekt-Formate (XAIP, LXAIP oder ASiC-AIP) sowie Evidence Records gemäß **[RFC4998]** bzw. gemäß [RFC4998] in der Profilierung gemäß **[TR-ESOR-ERS]** unterstützt werden müssen. 

- `DeletePO` gemäß Abschnitt 3.5 von **[TR-ESOR-TRANS]** muss unterstützt werden. 

- `UpdatePOC` gemäß Abschnitt 3.3 von **[TR-ESOR-TRANS]** muss unterstützt werden. 

- `RetrieveTrace` gemäß Abschnitt 5.3.7 von **[ETSI TS 119 512]** kann unterstützt werden. 

- `ValidateEvidence` gemäß Abschnitt 3.6 von **[TR-ESOR-TRANS]** soll unterstützt werden. Sofern diese Operation unterstützt wird, muss zumindest die Validierung von Evidence Records gemäß **[RFC4998]** oder gemäß **[RFC4998]** in der Profilierung gemäß **[TR-ESORERS, Basic-ERS-Profile] und** die Validierung der in **[TR-ESOR-F]** definierten Archivdatenobjekt-Formate **(XAIP, LXAIP oder ASiC-AIP)** unterstützt werden. Darüber hinaus kann die Validierung von Evidence Records gemäß **[RFC6283]** unterstützt werden. 

- `Search` gemäß Abschnitt 3.7 von **[TR-ESOR-TRANS]** kann unterstützt werden. 

Bundesamt für Sicherheit in der Informationstechnik 

23 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

- (Α4.0−2) Die Belegung der Eingabe- und Ausgabe-Parameter der unterstützten Funktionen im Rahmen des „Preservation-APIs“ muss gemäß dem TR-ESOR-Anlage **[TR-ESOR-TRANS]** erfolgen, der eine geeignet profilierte Ausprägung der Preservation-API gemäß **[ETSI TS 119 512]** spezifiziert, die auf die TR-ESOR S.4-Schnittstelle gemäß **[BSI TR-ESOR-E]** abgebildet werden kann. 

- (Α4.0−3) Für den Einsatz der „Preservation-API“ gemäß **[ETSI TS 119 512]** in der Profilierung **[TR-ESOR-TRANS]** im Rahmen der vorliegenden Technischen Richtlinie müssen die folgenden Basistypen für „Request“ und „Response“ unterstützt werden: 

   - Falls das optional OptionalInputs Element vorhanden ist, dann muss es eine Sub-Komponente, wie definiert in ( **[OASIS DSS-X]** , Kapitel 4.1.8), enthalten. 

   - Falls das optional OptionalOutputs Element vorhanden ist, dann muss es eine SubKomponente, wie definiert in ( **[OASIS DSS-X]** , Kapitel 4.1.9), enthalten. 

Bundesamt für Sicherheit in der Informationstechnik 

24 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

## **7. Additional Test Cases for Conformity Level 1 – Functional Conformity** 

Wenn die Zertifizierung des Preservation Service, in dem ein TR-ESOR V1.2.1- bzw. TR-ESOR V1.2.2-Produkt integriert ist, auf Basis von **[ASS 119 401]** und **[ASS 119 511]** durchgeführt wird, dann ist es empfehlenswert, die folgenden Testfälle in dem hier vorliegenden Anhang [ **TR-ESOR-APP]** als einen zusätzlichen Baustein für die TR-ESOR-V1.2.1 – bzw. TR-ESOR-V1.2.2 - Zertifizierung anzuwenden. 

## **7.1 Additional Tests for all products** 

- **7.1.1 A-11 – What happens to the Data at the End of the Preservation Period shall be stated in the in the Preservation Evidence Policy of the TR-ESOR Product-Manufacturer** 

A **new** test case in TR-ESOR V1.2.2. 

25 

Bundesamt für Sicherheit in der Informationstechnik 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

|**Identifier**|**Identifier**|**A-11**|**A-11**|**A-11**|
|---|---|---|---|---|
|**Requirement**||MD: A4.1-1<br>_OVR-6.1-09_|||
|**Test Purpose**||The test shall verify that in the Preservation Evidence Policy (PEP) of the TR-ESOR-Product Manufacturer, based on the BSI-**[TR-ESOR-PEPT],**is described<br>what happens to the data at the end of the preservation period.|||
|**Configuration**||CONFIG_ArchiSafe|||
|**Pre-test conditions**||•<br>Preservation Evidence Policy (PEP) of the TR-ESOR-Product-Manufacturer, based on the BSI-**[TR-ESOR-PEPT],**is present and published.|||
|Step|Test sequence||Expected Results|Observations|
|1.|Check the Preservation Evidence Policy for information<br>about what happens to the data at the end of the preserva-<br>tion period.||The necessary details of what happens to the data at the end of the<br>preservation period.are stated.||
|2.|Check onsite and verify:<br>- whether what happens to the data at the end of the<br>preservation period, takes place as documented||What happens to the data at the end of the preservation period,<br>takes place as documented in the Preservation Evidence Policy of<br>the TR-ESOR product.||
|3.|Conditional: In case of federal and state public bodies,<br>check, whether the requirement (A4.1-1) pursuant to<br>[TR-ESOR], clause 4 is fulfilled at the end of the preser-<br>vation period.||What happens to the data at the end of the preservation period,<br>takes place as documented in [TR-ESOR], clause 4, (A4.1-1).||
|**Verdict**|||||
||||||



26 

Bundesamt für Sicherheit in der Informationstechnik 

## **Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

## **7.1.2 A-12 – The TOT shall support at least one Preservation Profile, which is publicly published and can be retrieved as described in the User Manual and Preservation Evidence Policy (PEP) of the TOT (TR-ESOR Product)** 

A new test case in TR-ESOR V1.2.2. 

Bundesamt für Sicherheit in der Informationstechnik 

27 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

|**Identifier**|**Identifier**|**A-12**|**A-12**|**A-12**|
|---|---|---|---|---|
|**Requirement**||MD:A6.1-6<br>OVR-6.4-01<br>OVR-6.4-04 b**)**<br>PRP-8.1-04|||
|**Test Purpose**||The test shall verify that how to retrieve the Preservation Profile is described in the User Manual.<br>The test shall verify that the supported input formats and conditionally additional output formats are contained or referred in each publicly published Preservation<br>Profile.|||
|**Configuration**||CONFIG_ArchiSafe|||
|**Pre-test conditions**||•<br>User manual is present.<br>•<br>Preservation Evidence Policy (PEP) of the TR-ESOR-Product Manufacturer, based on the BSI-**[TR-ESOR-PEPT],**is present and published.<br>•<br>Preservation Profile is present and published.<br>•<br>The middleware is installed and configured.<br>•<br>Either the S.4 interface or the TS119512 interface S.512 in the profiling of**[TR-ESOR-TRANS] **shallbe configured.|||
|Step|Test sequence||Expected Results|Observations|
|1.|Check whether at least one Preservation Profile is pub-<br>lished and supported by the TOT.||At least one Preservation Profile is published and is supported by<br>the TOT.||
|2.|Check the user manual and Preservation Evidence Policy<br>for information about how to retrieve the Preservation<br>Profile.||The necessary details, how to retrieve the Preservation Profile, are<br>stated.||
|3.|Retrieve the publicly published Preservation Profiles and<br>check, whether the supported input formats and condi-<br>tionally additional output formats are contained or re-<br>ferred in each received Preservation Profile described in<br>a documentation referenced by the Preservation Profile.||Foreach operation the Preservation Profile contains:<br>•<br>the supported input formats<br>•<br>and [CONDITIONAL] additional output formats.||
|4.|Use the interface function “`RetrieveInfo`” to receive<br>a Preservation Profile.||The call of the function is possible.||
|5.|Observe the output of the interface function “`Re-`<br>`trieveInfoResponse`”.||A positive feedback is received. No error message or error code<br>occurs. At least one Preservation Profile is received.||



Bundesamt für Sicherheit in der Informationstechnik 

28 

## **Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

|**Identifier**|**Identifier**|**A-12**|**A-12**|**A-12**|
|---|---|---|---|---|
|6.|Observe the received Preservation Profiles and verify,<br>whether the supported input formats and additional out-<br>put formats in each received Preservation Profile are<br>described in a documentation referenced by the Preserva-<br>tion Profile (e.g.**[TR-ESOR-E]**).||The supported input formats and additional output formats in each<br>received Preservation Profile are described in a documentation<br>referenced by the Preservation Profile (e.g.**[TR-ESOR-E]**).||
|**Verdict**|||||
||||||



Bundesamt für Sicherheit in der Informationstechnik 

29 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

**7.1.3 A-13 – Each installed Preservation Profile shall contain an identifier which uniquely identifies this Preservation Profile** A new test case in TR-ESOR V1.2.2. 

|**Identifier**|**Identifier**|**A-13**|**A-13**|**A-13**|
|---|---|---|---|---|
|**Requirement**||MD:A6.1-6<br>_OVR-6.4-04 a_|||
|**Test Purpose**||The test shall verify that each installed Preservation Profile contains an identifier, which uniquely identifies this Preservation Profile.|||
|**Configuration**||CONFIG_Common|||
|**Pre-test conditions**||•<br>Preservation Profile is present.<br>•<br>User has administrator rights on the system.<br>•<br>If required, perform identification and authentication.<br>•<br>Test case A-12 was performed successful and the identifiers of the active Preservation Profiles are known.|||
|Step|Test sequence||Expected Results|Observations|
|1.|Compare on-site the known Preservation Profile identifi-<br>ers.||No two Preservation Profile identifiers are equal.||
|**Verdict**|||||
||||||



Bundesamt für Sicherheit in der Informationstechnik 

30 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

## **7.1.4 A-14 – The Preservation Evidence Policy of the TR-ESOR-Product Manufacturer shall contain the description of how the preservation evidence is created including which cryptographic algorithms are used.** 

## A new test case in TR-ESOR V1.2.2. 

|**Identifier**|**Identifier**|**A-14**|**A-14**|**A-14**|
|---|---|---|---|---|
|**Requirement**||_MD:A6.1-7_<br>_OVR-6.5-03_|||
|**Test Purpose**||The test shall verify that each installed_Preservation Evidence Policy_(PEP) of the TR-ESOR-Product Manufacturer, based on the BSI-**[TR-ESOR-PEPT],**shall<br>contain the description of how the preservation evidence is created including which cryptographic algorithms are used.|||
|**Configuration**||CONFIG_Common|||
|**Pre-test conditions**||•<br>Preservation Evidence Policy (PEP) of the TR-ESOR-Product Manufacturer, based on the BSI-**[TR-ESOR-PEPT],**is present and published.<br>•<br>Preservation Profile is present and published.<br>•<br>Test case A-12 was performed successful and the identifiers of the active Preservation Profiles are known.|||
|Step|Test sequence||Expected Results|Observations|
|1.|Check the Preservation Evidence Policy, which is refer-<br>enced by the Preservation Profile.||This Preservation Evidence Policy contains or references the de-<br>scription of how the preservation evidence is created and describes<br>which cryptographic algorithms are used.||
|2.|Check and compareon-site<br>- how the preservation evidence is created and<br>- which cryptographic algorithms are used<br>with the documentation in the Preservation Evidence<br>Policy.||The result of the comparison is that<br>•<br>how the preservation evidence is created and<br>•<br>which cryptographic algorithms are used,<br>are implemented and work as documented in the Preservation<br>Evidence Policy.||
|**Verdict**|||||
||||||



Bundesamt für Sicherheit in der Informationstechnik 

31 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

## **7.1.5 A-15 – The Evaluation Report of the TR-ESOR-Product, written by the Testing Body, shall contain the digital fingerprints of the relevant Programs of the TR-ESOR-Product.** 

A new test case in TR-ESOR V1.2.2. 

|**Identifier**|**Identifier**|**A-14**|**A-14**|**A-14**|
|---|---|---|---|---|
|**Requirement**||_MD:A9.0-1_|||
|**Test Purpose**||The testshallverify that the Evaluation Report of the TR-ESOR-Product, written by the Testing Body, contains the digital fingerprints of the relevant programs of<br>the TR-ESOR-Product.|||
|**Configuration**||CONFIG_Common|||
|**Pre-test conditions**||•<br>User Manual<br>•<br>Evaluation Report of the Testing Body|||
|Step|Test sequence||Expected Results|Observations|
|1.|Check the User Manual of the TR-ESOR-Product con-<br>cerning the “digital Fingerprints” concerning the relevant<br>programs of the TR-ESOR-Product.||The “digital Fingerprints” of the relevant programs of the TR-<br>ESOR-Product.are listed in the user manual.||
|2.|Compare the “digital fingerprints” of the relevant pro-<br>grams of the evaluated TR-ESOR-Product with the “digi-<br>tal fingerprints” written down in the user manual.||The “digital Fingerprints” of the relevant programs of the TR-<br>ESOR-Product are equal to the “digital Fingerprints” of the rele-<br>vant programs of the TR-ESOR-Product, documented in the user<br>manual.||
|3.|Check the own Evaluation Report (of the testing body),<br>whether the “digital Fingerprints” concerning the rele-<br>vant programs of the TR-ESOR-Product are written<br>down and documented there.||The “digital Fingerprints” of the relevant programs of the TR-<br>ESOR-Product are documented in the own Evaluation Report of<br>the Testing Body.||
|**Verdict**|||||
||||||



Bundesamt für Sicherheit in der Informationstechnik 

32 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

## **7.2 Appendix to Module 2 – Crypto-Module** 

## **7.2.1 M.2-05 – Support of Hash functions** 

Preservation Evidence Policy included. 

|**Identifier**|**M.2-05**|
|---|---|
|**Requirement**|M2:A4.2-1<br>M2:A4.2-2<br>M2:A4.2-3<br>M2:A5.3-1<br>_OVR-6.5-04_<br>_OVR-7.14-03_|
|**Test Purpose**|The Cryptographic-Module shall have functions to calculate hash values for information packages. In doing so, the requirements for hash procedures shall be ful-<br>filled.10|
|**Configuration**|CONFIG_ArchiSafe|
|**Pre-test conditions**|•<br>The list of hash algorithms and parameters recommended by [**ETSI TS 119 312]**and**[SOG-IS]**is accessible.<br>•<br>User manual is present.<br>•<br>**_Preservation Evidence Policy (PEP) of the TR-ESOR-Product Manufacturer,_**based on the BSI-**[TR-ESOR-PEPT],**is present and published.<br>•<br>XAIP means “XAIP” or “LXAIP” pursuant to**[TR-ESOR-F] V1.2.2.**<br>•<br>DXAIP means “DXAIP” or “DLXAIP” pursuant to**[TR-ESOR-F] V1.2.2**.<br>•<br>XAIP shall be supported, “LXAIP” may be supported, if configured.|



> 10 Exclusively those hash algorithms and parameters recommended by **[ETSI TS 119 312]** and **[SOG-IS]** shall be used to form hash values. However, the Cryptographic- Module shall continue to support all hash algorithms previously used by the  Cryptographic-Module in order to enable validation of hash values generated in the past according to **[ALGCAT]** , **[ETSI TS 119 312]/[SOG-IS]** and **[TR-ESOR-ERS, chapter 5.2.1])** . 

Bundesamt für Sicherheit in der Informationstechnik 

33 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

|**Identifier**|**Identifier**|**M.2-05**|**M.2-05**|**M.2-05**|
|---|---|---|---|---|
|Step|Test sequence||Expected Results|Observations|
|1.|Check the user manual and**_Preservation Evidence Poli-_**<br>**_cy_**of the TR-ESOR-Manufacturer for the hash algo-<br>rithms, which are used by the Cryptographic-Module.<br>The Cryptographic-Module shall support at least two<br>hash algorithms which have been assessed by**[ETSI TS**<br>**119 312]**and**[SOG-IS] and [TR 03116] and [TR**<br>**02102]**as suitable for security and published.||The used hash algorithms are in the list of the recommended algo-<br>rithms.||
|2.|Check the user manual and**_Preservation Evidence Poli-_**<br>**_cy of the TR-ESOR-Manufacturer_**whether the Crypto-<br>graphic-Module continues to support all hash algorithms<br>previously used pursuant to**[ALGCAT]**or (**[TR-ESOR-**<br>**ERS]**, Chap. 5.2.1) in order to enable the validation of<br>hash values computed in the past.||The used hash algorithms are in the list of the supported algo-<br>rithms.||
|3.|Check the user manual and**_Preservation Evidence Poli-_**<br>**_cy of the TR-ESOR-Manufacturer_**for the supported<br>hash algorithms.||The Cryptographic-Module supports all previously used hash<br>algorithms.||
|4.|Transfer the signed XAIP_OK, DXAIP_OK or BIN to<br>the Cryptographic-Module using the interface function<br>„Hash“.||The call of the function with this XAIP / DXAIP_OK / BIN as<br>parameter is possible.||
|5.|Observe the output of the interface function “Hash”.||A positive feedback and aHashResponse-Element will be re-<br>ceived.||
|6.|Check the Hash-Element in the HashResponse-Element<br>whether the Hash-value is correct by using a   certified<br>tool or product, e.g. a certified eCard-Crypto-Modul, for<br>comparison of the Hash-value calculated on base of the<br>signed XAIP_OK or DXAIP_OK or BIN.||The received Hash-value was verified by comparison of the hash<br>calculations with a certified Crypto-Modul.||
|7.|**Conditional:**_If LXAIP is implemented,_test steps from<br>No. 1 to No. 6 are to be repeated for LXAIP.||See expected results of the test cases from No. 1 to No. 6 for<br>LXAIP.||
|**Verdict**|||||



Bundesamt für Sicherheit in der Informationstechnik 

34 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

## **7.2.2 M.2-11 – Suitability of cryptographic algorithms should be defined by User Manual and the Preservation Evidence Policy (PEP) of the TR-ESOR-Product Manufacturer, based on the BSI-[TR-ESOR-PEPT]** 

## Preservation Evidence Policy included. 

|**Identifier**|**Identifier**|**M.2-11**|**M.2-11**|**M.2-11**|
|---|---|---|---|---|
|**Requirement**||M3:A5.3-2|||
|**Test Purpose**||Check whether the validity periods of hash and digital signature algorithms are stored and managed in the form of a Preservation Evidence Policy file|||
|**Configuration**||CONFIG_Common|||
|**Pre-test conditions**||•<br>User manual is present.<br>•<br>Preservation Evidence Policy (PEP) of the TR-ESOR-Product Manufacturer, based on the BSI-**[TR-ESOR-PEPT],**is present and published.|||
|Step|Test sequence||Expected Results|Observations|
|1.|Check the user manual **_and the Preservation Evidence_**<br>**_Policy_**how the validity periods of hash and digital signa-<br>ture algorithms are stored and managed.||The validity periods of hash and digital signature algo-<br>rithms should be stored and managed in the form of a pol-<br>icy file.||
|**Verdict**|||||



35 

Bundesamt für Sicherheit in der Informationstechnik 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

## **7.2.3 M.2-18 – Crypto-Module supports [RFC 3161], [RFC5816], [RFC5652] and [EN 319 422] and suitable algorithms** 

The test case is extended by Step 3 and 4. 

|**Identifier**|**Identifier**|**M.2-18**|**M.2-18**|**M.2-18**|
|---|---|---|---|---|
|**Requirement**||M2:A5.4-3<br>M3:A4.7-4<br>_OVR-9.2-01_|||
|**Test Purpose**||The  Cryptographic-Module shall check whether requested electronic time-stamp fulfils the requirements and specifications of the electronic time-stamp protocol<br>pursuant to**[RFC3161]**,**[RFC5816], [RFC5652]**and**[EN 319 422]]**and whether the limitations for algorithms and parameters assessed as suitable for security<br>according to**[ETSI TS 119 312]**and**[SOG-IS]**are implemented.|||
|**Configuration**||CONFIG_Common|||
|**Pre-test condition**||•<br>Install an access to a qualified time-stamp Trust Service Provider, which accepts requests compliant with TSP (RFC 3161).<br>•<br>Configure the Crypto-Module to use this Time-Stamp Service.<br>•<br>Supply the list of algorithms and parameters assessed as suitable according to**[ETSI TS 119 312]**and**[SOG-IS].**|||
|Step|Test sequence||Expected Results|Observations|
|1.|Configure the Crypto-Module according to the guidance;<br>especially the protocol used to access the qualified time-<br>stamp trust service provider according to**[eIDAS-VO,**<br>**Articel 42c]**.<br>Check also whether there are guidance hints regarding<br>the configuration of algorithms and other cryptographic<br>parameters.||It is expected that there are at least some hints regarding the con-<br>figuration of algorithms according to the eIDAS recommendations<br>of**[ETSI TS 119 312]**and [**SOG-IS]**.||
|2.|Request the qualified electronic time-stamp using the<br>interface function „TimestampRequest“ for each hash<br>algorithm supported by the Cryptographic-Module. The<br>requestData contain the corresponding hash-algorithm-<br>identifier.||The request of the qualified electronic time-stamp with algorithm-<br>identifier in requestData as parameter is possible.<br>A positive feedback will be received; no error message or error<br>code. The electronic time-stamp shall be received for at least one<br>algorithm.||



36 

Bundesamt für Sicherheit in der Informationstechnik 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

|**Identifier**|**Identifier**|**M.2-18**|**M.2-18**|**M.2-18**|
|---|---|---|---|---|
|3.|**_Check whether the time-stamp protocol is pursuant to_**<br>**_[RFC3161], [RFC5816], [RFC5652]_**_and_**_[EN 319 422]._**||**_The time-stamp protocol, used in step 2, has an allowed format_**<br>**_pursuant to [RFC3161], [RFC5816], [RFC5652]_**_and_**_[EN 319_**<br>**_422]._**||
|4.|**_Check whether the cryptographic algorithms and pa-_**<br>**_rameters used in the time-stamp protocol are suitable_**<br>**_for security according to [ETSI TS 119 312] and [SOG-_**<br>**_IS]._**||**_The cryptographic algorithms and parameters used in the time-_**<br>**_stamp protocol in step 2 are suitable for security according to_**<br>**_[ETSI TS 119 312] and [SOG-IS]._**||
|5.|Request a qualified electronic time-stamp using the<br>interface function “TimestampRequest” where the time<br>of the executing the request has been manipulated in<br>such a manner that it differs substantial from the moment<br>of the request.||The Crypto-Module returns an error message indicating that the<br>returned time is incorrect.||
|6.|Request an electronic time-stamp using the interface<br>function “TimestampRequest” where the digital signa-<br>ture of the electronic time-stamp is invalid.||The Crypto-Module returns an error message indicating that the<br>digital signature of the electronic time-stamp is invalid.||
|**Verdict**|||||
||||||



Bundesamt für Sicherheit in der Informationstechnik 

37 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

Bundesamt für Sicherheit in der Informationstechnik 

38 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

## **7.2.4 M.2-20 – Crypto-Module shall validate digital signatures of received electronic time-stamps or hash values (or another cryptographic security element) in <asic:DataObjectReference> of a LXAIP according to the signature validation policy** The Testcase M.2-20 is extended by Step 1, 6 and 7. 

|**Identifier**|**Identifier**|**M.2-20**|**M.2-20**|**M.2-20**|
|---|---|---|---|---|
|**Requirement**||MD: A7.4-4<br>MD: A7.4-7<br>M2:A5.4-4<br>M2:A5.4-5<br>_OVR-7.10-02_<br>_PRP-8.1-06_<br>_OVR-9.3-01_<br>_OVR-9.3-02_|||
|**Test Purpose**||Check whether the Cryptographic-Module validates the authenticity and integrity of received qualified electronic time-stamps immediately upon receipt and prior to<br>further processing including the validation of the certificate chain back to a trustworthy root TSP<br>•<br>by itself according to the Time-Stamp Validation Policy supported by the Preservation Profile or Preservation Evidence Policy (PEP) of the TR-ESOR-<br>Product Manufacturer, based on the BSI-**[TR-ESOR-PEPT]**.<br>•<br>by requesting a validation service from a Trust Service Provider according to the Time-Stamp Validation Policy supported by the Preservation Profile or<br>Preservation Evidence Policy (PEP) of the TR-ESOR-Product Manufacturer, based on the BSI-**[TR-ESOR-PEPT]**.|||
|**Configuration**||CONFIG_Common|||
|**Pre-test conditions**||•<br>**User**manual is present.<br>•<br>Preservation Evidence Policy (PEP) of the TR-ESOR-Product Manufacturer, based on the BSI-**[TR-ESOR-PEPT],**is present and published.<br>•<br>**Preservation Profile is present and published.**<br>•<br>**Signature and Time-Stamp Validation Policy is present and published.**<br>•<br>Configure Crypto-Module to maximum verbose logging.<br>•<br>The Cryptographic-Module may be configured to ask for a time-stamp validation service from a Trust Service Provider.|||
|Step|Test sequence||Expected Results|Observations|
|1.|**_Check the Preservation Evidence Policy (PEP) of the_**<br>**_TR-ESOR-Product Manufacturer where to find the_**<br>**_actual Preservation Profile. Check the Preservation_**||**_In the PEP of the TR-ESOR-Product Manufacturer, there is the_**<br>**_information, where to find the actual Preservation Profile. In the_**<br>**_actual profile, the Time-Stamp Validation Policy or a reference_**||



Bundesamt für Sicherheit in der Informationstechnik 

39 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

||**Identifier**||**M.2-20**||
|---|---|---|---|---|
||**_Profile in order to find a Time-Stamp Validation Policy_**<br>**_or a reference to a Time-Stamp Validation Policy._**||**_to the Time-Stamp Validation Policy is to be found._**||
|2.|Request a qualified electronic time-stamp using the<br>functions of the Crypto-Module.||The Crypto-Module performs the request.||
|3.|Check log files or other evidences whether the Crypto-<br>Module has verified the authenticity and integrity of the<br>received qualified electronic time-stamp (the digital<br>signature) by itself**_or by a connected time-stamp valida-_**<br>**_tion service from a Trust Service Provider_**.||The Crypto-Module**_or the connected Time-Stamp Validation_**<br>**_Trust Service Provider_**has successfully verified the mathematical<br>correctness of the digital signature.||
|4.|Check log files or other evidences whether the Crypto-<br>Module**_or the connected Time-Stamp Validation Trust_**<br>**_Service Provider_**has verified the certificate used for<br>digital signature.||The Crypto-Module**_or the connected Time-Stamp Validation_**<br>**_Trust Service Provider_**has verified successfully the digital signa-<br>ture certificate.||
|5.|Check log files or other evidences whether the Crypto-<br>Module**_or the connected Time-Stamp Validation Trust_**<br>**_Service Provider_**has verified the CA certificate used to<br>sign the certificate used for digital signature.||The Crypto-Module**_or the connected Time-Stamp Validation_**<br>**_Trust Service Provider_**has verified successfully the CA certificate||
|6.|Emulate the check of invalid digital signatures and certif-<br>icates.||The Cryptographic-Module detects and logs the failures**_with its_**<br>**_reason codes._**||
|7.|**_Check that the validation of the digital signatures of the_**<br>**_received electronic time-stamps and the validation of_**<br>**_the certificate chain back to a trustworthy root TSP_**<br>**_were done according to the Time-Stamp Validation_**<br>**_Policy._**||**_The validation of the digital signatures and the certificate were_**<br>**_done according to the Time-Stamp Validation Policy._**||
|8.|**Conditional:**_If LXAIP is implemented:_<br>Store an`LXAIP_OK`using the “ArchiveSubmissionRe-<br>quest” or the “`PreservePO`” function.||The function call is possible.||
|9.|**Conditional:**_If LXAIP is implemented:_<br>Check the output of the “ArchiveSubmissionResponse”<br>or the “`PreservePOResponse”`function.||The XAIP/BIN object is assigned to an AOID and returned suc-<br>cessfully.||
|10.|**Conditional:**_If LXAIP is implemented:_<br>Check log files or other evidences whether the Crypto-||The Crypto-Module has retrieved the data object, referenced in in<br>the <asic:DataObjectReference> from the ECM-/ Long-Term||



Bundesamt für Sicherheit in der Informationstechnik 

40 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

|**Identifier**|**Identifier**|**M.2-20**|**M.2-20**|**M.2-20**|
|---|---|---|---|---|
||Module has retrieved the data object, referenced in in the<br><asic:DataObjectReference> from the ECM-/ Long-<br>Term Storage and verified the hash value (or another<br>cryptographic security element) in the<br><asic:DataObjectReference> of the `LXAIP_OK.`||Storage and has verified successfully the hash value (or another<br>cryptographic security element) in the<br><asic:DataObjectReference> of the `LXAIP_OK.`||
|11.|**Conditional:**_If LXAIP is implemented:_<br>Store an`LXAIP_NOK`using the “ArchiveSubmission-<br>Request” or the “`PreservePO`” function, where the<br>hash value or another cryptographic security element in<br>the <asic:DataObjectReference> of the `LXAIP_NOK`is<br>wrong.||The function call is possible.||
|12.|**Conditional:**_If LXAIP is implemented:_<br>Check the output of the “ArchiveSubmissionResponse”<br>or the “`PreservePOResponse”`function.||The XAIP/BIN object is not assigned to an AOID and a negative<br>feedback will be received with error message and error code.||
|13.|**Conditional:**_If LXAIP is implemented:_<br>Check log files or other evidences whether the Crypto-<br>Module has retrieved the data object, referenced in in the<br><asic:DataObjectReference> from the ECM-/ Long-<br>Term Storage and verified the hash value (or another<br>cryptographic security element) in the<br><asic:DataObjectReference> of the `LXAIP_OK.`||The Crypto-Module has retrieved the data object, referenced in in<br>the <asic:DataObjectReference> from the ECM-/ Long-Term<br>Storage and has not verified successfully the hash value (or another<br>cryptographic security element) in the<br><asic:DataObjectReference> of the `LXAIP_OK.`<br>The Cryptographic module detects and logs the failures.||
|**Verdict**|||||
||||||



Bundesamt für Sicherheit in der Informationstechnik 

41 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

## **7.3 Appendix to Module 3 – ArchiSig Module** 

## **7.3.1 M.3-04 – Creation of Initial Archive Timestamps according to [RFC4998] or [RFC6283]** 

The Testcase M.3-04 is extended by Step 4 extended and Step 5 new. 

|**Identifier**|**Identifier**|**M.3-04**|**M.3-04**|**M.3-04**|
|---|---|---|---|---|
|**Requirement**||M3:A4.5-1<br>M3:A4.5-4<br>_OVR-9.3-03_<br>_OVR-9.3-04_|||
|**Test Purpose**||The testshallverify that the creation of the Initial Archive Timestamp is automated and take place according to configurable rules reliably stored in the ArchiSig-<br>Module.<br>**_Conditional: In case of digitally signed or timestamped data, the test should verify that the Initial Archive Timestamp.gives a proof of existence of the signature_**<br>**_or time-stamp and of the validation data needed to validate the signatures or time-stamp and on the other side gives a proof of existence of the signed data._**|||
|**Configuration**||CONFIG_Common|||
|**Pre-test conditions**||•<br>User has administrator rights on the system.<br>•<br>If required, perform identification and authentication.<br>•<br>At least one archive object is already archived.|||
|Step|Test sequence||Expected Results|Observations|



Bundesamt für Sicherheit in der Informationstechnik 

42 

## **Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

|**Identifier**|**Identifier**|**M.3-04**|**M.3-04**|**M.3-04**|
|---|---|---|---|---|
|1.|Check the ArchiSig-Module, whether there are configu-<br>rable rules for the creation of Initial Archive<br>Timestamps.||There are configurable rules for the creation of Initial Archive<br>Timestamps.||
|2.|Configure the ArchiSig-Module in such a way that every<br>10 minutes (or another short time period) a new Archive<br>Timestamp will be created.||Configuration is possible.||
|3.|Request every 10 minutes (or the configured period of<br>time) a new ER of an already archived object (3 or 4<br>times).||ER can be retrieved.||
|4.|Check the last Initial Archive Timestamp.||The check is performed successfully. The Initial Archive<br>Timestamp is created according to [RFC4998]11or [RFC6283].||
|5.|**_Conditional: In case of digitally signed data or time-_**<br>**_stamped data,_**<br>**_Check, that the Initial Archive Timestamp.gives a proof_**<br>**_of existence of the signature or time-stamp and of the_**<br>**_validation data needed to validate the signatures or_**<br>**_time-stamp and on the other side gives a proof of exist-_**<br>**_ence of the signed data._**||**_The check is performed successfully_**||
|**Verdict**|||||



> 11 **[RFC4998]** must be supported, **[RFC6283]** can be supported. 

Bundesamt für Sicherheit in der Informationstechnik 

43 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

## **7.3.2 M.3-13– ArchiSig-Module supports Timestamp Renewal and Hash-Tree Renewal** 

Preservation Evidence Policy added, Extended test case, see step 2, 7, 15, 16, 17. 

Bundesamt für Sicherheit in der Informationstechnik 

44 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

|**Identifier**|**Identifier**|**M.3-13**|**M.3-13**|**M.3-13**|
|---|---|---|---|---|
|**Requirement**||MD:A5.1-6<br>MD:A5.1-7<br>MD:A6.1-8<br>MD:A6.1-9<br>MD:A8.2-6<br>MD:A8.2-7<br>_OVR-6.5-08_<br>_OVR-7.14-01_<br>_OVR-7.14-02_<br>_OVR-7.14-03_<br>_OVR-7.15-01_<br>_OVR-7.15-03_<br>_OVR-9.2-03_|||
|**Test Purpose**||The testshallverify that pursuant to§ 15 of the “Vertrauensdienstegesetz”the signed data can be re-signed and re-hashed by augmenting the preservation<br>evidence in order to “achieve the corresponding preservation goal” (OVR-7.15-01,OVR-7.15-03).|||
|**Configuration**||CONFIG_ArchiSafe|||
|**Pre-test conditions**||•<br>Preservation Evidence Policy (PEP) of the TR-ESOR-Product Manufacturer, based on the BSI-**[TR-ESOR-PEPT]**, is present and published.<br>•<br>Preservation Profile is present and published.<br>•<br>Test user has administrative rights on the system.<br>•<br>There are XAIPs or LXAIPs or BINs,restrictedto the_preservation object formats_described in clause 2, Notice 4, which were successfully stored in the<br>ECM/long-term storage and their AOID's were given back by the Response –Messages and therefore are now “known” in this test case.<br>•<br>If required, perform identification and authentication.<br>•<br>Either the S.4 interface or the TS119512 interface S.512 in the profiling of**[TR-ESOR-TRANS] **shallbe configured.<br>•<br>The**BSI-ERVerify-Tool**is accessible and the tester has access rights to it.<br>•<br>**Conditional:**The TR-ESOR-Product supports an automated monitoring of the strength of the used cryptographic algorithms on base of the ETSI Algo<br>Catalogue ETSI TS 119 312.|||
|Step|Test sequence||Expected Results|Observations|



45 

Bundesamt für Sicherheit in der Informationstechnik 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

||**Identifier**||**M.3-13**||
|---|---|---|---|---|
|1.|Use several interface functions “`ArchiveEvi-`<br>`denceRequest`” or “`RetrievePO”`with`Subjec-`<br>`tOfRetrieval “Evidence”`” with the known<br>AOIDs pursuant to S.4 or S.512.<br>If required, perform identification and authentication.||Several calls of the function with the AOIDs as parameters are<br>possible.<br>Appropriate Evidence Records will be received.||
|2.|Change the Preservation Evidence Policy, referenced<br>actually by the PSPS, concerning the signature algorithm<br>and start the re-sign (Timestamp Renewal) process based<br>on interfaces provided by the ArchiSig-Module.||The initiation of the re-sign process is possible. No error is indica-<br>ted.||
|3.|Check log for information about the re-sign process.||No error messages or error codes for the re-signing are in the log.||
|4.|Use several interface functions “`ArchiveEvi-`<br>`denceReques`t” or “`RetrievePO”`with`Subjec-`<br>`tOfRetrieval “Evidence”`” with the known<br>AOIDs pursuant to S.4 or S.512.||Appropriate Evidence Records will be received.||
|5.|Compare the new Evidence Records with the old Evi-<br>dence Records of the XAIPs or BINs from step 1.||The new and the old Evidence Records are not equal. The new<br>Evidence Records base on the new digital signature algorithms<br>pursuant to the new Preservation Evidence Policy.||
|6.|Change old hash-algorithm against new one.||The change of Hash-Algorithm is possible.||
|7.|Change the Preservation Evidence Policy, referenced<br>actually by the PSPS, concerning the signature algorithm<br>and initiate re-hash (Hash-tree Renewal) process.||The initiation of the re-hash process is possible.||
|8.|Check log for information about the re-hash process.||No error messages or error codes for the re-hashing are in the log.||
|9.|Start the re-sign (Timestamp Renewal) process based on<br>interfaces provided by the ArchiSig-Module.||The initiation of the re-sign process is possible. No error is indica-<br>ted.||
|10.|Check log for information about the re-sign process.||No error messages or error codes for the re-signing are in the log.||
|11.|Use several interface functions “`ArchiveEvi-`<br>`denceRequest`” or “`RetrievePO”`with`Subjec-`<br>`tOfRetrieval “Evidence”`” with the known<br>AOIDs.||Appropriate Evidence Records will be received.||



46 

Bundesamt für Sicherheit in der Informationstechnik 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

|**Identifier**|**Identifier**|**M.3-13**|**M.3-13**|**M.3-13**|
|---|---|---|---|---|
|12.|Compare the new Evidence Records with the old Evi-<br>dence Records of the XAIPs or BINs from step 1 and<br>step 4 and check whether there is a new Preservation<br>Evidence Policy.||The new and the old Evidence Records from step 1, 4 and 12 are<br>not equal. The new Evidence Records base on the new hash and<br>digital signature algorithms on base of a new Preservation Evi-<br>dence Policy.||
|13.|Use several interface functions “`ArchiveRetriev-`<br>`alRequest`” or “`RetrievePO`” with`SubjectOf-`<br>`Retrieval “PO”`” Request with the known AOIDs<br>pursuant to S.4 or S.512.||The XAIP's are retrieved from the storage.||
|14.|Check the credential section of the XAIPs.||The respective “old” Evidence Records with old hash value are<br>included in the credential section.||
|15.|**Conditional**(on-site): Check whether there exist an<br>automatic monitoring of the strength of every crypto-<br>graphic algorithm, that is used in connection with the<br>actual Preservation Evidence Policy, referenced by one<br>of the actual profile on base of an ETSI Algorithm Cata-<br>logue ETSI TS 119 322.||On-Site: The automatic monitoring is activated and the produced<br>monitoring protocol shows whether the strength of every cryp-<br>tographic algorithm used is no longer sufficient.||
|16.|Check the new Evidence Record of test step 4 with the<br>**BSI-ERVerify-Tool.**||The verification report, returned from the BSI-ERVerify-Tool,<br>shows no errors.||
|17.|Check the new Evidence Record of test step 11 with the<br>**BSI-ERVerify-Tool**.||The verification report, returned from the BSI-ERVerify-Tool,<br>shows no errors.||
|**Verdict**|||||
||||||



Bundesamt für Sicherheit in der Informationstechnik 

47 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

## **7.3.3 M.3-14 – Timestamp Renewal** 

Preservation Profile and Preservation Evidence Policy added. 

Check User manual or Preservation Profile. 

|**Identifier**|**Identifier**|**M.3-14**|**M.3-14**|**M.3-14**|
|---|---|---|---|---|
|**Requirement**||MD:A6.1-8<br>M3:A4.7-1<br>M3:A4.7-3<br>_OVR-6.5-07_<br>_OVR-7.14-02_<br>_OVR-7.15-01_<br>_OVR-7.15-03_|||
|**Test Purpose**||The test shall verify that when the function for renewal of the Archive Timestamp is requested, the latest Archive Timestamp will be renewed according to a new<br>version of the Preservation Evidence Policy.|||
|**Configuration**||CONFIG_Common|||
|**Pre-test conditions**||•<br>User manual is present.<br>•<br>_The_**_Preservation Profile is present and published._**<br>•<br>The Preservation Evidence Policy (PEP) of the TR-ESOR-Product Manufacturer, based on<br>•<br>User has administrator rights on the system.<br>•<br>If required, perform identification and authentication.<br>•<br>There are already archived Archival Information Packages without Archive Timestamp in<br>•<br>The**BSI-ERVerify-Tool**is accessible and the tester has access rights to it.||the BSI-**[TR-ESOR-PEPT]**, is present and published.<br>the ECM/long-term storage.|
|Step|Test sequence||Expected Results|Observations|



Bundesamt für Sicherheit in der Informationstechnik 

48 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

|**Identifier**|**Identifier**|**M.3-14**|**M.3-14**|**M.3-14**|
|---|---|---|---|---|
|1.|Use the function for renewal of the Archive Timestamp.||The renewal of the latest Archive Timestamps is done.||
|2.|Request the ERs for the archive object archived or up-<br>dated at the very last.||The ERs must contain the hash value of the archive object and<br>an initial Archive Timestamp. The latestelectronic time-stamp<br>should show the time of calling the function in step 1 or an<br>earlier time.|<br> <br>|
|3.|Check the new Evidence Record of test step 2 with the<br>**BSI-ERVerify-Tool.**||The verification report, returned from the BSI-ERVerify-<br>Tool, shows no errors.<br>Therefore, the solution for re-signing is compatible with the<br>„Evidence Record Syntax“ according to**[RFC4998]**or<br>**[RFC6283]**.||
|4.|Check, if the User manual and**_Preservation Profile_**<br>reference a new Preservation Evidence Policy.||There is a new published Preservation Evidence Policy, doc-<br>umented in user manual of TOT (TR-ESOR-Product) and ref-<br>erenced by the Preservation Profile.||
|5.|Disconnect the Crypto-Module from the ArchiSig-<br>Module and perform this test case again.||The calculation of the initial Archive Timestamp (the hash<br>value) is not possible because ArchiSig itself does not have<br>this functionality.|<br>|
|**Verdict**|||||
||||||



Bundesamt für Sicherheit in der Informationstechnik 

49 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

## **7.3.4 M.3-15 – ArchiSig-Module shall validate requested electronic time-stamps** 

The Testcase M.3-15 is extended by Step 16. 

|**Identifier**|**M.3-15**|
|---|---|
|**Requirement**|MD:A5.1-26<br>M3:A4.5-3<br>M3:A4.7-5<br>M3:A4.8-2<br>M3:A4.8-5<br>_OVR-9.3-01_<br>_OVR-9.3-02_<br>_OVR-9.3-03_<br>_OVR-9.3-04_<br>_OVR-7.5-03_<br>_OVR-7.15-03_|
|**Test Purpose**|The ArchiSig-Module shall in case of generating new electronic time-stamps ensure that the electronic time-stamp contains all information required for validation of<br>the electronic time-stamp, including the advanced digital signatures contained therein.<br>In case of renewal of the hash trees the electronic time-stamp shall contain all information required for validation of the electronic time-stamp, including the ad-<br>vanced digital signatures contained therein.<br>The concluding Archive Timestamp of the hash trees to be renewed will be re-verified for integrity and authenticity before these Archive Timestamps are trans-<br>ferred into a new hash tree or included there. To do so, the digital signature of this Archive Timestamp and the associated certificate chain will be re-verified with<br>the help of the functions of the TR-ESOR-M.2 Cryptographic-Module. An inclusion of this Archive Timestamp in the new hash tree only takes place if this valida-<br>tion has had a positive result.<br>**_If this validation has had a positive result, the renewed Archive Timestamp gives proof of existence of the digital signature of the previous Archive Timestamp_**<br>**_and of the validation data needed to validate the digital signature._**|
|**Configuration**|CONFIG_Common|
|**Pre-test conditions**|•<br>ECM/long-term storage contains already some objects and AOIDs are known.<br>•<br>Tester emulate a TR-ESOR M.2 Cryptographic-Module.|



50 

Bundesamt für Sicherheit in der Informationstechnik 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

||**Identifier**|**M.3-15**|**M.3-15**|**M.3-15**|
|---|---|---|---|---|
|||•<br>Test case M.3-16 was performed successfully.<br>•<br>Some archive objects are already archived.<br>•<br>**_The Signature and Time-Stamp Validation Policy is present and published._**<br>•<br>**_The Cryptographic-Module has a connection to a Trust Service Providers, in order to request the validation of certificates._**<br>•<br>The**BSI-ERVerify-Tool**is accessible and the tester has access rights to it.|||
|Step|Test sequence||Expected Results|Observations|
|1.|Ensure that ArchiSig creates a new Archive Timestamp<br>(e.g. by using a Crypto-Module).||ATS is generated.||
|2.|Request an Evidence Records for one known AOID.||Requesting of an Evidence Record was performed successfully.||
|3.|Check the Evidence Record for information about time-<br>stamps and validations (**including**OCSP Responses,<br>CRL-Reports) of digital signatures of time-stamps.||The information about the time-stamps, its digital signatures and<br>the validation information of the digital signatures are present<br>**(including OCSP Responses with reason code, CRL-Reports)**<br>and show all information required for validation of the time-stamp<br>up to the certificate of a trustworthy root TSP.||
|4.|Start the Hash-tree Renewal process.||The Hash-tree Renewal process was started successfully.||
|5.|Observe the requests of the ArchiSig-Module to the<br>Cryptographic-Module.||ArchiSig will request validation of the very last Archive<br>Timestamp with its digital signature.||
|6.|Emulation: the Cryptographic-Module send negative<br>response.||Sending of negative response was performed successfully.||
|7.|Check the log files of the ArchiSig-Module or observe<br>otherwise the reaction of ArchiSig.||ArchiSig should at least mention the failed validation of the quali-<br>fied time-stamp. The ArchiSig-Module must stop the hash tree<br>renewal and log an exception.||
|8.|Request an Evidence Record for one known AOID.||Requesting of an Evidence Record was performed successfully.||
|9.|Check the Evidence Records by the BSI test tool “ER-<br>Verify”12for information about the Archive Timestamp<br>and digital signature validation (OCSP Responses, CRL-||The check of the tool shows that the ERs resp. the Archive<br>Timestamp Chain is not integer.||



12 The only appropriate tool is the ERVerifyTool from the Federal Office of Information Security see: https://github.com/de-bund-bsi-tr-esor/ERVerifyTool. 

51 

Bundesamt für Sicherheit in der Informationstechnik 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

|**Identifier**|**Identifier**|**M.3-15**|**M.3-15**|**M.3-15**|
|---|---|---|---|---|
||Reports).||||
|10.|Start the Hash-tree Renewal process manually or wait the<br>preconfigured period of time till automatic renewal<br>process.||The Hash-tree Renewal process was started successfully.||
|11.|Observe the requests of the ArchiSig-Module to the<br>Cryptographic-Module.||ArchiSig will request validation of the very last Archive<br>Timestamp with its digital signature.||
|12.|Emulation: the Cryptographic-Module sends positive<br>response.||Sending of positive response was performed successfully.||
|13.|Check the log files of the ArchiSig-Module or observe<br>otherwise the reaction of ArchiSig.||ArchiSig should continue and finish the Hash-tree Renewal.||
|14.|Request an Evidence Record for one known AOID.||Requesting of an Evidence Record was performed successfully.||
|15.|Check the Evidence Records by the appropriate tool12for<br>information about the Archive Timestamp and the digital<br>signature validation of steps 11./12./13. (OCSP Respons-<br>es, CRL-Reports)||The check of the tool shows that the ERs resp. the Archive<br>Timestamp chain for the steps 11./12../13. is integer and for the<br>steps 5./6./7. is not integer.||
|16.|**_Check that the new Archive Timestamp of the Evidence_**<br>**_Records also covers the proof of existence of the previ-_**<br>**_ous Archive Timestamps and of the validation data_**<br>**_needed to validate the digital signature of the previous_**<br>**_Archive Timestamps._**||**_The ERs should contain the new Archive Timestamp as a proof_**<br>**_of existence of the previous Archive Timestamps and of the vali-_**<br>**_dation data needed to validate the digital signature of the previ-_**<br>**_ous Archive Timestamps._**||
|17.|Check the new Evidence Record of test step 2 and 8 with<br>the**BSI-ERVerify-Tool.**||The verification report, returned from the BSI-ERVerify-Tool,<br>shows no errors.<br>Therefore, the solution for re-signing is compatible with the „Evi-<br>dence Record Syntax“ according to**[RFC4998]**or**[RFC6283]**.||
|**Verdict**|||||



52 

Bundesamt für Sicherheit in der Informationstechnik 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

## **7.3.5 M.3-16 – Time-stamps shall be verified prior to renewal** 

The Testcase M.3-16 is extended by Step 14. 

|**Identifier**|**Identifier**|**M.3-16**|**M.3-16**|**M.3-16**|
|---|---|---|---|---|
|**Requirement**||M3:A4.7-2<br>M3:A4.7-3|||
|**Test Purpose**||Check, whether a complete Archive Timestamp Renewal verifies the integrity and authenticity of the Archive Timestamps to be renewed and whether the hash<br>values of these Archive Timestamps are included in the new Archive Timestamp.<br>**_Check, whether a renewed Archive Timestamp gives proof of existence of the digital signature of the previous Archive Timestamp and of the validation data_**<br>**_needed to validate the digital signature._**<br>**_Check, whether an Archive Timestamp to be renewed gives proof of existence of the digital signature of the previous Archive Timestamp and of the validation_**<br>**_data needed to validate the digital signature of the Archive Timestamp to be renewed._**|||
|**Configuration**||CONFIG_Common|||
|**Pre-test conditions**||•<br>Submit several archive objects to the storage and configure the automatic Archive Timestamping in such a way, that several Archive Timestamps will be<br>generated in parallel and they are not “covered” by a superior Archive Timestamp<br>•<br>If required, perform identification and authentication.<br>•<br>The Time-stamp Validation Policy13is present and published in the PEP of the TR-ESOR-Product Manufacturer (TR-ESOR-Product PEP), based on the<br>BSI-**[TR-ESOR-PEPT]**.<br>•<br>The**BSI-ERVerify-Tool**is accessible and the tester has access rights to it.|||
|Step|Test sequence||Expected Results|Observations|
|1.|Request the ERs of these archive objects, which are<br>covered by the mentioned parallel Archive Timestamps.||The hash value of each of the parallel Archive Timestamps is<br>documented in one ERS.||
|2.|Start the complete Archive Timestamp Renewal process.||The complete Archive Timestamp Renewal process was started<br>successfully.||
|3.|Observe the requests of the ArchiSig-Module to the<br>Cryptographic-Module.||ArchiSig will request validation of the very last Archive<br>Timestamp signature.||



13 See http://www.bsi.bund.de/DE/tr-esor/sigpolicy/verify-timestamp 

53 

Bundesamt für Sicherheit in der Informationstechnik 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

||**Identifier**||**M.3-16**||
|---|---|---|---|---|
|4.|Emulation: the Cryptographic-Module sends a negative<br>response.||Sending of negative response was performed successfully.||
|5.|Check the log files of the ArchiSig-Module or observe<br>otherwise the reaction of ArchiSig.||ArchiSig shall mention the failed validation of the qualified time-<br>stamp and stop the complete Archive Timestamp Renewal.||
|6.|Request an Evidence Records for one known AOID.||Requesting of an Evidence Records was performed successfully.||
|7.|Check the Evidence Records (ERs) for information about<br>the Archive Timestamp and its digital signature valida-<br>tion of steps 3./4./5. (OCSP Responses, CRL-Reports).||The ERs should contain no new Archive Timestamp.||
|8.|Start the connection to the true Cryptographic-Module<br>again and start the complete Archive Timestamp Renew-<br>al process.||The complete Archive Timestamp Renewal process was started<br>successfully.||
|9.|Observe the requests of the ArchiSig-Module to the<br>Cryptographic-Module.||ArchiSig will request validation of the very last Archive<br>Timestamp with its digital signature.||
|10.|Emulation: The Cryptographic-Module sends a positive<br>response.||Sending of positive response was performed successfully.||
|11.|Check the log files of the ArchiSig-Module or observe<br>otherwise the reaction of ArchiSig.||ArchiSig should continue and finish the complete Archive<br>Timestamp Renewal.||
|12.|Request an Evidence Records for one known AOID||Requesting of an Evidence Records was performed successfully.||
|13.|Check the Evidence Records for information about the<br>Archive Timestamp and check its digital signature con-<br>cerning the check of steps 9./10./11. (OCSP Responses,<br>CRL-Reports) and the hash algorithm used for this time-<br>stamp.||The ERs should contain the new Archive Timestamp. All the hash<br>values of the parallel Archive Timestamps are covered by the new<br>Archive Timestamp.||
|14.|**_Check that the new Archive Timestamp of the Evidence_**<br>**_Records also covers the proof of existence of the previ-_**<br>**_ous Archive Timestamps and of the validation data_**<br>**_needed to validate the digital signature in the previous_**<br>**_Archive Timestamps._**||**_The ERs should contain the new Archive Timestamp as a proof_**<br>**_of existence of the previous Archive Timestamps and of the vali-_**<br>**_dation data needed to validate the digital signature in the previ-_**<br>**_ous Archive Timestamps._**||
|15.|Check the new Evidence Record of test step 12 with the<br>**BSI-ERVerify-Tool.**||The verification report, returned from the BSI-ERVerify-Tool,<br>shows no errors.||



54 

Bundesamt für Sicherheit in der Informationstechnik 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

**Identifier M.3-16 Verdict** 

55 

Bundesamt für Sicherheit in der Informationstechnik 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

- **7.3.6 M.3-23 – The Process of requesting Export-Import package(s) and the Production Methods of the Export-Import Packages shall be stated in the User Manual and in the published TR-ESOR-Product Preservation Evidence Policy (PEP) of the TOT, based on the BSI-[TR-ESOR-PEPT], and is allowed for authorized clients or preservation services (TR-ESOR Product)** 

This is a new Test Case. 

56 

Bundesamt für Sicherheit in der Informationstechnik 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

|**Identifier**|**Identifier**||**M.3-23**|**M.3-23**|**M.3-23**|**M.3-23**|
|---|---|---|---|---|---|---|
|**Requirement**||M.3:A2.7-1<br>M.3:A2.7-2<br>_OVR-6.1-07_<br>_OVR-6.1-08_<br>_OVR-7.16-01_<br>_OVR-7.16-03_<br>_PRP-8.1-03_|||||
|**Test Purpose**||The test shall verify that the_processof requesting export-import package(s)_and the _production methodsof the export-import package(s)_are allowed for authorized<br>clients or preservation services only as described in the User Manual and in the  PEP of the TR-ESOR-Product Manufacturer, based on the [TR-ESOR-PEPT] of the<br>BSI.|||||
|**Configuration**||CONFIG_Common|||||
|**Pre-test conditions**||•<br>The User Manual is present of TOT (TR-ESOR-Product).<br>•<br>The PEP of the TR-ESOR-Product Manufacturer (TR-ESOR-Product PEP), based on the<br>•<br>Tester has read/write permissions on the middleware.<br>•<br>If required, perform identification and authentication.||||BSI-**[TR-ESOR-PEPT]**, is published.|
|Step|Test sequence|||Expected Results||Observations|
|1.|Check the user manual and the TR-ESOR-Product PEP<br>for information about the _processof requesting export-_<br>_import package(s)_**_and check whether the PSP had_**<br>**_chosen and described one process out of the alterna-_**<br>**_tives:  Alternative 1a) or Alternative 1b), described in_**<br>**_[TR-ESOR-M.3], clause 2.7. (A2.7-1)._**|||The necessary details of the_processof requesting export-import_<br>_package(s) are_stated,**_as expected._**|||
|2.|Check the user manual and the TR-ESOR-Product PEP<br>for information about the _production methodsof the_<br>_export-import package(s)_**_and check whether the PSP_**<br>**_had chosen and described the production method,_**<br>**_described in [TR-ESOR-APP], clause 5.1, (A2.7-2)._**|||The necessary details of the_production methodsof the export-_<br>_import package(s) are_stated in the user manual and the published<br>TR-ESOR-Product PEP.|||
|3.|Check that the TR-ESOR-Product PEP of the “TR-ESOR<br>Product Manufacturer” based on the [TR-ESOR-PEPT]<br>of the BSI.|||On base of BSI-[TR-ESOR-PEPT], the “TR-ESOR Product Manu-<br>facturer” had refined his actual PEP.|||



57 

Bundesamt für Sicherheit in der Informationstechnik 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

|**Identifier**|**Identifier**||**M.3-23**|**M.3-23**|**M.3-23**|
|---|---|---|---|---|---|
|4.|Check and compare_on-site_<br>- the_installed process_of requesting export-import pack-<br>age(s)<br>- the_installed production methods_of the export-import<br>package(s) (e.g. file type, data structure, integrity, etc.),-<br>containing the preserved data, the evidences and all<br>information needed to validate the evidences,<br>with the documentation in the user manual.|||The result of the comparison is that<br>- the process of requesting export-import package(s)**_pursuant to_**<br>**_[TR-ESOR-APP, clause 5.1] (A2.7-1),_**<br>•<br>**_either Alternative 1a_**<br>•<br>**_or Alternative 1b_**<br>**_and_**<br>**_- production method for export-import package(s),e.g. pursuant_**<br>**_to [TR-ESOR-APP, clause 5.1] (A2.7-2),_**<br>•<br>[see also approach 1, TR-ESOR-M.3, clause 2.6 V1.3]<br>•<br>containing the preserved data, the evidences and all<br>information needed to validate the evidences,<br>are implemented and working as documented in the manual and in<br>the TR-ESOR-Product PEP.||
|5.|Check the user manual whether only the preservation<br>client or another authorized preservation service or au-<br>thorized natural or legal persons are allowed_to request_<br>_the export-import package(s), containing the preserved_<br>_data, the evidences and all information needed to vali-_<br>_date the evidences._|||The necessary details concerning who is allowed to request the<br>export-import packages are stated.||
|6.|Check and verify_on-site_<br>- that the delivery of the preservation package(s) only<br>takes place in case of a successful authorization of the<br>legal or natural person or preservation client.|||The verification is successful.<br>It is able to show at least one example of an_export-import package_<br>for each Preservation Evidence Policy in connection with an au-<br>thorized person and with an unauthorized person.||
|**Verdict**||||||
|||||||



58 

Bundesamt für Sicherheit in der Informationstechnik 

## **Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

## **7.3.7 M.3-24 - How the Request for an Export-Import Package can be done with standardised formats, shall be stated in the User Manual and in the published TR-ESOR-Product Preservation Evidence Policy (PEP) of the TOT** 

This is a new Test Case. 

59 

Bundesamt für Sicherheit in der Informationstechnik 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

|**Identifier**|**Identifier**|**M.3-24**|**M.3-24**|**M.3-24**|
|---|---|---|---|---|
|**Requirement**||M3:A2.7-3<br>_OVR-6.2-05_<br>_OVR-7.16-02_|||
|**Test Purpose**||The test shall verify that,_how the request for an export-import package can be done,_are described in the User Manual and in the TR-ESOR-Product PEP.|||
|**Configuration**||CONFIG_Common|||
|**Pre-test conditions**||•<br>User Manual of TOT (TR-ESOR-Product) is present.<br>•<br>The PEP of the TR-ESOR-Product Manufacturer (TR-ESOR-Product PEP ), based on the BSI-**[TR-ESOR-PEPT]**, is published.|||
|Step|Test sequence||Expected Results|Observations|
|1.|Check the user manual and the TR-ESOR-Product PEP<br>for information_how the request for an export-import_<br>_package can be done._||The necessary details,_how the request for an export-import pack-_<br>_age can be done, are_stated.||
|2.|Check the user manual and the TR-ESOR-Product PEP<br>for information concerning a_standardised format for the_<br>_export-import package(s)_||The necessary details of a_standardised format for the export-_<br>_import package(s) are_stated in [TR-ESOR-M.3], clause 2.7 and<br>referenced in the user manual and in the TR-ESOR-Product PEP.||
|3.|Check on-site that<br>there is at least one example of<br>-the request for an export-import Package and<br>-an export-import package for each Preservation Evi-<br>dence Policy<br>and verify that :<br>- a standardised format for the request and for the export-<br>import package(s) is implemented as stated in the user<br>manual and in and the TR-ESOR-Product PEP of the<br>TOT.||A standardised format for the request for an export-import-package<br>and for the export-import package(s) are implemented as stated in<br>the user manual and in and the TR-ESOR-Product PEP.||
|**Verdict**|||||
||||||



60 

Bundesamt für Sicherheit in der Informationstechnik 

## **Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

## **7.3.8 M.3-25 – The TR-ESOR middleware shall keep records of all released export-import packages and shall allow only authorized clients or preservation services to request export-import packages** 

This is a new Test Case. 

61 

Bundesamt für Sicherheit in der Informationstechnik 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

|**Identifier**|**Identifier**|**M.3-25**|**M.3-25**|**M.3-25**|
|---|---|---|---|---|
|**Requirement**||M1:A4.0-3<br>M3:A2.7-4<br>_OVR-7.16-01_<br>_OVR-7.16-04_<br>_PRP-8.1-03_|||
|**Test Purpose**||The test shall verify that_the TR-ESOR middleware shall keep records of all released export-import packages and that only authorized clients or preservation ser-_<br>_vices are allowed to request the export-import package(s)._|||
|**Configuration**||CONFIG_ArchiSafe|||
|**Pre-test conditions**||•<br>User Manual of TOT (TR-ESOR-Product) is present.<br>•<br>Tester has read/write permissions on the middleware.<br>•<br>If required, perform identification and authentication.|||
|Step|Test sequence||Expected Results|Observations|
|1.|Request export-import packages according to [TR-<br>ESOR-M.3], clause 2.7, (A2.7-1) using the credentials of<br>an unauthorised user.||Access is denied.||
|2.|Request export-import packages according to [TR-<br>ESOR-M.3], clause 2.7, (A2.7-1) using the credentials of<br>an authorised user.||Access is granted.||
|3.|Observe the output of the export-import process.||A positive feedback is received. No error message or error code<br>occurs. An AOID is assigned.||
|4.|Check the log files of the ArchiSafe-Module, if there is<br>information about_all released export-import packages_<br>_including_ _the date of the event_and_the criteria that has_<br>_been used to select the set of preservation objects to be_<br>_included in the export-import package_.||There is information about the export-import process as required.||
|**Verdict**|||||
||||||



62 

Bundesamt für Sicherheit in der Informationstechnik 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

## **7.4 Interface S4** 

- **7.4.1 S.4.1-05 – 13 additional Test Steps to “Archive Submission includes the validation of supplemental evidence data and evidence records validation and storage of results”** 

13 additional Test Cases. 

63 

Bundesamt für Sicherheit in der Informationstechnik 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

|**Identifier**|**S.4.1-05**|
|---|---|
|**Requirement**|MD:A5.1-5<br>M1:A4.1-3<br>M1:A4.1-4<br>M2:A5.2-1<br>M2:A5.2-2<br>M2:A5.2-3<br>M3:A4.1-1<br>_OVR-6.2-06_<br>_OVR-7.5-03_<br>_PRP-8.1-05_<br>_PRP-8.1-08_<br>_OVR-9.3-01_<br>_OVR-9.3-02_|
|**Test Purpose**|The testshallverify that the ArchiSafe Module is able to initiate the validation of the supplemental evidence data (e.g. signatures, seals, time-stamps, certificates,<br>revocation lists, ocsp responses, etc.) and technical evidence records  of the XAIPs or BINs before they are stored, -<br>The testshallverify that an error message is received in the case of a failed validation of supplemental evidence data (e.g. signatures, seals, time-stamps, certificates,<br>revocation lists, ocsp responses, etc.) and/or technical evidence records.<br>The testshallverify that it is possible for the ArchiSafe Module to enter all validation results including the associated certificate information into the archive object.<br>The validation resultsshallbe returned either in the form of a Verification Report pursuant to**[TR-ESOR-VR]**or as a supplement of the XAIP container handed<br>over pursuant to**[TR-ESOR-F]**.<br>**_The test shall verify, that if the validation data of digital signatures or time-stamps is submitted by the preservation client, the TR-ESOR-Middlewar automati-_**<br>**_cally shall verify the validation data pursuant to the “signature validation policy“ or “time-stamp validation policy” and shall verify that the submitted valida-_**<br>**_tion data is appropriate, otherwise it should collect and verify the appropriate validation data.._**<br>**_The test shall verify, that if the validation data of digital signatures or time-stamps is not submitted or is not completely submitted by the preservation client, the_**<br>**_TR-ESOR-Middleware automatically shall make its best efforts to collect and verify the validation data pursuant to the “signature validation policy“ or “time-_**<br>**_stamp validation policy”._**<br>**_The test shall verify, that if the validation data of digital signatures or time-stamps is not completely submitted by the preservation client, and it is unable to_**<br>**_collect and verify all the validation data, the TR-ESOR-Middleware automaticallyshallreturn an understandable error message to the preservation client and_**<br>**_handle this case as a case of failure._**|
|**Configuration**|CONFIG_ArchiSafe|



64 

Bundesamt für Sicherheit in der Informationstechnik 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

|**Identifier**|**Identifier**|**S.4.1-05**|**S.4.1-05**|**S.4.1-05**|
|---|---|---|---|---|
|**Pre-test conditions**||•<br>**_User Manual is present._**<br>•<br>**_Preservation Evidence Policy_**(PEP) of the TR-ESOR-Product Manufacturer, based on the BSI-**[TR-ESOR-PEPT]**, is**_present and published._**<br>•<br>**_Preservation Profile is present and published_**<br>•<br>**_“Signature Validation Policy“ and “Time-Stamp Validation Policy”are present._**<br>•<br>The Cryptographic-Module has a connection to a Trust Service Providers, in order to request the validation of certificates.<br>•<br>Tester has Read/Write permissions on the system.<br>•<br>Perform authentication, if necessary<br>•<br>XAIP means “XAIP” or “LXAIP” pursuant to**[TR-ESOR-F]**.<br>•<br>DXAIP means “DXAIP” or “DLXAIP” pursuant to**[TR-ESOR-F].**<br>•<br>XAIP shall be supported, “LXAIP” may be supported, if configured.<br>•<br>BIN isrestrictedto the preservation object formats described in clause 2, Notice 4.<br>•<br>Either the S.4 interface or the TS119512 interface S.512 in the profiling of**[TR-ESOR-TRANS] **shallbe configured.<br>•<br>**_Conditional: The BSI-AIPeIDASValidation-Tool is accessible and the tester has access rights to it._**|||
|Step|Test sequence||Expected Results|Observations|
|1|**_Check the user manua_l ****_or the Preservation Evidence_**<br>**_Policy where to find the actual Preservation Profile._**<br>**_Check the Preservation Profile in order to find a signa-_**<br>**_ture validation policy or a reference to a time-stamp_**<br>**_validation policy._**||**_In the user manual or the Preservation Evidence Policy_**<br>**_there is the information, where to find the actual_**<br>**_Preservation Profile. In the actual profile, the signature_**<br>**_validataion policy and time-stamp validation policy or a_**<br>**_reference to the signature validation policy or time-_**<br>**_stamp validation policy are to be found._**||
|2|**_The automatic validation of the supplemental evidence_**<br>**_data (e.g. signatures, seals, time-stamps, certificates,_**<br>**_revocation lists, OCSP responses with its reason codes,_**<br>**_etc.) and technical evidence records is enabled._**<br>**_Store an XAIP_OK_SIG with appropriate validation_**<br>**_data, collected by the client, to the ECM/Long-term_**<br>**_Storage using the interface function “_****_`ArchiveSub-`_**<br>**_`missionRequest`” or “_****_`PreservePO`”-Request._**||**_The call of the function is possible._**||



65 

Bundesamt für Sicherheit in der Informationstechnik 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

||**Identifier**||**S.4.1-05**||
|---|---|---|---|---|
|3|**_Observe the output of the interface function “_****_`Ar-`_**<br>**_`chiveSubmissionResponse`” or “_****_`PreservePO`”-_**<br>**_Response._**||**_The automatic validation of the supplemental evidence data (e.g._**<br>**_signatures, seals, time-stamps, certificates, revocation lists, OCSP_**<br>**_responses, etc.) was successfully completed pursuant to the signa-_**<br>**_ture validation policy or time-stamp validation policy._**<br>**_The validation results is returned either in the form of a_**<br>**_Verification Report pursuant to [TR-ESOR-VR] or as a_**<br>**_supplement of the XAIP container._**||
|4|**_The automatic validation of the supplemental evidence_**<br>**_data (e.g. signatures, seals, time-stamps, certificates,_**<br>**_revocation lists, OCSP responses, with its reason codes_**<br>**_etc.) and technical evidence records is enabled._**<br>**_Store an XAIP_OK_SIG without validation data to the_**<br>**_ECM/Long-term Storage using the interface function_**<br>**_“_****_`ArchiveSubmissionRequest`” or “_****_`Preserve-`_**<br>**_`PO`”-Request._**||**_The call of the function is possible._**||
|5|**_Observe the output of the interface function “_****_`Ar-`_**<br>**_`chiveSubmissionResponse`” or “_****_`PreservePO`”-_**<br>**_Response._**||**_The automatic validation of the supplemental evidence data (e.g._**<br>**_signatures, seals, time-stamps, certificates, revocation lists, OCSP_**<br>**_responses, etc.) was successfully completed pursuant to the signa-_**<br>**_ture validation policy or time-stamp validation policy._**<br>**_The validation results is enriched in order that an ap-_**<br>**_propriate validation data is returned either in the form_**<br>**_of a Verification Report pursuant to [TR-ESOR-VR] or_**<br>**_as a supplement of the XAIP container._**||
|6|**_The automatic validation of the supplemental evidence_**<br>**_data (e.g. signatures, seals, time-stamps, certificates,_**<br>**_revocation lists, OCSP responses, etc.) and technical_**<br>**_evidence records is enabled._**<br>**_Store an XAIP_OK_SIG without complete validation_**<br>**_data to the ECM/Long-term Storage using the interface_**<br>**_function “_****_`ArchiveSubmissionRequest`” or_**<br>**_“_****_`PreservePO`”-Request._**||**_The call of the function is possible._**||



66 

Bundesamt für Sicherheit in der Informationstechnik 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

||**Identifier**||**S.4.1-05**||
|---|---|---|---|---|
|7|**_Observe the output of the interface function “_****_`Ar-`_**<br>**_`chiveSubmissionResponse`” or “_****_`PreservePO`”-_**<br>**_Response._**||**_The automatic validation of the supplemental evidence data (e.g._**<br>**_signatures, seals, time-stamps, certificates, revocation lists, OCSP_**<br>**_responses, etc.) was successfully completed pursuant to the signa-_**<br>**_ture validation policy or time-stamp validation policy._**<br>**_The validation results is enriched in order that an ap-_**<br>**_propriate validation data is returned either in the form_**<br>**_of a Verification Report pursuant to [TR-ESOR-VR] or_**<br>**_as a supplement of the XAIP container._**||
|8|**_The automatic validation of the supplemental evidence_**<br>**_data (e.g. signatures, seals, time-stamps, certificates,_**<br>**_revocation lists, OCSP responses, etc.) and technical_**<br>**_evidence records is not enabled._**<br>**_Store an XAIP_OK_SIG with not appropriate valida-_**<br>**_tion data, collected by the client, to the ECM/Long-term_**<br>**_Storage using the interface function “_****_`ArchiveSub-`_**<br>**_`missionRequest`” or “_****_`PreservePO`”-Request._**||**_The call of the function is possible._**||
|9|**_Observe the output of the interface function “_****_`Ar-`_**<br>**_`chiveSubmissionResponse`” or “_****_`PreservePO`”-_**<br>**_Response._**||**_The automatic validation of the supplemental evidence data (e.g._**<br>**_signatures, seals, time-stamps, certificates, revocation lists, OCSP_**<br>**_responses, etc.) was not successfully completed._**<br>**_The validation results is returned with an understandable error_**<br>**_message either in the form of a Verification Report pursuant to_**<br>**_[TR-ESOR-VR] or as a supplement of the XAIP container._**||
|10|**_Check that the validation of the digital signatures or the_**<br>**_electronic time-stamps and the validation of the certifi-_**<br>**_cate chain back to a trustworthy root TSP were done_**<br>**_according to the signature validation policy or time-_**<br>**_stamp validation policy._**||**_The validation of the digital signatures or the time-_**<br>**_stamp and the certificate were done according to the_**<br>**_signature validation policy or time-stamp validation_**<br>**_policy._**||
|11|Verify that the configuration of the ArchiSafe-Module<br>enables the automatic validation of the supplemental<br>evidence data (e.g. signatures, seals, time-stamps, certifi-<br>cates, revocation lists, OCSP responses, etc.) and tech-<br>nical evidence records while submitting an archive ob-<br>ject.||The automatic validation of the supplemental evidence data (e.g.<br>signatures, seals, time-stamps, certificates, revocation lists, OCSP<br>responses, etc.) and technical evidence records can be enabled and<br>is enabled.<br>The validation results will be returned either in the form<br>of a Verification Report pursuant to [TR-ESOR-VR] or<br>as a supplement of the XAIP container.||



67 

Bundesamt für Sicherheit in der Informationstechnik 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

||**Identifier**||**S.4.1-05**||
|---|---|---|---|---|
|12|**_Store an XAIP_NOK_SIG or BIN_NOK_SIG with a_**<br>**_revoked public key certificate to the TOT using the_**<br>**_interface function “_****_`ArchiveSubmissionRequest`” _**<br>**_or “_****_`PreservePO`”-Request._**||**_The call of the function is possible._**||
|13|**_Observe the output of the interface function “_****_`Ar-`_**<br>**_`chiveSubmissionResponse`” or “_****_`PreservePO`”-_**<br>**_Response._**||**_A negative feedback will be received in form of a Verification_**<br>**_Report. An error message or error code occurs. The log file con-_**<br>**_tains an error message._**<br>**_The archive object may be stored with an “OCSP with_**<br>**_reason code” as a supplement of the XAIP container_**<br>**_and an AOID may be returned._**||
|14|Store an XAIP_OK_SIG or BIN to the ECM/Long-term<br>Storage using the interface function “`ArchiveSub-`<br>`missionRequest`” or “`PreservePO`”-Request.||The call of the function is possible.||
|15|Observe the output of the interface function “`Archive-`<br>`SubmissionResponse`” or “`PreservePO`”-<br>Response.||A positive feedback is received. No error message or error code<br>occurs. An AOID is assigned to the stored archive object.||
|16|Store an XAIP_NOK_SIG or BIN_NOK_SIG to the<br>TOT using the interface function “`ArchiveSubmis-`<br>`sionRequest`” or “`PreservePO`”-Request.||The call of the function is possible.||
|17|Observe the output of the interface function “`Archive-`<br>`SubmissionResponse`” or “`PreservePO`”-<br>Response.||A negative feedback will be received. An error message or error<br>code occurs. The log file contains an error message.<br>The archive object may be stored and an AOID may be returned.||
|18|Retrieve the XAIP_OK_SIG by using the`“Archiv-`<br>`eRetrievalRequest`” or “`RetrievePO”`with<br>`SubjectOfRetrieval “PO”`” Request function and<br>the AOID from step 3.||The XAIP_OK_SIG is retrieved.||
|19|Check the XAIP_OK_SIG, especially the credential<br>section, whether the supplemental evidence data (e.g.<br>signatures, seals, time-stamps, certificates, revocation<br>lists, OCSP responses, etc.) and technical evidence rec-<br>ords are included.||The certificates, certification validation information and if existent,<br>further supplemental evidence data (e.g. signatures, seals, time-<br>stamps, certificates, revocation lists, OCSP responses, etc.) and<br>technical evidence records are included in the retrieved<br>XAIP_OK_SIG.||



68 

Bundesamt für Sicherheit in der Informationstechnik 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

||**Identifier**||**S.4.1-05**||
|---|---|---|---|---|
|20|Check whether the XAIP_OK_SIG is positively validat-<br>ed, e.g. using the**BSI-AIPeIDASValidation**-Tool.||If implemented and running, the**BSI-AIPeIDASValidation**-Tool<br>returns a Verification Report with a positive result. The schema of<br>the XAIP_OK_SIG and the Signatures or Seals or Time-Stamps<br>are positively tested pursuant to**[TR-ESOR-F]**.||
|21|If archived/stored, retrieve the XAIP_NOK_SIG by<br>using the “`ArchiveRetrievalRequest`” or “`Re-`<br>`trievePO`” with`SubjectOfRetrieval “PO”`”<br>Request function and the AOID from step 5.||The XAIP_NOK_SIG is retrieved.||
|22|Check the XAIP_NOK_SIG, especially the credential<br>section, whether the supplemental evidence data (e.g.<br>signatures, seals, time-stamps, certificates, revocation<br>lists, OCSP responses, etc.) and technical evidence rec-<br>ords are included.||The certificates, certification validation information and if existent,<br>further supplemental evidence data (e.g. signatures, seals, time-<br>stamps, certificates, revocation lists, OCSP responses, etc.) and<br>technical evidence records are included in the retrieved<br>XAIP_NOK_SIG.||
|23|Check whether the XAIP_NOK_SIG is positively vali-<br>dated, e.g. by using the**BSI-AIPeIDASValidation**-Tool.||If implemented and running, the**BSI-AIPeIDASValidation**-Tool<br>returns a Verification Report with a negative test result.||
|24|Retrieve the XAIP(BIN) by using the “`Archiv-`<br>`eRetrievalReques`t” or “`RetrievePO`” with<br>`SubjectOfRetrieval “PO”`” Request function and<br>the AOID from step 7.||The XAIP(BIN) is retrieved in the XAIP format including all<br>assigned metadata and the BIN data as content.||
|25|Check the retrieved XAIP and all the metadata whether<br>the supplemental evidence data (e.g. signatures, seals,<br>time-stamps, certificates, revocation lists, OCSP re-<br>sponses, etc.) and technical evidence records are includ-<br>ed.||The certificates, certification validation information and the  sup-<br>plemental evidence data (e.g. signatures, seals, time-stamps, certif-<br>icates, revocation lists, OCSP responses, etc.) and technical evi-<br>dence records are included in the retrieved XAIP||
|26|If archived/stored, retrieve the BIN_NOK_SIG by using<br>the “`ArchiveRetrievalReques`t” or “`Retrieve-`<br>`PO`” with`SubjectOfRetrieval “PO”`” Request<br>function and the AOID from step 9.||The BIN_NOK_SIG is retrieved in the XAIP format including all<br>assigned metadata and the BIN data as content.||
|27|Check the retrieved XAIP and all the metadata whether<br>the supplemental evidence data (e.g. signatures, seals,<br>time-stamps, certificates, revocation lists, OCSP re-<br>sponses, etc.) and technical evidence records are includ-<br>ed.||The certificates, certification validation information and the   sup-<br>plemental evidence data (e.g. signatures, seals, time-stamps, certif-<br>icates, revocation lists, OCSP responses, etc.) and technical evi-<br>dence records are included in the retrieved XAIP||



69 

Bundesamt für Sicherheit in der Informationstechnik 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

||**Identifier**||**S.4.1-05**||
|---|---|---|---|---|
|28|Store an XAIP_OK_SIG_OK_ER to the TOT using the<br>interface function “`ArchiveSubmissionRequest`”<br>or “`PreservePO`”-Request.||The call of the function is possible.||
|29|Observe the output of the interface function “Archive-<br>SubmissionResponse” or “PreservePO”-Response.||A positive feedback is received. No error message or error code<br>occurs. An AOID is assigned to the stored archive object.||
|30|Retrieve the XAIP_OK_SIG_OK_ER by using the “`Ar-`<br>`chiveRetrievalRequest`” or “`RetrievePO`”<br>with`SubjectOfRetrieval “PO”`” Request func-<br>tion and the AOID from step 15.||The XAIP_OK_SIG_OK_ER is retrieved.||
|31|Check the XAIP_OK_SIG_OK_ER, especially the cre-<br>dential section, whether the supplemental evidence data<br>(e.g. signatures, seals, time-stamps, certificates, revoca-<br>tion lists, OCSP responses, etc.) and evidence record<br>validation information are included.||The certificates, certification validation information and the sup-<br>plemental evidence data (e.g. signatures, seals, time-stamps, certif-<br>icates, revocation lists, OCSP responses, etc.) and evidence record<br>validation information are included in the retrieved<br>XAIP_OK_SIG_OK_ER.||
|32|Check whether the XAIP_OK_SIG_OK_ER is positively<br>validated, e.g by using the**BSI-AIPeIDASValidation**-<br>Tool.||If implemented, the**BSI-AIPeIDASValidation**-Tool returns a<br>Verification Report with a positive result. The schema of the<br>XAIP_OK_SIG_OK_ER and the Signatures or Seals or Time-<br>Stamps are positively tested pursuant to**[TR-ESOR-F]**.||
|33|Store an XAIP_NOK_SIG_OK_ER to the TOT using the<br>interface function “`ArchiveSubmissionRequest`”<br>or “`PreservePO`”-Request.||The call of the function is possible.||
|34|Observe the output of the interface function “Archive-<br>SubmissionResponse” or “`PreservePO`”-Response.||A negative feedback will be received. An error message or error<br>code occurs. The log file contains an error message with a digital<br>signature and an evidence record.<br>The archive object may be stored and an AOID may be returned.||
|35|If archived/stored, retrieve the<br>XAIP_NOK_SIG_OK_ER by using the “`Archiv-`<br>`eRetrievalRequest`” or “`RetrievePO`” with<br>`SubjectOfRetrieval “PO”`” Request function and<br>the AOID from step 19.||The XAIP_NOK_SIG_OK_ER is retrieved in the XAIP format.||



Bundesamt für Sicherheit in der Informationstechnik 

70 

## **Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

|**Identifier**|**Identifier**|**S.4.1-05**|**S.4.1-05**|**S.4.1-05**|
|---|---|---|---|---|
|36|Check whether the XAIP_NOK_SIG_OK_ER is posi-<br>tively validated, e.g. by using the**BSI-**<br>**AIPeIDASValidation**-Tool.||If implemented, the**BSI-AIPeIDASValidation**-Tool returns a<br>Verification Report with a negative test result.||
|37|Check the retrieved XAIP and all the metadata whether<br>the supplemental evidence data (e.g. signatures, seals,<br>time-stamps, certificates, revocation lists, OCSP re-<br>sponses, etc.) and the evidence record validation infor-<br>mation are included.||The certificates, certification validation information and the  sup-<br>plemental evidence data (e.g. signatures, seals, time-stamps, certif-<br>icates, revocation lists, OCSP responses, etc.) and the evidence<br>record validation information are included in the retrieved XAIP||
|38|Store an XAIP_NOK_ER to the TOT using the interface<br>function “`ArchiveSubmissionRequest`” or “`Pre-`<br>`servePO`”-Request.||The call of the function is possible.||
|39|Observe the output of the interface function “`Archive-`<br>`SubmissionResponse`” or “`PreservePO`”-<br>Response.||A negative feedback will be received. An error message or error<br>code occurs. The log file contains an error message with an evi-<br>dence record.<br>The archive object may be stored and an AOID may be returned.||
|40|If archived/stored, retrieve the XAIP_NOK_ER by using<br>the “`ArchiveRetrievalRequest`” or “`Re-`<br>`trievePO”`with`SubjectOfRetrieval “PO”`”<br>Request function and the AOID from step 23.||The XAIP_NOK_ER is retrieved in the XAIP format.||
|41|Check the retrieved XAIP and all the metadata whether<br>the supplemental evidence data (e.g. signatures, seals,<br>time-stamps, certificates, revocation lists, OCSP re-<br>sponses, etc.) and technical evidence and the evidence<br>record validation information are included.||The certificates, certification validation information and the  sup-<br>plemental evidence data (e.g. signatures, seals, time-stamps, certif-<br>icates, revocation lists, OCSP responses, etc.) and technical evi-<br>dence and the evidence record validation information are included<br>in the retrieved XAIP||
|42|Check whether the XAIP_NOK_ER is positively validat-<br>ed, e.g. by using the**BSI-AIPeIDASValidation**-Tool.||If implemented, the**BSI-AIPeIDASValidation**-Tool returns a<br>Verification Report with a negative test result.||
|43|**Conditional:**_If LXAIP is implemented,_test steps from<br>No. 1 to No. 35 are to be repeated for LXAIP.||See expected results of the test cases from No. 1 to No. 25 for<br>LXAIP.||
|**Verdict**|||||
||||||



Bundesamt für Sicherheit in der Informationstechnik 

71 

**TR-ESOR-Profil-APP: Appendix zu TR-ESOR V1.2.1 und TR-ESOR V1.2.2** 

Bundesamt für Sicherheit in der Informationstechnik 

72 

**Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung** 

## **8. Generelle Änderung von TR-ESOR-C.1 V1.2.1 seit 30.7.2019 unabhängig davon, ob der Einsatzes eines TR-** 

**ESOR-Produktes in einen Bewahrungsdienst gemäß** [ETSI TS 119 511] **angestrebt wird und die Prüferleichterungen gemäß** [ASS 119 511] **in Anspruch genommen werden sollen** 

Der Testfall „M.1-01 – ArchiSafe-module satisfies the requirements of PP-0049“ in Kapitel 4.2.1 des Anhangs TR-ESOR-C.1 V1.2.1 wurde am 30.07.2019 im TR-ESOR-Anhang TR-ESOR-C.1 gestrichen, siehe auch den BSI-Link „bsi.bund.de/tr-esor“: 

„Das im Jahr 2014 publizierte Common Criteria Protection Profile (ACMPP): BSI-CC-PP-0049-2014 ist historisch und wird nicht mehr gepflegt und nicht auf die eIDAS-Verordnung und die neuen ETSI Preservation Standards ETSI TS 119 511 und ETSI TS 119 512 umgestellt. Daher entfallen alle in der TR03125 V1.2.1 und TR-03125 V1.2.2 enthaltenen Anforderungen und Referenzen bezüglich "Common Criteria Protection Profile (ACMPP)", insbesondere die Anforderungen bzgl. TR-ESOR M1:A3.3-1 und TR-ESOR C.1:M.1-01.“ 

Bundesamt für Sicherheit in der Informationstechnik 

73 


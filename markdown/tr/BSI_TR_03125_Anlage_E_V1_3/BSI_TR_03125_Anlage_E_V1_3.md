## BSI Technische Richtlinie 03125 Beweiswerterhaltung kryptographisch signierter Dokumente 

Anlage TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks und ETSI TS 119 512 Bezeichnung Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks Kürzel BSI TR-ESOR-E Version 1.3 (auf Basis der eIDAS-Verordnung und der ETSI Preservation Standards mit einem neuen Zertifizierungsschema) Datum 31.03.2022 

## Änderungshistorie 

|Version|Datum|Name|Beschreibung|
|---|---|---|---|
|1.3|31.03.2022|BSI|TR-ESOR-E|
|||||



Tabelle 1: Änderungshistorie 

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn Tel.: +49 22899 9582-0 E-Mail:  tresor@bsi.bund.de Internet: https://www.bsi.bund.de © Bundesamt für Sicherheit in der Informationstechnik 2022 

Bundesamt für Sicherheit in der Informationstechnik 

2 

Inhalt 

## Inhalt 

|1.|Einführung.......................................................................................................................................................................................... 6|Einführung.......................................................................................................................................................................................... 6|
|---|---|---|
|2.|Überblick ............................................................................................................................................................................................. 9||
|3.|Funktionen der ArchiSafe-Schnittstelle (TR-S.4) ............................................................................................................. 14||
||3.1|Funktion: ArchiveSubmission ....................................................................................................................................... 14|
||3.1.1|Eingabeparameter: ArchiveSubmissionRequest ............................................................................................... 15|
||3.1.2|Ausgabeparameter: ArchiveSubmissionResponse ........................................................................................... 18|
||3.2|Funktion: ArchiveUpdate ................................................................................................................................................ 20|
||3.2.1|Eingabeparameter: ArchiveUpdateRequest ........................................................................................................ 20|
||3.2.2|Ausgabeparameter: ArchiveUpdateResponse .................................................................................................... 21|
||3.3|Funktion: ArchiveRetrieval ............................................................................................................................................. 22|
||3.3.1|Eingabeparameter: ArchiveRetrievalRequest ..................................................................................................... 23|
||3.3.2|Ausgabeparameter: ArchiveRetrievalResponse ................................................................................................. 25|
||3.4|Funktion: ArchiveEvidence ............................................................................................................................................ 27|
||3.4.1|Eingabeparameter: ArchiveEvidenceRequest .................................................................................................... 27|
||3.4.2|Ausgabeparameter: ArchiveEvidenceResponse ................................................................................................ 29|
||3.5|Funktion: ArchiveDeletion ............................................................................................................................................. 31|
||3.5.1|Eingabeparameter: ArchiveDeletionRequest ..................................................................................................... 31|
||3.5.2|Ausgabeparameter: ArchiveDeletionResponse ................................................................................................. 32|
||3.6|Funktion: ArchiveData ...................................................................................................................................................... 32|
||3.6.1|Eingabeparameter: ArchiveDataRequest ............................................................................................................. 33|
||3.6.2|Ausgabeparameter: ArchiveDataResponse.......................................................................................................... 35|
||3.7|Funktion: Verify ................................................................................................................................................................... 36|
||3.7.1|Eingabeparameter: VerifyRequest........................................................................................................................... 37|
||3.7.2|Ausgabeparameter: VerifyResponse ....................................................................................................................... 40|
||3.8|Funktion: RetrieveInfo ..................................................................................................................................................... 41|
||3.8.1|Eingabeparameter: RetrieveInfoRequest ............................................................................................................. 41|
||3.8.2|Ausgabeparameter: RetrieveInfoResponse ......................................................................................................... 42|
||3.9|Funktion: ArchiveTrace .................................................................................................................................................... 43|
||3.9.1|Eingabeparameter: ArchiveTraceRequest ............................................................................................................ 43|
||3.9.2|Ausgabeparameter: ArchiveTraceResponse ........................................................................................................ 44|
|4.|Funktionen der Preservation-API gemäß ETSI TS 119 512 in der Profilierung [TR-ESOR-TRANS] .......... 46||
||4.1|Vergleich der TR-S.512- mit der TR-S.4-Schnittstelle ......................................................................................... 46|
|5.|Funktionen der internen Schnittstellen ............................................................................................................................... 48||
||5.1|TR-S.1 (ArchiSafe-Modul – Krypto-Modul) ............................................................................................................. 48|
||5.1.1|Prüfung<br>von<br>digitalen<br>Signaturen,<br>beweisrelevanten<br>Daten,<br>Beweisdaten<br>und|
||Archivdatenobjekten .................................................................................................................................................................... 48||



Bundesamt für Sicherheit in der Informationstechnik 

Inhalt 

||5.1.2|Anforderung einer digitalen Signatur ................................................................................................................... 48|Anforderung einer digitalen Signatur ................................................................................................................... 48|Anforderung einer digitalen Signatur ................................................................................................................... 48|
|---|---|---|---|---|
||5.2|TR-S.2 (ArchiSig-Modul – ECM-/Langzeitspeichersystem) .............................................................................. 50|||
||5.2.1|Speichern eines Archivdatenobjektes .................................................................................................................... 50|||
||5.2.2|Ergänzen einer neuen|Version eines Archivdatenobjektes .......................................................................... 50||
||5.2.3|Auslesen von Archivdatenobjekten ........................................................................................................................ 50|||
||5.3|TR-S.3 (ArchiSig-Modul – Krypto-Modul)................................................................................................................ 51|||
||5.3.1|Anfordern eines (qualifizierten) Zeitstempels .................................................................................................... 51|||
||5.3.2|Prüfen eines (qualifizierten) Zeitstempels ........................................................................................................... 52|||
||5.3.3|Berechnung eines Hashwertes .................................................................................................................................. 54|||
||5.4|TR-S.5 (ArchiSafe-Modul / Krypto-Modul – ECM-Langzeitspeichersystem) ............................................ 56|||
||5.4.1|Abfrage beweiswerterhaltend archivierter Daten ............................................................................................ 56|||
||5.4.2|Löschen von Archivdatenobjekten ......................................................................................................................... 57|||
||5.4.3|Abfrage diskreter Datenobjekte ............................................................................................................................... 57|||
||5.5|TR-ESOR-S.6 (ArchiSafe-Modul – ArchiSig-Modul) ............................................................................................ 57|||
||5.5.1|Beweiswerterhaltende Archivierung elektronischer Daten ......................................................................... 57|||
||5.5.2|Ergänzen einer neuen|Version eines Archivdatenobjektes .......................................................................... 57||
||5.5.3|Rückgabe technischer|Beweisdaten ....................................................................................................................... 57||
|6.|Upload/Download-Schnittstelle||.................................................................................................................................................. 58||
||6.1|Upload-Funktion ................................................................................................................................................................. 58|||
||6.1.1|Upload-Anfrage .............................................................................................................................................................. 58|||
||6.1.2|Upload-Antwort ............................................................................................................................................................. 58|||
||6.2|Download-Funktion .......................................................................................................................................................... 59|||
||6.2.1|Download-Anfrage ........................................................................................................................................................ 60|||
||6.2.2|Download-Antwort ....................................................................................................................................................... 60|||
|7.|Fehlercodes ....................................................................................................................................................................................... 62||||
|8.|Spezifikation einer Webservice-basierten Schnittstelle ................................................................................................ 65||||
||8.1|Spezifikation der Aufruf- und Rückgabeparameter als XML-Schema.......................................................... 65|||
||8.2|WSDL-Spezifikation der Schnittstelle TR-S.4||......................................................................................................... 70|



## Abbildungen 

Abbildung 1: Schematische Darstellung der IT-Referenzarchitektur mit TR-S.4. ............................................ 7 Abbildung 2: Schematische Darstellung der IT-Referenzarchitektur mit TR-S.512. ........................................ 7 Abbildung 3: Umsetzung der IT-Referenzarchitektur auf Basis des eCard-API-Frameworks. ....................... 10 Abbildung 4: Umsetzung der IT-Referenzarchitektur auf Basis [ETSI TS 119 512]. ..................................... 10 

## Tabellen 

Tabelle 1: Änderungshistorie ................................................................................................................................................................. 2 Tabelle 2: Bewahrungstechniken ....................................................................................................................................................... 12 

Bundesamt für Sicherheit in der Informationstechnik 

4 

Inhalt 

Tabelle 3: Vergleich ETSI TS 119 512 (prof. [TR-ESOR-TRANS]) Preservation-API mit TR-ESOR-S.4Schnittstelle ................................................................................................................................................................................................ 47 Tabelle 4: Zusätzliche Fehlercodes. ................................................................................................................................................... 64 

Bundesamt für Sicherheit in der Informationstechnik 

5 

Einführung 

## 1. Einführung 

Ziel der Technischen Richtlinie „Beweiswerterhaltung kryptographisch signierter Dokumente“ ist die Spezifikation sicherheitstechnischer Anforderungen für den langfristigen Beweiswerterhalt von kryptographisch signierten elektronischen Dokumenten und Daten nebst zugehörigen elektronischen Verwaltungsdaten (Metadaten).[1] 

Eine für diese Zwecke definierte Middleware (TR-ESOR-Middleware) im Sinn dieser Richtlinie umfasst alle diejenigen Module ( M ) und Schnittstellen ( S) , die zur Sicherung und zum Erhalt der Authentizität und zum Nachweis der Integrität der aufbewahrten Dokumente und Daten eingesetzt werden. 

Die im Hauptdokument dieser Technischen Richtlinie vorgestellte Referenzarchitektur besteht aus den nachfolgend beschriebenen Schnittstellen, Funktionen und logischen Einheiten: 

- der TR-S.4 oder TS119512-Eingangs-Schnittstelle TR-S.512 in der Profilierung [TR-ESORTRANS] der TR-ESOR-Middleware, die dazu dient, die TR-ESOR-Middleware in die bestehende IT- und Infrastrukturlandschaft einzubetten; 

- dem „ArchiSafe-Modul“ (vgl. [TR-ESOR-M.1] ), welches den Informationsfluss in der Middleware regelt, die Sicherheitsanforderungen an die Schnittstellen zu den IT-Anwendungen umsetzt und für eine Entkopplung von Anwendungssystemen und ECM-/Langzeitspeicher sorgt; 

- dem „Krypto-Modul“ (vgl. [TR-ESOR-M.2] ) nebst den zugehörigen Schnittstellen TR-S.1 und TR-S.3, das alle erforderlichen Funktionen zur Berechnung von Hashwerten, Prüfung elektronischer Signaturen bzw. Siegel bzw. Zeitstempel, zur Nachprüfung elektronischer Zertifikate und zum Einholen qualifizierter Zeitstempel sowie (optional) elektronischer Signaturen bzw. Siegel für die Middleware zur Verfügung stellt. Darüber hinaus kann es Funktionen zur Ver- und Entschlüsselung von Daten und Dokumenten zur Verfügung stellen; 

- dem „ArchiSig-Modul“ (vgl. [TR-ESOR-M.3] ) mit der Schnittstelle TR-S.6, das die erforderlichen Funktionen für die Beweiswerterhaltung der digital signierten Unterlagen bereitstellt; 

- einem ECM-/Langzeitspeicher mit den Schnittstellen TR-S.2 und TR-S.5, der die physische Archivierung/Aufbewahrung und auch das Speichern der beweiswerterhaltenden Zusatzdaten übernimmt. 

   - Dieser ECM-/Langzeitspeicher ist nicht mehr direkt Teil der Technischen Richtlinie, gleichwohl werden über die beiden Schnittstellen, die noch Teil der TR-ESOR-Middleware sind, Anforderungen daran gestellt. 

Ebenso wenig ist die Applikationsschicht, die auch einen XML-Adapter enthalten kann, direkter Teil der Technischen Richtlinie, auch wenn dieser XML-Adapter als Teil einer Middleware implementiert werden kann. 

Die empfohlene IT-Referenzarchitektur ist in Abbildung 1 und Abbildung 2 dargestellt und besteht im Wesentlichen aus den in [TR-ESOR] , Kap. 7 grob beschriebenen logischen Komponenten und Schnittstellen. Die Grafik zeigt zudem die externen Komponenten und Systeme an, die das Bild vervollständigen. Grundsätzlich wird als obere Schnittstelle der TR-ESOR-Middleware entweder die TR-S.4-Schnittstelle gemäß [TR-ESOR-E] , die in Abbildung 1 dargestellt ist, oder die TR-S.512-Schnittstelle gemäß [ETSI TS 119 512] in der Profilierung [TR-ESOR-TRANS] , die in Abbildung 2 gezeigt wird, unterstützt. 

1Siehe Hinweis 1 

Bundesamt für Sicherheit in der Informationstechnik 

Einführung 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_3/BSI_TR_03125_Anlage_E_V1_3.pdf-0007-01.png)


Abbildung 1: Schematische Darstellung der IT-Referenzarchitektur mit TR-S.4. 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_3/BSI_TR_03125_Anlage_E_V1_3.pdf-0007-03.png)


Abbildung 2: Schematische Darstellung der IT-Referenzarchitektur mit TR-S.512. 

Bundesamt für Sicherheit in der Informationstechnik 

7 

Einführung 

Die in Abbildung 1 bzw. Abbildung 2 dargestellte IT-Referenzarchitektur orientiert sich an der ArchiSafe Referenzarchitektur und soll die logische (funktionale) Interoperabilität künftiger Produkte mit den Zielen und Anforderungen der Technischen Richtlinie ermöglichen und unterstützen. 

Sofern der optionale XML-Adapter und/oder der optionale TR-ESOR-512-Transformator[2] vorhanden sind, können beide in folgenden Ausprägungen vorliegen: 

- Jeweils eigenständige Komponente mit Schnittstellen zur Applikation sowie zum ArchiSafe-Modul 

- Jeweils eigenständige Komponente, jedoch Teil der Applikation mit Schnittstelle zum ArchiSafeModul 

- XML-Adapter und TR-ESOR-512-Transformator als eine gemeinsame Komponente, die beide Teile enthält mit Schnittstellen zur Applikation sowie zum ArchiSafe-Modul 

- XML-Adapter und TR-ESOR-512-Transformator als eine gemeinsame Komponente, die beide Teile enthält und Teil der Applikation ist, mit Schnittstelle zum ArchiSafe-Modul. 

Der “ETSI TS119512 TR-ESOR Transformator” ermöglicht Bewahrungsdiensten gemäß [eIDAS-VO] , empfangene ETSI TS119512 (V1.1.2) Nachrichten[3] in TR-S4 Nachrichten zu transformieren. Diese Nachrichten können dann an ein angeschlossenen TR-ESOR-System[4] geschickt werden, ohne irgendwelche Änderungen dieses TR-ESOR-Systems. 

Der Einsatz des TR-ESOR-512-Transformators wird EMPFOHLEN, sofern das TR-ESOR-Produkt mit einer TR-S.4-Schnittstelle in Europa zum Einsatz kommt und Interoperabilität mit europäischen (qualifizierten) Bewahrungsdiensten und Bewahrungsprodukten hergestellt werden soll. 

Diese Technische Richtlinie ist modular aufgebaut und spezifiziert in einzelnen Anlagen zum Hauptdokument die funktionalen und sicherheitstechnischen Anforderungen an die erforderlichen ITKomponenten und Schnittstellen der TR-ESOR-Middleware. Die Spezifikationen sind strikt plattform-, produkt-, und herstellerunabhängig. 

Das vorliegende Dokument trägt die Bezeichnung „Anlage TR-ESOR-E“ und konkretisiert die TR-ESORspezifischen Schnittstellen TR-S.4 auf Basis des in der [TR-03112] spezifizierten eCard-API-Frameworks sowie die TR-S.512-Schnittstelle auf Basis von [ETSI TS 119 512] in der Profilierung [TESOR-TRANS] . 

> 2 - Siehe ETSI TS 119512 TR ESOR Transformator unter einer Open Source Lizenz. 

> 3 In der Profilierung von [TR-ESOR-TRANS] 

> 4 - - Siehe https://www.bsi.bund.de/EN/tr esor oder https://www.bsi.bund.de/DE/tr esor 

Bundesamt für Sicherheit in der Informationstechnik 

8 

Überblick 

## 2. Überblick 

- (Α2.0−1) Als ArchiSafe-Schnittstelle muss entweder die nachfolgend spezifizierte TR-S.4-Schnittstelle implementiert sein oder die TR-S.512-Schnittstelle gemäß [ETSI TS 119 512] in der Profilierung [TRESOR-TRANS] . 

- (Α2.0−2) Falls die TR-S.4-Schnittstelle unterstützt wird, dann müssen die im Folgenden näher aufgeführten Funktionen mit den hier beschriebenen Parameterkonstellationen unterstützt werden: 

   - `ArchiveSubmission` (siehe Abs. 3.1) 

   - `ArchiveUpdate` (siehe Abs. 3.2) 

   - `ArchiveRetrieval` (siehe Abs. 3.3) 

   - `ArchiveEvidence` (siehe Abs. 3.4) 

   - `ArchiveDeletion` (siehe Abs. 3.5) 

   - `Verify` (siehe Abs. 3.7) 

   - `RetrieveInfo` (siehe Abs. 3.8). 

Falls die TR-S.4-Schnittstelle unterstützt wird, dann sollen in der Schnittstelle TR-S.4 die folgenden im vorliegenden Dokument näher aufgeführten Funktionen mit den hier beschriebenen Parameterkonstellationen unterstützt werden: 

   - `ArchiveData` (siehe Abs. 3.6) 

   - `ArchiveTrace` (siehe Abs. 3.9) 

- (Α2.0−3) Falls die TR-S.512-Schnittstelle unterstützt wird, dann müssen die im Folgenden näher aufgeführten Funktionen mit den in [ETSI TS 119 512] in der Profilierung [TR-ESOR-TRANS] beschriebenen Parameterkonstellationen unterstützt werden: 

   - `PreservePO` (siehe [TR-ESOR-TRANS] , Abs. 3.2) 

   - `UpdatePOC` (siehe [TR-ESOR-TRANS] , Abs. 3.3) 

   - `RetrievePO` (siehe [TR-ESOR-TRANS] , Abs. 3.4) 

   - `DeletePO` (siehe [TR-ESOR-TRANS] , Abs. 3.5) 

   - `ValidateEvidence` (siehe [TR-ESOR-TRANS] , Abs. 3.6) 

   - `RetrieveInfo` (siehe [TR-ESOR-TRANS] , Abs. 3.1). 

Falls die TR-S.512-Schnittstelle unterstützt wird, dann sollen in der Schnittstelle TR-S.512 die folgenden im vorliegenden Dokument näher aufgeführten Funktionen mit den dort beschriebenen Parameterkonstellationen unterstützt werden: 

- `Search` (siehe [TR-ESOR-TRANS] , Abs. 3.7) 

- `RetrieveTrace` (siehe [ETSI TS 119 512] Abs. 5.3.7). 

Bundesamt für Sicherheit in der Informationstechnik 

9 

Überblick 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_3/BSI_TR_03125_Anlage_E_V1_3.pdf-0010-01.png)


Abbildung 3: Umsetzung der IT-Referenzarchitektur auf Basis des eCard-API-Frameworks. 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_3/BSI_TR_03125_Anlage_E_V1_3.pdf-0010-03.png)


Abbildung 4: Umsetzung der IT-Referenzarchitektur auf Basis [ETSI TS 119 512]. 

Wie in Abbildung 1 und Abbildung 3 angedeutet, werden bei der vollständigen Umsetzung der ITReferenzarchitektur auf Basis des eCard-API-Frameworks 

1. die Schnittstellen des Krypto-Moduls gemäß des eCard-API-Frameworks (Technische Richtlinie des [TR-03112] ) realisiert undauch die Schnittstellen des ArchiSafe-, ArchiSig-Modul und ECM- 

Bundesamt für Sicherheit in der Informationstechnik 

10 

Überblick 

/Langzeitspeichers nutzen die gleichen grundlegenden Schnittstellentypen ( `dss:RequestBaseType` und `dss:ResponseBaseType` ) aus [OASIS-DSS] , die auch bei den Signaturund Verschlüsselungsfunktionen aus [eCard-2] genutzt werden. 

Die URI-Fehlercodes in den Rückgaben der nicht bereits in der Technischen Richtlinie des [TR-03112] - definierten Funktionen haben das Präfix http://www.bsi.bund.de/tr esor/api/1.3, welches um entsprechende Bezeichner ergänzt wird. Dieser Namensraum ist in den visualisierten XML-Strukturen am Kürzel „ `tr` “ erkennbar. 

Im Fall der Abbildung 2 und Abbildung 4 wird die obere Schnittstelle gemäß [ETSI TS 119 512] , Kap. 5 auf Basis von [OASIS DSS-X] , Core 2.0 realisiert. 

Falls die in diesem Dokument beschriebenen Schnittstellen und Funktionen asynchron genutzt werden sollen, kann dies unter Verwendung der hierfür vorgesehenen Mechanismen aus [OASIS-Async] realisiert werden. 

In den folgenden Abschnitten findet sich eine XML-basierte Spezifikation der Funktionen zur Beweiswerterhaltung kryptographisch signierter Dokumente. Hierbei werden die Funktionen der ArchiSafeSchnittstelle (TR-S.4) in Abschnitt 3 und der TR-S.512-Schnittstelle in Abschnitt 4 spezifiziert. In Abschnitt 5 findet sich eine Beschreibung der internen Schnittstellen der TR-ESOR-Middleware, die auf die vorherige Spezifikation der Funktionen in Abschnitt 3 Bezug nimmt. In Abschnitt 6 sind die verwendeten Fehlercodes zusammengefasst und näher erläutert und in Abschnitt 7 finden sich schließlich die normativen XMLSchema- und WSDL-Spezifikationen für die in Abschnitt 3 spezifizierte ArchiSafe-Schnittstelle (TR-S.4). 

## HINWEIS 1 

In der vorliegenden TR-ESOR-Version1.3 werden die drei Begriffe „(beweiswerterhaltende) Langzeitspeicherung“, „(beweiswerterhaltende) Bewahrung“ und „(beweiswerterhaltende) Archivierung“ synonym verwendet. Ebenso werden die drei Begriffe „ Archivinformationspaket (AIP) “, „ Archivinformationscontainer“ und „ Archivdatenobjekt “ sowie die Begriffe „aufbewahren“ und „archivieren“ synonym verwendet. 

## HINWEIS 2 

TR-ESOR spezifiziert ein Bewahrungsprodukt (engl. Preservation Product) gemäß [ETSI SR 019 510], [ETSI TS 119511] und [ETSI TS 119512] und [eIDAS-VO] . 

Die TR 03125 TR-ESOR ist in [ETSI SR 019510] in dem Kapitel 4.7.3 und 5.2 und B3.2 beschrieben. Die in TRESOR erforderlichen grundlegenden Bewahrungstechniken, z. B. das Bewahrungsprotokoll, das Beweisdaten-Format Evidence Record, die Archivdatenobjekt-Format (L)XAIP und ASiC-AIP sind in der ETSI-Publikation [ETSI TS 119512] als normative Elemente enthalten. 

## HINWEIS 3 

Die obere TR-ESOR-Eingangs-Schnittstelle TR-S.4 oder die TS119512-Eingangsschnittstelle TR-S.512 gemäß der „Preservation-API“ in [ETSI TS 119 512] in der Profilierung von [TR-ESOR-TRANS] , die logisch äquivalent zur Eingangsschnittstelle S.4 gemäß [TR-ESOR-E] ist wie in der Tabelle 2 in [TR-ESOR-E] , Kapitel 4.1dargestellt, muss benutzt werden. Eine andere Eingangs-Schnittstelle anstelle von TR-S.4 bzw. TR-S.512 ist nicht erlaubt (vgl. A7.1-1 in [TR-ESOR] ). 

## HINWEIS 4 

In der vorliegenden TR-ESOR-Version 1.3 umfasst der Begriff „Archivinformationscontainer“ (AIP) in allen TR-ESOR-Anhängen: 

- a) das Archivdatenobjekt „XAIP“ gem. [TR-ESOR-F] , Kap. 3.1als auch 

- b) das logische XAIP „LXAIP“ gem. [TR-ESOR V1.3] , Kap. 3.2 und 

- c) das „ASiC-AIP“ gem. [TR-ESOR-F] , Kap. 3.3auf Basis von [ETSI EN 319162-1] . 

In TR-ESOR Version V1.3 wird zwischen XAIP, LXAIP und ASiC-AIP differenziert. 

Mit (L)XAIP wird XAIP oder LXAIP bezeichnet. 

Bundesamt für Sicherheit in der Informationstechnik 

11 

Überblick 

## HINWEIS 5 

In dieser TR-ESOR Version 1.3 ist “BIN” beschränkt auf die folgenden Bewahrungsobjekt-Formate (engl. preservation object formats): 

- CAdES gemäß [ETSI TS 119 512] , Annex A.1.1 (http://uri.etsi.org/ades/CAdES). Sofern kein MIME Type gesetzt ist, wird als Default application/cms verwendet; 

- XAdES gemäß [ETSI TS 119 512] , Annex A.1.2 (http://uri.etsi.org/ades/XAdES). Sofern kein MIME Type gesetzt ist, wird als Default application/xml verwendet; 

- PAdES gemäß [ETSI TS 119 512 ], Annex A.1.3 (http://uri.etsi.org/ades/PAdES). Sofern kein MIME Type gesetzt ist, wird als Default application/pdf verwendet; 

- ASiC-E gemäß [ETSI TS 119 512] , Annex A.1.4 (http://uri.etsi.org/ades/ASiC/type/ASiC-E). Sofern kein - 

- MIME Type gesetzt ist, wird als Defaultapplication/vnd.etsi.asic e+zipverwendet; 

- ASiC-S gemäß [ETSI EN 319162] (http://uri.etsi.org/ades/ASiC/type/ASiC-S). Sofern kein MIME Type gesetzt ist, wird als Default application/vnd.etsi.asic-s+zip verwendet. 

- DigestList gemäß [ETSI TS 119 512] , Annex A.1.6 (http://uri.etsi.org/19512/format/DigestList). Sofern kein MIME Type gesetzt ist, wird als Default application/xml verwendet; 

- ASiC-ERS (in TR-ESOR v1.3 mit ASiC-AIP bezeichnet) gemäß [TR-ESOR-F] , Kapitel 3.3 und gemäß - 

- [ETSI TS 119 512] , Annex A.3.1 (http://uri.etsi.org/ades/ASiC/type/ASiC ERS). 

- Im Falle Upload/Download-Funktion ist zusätzlich nachfolgendes Format erlaubt: 

- Binärdaten (BIN) als “Octet Stream”, die ausschließlich in den ECM-/Langzeitspeicher mit “UploadRequest” gespeichert werden, – aber nur sofern: 

   - a) verbunden mit einem korrespondierenden LXAIP und dort referenziert gem. [ TR-ESOR-F] , Kap. 3.2, b) ggf. mit “Download-Request“ ausgelesen werden, – verbunden mit einem korrespondierenden LXAIP, das mit der „ArchiveRetrieval“-Funktion ausgelesen wurde,– oder eingebettet in einem XAIP und ausgelesen mit der „ArchivRetrieval“-Funktion. 

   - c) Der Upload von XAIP oder LXAIP oder ASiC-AIP ist nicht zugelassen. 

## HINWEIS 6 

TR-ESOR spezifiziert ein Bewahrungsprodukt (engl. Preservation Product) gemäß [ETSI SR 019 510 ], [ETSI TS 119 511] und [ETSI TS 119 512] und [eIDAS-VO] . 

Die TR 03125 TR-ESOR ist in [ETSI SR 019 510 ] in dem Kapitel 4.7.3 und 5.2 und B3.2 beschrieben. Die in TRESOR erforderlichen grundlegenden Bewahrungstechniken, z.B. das Bewahrungsprotokoll, das BeweisdatenFormat Evidence Record, die Archivdatenobjekt-Format (L)XAIP und ASiC-AIP sind in der ETSI-Publikation [ETSI TS 119 512] als normative Elemente enthalten, (siehe Tabelle darunter): 

Tabelle 2: Bewahrungstechniken 

|Bewahrungstechnik|ETSI TS<br>119 512|Verbindlichkeitsgra<br>d<br>N=normativ<br>O=optional<br>C=conditional|TR-ESOR<br>Dokument|Verbindlichkeitsgra<br>d<br>N=normativ<br>O=optional<br>C=conditional|
|---|---|---|---|---|
|Bewahrungsprotokoll<br>(„Preservation<br>Protocol“):<br>TR-S.512|Kapitel<br>5.3|N|[TR-ESOR-E],<br>Kap. 4|C<br>Auswahl:<br>TR-S.512|
|Beweisdaten-Format<br>(„Preservation<br>Evidence<br>Format“):Evidence Record|A.2.2<br>bzw.<br>A2.3|N|[TR-ESOR-F],<br>Kap. 5.5,<br>[TR-ESOR-<br>ERS]|N|
|Archivdatenobjekt-Format<br>„…Data<br>Object<br>Format”<br>XAIP|A.1.5<br>und<br>A.3.2|N|[TR-ESOR-F],<br>Kap. 3.1 und 3.2|N|



Bundesamt für Sicherheit in der Informationstechnik 

12 

Überblick 

|Bewahrungstechnik|ETSI TS<br>119 512|Verbindlichkeitsgra<br>d<br>N=normativ<br>O=optional<br>C=conditional|TR-ESOR<br>Dokument|Verbindlichkeitsgra<br>d<br>N=normativ<br>O=optional<br>C=conditional|
|---|---|---|---|---|
|Archivdatenobjekt-Format<br>„…Data<br>Object<br>Format”<br>LXAIP|A.1.5<br>und<br>A.3.2|N|[TR-ESOR-F],<br>Kap. 3.1 und 3.2|C|
|Archivdatenobjekt-Format<br>„…Data<br>Object<br>Format”<br>ASiC-E/ASiC-ERS|A.1.4<br>und<br>A.3.1|N|[TR-ESOR-F],<br>Kap. 3.3|C|
|Versionierung<br>von<br>Archivinformationspaketen<br>(“Preservation<br>Object<br>Container”)|E|C|[TR-ESOR-E],<br>Kap. 3.2<br>[TR-ESOR-F],<br>Kap. 3.1.6 und<br>3.2.2|N|



## HINWEIS 7. 

Im folgenden Text umfasst der Begriff „Digitale Signatur“ : 

- „fortgeschrittene elektronische Signaturen“ gemäß [eIDAS-VO] , Artikel 3 Nr. 11, 

- „qualifizierte elektronische Signaturen“ gemäß [eIDAS-VO] , Artikel 3 Nr. 12, 

- „fortgeschrittenen elektronische Siegel“ gemäß [eIDAS-VO] , Artikel 3 Nr. 26 und 

- „qualifizierte elektronische Siegel“ gemäß [eIDAS-VO] , Artikel 3 Nr. 27. 

Insofern umfasst der Begriff „digital signierte Dokumente“ sowohl solche, die fortgeschrittene elektronische Signaturen oder Siegel bzw. qualifizierte elektronische Signaturen oder Siegel tragen. 

Mit dem Begriff der „kryptographisch signierten Dokumente“ sind in dieser TR neben: 

- den gemäß [eIDAS-VO] , Artikel 3 Nr. 12 qualifiziert signierten, 

- den gemäß [eIDAS-VO] , Artikel 3 Nr. 27 qualifiziert gesiegelten oder 

- den gemäß [eIDAS-VO] , Artikel 3 Nr. 34 qualifiziert zeitgestempelten Dokumenten (im Sinne der eIDASVerordnung) 

## auch 

- Dokumente mit einer fortgeschrittenen Signatur gemäß [eIDAS-VO] , Artikel 3 Nr. 11 oder 

- mit einem fortgeschrittenen Siegel gemäß [eIDAS-VO] , Artikel 3 Nr. 26 oder 

- mit einem elektronischen Zeitstempel gemäß [eIDAS-VO] , Artikel 3 Nr. 33 erfasst, 

wie sie oft in der internen Kommunikation von Behörden entstehen. 

Nicht gemeint sind hier Dokumente mit einfachen Signaturen oder Siegeln basierend auf anderen (z. B. nichtkryptographischen) Verfahren. 

Bundesamt für Sicherheit in der Informationstechnik 

13 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

## 3. Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

In diesem Abschnitt findet sich eine XML-basierte Spezifikation der Funktionen und deren Eingabe- und Ausgabeparameter der TR-ESOR-Middleware an der ArchiSafe-Schnittstelle TR-S.4 : 

- Funktion `ArchiveSubmission` mit den Parametern `ArchiveSubmissionRequest` und `ArchiveSubmissionResponse` (siehe Abs. 3.1) 

- • Funktion `ArchiveUpdate` mit den Parametern `ArchiveUpdateRequest` und `ArchiveUpdateResponse` (siehe Abs. 3.2) 

- • Funktion `ArchiveRetrieval` mit den Parametern `ArchiveRetrievalRequest` und `ArchiveRetrievalResponse` (siehe Abs. 3.3) 

- • Funktion `ArchiveEvidence` mit den Parametern `ArchiveEvidenceRequest` und `ArchiveEvidenceResponse` (siehe Abs. 3.4) 

- • Funktion `ArchiveDelete` mit den Parametern `ArchiveDeletionRequest` und `ArchiveDeletionResponse` (siehe Abs. 3.5) 

- Funktion `ArchiveData` mit den Parametern `ArchiveDataRequest` und `ArchiveDataResponse` (siehe Abs. 3.6) 

- Funktion `Verify` mit den Parametern `VerifyRequest` und `VerifyResponse` (siehe Abs. 3.7) 

- Funktion `RetrieveInfo` mit den Parametern `RetrieveInfoRequest` und `RetrieveInfoResponse` (siehe Abs. 3.8) 

- Funktion `ArchiveTrace` mit den Parametern `ArchiveTraceRequest` und `ArchiveTraceResponse` (siehe Abs. 3.9) 

Die graphische Darstellung der Schnittstellen in diesem Kapitel wurde - analog zur Spezifikation des eCardAPI-Frameworks (siehe z. B. [eCard-2] ) - mit einem XML-Viewer erstellt und dient lediglich der Veranschaulichung der XML-Strukturen. Die normative Spezifikation der Schnittstellen ist durch das XMLSchema bzw. die darauf aufbauende WSDL-Spezifikation (siehe Abs. 7) gegeben. 

## 3.1 Funktion: ArchiveSubmission 

Mit dem Funktionsparameter `ArchiveSubmissionRequest` wird dem aufgerufenen Modul ein Archivdatenobjekt zur Ablage übergeben und das aufrufende Modul erhält im Erfolgsfall in dem Ausgabeparameter `ArchiveSubmissionResponse` eine `AOID` zurück, mit der später wieder auf das archivierte Objekt oder die zugehörigen technischen Beweisdaten zugegriffen werden kann. Hierbei kann im `xaip:XAIP` - Element entweder ein physisches XAIP (siehe Abs. 3.1 in [TR-ESOR-F] ) oder ein logisches XAIP (LXAIP) (siehe Abs. 3.2 in [TR-ESOR-F] ) übergeben werden. Alternativ können im `ArchiveData` -Element binäre Nutzdaten übergeben werden. Hierbei wird der Typ des übergebenen Datenobjektes durch das Type-Attribut näher bestimmt. Dabei kann insbesondere ein `base64Binary` -codierter[5] ASiC-AIP-Container gemäß Abs. 3.3 in [TR-ESOR-F] mit einem `Type=http://uri.etsi.org/ades/ASiC/type/ASiC-ERS` Attribut übergeben werden. 

Wie in Abbildung 3 oder Abbildung 4 ersichtlich, wird diese Funktion neben der hier betrachteten Schnittstelle TR-S.4 auch in den Schnittstellen TR-S.2 (vgl. Abs. 5.2) und TR-S.6 (vgl. Abs. 5.5) genutzt. 

> 5 - Siehe https://www.w3.org/TR/xmlschema 2/#base64Binary. 

Bundesamt für Sicherheit in der Informationstechnik 

14 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

## 3.1.1 Eingabeparameter: ArchiveSubmissionRequest 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_3/BSI_TR_03125_Anlage_E_V1_3.pdf-0015-02.png)


**----- Start of picture text -----**<br>
Name  ArchiveSubmissionRequest<br>Beschreibung Durch den Aufruf der Funktion  ArchiveSubmission  mit dem Eingabeparameter<br>ArchiveSubmissionRequest  wird dem aufgerufenen Modul ein oder mehrere<br>ArchiveData -Element(e) oder ein Archivinformationspaket (XAIP, LXAIP, ASiC-<br>AIP) übergeben.<br>Hierbei kann für eine effiziente Übertragung von großen Binärdaten der<br>optimierte  Nachrichtenübertragungsmechanismus  „SOAP  Message<br>Transmission Optimization Mechanism (MTOM)“ [6]  genutzt werden.<br>Details  Der Eingabeparameter  ArchiveSubmissionRequest  weist folgenden Aufbau auf<br>und kann wie folgt parametrisiert werden.<br>Name  Beschreibung<br>**----- End of picture text -----**<br>


> 6 - Siehe https://www.w3.org/TR/soap12 mtom/ . 

Bundesamt für Sicherheit in der Informationstechnik 

15 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

|Name|**_`ArchiveSubmissionRequest`_**|**_`ArchiveSubmissionRequest`_**|
|---|---|---|
||`dss:OptionalInputs`|Ist für optionale Eingabeelemente vorgesehen.<br>(A3.1.1-1)<br>:<br>Gemäß<br>der<br>vorliegenden<br>Spezifikation<br>sollen<br>folgende<br>Elemente<br>unterstützt werden:<br>•<br>`xaip:AOID,`<br>•<br>`vr:ReturnVerificationReport,`<br>•<br>`ImportEvidence.`<br>Dabei gilt:<br>•<br>`xaip:AOID`<br>Durch die Übergabe eines`xaip:AOID`-Elementes<br>kann<br>die<br>AOID<br>von<br>der<br>aufrufenden<br>Anwendung vergeben werden. Im Regelfall fehlt<br>dieses Element und die AOID wird vom<br>aufgerufenen Modul bereitgestellt.<br>•<br>`vr:ReturnVerificationReport`<br>Durch<br>die<br>Übergabe<br>eines<br>`ReturnVerificationReport`-Elementes gemäß<br>[OASIS<br>VR]<br>bzw.<br>[eCard-2]<br>kann<br>ein<br>ausführlicher<br>Prüfbericht<br>in<br>Form<br>eines<br>`VerificationReport`-Elementes für die im<br>`XAIP`-Element<br>oder<br>im<br>unten<br>genannten<br>`ImportEvidence`-Element<br>enthaltenen<br>Signatur- bzw. Siegel- bzw. Zeitstempelobjekte<br>oder Beweisdaten angefordert werden. Bei<br>einem übergebenen`xaip:XAIP`-Element wird<br>im`Details`-Element des`IndividualReport`-<br>Elementes des zurückgelieferten Prüfberichts<br>(vgl. Abs. 3.3 in[OASIS VR]) ein`XAIPReport`-<br>Element gemäß[TR-ESOR-VR]zurückgeliefert.<br>Sofern<br>kein<br>`xaip:XAIP`<br>sondern<br>ein<br>`ArchiveData`-Element<br>und<br>im<br>`ImportEvidence`-Element (siehe unten) ein<br>Evidence Record übergeben wird, wird für jeden<br>übergebenen<br>Evidence<br>Record<br>ein<br>`EvidenceRecordReport`gem.[TR-ESOR-VR]<br>zurückgeliefert.|



Bundesamt für Sicherheit in der Informationstechnik 

16 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

|Name|**_`ArchiveSubmissionRequest`_**|**_`ArchiveSubmissionRequest`_**|
|---|---|---|
|||•<br>`tr:ImportEvidence`<br>Mit<br>der<br>Übergabe<br>des<br>dargestellten<br>`ImportEvidence`-Elementeskannder Import<br>von einem oder mehreren zu einer bestimmten<br>XAIP- bzw. LXAIP-Version bzw. zu den<br>übergebenen Binärdaten gehörenden Evidence<br>Records gemäß[RFC4998]oder[RFC6283]7<br>oder[TR-ESOR-ERS] angestoßen werden. Die<br>Struktur des`xaip:evidenceRecord`-Elementes<br>ist in[TR-ESOR-F]erläutert. Um Evidence<br>Records für mehrere Versionen eines XAIPs oder<br>LXAIPs importieren zu können,kanndieses<br>Element<br>mehrmals<br>auftreten.<br>Das<br>`xaip:evidenceRecord`-Elementmusshier die<br>Attribute`AOID`und`VersionID` enthalten.<br>Sofern die zu importierenden Evidence Records<br>bereits im XAIP bzw. LXAIP enthalten sind, wird<br>statt<br>des<br>Evidence<br>Records<br>hier<br>die<br>entsprechende`CredentialID`übergeben.<br>(A3.1.1-2) : Im Zuge des Imports von Evidence<br>Recordsmüssendiese von der TR-ESOR-<br>Middleware vollständig geprüft werden.<br>Dies umfasst die im entsprechenden ERS-<br>Standard<br>vorgesehenen<br>Prüfungungsschritte8, wobei die jeweiligen<br>Zertifikate der Zeitstempel vollständig bis<br>hin zu einer vertrauenswürdigen Wurzel<br>oder Vertrauensanker gemäß der vom [TR-<br>ESOR-PEPT]<br>abgeleiteten<br>und<br>veröffentlichten Preservation Policy (PEP)<br>des<br>TR-ESOR-Produktes<br>bzw.<br>Bewahrungsdienstes<br>geprüft<br>werden<br>müssen.|
||`xaip:XAIP`|Enthält ein XML-basiertes Archivdatenobjekt gemäß<br>[TR-ESOR-F],<br>das<br>durch<br>den<br>Aufruf<br>der<br>beweiswerterhaltenden<br>Archivierung<br>zugeführt<br>werdensoll.<br>Hierbei kann es sich entweder ein XAIP (siehe<br>Abs. 3.1 in [TR-ESOR-F]) oder ein LXAIP (siehe<br>Abs. 3.2 in[TR-ESOR-F])handeln.|
||`ArchiveData`|Enthält ein in einem beliebigen anderen Format<br>vorliegendes<br>Archivdatenobjekt.<br>Der<br>hierfür|



> 7 [RFC4998] muss, [RFC6283] und [TR-ESOR-ERS] können unterstützt werden. 

> 8Siehe Abschnitt 3.3 in [RFC4998] und Abschnitt 2.3 in [RFC6283] sowie [TR-ESOR-ERS] . 

Bundesamt für Sicherheit in der Informationstechnik 

17 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

|Name|**_`ArchiveSubmissionRequest`_**|**_`ArchiveSubmissionRequest`_**|
|---|---|---|
|||genutzte`ArchiveDataType`ist als`anyType`mit<br>einem optionalen`Type`-Attribut definiert.<br>Durch das`Type`-Attribut<br>`http://uri.etsi.org/ades/ASiC/type/ASiC-ERS`<br>wird<br>klargestellt,<br>dass<br>es<br>sich<br>um<br>einen<br>`base64Binary`-codierten9<br>ASiC-AIP-Container<br>gemäß Abs. 3.3 in[TR-ESOR-F] handelt.<br>Darüber hinaus zugelassene binäre Datentypen mit<br>dem zugehörigen Wert für das Type-Attribut sind<br>dem HINWEIS 5 zu entnehmen.<br>Weitere Übergabetypenkönnenim Rahmen einer<br>Profilierung<br>der<br>vorliegenden<br>Spezifikation<br>spezifiziert werden.|



## 3.1.2 Ausgabeparameter: ArchiveSubmissionResponse 

|Name|**_`ArchiveSubmissionResponse`_**|**_`ArchiveSubmissionResponse`_**|
|---|---|---|
|Beschreibung|Als Antwort auf einen`ArchiveSubmissionRequest`wird ein entsprechendes<br>`ArchiveSubmissionResponse`-Element zurückgeliefert, das im Erfolgsfall einen<br>eindeutigen Identifikator des Archivdatenobjektes,die`AOID`,enthält.||
|Details|Der Ausgabeparameter`ArchiveSubmissionResponse`ist die Antwort zum<br>Eingabeparameter`ArchiveSubmissionRequest`und weist folgenden Aufbau||
||Name|Beschreibung|
||`dss:Result`|Enthält die Statusinformationen und die Fehler zu<br>einer durchgeführten Aktion. Die Struktur dieses<br>Elements ist in [eCard-1] und unten näher<br>beschrieben.|



> 9 - Siehe https://www.w3.org/TR/xmlschema 2/#base64Binary . 

Bundesamt für Sicherheit in der Informationstechnik 

18 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

|Name|**_`ArchiveSubmissionResponse`_**|**_`ArchiveSubmissionResponse`_**|**_`ArchiveSubmissionResponse`_**|**_`ArchiveSubmissionResponse`_**|**_`ArchiveSubmissionResponse`_**|
|---|---|---|---|---|---|
||`dss:OptionalOutputs`||||Ist für optionale Ausgabeelemente vorgesehen.<br>(A3.1.2-1) Gemäß<br>der<br>vorliegenden<br>Spezifikationkanndas folgende Element<br>auftreten:<br>•<br>`VerificationReport`gemäß[OASIS VR]bzw.<br>[eCard-2]<br>und<br>[TR-ESOR-VR],<br>der<br>zurückgeliefert werdenmuss, sofern er explizit<br>angefordert wurde oder bei der Prüfung der<br>übergebenen Daten ein Fehler oder eine<br>Warnung aufgetreten ist und deshalb als<br>`ResultMajor`<br>ein<br>Fehlercode<br>.../resultmajor#erroroder.../resultmajor#warning<br>zurückgeliefert wird.|
||`AOID`||||Muss,sofern die`AOID10`vom aufgerufenen Modul<br>erzeugt oder ergänzt wurde, vorhanden sein und<br>für zukünftige Zugriffe auf das Archivdatenobjekt<br>genutzt werden.|
||Statusinformationen und Fehler bei`ArchiveSubmissionResponse`(vgl.[eCard-<br>1]Abschnitt 4.1 und 4.2).|||||
||Name||Fehlercode|||
||`ResultMajor`||/resultmajor#ok<br>/resultmajor#error<br>/resultmajor#warning|||
||`ResultMinor`||/resultminor/al/common#noPermission<br>/resultminor/al/common#internalError<br>/resultminor/al/common#parameterError<br>/resultminor/arl/lowSpaceWarning<br>/resultminor/arl/noSpaceError<br>/resultminor/arl/existingAOID<br>/resultminor/arl/notSupported<br>/resultminor/arl/unknownArchiveDataType<br>/resultminor/arl/XAIP_NOK<br>/resultminor/arl/XAIP_NOK_EXPIRED<br>/resultminor/arl/XAIP_NOK_SUBMTIME<br>/resultminor/arl/XAIP_NOK_SIG<br>/resultminor/arl/XAIP_NOK_ER<br>/resultminor/sal#invalidSignature|||



> 10Die AOID (Archive Object Identifier) im vorliegenden Dokument entspricht dem POID (Preservation Object Identifier) aus [ETSI TS 119 512] . 

Bundesamt für Sicherheit in der Informationstechnik 

19 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

## 3.2 Funktion: ArchiveUpdate 

Mit dem Funktionseingabeparameter `ArchiveUpdateRequest` wird eine neue Version für ein bereits abgelegtes Archivdatenobjekt erzeugt. Hierbei werden die bereits abgelegten Daten nicht verändert, sondern es wird lediglich zusätzlich eine neue Version hinzugefügt. 

Wie in Abbildung 3 und Abbildung 4 ersichtlich, wird diese Funktion neben der hier betrachteten Schnittstelle TR-S.4 auch in TR-S.2 (vgl. Abs. 5.2) und TR-S.6 (vgl. Abs. 5.5) genutzt. 

## 3.2.1 Eingabeparameter: ArchiveUpdateRequest 

|Name|**_`ArchiveUpdateRequest`_**|**_`ArchiveUpdateRequest`_**|
|---|---|---|
|Beschreibung|Durch den Aufruf der Funktion`ArchiveUpdate`wird eine neue Version für ein<br>bereits abgelegtes Archivdatenobjekt erzeugt (vgl.[TR-ESOR-M.1]). Die<br>Beschreibung der neuen Version wird dabei mit Hilfe des Eingabeparameters<br>`ArchiveUpdateRequest`vorgegeben.||
|Details|Der Eingabeparameter`ArchiveUpdateRequest`weist folgenden Aufbau auf und<br>kann wie folgt parametrisiert werden.||
||Name|Beschreibung|
||`dss:OptionalInputs`|Ist für optionale Eingabeelemente vorgesehen.<br>**(A3.2.1-1) : **<br>Gemäß<br>der<br>vorliegenden<br>Spezifikationsollenhier die unter (A3.1.1-1)<br>spezifizierten optionalen Eingabeelemente<br>`AOID`,<br>`ReturnVerificationReport`<br>und<br>`ImportEvidence`unterstützt werden.|
||`xaip:DXAIP`|Enthält<br>ein<br>ergänzendes<br>XML-basiertes<br>Archivdatenobjekt (Delta-XAIP) gemäß ([TR-ESOR-<br>F], Abs. 3.1.6) bzw. (Delta-LXAIP) gemäß ([TR-ESOR-<br>F], Abs. 3.2.2) das ein neues`versionManifest`, die<br>Vorgängerversion, Verweise auf unverändert aus<br>dieser übernommene Objekte und die zu ergänzenden<br>Elemente enthält, die in einer neuen Version eines<br>bereits<br>abgelegten<br>Archivdatenobjektes<br>ergänzt<br>werden sollen.|



Bundesamt für Sicherheit in der Informationstechnik 

20 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

## 3.2.2 Ausgabeparameter: ArchiveUpdateResponse 

|Name|**_`ArchiveUpdateResponse`_**|**_`ArchiveUpdateResponse`_**|
|---|---|---|
|Beschreibung|Als Antwort auf einen`ArchiveUpdateRequest`wird ein entsprechendes<br>`ArchiveUpdateResponse`-Element zurückgeliefert, das im Erfolgsfall einen im<br>Kontext einer`AOID`eindeutigen Identifikator der neuen Version des<br>Archivdatenobjektes, die`VersionID`, enthält.||
|Details|Der Ausgabeparameter`ArchiveUpdateResponse`weist folgenden Aufbau auf<br>und kann wie folgt parametrisiert werden.||
||Name|Beschreibung|
||`dss:Result`|Enthält die Statusinformationen und die Fehler zu<br>einer durchgeführten Aktion. Die Struktur dieses<br>Elements ist in[eCard-1]und unten näher<br>beschrieben.|
||`dss:OptionalOutputs`|Ist für optionale Ausgabeelemente vorgesehen.<br>**(A3.2.2-1) :**<br>Gemäß<br>der<br>vorliegenden<br>Spezifikationkanndas folgende Element<br>auftreten:<br>•<br>`VerificationReport`gemäß[OASIS VR]<br>bzw.[eCard-2]und[TR-ESOR-VR], der<br>zurückgeliefert werdenmuss, sofern er<br>explizit angefordert wurde oder bei der<br>Prüfung der übergebenen Daten ein Fehler<br>oder eine Warnung aufgetreten ist und<br>deshalb als`ResultMajor`ein Fehlercode<br>.../resultmajor#error<br>oder<br>.../resultmajor#warningzurückgeliefert wird.|
||`VersionID`|Ist im Erfolgsfall vorhanden und enthält den<br>bezüglich des über die<br>`AOID`identifizierten<br>Archivdatenobjektes<br>eindeutigen<br>Versions-<br>Identifikator. Die`VersionID`sollin der Form v1, v2,<br>… vxgebildet werden.|
||Statusinformationen und Fehler bei`ArchiveUpdateResponse`(vgl.[eCard-1]<br>Abs. 4.1 und Abs. 4.2).||



Bundesamt für Sicherheit in der Informationstechnik 

21 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

|Name||**_`ArchiveUpdateResponse`_**|**_`ArchiveUpdateResponse`_**|
|---|---|---|---|
||Name|Fehlercode||
||`ResultMajor`|•<br>•<br>•|/resultmajor#ok<br>/resultmajor#error<br>/resultmajor#warning|
||`ResultMinor`|•<br>•<br>•<br>•<br>•<br>•<br>•<br>•<br>•<br>•<br>•<br>•<br>•<br>•<br>•<br>•|/resultminor/al/common#noPermission<br>/resultminor/al/common#internalError<br>/resultminor/al/common#parameterError<br>/resultminor/arl/lowSpaceWarning<br>/resultminor/arl/noSpaceError<br>/resultminor/arl/existingPackageInfoWarning<br>/resultminor/arl/notSupported<br>/resultminor/arl/DXAIP_NOK<br>/resultminor/arl/DXAIP_NOK_AOID<br>/resultminor/arl/DXAIP_NOK_EXPIRED<br>/resultminor/arl/DXAIP_NOK_SUBMTIME<br>/resultminor/arl/DXAIP_NOK_SIG<br>/resultminor/arl/XAIP_NOK_ER<br>/resultminor/arl/DXAIP_NOK_ID<br>/resultminor/arl/DXAIP_NOK_Version<br>/resultminor/sal#invalidSignature|



## 3.3 Funktion: ArchiveRetrieval 

Mit dem Funktionseingabeparameter `ArchiveRetrievalRequest` wird das zu einer übergebenen `AOID` und `VersionID` gehörende physische XAIP-Archivdatenobjekt gemäß [TR-ESOR-F ], Abs. 3.1, das logische `XAIP` gemäß [TR-ESOR-F ], Abs. 3.2, oder das ASiC-AIP gemäß [TR-ESOR-F ], Abs. 3.3 über die TR-ESORMiddleware aus dem ECM-/Langzeitspeichersystem ausgelesen. 

Wie in Abbildung 3 und Abbildung 4 ersichtlich, wird diese Funktion neben der hier betrachteten Schnittstelle TR-S.4 in ähnlicher Weise auch in den Schnittstellen TR-S.2 (vgl. Abs. 5.2) und TR-S.5 (vgl. Abs. 5.4) genutzt. 

Bundesamt für Sicherheit in der Informationstechnik 

22 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

## 3.3.1 Eingabeparameter: ArchiveRetrievalRequest 

|Name|**_`ArchiveRetrievalRequest`_**|**_`ArchiveRetrievalRequest`_**|
|---|---|---|
|Beschreibung|Durch den Aufruf der Funktion<br>`ArchiveRetrieval`wird ein im<br>Langzeitspeicher abgelegtes Archivdatenobjekt ausgelesen und zurückgeliefert.<br>Hierbei kann für eine effiziente Übertragung von großen Binärdaten der<br>optimierte<br>Nachrichtenübertragungsmechanismus<br>„SOAP<br>Message<br>Transmission Optimization Mechanism (MTOM)“11genutzt werden.||
|Details|Der Eingabeparameter`ArchiveRetrievalRequest`weist folgenden Aufbau auf<br>und kann wie folgt parametrisiert werden.||
||Name|Beschreibung|



> 11 - Siehe https://www.w3.org/TR/soap12 mtom/ . 

Bundesamt für Sicherheit in der Informationstechnik 

23 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

|Name|**_`ArchiveRetrievalRequest`_**|**_`ArchiveRetrievalRequest`_**|
|---|---|---|
||`dss:OptionalInputs`|Ist für optionale Eingabeelemente vorgesehen.<br>(A3.3.1-1) :<br>Gemäß<br>der<br>vorliegenden<br>Spezifikation<br>sollen<br>die<br>folgenden<br>optionalen Eingabeelemente unterstützt<br>werden:<br>•<br>`pres:POFormat`<br>•<br>`tr:IncludeERS.`<br>`pres:POFormat`12 – gibt das AIP-Format an, wobei<br>folgende Formate definiert sind:<br>•<br>`http://www.bsi.bund.de/tr-`<br>`esor/xaip/1.3` – für ein XAIP gem. Abs. 3.1<br>in[TR-ESOR-F],<br>•<br>`http://www.bsi.bund.de/tr-`<br>`esor/lxaip/1.3` – für ein „logisches XAIP“<br>gem. Abs. 3.2 in[TR-ESOR-F],<br>•<br>`http://uri.etsi.org/ades/ASiC/typ`<br>`e/ASiC-ERS `– für einen base64Binary-<br>codierten ASiC-AIP-Container gem. Abs. 3.3 in<br>[TR-ESOR-F]in einem`PO`-Element gemäß<br>[ETSI TS 119 512],<br>das<br>im<br>`dss:OptionalOutputs`-Element<br>des<br>`ArchiveRetrievalResponse`<br>zurückgeliefert wird.<br>Sollte das Element `POFormat` ausgelassen werden,<br>so<br>ist<br>`http://www.bsi.bund.de/tr-`<br>`esor/xaip/1.3` standardmäßig gesetzt.<br>`tr:IncludeERS`<br>–<br>gibt<br>an,<br>dass<br>das<br>zurückgelieferte XAIP oder das logische XAIP<br>(LXAIP) oder das ASiC-AIP den bzw. die<br>entsprechenden<br>Evidence<br>Record(s)<br>im<br>angegebenen Format (vgl. `ERSFormat`,Seite 28)<br>enthaltensoll.<br>Dieser bzw. diese Evidence Record(s) wird bzw.<br>werden<br>bei<br>XAIP<br>bzw.<br>LXAIP<br>im<br>dafür<br>vorgesehenen<br>`xaip:credential/xaip:EvidenceRecord`<br>Element oder im Fall ASiC-AIP im ASiC-AIP-Container<br>gem. Abs. 3.3 in[TR-ESOR-F]zurückgeliefert.<br>**(A3.3.1-2)**<br>**:**<br>Das<br>`VersionID`-Attribut des<br>`xaip:EvidenceRecord`Elementesmuss<br>auf die entsprechende Version verweisen.|



> 12Das POFormat-Element ist in [ETSI TS 119 512] folgendermaßen definiert: <element name="POFormat" type="anyURI"/>. 

Bundesamt für Sicherheit in der Informationstechnik 

24 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

|Name|**_`ArchiveRetrievalRequest`_**|**_`ArchiveRetrievalRequest`_**|**_`ArchiveRetrievalRequest`_**|
|---|---|---|---|
|||||
||||Sofern<br>das<br>`versionManifest`<br>nicht<br>kryptographisch geschützt ist,mussmit einem<br>`unprotectedObjectPointer`-Element<br>im<br>entsprechenden<br>`versionManifest`<br>auf<br>die<br>`credentialID`des`xaip:credential`-Elementes<br>verwiesen werden.<br>Umgekehrtmussauf die vom Evidence Record<br>geschützten Datenobjekte im`relatedObjects`-<br>Attribut<br>des<br>`xaip:credential`-Elementes<br>verwiesen werden.|
||`AOID`||Enthält<br>den<br>eindeutigen<br>Identifikator<br>des<br>angeforderten Archivdatenobjektes.|
||`VersionID`||Kanneine Folge von Versions-Identifikatoren<br>enthalten, durch die angegeben wird, welche<br>Versionen des Archivdatenobjektes XAIP bzw.<br>LXAIP genau zurückgeliefert werden sollen.<br>Sofern das`VersionID`-Element nicht angegeben<br>ist, werden die zur letzten Version gehörigen<br>Datenobjekte<br>und<br>Verwaltungsinformationen<br>eines XAIPs bzw. LXAIPs zurückgeliefert.<br>Durch<br>die<br>Angabe<br>von<br>`all`<br>werden<br>alle<br>existierenden<br>Versionen<br>eines<br>Archivdatenobjektes zurückgeliefert.|



## 3.3.2 Ausgabeparameter: ArchiveRetrievalResponse 

|Name|**_`ArchiveRetrievalResponse`_**|**_`ArchiveRetrievalResponse`_**|
|---|---|---|
|Beschreibung|Als Antwort auf einen`ArchiveRetrievalRequest`wird ein entsprechendes<br>`ArchiveRetrievalResponse`-Element zurückgeliefert, welches im Erfolgsfall<br>das angeforderte Archivdatenobjekt (L)XAIP im`xaip:XAIP`-Format gem.[TR-<br>ESOR-F]oder in dem`PO`-element gem.[ETSI TS 119 512] (als ein base64Binary-<br>codierter ASiC-E-Container gem. Abs. 3.3 in[TR-ESOR-F])enthält.||
|Details|Der Ausgabeparameter`ArchiveRetrievalResponse`weist folgenden Aufbau auf<br>und kann wie folgt parametrisiert werden.||
||Name|Beschreibung|



Bundesamt für Sicherheit in der Informationstechnik 

25 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

|Name|**_`ArchiveRetrievalResponse`_**|**_`ArchiveRetrievalResponse`_**|**_`ArchiveRetrievalResponse`_**|**_`ArchiveRetrievalResponse`_**|
|---|---|---|---|---|
||`dss:Result`|||Enthält die Statusinformationen und die Fehler zu<br>einer durchgeführten Aktion. Die Struktur dieses<br>Elements ist in[eCard-1]und weiter unten näher<br>beschrieben.<br>Sofern nur ein Teil der angeforderten Versionen<br>des Archivdatenobjektes zurückgeliefert werden<br>konnte,<br>wird<br>dies<br>durch<br>den<br>Fehlercode<br>.../resultminor/arl/requestOnlyPartlySuccessfulWarni<br>ngangezeigt.|
||`dss:OptionalOutputs`|||Ist für optionale Ausgabeelemente vorgesehen, die<br>im Rahmen einer Profilierung der vorliegenden<br>Spezifikation definiert werdensollen.<br>Insbesondere kann hier ein`PO`-Element gemäß<br>[ETSI TS 119 512]enthalten sein, das ein<br>base64Binary-codiertes ASiC-AIP gemäß Abs. 3.3<br>in[TR-ESOR-F]enthält, sofern dieses angefordert<br>wird.|
||`xaip:XAIP`|||Sofern kein Fehler aufgetreten ist, wird das<br>angeforderte<br>XML-basierte<br>Archivdatenobjekt<br>(XAIP<br>oder<br>LXAIP)<br>gemäß<br>[TR-ESOR-F]<br>zurückgeliefert.|
||Statusinformationen und Fehler bei`ArchiveRetrievalResponse`(vgl.[eCard-<br>1]).||||
||Name|Fehlercode|||
||`ResultMajor`|•<br>•<br>•|/resultmajor#ok<br>/resultmajor#error<br>/resultmajor#warning||
||`ResultMinor`|•<br>•<br>•<br>•<br>•<br>•<br>•<br>•|/resultminor/al/common#noPermission<br>/resultminor/al/common#internalError<br>/resultminor/al/common#parameterError<br>/resultminor/arl/unknownAOID<br>/resultminor/arl/notSupported<br>/resultminor/arl/requestOnlyPartlySuccessfulWarning<br>/resultminor/arl/unknownVersionID13<br>/resultminor/arl/unknownPOFormat||



> 13 Im `ResultMessage` -Element soll die problematische `VersionID` zurückgeliefert werden. 

Bundesamt für Sicherheit in der Informationstechnik 

26 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

## 3.4 Funktion: ArchiveEvidence 

Mit dem Funktionseingabeparameter `ArchiveEvidenceRequest` werden die zugehörigen technischen Beweisdaten (Evidence Records gemäß [RFC4998] oder [RFC6283][14 ] oder mit der Profilierung aus [TR-ESORERS] ) für ein beweiswerterhaltend aufbewahrtes und über ein `AOID` -Element adressiertes Archivdatenobjekt zurückgeliefert. 

Wie in Abbildung 3 und Abbildung 4 ersichtlich, wird diese Funktion neben der hier betrachteten Schnittstelle TR-S.4 auch in TR-S.6 (vgl. Abs. 5.5) genutzt. 

## 3.4.1 Eingabeparameter: ArchiveEvidenceRequest 

|Name|**_`ArchiveEvidenceRequest`_**|**_`ArchiveEvidenceRequest`_**|
|---|---|---|
|Beschreibung|Durch den Aufruf der Funktion<br>`ArchiveEvidence`können für ein<br>beweiswerterhaltend abgelegtes Archivdatenobjekt technische Beweisdaten in<br>Form von Evidence Records gemäß[RFC4998]oder[RFC6283]15oder in der<br>Profilierung gem.[TR-ESOR-ERS]angefordert werden.||
|Details|Der Eingabeparameter`ArchiveEvidenceRequest`weist folgenden Aufbau auf<br>und kann wie folgt parametrisiert werden.||
||Name|Beschreibung|



> 14 **[RFC4998]** muss, **[RFC6283]** kann unterstützt werden. 

> 15 **[RFC4998]** muss, **[RFC6283]** kann unterstützt werden. 

Bundesamt für Sicherheit in der Informationstechnik 

27 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

|Name|**_`ArchiveEvidenceRequest`_**|**_`ArchiveEvidenceRequest`_**|**_`ArchiveEvidenceRequest`_**|
|---|---|---|---|
||`dss:OptionalInputs`||Ist für optionale Eingabeelemente vorgesehen.<br>**(A3.4.1-1):**<br>Gemäß<br>der<br>vorliegenden<br>Spezifikation<br>soll<br>das<br>folgende<br>Element<br>unterstützt werden:<br>Mit dem Element`tr:ERSFormat`vom Typ`anyURI`<br>kann das gewünschte Format der zurückgelieferten<br>Evidence<br>Records<br>angegeben<br>werden,<br>wobei<br>folgende URIs vorgesehen sind:<br>•<br>urn:ietf:rfc:4998<br>für<br>`ASN.1-`basierte<br>Evidence Records gem.[RFC4998]oder<br>•<br>urn:ietf:rfc:6283 für XML-basierte Evidence<br>Records gem.[RFC6283]oder<br>•<br>http://www.bsi.bund.de/SharedDocs/Down<br>loads/DE/BSI/Publikationen/TechnischeRi<br>chtlinien/TR03125/BSI_TR_03125_Anlage_<br>ERS_V1_2.html#Basis-ERS-Profil gem.[TR-<br>ESOR-ERS]oder<br>•<br>http://www.bsi.bund.de/SharedDocs/Down<br>loads/DE/BSI/Publikationen/TechnischeRi<br>chtlinien/TR03125/BSI_TR_03125_Anlage_<br>ERS_V1_2.html#Basis-XERS-Profil<br>gem.<br>[TR-ESOR-ERS].<br>Fehlt das `ERSFormat`-Element, so werden ASN.1-<br>basierteEvidence Recordsgemäß[RFC4998]in der<br>ProfilierungBasis-ERS-Profilegem.[TR-ESOR-<br>ERS]zurückgeliefert.|
||`AOID`||Ist der eindeutige Identifikator des angeforderten<br>Archivdatenobjektes.|
||`VersionID`||Kannmehrfach auftreten und angeben, für welche<br>Versionen eines über die`AOID`identifizierten<br>Archivdatenobjektes XAIP bzw. LXAIP Evidence<br>Records zurückgeliefert werden sollen.<br>Sofern das`VersionID`-Element nicht angegeben ist,<br>wird der Beweisdatensatz für die aktuelle Version<br>des XAIP bzw. des LXAIP zurückgeliefert.<br>Durch die Angabe von`all`werden Evidence Records<br>für<br>alle<br>existierenden<br>Versionen<br>eines<br>Archivdatenobjektes zurückgeliefert.|



Bundesamt für Sicherheit in der Informationstechnik 

28 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

## 3.4.2 Ausgabeparameter: ArchiveEvidenceResponse 

|Name|**_`ArchiveEvidenceResponse`_**|**_`ArchiveEvidenceResponse`_**|**_`ArchiveEvidenceResponse`_**|
|---|---|---|---|
|Beschreibung|Als Antwort auf einen`ArchiveEvidenceRequest`wird ein entsprechendes<br>`ArchiveEvidenceResponse`-Element zurückgeliefert, das die angeforderten<br>Beweisdaten enthält.|||
|Details|Der Ausgabeparameter`ArchiveRetrievalResponse`weist folgenden Aufbau auf<br>und kann wie folgt parametrisiert werden.|||
||Name||Beschreibung|
||`dss:Result`||Enthält die Statusinformationen und die Fehler zu<br>einer durchgeführten Aktion. Die Struktur dieses<br>Elements ist in Abs. 4.1.2 von[eCard-1]und unten<br>näher beschrieben.<br>Sofern nicht für alle mittels der übergebenen`AOID`<br>adressierten Archivdatenobjekte entsprechende<br>Beweisdaten (Evidence Records) zurückgeliefert<br>werden<br>konnten,<br>wird<br>dies<br>durch<br>die<br>.../resultminor/arl/requestOnlyPartly<br>SuccessfulWarningangezeigt.|
||`dss:OptionalOutputs`||Ist für optionale Ausgabeelemente vorgesehen und<br>kannbeispielsweise entsprechende Steuerelemente<br>(`responseControls)`enthalten, die im Rahmen<br>einer Profilierung der vorliegenden Spezifikation<br>definiertwerdensollen.|
||`xaip:evidenceRecord`||Sofern<br>vom<br>ArchiSig-Modul<br>entsprechende<br>Evidence<br>Records16<br>gemäß<br>[RFC4998]<br>bzw.<br>[RFC6283]<br>oder<br>[TR-ESOR-ERS]<br>konstruiert<br>werden können, werden diese zurückgeliefert. Die<br>detaillierte<br>Struktur<br>dieses<br>Elementes<br>ist<br>nachfolgend erläutert.|



> 16 Sofern die TR-ESOR-Middleware mehrere redundante Hashbäume pflegt, werden hier mehrere Evidence Records zurückgeliefert. 

Bundesamt für Sicherheit in der Informationstechnik 

29 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

|Name|**_`ArchiveEvidenceResponse`_**|**_`ArchiveEvidenceResponse`_**|**_`ArchiveEvidenceResponse`_**|**_`ArchiveEvidenceResponse`_**|
|---|---|---|---|---|
||<br>Das`xaip:evidenceRecord`-Element gemäß[TR-ESOR-F]ist vom Typ<br>`xaip:EvidenceRecordType`, der entsprechend den Evidence Record beinhaltet<br>und zusätzlich die Attribute`AOID`und`VersionID`, enthält, die in[TR-ESOR-F]<br>näher erläutert sind.<br>**(A3.4.2-1) :**<br>Bei<br>der<br>hier<br>beschriebenen<br>Verwendung<br>von<br>`xaip:evidenceRecord` müssendie Attribute `AOID` und`VersionID`<br>gesetzt sein.||||
||Name|||Beschreibung|
||`xmlEvidenceRecord`|||Enthält einen XML-basierten Evidence Record<br>gemäß[RFC6283].|
||`asn1EvidenceRecord`|||Enthält einen ASN.1-basierten Evidence Record<br>gemäß[RFC4998].|
||Statusinformationen und Fehler bei`ArchiveEvidenceResponse`(vgl.[eCard-<br>1]).||||
||Name|Fehlercode|||
||`ResultMajor`|•<br>•<br>•|/resultmajor#ok<br>/resultmajor#error<br>/resultmajor#warning||
||`ResultMinor`|•<br>•<br>•<br>•<br>•<br>•<br>•|/resultminor/al/common#noPermission<br>/resultminor/al/common#internalError<br>/resultminor/al/common#parameterError<br>/resultminor/arl/notSupported17<br>/resultminor/arl/unknownAOID<br>/resultminor/arl/unknownVersionID/<br>resultminor/arl/requestOnlyPartlySuccessfulWarning||



> 17Im `ResultMessage` -Element sollen nähere Informationen darüber zurückgeliefert werden, welche angeforderte Funktionalität nicht unterstützt wird. 

Bundesamt für Sicherheit in der Informationstechnik 

30 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

## 3.5 Funktion: ArchiveDeletion 

Mit dem Funktionseingabeparameter `ArchiveDeletionRequest` wird ein Archivdatenobjekt (inklusive aller zugehörigen Versionen und im Fall eines LXAIPs auch inklusive aller dort referenzierten Nutzdaten) über die TR-ESOR-Middleware aus dem ECM-/Langzeitspeichersystem gelöscht. 

Wie in Abbildung 3 und Abbildung 4 ersichtlich, wird diese Funktion neben der hier betrachteten Schnittstelle TR-S.4 auch in der Schnittstelle TR-S.5 (vgl. Abs. 5.4) genutzt. 

## 3.5.1 Eingabeparameter: ArchiveDeletionRequest 

|Name|**_`ArchiveDeletionRequest`_**|**_`ArchiveDeletionRequest`_**|
|---|---|---|
|Beschreibung|Durch den Aufruf der Funktion`ArchiveDeletion`kann ein im Langzeitspeicher<br>abgelegtes Archivdatenobjekt (z.B. XAIP oder LXAIP oder ASiC-AIP oder die in<br>[TR-ESOR-F],<br>HINWEIS<br>5<br>aufgezählten<br>Binärdaten),<br>inklusive<br>aller<br>dazugehörigen Versionen und referenzierten Nutzdaten, gelöscht werden.||
|Details|Der Eingabeparameter`ArchiveDeletionRequest`weist folgenden Aufbau auf<br>und kann wie folgt parametrisiert werden.||
||Name|Beschreibung|
||`dss:OptionalInputs`|Ist für optionale Eingabeelemente vorgesehen.<br>Insbesondere bei einer vorzeitigen Löschungmuss<br>das folgende Element`ReasonOfDeletion`genutzt<br>und unterstützt werden:<br>**(A3.5.1-1):** Das `ReasonOfDeletion`-Element<br>muss<br>vorhanden<br>sein,<br>sofern<br>die<br>Aufbewahrungsdauer der letzten Version noch<br>nicht abgelaufen ist, und enthält neben dem<br>Namen der aufrufenden Instanz auch eine<br>Begründung für die Löschung.<br>**(A3.5.1-2):**Die gesamte Aktion einschließlich<br>der Begründungmussprotokolliert werden und<br>der übergebene `RequestorName` sollmit den<br>verwendeten<br>Authentisierungsinformationen<br>abgeglichen werden.|
||`AOID`|Das<br>`AOID`-Element<br>gibt<br>an,<br>welches<br>Archivdatenobjekt gelöscht werden soll.|



Bundesamt für Sicherheit in der Informationstechnik 

31 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

## 3.5.2 Ausgabeparameter: ArchiveDeletionResponse 

|3.5.2<br>Ausgabep|arameter: ArchiveDeletionResponse|arameter: ArchiveDeletionResponse|arameter: ArchiveDeletionResponse|arameter: ArchiveDeletionResponse|arameter: ArchiveDeletionResponse|
|---|---|---|---|---|---|
|Name|**`ArchiveDeletionResponse`**|||||
|Beschreibung|Als Antwort auf einen`ArchiveDeletionRequest`wird ein entsprechendes<br>`ArchiveDeletionResponse`-Element zurückgeliefert, das Informationen über<br>den Erfolg oder Misserfolg der Anfrage enthält.|||||
|Details|Der Ausgabeparameter`ArchiveDeletionResponse`weist folgenden Aufbau auf<br>und kann wie folgt parametrisiert werden.|||||
||Name||||Beschreibung|
||`dss:Result`||||Enthält die Statusinformationen und die Fehler zu<br>einer durchgeführten Aktion. Die Struktur dieses<br>Elements ist in[eCard-1]und unten näher<br>beschrieben.|
||`dss:OptionalOutputs`||||Ist für optionale Ausgabeelemente vorgesehen und<br>kann<br>beispielsweise<br>entsprechende<br>Steuerelemente (`responseControls)`enthalten,<br>die<br>im<br>Rahmen<br>einer<br>Profilierung<br>der<br>vorliegenden<br>Spezifikation<br>definiert<br>werden|
||Statusinformationen und Fehler bei`ArchiveDeletionResponse`(vgl.[eCard-<br>1]).|||||
||Name|Fehlercode||||
||`ResultMajor`|•<br>•|/resultmajor#ok<br>/resultmajor#error|||
||`ResultMinor`|•<br>•<br>•<br>•<br>•<br>•|/resultminor/al/common#noPermission<br>/resultminor/al/common#internalError<br>/resultminor/al/common#parameterError<br>/resultminor/arl/unknownAOID<br>/resultminor/arl/notSupported<br>/resultminor/arl/missingReasonOfDeletion|||



## 3.6 Funktion: ArchiveData 

Mit dem Funktionseingabeparameter `ArchiveDataRequest` können diskrete Datenelemente aus einem bereits abgelegten Archivdatenobjekt ( `xaip:XAIP` ) ausgelesen werden. 

Bundesamt für Sicherheit in der Informationstechnik 

32 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

Die detaillierte Ausgestaltung dieser Funktion wird dem Hersteller überlassen. Der Hersteller ist zur Dokumentation der an der Schnittstelle unterstützten Funktionalität verpflichtet. Im Zuge der Zertifizierung wird geprüft, dass die in der Dokumentation beschriebene Funktionalität umgesetzt ist. 

Wie in Abbildung 3 und Abbildung 4 ersichtlich, wird diese Funktion neben der hier betrachteten Schnittstelle TR-S.4 auch in TR-S.5 (vgl. Abs. 5.4) genutzt. 

## 3.6.1 Eingabeparameter: ArchiveDataRequest 

|Name|**_`ArchiveDataRequest`_**|**_`ArchiveDataRequest`_**|**_`ArchiveDataRequest`_**|
|---|---|---|---|
|Beschreibung|Mit dem Aufruf der Funktion`ArchiveData`können diskrete Datenelemente aus<br>einem im zuvor abgelegten Archivinformationspaket (vgl. Abs. 3.1) ausgelesen<br>werden. Die Archivdaten-Container müssen dabei als XAIP oder LXAIP gem.<br>dieser Spezifikation vorliegen.|||
|Details|Der Eingabeparameter`ArchiveDataRequest`weist folgenden Aufbau auf und<br>kann wie folgt parametrisiert werden.|||
||Name||Beschreibung|
||`dss:OptionalInputs`||Ist für optionale Eingabeelemente vorgesehen und<br>kann<br>beispielsweise<br>Steuerelemente<br>(`requestControls)`enthalten, die im Rahmen<br>einer Profilierung der vorliegenden Spezifikation<br>definiert werdensollen.<br>Die vorliegende Spezifikation definiert keine<br>solchen optionalen Eingabeelemente.|
||`AOID`||Dieses Element enthält den Identifikator eines<br>bestimmten Archivdatenobjektes.|



Bundesamt für Sicherheit in der Informationstechnik 

33 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

|Name|**_`ArchiveDataRequest`_**|**_`ArchiveDataRequest`_**|
|---|---|---|
||`tr:DataLocation`|Das`tr:DataLocation`-Element kann mehrmals<br>auftreten und bestimmt die „Lokation“ der<br>auszulesenden diskreten Datenelemente bezüglich<br>eines zumindest logisch im`xaip:XAIP`-Format<br>gemäß<br>[TR-ESOR-F]18<br>vorliegenden<br>Archivdatenobjektes.<br>Die detaillierte Ausgestaltung der hier unterstützen<br>Funktionalität bleibt dem Hersteller überlassen.<br>**(A3.6.1-1) :**Sofern der`ArchiveDataRequest`<br>unterstützt wird,mussdieser die Details der<br>an<br>der<br>Schnittstelle<br>angebotenen<br>Funktionalität dokumentieren.|
||Das`DataLocation`-Element spezifiziert, welche Teile eines Archivobjektes<br>zurückgeliefert werden sollen und ist folgendermaßen definiert:<br>Im`Type`-Attribut wird angegeben, welche Transformation für den Zugriff auf die<br>gewünschten Daten angewandt werden soll, wobei die folgenden URIs<br>vorgesehen sind:<br>•<br>http://www.w3.org/TR/2007/REC-xpath20-20070123/ für XPath.<br>Der zugehörige XPATH-Ausdruck ist in das`XPathFilter`-Element abzulegen<br>und als Wert des`DataLocation`-Element zu übergeben.||



> 18Im Falle eines XML-basierten Archivinformationspakets sind die folgenden diskreten Adressierung von XML Datenelementen möglich: XPath (siehe http://www.w3.org/TR/2007/REC-xpath20-20070123/). 

Bundesamt für Sicherheit in der Informationstechnik 

34 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

## 3.6.2 Ausgabeparameter: ArchiveDataResponse 

|Name|**_`ArchiveDataResponse`_**|**_`ArchiveDataResponse`_**|**_`ArchiveDataResponse`_**|
|---|---|---|---|
|Beschreibung|Als Antwort auf einen`ArchiveDataRequest`wird ein entsprechendes<br>`ArchiveDataResponse`-Element<br>zurückgeliefert,<br>das<br>die<br>gewünschten<br>Informationen enthält.|||
|Details|Der Ausgabeparameter`ArchiveDataResponse`weist folgenden Aufbau auf und<br>kann wie folgt parametrisiert werden.|||
||Name||Beschreibung|
||`dss:Result`||Enthält die Statusinformationen und die Fehler zu<br>einer durchgeführten Aktion. Die Struktur dieses<br>Elements ist in[eCard-1]und unten näher<br>beschrieben. Sofern nur ein Teil der angefragten<br>diskreten Datenobjekte zurückgeliefert werden<br>konnte,<br>wird<br>dies<br>durch<br>den<br>Fehlercode<br>…/resultminor/arl/requestOnlyPartlySuccessfulWarnin<br>gangezeigt.|
||`dss:OptionalOutputs`||Ist für optionale Ausgabeelemente vorgesehen und<br>kannbeispielsweise entsprechende Steuerelemente<br>(`responseControls)`enthalten, die im Rahmen<br>einer Profilierung der vorliegenden Spezifikation<br>definiert werdensollen.|
||`XAIPData`||Enthält im Erfolgsfall die gewünschten Daten und<br>die „Lokation“, aus der diese aus der im ECM-<br>/Langzeitspeichersystem<br>zumindest<br>logisch<br>existierenden<br>`XAIP`-<br>bzw.<br>`LXAIP`-Struktur<br>ausgelesen wurden. Die detaillierte Struktur dieses<br>Elementes ist nachfolgend dargestellt und erläutert.|
||Das`XAIPData`-Element enthält im Erfolgsfall die gewünschten Daten.|||
||Name|Beschreibung||



Bundesamt für Sicherheit in der Informationstechnik 

35 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

|Name|**_`ArchiveDataResponse`_**|**_`ArchiveDataResponse`_**|**_`ArchiveDataResponse`_**|**_`ArchiveDataResponse`_**|
|---|---|---|---|---|
||`dss:Result`|||Gibt an, ob die Anfrage erfolgreich durchgeführt<br>werden konnte oder nicht.<br>Als`ResultMajor`sind die beiden folgenden Werte<br>möglich:<br>•<br>.../resultmajor#ok<br>•<br>.../resultmajor#error<br>Als`ResultMinor`sind die folgenden Werte<br>möglich:<br>•<br>.../resultminor/arl/unknownLocation<br>•<br>.../resultminor/al/common#parameterError<br>•<br>.../resultminor/al/common#internalError|
||`tr:DataLocation`|||Das`DataLocation`-Element spezifiziert, welche<br>Teile eines Archivobjektes zurückgeliefert werden.<br>Die detaillierte Ausgestaltung dieses Parameters ist<br>derSeite 33zu entnehmen.|
||`Value`|||Enthält im Erfolgsfall diegewünschten Daten.|
||Statusinformationen und Fehler bei`ArchiveDataResponse`(vgl.[eCard-1]).||||
||Name|Fehlercode|||
||`ResultMajor`|•<br>•<br>•|/resultmajor#ok<br>/resultmajor#error<br>/resultmajor#warning||
||`ResultMinor`|•<br>•<br>•<br>•<br>•<br>•|/resultminor/al/common#noPermission<br>/resultminor/al/common#internalError<br>/resultminor/al/common#parameterError<br>/resultminor/arl/unknownAOID<br>/resultminor/arl/notSupported<br>/resultminor/arl/requestOnlyPartlySuccessfulWarning||



## 3.7 Funktion: Verify 

Mit dem Funktionseingabeparameter `VerifyRequest` werden XML-basierte Archivinformationspakete (XAIP), logische XAIP (LXAIP) oder ASiC-AIP-basierte Datencontainer oder binäre Daten gemäß HINWEIS 5 oder optional XML-basiertes Delta- Archivinformationspakete (Delta-(L)XAIP) und Beweisdaten (Evidence Records) sowie den darin enthaltenen oder zusätzlich übergebenen beweisrelevanten Daten (Signaturen, Siegel, Zeitstempel, Zertifikate, Sperrlisten, OCSP-Responses etc.) geprüft. 

Wie in Abbildung 3 und Abbildung 4 ersichtlich, wird diese Funktion neben der hier betrachteten Schnittstelle TR-S.4 auch in TR-S.1 (vgl. Abs. 5.1) genutzt. 

Bundesamt für Sicherheit in der Informationstechnik 

36 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

## 3.7.1 Eingabeparameter: VerifyRequest 

|Name|**_`VerifyRequest`_**|**_`VerifyRequest`_**|**_`VerifyRequest`_**|<br> <br> <br> <br> <br> <br> <br> <br> <br>|
|---|---|---|---|---|
||||||
|Beschreibung<br> <br> <br> <br> <br> <br> <br>|Mit der Funktion`VerifyRequest`(vgl. Abs. 3.2.2 von[eCard-2]) werden XML-basierte<br>Archivinformationspakete<br>(XAIP),<br>logische<br>XAIP<br>oder<br>ASiC-AIP-basierte<br>Datencontainer oder optional XML-basiertes Archivinformationspakete Delta-<br>(L)XAIP), mit den darin enthaltenen beweisrelevanten Daten (Signaturen, Siegel,<br>Zeitstempel, Zertifikate, Sperrlisten, OCSP-Responses etc.), und ebenfalls darin<br>enthalten oder zusätzlich übergebenen Beweisdaten (Evidence Records), oder<br>zusätzlich übergebenen beweisrelevanten Daten (Signaturen, Siegel, Zeitstempel,<br>Zertifikate, Sperrlisten, OCSP-Responses etc.) geprüft.||||
|Details|Der Eingabeparameter`VerifyRequest`weist folgenden Aufbau auf und kann wie<br>folgt parametrisiert werden.||||
||Name|Beschreibung|||
||`dss:OptionalInputs`|Das<br>`OptionalInputs`-Element<br>kann<br>zusätzliche<br>Eingabeelemente enthalten.<br>**(A3.7.1-1)**<br>**:**Hierbei werden insbesondere die in<br>**[eCard-2]**<br>definierten<br>Elemente<br>und Aufrufoptionen<br>unterstützt.<br>Dies umfasst insbesondere die folgenden Elemente:<br>•<br>`VerifyUnderSignaturePolicy`<br>soll<br>unterstützt werden,<br>•<br>`ReturnVerificationReport`<br>muss<br>unterstützt werden.<br>Es gilt im Einzelnen:<br>•<br>`VerifyUnderSignaturePolicy`<br>Sofern in einem`dss:Document/InlineXML`-<br>Kindelement von`dss:InputDocuments`ein<br>`XAIP`-Element in Form eines gewöhnlichen<br>XAIP oder eines logischen XAIP gemäß[TR-<br>ESOR-F]enthalten ist, kann mit dem Element<br>`VerifyUnderSignaturePolicy`und der<br>im<br>`DefaultPolicy/`<br>`SignaturePolicyIdentifier`-Element<br>angegebenen Signature-Policy:<br>◦ `http://www.bsi.bund.de/DE/tr-`<br>`esor/sigpolicy/verify-xaip` oder|||



Bundesamt für Sicherheit in der Informationstechnik 

37 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

|Name||**_`VerifyRequest`_**|**_`VerifyRequest`_**|
|---|---|---|---|
|||||
|||◦ `http://www.bsi.bund.de/DE/tr-`<br>`esor/sigpolicy/verify-`<br>`xaip/shell` oder<br>◦ `http://www.bsi.bund.de/DE/tr-`<br>`esor/sigpolicy/verify-`<br>`xaip/chain`<br>die<br>Prüfung<br>und<br>Ergänzung<br>aller<br>im<br>übergebenen XAIP- bzw. LXAIP-Container bzw.<br>ASiC-AIP enthaltenen digitalen Signaturen<br>angefordert werden.<br>(A3.7.1-2) **:**<br>Hierbei<br>müssen<br>alle<br>digitalen<br>Signaturinformationen<br>(Signaturen,<br>Siegel,<br>Zeitstempel,<br>Zertifikate,<br>Sperrlisten,<br>OCSP-<br>Responses<br>etc.)<br>bis<br>hin<br>zu<br>einer<br>vertrauenswürdigen<br>Wurzel<br>oder<br>Vertrauensanker gemäß der vom[TR-ESOR-<br>PEPT]<br>abgeleiteten<br>und<br>veröffentlichten<br>Preservation<br>Policy<br>(PEP)<br>des<br>TR-ESOR-<br>Produktes bzw. Bewahrungsdienstes geprüft<br>werden.<br>Die<br>hierbei<br>ermittelten<br>Prüfinformationen<br>(Zertifikate,<br>Sperrlisten,<br>OCSP-Responses)<br>müssen<br>nach<br>Möglichkeit<br>als<br>unsignierte<br>Attribute bzw. Properties in den entsprechenden<br>digitalen Signaturen bzw. in den Kind-Elementen<br>`certificateValues`<br>bzw.<br>`revocationValues`<br>des<br>`credential`-<br>Elementes abgelegt werden.<br>Wenn sowohl die Signature-Policy:<br>◦ `http://www.bsi.bund.de/DE/tr-`<br>`esor/sigpolicy/verify-xaip` oder<br>◦ `http://www.bsi.bund.de/DE/tr-`<br>`esor/sigpolicy/verify-`<br>`xaip/shell` oder<br>◦ `http://www.bsi.bund.de/DE/tr-`<br>`esor/sigpolicy/verify-`<br>`xaip/chain`<br>als<br>auch<br>das<br>Element<br>`ReturnVerificationReport`<br>übergeben<br>werden,<br>dann<br>muss<br>der<br>dann<br>erzeugte<br>Prüfbericht<br>in<br>das<br>Kind-Element<br>`vr:VerificationReport`des`credential`-<br>Elements abgelegt werden.<br>(A3.7.1-3) **:**Sofern in der `credentialsSection`<br>des übergebenen XAIP-, LXAIP- oder Delta-<br>(L)XAIP oder ASiC-AIP-Containers ein oder<br>mehrere<br>`xaip:EvidenceRecord`-Elemente<br>gemäß[TR-ESOR-F]enthalten sind,müssen<br>diese entsprechendgeprüft werden.||
|||||



Bundesamt für Sicherheit in der Informationstechnik 

38 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

|Name||**_`VerifyRequest`_**|**_`VerifyRequest`_**|
|---|---|---|---|
|||||
|||Die<br>hierbei<br>ermittelten<br>Prüfinformationen<br>(Zertifikate,<br>Sperrlisten,<br>OCSP-Responses)<br>müssen<br>nach Möglichkeit<br>als<br>unsignierte<br>Attribute bzw. Properties in den entsprechenden<br>digitalen<br>Signaturen<br>bzw.<br>in<br>den<br>Kind-<br>Elementen<br>`certificateValues`<br>bzw.<br>`revocationValues`<br>des<br>`credential`-<br>Elementes mit Bezug auf den entsprechenden<br>Evidence Record abgelegt werden.<br>•<br>`ReturnVerificationReport`<br>Durch<br>die<br>Übergabe<br>eines<br>`ReturnVerificationReport`-Elementes<br>gemäß[OASIS VR]bzw.[eCard-2]und[TR-<br>ESOR-VR] kannein ausführlicher Prüfbericht in<br>Form eines`VerificationReport`-Elementes<br>für die übergebenen Objekte (Signaturen, Siegel,<br>Zeitstempel,<br>Zertifikate,<br>Sperrinformationen,<br>Evidence Records, XAIP, LXAIP, ASiC-AIP mit den<br>vorgenannten Daten) angefordert werden. Wenn<br>nur<br>das<br>Element<br>`ReturnVerificationReport`<br>übergeben<br>wird ohne Angabe der Signature-Policy, dannist<br>im Rahmen des`VerifyResponse`-Elements<br>nur<br>das<br>erzeugte<br>`VerificationReport`-<br>Element zurück zu geben.||
||`dss:InputDocuments`|Das<br>`dss:InputDocuments`-Element enthält die zur<br>Prüfung benötigten Dokumente, sofern diese nicht<br>bereits im unten erläuterten`SignatureObject`-Element<br>enthalten sind.<br>Außerdemkannin einem`dss:Document/InlineXML`-<br>Kindelement ein`XAIP`-Element mit einem XAIP gemäß<br>[TR-ESOR-F](Abs. 3.1) oder einem LXAIP-Element<br>gemäß<br>[TR-ESOR-F]<br>(Abs. 3.2)<br>bzw.<br>in<br>einem<br>`dss:Document/dss:Base64Data`-Kindelement ein ASiC-<br>AIP gemäß[TR-ESOR-F](Abs. 3.3) übergeben werden, so<br>dass alle darin enthaltenen digitalen Signaturen in<br>Verbindung mit der oben angegebenen Signature-Policy<br>geprüft und ergänzt werden oder die Prüfung der darin<br>enthaltenen Evidence Records angestoßen wird.||
||`dss:SignatureObject`|**(A3.7.1-4) :**<br>Als<br>Kindelement<br>von<br>`dss:SignatureObject/Other` kannauch ein<br>`xaip:EvidenceRecord`-Element<br>übergeben<br>werden, um die entsprechende Prüfung des<br>Evidence Record anzustoßen. In diesem Fall<br>müssendie Attribute `AOID` und`VersionID`<br>vorhanden sein und das zugehörige`XAIP`-bzw.<br>`LXAIP`-<br>muss<br>als<br>Kindelement<br>von<br>`dss:InputDocuments/`<br>`dss:Document/dss:InlineXML` und im Falle von<br>ASiC-AIP-Elementmussals Kindelement von||



Bundesamt für Sicherheit in der Informationstechnik 

39 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

|Name||**_`VerifyRequest`_**||
|---|---|---|---|
|||||
|||`dss:InputDocuments/dss:Document`<br>`/dss:Base64Data`übergeben werden.<br>Sofern das`dss:SignatureObject`-Element fehlt,muss<br>genau ein`dss:InputDocuments`-Element vorhanden<br>sein, das die zu prüfenden digitalen Signaturobjekte<br>enthält.|muss|



## 3.7.2 Ausgabeparameter: VerifyResponse 

|Name|**_`VerifyResponse`_**|**_`VerifyResponse`_**|
|---|---|---|
|Beschreibung|Als<br>Antwort<br>auf<br>einen<br>`VerifyRequest`<br>wird<br>ein<br>entsprechendes<br>`VerifyResponse`-Element gemäß Abs. 3.2.2 von[eCard-2]zurückgeliefert.||
|Details|Der Ausgabeparameter`ArchiveDataResponse`weist folgenden Aufbau auf<br>und kann wie folgt parametrisiert werden.||
||Name|Beschreibung|
||`dss:Result`|Enthält die Statusinformationen und die Fehler<br>zu einer durchgeführten Aktion. Die Struktur<br>dieses Elements und die möglichen Fehlercodes<br>sind in Abs. 4.1.2 von[eCard-1]und Abs. 3.2.2<br>von[eCard-2]beschrieben.|
||`dss:OptionalOutputs`|Sofern ein VerificationReport angefordert wurde<br>oder ein Fehler aufgetreten ist, enthält dieses<br>Element den Prüfbericht in Form eines<br>`VerificationReport`-Elementes oder das um<br>diese<br>Prüfinformationen<br>ergänzte<br>Archivdatenobjekt in Form eines`xaip:XAIP`-<br>Elements.<br>Die grundsätzliche Struktur des Prüfberichtes ist<br>in<br>[OASIS-VR]<br>näher<br>beschrieben.<br>In<br>[TR-ESOR-VR]<br>finden<br>sich<br>entsprechende<br>Korrekturen für den`EvidenceRecordReport`<br>sowie die Beschreibung des`XAIPReport`.<br>Details zur Ablage dieser Prüfinformationen im<br>XAIP- bzw. LXAIP-Container finden sich in[TR-<br>ESOR-F].|



Bundesamt für Sicherheit in der Informationstechnik 

40 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

## 3.8 Funktion: RetrieveInfo 

Mit dem Aufruf der Funktion `RetrieveInfo` ist es möglich, die in Form eines Profils verfasste Beschreibung der Fähigkeiten des Bewahrungsproduktes bzw. -dienstes zu erfragen. Da es im Laufe der Zeit dazu kommen kann, dass ein Bewahrungsdienst bzw. –produkt mehrere solcher Profile unterstützt, ist es mit Hilfe entsprechenden Parametrisierung der Funktionseingabe ( `RetrieveInfoRequest` ) möglich, nach gewünschten Profilen zu filtern. Die durch das Bewahrungsprodukt bzw. den Bewahrungsdienst ermittelten Ergebnisse werden mit Hilfe des Ausgabeparameters `RetrieveInfoReponse` zurückgeliefert. 

Wie in Abbildung 3 und Abbildung 4 ersichtlich, wird diese Funktion ausschließlich an der hier betrachteten Schnittstelle TR-S.4 angeboten. 

## 3.8.1 Eingabeparameter: RetrieveInfoRequest 

|Name|**_`RetrieveInfoRequest`_**|**_`RetrieveInfoRequest`_**|**_`RetrieveInfoRequest`_**|
|---|---|---|---|
|||||
|Beschreibung<br><br>|Mit dem Eingabeparameter`RetrieveInfoRequest`wird beim Aufruf der Funktion<br>`RetrieveInfo`vorgegeben, nach welchen Profilen eines Bewahrungsprodukts bzw.<br>-dienstes gesucht wird.|||
|Details<br>|Der Eingabeparameter`RetrieveInfoRequest`weist folgenden Aufbau auf und<br>kann wie folgt parametrisiert werden.|||
||Name|Beschreibung||
||`dss:OptionalInputs`<br>|Es<br>werden<br>standardmäßig<br>Eingabeelemente unterstützt.|keine<br>optionalen|
||`tr:ProfileIdentifier`<br> <br> <br>|Mit Hilfe dieses Parameterskannein durch die Eingabe<br>einer URI (gem.[RFC3986]) spezifizierte Profile gezielt<br>angefragt werden.<br>Gegenwärtig werden durch diese TR-ESOR-Spezifikation<br>V1.3 folgende URIs unterstützt:<br>•<br>`http://www.bsi.bund.de/tr-`<br>`esor/V1.3.0/profile/S.4/V1.0`<br>oder<br>•<br>`http://www.bsi.bund.de/tr-`<br>`esor/V1.3.0/profile/preservation-`<br>`api/v1.1.2` - Verweis auf die aktuelle TR-ESOR-<br>S.512-Schnittstelle||



Bundesamt für Sicherheit in der Informationstechnik 

41 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

|Name||**_`RetrieveInfoRequest`_**|**_`RetrieveInfoRequest`_**|
|---|---|---|---|
|||||
||`tr:Status`<br> <br>|Mit Hilfe dieses Parameterskannzwischen:<br>•<br>aktiven (Wert: `active`),<br>•<br>nicht aktiven (Wert: `inactive`) oder<br>•<br>beiden (Wert: `all`)<br>Profilen bei der Suche unterschieden werden (vgl. Kap.<br>5.4.8[ETSI TS 119 512]).<br>Sollte dieser Parameter ungesetzt bleiben, so gilt die<br>Standardbelegung:`active`.||



## 3.8.2 Ausgabeparameter: RetrieveInfoResponse 

|Name|**_`RetriveInfoResponse`_**|**_`RetriveInfoResponse`_**|**_`RetriveInfoResponse`_**|
|---|---|---|---|
|||||
|Beschreibung|Als Antwort auf`RetrieveInfoRequest`wird ein`RetrieveInfoResponse`-<br>Element zurückgeliefert, das die ermittelten Profile des Bewahrungsproduktes<br>bzw. -dienstes beinhaltet.|||
|Details|Der Ausgabeparameter`RetrieveInfoResponse`weist folgenden Aufbau auf und<br>kann wie folgt parametrisiert werden.|||
||Name|Beschreibung||
||`dss:Result`|Das Element enthält die Statusinformationen und<br>die Fehler zu einer durchgeführten Aktion. Die<br>Struktur dieses Elements ist in[eCard-1]und unten<br>näher beschrieben.||
||`dss:OptionalOutputs`|Es<br>werden<br>standardmäßig<br>Ausgabeelemente unterstützt.|keine<br>optionalen|
||`pres:Profile`|Eine Liste der ermittelten Profile, die entsprechend<br>der Parametrisierung der Eingabe ermittelt wurden.<br>Die Liste kann auch u.U. leer sein.<br>Die<br>Inhalte<br>der<br>Profile<br>entsprechend<br>der<br>Spezifikation des Elements`pres:Profile`in[ETSI<br>TS 119 512], Kap. 5.4.7.||



Bundesamt für Sicherheit in der Informationstechnik 

42 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

|Name|**_`RetriveInfoResponse`_**|**_`RetriveInfoResponse`_**|**_`RetriveInfoResponse`_**|
|---|---|---|---|
|||||
||Statusinformationen und Fehler beim Aufruf der Funktion`RetrieveInfo`(vgl.<br>[eCard-1]Abs. 4.1 und Abs. 4.2).|||
||Name|Fehlercode||
||`dss:ResultMajor`|•<br>•|/resultmajor#ok<br>/resultmajor#error|
||`dss:ResultMinor`|•<br>•<br>•<br>•|/resultminor/al/common#noPermission<br>/resultminor/al/common#internalError<br>/resultminor/al/common#parameterError<br>/resultminor/arl/notSupported19|



## 3.9 Funktion: ArchiveTrace 

Die Funktion `ArchiveTrace` erlaubt es, eine Dokumentation der bei der Verarbeitung eines Archivdatenobjekts innerhalb des Bewahrungsproduktes bzw. -diensts ausgeführten Schritte abzurufen. Diese Dokumentation kann beispielweise im Zuge eines Audits verwendet werden. 

## 3.9.1 Eingabeparameter: ArchiveTraceRequest 

|Name|**_`ArchiveTraceRequest`_**|**_`ArchiveTraceRequest`_**|
|---|---|---|
||||
|Beschreibung|Mit dem Eingabeparameter`ArchiveTraceRequest`wird beim Aufruf der<br>Funktion`ArchiveTrace`vorgegeben, nach welcher Verarbeitungsdokumentation<br>(z.B. Logdateien) für welches Archivdatenobjekt eines Bewahrungsproduktes bzw.<br>-dienstes gesucht wird.||
|Details|Der Eingabeparameter`ArchiveTraceRequest`weist folgenden Aufbau auf und<br>kann wie folgt parametrisiert werden.||
||Name<br>|Beschreibung|



- 19 Im ResultMessage-Element sollen nähere Informationen darüber zurückgeliefert werden, welche angeforderte Funktionalität nicht unterstützt wird. 

Bundesamt für Sicherheit in der Informationstechnik 

43 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

|Name|**_`ArchiveTraceRequest`_**|**_`ArchiveTraceRequest`_**|||
|---|---|---|---|---|
||||||
||`dss:OptionalInputs`|Es werden standardmäßig<br>Eingabeelemente unterstützt.|keine|optionalen|
||`tr:AOID`|Mit<br>Hilfe<br>dieses<br>Parameters<br>muss<br>das<br>Archivdatenobjekt,<br>dessen<br>Verarbeitungsdokumentation ermittelt werden<br>soll, referenziert werden.|||



## 3.9.2 Ausgabeparameter: ArchiveTraceResponse 

|Name|**_`ArchiveTraceResponse`_**|**_`ArchiveTraceResponse`_**|**_`ArchiveTraceResponse`_**|
|---|---|---|---|
|||||
|Beschreibung|Als Antwort auf den Eingabeparameter`ArchiveTraceRequest`wird ein<br>`ArchiveTraceReponse`-Element<br>zurückgeliefert,<br>das<br>die<br>angeforderte<br>Verarbeitungsdokumentation des gewünschten Archivdatenobjekts beinhaltet.|||
|Details|Der Ausgabeparameter`ArchiveTraceResponse`weist folgenden Aufbau auf und<br>kann wie folgt parametrisiert werden.|||
||Name|Beschreibung||
||`dss:Result`|Das Element enthält die Statusinformationen und<br>die Fehler zu einer durchgeführten Aktion. Die<br>Struktur dieses Elements ist in[eCard-1]und unten<br>näher beschrieben.||
||`dss:OptionalOutputs`|Es<br>werden<br>standardmäßig<br>Ausgabeelemente unterstützt.|keine<br>optionalen|
||`pres:Trace`|Die Rückgabe der Funktionmussdas`pres:Trace`-<br>Element enthalten.<br>Im Erfolgsfallmussdieses Element zumindest ein<br>Unterelement`pres:Event`beinhalten. Die genaue<br>Ausgestaltung des`pre:Event`-Elements ist dem Kap.<br>5.4.10 in[ETSI TS 119 512]zu entnehmen.<br>In einem Fehlerfall kann das`pres:Trace`-Element<br>leer sein.||



Bundesamt für Sicherheit in der Informationstechnik 

44 

Funktionen der ArchiSafe-Schnittstelle (TR-S.4) 

Name _**`ArchiveTraceResponse`**_ Statusinformationen und Fehler beim Aufruf der Funktion `ArchiveTrace` (vgl. [eCard-1] Abs. 4.1 und Abs. 4.2). 

|Name|Fehlercode|Fehlercode|
|---|---|---|
|`dss:ResultMajor`|•|/resultmajor#ok|
||•|/resultmajor#error|
|`dss:ResultMinor`|•|/resultminor/al/common#noPermission|
||•|/resultminor/al/common#internalError|
||•|/resultminor/al/common#parameterError|
||•|/resultminor/arl/notSupported20|
||•|/resultminor/arl/unknownAOID|



> 20Im ResultMessage-Element sollen nähere Informationen darüber zurückgeliefert werden, welche angeforderte Funktionalität nicht unterstützt wird. 

Bundesamt für Sicherheit in der Informationstechnik 

45 

Funktionen der Preservation-API gemäß ETSI TS 119 512 in der Profilierung [TR-ESOR-TRANS] 

## 4. Funktionen der Preservation-API gemäß ETSI TS 119 512 in der Profilierung [TR-ESOR-TRANS] 

Neben der in Abs. 3 spezifizierten TR-ESOR-S.4 Schnittstelle steht mit der „Preservation-API“ aus [ETSI TS 119 512] in der Profilierung [TR-ESOR-TRANS] eine funktional weitgehend äquivalente, international standardisierte Alternative zur Verfügung, die zusätzlich oder anstatt der TR-ESOR-S.4-Schnittstelle als Eingangsschnittstelle zur TR-ESOR-Middleware genutzt werden kann. 

- (Α4.0−1) Für den Einsatz der „Preservation-API“ gemäß [ETSI TS 119 512] in der Profilierung [TRESOR-TRANS] im Rahmen der vorliegenden Technischen Richtlinie müssen die folgenden Mindestanforderungen unterstützt werden: • `RetrieveInfo` gemäß Abs. 3.1 von **[TR-ESOR-TRANS]** muss unterstützt werden. Hierbei muss zumindest ein Bewahrungsprofil unterstützt werden, welches das Bewahrungsschema `http://uri.etsi.org/19512/scheme/pds+pgd+aug+wst+ers` gemäß Annex F.1 von **[ETSI TS 119 512]** umsetzt. 

   - `PreservePO` gemäß Abs. 3.2 von [TR-ESOR-TRANS] muss unterstützt werden, wobei zumindest eines der in [TR-ESOR-F] definierten Archivdatenobjekt-Formate (XAIP, LXAIP oder ASiC-AIP) unterstützt werden muss. 

   - `RetrievePO` gemäß Abs. 3.4 von [TR-ESOR-TRANS] muss unterstützt werden, wobei zumindest eines der in [TR-ESOR-F] definierten Archivdatenobjekt-Formate (XAIP, LXAIP oder ASiC-AIP) sowie Evidence Records gemäß [RFC4998] bzw. gemäß [RFC4998] in der Profilierung gemäß [TRESOR-ERS] unterstützt werden müssen. 

   - `DeletePO` gemäß Abs. 3.5 von [TR-ESOR-TRANS] muss unterstützt werden. 

   - `UpdatePOC` gemäß Abs. 3.3 von [TR-ESOR-TRANS] muss unterstützt werden. 

   - `RetrieveTrace` gemäß Abs. 5.3.7 von [ETSI TS 119 512] kann unterstützt werden. 

   - `ValidateEvidence` gemäß Abs. 3.6 von [TR-ESOR-TRANS] muss unterstützt werden. Sofern diese Operation unterstützt wird, muss zumindest die Validierung von Evidence Records gemäß [RFC4998] oder gemäß [RFC4998] in der Profilierung gemäß [TR-ESOR-ERS] , Basic-ERS-Profile und die Validierung der in [TR-ESOR-F] definierten Archivdatenobjekt-Formate (XAIP, LXAIP oder ASiC-AIP) unterstützt werden. Darüber hinaus kann die Validierung von Evidence Records gemäß [RFC6283] unterstützt werden. 

   - `Search` gemäß Abs. 3.7 von [TR-ESOR-TRANS] kann unterstützt werden. 

- (Α4.0−2) Die Belegung der Eingabe- und Ausgabe-Parameter der unterstützten Funktionen im Rahmen des „Preservation-APIs“ muss gemäß dem TR-ESOR-Anlage [TR-ESOR-TRANS] erfolgen, der eine geeignet profilierte Ausprägung der Preservation-API gemäß [ETSI TS 119 512] spezifiziert, die auf die TR-S.4-Schnittstelle gemäß [TR-ESOR-E] abgebildet werden kann. 

- (Α4.0−3) Für den Einsatz der „Preservation-API“ gemäß [ETSI TS 119 512] in der Profilierung [TRESOR-TRANS] im Rahmen der vorliegenden Technischen Richtlinie müssen die folgenden Basistypen für „Request“ und „Response“ unterstützt werden: 

   - Falls das `OptionalInputs` Element vorhanden ist, dann muss es eine Sub-Komponente, wie definiert in ( [OASIS DSS-X] , Kapitel 4.1.8), enthalten. 

- Falls das `OptionalOutputs` Element vorhanden ist, dann muss es eine Sub-Komponente, wie definiert in ( [OASIS DSS-X] , Kapitel 4.1.9), enthalten. 

- 4.1 Vergleich der TR-S.512- mit der TR-S.4-Schnittstelle 

Hierbei entspricht die Preservation-API gemäß [ETSI TS 119 512] in der Profilierung [TR-ESOR-TRANS] – TR-S.512 – der Eingangs-Schnittstelle TR-S.4 zur TR-ESOR-Middleware [TR-ESOR-E], wie in der folgenden Tabelle dargestellt. 

Bundesamt für Sicherheit in der Informationstechnik 

46 

Funktionen der Preservation-API gemäß ETSI TS 119 512 in der Profilierung [TR-ESOR-TRANS] 

Tabelle 3: Vergleich ETSI TS 119 512 (prof. [TR-ESOR-TRANS]) Preservation-API mit TR-ESOR-S.4-Schnittstelle 

|ETSI TS 119 512|Verbindlichkeitsgrad|TR-ESOR V1.3 ff|Verbindlichkeitsgrad|
|---|---|---|---|
|(prof. [TR-ESOR-||||
|||||
|TRANS])||||
|`PreservePO`|verpflichtend|`ArchiveSubmission`|verpflichtend|
|`DeletePO`|verpflichtend|`ArchiveDeletion`|verpflichtend|
|`RetrievePO`|verpflichtend|`ArchiveEvidence`|verpflichtend|
|`RetrievePO`|verpflichtend|`ArchiveRetrieval`|verpflichtend|
|`UpdatePOC`|verpflichtend|`ArchiveUpdate`|verpflichtend|
|`ValidateEvidence`|verpflichtend|`Verify`|verpflichtend|
|`RetrieveInfo`|verpflichtend|`RetrieveInfo`|verpflichtend|
|`RetrieveTrace`|optional|`ArchiveTrace`|optional|
|`Search`|optional|`ArchiveData`|optional|



Bundesamt für Sicherheit in der Informationstechnik 

47 

Funktionen der internen Schnittstellen 

## 5. Funktionen der internen Schnittstellen 

In diesem Abschnitt werden die internen Schnittstellen der Referenzarchitektur TR-S.1 bis TR-S.3 und TRS.5 bis TR-S.6 (vgl. Abbildung 3 und Abbildung 4) erläutert: 

- TR-S.1 (ArchiSafe-Modul – Krypto-Modul) (siehe Abs. 5.1) 

- TR-S.2 (ArchiSig-Modul – ECM-/Langzeitspeichersystem) (siehe Abs. 5.2) 

- TR-S.3 (ArchiSig-Modul – Krypto-Modul) (siehe Abs. 5.3) 

- TR-S.5 (ArchiSafe-Modul – ECM-/Langzeitspeichersystem) (siehe Abs. 5.4) 

- TR-S.6 (ArchiSafe-Modul – ArchiSig-Modul) (siehe Abs. 5.5). 

## 5.1 TR-S.1 (ArchiSafe-Modul – Krypto-Modul) 

Dieser Abschnitt beschreibt, wie die Abbildung 3 und Abbildung 4 dargestellte Schnittstelle TR-S.1 auf Basis des eCard-API-Frameworks (vgl. [TR-03112] ) umgesetzt werden kann. 

Diese Schnittstelle TR-S.1 umfasst zwei wesentliche Funktionen: 

   - Prüfung von digitalen Signaturen, beweisrelevanten Daten, Beweisdaten und Archivdatenobjekten (Funktion `VerifyRequest` ) 

   - Anforderung von digitalen Signaturen (optional) (Funktion `SignRequest` ) 

- 5.1.1 Prüfung von digitalen Signaturen, beweisrelevanten Daten, Beweisdaten und Archivdatenobjekten 

Für die Prüfung von digitalen Signaturen, beweisrelevanten Daten (Zertifikaten, Zertifikatstatusinformationen, Zeitstempeln, etc.), Beweisdaten (Evidence Records) und Archivdatenobjekten (XAIPs bzw. LXAIPs bzw. ASiC-AIP) ist in [OASIS-DSS] und [eCard-2] der Funktionsaufruf `VerifyRequest` und die zugehörige Antwort `VerifyResponse` definiert. Entsprechende Korrekturen und Ergänzungen sind darüber hinaus in [TR-ESOR-VR] bzw. in Abs. 3.7 erläutert. 

- (Α5.1.1−1) Die Durchführung der eigentlichen Prüffunktion von beweisrelevanten Daten sowie Beweisdaten muss im Krypto-Modul (siehe Anlage [TR-ESOR-M.2] ) als Komponente der TR-ESORMiddleware oder in einem vom Krypto-Modul aufgerufenen, (qualifizierten) Vertrauensdienst erfolgen. Die für die Prüfung notwendiger Prüfinformationen (z. B. OCSP-Antworten oder Sperrlisten) müssen von den Vertrauensdiensteanbietern abgerufen werden. 

## 5.1.2 Anforderung einer digitalen Signatur 

Für die Anforderung einer digitalen Signatur ist in [OASIS-DSS] und [eCard-2] die Anfrage `SignRequest` und die zugehörige Antwort `SignResponse` definiert. 

## 5.1.2.1 SignRequest (Anforderung einer digitalen Signatur) 

Ein `SignRequest` im Kontext der Schnittstelle S.1 übergibt ein Archivdatenobjekt (XAIP- bzw. LXAIP- bzw. ASiC-AIP-Dokument) an das Krypto-Modul zur Anforderung einer digitalen Signatur. 

Bundesamt für Sicherheit in der Informationstechnik 

48 

Funktionen der internen Schnittstellen 

|Name|**_`SignRequest`_**|**_`SignRequest`_**|**_`SignRequest`_**|
|---|---|---|---|
|Beschreibung|(Α5.1.2−1)<br>Mit dem Funktionseingabeparameter`SignRequest` aus[eCard-<br>2] kannfür das übergebene Archivdatenobjekt eine digitale Signatur von<br>einem (qualifizierten) Vertrauensdiensteanbieter gemäß[eIDAS-VO],<br>Artikel 3 Nr. 19 bzw. Nr. 20 angefordert werden.|||
|Details|Der Eingabeparameter`SignRequest`weist folgenden Aufbau auf und kann wie<br>folgt parametrisiert werden.|||
||Name||Beschreibung|
||`dss:OptionalInputs`||Kanneines oder mehrere der in[eCard-2]<br>definierten<br>optionalen<br>Eingabeelemente<br>|
||`dss:InputDocuments`||~~th lt~~<br>Enthält die zu signierenden Dokumente oder<br>Datenstrukturen. Weitere Informationen hierzu<br>finden sich in[OASIS-DSS]und[eCard-2].|



## 5.1.2.2 SignResponse 

|Name|**_`SignResponse`_**|**_`SignResponse`_**|
|---|---|---|
|Beschreibung|Als Antwort auf einen<br>`SignRequest`<br>wird vom Krypto-Modul ein<br>entsprechendes`SignResponse`-Element gemäß Abs. 3.2.1 von[eCard-2]<br>zurückgeliefert.||
|Details|Der Ausgabeparameter`SignResponse` weist folgenden Aufbau auf und kann wie<br>folgt parametrisiert werden.||
||Name|Beschreibung|
||`dss:Result`|Dieses Element enthält die Statusinformationen<br>und die Fehler zu einer durchgeführten Aktion. Die<br>Struktur dieses Elements und die möglichen<br>Fehlercodes sind in Abs. 4.1.2 von[eCard-1]und in<br>Abs. 3.2.1 von[eCard-2]beschrieben.|



Bundesamt für Sicherheit in der Informationstechnik 

49 

Funktionen der internen Schnittstellen 

|Name|||**_`SignResponse`_**|
|---|---|---|---|
||`dss:OptionalOutputs`||Kann<br>ein<br>`DocumentWithSignature`-Element<br>enthalten, in denen z.B. ein`XAIP`-Element mit der<br>eingebetteten digitalen Signatur enthalten ist.<br>Details finden sich in Abs. 3.2.1 von[eCard-2].|
||`dss:SignatureObject`||Kanneine erzeugte digitale Signatur in Form eines<br>`dss:SignatureObject`-Elementes<br>enthalten.<br>Details finden sich in Abs. 3.2.1 von[eCard-2].<br>Sofern die erstellte digitale Signatur bereits im<br>oben<br>genannten<br>`DocumentWithSignature`-<br>Element<br>vorhanden<br>ist,<br>wird<br>kein<br>`dss:SignatureObject`-Element zurückgeliefert.|



## 5.2 TR-S.2 (ArchiSig-Modul – ECM-/Langzeitspeichersystem) 

Dieser Abschnitt beschreibt in den folgenden Unterkapiteln, wie die in Abbildung 3 und Abbildung 4 dargestellte Schnittstelle TR-S.2 auf Basis der auch dem eCard-API-Frameworks (vgl. [TR-03112] zu Grunde liegenden Basistypen aus [OASIS-DSS] umgesetzt werden kann. 

Diese Schnittstelle umfasst drei wesentliche Funktionen: 

- Speichern eines Archivdatenobjektes (Funktion `ArchiveSubmission` ) 

- Ergänzen einer neuen Version eines Archivdatenobjektes (Funktion `ArchiveUpdate` ) 

Auslesen eines Archivdatenobjektes (Funktion `ArchiveRetrieval` ). 

- (Α5.2−1) Neben der Umsetzung der Funktion „Speichern eines Archivdatenobjektes“ ( `ArchiveSubmission` ) auf Basis der, auch dem eCard-API-Frameworks [TR-03112] zu Grunde liegenden, Basistypen aus [OASIS-DSS] kann diese Funktion auch als „UploadRequest“ beliebig anders technisch umgesetzt werden, um den Upload von Datenobjekten im Rahmen eines logischen XAIP (LXAIP) gemäß [TR-ESOR-F] , Abs. 3.2 technisch performant zu ermöglichen. Dabei müssen die Anforderungen gemäß [TR-ESOR] , Abs. 7, insbesondere Abs. 7.2 und Abs. 7.4.4 erfüllt werden. 

- (Α5.2−2) Laut [ETSI TS 119 511] muss die folgende Anforderung erfüllt sein: „OVR-7.8-02 [WST] The preservation service shall be integrated in the IT environment implemented in such a way that all storage access by the preservation client changing the content of the storage shall only be done by the preservation service“. Daher ist es erforderlich, dass die eigentliche „Upload-Komponente“ ein (eigenständiges) Modul der TR-ESOR-Middleware darstellen muss und logisch als Teil des TR-ESORSystems zu betrachten sein muss. 

## 5.2.1 Speichern eines Archivdatenobjektes 

Für das Speichern eines Archivdatenobjektes ist in Abbildung 3 und Abbildung 4 die Anfrage `ArchiveSubmissionRequest` und die zugehörige Antwort `ArchiveSubmissionResponse` gemäß Abs. 3.1 vorgesehen. 

## 5.2.2 Ergänzen einer neuen Version eines Archivdatenobjektes 

Für das Ergänzen einer neuen Version eines Archivdatenobjektes ist in Abbildung 3 und Abbildung 4 die Anfrage `ArchiveUpdateRequest` und die zugehörige Antwort `ArchiveUpdateResponse` gemäß Abs. 3.2 vorgesehen. 

## 5.2.3 Auslesen von Archivdatenobjekten 

Für das Auslesen von Archivdatenobjekten ist in Abbildung 3 und Abbildung 4 die Anfrage `ArchiveRetrievalRequest` und `ArchiveRetrievalResponse` gemäß Abs. 3.3 vorgesehen. 

Bundesamt für Sicherheit in der Informationstechnik 

50 

Funktionen der internen Schnittstellen 

## 5.3 TR-S.3 (ArchiSig-Modul – Krypto-Modul) 

Dieser Abschnitt beschreibt, wie die in Abbildung 3 und Abbildung 4 dargestellte Schnittstelle TR-S.3 auf Basis des eCard-API-Frameworks [TR-03112] umgesetzt werden kann. 

Die Schnittstelle TR-S.3 umfasst drei wesentliche Funktionen: 

   - Anfordern eines (qualifizierten) Zeitstempels (Funktion `SignRequest` ) 

   - Prüfen eines (qualifizierten) Zeitstempels (Funktion `VerifyRequest` ) 

   - Berechnung eines Hashwertes (Funktion `HashRequest` ) 

- 5.3.1 Anfordern eines (qualifizierten) Zeitstempels 

Zum Anfordern eines (qualifizierten) Zeitstempels kann eine geeignet profilierte Anfrage `SignRequest` mit entsprechender Antwort `SignResponse` gemäß [OASIS-DSS] bzw. [eCard-2] genutzt werden. 

- (Α5.3.1−1) Der qualifizierte Zeitstempel muss von einem qualifizierten Vertrauensdiensteanbieter gemäß [eIDAS-VO] , Artikel 3 Nr. 20 durch das Krypto-Modul (siehe Anlage [TR-ESOR-M.2] ) als eine Komponente der Middleware angefordert werden. 

- 5.3.1.1 SignRequest für das Anfordern eines Zeitstempels 

|Name|**_`SignRequest`_**|**_`SignRequest`_**|
|---|---|---|
|Beschreibung|Ein`SignRequest`im Kontext der Schnittstelle S.3 übergibt einen Hashwert, zu<br>dem ein (qualifizierter) Zeitstempel erstellt werden soll, an das Krypto-Modul.||
|Details|Der Eingabeparameter`SignRequest`weist folgenden Aufbau auf und kann wie<br>folgt parametrisiert werden.||
||Name|Beschreibung|
||`dss:OptionalInputs`|Enthält genau ein Element`SignatureType` mit der<br>URIurn:ietf:rfc:3161, durch die klargestellt wird,<br>dass ein Zeitstempel gemäß[RFC3161]erzeugt<br>werden soll.|
||`dss:InputDocuments`|**(A5.3.1-2)**<br>Während<br>das<br>Element<br>`dss:InputDocuments` in[OASIS-DSS]und<br>[eCard-2]optional ist,musses hier vorhanden<br>sein und genau ein `dss:Document`-Elementin<br>der<br>`DocumentHash`-Ausprägung<br>enthalten.<br>Dieses Element enthält den Hashwert, aus dem<br>ein (qualifizierter) Zeitstempel erzeugt werden<br>soll.|



Bundesamt für Sicherheit in der Informationstechnik 

51 

Funktionen der internen Schnittstellen 

## 5.3.1.2 SignResponse mit Zeitstempel 

|Name|**_`SignResponse`_**|**_`SignResponse`_**|
|---|---|---|
|Beschreibung|Als Antwort auf einen<br>`SignRequest`<br>wird vom Krypto-Modul ein<br>entsprechendes`SignResponse`-Element gemäß Abs. 3.2.1 von[eCard-2]<br>zurückgeliefert. Im Kontext der Schnittstelle S.3 wird hier ein (qualifizierter)<br>Zeitstempel zurückgeliefert.||
|Details|Der Ausgabeparameter`SignResponse` weist folgenden Aufbau auf und kann wie<br>folgt parametrisiert werden.||
||Name|Beschreibung|
||`dss:Result`|Enthält die Statusinformationen und die Fehler<br>zu einer durchgeführten Aktion. Die Struktur<br>dieses Elements und die möglichen Fehlercodes<br>sind in Abs. 4.1.2 von[eCard-1]und in Abs. 3.2.1<br>von[eCard-2]beschrieben.|
||`dss:OptionalOutputs`|Das optionale Element`dss:OptionalOutputs` ist<br>nicht vorhanden.|
||`dss:SignatureObject`|Enthält – sofern kein Fehler aufgetreten ist –<br>genau ein`dss:SignatureObject`-Element, das<br>ein`dss:Timestamp`-Element enthält, in dem der<br>Zeitstempel<br>in<br>Form<br>eines<br>`RFC3161TimeStampToken`-Elementes<br>enthalten<br>ist.|



## 5.3.2 Prüfen eines (qualifizierten) Zeitstempels 

Zum Prüfen eines (qualifizierten) Zeitstempels ist in TR-S.3 (vgl. Abbildung 3 und Abbildung 4) die Anfrage `VerifyRequest` und die Antwort `VerifyResponse` gemäß [OASIS-DSS] und [eCard-2] vorgesehen. 

(Α5.3.2−1) Die Durchführung der eigentlichen Prüffunktion eines (qualifizierten Zeitstempels) muss im Krypto-Modul (siehe Anlage [TR-ESOR-M.2] ) als Komponente der TR-ESOR-Middleware oder in einem, vom Krypto-Modul aufgerufen, externen Validierungsdienst eines (qualifizierten) Vertrauensdiensteanbieters erfolgen. Die für die Prüfung notwendigen Prüfinformationen (z. B. OCSPAntworten oder Sperrlisten) müssen von den (qualifizierten) Vertrauensdiensteanbietern abgerufen werden. 

Bundesamt für Sicherheit in der Informationstechnik 

52 

Funktionen der internen Schnittstellen 

## 5.3.2.1 VerifyRequest 

|Name|**_`VerifyRequest`_**|**_`VerifyRequest`_**|**_`VerifyRequest`_**|
|---|---|---|---|
|Beschreibung|Ein<br>`VerifyRequest` im Kontext der Schnittstelle S.3 übergibt einen<br>(qualifizierten) Zeitstempel an das Krypto-Modul zur Verifikation der darin<br>enthaltenen digitalen Signatur. Außerdem werden die für die Prüfung genutzten<br>Zertifikate und Sperrinformationen in den zurück gelieferten Zeitstempel<br>eingefügt. Entsprechende Empfehlungen für die Ablage dieser Informationen<br>finden sich in[TR-ESOR-F].|||
|Details|Der Eingabeparameter`VerifyRequest` weist folgenden Aufbau auf und kann wie<br>folgt parametrisiert werden.|||
||Name||Beschreibung|
||`dss:OptionalInputs`||Kannoptionale Eingabeelemente enthalten.<br>(Α5.3.2−2)<br>Gemäß der vorliegenden Spezifikation<br>muss<br>das<br>optionale<br>Eingabeelement<br>`ReturnUpdatedSignature`<br>aus<br>Abs. 4.5.8<br>von<br>[OASIS-DSS]unterstützt werden, bei dem mit dem<br>Type-Attribut:<br>•<br>`http://www.bsi.bund.de/DE/tr-`<br>`esor/sigpolicy/verify-timestamp`<br>•<br>`http://www.bsi.bund.de/DE/tr-`<br>`esor/sigpolicy/verify-timestamp/shell`<br>oder<br>•<br>`http://www.bsi.bund.de/DE/tr-`<br>`esor/sigpolicy/verify-timestamp/chain`<br>klargestellt wird, dass:<br>1)<br>alle bei der Prüfung verwendeten Zertifikate und<br>Sperrinformationen und Prüfinformationen, wie in<br>[TR-ESOR-F]spezifiziert, in den Zeitstempel<br>eingefügt werdenmüssen.<br>2)<br>alle digitalen Signaturinformationen (Signaturen,<br>Siegel, Zeitstempel, Zertifikate, Sperrlisten, OCSP-<br>Responses etc.) bis hin zu einer vertrauenswürdigen<br>Wurzel bzw. Vertrauensanker gemäß der vom[TR-<br>ESOR-PEPT]abgeleiteten und veröffentlichten<br>Preservation Policy (PEP) des TR-ESOR-Produktes<br>bzw. Bewahrungsdienstes geprüft werdenmüssen.<br>(A5.3.2-3)<br>Darüber<br>hinaus<br>soll<br>das<br>optionale<br>Eingabeelement<br>`ReturnVerificationReport`<br>unterstützt werden, sodass für den entsprechenden<br>Zeitstempel<br>ein<br>Prüfbericht<br>gemäß<br>[OASIS-VR]<br>zurückgeliefert werden kann.|



Bundesamt für Sicherheit in der Informationstechnik 

53 

Funktionen der internen Schnittstellen 

|Name|||**_`VerifyRequest`_**|
|---|---|---|---|
|||||
||`dss:InputDocuments`||Das optionale Element`dss:InputDocuments` soll<br>nichtvorhanden sein und wird ignoriert.|
||`dss:SignatureObject`||Es ist genau ein`dss:SignatureObject`-Element in der<br>`dss:TimeStamp/RFC3161TimeStampToken`<br>Ausprägung vorhanden, das den zu prüfenden<br>Zeitstempel enthält.|



## 5.3.2.2 VerifyResponse 

|Name|**_`VerifyResponse`_**|**_`VerifyResponse`_**|
|---|---|---|
|Beschreibung|Als Antwort auf einen`VerifyRequest` wird vom Krypto-Modul ein<br>entsprechendes`VerifyResponse`-Element gemäß Abs. 3.2.2 von[eCard-2]<br>zurückgeliefert.||
|Details|Der Ausgabeparameter`ArchiveDataResponse` weist folgenden Aufbau auf<br>und kann wie folgt parametrisiert werden.||
||Name|Beschreibung|
||`dss:Result`|Enthält die Statusinformationen und die Fehler<br>zu einer durchgeführten Aktion. Die Struktur<br>dieses Elements und die möglichen Fehlercodes<br>sind in Abs. 4.1.2 von[eCard-1]und in Abs. 3.2.2<br>von[eCard-2]beschrieben.|
||`dss:OptionalOutputs`|Sofern nicht ein Fehler aufgetreten ist,mussein<br>`UpdatedSignature`-Element vorhanden sein,<br>das ein`dss:SignatureObject`-Element in der<br>`dss:TimeStamp/`<br>`RFC3161TimeStampToken`-<br>Ausprägung enthält, in dem sich der um die bei<br>der<br>Prüfung<br>genutzten<br>Zertifikate<br>und<br>Sperrinformationen<br>ergänzte<br>Zeitstempel<br>befindet.<br>Darüber hinauskannein`VerificationReport`-<br>Element gemäß[OASIS VR]vorhanden sein, das<br>im`IndividualReport/Details`-Element ein<br>`IndividualTimeStampReport`-Element enthält.|



## 5.3.3 Berechnung eines Hashwertes 

Zur Berechnung eines Hashwertes ist in TR-S.3 (vgl. Abbildung 3 und Abbildung 4) die Anfrage `HashRequest` und die Antwort `HashResponse` aus [eCard-4] in Verbindung mit dem Generic Cryptography-Protokoll aus [eCard-7] vorgesehen. 

Bundesamt für Sicherheit in der Informationstechnik 

54 

Funktionen der internen Schnittstellen 

## 5.3.3.1 HashRequest 

|Name|**_`HashRequest`_**|**_`HashRequest`_**|
|---|---|---|
|Beschreibung|Bei einem`Hash`-Aufruf im Kontext der Schnittstelle TR-S.3 wird für die<br>übergebenen Daten ein Hashwert berechnet.||
|Details|Der Eingabeparameter`HashRequest` weist folgenden Aufbau auf und kann wie folgt<br>parametrisiert werden.||
||Name|Beschreibung|
||`ConnectionHandle`|Das<br>`ConnectionHandle`-Element<br>(vgl.<br>[eCard-4],<br>Abs. 3.1.3)<br>gibt<br>bei<br>Bedarf<br>an,<br>auf<br>welchem<br>Hardwaremodul<br>oder<br>entfernten<br>eCard-API-<br>Framework die Berechnung des Hashwertes erfolgen<br>soll. Sofern die Berechnung des Hashwertes durch das<br>lokale<br>Software-Modul<br>erfolgen<br>soll,<br>soll<br>das<br>`ConnectionHandle`-Element leer sein.|
||`DIDName21`|Dieser Parameter spezifiziert den zu verwendenden<br>Hashalgorithmus.<br>Welche<br>kryptographischen<br>Algorithmen zu einem bestimmten Zeitpunkt als<br>geeignet erachtet werden, ist Gegenstand von[ETSI TS<br>119 312]und[SOG-IS].|
||`DIDScope`|Löst im[ISO 24727-3]Standard Mehrdeutigkeiten<br>zwischen lokalen und globalen DIDs mit gleichem<br>Namen auf. Dieser Parameter wird hier nicht verwendet<br>und sofern vorhanden ignoriert.|
||`Message`|Enthält die Nachricht (bzw. einen Teil derselben, siehe<br>[eCard-7]), aus der ein Hashwert berechnet werden soll.<br>Wird<br>als<br>Inhalt<br>von<br>`Message`-Feld<br>ein<br>`asic:DataObjectReference`-Element<br>gem.<br>[TR-<br>ESOR-F], Kap. 3.2.1 übergeben, so wird der Hashwert<br>nicht über den Elementinhalt selbst, sondern über die<br>aus dem Element referenzierten Daten berechnet. Die<br>referenzierten Daten sind entsprechend anhand der<br>mitgeführten Referenz zu ermitteln|



> 21Eine in [ISO 24727-3] näher beschriebene Differential Identity ermöglicht die Ausführung von kryptographischen Operationen. Der `DIDName` ist der logische Name, der für den Zugriff auf dieses kryptographische Objekt genutzt wird. 

Bundesamt für Sicherheit in der Informationstechnik 

55 

Funktionen der internen Schnittstellen 

## 5.3.3.2 HashResponse 

|Name|**_`HashResponse`_**|**_`HashResponse`_**|
|---|---|---|
|Beschreibung|Als Antwort auf einen<br>`Hash`-Aufruf wird vom Krypto-Modul ein<br>entsprechendes`HashResponse`-Element gemäß Abs. 3.5.4 von[eCard-4]<br>zurückgeliefert.||
|Details|Der Ausgabeparameter`HashResponse` weist folgenden Aufbau auf und kann<br>wie folgt parametrisiert werden.||
||Name|Beschreibung|
||`dss:Result`|Enthält die Statusinformationen und die<br>Fehler zu einer durchgeführten Aktion. Die<br>Struktur dieses Elements und die möglichen<br>Fehlercodes sind in Abs. 4.1.2 von[eCard-1]<br>und in Abs. 3.5.4 von[eCard-4]beschrieben.|
||`Hash`|Enthält den Hashwert, sofern ein solcher<br>berechnet werden konnte.|
|5.4<br>TR-S.5<br>(ArchiSafe-Modul<br>Langzeitspeichersystem)|||



Dieser Abschnitt beschreibt in den folgenden Unterkapiteln, wie die in TR-S.5 (vgl. Abbildung 3 und Abbildung 4) skizzierte Schnittstelle auf Basis der auch dem eCard-API-Framework [TR-03112] zu Grunde liegenden Basistypen aus [OASIS-DSS] umgesetzt werden kann. 

Die in TR-S.5 definierte Schnittstelle umfasst die folgenden Funktionen: 

   - Abfrage beweiswerterhaltend archivierter Daten (Funktion `ArchiveRetrieval` ) 

   - Löschen von Archivdatenobjekten (Funktion `ArchiveDeletion` ) 

   - Abfrage diskreter Datenobjekte (Funktion `ArchiveData` ) 

- (Α5.4−1) Neben der Umsetzung der Funktion „Abfrage beweiswerterhaltend archivierter Daten ( `ArchiveRetrieval` )“ auf Basis der, auch dem eCard-API-Frameworks [TR-03112] zu Grunde liegenden, Basistypen aus [OASIS-DSS] kann diese Funktion auch mittels eines „Download-Requests“ beliebig anders technisch umgesetzt werden, um den Download von Datenobjekten im Rahmen eines LXAIP gemäß [TR-ESOR-F] , Abs. 3.2 technisch performant zu ermöglichen. In diesem Fall müssen die Anforderungen gemäß [TR-ESOR] , Abs. 7 und insbesondere Abs. 7.2 und Abs. 7.4.5 erfüllt werden. 

- 5.4.1 Abfrage beweiswerterhaltend archivierter Daten 

Für die Abfrage beweiswerterhaltend archivierter Daten ist die Anfrage `ArchiveRetrievalRequest` und die Antwort `ArchiveRetrievalResponse` gemäß Abs. 3.3 vorgesehen. 

Bundesamt für Sicherheit in der Informationstechnik 

56 

Funktionen der internen Schnittstellen 

## 5.4.2 Abfrage diskreter Datenobjekte 

Für die Abfrage diskreter Datenobjekte ist die Anfrage `ArchiveDataRequest` und `ArchiveDataResponse` gemäß Abs. 3.6 vorgesehen. 

## 5.4.3 Löschen von Archivdatenobjekten 

Für das Löschen von Archivdatenobjekten ist die Anfrage `ArchiveDeletionRequest` und `ArchiveDeletionResponse` gemäß Abs. 3.5 vorgesehen. 

## 5.5 TR-ESOR-S.6 (ArchiSafe-Modul – ArchiSig-Modul) 

Dieser Abschnitt beschreibt, wie die in Abbildung 3 und Abbildung 4 dargestellte Schnittstelle TR-S.6 auf Basis der auch dem eCard-API-Framework [TR-03112] zu Grunde liegenden Basistypen aus [OASIS-DSS] umgesetzt werden kann. 

Die in Abbildung 3 und Abbildung 4 dargestellte Schnittstelle TR-S.6 umfasst die folgenden Funktionen: 

   - Beweiswerterhaltende Archivierung elektronischer Daten (Funktion `ArchiveSubmission` ) 

   - Ergänzen einer neuen Version eines Archivdatenobjektes (Funktion `ArchiveUpdate` ) 

   - Rückgabe technischer Beweisdaten (Funktion `ArchiveEvidence` ) 

- 5.5.1 Beweiswerterhaltende Archivierung elektronischer Daten 

Für die beweiswerterhaltende Archivierung elektronischer Daten ist die Anfrage `ArchiveSubmissionRequest` und die Antwort `ArchiveSubmissionResponse` gemäß Abs. 3.1 vorgesehen. 

## 5.5.2 Ergänzen einer neuen Version eines Archivdatenobjektes 

Für das Ergänzen einer neuen Version eines Archivdatenobjektes ist die Anfrage `ArchiveUpdateRequest` und die Antwort `ArchiveUpdateResponse` gemäß Abs. 3.2 vorgesehen. 

## 5.5.3 Rückgabe technischer Beweisdaten 

Für die Rückgabe technischer Beweisdaten ist die Anfrage `ArchiveEvidenceRequest` und die Antwort `ArchiveEvidenceResponse` gemäß Abs. 3.4 vorgesehen. 

Bundesamt für Sicherheit in der Informationstechnik 

57 

Upload/Download-Schnittstelle 

## 6. Upload/Download-Schnittstelle 

Die genaue Ausgestaltung der Upload/Download-Schnittstelle wird grundsätzlich dem einzelnen Hersteller überlassen. Die bereits genannten Anforderungen an die Upload/Download-Schnittstelle müssen aber stets eingehalten werden, darüber hinaus werden in den nachfolgenden Kapiteln einige wichtige Aspekte der Schnittstelle präzisiert, die bei der Umsetzung zwingend zu beachten sind. 

## 6.1 Upload-Funktion 

Mit Hilfe der Upload-Funktion können binäre Daten (BIN gem. HINWEIS 5) an die Middleware initial übermittelt werden, die erst im Nachgang mit Hilfe der Funktionen `ArchiveSubmission` (vgl. Kap. 3.1) bzw. `ArchiveUpdate` (vgl. Kap. 3.2) unter Verwendung des korrespondierenden `LXAIP` bzw. `DLXAIP` in die beweiswerterhaltende Bewahrung aufgenommen werden (vgl. auch hierzu [TR-ESOR] , Kap. 7.5.1 und Kap. 7.5.2). Ohne diesen Aufruf der Funktionen `ArchiveSubmission` (vgl. Kap. 3.1) bzw. `ArchiveUpdate` (vgl. Kap. 3.2) erfolgt keine beweiswerterhaltende Bewahrung der zuvor übermittelten Daten und diese binären Daten werden nach Ablauf einer Frist unwiderruflich gelöscht . 

## 6.1.1 Upload-Anfrage 

|Name|**_`Upload-Anfrage`_**|
|---|---|
|Beschreibung|Upload-Anfrage kann binäre Daten in die Middleware übermitteln.|
|Details|(A6.1-1)<br>Esdürfenausschließlich die im HINWEIS 5 als BIN definierten<br>Datenformate angenommen werden.Ausgeschlossensind explizit<br>folgende Formate:<br>•<br>XAIP gem. [TR-ESOR-F], Kap. 3.1<br>•<br>LXAIP gem. [TR-ESOR-F, Kap. 3.2<br>•<br>ASiC-AIP gem. [TR-ESOR-F], Kap. 3.3.<br>(A6.1-2)<br>Die übermittelten Datenobjektemüssenin einer Relation mit<br>einem LXAIP gem. [TR-ESOR-F] Kap. 3.2 stehen.|



## 6.1.2 Upload-Antwort 

|Name|**_`Upload-Antwort`_**|**_`Upload-Antwort`_**|
|---|---|---|
|Beschreibung|Als Antwort auf eine Upload-Anfrage wird von der Upload/Download-<br>Schnittstelle<br>für<br>je<br>ein<br>übermitteltes<br>Datenobjekt<br>eine<br>`asic:DataObjectReference`zurückgeliefert. Im Falle eines Fehlermussder<br>Zustand an die übermittelnde Instanz deutlich signalisiert werden.||
|Details|Folgende Darstellung einer möglichen Upload-Antwort in Form des<br>`UploadResponse`stellt eine Empfehlung für die Umsetzung dar.|Elements|



Bundesamt für Sicherheit in der Informationstechnik 

58 

Upload/Download-Schnittstelle 

|Name|**_`Upload-Antwort`_**|**_`Upload-Antwort`_**|**_`Upload-Antwort`_**|
|---|---|---|---|
||Name|Beschreibung||
||`dss:Result`|Enthält die Statusinformationen und die Fehler<br>zu einer durchgeführten Aktion. Die Struktur<br>dieses Elements und die möglichen Fehlercodes<br>sind in Abs. 4.1.2 von[eCard-1]und in Abs. 3.2.1<br>von[eCard-2]beschrieben.||
||`dss:OptionalOutputs`|Das optionale Element`dss:OptionalOutputs` ist<br>nicht vorhanden.||
||`asic:DataObjectReferenc`<br>`e`|Enthält – sofern kein Fehler aufgetreten ist –<br>mindestens<br>eine<br>Instanz<br>des<br>Elements<br>`asic:DataObjectReference`<br>gem.<br>[TR-<br>ESOR-F], Kap. 3.2.1, die das übermittelte<br>Datenobjekt eindeutig referenziert.||
||Statusinformationen und Fehler beim Aufruf der Funktion`Upload`(vgl.[eCard-<br>1]Abs. 4.1 und Abs. 4.2).|||
||Name|Fehlercode||
||`ResultMajor`|•<br>•|/resultmajor#ok<br>/resultmajor#error|
||`ResultMinor`|•|/resultminor/arl/uploadDataFormatNotSup<br>ported|



## 6.2 Download-Funktion 

Mit Hilfe der Download-Funktion können in einem zuvor bewahrten `LXAIP` bzw. `DLXAIP` referenzierten Datenobjekte ausgelesen werden. 

Bundesamt für Sicherheit in der Informationstechnik 

59 

Upload/Download-Schnittstelle 

## 6.2.1 Download-Anfrage 

|Name|**`Download-Anfrage`**|**`Download-Anfrage`**|
|---|---|---|
|Beschreibung|Mit Hilfe der Download-Anfrage wird ein (oder mehrere) zuvor im<br>Langzeitspeicher und in einem LXAIP referenziertes/-en Datenobjekt(e)<br>ausgelesen werden.||
|Details|Folgende Darstellung einer möglichen Download-Anfrage in Form des Elements<br>`DownloadRequest`stellt eine Empfehlung für die Umsetzung dar.||
||Name|Beschreibung|
||`dss:OptionalInputs`|Das optionale Element`dss:OptionalInputs` ist<br>nicht vorhanden.|
||`asic:DataObjectReferenc`<br>`e`|Enthält mindestens eine Instanz des Elements<br>`asic:DataObjectReference`<br>gem.<br>[TR-<br>ESOR-F], Kap. 3.2.1, die das zuvor übermittelte<br>und<br>im<br>zugehörigen<br>`LXAIP`<br>referenzierte<br>Datenobjekt eindeutig beschreibt.|



## 6.2.2 Download-Antwort 

|Name|**_`Download-Antwort`_**|
|---|---|
|Beschreibung|Als Antwort auf eine Download-Anfrage wird von der Upload/Download-<br>Schnittstelle<br>zu<br>jedem<br>mit<br>einer<br>Instanz<br>des<br>Elements<br>`asic:DataObjectReference`<br>angefragten<br>Datenobjekt<br>dieses<br>auch<br>ausgeliefert.<br>Wenn die Anfrage nicht erfolgreich ausgeführt werden kann, muss eine<br>Fehlermeldung zurückgegeben werden|
|Details|Folgende Darstellung einer möglichen Download-Antwort in Form des<br>Elements`DownloadResponse`stellt eine Empfehlung für die Umsetzungim<br>Falle eines Fehlersdar.|



Bundesamt für Sicherheit in der Informationstechnik 

60 

Upload/Download-Schnittstelle 

|Name|**_`Download-Antwort`_**|**_`Download-Antwort`_**|**_`Download-Antwort`_**|
|---|---|---|---|
||Name|Beschreibung||
||`dss:Result`|Enthält die Statusinformationen und die Fehler<br>zu einer durchgeführten Aktion. Die Struktur<br>dieses Elements und die möglichen Fehlercodes<br>sind in Abs. 4.1.2 von[eCard-1]und in Abs. 3.2.1<br>von[eCard-2]beschrieben.||
||`dss:OptionalOutputs`|Das optionale Element`dss:OptionalOutputs` ist<br>nicht vorhanden.||
||Statusinformationen und Fehler beim Aufruf der Funktion`ArchiveTrace`(vgl.<br>[eCard-1]Abs. 4.1 und Abs. 4.2).|||
||Name|Fehlercode||
||`ResultMajor`|•<br>•|/resultmajor#ok<br>/resultmajor#error|
||`ResultMinor`|•|/resultminor/arl/unknownDataObjectRefere<br>nce|



Bundesamt für Sicherheit in der Informationstechnik 

61 

Fehlercodes 

## 7. Fehlercodes 

Die vorliegende Spezifikation nutzt die folgenden generellen Fehlercodes aus [eCard-1] : 

- .../resultmajor#ok 

- .../resultmajor#error 

- .../resultmajor#warning 

- .../resultminor/al/common#noPermission 

- .../resultminor/al/common#internalError 

- .../resultminor/al/common#parameterError 

Darüber hinaus werden zusätzlich die folgenden Fehlercodes definiert: 

|Fehlercode|Beschreibung|
|---|---|
|.../resultminor/arl/DXAIP_NOK|Die<br>Syntax<br>des<br>beim<br>`ArchiveUpdateRequest`<br>übergebenen Delta-XAIP-Elements ist nicht korrekt.|
|.../resultminor/arl/DXAIP_NOK_AOID|Die AOID in dem beim`ArchiveUpdateRequest`<br>übergebenen Delta-XAIP ist nicht bekannt.|
|.../resultminor/arl/DXAIP_NOK_EXPIRED|Das beim`ArchiveUpdateRequest`übergebene Delta-<br>XAIP-Element kann nicht abgelegt werden, da die<br>Aufbewahrungsfrist abgelaufen ist.|
|.../resultminor/arl/DXAIP_NOK_SUBMTI<br>ME|Die beim`ArchiveUpdateRequest`im übergebenen<br>Delta-XAIP-Element angegebene`submissionTime`ist<br>nicht korrekt, da sie in der Zukunft liegt.|
|.../resultminor/arl/DXAIP_NOK_SIG|Das beim`ArchiveUpdateRequest`übergebene Delta-<br>XAIP-Element enthält zumindest eine ungültige digitale<br>Signatur.|
|.../resultminor/arl/DXAIP_NOK_ER|Das beim`ArchiveUpdateRequest`übergebene Delta-<br>XAIP-Element enthält zumindest einen ungültigen<br>Evidence Record.|
|.../resultminor/arl/DXAIP_NOK_ID|Die beim ArchiveUpdateRequest in einem `placeHolder`-<br>Element übergebene`XML-ID`ist im bereits abgelegten<br>XAIP-Element nicht vorhanden.|
|.../resultminor/arl/DXAIP_NOK_Version|Die beim ArchiveUpdateRequest im<br>`prevVersion`-<br>Element übergebene Version ist nicht die aktuellste<br>Version.|
|.../resultminor/arl/existingAOID|Die<br>im<br>Rahmen<br>des<br>`ArchiveSubmissionRequest`<br>übergebene`AOID`existiert bereits.|
|.../resultminor/arl/existingPackage<br>InfoWarning|Bei der `ArchiveUpdateRequest`-Funktion wird ein Delta-<br>XAIP-Element übergeben, das ein`packageInfo`-Element<br>enthält. Da im vorher existierenden XAIP bereits das<br>`packageInfo`-Element belegt war, wird das übergebene<br>`packageInfo`-Element ignoriert und eine entsprechende<br>Warnung zurückgeliefert.|
|.../resultminor/arl/lowSpaceWarning|Diese Warnung gibt an, dass der verfügbare Speicherplatz<br>einen kritischen Wert unterschritten hat.|



Bundesamt für Sicherheit in der Informationstechnik 

62 

Fehlercodes 

|Fehlercode|Beschreibung|
|---|---|
|.../resultminor/arl/missingReasonOf<br>Deletion|Da<br>beim<br>`ArchiveDeletionRequest`<br>kein<br>`ReasonOfDeletion`-Element übergeben wurde, muss<br>der Löschvorgang abgewiesen werden.|
|.../resultminor/arl/noSpaceError|Diese Fehlermeldung gibt an, dass kein Speicherplatz<br>verfügbar war und deshalb das Archivdatenobjekt nicht<br>abgelegt werden konnte.|
|.../resultminor/arl/notSupported|Diese Fehlermeldung gibt an, dass eine angeforderte<br>Funktion, ein angefordertes Format oder ein übergebener<br>optionaler Eingabeparameter nicht unterstützt wird.|
|.../resultminor/arl/requestOnlyPartly<br>SuccessfulWarning|Diese Warnung gibt an, dass nicht alle angeforderten<br>Daten zurückgeliefert werden konnten.|
|.../resultminor/arl/unknownArchiveData<br>Type|Es wird ein binäres Datenobjekt mit einem nicht<br>unterstützten Datenformat übergeben.|
|.../resultminor/arl/unknownLocation|Die<br>im<br>`ArchiveDataRequest`<br>angegebene<br>`DataLocation` ist nicht vorhanden bzw. fehlerhaft.|
|.../resultminor/arl/unknownAOID|Die übergebene `AOID` existiert nicht.|
|.../resultminor/arl/unknownVersionID|Die übergebene `VersionID`ist im entsprechenden XAIP<br>nicht bekannt.|
|.../resultminor/arl/XAIP_NOK|Die Syntax des übergebenen AIP-Containers (d. h. XAIP,<br>LXAIP, ASiC-AIP) ist nicht korrekt.|
|.../resultminor/arl/XAIP_NOK_ER|Der übergebene AIP-Container (d. h. XAIP, LXAIP, ASiC-<br>AIP) enthält zumindest einen ungültigen Evidence<br>Record.|
|.../resultminor/arl/XAIP_NOK_EXPIRED|Der übergebene AIP-Container (d. h. XAIP, LXAIP, ASiC-<br>AIP)<br>kann<br>nicht<br>abgelegt<br>werden,<br>da<br>die<br>Aufbewahrungsfrist abgelaufen ist.|
|.../resultminor/arl/XAIP_NOK_SIG|Der übergebene AIP-Container (d. h. XAIP, LXAIP, ASiC-<br>AIP) enthält zumindest eine ungültige Signatur.|
|.../resultminor/arl/XAIP_NOK_SUBMTIM<br>E|Die im übergebenen AIP-Container (d. h. XAIP, LXAIP,<br>ASiC-AIP) angegebene `submissionTime` ist nicht<br>korrekt, da sie in der Zukunft liegt.|
|.../resultminor/arl/noDataAccessWarning|Der Zugriff auf die in einem übergebenen LXAIP<br>referenzierten Daten ist nicht möglich.|
|.../resultminor/arl/unknownPOFormat|Der angeforderte`POFormat`- Typ ist nicht bekannt.|
|.../resultminor/arl/uploadDataFormatNot<br>Supported|Das Datenformat ist für den Upload nicht zugelassen.|
|.../resultminor/arl/unknownDataObjectR<br>eference|Das<br>durch<br>eine<br>Instanz<br>von<br>`asic:DataObjectReference`<br>beschriebene<br>Datenobjekt ist nicht bekannt.|
|.../resultminor/sal#invalidSignature|Die übergebene  Signatur ist falsch.|



Bundesamt für Sicherheit in der Informationstechnik 

63 

Fehlercodes 

## Tabelle 4: Zusätzliche Fehlercodes. 

Bundesamt für Sicherheit in der Informationstechnik 

64 

Spezifikation einer Webservice-basierten Schnittstelle 

## 8. Spezifikation einer Schnittstelle 

## Webservice-basierten 

Die Spezifikation der Webservice-basierten Schnittstelle besteht aus zwei Bestandteilen: Zunächst werden die Aufruf- und Rückgabeparameter als XML-Schema [XSD] spezifiziert (vgl. Abs. 7.1). Darauf aufbauend wird in einem zweiten Schritt eine Webservice-Spezifikation gemäß [WSDL] entwickelt. 

Abschnitt 7.2 enthält die Webservice-Spezifikation der Schnittstelle TR-S.4 (vgl. Abs. 3). Die internen Schnittstellen der TR-ESOR-Middleware können bei Bedarf leicht daraus abgeleitet werden, indem nur die benötigte Teilmenge der Funktionen genutzt wird. 

   - (A8.0-1) Die Unterstützung des optimierten Nachrichtenübertragungsmechanismus „SOAP Message Transmission Optimization Mechanism (MTOM)“[22] kann durch den Import des geringfügig angepassten XAIP-Schema ( `tr-esor-xaip-v1.3.xsd` ) erfolgen. 

- 8.1 Spezifikation der Aufruf- und Rückgabeparameter als XMLSchema 

```
<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://www.w3.org/2001/XMLSchema"
xmlns:tr="http://www.bsi.bund.de/tr-esor/api/1.3"
xmlns:xaip="http://www.bsi.bund.de/tr-esor/xaip"
xmlns:ers="urn:ietf:params:xml:ns:ers"
xmlns:ec="http://www.bsi.bund.de/ecard/api/1.1"
xmlns:dss="urn:oasis:names:tc:dss:1.0:core:schema"
xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
xmlns:xmime="http://www.w3.org/2005/05/xmlmime"
xmlns:pres="http://uri.etsi.org/19512/v1.1.2#"
xmlns:asic="http://uri.etsi.org/02918/v1.2.1#"
targetNamespace="http://www.bsi.bund.de/tr-esor/api/1.3"
elementFormDefault="qualified" attributeFormDefault="unqualified"
version="1.3.0">
<!-- ======================================= -->
 <!-- Version 1.3.0 vom 14.03.2022            -->
 <!-- ======================================= -->
<import namespace="http://www.bsi.bund.de/tr-esor/xaip"
schemaLocation="tr-esor-xaip-v1.3.xsd"/>
 <import namespace="urn:oasis:names:tc:dss:1.0:core:schema"
schemaLocation="./deps/oasis-dss-core-schema-v1.0-os.xsd"/>
 <import namespace="urn:ietf:params:xml:ns:ers"
schemaLocation="./deps/xml-ers-rfc6283.xsd"/>
 <import namespace="http://www.bsi.bund.de/ecard/api/1.1"
schemaLocation="./deps/eCard.xsd"/>
 <import namespace="urn:oasis:names:tc:SAML:2.0:assertion"
schemaLocation="./deps/saml-schema-assertion-2.0.xsd"/>
 <import namespace="http://www.w3.org/2005/05/xmlmime"
schemaLocation="./deps/xmlmime.xsd"/>
 <import namespace="http://uri.etsi.org/19512/v1.1.2#"
schemaLocation="19512-Preservation-API_V.1.1.2.xsd"/>
 <import namespace="http://uri.etsi.org/02918/v1.2.1#"
schemaLocation="./deps/en_31916201v010101.xsd"/>
<!-- =================================== -->
 <!--     Uebergreifende Definitionen     -->
 <!-- =================================== -->
<complexType name="RequestType">
  <complexContent>
   <restriction base="dss:RequestBaseType">
    <sequence>
     <element ref="dss:OptionalInputs" minOccurs="0"/>
    </sequence>
   </restriction>
```

> 22Siehe https://www.w3.org/TR/soap12-mtom/ . 

Bundesamt für Sicherheit in der Informationstechnik 

65 

Spezifikation einer Webservice-basierten Schnittstelle 

```
  </complexContent>
```

```
 </complexType>
```

```
 <complexType name="ResponseType">
```

```
  <complexContent>
```

```
   <restriction base="dss:ResponseBaseType">
```

```
    <sequence>
```

```
     <element ref="dss:Result"/>
```

```
     <element ref="dss:OptionalOutputs" minOccurs="0"/>
```

```
    </sequence>
```

```
   </restriction>
```

```
  </complexContent>
```

```
 </complexType>
```

```
 <element name="AOID" type="string"/>
```

```
 <element name="VerifyUnderSignaturePolicy" type="anyURI"/>
 <element name="XPathFilter" type="string"/>
```

```
<!-- ================================ -->
```

```
 <!--    RetrieveInfo                  -->
```

```
 <!-- ================================ -->
```

```
<element name="RetrieveInfoRequest">
```

```
  <complexType>
```

```
   <complexContent>
```

```
    <extension base="tr:RequestType">
```

```
     <sequence>
```

```
      <element name="ProfileIdentifier" type="anyURI" minOccurs="0"/>
```

```
      <element name="Status" type="pres:StatusType" minOccurs="0"/>
```

```
     </sequence>
```

```
    </extension>
```

```
   </complexContent>
```

```
  </complexType>
```

```
 </element>
```

```
 <element name="RetrieveInfoResponse">
```

```
  <complexType>
```

```
   <complexContent>
```

```
    <extension base="tr:ResponseType">
```

```
     <sequence>
```

```
      <element ref="pres:Profile" minOccurs="0" maxOccurs="unbounded"/>
```

```
     </sequence>
```

```
    </extension>
```

```
   </complexContent>
```

```
  </complexType>
```

```
 </element>
```

```
<!-- ================================ -->
```

```
 <!--    ArchiveSubmission             -->
```

```
 <!-- ================================ -->
```

```
<complexType name="ArchiveDataType" xmime:expectedContentTypes="*/*">
```

```
  <simpleContent>
```

```
   <extension base="base64Binary">
```

```
    <attribute name="Type" type="anyURI" use="required"/>
```

```
    <attribute name="archiveDataID" type="ID" use="required"/>
```

```
    <attribute name="MimeType" type="string" use="optional"/>
```

```
    <attribute name="relatedObjects" type="IDREFS" use="optional"/>
```

```
   </extension>
```

```
  </simpleContent>
```

```
 </complexType>
```

```
 <element name="ImportEvidence" type="tr:ImportEvidenceType"/>
```

```
 <complexType name="ImportEvidenceType">
```

```
  <choice>
```

```
   <element ref="xaip:evidenceRecord" maxOccurs="unbounded"/>
   <element name="CredentialID" type="string" maxOccurs="unbounded"/>
```

```
  </choice>
```

```
 </complexType>
```

```
 <element name="ArchiveSubmissionRequest">
```

```
  <complexType>
```

```
   <complexContent>
```

```
    <extension base="tr:RequestType">
```

```
     <choice>
```

```
      <element ref="xaip:XAIP"/>
```

```
      <element name="ArchiveData" type="tr:ArchiveDataType" maxOccurs="unbounded"/>
     </choice>
    </extension>
   </complexContent>
```

Bundesamt für Sicherheit in der Informationstechnik 

66 

Spezifikation einer Webservice-basierten Schnittstelle 

```
  </complexType>
 </element>
 <element name="ArchiveSubmissionResponse">
  <complexType>
   <complexContent>
    <extension base="tr:ResponseType">
     <sequence>
      <element name="AOID" type="string" minOccurs="0"/>
     </sequence>
    </extension>
   </complexContent>
  </complexType>
 </element>
<!-- ========================== -->
 <!--    ArchiveUpdate           -->
 <!-- ========================== -->
<element name="ArchiveUpdateRequest">
  <complexType>
   <complexContent>
    <extension base="tr:RequestType">
     <sequence>
      <element ref="xaip:DXAIP"/>
     </sequence>
    </extension>
   </complexContent>
  </complexType>
 </element>
 <element name="ArchiveUpdateResponse">
  <complexType>
   <complexContent>
    <extension base="tr:ResponseType">
     <sequence>
      <element name="VersionID" type="string" minOccurs="0"/>
     </sequence>
```

```
    </extension>
```

```
   </complexContent>
```

```
  </complexType>
```

```
 </element>
```

```
<!-- ================================ -->
```

```
 <!--    ArchiveRetrieval              -->
```

```
 <!-- ================================ -->
```

```
<element name="ArchiveRetrievalRequest">
```

```
  <complexType>
```

```
   <complexContent>
```

```
    <extension base="tr:RequestType">
```

```
     <sequence>
      <element name="AOID" type="string"/>
```

```
      <element name="VersionID" type="string" minOccurs="0" maxOccurs="unbounded"/>
     </sequence>
```

```
    </extension>
```

```
   </complexContent>
```

```
  </complexType>
```

```
 </element>
```

```
 <element name="IncludeERS" type="anyURI"/>
 <element name="ArchiveRetrievalResponse">
```

```
  <complexType>
```

```
   <complexContent>
```

```
    <extension base="tr:ResponseType">
```

```
     <sequence>
```

```
      <element ref="xaip:XAIP" minOccurs="0"/>
```

```
     </sequence>
```

```
    </extension>
```

```
   </complexContent>
```

```
  </complexType>
```

```
 </element>
```

```
<!-- ================================ -->
```

```
 <!--    ArchiveEvidence               -->
```

```
 <!-- ================================ -->
```

```
<element name="ArchiveEvidenceRequest">
  <complexType>
```

```
   <complexContent>
```

Bundesamt für Sicherheit in der Informationstechnik 

67 

Spezifikation einer Webservice-basierten Schnittstelle 

```
    <extension base="tr:RequestType">
```

```
     <sequence>
      <element name="AOID" type="string"/>
```

```
      <element name="VersionID" type="string" minOccurs="0" maxOccurs="unbounded"/>
     </sequence>
    </extension>
   </complexContent>
  </complexType>
 </element>
 <element name="ERSFormat" type="anyURI"/>
 <element name="ArchiveEvidenceResponse">
  <complexType>
   <complexContent>
    <extension base="tr:ResponseType">
     <sequence>
      <element ref="xaip:evidenceRecord" minOccurs="0" maxOccurs="unbounded"/>
     </sequence>
    </extension>
   </complexContent>
  </complexType>
 </element>
```

```
<!-- ================================ -->
```

```
 <!--    ArchiveDeletion               -->
 <!-- ================================ -->
<element name="ArchiveDeletionRequest">
```

```
  <complexType>
```

```
   <complexContent>
    <extension base="tr:RequestType">
     <sequence>
      <element name="AOID" type="string"/>
     </sequence>
    </extension>
```

```
   </complexContent>
```

```
  </complexType>
```

```
 </element>
 <element name="ReasonOfDeletion">
```

```
  <complexType>
   <sequence>
    <element name="RequestorName" type="saml:NameIDType"/>
    <element name="RequestInfo" type="string"/>
   </sequence>
  </complexType>
 </element>
 <element name="ArchiveDeletionResponse" type="tr:ResponseType"/>
<!-- ========================== -->
 <!--    ArchiveData             -->
 <!-- ========================== -->
<element name="ArchiveDataRequest">
  <complexType>
   <complexContent>
    <extension base="tr:RequestType">
```

```
     <sequence>
      <element name="AOID" type="string"/>
      <element ref="tr:DataLocation" maxOccurs="unbounded"/>
     </sequence>
```

```
    </extension>
```

```
   </complexContent>
```

```
  </complexType>
```

```
 </element>
```

```
 <element name="DataLocation">
  <complexType>
   <complexContent>
    <extension base="anyType">
     <attribute name="Type" type="anyURI"/>
    </extension>
```

```
   </complexContent>
```

```
  </complexType>
```

```
 </element>
 <element name="ArchiveDataResponse">
  <complexType>
   <complexContent>
```

Bundesamt für Sicherheit in der Informationstechnik 

68 

Spezifikation einer Webservice-basierten Schnittstelle 

```
    <extension base="tr:ResponseType">
     <sequence>
      <element name="XAIPData" maxOccurs="unbounded">
       <complexType>
        <sequence>
         <element ref="dss:Result"/>
         <element ref="tr:DataLocation"/>
         <element name="Value" type="anyType" minOccurs="0"/>
        </sequence>
       </complexType>
      </element>
     </sequence>
    </extension>
   </complexContent>
  </complexType>
 </element>
<!-- ========================== -->
 <!--    ArchiveTrace            -->
 <!-- ========================== -->
<element name="ArchiveTraceRequest">
  <complexType>
   <complexContent>
    <extension base="tr:RequestType">
     <sequence>
      <element ref="tr:AOID"/>
     </sequence>
    </extension>
   </complexContent>
  </complexType>
 </element>
 <element name="ArchiveTraceResponse">
  <complexType>
   <complexContent>
    <extension base="tr:ResponseType">
```

```
     <sequence>
      <element ref="pres:Trace"/>
```

```
     </sequence>
```

```
    </extension>
```

```
   </complexContent>
```

```
  </complexType>
```

```
 </element>
```

```
<!-- ========================== -->
```

```
 <!--    Upload                  -->
```

```
 <!-- ========================== -->
```

```
<element name="UploadResponse">
```

```
  <complexType>
```

```
   <complexContent>
```

```
    <extension base="tr:ResponseType">
```

```
     <sequence>
      <element ref="asic:DataObjectReference" minOccurs="0" maxOccurs="unbounded"/>
     </sequence>
    </extension>
```

```
   </complexContent>
```

```
  </complexType>
```

```
 </element>
```

```
<!-- ========================== -->
```

```
 <!--    Download                -->
```

```
 <!-- ========================== -->
```

```
<element name="DownloadRequest">
```

```
  <complexType>
```

```
   <complexContent>
```

```
    <extension base="tr:RequestType">
```

```
     <sequence>
```

```
      <element ref="asic:DataObjectReference" maxOccurs="unbounded"/>
     </sequence>
```

```
    </extension>
```

```
   </complexContent>
```

```
  </complexType>
 </element>
 <element name="DownloadResponse">
  <complexType>
```

Bundesamt für Sicherheit in der Informationstechnik 

69 

Spezifikation einer Webservice-basierten Schnittstelle 

```
   <complexContent>
```

```
    <extension base="tr:ResponseType"/>
```

```
   </complexContent>
```

```
  </complexType>
 </element>
</schema>
```

## 8.2 WSDL-Spezifikation der Schnittstelle TR-S.4 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_3/BSI_TR_03125_Anlage_E_V1_3.pdf-0070-06.png)


**----- Start of picture text -----**<br>
<?xml version="1.0" encoding="UTF-8"?><br><wsdl:definitions xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"<br>xmlns:xsd="http://www.w3.org/2001/XMLSchema"<br>xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"<br>xmlns:dss="urn:oasis:names:tc:dss:1.0:core:schema"<br>xmlns:tr="http://www.bsi.bund.de/tr-esor/api/1.3"<br>targetNamespace="http://www.bsi.bund.de/tr-esor/api/1.3"><br><!--============================================================--><br>  <!-- Version 1.3.0 of 14.03.2022                                --><br>  <!--============================================================--><br>  <!-- ======================== --><br>  <!-- Definition of types      --><br>  <!-- (only include XSDs)      --><br>  <!-- ======================== --><br><wsdl:types><br>    <xsd:schema targetNamespace="http://www.bsi.bund.de/tr-esor/api/1.3"<br>xmlns:xsd="http://www.w3.org/2001/XMLSchema"<br>xmlns:xaip="http://www.bsi.bund.de/tr-esor/xaip"<br>xmlns:dss="urn:oasis:names:tc:dss:1.0:core:schema"<br>elementFormDefault="qualified"><br>      <xsd:include schemaLocation="tr-esor-interfaces-v1.3.xsd"/><br>    </xsd:schema><br>  </wsdl:types><br><!-- ======================== --><br>  <!-- Definition of messages   --><br>  <!-- ======================== --><br>  <!-- RetrieveInfo --><br><wsdl:message name="RetrieveInfoRequest"><br>    <wsdl:part name="parameters" element="tr:RetrieveInfoRequest"/><br>  </wsdl:message><br>  <wsdl:message name="RetrieveInfoResponse"><br>    <wsdl:part name="parameters" element="tr:RetrieveInfoResponse"/><br>  </wsdl:message><br><!-- Archivesubmission --><br><wsdl:message name="ArchiveSubmissionRequest"><br>    <wsdl:part name="parameters" element="tr:ArchiveSubmissionRequest"/><br>  </wsdl:message><br>  <wsdl:message name="ArchiveSubmissionResponse"><br>    <wsdl:part name="parameters" element="tr:ArchiveSubmissionResponse"/><br>  </wsdl:message><br><!-- ArchiveUpdate --><br><wsdl:message name="ArchiveUpdateRequest"><br>    <wsdl:part name="parameters" element="tr:ArchiveUpdateRequest"/><br>  </wsdl:message><br>  <wsdl:message name="ArchiveUpdateResponse"><br>    <wsdl:part name="parameters" element="tr:ArchiveUpdateResponse"/><br>  </wsdl:message><br><!-- ArchiveRetrieval --><br><wsdl:message name="ArchiveRetrievalRequest"><br>    <wsdl:part name="parameters" element="tr:ArchiveRetrievalRequest"/><br>  </wsdl:message><br>  <wsdl:message name="ArchiveRetrievalResponse"><br>    <wsdl:part name="parameters" element="tr:ArchiveRetrievalResponse"/><br>  </wsdl:message><br><!-- ArchiveEvidence --><br><wsdl:message name="ArchiveEvidenceRequest"><br>    <wsdl:part name="parameters" element="tr:ArchiveEvidenceRequest"/><br>  </wsdl:message><br>  <wsdl:message name="ArchiveEvidenceResponse"><br>    <wsdl:part name="parameters" element="tr:ArchiveEvidenceResponse"/><br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

70 

Spezifikation einer Webservice-basierten Schnittstelle 

```
  </wsdl:message>
<!-- ArchiveDeletion -->
```

```
<wsdl:message name="ArchiveDeletionRequest">
    <wsdl:part name="parameters" element="tr:ArchiveDeletionRequest"/>
  </wsdl:message>
  <wsdl:message name="ArchiveDeletionResponse">
    <wsdl:part name="parameters" element="tr:ArchiveDeletionResponse"/>
  </wsdl:message>
<!-- ArchiveData -->
<wsdl:message name="ArchiveDataRequest">
    <wsdl:part name="parameters" element="tr:ArchiveDataRequest"/>
  </wsdl:message>
```

```
  <wsdl:message name="ArchiveDataResponse">
    <wsdl:part name="parameters" element="tr:ArchiveDataResponse"/>
  </wsdl:message>
<!-- Verify -->
<wsdl:message name="VerifyRequest">
    <wsdl:part name="parameters" element="dss:VerifyRequest"/>
  </wsdl:message>
```

```
  <wsdl:message name="VerifyResponse">
    <wsdl:part name="parameters" element="dss:VerifyResponse"/>
  </wsdl:message>
<!-- ArchiveTrace -->
```

```
<wsdl:message name="ArchiveTraceRequest">
    <wsdl:part name="parameters" element="tr:ArchiveTraceRequest"/>
  </wsdl:message>
  <wsdl:message name="ArchiveTraceResponse">
    <wsdl:part name="parameters" element="tr:ArchiveTraceResponse"/>
  </wsdl:message>
```

```
<!-- ====================== -->
```

```
  <!-- Definition of portType -->
  <!-- ====================== -->
```

```
<wsdl:portType name="S4">
```

```
    <wsdl:operation name="RetrieveInfo">
      <wsdl:input message="tr:RetrieveInfoRequest"/>
      <wsdl:output message="tr:RetrieveInfoResponse"/>
    </wsdl:operation>
```

```
    <wsdl:operation name="ArchiveSubmission">
      <wsdl:input message="tr:ArchiveSubmissionRequest"/>
      <wsdl:output message="tr:ArchiveSubmissionResponse"/>
    </wsdl:operation>
```

```
    <wsdl:operation name="ArchiveUpdate">
```

```
      <wsdl:input message="tr:ArchiveUpdateRequest"/>
```

```
      <wsdl:output message="tr:ArchiveUpdateResponse"/>
    </wsdl:operation>
```

```
    <wsdl:operation name="ArchiveRetrieval">
      <wsdl:input message="tr:ArchiveRetrievalRequest"/>
      <wsdl:output message="tr:ArchiveRetrievalResponse"/>
    </wsdl:operation>
    <wsdl:operation name="ArchiveEvidence">
      <wsdl:input message="tr:ArchiveEvidenceRequest"/>
      <wsdl:output message="tr:ArchiveEvidenceResponse"/>
    </wsdl:operation>
```

```
    <wsdl:operation name="ArchiveDeletion">
      <wsdl:input message="tr:ArchiveDeletionRequest"/>
      <wsdl:output message="tr:ArchiveDeletionResponse"/>
    </wsdl:operation>
```

```
    <wsdl:operation name="ArchiveData">
      <wsdl:input message="tr:ArchiveDataRequest"/>
      <wsdl:output message="tr:ArchiveDataResponse"/>
    </wsdl:operation>
    <wsdl:operation name="Verify">
      <wsdl:input message="tr:VerifyRequest"/>
      <wsdl:output message="tr:VerifyResponse"/>
    </wsdl:operation>
    <wsdl:operation name="ArchiveTrace">
      <wsdl:input message="tr:ArchiveTraceRequest"/>
      <wsdl:output message="tr:ArchiveTraceResponse"/>
    </wsdl:operation>
  </wsdl:portType>
<!-- ===================== -->
```

Bundesamt für Sicherheit in der Informationstechnik 

71 

Spezifikation einer Webservice-basierten Schnittstelle 

```
  <!-- Definition of Binding -->
  <!-- ===================== -->
```

```
<wsdl:binding name="S4" type="tr:S4">
```

```
    <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>
    <wsdl:operation name="RetrieveInfo">
      <soap:operation soapAction="http://www.bsi.bund.de/tr-esor/RetrieveInfo"/>
      <wsdl:input>
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal"/>
      </wsdl:output>
```

```
    </wsdl:operation>
```

```
    <wsdl:operation name="ArchiveSubmission">
```

```
      <soap:operation soapAction="http://www.bsi.bund.de/tr-esor/ArchiveSubmission"/>
      <wsdl:input>
```

```
        <soap:body use="literal"/>
```

```
      </wsdl:input>
```

```
      <wsdl:output>
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
```

```
    <wsdl:operation name="ArchiveUpdate">
```

```
      <soap:operation soapAction="http://www.bsi.bund.de/tr-esor/ArchiveUpdate"/>
      <wsdl:input>
```

```
        <soap:body use="literal"/>
```

```
      </wsdl:input>
```

```
      <wsdl:output>
```

```
        <soap:body use="literal"/>
```

```
      </wsdl:output>
```

```
    </wsdl:operation>
```

```
    <wsdl:operation name="ArchiveRetrieval">
```

```
      <soap:operation soapAction="http://www.bsi.bund.de/tr-esor/ArchiveRetrieval"/>
      <wsdl:input>
```

```
        <soap:body use="literal"/>
```

```
      </wsdl:input>
```

```
      <wsdl:output>
```

```
        <soap:body use="literal"/>
```

```
      </wsdl:output>
```

```
    </wsdl:operation>
```

```
    <wsdl:operation name="ArchiveEvidence">
```

```
      <soap:operation soapAction="http://www.bsi.bund.de/tr-esor/ArchiveEvidence"/>
      <wsdl:input>
```

```
        <soap:body use="literal"/>
```

```
      </wsdl:input>
```

```
      <wsdl:output>
```

```
        <soap:body use="literal"/>
```

```
      </wsdl:output>
```

```
    </wsdl:operation>
```

```
    <wsdl:operation name="ArchiveDeletion">
```

```
      <soap:operation soapAction="http://www.bsi.bund.de/tr-esor/ArchiveDeletion"/>
```

```
      <wsdl:input>
```

```
        <soap:body use="literal"/>
```

```
      </wsdl:input>
```

```
      <wsdl:output>
```

```
        <soap:body use="literal"/>
```

```
      </wsdl:output>
```

```
    </wsdl:operation>
```

```
    <wsdl:operation name="ArchiveData">
```

```
      <soap:operation soapAction="http://www.bsi.bund.de/tr-esor/ArchiveData"/>
      <wsdl:input>
```

```
        <soap:body use="literal"/>
```

```
      </wsdl:input>
```

```
      <wsdl:output>
```

```
        <soap:body use="literal"/>
```

```
      </wsdl:output>
    </wsdl:operation>
```

```
    <wsdl:operation name="Verify">
```

```
      <soap:operation soapAction="http://www.bsi.bund.de/tr-esor/Verify"/>
      <wsdl:input>
```

```
        <soap:body use="literal"/>
```

Bundesamt für Sicherheit in der Informationstechnik 

72 

Spezifikation einer Webservice-basierten Schnittstelle 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_3/BSI_TR_03125_Anlage_E_V1_3.pdf-0073-01.png)


**----- Start of picture text -----**<br>
      </wsdl:input><br>      <wsdl:output><br>        <soap:body use="literal"/><br>      </wsdl:output><br>    </wsdl:operation><br>    <wsdl:operation name="ArchiveTrace"><br>      <soap:operation soapAction="http://www.bsi.bund.de/tr-esor/ArchiveTrace"/><br>      <wsdl:input><br>        <soap:body use="literal"/><br>      </wsdl:input><br>      <wsdl:output><br>        <soap:body use="literal"/><br>      </wsdl:output><br>    </wsdl:operation><br>  </wsdl:binding><br><!-- ===================== --><br>  <!-- Definition of Service --><br>  <!-- ===================== --><br><wsdl:service name="S4"><br>    <wsdl:port name="S4" binding="tr:S4"><br>      <soap:address location="http://127.0.0.1:18080"/><br>    </wsdl:port><br>  </wsdl:service><br></wsdl:definitions><br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

73 


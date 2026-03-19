
![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0001-00.png)


BSI Technische Richtlinie 03125 Beweiswerterhaltung kryptographisch signierter Dokumente 

## **Anlage TR-ESOR-E:** 

## **Konkretisierung der Schnittstellen auf Basis des eCard-APIFrameworks** 

|Bezeichnung|Konkretisierung der Schnittstellen auf Basis des eCard-API-|
|---|---|
||Frameworks|
|Kürzel|BSI TR-ESOR-E|
|Version|1.2.2 (auf Basis der eIDAS-Verordnung und der ETSI Preservation Standards)|
|Datum|02.05.2019|



Beweiswerterhaltung kryptographisch signierter Dokumente (TR-ESOR) 

BSI TR 03125 

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn Tel.: +49 228 99 9582-0 E-Mail:  tresor@bsi.bund.de Internet: https://www.bsi.bund.de © Bundesamt für Sicherheit in der Informationstechnik 2019 

Bundesamt für Sicherheit in der Informationstechnik 

Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

## **Inhaltsverzeichnis** 

1.Einführung...........................................................................................................................................5 2.Überblick.............................................................................................................................................7 3.Funktionen der ArchiSafe-Schnittstelle (TR-ESOR-S.4).....................................................................9 3.1ArchiveSubmissionRequest und ArchiveSubmissionResponse.........................................................9 3.1.1ArchiveSubmissionRequest..........................................................................................................10 3.1.2ArchiveSubmissionResponse........................................................................................................13 3.2ArchiveUpdateRequest und ArchiveUpdateResponse.....................................................................15 3.2.1ArchiveUpdateRequest.................................................................................................................15 3.2.2ArchiveUpdateResponse...............................................................................................................16 3.3ArchiveRetrievalRequest und ArchiveRetrievalResponse...............................................................18 3.3.1ArchiveRetrievalRequest..............................................................................................................18 3.3.2ArchiveRetrievalResponse............................................................................................................20 3.4ArchiveEvidenceRequest und ArchiveEvidenceResponse...............................................................22 3.4.1ArchiveEvidenceRequest..............................................................................................................22 3.4.2ArchiveEvidenceResponse...........................................................................................................24 3.5ArchiveDeletionRequest und ArchiveDeletionResponse.................................................................26 3.5.1ArchiveDeletionRequest...............................................................................................................26 3.5.2ArchiveDeletionResponse............................................................................................................27 3.6ArchiveDataRequest und ArchiveDataResponse.............................................................................28 3.6.1ArchiveDataRequest.....................................................................................................................29 3.6.2ArchiveDataResponse...................................................................................................................30 3.7VerifyRequest und VerifyResponse.................................................................................................32 3.7.1VerifyRequest...............................................................................................................................32 3.7.2VerifyResponse.............................................................................................................................36 4.Funktionen der Preservation-API gemäß ETSI TS 119 512...............................................................38 4.1Vergleich der ETSI TS 119 512 Preservation-API mit der TR-ESOR-S.4-Schnittstelle..................38 5.Funktionen der internen Schnittstellen..............................................................................................39 5.1TR-ESOR-S.1 (ArchiSafe-Modul – Krypto-Modul)........................................................................39 5.1.1Prüfung von digitalen Signaturen, beweisrelevanten Daten, Beweisdaten und Archivdatenobjekten..................................................................................................................39 5.1.2Anforderung einer digitalen Signatur............................................................................................39 5.2TR-ESOR-S.2 (ArchiSig-Modul – ECM-/Langzeitspeichersystem)................................................41 5.2.1Speichern eines Archivdatenobjektes............................................................................................41 5.2.2Ergänzen einer neuen Version eines Archivdatenobjektes............................................................41 5.2.3Auslesen von Archivdatenobjekten...............................................................................................41 5.3TR-ESOR-S.3 (ArchiSig-Modul – Krypto-Modul).........................................................................42 5.3.1Anfordern eines (qualifizierten) Zeitstempels...............................................................................42 5.3.2Prüfen eines (qualifizierten) Zeitstempels.....................................................................................43 5.3.3Berechnung eines Hashwertes......................................................................................................45 5.4TR-ESOR-S.5 (ArchiSafe-Modul – ECM-Langzeitspeichersystem)...............................................47 5.4.1Abfrage beweiswerterhaltend archivierter Daten..........................................................................47 5.4.2Löschen von Archivdatenobjekten................................................................................................48 5.4.3Abfrage diskreter Datenobjekte....................................................................................................48 5.5TR-ESOR-S.6 (ArchiSafe-Modul – ArchiSig-Modul).....................................................................48 

Bundesamt für Sicherheit in der Informationstechnik 

3 

Beweiswerterhaltung kryptographisch signierter Dokumente (ESOR) 

BSI TR 03125 

5.5.1Beweiswerterhaltende Archivierung elektronischer Daten...........................................................48 5.5.2Ergänzen einer neuen Version eines Archivdatenobjektes............................................................48 5.5.3Rückgabe technischer Beweisdaten..............................................................................................48 6.Fehlercodes........................................................................................................................................49 7.Spezifikation einer Webservice-basierten Schnittstelle......................................................................51 7.1Spezifikation der Aufruf- und Rückgabeparameter als XML-Schema.............................................51 7.2WSDL-Spezifikation der Schnittstelle TR-ESOR-S.4.....................................................................57 

## **Abbildungsverzeichnis** 

Abbildung 1: Schematische Darstellung der IT-Referenzarchitektur.....................................................6 Abbildung 2: Umsetzung der IT-Referenzarchitektur auf Basis des eCard-API-Frameworks................8 

## **Tabellenverzeichnis** 

Tabelle 1: Vergleich ETSI TS 119 512 Preservation-API mit TR-ESOR-S.4-Schnittstelle...................39 

Bundesamt für Sicherheit in der Informationstechnik 

4 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

## **1. Einführung** 

Ziel der Technischen Richtlinie „Beweiswerterhaltung kryptographisch signierter Dokumente“ ist die Spezifikation sicherheitstechnischer Anforderungen für den langfristigen Beweiswerterhalt von kryptographisch signierten elektronischen Dokumenten und Daten nebst zugehörigen elektronischen Verwaltungsdaten (Metadaten). 

Eine für diese Zwecke definierte Middleware (TR-ESOR-Middleware) im Sinn dieser Richtlinie umfasst alle diejenigen  Module ( **M** ) und Schnittstellen ( **S)** , die zur  Sicherung und zum Erhalt der Authentizität und zum Nachweis der Integrität der aufbewahrten Dokumente und Daten eingesetzt werden. 

Die im Hauptdokument dieser Technischen Richtlinie vorgestellte Referenzarchitektur besteht aus den nachfolgend beschriebenen funktionalen und logischen Einheiten: 

- der Eingangs-Schnittstelle S.4 der TR-ESOR-Middleware, die dazu dient, die TR-ESORMiddleware in die bestehende IT- und Infrastrukturlandschaft einzubetten; 

- dem  „ArchiSafe-Modul“  ( **[TR-ESOR-M.1]** ),  welches  den  Informationsfluss  in  der Middleware  regelt,  die  Sicherheitsanforderungen  an  die  Schnittstellen  zu  den  ITAnwendungen  umsetzt  und  für  eine  Entkopplung  von  Anwendungssystemen  und ECM/Langzeitspeicher sorgt; 

- dem „Krypto-Modul“ ( **[TR-ESOR-M.2]** ) nebst den zugehörigen Schnittstellen S.1 und S.3,  das  alle  erforderlichen  Funktionen  zur Berechnung  von  Hashwerten, Prüfung elektronischer Signaturen bzw. Siegel bzw. Zeitstempel, zur Nachprüfung elektronischer Zertifikate und zum Einholen qualifizierter Zeitstempel sowie (optional) elektronischer Signaturen bzw. Siegel für die Middleware zur Verfügung stellt. Darüber hinaus kann es Funktionen zur Ver- und Entschlüsselung von Daten und Dokumenten zur Verfügung stellen; 

- dem „ArchiSig-Modul“ ( **[TR-ESOR-M.3]** ) mit der Schnittstelle S.6, das die erforderlichen Funktionen für die Beweiswerterhaltung der digital signierten Unterlagen bereitstellt; 

- einem ECM/Langzeitspeicher mit den Schnittstellen S.2 und S.5, der die physische Archivierung/Aufbewahrung und auch das Speichern der beweiswerterhaltenden Zusatzdaten übernimmt. 

   - _Dieser ECM/Langzeitspeicher ist nicht mehr direkt Teil der Technischen Richtlinie, gleichwohl werden über die beiden Schnittstellen, die noch Teil der TR-ESORMiddleware sind, Anforderungen daran gestellt._ 

   - _Ebenso wenig ist die Applikationsschicht, die auch einen XML-Adapter enthalten kann, direkter Teil der Technischen Richtlinie, auch wenn dieser XML-Adapter als Teil einer Middleware implementiert werden kann._ 

Die in Abbildung Abbildung 1 dargestellte IT-Referenzarchitektur orientiert sich an der ArchiSafe[1] Referenzarchitektur und soll die logische (funktionale) Interoperabilität künftiger Produkte mit den Zielen und Anforderungen der Technischen Richtlinie ermöglichen und unterstützen. 

> 1 Siehe dazu http://www.archisafe.de 

Bundesamt für Sicherheit in der Informationstechnik 

5 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0006-01.png)


**Abbildung 1: Schematische Darstellung der IT-Referenzarchitektur** 

Diese Technische Richtlinie ist modular aufgebaut und spezifiziert in einzelnen Anlagen zum Hauptdokument die funktionalen und sicherheitstechnischen Anforderungen an die erforderlichen ITKomponenten und Schnittstellen der TR-ESOR-Middleware. Die Spezifikationen sind strikt plattform-, produkt-, und herstellerunabhängig. 

Das vorliegende Dokument trägt die Bezeichnung „Anlage TR-ESOR-E“ und konkretisiert die TRESOR-spezifischen  Schnittstellen auf Basis des in der BSI TR 03112 spezifizierten eCard-APIFrameworks. 

Bundesamt für Sicherheit in der Informationstechnik 

6 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

## **2. Überblick** 

In der Schnittstelle TR-S.4  müssen die im Folgenden näher aufgeführten Funktionen mit den hier beschriebenen Parameterkonstellationen unterstützt werden: 

- ArchiveSubmissionRequest und ArchiveSubmissionResponse (siehe Abschnitt 3.1) 

- ArchiveUpdateRequest und ArchiveUpdateResponse (siehe Abschnitt 3.2) 

- ArchiveRetrievalRequest und ArchiveRetrievalResponse (siehe Abschnitt 3.3) 

- ArchiveEvidenceRequest und ArchiveEvidenceResponse (siehe Abschnitt 3.4) 

- ArchiveDeletionRequest und ArchiveDeletionResponse (siehe Abschnitt 3.5) 

Darüber hinaus sollen die folgenden im vorliegenden Dokument näher aufgeführten Funktionen mit den hier beschriebenen Parameterkonstellationen unterstützt werden: 

- ArchiveDataRequest und ArchiveDataResponse (siehe Abschnitt 3.6) 

- VerifyRequest und VerifyResponse (siehe Abschnitt 3.7) 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0007-11.png)


## **Abbildung 2: Umsetzung der IT-Referenzarchitektur auf Basis des eCard-API-Frameworks** 

Wie in Abbildung 2 angedeutet, werden bei der vollständigen Umsetzung der IT-Referenzarchitektur auf Basis des eCard-API-Frameworks 

1. die Schnittstellen des Krypto-Moduls gemäß des eCard-API-Frameworks (Technische Richtlinie des BSI TR 03112) realisiert und 

2. auch die Schnittstellen des ArchiSafe-, ArchiSig-Modul und ECM/Langzeitspeichers nutzen die gleichen grundlegenden Schnittstellentypen (dss:RequestBaseType und 

Bundesamt für Sicherheit in der Informationstechnik 

7 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

dss:ResponseBaseType) aus **[OASIS-DSS]** , die auch bei den Signatur- und Verschlüsselungsfunktionen aus **[eCard-2]** genutzt werden. 

Die URI-Fehlercodes in den Rückgaben der nicht bereits in der Technischen Richtlinie des BSI TR 03112 definierten Funktionen haben das Präfix  http://www.bsi.bund.de/tr-esor/api/1.2, welches um entsprechende Bezeichner ergänzt wird. Dieser Namensraum ist in den visualisierten XML-Strukturen am Kürzel „tr“ erkennbar. 

Falls die in diesem Dokument beschriebenen Schnittstellen und Funktionen asynchron genutzt werden sollen,  kann dies unter Verwendung der hierfür vorgesehenen Mechanismen aus **[OASIS-Async]** realisiert werden. 

In den folgenden Abschnitten findet sich eine XML-basierte Spezifikation der  Funktionen zur Beweiswerterhaltung  kryptographisch  signierter  Dokumente.  Hierbei  werden  die  Funktionen  der ArchiSafe-Schnittstelle (TR-S.4) in Abschnitt 3 spezifiziert. In Abschnitt 4 wird das Preservation-API von **[TR 119 512]** beschrieben und mit der TR-ESOR-S.4-Schnittstelle verglichen. In  Abschnitt 5 findet sich eine Beschreibung der internen Schnittstellen der TR-ESOR-Middleware, die auf die vorherige  Spezifikation  der  Funktionen  in  Abschnitt 3 Bezug  nimmt.  In  Abschnitt 6 sind  die verwendeten  Fehlercodes  zusammengefasst  und  näher  erläutert  und  in  Abschnitt 7 finden  sich schließlich  die  normativen  XML-Schema-  und  WSDL-Spezifikationen  für  die  in  Abschnitt 3 spezifizierte ArchiSafe-Schnittstelle (TR-S.4). 

_**HINWEIS:** Im folgenden Text umfasst der Begriff_ _**„Digitale Signatur“** „fortgeschrittene elektronische Signaturen“  gemäß_ _**[eIDAS-VO,  Artikel  3  Nr. 11],** „qualifizierte  elektronische  Signaturen“  gemäß_ _**[eIDAS-VO, Artikel 3 Nr. 12]** , „fortgeschrittenen elektronische Siegel“ gemäß_ _**[eIDAS-VO, Artikel 3 Nr. 26]** und „qualifizierte elektronische Siegel“ gemäß_ _**[eIDAS-VO, Artikel 3 Nr. 27]** . Insofern umfasst der Begriff „digital signierte Dokumente“ sowohl solche, die fortgeschrittene elektronische Signaturen oder Siegel bzw. qualifizierte elektronische Signaturen oder Siegel tragen. Mit dem Begriff der_ _**„kryptographisch signierten Dokumente“** sind in dieser TR neben den gemäß_ _**[eIDAS-VO, Artikel 3 Nr. 12]** qualifiziert signierten, den gemäß_ _**[eIDAS-VO, Artikel 3 Nr. 27]** qualifiziert gesiegelten oder den gemäß_ _**[eIDAS-VO, Artikel 3 Nr. 34]** qualifiziert zeitgestempelten Dokumenten (im Sinne der eIDAS-Verordnung) ) auch Dokumente mit einer fortgeschrittenen Signatur gemäß_ _**[eIDAS-VO, Artikel 3 Nr. 11]** oder mit einem fortgeschrittenen Siegel gemäß_ _**[eIDAS-VO, Artikel 3 Nr. 26]** oder mit einem elektronischen Zeitstempel gemäß_ _**[eIDAS-VO, Artikel 3 Nr. 33]** erfasst, wie sie oft in der internen Kommunikation von Behörden entstehen. Nicht gemeint sind hier Dokumente mit einfachen Signaturen oder Siegeln basierend auf anderen (z. B. nicht-kryptographischen) Verfahren._ 

Bundesamt für Sicherheit in der Informationstechnik 

8 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

## **3. Funktionen der ArchiSafe-Schnittstelle (TR-ESOR-S.4)** 

In diesem Abschnitt findet sich eine XML-basierte Spezifikation der  Funktionen der TR-ESORMiddleware an der ArchiSafe-Schnittstelle **TR-ESOR-S.4 (TR-S.4)** : 

- ArchiveSubmissionRequest und ArchiveSubmissionResponse (siehe Abschnitt 3.1) 

- ArchiveUpdateRequest und ArchiveUpdateResponse (siehe Abschnitt 3.2) 

- ArchiveRetrievalRequest und  ArchiveRetrievalResponse (siehe Abschnitt 3.3) 

- ArchiveEvidenceRequest und ArchiveEvidenceResponse (siehe Abschnitt 3.4) 

- ArchiveDeletionRequest und ArchiveDeletionResponse (siehe Abschnitt 3.5) 

- ArchiveDataRequest und ArchiveDataResponse (siehe Abschnitt 3.6) 

- VerifyRequest und VerifyResponse (siehe Abschnitt 3.7) 

Die graphische Darstellung der Schnittstellen in diesem Kapitel wurde - analog zur Spezifikation des eCard-API-Frameworks (siehe z.B. **[eCard-2]** ) - mit einem XML-Viewer erstellt und dient lediglich der Veranschaulichung der XML-Strukturen. Die normative Spezifikation der Schnittstellen ist durch das XML-Schema bzw. die darauf aufbauende WSDL-Spezifikation (siehe Abschnitt 7) gegeben. 

## **3.1 ArchiveSubmissionRequest und ArchiveSubmissionResponse** 

Mit  der  Funktion ArchiveSubmissionRequest wird  dem  aufgerufenen  Modul  ein  Archivdatenobjekt  zur  Ablage  übergeben  und  das  aufrufende  Modul  erhält  im  Erfolgsfall  in  der ArchiveSubmissionResponse eine AOID zurück, mit der später wieder auf das archivierte Objekt oder  die  zugehörigen  technischen  Beweisdaten  zugegriffen  werden  kann.  Hierbei  kann  im xaip:XAIP-Element entweder ein physisches  XAIP (siehe Abschnitt 3.1 in **[TR-ESOR-F]** ) oder ein logisches  XAIP (LXAIP)  (siehe  Abschnitt  3.2  in **[TR-ESOR-F]** ) übergeben  werden.  Alternativ können im ArchiveData-Element binäre Nutzdaten übergeben werden. Hierbei wird der Typ des übergebenen Datenobjektes durch das Type-Attribut näher bestimmt. Dabei kann insbesondere ein base64Binary-codierter[2] ASiC-AIP-Container gemäß Abschnitt 3.3 in **[TR-ESOR-F]** mit einem Type=http://uri.etsi.org/ades/ASiC/type/ASiC-ERS Attribut übergeben werden. 

Wie in Abbildung 2 ersichtlich, wird diese Funktion neben der hier betrachteten Schnittstelle TR-S.4 auch in den Schnittstellen TR-S.2 (vgl. Abschnitt 5.2) und TR-S.6 (vgl. Abschnitt 5.5) genutzt. 

> 2 Siehe https://www.w3.org/TR/xmlschema-2/#base64Binary . 

Bundesamt für Sicherheit in der Informationstechnik 

9 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

## **3.1.1 ArchiveSubmissionRequest** 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0010-02.png)


**----- Start of picture text -----**<br>
Name ArchiveSubmissionRequest<br>Beschreibung Mit der Funktion ArchiveSubmissionRequest wird dem aufgerufenen Modul<br>ein Archivdatenobjekt übergeben.<br>Hierbei kann für eine effiziente Übertragung von großen Binärdaten der<br>optimierte Nachrichtenübertragungsmechanismus „SOAP Message Transmission<br>Optimization Mechanism (MTOM)“ [3]  genutzt werden.<br>Aufruf<br>Aufruf der ArchiveSubmissionRequest-Funktion<br>Name Beschreibung<br>**----- End of picture text -----**<br>


> 3 Siehe https://www.w3.org/TR/soap12-mtom/ . 

Bundesamt für Sicherheit in der Informationstechnik 

10 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

|||dss:OptionalInputs|Ist für optionale Eingabeelemente vorgesehen.<br>**(A3.1.1-1):**Gemäß der vorliegenden Spezifikation<br>sollen<br>folgende Elemente unterstützt werden:<br><br>AOID,<br><br>ReturnVerificationReport,<br><br>ImportEvidence.<br>Dabei gilt:<br><br>AOID<br>Durch die Übergabe einesAOID-<br>Elementeskann<br> die AOID von der<br>aufrufenden Anwendung vergeben<br>werden. Im Regelfall fehlt dieses Element<br>und die AOID wird vom aufgerufenen<br>Modul bereitgestellt.<br><br>ReturnVerificationReport<br>Durch die Übergabe eines<br>ReturnVerificationReport-<br>Elementes gemäß**[OASIS VR]**bzw.<br>**[eCard-2]**kann<br> ein ausführlicher<br>Prüfbericht in Form eines<br>VerificationReport-Elementes für<br>die imXAIP-Element oder im unten<br>genanntenImportEvidence-Element<br>enthaltenen Signatur- bzw. Siegel- bzw.<br>Zeitstempelobjekte oder Beweisdaten<br>angefordert werden. Bei einem<br>übergebenenxaip:XAIP-Element wird<br>imDetails-Element des<br>IndividualReport-Elementes des<br>zurückgelieferten Prüfberichts (vgl.<br>Abschnitt 3.3 in**[OASIS VR]**) ein<br>XAIPReport-Element gemäß**[TR-**<br>**ESOR-VR]**zurückgeliefert.<br>Sofern keinxaip:XAIPsondern ein<br>ArchiveData-Element und im<br>ImportEvidence-Element (siehe<br>unten) ein Evidence Record übergeben<br>wird, wird für jeden übergebenen<br>Evidence Record ein<br>EvidenceRecordReportgemäß<br>**[TR-ESOR-VR]**zurückgeliefert.|
|---|---|---|---|



Bundesamt für Sicherheit in der Informationstechnik 

11 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0012-01.png)


**----- Start of picture text -----**<br>
 ImportEvidence<br>Mit der Übergabe des nachfolgend<br>-<br>dargestellten ImportEvidence<br>Elementes kann der Import von einem<br>oder mehreren zu einer bestimmten XAIP-<br>bzw. LXAIP-Version bzw. zu den<br>übergebenen Binärdaten gehörenden<br>Evidence Records gemäß  [RFC4998]  oder<br>[RFC6283] [4]  oder  [TR-ESOR-ERS]<br>angestoßen werden. Die Struktur des<br>xaip:evidenceRecord-Elementes ist in<br>[TR-ESOR-F]  erläutert. Um Evidence<br>Records für mehrere Versionen eines<br>XAIPs oder LXAIPs importieren zu<br>können, kann dieses Element mehrmals<br>auftreten. Das<br>xaip:evidenceRecord-Element<br>muss hier die Attribute AOID und<br>VersionID enthalten.<br>Sofern die zu importierenden Evidence<br>Records bereits im XAIP bzw. LXAIP<br>enthalten sind, wird statt des Evidence<br>Records hier die entsprechende<br>CredentialID übergeben.<br>(A3.1.1-2):  Im Zuge des Imports von<br>Evidence Records müssen diese von der<br>TR-ESOR-Middleware vollständig geprüft<br>werden. Dies umfasst die im<br>entsprechenden ERS-Standard<br>vorgesehenen Prüfungungsschritte [5] , wobei<br>die jeweiligen Zertifikate der Zeitstempel<br>vollständig bis hin zu einer<br>vertrauenswürdigen Wurzel geprüft<br>werden müssen.<br>xaip:XAIP Enthält ein XML-basiertes Archivdatenobjekt<br>gemäß  [TR-ESOR-F] , das durch den Aufruf der<br>beweiswerterhaltenden Archivierung zugeführt<br>werden soll.<br>Hierbei  kann  es  sich  entweder  ein  physisches<br>XAIP (siehe Abschnitt 3.1 in  [TR-ESOR-F] ) oder<br>ein logisches XAIP (LXAIP) (siehe Abschnitt 3.2<br>in  [TR-ESOR-F] ) handeln.<br>**----- End of picture text -----**<br>


> 4 **[RFC4998]** muss, **[RFC6283]** kann unterstützt werden. 

> 5 Siehe Abschnitt 3.3 in **[RFC4998]** und Abschnitt 2.3 in **[RFC6283]** sowie **[TR-ESOR-ERS]** . 

Bundesamt für Sicherheit in der Informationstechnik 

12 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0013-01.png)


**----- Start of picture text -----**<br>
ArchiveData Enthält ein in einem beliebigen anderen Format<br>vorliegendes Archivdatenobjekt. Der hierfür<br>genutzte ArchiveDataType ist als anyType mit<br>einem optionalen Type-Attribut definiert.<br>Durch das Type-Attribut<br>http://uri.etsi.org/ades/ASiC/typ<br>e/ASiC-ERS wird klargestellt, dass es sich um<br>einen base64Binary-codierten [6] ASiC-AIP-<br>Container gemäß Abschnitt 3.3 in  [TR-ESOR-F]<br>handelt.<br>Durch das Type-Attribut<br>http://www.bsi.bund.de/tr-<br>esor/api/1.2/type/binaryData wird<br>klargestellt, dass im ArchiveData-Element ein<br>Kindelement binaryData übergeben wird, das<br>Base 64 codierte Nutzdaten und ein MimeType-<br>Attribut enthält, die beim entsprechenden XAIP in<br>ein dataObject-Element eingebettet werden.<br>Weitere Übergabetypen können im Rahmen einer<br>Profilierung der vorliegenden Spezifikation<br>spezifiziert werden.<br>**----- End of picture text -----**<br>


## **3.1.2 ArchiveSubmissionResponse** 

**Name ArchiveSubmissionResponse Beschreibung** Als Antwort auf einen ArchiveSubmissionRequest wird ein entsprechendes ArchiveSubmissionResponse-Element zurückgeliefert, das im Erfolgsfall einen eindeutigen Identifikator des Archivdatenobjektes, die AOID, enthält. **Rückgabe** ArchiveSubmissionResponse ist die Antwort zum ArchiveSubmissionRequest-Aufruf **Name Beschreibung** dss:Result Enthält die Statusinformationen und die Fehler zu einer durchgeführten Aktion. Die Struktur dieses Elements ist in **[eCard-1]** und unten näher beschrieben. 

> 6 Siehe https://www.w3.org/TR/xmlschema-2/#base64Binary . 

Bundesamt für Sicherheit in der Informationstechnik 

13 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0014-01.png)


**----- Start of picture text -----**<br>
Name ArchiveSubmissionResponse<br>dss:OptionalOutputs Ist für optionale Ausgabeelemente vorgesehen.<br>(A3.1.2-1):  Gemäß der vorliegenden Spezifikation<br>kann das folgende Element auftreten:<br> VerificationReport gemäß  [OASIS<br>VR]  bzw.  [eCard-2]  und  [TR-ESOR-VR] ,<br>der zurückgeliefert werden muss, sofern er<br>explizit angefordert wurde oder bei der<br>Prüfung der übergebenen Daten ein Fehler<br>oder eine Warnung aufgetreten ist und deshalb<br>als ResultMajor ein Fehlercode<br>.../resultmajor#error oder<br>.../resultmajor#warning zurückgeliefert wird.<br>AOID Muss, sofern die AOID [7]  vom aufgerufenen Modul<br>erzeugt oder ergänzt wurde, vorhanden sein und<br>für zukünftige Zugriffe auf das Archivdatenobjekt<br>genutzt werden.<br>Statusinformationen und Fehler bei ArchiveSubmissionResponse (vgl.<br>[eCard-1]  Abschnitt 4.1 und 4.2).<br>Name Fehlercode<br>ResultMajor  /resultmajor#ok<br> /resultmajor#error<br> /resultmajor#warning<br>**----- End of picture text -----**<br>


> 7 Die AOID (Archive Object Identifier) im vorliegenden Dokument entspricht dem POID (Preservation Object Identifier) aus **[ETSI TS 119 512]** . 

Bundesamt für Sicherheit in der Informationstechnik 

14 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0015-01.png)


**----- Start of picture text -----**<br>
Name ArchiveSubmissionResponse<br>ResultMinor  /resultminor/al/common#noPermission<br> /resultminor/al/common#internalError<br> /resultminor/al/common#parameterError<br> /resultminor/arl/lowSpaceWarning<br> /resultminor/arl/noSpaceError<br> /resultminor/arl/existingAOID<br> /resultminor/arl/notSupported<br> /resultminor/arl/unknownArchiveDataType<br> /resultminor/arl/XAIP_NOK<br> /resultminor/arl/XAIP_NOK_EXPIRED<br> /resultminor/arl/XAIP_NOK_SUBMTIME<br> /resultminor/arl/XAIP_NOK_SIG<br> /resultminor/arl/XAIP_NOK_ER<br>**----- End of picture text -----**<br>


## **3.2 ArchiveUpdateRequest und ArchiveUpdateResponse** 

Mit  der  Funktion ArchiveUpdateRequest wird  eine  neue  Version  für  ein  bereits  abgelegtes Archivdatenobjekt erzeugt. Hierbei werden die bereits abgelegten Daten nicht verändert, sondern es wird lediglich zusätzlich eine neue Version hinzugefügt. 

Wie  in  Abbildung  Abbildung  2  ersichtlich,  wird  diese  Funktion  neben  der  hier  betrachteten Schnittstelle TR-S.4 auch in TR-S.2 (vgl. Abschnitt 5.2) und TR-S.6 (vgl. Abschnitt 5.5) genutzt. 

## **3.2.1 ArchiveUpdateRequest** 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0015-06.png)


**----- Start of picture text -----**<br>
Name ArchiveUpdateRequest<br>Beschreibung Mit der Funktion ArchiveUpdateRequest wird eine neue Version für ein<br>bereits abgelegtes Archivdatenobjekt erzeugt (vgl.  [TR-ESOR-M.1] ).<br>Aufruf der ArchiveUpdateRequest-Funktion<br>Name Beschreibung<br>dss:OptionalInputs Ist für optionale Eingabeelemente vorgesehen.<br>(A3.2.1-1):  Gemäß der vorliegenden Spezifikation<br>sollen hier die auf Seite 11 spezifizierten<br>optionalen Eingabeelemente AOID,<br>ReturnVerificationReport und<br>ImportEvidence unterstützt werden.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

15 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

> xaip:DXAIP Enthält ein ergänzendes XML-basiertes Archivdatenobjekt (Delta-XAIP) gemäß ( **[TRESOR-F]** , Kap.3.1.6)  bzw. (Delta-LXAIP) gemäß ( **[TR-ESOR-F]** , Kap.3.2.2) das ein neues versionManifest, die Vorgängerversion, Verweise auf unverändert aus dieser übernommene Objekte und die zu ergänzenden Elemente enthält, die in einer neuen Version eines bereits abgelegten Archivdatenobjektes ergänzt werden sollen. 

## **3.2.2 ArchiveUpdateResponse** 

**Name ArchiveUpdateResponse Beschreibung** Als Antwort auf einen ArchiveUpdateRequest wird ein entsprechendes ArchiveUpdateResponse-Element zurückgeliefert, das im Erfolgsfall einen im Kontext einer AOID eindeutigen Identifikator der neuen Version des Archivdatenobjektes, die VersionID, enthält. **Rückgabe** 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0016-04.png)


**----- Start of picture text -----**<br>
ArchiveUpdateResponse ist die Antwort zum ArchiveUpdateRequest-<br>Aufruf<br>Name Beschreibung<br>dss:Result Enthält die Statusinformationen und die Fehler zu<br>einer durchgeführten Aktion. Die Struktur dieses<br>Elements ist in  [eCard-1]  und unten näher<br>beschrieben.<br>dss:OptionalOutputs Ist für optionale Ausgabeelemente vorgesehen.<br>(A3.2.2-1):  Gemäß der vorliegenden Spezifikation<br>kann das folgende Element auftreten:<br> VerificationReport gemäß  [OASIS<br>VR]  bzw.  [eCard-2]  und  [TR-ESOR-VR] ,<br>der zurückgeliefert werden muss, sofern er<br>explizit angefordert wurde oder bei der<br>Prüfung der übergebenen Daten ein Fehler<br>oder eine Warnung aufgetreten ist und<br>deshalb als ResultMajor ein Fehlercode<br>.../resultmajor#error oder<br>.../resultmajor#warning zurückgeliefert<br>wird.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

16 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0017-01.png)


**----- Start of picture text -----**<br>
Name ArchiveUpdateResponse<br>VersionID Ist im Erfolgsfall vorhanden und enthält den<br>bezüglich des über die AOID identifizierten AOID identifizierten  identifizierten<br>Archivdatenobjektes eindeutigen Versions-<br>Identifikator. Die VersionID sollsoll in der Form v1, v2,<br>… v x  gebildet werden.<br>Statusinformationen und Fehler bei ArchiveUpdateResponseArchiveUpdateResponse (vgl.  [eCard-<br>1]  Abschnitt 4.1 und 4.2).<br>Name Fehlercode<br>ResultMajor  /resultmajor#ok<br> /resultmajor#error<br> /resultmajor#warning<br>ResultMinor  /resultminor/al/common#noPermission<br> /resultminor/al/common#internalError<br> /resultminor/al/common#parameterError<br> /resultminor/arl/lowSpaceWarning<br> /resultminor/arl/noSpaceError<br> /resultminor/arl/existingPackage<br>InfoWarning<br> /resultminor/arl/notSupported<br> /resultminor/arl/DXAIP_NOK<br> /resultminor/arl/DXAIP_NOK_AOID<br> /resultminor/arl/DXAIP_NOK_EXPIREDXAIP_NOK_EXPIRED<br> /resultminor/arl/DXAIP_NOK_SUBM-XAIP_NOK_SUBM--<br>TIME<br> /resultminor/arl/DXAIP_NOK_SIGXAIP_NOK_SIG<br> /resultminor/arl/XAIP_NOK_ERXAIP_NOK_ER<br> /resultminor/arl/DXAIP_NOK_IDDXAIP_NOK_ID<br> /resultminor/arl/DXAIP_NOK_VersionDXAIP_NOK_Version<br>**----- End of picture text -----**<br>



![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0017-02.png)


**----- Start of picture text -----**<br>
Name ArchiveUpdateResponse<br>VersionID Ist im Erfolgsfall vorhanden und enthält den<br>bezüglich des über die AOID identifizierten AOID identifizierten  identifizierten<br>Archivdatenobjektes eindeutigen Versions-<br>Identifikator. Die VersionID sollsoll in der Form v1, v2,<br>… v x  gebildet werden.<br>Statusinformationen und Fehler bei ArchiveUpdateResponseArchiveUpdateResponse (vgl.  [eCard-<br>1]  Abschnitt 4.1 und 4.2).<br>Name Fehlercode<br>ResultMajor  /resultmajor#ok<br> /resultmajor#error<br> /resultmajor#warning<br>ResultMinor  /resultminor/al/common#noPermission<br> /resultminor/al/common#internalError<br> /resultminor/al/common#parameterError<br> /resultminor/arl/lowSpaceWarning<br> /resultminor/arl/noSpaceError<br> /resultminor/arl/existingPackage<br>InfoWarning<br> /resultminor/arl/notSupported<br> /resultminor/arl/DXAIP_NOK<br> /resultminor/arl/DXAIP_NOK_AOID<br> /resultminor/arl/DXAIP_NOK_EXPIREDXAIP_NOK_EXPIRED<br> /resultminor/arl/DXAIP_NOK_SUBM-XAIP_NOK_SUBM--<br>TIME<br> /resultminor/arl/DXAIP_NOK_SIGXAIP_NOK_SIG<br> /resultminor/arl/XAIP_NOK_ERXAIP_NOK_ER<br> /resultminor/arl/DXAIP_NOK_IDDXAIP_NOK_ID<br> /resultminor/arl/DXAIP_NOK_VersionDXAIP_NOK_Version<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

17 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

## **3.3 ArchiveRetrievalRequest und ArchiveRetrievalResponse** 

Mit  der  Funktion ArchiveRetrievalRequest wird  das  zu  einer  übergebenen AOID und VersionID gehörende physische XAIP-Archivdatenobjekt  gemäß **[TR-ESOR-F]** (Abschnitt 3.1), das logische XAIP gemäß **[TR-ESOR-F]** (Abschnitt 3.2) oder das ASiC-AIP gemäß **[TR-ESOR-F]** (Abschnitt 3.3) über die TR-ESOR-Middleware aus dem ECM-/Langzeitspeichersystem ausgelesen. 

Wie in Abbildung 2 ersichtlich, wird diese Funktion neben der hier betrachteten Schnittstelle TR-S.4 in ähnlicher Weise auch in den Schnittstellen S.2 (vgl. Abschnitt  5.2) und S.5 (vgl. Abschnitt  5.4) genutzt. 

## **3.3.1 ArchiveRetrievalRequest** 

**Name ArchiveRetrievalRequest Beschreibung** Mit der Funktion ArchiveRetrievalRequest wird ein im Langzeitspeicher abgelegtes Archivdatenobjekt  ausgelesen und zurückgeliefert. Hierbei kann für eine effiziente Übertragung von großen Binärdaten der optimierte Nachrichtenübertragungsmechanismus „SOAP Message Transmission Optimization Mechanism (MTOM)“[8] genutzt werden. **Beschreibung** Aufruf der ArchiveRetrievalRequest-Funktion **Name Beschreibung** 

> 8 Siehe https://www.w3.org/TR/soap12-mtom/ . 

Bundesamt für Sicherheit in der Informationstechnik 

18 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0019-01.png)


**----- Start of picture text -----**<br>
Name ArchiveRetrievalRequest<br>dss:OptionalInput Ist für optionale Eingabeelemente vorgesehen.<br>s<br>(A3.3.1-1):  Gemäß der vorliegenden Spezifikation<br>sollen die folgenden optionalen Eingabeelemente<br>unterstützt werden:<br>• POFormat<br>• IncludeERS<br>POFormat [9] – gibt das AIP-Format an, wobei<br>folgende Formate definiert sind:<br>• http://www.bsi.bund.de/tr-<br>esor/xaip/1.2 – für ein XAIP gemäß<br>Abschnitt 3.1 in  [TR-ESOR-F] ,<br>• http://www.bsi.bund.de/tr-<br>esor/l xaip/1.3 – für ein „Logisches<br>XAIP“ gemäß Abschnitt 3.2 in  [TR-ESOR-F] ,<br>• http://uri.etsi.org/ades/ASiC/type/ASiC-ERS für<br>einen base64Binary-codierten ASiC-AIP-<br>Container gemäß Abschnitt 3.3 in  [TR-ESOR-<br>F]  in einem PO-Element gemäß  [ETSI TS 119<br>-<br>512] , das im dss:OptionalOutputs<br>Element des ArchiveRetrievalResponse<br>zurückgeliefert wird.<br>Bei Nicht-Eingabe eines POFormats ist<br>XAIP das Default-Format.<br>IncludeERS – gibt an, dass das zurückgelieferte XAIP<br>oder das logische XAIP (LXAIP) oder das ASiC-AIP den<br>bzw. die  entsprechenden Evidence Record(s) im<br>angegebenen Format (vgl. ERSFormat, Seite 23)<br>enthalten soll.<br>Dieser bzw. diese Evidence Record(s) wird bzw. werden<br>bei XAIP bzw. LXAIP im dafür vorgesehenen<br>xaip:credential/xaip:EvidenceRecord<br>Element oder im Fall ASiC-AIP im ASiC-AIP-Container<br>gemäß Abschnitt 3.3 in   [TR-ESOR-F]  zurückgeliefert.<br>(A3.3.1-2):  Das VersionID-Attribut des<br>xaip:EvidenceRecord Elementes muss auf<br>die entsprechende Version verweisen.<br>Sofern das versionManifest nicht<br>kryptographisch geschützt ist, muss mit einem<br>unprotectedObjectPointer Element im<br>entsprechenden versionManifest auf die<br>credentialID des xaip:credential-<br>Elementes verwiesen werden.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

19 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0020-01.png)


**----- Start of picture text -----**<br>
Name ArchiveRetrievalRequest<br>Umgekehrt muss auf die vom Evidence Record<br>-<br>geschützten Datenobjekte im relatedObjects<br>Attribut des xaip:credential-Elementes<br>verwiesen werden.<br>AOID Enthält den eindeutigen Identifikator des<br>angeforderten Archivdatenobjektes.<br>VersionID Kann eine Folge von Versions-Identifikatoren<br>enthalten, durch die angegeben wird welche<br>Versionen des Archivdatenobjektes XAIP bzw.<br>LXAIP genau zurückgeliefert werden sollen.<br>Sofern das VersionID-Element nicht angegeben<br>ist, werden die zur letzten Version gehörigen<br>Datenobjekte und Verwaltungsinformationen eines<br>XAIPs bzw. LXAIPs zurückgeliefert.<br>Durch die Angabe von all werden alle<br>existierenden Versionen eines Archivdatenobjektes<br>zurückgeliefert.<br>**----- End of picture text -----**<br>


## **3.3.2 ArchiveRetrievalResponse** 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0020-03.png)


**----- Start of picture text -----**<br>
Name ArchiveRetrievalResponse<br>Beschreibung Als Antwort auf einen ArchiveRetrievalRequest wird ein entsprechendes<br>ArchiveRetrievalResponse-Element zurückgeliefert, welches im<br>Erfolgsfall das angeforderte Archivdatenobjekt im xaip:XAIP-Format gemäß<br>[TR-ESOR-F]  enthält.<br>Rückgabe<br>ArchiveRetrievalResponse ist die Antwort zum<br>ArchiveRetrievalRequest-Aufruf<br>Name Beschreibung<br>**----- End of picture text -----**<br>


> 9 Das POFormat-Element ist in **[ETSI TS 119 512]** folgendermaßen definiert: <element name="POFormat" type="anyURI" /> 

Bundesamt für Sicherheit in der Informationstechnik 

20 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0021-01.png)


**----- Start of picture text -----**<br>
Name ArchiveRetrievalResponse<br>dss:Result Enthält die Statusinformationen und die Fehler zu<br>einer durchgeführten Aktion. Die Struktur dieses<br>Elements ist in  [eCard-1]  und weiter unten näher<br>beschrieben.<br>Sofern nur ein Teil der angeforderten Versionen<br>des Archivdatenobjektes zurückgeliefert werden<br>konnte, wird dies durch den Fehlercode<br>.../resultminor/arl/requestOnlyPartlySuccessfulWar<br>ning angezeigt.<br>dss:OptionalOutputs Ist für optionale Ausgabeelemente vorgesehen, die<br>im Rahmen einer Profilierung der vorliegenden<br>Spezifikation definiert werden sollen.<br>Insbesondere kann hier ein PO-Element gemäß<br>[ETSI TS 119 512]  enthalten sein, das ein<br>base64Binary-codierten ASiC-AIP gemäß<br>Abschnitt 3.3 in  [TR-ESOR-F]  enthält, sofern<br>dieses angefordert wird.<br>xaip:XAIP Sofern kein Fehler aufgetreten ist, wird das<br>angeforderte XML-basierte Archivdatenobjekt<br>(XAIP oder LXAIP) gemäß  [TR-ESOR-F]<br>zurückgeliefert.<br>Statusinformationen und Fehler bei ArchiveRetrievalResponse (vgl.<br>[eCard-1] ).<br>Name Fehlercode<br>ResultMajor  /resultmajor#ok<br> /resultmajor#error<br> /resultmajor#warning<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

21 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0022-01.png)


**----- Start of picture text -----**<br>
Name ArchiveRetrievalResponse<br>ResultMinor  /resultminor/al/common#noPermission<br> /resultminor/al/common#internalError<br> /resultminor/al/common#parameterError<br> /resultminor/arl/unknownAOID<br> /resultminor/arl/notSupported<br> /resultminor/arl/requestOnlyPartlySuc-<br>cessfulWarning<br> /resultminor/arl/unknownVersionID<br> /resultminor/arl/unknownPOFormat<br>ResultMessage Beim Auftreten der Fehlermeldung .../unknown-<br>VersionID soll die problematische VersionID<br>hier zurückgeliefert werden.<br>**----- End of picture text -----**<br>


## **3.4 ArchiveEvidenceRequest und ArchiveEvidenceResponse** 

Mit der Funktion  ArchiveEvidenceRequest werden die zugehörigen technischen Beweisdaten (Evidence Records gemäß **[RFC4998]** oder **[RFC6283]**[10 ] oder **[RFC4998]** mit der Profilierung aus **[TR-ESOR-ERS]** )  für  beweiswerterhaltend  aufbewahrte  und  über AOID-Elemente  adressierte Archivdatenobjekte (xaip:XAIP) zurückgeliefert. 

Wie  in  Abbildung  Abbildung  2  ersichtlich,  wird  diese  Funktion  neben  der  hier  betrachteten Schnittstelle TR-S.4 auch in TR-S.6 (vgl. Abschnitt 5.5) genutzt. 

## **3.4.1 ArchiveEvidenceRequest** 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0022-06.png)


**----- Start of picture text -----**<br>
Name ArchiveEvidenceRequest<br>Beschreibung Mit der Funktion ArchiveEvidenceRequest können für beweiswerterhaltend<br>abgelegte Archivdatenobjekte technische Beweisdaten in Form von Evidence<br>Records gemäß  [RFC4998]  oder  [RFC6283] [11]  in der Profilierung gemäß<br>[TR-ESOR-ERS]  angefordert werden.<br>Beschreibung<br>Aufruf der ArchiveEvidenceRequest-Funktion<br>Name Beschreibung<br>**----- End of picture text -----**<br>


> 10 **[RFC4998]** muss, **[RFC6283]** kann unterstützt werden. 

> 11 **[RFC4998]** muss, **[RFC6283]** kann unterstützt werden. 

Bundesamt für Sicherheit in der Informationstechnik 

22 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0023-01.png)


**----- Start of picture text -----**<br>
Name ArchiveEvidenceRequest<br>dss:OptionalInputs Ist für optionale Eingabeelemente vorgesehen.<br>(A3.4.1-1):  Gemäß der vorliegenden Spezifikation<br>soll das folgende Element unterstützt werden:<br>Mit dem Element tr:ERSFormat vom Typ<br>anyURI kann das gewünschte Format der<br>zurückgelieferten Evidence Records angegeben<br>werden, wobei folgende URIs vorgesehen sind:<br> urn:ietf:rfc:4998 für ASN.1-basierte<br>Evidence Records gemäß  [RFC4998]<br>oder<br> urn:ietf:rfc:6283 für XML-basierte<br>Evidence Records gemäß  [RFC6283] .<br>Fehlt das ERSFormat-Element, so werden<br>ASN.1-basierte Evidence Records gemäß<br>[RFC4998]  in der Profilierung gemäß<br>[TR-ESOR-ERS]  zurückgeliefert.<br>AOID Ist der eindeutige Identifikator des angeforderten<br>Archivdatenobjektes.<br>VersionID Kann mehrfach auftreten und angeben für welche<br>Versionen eines über die AOID identifizierten<br>Archivdatenobjektes XAIP bzw. LXAIP  Evidence<br>Records zurückgeliefert werden sollen.<br>Sofern das VersionID-Element nicht angegeben<br>ist, wird der Beweisdatensatz für die aktuelle<br>Version des XAIP bzw. des LXAIP<br>zurückgeliefert.<br>Durch die Angabe von all werden Evidence<br>Records für alle existierenden Versionen eines<br>Archivdatenobjektes zurückgeliefert.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

23 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

## **3.4.2 ArchiveEvidenceResponse** 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0024-02.png)


**----- Start of picture text -----**<br>
Name ArchiveEvidenceResponse<br>Beschreibung Als Antwort auf einen ArchiveEvidenceRequest wird ein entsprechendes<br>ArchiveEvidenceResponse-Element zurückgeliefert, das die angeforderten<br>Beweisdaten enthält.<br>Rückgabe<br>ArchiveEvidenceResponse ist die Antwort zum<br>ArchiveEvidenceRequest-Aufruf<br>Name Beschreibung<br>dss:Result Enthält die Statusinformationen und die Fehler zu<br>einer durchgeführten Aktion. Die Struktur dieses<br>Elements ist in Abschnitt 4.1.2 von  [eCard-1]  und<br>unten näher beschrieben.<br>Sofern nicht für alle mittels der übergebenen AOID<br>adressierten Archivdatenobjekte entsprechende<br>Beweisdaten (Evidence Records) zurückgeliefert<br>werden konnten, wird dies durch<br>die .../resultminor/arl/requestOnlyPartly<br>SuccessfulWarning angezeigt.<br>dss:OptionalOutputs Ist für optionale Ausgabeelemente vorgesehen und<br>kann beispielsweise entsprechende Steuerelemente<br>(responseControls) enthalten, die im Rahmen<br>einer Profilierung der vorliegenden Spezifikation<br>definiert werden sollen.<br>xaip:evidenceRecord Sofern vom ArchiSig-Modul entsprechende<br>Evidence Records [12]  gemäß  [RFC4998]  bzw.<br>[RFC6283]  konstruiert werden können, werden<br>diese hier in der Profilierung gemäß  [TR-ESOR-<br>ERS]  zurückgeliefert. Die detaillierte Struktur<br>dieses Elementes ist nachfolgend erläutert.<br>**----- End of picture text -----**<br>


> 12 Sofern die TR-ESOR-Middleware mehrere redundante Hashbäume pflegt, werden hier mehrere Evidence Records zurückgeliefert. 

Bundesamt für Sicherheit in der Informationstechnik 

24 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

## **Name** 

## **ArchiveEvidenceResponse** 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0025-03.png)


Das xaip:evidenceRecord-Element gemäß **[TR-ESOR-F]** ist vom Typ **xaip:EvidenceRecordType** , der als Erweiterung des **ec:EvidenceRecordType** aus **[eCard-2]** definiert ist und zusätzlich die Attribute AOID und VersionID, enthält, die in **[TR-ESOR-F]** näher erläutert sind. 

**(A3.4.2-1):** Bei der hier beschriebenen Verwendung von xaip:evidenceRecord müssen die Attribute AOID und VersionID gesetzt sein. 

**Name Beschreibung** xmlEvidenceRecord Enthält einen XML-basierten Evidence Record gemäß **[RFC6283]** . asn1EvidenceRecord Enthält  einen  ASN.1-basierten  Evidence  Record gemäß **[RFC4998]** . 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0025-07.png)


Statusinformationen und Fehler bei ArchiveEvidenceResponse (vgl. **[eCard-1]** ). 

**Name Fehlercode** ResultMajor  /resultmajor#ok  /resultmajor#error  /resultmajor#warning 

Bundesamt für Sicherheit in der Informationstechnik 

25 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0026-01.png)


**----- Start of picture text -----**<br>
Name ArchiveEvidenceResponse<br>ResultMinor  /resultminor/al/common#noPermission<br> /resultminor/al/common#internalError<br> /resultminor/al/common#parameterError<br> /resultminor/arl/notSupported13<br> /resultminor/arl/unknownAOID<br> /resultminor/arl/unknownVersionID/<br> resultminor/arl/requestOnlyPartly<br>SuccessfulWarning<br>**----- End of picture text -----**<br>


## **3.5 ArchiveDeletionRequest und ArchiveDeletionResponse** 

Mit der Funktion  ArchiveDeletionRequest wird ein Archivdatenobjekt  über  die TR-ESORMiddleware aus dem ECM-/Langzeitspeichersystem gelöscht. 

Wie in Abbildung 2 ersichtlich, wird diese Funktion neben der hier betrachteten Schnittstelle TR-S.4 auch in der Schnittstelle TR-S.5 (vgl. Abschnitt 5.4) genutzt. 

## **3.5.1 ArchiveDeletionRequest** 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0026-06.png)


**----- Start of picture text -----**<br>
Name ArchiveDeletionRequest<br>Beschreibung Mit der Funktion ArchiveDeletionRequest kann ein im Langzeitspeicher<br>abgelegtes Archivdatenobjekt (XAIP oder LXAIP oder ASiC-AIP) gelöscht<br>werden.<br>Beschreibung<br>Aufruf der ArchiveDeletionRequest-Funktion<br>Name Beschreibung<br>**----- End of picture text -----**<br>


> 13 Im ResultMessage-Element sollen nähere Informationen darüber zurückgeliefert werden, welche angeforderte Funktionalität nicht unterstützt wird. 

Bundesamt für Sicherheit in der Informationstechnik 

26 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0027-01.png)


**----- Start of picture text -----**<br>
Name ArchiveDeletionRequest<br>dss:OptionalInputs Ist für optionale Eingabeelemente vorgesehen.<br>Insbesondere bei einer vorzeitigen Löschung muss<br>das folgende Element ReasonOfDeletion<br>genutzt und unterstützt werden:<br>(A3.5.1-1):  Das ReasonOfDeletion-Element<br>muss vorhanden sein, sofern die<br>Aufbewahrungsdauer der letzten Version noch<br>nicht abgelaufen ist, und enthält neben dem<br>Namen der aufrufenden Instanz auch eine<br>Begründung für die Löschung.<br>(A3.5.1-2):  Die gesamte Aktion einschließlich der<br>Begründung muss protokolliert werden und der<br>übergebene RequestorName soll mit den<br>verwendeten Authentisierungsinformationen<br>abgeglichen werden.<br>AOID Das AOID-Element gibt an, welches<br>Archivdatenobjekt gelöscht werden soll.<br>**----- End of picture text -----**<br>


## **3.5.2 ArchiveDeletionResponse** 

**Name ArchiveDeletionResponse Beschreibung** Als Antwort auf einen ArchiveDeletionRequest wird ein entsprechendes ArchiveDeletionResponse-Element zurückgeliefert, das Informationen über den Erfolg oder Misserfolg der Anfrage enthält. **Rückgabe** ArchiveDeletionResponse ist die Antwort zum ArchiveDeletionRequest-Aufruf 

**Name Beschreibung** dss:Result Enthält die Statusinformationen und die Fehler zu einer durchgeführten Aktion. Die Struktur dieses Elements ist in **[eCard-1]** und unten näher beschrieben. 

Bundesamt für Sicherheit in der Informationstechnik 

27 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0028-01.png)


**----- Start of picture text -----**<br>
Name ArchiveDeletionResponse<br>dss:OptionalOutputs Ist für optionale Ausgabeelemente vorgesehen<br>und kann beispielsweise entsprechende<br>Steuerelemente (responseControls)<br>enthalten, die im Rahmen einer Profilierung der<br>vorliegenden Spezifikation definiert werden<br>sollen.<br>Statusinformationen und Fehler bei ArchiveDeletionResponse (vgl.<br>[eCard-1] ).<br>Name Fehlercode<br>ResultMajor  /resultmajor#ok<br> /resultmajor#error<br>ResultMinor  /resultminor/al/common#noPermission<br> /resultminor/al/common#internalError<br> /resultminor/al/common#parameterError<br> /resultminor/arl/unknownAOID<br> /resultminor/arl/notSupported<br> /resultminor/arl/missingReasonOf<br>Deletion<br>**----- End of picture text -----**<br>


## **3.6 ArchiveDataRequest und ArchiveDataResponse** 

Mit  der  Funktion ArchiveDataRequest können  diskrete  Datenelemente  aus  einem  bereits abgelegten Archivdatenobjekt (xaip:XAIP) ausgelesen werden. 

Die detaillierte Ausgestaltung dieser Funktion wird dem Hersteller überlassen. Der Hersteller ist zur Dokumentation  der  an  der  Schnittstelle  unterstützten  Funktionalität  verpflichtet.  Im  Zuge  der Zertifizierung wird geprüft, dass die in der Dokumentation beschriebene Funktionalität umgesetzt ist. Wie in Abbildung 2 ersichtlich, wird diese Funktion neben der hier betrachteten Schnittstelle TR-S.4 auch in TR-S.5 (vgl. Abschnitt 5.4) genutzt. 

Bundesamt für Sicherheit in der Informationstechnik 

28 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

## **3.6.1 ArchiveDataRequest** 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0029-02.png)


**----- Start of picture text -----**<br>
Name ArchiveDataRequest<br>Beschreibung Mit der Funktion ArchiveDataRequest können diskrete Datenelemente aus<br>einem im ECM-/Langzeitspeichersystem abgelegten, zumindest logisch im<br>xaip:XAIP-Format gemäß [TR-ESOR-F]  vorliegenden, Archivdatenobjekt<br>ausgelesen werden.<br>Beschreibung<br>Aufruf der ArchiveDataRequest-Funktion<br>Name Beschreibung<br>dss:OptionalInputs Ist für optionale Eingabeelemente vorgesehen und<br>kann beispielsweise Steuerelemente<br>(requestControls) enthalten, die im Rahmen<br>einer Profilierung der vorliegenden Spezifikation<br>definiert werden sollen.<br>Die vorliegende Spezifikation definiert keine<br>solchen optionalen Eingabelemente.<br>AOID Dieses Element enthält den Identifikator eines<br>bestimmten Archivdatenobjektes.<br>tr:DataLocation Das tr:DataLocation-Element kann mehrmals<br>auftreten und bestimmt die „Lokation“ der<br>auszulesenden diskreten Datenelemente bezüglich<br>eines zumindest logisch im xaip:XAIP-Format<br>gemäß  [TR-ESOR-F]  vorliegenden<br>Archivdatenobjektes.<br>Die detaillierte Ausgestaltung der hier unterstützen<br>Funktionalität bleibt dem Hersteller überlassen.<br>Sofern der ArchiveDataRequest unterstützt<br>wird, muss dieser die Details der an der<br>Schnittstelle angebotenen Funktionalität<br>dokumentieren.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

29 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

**Name ArchiveDataRequest** Das DataLocation-Element spezifiziert, welche Teile eines Archivobjektes zurückgeliefert werden sollen und ist folgendermaßen definiert: <element name="DataLocation"> <complexType> <complexContent> <extension base="anyType"> <attribute name="Type" type="anyURI"/> </extension> </complexContent> </complexType> </element> 

Im Type-Attribut wird angegeben, welche Transformation für den Zugriff auf die gewünschten Daten angewandt werden soll, wobei die folgenden URIs vorgesehen sind: 

 http://www.w3.org/TR/2007/REC-xpath20-20070123/ für XPath,  http://www.w3.org/TR/2007/REC-xquery-20070123/ für XQuery und  http://www.w3.org/TR/2003/REC-xptr-framework-20030325 für XPointer 

## **3.6.2 ArchiveDataResponse** 

**Name ArchiveDataResponse Beschreibung** Als Antwort auf einen ArchiveDataRequest wird ein entsprechendes ArchiveDataResponse-Element zurückgeliefert, das die gewünschten Informationen enthält. 

## **Rückgabe** 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0030-07.png)


ArchiveDataResponse ist die Antwort zum ArchiveDataRequest-Aufruf 

**Name Beschreibung** dss:Result Enthält die Statusinformationen und die Fehler zu einer durchgeführten Aktion. Die Struktur dieses Elements ist in **[eCard-1]** und unten näher beschrieben. Sofern nur ein Teil der angefragten diskreten Datenobjekte zurückgeliefert werden konnte, wird dies durch den Fehlercode …/resultminor/arl/requestOnlyPartlySuccessfulWar ning angezeigt. 

Bundesamt für Sicherheit in der Informationstechnik 

30 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0031-01.png)


**----- Start of picture text -----**<br>
Name ArchiveDataResponse<br>dss:OptionalOutputs Ist für optionale Ausgabeelemente vorgesehen und<br>kann beispielsweise entsprechende Steuerelemente<br>(responseControls) enthalten, die im Rahmen responseControls) enthalten, die im Rahmen ) enthalten, die im Rahmen  enthalten, die im Rahmen<br>einer Profilierung der vorliegenden Spezifikation<br>definiert werden sollen.sollen..<br>XAIPData Enthält im Erfolgsfall die gewünschten Daten und<br>die „Lokation“, aus der diese aus der im<br>ECM-/Langzeitspeichersystem zumindest logisch<br>existierenden XAIP- bzw. LXAIP-Struktur XAIP- bzw. LXAIP-Struktur - bzw. LXAIP-Struktur<br>ausgelesen wurden. Die detaillierte Struktur dieses<br>Elementes ist nachfolgend dargestellt und erläutert.<br>Das XAIPData-Element enthält im Erfolgsfall die gewünschten Daten.XAIPData-Element enthält im Erfolgsfall die gewünschten Daten.-Element enthält im Erfolgsfall die gewünschten Daten.<br>Name Beschreibung<br>dss:Result Gibt an, ob die Anfrage erfolgreich durchgeführt<br>werden konnte oder nicht.<br>Als ResultMajorResultMajor sind die beiden folgenden<br>Werte möglich:<br> .../resultmajor#ok<br> .../resultmajor#error<br>Als ResultMinorResultMinor sind die folgenden Werte<br>möglich:<br> .../resultminor/arl/unknownLocation<br> .../resultminor/al/common#parameterError<br> .../resultminor/al/common#internalError<br>tr:DataLocation Das DataLocation-Element spezifiziert, welche DataLocation-Element spezifiziert, welche -Element spezifiziert, welche<br>Teile eines Archivobjektes zurückgeliefert werden.<br>Die detaillierte Ausgestaltung dieses Parameters ist<br>dem Hersteller überlassen. Siehe auch oben (Seite<br>30).<br>Value Enthält im Erfolgsfall die gewünschten Daten.<br>**----- End of picture text -----**<br>



![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0031-02.png)


**----- Start of picture text -----**<br>
Name ArchiveDataResponse<br>dss:OptionalOutputs Ist für optionale Ausgabeelemente vorgesehen und<br>kann beispielsweise entsprechende Steuerelemente<br>(responseControls) enthalten, die im Rahmen responseControls) enthalten, die im Rahmen ) enthalten, die im Rahmen  enthalten, die im Rahmen<br>einer Profilierung der vorliegenden Spezifikation<br>definiert werden sollen.sollen..<br>XAIPData Enthält im Erfolgsfall die gewünschten Daten und<br>die „Lokation“, aus der diese aus der im<br>ECM-/Langzeitspeichersystem zumindest logisch<br>existierenden XAIP- bzw. LXAIP-Struktur XAIP- bzw. LXAIP-Struktur - bzw. LXAIP-Struktur<br>ausgelesen wurden. Die detaillierte Struktur dieses<br>Elementes ist nachfolgend dargestellt und erläutert.<br>Das XAIPData-Element enthält im Erfolgsfall die gewünschten Daten.XAIPData-Element enthält im Erfolgsfall die gewünschten Daten.-Element enthält im Erfolgsfall die gewünschten Daten.<br>Name Beschreibung<br>dss:Result Gibt an, ob die Anfrage erfolgreich durchgeführt<br>werden konnte oder nicht.<br>Als ResultMajorResultMajor sind die beiden folgenden<br>Werte möglich:<br> .../resultmajor#ok<br> .../resultmajor#error<br>Als ResultMinorResultMinor sind die folgenden Werte<br>möglich:<br> .../resultminor/arl/unknownLocation<br> .../resultminor/al/common#parameterError<br> .../resultminor/al/common#internalError<br>tr:DataLocation Das DataLocation-Element spezifiziert, welche DataLocation-Element spezifiziert, welche -Element spezifiziert, welche<br>Teile eines Archivobjektes zurückgeliefert werden.<br>Die detaillierte Ausgestaltung dieses Parameters ist<br>dem Hersteller überlassen. Siehe auch oben (Seite<br>30).<br>Value Enthält im Erfolgsfall die gewünschten Daten.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

31 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0032-01.png)


**----- Start of picture text -----**<br>
Name ArchiveDataResponse<br>Statusinformationen und Fehler bei ArchiveDataResponseArchiveDataResponse<br>Name Fehlercode<br>ResultMajor  /resultmajor#ok<br> /resultmajor#error<br> /resultmajor#warning<br>ResultMinor <br><br><br> /resultminor/arl/unknownAOID<br> /resultminor/arl/notSupported<br><br>fulWarning<br>**----- End of picture text -----**<br>



![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0032-02.png)


**----- Start of picture text -----**<br>
Statusinformationen und Fehler bei ArchiveDataResponseArchiveDataResponse (vgl.  [eCard-1] ).<br>Name Fehlercode<br>ResultMajor  /resultmajor#ok<br> /resultmajor#error<br> /resultmajor#warning<br>ResultMinor  /resultminor/al/common#noPermission<br> /resultminor/al/common#internalError<br> /resultminor/al/common#parameterError<br> /resultminor/arl/unknownAOID<br> /resultminor/arl/notSupported<br> /resultminor/arl/requestOnlyPartlySuccess-<br>fulWarning<br>**----- End of picture text -----**<br>


## **3.7 VerifyRequest und VerifyResponse** 

## **3.7.1 VerifyRequest** 

Mit der Funktion VerifyRequest werden XML-basierte Archivdatenobjekte (XAIP), logische XAIP (LXAIP)  oder  ASiC-AIP-basierte  Datencontainer  samt  der  darin  enthaltenen  oder  zusätzlich übergebenen beweisrelevanten Daten (Signaturen, Siegel, Zeitstempel, Zertifikate, Sperrlisten, OCSPResponses etc.) und Beweisdaten (Evidence Records) geprüft. 

Wie in Abbildung 2 ersichtlich, wird diese Funktion neben der hier betrachteten Schnittstelle TR-S.4 auch in TR-S.1 (vgl. Abschnitt 5.1) genutzt. 

Bundesamt für Sicherheit in der Informationstechnik 

32 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

## **VerifyRequest** 

**Name VerifyRequest Beschreibung** Mit der Funktion VerifyRequest (vgl. Abschnitt 3.2.2 von **[eCard-2]** ) werden XML-basierte Archivdatenobjekte (XAIP), logische XAIP oder ASiC-AIPbasierte Datencontainer samt der darin enthaltenen oder zusätzlich übergebenen beweisrelevanten Daten (Signaturen, Siegel, Zeitstempel, Zertifikate, Sperrlisten, OCSP-Responses etc.) und Beweisdaten (Evidence Records), geprüft. **Aufrufparameter** Aufruf der VerifyRequest-Funktion. **Name Beschreibung** 

Bundesamt für Sicherheit in der Informationstechnik 

33 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0034-01.png)


**----- Start of picture text -----**<br>
Name VerifyRequest<br>dss:OptionalInputs Das OptionalInputs-Element kann zusätzliche<br>Eingabeelemente enthalten.<br>(A3.7.1-1):  Hierbei sollen insbesondere die in<br>[eCard-2]  definierten Elemente und Aufrufoptionen<br>unterstützt werden.<br>Dies umfasst insbesondere die folgenden Elemente:<br> VerifyUnderSignaturePolicy,<br> ReturnVerificationReport<br>Es gilt im Einzelnen:<br> VerifyUnderSignaturePolicy<br>Sofern in einem<br>dss:Document/InlineXML-Kindelement<br>von dss:InputDocuments ein XAIP-<br>Element in Form eines gewöhnlichen XAIP<br>oder eines logischen XAIP gemäß  [TR-<br>ESOR-F]  enthalten ist, kann mit dem Element<br>VerifyUnderSignaturePolicy und der<br>im DefaultPolicy/<br>SignaturePolicyIdentifier-Element<br>angegebenen Signature-Policy<br>-<br>http://www.bsi.bund.de/tr<br>-<br>esor/sigpolicy/verify xaip<br>die Prüfung und Ergänzung aller im<br>übergebenen XAIP- bzw. LXAIP-Container<br>bzw. ASiC-AIP enthaltenen digitalen<br>Signaturen angefordert werden.<br>(A3.7.1-2):  Hierbei müssen alle digitalen<br>Signaturinformationen (Signaturen, Siegel,<br>Zeitstempel, Zertifikate, Sperrlisten, OCSP-<br>Responses etc.) bis hin zu einer<br>vertrauenswürdigen Wurzel geprüft werden.<br>Die hierbei ermittelten Prüfinformationen<br>(Zertifikate, Sperrlisten, OCSP-Responses)<br>werden nach Möglichkeit als unsignierte<br>Attribute bzw. Properties in den<br>entsprechenden digitalen Signaturen bzw. in<br>den Kind-Elementen certificateValues<br>bzw. revocationValues des credential-<br>Elementes abgelegt.<br>Wenn sowohl die Signature-Policy<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

34 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0035-01.png)


**----- Start of picture text -----**<br>
Name VerifyRequest<br>-<br>http://www.bsi.bund.de/tr<br>-<br>esor/sigpolicy/verify xaip<br>als auch das Element<br>ReturnVerificationReport  übergeben<br>wird, dann muss der dann erzeugte Prüfbericht<br>in das Kind-Element<br>vr:VerificationReport des<br>credential-  Elements  abgelegt werden.<br>(A3.7.1-3):  Sofern in der credentialSection<br>des übergebenen XAIP-, LXAIP- oder ASiC-AIP-<br>Containers ein oder mehrere<br>xaip:EvidenceRecord-Elemente gemäß  [TR-<br>ESOR-F]  enthalten sind, müssen diese entsprechend<br>geprüft werden.<br> ReturnVerificationReport<br>Durch die Übergabe eines<br>ReturnVerificationReport-Elementes<br>gemäß  [OASIS VR]  bzw.  [eCard-2]  und<br>[TR-ESOR-VR] kann ein ausführlicher<br>Prüfbericht in Form eines<br>VerificationReport-Elementes für die<br>übergebenen Objekte (Signaturen, Siegel,<br>Zeitstempel, Zertifikate, Sperrinformationen,<br>Evidence Records, XAIP, LXAIP, ASiC-AIP<br>mit den vorgenannten Daten) angefordert<br>werden. Wenn nur das Element<br>ReturnVerificationReport  übergeben<br>wird ohne Angabe der Signature-Policy, dann<br>ist im Rahmen des VerifyResponse nur das<br>erzeugte VerificationReport- Element<br>zurück zu geben.<br>dss:InputDocuments Das dss:InputDocuments-Element enthält die zur<br>Prüfung benötigten Dokumente, sofern diese nicht<br>bereits im unten erläuterten SignatureObject-<br>Element enthalten sind.<br>Außerdem kann in einem<br>dss:Document/InlineXML-Kindelement ein XAIP-<br>Element mit einem XAIP gemäß  [TR-ESOR-F]<br>(Abschnitt 3.1) oder einem LXAIP-Element gemäß<br>[TR-ESOR-F]  (Abschnitt 3.2) bzw. in einem<br>dss:Document/dss:Base64Data-Kindelement<br>ein ASiC-AIP gemäß  [TR-ESOR-F]  (Abschnitt 3.3)<br>übergeben werden, so dass alle darin enthaltenen<br>digitalen Signaturen in Verbindung mit der oben<br>angegebenen Signature-Policy geprüft und ergänzt<br>werden oder die Prüfung der darin enthaltenen<br>Evidence Records angestoßen wird.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

35 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0036-01.png)


**----- Start of picture text -----**<br>
Name VerifyRequest<br>dss:Signature In dss:SignatureObject-Elementen können<br>Object grundsätzlich eigenständige digitale Signaturen<br>(detached digital signatures) zur Prüfung übergeben<br>werden. Wenn digitale Signaturen bereits im<br>dss:InputDocuments enthalten sind, können die<br>optionalen dss:SignatureObject-Elemente<br>entfallen.<br>(A3.7.1-4):  Als Kindelement von<br>dss:SignatureObject/Other kann auch ein<br>xaip:EvidenceRecord-Element übergeben<br>werden, um die entsprechende Prüfung des Evidence<br>Record anzustoßen. In diesem Fall müssen die<br>Attribute AOID und VersionID vorhanden sein und<br>das zugehörige XAIP- bzw. LXAIP- bzw. ASiC-AIP-<br>Element muss als Kindelement von<br>dss:InputDocuments/dss:<br>Document/InlineXML übergeben werden.<br>Sofern das dss:SignatureObject-Element fehlt,<br>muss genau ein dss:InputDocuments-Element<br>vorhanden sein, das die zu prüfenden digitalen<br>Signaturobjekte enthält.<br>**----- End of picture text -----**<br>


## **3.7.2 VerifyResponse** 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0036-03.png)


**----- Start of picture text -----**<br>
Name VerifyResponse<br>Beschreibung Als Antwort auf einen VerifyRequest wird ein entsprechendes<br>VerifyResponse-Element gemäß Abschnitt 3.2.2 von  [eCard-2]<br>zurückgeliefert.<br>Rückgabe<br>Rückgabe der VerifyRequest-Funktion<br>Name Beschreibung<br>dss:Result Enthält die Statusinformationen und die Fehler<br>zu einer durchgeführten Aktion. Die Struktur<br>dieses Elements und die möglichen Fehlercodes<br>sind in Abschnitt 4.1.2 von  [eCard-1]  und<br>Abschnitt 3.2.2 von  [eCard-2]  beschrieben.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

36 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0037-01.png)


**----- Start of picture text -----**<br>
Name VerifyResponse<br>dss:OptionalOutputs Sofern ein VerificationReport angefordert wurde<br>oder ein Fehler aufgetreten ist, enthält dieses<br>Element den Prüfbericht in Form eines<br>VerificationReport-Elementes oder das um<br>diese Prüfinformationen ergänzte<br>-<br>Archivdatenobjekt in Form eines xaip:XAIP<br>Elements.<br>Die grundsätzliche Struktur des Prüfberichtes ist<br>in  [OASIS-VR]  näher beschrieben. In<br>[TR-ESOR-VR]  finden sich entsprechende<br>Korrekturen für den EvidenceRecordReport<br>sowie die Beschreibung des XAIPReport.<br>Details zur Ablage dieser Prüfinformationen im<br>(L)XAIP-Container finden sich in  [TR-ESOR-<br>F] .<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

37 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

## **4. Funktionen der Preservation-API gemäß ETSI TS 119 512** 

Neben der in Abschnitt 3 spezifizierten TR-ESOR-S.4 Schnittstelle steht mit der „Preservation-API“ aus **[ETSI TS 119 512]** eine funktional weitgehend äquivalente, aber in Kürze international standardisierte Alternative zur Verfügung, die zusätzlich oder anstatt der TR-ESOR-S.4-Schnittstelle als Eingangsschnittstelle zur TR-ESOR-Middleware genutzt werden kann. 

Für den Einsatz der „Preservation-API“ gemäß **[ETSI TS 119 512]** im Rahmen der vorliegenden Technischen Richtlinie werden im Rahmen von TR-ESOR die folgenden Mindestanforderungen definiert: 

- RetrieveInfo gemäß Abschnitt 5.3.2 von **[ETSI TS 119 512]** muss unterstützt werden. Hierbei muss zumindest ein Bewahrungsprofil unterstützt werden, welches das Bewahrungsschema 

   - http://uri.etsi.org/19512/scheme/pds+pgd+aug+wst+ers gemäß Annex F.1 von **[ETSI TS 119 512]** umsetzt. 

- PreservePO gemäß Abschnitt 5.3.3 von **[ETSI TS 119 512]** muss unterstützt werden, wobei zumindest eines der in **[TR-ESOR-F]** definierten Archivdatenobjekt-Formate (XAIP, LXAIP oder ASiC-AIP) unterstützt werden muss. 

- RetrievePO gemäß Abschnitt 5.3.4 von **[ETSI TS 119 512]** muss unterstützt werden, wobei zumindest eines der in **[TR-ESOR-F]** definierten Archivdatenobjekt-Formate (XAIP, LXAIP oder ASiC-AIP) sowie Evidence Records gemäß **[RFC4998]** in der Profilierung gemäß **[TR-ESOR-ERS]** unterstützt werden müssen. 

- DeletePO gemäß Abschnitt 5.3.5 von **[ETSI TS 119 512]** muss unterstützt werden. 

- UpdatePOC gemäß Abschnitt 5.3.6 von **[ETSI TS 119 512]** muss unterstützt werden. 

- RetrieveTrace gemäß Abschnitt 5.3.7 von **[ETSI TS 119 512]** kann unterstützt werden. 

- ValidateEvidence gemäß Abschnitt 5.3.8 von **[ETSI TS 119 512]** soll unterstützt werden. Sofern diese Operation unterstützt wird, muss zumindest die Validierung von Evidence Records gemäß **[RFC4998]** in der Profilierung gemäß **[TR-ESOR-ERS] sowie** die Validierung der in **[TR-ESOR-F]** definierten Archivdatenobjekt-Formate **(XAIP, LXAIP oder ASiC-AIP)** unterstützt werden. Darüber hinaus kann die Validierung von Evidence Records gemäß **[RFC6283]** unterstützt werden. 

- Search gemäß Abschnitt 5.3.7 von **[ETSI TS 119 512]** kann unterstützt werden. 

## **4.1 Vergleich der ETSI TS 119 512 Preservation-API mit der TR-ESORS.4-Schnittstelle** 

Hierbei entspricht die Preservation-API gemäß **[ETSI TS 119 512]** der Eingangs-Schnittstelle S.4 zur TR-ESOR-Middleware **[TR-ESOR-F],** wie in der folgenden Tabelle dargestellt. 

Bundesamt für Sicherheit in der Informationstechnik 

38 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

|**ETSI TS 119 512**|**Verbindlich**|**TR-ESOR V1.2 ff**|**Verbindlich-**|
|---|---|---|---|
||**-keitsgrad**||**keitsgrad**|
|PreservePO|mandatory|ArchiveSubmissionRequest|mandatory|
|DeletePO|mandatory|ArchiveDeletionRequest|mandatory|
|RetrievePO|mandatory|ArchiveEvidenceRequest|Mandatory|
|RetrievePO|mandatory|ArchiveRetrievalRequest|mandatory|
|UpdatePOC|optional|ArchiveUpdateRequest|optional|
|(optional)||||
|Validate Evidence|optional|VerifyRequest|optional|
|RetrieveInfo|mandatory|||
|RetrieveTrace|optional|||
|Search|optional|ArchiveDataRequest|optional|



## **Tabelle 1: Vergleich ETSI TS 119 512 Preservation-API mit TR-ESOR-S.4-Schnittstelle** 

In TR-ESOR V1.3 wird die Transformation von der ETSI TS 119 512 Preservation-API mit der TRESOR-S.4-Schnittstelle im Detail weiter ausgearbeitet. 

Bundesamt für Sicherheit in der Informationstechnik 

39 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

Bundesamt für Sicherheit in der Informationstechnik 

40 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

## **5. Funktionen der internen Schnittstellen** 

In diesem Abschnitt werden die internen Schnittstellen der Referenzarchitektur TR-S.1 bis TR-S.3 und TR-S.5 bis TR-S.6 (vgl. Abbildung Abbildung 2) erläutert: 

- TR-S.1: TR-ESOR-S.1 (ArchiSafe-Modul – Krypto-Modul) (siehe Abschnitt 5.1) 

- TR-S.2: TR-ESOR-S.2 (ArchiSig-Modul – ECM-/Langzeitspeichersystem) (siehe Abschnitt 5.2) 

- TR-S.3: TR-ESOR-S.3 (ArchiSig-Modul – Krypto-Modul) (siehe Abschnitt 5.3) 

- TR-S.5: TR-ESOR-S.5 (ArchiSafe-Modul –ECM-/Langzeitspeichersystem) (siehe Abschnitt 5.4) 

- TR-S.6: TR-ESOR-S.6 (ArchiSafe-Modul – ArchiSig-Modul) (siehe Abschnitt 5.5) 

## **5.1 TR-ESOR-S.1 (ArchiSafe-Modul – Krypto-Modul)** 

Dieser Abschnitt beschreibt, wie die Abbildung 2 dargestellte Schnittstelle TR-S.1 auf Basis des eCard-API-Frameworks ( **[BSI TR 03112]** ) umgesetzt werden kann. 

Diese Schnittstelle TR-S.1 umfasst zwei wesentliche Funktionen: 

- Prüfung von digitalen Signaturen, beweisrelevanten Daten, Beweisdaten und Archivdatenobjekten (VerifyRequest / VerifyResponse) 

- Anforderung von digitalen Signaturen (optional) (SignRequest / SignResponse) 

## **5.1.1 Prüfung von digitalen Signaturen, beweisrelevanten Daten, Beweisdaten und Archivdatenobjekten** 

Für die Prüfung von digitalen Signaturen, beweisrelevanten Daten (Zertifikaten, Zertifikatstatusinformationen, Zeitstempeln, etc.), Beweisdaten (Evidence Records) und Archivdatenobjekten (XAIPs bzw. LXAIPs bzw. ASiC-AIPs) ist in **[OASIS-DSS]** und **[eCard-2]** der Funktionsaufruf VerifyRequest und  die  zugehörige  Antwort VerifyResponse definiert. Entsprechende Korrekturen  und  Ergänzungen  sind  darüber  hinaus  in **[TR-ESOR-VR]  bzw.** in Abschnitt 3.7 erläutert. 

Die Durchführung der eigentlichen Prüffunktion von beweisrelevanten Daten sowie Beweisdaten muss im Krypto-Modul (siehe Anlage **[TR-ESOR-M.2]** ) als Komponente der TR-ESOR-Middleware oder in einem, vom Krypto-Modul aufgerufen, (qualifizierten) Vertrauensdiensteanbieter erfolgen. Die für die Prüfung notwendigen Prüfinformationen (z.B. OCSP-Antworten oder Sperrlisten) müssen von den Vertrauensdiensteanbietern abgerufen werden. 

## **5.1.2 Anforderung einer digitalen Signatur** 

Für die Anforderung einer digitalen Signatur ist in **[OASIS-DSS]** und **[eCard-2]** die Funktion **SignRequest** und die zugehörige Antwort **SignResponse** definiert. 

## **5.1.2.1 SignRequest (Anforderung einer digitalen Signatur)** 

Ein  SignRequest im Kontext der Schnittstelle S.1 übergibt ein Archivdatenobjekt (XAIP- bzw. LXAIP- bzw. ASiC-AIP-Dokument) an das Krypto-Modul zur Anforderung einer digitalen Signatur. 

Bundesamt für Sicherheit in der Informationstechnik 

41 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0042-01.png)


**----- Start of picture text -----**<br>
Name SignRequest<br>Beschreibung Mit der Funktion SignRequest aus  [eCard-2]  kann für das übergebene<br>Archivdatenobjekt eine digitale Signatur von einem (qualifizierten)<br>Vertrauensdiensteanbieter gemäß  [eIDAS-VO, Artikel 3 Nr. 19 bzw. Nr. 20]<br>angefordert  werden.<br>Beschreibung<br>Aufruf der SignRequest-Funktion<br>Name Beschreibung<br>dss:OptionalInputs Kann eines oder mehrere der in  [eCard-2]<br>definierten optionalen Eingabeelemente enthalten.<br>dss:InputDocuments Enthält die zu signierenden Dokumente oder<br>Datenstrukturen. Weitere Informationen hierzu<br>finden sich in  [OASIS-DSS]  und  [eCard-2] .<br>**----- End of picture text -----**<br>


## **5.1.2.2 SignResponse** 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0042-03.png)


**----- Start of picture text -----**<br>
Name SignResponse<br>Beschreibung Als Antwort auf einen SignRequest wird vom Krypto-Modul ein<br>entsprechendes SignResponse-Element gemäß Abschnitt 3.2.1 von<br>[eCard-2]  zurückgeliefert.<br>Rückgabe<br>SignResponse ist die Antwort zum SignRequest-Aufruf<br>Name Beschreibung<br>dss:Result Enthält die Statusinformationen und die Fehler zu<br>einer durchgeführten Aktion. Die Struktur dieses<br>Elements und die möglichen Fehlercodes sind in<br>Abschnitt 4.1.2 von  [eCard-1]  und in Abschnitt<br>3.2.1 von  [eCard-2]  beschrieben.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

42 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0043-01.png)


**----- Start of picture text -----**<br>
Name SignResponse<br>dss:OptionalOutputs Kann ein DocumentWithSignature-Element<br>enthalten, in denen z.B. ein XAIP-Element mit der<br>eingebetteten digitalen Signatur enthalten ist.<br>Details finden sich in Abschnitt 3.2.1 von  [eCard-<br>2] .<br>dss:SignatureObject Kann eine erzeugte digitale Signatur in Form eines<br>dss:SignatureObject-Elementes enthalten.<br>Details finden sich in Abschnitt 3.2.1 von  [eCard-<br>2] . Sofern die erstellte digitale Signatur bereits im<br>oben genannten DocumentWithSignature-<br>Element vorhanden ist, wird kein<br>dss:SignatureObject-Element<br>zurückgeliefert.<br>**----- End of picture text -----**<br>


## **5.2 TR-ESOR-S.2 (ArchiSig-Modul – ECM-/Langzeitspeichersystem)** 

Dieser Abschnitt beschreibt in den folgenden Unterkapiteln, wie die in Abbildung 2 dargestellte Schnittstelle TR-S.2 auf Basis der auch dem eCard-API-Frameworks ( **[BSI TR 03112]** ) zu Grunde liegenden Basistypen aus **[OASIS-DSS]** umgesetzt werden kann. 

Diese Schnittstelle umfasst drei wesentliche Funktionen: 

- Speichern eines Archivdatenobjektes (ArchiveSubmissionRequest / ArchiveSubmissionResponse) 

- Ergänzen einer neuen Version eines Archivdatenobjektes (ArchiveUpdateRequest / ArchiveUpdateResponse) 

- Auslesen eines Archivdatenobjektes (ArchiveRetrievalRequest / ArchiveRetrievalResponse) 

Neben der Umsetzung der Funktion „ArchivSubmission-Request/-Response” zum Speichern eines Archivdatenobjektes“ (Upload)  auf Basis der, auch dem eCard-API-Frameworks ( **[BSI TR 03112]** ) zu Grunde liegenden, Basistypen aus **[OASIS-DSS]** kann diese Funktion auch anders technisch umgesetzt werden, um den Upload von Datenobjekten im Rahmen eines logischen XAIP (LXAIP) gemäß ( **[TR-ESOR-F]** , Kap. 3.2) technisch performant zu ermöglichen. Dabei sind die Anforderungen gemäß  ( **[TR-ESOR]** , Kap. 7.2 und 7.4.4) zu erfüllen. 

Laut **[ETSI TS 119 511]** gilt: OVR-7.8-02 [WST] The preservation service shall be integrated in the IT environment implemented in such a way that all storage access by the preservation client changing the content of the storage shall only be done by the preservation service. 

Daher ist es erforderlich, dass die eigentliche „Upload-Komponente“ ein (eigenständiges) Modul des TR-ESOR-Bewahrungsdienstes darstellt und logisch als Teil des TR-ESOR-Systems zu betrachten ist. 

## **5.2.1 Speichern eines Archivdatenobjektes** 

Für das Speichern eines Archivdatenobjektes ist in Abbildung 2 der Funktionsaufruf ArchiveSubmissionRequest und  die  zugehörige  Antwort ArchiveSubmissionResponse gemäß Abschnitt 3.1 vorgesehen. 

## **5.2.2 Ergänzen einer neuen Version eines Archivdatenobjektes** 

Für  das  Ergänzen  einer  neuen  Version  eines  Archivdatenobjektes  ist  in  Abbildung  2  der Funktionsaufruf ArchiveUpdateRequest und die zugehörige Antwort ArchiveUpdateResponse gemäß Abschnitt 3.2 vorgesehen. 

Bundesamt für Sicherheit in der Informationstechnik 

43 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

## **5.2.3 Auslesen von Archivdatenobjekten** 

Für das Auslesen von Archivdatenobjekten ist in Abbildung 2 der Funktionsaufruf ArchiveRetrievalRequest und ArchiveRetrievalResponse gemäß Abschnitt 3.3 vorgesehen. 

## **5.3 TR-ESOR-S.3 (ArchiSig-Modul – Krypto-Modul)** 

Dieser Abschnitt beschreibt, wie die in Abbildung 2 dargestellte Schnittstelle TR-S.3 auf Basis des eCard-API-Frameworks (BSI TR 03112) umgesetzt werden kann. 

Die Schnittstelle TR-S.3 umfasst drei wesentliche Funktionen: 

- Anfordern eines (qualifizierten) Zeitstempels (TimestampRequest / TimeStampResponse) 

- Prüfen eines (qualifizierten) Zeitstempels (VerifyRequest / VerifyResponse) 

- Berechnung eines Hashwertes (Hash / HashResponse) 

## **5.3.1 Anfordern eines (qualifizierten) Zeitstempels** 

Zum Anfordern eines (qualifizierten) Zeitstempels kann ein geeignet profilierter Funktionsaufruf SignRequest  mit entsprechender Antwort SignResponse gemäß **[OASIS-DSS]** bzw. **[eCard-2]** genutzt werden. 

Der  qualifizierte  Zeitstempel muss von  einem  qualifizierten  Vertrauensdiensteanbieter  gemäß **[eIDAS-VO, Artikel 3 Nr. 20]** durch das Krypto-Modul (siehe Anlage **[TR-ESOR-M.2]** ) als eine Komponente der Middleware angefordert werden. 

## **5.3.1.1 SignRequest für das Anfordern eines Zeitstempels** 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0044-13.png)


**----- Start of picture text -----**<br>
Name SignRequest<br>Beschreibung Ein SignRequest im Kontext der Schnittstelle S.3 übergibt einen Hashwert, zu<br>dem ein (qualifizierter) Zeitstempel erstellt werden soll, an das Krypto-Modul.<br>Beschreibung<br>Aufruf der SignRequest-Funktion<br>Name Beschreibung<br>dss:OptionalInputs Enthält genau ein Element SignatureType mit<br>der URI urn:ietf:rfc:3161, durch die klargestellt<br>wird, dass ein Zeitstempel gemäß  [RFC3161]<br>erzeugt werden soll.<br>dss:InputDocuments (A4.3.1.1-1):  Während das Element<br>dss:InputDocuments in  [OASIS-DSS]  und<br>[eCard-2]  optional ist, muss es hier vorhanden sein<br>und genau ein dss:Document-Element in der<br>DocumentHash-Ausprägung enthalten. Dieses<br>Element enthält den Hashwert, aus dem ein<br>(qualifizierter) Zeitstempel erzeugt werden soll.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

44 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

## **5.3.1.2 SignResponse mit Zeitstempel** 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0045-02.png)


**----- Start of picture text -----**<br>
Name SignResponse<br>Beschreibung Als Antwort auf einen SignRequest wird vom Krypto-Modul ein<br>entsprechendes SignResponse-Element gemäß Abschnitt 3.2.1 von  [eCard-2]<br>zurückgeliefert. Im Kontext der Schnittstelle S.3 wird hier ein (qualifizierter)<br>Zeitstempel zurückgeliefert.<br>Rückgabe<br>SignResponse ist die Antwort zum SignRequest-Aufruf<br>Name Beschreibung<br>dss:Result Enthält die Statusinformationen und die Fehler zu<br>einer durchgeführten Aktion. Die Struktur dieses<br>Elements und die möglichen Fehlercodes sind in<br>Abschnitt 4.1.2 von  [eCard-1]  und in Abschnitt<br>3.2.1 von  [eCard-2]  beschrieben.<br>dss:OptionalOutputs Das optionale Element dss:OptionalOutputs<br>ist nicht vorhanden.<br>dss:SignatureObject Enthält – sofern kein Fehler aufgetreten ist –<br>genau ein dss:SignatureObject-Element,<br>das ein dss:Timestamp-Element enthält, in<br>dem der Zeitstempel in Form eines<br>RFC3161TimeStampToken-Elementes enthalten<br>ist.<br>**----- End of picture text -----**<br>


## **5.3.2 Prüfen eines (qualifizierten) Zeitstempels** 

Zum Prüfen eines (qualifizierten) Zeitstempels ist in TR-S.3 (vgl. Abbildung 2) der Funktionsaufruf VerifyRequest und  die  Antwort VerifyResponse gemäß **[OASIS-DSS]** und **[eCard-2]** vorgesehen. 

Die Durchführung der eigentlichen Prüffunktion eines (qualifizierten Zeitstempels) muss im KryptoModul (siehe Anlage **[TR-ESOR-M.2]** ) als Komponente der TR-ESOR-Middleware oder in einem, vom Krypto-Modul aufgerufen, externen Validierungsdienst eines (qualifizierten) Vertrauensdiensteanbieters erfolgen. Die für die Prüfung notwendigen Prüfinformationen (z.B. OCSPAntworten oder Sperrlisten)  müssen von den (qualifizierten) Vertrauensdiensteanbietern abgerufen werden. 

Bundesamt für Sicherheit in der Informationstechnik 

45 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

## **5.3.2.1 VerifyRequest** 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0046-02.png)


**----- Start of picture text -----**<br>
Name VerifyRequest<br>Beschreibung Ein VerifyRequest im Kontext der Schnittstelle S.3 übergibt einen<br>(qualifizierten) Zeitstempel an das Krypto-Modul zur Verifikation der darin<br>enthaltenen  digitalen Signatur. Außerdem werden die für die Prüfung genutzten<br>Zertifikate und Sperrinformationen in den zurück gelieferten Zeitstempel<br>eingefügt. Entsprechende Empfehlungen für die Ablage dieser Informationen<br>finden sich in  [TR-ESOR-F] .<br>Aufrufparameter<br>Aufruf der VerifyRequest-Funktion.<br>Name Beschreibung<br>dss:OptionalInputs Kann optionale Eingabeelemente enthalten.<br>(A4.3.2.1-1):  Gemäß der vorliegenden<br>Spezifikation muss das optionale Eingabeelement<br>ReturnUpdatedSignature aus Abschnitt<br>4.5.8 von  [OASIS-DSS]  unterstützt werden, bei<br>dem mit dem Type-Attribut<br>-<br>http://www.bsi.bund.de/tr esor/api/1.2 klargestellt<br>wird, dass alle bei der Prüfung verwendeten<br>Zertifikate und Sperrinformationen wie in  [TR-<br>ESOR-F]  spezifiziert in den Zeitstempel eingefügt<br>werden müssen.<br>(A4.3.2.1-2):  Darüber hinaus soll das optionale<br>Eingabeelement<br>ReturnVerificationReport unterstützt<br>werden, so dass für den entsprechenden Zeitstempel<br>ein Prüfbericht gemäß  [OASIS-VR]  zurückgeliefert<br>werden kann.<br>dss:InputDocuments Das optionale Element dss:InputDocuments soll<br>nicht vorhanden sein und wird ignoriert.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

46 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

**Name VerifyRequest** dss:SignatureObject Es ist genau ein dss:SignatureObject-Element in der dss:TimeStamp/ RFC3161TimeStampToken Ausprägung vorhanden, das den zu prüfenden Zeitstempel enthält. 

## **5.3.2.2 VerifyResponse** 

**Name VerifyResponse Beschreibung** Als Antwort auf einen VerifyRequest wird vom Krypto-Modul ein entsprechendes VerifyResponse-Element gemäß Abschnitt 3.2.2 von **[eCard-2]** zurückgeliefert. **Rückgabe** Rückgabe der VerifyRequest-FunktionVerifyRequest-Funktion-Funktion 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0047-04.png)


**----- Start of picture text -----**<br>
Rückgabe der VerifyRequest-FunktionVerifyRequest-Funktion-Funktion<br>Name Beschreibung<br>dss:Result Enthält die Statusinformationen und die Fehler<br>zu einer durchgeführten Aktion. Die Struktur<br>dieses Elements und die möglichen Fehlercodes<br>sind in Abschnitt 4.1.2 von  [eCard-1]  und in<br>Abschnitt 3.2.2 von  [eCard-2]  beschrieben.<br>dss:OptionalOutputs Sofern nicht ein Fehler aufgetreten ist, muss ein<br>UpdatedSignature-Element vorhanden sein,<br>das ein dss:SignatureObject-Element in<br>der dss:TimeStamp/<br>RFC3161TimeStampToken-Ausprägung<br>enthält, in dem sich der um die bei der Prüfung<br>genutzten Zertifikate und Sperrinformationen<br>ergänzte Zeitstempel befindet.<br>Darüber hinaus kann ein<br>VerificationReport-Element gemäß<br>[OASIS VR]  vorhanden sein, das im<br>IndividualReport/Details-Element<br>ein IndividualTimeStampReport-<br>Element enthält.<br>**----- End of picture text -----**<br>


## **5.3.3 Berechnung eines Hashwertes** 

Zur Berechnung eines Hashwertes ist in TR-S.3 (vgl. Abbildung 2) der Funktionsaufruf Hash und die Antwort HashResponse aus **[eCard-4]** in Verbindung mit dem Generic Cryptography-Protokoll aus **[eCard-7]** vorgesehen. 

Bundesamt für Sicherheit in der Informationstechnik 

47 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

## **5.3.3.1 Hash** 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0048-02.png)


**----- Start of picture text -----**<br>
Name Hash<br>Beschreibung Bei einem Hash-Aufruf im Kontext der Schnittstelle S.3 wird für die übergebenen<br>Daten ein Hashwert berechnet.<br>Aufruf<br>parameter<br>Aufruf der Funktion Hash.<br>Name Beschreibung<br>ConnectionHandle Das ConnectionHandle-Element (vgl.  [eCard-4] ,<br>Abschnitt 3.1.3) gibt bei Bedarf an, auf welchem<br>Hardwaremodul oder entfernten eCard-API-Framework<br>die Berechnung des Hashwertes erfolgen soll. Sofern<br>die Berechnung des Hashwertes durch das lokale<br>Software-Modul erfolgen soll, soll das<br>ConnectionHandle-Element leer sein.<br>DIDName [14] Dieser Parameter spezifiziert den zu verwendenden<br>Hashalgorithmus. Welche kryptographischen<br>Algorithmen zu einem bestimmten Zeitpunkt als<br>geeignet erachtet werden, ist Gegenstand von  [ETSI TS<br>119 312]  und  [SOG-IS] .<br>DIDScope Löst im ISO/IEC 24727-3 Standard Mehrdeutigkeiten<br>zwischen lokalen und globalen DIDs mit gleichem<br>Namen auf. Dieser Parameter wird hier nicht verwendet<br>und sofern vorhanden ignoriert.<br>Message Enthält die Nachricht (bzw. einen Teil derselben, siehe<br>[eCard-7] ), aus der ein Hashwert berechnet werden soll.<br>**----- End of picture text -----**<br>


> 14 Eine in ISO/IEC 24727 näher beschriebene Differential Identity ermöglicht die Ausführung von kryptographischen Operationen. Der DIDName ist der logische Name, der für den Zugriff auf dieses kryptographische Objekt genutzt wird. 

Bundesamt für Sicherheit in der Informationstechnik 

48 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

## **5.3.3.2 HashResponse** 

**Name HashResponse Beschreibung** Als Antwort auf einen Hash-Aufruf wird vom Krypto-Modul ein entsprechendes HashResponse-Element gemäß Abschnitt 3.5.4 von **[eCard4]** zurückgeliefert. **Rückgabe** Rückgabe der Funktion Hash. **Name Beschreibung** dss:Result Enthält die Statusinformationen und die Fehler zu einer durchgeführten Aktion. Die Struktur dieses Elements und die möglichen Fehlercodes sind in Abschnitt 4.1.2 von **[eCard-1]** und in Abschnitt 3.5.4 von **[eCard-4]** beschrieben. Hash Enthält den Hashwert, sofern ein solcher berechnet werden konnte. 

## **5.4 TR-ESOR-S.5 (ArchiSafe-Modul – ECM-Langzeitspeichersystem)** 

Dieser Abschnitt beschreibt in den folgenden Unterkapiteln, wie die in TR-S.5 (vgl. Abbildung 2) skizzierte Schnittstelle auf Basis der auch dem eCard-API-Framework ( **[BSI TR 03112]** ) zu Grunde liegenden Basistypen aus **[OASIS-DSS]** umgesetzt werden kann. 

Die in TR-S.5 definierte Schnittstelle umfasst die folgenden Funktionen: 

- Abfrage beweiswerterhaltend archivierter Daten (ArchiveRetrievalRequest / -Response) 

- Löschen von Archivdatenobjekten (ArchiveDeletionRequest / -Response) 

- Abfrage diskreter Datenobjekte (ArchiveDataRequest / -Response) 

Neben  der  Umsetzung  der  Funktion  „ArchivRetrieval-Request/-Request”  zum Auslesen  eines Archivdatenobjektes“ (Download) auf Basis der, auch dem eCard-API-Frameworks ( **[BSI TR 03112]** ) zu Grunde liegenden, Basistypen aus **[OASIS-DSS]** kann diese Funktion auch anders technisch umgesetzt werden, um den Download  von Datenobjekten im Rahmen eines logischen XAIP (LXAIP) gemäß ( **[TR-ESOR-F]** , Kap. 3.2) technisch performant zu ermöglichen. Dabei sind die Anforderungen gemäß  des Hauptdokuments ( **[TR-ESOR]** , Kap. 7.2 und 7.45) zu erfüllen. 

## **5.4.1 Abfrage beweiswerterhaltend archivierter Daten** 

Für die Abfrage beweiswerterhaltend archivierter Daten ist der Funktionsaufruf ArchiveRetrievalRequest und die Antwort ArchiveRetrievalResponse gemäß Abschnitt 3.3 vorgesehen. 

Bundesamt für Sicherheit in der Informationstechnik 

49 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

## **5.4.2 Löschen von Archivdatenobjekten** 

Für das Löschen von Archivdatenobjekten ist der Funktionsaufruf  ArchiveDeletionRequest und ArchiveDeletionResponse gemäß Abschnitt 3.5 vorgesehen. 

## **5.4.3 Abfrage diskreter Datenobjekte** 

Für  die  Abfrage  diskreter  Datenobjekte  ist  der  Funktionsaufruf   ArchiveDataRequest und ArchiveDataResponse gemäß Abschnitt 3.5 vorgesehen. 

## **5.5 TR-ESOR-S.6 (ArchiSafe-Modul – ArchiSig-Modul)** 

Dieser Abschnitt beschreibt, wie die in Abbildung 2 dargestellte Schnittstelle TR-S.6 auf Basis der auch dem eCard-API-Framework (BSI TR-03112) zu Grunde liegenden Basistypen aus **[OASIS-DSS]** umgesetzt werden kann. 

Die in Abbildung 2 dargestellte Schnittstelle TR-S.6 umfasst die folgenden Funktionen: 

- Beweiswerterhaltende Archivierung elektronischer Daten (ArchiveSubmissionRequest / ArchiveSubmissionResponse) 

- Ergänzen einer neuen Version eines Archivdatenobjektes (ArchiveUpdateRequest / ArchiveUpdateResponse) 

- Rückgabe technischer Beweisdaten (ArchiveEvidenceRequest / ArchiveEvidenceResponse) 

## **5.5.1 Beweiswerterhaltende Archivierung elektronischer Daten** 

Für die beweiswerterhaltende Archivierung elektronischer Daten ist der Funktionsaufruf ArchiveSubmissionRequest und die Antwort  ArchiveSubmissionResponse gemäß Abschnitt 3.1 vorgesehen. 

## **5.5.2 Ergänzen einer neuen Version eines Archivdatenobjektes** 

Für  das  Ergänzen  einer  neuen  Version  eines  Archivdatenobjektes  ist  der  Funktionsaufruf ArchiveUpdateRequest und  die  Antwort   ArchiveUpdateResponse gemäß  Abschnitt 3.2 vorgesehen. 

## **5.5.3 Rückgabe technischer Beweisdaten** 

Für die Rückgabe technischer Beweisdaten ist der Funktionsaufruf  ArchiveEvidenceRequest und die Antwort ArchiveEvidenceResponse gemäß Abschnitt 3.4 vorgesehen. 

Bundesamt für Sicherheit in der Informationstechnik 

50 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

## **6. Fehlercodes** 

Die vorliegende Spezifikation nutzt die folgenden generellen Fehlercodes aus **[eCard-1]** : 

- .../resultmajor#ok 

- .../resultmajor#error 

- .../resultmajor#warning 

- .../resultminor/al/common#noPermission 

- .../resultminor/al/common#internalError 

- .../resultminor/al/common#parameterError 

Darüber hinaus werden zusätzlich die folgenden Fehlercodes definiert: 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0051-10.png)


**----- Start of picture text -----**<br>
Fehlercode Beschreibung<br>.../resultminor/arl/DXAIP_NOK Die  Syntax  des  beim ArchiveUpdateRequest<br>übergebenen Delta-XAIP-Elements ist nicht korrekt.<br>.../resultminor/arl/DXAIP_NOK_AOID Die AOID in  dem beim ArchiveUpdateRequest<br>übergebenen Delta-XAIP ist nicht bekannt.<br>.../resultminor/arl/DXAIP_NOK_EXPIRED Das  beim ArchiveUpdateRequest übergebene<br>Delta-XAIP-Element kann nicht abgelegt werden, da die<br>Aufbewahrungsfrist abgelaufen ist.<br>.../resultminor/arl/DXAIP_NOK_SUBMTIME Die beim ArchiveUpdateRequest im übergebenen<br>Delta-XAIP-Element  angegebene submissionTime<br>ist nicht korrekt, da sie in der Zukunft liegt.<br>.../resultminor/arl/DXAIP_NOK_SIG Das  beim ArchiveUpdateRequest übergebene<br>Delta-XAIP-Element  enthält  zumindest  eine  ungültige<br>digitale Signatur.<br>.../resultminor/arl/DXAIP_NOK_ER Das  beim ArchiveUpdateRequest übergebene<br>Delta-XAIP-Element  enthält  zumindendest  einen<br>ungültigen Evidence Record.<br>.../resultminor/arl/DXAIP_NOK_ID Die  beim ArchiveUpdateRequest in  einem<br>placeHolder-Element übebergebene XML-ID ist im<br>bereits abgelegten XAIP-Elemen nicht vorhanden.<br>.../resultminor/arl/DXAIP_NOK_Version Die beim ArchiveUpdateRequest im<br>prevVersion-Element  übergebene  Version  ist  nicht<br>die aktuellste Version.<br>.../resultminor/arl/existingAOID Die im Rahmen des ArchiveSubmissionRequest<br>übergebene AOID existiert bereits.<br>.../resultminor/arl/existingPackage Bei der ArchiveUpdateRequest-Funktion wird ein<br>InfoWarning Delta-XAIP-Element übergeben, das ein<br>packageInfo-Element  enthält.  Da  im  vorher<br>existierenden XAIP bereits das packageInfo-Element<br>-<br>belegt  war,  wird  das  übergebene packageInfo<br>Element  ignoriert  und  eine  entsprechende  Warnung<br>zurückgeliefert.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

51 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 


![](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2/BSI_TR_03125_Anlage_E_V1_2_2.pdf-0052-01.png)


**----- Start of picture text -----**<br>
Fehlercode Beschreibung<br>.../resultminor/arl/lowSpaceWarning Diese  Warnung  gibt  an,  dass  der  verfügbare<br>Speicherplatz einen kritischen Wert unterschritten hat.<br>.../resultminor/arl/missingReasonOf Da  beim ArchiveDeletionRequest kein<br>Deletion ReasonOfDeletion-Element übergeben wurde, muss<br>der Löschvorgang abgewiesen werden.<br>.../resultminor/arl/noSpaceError Diese Fehlermeldung gibt an, dass kein Speicherplatz<br>verfügbar war und deshalb das Archivdatenobjekt nicht<br>abgelegt werden konnte.<br>.../resultminor/arl/notSupported Diese  Fehlermeldung  gibt  an,  dass  eine  angeforderte<br>Funktion, ein angefordertes Format oder ein übergebener<br>optionaler Eingabeparameter nicht unterstützt wird.<br>.../resultminor/arl/requestOnlyPartly Diese Warnung  gibt an, dass nicht alle angeforderten<br>SuccessfulWarning Daten zurückgeliefert werden konnten.<br>.../resultminor/arl/unknownArchiveDataType Es  wird  ein  binäres  Datenobjekt  mit  einem  nicht<br>unterstützten Datenformat übergeben.<br>.../resultminor/arl/unknownLocation Die  im ArchiveDataRequest angegebene<br>DataLocation ist nicht vorhanden bzw. fehlerhaft.<br>.../resultminor/arl/unknownAOID Die übergebene AOID existiert nicht.<br>.../resultminor/arl/unknownVersionID Die  übergebene VersionID ist  im  entsprechenden<br>XAIP nicht bekannt.<br>.../resultminor/arl/XAIP_NOK Die Syntax des übergebenen AIP-Containers (d.h. XAIP,<br>LXAIP, ASiC-AIP) ist nicht korrekt.<br>.../resultminor/arl/XAIP_NOK_ER Der  übergebene  AIP-Container  (d.h.  XAIP,  LXAIP,<br>ASiC-AIP) enthält zumindest einen ungültigen Evidence<br>Record.<br>.../resultminor/arl/XAIP_NOK_EXPIRED Der  übergebene  AIP-Container  (d.h.  XAIP,  LXAIP,<br>ASiC-AIP) kann  nicht  abgelegt  werden,  da  die<br>Aufbewahrungsfrist abgelaufen ist.<br>.../resultminor/arl/XAIP_NOK_SIG Der  übergebene  AIP-Container  (d.h.  XAIP,  LXAIP,<br>ASiC-AIP) enthält zumindest eine ungültige Signatur.<br>.../resultminor/arl/XAIP_NOK_SUBMTIME Die im übergebenen AIP-Container (d.h. XAIP, LXAIP,<br>ASiC-AIP)  angegebene submissionTime ist  nicht<br>korrekt, da sie in der Zukunft liegt.<br>.../resultminor/arl/noDataAccessWarning Der  Zugriff  auf  die  in  einem  übergebenen  LXAIP<br>referenzierten Daten ist nicht möglich.<br>.. /resultminor/arl/unknownPOFormat Der angeforderte POFormat- Typ ist nicht bekannt.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

52 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

## **7. Spezifikation einer Webservice-basierten Schnittstelle** 

Die Spezifikation der Webservice-basierten Schnittstelle besteht aus zwei Bestandteilen: Zunächst werden die Aufruf- und Rückgabeparameter als XML-Schema **[XSD]** spezifiziert (vgl. Abschnitt 7.1). Darauf aufbauend wird in einem zweiten Schritt eine Webservice-Spezifikation gemäß **[WSDL]** entwickelt. 

Abschnitt  7.2 enthält die Webservice-Spezifikation der Schnittstelle TR-S.4 (vgl. Abschnitt  3). Die internen Schnittstellen der TR-ESOR-Middleware können bei Bedarf leicht daraus abgeleitet werden, indem nur die benötigte Teilmenge der Funktionen genutzt wird. 

Die Unterstützung des optimierten Nachrichtenübertragungsmechanismus „SOAP Message Transmission  Optimization  Mechanism  (MTOM)“[15] kann  durch  den  Import  des  geringfügig angepassten XAIP-Schema (tr-esor-xaip-v1.2+xmlmime.xsd) erfolgen. 

## **7.1 Spezifikation der Aufruf- und Rückgabeparameter als XML-Schema** 

<?xml version="1.0" encoding="UTF-8"?> 

<schema xmlns="http://www.w3.org/2001/XMLSchema" xmlns:tr="http://www.bsi.bund.de/tr-esor/api/1.2" xmlns:xaip="http://www.bsi.bund.de/tr-esor/xaip/1.2" xmlns:ers="urn:ietf:params:xml:ns:ers" xmlns:ec="http://www.bsi.bund.de/ecard/api/1.1" xmlns:dss="urn:oasis:names:tc:dss:1.0:core:schema" xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion" targetNamespace="http://www.bsi.bund.de/tr-esor/api/1.2" elementFormDefault="qualified" attributeFormDefault="unqualified"> 

<!-- ======================================= --> <!-- Version 1.2 (+xmlmime) vom 20.12.2018   --> <!-- ======================================= --> <import namespace="http://www.bsi.bund.de/tr-esor/xaip/1.2" schemaLocation="tr-esor-xaip-v1.2+xmlmime.xsd" /> <import namespace="urn:oasis:names:tc:dss:1.0:core:schema" schemaLocation="./deps/oasis-dss-core-schema-v1.0-os.xsd" /> <import namespace="urn:ietf:params:xml:ns:ers" schemaLocation="./deps/xml-ers-rfc6283.xsd" /> 

<import namespace="http://www.bsi.bund.de/ecard/api/1.1" schemaLocation="./deps/eCard.xsd" /> <import namespace="urn:oasis:names:tc:SAML:2.0:assertion" schemaLocation="./deps/saml-schema-assertion-2.0.xsd" /> <!-- =================================== --> 

> 15 Siehe https://www.w3.org/TR/soap12-mtom/ . 

Bundesamt für Sicherheit in der Informationstechnik 

53 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

<!--     Uebergreifende Definitionen     --> <!-- =================================== --> <complexType name="RequestType"> <complexContent> <restriction base="dss:RequestBaseType"> <sequence> <element ref="dss:OptionalInputs" maxOccurs="1" minOccurs="0" /> </sequence> </restriction> </complexContent> </complexType> <complexType name="ResponseType"> <complexContent> <restriction base="dss:ResponseBaseType"> <sequence> <element ref="dss:Result" /> <element ref="dss:OptionalOutputs" maxOccurs="1" minOccurs="0" /> </sequence> </restriction> </complexContent> </complexType> <element name="AOID" type="string"/> <!-- ================================ --> <!--    ArchiveSubmissionRequest      --> <!-- ================================ --> <complexType name="ArchiveDataType"> <complexContent> <extension base="anyType"> <attribute name="Type" type="anyURI" /> </extension> </complexContent> </complexType> <element name="ImportEvidence" type="tr:ImportEvidenceType"/> <complexType name="ImportEvidenceType"> <choice> 

Bundesamt für Sicherheit in der Informationstechnik 

54 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

<element ref="xaip:evidenceRecord" maxOccurs="unbounded" minOccurs="1" /> <element name="CredentialID" type="string" maxOccurs="unbounded" minOccurs="1" /> </choice> </complexType> 

<element name="ArchiveSubmissionRequest"> <complexType> <complexContent> <extension base="tr:RequestType"> <choice> <element ref="xaip:XAIP"></element> <element name="ArchiveData" type="tr:ArchiveDataType"></element> </choice> </extension> </complexContent> </complexType> </element> <element name="ArchiveSubmissionResponse"> <complexType> <complexContent> <extension base="tr:ResponseType"> <sequence> <element name="AOID" type="string" maxOccurs="1" minOccurs="0"> </element> </sequence> </extension> </complexContent> </complexType> </element> <!-- ========================== --> <!--    ArchiveUpdateRequest    --> <!-- ========================== --> 

<element name="ArchiveUpdateRequest"> <complexType> <complexContent> <extension base="tr:RequestType"> 

Bundesamt für Sicherheit in der Informationstechnik 

55 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

<sequence> <element ref="xaip:DXAIP"></element> </sequence> </extension> </complexContent> </complexType> </element> 

<element name="ArchiveUpdateResponse"> <complexType> <complexContent> <extension base="tr:ResponseType"> <sequence> 

<element name="VersionID" type="string" 

maxOccurs="1" minOccurs="0"></element> 

</sequence> 

</extension> 

</complexContent> 

</complexType> 

</element> 

<!-- ================================ --> <!--    ArchiveRetrievalRequest       --> <!-- ================================ --> 

<element name="ArchiveRetrievalRequest"> <complexType> <complexContent> <extension base="tr:RequestType"> <sequence> <element name="AOID" type="string" /> <element name="VersionID" type="string" 

maxOccurs="unbounded" minOccurs="0"></element> 

</sequence> 

</extension> </complexContent> </complexType> </element> 

<element name="IncludeERS" type="anyURI" /> 

<element name="ArchiveRetrievalResponse"> <complexType> <complexContent> <extension base="tr:ResponseType"> 

Bundesamt für Sicherheit in der Informationstechnik 

56 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

<sequence> <element ref="xaip:XAIP" maxOccurs="1" minOccurs="0"/> </sequence> </extension> </complexContent> </complexType> </element> 

<!-- ================================ --> <!--    ArchiveEvidenceRequest       --> <!-- ================================ --> <element name="ArchiveEvidenceRequest"> <complexType> <complexContent> <extension base="tr:RequestType"> <sequence> <element name="AOID" "string"></element>></element>element>> <element name="VersionID" type="string" 

type="string"></element>></element>element>> 

maxOccurs="unbounded" minOccurs="0"></element> 

</sequence> </extension> </complexContent> </complexType> </element> 

<element name="ERSFormat" type="anyURI" /> 

<element name="ArchiveEvidenceResponse"> <complexType> <complexContent> <extension base="tr:ResponseType"> <sequence> <element ref="xaip:evidenceRecord" 

maxOccurs="unbounded" 

minOccurs="0"> </element> </sequence> </extension> </complexContent> </complexType> 

</element> 

Bundesamt für Sicherheit in der Informationstechnik 

57 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

<!-- ================================ --> <!--    ArchiveDeletionRequest      --> <!-- ================================ --> <element name="ArchiveDeletionRequest"> <complexType> <complexContent> <extension base="tr:RequestType"> <sequence> <element name="AOID" type="string"></element> </sequence> </extension> </complexContent> </complexType> </element> <element name="ReasonOfDeletion"> <complexType> <sequence> <element name="RequestorName" type="saml:NameIDType" /> <element name="RequestInfo" type="string" /> </sequence> </complexType> </element> 

<element name="ArchiveDeletionResponse" type="tr:ResponseType"/> 

<!-- ========================== --> <!--    ArchiveDataRequest      --> <!-- ========================== --> <element name="ArchiveDataRequest"> <complexType> <complexContent> <extension base="tr:RequestType"> <sequence> <element name="AOID" "string"></element>></element>element>> <element ref="tr:DataLocation" maxOccurs="unbounded" ="1" />"1" />/> </sequence> </extension> </complexContent> </complexType> 

type="string"></element>></element>element>> 

minOccurs="1" />"1" />/> 

Bundesamt für Sicherheit in der Informationstechnik 

58 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

</element> 

<element name="DataLocation"> <complexType> <complexContent> <extension base="anyType"> <attribute name="Type" type="anyURI" /> </extension> </complexContent> </complexType> </element> <element name="ArchiveDataResponse"> <complexType> <complexContent> <extension base="tr:ResponseType"> <sequence> <element name="XAIPData" maxOccurs="unbounded" ="1">"1">> <complexType> <sequence> <element "dss:Result" maxOccurs="1" minOccurs="1" />maxOccurs="1" minOccurs="1" />="1" minOccurs="1" />"1" minOccurs="1" />minOccurs="1" />="1" />"1" />/> <element "tr:DataLocation" />/> <element name="Value" "anyType" maxOccurs="1" minOccurs="0" />maxOccurs="1" minOccurs="0" />="1" minOccurs="0" />"1" minOccurs="0" />minOccurs="0" />="0" />"0" />/> </sequence> </complexType> </element> </sequence> </extension> </complexContent> </complexType> 

minOccurs="1">"1">> 

ref="dss:Result" maxOccurs="1" minOccurs="1" />maxOccurs="1" minOccurs="1" />="1" minOccurs="1" />"1" minOccurs="1" />minOccurs="1" />="1" />"1" />/> ref="tr:DataLocation" />/> type="anyType" maxOccurs="1" minOccurs="0" />maxOccurs="1" minOccurs="0" />="1" minOccurs="0" />"1" minOccurs="0" />minOccurs="0" />="0" />"0" />/> 

</element> 

</schema> 

## **7.2 WSDL-Spezifikation der Schnittstelle TR-ESOR-S.4** 

<?xml version="1.0" encoding="UTF-8"?> 

<wsdl:definitions targetNamespace="http://www.bsi.bund.de/tr-esor/api/1.2" xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:dss="urn:oasis:names:tc:dss:1.0:core:schema" xmlns:tr="http://www.bsi.bund.de/tr-esor/api/1.2" 

Bundesamt für Sicherheit in der Informationstechnik 

59 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

> <!--============================================================--> <!-- Version 1.2 (+xmlmime) vom 20.12.2018 --> <!--============================================================--> 

<!-- =================== --> <!-- Definition of types --> <!-- (only include XSDs) --> <!-- =================== --> 

<wsdl:types> <xsd:schema targetNamespace="http://www.bsi.bund.de/tresor/api/1.2" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xaip="http://www.bsi.bund.de/tr-esor/xaip/1.2" xmlns:dss="urn:oasis:names:tc:dss:1.0:core:schema" elementFormDefault="qualified"> <xsd:include schemaLocation="tr-esor-interfacesv1.2+xmlmime.xsd" /> 

</xsd:schema> </wsdl:types> 

<!-- ====================== --> <!-- Definition of messages --> <!-- ====================== --> 

<!-- ArchiveSubmissionRequest --> <wsdl:message name="ArchiveSubmissionRequest"> <wsdl:part name="parameters" element="tr:ArchiveSubmissionRequest" /> </wsdl:message> <wsdl:message name="ArchiveSubmissionResponse"> <wsdl:part name="parameters" element="tr:ArchiveSubmissionResponse"/> </wsdl:message> <!-- ArchiveUpdateRequest --> <wsdl:message name="ArchiveUpdateRequest"> <wsdl:part name="parameters" element="tr:ArchiveUpdateRequest" /> </wsdl:message> <wsdl:message name="ArchiveUpdateResponse"> 

Bundesamt für Sicherheit in der Informationstechnik 

60 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

<wsdl:part name="parameters" element="tr:ArchiveUpdateResponse"/> 

</wsdl:message> 

<!-- ArchiveRetrievalRequest --> 

<wsdl:message name="ArchiveRetrievalRequest"> 

<wsdl:part name="parameters" element="tr:ArchiveRetrievalRequest" /> 

</wsdl:message> 

<wsdl:message name="ArchiveRetrievalResponse"> 

<wsdl:part name="parameters" element="tr:ArchiveRetrievalResponse" /> </wsdl:message> 

<!-- ArchiveEvidenceRequest --> 

<wsdl:message name="ArchiveEvidenceRequest"> 

<wsdl:part name="parameters" element="tr:ArchiveEvidenceRequest" /> </wsdl:message> 

<wsdl:message name="ArchiveEvidenceResponse"> 

<wsdl:part name="parameters" element="tr:ArchiveEvidenceResponse" /> </wsdl:message> 

<!-- ArchiveDeletionRequest --> 

<wsdl:message name="ArchiveDeletionRequest"> <wsdl:part name="parameters" element="tr:ArchiveDeletionRequest" /> </wsdl:message> <wsdl:message name="ArchiveDeletionResponse"> <wsdl:part name="parameters" element="tr:ArchiveDeletionResponse" /> </wsdl:message> 

<!-- ArchiveDataRequest --> 

<wsdl:message name="ArchiveDataRequest"> <wsdl:part name="parameters" element="tr:ArchiveDataRequest" /> </wsdl:message> <wsdl:message name="ArchiveDataResponse"> <wsdl:part name="parameters" element="tr:ArchiveDataResponse" /> </wsdl:message> 

Bundesamt für Sicherheit in der Informationstechnik 

61 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

<!-- VerifyRequest --> 

<wsdl:message name="VerifyRequest"> <wsdl:part name="parameters" element="dss:VerifyRequest" /> </wsdl:message> <wsdl:message name="VerifyResponse"> <wsdl:part name="parameters" element="dss:VerifyResponse"/> </wsdl:message> 

<!-- ====================== --> <!-- Definition of portType --> <!-- ====================== --> 

<wsdl:portType name="S4"> 

<wsdl:operation name="ArchiveSubmission"> 

<wsdl:input message="tr:ArchiveSubmissionRequest" /> 

<wsdl:output message="tr:ArchiveSubmissionResponse" /> </wsdl:operation> 

<wsdl:operation name="ArchiveUpdate"> 

<wsdl:input message="tr:ArchiveUpdateRequest" /> 

<wsdl:output message="tr:ArchiveUpdateResponse" /> </wsdl:operation> 

<wsdl:operation name="ArchiveRetrieval"> 

<wsdl:input message="tr:ArchiveRetrievalRequest" /> <wsdl:output message="tr:ArchiveRetrievalResponse" /> </wsdl:operation> 

<wsdl:operation name="ArchiveEvidence"> 

<wsdl:input message="tr:ArchiveEvidenceRequest" /> 

<wsdl:output message="tr:ArchiveEvidenceResponse" /> </wsdl:operation> 

<wsdl:operation name="ArchiveDeletion"> <wsdl:input message="tr:ArchiveDeletionRequest" /> <wsdl:output message="tr:ArchiveDeletionResponse" /> </wsdl:operation> 

<wsdl:operation name="ArchiveData"> <wsdl:input message="tr:ArchiveDataRequest" /> <wsdl:output message="tr:ArchiveDataResponse" /> </wsdl:operation> 

<wsdl:operation name="Verify"> <wsdl:input message="tr:VerifyRequest" /> <wsdl:output message="tr:VerifyResponse" /> </wsdl:operation> 

</wsdl:portType> 

Bundesamt für Sicherheit in der Informationstechnik 

62 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

<!-- ===================== --> <!-- Definition of Binding --> <!-- ===================== --> <wsdl:binding name="S4" type="tr:S4"> <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http" /> <wsdl:operation name="ArchiveSubmission"> <soap:operation soapAction="http://www.bsi.bund.de/tresor/ArchiveSubmission" /> <wsdl:input> <soap:body use="literal" /> </wsdl:input> <wsdl:output> <soap:body use="literal" /> </wsdl:output> </wsdl:operation> <wsdl:operation name="ArchiveUpdate"> <soap:operation soapAction="http://www.bsi.bund.de/tresor/ArchiveUpdate" /> <wsdl:input> <soap:body use="literal" /> </wsdl:input> <wsdl:output> <soap:body use="literal" /> </wsdl:output> </wsdl:operation> <wsdl:operation name="ArchiveRetrieval"> <soap:operation soapAction="http://www.bsi.bund.de/tresor/ArchiveRetrieval" /> <wsdl:input> <soap:body use="literal" /> </wsdl:input> <wsdl:output> <soap:body use="literal" /> </wsdl:output> </wsdl:operation> <wsdl:operation name="ArchiveEvidence"> <soap:operation soapAction="http://www.bsi.bund.de/tresor/ArchiveEvidence" /> <wsdl:input> <soap:body use="literal" /> </wsdl:input> <wsdl:output> <soap:body use="literal" /> 

Bundesamt für Sicherheit in der Informationstechnik 

63 

BSI TR-ESOR-E: Konkretisierung der Schnittstellen auf Basis des eCard-API-Frameworks 

</wsdl:output> </wsdl:operation> <wsdl:operation name="ArchiveDeletion"> <soap:operation soapAction="http://www.bsi.bund.de/tresor/ArchiveDeletion" /> <wsdl:input> <soap:body use="literal" /> </wsdl:input> <wsdl:output> <soap:body use="literal" /> </wsdl:output> </wsdl:operation> <wsdl:operation name="ArchiveData"> <soap:operation soapAction="http://www.bsi.bund.de/tresor/ArchiveData" /> <wsdl:input> <soap:body use="literal" /> </wsdl:input> <wsdl:output> <soap:body use="literal" /> </wsdl:output> </wsdl:operation> <wsdl:operation name="Verify"> <soap:operation soapAction="http://www.bsi.bund.de/tr-esor/Verify" /> <wsdl:input> <soap:body use="literal" /> </wsdl:input> <wsdl:output> <soap:body use="literal" /> </wsdl:output> </wsdl:operation> </wsdl:binding> 

<!-- Definition of Support-Service --> 

<wsdl:service name="S4"> <wsdl:port name="S4" binding="tr:S4"> <soap:address location="http://127.0.0.1:18080" /> </wsdl:port> </wsdl:service> </wsdl:definitions> 

Bundesamt für Sicherheit in der Informationstechnik 

64 


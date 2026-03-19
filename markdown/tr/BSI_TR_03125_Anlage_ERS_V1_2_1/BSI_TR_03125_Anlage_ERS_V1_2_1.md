
![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0001-00.png)


BSI Technische Richtlinie 03125 Beweiswerterhaltung kryptographisch signierter Dokumente **Anlage TR-ESOR-ERS: Profilierung der Evidence Records gemäß RFC4998 und RFC6283 (Konformitätsstufe 2 - technische Konformität)** 

Bezeichnung Profilierung derEvidence Records gemäß RFC 4998 und RFC 6283 (Konformitätsstufe 2 - technische Konformität) Kürzel BSI TR-ESOR-ERS Version 1.2.1 (auf Basis der eIDAS-Verordnung) Datum 15.03.2018 

Beweiswerterhaltung kryptographisch signierter Dokumente (TR-ESOR) 

BSI TR 03125 

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn Tel.: +49 228 99 9582-0 E-Mail:  tresor@bsi.bund.de Internet: https://www.bsi.bund.de © Bundesamt für Sicherheit in der Informationstechnik 2018 

Bundesamt für Sicherheit in der Informationstechnik 

Profilierung der  Evidence Records gemäß RFC 4998 und RFC 6283 

## **Inhaltsverzeichnis** 

|**Inhaltsverzeichnis**||
|---|---|
|1.  Einführung|5|
|2.  Überblick|7|
|3.  Profilierung des Evidence Record (normativ)|8|
|3.1.  Einleitung.......................................................................................................................................8||
|3.2.  Definition des Verpflichtungsgrades...............................................................................................8||
|3.3.  Strukturen eines Evidence Records gem. dem Basis-ERS-Profil....................................................9||
|3.3.1.  Typ EvidenceRecord|9|
|3.4.  Regeln für den_TimeStampToken_im ASN.1-Format.....................................................................11||
|3.4.1.  Typ_TimeStampToken_|12|
|3.4.2.  Typ_SignedData_|12|
|3.4.3.  Typ_SignerInfo_|17|
|3.4.4.  Signierte Attribute (signed attributes)|19|
|3.5.  Erzeugen eines Evidence Records................................................................................................21||
|3.5.1.  Behandlung des Archivzeitstempels|21|
|3.6.  Verifikation eines Evidence Records............................................................................................22||
|4.  Anhang A: Profil-Überblick (normativ)|24|
|4.1.  Basis-ERS-Profil – Überblick.......................................................................................................24||
|5.  Anhang B: Anforderungen an die kryptographischen Algorithmen und Parameter (normativ)|26|
|5.1.  Erstellung eines Evidence Records gem. Basis-ERS-Profil..........................................................26||
|5.1.1.  Hashalgorithmen|26|
|5.1.2.  Digitale Signaturalgorithmen|26|
|5.2.  Verifikation eines Evidence Records............................................................................................26||
|5.2.1.  Hashalgorithmen|27|
|5.2.2.  Digitale Signaturalgorithmen|27|
|5.2.3.  ESSCertIDv2 und ESSCertID|28|
|6.  Anhang C: Weitere ERS-Profile (informativ)|29|
|6.1.  Struktur eines Evidence Records gem. dem Basis-XERS-Profil...................................................29||
|6.2.  Zeitstempelerneuerung mithilfe eines ATSv3 (nur CMS-basiert).................................................31||
|6.2.1.  Verwendung von ATSv3|31|
|6.2.2.  Attribut_archive-time-stamp-v3_(_ATSv3_)|32|
|6.2.3.  Attribut_ats-hash-index_|33|
|7.  Anhang D Syntaxdefinitionen (informativ)|36|
|7.1.  Evidence Records gem. [RFC4998]..............................................................................................36||
|7.1.1.  Element_EvidenceRecord_gem. [RFC4998]|36|
|7.1.2.  Element_ArchiveTimeStamp_gem. [RFC4998]|36|
|7.2.  Evidence Records gem. [RFC6283]..............................................................................................36||
|7.2.1.  Element_<EvidenceRecord>_gem. [RFC6283]|36|
|7.2.2.  Element_<HashTree>_gem. [RFC6283]|37|
|7.2.3.  Element_<TimeStamp>_gem. [RFC6283]|37|



Bundesamt für Sicherheit in der Informationstechnik 

3 

Profilierung der Evidence Records gemäß RFC 4998 und RFC 6283 

**Abbildungsverzeichnis** Abbildung 1: Schematische Darstellung der IT-Referenzarchitektur......................................................6 Abbildung 2: Zeitstempelerneuerung mithilfe eines ATSv3.................................................................32 Abbildung 3: Zusammenhang digitale CAdES Signatur, ATSv3 und ats-hash-index...........................34 

## **Tabellenverzeichnis** 

Tabelle 1: Felder des Typs EvidenceRecord.........................................................................................10 Tabelle 2: Aufbau des Typs ArchiveTimeStampSequence....................................................................10 Tabelle 3: Aufbau des Typs ArchiveTimeStampChain..........................................................................10 Tabelle 4: Felder des Typs ArchiveTimeStamp.....................................................................................11 Tabelle 5: Aufbau des Typs PartialHashtree..........................................................................................11 Tabelle 6: Felder des Typs ContentInfo eines TimeStampTokens.........................................................12 Tabelle 7: Felder des Typs SignedData.................................................................................................14 Tabelle 8: Felder des Typs EncapsulatedContentInfo...........................................................................15 Tabelle 9: Aufbau des Typs CertificateSet (gem. [RFC5652], Kap. 10.2.3)..........................................15 Tabelle 10: Aufbau des Typs CertificateChoices (gem. [RFC5652], Kap. 10.2.2)................................16 Tabelle 11: Aufbau des Typs RevocationInfoChoices (gem. [RFC5652], Kap. 10.2.1)........................16 Tabelle 12: Aufbau des Typs RevocationInfoChoices (gem. [RFC5652], Kap. 10.2.1)........................17 Tabelle 13: Felder des Typs SignerInfo.................................................................................................18 Tabelle 14: Felder des Typs Attribute gem. [RFC5652]........................................................................18 Tabelle 15: Auflistung der relevanten signierten Attribute (Zeitstempel gem. [RFC3161])..................20 Tabelle 16: Attribut content-type gem. [RFC5652]...............................................................................20 Tabelle 17: Attribut message-digest gem. [RFC5652]..........................................................................20 Tabelle 18: Attribut signing-certificate-v2 gem. [RFC5035]................................................................21 Tabelle 19: Überblick über den Aufbau eines Evidence Records gem. dem Basis-ERS-Profil.............24 Tabelle 20: Überblick über den Aufbau eines Zeitstempels gem. dem Basis-ERS-Profil.....................25 Tabelle 21: Aktuell zugelassene Hashalgorithmen für die Erzeugung technische Beweisdaten (Evidence Records) (Stand 30.09.2014)...............................................................................................26 Tabelle 22: Aktuell zusätzlich erforderliche Hashalgorithmen für die Verifikation eines Evidence Records (Stand 01.08.2014).................................................................................................................27 Tabelle 23: Weitere aktuell zu unterstützende digitale Signatur-Suites bei der Prüfung eines Evidence Records (Stand: 01.08.2014)................................................................................................................28 Tabelle 24: Der Typ EvidenceRecordType gem. [RFC6283] und Basis-XERS-Profil..........................29 Tabelle 25: Der Typ ArchiveTimeStampChainType gem. [RFC6283] und Basis-XERS-Profil............30 Tabelle 26: Der Typ ArchiveTimeStampType gem. [RFC6283] und Basis-XERS-Profil.....................31 Tabelle 27: Der Typ TimeStampType gem. [RFC6283] und Basis-XERS-Profil..................................31 Tabelle 28: Attribut archive-time-stamp-v3 gem. [ETSI 101733] Kap. 6.4.3.......................................33 Tabelle 29: Aufbau von message imprint eines ATSv3.........................................................................33 Tabelle 30: Das Attribut ats-hash-index................................................................................................34 Tabelle 31: Felder des Typs ATSHashIndex..........................................................................................34 

Bundesamt für Sicherheit in der Informationstechnik 

4 

Profilierungder Evidence Records gemäß RFC 4998 und RFC6283 

## **1. Einführung** 

Ziel der Technischen Richtlinie „Beweiswerterhaltung kryptographisch signierter Dokumente“ ist die Spezifikation sicherheitstechnischer Anforderungen für den langfristigen Beweiswerterhalt  von  kryptographisch  signierten  elektronischen  Dokumenten  und  Daten nebst zugehörigen elektronischen Verwaltungsdaten (Metadaten). 

Eine  für  diese  Zwecke  definierte  Middleware  (TR-ESOR-Middleware)  im  Sinn  dieser Richtlinie umfasst alle diejenigen Module ( **M** ) und Schnittstellen ( **S)** , die zur Sicherung und zum Erhalt der Authentizität und zum Nachweis der Integrität der aufbewahrten Dokumente und Daten eingesetzt werden. 

Die im Hauptdokument dieser Technischen Richtlinie vorgestellte Referenzarchitektur besteht aus den nachfolgend beschriebenen funktionalen und logischen Einheiten: 

- der Eingangs-Schnittstelle S.4 der  TR-ESOR-Middleware, die dazu dient, die  TRESOR-Middleware in die bestehende IT- und Infrastrukturlandschaft einzubetten; 

- dem „ArchiSafe-Modul“ (vgl. **[TR-ESOR-M.1]** ), welches den Informationsfluss in der Middleware regelt, die Sicherheitsanforderungen an die Schnittstellen zu den ITAnwendungen  umsetzt  und für eine  Entkopplung  von Anwendungssystemen  und ECM/Langzeitspeicher sorgt; 

- dem „Krypto-Modul“ (vgl. **[TR-ESOR-M.2]** ) nebst den zugehörigen Schnittstellen S.1 und S.3, das alle erforderlichen Funktionen zur Berechnung von Hashwerten, Prüfung elektronischer Signaturen bzw. Siegel bzw. Zeitstempel, zur Nachprüfung elektronischer  Zertifikate  und  zum  Einholen qualifizierter Zeitstempel sowie (optional) elektronischer Signaturen bzw. Siegel für die Middleware zur Verfügung stellt. Darüber hinaus kann es Funktionen zur Ver- und Entschlüsselung von Daten und Dokumenten zur Verfügung stellen; 

- dem „ArchiSig-Modul“ (vgl. **[TR-ESOR-M.3]** ) mit der Schnittstelle S.6, dass die erforderlichen Funktionen  für  die  Beweiswerterhaltung der  digital signierten Unterlagen bereitstellt; 

- einem  ECM/Langzeitspeicher mit den Schnittstellen S.2 und S.5, der die physische Archivierung/Aufbewahrung  und  auch  das  Speichern  der  beweiswerterhaltenden Zusatzdaten übernimmt. 

   - _Dieser  ECM/Langzeitspeicher ist nicht mehr direkt Teil der Technischen Richtlinie, gleichwohl  werden  über  die  beiden  Schnittstellen,  die  noch  Teil  der  TR-ESORMiddleware sind, Anforderungen daran gestellt._ 

   - _Ebenso wenig ist die Applikationsschicht, die auch einen XML-Adapter enthalten kann, direkter Teil der Technischen Richtlinie, auch wenn dieser XML-Adapter als Teil einer Middleware implementiert werden kann._ 

Die in Abbildung 1 dargestellte  IT-Referenzarchitektur  orientiert  sich an der ArchiSafe[1 ] Referenzarchitektur und soll die logische (funktionale) Interoperabilität künftiger Produkte mit den Zielen und Anforderungen der Technischen Richtlinie ermöglichen und unterstützen. 

1 

Siehe dazu http://www.archisafe.de 

Bundesamt für Sicherheit in der Informationstechnik 

5 

Profilierung der Evidence Records gemäß RFC 4998 und RFC 6283 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0006-01.png)


## **Abbildung 1: Schematische Darstellung der IT-Referenzarchitektur** 

Diese Technische Richtlinie ist modular aufgebaut und spezifiziert in einzelnen Anlagen zum Hauptdokument die funktionalen und sicherheitstechnischen Anforderungen an die erforderlichen IT-Komponenten und Schnittstellen der TR-ESOR-Middleware. Die Spezifikationen sind strikt plattform-, produkt-, und herstellerunabhängig. 

Das vorliegende Dokument trägt die Bezeichnung „Profilierungder Evidence Records gemäß RFC 4998/6283“ (auch kurz „Anlage TR-ESOR-ERS“ bzw. nur „TR-ESOR-ERS“ genannt) und  beschreibt  die  vorgeschriebene  Belegung  der  Felder  der  gemäß **[RFC4998]** und **[RFC6283]** aufgebauten Evidence Records. 

Bundesamt für Sicherheit in der Informationstechnik 

6 

Profilierungder Evidence Records gemäß RFC 4998 und RFC6283 

## **2. Überblick** 

Die TR 03125 TR-ESOR stellt ein Konzept für die Beweiswerterhaltung elektronischer Unterlagen durch den Einsatz kryptographisch-signierter Daten und Dokumente bereit. Wesentliche Grundlagen dieses Konzeptes sind daher u.a. die Erzeugung, Prüfung und Rückgabe technischer Beweisdaten als informationstechnische Umsetzung der Evidence Record[2 ] Syntax (kurz: ERS) Standards der IETF (vgl. **[RFC4998]** bzw. **[RFC6283]**[3] ) sowie die Prüfung und ggf. Erzeugung von beweisrelevanten Daten, z. B. Zeitstempel, elektronischer Signaturen, Siegel, Zertifikaten, Sperrinformationen, etc. 

In den folgenden Abschnitten befindet sich die Darstellung der Profilierungen des Evidence Records und der darin enthaltenen beweisrelevanten Daten, insbesondere auch in Bezug auf die  Zeitstempelsignatur  bzw.  -siegel,  mit  dem **Ziel  der  nachhaltigen  Erhaltung  des Beweiswerts und der technischen Konformität und Interoperabilität** zwischen unterschiedlichen TR-ESOR-konformen Systemen. 

Um Interoperabilität zu erreichen, wird in diesem Profil nur eine begrenzte Anzahl von möglichen Elementen und Attributen für technische Beweisdaten und beweisrelevante Daten zugelassen bzw. vorgeschrieben, die weithin genutzt werden und als interoperabel anzusehen sind. 

Es  werden  insbesondere  zwei  Basis-Profile  für  den  Aufbau  eines  Evidence  Records vorgestellt: 

- Basis-ERS-Profil  –  ein  obligatorisches  Profil,  das  den  Aufbau  eines  ERS  gem. **[RFC4998]** regelt (vgl. Kapitel 3), 

- Basis-XERS-Profil – ein optionales Profil, das den Aufbau eines ERS gem. **[RFC6283]** regelt (vgl. Kapitel 6.1). 

_**Hinweis 1:**_ 

_Um die Übersichtlichkeit und Lesbarkeit des Dokumentes besser zu gestalten, wurden an einigen Stellen in diesem Dokument Fragmente anderer Standards und Richtlinien zitiert. Die sich somit ergebende Redundanz wird demnach bewusst gepflegt. Grundsätzlich gilt, dass die Originalquellen einen Vorrang genießen. Die explizit gewünschten Abweichungen von der Originalfassung  der  Standards  werden  in  der  Form  von  Anforderungen  im  Dokument definiert und explizit gekennzeichnet._ 

_**Hinweis 2:** - Im folgenden Text umfasst der Begriff_ _**„Digitale Signatur“** „fortgeschrittene elektronische Signaturen“ ge mäß_ _**[eIDAS-VO, Artikel 3 Nr. 11],** „qualifizierte elektronische Signaturen“ gemäß_ _**[eIDAS-VO, Artikel 3 Nr. 12]** , „fortgeschrittenen elektronische Siegel“ gemäß_ _**[eIDAS-VO, Artikel 3 Nr. 26]** und „qualifizierte elektronische Siegel“ gemäß_ _**[eiDAS-VO, Artikel 3 Nr. 27]** . Insofern umfasst der Begriff „digital signierte Dokumente“ sowohl solche, die fortgeschrittene elektronische Signaturen oder Siegel bzw. qualifizierte elektronische Signaturen oder Siegel tragen._ _**-** Mit dem Begriff der_ _**„kryptographisch signierten Dokumente“** sind in dieser TR neben den gemäß_ _**[eI** -_ _**DAS-VO, Artikel 3 Nr. 12]** qualifiziert signierten, den gemäß_ _**[eIDAS-VO, Artikel 3 Nr. 27]** qualifiziert ge - siegelten oder den gemäß_ _**[eIDAS-VO, Artikel 3 Nr. 34]** qualifiziert zeitgestempelten Dokumenten (im Sin_ _**-** ne der eIDAS-Verordnung) ) auch Dokumente mit einer fortgeschrittenen Signatur gemäß_ _**[eIDAS-VO, Ar tikel 3 Nr. 11]** oder mit einem fortgeschrittenen Siegel gemäß_ _**[eIDAS-VO, Artikel 3 Nr. 26]** oder mit einem - elektronischen Zeitstempel gemäß_ _**[eIDAS-VO, Artikel 3 Nr. 33]** erfasst, wie sie oft in der internen Kom munikation von Behörden entstehen. Nicht gemeint sind hier Dokumente mit einfachen Signaturen oder Siegeln basierend auf anderen (z. B. nicht-kryptographischen) Verfahren._ 

> 2 Hinweis! Der Begriff **Evidence Record** wird im weiteren Verlauf auch mit **ER** abgekürzt. 

> 3 Hinweis! Die Liste der Quellen wird im Hauptdokument der TR-03125 gepflegt. 

Bundesamt für Sicherheit in der Informationstechnik 

7 

Profilierung der Evidence Records gemäß RFC 4998 und RFC 6283 

## **3. Profilierung des Evidence Record (normativ)** 

## **3.1. Einleitung** 

Der Zweck dieser Spezifikation ist es, ein Interoperabilitätsprofil für die technischen Beweisdaten (Evidence Record) gemäß **[RFC4998]** bzw. **[RFC6283]** zu erstellen, das eine langfristige und weitgehend system- und plattformunabhängige Interpretierbarkeit der Daten und eine Interoperabilität zwischen unterschiedlichen TR-ESOR- Implementierungen unterstützt. In den folgenden Abschnitten werden die Ausführungen in **[TR-ESOR-F]** , insbesondere in Kapitel 5 „Kryptographische Datenformate“, auf Basis 

- der  „Cryptographic Message  Syntax (CMS)“  gemäß **[RFC5652]** bzw.  vormals **[RFC3852]** , 

- des „Time-Stamp Protocol (TSP)“ gemäß **[RFC3161]** und **[RFC5816] (** zukünftig **[EN 319 422]** ), 

- der Langzeit-Signaturprofilefür CMS-basierte digitale Signaturen, **[ETSI 101733]** (bzw. **[RFC5126]** ) bzw. insbesondere das im Durchführungsrechtsakt **[2015/1506/EU]** referenzierte CAdES Baseline Profile **[ETSI 103 173]** ,  (zukünftig **[ETSI EN 319122-1]** bzw. **[ETSI EN 319122-2] bzw. [ETSI EN 319122-3])** , 

- der Evidence Record Syntax Standards **[RFC4998]** und **[RFC6283]** sowie 

- des Langzeitsignaturprofils für CMS-basierte digitale  Signaturen **[ISO14533-1]** und des Langzeitsignaturprofils für XML-basierte digitale Signaturen **[ISO14533-2]** 

- weiter verfeinert. 

Die in **[TR-ESOR-F]** formulierten Anforderungen werden dabei als bekannt vorausgesetzt und ggf. bedarfsgerecht ergänzt. 

Die Syntax der Evidence Records gemäß **[RFC4998]** und **[RFC6283]** ist im Kapitel 7 - Anhang D skizziert worden. 

In den folgenden Kapiteln wird zunächst die Struktur des Basis-ERS-Profils eines Evidence Records  gem. **[RFC4998]** vorgestellt  (vgl.  Kap. 3.3, 3.4)  und  beschrieben  sowie grundsätzliche Aussagen zur Erstellung und Prüfung von Evidence Records  getroffen (vgl. Kap. 3.5 und 3.6). 

## **3.2. Definition des Verpflichtungsgrades** 

Der Grad der Verpflichtung (VG) der einzelnen Elemente wird durch die folgenden Symbole gekennzeichnet: 

- V – verpflichtend, 

- O – optional, 

- B – bedingt. 

**(A3.2-1)** Elemente, deren Verpflichtungsgrad „ _V – verpflichtend“_ ist,  müssen in einem Evidence Record gemäß diesem Profil wie vorgegeben implementiert sein. Wenn dieses Element  optionale  Unterelemente  hat,  so muss mindestens  eines  dieser  Unterelemente umgesetzt sein. 

**(A3.2-2)** Sofern bei der Erzeugung oder Verifikation eines Evidence Records die technische Konformität und Interoperabilität der _Konformitätsstufe 2_ nachgewiesen werden soll, muss dieses auf Basis der in diesem Dokument beschriebenen Profilierung „Basis-ERS-Profil“ und „Basis-XERS-Profil“ umgesetzt werden. 

Dabei ist die Erzeugung und Verifizierung eines Evidence Records gem. **[RFC4998]** konform 

Bundesamt für Sicherheit in der Informationstechnik 

8 

Profilierungder Evidence Records gemäß RFC 4998 und RFC6283 

zum nachstehenden Basis-ERS-Profile aufgebaut, wenn: 

- die Verarbeitung aller Elemente des Evidence Records, dessen erforderlicher Grad der Verpflichtung im Basis-ERS-Profil „ _V – verpflichtend_ “ ist, so durchgeführt wird, wie es nachfolgend in Kapitel 3.3 und Kapitel 3.4 vorgegeben ist. 

Dabei ist die Erzeugung und Verifizierung eines Evidence Records gem. **[RFC6283]** konform zum nachstehenden Basis-XERS-Profile aufgebaut, wenn: 

- die Verarbeitung aller Elemente des Evidence Records, dessen erforderlicher Grad der Verpflichtung im Basis-XERS-Profil „ _V – verpflichtend_ “ ist, so durchgeführt wird, wie es nachfolgend in Kapitel 6.1 und Kapitel 3.4 vorgegeben ist. 

- Insbesondere beinhalten alle im Evidence Record enthaltenen Instanzen des Elementes _TimeStampToken_ einen gem. dem Basis-ERS-Profil aufgebauten Zeitstempeltoken (vgl. Kapitel 3.4) 

## **3.3. Strukturen eines Evidence Records gem. dem Basis-ERS-Profil** 

Eine grundlegende Einführung zum „Beweisdatenbericht“ (Evidence Record) auf Basis von **[RFC4998]** bzw. **[RFC6283]** befindet sich in **[TR-ESOR-F]** , Kap. 5.5. Die folgenden Unterkapitel stellen ergänzend dazu dar: 

- die benötigten Datenstrukturen für den Beweisdatenbericht, 

- den Verpflichtungsgrad der darin enthaltenen Felder, Elemente und/oder Attribute sowie 

- den Bezug zu den zugrunde liegenden Standards 

- und machen 

- z. T. Vorgaben für den Inhalt der Felder, Elemente und/oder Attribute. 

## **3.3.1. Typ EvidenceRecord** 

Die grundlegenden Beschreibungen der Felder des Typs _Evidence Records_ sind dem Anhang **[TR-ESOR-F]** , Kapitel 5.5.1 zu entnehmen. Der folgende Text definiert noch darüber hinaus gehende Beschreibungen oder Belegungen der Felder. 

Der  Typ _EvidenceRecord_ gem. **[RFC4998]** besteht  aus  drei  verpflichtenden  und  zwei optionalen Feldern (vgl. Tabelle 1), für die in diesem Profil Folgendes gilt: 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0009-15.png)


**----- Start of picture text -----**<br>
Feld Typ VG Referenz<br>EvidenceRecord ::<br>=SEQUENCE {<br>  version INTEGER V(a) [RFC4998] , Kapitel 3.1<br>  digestAlgorithms SEQUENCE OF  V [RFC4998] , Kapitel 3.1,<br>AlgorithmIdentifier dieses Dokument, Kapitel 5.1.1<br>  cryptoInfos CryptoInfos O(b) [RFC4998] , Kapitel 3.1<br>  encryptionInfo EncryptionInfo O(c) [RFC4998] , Kapitel 3.1<br>  archiveTimeStampSequence ArchiveTimeStampSequence V [RFC4998] , Kapitel 3.1<br>}<br>Anforderungen  (A3.3-1) :<br>(a) – Das Feld  version muss aktuell gem.  [RFC4998] , Kap. 3.1 auf „1“ gesetzt werden.<br>(b) – Das Feld  cryptoInfos soll im Rahmen des Basis-ERS-Profils nicht vorhanden.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

9 

Profilierung der Evidence Records gemäß RFC 4998 und RFC 6283 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0010-01.png)


**----- Start of picture text -----**<br>
Feld Typ VG Referenz<br>(c) – Das Feld  encryptionInfo  soll im Rahmen des Basis-ERS-Profils nicht vorhanden sein.<br>**----- End of picture text -----**<br>


**Tabelle 1: Felder des Typs** _**EvidenceRecord**_ 

## **3.3.1.1. Typ ArchiveTimeStampSequence  und Typ ArchiveTimeStampChain** 

Es gelten die folgenden Festlegungen (vgl. Tabelle 2 und 3). 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0010-05.png)


**----- Start of picture text -----**<br>
Typ Subtyp VG Referenz<br>ArchiveTimeStampSequence SEQUENCE OF  V(a)(b) [RFC4998] , Kapitel 5.1<br>ArchiveTimeStampChain<br>Anforderungen  (A3.3-2) :<br>(a) – Dieses Feld  ArchiveTimeStampSequence muss mindestens ein Feld vom Typ<br>ArchiveTimeStampChain enthalten ,<br>(b) – Die Felder vom Typ  ArchiveTimeStampChain im Feld ArchiveTimeStampSequence  sind<br>aufsteigend nach dem Zeitpunkt der beinhalteten  Zeitstempel zu sortieren [4] .<br>**----- End of picture text -----**<br>


**Tabelle 2: Aufbau des Typs** _**ArchiveTimeStampSequence**_ 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0010-07.png)


**----- Start of picture text -----**<br>
Typ Subtyp VG Referenz<br>ArchiveTimeStampChain SEQUENCE OF  V(a)(b) [RFC4998] , Kapitel 5.1<br>ArchiveTimeStamp<br>Anforderungen  (A3.3-3) :<br>(a) – Das Feld  ArchiveTimeStampChain  muss mindestens ein Feld vom Typ  ArchiveTimeStamp<br>enthalten.<br>(b)  –  Die Felder  ArchiveTimeStamp  im Feld  ArchiveTimeStampChain sind aufsteigend nach dem<br>Zeitpunkt der beinhalteten abschließenden Zeitstempel zu sortieren.<br>**----- End of picture text -----**<br>


**Tabelle 3: Aufbau des Typs** _**ArchiveTimeStampChain**_ 

## **3.3.1.2. Typ ArchiveTimeStamp und Typ PartialHashtree** 

Der  Typ _ArchiveTimeStamp_ beinhaltet  drei  optionale  und  ein  verpflichtendes  Feld  (vgl. **[RFC4998]** , Kapitel 4.1 und Tabelle 4). 

Darüber hinaus gelten die folgenden Anforderungen: 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0010-12.png)


**----- Start of picture text -----**<br>
Feld Typ VG Referenz<br>ArchiveTimeStamp :: =<br>SEQUENCE {<br>  digestAlgorithm AlgorithmIdentifier O(a) [RFC4998] , Kapitel 4.1,<br>dieses Dokument, Kapitel 5.1.1<br>  attributes Attributes O(b) [RFC4998] , Kapitel 4.1<br>  reducedHashtree SEQUENCE OF  O(c) [RFC4998] , Kapitel 4.1<br>PartialHashtree<br>  timeStamp ContentInfo V(d) [RFC4998] , Kapitel 4.1<br>**----- End of picture text -----**<br>


> 4 Es muss der im **[RFC4998]** , Kap. 5.1 beschriebene Sortieralgorithmus beachtet werden. 

Bundesamt für Sicherheit in der Informationstechnik 

10 

Profilierungder Evidence Records gemäß RFC 4998 und RFC6283 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0011-01.png)


**----- Start of picture text -----**<br>
Feld Typ VG Referenz<br>}<br>Anforderungen  (A3.3.-4) :<br>(a) – Wenn dieses Feld  digestAlgorithm  fehlt, dann muss der Digest-Algorithmus des Zeitstempels<br>timeStamp  benutzt werden. (vgl.  [RFC4998] , Kapitel 4.1)<br>(b) – Dieses Feld  attributes  soll im Rahmen dieses Profils nicht vorhanden sein .<br>(c) – Alle Vorkommen von  reducedHashtree  innerhalb der einzelnen Elemente vom Typ<br>ArchiveTimeStamp  einer Archivzeitstempelkette  ArchiveTimeStampChain  müssen den<br>gleichen Hashalgorithmus verwenden (vgl.  [RFC4998] , Kap. 5.1).<br>(d) – Dieses Feld  timeStamp  muss den Anforderungen an einen Zeitstempeltoken gemäß  [RFC3161]<br>genügen.<br>**----- End of picture text -----**<br>


Tabelle 4: Felder des Typs _ArchiveTimeStamp_ 

## Grundsätzlich gilt dabei: 

## _reducedHashtree_ [optional]: 

Das Feld _reducedHashtree_ besteht aus einer oder mehreren Listen der Hashwerte, die jeweils einen partiellen Hashbaum repräsentieren. Dieser kann soweit reduziert sein, dass er nur noch die Hashwerte enthält, die für die Verifikation eines einzigen Datenobjektes erforderlich sind. Ein solcher _reducedHashtree_ kann  dazu  genutzt  werden, den  Zeitstempel _timestamp_ des _ArchiveTimeStamp_ und  die  geschützten  Datenobjekte  zu verbinden. Falls das optionale Feld reducedHashtree nicht vorhanden ist, dann bezieht sich der  Zeitstempel  des ArchiveTimeStamps auf  ein  einziges  Datenobjekt  bzw.  eine  einzige Datenobjektgruppe, das bzw. die entweder ein originäres signiertes Datenobjekt darstellt oder ein vorausgegangener Zeitstempel ist. 

Ein Feld vom Typ _PartialHahstree_ beinhaltet eine Sequenz von Ketten der binären Daten (vgl. Tabelle 5). 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0011-07.png)


**----- Start of picture text -----**<br>
Typ Subtyp VG Referenz<br>PartialHashtree SEQUENCE OF OCTET  V(a) [RFC4998] , Kapitel 4.1<br>STRING<br>Bemerkungen:<br>(a) – Dieses Feld beinhaltet einen oder mehrere in Form von binären Daten abgelegte(n) Hashwert(e),<br>die in einer Sequenz abgelegt sind. Die einzelnen Sequenzelemente werden im Zuge der<br>Erstellung des reduzierten Hashbaums (vgl.  [RFC4998] , Kap. 4.2) erstellt.<br>**----- End of picture text -----**<br>


**Tabelle 5: Aufbau des Typs** _**PartialHashtree**_ 

## **3.4. Regeln für den** _**TimeStampToken**_ **im ASN.1-Format** 

Dieses Kapitel ist in vier Abschnitte unterteilt. In Anlehnung an **[RFC5652]** und **[ETSI 101733]** beschreibt dieses Kapitel im ersten Teil allgemeine Eigenschaften des _TimeStampTokens[5]_ , im zweiten Teil den Typ _SignedData_ , im dritten Teil den Typ _SignerInfo_ und im letzten Teil den Typ _SignedAttribute_ . 

Dabei gilt grundsätzlich das Folgende: 

- die Wertebelegung der Elemente des _TimeStampToken_ im ASN.1-Format erfolgt in diesem Profil in Anlehnung an **[COMMON PKI]** , Part 3. Abweichungen oder Verfeinerungen 

- 5 Vgl. **[RFC3161]** bzw. **[TR-ESOR-F]** , Kap. 5.5.1. 

Bundesamt für Sicherheit in der Informationstechnik 

11 

Profilierung der Evidence Records gemäß RFC 4998 und RFC 6283 

werden dabei im folgenden Text als weitere Anforderungen in den jeweiligen Tabellen dargestellt. 

## **3.4.1.** Typ _TimeStampToken_ 

Der Typ _ContentInfo_ beinhaltet zwei Elemente und stellt grundsätzlich einen universellen (abstrakten) Behälter für die Inhaltsdaten dar. Grundsätzlich gilt daher: 

_contentType_ [verpflichtend] 

Das Element _contentType_ beinhaltet eine OID des Datentyps, der in _content_ als „associated and protected object“ (vgl. **[COMMON PKI]** , Kap. 3.1) enthalten ist. 

_content_ [verpflichtend] 

Das Element beinhaltet ein „associated and protected object“, z. B. eine CMS-Signatur (vgl. **[RFC3852]** ), die um die der Beweiskrafterhaltung dienenden Aspekte erweitert wird, wie z. B. Zertifikate oder Sperrlisten etc. 

Im vorliegenden Profil gelten darüber hinaus die folgenden Anforderungen und Festlegungen: 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0012-09.png)


**----- Start of picture text -----**<br>
Feld Typ VG Referenz<br>ContentInfo :: =<br>SEQUENCE {<br>  contentType ContentType V(a) [RFC5652]  Kapitel 5.1,<br>[ETSI 101733] , Kapitel 4.3.1,<br>Kapitel 5.3<br>[RFC4998] , Kapitel 4.1<br>  content  SignedData V(b) [RFC5652] , Kapitel 5.1<br>[ETSI 101733] , Kapitel 5.4<br>}<br>Anforderungen  (A3.4-2) :<br>(a) – Diese OID für den  contentType  von  SignedData  muss „1.2.840.113549.1.7.2“ lauten.<br>(b) – Die in diesem Anwendungsfall zur Geltung kommende Ausprägung des Behälters muss der Typ<br>SignedData (vgl.  [RFC3161] , Kapitel 2.4.2, Seite 7) sein.<br>**----- End of picture text -----**<br>


**Tabelle 6: Felder des Typs** _**ContentInfo**_ **eines** _**TimeStampTokens**_ 

## **3.4.2. Typ** _**SignedData**_ 

Der Typ _SignedData_ beinhaltet sechs Felder (vgl. **[RFC5652]** , Kapitel 5.1), die alle im Rahmen  dieses Profils  verpflichtend sind. Dies weicht von den zitierten  internationalen Standards ab, in denen die Felder _certificates_ und _crls_ nicht verpflichtend sind[6] . Grundsätzlich gilt Folgendes: 

_version_ [verpflichtend] 

_Der  Wert  dieses  Elementes  bestimmt  die  zugrunde  liegende  Syntax-Version  von  diesem SignedData-Element_ 

> 6 Im Rahmen dieses Profils dienen die beiden Felder der Ablage der vollständigen Prüfinformationen (Sperrmaterial, Zertifikate), die eine erfolgreiche Verifikation der digitalen Signatur ermöglichen (vgl. LTLevel-Konformitätsstufe gem. **[ETSI EN 319122-2]** ). 

Bundesamt für Sicherheit in der Informationstechnik 

12 

Profilierungder Evidence Records gemäß RFC 4998 und RFC6283 

## _digestAlgorithms_ [verpflichtend] 

In diesem Element wird eine Sammlung von Kennungen der Hashalgorithmen abgelegt, die für die Hashwertberechnung des zu signierenden Objektes benutzt werden. 

## _encapContentInfo_ [verpflichtend] 

Spezifiziert und  enthält ggf. den zu schützenden (zu unterschreibenden) Inhalt. (vgl. auch **[RFC5652]** , Kap. 5.2) 

## _certificates_ [verpflichtend][7] 

Eine Möglichkeit der Ablage der Zertifikate, die für die Verifikation der digitalen Signaturen benutzt werden. 

_crls_ [verpflichtend][8] 

Eine Möglichkeit der Ablage der Sperrinformation für die vollständige Verifikation der digitalen Signaturen. 

- _signerInfos_ [verpflichtend] 

Eine Sammlung von Daten bzgl. des Signierenden zusammen mit seiner digitalen Signatur[9] . 

Im Rahmen dieses Profils werden dabei die folgenden Festlegungen getroffen: 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0013-12.png)


**----- Start of picture text -----**<br>
Feld Typ VG Referenz<br>SignedData:: =<br>SEQUENCE {<br>  version CMSVersion V(a)  [RFC5652] , Kapitel 5.1<br>[ETSI 101733] , Kapitel 5.4<br>  digestAlgorithms DigestAlgorithmidentifiers  V [RFC5652] , Kapitel 5.1<br>[ETSI 101733] , Kapitel 5.4<br>dieses Dokument, Kap. 5.1.1<br>  encapContentInfo EncapsulatedContentInfo V [RFC5652] , Kapitel 5.1<br>[ETSI 101733] , Kapitel 5.4<br>  certificates CertificateSet Hier:  [RFC5652] , Kapitel 5.1<br>V(b) (c) (f)   [ETSI 103173] , Kapitel 8.1<br>[ETSI EN 319122-2] , Kap. 8.1<br>  crls RevocationInfoChoices Hier:  [RFC5652] , Kapitel 5.1<br>V(d)(f)  [ETSI 103173] , Kapitel 8.2,<br>[ETSI EN 319122-2] , Kap. 8.2<br>  signerInfos SignerInfos V(e) [RFC5652] , Kapitel 5.1<br>[ETSI 101733] , Kapitel 5.4<br>}<br>Anforderungen ( A3.4-3 ):<br>(a) – Der Wert in dem Feld  version muss „3“ gem.  [COMMON PKI] , Part 3 sein.<br>(b) – Im Rahmen dieses Profil müssen innerhalb des Feldes  certificates  die verwendeten Zertifikate<br>**----- End of picture text -----**<br>


> 7 Abweichend von den zitierten internationalen Standards ist dieses Element hier verpflichtend. 

> 8 Abweichend von den zitierten internationalen Standards ist dieses Element hier verpflichtend. 

> 9 Vgl. **[COMMON PKI]** , Part 3 

Bundesamt für Sicherheit in der Informationstechnik 

13 

Profilierung der Evidence Records gemäß RFC 4998 und RFC 6283 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0014-01.png)


**----- Start of picture text -----**<br>
Feld Typ VG Referenz<br>inkl. des vollständigen Zertifikatspfads inklusive der vertrauenswürdigen Wurzelzertifikate<br>abgelegt werden.<br>(c) – Hinweis! Die Referenz auf das Signatur- bzw. Siegelzertifikat muss im Feld  signerInfo  im<br>signierten Attribut   SigningCertificateReference  zusätzlich beigelegt werden. [10]<br>(d) – Im Rahmen dieses Profils muss die vollständige Sperrinformation, benötigt für die Prüfung der<br>digitalen Signatur, in dem Feld  crls abgelegt werden. Primär handelt sich dabei um Sperrlisten<br>(CRLs) und/oder  OSCP-Antworten. [11]<br>(e) – Das Feld  signerInfos darf gem.  [RFC3161]  nur eine Instanz beinhalten.<br>(f) – Abweichend von den zitierten internationalen Standards sind die Felder  certificates  und  crls  in<br>diesem Profil verpflichtend.<br>**----- End of picture text -----**<br>


## **Tabelle 7: Felder des Typs** _**SignedData**_ 

## **3.4.2.1.  Typ  EncapsulatedContentInfo** 

Das Elemente _encapContentInfo_ vom Typ EncapsulatedContentInfo beschreibt den Inhalt, der im Rahmen der Signatur- bzw. Siegelbildung zu verhashen ist. Das Feld besteht aus einem Identifier _eContentType_ und dem Inhalt _eContent_ selbst. Dabei gilt es: 

- e _ContentType_ [verpflichtend] 

Das Element _eContentType_ ist ein Objekt-Identifikator, der eine OID des Datentyps beinhaltet, der in _eContent_ abgelegt ist und im Rahmen der digitalen Signatur zu hashen ist (vgl. **[COMMON PKI]** , Kap. 3.1). 

_eContent_ [verpflichtend][12] 

In diesem Profil beinhaltet das Feld aber stets eine DER-kodierte Instanz der Datenstruktur _TSTInfo_ (vgl. **[RFC3161],** Kap. 2.4.2). Dabei enthält das Attribut „ _messageImprint_ “ im _TSTInfo_ generell eine Hash-Algorithmus OID (vgl. hashAlgorithm in **[RFC3161]** ) und den Hashwert der Daten (vgl. _hashedMessage_ in **[RFC3161]** ), die zeitgestempelt werden sollen. 

Das  Elementes _encapContentInfo_ muss  der  in  der  Tabelle  8  vorgestellten  Struktur entsprechen (vgl. **[RFC3161]** Kap. 2.4.2). 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0014-10.png)


**----- Start of picture text -----**<br>
Feld Typ VG Referenz<br>eContentType ContentType V(a) [RFC5652] , Kapitel 5.2<br>[ETSI 101733] , Kapitel 5.5<br>eContent OCTET STRING V(b)(c)  [RFC5652] , Kapitel 5.2<br>[ETSI 101733] , Kapitel 5.5<br>Anforderungen  (A3.4-4) :<br>(a) – Der Wert dieses Feldes  eContentType  ist konstant und muss „1.2.840.113549.1.9.16.1.4“ ( id-<br>ct-TSTInfo, vgl.  [RFC3161],  Kap. 2.4.2) lauten.<br>(b) – laut  [RFC5652]  ist dieses Feld  eContent  optional. Im vorliegenden Fall eines Zeitstempels<br>muss dieses Feld (vgl.  [RFC3161],  Kap. 2.4.2) vorhanden sein.<br>**----- End of picture text -----**<br>


> 10 Siehe auch **[TR-ESOR-F]** , Kap. 5.1.1 

> 11 Siehe auch **[TR-ESOR-F]** , Kap. 5.1.1 

12Abweichend von den zitierten internationalen Standards ist dieses Element hier verpflichtend. 

Bundesamt für Sicherheit in der Informationstechnik 

14 

Profilierungder Evidence Records gemäß RFC 4998 und RFC6283 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0015-01.png)


**----- Start of picture text -----**<br>
Feld Typ VG Referenz<br>(c) – Dieses Feld  eContent muss hier eine DER-kodierte Instanz der Datenstruktur  TSTInfo  (vgl.<br>[RFC3161],  Kap. 2.4.2) beinhalten. Dabei gilt:<br>Falls der Evidence Record im   initialArchiveTimeStamp  einen   reducedHashtree  enthält,<br>muss im Attribut  hashedMessage  des  TSTInfo.messageImprint  der  DER-kodierte „root hash<br>value“ des reducedHashtrees  enthalten sein. Der Hashwert wird vom Inhalt des OCTET<br>STRINGs ohne umschließende Tags und Länge des OCTET STRINGs übernommen.<br>Andernfalls  muss im Fall eines   initialArchiveTimeStamp   im Attribut   hashedMessage  des<br>TSTInfo.messageImprint,  wie bei einem normalen Zeitstempel, mindestens der DER-kodierte<br>Hashwert  der zeitzustempelnden Daten  eines Datenobjektes enthalten sein. Der Hashwert wird<br>vom Inhalt des OCTET STRINGs ohne umschließende Tags und Länge des OCTET STRINGs<br>verwendet.<br>Im  Fall  der  Zeitstempelerneuerung muss im  Attribut hashedMessage des<br>TSTInfo.messageImprint der Hashwert des Elements  timeStamp des alten Archivzeitstempels<br>gespeichert sein.  Der Hashwert wird vom Inhalt des OCTET STRINGs ohne umschließende<br>Tags und Länge des OCTET STRINGs verwendet.<br>Im  Fall  der  Hashbaumerneuerung muss hier  im  Attribut hashedMessage des<br>TSTInfo.messageImprint  der DER-kodierte  „root  hash  value“  des  neu  erzeugten<br>reducedHashtrees  gespeichert sein.<br>**----- End of picture text -----**<br>


## **Tabelle 8: Felder des Typs** _**EncapsulatedContentInfo**_ 

## **3.4.2.2. Typ CertificateSet und Typ RevocationInfoChoices** 

Ein Element _certificates_ vom Typ _CertificateSet_ besteht aus einer nicht leeren Menge von Elementen des Typs _CertificateChoices_ . 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0015-05.png)


**----- Start of picture text -----**<br>
Typ Subtyp VG Referenz<br>CertificateSet SET OF CertificateChoices V(a) [RFC5652] , Kapitel 10.2.3<br>Anforderungen  (A3.4-5) :<br>(a) – Dieses Feld CertificateSet muss zumindest ein Element vom Typ  CertificateChoices<br>enthalten.<br>**----- End of picture text -----**<br>


**Tabelle 9: Aufbau des Typs** _**CertificateSet**_ **(gem. [RFC5652], Kap. 10.2.3)** 

Der Typ _CertificateChoices_ spezifiziert eine Auswahl aus 5 unterschiedlichen zur Verfügung stehenden Elementen (vgl. Tabelle 10). 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0015-08.png)


**----- Start of picture text -----**<br>
Feld Typ VG Referenz<br>CertificateChoices ::<br>=CHOICE {<br>  certificate Certificate V(a) [RFC5652] , Kapitel 10.2.2<br>  extendedCertificate ExtendedCertificate B(x) [RFC5652] , Kapitel 10.2.2<br>  v1AttrCert AttributeCertificateV1 B(x) [RFC5652] , Kapitel 10.2.2<br>  v2AttrCert AttributeCertificateV2 B(y) [RFC5652] , Kapitel 10.2.2<br>  other OtherCertificateFormat B(y) [RFC5652] , Kapitel 10.2.2<br>}<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

15 

Profilierung der Evidence Records gemäß RFC 4998 und RFC 6283 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0016-01.png)


**----- Start of picture text -----**<br>
Feld Typ VG Referenz<br>Anforderungen  (A3.4-6) :<br>(a) – Im vorliegenden Profil muss certificate  vom Typ  Certificate  genutzt werden.<br>Bemerkungen:<br>(x) – diese Daten sind gem.  [RFC5652] , Kap. 10.2.2 bereits obsolet und werden deshalb im Rahmen<br>dieser Profilierung nicht weiter verfolgt.<br>(y) – werden im Rahmen dieser Profilierung nicht unterstützt.<br>**----- End of picture text -----**<br>


**Tabelle 10: Aufbau des Typs** _**CertificateChoices**_ **(gem. [RFC5652], Kap. 10.2.2)** 

_certificate_ [verbindlich] 

Enthält ein X.509-v3-Zertifikat (vgl. **[RFC5280]** , Kap. 3.1 und 4 sowie ggf. **[RFC6818]** ). 

Ein Element _crls_ vom Typ _RevocationInfoChoices_ besteht aus einer nicht leeren Menge von Elementen des Typs _RevocationInfoChoice_ (vgl. Tabelle 11). 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0016-06.png)


**----- Start of picture text -----**<br>
Typ Subtyp VG Referenz<br>RevocationInfoChoices SET OF RevocationInfoChoice V(a) [ RFC5652] , Kapitel 10.2.1<br>Anforderungen  (A3.4-7) :<br>(a) – Dieses Feld  RevocationInfoChoices muss zumindest ein Element vom Typ<br>RevocationInfoChoice enthalten.<br>**----- End of picture text -----**<br>


## **Tabelle 11: Aufbau des Typs** _**RevocationInfoChoices**_ **(gem. [RFC5652], Kap. 10.2.1)** 

Der Typ _RevocationInfoChoice_ stellt eine Auswahl von einem aus 2 zur Verfügung stehenden Elementen (vgl. Tabelle 12) zur Verfügung. 

_crl_ [bedingt] 

_ist Speicherplatz für die Sperrliste (CRL gem._ _**[RFC5280]** , Kapitel 5)._ 

_other_ [bedingt] 

Enthält sonstige Sperrinformationen, insbesondere eine OCSP-Antwort gem. **[RFC2560]** , Kapitel 4.2. 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0016-13.png)


**----- Start of picture text -----**<br>
Typ Subtyp VG Referenz<br>RevocationInfoChoice ::<br>=CHOICE {<br>  crl CertificateList B(a) [RFC5652] , Kapitel 10.2.1<br>  other OtherRevocationInfoFormat B(b)(c)(a) [RFC5652] , Kapitel 10.2.1<br>}<br>Anforderungen  (A3.4-8) :<br>(a) – Zertifikatssperrlisten X.509 Certificate Revocation Lists (CRLs) sind eine oft genutzte Quelle<br>für Sperrstatusinformationen. Sofern für das zu prüfende Zertifikat sowohl Sperrinformationen<br>in Form von CRLs als auch OCSP-Responses vorliegen, sollen hier OCSP-Responses verwendet<br>werden (vgl.  [TR-ESOR-F] , Fußnote 20).<br>(b) – Wenn OCSP-Auskünfte genutzt werden, muss das Attribut  otherRevInfoFormat  die OID   id-<br>pkix-ocsp-basic  mit dem Wert „1.3.6.1.5.5.7.48.1.1“ beinhalten und das Element<br>otherRevInfo  muss BasicOCSPResponse  enthalten.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

16 

Profilierungder Evidence Records gemäß RFC 4998 und RFC6283 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0017-01.png)


**----- Start of picture text -----**<br>
Typ Subtyp VG Referenz<br>(c) –  BasicOCSPResponse  gemäß  [RFC2560]  muss mindestens ein OCSP signer certificate in<br>BasicOCSPResponse.certs  enthalten. Bezogen auf das Feld  ResponderID  soll die Auswahl<br>byName  genutzt werden.<br>(d) – Der  SingleResponse.singleExtensions  enthält  CertHash , das in  [Common PKI] , Part 4 und<br>Part 9 definiert ist.<br>**----- End of picture text -----**<br>


## **Tabelle 12: Aufbau des Typs** _**RevocationInfoChoices**_ **(gem. [RFC5652], Kap. 10.2.1)** 

## **3.4.3. Typ** _**SignerInfo**_ 

Der Typ _SignerInfo_ ist in **[RFC5652]** , im Kapitel 5.3 festgelegt. Es gilt im Allgemeinen: 

_version_ [verpflichtend] 

Der Wert dieses Elements beschreibt die zugrunde liegende Version der Syntax. 

## _sid_ [verpflichtend] 

Spezifiziert  das  Signatur-  bzw.  Siegel-Zertifikat (signer's  certificate)  und  damit  den  dabei verwendeten öffentlichen Schlüssel, der für die Verifikation der digitalen Signatur erforderlich ist. 

## _digestAlgorithm_ [verpflichtend] 

Beinhaltet die Kennung (ggf. auch zusätzliche Parameter) des Hashalgorithmus und wird benutzt für die Berechnung des sog. _message digests_ . 

## _signedAttrs_ [verpflichtend] 

Dieses Element beherbergt eine Sammlung von Attributen, die mit signiert wurden (zu beachten ist insbesondere Bemerkung (e) in der Tabelle 13). 

## _signatureAlgorithm_ [verpflichtend] 

Mithilfe dieses Elements wird die Kennung des benutzten digitalen Signaturalgorithmus (ggf. mit zusätzlichen Parametern) beschrieben. 

## _signatureValue_ [verpflichtend] 

Innerhalb vom diesem Element wird das Ergebnis der Anwendung des privaten Schlüssels auf den berechneten _message digest_ , vorgegeben durch den Inhalt des Elements _signatureAlgorithm_ . 

## _unsignedAttrs_ [optional] 

Dieses Element beinhaltet die Sammlung von Attributen, die nicht signiert wurden (insbesondere ist die Bemerkung (f) in der Tabelle 13 zu beachten). 

Im Rahmen dieser Profilierung werden folgende Festlegungen getroffen: 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0017-20.png)


**----- Start of picture text -----**<br>
Feld Typ VG Referenz<br>SignerInfo :: =<br>SEQUENCE {<br>  version CMSVersion V(a) [RFC5652] , Kapitel 5.3<br>[ETSI 101733] , Kapitel 5.6<br>[COMMON PKI] , Part 3<br>  sid SignerIdentifier V(b) [RFC5652] , Kapitel 5.3<br>[ETSI 101733] , Kapitel 5.6<br>[COMMON PKI] , Part 3, T. 4<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

17 

Profilierung der Evidence Records gemäß RFC 4998 und RFC 6283 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0018-01.png)


**----- Start of picture text -----**<br>
Feld Typ VG Referenz<br>  digestAlgorithm DigestAlgorithIdentifier V(c) [RFC5652] , Kapitel 5.3<br>[ETSI 101733] , Kapitel 5.6<br>dieses Dokument, Kap. 5.1.1<br>  signedAttrs SignedAttributes V(d) (e) [RFC5652] , Kapitel 5.3<br>[ETSI 101733] , Kapitel 5.6<br>  signatureAlgorithm SignatureAlgorithmIdentifier V [RFC5652] , Kapitel 5.3<br>[ETSI 101733] , Kapitel 5.6<br>  signatureValue SignatureValue V [RFC5652] , Kapitel 5.3<br>[ETSI 101733] , Kapitel 5.6<br>  unsignedAttrs UnsignedAttributes O(f) [RFC5652] , Kapitel 5.3<br>[ETSI 101733] , Kapitel 5.6<br>}<br>Anforderungen  (A3.4-9) :<br>(a) – Das Feld  version muss den Wert „1“ gem.  [COMMON PKI] , Part 3 enthalten.<br>(b) – Im Feld  sid  innerhalb von diesem Profil muss die gem.  [COMMON PKI] , Part 3 geforderte<br>issuerAndSerialNumber  benutzt werden.<br>(c) – Der im Feld  digestAlgorithm  angegebene Wert muss mit einem der Werte in dem Feld<br>SignedData.digestAlgorithms  übereinstimmen.<br>(d) – Gem.  [RFC5652]  ist dieses Feld  signedAttrs  optional, gem.  [RFC3161]  muss dieses Feld aber<br>das  SigningCertificate - bzw.  SigningCertificateV2 -Attribut beinhalten und wird daher<br>verpflichtend. Im Rahmen dieses Profils muss das   SigningCertificateV2 -Attribut (vgl.<br>[RFC5035] ) verwendet werden.<br>(e) – Das Feld  signedAttrs  ist ein Set von Attributen, das signiert wird und DER-kodiert sein muss.<br>(f) – Das Feld  unsignedAttrs  ist gem.  [RFC5652]  optional, es soll aber im Rahmen dieses Profils<br>bei der Erzeugung eines  TimeStampToken  nicht benutzt werden.<br>**----- End of picture text -----**<br>


**Tabelle 13: Felder des Typs** _**SignerInfo**_ 

Der  Typ _SignedAttributes_ bzw. _UnsignedAttributes_ ist  in **[RFC5652]** im  Kapitel  5.3 vorgegeben, und besteht jeweils aus zwei verpflichtenden Feldern (vgl. Tabelle 14). 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0018-04.png)


**----- Start of picture text -----**<br>
Feld Typ VG Referenz<br>Attribute::=<br>SEQUENCE {<br>  attrType OBJECT IDENTIFIER V [RFC5652] , Kapitel 5.3<br>  attrValues SET OF  V [RFC5652] , Kapitel 5.3<br>AttributeValue<br>}<br>Bemerkungen: keine<br>**----- End of picture text -----**<br>


**Tabelle 14: Felder des Typs** _**Attribute**_ **gem. [RFC5652]** 

Bundesamt für Sicherheit in der Informationstechnik 

18 

Profilierungder Evidence Records gemäß RFC 4998 und RFC6283 

## _attrType [verpflichtend]_ 

Der Wert von diesem Feld beschreibt den Typ eines Attributes. 

## _attrValues_ [verpflichtend] 

Dieses Feld beinhaltet eine Menge von Attributwerten, deren Wert durch den Wert des Feldes _attrType_ eindeutig charakterisiert wurde. Der festgelegte Typ des Attributs kann auch die Anzahl der vorhandenen Werte einschränken. 

## **3.4.4. Signierte Attribute (signed attributes)** 

Die Tabelle 15 stellt eine Auflistung der für diese Profilierung relevanten signierten Attribute. Das _signing-certificate-reference_ Attribut ist im Falle eines Zeitstempels gem. **[RFC3161],** Kapitel 2.4.2 verpflichtend. 

_**Hinweis! [RFC3161]** verbietet nicht die Verwendung von weiteren signierten Attributen. Im Rahmen  dieses  Profils dürfen  nur genau[13] die  in  der  Tabelle  16  definierten  Attribute vorhanden sein,  d.h.  neben  den obligatorischen  signierten  Attributen  (ContentType und messageDigest )  darf nur das signierte Attribut  SigningCertificateV2 in der  ESSCertIDv2Ausprägung gemäß_ _**[RFC5816]** vorhanden sein._ 

Es gilt im Allgemeinen: 

_content-type_ [verpflichtend] 

Dieses Attribut beschreibt den Inhaltstyp der unterschriebenen Daten. 

## _message-digest_ [verpflichtend] 

Das Attribut beinhaltet den Hashwert, berechnet über den Inhalt, spezifiziert durch den Wert von _SigneData.encapContentInfo.eContent_ (vgl. Tabelle 8). 

## _signing-certificate-reference_ [verpflichtend] 

Gem. **[RFC3161],** Kap. 2.4.2 ist die Referenz auf das Signatur- bzw. Siegelzertifikat zwingend innerhalb dieses Attributs abzulegen. 

Darüber hinaus gelten die folgenden Anforderungen: 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0019-16.png)


**----- Start of picture text -----**<br>
Attribut Typ VG Referenz<br>SignedAttributes :: = SET OF<br>Attribute {<br>  content-type Attribute V [RFC5652] , Kapitel 11.1<br>[ETSI 101733] , Kapitel 5.7.1<br>  message-digest Attribute V(a)(b) [RFC5652] , Kapitel 11.2<br>[ETSI 101733] , Kapitel 5.7.2<br>dieses Dokument, Kap. 5.1.1<br>  signing-certificate-reference Attribute  V(c) [RFC2634] , Kapitel 5.4<br>[RFC5035] , Kapitel 5.4.1<br>[ETSI 101733] , Kapitel 5.7.3<br>[RFC5816]<br>}<br>Anforderungen  (A3.4-10) :<br>(a) – Das Attribut  message-digest  darf nur einen einzigen Attributwert enthalten, nämlich den<br>**----- End of picture text -----**<br>


> 13 Das hier definierte Profil schränkt absichtlich die **[RFC3161]** -Definition eines Zeitstempels ein. 

Bundesamt für Sicherheit in der Informationstechnik 

19 

Profilierung der Evidence Records gemäß RFC 4998 und RFC 6283 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0020-01.png)


**----- Start of picture text -----**<br>
Attribut Typ VG Referenz<br>Hashwert des Inhalts in  encapContentInfo.eContent .<br>(b) – Das  SignedAttributes  in a  signerInfo  darf nur eine Instanz des  message-digest  – Attributs<br>enthalten. In dem Falle handelt sich um ein Hashwert über eine Instanz des Elementes  TSTInfo<br>aus  SignedData .<br>(c) – In diesem Profil darf kein ESS signing-certificate  gem.  [RFC2634]  oder  [ETSI 101733] ,<br>Kap. 5.7.3.1 genutzt werden, da es auf dem Hashalgorithmus SHA-1 aufsetzt. Vielmehr muss<br>ein  ESS signing-certificate-v2  gem.  [RFC5035]  oder  [ETSI 101733] , Kap. 5.7.3.2 Attribut<br>benutzt werden.<br>**----- End of picture text -----**<br>


## **Tabelle 15: Auflistung der relevanten signierten Attribute (Zeitstempel gem. [RFC3161])** 

Die Tabelle 16 stellt die für den Zeitstempeltoken (gem. **[RFC3161]** ) benutze Ausprägung des signierten Attributes _content-type_ . 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0020-04.png)


**----- Start of picture text -----**<br>
Feld Typ VG Referenz<br>attrType OBJECT IDENTIFIER V (a) [RFC5652] , 11.1<br>[ETSI 101733] , 5.7.1<br>attrValues ContentType  V (b)(c) [RFC5652] , 11.1<br>[ETSI 101733] , 5.7.1<br>Anforderungen ( A3.4-11 ):<br>(a) – Der OID von  attrType  im Attribut  content-type muss gem.  [RFC5652] , Kap. 11.1 auf<br>„1.2.840.113549.1.9.3“ gesetzt werden.<br>(b) – Der OID von  attrValues  im Attribut  content-type muss gem.  [RFC3161] , Kap. 2.4.2 auf<br>„1.2.840.113549.1.9.16.1.4“ ( TSTInfo ) gesetzt werden.<br>(c) – gem.  [RFC5625] , Kap. 11.1 muss dieser Wert von  attrValues Attribut content-type  dem<br>Wert des Elementes  SignedData.encapContentInfo.eContentType  entsprechen.<br>**----- End of picture text -----**<br>


## **Tabelle 16: Attribut** _**content-type**_ **gem. [RFC5652].** 

Die Tabelle 17 beschreibt den syntaktischen Aufbau des _message-digest_ Attributes. 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0020-07.png)


**----- Start of picture text -----**<br>
Feld Typ VG Referenz<br>attrType OBJECT IDENTIFIER V (a) [RFC5652] , Kapitel 11.2<br>attrValues MessageDigest V [RFC5652] , Kapitel 11.2<br>Anforderung ( A3.4-12 ):<br>(a) – Der OID von  attrValues  im Attribut  message-digest muss gem.  [RFC5652],  Kap. 11.2 auf<br>„1.2.840.113549.1.9.4“ gesetzt werden.<br>**----- End of picture text -----**<br>


## **Tabelle 17: Attribut** _**message-digest**_ **gem. [RFC5652].** 

_attrValues_ [verpflichtend] 

Beinhaltet  den  Hashwert berechnet  über die  Daten, welche  durch den  Inhalt  des Elements _SignedData.encapContentInfo.eContent_ gegeben sind _._ In diesem Profil handelt sich um eine DER-kodierte Instanz des Elements _TST-Info_ (vgl. Tabelle 8 und **[RFC3161],** Kap. 2.4.2). 

Gem. **[RFC3161]** Kap.  2.4.2  ist  das  Vorhandensein  des  signierten  Attributes _signingcertificate-reference_ in  einer  digitalen  Signatur  eines  Zeitstempels  verpflichtend.  Die 

Bundesamt für Sicherheit in der Informationstechnik 

20 

Profilierungder Evidence Records gemäß RFC 4998 und RFC6283 

Struktur des _signing-certificate-v2_ -Attribut (vgl. **[RFC5035]** , Kapitel 5.4.1) ist in der Tabelle 18 dargestellt. 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0021-02.png)


**----- Start of picture text -----**<br>
Feld Typ VG Referenz<br>attrType OBJECT IDENTIFIER V(a) [RFC5035] , 5.4.1<br>[ETSI 101733] , 5.7.3.2<br>attrValues ESS SigningCertificateV2 V(b)(c)(d) [RFC5035] , 5.4.1<br>(e)<br>[ETSI 101733] , 5.7.3.2<br>Anforderung ( A3.4-13 ):<br>(a) – Der OID von  attrValues  im  signing-certificate-v2 -Attribut muss gem.  [RFC5035],<br>Kapitel 5.4.1 gesetzt auf „1.2.840.113549.1.9.16.2.47“.<br>(b) – Der Wert vom  SigningCertificateV2 -Attribut muss mindestens eine Referenz ESSCertIDv2<br>zum  signer certificate  enthalten.<br>(c) – Der Wert  vom  SigningCertificateV2 -Attribut soll eine Referenz zum vollständigen<br>Zertifikatspfad inklusive des vertrauenswürdigen Wurzelzertifikats enthalten.<br>(d) – Das Format dieser Referenz muss dem  ESSCertIDv2  gem.  [RFC5035]  entsprechen.<br>**----- End of picture text -----**<br>


**Tabelle 18: Attribut** _**signing-certificate-v2**_ **gem. [RFC5035].** 

## **3.5. Erzeugen eines Evidence Records** 

( **A3.5-1** ) Die Erzeugung eines Evidence Records gem. **[RFC4998]** , der konform zum BasisERS-Profil aufgebaut ist, muss unterstützt werden. 

( **A3.5-2** ) Die Erzeugung eines Evidence Records gem. **[RFC6283]** , der konform zum BasisXERS-Profil (vgl. Kapitel 6) aufgebaut ist, kann unterstützt werden. 

## **3.5.1. Behandlung des Archivzeitstempels** 

Die folgende Anforderung gilt sowohl für die initial angeforderten Zeitstempeltoken als auch für die Zeitstempeltoken, die im Zuge der Zeitstempelerneuerung oder Hashbaumerneuerung angefordert werden. 

Nachfolgend wird ein Überblick über die einzelnen Schritte, die im Zuge der Zeitstempelbeschaffung sowohl auf der Seite des Zeitstempelproviders als auch auf der Seite der TR-ESOR-Middleware durchzuführen sind, skizziert. 

Bevor  die  Erzeugung  des  eigentlichen _timestamp_ im  Rahmen  des _ArchiveTimeStamps_ erfolgreich  abgeschlossen  wird, müssen mindestens  die  folgenden  Schritte  durchgeführt werden: 

- Die TR-ESOR-Middleware berechnet den zu zeitstempelnden Hashwert und bereitet eine Zeitstempelanfrage (TS-Request) vor, 

- Die TR-ESOR-Middleware sendet die vorbereitete Zeitstempelanfrage an den Zeitstempelanbieter. 

- Der Zeitstempelanbieter wählt das Zertifikat für die Erzeugung des _timestamp_ aus und baut den vollständigen Zertifikatspfad inklusive dem vertrauenswürdigen Wurzelzertifikat auf. 

- Wenn mehrere Zertifikatspfade möglich sind, wird ein für die Verifikation geeigneter Zertifikatspfad ausgewählt. 

- Es wird ein Zeitstempel über den in der Zeitstempelanfrage enthaltenen Hashwert erzeugt. Dabei ist darauf zu achten, einen Zeitstempelanbieter zu wählen, der die folgenden Bedingungen erfüllt: 

Bundesamt für Sicherheit in der Informationstechnik 

21 

Profilierung der Evidence Records gemäß RFC 4998 und RFC 6283 

a)  Das  Zertifikat  für  die  Erzeugung  des _timestamp_ und dessen  vollständiger Zertifikatspfad inklusive  das  vertrauenswürdige  Wurzelzertifikat  werden im  Feld _SignedData.certificates_ abgelegt, 

b) eine Referenz _ESSCertIDv2_ zum _signer certificate_ wird im _SigningCertificateV2–_ Attribut hinterlegt und 

c) eine Referenz zum vollständigen Zertifikatspfad inklusive dem vertrauenswürdigen _–_ Wurzelzertifikat wird im _SigningCertificateV2_ Attribut hinterlegt. 

- Der erzeugte _timestamp_ wird an die TR-ESOR-Middleware zurückgeliefert. 

- Die TR-ESOR-Middleware  prüft den  erhaltenen  Zeitstempel  mit  Hilfe der Funktion verifyRequest (vgl. **[TR-ESOR-E]** , Kap. 4.3.2) und setzt dabei die ReturnUpdatedSignatur-Policy mit dem Type-Attribut _http://www.bsi.bund.de/tresor/api/1.2_ ein  (vgl. **[TR-ESOR-E]** ,  Kap.  4.3.2.1),  damit  alle  bei  der  Prüfung verwendeten Zertifikate und Sperrinformationen gem. den Profilen aus diesem Dokument im timestamp hinterlegt werden. 

_**Hinweis!** Gem._ _**[RFC4998]** ,  Kapitel  4.2,  letzter  Absatz_ ,  gilt  bei  der  Erstellung  eines Archivzeitstempels: „The data  (e.g. certificates,  Certificate  Revocation  Lists  (CRLs), or Online Certificate Status Protocol (OCSP) responses) needed to verify the timestamp MUST be preserved, and SHOULD be stored in the timestamp itself unless this causes unnecessary duplication. A timestamp according to **[RFC3161]** is a CMS object in which certificates can be stored in the certificates field and CRLs can be stored in the crls field of signed data.” Nachdem der neue Archivzeitstempel erzeugt wurde, muss er den vollständigen Zertifikatspfad inklusive dem vertrauenswürdigen Wurzelzertifikat für die Validierung der im Rahmen der Archivzeitstempels benutzten Signatur- bzw. Siegelzertifikate enthalten. 

## **3.6. Verifikation eines Evidence Records** 

( **A3.6-1** ) Die Prüfung von Evidence Records, die gem. dem Basis-ERS-Profil aufgebaut sind, muss unterstützt werden. 

( **A3.6-2** ) Die Prüfung eines gem. dem Basis-XERS-Profil aufgebauten Evidence Records muss unterstützt werden[14] . 

( **A3.6-3** ) Wenn das _SigningCertificateV2–_ Attribut  Angaben  zum  Zertifikatspfad  enthält, müssen diese Zertifikate für die Signatur- bzw. Siegelprüfung verwendet werden. 

Falls  der vollständige Zertifikatspfad inklusive dem vertrauenswürdigen Wurzelzertifikat in dem  zeitlich  zuletzt  erstellten _timestamp_ nicht  bereits  hinterlegt  ist  und die  fehlenden Informationen immer noch beschafft werden können, fließen diese in die Prüfung hinein und sollen für die zukünftige Verwendung mit den geprüften Artefakten abgespeichert werden. Dabei gilt: 

( **A3.6-4** ) Falls der vollständige Zertifikatspfad inklusive dem vertrauenswürdigen Wurzelzertifikat in dem zeitlich zuletzt erstellten _timestamp_ nicht bereits hinterlegt ist, muss die Signatur- bzw. Siegelprüfungsanwendung in der Lage sein: 

- den  vollständigen  Zertifikatspfad  inklusive  dem  vertrauenswürdigen  Wurzelzertifikat aufzubauen sowie 

- wenn mehrere Zertifikatspfade vorhanden sind, einen zur Verifikation geeigneten Pfad auszuwählen. 

Sofern ein Fehler dabei aufgetreten ist, wird entweder 

 der Prüfbericht in Form eines _VerificationReport_ -Elementes oder 

> 14 Im Spezialfall eines Import eines gem. Basis-XERS-Profils aufgebauten Evidence Records muss dieser nicht zwingend in dieser Form fortgeschrieben werden., 

Bundesamt für Sicherheit in der Informationstechnik 

22 

Profilierungder Evidence Records gemäß RFC 4998 und RFC6283 

- das um diese Prüfinformationen ergänzte Archivdatenobjekt in Form eines _xaip:XAIP_ - Elements enthalten im Element _VerifyResponse_ als Antwort auf den _VerifyRequest_ (vgl. **[TR-ESOR-E]** ) zurückgegeben. 

- Dabei gilt im Detail: 

- Sollten während der Prüfung eines Evidence Records die in den Basis-ERS-Profil und Basis-XERS-Profil  ausgeschlossenen  Datenstrukturen  gefunden  werden  (z.  B.  das Element cryptoInfos oder das Element encryptionInfo etc.), so  muss dieses mit einer Warnung gekennzeichnet werden. 

- Sollten während der Verifikation eines Evidence Records zusätzliche Zertifikate oder Sperrinformationen beschafft worden sein, so  sollen diese innerhalb der  CredentialSection des dazugehörigen XAIP-Containers abgelegt werden. 

Bundesamt für Sicherheit in der Informationstechnik 

23 

Profilierung der Evidence Records gemäß RFC 4998 und RFC 6283 

## **4. Anhang A: Profil-Überblick (normativ)** 

## **4.1. Basis-ERS-Profil – Überblick** 

In  den  folgenden  Tabellen  wird  ein  Überblick  über  die  durch  das  Basis-ERS-Profil verpflichtende Elemente bezogen auf das ERS selbst und die Zeitstempeltoken gegeben. 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0024-04.png)


**----- Start of picture text -----**<br>
Element Grad der Verpflichtung Wert<br>EvidenceRecord V 1<br>  digestAlgorithms V (a)<br>  archiveTimeStampSequence V<br>    ArchiveTimeStampChain V (b)<br>      ArchiveTimeStamp V (b)<br>        digestAlgorithm O (a)<br>        reducedHashtree O<br>        timeStamp V SignedData<br>Anmerkungen:<br>(a) – vgl. Kapitel 5.1.1<br>(b) – enthält mindestens ein Element<br>**----- End of picture text -----**<br>


**Tabelle 19: Überblick über den Aufbau eines** _**Evidence Records**_ **gem. dem Basis-ERS-Profil** 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0024-06.png)


**----- Start of picture text -----**<br>
Element Grad der Verpflichtung Wert<br>ContentType V Id-signedData<br>(OID =  “1.2.840.113549.1.7.2“)<br>Content V Signed Data<br>   CMSVersion V 3<br>   DigestAlgorithmIdentifiers V (a)  Hash-alg-oid<br>   EncapsulatedContentInfo V<br>      eContentType V Id-ct-TSTInfo<br>(OID= „1.2.840.113549.1.9.16.1.4“)<br>      eContent V DER-encoded value of TSTInfo<br>   CertificateSet (certificates) V(d) X509v3<br>   RevocationInfoChoices (crls) V (c)(d) CertificateList<br>oder<br>pkix-basic-response<br>(OID=”1.3.6.1.5.5.7.48.1.1“)<br>   SignerInfos V<br>      SignerInfo V<br>         CMSVersion V<br>         SignerIdentifier V<br>         DigestAlgorithmIdentifier V (a)<br>         SignedAttributes V<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

24 

Profilierungder Evidence Records gemäß RFC 4998 und RFC6283 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0025-01.png)


**----- Start of picture text -----**<br>
Element Grad der Verpflichtung Wert<br>ContentType V Id-signedData<br>(OID =  “1.2.840.113549.1.7.2“)<br>            ContentType V attrType(OID=“1.2.840.113549.1.9.3“)<br>attrValues(id-ct-TSTInfo)<br>            MessageDigest V<br>            SigningCertificateReference V<br>               ESS SigningCertificate v2 V(d) ESSCertIDv2<br>OID=“1.2.840.113549.1.9.16.2.47“<br>         SignatureAlgorithmIdentifier V(b)<br>         SignatureValue V<br>         UnsignedAttributes B(e)<br>            ATSHashIndex B(e) AttrType: id-aa-ATSHashIndex<br>OID=”0.4.0.1733.2.5”<br>Anmerkungen:<br>(a) – vgl. Kapitel 5.1.1<br>(b) – vgl. Kapitel 5.1.2<br>(c) –  nach Möglichkeit soll die Benutzung von OCSP-Antworten  bevorzugt werden.<br>(d) – in diesem Profil abweichend vom Standard verbindlich<br>(e) – Attribut nur zulässig, wenn im Rahmen einer Zeitstempelerneuerung ein ATSv3 gemäß Kap. 6.2 eingefügt wird.<br>**----- End of picture text -----**<br>


_**Tabelle 20: Überblick über den Aufbau eines Zeitstempels gem. dem Basis-ERS-Profil**_ 

Bundesamt für Sicherheit in der Informationstechnik 

25 

Profilierung der Evidence Records gemäß RFC 4998 und RFC 6283 

## **5. Anhang B: Anforderungen an die kryptographischen Algorithmen und Parameter (normativ)** 

## **5.1. Erstellung eines Evidence Records gem. Basis-ERS-Profil** 

Bei der Erstellung eines Evidence Records gem. Basis-Profil (vgl. Kapitel 3) sind folgende Vorgaben zu den verwendeten Algorithmen zu befolgen. 

Die Anforderungen an die kryptographischen Algorithmen und Parameter bei der Erstellung von Evidence Records unter Einsatz von qualifizierten Zeitstempeln gemäß **[eIDAS-VO, Artikel 42]** basieren auf den Vorgaben der jeweils aktuellen Fassung des Algorithmenkataloges **[ETSI TS 119 312]** , der auf der Webseite https://portal.etsi.org/TBSiteMap/ESI/ESIActivities.aspx veröffentlicht wird, und der auf dem Algorithmenkatalog **[SOG-IS],** veröffentlicht auf der Webseite https://www.sogis.org/uk/supporting_doc_en.htmlwww.sogis.org, basiert Diese Vorgaben sind verbindlich und müssen stets den aktuellen Vorgaben gemäß **[ETSI TS 119 312]** und **[SOGIS]** werden. 

Für die Erzeugung von technischen Beweisdaten (Evidence Records) gilt die Anforderung **(A4.3-1)** des **Krypto-Moduls M.2** . 

Für die Verifikation von technischen Beweisdaten (Evidence Records) gilt die Anforderung **(A4.2-3)** des **Krypto-Moduls M.2** . Bei der Verifikation eines Evidence Records müssen im Bedarfsfall auch die Hashalgorithmen gemäß (vgl. **[ALGCAT]** , Kapitel 6) unterstützt werden. Die OIDs der verwendeten Algorithmen sind **[ETSI TS 119 312]** zu entnehmen. 

## **5.1.1. Hashalgorithmen** 

Aktuell dürfen  nur folgende  Hashalgorithmen für  die  Erzeugung  von  technischen Beweisdaten (Evidence Records) gemäß Kap. 3 verwendet werden: 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0026-09.png)


**----- Start of picture text -----**<br>
Algorithmus OID/URN Normative Referenzen<br>SHA-256 OID:  2.16.840.1.101.3.4.2.1 [RFC4055]<br>URN: http://www.w3.org/2001/04/xmlenc#sha256 [XMLENC]<br>SHA-384 OID:  2.16.840.1.101.3.4.2.2 [RFC4055]<br>URN: http://www.w3.org/2001/04/xmldsig-more#sha384 [RFC6931]<br>SHA-512 OID:  2.16.840.1.101.3.4.2.3 [RFC4055]<br>URN: http://www.w3.org/2001/04/xmlenc#sha512 [XMLENC]<br>**----- End of picture text -----**<br>


**Tabelle 21: Aktuell zugelassene Hashalgorithmen für die Erzeugung technische Beweisdaten (Evidence Records)  (Stand 30.09.2014)** 

## **5.1.2. Digitale Signaturalgorithmen** 

Hier  sind die  Vorgaben und Empfehlungen  gemäß **[ETSI  TS  119  312]** und **[SOG-IS]** einzuhalten. 

## **5.2. Verifikation eines Evidence Records** 

Zusätzlich zu den in den Kapiteln  5.1.1 aufgelisteten Algorithmen  sollen folgende Hashalgorithmen während der Verifikation eines Evidence Records unterstützt werden. 

Bundesamt für Sicherheit in der Informationstechnik 

26 

Profilierungder Evidence Records gemäß RFC 4998 und RFC6283 

## **5.2.1. Hashalgorithmen** 

Für das Prüfen eines Evidence Records müssen alle Algorithmen unterstützt werden, die in diesem  Evidence  Record  verwendet  werden.  Auch  Hash-  und  Signatur-  bzw.  Siegel algorithmen, deren Sicherheitseignung abgelaufen ist, müssen weiterhin für die Validierung der Beweisdaten vom System unterstützt werden. 

Aktuell müssen im  Bedarfsfall  zusätzlich  mindestens  auch  noch   die  folgenden Hashalgorithmen unterstützt werden. Grundsätzlich gilt **[ALGCAT]** , insbesondere Kapitel 6, in der jeweils gültigen Fassung. 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0027-04.png)


**----- Start of picture text -----**<br>
Algorithmus OID/URN Normative Referenzen<br>SHA-1 OID:  1.3.14.3.2.26 [RFC3279]<br>URN: http://www.w3.org/2000/09/xmldsig#sha1 [XMLENC]<br>SHA-224 OID:  2.16.840.1.101.3.4.2.1 [RFC4055]<br>URN: http://www.w3.org/2001/04/xmldsig-more#sha384 [RFC4051]<br>RIPEMD-160 OID:  1.3.36.3.2.1 [CRYPTO3N2]<br>URN: http://www.w3.org/2001/04/xmlenc#ripemd160 [XMLENC]<br>**----- End of picture text -----**<br>


_**Tabelle 22: Aktuell zusätzlich erforderliche Hashalgorithmen für die Verifikation eines Evidence Records (Stand 01.08.2014)**_ 

## **5.2.2. Digitale Signaturalgorithmen** 

Für die Erzeugung müssen die Vorgaben und Empfehlungen  gemäß **[ETSI TS 119 312] und [SOG-IS]** beachtet werden. 

Darüber hinaus sollen nach  aktuellem  Stand bei  der Prüfung auch noch  die folgenden Signatur- bzw. Siegelalgorithmen unterstützt werden (vgl. Tabelle 23): 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0027-09.png)


**----- Start of picture text -----**<br>
Algorithmus OID/URN Normative<br>Referenzen<br>sha1WithRSAEncryption OID:  1.2.840.113549.1.1.5 [RFC3279]<br>URN:  http://www.w3.org/2000/09/xmldsig#rsa-sha1 [XMLDSIG]<br>sha224WithRSAEncryption OID:  1.2.840.113549.1.1.14 [RFC4055]<br>URN:  http://www.w3.org/2000/09/xmldsig#rsa- [XMLDSIG]<br>sha244<br>RSASSA-PSS  mit  mgf1- OID:  1.2.840.113549.1.1.10 [RFC4055]<br>SHA-1und:<br> SHA-1 URN:  [RFC6931]<br> SHA-224 http://www.w3.org/2007/05/xmldsig-more#sha1-rsa-<br>MGF1<br>http://www.w3.org/2007/05/xmldsig-more#sha224-<br>rsa-MGF1<br>dsa-with-sha1 OID:  1.2.840.10040.4.3 [RFC3279]<br>URN: http://www.w3.org/2000/09/xmldsig#dsa-sha1 [XMLDSIG]<br>dsa-with-sha224 OID:  2.16.840.1.101.3.4.3.1 [RFC5758]<br>URN: urn:oid:2.16.840.1.101.3.4.3.1<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

27 

Profilierung der Evidence Records gemäß RFC 4998 und RFC 6283 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0028-01.png)


**----- Start of picture text -----**<br>
Algorithmus OID/URN Normative<br>Referenzen<br>ecdsa-with-sha1 OID:  1.2.840.10045.4.1 [ANSI X9.62]<br>URN: http://www.w3.org/2001/04/xmldsig- [RFC6931]<br>more#ecdsa-sha1<br>ecdsa-with-sha224 OID:  1.2.840.10045.4.3.1 [ANSI X9.62]<br>URN: http://www.w3.org/2001/04/xmldsig- [RFC6931]<br>more#ecdsa-sha224<br>ecgSignatureWithsha1 [15] OID:  1.3.36.3.3.2.5.4.2<br>URN: urn:oid:1.3.36.3.3.2.5.4.2<br>ecgSignatureWithsha224 OID:  1.3.36.3.3.2.5.4.3<br>URN: urn:oid:1.3.36.3.3.2.5.4.3<br>**----- End of picture text -----**<br>


**Tabelle 23: Weitere aktuell zu unterstützende digitale Signatur-Suites bei der Prüfung eines Evidence Records (Stand: 01.08.2014)** 

## **5.2.3. ESSCertIDv2 und ESSCertID** 

**(A5.2-1)** Die Zertifikatsreferenzen in der ESSCertIDv2-Ausprägung (vgl. **[RFC5816]** ) müssen und die ESSCertID-Ausprägung (vgl. **[RFC2634]** ) sollen bei der Verifikation eines Evidence Records unterstützt werden. 

> 15 Siehe https://www.teletrust.de/fileadmin/docs/projekte/oid/OID-Liste_1_3_36_3_3_2_5.pdf . 

Bundesamt für Sicherheit in der Informationstechnik 

28 

Profilierungder Evidence Records gemäß RFC 4998 und RFC6283 

## **6. Anhang C: Weitere ERS-Profile (informativ)** 

## **6.1. Struktur eines Evidence Records gem. dem Basis-XERS-Profil** 

Im Dokument **[TR-ESOR-M.3]** wird eine XML-basierte Ausprägung des Evidence Records gem. **[RFC6283]** detailliert  beschrieben,  sowie  ein  Beispiel  für  einen  XML-basierten Zeitstempel vorgestellt. Um den Beweiskraft des beinhalteten Zeitstempels langfristig zu erhalten,  muss  dieser  um  die  Sperrinformationen  angereichert  werden.  Die  folgenden Unterkapitel  beschreiben  das  Basis-XERS-Profil,  das die  nachhaltige  Erhaltung  des Beweiswerts eines gem. **[RFC6283]** erzeugten Evidence Record sichert. Der Typ _EvidenceRecordType_ weist folgende Struktur auf: 

Versio _n_ [verpflichtend] 

Durch dieses Attribut wird die Version der Syntax beschrieben. 

## EncryptionInformation [optional] 

Dieses Element enthält ggf. Information bezüglich der benutzten Verschlüsselung. 

## SupportinginformationList [optional] 

Mithilfe dieses Elements können Informationen zur notwendigen Verarbeitung von Evidence Record spezifiziert werden (z. B. Eingabe von bestimmten Policies). 

## ArchiveTimeStampSequence [verpflichtend] 

Dieses Element muss vorhanden sein. 

## _ArchiveTimeStampChain_ [verpflichtend] 

Dieses Element muss vorhanden sein und eine Sequenz von Archivzeitstempel beinhalten. 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0029-14.png)


**----- Start of picture text -----**<br>
Feld Typ VG Referenz<br>Version (Attr) decimal (x) V(a) [RFC6283] , Kapitel 2.1<br>EncryptionInformation EncryptioInfo O(b) [RFC6283] , Kapitel 2.1<br>SupportingInformationList SupportingInformationType O(c) [RFC6283] , Kapitel 2.1<br>ArchiveTimeStampSequence ArchiveTimeStampSequenceType V [RFC6283] , Kapitel 2.1<br>    ArchiveTimeStampChain (inline definition) V(d) [RFC6283] , Kapitel 2.1<br>Anforderungen ( A6.1-1 ):<br>(x) – Definition ist durch XML-Schema gegeben (vgl.  [XSD2012] ).<br>(a) – der Wert des Feldes  Version  ist fix und muss auf „1.0“ gesetzt werden.<br>(b) – das Feld  EncryptionInformation  soll im Basis-XERS-Profil NICHT vorhanden sein.<br>(c) – das Feld  SupportingInformationList  soll im Basis-XERS-Profil NICHT vorhanden sein.<br>(d) – das Feld  ArchiveTimeStampChain  muss mindestens ein mal enthalten sein.<br>**----- End of picture text -----**<br>


## **Tabelle 24: Der Typ** _**EvidenceRecordType**_ **gem. [RFC6283] und Basis-XERS-Profil** 

Ein Element _ArchiveTimeStampChain_ wird wie folgt aufgebaut: 

@Ord _er_ [verpflichtend] 

Dieses Attribut erlaubt die Sortierung der einzelnen Zeitstempelketten in der Reihenfolge deren Entstehung. 

Bundesamt für Sicherheit in der Informationstechnik 

29 

Profilierung der Evidence Records gemäß RFC 4998 und RFC 6283 

DigestMetho _d_ [verpflichtend] 

Der  Inhalt  dieses  Elementes  spezifiziert  den  Hashalgorithmus,  der  innerhalb  der  aktuellen Zeitstemeplkette für die Berechnung der Hashwerte benutzt wird. 

## CanonicalizationMeth _od_ [verpflichtend] 

Der Inhalt von diesem Element spezifiziert, welche Kanonisierungsmethoden auf die XMLbasierte Elemente angewandt werden sollen, bevor diese gehasht werden. 

ArchiveTimeSta _mp_ [verpflichtend] 

Der tatsächliche Archivzeitstempel muss in diesem Element abgelegt werden. 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0030-07.png)


**----- Start of picture text -----**<br>
Feld Typ VG Referenz<br>Order (Attr) INTEGER V(a) [RFC6283] , Kapitel 2.1<br>DigestMethod DigestMethodType V(b) [RFC6283] , Kapitel 2.1<br>dieses Dokument, Kap. 5.1.1<br>CanonicalizationMethod CanonicalizationMethodType V(c) [RFC6283] , Kapitel 2.1<br>ArchiveTimeStamp ArchiveTimeStampType V(d) [RFC6283] , Kapitel 2.1<br>Anforderungen ( A6.1-2 ):<br>(a) – Das Attribut  Order  muss gesetzt werden.<br>(b) – Der Wert dieses Elementes  DigestMethod muss gesetzt sein und ist durch die Liste im Kapitel<br>5.1.1 verschränkt.<br>(c) – Das Feld  CanonicalizationMethod muss vorhanden sein.<br>(d) – Das Attribut  ArchiveTimeStamp  muss mindestens ein Element enthalten.<br>**----- End of picture text -----**<br>


**Tabelle 25: Der Typ** _**ArchiveTimeStampChainType**_ **gem. [RFC6283] und Basis-XERSProfil** 

Der Typ _ArchiveTimeStampType_ weist folgende Struktur auf: 

HashTre _e_ [optional] 

Ein optionales Element, das den entsprechenden reduzierten Hashbaum beinhaltet. 

_Tim_ eStam _p_ [verpflichtend] 

In diesem Element muss der Zeitstempeltoken abgelegt werden. 

Attribute _s_ [optional] 

Dieses Element kann weitere Informationen beinhalten (z. B. Policies), die für die Verarbeitung des Evidence Records notwendig sind. Im Basis-XERS-Profil soll dieses Element nicht vorhanden sein. 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0030-16.png)


**----- Start of picture text -----**<br>
Feld Typ VG Referenz<br>HashTree HashTreeType O [RFC6283] , Kapitel 3.1<br>TimeStamp TimeStampType V(a) [RFC6283] , Kapitel 3.1<br>Attributes Attributes O(b) [RFC6283] , Kapitel 3.1<br>Anforderungen ( A6.1-3 ):<br>(a) – In dem Element  TimeStamp muss der Zeitstempeltoken abgelegt werden.<br>(b) – das Element  Attributes  soll im Basis-XERS-Profil nicht vorhanden sein.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

30 

Profilierungder Evidence Records gemäß RFC 4998 und RFC6283 

## **Tabelle 26: Der Typ** _**ArchiveTimeStampType**_ **gem. [RFC6283] und Basis-XERS-Profil** 

Der Typ _TimeStampType_ weist folgende Struktur auf: 

TimeStampToke _n_ [verpflichtend] 

Innerhalb dieses Elements muss der Zeitstempeltoken in Form von Rohdaten abgelegt werden. 

## TimeStampToken.Typ _e_ [verpflichtend] 

Dieses Attribut muss gesetzt werden und innerhalb vom Basis-XERS-Profil muss der Wert dieses Attributs „RFC3161“ lauten. 

## _CryptographicInformationList_ [optional] 

Dieses Element bietet eine Möglichkeit zum Speichern von zusätzlichen Validierungsinformationen (z. B. Zertifikate oder Sperrlisten bzw. OCSP-Antworten), wenn diese nicht innerhalb des Zeitstempeltokens selbst abgelegt werden können. 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0031-09.png)


**----- Start of picture text -----**<br>
Feld Typ VG Referenz<br>TimeStampToken any V(a)(b) [RFC6283] , Kapitel 3.1.2<br>dieses Dokument, Kap.3.4<br>TimeStampToken.Type (Attr) NMTOKEN V(c) [RFC6283] , Kapitel 3.1.2<br>CryptographicInformationList CryptographicInformationType O(d) [RFC6283] , Kapitel 3.1.3<br>Bemerkungen:<br>(a) – der Wert  TimeStampToken muss aus einem gem.  [RFC3161]  Zeitstempeltoken bestehen<br>(b) – der Wert  TimeStampToken muss zum Basis-ERS-Profil konform sein.<br>(c) – der Wert  TimeStampToken.Type  ist fix und muss auf „RFC3161“ gesetzt werden<br>(d) – das Element  CryptographicInformationList  soll im Basis-XERS-Profil nicht vorhanden sein.<br>**----- End of picture text -----**<br>


## **Tabelle 27: Der Typ TimeStampType gem. [RFC6283] und Basis-XERS-Profil** 

## **6.2. Zeitstempelerneuerung mithilfe eines ATSv3 (nur CMS-basiert)** 

## **6.2.1. Verwendung von ATSv3** 

Es kann auch eine Zeitstempelkette mithilfe eines ATSv3-Zeitstempels im Rahmen einer Zeitstempelerneuerung abgeschlossen werden oder als Archivzeitstempel verwendet werden, wenn nur ein Archivdatenobjekt vorhanden ist. Solch ein ATSv3-Zeitstempel wird sich im Fall der Zeitstempelerneuerung auf den letzten bereits vorhanden Zeitstempel der letzten bereits vorhandenen Zeitstempelkette beziehen (vgl. Abbildung 2). 

Bundesamt für Sicherheit in der Informationstechnik 

31 

Profilierung der Evidence Records gemäß RFC 4998 und RFC 6283 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0032-01.png)


**Abbildung 2: Zeitstempelerneuerung mithilfe eines ATSv3** 

**(A6.2-1)** Die Prüfung von im Evidence Record enthaltenen Zeitstempeltokens gem. ATSv3 soll unterstützt werden. Der Vorteil von ATSv3 besteht darin, dass es in den letzten ATSv3-Zeitstempel weitere _crls_ und _certificates_ in _signedData.certificates_ bzw. _signedData.crls_ abgelegt  werden können, ohne den letzten ATSv3 zu zerstören. Ein weiterer Vorteil des ATSv3-Zeitstempels besteht darin, dass ein auf dieser Weise aufgebaute Zeitstempel gem. Basis-ERS-Profil den „LTA-Level“-Konformitätsanforderungen  gemäß **[ETSI  EN  319122-2]** , Kap. 9, Tabelle  13 genügen kann.Auf der anderen Seite wird für jedes zu schützende Archivdatenobjekt ein eigenständiger Zeitstempel benötigt; die Verwendung von Hashbäumen ist bei ATSv3-artigen Zeitstempeln bislang nicht vorgesehen. Ein gem. **[RFC4998]** und dem Basis-ERS-Profil erstellte Evidence Record beinhaltet eine Sequenz von Archivzeitstempel (vgl. Kapitel  3 und **[RFC4998]** Kap. 3.1). Ein einzelner Archivzeitstempel beinhaltet einen gem. **[RFC3161]** ausgestellten Zeitstempeltoken (vgl. **[RFC4998]** , Kap. 4.1), der gem. dem Basis-ERS-Profil erweitert wurde (vgl. Kapitel 3.4). Für  eine  auf  diese  Weise  vorbereitete  Datenstruktur  kann  auch  mit  Hilfe  der  hier beschriebenen alternativen Methode eine Zeitstempelerneuerung durchgeführt werden, indem für diese Operation ein Zeitstempel vom Typ _archive-time-stamp-v3_ (ATSv3) zusammen mit der  gesammelten  Sperrinformation  verwendet  wird.  Das  erstellte _ATSv3_ -Attribut  wird abschließend  als  ein  unsigniertes  Attribut  der  digitalen  Signatur  des  zuletzt  gültigen Archivzeitstempels abgelegt (vgl. Abbildung 2). 

## **6.2.2. Attribut** _**archive-time-stamp-v3**_ **(** _**ATSv3**_ **)** 

Es können mehrerer Instanzen von einem _ATSv3_ in einer digitalen Signatur auftreten (vgl. hierzu **[ETSI 101733]** , Kap. 6.4.3). Der  Aufbau  des _ATSv3_ -Attributes  ist  angelehnt  an **[RFC5652]** Kapitel  5.3  wie  in  der Tabelle 28 festgelegt. 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0032-06.png)


**----- Start of picture text -----**<br>
Feld Typ VG Referenz<br>attrType OBJECT IDENTIFIER (a) V [ETSI 101733] , Kapitel 6.4.3<br>attrValues ArchiveTimeStampToken (b)(c) V [ETSI 101733] , Kapitel 7.4<br>Bemerkungen:<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

32 

Profilierungder Evidence Records gemäß RFC 4998 und RFC6283 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0033-01.png)


**----- Start of picture text -----**<br>
Feld Typ VG Referenz<br>(a) – gem.  [ETSI 101733]  (Kapitel 6.4.3) ist das Feld  attrType  gesetzt auf „0.4.0.1733.2.4“.<br>(b) – gem.  [ETSI 101733]  (Kapitel 6.4.3) muss ein  ATSv3 -Attribut genau einen  attrValue   in Form<br>eines ArchiveTimeStampToken enthalten.<br>(c) – der Inhalt der enthaltenen Archivzeitstempels, insbesondere im Hinblick auf den Aufbau des<br>sog. „ message imprint “, muss gem.  [ETSI 101733]  Kap. 6.4.3 und 6.4.2 erstellt werden.<br>**----- End of picture text -----**<br>


## **Tabelle 28: Attribut archive-time-stamp-v3 gem. [ETSI 101733] Kap. 6.4.3** 

Die Tabelle 29 skizziert den Aufbau des „ _message imprint_ “ gem. **[ETSI 101733],** Kap. 6.4.3. Die Reihenfolge ist wichtig. Die Werte der einzelnen Felder werden miteinander konkateniert. 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0033-04.png)


**----- Start of picture text -----**<br>
Feld Typ VG Referenz<br>SignedData<br>  encapContentInfo<br>    eContentType ContentType V [RFC5652] , Kapitel 5.2<br>Hash über signierte  OCTET STRING V [ETSI 101733] , Kapitel 6.4.3,<br>Daten (a) Punkt 2)<br>[RFC5652] , Kapitel 5.4<br>SignedData<br>  SignerInfo (b) V [RFC5652] , Kapitel 5.3<br>    version CMSVersion<br>    sid SignerIdentifier<br>    digestAlgorithm DigestAlgorithmIdentifier<br>    signedAttrs SignedAttributes<br>    signatureAlgorithm SignatureAlgorithmIdentifier<br>    signature SignatureValue<br>ATSHashindex (c) ats-hash-index V [ETSI 101733] , Kapitel 6.4.2<br>Bemerkungen:<br>(a) – wird analog zu dem signierten Attribut  message-digest  der digitalen Signatur berechnet.<br>(b) – es werden alle Instanzen des Elementes  SignerInfo  in der Reihenfolge des Auftretens<br>berücksichtigt.<br>(c) – siehe Kapitel 6.2.3 für weiter Informationen<br>**----- End of picture text -----**<br>


**Tabelle 29: Aufbau von** _**message imprint**_ **eines** _**ATSv3**_ 

## **6.2.3. Attribut** _**ats-hash-index**_ 

Ein _ats-hash-index_ stellt ein Attribut im Sinne von **[RFC5652],** Kapitel 5.3 dar, dessen Aufbau der Tabelle 30 zu entnehmen ist. 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0033-08.png)


**----- Start of picture text -----**<br>
Feld Typ VG Referenz<br>attrType OBJECT IDENTIFIER (a) V [ETSI 101733] , Kapitel 6.4.2<br>attrValues ATSHashIndex (b) V [ETSI 101733] , Kapitel 6.4.2<br>Bemerkungen:<br>(a) – gem.  [ETSI 101733]  (Kapitel 6.4.3) gesetzt auf „0.4.0.1733.2.5“.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

33 

Profilierung der Evidence Records gemäß RFC 4998 und RFC 6283 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0034-01.png)


**----- Start of picture text -----**<br>
Feld Typ VG Referenz<br>(b) – gem.  [ETSI 101733]  (Kapitel 6.4.2) muss ein  ats-hash-index -Attribut genau ein Wert-<br>Element enthalten.<br>**----- End of picture text -----**<br>


## **Tabelle 30: Das Attribut** _**ats-hash-index**_ 

Ein _ats-hash-index_ Attribut bezieht sich auf eine digitale CAdES-Signatur, welche mit einem _ATSv3_ abgesichert wird. Der _ATSv3_ referenziert das _ats-hash-index_ Attribut und beherbergt dieses als ein unsigniertes Attribut der eigenen digitalen Signatur (vgl. Abbildung 3). 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0034-04.png)


**Abbildung 3: Zusammenhang digitale CAdES Signatur,** _**ATSv3**_ **und** _**atshash-index**_ 

Die Nutzung des _ats-hash-index_ Attributs  ermöglicht  das  Hinzufügen von Zertifikaten, Sperrinformationen in _SignedData.certificate_ und _SignedData.crls_ (vgl. Tabelle 7), auch nachdem schon ein Archivzeitstempel für die vorliegende digitale Signatur erstellt wurde (vgl. [ETSI 101733], Kap. 6.4.2, Note 3 oder [ETSI 319122], Kap. 6.5.1, Note 3). 

Der Aufbau des Elements vom Typ _ATSHashIndex_ , das der Wert des _ats-hash-index_ Attributs darstellt ist der Tabelle 31 zu entnehmen. 


![](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf-0034-08.png)


**----- Start of picture text -----**<br>
Feld Typ VG Referenz<br>hashIndAlgorithm AlgorithmIdentifier (a) V [ETSI 101733] , Kapitel 6.4.2<br>certificatesHashIndex SEQ OF OCTET STRING V [ETSI 101733] , Kapitel 6.4.2<br>crlsHashIndex SEQ OF OCTET STRING V [ETSI 101733] , Kapitel 6.4.2<br>unsignedAttrsHashIndex  [SEQ OF OCTET STRING] V [ETSI 101733] , Kapitel 6.4.2<br>Bemerkungen:<br>(a) – gem.  [ETSI 101733], Kapitel 6.4.2 standardmäßig  id-sha256<br>**----- End of picture text -----**<br>


**Tabelle 31: Felder des Typs** _**ATSHashIndex**_ 

## _**hashIndAlgorithm**_ **[verpflichtend]** 

Beinhaltet die Kennung des für die Erstellung der Hashwerte von _certificatesHashIndex_ , _crlsHashIndex_ und _unsignedAttrsHashIndex_ benutzen Hashalgorithmus. Der Algorithmus soll dem aus der Erstellung von _message imprint_ in dem dazugehörigen _ATSv3_ identisch sein. 

_**certificatesHashIndex**_ **[verpflichtend]** 

Bundesamt für Sicherheit in der Informationstechnik 

34 

Profilierungder Evidence Records gemäß RFC 4998 und RFC6283 

Eine Abfolge von Hashwerten berechnet über jedes Element (hier vom _Typ CertificateChoices_ ) des Feldes _SignedData.certificates_ (vgl. Tabelle 7). 

## _**crlsHashIndex**_ **[verpflichtend]** 

Eine Abfolge von berechneten Hashwerten über jedes Element (hier vom Typ _RevocationInfoChoice_ ) des Feldes _SignedData.crls_ (vgl. Tabelle 7). 

## _**unsignedAttrsHashIndex**_ **[verpflichtend]** 

Der Inhalt dieses Element stellt eine Abfolge von berechneten Hashwerten über jedes Attribut aus der Menge der unsignierten Attribute bezogen auf jede Instanz des Elementes _SignerInfo_ (vgl. Tabelle 13). 

Bundesamt für Sicherheit in der Informationstechnik 

35 

Profilierung der Evidence Records gemäß RFC 4998 und RFC 6283 

## **7. Anhang D Syntaxdefinitionen (informativ)** 

In diesem Kapitel wird ein Extrakt der wichtigsten Syntaxdefinitionen aus dem Dokumenten **[RFC4998]** und **[RFC6283]** als ein Nachschlagewerk dargestellt. 

## **7.1. Evidence Records gem. [RFC4998]** 

Ein Evidence Record wird gem. **[RFC4889]** mithilfe von ASN.1 kodiert. Die nachfolgenden Kapitel stellen in Auszügen aus **[RFC4998]** den syntaktischen Aufbau eines ASN.1 Evidence Records. 

## **7.1.1. Element** _**EvidenceRecord**_ **gem. [RFC4998]** 

Der _EvidenceRecord_ hat die folgende ASN.1 Syntax (vgl. Listing 1). 

EvidenceRecord ::= SEQUENCE { version INTEGER { v1(1) } , digestAlgorithms SEQUENCE OF AlgorithmIdentifier, cryptoInfos [0] CryptoInfos OPTIONAL, encryptionInfo [1] EncryptionInfo OPTIONAL, archiveTimeStampSequence ArchiveTimeStampSequence } CryptoInfos ::= SEQUENCE SIZE (1..MAX) OF Attribute 

**Listing 1: Das Element** _**EvidenceRecord**_ **gem. [RFC4998]** 

## **7.1.2. Element** _**ArchiveTimeStamp**_ **gem. [RFC4998]** 

Der _ArchiveTimeStamp_ hat die folgende ASN.1 Syntax (vgl. Listing 2): 

ArchiveTimeStamp ::= SEQUENCE { digestAlgorithm [0] AlgorithmIdentifier OPTIONAL, attributes [1] Attributes OPTIONAL, reducedHashtree [2] SEQUENCE OF PartialHashtree OPTIONAL, timeStamp ContentInfo} PartialHashtree ::= SEQUENCE OF OCTET STRING Attributes ::= SET SIZE (1..MAX) OF Attribute 

Listing 2: Das Element ArchiveTimeStamp gem. [RFC4998] 

## **7.2. Evidence Records gem. [RFC6283]** 

Ein Evidence  Record gem.  [RFC6283] wird mithilfe  von Extensible  Markup Language (XML) definiert. Im Folgenden wird mithilfe der Auszüge aus dem **[RFC6283]** der Aufbau eines Evidence Records dargestellt. 

_Hinweis! Die folgenden Definitionen wurden mithilfe eines Pseudo-XML-Dialektes dargestellt. Es gelten dabei folgende Annahmen bezüglich der Kardinalität der Elemente:_ 

_- „?“ - bedeutet 0 oder 1 (0..1),_ 

- _„+“ - bedeutet 1 oder mehr (1..n), - „*“ - bedeutet 0 oder mehr (0..n)._ 

## **7.2.1. Element** _**<EvidenceRecord>**_ **gem. [RFC6283]** 

Das Element _<EvidenceRecord>_ weist gem. **[RFC6283]** die im Listing 3 abgebildete Struktur auf. 

Bundesamt für Sicherheit in der Informationstechnik 

36 

Profilierungder Evidence Records gemäß RFC 4998 und RFC6283 

<EvidenceRecord Version> <EncryptionInformation> <EncryptionInformationType> <EncryptionInformationValue> </EncryptionInformation> ? <SupportingInformationList> <SupportingInformation Type /> + 

</SupportingInformationList> ? 

<ArchiveTimeStampSequence> 

<ArchiveTimeStampChain Order> <DigestMethod Algorithm /> <CanonicalizationMethod Algorithm /> 

<ArchiveTimeStamp Order> 

<HashTree /> ? 

<TimeStamp> 

<TimeStampToken Type /> 

<CryptographicInformationList> 

<CryptographicInformation Order Type /> + 

</CryptographicInformationList> ? 

</TimeStamp> 

<Attributes> 

<Attribute Order Type /> + 

</Attributes> ? 

</ArchiveTimeStamp> + 

</ArchiveTimeStampChain> + 

</ArchiveTimeStampSequence> 

</EvidenceRecord> 

**Listing 3: Das Element** _**<EvidenceRecord>**_ 

## **7.2.2. Element** _**<HashTree>**_ **gem. [RFC6283]** 

Das Element _<HashTree>_ muss der folgenden Datenstruktur entsprechen (vgl. Listing 4). 

<HashTree> 

<Sequence Order> 

<DigestValue>base64 encoded hash value</DigestValue> + 

</Sequence> + 

</HashTree> 

**Listing 4: Das Element** _**<HashTree>**_ 

## **7.2.3. Element** _**<TimeStamp>**_ **gem. [RFC6283]** 

Das Element _<TimeStamp>_ abhängig vom Wert des Attributs _Type_ beinhaltet entweder einen gem. **[RFC3161]** erstellten  Zeitstempeltoken,  oder  eine  alternative  Darstellung,  wie.  z.  B. **[TSENTRUST]** (vgl. **[RFC6283]** , Kap. 3.1.2). 

Bundesamt für Sicherheit in der Informationstechnik 

37 


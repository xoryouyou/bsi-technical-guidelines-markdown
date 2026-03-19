
![](markdown/tr/BSI_TR_03125_Anlage_XBDP_V1_2_1/BSI_TR_03125_Anlage_XBDP_V1_2_1.pdf-0001-00.png)


Profilierungen im Rahmen der BSI Technischen Richtlinie 03125 Beweiswerterhaltung kryptographisch signierter Dokumente 

## **Anlage TR-ESOR-Profil-XBDP: Profilierung des XAIP mit XBARCH, XDOMEA und PREMIS** 

Bezeichnung Profilierung des XAIP mit **XB** ARCH, X **D** OMEA und **P** REMIS Kürzel BSI TR-ESOR-Profil-XBDP Version 1.2.1 (auf Basis der eIDAS-Verordnung) Datum 15.03.2018 

TR-ESOR-Profil: XAIP mit XBARCH und XDOMEA 

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn Tel.: +49 228 99 9582-0 E-Mail:  tresor@bsi.bund.de Internet: https://www.bsi.bund.de © Bundesamt für Sicherheit in der Informationstechnik 2018 

Bundesamt für Sicherheit in der Informationstechnik 

TR-ESOR-Profil: XAIP mit XBARCH, XDOMEA und PREMIS 

## **Inhaltsverzeichnis** 

|1. Einführung<br>4|
|---|
|2. Übersicht<br>6|
|3. Profilierung des XML-Schemas für XAIP im Zusammenhang mit XBARCH, XDOMEA und PRE-|
|MIS für die Behörden der Bundesverwaltung<br>7|
|3.1 TR-ESOR Anlage F..........................................................................................................................7|
|3.1.1 Überblick über die XAIP-Datenstruktur – das <XAIP>-Element<br>7|
|3.1.2 Der xaip:packageHeaderType<br>8|
|3.1.3 Profilierung der XAIP-MetaDataSection im Zusammenhang mit XBARCH und XDOMEA<br>9|
|3.2 Technische Metadaten (optional)....................................................................................................10|
|3.3 Fachliche Metadaten (optional)......................................................................................................11|
|3.4 Wertesystem für Kategorisierung und Klassifizierung der Metadaten............................................11|
|4. Anhang A – XML-Schema-Definition<br>13|
|4.1 XAIP-Schema-Erweiterung............................................................................................................13|
|4.2 XBarch-Schema-Erweiterung.........................................................................................................13|



## **Abbildungsverzeichnis** 

Abbildung 1: Schematische Darstellung der IT-Referenzarchitektur.....................................................5 Abbildung 2: Aufbau des Datentypes xaip:TechnischeMetadatenTyp.................................................10 Abbildung 3: Beispiel einer Ablage von technischen Metadaten..........................................................11 Abbildung 4: Beispiel einer Ablage von fachlichen Metadaten............................................................11 Abbildung 5: XAIP-Schema erweitert um die Aspekte dieser Profilierung..........................................13 Abbildung 6 Definition des vom XBarch abgeleiteten Typs xbarch:Technische_Daten.......................14 

## **Tabellenverzeichnis** 

Tabelle 1: Wertesystem für Kategorisierung und Klassifizierung der Metadaten..................................12 

Bundesamt für Sicherheit in der Informationstechnik 

3 

TR-ESOR-Profil: XAIP mit XBARCH, XDOMEA und PREMIS 

## **1. Einführung** 

Ziel der Technischen Richtlinie „Beweiswerterhaltung kryptographisch signierter Dokumente“ ist die Spezifikation sicherheitstechnischer Anforderungen für den langfristigen Beweiswerterhalt von kryptographisch signierten elektronischen Dokumenten und Daten nebst zugehörigen elektronischen Verwaltungsdaten (Metadaten). 

Eine für diese Zwecke definierte Middleware (TR-ESOR-Middleware) im Sinn dieser Richtlinie umfasst alle diejenigen Module ( **M** ) und Schnittstellen ( **S)** , die zur Sicherung und zum Erhalt der Authentizität und zum Nachweis der Integrität der aufbewahrten Dokumente und Daten eingesetzt werden. Die im Hauptdokument dieser Technischen Richtlinie vorgestellte Referenzarchitektur besteht aus den nachfolgend beschriebenen funktionalen und logischen Einheiten: 

- der Eingangs-Schnittstelle S.4 der TR-ESOR-Middleware, die dazu dient, die TR-ESORMiddleware in die bestehende IT- und Infrastrukturlandschaft einzubetten; 

- dem zentralen Middlewaremodul (vgl. **[TR-ESOR-M.1]** ), welches den Informationsfluss in der Middleware regelt, die Sicherheitsanforderungen an die Schnittstellen zu den ITAnwendungen  umsetzt  und  für  eine  Entkopplung  von  Anwendungssystemen  und ECM/Langzeitspeicher sorgt; 

- dem „Krypto“-Modul (vgl. **[TR-ESOR-M.2]** ) nebst den zugehörigen Schnittstellen S.1 und S.3, das alle erforderlichen Funktionen zur Berechnung von Hashwerten, Prüfung elektronischer Signaturen bzw. Siegel bzw. Zeitstempel, zur Nachprüfung elektronischer Zertifikate und zum Einholen qualifizierter Zeitstempel sowie (optional) elektronischer Signaturen bzw. Siegel für die Middleware zur Verfügung stellt. Darüber hinaus kann es Funktionen zur Ver- und Entschlüsselung von Daten und Dokumenten zur Verfügung stellen; 

- dem „ArchiSig-Modul“ (vgl. **[TR-ESOR-M.3]** ) mit der Schnittstelle S.6, das die erforderlichen Funktionen für die Beweiswerterhaltung der digital signierten Unterlagen bereitstellt; 

- einem ECM/Langzeitspeicher mit den Schnittstellen S.2 und S.5, der die physische Archivierung/Aufbewahrung und auch das Speichern der beweiswerterhaltenden Zusatzdaten übernimmt. 

   - _Dieser ECM/Langzeitspeicher ist nicht mehr direkt Teil der Technischen Richtlinie, gleichwohl werden über die beiden Schnittstellen, die noch Teil der TR-ESOR-Middleware sind, Anforderungen daran gestellt._ 

   - _Ebenso wenig ist die Applikationsschicht, die auch einen XML-Adapter enthalten kann, direkter Teil der Technischen Richtlinie, auch wenn dieser XML-Adapter als Teil einer Middleware implementiert werden kann._ 

Die in Abbildung 1 dargestellte IT-Referenzarchitektur orientiert sich an der ArchiSafe[1] Referenzarchitektur und soll die logische (funktionale) Interoperabilität künftiger Produkte mit den Zielen und Anforderungen der Technischen Richtlinie ermöglichen und unterstützen. 

Diese Technische Richtlinie ist modular aufgebaut und spezifiziert in einzelnen Anlagen zum Hauptdokument die funktionalen und sicherheitstechnischen Anforderungen an die erforderlichen IT-Komponenten und Schnittstellen der TR-ESOR-Middleware. Die Spezifikationen sind strikt plattform-, produkt-, und herstellerunabhängig. 

Das vorliegende Dokument trägt die Bezeichnung „Anlage TR-ESOR-Profil-XBDP: Profilierung des XAIP mit XBARCH, XDOMEA und PREMIS“ **[TR-ESOR-XBDP]** und spezifiziert die Integration von XBARCH-, XDOMEA- und PREMIS-Datenelementen in die Datenstruktur xaip:XAIP gemäß Anhang **[TR-ESOR-F]** im Rahmen des **Bundesbehördenprofils** gemäß **[TR-ESOR-B]** . 

> 1 Siehe dazu http://www.archisafe.de 

Bundesamt für Sicherheit in der Informationstechnik 

4 

TR-ESOR-Profil: XAIP mit XBARCH, XDOMEA und PREMIS 


![](markdown/tr/BSI_TR_03125_Anlage_XBDP_V1_2_1/BSI_TR_03125_Anlage_XBDP_V1_2_1.pdf-0005-01.png)


**Abbildung 1: Schematische Darstellung der IT-Referenzarchitektur** 

Bundesamt für Sicherheit in der Informationstechnik 

5 

TR-ESOR-Profil: XAIP mit XBARCH, XDOMEA und PREMIS 

## **2. Übersicht** 

Insbesondere im behördlichen Umfeld ist die langfristige beweiswerterhaltende Aufbewahrung elektronisch signierter Daten und Dokumente von großen Bedeutung. Dabei ist nicht nur die Auswahl geeigneter Formate für die Aufbewahrung der Daten und Dokumente sondern auch die Bereitstellung von Informationen über die Daten und Dokumente selbst (sog. Metadaten) sehr wichtig. 

Ziel des vorliegenden Dokumentes ist eine Profilierung des _XAIP_ gemäß ( **[TR-ESOR-F]** , V1.2), um Metadaten gemäß **[XBARCH]** , **[XDOMEA]** und **[PREMIS]** geeignet zu integrieren. 

Das Dokument ist daher als ergänzende Profilierung der Anlage **[TR-ESOR-F]** im Rahmen des **Bundesbehördenprofils** gemäß **[TR-ESOR-B]** anzusehen. 

Dabei werden folgenden Typen von Metadaten unterschieden: 

- **technische Metadaten** – Darstellung der technischen Aspekte der aufbewahrten Daten und Dokumente, die eine Wiedergabe zu einem späteren Zeitpunkt erlaubt. 

- **fachliche Metadaten** – Beschreibung der fachlichen Bedeutung der aufbewahrten Daten und Dokumenten sowie die Darstellung des fachlichen Zusammenhangs der Daten und Dokumente. 

## **HINWEIS:** 

_**Die Definition der Element der xaip:XAIP-Datenstruktur liegt in englischer Sprache vor. Die in diesem Dokument referenzierten Standards sind überwiegend in der deutschen Sprache definiert und werden daher im folgenden Text auch so belassen.**_ 

## **HINWEIS:** 

_Im folgenden Text umfasst der Begriff_ _**„Digitale Signatur“** „fortgeschrittene elektronische Signaturen“ gemäß_ _**[eIDAS-VO, Artikel 3 Nr. 11],** „qualifizierte elektronische Signaturen“ gemäß_ _**[eIDAS-VO, Artikel 3 Nr. 12]** , „fortgeschrittenen elektronische Siegel“ gemäß_ _**[eIDAS-VO, Artikel 3 Nr. 26]** und „qualifizierte elektronische Siegel“ gemäß_ _**[eiDAS-VO, Artikel 3 Nr. 27]** . Insofern umfasst der Begriff „digital signierte Dokumente“ sowohl solche, die fortgeschrittene elektronische Signaturen oder Siegel bzw. qualifizierte elektronische Signaturen oder Siegel tragen._ _**-** Mit dem Begriff der_ _**„kryptographisch signierten Dokumente“** sind in dieser TR neben den gemäß_ _**[eI** -_ _**DAS-VO, Artikel 3 Nr. 12]** qualifiziert signierten, den gemäß_ _**[eIDAS-VO, Artikel 3 Nr. 27]** qualifiziert ge - siegelten oder den gemäß_ _**[eIDAS-VO, Artikel 3 Nr. 34]** qualifiziert zeitgestempelten Dokumenten (im Sin_ _**-** ne der eIDAS-Verordnung) ) auch Dokumente mit einer fortgeschrittenen Signatur gemäß_ _**[eIDAS-VO, Ar tikel 3 Nr. 11]** oder mit einem fortgeschrittenen Siegel gemäß_ _**[eIDAS-VO, Artikel 3 Nr. 26]** oder mit einem - elektronischen Zeitstempel gemäß_ _**[eIDAS-VO, Artikel 3 Nr. 33]** erfasst, wie sie oft in der internen Kom munikation von Behörden entstehen. Nicht gemeint sind hier Dokumente mit einfachen Signaturen oder Siegeln basierend auf anderen (z. B. nicht-kryptographischen) Verfahren._ 

Bundesamt für Sicherheit in der Informationstechnik 

6 

TR-ESOR-Profil: XAIP mit XBARCH, XDOMEA und PREMIS 

## **3. Profilierung des XML-Schemas für XAIP im Zusammenhang mit XBARCH, XDOMEA und PREMIS für die Behörden der Bundesverwaltung** 

Im Folgenden werden die Anforderungen an ein _XAIP_ gemäß Anhang TR-ESOR F (vgl. **[TR-ESORF])** im Zusammenhang mit **[XBARCH], [XDOMEA] und [PREMIS]** speziell für die Belange in der Bundesverwaltung konkretisiert. Zur besseren Nachvollziehbarkeit sind hier jeweils die Original-Fassung der Anforderungen und die geänderte Fassung (bzw. Erweiterung) aufgeführt. Weiterhin ist für jede geänderte Anforderung eine Begründung angegeben. 

## **3.1 TR-ESOR Anlage F** 

## **3.1.1 Überblick über die XAIP-Datenstruktur – das <XAIP>-Element** 

## **3.1 Überblick über die XAIP-Datenstruktur – das <XAIP>-Element** 

Das <metaDataSection>-Element enthält Metainformationen zur Beschreibung des Geschäftsund Archivierungskontextes, sofern solche vorhanden sind. Die metaDataSection soll alle Informationen enthalten, die zur transparenten und nachhaltigen Interpretation des Geschäfts- und Archivierungskontextes benötigt werden. 

- _**(A3.1-1B) Sofern zusätzliche Metadaten auf Basis von [XDOMEA], [XBARCH] bzw. [PREMIS] vorhanden sind, sollen diese Metadaten im Rahmen dieses Profils, wie im weiteren Verlauf dieses Kapitels ausgeführt, in der metaDataSection des XAIP-Containers gespeichert werden. Andere technische Umsetzungen der Speicherung technische Metadaten bzw. fachliche Metadaten sind zulässig, allerdings muss dann erläutert werden, dass gleichwertige Funktionalität unterstützt wird.**_ 

_**(A3.1-2B) Sofern zusätzliche Absender-Metadaten auf Basis von [XDOMEA], [XBARCH] bzw. [PREMIS] zur Speicherung im Archivdatenobjekt zur Verfügung stehen, sollen diese Metadaten im Rahmen dieses Profils, wie im weiteren Verlauf dieses Kapitels ausgeführt, im Element „Extension“ des „Package Headers“ des XAIP gemäß TR-ESOR-F, Kapitel 3, gespeichert werden. Andere technische Umsetzungen der Speicherung der Absender-Metadaten  sind zulässig, allerdings muss dann erläutert werden, dass gleichwertige Funktionalität unterstützt wird.**_ 

Erläuterung: 

§ 18 RegR bestimmt für die Aufbewahrung von elektronischem Schriftgut, dass durch geeignete Maßnahmen, die nicht näher vorgegeben werden, Vollständigkeit, Integrität, Authentizität und Lesbarkeit zu gewährleisten sind (§ 18 Abs. 1 Satz 2 RegR). Insbesondere müssen die Daten und Dokumente in einer langfristig verkehrsfähigen und standardisierten Form abgelegt werden, so dass die Wiedergabe auf den zum Zeitpunkt der Wiedervorlage gängigen ITSystemen als gesichert angenommen werden kann. Dazu ist insbesondere auch eine „Metadata Preservation Stategy“ mit einer standardisierten Ablage der Metadaten im Archivdatenobjekt erforderlich. 

Bundesamt für Sicherheit in der Informationstechnik 

7 

TR-ESOR-Profil: XAIP mit XBARCH, XDOMEA und PREMIS 

## **3.1.2 Der xaip:packageHeaderType** 

## **3.2 Der xaip:packageHeaderType** 

Die Struktur des **xaip:preservationInfoType** ist folgendermaßen gegeben: […] <status> [optional] Das <status>-Element kannkann Informationen über den Status des Archivdatenobjektes enthalten, die vor dem Löschen des Archivdatenobjektes ausgewertet werden können.[[2]] - Die konkrete Belegung und Auswertung dieses Elementes ist nicht Gegenstand der vorlie genden Spezifikation. Vielmehr sollensollen derartige Festlegungen Gegenstand von XAIP-Pro-filen sein. Es wird empfohlen, solche XAIP-Profile mit dem Bundesamt für Sicherheit in der Informationstechnik abzustimmen. Die Struktur des **xaip:preservationInfoType** ist folgendermaßen gegeben: […] <status> [ ~~optionalr~~ equired] Das <status>-Element kann Informationen über den Status des Archivdatenobjektes enthalten, die vor dem Löschen des Archivdatenobjektes ausgewertet werden können.[3] 

Das <status>-Element kannkann Informationen über den Status des Archivdatenobjektes enthalten, die vor dem Löschen des Archivdatenobjektes ausgewertet werden können.[[2]] - Die konkrete Belegung und Auswertung dieses Elementes ist nicht Gegenstand der vorlie genden Spezifikation. Vielmehr sollensollen derartige Festlegungen Gegenstand von XAIP-Pro-filen sein. Es wird empfohlen, solche XAIP-Profile mit dem Bundesamt für Sicherheit in der Informationstechnik abzustimmen. 

~~Die konkrete Belegung und Auswertung dieses Elementes ist nicht Gegenstand der vorlie genden Spezifikation. Vielmehr sollen derartige Festlegungen Gegenstand von XAIP-Profilen sein. Es wird empfohlen, solche XAIP-Profile mit dem Bundesamt für Sicherheit in der Informationstechnik abzustimmen.~~ 

_**(A3.2-1B)**_ 

_**Dieses Feld muss im vorliegenden Profil den sog. Bewertungsvermerk enthalten. Folgende Werte sind zugelassen:**_ 

- _**A – (archivwürdig) – das Löschen ist erst nach der erfolgreichen Übergabe der -**_ 

- _**Daten an die zuständige Archivbehörde und einer stattgefundenen Löschfrei gabe des öffentlichen Archivs bezogen auf die Kopien im Langzeitspeicher möglich,**_ 

- _**B – (bewerten) – das Löschen ist erst nach einer zuvor stattgefundenen Bewer-**_ 

- _**tung möglich; sollten die Daten als „archivwürdig“ bewertet werden, dann gel ten die entsprechenden Regeln,**_ 

- _**V – (vernichten) – das Löschen ist direkt möglich.**_ 

- _**Der Bewertungsvermerk soll im Archivdatenobjekt gemäß [TR-ESOR-F], Kap. 3.2 vorliegen. Ganz andere technische Umsetzungen bzgl. des Bewertungsvermerks sind zulässig, allerdings muss dann erläutert werden, dass gleichwertige Funktionalität unterstützt wird.**_ 

Erläuterung: 

Für die Behörden sind das Bundesarchivgesetz bzw. die entsprechenden Länderarchivgesetze bzgl. der Anbietungspflicht zu beachten. 

> 2 Mit diesem Element kann insbesondere der im behördlichen Umfeld benötigte “Bewertungsvermerk” realisiert werden. 

> 3 Mit diesem Element kann insbesondere der im behördlichen Umfeld benötigte “Bewertungsvermerk” realisiert werden. 

Bundesamt für Sicherheit in der Informationstechnik 

8 

TR-ESOR-Profil: XAIP mit XBARCH, XDOMEA und PREMIS 

## **3.1.3 Profilierung der XAIP-MetaDataSection im Zusammenhang mit XBARCH und XDOMEA** 

Die TR 03125 TR-ESOR V1.2 lässt es zu, dass eine Profilierung der Metadaten, zum Beispiel _**auf Basis von [XDOMEA], [XBARCH] oder [PREMIS], in der jeweils gültigen Fassung**_ vorgenommen werden kann. 

_**Die in diesem Dokument definierte Profilierung bezieht sich im Wesentlichen auf die Behandlung von elektronischen Akten und anderem elektronischen Schriftgut. Für weitere Arten von aufzubewahrenden Daten können u. U. andere XÖV-Standards besser geeignet sein.**_ 

Die hier vorliegende Profilierung des _XAIP_ auf Basis von _XBARCH_ , _XDOMEA_ und _PREMIS_ sieht die Ablage der folgenden zwei Arten von Metainformationen innerhalb der _Metadaten_ eines _XAIP_ -Containers vor: 

- technischen Metadaten, die sich auf ein innerhalb des _XAIP_ -Containers enthaltenes Datenobjekt beziehen (vgl. Kapitel 3.2), 

- fachliche Metadaten, die bezogen auf ein enthaltenes Datenobjekt dessen fachliche Inhalte näher charakterisieren (vgl. Kapitel 3.3). 

Im Kapitel 3.4 ist ein für dieses Profil geltende Wertebelegung für Kategorisierung und Klassifizierung der Metadaten enthalten. 

Für die technische Umsetzung der Ablage in der _MetaDataSection_ werden hier die folgenden Empfehlungen ausgesprochen. 

**(A3.3-1B)** Jede Instanz von _xaip:dataObject_ , aus _xaip:dataObjectsSection_ (vgl. **[TRESOR-F]** , Kapitel 3.4), soll durch eine Instanz des Elementes _xaip:TechnischeMetadaten_ beschrieben werden. 

Jede Instanz _xaip:credential_ , aus _xaip:credentialsSection_ (vgl. **[TR-ESOR-F]** , Kap. 3.5), die nicht gemäß einem internationalen Standard aufgebaut ist, soll ebenfalls durch eine Instanz des Elementes _xaip:TechnischeMetadaten_ beschrieben werden. 

Eine Empfehlung für den Aufbau des Elementes _xaip:TechnischeMetadaten_ ist dem Kapitel 3.2 zu entnehmen. 

**(A3.3-2B)** Jede Instanz von _xaip:dataObject_ , aus _xaip:dataObjectsSection_ (vgl. **[TRESOR-F]** , Kapitel 3.4), soll durch die Ablage von fachlichen Metadaten beschrieben werden. Eine Empfehlung für den Aufbau der fachlichen Metadaten ist dem Kapitel 3.3 zu entnehmen. 

**(A3.3-3B)** Bei der Ablage der technischen bzw. fachlichen Metadaten müssen die im Kapitel 3.4 beschriebenen Werte für die Attribute _category_ und _classification_ eines Elementes vom Typ _xaip:metaDataObjectType_ benutzt werden. 

**Es gelten derzeit die folgenden Namensräume (namespaces):** 

- „xaip“ - „http://www.bsi.bund.de/tr-esor/xaip/1.2", 

- “[4] 

- „xbarch“ - „http://www.xbarch.de (in der Version 1.4.3), 

- „xdomea“ - „http://www.xdomea.de/V2.2.0“, 

- „premis“ - „info:lc/xmlns/premis-v2“ (in der Version 2.3) 

Wenn der benutzte Namensraum im Falle eines Elementes nicht explizit benannt wurde, dann wird davon ausgegangen, dass der Namensraum „ _xaip_ “ gemeint wird. 

> 4 Momentan handelt es sich hierbei ausschließlich um den Bezeichner eines Namensraums; unter der entsprechenden URL findet sich kein Schema. 

Bundesamt für Sicherheit in der Informationstechnik 

9 

TR-ESOR-Profil: XAIP mit XBARCH, XDOMEA und PREMIS 

## **3.2 Technische Metadaten (optional)** 

Die technischen Metadaten werden mit Hilfe des Elements _xaip:TechnischeMetadaten_ beschrieben. 


![](markdown/tr/BSI_TR_03125_Anlage_XBDP_V1_2_1/BSI_TR_03125_Anlage_XBDP_V1_2_1.pdf-0010-03.png)


## **Abbildung 2: Aufbau des Datentypes xaip:TechnischeMetadatenTyp** 

Die Struktur des Elementes _xaip:TechnischeMetadaten_ ist durch den Datentyp _xaip:TechnischeMetadatenType_ vorgegeben und weist folgenden Aufbau auf: 

## _@TechMetadatenID_ [optional] 

Das _TechMetadatenID_ -Attribut identifiziert eindeutig dieses Element, somit kann auf dieses Element auch eindeutig Bezug genommen werden. 

## _xbarch:Technische_Daten_ [required] 

Das _xbarch:Technische_Daten_ -Element beinhaltet eine technische Beschreibung der Objekte, sowie der für die Langzeitspeicherung/Archivierung notwendigen technischen Maßnahmen gemäß **[XBARCH]** , welches sich stark an den Industriestandard **[PREMIS]** orientiert. 

## _ZusatzTechnischeDaten_ [optional] 

Das _ZusatzTechnischeDaten_ -Element bietet eine Möglichkeit an, zusätzlich technische Daten abzulegen. Das Element beinhaltet nur ein Feld. 

_any_ [optional, unbounded] 

Das _any_ -Element steht für beliebige Elemente aus dem Namensraum “ _premis_ ” und bietet somit eine Möglichkeit an, ggf. die technische Beschreibung durch Einsatz des _PREMIS_ -Standards zu erweitern. 

## **Beispiel:** 

Die Abbildung 3 ist eine beispielhafte Darstellung einer Ablage von technischen Metadaten innerhalb der xaip:metaDataSection. Die Metadaten beziehen sich auf das _XAIP_ -Element mit der ID „ _dataObjectID_10_ “. Zusätzlich zum obligatorischen Element _xbarch:Technische_Daten_ wurde ein Element direkt aus dem _PREMIS_ -Standard innerhalb des Elementes _xaip:ZusatzTechnischeMetadaten_ abgelegt. 

Bundesamt für Sicherheit in der Informationstechnik 

10 

TR-ESOR-Profil: XAIP mit XBARCH, XDOMEA und PREMIS 


![](markdown/tr/BSI_TR_03125_Anlage_XBDP_V1_2_1/BSI_TR_03125_Anlage_XBDP_V1_2_1.pdf-0011-01.png)


## **Abbildung 3: Beispiel einer Ablage von technischen Metadaten.** 

## **3.3 Fachliche Metadaten (optional)** 

Die fachlichen Metadaten werden durch den direkten Einsatz der aus _XDOMEA_ -Standard kommenden Elemente unterstützt. Es wird für die Beschreibung der fachlichen Metadaten keine gesonderte Datenstruktur verwendet. 

## **Beispiel:** 

Die Abbildung 4 stellt ein Beispiel einer Ablage von fachlichen Metadaten dar. Es wurden zwei Elemente aus dem _XDOMEA_ -Standard bezogen auf das _XAIP_ -Element mit der ID „ _dataObjectID_10_ “ abgelegt: 

- xdomea:Aktenplan.Aktenplan.0301, 

- xdomea:Information.Information.0101. 


![](markdown/tr/BSI_TR_03125_Anlage_XBDP_V1_2_1/BSI_TR_03125_Anlage_XBDP_V1_2_1.pdf-0011-09.png)


## **Abbildung 4: Beispiel einer Ablage von fachlichen Metadaten** 

## **3.4 Wertesystem für Kategorisierung und Klassifizierung der Metadaten** 

Die Tabelle 1 führt die  festgelegte Wertebelegung auf, mit der die Attribute _category_ und _classification_ eines Elementes des Datentyps _xaip:metaDataObjectType_ innerhalb dieses 

Bundesamt für Sicherheit in der Informationstechnik 

11 

TR-ESOR-Profil: XAIP mit XBARCH, XDOMEA und PREMIS 

Profils versehen werden sollen. Die Belegung ist aus dem im **[TR-ESOR-F]** , Kapitel 3.3 vorgestellten Wertesystem entnommen worden. 


![](markdown/tr/BSI_TR_03125_Anlage_XBDP_V1_2_1/BSI_TR_03125_Anlage_XBDP_V1_2_1.pdf-0012-02.png)


**----- Start of picture text -----**<br>
Information @category @classification Erläuterung<br>technische Metadaten OTHER - Aufgrund der Heterogenität der in-<br>nerhalb des XBARCH-Standards be-<br>nutzten Datenstrukturen, lässt sich<br>keine präzisere Zuordnung ableiten.<br>fachliche Metadaten DMD DESCRIPTION Fachliche Metadaten, die das refe-<br>renzierendes Objekt näher beschrei-<br>ben.<br>**----- End of picture text -----**<br>


**Tabelle 1: Wertesystem für Kategorisierung und Klassifizierung der Metadaten** 

Bundesamt für Sicherheit in der Informationstechnik 

12 

TR-ESOR-Profil: XAIP mit XBARCH, XDOMEA und PREMIS 

## **4. Anhang A – XML-Schema-Definition** 

## **4.1 XAIP-Schema-Erweiterung** 


![](markdown/tr/BSI_TR_03125_Anlage_XBDP_V1_2_1/BSI_TR_03125_Anlage_XBDP_V1_2_1.pdf-0013-03.png)


## **Abbildung 5: XAIP-Schema erweitert um die Aspekte dieser Profilierung** 

## **4.2 XBarch-Schema-Erweiterung** 

Der überwiegende Anzahl der _XBarch_ -Elemente ist in Form einer inline-Definition abgelegt. Um die innerhalb des _XBarch_ -Standards definierte Beschreibung der technischen Daten verwenden zu können, müssten diese in einer Wrapper-Schema als ein Datentyp redefiniert werden (vgl. Abbildung 6). Die Ausgestaltung der Unterelemente (z. B. _xbarch:objekt_ , _xbarch:agent_ etc.) weicht von der Originaldefinition nicht ab, weshalb auf deren detaillierte Darstellung hier verzichtet wurde. 

Bundesamt für Sicherheit in der Informationstechnik 

13 

TR-ESOR-Profil: XAIP mit XBARCH, XDOMEA und PREMIS 


![](markdown/tr/BSI_TR_03125_Anlage_XBDP_V1_2_1/BSI_TR_03125_Anlage_XBDP_V1_2_1.pdf-0014-01.png)


## **Abbildung 6 Definition des vom XBarch abgeleiteten Typs xbarch:Technische Daten** 

Bundesamt für Sicherheit in der Informationstechnik 

14 


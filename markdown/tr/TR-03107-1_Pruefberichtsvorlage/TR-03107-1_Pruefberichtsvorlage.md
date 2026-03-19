## Ergebnisse der Prüfung gemäß TR03107-1 in Version 1.1.1 

Produkt XY 

Version des Prüfberichtes: 0.15 

Gemäß Prüfberichtsschema in Version: 1.05 11.12.2020 

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn Tel.: +49 22899 9582-0 E-Mail: eid@bsi.bund.de Internet: https://www.bsi.bund.de © Bundesamt für Sicherheit in der Informationstechnik 2020 

Inhaltsverzeichnis 

## Inhaltsverzeichnis 

|1|Einleitung............................................................................................................................................................................................... 7|
|---|---|
|2|Beschreibung des Authentisierungsverfahrens...................................................................................................................8|
|2.1|Allgemeine Angaben.................................................................................................................................................................. 8|
|2.2|Zertifzierungen............................................................................................................................................................................ 8|
|2.3|URLs bzw. Online-Verfügbarkeit..........................................................................................................................................8|
|2.4|Angestrebtes Vertrauensniveau............................................................................................................................................9|
|2.5|Aufistung der eingesetzten Protokolle.............................................................................................................................9|
|2.6|Festlegung des Authentisierungsmittels...........................................................................................................................9|
|2.7|Anwendbarkeit der Module.................................................................................................................................................... 9|
|2.8|Zeitraum der Prüfung............................................................................................................................................................. 10|
|2.9|Annahmen.................................................................................................................................................................................... 10|
|3|Generischer Anforderungskatalog...........................................................................................................................................11|
|3.1|Generische Anforderung G1: Identitätsprüfung nach [TR-03147]....................................................................11|
|3.2|Generische Anforderung G2: Ausgabe nur an berechtigte Inhaber...................................................................11|
|3.3|Generische Anforderung G3: Explizite Aktivierung.................................................................................................11|
|3.4|Generische Anforderung G4: Geschäftsbedingungen und Verhaltensregeln...............................................11|
|3.5|Generische Anforderung G5: Änderungen der Geschäftsbedingungen..........................................................11|
|3.6|Generische Anforderung G6: Sicherheit des Authentisierungsprotokolls.....................................................12|
|3.7|Generische Anforderung G7: Forward Secrecy...........................................................................................................12|
|3.8|Generische Anforderung G8: Dynamisches Authentisierungsprotokoll........................................................12|
|3.9|Generische Anforderung G9: Sperrung..........................................................................................................................12|
|3.10|Generische Anforderung G10: Übermittlung der Sperrmeldung.......................................................................13|
|3.11|Generische Anforderung G11: Attributsänderung....................................................................................................13|
|3.12|Generische Anforderung G12: Absicherung von Kommunikationsbeziehungen......................................13|
|3.13|Generische Anforderung G13: Kryptographie.............................................................................................................13|
|3.14|Generische Anforderung G14: Speicherung privater Schlüssel...........................................................................14|
|3.15|Generische Anforderung G15: Speicherung öffentlicher Schlüssel..................................................................14|
|3.16|Generische Anforderung G16: Agilität............................................................................................................................14|
|3.17|Generische Anforderung G17: Nutzerumgebung......................................................................................................14|
|3.18|Generische Anforderung G18: Eindeutige Inhaberidentifzierung...................................................................14|
|3.19|Generische Anforderung G19: Geheimhaltung der Nutzerkennung................................................................15|
|3.20|Generische Anforderung G20: Dienstbindung an den Sitzungskontext.........................................................15|
|3.21|Generische Anforderung G21: Nutzerbindung an den Sitzungskontext........................................................15|
|3.22|Generische Anforderung G22: Übermittlung der Identitätsattribute..............................................................15|
|3.23|Generische Anforderung G23: Identifzierung des Dienstes.................................................................................15|
|3.24|Generische Anforderung G24: Multi-Faktor................................................................................................................16|
|3.25|Generische Anforderung G25: Widerstandsfähigkeit des Authentisierungsmittels..................................16|
|4|Prüfobjektspezifsche Module....................................................................................................................................................17|
|4.1|Anforderungskatalog zu Stellen.........................................................................................................................................17|
|4.1.1|Spezifsche Anforderung S1: Stellen..........................................................................................................................17|



Bundesamt für Sicherheit in der Informationstechnik 

3 

Inhaltsverzeichnis 

|4.2|Anforderungskatalog zum Authentisierungsmittel Besitz....................................................................................17|
|---|---|
|4.2.1<br>4.2.2|Spezifsche Anforderung B1: Ausgabe des Tokens..............................................................................................17<br>Spezifsche Anforderung B2: Anforderungen an den Token..........................................................................17|
|4.2.3|Spezifsche Anforderung B3: Besondere Anforderungen für das Vertrauensniveau „hoch“...........18|
|4.3|Anforderungskatalog zum Authentisierungsmittel Wissen.................................................................................18|
|4.3.1<br>4.3.2|Spezifsche Anforderung W1: Ausgabe des Wissens...........................................................................................18<br>Spezifsche Anforderung W2: Anforderungen an das Wissen.......................................................................18|
|4.3.3<br>4.3.4|Spezifsche Anforderung W3: Passwortgebrauch................................................................................................18<br>Spezifsche Anforderung W4: Passwortentropie.................................................................................................18|
|4.4|Anforderungskatalog zum Authentisierungsmittel Biometrie...........................................................................19|
|4.4.1|Spezifsche Anforderung Bio1: Anforderungen an die Biometrie...............................................................19|
|4.4.2|Spezifsche Anforderung Bio2: Sicherheit Biometrie........................................................................................19|
|4.5|Anforderungskatalog zu Multi-Faktor Authentisierung........................................................................................19|
|4.5.1<br>4.5.2|Spezifsche Anforderung MF1: Verknüpfung Sicherungsfaktoren.............................................................19<br>Spezifsche Anforderung MF2: Fehlschlagen eines Faktors............................................................................19|
|4.5.3<br>4.5.4|Spezifsche Anforderung MF3: Resistenz beider Faktoren..............................................................................19<br>GenerischeSpezifsche Anforderung MF4: Ausgabe über getrennte Übermittlungswege...............20|
|4.6|Anforderungskatalog zum Authentisierungsmittel eID.........................................................................................20|
|4.6.1|Spezifsche Anforderung eID1: eID-Funktion.......................................................................................................20|
|4.7|Anforderungskatalog zum Authentisierungsmittel Softwaretoken.................................................................20|
|4.7.1<br>4.7.2|Spezifsche Anforderung SW1: Schlüsselspeicherung......................................................................................20<br>Spezifsche Anforderung SW2: Erzeugung und Löschung der Schlüssel.................................................20|
|4.8|Anforderungskatalog zum Authentisierungsmittel OTP.......................................................................................20|
|4.8.1<br>4.8.2|Spezifsche Anforderung OTP1: TANs......................................................................................................................20<br>Spezifsche Anforderung OTP2: TAN-Generatoren...........................................................................................21|
|4.9|Anforderungskatalog zum Authentisierungsmittel smsTAN...............................................................................21|
|4.9.1<br>4.9.2<br>4.9.3|Spezifsche Anforderung sms1: Registrierung der SIM....................................................................................21<br>Spezifsche Anforderung sms2: Displaysperre......................................................................................................21<br>Spezifsche Anforderung sms3: Getrennter Kanal..............................................................................................21|
|4.10|Anforderungskatalog zur Reaktivierung........................................................................................................................22|
|4.10.1<br>4.10.2|<br>Spezifsche Anforderung R1: Identifzierung........................................................................................................22<br> <br>Spezifsche Anforderung R2: Kompromittierung...............................................................................................22|
|5|Ergebnis der Prüfung..................................................................................................................................................................... 23|
|5.1|Vertrauensniveau des Prüfobjekts.....................................................................................................................................23|
|5.2|Begründung................................................................................................................................................................................. 23|
|6|Informationen zu den Prüfern..................................................................................................................................................24|
|7|Anhang.................................................................................................................................................................................................. 25|
|7.1|Fragebogen zur allgemeinen Beschreibung des Authentisierungsverfahrens.............................................25|
|7.1.1|Allgemeine Angaben......................................................................................................................................................... 25|
|7.1.2|Zertifzierungen................................................................................................................................................................... 25|
|7.1.3|URLs bzw. Online-Verfügbarkeit.................................................................................................................................26|
|7.1.4|Allgemeine Beschreibung des Prüfobjekts.............................................................................................................26|
|7.1.5|Angestrebtes Vertrauensniveau...................................................................................................................................26|
|7.1.6|Aufistung der eingesetzten Protokolle....................................................................................................................26|
|7.1.7|Festlegung des Authentisierungsmittels.................................................................................................................27|
|7.1.8|Nutzung von externen Stellen......................................................................................................................................27|
|7.1.9|Reaktivierung....................................................................................................................................................................... 27|
|7.2|Prüfobjektbezogener Fragenkatalog................................................................................................................................27|



Bundesamt für Sicherheit in der Informationstechnik 

4 

Inhaltsverzeichnis 

|7.2.1|Generische Fragen.............................................................................................................................................................. 27|
|---|---|
|7.2.2|Fragen zu Stellen................................................................................................................................................................. 32|
|7.2.3|Fragen zum Authentisierungsmittel Besitz............................................................................................................34|
|7.2.4|Fragen zum Authentisierungsmittel Wissen.........................................................................................................34|
|7.2.5|Fragen zum Authentisierungsmittel Biometrie...................................................................................................36|
|7.2.6|Fragen zur Multi-Faktor Authentisierung..............................................................................................................36|
|7.2.7|Fragen zum Authentisierungsmittel eID.................................................................................................................37|
|7.2.8|Fragen zum Authentisierungsmittel Softwaretoken.........................................................................................37|
|7.2.9|Fragen zum Authentisierungsmittel OTP...............................................................................................................38|
|7.2.10|<br>Fragen zum Authentisierungsmittel smsTAN.......................................................................................................38|
|7.2.11|<br>Fragen zur Reaktivierung...............................................................................................................................................39|
||Literaturverzeichnis........................................................................................................................................................................ 40|



## Tabellenverzeichnis 

Tabelle 1: Anwendbarkeit von Modulen.............................................................................................................................................10 Tabelle 2: Generische Fragen.................................................................................................................................................................... 31 Tabelle 3: Fragen zu Stellen....................................................................................................................................................................... 32 Tabelle 4: Fragen zum Authentisierungsmittel Besitz..................................................................................................................33 Tabelle 5: Fragen zum Authentisierungsmittel Wissen...............................................................................................................35 Tabelle 6: Fragen zum Authentisierungsmittel Biometrie.........................................................................................................35 Tabelle 7: Fragen zur Multi-Faktor Authentisierung....................................................................................................................36 Tabelle 8: Fragen zum Authentisierungsmittel eID.......................................................................................................................36 Tabelle 9: Fragen zum Authentisierungsmittel Softwaretoken...............................................................................................37 Tabelle 10: Fragen zum Authentisierungsmittel OTP..................................................................................................................38 Tabelle 11: Fragen zum Authentisierungsmittel smsTAN..........................................................................................................38 Tabelle 12: Fragen zur Reaktivierung...................................................................................................................................................39 

Bundesamt für Sicherheit in der Informationstechnik 

5 

Einleitung 1 

## 1 Einleitung 

Die [TR-03107-1] bewertet Verfahren zu elektronischen Identitäten und Vertrauensdiensten für verschiedene Prozesse des E-Governments. Die Kriterien sollen es ermöglichen, diese Verfahren zu definierten Vertrauensniveaus zuzuordnen. Dafür werden unterschiedliche Kriterien betrachtet, die generisch oder spezifisch für einen bestimmten Prozess sind. Im Rahmen des Prüfverfahrens wurden die relevanten Kriterien auf das in diesem Dokument betrachtete Prüfobjekt angewendet und die Ergebnisse ausgewertet. Eine maßgebliche Rolle spielen hierbei die Angaben des Verfahrensbetreibers sowie Zertifizierungen, welche im Rahmen der Prüfung herangezogen wurden und als Grundlage der Bewertung dienen. 

Der vorliegende Prüfbericht gliedert sich in mehrere Abschnitte, welche sich jeweils mit den unterschiedlichen zu dem Prüfobjekt gehörenden Komponenten befassen. Er beinhaltet und bewertet nur diejenigen Anforderungen der [TR-03107-1], welche auch tatsächlich für das zu analysierende Prüfobjekt relevant sind. Weiterhin werden nur Authentisierungs- und Identifizierungsprozesse im E-Government betrachtet. Prozesse zum Zweck der Abgabe einer Willenserklärung oder zur Dokumentenübermittlung werden hier nicht berücksichtigt. Dies stellt jedoch keine Einschränkung hinsichtlich der zu betrachtenden „Mechanismen / Funktionen“ oder „Kriterien“ gemäß der [TR-03107-1] dar. Als Identifizierung wird in diesem Dokument sowohl die Identifizierung von Personen, als auch von Diensteanbietern verstanden. 

Sämtliche Referenzen in diesem Dokument beziehen sich, soweit nicht anderweitig erwähnt, auf die zugrunde liegende Version der [TR-03107-1]. Die Bewertungsgrundlage für die hier dokumentierten Ergebnisse stellt, neben dieser Technischen Richtlinie selbst, insbesondere auch [Bew/TR-03107] in der zugehörigen Version dar. 

Bundesamt für Sicherheit in der Informationstechnik 

7 

2 Beschreibung des Authentisierungsverfahrens 

## 2 Beschreibung des Authentisierungsverfahrens 

Dieser Prüfbericht bezieht sich auf eine konkrete Ausprägung des analysierten Verfahrens. Dies bedeutet, dass das Ergebnis einen eindeutigen Bezug zu einem bestimmten Prüfobjekt (Authentisierungsverfahren in einer bestimmten Konfiguration mitsamt dem zugehörigen E-Government-Onlinedienst) eines bestimmten Betreibers hat. Insbesondere sind die Ergebnisse nicht notwendigerweise auf andere Ausprägungen des Authentisierungsverfahrens, z. B. andere Versionsnummern oder Konfigurationen, übertragbar. Die untersuchte Konstellation ist in diesem Kapitel eindeutig festgehalten. 

## 2.1 Allgemeine Angaben 

Hier werden die allgemeinen Angaben zum Prüfobjekt aufgeführt. Die Prüfung bezieht sich ausschließlich auf folgendes Authentisierungsverfahren: 

- Angaben zum Verfahrensbetreiber 

   - __________________________________________________________________________________________________________ 

- Kontaktdaten des technischen Ansprechpartners auf Seiten des Verfahrensbetreibers 

__________________________________________________________________________________________________________ 

- Name und Versionsnummer des Prüfobjekts 

__________________________________________________________________________________________________________ 

- Auflistung aller Module des Prüfobjekts mit Namen und Version 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

## 2.2 Zertifizierungen 

Falls das Prüfobjekt oder von diesem verwendete Bestandteile bereits zertifiziert wurden (Common Criteria, ISO, IT-Grundschutz, Technische Richtlinien, Pentests etc.), sind diese Zertifizierungen im Folgenden aufgeführt. 

- Das Produkt besitzt folgende Zertifizierungen 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

## 2.3 URLs bzw. Online-Verfügbarkeit 

Die Prüfung bezieht sich auf ein Prüfobjekt, welches den Nutzern Zugriff auf Dienste im E-Government-Bereich anbietet und besitzt dementsprechend Onlineschnittstellen, die bei der Prüfung zu berücksichtigen sind. Im Folgenden sind sämtliche URLs angeben, welche dabei benutzt werden. 

- Das Produkt steht unter folgenden URLs zur Verfügung 

Bundesamt für Sicherheit in der Informationstechnik 

8 

Beschreibung des Authentisierungsverfahrens 2 

## 2.4 Angestrebtes Vertrauensniveau 

Bitte legen Sie fest, für welches Vertrauensniveau Sie eine Prüfung Ihres Verfahrens anvisieren. Ohne Angaben kann das höchstmögliche Vertrauensniveau in der Prüfung ermittelt werden. Dies kann allerdings erheblichen zeitlichen und organisatorischen Zusatzaufwand verursachen. 

_normal_ [  ] 

_substantiell_ [  ] 

_hoch_ [  ] 

## 2.5 Auflistung der eingesetzten Protokolle 

Bei einem Authentisierungsverfahren kommen meistens mehrere Protokolle zum Einsatz (z. B. TLS, SAML, Kerberos etc.). Um einen Überblick über die relevanten Protokolle zu geben, listen Sie bitte diese auf. Bitte ergänzen Sie nach Möglichkeit entsprechende Zusatzinformationen (z. B. SAML mit WebSSO-Profil). 

- Das Produkt verwendet folgende Protokolle 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

## 2.6 Festlegung des Authentisierungsmittels 

Falls Ihr Authentisierungsverfahren mehrere Authentisierungsmittel unterstützt (z. B. Benutzername/Passwort, Softwaretoken und Hardwaretoken), muss hier eine Festlegung getroffen werden, welches Mittel als Grundlage für die Bewertung gelten soll. Eine Feststellung des Sicherheitsniveaus bezieht sich dann genau auf dieses bestimmte Authentisierungsmittel. Sollten mehrere Authentisierungsmittel bewertet werden, so müssen separate Vertrauensniveaubewertungen durchgeführt werden. 

- Die Vertrauensniveaubewertung bezieht sich auf folgendes Authentisierungsmittel 

__________________________________________________________________________________________________________ 

## 2.7 Anwendbarkeit der Module 

Für die Feststellung des Vertrauensniveaus werden unterschiedliche Aspekte des Authentisierungsverfahrens betrachtet, die in mehrere spezifische Module unterteilt sind. Meistens sind nicht alle diese Aspekte auf ein bestimmtes Authentisierungsverfahren anwendbar. So ist z. B. das Modul zum Authentisierungsmittel Biometrie nur dann relevant, wenn Biometrie tatsächlich für die Authentisierung zum Einsatz kommt. Andernfalls muss dieses Modul ausgeblendet werden. 

In diesem Abschnitt soll die Anwendbarkeit von spezifischen Modulen auf das Prüfobjekt beschrieben werden. Dabei soll klar ersichtlich sein, warum ein bestimmtes Modul anwendbar oder nicht anwendbar ist. Die nicht anwendbaren Module bleiben dann bei der Prüfung unberücksichtigt. Zu beachten ist, dass die generischen Anforderungen so definiert sind, dass sie grundsätzlich immer anwendbar sind. Die Entscheidung betrifft daher nur spezifische Module. 

Bundesamt für Sicherheit in der Informationstechnik 

9 

2 Beschreibung des Authentisierungsverfahrens 

|**Modul**|**Anwendbarkeit**|**Begründung**|
|---|---|---|
|Stellen|||
|Authentisierungsmittel Besitz|||
|Authentisierungsmittel Wissen|||
|Authentisierungsmittel Biometrie|||
|Multi-Faktor Authentisierung|||
|Authentisierungsmittel eID|||
|Authentisierungsmittel Softwaretoken|||
|Authentisierungsmittel OTP|||
|Authentisierungsmittel smsTAN|||
|Reaktivierung|||



_Tabelle 1: Anwendbarkeit von Modulen_ 

## 2.8 Zeitraum der Prüfung 

Die Prüfung fand vom TT.MM.JJJJ bis zum TT.MM.JJJJ statt. 

## 2.9 Annahmen 

Folgende Annahmen gelten für die in diesem Prüfbericht beschriebenen Ergebnisse. 

|**ID**|**Annahme**|
|---|---|
|A.1||



Bundesamt für Sicherheit in der Informationstechnik 

10 

Generischer Anforderungskatalog 3 

## 3 Generischer Anforderungskatalog 

Dieses Kapitel beinhaltet mechanismenübergreifende Anforderungen, welche für sämtliche Verfahren relevant sind. 

## 3.1 Generische Anforderung G1: Identitätsprüfung nach [TR-03147] 

**Referenz** : 3.2.1 Identitätsprüfung 

**Anforderung** : Die Identitätsprüfung wurde gemäß den Anforderungen aus [TR-03147] bewertet. 

**Bewertung:** 

**Begründung:** 

## 3.2 Generische Anforderung G2: Ausgabe nur an berechtigte Inhaber 

**Referenz** : 3.2.2 Ausgabe der Authentisierungsmittel 

**Anforderung** : _Es muss sichergestellt werden, dass Authentisierungsmittel nur an den berechtigten Inhaber ausgegeben werden._ 

**Bewertung** : 

**Begründung** : 

## 3.3 Generische Anforderung G3: Explizite Aktivierung 

**Referenz** : 3.2.2 Ausgabe der Authentisierungsmittel 

**Anforderung** : _Für das Vertrauensniveau hoch ist eine explizite Aktivierung der Authentisierungsmittel durch den Inhaber notwendig. Die Aktivierung muss so gestaltet sein, dass sie nur durch den berechtigten Inhaber erfolgt bzw. dieser zuverlässig eine unberechtigte Aktivierung erkennen kann._ 

**Bewertung** : 

**Begründung** : 

## 3.4 Generische Anforderung G4: Geschäftsbedingungen und Verhaltensregeln 

**Referenz** : 3.2.3 Informationen für den Inhaber 

**Anforderung** : _Dem Inhaber der Authentisierungsmittel müssen in geeigneter Weise die Geschäftsbedingungen sowie notwendige Verhaltensregeln zum Umgang mit den Authentisierungsmitteln übermittelt werden._ 

**Bewertung** : 

**Begründung** : 

## 3.5 Generische Anforderung G5: Änderungen der Geschäftsbedingun- 

## gen 

**Referenz** : 3.2.3 Informationen für den Inhaber 

Bundesamt für Sicherheit in der Informationstechnik 

11 

3 Generischer Anforderungskatalog 

**Anforderung** : _Dem Inhaber der Authentisierungsmittel müssen in geeigneter Weise die Geschäftsbedingungen sowie notwendige Verhaltensregeln zum Umgang mit den Authentisierungsmitteln übermittelt werden. Wenn sich die Geschäftsbedingungen oder notwendigen Verhaltensregeln ändern, müssen alle betroffenen Stellen und insbesondere der Authentisierungsmittelinhaber geeignet über die Änderungen informiert werden._ 

**Bewertung** : 

**Begründung** : 

## 3.6 Generische Anforderung G6: Sicherheit des Authentisierungsproto- 

## kolls 

**Referenz** : 3.3.2 Authentisierungsprotokoll 

**Anforderung** : _Das Authentisierungsprotokoll muss gegen Angreifer mit Angriffspotential gemäß Abschnitt 3.1 sicher sein._ 

**Bewertung** : 

**Begründung** : 

## 3.7 Generische Anforderung G7: Forward Secrecy 

**Referenz** : 3.3.2 Authentisierungsprotokoll 

**Anforderung** : _Sofern für einen Mechanismus die Vertraulichkeit ein Sicherheitsziel ist, so sollen kryptographische Verfahren eingesetzt werden, die Vorwärtssicherheit (Forward Secrecy) bieten._ 

**Bewertung** : 

**Begründung** : 

## 3.8 Generische Anforderung G8: Dynamisches Authentisierungsproto- 

## koll 

**Referenz** : 3.3.2 Authentisierungsprotokoll 

**Anforderung** : _Für die Vertrauensniveaus substantiell und hoch muss das Authentisierungsprotokoll dynamisch sein, d.h. das Verfahren muss dazu geeignet sein nachzuweisen, dass sich die Authentisierungsmittel im Augenblick der Authentisierung unter Kontrolle des Inhabers befinden. Dieser Nachweis muss für jede Authentisierung neu erzeugt werden._ 

**Bewertung** : 

**Begründung** : 

## 3.9 Generische Anforderung G9: Sperrung 

**Referenz** : 3.4 Rückruf/Sperrung, 3.4.1 Sperrung 

**Anforderung** : _Im Falle der Kompromittierung von Authentisierungsmitteln muss es dem Inhaber möglich sein, die Authentisierungsmittel zu sperren;_ 

_Für alle Vertrauensniveaus muss der Rückruf bzw. Sperrung von Authentisierungsmitteln durch den Inhaber möglich sein._ 

**Bewertung** : 

## **Begründung** : 

Bundesamt für Sicherheit in der Informationstechnik 

12 

Generischer Anforderungskatalog 3 

## 3.10 Generische Anforderung G10: Übermittlung der Sperrmeldung 

**Referenz** : 3.4.1 Sperrung 

**Anforderung** : _Die Möglichkeit zur Übermittlung der Sperrmeldung muss über öffentliche Kommunikationswege verfügbar sein und den Inhabern von Authentisierungsmitteln in geeigneter Weise bekannt gemacht werden._ 

**Bewertung** : 

**Begründung** : 

## 3.11 Generische Anforderung G11: Attributsänderung 

**Referenz** : 3.4 Rückruf/Sperrung, 3.2.1 Identitätsprüfung 

**Anforderung** : _Ein Rückruf von Authentisierungsmitteln ist auch dann notwendig, wenn die authentisierten Identitätsattribute nicht mehr gültig sind (z. B. Namensänderung) oder der Inhaber nicht mehr zum Besitz berechtigt ist._ 

_Sowohl für externe als auch interne Attribute muss festgelegt sein, inwiefern deren Gültigkeit erlischt, wenn sich die zugrunde liegende nachgewiesene Identität der Entität ändert._ 

**Bewertung** : 

**Begründung** : 

## 3.12 Generische Anforderung G12: Absicherung von Kommunikationsbeziehungen 

**Referenz** : 3.6 Absicherung von Kommunikationsbeziehungen 

**Anforderung** : Diverse Anforderungen aus Abschnitt 3.6 aus [TR-03107-1] „ _Absicherung von Kommunikationsbeziehungen_ “. 

_Für das Vertrauensniveau normal ist eine Absicherung der Kommunikation zwischen den beteiligten Stellen auf Transportebene ausreichend._ 

_Für die Vertrauensniveaus substantiell und hoch ist eine Ende-zu-Ende-Beziehung zwischen den beteiligten Stellen notwendig._ 

**Bewertung** : 

**Begründung** : 

## 3.13 Generische Anforderung G13: Kryptographie 

**Referenz** : 3.7 Kryptographie 

**Anforderung** : _Für verschiedene Mechanismen werden konkrete kryptographische Anforderungen in den verschiedenen Teilen der [TR-03116] festgelegt, die jeweils in den Beschreibungen der Mechanismen referenziert werden. Sofern die [TR-03116] für einen Mechanismus keine Vorgaben enthält, so sind die Anforderungen aus [TR-02102] einzuhalten._ 

**Bewertung** : 

**Begründung** : 

Bundesamt für Sicherheit in der Informationstechnik 

13 

3 Generischer Anforderungskatalog 

## 3.14 Generische Anforderung G14: Speicherung privater Schlüssel 

**Referenz** : 3.7.1 Schlüsselspeicherung 

**Anforderung** : _Private kryptographische Schlüssel aller Entitäten eines Authentisierungssystems (einschließlich des Inhabers von Authentisierungsmitteln) müssen sicher, das heißt vertraulich, gespeichert werden. Dies setzt voraus, dass der private Schlüssel gegen Kopieren geschützt ist und die Verwendung des Schlüssels durch Unberechtigte verhindert wird._ 

**Bewertung** : 

**Begründung** : 

## 3.15 Generische Anforderung G15: Speicherung öffentlicher Schlüssel 

**Referenz** : 3.7.1 Schlüsselspeicherung 

**Anforderung** : _[...] müssen öffentliche Schlüssel, die für die Authentifizierung genutzt werden, sicher, also gegen Manipulation geschützt, gespeichert werden._ 

**Bewertung** : 

**Begründung** : 

## 3.16 Generische Anforderung G16: Agilität 

**Referenz** : 3.7.2 Agilität 

**Anforderung** : _Die kryptographischen Verfahren müssen so gestaltet sein, dass sie neuen kryptographischen Erkenntnissen angepasst werden können._ 

**Bewertung** : 

**Begründung** : 

## 3.17 Generische Anforderung G17: Nutzerumgebung 

**Referenz** : 3.8 Anforderungen an die Nutzerumgebung 

**Anforderung** : _Es muss sichergestellt werden, dass die Mechanismen mit entsprechend den Empfehlungen [des BSI für Bürger zur Absicherung des lokalen Endgeräts] konfigurierten Rechnern verwendbar sind, Mechanismen dürfen keine Anforderungen stellen, die den Empfehlungen des BSI [für Bürger zur Absicherung des lokalen_ Endgeräts _] widersprechen._ 

**Bewertung** : 

**Begründung** : 

## 3.18 Generische Anforderung G18: Eindeutige Inhaberidentifizierung 

**Referenz** : 4 Authentisierungsverfahren 

**Anforderung** : _Authentisierungsverfahren müssen den Inhaber der Authentisierungsmittel gegenüber der Gegenstelle eindeutig identifizieren (üblicherweise durch die Registrierung einer eindeutigen Kennung des Authentisierungsmittels bei der Gegenstelle)._ 

**Bewertung** : 

**Begründung** : 

Bundesamt für Sicherheit in der Informationstechnik 

14 

Generischer Anforderungskatalog 3 

## 3.19 Generische Anforderung G19: Geheimhaltung der Nutzerkennung 

**Referenz** : 4 Authentisierungsverfahren 

**Anforderung** : _Das Authentisierungsverfahren muss einerseits diese Kennung der Gegenstelle gegenüber entsprechend der Anforderungen des jeweiligen Vertrauensniveaus nachweisen, Dritten darf die Kennung aus Datenschutzgründen aber nicht bekannt werden._ 

**Bewertung** : 

**Begründung** : 

## 3.20 Generische Anforderung G20: Dienstbindung an den Sitzungskon- 

## text 

**Referenz** : 6.2.3 Bindung der Identifizierung an den Sitzungskontext 

**Anforderung** : _Als Bestandteil des Aufbaus eines Sitzungskontextes muss sichergestellt werden, dass die Identifizierungen des Dienstes an diese Sitzung gebunden werden. Dies umfasst, dass die Identität eindeutig einer bestimmten Session und nicht lediglich einem bestimmten Kommunikationsendpunkt zugeordnet werden muss und auch nur dort gültig sein darf. Für die Vertrauensniveaus substantiell/hoch muss diese Bindung über geeignete technische/kryptographische Mechanismen erfolgen, etwa kryptographisch sichere Session-Identifier/-Cookies._ 

**Bewertung** : 

**Begründung** : 

## 3.21 Generische Anforderung G21: Nutzerbindung an den Sitzungskon- 

## text 

**Referenz** : 5.2.3 Bindung der Identifizierung an den Sitzungskontext 

**Anforderung** : _Die übertragene Identität muss an den Sitzungskontext gebunden werden. Dies bedeutet unter anderem, dass die Identität einer Person eindeutig einer bestimmten Session und nicht lediglich einem bestimmten Kommunikationsendpunkt zugeordnet werden muss und auch nur dort gültig sein darf. Für die Vertrauensniveaus substantiell/hoch muss diese Bindung über geeignete technische/kryptographische Mechanismen erfolgen._ 

**Bewertung** : 

**Begründung** : 

## 3.22 Generische Anforderung G22: Übermittlung der Identitätsattribute 

**Referenz** : 5.2.4 Vertraulichkeit der Identitätsattribute 

**Anforderung** : _Es muss sichergestellt sein, dass Identitätsattribute erst nach erfolgter Freigabe durch die Person übermittelt werden._ 

**Bewertung** : 

**Begründung** : 

## 3.23 Generische Anforderung G23: Identifizierung des Dienstes 

**Referenz** : 5.2.2 Identifizierung des Dienstanbieters, 5.2.4 Vertraulichkeit der Identitätsattribute 

Bundesamt für Sicherheit in der Informationstechnik 

15 

3 Generischer Anforderungskatalog 

**Anforderung** : _Eine vorhergehende Identifizierung des Dienstes (und damit verbunden der Aufbau einer sicheren Verbindung) ist Voraussetzung für die nachfolgenden Kriterien und muss daher mindestens mit dem angestrebten Vertrauensniveau der Identifizierung einer Person erfolgen;_ 

_Die Vertraulichkeit der Identitätsattribute einer Person setzt eine Identifizierung des empfangenden Dienstanbieters auf gleichem Vertrauensniveau wie die Identifizierung der Person voraus._ 

**Bewertung** : 

**Begründung** : 

## 3.24 Generische Anforderung G24: Multi-Faktor 

**Referenz** : 3.3.1.4 Zwei-Faktor-Authentifizierung 

**Anforderung** : _Zur Erreichung des Vertrauensniveaus substantiell ist grundsätzlich die Nutzung von zwei Faktoren zur Absicherung der Authentisierungsmittel notwendig, die die alleinige Kontrolle des Nutzers über seine Authentisierungsmittel sicherstellen. Dabei müssen die beiden Faktoren unterschiedlichen Kategorien angehören._ 

**Bewertung** : 

**Begründung** : 

## 3.25 Generische Anforderung G25: Widerstandsfähigkeit des Authentisierungsmittels 

**Referenz** : 3.3.1 Authentisierungsmittel 

**Anforderung** : _Die Authentisierungsmittel müssen so gestaltet werden, dass der berechtigte Inhaber sie gegen Missbrauch durch Dritte mit Angriffspotential gemäß Abschnitt 3.1 schützen kann._ 

_Für Vertrauensniveau hoch müssen die Authentisierungsmittel gegen Duplizierung und Manipulation durch Angreifer mit hohem Angriffspotential (siehe Abschnitt 3.1) geschützt sein_ 

**Bewertung** : 

**Begründung** : 

Bundesamt für Sicherheit in der Informationstechnik 

16 

Prüfobjektspezifische Module  4 

## 4 Prüfobjektspezifische Module 

Dieses Kapitel beinhaltet diejenigen spezifischen Anforderungen aus [TR-03107-1], welche für das Prüfobjekt relevant sind. 

## 4.1 Anforderungskatalog zu Stellen 

## 4.1.1 Spezifische Anforderung S1: Stellen 

## **Referenz** : 3.5 Vertrauenswürdigkeit von Stellen 

**Anforderung** : _Bei den meisten Mechanismen übernehmen – neben dem Inhaber der Authentisierungsmittel und der vertrauenden Entität – weitere Stellen für die Sicherheit des Mechanismus relevante Aufgaben, zum Beispiel Enrolment, Identitätsprüfung und Ausgabe der Authentisierungsmittel (Abschnitt 3.2), Sicherung von Kommunikationsbeziehungen (Abschnitt 3.6) oder Speicherung von Daten. Auch Identitätsprovider sind Stellen in diesem Sinne._ 

_Sämtliche Stellen müssen_ 

- _Behörden oder juristische Personen sein und rechtlich befugt sein, die jeweilige Aufgabe wahrzunehmen;_ 

- _für ihre jeweiligen wahrgenommen Aufgaben ein Regelwerk aufstellen und dieses einhalten;_ 

- _organisatorisch und technisch in der Lage sein, die Aufgaben auf Basis des Regelwerks wahrzunehmen;_ 

- _genügend Ressourcen für die Erfüllung der Aufgaben und ggf. die Übernahme der sich aus den Aufgaben ergebende Haftung haben; und_ 

_ein Informationssicherheitsmanagementsystem auf Basis etablierter Standards (z. B. IT-Grundschutz [BSI100-2] oder [ISO27001]) nutzen._ 

**Bewertung** : 

**Begründung** : 

## 4.2 Anforderungskatalog zum Authentisierungsmittel Besitz 

## 4.2.1 Spezifische Anforderung B1: Ausgabe des Tokens 

## **Referenz** : 3.2.2 Ausgabe der Authentisierungsmittel 

**Anforderung** : _Die Ausgabe eines auf Besitz basierenden Sicherungsmittels muss so erfolgen, dass der berechtigte Inhaber nach Erhalt erkennen kann, ob das Sicherungsmittel unberechtigt benutzt wurde [...]_ 

**Bewertung** : 

**Begründung** : 

## 4.2.2 Spezifische Anforderung B2: Anforderungen an den Token 

## **Referenz** : 3.3.1 Authentisierungsmittel 

**Anforderung** : _Anforderungen aus Tabelle 3 in [TR-03107-1]: Eigenschaften von Authentisierungsfaktoren_ 

**Bewertung** : 

## **Begründung** : 

Bundesamt für Sicherheit in der Informationstechnik 

17 

4 Prüfobjektspezifische Module 

## 4.2.3 Spezifische Anforderung B3: Besondere Anforderungen für das Vertrauensniveau „hoch“ 

**Referenz** : 3.3.1.1 Besitz 

**Anforderung** : _Für das Vertrauensniveau hoch muss der Token auch gegen Veränderung (Manipulation) durch Angreifer mit hohem Angriffspotential geschützt sein. Darüber hinaus muss der Inhaber sicherstellen können, dass der Besitztoken nur für eine intendierte Authentisierung aktiviert wird._ 

**Bewertung** : 

## **Begründung** : 

## 4.3 Anforderungskatalog zum Authentisierungsmittel Wissen 

## 4.3.1 Spezifische Anforderung W1: Ausgabe des Wissens 

**Referenz** : 3.2.2 Ausgabe der Authentisierungsmittel 

**Anforderung** : _Die Ausgabe von wissensbasierten Sicherungsmitteln muss so erfolgen, dass der Inhaber unberechtigte Kenntnisnahme erkennen kann (Unversehrtheit des „PIN-Briefes“)_ 

**Bewertung** : 

**Begründung** : 

## 4.3.2 Spezifische Anforderung W2: Anforderungen an das Wissen 

**Referenz** : 3.3.1 Authentisierungsmittel 

**Anforderung** : _Anforderungen aus Tabelle 3 in [TR-03107-1]: Eigenschaften von Authentisierungsfaktoren_ 

**Bewertung** : 

**Begründung** : 

## 4.3.3 Spezifische Anforderung W3: Passwortgebrauch 

**Referenz** : 3.3.1.2 Wissen 

**Anforderung** : _Bei Nutzung von Wissen als alleinigem Sicherungsfaktor sind die Anforderungen aus Maßnahme M 2.11 „Regelung des Passwortgebrauchs“ der IT-Grundschutz-Kataloge des BSI (siehe [BSI-GS]) einzuhalten._ 

**Bewertung** : 

**Begründung** : 

## 4.3.4 Spezifische Anforderung W4: Passwortentropie 

**Referenz** : 3.3.1.2 Wissen 

**Anforderung** : _Bei Verwendung eines Fehlbedienungszählers, der maximal drei Versuche, eine PIN zu raten zulässt, sollte eine PIN mindestens 4 (Vertrauensniveau normal), 5 (Vertrauensniveau substantiell) bzw. 6 (Vertrauensniveau hoch) dezimale Stellen haben (vgl. [AIS 20/31])._ 

**Bewertung** : 

**Begründung** : 

Bundesamt für Sicherheit in der Informationstechnik 

18 

Prüfobjektspezifische Module  4 

## 4.4 Anforderungskatalog zum Authentisierungsmittel Biometrie 

## 4.4.1 Spezifische Anforderung Bio1: Anforderungen an die Biometrie 

**Referenz** : 3.3.1 Authentisierungsmittel 

**Anforderung** : _Anforderungen aus Tabelle 3 in [TR-03107-1]: Eigenschaften von Authentisierungsfaktoren_ 

**Bewertung** : 

**Begründung** : 

## 4.4.2 Spezifische Anforderung Bio2: Sicherheit Biometrie 

**Referenz** : 3.3.1.3 Biometrie 

**Anforderung** : _Die Erfolgswahrscheinlichkeit für eine Überwindung der biometrischen Erkennung, ausgedrückt durch False Acceptance Rate, darf nicht wesentlich schlechter als die entsprechenden Vorgaben für den Sicherungsfaktor Wissen sein._ 

**Bewertung** : 

**Begründung** : 

## 4.5 Anforderungskatalog zu Multi-Faktor Authentisierung 

## 4.5.1 Spezifische Anforderung MF1: Verknüpfung Sicherungsfaktoren 

**Referenz** : 3.3.1.2 Wissen 

**Anforderung** : _Bei Nutzung von Wissen in Kombination mit Besitz müssen beide Sicherungsfaktoren miteinander verknüpft sein, zum Beispiel die Benutzung einer PIN zur Freischaltung einer Chipkarte._ 

**Bewertung** : 

**Begründung** : 

## 4.5.2 Spezifische Anforderung MF2: Fehlschlagen eines Faktors 

**Referenz** : 3.3.1.4 Zwei-Faktor-Authentisierung 

**Anforderung** : _[…] darf ein Angreifer das Fehlschlagen eines Authentisierungsversuchs nicht einem einzelnen Authentisierungsfaktor zuordnen können._ 

**Bewertung** : 

**Begründung** : 

## 4.5.3 Spezifische Anforderung MF3: Resistenz beider Faktoren 

**Referenz** : 3.3.1.4 Zwei-Faktor-Authentisierung 

**Anforderung** : _[…] dürfen nicht beide Faktoren gemeinsam durch einen einzelnen Angriff auf die Nutzerumgebung angreifbar sein._ 

**Bewertung** : 

## **Begründung** : 

Bundesamt für Sicherheit in der Informationstechnik 

19 

4 Prüfobjektspezifische Module 

## 4.5.4 Spezifische Anforderung MF4: Ausgabe über getrennte Übermittlungswege 

**Referenz** : 3.2.2 Ausgabe der Authentisierungsmittel 

**Anforderung** : _Die Ausgabe für die Vertrauensniveaus substantiell/hoch muss so erfolgen, dass die beiden Sicherungsfaktoren [...] auf verschiedenen Übermittlungswegen ausgegeben werden. Diese Anforderung kann auch dadurch erfüllt werden, in dem die beiden Faktoren zeitlich getrennt auf gleichem Wege übermittelt werden, sofern sichergestellt ist, dass der erste Faktor den Inhaber erreicht hat, bevor der zweite übermittelt wird._ 

**Bewertung** : 

**Begründung** : 

## 4.6 Anforderungskatalog zum Authentisierungsmittel eID 

## 4.6.1 Spezifische Anforderung eID1: eID-Funktion 

**Referenz** : 4.1 Elektronischer Identitätsnachweis 

**Anforderung** : _Der elektronische Identitätsnachweis [...] ist für die Authentisierung auf hohem Vertrauensniveau geeignet. Dies gilt auch bei Einsatz des Pseudonyms (dienste- und kartenspezifische Kennung)._ 

**Bewertung** : 

**Begründung** : 

## 4.7 Anforderungskatalog zum Authentisierungsmittel Softwaretoken 

## 4.7.1 Spezifische Anforderung SW1: Schlüsselspeicherung 

**Referenz** : 4.2 Kryptographische Token 

**Anforderung** : _Es gelten die Anforderungen aus Abschnitt 3.7 [„Kryptographie“]. Die privaten kryptographischen Schlüssel dürfen nicht außerhalb des Tokens vorliegen (kein Key-Backup oder Key-Escrow)._ 

**Bewertung** : 

**Begründung** : 

## 4.7.2 Spezifische Anforderung SW2: Erzeugung und Löschung der Schlüssel 

**Referenz** : 4.2 Kryptographische Token 

**Anforderung** : _Sofern Schlüssel außerhalb des Tokens erzeugt werden, so muss dies in einer sicheren Umgebung erfolgen und die außerhalb des Tokens vorliegenden privaten Schlüssel vor Auslieferung des Tokens gelöscht werden._ 

**Bewertung** : 

**Begründung** : 

## 4.8 Anforderungskatalog zum Authentisierungsmittel OTP 

## 4.8.1 Spezifische Anforderung OTP1: TANs 

**Referenz** : 4.3 One Time Passwords 

**Anforderung** : _Diverse Anforderungen aus Abschnitt 4.3 von [TR-03107-1]_ 

Bundesamt für Sicherheit in der Informationstechnik 

20 

Prüfobjektspezifische Module  4 

_Das Vertrauensniveau hoch kann grundsätzlich nur mit TAN-Verfahren erreicht werden, bei denen wesentliche Vorgangsdaten in die Erzeugung der TAN eingehen und dem Nutzer unabhängig von der primären Verbindung zwischen Bürger und vertrauenden Entität angezeigt werden._ 

**Bewertung** : 

**Begründung** : 

## 4.8.2 Spezifische Anforderung OTP2: TAN-Generatoren 

## **Referenz** : 4.3.4 TAN-Generatoren 

**Anforderung** : _Der TAN-Generator muss individuell sein, d. h. Generatoren unterschiedlicher Inhaber sind nicht gegeneinander austauschbar;_ 

_Der Generator (Faktor Besitz, z. B. eine Chipkarte) ist zur Erzeugung der TAN durch eine PIN oder Ähnliches (Faktor Wissen) geschützt._ 

**Bewertung** : 

**Begründung** : 

## 4.9 Anforderungskatalog zum Authentisierungsmittel smsTAN 

## 4.9.1 Spezifische Anforderung sms1: Registrierung der SIM 

## **Referenz** : 4.3.2 smsTAN 

**Anforderung** : _Die Registrierung der SIM-Karte (bzw. genauer der Telefonnummer) auf das Konto des Bürgers bei der Behörde erfolgt in Verbindung mit einer Identifizierung des Bürgers mindestens auf Vertrauensniveau substantiell [...]._ 

**Bewertung** : 

**Begründung** : 

## 4.9.2 Spezifische Anforderung sms2: Displaysperre 

## **Referenz** : 4.3.2 smsTAN 

**Anforderung** : _Das smsTAN-Verfahren bildet eine Zwei-Faktor-Authentisierung über die Telefonnummer (Faktor Besitz) und den Zugangscode (PIN, Geste – Faktor Wissen) des Mobiltelefons. Daher darf das Verfahren nur mit Mobiltelefonen benutzt werden, die einen eingeschalteten und wirksamen Mechanismus zur Zugangssperre haben. Alternativ kann die smsTAN in Verbindung mit einem anderen wissensbasierten Faktor eingesetzt werden, wobei Abschnitt 3.3.1.4 zu beachten ist._ 

**Bewertung** : 

**Begründung** : 

## 4.9.3 Spezifische Anforderung sms3: Getrennter Kanal 

## **Referenz** : 4.3.2 smsTAN 

**Anforderung** : _Die primäre Verbindung zwischen Bürger und Behörde (d.h. die eigentliche Transaktion) erfolgt nicht über das Mobiltelefon, sondern über ein separates Endgerät und ein anderes Netzwerk._ 

## **Bewertung** : 

## **Begründung** : 

Bundesamt für Sicherheit in der Informationstechnik 

21 

4 Prüfobjektspezifische Module 

## 4.10 Anforderungskatalog zur Reaktivierung 

## 4.10.1 Spezifische Anforderung R1: Identifizierung 

**Referenz** : 3.4.2 Reaktivierung 

**Anforderung** : _Für eine Rücknahme einer Sperrung – sofern vom System unterstützt – muss eine Identifizierung des Inhabers eines Authentisierungsmittels mindestens auf dem Vertrauensniveau des Authentisierungssystems erfolgen._ 

**Bewertung** : 

**Begründung** : 

## 4.10.2 Spezifische Anforderung R2: Kompromittierung 

**Referenz** : 3.4.2 Reaktivierung 

**Anforderung** : _Es muss sichergestellt sein, dass die Sicherheit der Authentisierungsmittel nicht kompromittiert wurde._ 

**Bewertung** : 

**Begründung** : 

Bundesamt für Sicherheit in der Informationstechnik 

22 

Ergebnis der Prüfung 5 

## 5 Ergebnis der Prüfung 

Dieses Kapitel beinhaltet das Ergebnis der Prüfung sowie etwaige Anmerkungen und Auflagen, welche bei der Bewertung zu beachten sind. Die Bewertung ist anhand einer Zusammenfassung aller Teilbewertungen vorzunehmen. 

## 5.1 Vertrauensniveau des Prüfobjekts 

Das Prüfobjekt hat folgendes Vertrauensniveau erreicht: _____________________ 

## 5.2 Begründung 

Das Vertrauensniveau wird wie folgt begründet: _____________________________________________________ 

Bundesamt für Sicherheit in der Informationstechnik 

23 

6 Informationen zu den Prüfern 

## 6 Informationen zu den Prüfern 

Die Prüfung wurde durch die im Folgenden benannten Prüfer durchgeführt. Diese bestätigen durch ihre Unterschrift die Richtigkeit der im Dokument festgehaltenen Angaben. 

## **1. Prüfer** 

_Name_ : 

_Vorname_ : _Anschrift_ : 

_Unterschrift_ : ____________________________ 

## **2. Prüfer** 

_Name_ : 

_Vorname_ : _Anschrift_ : 

_Unterschrift_ : ____________________________ 

Bundesamt für Sicherheit in der Informationstechnik 

24 

Anhang 7 

## 7 Anhang 

## 7.1 Fragebogen zur allgemeinen Beschreibung des Authentisierungsverfahrens 

Dieser Prüfbericht bezieht sich auf eine konkrete Ausprägung des analysierten Authentisierungsverfahrens (nachfolgend Prüfobjekt). Dies bedeutet, dass das Ergebnis einen eindeutigen Bezug zu einem bestimmten Authentisierungsverfahren in einer bestimmten Konfiguration mitsamt dem zugehörigen E-GovernmentOnlinedienst hat. Insbesondere sind die Ergebnisse nicht notwendigerweise auf anderen Ausprägungen des Verfahrens, z. B. andere Versionsnummern oder Konfigurationen, übertragbar. 

In diesem Fragebogen soll Ihr Authentisierungsverfahren eindeutig identifiziert werden. Die korrekte und ausführliche Beantwortung der Fragen ist essentiell, um weitere Nachfragen zu vermeiden. Um die Prüfung schnellstmöglich durchführen zu können, sollten Sie einen konkreten Ansprechpartner benennen, der für eine korrekte und zeitnahe Beantwortung der Fragen während der Prüfung zur Verfügung steht. 

## 7.1.1 Allgemeine Angaben 

Zur Prüfung wird folgendes Authentisierungsverfahren angemeldet: 

- Angaben zum Verfahrensbetreiber 

__________________________________________________________________________________________________________ 

- Kontaktdaten des technischen Ansprechpartners 

__________________________________________________________________________________________________________ 

- Name und Versionsnummer des Prüfobjekts (falls zutreffend) 

__________________________________________________________________________________________________________ 

- Falls das Prüfobjekt aus mehreren Komponenten besteht, listen Sie bitte alle verwendeten Module hier auf 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

## 7.1.2 Zertifizierungen 

Falls das Prüfobjekt oder von diesem verwendete Bestandteile bereits zertifiziert wurden (Pentests, ISO, etc.), tragen Sie diese bitte im Folgendem ein. Fügen Sie Ihrer Antwort bitte die entsprechenden Nachweise bei. 

- Das Produkt besitzt folgende Zertifizierungen 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

Bundesamt für Sicherheit in der Informationstechnik 

25 

7 Anhang 

## 7.1.3 URLs bzw. Online-Verfügbarkeit 

Die Prüfung bezieht sich auf ein Prüfobjekt, welches den Nutzern Zugriff auf Dienste im E-Government-Bereich anbietet und besitzt dementsprechend Onlineschnittstellen, die bei der Prüfung zu berücksichtigen sind. Bitte geben Sie sämtliche verwendeten URLs hier an. Falls es bei der Authentisierung zur Kommunikation mit externen Serverbetreibern kommt, geben sie bitte jeweils auch den jeweiligen Kommunikationspartner an. Beispiel: _https://egov.meindienst.de (Adresse für Nutzer), https://oauth.dienstleister.de (Adresse des Authentisierungsfaktors x)_ 

- Das Produkt steht unter folgenden URLs zur Verfügung 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

## 7.1.4 Allgemeine Beschreibung des Prüfobjekts 

Bitte liefern Sie eine Übersicht über das Prüfobjekt und seine Komponenten. Hierbei ist, neben einer textuellen Beschreibung, auch ein Ablaufdiagramm der drei Funktionen Enrolment, Authentisierung und Revozierung wichtig. Welche Mechanismen gemäß [TR-03107-1] werden dabei genutzt? Welche Authentisierungsfaktoren kommen in Ihrem Authentisierungsverfahren zum Einsatz? 

## 7.1.5 Angestrebtes Vertrauensniveau 

Bitte legen Sie fest, für welches Vertrauensniveau Sie eine Prüfung Ihres Verfahrens anvisieren. Ohne Angaben kann das höchstmögliche Vertrauensniveau in der Prüfung ermittelt werden. Dies kann allerdings erheblichen zeitlichen und organisatorischen Zusatzaufwand verursachen. 

_normal_ [  ] 

## _substantiell_ [  ] 

_hoch_ [  ] 

## 7.1.6 Auflistung der eingesetzten Protokolle 

Bei einem Authentisierungsverfahren kommen meistens mehrere Protokolle zum Einsatz (z. B. TLS, SAML, Kerberos etc.). Um einen Überblick über die relevanten Protokolle zu geben, listen Sie bitte diese auf. Bitte ergänzen Sie nach Möglichkeit entsprechende Zusatzinformationen (z. B. SAML mit WebSSO-Profil). 

- Das Produkt verwendet folgende Protokolle 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

__________________________________________________________________________________________________________ 

Bundesamt für Sicherheit in der Informationstechnik 

26 

Anhang 7 

## 7.1.7 Festlegung des Authentisierungsmittels 

Falls Ihr Authentisierungsverfahren mehrere Authentisierungsmittel unterstützt (z. B. Benutzername/Passwort, Softwaretoken und Hardwaretoken), muss hier eine Festlegung getroffen werden, welches Mittel als Grundlage für die Bewertung gelten soll. Eine Feststellung des Sicherheitsniveaus bezieht sich dann genau auf dieses bestimmte Authentisierungsmittel. Sollten mehrere Authentisierungsmittel bewertet werden, so müssen separate Vertrauensniveaubewertungen durchgeführt werden. 

- Die Vertrauensniveaubewertung bezieht sich auf folgendes Authentisierungsmittel 

__________________________________________________________________________________________________________ 

## 7.1.8 Nutzung von externen Stellen 

Die [TR-03107-1] berücksichtigt neben dem Inhaber des Authentisierungsmittels und der vertrauenden Entität auch weitere externe Stellen, die z. B. für Enrolment, Identitätsprüfung, Ausgabe der Authentisierungsmittel, Sicherung von Kommunikationsbeziehungen oder Speicherung von Daten zuständig sein können. Diese Stellen müssen vom Hersteller identifiziert und benannt werden. Im weiteren Verlauf der Vertrauensniveaufeststellung werden hierzu gesonderte Fragen gestellt. 

Bitte benennen Sie daher hier alle Stellen, die im Sinne der [TR-03107-1] relevant sind. 

## 7.1.9 Reaktivierung 

Die [TR-03107-1] stellt besondere Anforderungen an die Rücknahme einer Sperrung. Sollte eine Rücknahme möglich sein, werden auch entsprechende Fragen für die Bewertung gestellt. Geben Sie bitte an, ob eine Reaktivierung in Ihrem Produkt vorgesehen ist. 

Reaktivierung ist vorgesehen [  ] 

Reaktivierung ist nicht vorgesehen [  ] 

## 7.2 Prüfobjektbezogener Fragenkatalog 

Die Bewertung wird anhand der folgenden Fragen vorgenommen. 

## 7.2.1 Generische Fragen 

|7.2.1|Generische Fragen|
|---|---|
|**ID**|**Frage**|
|G1<br>3.1|Liegt für die Identitätsprüfung eine Bewertung gemäß [TR-03147] vor? Wie lautet ggf. das Ender-<br>gebnis dieser Bewertung?|
|||
|G2<br>3.2|Mit welchen Verfahren wird sichergestellt, dass verwendete Authentisierungsmittel nur an die da-<br>für berechtigten Nutzer ausgegeben werden?<br>Falls keine Ausgabe des Authentisierungsmittels seitens des Prüfings erfolgt, sondern stattdessen<br>ein beim Benutzer bereits vorhandenes Authentisierungsmittel verwendet wird, wie erfolgt die Bin-<br>dung des Authentisierungsmittels an den Nutzer?|
|||
|G3<br>3.3|_Nur relevant, falls das Vertrauensniveau hoch angestrebt wird_<br>Ist eine explizite Aktivierung eines oder mehrerer der Authentisierungsmittel erforderlich? Falls ja,<br>wie ist diese Aktivierung jeweils ausgestaltet?|



Bundesamt für Sicherheit in der Informationstechnik 

27 

7 Anhang 

|||
|---|---|
|G4<br>3.4|Wie werden dem Authentisierungsmittelinhaber Geschäftsbedingungen sowie notwendige Verhal-<br>tensregeln zum Umgang mit den Authentisierungsmitteln übermittelt?|
|||
|G5<br>3.5|Wie werden alle betroffenen Stellen und Authentisierungsmittelinhaber über Änderungen im Um-<br>gang mit den Authentisierungsmitteln oder notwendigen Verhaltensregeln informiert? Bitte be-<br>nennen Sie dabei insbesondere, ob die Benachrichtigung aktiv erfolgt, oder die Stellen sich selbst<br>regelmäßig informieren müssen.|
|||
|G6<br>3.6|Gegen welches Angriffspotential (_enhanced-basic_,_moderate_oder_high_gemäß [CC] / [CEM]) ist das<br>eingesetzte Authentisierungsprotokoll geschützt? Wurden für kryptographische Verfahren entspre-<br>chende Sicherheitsbeweise durchgeführt?|
|||
||Wenn keine Nachweise zum Schutzniveau vorliegen, muss eine Beschreibung des Authentisie-<br>rungsprotokolls zur Verfügung gestellt werden. Diese soll ausreichend detailliert sein, damit der<br>Prüfer eine Einschätzung selbstständig vornehmen kann. Z. B. können hierfür weitere Dokumente<br>angegeben werden, die das Authentisierungsprotokoll technisch beschreiben. Sollten zudem noch<br>Sicherheitsbeweise existieren, so sollen diese ebenfalls angegeben werden.|
|||
|G7<br>3.7|Welche der eingesetzten Mechanismen / Protokolle verwenden Forward Secrecy? Legen Sie ggf. dar,<br>ob Forward Secrecy garantiert oder nur optional ist.|
|||
|G8<br>3.8|_Nur relevant, falls Vertrauensniveau substantiell oder hoch angestrebt wird_<br>Wie kann das von Ihnen eingesetzte Authentisierungsprotokoll nachweisen, dass sich die Authenti-<br>sierungsmittel im Augenblick der Authentisierung unter Kontrolle des Nutzers befnden? Wird die-<br>ser Nachweis für jede Authentisierung neu erzeugt?|
|||
|G9<br>3.9|Wie kann ein Nutzer sein Authentisierungsmittel bei Bedarf (z. B. im Falle der Kompromittierung<br>oder Verlust) sperren? Bitte machen Sie eine genaue Angabe zu allen vorgesehenen Sperrmöglich-<br>keiten. Ist für die Sperrung das Authentisierungsmittel erforderlich (z. B. für das Anmelden am Self-<br>Service)?|
|||
||Wie viel Zeit wird für eine effektive Sperrung eines Authentisierungsmittels nach der Sperrmel-<br>dung durch den Nutzer maximal benötigt? Nach [TR-03107-1], „_eine Sperrung ist effektiv zu dem_<br>_Zeitpunkt, an dem die Sperrinformation für vertrauende Entitäten zur Verfügung steht._“|
|||
||Bitte wählen Sie, zu welchen Zeiten die Sperrung durch den Nutzer möglich ist:<br>•<br>[  ] während der üblichen Geschäftszeiten (bitte Zeiten angeben)<br>•<br>[  ] jederzeit<br>•<br>[  ] jederzeit und allgemein bekannt (z. B. unmittelbar auf der Online-Präsenz des Dienstes er-<br>sichtlich)|
|||



Bundesamt für Sicherheit in der Informationstechnik 

28 

Anhang 7 

|G10<br>3.10|Wie werden die Möglichkeiten zur Übermittlung der Sperrmeldung den Nutzern von Authentisie-<br>rungsmitteln bekannt gemacht? Mit Hilfe von welchen öffentlichen Kommunikationswegen wer-<br>den die Sperrmöglichkeiten bekannt gemacht?|
|---|---|
|||
|G11<br>3.11|Wie erlangt der Vertrauensdienst Kenntnis davon, dass der Nutzer nicht mehr zum Besitz des Au-<br>thentisierungsmittels berechtigt ist oder sich seine relevanten / authentisierten Identitätsattribute<br>ändern?|
|||
||Welche Identitätsattribute werden zu einer Identität erfasst? Bitte geben Sie eine Liste mit allen<br>durch den Dienst erfassten Identitätsattributen und markieren Sie dabei, welche davon den mini-<br>malen konstanten Datensatz für eine Identität darstellen.|
|||
||Was passiert, wenn sich mindestens eines der Identitätsattribute ändert, das zum minimalen kon-<br>stanten Datensatz gehört?|
|||
|G12<br>3.12|Wie ist die Kommunikation zwischen den beteiligten Stellen gesichert? Bitte die Protokolle benen-<br>nen, z. B. TLS mit oder ohne Client-Authentisierung|
|||
|G13<br>3.13|Erläutern Sie die kryptographischen Mechanismen, Algorithmen, Schlüssellängen, Cipher Suites<br>etc., die Sie einsetzen. Listen Sie diese nach Schnittstellen (URL angeben) bzw. Kommunikationsbe-<br>ziehungen und auf allen Ebenen (Transport/Inhalt) eingesetzten kryptografschen Mechanismen<br>gegliedert auf. Sofern die Verfahren gemäß Technischen Richtlinien des BSI formuliert sind, geben<br>Sie diese zusätzlich an und schlüsseln Sie die Algorithmen in vergleichbarer Weise auf.|
|||
|G14<br>3.14|Wie werden die privaten kryptographischen Schlüssel aller Entitäten gespeichert? Benennen Sie<br>hierbei insbesondere auch die relevanten Zertifzierungen der verwendeten Komponenten.|
|||
||Wie wird sichergestellt, dass Auslesen, Kopieren oder unberechtigtes Nutzen von privaten Schlüs-<br>seln nicht möglich ist?|
|||
||Werden einzelne, zur Aufewahrung privater Schlüssel genutzte Komponenten in geschützten Um-<br>gebungen (entsprechend [ISO27001]) betrieben? Falls ja, geben Sie bitte an, welche Komponenten<br>dies sind und in welcher Umgebung sich diese jeweils befnden.|
|||
|G15<br>3.15|Wie werden die öffentlichen Schlüssel, die für die Authentifzierung genutzt werden, gegen Mani-<br>pulation geschützt? Benennen Sie hierbei insbesondere auch die relevanten Zertifzierungen der<br>zur Aufewahrung genutzten Komponenten.|
|||



Bundesamt für Sicherheit in der Informationstechnik 

29 

7 Anhang 

||Werden einzelne, zur Aufewahrung öffentlicher Schlüssel genutzte Komponenten in geschützten<br>Umgebungen (entsprechend [ISO27001]) betrieben? Falls ja, geben Sie bitte an welche Komponen-<br>ten dies sind und in welcher Umgebung sich diese jeweils befnden.|
|---|---|
|||
|G16<br>3.16|Bitte beschreiben Sie in wie fern Ihr Authentisierungsverfahren modularisiert und konfgurierbar<br>ist, sodass die kryptographischen Verfahren neuen kryptographischen Erkenntnissen angepasst<br>werden können (z. B. Austausch von Schlüsseln, Austausch kryptographischer Primitiven und die<br>Erhöhung von Schlüssellängen)? Bitte listen Sie auf, welche Parameter genau angepasst werden<br>können (TLS Version, Cipher Suites, Elliptische Kurven, Hashalgorithmen, Schlüssellängen, xmlenc,<br>xmldsig etc.). Sollten Sie externe Kryptografebibliotheken einsetzen, listen Sie diese hier bitte auf.|
|||
|G17<br>3.17|Gibt es spezielle Anforderungen an die Client-Systeme der Nutzer, welche Technischen Richtlinien<br>oder Empfehlungen des BSI widersprechen (insbesondere den unterhttps://www.bsi-fuer-<br>buerger.de/BSIFB/DE/Empfehlungen/empfehlungen_node.htmlbereitgestellten Empfehlungen)?<br>Bitte benennen Sie sämtliche notwendige Abweichungen. Benennen Sie bitte weiterhin, welche<br>Empfehlungen des BSI dabei berücksichtigt wurden (z. B. aktive Firewall, aktueller Virusscanner,<br>letzte Sicherheitsupdates etc.)|
|||
|G18<br>3.18|Wird der Inhaber des Authentisierungsmittels gegenüber dem Diensteanbieter eindeutig identif-<br>ziert? Falls ja, wie ist die Eindeutigkeit sichergestellt?|
|||
|G19<br>3.19|Falls bei Ihrem Verfahren eine eindeutige Kennung verwendet wird, wie wird diese geschützt, so-<br>dass diese gegenüber Dritten nicht zugänglich ist?|
|||
|G20<br>3.20|Wie wird sichergestellt, dass die Identifzierungen des Dienstes eindeutig einer bestimmten Session<br>zugeordnet werden und auch nur dort gültig sind? Über welche organisatorische/technische/kryp-<br>tographische Mechanismen fndet die Bindung statt? Beschreiben Sie diese (inklusive Algorithmen,<br>Schlüssellängen etc.).|
|||
|G21<br>3.21|Wie fndet die Bindung der übertragenen Identität bzw. eines vorangegangenen Identifzierungs-<br>prozesses an den Sitzungskontext statt? Wird die Identität einer Person eindeutig einer bestimmten<br>Session zugeordnet? Wie wird sichergestellt, dass sie auch nur dort gültig ist? Über welche techni-<br>sche/kryptographische Mechanismen fndet die Bindung statt? Beschreiben Sie diese (inklusive Al-<br>gorithmen, Schlüssellängen etc.).|
|||
|G22<br>3.22|_Nur relevant, falls datenschutzrechtlich relevante ID-Attribute übertragen werden._<br>Wie wird sichergestellt, dass Identitätsattribute erst nach erfolgter Freigabe durch den Nutzer über-<br>mittelt werden?|



Bundesamt für Sicherheit in der Informationstechnik 

30 

Anhang 7 

|||
|---|---|
|||
|||
|G23<br>3.23|Wie erfolgt eine Identifzierung des Dienstes gegenüber dem Nutzer bevor sich dieser authentisiert?|
|||
|G25<br>3.25|Gegen welches Angriffspotential (_enhanced-basic_,_moderate_oder_high_gemäß [CC] / [CEM]) sind die<br>eingesetzten Authentisierungsmittel geschützt? Bitte für jedes zum Einsatz kommende Authenti-<br>sierungsmittel benennen und begründen.|
|||



## Tabelle 2: Generische Fragen 

Bundesamt für Sicherheit in der Informationstechnik 

31 

7 Anhang 

## 7.2.2 Fragen zu Stellen 

|7.2.2|Fragen zu Stellen|Fragen zu Stellen|
|---|---|---|
|**ID**|**Frage**||
|S1<br>4.1.1|Bitte benennen Sie alle weiteren Stellen, die mit folgenden Aufgaben in Ihrem Authentisierungs-<br>verfahren betraut sind:<br>•<br>Enrolment<br>•<br>Identitätsprüfung<br>•<br>Ausgabe der Authentisierungsmittel<br>•<br>Sicherung von Kommunikationsbeziehungen<br>•<br>Speicherung von Daten<br>•<br>Andere relevanten Stellen<br>Bitte beachten Sie, dass für die Beantwortung dieser Frage nur externe Stellen relevant sind, also<br>solche, die nicht dem Vertrauensdienstanbieter selbst angehören.||
||**ID**|**Stelle**|
||1||



Bundesamt für Sicherheit in der Informationstechnik 

32 

Anhang 7 

Bitte für jede der genannten Stellen, für welche die jeweilige Aussage zutrifft, die ihr zugeordnete ID eintragen: 

- Die Stelle ist eine Behörde oder juristische Person 

______________________________________________________________________________________________ 

- Die Stelle ist rechtlich befugt, ihre Aufgabe wahrzunehmen 

______________________________________________________________________________________________ 

- Die Stelle stellt für ihre Aufgabe ein Regelwerk auf und hält dieses ein. Bitte benennen Sie das Dokument und die aktuell gültige Versionsnummer. Besteht seitens der Stelle die Möglichkeit, dem Prüfer Einsicht in das Dokument zu gewähren (ggf. in gekürzter Form)? 

______________________________________________________________________________________________ 

- Die Stelle ist organisatorisch und technisch in der Lage, ihre Aufgaben auf Basis des Regelwerks wahrzunehmen 

______________________________________________________________________________________________ 

- Sämtliche anwendbare Technischen Richtlinien des BSI und relevante Standards werden durch die Stelle eingehalten. Dies betrifft insbesondere die Einhaltung der Vorgaben von [TR-02102] / [TR-03116] sowie die anwendbaren Module des IT-Grundschutzes 

______________________________________________________________________________________________ 

- Die Stelle hat genügend Ressourcen für die Erfüllung ihrer Aufgaben und ggf. für die Übernahme der sich aus den Aufgaben ergebender Haftung 

______________________________________________________________________________________________ 

- Die Stelle greift zur Erfüllung Ihrer Aufgaben auf externe Dritte zurück. Sind diese Dritten dem eigentlichen Dienst bekannt und erreichen sie mindestens das gleiche Vertrauensniveau? 

______________________________________________________________________________________________ 

- Die Stelle ist gemäß IT-Grundschutz [BSI100-2] oder [ISO27001] zertifiziert. Die Zertifizierung erstreckt sich über sämtliche für die Tätigkeit in Ihrem Authentisierungsverfahren relevanten Systeme und Komponenten 

______________________________________________________________________________________________ 

- Falls die Stelle nicht selbst eine Behörde ist: ist sie behördlich für die wahrgenommene Aufgabe nach geltenden Gesetzen / Prozessen anerkannt? Durch welche Behörde? 

______________________________________________________________________________________________ 

Tabelle 3: Fragen zu Stellen 

Bundesamt für Sicherheit in der Informationstechnik 

33 

7 Anhang 

## 7.2.3 Fragen zum Authentisierungsmittel Besitz 

|7.2.3|Fragen zum Authentisierungsmittel Besitz|
|---|---|
|**ID**|**Frage**|
|B1<br>4.2.1|Wie kann der berechtigte Inhaber nach Erhalt erkennen, ob das Sicherungsmittel unberechtigt be-<br>nutzt wurde?|
|||
|B2<br>4.2.2|_Nicht relevant für Softwaretoken_<br>Wie wird die Einmaligkeit und Nicht-Kopierbarkeit des Besitzes sichergestellt?|
|||
||Wie wird der Inhaber darauf hingewiesen, dass er den Besitz nicht weitergeben darf?|
|||
||_Nicht relevant für Softwaretoken_<br>Wie wird verifziert, ob der Besitz unter physischer Kontrolle des Inhabers ist?|
|||
||Wie wird der Inhaber darauf hingewiesen, dass der Besitz nur zur Authentisierung genutzt werden<br>darf?|
|||
||Wie wird ein Verlust des Besitzes erkannt?|
|||
||Ist eine Missbrauchserkennung realisiert? Falls ja: wie?|
|||
||Ist eine Sperrung über ein eindeutiges Merkmal des Besitzes möglich? Falls ja: wie?|
|||
||Ist die Ausstellung eines neuen Besitztokens als Ersatz für ein gesperrtes Authentisierungsmittel<br>möglich?|
|||
|B3<br>4.2.3|_Nur relevant, falls das Vertrauensniveau hoch angestrebt wird_<br>Wie kann der Inhaber des Authentisierungsmittels sicherstellen, dass der Besitztoken nur für eine<br>intendierte Authentisierung aktiviert wird?|
|||



Tabelle 4: Fragen zum Authentisierungsmittel Besitz 

## 7.2.4 Fragen zum Authentisierungsmittel Wissen 

|7.2.4|Fragen zum Authentisierungsmittel Wissen|
|---|---|
|**ID**|**Frage**|
|W1<br>4.3.1|Wie kann der berechtigte Inhaber nach Erhalt erkennen, ob das Sicherungsmittel unberechtigt von<br>einem Dritten eingesehen wurde?|
|||



Bundesamt für Sicherheit in der Informationstechnik 

34 

Anhang 7 

||Wie werden diese Erkennungsmerkmale für eine unberechtigte Kenntnisnahme an den Inhaber<br>kommuniziert?|
|---|---|
|||
||Wie wird der Inhaber über die auf seiner Seite notwendigen Schritte hingewiesen, falls eine unbe-<br>rechtigte Kenntnisnahme des Wissens festgestellt wird?|
|||
|W2<br>4.3.2|Wie wird sichergestellt, dass das Wissen nur dem Inhaber und ggf. der verifzierenden Entität be-<br>kannt ist?|
|||
||Wird das Wissen zu irgendeinem Zeitpunkt ungesichert übertragen oder gespeichert?|
|||
||Können die Mitarbeiter oder Dienstleister des Verfahrensbetreibers einen Zugriff auf ungesichertes<br>Wissen erhalten?|
|||
||Wie wird der Inhaber darauf hingewiesen, dass das Wissen nicht weitergegeben werden darf?|
|||
||Wie wird der Inhaber darauf hingewiesen, dass das Wissen nur zur Authentisierung genutzt werden<br>darf?|
|||
||Wie wird der Inhaber darauf hingewiesen, dass der gleiche Wissens-Token nicht noch für andere<br>Dienste verwendet werden darf?|
|||
||Wird der Inhaber darauf hingewiesen, dass er den Wissens-Token nicht aufschreiben oder in der<br>Cloud speichern soll? Gibt es besondere Ausnahmen, die erlauben, das Wissen aufzuschreiben?|
|||
||Ist eine Missbrauchserkennung realisiert? Falls ja, wie?|
|||
||Ist Sperren des zugehörigen Accounts (bei entfernter Verifkation durch Server) bzw. Besitzes (bei<br>lokaler Verifkation durch Besitztoken) bei Missbrauchsverdacht möglich?|
|||
||Ist Setzen eines neuen Passworts / einer neuen PIN als Ersatz für gesperrtes Passwort / PIN mög-<br>lich?|
|||
|W3<br>4.3.3|_Diese Anforderung gilt nur für Passwort-basierte Sicherungsfaktoren._<br>Nur bei Nutzung von Wissen als alleinigem Sicherungsfaktor: Wie sind die Anforderungen aus<br>Maßnahme M 2.11 „Regelung des Passwortgebrauchs“ der IT-Grundschutz-Kataloge des BSI (siehe<br>[BSI-GS]) auf Diensteseite umgesetzt? Wie werden die durch den Nutzer beeinfussbaren Regelun-<br>gen forciert?|
|||



Bundesamt für Sicherheit in der Informationstechnik 

35 

7 Anhang 

|W4<br>4.3.4|Ist ein Fehlbedienungszähler implementiert? Wie viele Versuche lässt er zu? Wie viele Stellen hat<br>das Passwort/die PIN mindestens? Welcher Zeichensatz ist erlaubt?|
|---|---|
|||
||Wenn kein Fehlbedienungszähler vorhanden ist, welcher andere wirksamer Schutz ist gegen Brute-<br>Force Angriffe implementiert?|
|||



Tabelle 5: Fragen zum Authentisierungsmittel Wissen 

## 7.2.5 Fragen zum Authentisierungsmittel Biometrie 

|**ID**|**Frage**|
|---|---|
|Bio1<br>4.4.1|Wird Lebenderkennung bei Authentisierung durchgeführt? Falls ja, wie?|
|||
||Wird das biometrische Merkmal ausschließlich für die Authentisierung verwendet?|
|||
||Ist eine Missbrauchserkennung realisiert? Falls ja, wie?|
|||
||Ist Sperren des zugehörigen Accounts (bei entfernter Verifkation durch Server) bzw. Besitzes (bei<br>lokaler Verifkation durch Besitztoken) möglich?|
|||
||Wie ist eine Registrierung und Nutzung eines anderen biometrischen Merkmals als Ersatz für ein<br>gesperrtes Merkmal realisiert?|
|||
|Bio2<br>4.4.2|Bitte benennen Sie die ermittelte False Acceptance Rate. Wie wurden diese ermittelt?|
|||



Tabelle 6: Fragen zum Authentisierungsmittel Biometrie 

## 7.2.6 Fragen zur Multi-Faktor Authentisierung 

_Nur relevant, falls die Vertrauensniveaus substantiell oder hoch angestrebt werden._ 

|**ID**|**Frage**|
|---|---|
|MF1<br>4.5.1|_Nur relevant, falls Wissen in Kombination mit Besitz verwendet wird. Sonst ist die Frage nicht anwend-_<br>_bar._<br>Wie sind die Sicherungsfaktoren miteinander verknüpft?|
|||
|MF2<br>4.5.2|Wie wird sichergestellt, dass das Fehlschlagen eines Authentisierungsversuchs nicht einem einzel-<br>nen Authentisierungsfaktor zugeordnet werden kann?|
|||
|MF3|Wie wird verhindert, dass bei einem einzelnen Angriff auf die Nutzerumgebung das gesamte Ver-<br>fahren kompromittiert werden kann? Bitte berücksichtigen Sie bei Ihrer Antwort sowohl die Aufe-|



Bundesamt für Sicherheit in der Informationstechnik 

36 

Anhang 7 

|4.5.3|wahrung der Faktoren, als auch deren Einsatz während des Authentisierungsvorgangs.|
|---|---|
|||
|MF4<br>4.5.4|Auf welchen Übermittlungswegen werden dem Nutzer die Authentisierungsmittel bereitgestellt?<br>Bitte für jedes Authentisierungsmittel einzeln benennen.|
|||



Tabelle 7: Fragen zur Multi-Faktor Authentisierung 

## 7.2.7 Fragen zum Authentisierungsmittel eID 

|7.2.7|Fragen zum Authentisierungsmittel eID|
|---|---|
|**ID**|**Frage**|
|eID1<br>4.6.1|Auf welche Art und Weise wird die eID-Funktion in Ihrem Prüfobjekt genutzt? Ist die Verwendung<br>der eID-Funktion für jeden einzelnen Authentisierungsvorgang vorgesehen?|
|||



Tabelle 8: Fragen zum Authentisierungsmittel eID 

## 7.2.8 Fragen zum Authentisierungsmittel Softwaretoken 

|7.2.8|Fragen zum Authentisierungsmittel Softwaretoken|
|---|---|
|**ID**|**Frage**|
|SW1<br>4.7.1|Liegen die privaten kryptographischen Schlüssel auch außerhalb des Tokens vor (beispielsweise für<br>Key-Backup oder Key-Escrow)?|
|||
||Wird der Nutzer darauf hingewiesen, dass er diese auch bei gegebenen technischen Möglichkeiten<br>nicht extrahieren darf?|
|||
||Welche Schlüsselableitungsfunktion wurde implementiert, um Brute-Force Angriffe abzuwehren?<br>Welchen Rechenaufwand und Speicherplatz erfordert diese?|
|||
||Wie werden die Benutzer verpfichtet, keine leicht zu erratenden Passwörter („Trivialpasswörter“) zu<br>wählen? Bietet das System Hilfestellungen wie starke Passwörter gewählt werden können?|
|||
||Wenn der Token auf dem Computersystem gespeichert wird, wie ist er vor Kopieren oder Export ge-<br>schützt (z. B. Windows Zertifkatsspeicher, macOS Schlüsselbund)?|
|||
||Werden bestimmte Anforderungen an die Nutzergruppen gestellt, die den Zugriff auf das Compu-<br>tersystem regeln?|
|||



Bundesamt für Sicherheit in der Informationstechnik 

37 

7 Anhang 

|**ID**|**Frage**|
|---|---|
|SW2<br>4.7.2|In welcher Umgebung wird das Schlüsselmaterial erzeugt? Sollte die Erzeugung außerhalb des To-<br>kens erfolgen, wann werden die vorliegenden privaten Schlüssel gelöscht?|
|||



## Tabelle 9: Fragen zum Authentisierungsmittel Softwaretoken 

## 7.2.9 Fragen zum Authentisierungsmittel OTP 

|7.2.9|Fragen zum Authentisierungsmittel OTP|
|---|---|
|**ID**|**Frage**|
|OTP1<br>4.8.1|Wie werden die TANs generiert? Bitte beschreiben Sie insbesondere, wie und welche Vorgangsdaten<br>in die Erzeugung der TAN eingehen. Wie werden diese dem Inhaber angezeigt?|
|||
|OTP2<br>4.8.2|_Nur relevant, falls die Vertrauensniveaus substantiell oder hoch angestrebt werden_<br>_Nicht anwendbar, falls keine TAN-Generatoren zum Einsatz kommen._<br>Falls TAN-Generatoren eingesetzt werden (z. B. ChipTAN): Sind diese individuell? D.h. wie lässt sich<br>sicherstellen, dass die Generatoren unterschiedlicher Inhaber nicht gegeneinander austauschbar<br>sind? Wie ist die Erzeugung der TAN geschützt (bspw. durch eine PIN)?|
|||



## Tabelle 10: Fragen zum Authentisierungsmittel OTP 

## 7.2.10 Fragen zum Authentisierungsmittel smsTAN 

|**ID**|**Frage**|
|---|---|
|sms2<br>4.9.2|_Nur relevant, falls das Vertrauensniveau substantiell angestrebt wird_<br>Wie wird dem Benutzer mitgeteilt, dass das Prüfobjekt nur mit Mobiltelefonen benutzt werden darf,<br>die einen eingeschalteten und wirksamen Mechanismus zur Zugangssperre haben? Wird ein weite-<br>rer Faktor Wissen zusätzlich eingesetzt?|
|||
|sms3<br>4.9.3|_Nur relevant, falls das Vertrauensniveau substantiell angestrebt wird_<br>Wie wird sichergestellt, dass die primäre Verbindung zwischen Bürger und Behörde (d.h. die eigent-<br>liche Transaktion) nicht über das Mobiltelefon erfolgt, sondern über ein separates Endgerät und ein<br>anderes Netzwerk? Wie wird dem Nutzer diese Notwendigkeit signalisiert?|
|||



Tabelle 11: Fragen zum Authentisierungsmittel smsTAN 

Bundesamt für Sicherheit in der Informationstechnik 

38 

Anhang 7 

## 7.2.11 Fragen zur Reaktivierung 

|**ID**|**Frage**|
|---|---|
|R1<br>4.10.1|Wie fndet die Identifzierung des Inhabers eines Authentisierungsmittels für eine Rücknahme ei-<br>ner Sperrung statt?|
|||
|R2<br>4.10.2|Wie wird sichergestellt, dass die Sicherheit der Authentisierungsmittel vor oder während einer<br>Sperrung nicht kompromittiert wurde?|
|||



Tabelle 12: Fragen zur Reaktivierung 

Bundesamt für Sicherheit in der Informationstechnik 

39 

Literaturverzeichnis 

## Literaturverzeichnis 

- [AIS 20/31] BSI: AIS 20/31 -- A proposal for: Functionality classes for random number generators [Bew/TR-03107] BSI: Bewertung von Authentisierungslösungen gemäß TR-03107: Anwendungs- und Vorgehensbeschreibung Version 0.6 

- [BSI-GS] BSI: IT-Grundschutz-Kataloge, https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ ITGrundschutzKataloge/itgrundschutzkataloge_node.html 

- [BSI100-2] BSI: BSI-Standard 100-2: IT-Grundschutz-Vorgehensweise [CC] CCRA: Common Criteria for Information Technology Security Evaluation 3.1 [CEM] CCMB: Common Methodologyfor Information TechnologySecurity Evaluation [ISO27001] ISO/IEC: ISO/IEC 27001: Information technology -- Security techniques -- Information security management systems -- Requirements 

- [TR-02102] BSI: Technische Richtlinie TR-02102, Kryptographische Verfahren: Empfehlungen und Schlüssellängen 

- [TR-03107-1] BSI: Technische Richtlinie TR-03107, Elektronische Identitäten und Vertrauensdienste im E-Government 

- [TR-03107-1] BSI: Technische Richtlinie TR-03107-1, Elektronische Identitäten und Vertrauensdienste im E-Government 

- [TR-03116] BSI: Technische Richtlinie TR-03116, Kryptographische Vorgaben für Projekte der Bundesregierung 

- [TR-03147] BSI: Technische Richtlinie TR-03147, Vertrauensniveaubewertung von Verfahren zur Identitätsprüfung natürlicher Personen 

Bundesamt für Sicherheit in der Informationstechnik 

40 


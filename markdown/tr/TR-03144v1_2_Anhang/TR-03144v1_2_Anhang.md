
![](markdown/tr/TR-03144v1_2_Anhang/TR-03144v1_2_Anhang.pdf-0001-00.png)


## **Technische Richtlinie BSI TR-03144 Anhang** 

**eHealth –** 

**Sicherungsmechanismen im Umfeld der TR-Zertifizierung von G2-Karten-Produkten** 

**Version 1.2 – 27.07.2017** 

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn E-Mail: bsi@bsi.bund.de Internet: https://www.bsi.bund.de © Bundesamt für Sicherheit in der Informationstechnik 2017 

BSI TR-03144 Anhang 

## **Inhaltsverzeichnis** 

|1|Einleitung....................................................................................................................................4|
|---|---|
|1.1|Gegenstand, Zielsetzung und Übersicht des Dokuments...................................................................4|
|1.2|Einordnung des Dokuments...............................................................................................................4|
|1.3|Terminologie.....................................................................................................................................5|
|1.4|Abkürzungen.....................................................................................................................................5|
|1.5|Änderungshistorie.............................................................................................................................6|
|2|Rollenkonzept.............................................................................................................................8|
|3|Artefakte und ihre Sicherung....................................................................................................10|
|4|Übersicht über die Signaturschlüsselpaare...............................................................................22|
|5|Kryptographische Vorgaben......................................................................................................24|
|6|Schlüsselverwaltung..................................................................................................................25|
||Literaturverzeichnis..................................................................................................................27|



## **Tabellenverzeichnis** 

Tabelle 1: Änderungshistorie................................................................................................................7 Tabelle 2: Aufgaben und Aufgabenbeschreibung.................................................................................8 Tabelle 3: Zuordnung von Rollen und ihren Aufgaben........................................................................9 Tabelle 4: Artefakte und ihre Sicherheitsziele....................................................................................12 Tabelle 5: Artefakte und ihre Sicherungsmechanismen.....................................................................21 Tabelle 6: Übersicht der Signaturschlüsselpaare................................................................................23 

Bundesamt für Sicherheit in der Informationstechnik 

3 

BSI TR-03144 Anhang 

## **1 Einleitung** 

## **1.1 Gegenstand, Zielsetzung und Übersicht des Dokuments** 

Im Rahmen der TR-Konformitätsprüfung von eHealth Karten-Produkten der Kartengeneration G2 nach der Technischen Richtlinie BSI TR-03144 ([TR-03144]) unter Verwendung des KonsistenzPrüftools gemäß der Technischen Richtlinie BSI TR-03143 ([TR-03143]) werden aus Sicherheitsgründen heraus an verschiedenen Stellen Sicherungsmechanismen wie z.B. Signaturen verwendet. Das vorliegende Dokument betrachtet die hierzu erforderlichen Details, insbesondere hinsichtlich des Key Managements sowie hinsichtlich technischer und/oder organisatorischer Verfahren und Maßnahmen. 

Berücksichtigt werden in den nachfolgenden Ausführungen nur die für die TR-Konformitätsprüfung eines Karten-Produktes nach der Technischen Richtlinie BSI TR-03144 ([TR-03144]) auf Seiten des Herstellers des Karten-Produktes, der TR-Prüfstelle für das betreffende Karten-Produkt, der CCPrüfstelle für die dem Karten-Produkt unterliegende Karten-Plattform, der TR-Zertifizierungsstelle des BSI und der gematik für die Nutzung des Konsistenz-Prüftools der gematik _grundsätzlich_ benötigten Artefakte. Nicht betrachtet werden die vom Hersteller des Karten-Produktes und der dem Karten-Produkt unterliegenden Karten-Plattform für die TR-Konformitätsprüfung des betreffenden Karten-Produktes beizusteuernden _Hersteller-abhängigen_ Artefakte (wie z.B. das Karten-Produkt selbst, zugehörige Benutzerdokumentation zur Karten-Plattform und zum Karten-Produkt usw.) mit Ausnahme des Challenge/Fingerprint-Referenzwert-Paars der Karten-Plattform. Für diese Beistellungen des Herstellers des Karten-Produktes und der dem Karten-Produkt unterliegenden KartenPlattform kommen in der Regel Hersteller-spezifische Sicherungsmechanismen, insbesondere für den Auslieferungsweg zum tragen, die außerhalb des Scopes des vorliegenden Dokuments liegen. 

Der  vorliegende Anhang zur Technischen Richtlinie BSI TR-03144 ([TR-03144]) richtet sich an TR-Prüfstellen, die die TR-Konformitätsprüfung von Karten-Produkten der Kartengeneration G2 im Rahmen des G2-Zertifizierungskonzepts wie in der Technischen Richtlinie BSI TR-03106 ([TR03106]) dargestellt auf Basis der Technischen Richtlinie BSI TR-03144 ([TR-03144]) durchführen. Weiterhin richtet sich der vorliegende Anhang zur Technischen Richtlinie BSI TR-03144 ([TR03144]) an Hersteller von Karten-Produkten der Generation G2, die ihre Karten-Produkte einer TRZertifizierung nach der Technischen Richtlinie BSI TR-03144 ([TR-03144]) im Rahmen des G2Zertifizierungskonzepts mit dem Ziel einer Zulassung ihrer Karten-Produkte durch die gematik für einen Einsatz in der Telematikinfrastruktur im deutschen Gesundheitswesen unterziehen. 

Das vorliegende Dokument beschreibt in Kap. 2 das für die Ausgestaltung der oben genannten Sicherungsmechanismen vorgesehene Rollenkonzept. In Kap. 3 werden die Artefakte und ihre Sicherung genauer beleuchtet. Kap. 4 gibt eine Übersicht über die erforderlichen Signaturschlüsselpaare. In Kap. 5 werden kryptographische Vorgaben zusammengestellt und in Kap. 6 schließlich Informationen zur Schlüsselverwaltung bereitgestellt. 

## **1.2 Einordnung des Dokuments** 

Das vorliegende Dokument bildet einen Anhang zur Technischen Richtlinie BSI TR-03144 ([TR03144]), die die TR-Konformitätsprüfung und -Zertifizierung von eHealth Karten-Produkten der Kartengeneration G2 im Fokus hat. 

Die Technische Richtlinie BSI TR-03144 ([TR-03144]) gliedert sich in das Zertifizierungskonzept für die eHealth-Karten der Kartengeneration G2 ein und ist als nachgelagerte Dokumentation zur 

Bundesamt für Sicherheit in der Informationstechnik 

4 

BSI TR-03144 Anhang 

Technischen Richtlinie BSI TR-03106 „eHealth – Zertifizierungskonzept für Karten der Generation G2“ ([TR-03106]), die eine detaillierte Beschreibung dieses Zertifizierungskonzepts für die G2Karten beinhaltet, zu betrachten. 

Die Technische Richtlinie BSI TR-03144 ([TR-03144]) referenziert weiterhin auf die Technische Richtlinie BSI TR-03143 „eHealth – G2-COS Konsistenz-Prüftool“ ([TR-03143]), die das für das G2-Zertifizierungskonzept bzw. für die TR-Konformitätsprüfung von Karten-Produkten nach der Technischen Richtlinie BSI TR-03144 ([TR-03144]) erforderliche Konsistenz-Prüftool der gematik spezifiziert sowie die TR-Zertifizierung dieses Konsistenz-Prüftools selbst regelt. Die TR-Zertifizierung eines Karten-Produktes, die Gegenstand der Technischen Richtlinie BSI TR-03144 ([TR03144]) ist, macht von dem nach der Technischen Richtlinie BSI TR-03143 ([TR-03143]) implementierten und zertifizierten Konsistenz-Prüftool der gematik wesentlich Gebrauch. 

## **1.3 Terminologie** 

Dieser Anhang zur Technischen Richtlinie BSI TR-03144 ([TR-03144]) ist grundsätzlich als normativ anzusehen. Informative Teile werden explizit als solche gekennzeichnet (mit dem Vermerk „informativ“ oder „Hinweis“). 

Ferner orientiert sich dieser Anhang zur Technischen Richtlinie BSI TR-03144 ([TR-03144]) an den dort vereinbarten Begrifflichkeiten und deren Beschreibungen. 

## **1.4 Abkürzungen** 

In diesem Anhang zur Technischen Richtlinie BSI TR-03144 ([TR-03144]) sowie in den Dokumenten [TR-03106] und [TR-03143] werden folgende Abkürzungen verwendet: 

A Application ADF Application Dedicated File APDU Application Protocol Data Unit ATR Answer To Reset BMG Bundesministerium für Gesundheit BSI Bundesamt für Sicherheit in der Informationstechnik CC Common Criteria CMS Card Management System COS Card Operating System DF Dedicated File EF Elementary File eGK elektronische Gesundheitskarte eIDAS Verordnung (EU) Nr. 910/2014 über elektronische Identifizierung und Vertrauensdienste FW Firmware G1 eHealth Kartengeneration G1 G2 eHealth Kartengeneration G2 

Bundesamt für Sicherheit in der Informationstechnik 

5 

BSI TR-03144 Anhang 

|G2-COS|G2 Card Operating System|
|---|---|
|gSMC-K|gerätespezifische Security Module Card Typ K|
|gSMC-KT|gerätespezifische Security Module Card Typ KT|
|HBA|Heilberufsausweis|
|IC|Integrated Circuit|
|PDF|Portable Document Format|
|PGP|Pretty Good Privacy|
|PIN|Personal Identification Number|
|PKI|Public Key Infrastructure|
|PP|Protection Profile (Common Criteria)|
|PT|Prüftool|
|PTV|Produkttypversion|
|PUK|Personal Unblocking Key|
|QES|Qualified Electronic Signature|
|RSA|Rivest, Shamir, Adleman|
|SAK|Signaturanwendungskomponente|
|SFR|Security Functional Requirement (Common Criteria)|
|SGB|Sozialgesetzbuch|
|SHA|Secure Hash Algorithm|
|SMC-B|Security Module Card Typ B|
|SSCD|Secure Signature Creation Device|
|SSEE|Sichere Signaturerstellungseinheit|
|TI|Telematikinfrastruktur|
|TOE|Target Of Evaluation (Common Criteria)|
|TR|Technische Richtlinie|
|VSDD|Versichertenstammdatendienst|
|XML|Extensible Markup Language|
|ZDA|Zertifizierungsdiensteanbieter|



## **1.5 Änderungshistorie** 


![](markdown/tr/TR-03144v1_2_Anhang/TR-03144v1_2_Anhang.pdf-0006-03.png)


**----- Start of picture text -----**<br>
Version Datum Änderung<br>v0.1 05.06.2014 Erstausgabe<br>v1.0 29.07.2014 Veröffentlichung<br>v1.1 22.05.2015 Einzelne inhaltliche Ergänzungen und Klarstellungen in verschiedenen<br>Kapiteln<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

6 

BSI TR-03144 Anhang 


![](markdown/tr/TR-03144v1_2_Anhang/TR-03144v1_2_Anhang.pdf-0007-01.png)


**----- Start of picture text -----**<br>
Version Datum Änderung<br>v1.2 27.07.2017 Anpassung an das Update der BSI TR-03143 (Version 1.1, 2017),<br>Bugfixing, Einfügung von Klarstellungen, Aktualisierung von<br>Referenzen und bzgl. eIDAS<br>**----- End of picture text -----**<br>


Tabelle 1: Änderungshistorie 

Bundesamt für Sicherheit in der Informationstechnik 

7 

BSI TR-03144 Anhang 

## **2 Rollenkonzept** 

Im Rahmen der TR-Konformitätsprüfung eines Karten-Produktes nach der Technischen Richtlinie BSI TR-03144 ([TR-03144]) unter Nutzung des Konsistenz-Prüftools werden grundsätzlich einige Artefakte benötigt, die aus Sicherheitsgründen heraus abzusichern sind. Siehe hierzu die genaueren Ausführungen in Kap. 3. 

In der nachfolgenden Tabelle 2 werden die für diese Absicherung der Artefakte anfallenden Aufgaben zusammengestellt und genauer beschrieben. 

Notation: Der konkrete Inhalt der Beschreibung „Sicherung der ...“ in der nachstehenden Tabelle 2 wird in den folgenden Kapiteln genauer bestimmt und ausgeführt. 


![](markdown/tr/TR-03144v1_2_Anhang/TR-03144v1_2_Anhang.pdf-0008-05.png)


**----- Start of picture text -----**<br>
Aufgabe Aufgabenbeschreibung<br>R_Prüftool-Code Sicherung der Implementierung des Konsistenz-Prüftools.<br>R_Prüftool-Schemata Sicherung der zum Konsistenz-Prüftool zugehörigen XML-Schemata für<br>Objektsystem-Spezifikationen, Fingerprint-Sollwerte, Übersetzungstabel-<br>len und Testberichte.<br>R_Prüftool-Dokumentation Sicherung der zum Konsistenz-Prüftool zugehörigen Dokumentation (Be-<br>nutzerdokumentation usw.).<br>R_Prüftool-Konf-Dateien Sicherung der vom Konsistenz-Prüftool im Rahmen der Überprüfung ei-<br>nes Karten-Produktes benötigten Konfigurationsdateien.<br>Hinweis: Diese gemäß den Vorgaben der Benutzerdokumentation zum<br>Konsistenz-Prüftool codierten Konfigurationsdateien enthalten jeweils<br>eine Signatur bzw. einen Signaturprüfschlüssel (siehe untenstehende Aus-<br>führungen in Kap. 3).<br>R_Objektsys-Spezifikation Sicherung der XML-Datei der Objektsystem-Spezifikation (XML-<br>Master / XML-Derivat).<br>R_Plattform-Fingerprint Sicherung des Challenge/Fingerprint-Referenzwert-Paars einer Karten-<br>Plattform.<br>R_Übersetzungstabelle Sicherung der XML-Datei mit der Übersetzungstabelle zu einer Karten-<br>Plattform.<br>R_Testbericht Sicherung des vom Konsistenz-Prüftool für ein Karten-Produkt ausgege-<br>benen Testberichts.<br>R_Schlüsseltabelle Verwaltung und Sicherung der Schlüsseltabelle mit den Signaturprüf-<br>schlüsseln (siehe Kap. 6).<br>**----- End of picture text -----**<br>


Tabelle 2: Aufgaben und Aufgabenbeschreibung 

In der nachfolgenden Tabelle 3 erfolgt eine Zuordnung der in die TR-Konformitätsprüfung eines Karten-Produktes nach der Technischen Richtlinie BSI TR-03144 ([TR-03144]) involvierten Rollen und der in Tabelle 2 definierten Aufgaben. 

Bundesamt für Sicherheit in der Informationstechnik 

8 

BSI TR-03144 Anhang 


![](markdown/tr/TR-03144v1_2_Anhang/TR-03144v1_2_Anhang.pdf-0009-01.png)


**----- Start of picture text -----**<br>
Rolle Aufgaben<br>TR-Prüfstelle für Karten-Produkt R_Testbericht<br>falls eine Übersetzungstabelle von der TR-Prüfstelle generiert<br>und signiert wird:<br>R_Prüftool-Konf-Dateien<br>R_Übersetzungstabelle<br>CC-Prüfstelle für Karten-Plattform R_Plattform-Fingerprint<br>falls eine Übersetzungstabelle von der CC-Prüfstelle generiert<br>und signiert wird:<br>R_Prüftool-Konf-Dateien<br>R_Übersetzungstabelle<br>gematik R_Prüftool-Code<br>R_Prüftool-Schemata<br>R_Prüftool-Dokumentation<br>R_Prüftool-Konf-Dateien<br>R_Objektsys-Spezifikation<br>TR-Zertifizierungsstelle (BSI) R_Schlüsseltabelle<br>**----- End of picture text -----**<br>


Tabelle 3: Zuordnung von Rollen und ihren Aufgaben 

Bundesamt für Sicherheit in der Informationstechnik 

9 

BSI TR-03144 Anhang 

## **3 Artefakte und ihre Sicherung** 

In der nachfolgenden Tabelle 4 werden die für die TR-Konformitätsprüfung eines Karten-Produktes nach der Technischen Richtlinie BSI TR-03144 ([TR-03144]) für die Nutzung des Konsistenz-Prüftools grundsätzlich benötigten Artefakte zusammengestellt. Für jedes Artefakt werden seine Sicherheitsziele definiert und Informationen zu seiner kryptographischen Sicherung angegeben. 

In den nachfolgenden Ausführungen wird der Begriff „Konfigurationsdatei“ für Dateien verwendet, die zur Übergabe von Signaturen und Signaturprüfschlüsseln an das Konsistenz-Prüftool benutzt werden. Formatierungsvorgaben für solche Konfigurationsdateien sind Gegenstand der zum Konsistenz-Prüftool zugehörigen Benutzerdokumentation. 


![](markdown/tr/TR-03144v1_2_Anhang/TR-03144v1_2_Anhang.pdf-0010-04.png)


**----- Start of picture text -----**<br>
Artefakt Sicherheitsziel(e) Kryptographische  Art der Signatur<br>Sicherung<br>Konsistenz-Prüftool<br>Code / Dateien mit den Java-Bibliothe- Integrität, Signatur äußere technische<br>ken des Konsistenz-Prüftools (inklusive  Authentizität Signatur<br>Java-Laufzeitumgebung)<br>XML-Schema für Objektsystem-Spezi- Integrität, Signatur äußere technische<br>fikationen Authentizität Signatur<br>(zugehörig zum Konsistenz-Prüftool)<br>XML-Schema für Fingerprint-Sollwerte Integrität, Signatur äußere technische<br>(zugehörig zum Konsistenz-Prüftool) Authentizität Signatur<br>XML-Schema für Übersetzungstabellen Integrität, Signatur äußere technische<br>(zugehörig zum Konsistenz-Prüftool) Authentizität Signatur<br>XML-Schema für Testberichte Integrität, Signatur äußere technische<br>(zugehörig zum Konsistenz-Prüftool) Authentizität Signatur<br>Benutzerdokumentation zum Konsis- Integrität, Signatur (bei elek- äußere technische<br>tenz-Prüftool Authentizität tronischer Aus- Signatur<br>lieferung)<br>--- ---<br>TR-Zertifikat und -Konformitätsreport  Integrität,<br>zum Konsistenz-Prüftool Authentizität<br>Inputquellen für das Konsistenz-Prüftool<br>--- ---<br>Konfigurationsdatei mit der Signatur  Integrität,<br>über das Konsistenz-Prüftool (Code /  Authentizität<br>Dateien mit den Java-Bibliotheken in-<br>klusive Java-Laufzeitumgebung)<br>--- ---<br>Konfigurationsdatei mit der Signatur  Integrität,<br>über das XML-Schema für Objektsys- Authentizität<br>tem-Spezifikationen<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

10 

BSI TR-03144 Anhang 


![](markdown/tr/TR-03144v1_2_Anhang/TR-03144v1_2_Anhang.pdf-0011-01.png)


**----- Start of picture text -----**<br>
Artefakt Sicherheitsziel(e) Kryptographische  Art der Signatur<br>Sicherung<br>--- ---<br>Konfigurationsdatei mit der Signatur  Integrität,<br>über das XML-Schema für Fingerprint- Authentizität<br>Sollwerte<br>--- ---<br>Konfigurationsdatei mit der Signatur  Integrität,<br>über das XML-Schema für Überset- Authentizität<br>zungstabellen<br>--- ---<br>Konfigurationsdatei mit der Signatur  Integrität,<br>über das XML-Schema für Testberichte Authentizität<br>--- ---<br>Konfigurationsdatei mit der Signatur  Integrität,<br>über die XML-Datei der Objektsystem- Authentizität<br>Spezifikation xy (XML-Master / XML-<br>Derivat)<br>(xy = eGK/HBA/SMC-B/gSMC-K/<br>gSMC-KT/...)<br>--- ---<br>Konfigurationsdatei mit der Signatur  Integrität,<br>über das Challenge/Fingerprint-Refe- Authentizität<br>renzwert-Paar der Karten-Plattform<br>--- ---<br>Konfigurationsdatei mit der Signatur  Integrität,<br>über die Übersetzungstabelle (XML-Da- Authentizität<br>tei) zur Karten-Plattform<br>--- ---<br>Konfigurationsdatei mit dem Signatur- Integrität,<br>prüfschlüssel für die Prüfung der Signa- Authentizität<br>tur über die XML-Datei der Objektsys-<br>tem-Spezifikation xy (XML-Master /<br>XML-Derivat)<br>(xy = eGK/HBA/SMC-B/gSMC-K/<br>gSMC-KT/...)<br>--- ---<br>Konfigurationsdatei mit dem Signatur- Integrität,<br>prüfschlüssel für die Prüfung der Signa- Authentizität<br>tur über das Challenge/Fingerprint-Re-<br>ferenzwert-Paar der Karten-Plattform<br>--- ---<br>Konfigurationsdatei mit dem Signatur- Integrität,<br>prüfschlüssel für die Prüfung der Signa- Authentizität<br>tur über die Übersetzungstabelle (XML-<br>Datei) zur Karten-Plattform<br>XML-Datei der Objektsystem-Spezifi- Integrität, Signatur äußere technische<br>kation xy (XML-Master / XML-Deri- Authentizität Signatur<br>vat)<br>(xy = eGK/HBA/SMC-B/gSMC-K/<br>gSMC-KT/...)<br>Challenge/Fingerprint-Referenzwert- Integrität, Signatur, äußere technische<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

11 

BSI TR-03144 Anhang 


![](markdown/tr/TR-03144v1_2_Anhang/TR-03144v1_2_Anhang.pdf-0012-01.png)


**----- Start of picture text -----**<br>
Artefakt Sicherheitsziel(e) Kryptographische  Art der Signatur<br>Sicherung<br>Paar der Karten-Plattform Authentizität, Verschlüsselung Signatur<br>Vertraulichkeit<br>Übersetzungstabelle (XML-Datei) zur  Integrität, Signatur äußere technische<br>Karten-Plattform Authentizität Signatur<br>Output des Konsistenz-Prüftools<br>Testbericht Integrität, --- ---<br>Authentizität,<br>ggf. Vertraulichkeit<br>**----- End of picture text -----**<br>


Tabelle 4: Artefakte und ihre Sicherheitsziele 

In der nachfolgenden Tabelle 5 werden die für die TR-Konformitätsprüfung eines Karten-Produktes nach der Technischen Richtlinie BSI TR-03144 ([TR-03144]) für die Nutzung des Konsistenz-Prüftools grundsätzlich benötigten Artefakte aus Tabelle 4 genauer betrachtet und für jedes Artefakt geeignete Sicherungsmechanismen technischer und/oder organisatorischer Art angegeben. 

Notation: Für die Bezeichnung von Typen von Signaturschlüsseln und Signaturprüfschlüsseln siehe (Übersichts-) Tabelle 6 in Kap. 4. 


![](markdown/tr/TR-03144v1_2_Anhang/TR-03144v1_2_Anhang.pdf-0012-05.png)


**----- Start of picture text -----**<br>
Artefakt Technische / Organisatorische Lö- Typ des Signatur- Speicherort des Si-<br>sung schlüssels gnaturprüfschlüssels<br>(abgesehen von der Schlüs-<br>seltabelle der TR-Zertifi-<br>zierungsstelle des BSI, sie-<br>he Kap. 6)<br>Konsistenz-Prüftool<br>Code / Dateien mit den  Äußere technische Signatur über den  S_Prüftool-Code P_Prüftool-Code ist<br>Java-Bibliotheken des  Code des Konsistenz-Prüftools. im Konsistenz-Prüf-<br>Konsistenz-Prüftools  tool selbst hinterlegt<br>Automatische Signaturprüfung im<br>(inklusive Java-Lauf-<br>Konsistenz-Prüftool selbst im Rah-<br>zeitumgebung)<br>men seines Selbsttests.<br>Für die automatische Signaturprü-<br>fung ist ein vorhergehender Import<br>der zugehörigen Konfigurationsdatei<br>mit der zu prüfenden Signatur über<br>das Konsistenz-Prüftool in das Kon-<br>sistenz-Prüftool erforderlich.<br>Zusätzlich kann eine externe Signa-<br>turprüfung (ohne Nutzung des Kon-<br>sistenz-Prüftools) durchgeführt wer-<br>den.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

12 

BSI TR-03144 Anhang 


![](markdown/tr/TR-03144v1_2_Anhang/TR-03144v1_2_Anhang.pdf-0013-01.png)


**----- Start of picture text -----**<br>
Artefakt Technische / Organisatorische Lö- Typ des Signatur- Speicherort des Si-<br>sung schlüssels gnaturprüfschlüssels<br>(abgesehen von der Schlüs-<br>seltabelle der TR-Zertifi-<br>zierungsstelle des BSI, sie-<br>he Kap. 6)<br>XML-Schema für Ob- Äußere technische Signatur über das  S_Prüftool-Schema P_Prüftool-Schema ist<br>jektsystem-Spezifikatio- XML-Schema. im Konsistenz-Prüf-<br>nen tool selbst hinterlegt<br>Automatische Signaturprüfung im<br>(zugehörig zum Konsis- Konsistenz-Prüftool selbst.<br>tenz-Prüftool)<br>Für die automatische Signaturprü-<br>fung ist ein vorhergehender Import<br>des XML-Schemas und der zugehö-<br>rigen Konfigurationsdatei mit der zu<br>prüfenden Signatur über das XML-<br>Schema in das Konsistenz-Prüftool<br>erforderlich.<br>Zusätzlich kann eine externe Signa-<br>turprüfung (ohne Nutzung des Kon-<br>sistenz-Prüftools) durchgeführt wer-<br>den.<br>XML-Schema für Fin- Äußere technische Signatur über das  S_Prüftool-Schema P_Prüftool-Schema ist<br>gerprint-Sollwerte XML-Schema. im Konsistenz-Prüf-<br>(zugehörig zum Konsis- Automatische Signaturprüfung im  tool selbst hinterlegt<br>tenz-Prüftool) Konsistenz-Prüftool selbst.<br>Für die automatische Signaturprü-<br>fung ist ein vorhergehender Import<br>des XML-Schemas und der zugehö-<br>rigen Konfigurationsdatei mit der zu<br>prüfenden Signatur über das XML-<br>Schema in das Konsistenz-Prüftool<br>erforderlich.<br>Zusätzlich kann eine externe Signa-<br>turprüfung (ohne Nutzung des Kon-<br>sistenz-Prüftools) durchgeführt wer-<br>den.<br>XML-Schema für Über- Äußere technische Signatur über das  S_Prüftool-Schema P_Prüftool-Schema ist<br>setzungstabellen XML-Schema. im Konsistenz-Prüf-<br>(zugehörig zum Konsis- Automatische Signaturprüfung im  tool selbst hinterlegt<br>tenz-Prüftool) Konsistenz-Prüftool selbst.<br>Für die automatische Signaturprü-<br>fung ist ein vorhergehender Import<br>des XML-Schemas und der zugehö-<br>rigen Konfigurationsdatei mit der zu<br>prüfenden Signatur über das XML-<br>Schema in das Konsistenz-Prüftool<br>erforderlich.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

13 

BSI TR-03144 Anhang 


![](markdown/tr/TR-03144v1_2_Anhang/TR-03144v1_2_Anhang.pdf-0014-01.png)


**----- Start of picture text -----**<br>
Artefakt Technische / Organisatorische Lö- Typ des Signatur- Speicherort des Si-<br>sung schlüssels gnaturprüfschlüssels<br>(abgesehen von der Schlüs-<br>seltabelle der TR-Zertifi-<br>zierungsstelle des BSI, sie-<br>he Kap. 6)<br>Zusätzlich kann eine externe Signa-<br>turprüfung (ohne Nutzung des Kon-<br>sistenz-Prüftools) durchgeführt wer-<br>den.<br>XML-Schema für Test- Äußere technische Signatur über das  S_Prüftool-Schema P_Prüftool-Schema ist<br>berichte XML-Schema. im Konsistenz-Prüf-<br>(zugehörig zum Konsis- Automatische Signaturprüfung im  tool selbst hinterlegt<br>tenz-Prüftool) Konsistenz-Prüftool selbst.<br>Für die automatische Signaturprü-<br>fung ist ein vorhergehender Import<br>des XML-Schemas und der zugehö-<br>rigen Konfigurationsdatei mit der zu<br>prüfenden Signatur über das XML-<br>Schema in das Konsistenz-Prüftool<br>erforderlich.<br>Zusätzlich kann eine externe Signa-<br>turprüfung (ohne Nutzung des Kon-<br>sistenz-Prüftools) durchgeführt wer-<br>den.<br>Benutzerdokumentation  Integre/authentische Auslieferung  (S_Prüftool-Dok) ---<br>zum Konsistenz-Prüf- der Dokumentation durch die gema-<br>tool tik in Papierform oder in elektroni-<br>scher Form.<br>Äußere Signatur über die Dokumen-<br>tation im Falle einer elektronischen<br>Auslieferung.<br>TR-Zertifikat und -Kon- Bezug von den Webseiten des BSI  --- ---<br>formitätsreport zum  oder sonstige integre/authentische<br>Konsistenz-Prüftool Auslieferung einer Kopie des Origi-<br>nals.<br>Inputquellen für das Konsistenz-Prüftool<br>--- ---<br>Konfigurationsdatei mit  Im Konsistenz-Prüftool erfolgt unter<br>der Signatur über das  Verwendung des im Konsistenz-<br>Konsistenz-Prüftool  Prüftool hinterlegten Signaturprüf-<br>(Code / Dateien mit den  schlüssels P_Prüftool-Code eine<br>Java-Bibliotheken inklu- Prüfung der in der Konfigurations-<br>sive Java-Laufzeitumge- datei enthaltenen Signatur über das<br>bung) Konsistenz-Prüftool.<br>Für die Signaturprüfung ist ein vor-<br>hergehender Import der Konfigura-<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

14 

BSI TR-03144 Anhang 


![](markdown/tr/TR-03144v1_2_Anhang/TR-03144v1_2_Anhang.pdf-0015-01.png)


**----- Start of picture text -----**<br>
Artefakt Technische / Organisatorische Lö- Typ des Signatur- Speicherort des Si-<br>sung schlüssels gnaturprüfschlüssels<br>(abgesehen von der Schlüs-<br>seltabelle der TR-Zertifi-<br>zierungsstelle des BSI, sie-<br>he Kap. 6)<br>tionsdatei in das Konsistenz-Prüftool<br>erforderlich.<br>Auf eine kryptographische Siche-<br>rung der Konfigurationsdatei selbst<br>kann verzichtet werden.<br>--- ---<br>Konfigurationsdatei mit  Im Konsistenz-Prüftool erfolgt unter<br>der Signatur über das  Verwendung des im Konsistenz-<br>XML-Schema für Ob- Prüftool hinterlegten Signaturprüf-<br>jektsystem-Spezifikatio- schlüssels P_Prüftool-Schema eine<br>nen Prüfung der in der Konfigurations-<br>datei enthaltenen Signatur über das<br>XML-Schema.<br>Für die Signaturprüfung ist ein vor-<br>hergehender Import der Konfigura-<br>tionsdatei in das Konsistenz-Prüftool<br>erforderlich.<br>Auf eine kryptographische Siche-<br>rung der Konfigurationsdatei selbst<br>kann verzichtet werden.<br>--- ---<br>Konfigurationsdatei mit  Im Konsistenz-Prüftool erfolgt unter<br>der Signatur über das  Verwendung des im Konsistenz-<br>XML-Schema für Fin- Prüftool hinterlegten Signaturprüf-<br>gerprint-Sollwerte schlüssels P_Prüftool-Schema eine<br>Prüfung der in der Konfigurations-<br>datei enthaltenen Signatur über das<br>XML-Schema.<br>Für die Signaturprüfung ist ein vor-<br>hergehender Import der Konfigura-<br>tionsdatei in das Konsistenz-Prüftool<br>erforderlich.<br>Auf eine kryptographische Siche-<br>rung der Konfigurationsdatei selbst<br>kann verzichtet werden.<br>--- ---<br>Konfigurationsdatei mit  Im Konsistenz-Prüftool erfolgt unter<br>der Signatur über das  Verwendung des im Konsistenz-<br>XML-Schema für Über- Prüftool hinterlegten Signaturprüf-<br>setzungstabellen schlüssels P_Prüftool-Schema eine<br>Prüfung der in der Konfigurations-<br>datei enthaltenen Signatur über das<br>XML-Schema.<br>Für die Signaturprüfung ist ein vor-<br>hergehender Import der Konfigura-<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

15 

BSI TR-03144 Anhang 


![](markdown/tr/TR-03144v1_2_Anhang/TR-03144v1_2_Anhang.pdf-0016-01.png)


**----- Start of picture text -----**<br>
Artefakt Technische / Organisatorische Lö- Typ des Signatur- Speicherort des Si-<br>sung schlüssels gnaturprüfschlüssels<br>(abgesehen von der Schlüs-<br>seltabelle der TR-Zertifi-<br>zierungsstelle des BSI, sie-<br>he Kap. 6)<br>tionsdatei in das Konsistenz-Prüftool<br>erforderlich.<br>Auf eine kryptographische Siche-<br>rung der Konfigurationsdatei selbst<br>kann verzichtet werden.<br>--- ---<br>Konfigurationsdatei mit  Im Konsistenz-Prüftool erfolgt unter<br>der Signatur über das  Verwendung des im Konsistenz-<br>XML-Schema für Test- Prüftool hinterlegten Signaturprüf-<br>berichte schlüssels P_Prüftool-Schema eine<br>Prüfung der in der Konfigurations-<br>datei enthaltenen Signatur über das<br>XML-Schema.<br>Für die Signaturprüfung ist ein vor-<br>hergehender Import der Konfigura-<br>tionsdatei in das Konsistenz-Prüftool<br>erforderlich.<br>Auf eine kryptographische Siche-<br>rung der Konfigurationsdatei selbst<br>kann verzichtet werden.<br>--- ---<br>Konfigurationsdatei mit  Im Konsistenz-Prüftool erfolgt unter<br>der Signatur über die  Verwendung des in das Konsistenz-<br>XML-Datei der Objekt- Prüftool importierten Signaturprüf-<br>system-Spezifikation xy  schlüssels P_Objektsys-Spez (Im-<br>(XML-Master / XML- port mittels seiner zugehörigen Kon-<br>Derivat) figurationsdatei, siehe unten) eine<br>(xy = eGK/HBA/ Prüfung der in der Konfigurations-<br>SMC-B/gSMC-K/ datei enthaltenen Signatur über die<br>gSMC-KT/...) XML-Datei der Objektsystem-Spe-<br>zifikation xy.<br>Für die Signaturprüfung ist ein vor-<br>hergehender Import der Konfigura-<br>tionsdatei in das Konsistenz-Prüftool<br>erforderlich.<br>Auf eine kryptographische Siche-<br>rung der Konfigurationsdatei selbst<br>kann verzichtet werden.<br>--- ---<br>Konfigurationsdatei mit  Im Konsistenz-Prüftool erfolgt unter<br>der Signatur über das  Verwendung des in das Konsistenz-<br>Challenge/Fingerprint- Prüftool importierten Signaturprüf-<br>Referenzwert-Paar der  schlüssels P_Plattform-FP (Import<br>Karten-Plattform mittels seiner zugehörigen Konfigu-<br>rationsdatei, siehe unten) eine Prü-<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

16 

BSI TR-03144 Anhang 


![](markdown/tr/TR-03144v1_2_Anhang/TR-03144v1_2_Anhang.pdf-0017-01.png)


**----- Start of picture text -----**<br>
Artefakt Technische / Organisatorische Lö- Typ des Signatur- Speicherort des Si-<br>sung schlüssels gnaturprüfschlüssels<br>(abgesehen von der Schlüs-<br>seltabelle der TR-Zertifi-<br>zierungsstelle des BSI, sie-<br>he Kap. 6)<br>fung der in der Konfigurationsdatei<br>enthaltenen Signatur über das Chal-<br>lenge/Fingerprint-Referenzwert-<br>Paar.<br>Für die Signaturprüfung ist ein vor-<br>hergehender Import der Konfigura-<br>tionsdatei in das Konsistenz-Prüftool<br>erforderlich.<br>Auf eine kryptographische Siche-<br>rung der Konfigurationsdatei selbst<br>kann verzichtet werden.<br>--- ---<br>Konfigurationsdatei mit  Im Konsistenz-Prüftool erfolgt unter<br>der Signatur über die  Verwendung des in das Konsistenz-<br>Übersetzungstabelle  Prüftool importierten Signaturprüf-<br>(XML-Datei) zur Kar- schlüssels P_Übersetzung (Import<br>ten-Plattform mittels seiner zugehörigen Konfigu-<br>rationsdatei, siehe unten) eine Prü-<br>fung der in der Konfigurationsdatei<br>enthaltenen Signatur über die XML-<br>Datei mit der Übersetzungstabelle.<br>Für die Signaturprüfung ist ein vor-<br>hergehender Import der Konfigura-<br>tionsdatei in das Konsistenz-Prüftool<br>erforderlich.<br>Auf eine kryptographische Siche-<br>rung der Konfigurationsdatei selbst<br>kann verzichtet werden.<br>Konfigurationsdatei mit  Außerhalb des Konsistenz-Prüftools  --- ---<br>dem Signaturprüf- erfolgt eine Überprüfung der Integri-<br>schlüssel für die Prü- tät/Authentizität der Konfigurations-<br>fung der Signatur über  datei bzw. des darin enthaltenen Si-<br>die XML-Datei der Ob- gnaturprüfschlüssels P_Objektsys-<br>jektsystem-Spezifi- Spez gegen die mit S_Schlüsselta-<br>kation xy (XML-Mas- belle signierte Schlüsseltabelle von<br>ter / XML-Derivat) Signaturprüfschlüsseln (siehe Kap.<br>(xy = eGK/HBA/ 6).<br>SMC-B/gSMC-K/ Auf eine kryptographische Siche-<br>gSMC-KT/...) rung der Konfigurationsdatei selbst<br>kann verzichtet werden.<br>Es erfolgt ein Import der Konfigura-<br>tionsdatei in das Konsistenz-Prüf-<br>tool, damit der enthaltene Signatur-<br>prüfschlüssel P_Objektsys-Spez im<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

17 

BSI TR-03144 Anhang 


![](markdown/tr/TR-03144v1_2_Anhang/TR-03144v1_2_Anhang.pdf-0018-01.png)


**----- Start of picture text -----**<br>
Artefakt Technische / Organisatorische Lö- Typ des Signatur- Speicherort des Si-<br>sung schlüssels gnaturprüfschlüssels<br>(abgesehen von der Schlüs-<br>seltabelle der TR-Zertifi-<br>zierungsstelle des BSI, sie-<br>he Kap. 6)<br>Konsistenz-Prüftool zur weiteren<br>Verwendung zur Verfügung steht.<br>Konfigurationsdatei mit  Außerhalb des Konsistenz-Prüftools  --- ---<br>dem Signaturprüf- erfolgt eine Überprüfung der Integri-<br>schlüssel für die Prü- tät/Authentizität der Konfigurations-<br>fung der Signatur über  datei bzw. des darin enthaltenen Si-<br>das Challenge/ gnaturprüfschlüssels P_Plattform-FP<br>Fingerprint-Referenz- gegen die mit S_Schlüsseltabelle si-<br>wert-Paar der Karten- gnierte Schlüsseltabelle von Signa-<br>Plattform turprüfschlüsseln (siehe Kap. 6).<br>Auf eine kryptographische Siche-<br>rung der Konfigurationsdatei selbst<br>kann verzichtet werden.<br>Es erfolgt ein Import der Konfigura-<br>tionsdatei in das Konsistenz-Prüf-<br>tool, damit der enthaltene Signatur-<br>prüfschlüssel P_Plattform-FP im<br>Konsistenz-Prüftool zur weiteren<br>Verwendung zur Verfügung steht.<br>Konfigurationsdatei mit  Außerhalb des Konsistenz-Prüftools  --- ---<br>dem Signaturprüf- erfolgt eine Überprüfung der Integri-<br>schlüssel für die Prü- tät/Authentizität der Konfigurations-<br>fung der Signatur über  datei bzw. des darin enthaltenen Si-<br>die Übersetzungstabelle  gnaturprüfschlüssels P_Übersetzung<br>(XML-Datei) zur Kar- gegen die mit S_Schlüsseltabelle si-<br>ten-Plattform gnierte Schlüsseltabelle von Signa-<br>turprüfschlüsseln (siehe Kap. 6).<br>Auf eine kryptographische Siche-<br>rung der Konfigurationsdatei selbst<br>kann verzichtet werden.<br>Es erfolgt ein Import der Konfigura-<br>tionsdatei in das Konsistenz-Prüf-<br>tool, damit der enthaltene Signatur-<br>prüfschlüssel P_Übersetzung im<br>Konsistenz-Prüftool zur weiteren<br>Verwendung zur Verfügung steht.<br>XML-Datei der Objekt- Äußere Signatur der XML-Datei. S_Objektsys-Spez Konfigurationsdatei<br>system-Spezifikation xy  mit dem Signatur-<br>Im Konsistenz-Prüftool erfolgt unter<br>(XML-Master / XML- prüfschlüssel P_Ob-<br>Verwendung des Signaturprüf-<br>Derivat) jektsys-Spez<br>schlüssels P_Objektsys-Spez eine<br>(xy = eGK/HBA/ Prüfung der Signatur über die XML-<br>SMC-B/gSMC-K/ Datei der Objektsystem-Spezifikati-<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

18 

BSI TR-03144 Anhang 


![](markdown/tr/TR-03144v1_2_Anhang/TR-03144v1_2_Anhang.pdf-0019-01.png)


**----- Start of picture text -----**<br>
Artefakt Technische / Organisatorische Lö- Typ des Signatur- Speicherort des Si-<br>sung schlüssels gnaturprüfschlüssels<br>(abgesehen von der Schlüs-<br>seltabelle der TR-Zertifi-<br>zierungsstelle des BSI, sie-<br>he Kap. 6)<br>gSMC-KT/...) on xy.<br>Für die Signaturprüfung ist ein vor-<br>hergehender Import der zugehörigen<br>Konfigurationsdatei mit dem Signa-<br>turprüfschlüssel P_Objektsys-Spez<br>in das Konsistenz-Prüftool erforder-<br>lich.<br>Challenge/Fingerprint- Die vertrauliche Übermittlung des  S_Plattform-FP Konfigurationsdatei<br>Referenzwert-Paar der  signierten Challenge/Fingerprint-Re- mit dem Signatur-<br>Karten-Plattform ferenzwert-Paars vom Hersteller der  prüfschlüssel P_Platt-<br>dem Karten-Produkt unterliegenden  form-FP<br>Karten-Plattform an die TR-Prüfstel-<br>le für das betreffende Karten-Pro-<br>dukt erfolgt verschlüsselt. Das erfor-<br>derliche Schlüsselmaterial zur Ver-<br>schlüsselung des Datenaustausches<br>ist vorab gesichert zwischen dem<br>Hersteller der Karten-Plattform und<br>der TR-Prüfstelle für das Karten-<br>Produkt auszutauschen.<br>Für den Hersteller der Karten-Platt-<br>form und die TR-Prüfstelle für das<br>Karten-Produkt wird von einer aus-<br>reichend gesicherten Umgebung<br>ausgegangen, so dass ein dort im<br>Klartext vorliegendes Challen-<br>ge/Fingerprint-Referenzwert-Paar<br>ausreichend gesichert behandelt<br>wird.<br>Hinweis: Das Konsistenz-Prüftool<br>benötigt für die Weiterverwendung<br>des Challenge/Fingerprint-Referenz-<br>wert-Paars dieses im Klartext, da das<br>Konsistenz-Prüftool selbst keine<br>Entschlüsselungsfunktion bereit-<br>stellt.<br>Äußere Signatur des Challenge/Fin-<br>gerprint-Referenzwert-Paars.<br>Im Konsistenz-Prüftool erfolgt unter<br>Verwendung des Signaturprüf-<br>schlüssels P_Plattform-FP eine Prü-<br>fung der Signatur über das Challen-<br>ge/Fingerprint-Referenzwert-Paar.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

19 

BSI TR-03144 Anhang 


![](markdown/tr/TR-03144v1_2_Anhang/TR-03144v1_2_Anhang.pdf-0020-01.png)


**----- Start of picture text -----**<br>
Artefakt Technische / Organisatorische Lö- Typ des Signatur- Speicherort des Si-<br>sung schlüssels gnaturprüfschlüssels<br>(abgesehen von der Schlüs-<br>seltabelle der TR-Zertifi-<br>zierungsstelle des BSI, sie-<br>he Kap. 6)<br>Für die Signaturprüfung ist ein vor-<br>hergehender Import der zugehörigen<br>Konfigurationsdatei mit dem Signa-<br>turprüfschlüssel P_Plattform-FP in<br>das Konsistenz-Prüftool erforder-<br>lich.<br>Übersetzungstabelle  Äußere Signatur der XML-Datei. S_Übersetzung Konfigurationsdatei<br>(XML-Datei) zur Kar- mit dem Signatur-<br>Im Konsistenz-Prüftool erfolgt unter<br>ten-Plattform prüfschlüssel P_Über-<br>Verwendung des Signaturprüf-<br>setzung<br>schlüssels P_Übersetzung eine Prü-<br>fung der Signatur über die XML-Da-<br>tei mit der Übersetzungstabelle.<br>Für die Signaturprüfung ist ein vor-<br>hergehender Import der zugehörigen<br>Konfigurationsdatei mit dem Signa-<br>turprüfschlüssel P_Übersetzung in<br>das Konsistenz-Prüftool erforder-<br>lich.<br>Output des Konsistenz-Prüftools<br>Testbericht Es wird auf eine kryptographische  --- ---<br>Sicherung durch das Konsistenz-<br>Prüftool selbst verzichtet.<br>Es steht der TR-Prüfstelle für das<br>betreffende Karten-Produkt aber<br>frei, zusätzlich selbst eine kryptogra-<br>phische Sicherung an den Testbe-<br>richt (z.B. in Form einer Signatur<br>und/oder Verschlüsselung) anzubrin-<br>gen. In diesem Fall obliegt es der<br>TR-Prüfstelle, zugehöriges Schlüs-<br>selmaterial (z.B. für die Prüfung der<br>Signatur und/oder die Entschlüsse-<br>lung) gesichert mit der den Testbe-<br>richt nutzenden Stelle auszutau-<br>schen.<br>Der vom Konsistenz-Prüftool ausge-<br>gebene Testbericht wird dem TR-<br>Prüfbericht der TR-Prüfstelle für das<br>betreffende Karten-Produkt beige-<br>fügt. Dieser TR-Prüfbericht wird<br>insgesamt von der TR-Prüfstelle in<br>Papierform unterschrieben und der<br>TR-Zertifizierungsstelle des BSI<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

20 

BSI TR-03144 Anhang 


![](markdown/tr/TR-03144v1_2_Anhang/TR-03144v1_2_Anhang.pdf-0021-01.png)


**----- Start of picture text -----**<br>
Artefakt Technische / Organisatorische Lö- Typ des Signatur- Speicherort des Si-<br>sung schlüssels gnaturprüfschlüssels<br>(abgesehen von der Schlüs-<br>seltabelle der TR-Zertifi-<br>zierungsstelle des BSI, sie-<br>he Kap. 6)<br>übermittelt.<br>**----- End of picture text -----**<br>


Tabelle 5: Artefakte und ihre Sicherungsmechanismen 

## Hinweis: 

Die Signaturen über die XML-Schemata für Objektsystem-Spezifikationen, Fingerprint-Sollwerte, Übersetzungstabellen und Testberichte sowie die Signaturen über die XML-Dateien der Objektsystem-Spezifikationen (XML-Master / XML-Derivat) und der Übersetzungstabellen sind _nicht_ Bestandteil der zuvor genannten XML-Strukturen. Diese Signaturen werden jeweils als äußere Signaturen an die XML-Schemata bzw. XML-Dateien angebracht. Hintergrund hierfür ist, dass XML-Signaturen für XML-Schemata nach dem standardisierten XML-Signatur-Verfahren nicht möglich sind. Um eine einheitliche Implementierung der Signaturprüfung im Konsistenz-Prüftool zu erreichen, wird auch für XML-Dateien entsprechend mit einer äußeren Signatur gearbeitet. Weiterer Vorteil äußerer Signaturen im vorliegenden Fall ist die größere Flexibilität bzgl. der Auswahl kryptographischer Verfahren. 

Bundesamt für Sicherheit in der Informationstechnik 

21 

BSI TR-03144 Anhang 

## **4 Übersicht über die Signaturschlüsselpaare** 

In der nachfolgenden Tabelle  6 wird eine Übersicht über die benötigten Typen von Signaturschlüsselpaaren  (bzw. Signaturschlüsseln  und  zugehörigen  Signaturprüfschlüsseln),  deren  Verwendungszweck und deren Inhaber bzw. Nutzer gegeben. Siehe hierzu auch Kap. 3. 

Notation: In der letzten Tabellenspalte werden nur diejenigen Stellen benannt, die mindestens den betreffenden Signaturprüfschlüssel (direkt oder indirekt, z.B. bei der Nutzung des Konsistenz-Prüftools) verwenden. 


![](markdown/tr/TR-03144v1_2_Anhang/TR-03144v1_2_Anhang.pdf-0022-04.png)


**----- Start of picture text -----**<br>
Signaturschlüsselpaar Verwendungszweck des  Generierende Stelle /  Verwendende Stelle des Si-<br>Signaturschlüssels Inhaber des Signa- gnaturprüfschlüssels<br>(Signaturschlüssel /<br>turschlüsselpaars<br>Signaturprüfschlüssel)<br>S_Prüftool-Code / Signatur über die Imple- gematik • TR-Zertifizierungsstelle<br>P_Prüftool-Code mentierung des Konsistenz- (BSI)<br>Prüftools • TR-Prüfstellen für Kar-<br>ten-Produkte<br>Hinweis:<br>Der Signaturprüfschlüssel P_<br>Prüftool-Code ist im Konsis-<br>tenz-Prüftool enthalten.<br>S_Prüftool-Schema / Signatur über die zum Kon- gematik • TR-Zertifizierungsstelle<br>P_Prüftool-Schema sistenz-Prüftool zugehöri- (BSI)<br>gen XML-Schemata für  • TR-Prüfstellen für Kar-<br>Objektsystem-Spezifikatio-<br>ten-Produkte<br>nen, Fingerprint-Sollwerte,<br>Übersetzungstabellen und  Hinweis:<br>Testberichte Der Signaturprüfschlüssel P_<br>Prüftool-Schema ist im Kon-<br>sistenz-Prüftool enthalten.<br>S_Prüftool-Dok / Signatur der Benutzerdoku- gematik • TR-Zertifizierungsstelle<br>P_Prüftool-Dok mentation zum Konsistenz- (BSI)<br>Prüftool (sofern elektroni- • TR-Prüfstellen für Kar-<br>sche Auslieferung vorgese-<br>ten-Produkte<br>hen)<br>S_Objektsys-Spez / Signatur über die XML-Da- gematik • TR-Zertifizierungsstelle<br>P_Objektsys-Spez tei der Objektsystem-Spezi- (BSI)<br>fikation (XML-Master /  • TR-Prüfstellen für Kar-<br>XML-Derivat)<br>ten-Produkte<br>Hinweis:<br>Der Signaturprüfschlüssel<br>P_Objektsys-Spez ist in der<br>zur Objektsystem-Spezifika-<br>tion zugehörigen Konfigura-<br>tionsdatei für das Konsistenz-<br>Prüftool enthalten.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

22 

BSI TR-03144 Anhang 


![](markdown/tr/TR-03144v1_2_Anhang/TR-03144v1_2_Anhang.pdf-0023-01.png)


**----- Start of picture text -----**<br>
Signaturschlüsselpaar Verwendungszweck des  Generierende Stelle /  Verwendende Stelle des Si-<br>Signaturschlüssels Inhaber des Signa- gnaturprüfschlüssels<br>(Signaturschlüssel /<br>turschlüsselpaars<br>Signaturprüfschlüssel)<br>S_Plattform-FP / Signatur über das Challen- CC-Prüfstelle der be- • TR-Zertifizierungsstelle<br>P_Plattform-FP ge/Fingerprint-Referenz- treffenden Karten- (BSI)<br>wert-Paar einer Karten- Plattform • TR-Prüfstellen für Kar-<br>Plattform<br>ten-Produkte, die auf der<br>betreffenden Karten-Platt-<br>form aufsetzen<br>Hinweis:<br>Der Signaturprüfschlüssel<br>P_Plattform-FP ist in der<br>zum Challenge/Fingerprint-<br>Referenzwert-Paar zugehöri-<br>gen Konfigurationsdatei für<br>das Konsistenz-Prüftool ent-<br>halten.<br>S_Übersetzung / Signatur über die Überset- CC-Prüfstelle der  • TR-Zertifizierungsstelle<br>P_Übersetzung zungstabelle (XML-Datei)  (dem betreffenden  (BSI)<br>zu einer Karten-Plattform Karten-Produkt unter- • TR-Prüfstelle des betref-<br>liegenden) Karten-<br>fenden Karten-Produktes<br>Plattform oder TR-<br>Prüfstelle des betref- Hinweis:<br>fenden Karten-Pro- Der Signaturprüfschlüssel<br>duktes P_Übersetzung ist in der zur<br>Übersetzungstabelle zugehö-<br>rigen Konfigurationsdatei für<br>das Konsistenz-Prüftool ent-<br>halten.<br>S_Schlüsseltabelle / Signatur über die Schlüssel- TR-Zertifizierungs- • gematik<br>P_Schlüsseltabelle tabelle mit den Signatur- stelle (BSI) • TR-Prüfstellen für Kar-<br>prüfschlüsseln ten-Produkte<br>**----- End of picture text -----**<br>


Tabelle 6: Übersicht der Signaturschlüsselpaare 

Es besteht die Möglichkeit, die Signaturschlüsselpaare 

- (S_Prüftool-Code, P_Prüftool-Code), 

- (S_Prüftool-Schema, P_Prüftool-Schema), 

- (S_Prüftool-Dok, P_Prüftool-Dok) und 

- (S_Objektsys-Spez, P_Objektsys-Spez) 

zusammenzufassen, also durch ein einziges Schlüsselpaar zu repräsentieren. 

Für die sichere (d.h. integre und authentische) Auslieferung der Signaturprüfschlüssel an die TRZertifizierungsstelle für die Schlüsseltabelle (siehe Kap. 6) ist der jeweilige Inhaber des zugehörigen Signaturschlüsselpaars bzw. dessen zugeordnete Stelle verantwortlich. 

Bundesamt für Sicherheit in der Informationstechnik 

23 

BSI TR-03144 Anhang 

## **5 Kryptographische Vorgaben** 

Für die in Kap. 3 genannten Signaturen soll RSA mit einer Schlüssellänge von mindestens 2048 Bit mit SHA-256 (mit einem ausreichend sicheren Signatur-/Paddingverfahren) verwendet werden. 

Für die Erzeugung von Signaturen (siehe Kap. 3) soll (zunächst) eine PGP-Implementierung, die konform zur standardisierten Version OpenPGP gemäß [RFC 4880] ist, eingesetzt werden. 

Die Generierung der Signaturschlüsselpaare soll ebenfalls durch eine solche PGP-Implementierung erfolgen. Die PGP-Signaturschlüsselpaare werden dabei in einem zu [RFC 4880] konformen PGPFormat angelegt; das Feld userID ist dabei mit dem Namen der Organisation, der der Inhaber des Signaturschlüsselpaars angehört, zu füllen. Für weitere Details hierzu sei auf die Benutzerdokumentation zum Konsistenz-Prüftool verwiesen. 

Die für die Generierung eines Signaturschlüsselpaars eingesetzte PGP-Implementierung soll weiterhin für den Signaturprüfschlüssel die Erstellung und Ausgabe eines PGP-Fingerprints ermöglichen, der dann in der Schlüsseltabelle mit den Signaturprüfschlüsseln (siehe Kap. 6) hinterlegt wird. 

## Hinweis: 

Zukünftig ist vorgesehen, die PGP-Lösung durch eine andere, PKI-basierte Lösung, die sich an den Vorgaben der Technischen Richtlinie BSI TR-03116-1 ([TR-03116-1]) orientiert, zu ersetzen. 

Bundesamt für Sicherheit in der Informationstechnik 

24 

BSI TR-03144 Anhang 

## **6 Schlüsselverwaltung** 

Zwecks Schlüsselverwaltung wird eine Schlüsseltabelle mit den im Rahmen von TR-Konformitätsprüfungen von Karten-Produkten nach der Technischen Richtlinie BSI TR-03144 ([TR-03144]) verwendeten Signaturprüfschlüsseln (siehe auch Kap. 4) aufgesetzt und gepflegt. 

Die Schlüsseltabelle liefert eine Übersicht über die verwendeten Signaturprüfschlüssel und stellt für jeden eingetragenen Signaturprüfschlüssel folgende Informationen bereit: 

- Name und Anschrift der Stelle, der der Inhaber des zugehörigen Signaturschlüsselpaars angehört. 

Als Stelle kommt zur Auswahl: 

CC-Prüfstelle für Karten-Plattform, gematik, TR-Prüfstelle für Karten-Produkt, TRZertifizierungsstelle (BSI). 

- Name des Inhabers des zugehörigen Signaturschlüsselpaars. 

- Schlüssel-ID des Signaturprüfschlüssels. 

- Typ des Signaturprüfschlüssels. 

Als Typ des Signaturprüfschlüssels kommt zur Auswahl: 

   - P_Prüftool-Code, P_Prüftool-Schema, P_Prüftool-Dok, P_Objektsys-Spez, P_Plattform-FP, P_Übersetzung, P_Schlüsseltabelle. 

- Laufzeit (insbesondere Ablaufdatum) des zugehörigen Signaturschlüsselpaars. 

- PGP-Fingerprint des Signaturprüfschlüssels. 

Es empfiehlt sich, für einen Signaturprüfschlüssel bzw. ein Signaturschlüsselpaar eine geeignete Vertreterregelung einzurichten bzw. pro Stelle mehrere Signaturschlüsselpaare bzw. Signaturprüfschlüssel vorzusehen. 

Die Schlüsseltabelle enthält insbesondere den (bzw. die) Signaturprüfschlüssel der TR-Zertifizierungsstelle des BSI vom Typ P_Schlüsseltabelle. 

Die Ausgestaltung und Verwaltung der Schlüsseltabelle erfolgt durch die TR-Zertifizierungsstelle des BSI. Die Schlüsselinhaber bzw. deren zugeordnete Stelle haben der TR-Zertifizierungsstelle des BSI für die Schlüsseltabelle ihre Signaturprüfschlüssel sowie die benötigten weiteren Informationen zu ihren Schlüsseln in integrer und authentischer Weise bereitzustellen. Die Vergabe der SchlüsselID für einen Signaturprüfschlüssel erfolgt durch die TR-Zertifizierungsstelle des BSI. Die Schlüsseltabelle unterliegt einer Versionierung und wird mit Versionsnummer und Datum versehen. 

Die Schlüsseltabelle kann für Zwecke der TR-Konformitätsprüfung von Karten-Produkten nach der Technischen Richtlinie BSI TR-03144 ([TR-03144]) von der TR-Zertifizierungsstelle des BSI von den in eine solche Prüfung involvierten Stellen bezogen werden. Gleiches gilt für Zwecke weitergehender Prüf- oder Zulassungs-Prozesse/Verfahren von Karten-Plattformen und Karten-Produkten auf Seiten der gematik, die außerhalb der vorgenannten TR-Konformitätsprüfung von Karten-Produkten liegen. 

Hinweis: Je nach Erfordernis kann die Schlüsseltabelle auch an CC-Prüfstellen weitergegeben werden, die im Rahmen der CC-Zertifizierung von Karten-Produkten als Sichere Signaturerstellungseinheit (SSEE) nach eIDAS vom Konsistenz-Prüftool Gebrauch machen wollen. 

Bundesamt für Sicherheit in der Informationstechnik 

25 

BSI TR-03144 Anhang 

Für eine integre und authentische Auslieferung der Schlüsseltabelle wird diese von der TR-Zertifizierungsstelle des BSI unter Verwendung eines Signaturschlüssels vom Typ S_Schlüsseltabelle signiert und zusammen mit ihrer Signatur ausgeliefert. Der für die Prüfung der Signatur über die Schlüsseltabelle  relevante  Signaturprüfschlüssel  vom  Typ  P_Schlüsseltabelle  wird  mit  seiner Schlüssel-ID in der Schlüsseltabelle ausgewiesen. (Hinweis: Auf eine Signatur eines jeden einzelnen in der Schlüsseltabelle eingetragenen Signaturprüfschlüssels durch die TR-Zertifizierungsstelle des BSI kann (und soll aus Effizienzgründen) verzichtet werden, da eine Signatur über die Schlüsseltabelle, die insbesondere für jeden eingetragenen Signaturprüfschlüssel seinen PGP-Fingerprint beinhaltet, als ausreichend zu erachten ist.) 

Bundesamt für Sicherheit in der Informationstechnik 

26 

BSI TR-03144 Anhang 

## **Literaturverzeichnis** 

- [TR-03106] BSI TR-03106 eHealth - Zertifizierungskonzept für Karten der Generation G2, aktuelle Fassung, BSI 

- [TR-03143] BSI TR-03143 eHealth - G2-COS Konsistenz-Prüftool, aktuelle Fassung, BSI 

- [TR-03144] BSI TR-03144 eHealth - Konformitätsnachweis für Karten-Produkte der Kartengeneration G2, aktuelle Fassung, BSI 

- [TR-03116-1] BSI TR-03116-1 Kryptographische Vorgaben für Projekte der Bundesregierung, Teil 1: Telematikinfrastruktur, aktuelle Fassung, BSI 

- [RFC 4880] RFC 4880, J. Callas, L. Donnerhacke, H. Finney, D. Shaw, R. Thayer, OpenPGP Message Format, 2007, IETF 

Bundesamt für Sicherheit in der Informationstechnik 

27 


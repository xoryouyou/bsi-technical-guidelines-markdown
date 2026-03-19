
![](markdown/tr/TR_De_Mail_ID_IO/TR_De_Mail_ID_IO.pdf-0001-00.png)



![](markdown/tr/TR_De_Mail_ID_IO/TR_De_Mail_ID_IO.pdf-0001-01.png)


BSI – Technische Richtlinie Bezeichnung: Identitätsbestätigungsdienst Interoperabilitätsspezifikation Anwendungsbereich: De-Mail Kürzel: BSI TR 01201 Teil 4.4 Version: 1.8 

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn Tel.: +49 22899 9582-0 E-Mail: de-mail@bsi.bund.de Internet: https://www.bsi.bund.de © Bundesamt für Sicherheit in der Informationstechnik 2024 

## **Inhaltsverzeichnis** 

|1|Einleitung....................................................................................................................................4|
|---|---|
|2|Datenstrukturen...........................................................................................................................5|
|2.1|Datenformate.......................................................................................................................................5|
|2.2|Ident-Karten.........................................................................................................................................6|
|2.3|Altersnachweise...................................................................................................................................7|
|2.4|Adresskarte..........................................................................................................................................8|
|2.5|De-Mail-Adress-Karte.........................................................................................................................8|
|2.6|XML-Format einer Ident-Bestätigung.................................................................................................9|
|2.7|XSD der Ident-Karten........................................................................................................................10|



Bundesamt für Sicherheit in der Informationstechnik 

3 

1 Einleitung 

## **1 Einleitung** 

Dieses Modul ist Bestandteil von [TR DM ID M]. Hier werden Datenstrukturen und Datenformate des Identitätsbestätigungsdienstes spezifiziert. 

Bundesamt für Sicherheit in der Informationstechnik 

4 

Datenstrukturen 2 

## **2 Datenstrukturen** 

In diesem Abschnitt werden die im ID verwendeten Datenstrukturen beschrieben. 

## **2.1 Datenformate** 

Gemäß [TR DM ID FU] muss eine Ident-Bestätigung eine von mehreren möglichen Ident-Karten gemäß [TR DM ID FU] sowie zusätzliche Metadaten beinhalten. In die Metadaten der IdentBestätigungsnachricht müssen diese Metadaten übernommen werden und darüber hinaus weitere Metadaten auf bestimmte Werte gesetzt werden. Nachfolgend werden die Metadaten der IdentBestätigungsnachricht spezifiziert. Die Spezifikation der Metadaten der Ident-Bestätigung erfolgt im Rahmen der Beschreibung der XML-Struktur in Abschnitt 2.6. 

## **2.1.1 Metadaten einer Ident-Bestätigungsnachricht** 

Eine Ident-Bestätigungsnachricht muss die folgenden Metadaten gemäß [TR DM PVD FU] beinhalten: 

|**_Metadatum-_**<br>**_Nummer_**|**_Bezeichnung_**|**_Inhalt_**|
|---|---|---|
|5|Versandoption:|Persönlich=“yes“|
||Empfänger|Service Provider der Ident-Bestätigung erhalten soll|
|6|Absender:|Ident-Bestaetigung@<DMDA>|
|7,19|CC:|Auftraggeber der Ident-Bestätigung|
|8|Betreff:|„Ident-Bestätigung“|
|16|Nachrichten-<br>Typ:|Ident-Bestätigung (X-De-Mail-Message-Type:<br>identification)|



_Tabelle 1: Metadaten einer Ident-Bestätigung_ 

Der Inhalt der Nachricht muss folgenden Text enthalten: 

```
Hiermit werden die folgende Identitätsdaten zur angegebenen De-Mail-
Adresse bestätigt:
```

```
<Es werden alle Attribute aufgeführt, die auch in der XML-Datei enthalten
sind. Dazu SOLLTE die Bedeutung der Felder und der Werte des Feldes
dargestellt werden.>
```

Bundesamt für Sicherheit in der Informationstechnik 

5 

2 Datenstrukturen 

## **2.2 Ident-Karten** 

Identitätsinformationen werden in verschiedenen Ident-Karten (siehe [TR DM ID FU]) übermittelt. Eine Ident-Bestätigungsnachricht muss eine dieser Karten enthalten. Als Darstellungsformat werden im Folgenden für jeden Kartentyp XML-Datenstrukturen in Form einer XML Schema Definition (XSD) definiert. Aus Gründen der Übersichtlichkeit fehlen in den folgenden Darstellungen an jedem XML-Element einer Karte ein weiteres XML-Attribut (Validierungszeitpunkt), das immer vorhanden sein muss. Das Element `ValidationTime` enthält den Zeitpunkt, zu dem die Ausprägung des Attributes überprüft wurde. 

## **2.2.1 Identitätskarte einer natürlichen Person** 

Für die Identitätskarte einer natürliche Person können folgende Attribute verwendet werden. Die einzelnen Datenelemente sind: 

|**_Name_**|**_Datentyp_**|**_Maximale_**<br>**_Länge_**|**_Bedeutung_**|
|---|---|---|---|
|personalTitle|xs:string|40|Titel (akademischer Grad)|
|pseudonym|xs:string|60|Künstler-oder Ordensname (optional)|
|surname|xs:string|120|Nachname|
|givenname|xs:string|80|Vorname(n)|
|street|xs:string|100|Straße und Hausnummer|
|locality|xs:string|100|Wohnort|
|zip|Xs:int|10|Postleitzahl|
|country|xs:string|2|Staat (nach DIN EN ISO 3166 ALPHA-2)|
|dateOfBirth|xs:string|10|Geburtsdatum|
|locationOfBirth|xs:string|100|Geburtsort|
|age|xs:int||Alter als Zahl|
|de-mail-address|xs:string|255|De-Mail-Adresse|



_Tabelle 2: Identitätskarte einer natürlichen Person_ 

Die Felder „pseudonym“ und die Kombination der Felder „personalTitle“, „surname“ und „givenname“ können wahlweise zum Einsatz kommen. Es muss nur jeweils eines dieser Felder vorhanden sein. Bei Nutzung einer Pseudonym-Adresse als De-Mail-Adresse muss „pseudonym“ verwendet werden. 

Wenn für einen Nutzer kein vollständiges Geburtsdatum erfasst werde konnte, werden die nicht erfassten Teile mit dem Zeichen < im Feld „dateOfBirth“ aufgefüllt. Das Datum muss die Form dd.mm.yyyy (z.B. 01.01.2000) haben. 

Bundesamt für Sicherheit in der Informationstechnik 

6 

Datenstrukturen 2 

## **2.2.2 Identitätskarte einer Institution** 

Die Identitätskarte einer Institution kann folgende Felder enthalten: 

|**_Name_**|**_Datentyp_**|**_Maximale_**<br>**_Länge_**|**_Bedeutung_**|
|---|---|---|---|
|commonName|xs:string|255|Name der Institution|
|street|xs:string|100|Straße und Hausnummer|
|locality|xs:string|100|Ort|
|postOfficeBox|xs:string|10|Postfach|
|zip|xs:int|10|Postleitzahl|
|country|xs:string|2|Staat|
|legalForm|xs:string|60|Rechtsform|
|authorisedRepresentative|xs:string|255|Namen der Mitglieder des<br>Vertretungsorgans oder der gesetzliche<br>Vertreter|
|commercialRegisterType|xs:string|255|Art des Registereintrag|
|commercialRegisterEntry|xs:string|255|Registereintrag|
|commercialRegisterLocality|xs:string|255|Ort des Register|
|de-mail-address|xs:string|255|De-Mail-Adresse|



_Tabelle 3: Identitätskarte einer Institution_ 

## **2.3 Altersnachweise** 

Die Identitätskarte für einen Altersnachweis muss folgende Felder enthalten: 

|**_Name_**|**_Datentyp_**|**_Maximale_**<br>**_Länge_**|**_Bedeutung_**|
|---|---|---|---|
|age|xs:int||Alter des Nutzers|
|de-mail-address|xs:string|255|De-Mail-Adresse|



_Tabelle 4: Allgemeiner Altersnachweis_ 

|**_Name_**|**_Datentyp_**|**_Maximale_**<br>**_Länge_**|**_Bedeutung_**|
|---|---|---|---|
|over16|xs:boolean||Wahr, wenn der Nutzer älter als 16|



Bundesamt für Sicherheit in der Informationstechnik 

7 

2 Datenstrukturen 

||||Jahre ist, ansonsten unwahr|
|---|---|---|---|
|de-mail-address|xs:string|255|De-Mail-Adresse|



_Tabelle 5: Alternachweis für Nutzer über 16 Jahre_ 

|**_Name_**|**_Datentyp_**|**_Maximale_**<br>**_Länge_**|**_Bedeutung_**|
|---|---|---|---|
|over18|xs:boolean||Wahr, wenn der Nutzer älter als 18<br>Jahre ist, ansonsten unwahr|
|de-mail-address|xs:string|255|De-Mail-Adresse|



_Tabelle 6: Alternachweis für Nutzer über 18 Jahre_ 

## **2.4 Adresskarte** 

Die Identitätskarte für einen Adressnachweis muss folgende Felder enthalten: 

|**_Name_**|**_Datentyp_**|**_Maximale_**<br>**_Länge_**|**_Bedeutung_**|
|---|---|---|---|
|personalTitle|xs:string|40|Titel (akademischer Grad)|
|pseudonym|xs:string|60|Künstler-oder Ordensname|
|surname|xs:string|120|Nachname|
|givenname|xs:string|80|Vorname(n)|
|street|xs:string|100|Straße|
|locality|xs:string|100|Wohnort|
|zip|xs:int|10|Postleitzahl|
|country|xs:string|2|Staat (nach DIN EN ISO 3166 ALPHA-2)|
|de-mail-address|xs:string|255|De-Mail-Adresse|



## **2.5 De-Mail-Adress-Karte** 

Die Identitätskarte für eine De-Mail-Adress-Karte muss folgende Felder enthalten: 

Bundesamt für Sicherheit in der Informationstechnik 

8 

Datenstrukturen 2 

|**_Name_**|**_Datentyp_**|**_Maximale_**<br>**_Länge_**|**_Bedeutung_**|
|---|---|---|---|
|de-mail-address|xs:string|255|De-Mail-Adresse|



## **2.6 XML-Format einer Ident-Bestätigung** 

Eine Ident-Bestätigung muss als SAML-Assertion [SAML-CORE20] dargestellt werden. 

Das Attribut „Version“ muss auf den Wert „2.0“ fixiert sein. 

Das Attribut „ID“ muss zufällig und eineindeutig pro DMDA für jede neue Ident-Bestätigung erzeugt werden. 

Das Attribut „IssueInstant“ muss den Ausstellungszeitpunkt der Nachricht enthalten. 

Das Element „Issuer“ muss die De-Mail-Adresse des ausstellenden DMDA enthalten. Das Attribut „Format“ des Elements „Issuer“ muss „urn:oasis:names:tc:SAML:1.1:nameidformat:emailAddress” lauten. 

Es muss ein Element „signature“ vorhanden sein. Das Element „signature“ muss eine  qualifizierte elektronische Signatur über die XML-Struktur „Ident-Message“ enthalten. Es muss gemäß Abschnitt 5.4 in [SAML-CORE20] erstellt werden. Als Transformationen für die Erzeugung der Signatur müssen `Algorithm="http://www.w3.org/2000/09/xmldsig#envelopedsignature"` und `Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n20010315"` verwendet werden. 

Es muss ein Element „subject“ vorhanden sein. Das Element „subject“ muss den Auftraggeber der Ident-Bestätigungsnachricht angeben, dem die in der Assertion enthaltene Ident-Karte zugeordnet ist. Das Element „subject“ enthält nur das Element „NameID“, dessen Attribut „Format“ „urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress” lauten muss. Hier muss die De-MailAdresse (Primäre oder Pseudonym-De-Mail-Adresse) des Auftraggebers angegeben werden. 

Es muss ein Element „conditions“ vorhanden sein. Das Element „conditions“ enthält genau ein Element „audienceRestriction“. Das Element „audience“ enthält die De-Mail-Adresse des Empfängers der Karte. 

Eine Ident-Bestätigung gemäß dieser Spezfikation enthält genau ein „AuthnStatement“ und genau ein „AttributeStatement“. 

Das Element „AuthnStatement“ muss im Attribut „AuthInstant“ den Zeitpunkt enthalten, zu dem sich der Auftraggeber das letzte Mal gegenüber dem die Ident-Bestätigung ausstellenden De-MailPortal authentifiziert hat. Das Authentisierungsverfahren muss im Element „AuthnContext“ angegeben werden. Dies muss genau ein „AuthnContextClassRef“-Element enthalten, dessen Wert gemäß Abschnitt 3.4 [SAML-CORE20] das verwendete Verfahren bezeichnet. Da die Nutzung des ID nur mit Authentisierungsniveau „hoch“ möglich ist, kann unabhängig von dem angegebenen Verfahren von mindestens hohem Authentisierungsniveau ausgegangen werden. 

Ein Beispiel: 

Bundesamt für Sicherheit in der Informationstechnik 

9 

## 2 Datenstrukturen 

```
<saml:AuthnStatement AuthnInstant="2001-12-17T09:30:47.0Z"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">
```

```
<saml:AuthnContext>
```

## `<saml:AuthnContextClassRef>` 

```
urn:oasis:names:tc:SAML:2.0:ac:classes:MobileTwoFactorContract
```

```
</saml:AuthnContextClassRef>
```

```
</saml:AuthnContext>
```

```
</saml:AuthnStatement>
```

Das Element „AttributeStatement“ muss die übermittelte Identitätskarte enthalten. Diese muss als „Ident-Card“-Struktur im „AttributeValue“-Element des „Attribute“-Elements dieses Statements abgelegt werden. Ein Beispiel: 

## `<saml:AttributeStatement` 

```
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion">
```

```
<saml:Attribute Name="Card">
```

```
<saml:AttributeValue xsi:type=”de-mail:Identcard”>
```

```
<Identcard><NaturalPerson>…</NaturalPerson>
```

```
</Identcard>
```

```
 </saml:AttributeValue>
```

```
</saml:Attribute>
```

```
</saml:AttributeStatement>
```

Die „Ident-Card“-Struktur beinhaltet ein Element des Type NaturalPerson oder LegalPerson. Weitere mögliche Elemente einer SAML-Assertion werden nicht benutzt. 

## **2.7 XSD der Ident-Karten** 

Alle vom DMDA erstellten Ident-Karten müssen den Definitionen in der XSD entsprechen: 

```
<?xml version="1.0" encoding="UTF-8"?>
```

```
<xs:schema targetNamespace="http://www.de-mail.de/xml/2010/01/ident"
```

```
elementFormDefault="qualified" xmlns:xs="http://www.w3.org/2001/XMLSchema"
```

```
xmlns:de-mail="http://www.de-mail.de/xml/2010/01/ident"
xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
```

```
xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
```

```
<xs:simpleType name="Char2SimpleType">
```

```
<xs:restriction base="xs:string">
```

```
<xs:maxLength value="2"></xs:maxLength>
```

```
</xs:restriction>
```

Bundesamt für Sicherheit in der Informationstechnik 

10 

Datenstrukturen 2 

```
</xs:simpleType>
```

- `<xs:simpleType name="Char10SimpleType">` 

   - `<xs:restriction base="xs:string">` 

```
<xs:maxLength value="10"></xs:maxLength>
```

```
</xs:restriction>
```

```
</xs:simpleType>
```

```
<xs:simpleType name="Char40SimpleType">
```

```
<xs:restriction base="xs:string">
```

```
<xs:maxLength value="40"></xs:maxLength>
```

```
</xs:restriction>
```

```
</xs:simpleType>
```

```
<xs:simpleType name="Char60SimpleType">
```

```
<xs:restriction base="xs:string">
```

```
<xs:maxLength value="60"></xs:maxLength>
```

```
</xs:restriction>
```

```
</xs:simpleType>
```

```
<xs:simpleType name="Char80SimpleType">
```

```
<xs:restriction base="xs:string">
```

```
<xs:maxLength value="80"></xs:maxLength>
```

```
</xs:restriction>
```

```
</xs:simpleType>
```

```
<xs:simpleType name="Char100SimpleType">
```

```
<xs:restriction base="xs:string">
```

```
<xs:maxLength value="100"></xs:maxLength>
```

```
</xs:restriction>
```

```
</xs:simpleType>
```

```
<xs:simpleType name="Char120SimpleType">
```

```
<xs:restriction base="xs:string">
```

```
<xs:maxLength value="120"></xs:maxLength>
```

```
</xs:restriction>
```

```
</xs:simpleType>
```

```
<xs:simpleType name="Char255SimpleType">
```

```
<xs:restriction base="xs:string">
```

```
<xs:maxLength value="255"></xs:maxLength>
```

```
</xs:restriction>
```

```
</xs:simpleType>
```

```
<xs:simpleType name="BooleanSimpleType">
```

```
<xs:restriction base="xs:boolean">
```

Bundesamt für Sicherheit in der Informationstechnik 

11 

## 2 Datenstrukturen 

```
</xs:restriction>
```

```
</xs:simpleType>
```

```
<xs:complexType name="Char2Type">
```

```
<xs:simpleContent>
```

```
<xs:extension base="de-mail:Char2SimpleType">
```

```
<xs:attribute name="validationTime" type="xs:dateTime"
```

```
use="required">
```

```
</xs:attribute>
```

```
</xs:extension>
```

```
</xs:simpleContent>
```

```
</xs:complexType>
```

```
<xs:complexType name="Char10Type">
```

```
<xs:simpleContent>
```

```
<xs:extension base="de-mail:Char10SimpleType">
```

```
<xs:attribute name="validationTime" type="xs:dateTime"
```

```
use="required">
```

```
</xs:attribute>
```

```
</xs:extension>
```

```
</xs:simpleContent>
```

```
</xs:complexType>
```

```
<xs:complexType name="Char40Type">
```

```
<xs:simpleContent>
```

```
<xs:extension base="de-mail:Char40SimpleType">
```

```
<xs:attribute name="validationTime" type="xs:dateTime"
```

```
use="required">
```

```
</xs:attribute>
```

```
</xs:extension>
```

```
</xs:simpleContent>
```

```
</xs:complexType>
```

```
<xs:complexType name="Char60Type">
```

```
<xs:simpleContent>
```

```
<xs:extension base="de-mail:Char60SimpleType">
```

```
<xs:attribute name="validationTime" type="xs:dateTime"
```

```
use="required">
```

```
</xs:attribute>
```

```
</xs:extension>
```

```
</xs:simpleContent>
```

```
</xs:complexType>
```

Bundesamt für Sicherheit in der Informationstechnik 

12 

Datenstrukturen 2 

```
<xs:complexType name="Char80Type">
```

```
<xs:simpleContent>
```

```
<xs:extension base="de-mail:Char80SimpleType">
```

```
<xs:attribute name="validationTime" type="xs:dateTime"
```

```
use="required">
```

```
</xs:attribute>
```

```
</xs:extension>
```

```
</xs:simpleContent>
```

```
</xs:complexType>
```

```
<xs:complexType name="Char100Type">
```

```
<xs:simpleContent>
```

```
<xs:extension base="de-mail:Char100SimpleType">
```

```
<xs:attribute name="validationTime" type="xs:dateTime"
```

```
use="required">
```

```
</xs:attribute>
```

```
</xs:extension>
```

```
</xs:simpleContent>
```

```
</xs:complexType>
```

```
<xs:complexType name="Char120Type">
```

```
<xs:simpleContent>
```

```
<xs:extension base="de-mail:Char120SimpleType">
```

```
<xs:attribute name="validationTime" type="xs:dateTime"
```

```
use="required">
```

```
</xs:attribute>
```

```
</xs:extension>
```

```
</xs:simpleContent>
```

```
</xs:complexType>
```

```
<xs:complexType name="Char255Type">
```

```
<xs:simpleContent>
```

```
<xs:extension base="de-mail:Char255SimpleType">
```

```
<xs:attribute name="validationTime" type="xs:dateTime"
```

```
use="required">
```

```
</xs:attribute>
```

```
</xs:extension>
```

```
</xs:simpleContent>
```

```
</xs:complexType>
```

```
<xs:complexType name="BooleanType">
```

```
<xs:simpleContent>
```

```
<xs:extension base="de-mail:BooleanSimpleType">
```

Bundesamt für Sicherheit in der Informationstechnik 

13 

2 Datenstrukturen 

```
<xs:attribute name="validationTime" type="xs:dateTime"
use="required">
```

```
</xs:attribute>
```

```
</xs:extension>
```

```
</xs:simpleContent>
```

```
</xs:complexType>
```

```
<xs:complexType name="Identcard">
```

```
<xs:choice>
```

```
<xs:element name="LegalPerson" maxOccurs="1" minOccurs="0">
```

```
<xs:annotation>
```

```
<xs:documentation>Identitaetskarte einer Institution
```

```
</xs:documentation>
```

```
</xs:annotation>
```

```
<xs:complexType>
```

```
<xs:sequence>
```

```
<xs:element name="commonName" type="de-mail:Char60Type"
minOccurs="1" maxOccurs="1">
```

```
</xs:element>
```

```
<xs:element name="street" type="de-mail:Char100Type"
minOccurs="0" maxOccurs="1">
```

```
</xs:element>
```

```
<xs:element name="postOfficeBox" type="de-mail:Char10Type"
minOccurs="0" maxOccurs="1">
```

```
</xs:element>
```

```
<xs:element name="locality" type="de-mail:Char100Type"
minOccurs="1" maxOccurs="1">
```

```
</xs:element>
```

```
<xs:element name="country" type="de-mail:Char2Type"
minOccurs="1" maxOccurs="1">
```

```
</xs:element>
```

```
<xs:element name="legalForm" type="de-mail:Char60Type"
minOccurs="1" maxOccurs="1">
```

```
</xs:element>
```

```
<xs:element name="authorisedRepresentative" type="de-
```

```
mail:Char255Type"
```

```
minOccurs="1" maxOccurs="unbounded">
```

```
</xs:element>
```

```
<xs:element name="commercialRegisterType" type="de-
```

```
mail:Char255Type"
```

Bundesamt für Sicherheit in der Informationstechnik 

14 

Datenstrukturen 2 

```
minOccurs="0" maxOccurs="1">
```

```
</xs:element>
```

```
<xs:element name="commercialRegisterEntry" type="de-
mail:Char255Type"
```

```
minOccurs="0" maxOccurs="1">
```

```
</xs:element>
```

```
<xs:element name="commercialRegisterLocality" type="de-
mail:Char255Type"
```

```
minOccurs="0" maxOccurs="1">
```

```
</xs:element>
```

```
<xs:element name="de-mail-address" type="de-
mail:Char255Type"
```

```
minOccurs="1" maxOccurs="1">
```

```
</xs:element>
```

```
</xs:sequence>
```

```
</xs:complexType>
```

```
</xs:element>
```

```
<xs:element name="NaturalPerson" maxOccurs="1" minOccurs="0">
```

```
<xs:annotation>
```

```
<xs:documentation>Identitaetskarte einer natuerlichen
```

```
Person</xs:documentation>
```

```
</xs:annotation>
```

```
<xs:complexType>
```

```
<xs:sequence>
```

```
<xs:element name="personalTitle" type="de-mail:Char40Type"
minOccurs="0" maxOccurs="1">
```

```
</xs:element>
```

```
<xs:element name="surname" type="de-mail:Char120Type"
minOccurs="1" maxOccurs="1">
```

```
</xs:element>
```

```
<xs:element name="givenname" type="de-mail:Char80Type"
minOccurs="1" maxOccurs="1">
```

```
</xs:element>
```

```
<xs:element name="pseudonym" type="de-mail:Char60Type"
minOccurs="0" maxOccurs="1">
```

```
</xs:element>
```

```
<xs:element name="street" type="de-mail:Char100Type"
minOccurs="1" maxOccurs="1">
```

```
</xs:element>
```

Bundesamt für Sicherheit in der Informationstechnik 

15 

2 Datenstrukturen 

```
<xs:element name="locationOfBirth" type="de-
```

```
mail:Char100Type"
```

```
minOccurs="1" maxOccurs="1">
```

```
</xs:element>
```

```
<xs:element name="dateOfBirth" type="de-mail:Char10Type"
minOccurs="1" maxOccurs="1">
```

```
</xs:element>
```

```
<xs:element name="locality" type="de-mail:Char100Type"
minOccurs="1" maxOccurs="1">
```

```
</xs:element>
```

```
<xs:element name="country" type="de-mail:Char2Type"
minOccurs="1" maxOccurs="1">
```

```
</xs:element>
```

```
<xs:element name="age" type="de-mail:Char10Type"
minOccurs="1" maxOccurs="1">
```

```
</xs:element>
```

```
<xs:element name="de-mail-address" type="de-
mail:Char255Type"
```

```
minOccurs="1" maxOccurs="1">
```

```
</xs:element>
```

```
</xs:sequence>
```

```
</xs:complexType>
```

```
</xs:element>
```

```
<xs:element name="Address" maxOccurs="1" minOccurs="0">
```

```
<xs:annotation>
```

```
<xs:documentation>Adresskarte einer natuerlichen
```

```
Person</xs:documentation>
```

```
</xs:annotation>
```

```
<xs:complexType>
```

```
<xs:sequence>
```

```
<xs:element name="personalTitle" type="de-mail:Char40Type"
```

```
minOccurs="0" maxOccurs="1">
```

```
</xs:element>
```

```
<xs:element name="surname" type="de-mail:Char120Type"
```

```
minOccurs="1" maxOccurs="1">
```

```
</xs:element>
```

```
<xs:element name="givenname" type="de-mail:Char80Type"
minOccurs="1" maxOccurs="1">
```

```
</xs:element>
```

Bundesamt für Sicherheit in der Informationstechnik 

16 

Datenstrukturen 2 

```
<xs:element name="pseudonym" type="de-mail:Char60Type"
minOccurs="0" maxOccurs="1">
```

```
</xs:element>
```

```
<xs:element name="street" type="de-mail:Char100Type"
minOccurs="1" maxOccurs="1">
```

```
</xs:element>
```

```
<xs:element name="locality" type="de-mail:Char100Type"
minOccurs="1" maxOccurs="1">
```

```
</xs:element>
```

```
<xs:element name="country" type="de-mail:Char2Type"
minOccurs="1" maxOccurs="1">
```

```
</xs:element>
```

```
<xs:element name="de-mail-address" type="de-
mail:Char255Type"
```

```
minOccurs="1" maxOccurs="1">
```

```
</xs:element>
```

```
</xs:sequence>
```

```
</xs:complexType>
```

```
</xs:element>
```

```
<xs:element name="Age" maxOccurs="1" minOccurs="0">
```

```
<xs:annotation>
```

```
<xs:documentation>Alterskarte</xs:documentation>
```

```
</xs:annotation>
```

```
<xs:complexType>
```

```
<xs:sequence>
```

```
<xs:element name="age" type="de-mail:Char10Type"
minOccurs="1" maxOccurs="1">
```

```
</xs:element>
```

```
<xs:element name="de-mail-address" type="de-
```

```
mail:Char255Type"
```

```
minOccurs="1" maxOccurs="1">
```

```
</xs:element>
```

```
</xs:sequence>
```

```
</xs:complexType>
```

```
</xs:element>
```

```
<xs:element name="AgeOver16" maxOccurs="1" minOccurs="0">
```

```
<xs:annotation>
```

```
<xs:documentation>Alterskarte</xs:documentation>
```

```
</xs:annotation>
```

Bundesamt für Sicherheit in der Informationstechnik 

17 

2 Datenstrukturen 

```
<xs:complexType>
```

```
<xs:sequence>
```

```
<xs:element name="over16" type="de-mail:BooleanType"
```

```
minOccurs="1"
```

```
maxOccurs="1">
```

```
</xs:element>
<xs:element name="de-mail-address" type="de-
mail:Char255Type"
```

```
minOccurs="1" maxOccurs="1">
```

```
</xs:element>
```

```
</xs:sequence>
</xs:complexType>
</xs:element>
```

```
<xs:element name="AgeOver18" maxOccurs="1" minOccurs="0">
<xs:annotation>
```

```
<xs:documentation>Alterskarte</xs:documentation>
```

```
</xs:annotation>
```

```
<xs:complexType>
<xs:sequence>
```

```
<xs:element name="over18" type="de-mail:BooleanType"
```

```
minOccurs="1"
```

```
maxOccurs="1">
```

```
</xs:element>
```

```
<xs:element name="de-mail-address" type="de-
```

```
mail:Char255Type"
```

```
minOccurs="1" maxOccurs="1">
```

```
</xs:element>
```

```
</xs:sequence>
```

```
</xs:complexType>
```

```
</xs:element>
```

```
<xs:element name="DeMailAddress" maxOccurs="1" minOccurs="0">
```

```
<xs:annotation>
```

```
<xs:documentation>Adresskarte</xs:documentation>
```

```
</xs:annotation>
```

```
<xs:complexType>
```

```
<xs:sequence>
```

```
<xs:element name="de-mail-address" type="de-
```

```
mail:Char255Type"
```

```
minOccurs="1" maxOccurs="1">
```

```
</xs:element>
```

Bundesamt für Sicherheit in der Informationstechnik 

18 

Datenstrukturen 2 

```
</xs:sequence>
```

```
</xs:complexType>
```

```
</xs:element>
```

```
</xs:choice>
```

```
</xs:complexType>
```

```
</xs:schema>
```

Bundesamt für Sicherheit in der Informationstechnik 

19 


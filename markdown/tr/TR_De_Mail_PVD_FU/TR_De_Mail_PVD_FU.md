
![](markdown/tr/TR_De_Mail_PVD_FU/TR_De_Mail_PVD_FU.pdf-0001-00.png)



![](markdown/tr/TR_De_Mail_PVD_FU/TR_De_Mail_PVD_FU.pdf-0001-01.png)


## BSI – Technische Richtlinie 

Bezeichnung: Postfach- und Versanddienst Funktionalitätsspezifikation Anwendungsbereich: De-Mail Kürzel: BSI TR 01201 Teil 3.1 Version: 1.8 

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn Tel.: +49 22899 9582-0 E-Mail: de-mail@bsi.bund.de Internet: https://www.bsi.bund.de © Bundesamt für Sicherheit in der Informationstechnik 2024 

## **Inhaltsverzeichnis** 

|1|Einleitung....................................................................................................................................5|
|---|---|
|2|Gesamtüberblick.........................................................................................................................6|
|3|Funktionale Anforderungen........................................................................................................8|
|3.1|Postfachdienst und Postfach................................................................................................................8|
|3.2|Versanddienst....................................................................................................................................12|
|3.3|Versandoptionen................................................................................................................................13|
|4|Besondere nicht-funktionale Anforderungen............................................................................16|
|4.1|Speicherplatz......................................................................................................................................16|
|4.2|Transportzeiten..................................................................................................................................16|
|4.3|System-Adressen...............................................................................................................................16|
|5|Datenstrukturen.........................................................................................................................17|
|5.1|Nachrichten........................................................................................................................................17|
|5.2|Bestätigungen und Bestätigungsnachrichten.....................................................................................21|
|5.3|Meldungen und Meldungsnachrichten..............................................................................................21|
|6|Funktionale Beschreibung.........................................................................................................23|
|6.1|Erstellen von Nachrichten durch den Absender................................................................................23|
|6.2|Entgegennahme von Nachrichten durch Postfachdienst des Absenders...........................................28|
|6.3|Transport von Nachrichten durch Versanddienst des Absenders......................................................37|
|6.4|Transport von Nachrichten durch Versanddienst des Empfängers....................................................40|
|6.5|Empfangen der Nachrichten durch Postfachdienst des Empfängers.................................................44|
|6.6|Abrufen der Nachrichten durch Empfänger......................................................................................57|
|6.7|Empfang und Lesen der Nachricht durch Empfänger.......................................................................61|
|7|Weitere Funktionen...................................................................................................................64|
|7.1|Durch das System ausgeführte Funktionen.......................................................................................64|
|7.2|Durch den Nutzer initiierte Funktionen.............................................................................................65|
|8|Obligatorische und optionale Funktionalität.............................................................................76|



## **Abbildungsverzeichnis** 

Abbildung 1: Architekturüberblick über den PVD..............................................................................6 Abbildung 2: Transport von Nachrichten innerhalb von De-Mail.....................................................13 

## **Tabellenverzeichnis** 

Tabelle 1: Liste der in dem PVD verwendeten System-Adressen......................................................16 Tabelle 2: Metadaten einer Nachricht................................................................................................21 Tabelle 3: Schritte zum Erstellen von Nachrichten............................................................................28 Tabelle 4: Schritte zum Versenden von Nachrichten.........................................................................37 Tabelle 5: Schritte zum Transport von Nachrichten durch Versanddienst des Absenders................40 Tabelle 6: Schritte zum Transport von Nachrichten durch Versanddienst des Empfängers..............43 Tabelle 7: Schritte zum Empfangen der Nachrichten.........................................................................56 

Bundesamt für Sicherheit in der Informationstechnik 

3 

Tabelle 8: Schritte zum Abrufen und Lesen der Nachrichten............................................................61 Tabelle 9: Durch das System ausgeführte Funktionen.......................................................................65 Tabelle 10: Durch den Nutzer initiierte Funktionen...........................................................................75 Tabelle 11: Obligatorische und optionale Funktionalität...................................................................76 

Bundesamt für Sicherheit in der Informationstechnik 

4 

1 Einleitung 

## **1 Einleitung** 

Dieses Modul beinhaltet die funktionalen Spezifikationen des Postfach- und Versanddienstes und ist Bestandteil von [TR DM PVD M]. 

In diesem Modul werden die zwingenden Anforderungen an den PVD von De-Mail technikneutral beschrieben. Eine Spezifikation von Protokollen und zugehörigen Parametern erfolgt nur dort, wo dies aus funktionaler Sicht explizit erforderlich ist. 

Bundesamt für Sicherheit in der Informationstechnik 

5 

2 Gesamtüberblick 

## **2 Gesamtüberblick** 

Der Postfachdienst von De-Mail ermöglicht dem Nutzer als elektronischer Briefkasten, elektronische Nachrichten sowohl zu versenden als auch zu empfangen. Der Versanddienst ist für das verbindliche Versenden der Nachrichten verantwortlich. Beide Dienste sind eng miteinander verknüpft. Einerseits kann ein Nutzer ohne Postfachdienst keine an ihn adressierten Nachrichten empfangen, und andererseits wird der Versanddienst benötigt, um Nachrichten von einem Nutzer an einen anderen zu versenden. Die Abbildung 1 gibt einen Überblick über die Architektur des PVD. Die Bestandteile der Architektur und deren Zusammenwirken werden in den nachfolgenden Abschnitten beschrieben. 


![](markdown/tr/TR_De_Mail_PVD_FU/TR_De_Mail_PVD_FU.pdf-0006-03.png)


_Abbildung 1: Architekturüberblick über den PVD_ 

Absender und Empfänger von Nachrichten greifen über einen lokalen Web- oder NachrichtenClient auf ihren Postfachdienst zu. 

Der Postfachdienst erlaubt dem Nutzer, elektronische Nachrichten sowohl zu versenden als auch zu empfangen (siehe Abschnitt 3.1). Er sichert vor dem Versand von Nachrichten deren Integrität und schützt die Nachrichten durch Verschlüsselung vor dem Einblick unberechtigter Dritter. Beim Empfang entschlüsselt der Dienst die Nachrichten und prüft deren Integrität vor Abruf durch den Empfänger. 

Empfangene und versendete Nachrichten werden im Postfach des Nutzers gespeichert und können dort von diesem verwaltet werden. Mit dem Postfach werden die De-Mail-Adressen des De-MailKontos des Nutzers verbunden (primäre und pseudonyme Adressen, vgl. [TR DM ACM FU]). Unter dieser Adresse ist er einerseits als Empfänger erreichbar, andererseits kann er Nachrichten darunter als Absender versenden. 

Zugriff erhält ein Nutzer auf sein Postfach über den Postfachdienst, wenn er sich an seinem DeMail-Konto erfolgreich angemeldet hat (s. a. [TR DM ACM FU]). Das Authentisierungsniveau, mit dem der Nutzer sich am De-Mail-Konto anmeldet, wird sowohl beim Versand einer Nachricht als auch beim Lesen von empfangenen Nachrichten berücksichtigt. 

Möchte der Absender die Nachricht zusätzlich elektronisch signieren und/oder Ende-zu-Endeverschlüsseln, so kann er dies mit einer lokalen Signaturanwendungskomponente (SAK) bzw. mit 

Bundesamt für Sicherheit in der Informationstechnik 

6 

2 Gesamtüberblick 

einer lokalen Verschlüsselungskomponente durchführen. Diese Komponenten können auch in dem lokalen Web- oder Nachrichten-Client, mit dem er die Nachrichten erstellt, integriert sein und können auch unabhängig von De-Mail genutzt werden. Auf diese Weise signierte und/oder verschlüsselte Nachrichten kann der Empfänger ebenfalls mit lokalen Komponenten entschlüsseln und vorhandene Signaturen prüfen. Der DMDA gewährleistet die transparente Weiterleitung von bereits auf Nutzerseite verschlüsselten und/oder signierten Nachrichten. 

Für das zuverlässige Versenden von elektronischen Nachrichten steht dem Nutzer der Versanddienst zur Verfügung (siehe Abschnitt 3.2). Dieser ermöglicht es, Nachrichten zu versenden und vom DMDA entsprechende Bestätigungen darüber zu erlangen, ob die Nachrichten versendet oder im Postfach des Empfängers eingegangen sind. 

Nachrichten, die innerhalb des De-Mail-Verbundes versendet oder empfangen werden, werden obligatorisch auf Schadsoftware geprüft. Für qualifiziert signierte Nachrichtenanhänge kann der DMDA des Empfängers optional eine Signaturprüfung durchführen. 

Bundesamt für Sicherheit in der Informationstechnik 

7 

3 Funktionale Anforderungen 

## **3 Funktionale Anforderungen** 

Die funktionalen Anforderungen an den PVD von De-Mail werden in diesem Abschnitt beschrieben. 

## **3.1 Postfachdienst und Postfach** 

Jeder Nutzer von De-Mail besitzt mindestens ein Postfach. Auf dieses erhält er über den Postfachdienst Zugriff, wenn er sich an seinem De-Mail-Konto erfolgreich angemeldet hat (vgl. [TR DM ACM FU]). Das Authentisierungsniveau, mit dem der Nutzer sich am De-Mail-Konto angemeldet hat, wird sowohl beim Versand einer Nachricht als auch beim Abruf von Nachrichten (siehe Abschnitt 3.1.2.3) berücksichtigt. 

In dem Postfach werden vom Nutzer versendete und an ihn übermittelte Nachrichten abgelegt. Zusätzlich können in dem Postfach z. B. Entwürfe von Nachrichten gespeichert werden. 

Nachrichten werden an den Versanddienst für den zuverlässigen Transport an den oder die Empfänger übergeben und, wenn gefordert, Bestätigungen für den Versand, Eingang oder Abholung ausgestellt. 

## **3.1.1 Erstellen und Versenden von Nachrichten** 

Bei der Erstellung der Nachrichten kann der Nutzer mindestens auswählen 

- Versandoptionen (vgl. Abschnitt 3.3) 

- Absenderadresse 

   - Der Nutzer hat die Auswahl zwischen der primären und einer ggf. gewählten pseudonymen De-Mail-Adresse, die dem De-Mail-Konto zugeordnet ist. Andere Adressen können nicht genutzt werden. 

- Empfängeradresse 

   - Die Adressen können aus dem persönlichen Adressbuch, dem ÖVD oder manuell eingegeben werden. Es werden die Adressierungsarten „To:“ (Primärer Adressat), „CC:“ ( _Carbon Copy_ , Kopie) und „BCC:“ ( _Blind Carbon Copy_ , Blindkopie) unterstützt. 

- Nachrichtentext 

- Anhänge 

   - Die Anhänge können von dem lokalen Dateisystem des Nutzers oder aus der DA (optional) ausgewählt werden. 

Des Weiteren kann die Nachricht optional durch den Nutzer mit einer (qualifizierten) Signatur versehen oder zusätzlich Ende-zu-Ende-verschlüsselt werden. Dies hat der DMDA in geeigneter Weise zu ermöglichen. 

## **3.1.1.1 Übergabe einer Nachricht an den Postfachdienst zum Versand** 

Die erstellte Nachricht wird vom lokalen Web- oder Nachrichten-Client mitsamt den ausgewählten Versandoptionen an den Postfachdienst des DMDA des Absenders übergeben. 

Bundesamt für Sicherheit in der Informationstechnik 

8 

3 Funktionale Anforderungen 

Hat der Absender sich mit dem Authentisierungsniveau „normal“ am Postfachdienst angemeldet, so darf dieser pro Tag höchstens 100 Nachrichten versenden, wobei insgesamt (d.h. für alle 100 Nachrichten zusammen) höchstens 300 Empfänger adressiert werden dürfen. Dies soll verhindern, dass über eine kompromittierte De-Mail-Adresse Massensendungen verteilt werden. 

Nach Entgegennahme der Nachricht durch den Postfachdienst prüft dieser die Nachricht auf Schadsoftware (vgl. Abschnitt 3.1.3.1), sofern die Nachricht nicht Ende-zu-Ende verschlüsselt ist. Wenn keine Schadsoftware gefunden worden ist, werden notwendige Metadaten der Nachricht, wie z. B. die korrekte Absender-Adresse oder die aktuelle Zeit, kontrolliert und ggf. ergänzt. Falls Schadsoftware gefunden worden ist, wird der Nutzer über das weitere Vorgehen informiert. 

Der Postfachdienst versieht die Nachricht unter Einbeziehung der Metadaten mit einer Integritätssicherung. Die Nachricht wird über einen sicheren Kommunikationskanal an den Versanddienst übertragen und verschlüsselt im Postfach abgelegt (s. a. Abschnitt 3.2.2). Falls vom Absender eine Versandbestätigung angefordert wurde, wird ihm diese von seinem Versanddienst ausgestellt und in Form einer Nachricht in sein Postfach abgelegt. 

## **3.1.2 Empfang und Abruf von Nachrichten** 

## **3.1.2.1 Ablage von Nachrichten im Postfach des Empfängers** 

Der Postfachdienst des Empfängers nimmt von seinem Versanddienst die übermittelten Nachrichten entgegen, legt diese im Postfach des Empfängers ab und erstellt eine Eingangsbestätigung, falls dies der Absender der Nachricht angefordert hat. Diese wird in einer separaten Nachricht an den Absender übermittelt. Der Empfänger der ursprünglichen Nachricht erhält eine Kopie der Eingangsbestätigung. 

## **3.1.2.2 Darstellung der Nachrichten im Postfach** 

Im Postfach des Nutzers gespeicherte Nachrichten werden durch den Postfachdienst zu einer Liste zusammengefasst und entsprechend im lokalen Web- oder Nachrichten-Client dargestellt. Neu empfangene und noch nicht gelesene Nachrichten werden besonders gekennzeichnet. Weiterhin werden verschiedene Merkmale der Nachricht kenntlich gemacht. Der Nutzer hat die Möglichkeit, die Nachrichten nach diesen Merkmalen zu sortieren oder anzeigen zu lassen. 

Nach folgenden Merkmalen muss in der Übersicht der eingegangenen Nachrichten mindestens differenziert werden können: 

- Betreff der Nachricht, 

- Absendezeitpunkt der Nachricht, 

- Name des Absenders bzw. seine Adresse, 

- Vorhandensein von Nachrichtenanhängen, 

- Hinweis, ob vom Absender die Versandoptionen „Persönlich“ und/oder „Absenderbestätigt“ gewählt worden sind. 

Folgende Informationen können optional in der Übersichtsansicht, müssen obligatorisch jedenfalls in der Einzelansicht einer Nachricht ersichtlich sein: 

- Name des Empfängers bzw. seine Adresse, 

- Authentisierungsniveau des Absenders, 

Bundesamt für Sicherheit in der Informationstechnik 

9 

## 3 Funktionale Anforderungen 

- Vorhandensein einer Verschlüsselung, 

- Vorhandensein von Signaturen (ggf. inkl. Prüfergebnisse), 

- Hinweis, ob vom Absender eine Versand-, Eingangs- und/oder Abholbestätigung angefordert worden ist. 

## **3.1.2.3 Abruf der Nachrichten** 

Der Postfachdienst muss sicherstellen, dass der Nutzer mit Authentisierungsniveau „normal“ nicht auf Nachrichten zugreifen kann, falls für die Nachricht die Versandoption „persönlich“ oder die Versandoption „Abholbestätigung“ gewählt wurde. 

Sofern ein ausreichendes Authentisierungsniveau gegeben ist, entschlüsselt der Postfachdienst die Nachricht und überträgt diese an den Nutzer. 

## **3.1.2.4 Entschlüsselung der Nachrichten und Überprüfung von Signaturen** 

Bei Ende-zu-Ende verschlüsselten Nachrichten oder Nachrichtenanhängen kann eine lokale Entschlüsselungskomponente dem Nutzer ermöglichen, diese auf seinem System zu entschlüsseln. Unabhängig von einer Signaturprüfung (s. a. Abschnitt 3.2.2) durch den DMDA, die optional durchgeführt werden kann, kann der Empfänger auch eine eigene, auf seinem lokalen System installierte Verifikationskomponente zur Prüfung der Signaturen nutzen. 

Der DMDA hat den Einsatz derartiger Komponenten in geeigneter Weise zu unterstützen. 

## **3.1.3 Weitere Funktionen des Postfachdienstes und des Postfaches** 

Neben Erstellung, Versand und Empfang von Nachrichten unterstützt der Postfachdienst von DeMail in diesem Zusammenhang relevante Funktionen, die in den nachfolgenden Abschnitten aufgeführt werden. 

## **3.1.3.1 Prüfung auf Schadsoftware** 

Der Postfachdienst überprüft Nachrichten vom Absender, die er an diesen für den Versand übergeben hat, auf Schadsoftware. Nachrichten, in denen Schadsoftware festgestellt wurde, dürfen nicht weiterversendet werden, der Absender ist entsprechend zu informieren und die Nachricht in einen dafür vorgesehenen Ordner zu verschieben oder zu löschen. 

Nachrichten, die der Postfachdienst des Empfängers entgegen nimmt, werden ebenfalls auf Schadsoftware geprüft. Nachrichten, in denen Schadsoftware festgestellt wurde, dürfen dem Empfänger nicht übermittelt werden. Sowohl der Absender als auch der Empfänger der Nachricht erhalten eine entsprechende Information. 

Wurde vom DMDA des Empfängers keine Schadsoftware gefunden, wird die Nachricht zugestellt. Beim Abruf der Nachricht darf der Nutzer diese erneut auf Schadsoftware untersuchen lassen. Wird nun eine solche gefunden, darf der Nutzer erst nach einem expliziten Warnhinweis auf diese Nachricht zugreifen, die sich dann in einem dafür vorgesehenen Ordner befinden muss. 

## **3.1.3.2 Automatisierte Weiterleitung an eine andere De-Mail-Adresse** 

Der Nutzer muss die Möglichkeit haben an sein De-Mail-Konto gesendete Nachrichten automatisch an eine andere De-Mail-Adresse weiterleiten zu lassen. Bei der automatisierten Weiterleitung wird 

Bundesamt für Sicherheit in der Informationstechnik 

10 

3 Funktionale Anforderungen 

die Nachricht im Postfach des Nutzers abgelegt, bevor eine Kopie an die Weiterleitungs-Adresse gesendet wird. Die Weiterleitung an eine Adresse, die keine De-Mail-Adresse ist, ist unzulässig. Eine ggf. angeforderte Eingangsbestätigung wird bei Ablage der Nachricht nur im Postfach des ursprünglichen Empfängers erzeugt. 

Für Nachrichten mit der Versandoption „persönlich“  kann der Nutzer eine Weiterleitung ausschließen. In diesem Fall erfolgt keine Weiterleitung, sondern nur eine Benachrichtigung an die Weiterleitungsadresse über den Eingang einer Nachricht (vgl §5 Absatz 11„De-Mail-G). Andernfalls wird eine Kopie der Nachricht ebenfalls mit Versandoption „persönlich“ an die Weiterleitungsadresse weitergeleitet. 

Für Nachrichten mit der Versandoption „Abholbestätigung“ erfolgt keine Weiterleitung, sondern eine Benachrichtigung an die Weiterleitungsadresse. 

## **3.1.3.3 Nachsendeauftrag an eine andere De-Mail-Adresse** 

Von der automatisierten Weiterleitung ist der Nachsendeauftrag an eine andere De-Mail-Adresse abzugrenzen. Innerhalb eines Auflösungsantrags zu seinem De-Mail-Konto (vgl. [TR DM ACM FU]) muss der DMDA dem Nutzer die Möglichkeit anbieten, einen Nachsendeauftrag an eine andere De-Mail-Adresse zu stellen. Alle empfangenen Nachrichten werden während einer festgelegten Übergangszeit an diese weitergeleitet. Bei einem Nachsendeauftrag wird keine Kopie im Postfach des Nutzers abgelegt. Eine ggf. angeforderte Eingangsbestätigung oder Abholbestätigung wird erst durch den Postfachdienst erzeugt, an den die Nachricht nachgesendet worden ist. 

## **3.1.3.4 Export von Nachrichten** 

Der Nutzer muss die Möglichkeit haben, empfangene und versendete Nachrichten und deren Anhänge auf sein lokales System zu exportieren. Der Export erfolgt durch den Postfachdienst auf Anforderung des Nutzers, inkl. des Integritätsschutzes (vgl. Abschnitt 3.2.2). 

**3.1.3.5 Zugriff auf Adressbuch und ÖVD** Über den Postfachdienst kann der Nutzer auf die Kontaktdaten zugreifen, die in dem Adressbuch seines De-Mail-Kontos hinterlegt sind. 

Zusätzlich zu dem persönlichen Adressbuch kann der Nutzer auch den ÖVD von De-Mail (siehe [TR DM IT-BInfra FU]) nutzen, in dem die freigegebenen Kontaktdaten der De-Mail-Nutzer veröffentlicht sind. 

## **3.1.3.6 Weiterleiten und Beantworten von Nachrichten** 

Der Nutzer hat die Möglichkeit, eine Nachricht an andere De-Mail-Empfänger weiterzuleiten und diese zu beantworten. Standardmäßig wird die ursprüngliche Nachricht als Anhang einer neuen Nachricht weitergeleitet, sodass die Metadaten der ursprünglichen Nachricht erhalten bleiben. Andere Weiterleitungsformate (z. B. ein „>“ vor jeder Zeile der ursprünglichen Nachricht) kann der Nutzer konfigurieren. Es ergeben sich die gleichen Anforderungen wie für eine neue Nachricht (vgl. Abschnitt 3.1.1). 

Bundesamt für Sicherheit in der Informationstechnik 

11 

## 3 Funktionale Anforderungen 

## **3.1.3.7 Ablage von Nachrichten in Kategorien** 

Nachrichten können vom Nutzer in eigene Kategorien sortiert werden. Eine Kategorie entspricht einem Ordner, in dem die Nachricht abgelegt werden kann. Die Möglichkeit einer Zuordnung zu mehreren Kategorien kann optional durch den DMDA angeboten werden. 

Es ist optional auch möglich, Nachrichten automatisch bei Empfang im Postfach entsprechenden Kategorien zuzuordnen. Eine Administration dieser Regeln erfolgt durch den Nutzer selbst. 

## **3.1.3.8 Suchfunktionen für Nachrichten** 

Der Nutzer muss eine Suchfunktion des Postfachdienstes nutzen können, um Nachrichten innerhalb seines Postfaches aufzufinden. Optional können Anhänge von Nachrichten mit Office- und PDFDokumenten durchsucht werden, sofern diese nicht Ende-zu-Ende-verschlüsselt sind. 

## **3.1.3.9 Löschen von Nachrichten** 

Nachrichten dürfen durch den Nutzer nur in einem 2-Stufen-Prozess gelöscht werden können: 

1. Stufe: Verschieben der zu löschenden Nachricht in einen Papierkorb, in dem zu löschende Dokumente abgelegt werden. 

2. Stufe: Endgültiges und unwiederbringliches Löschen von allen bzw. einzelnen Nachrichten aus dem Papierkorb. 

Nachrichten, bei denen sich der Empfänger mit Authentisierungsniveau „hoch“ anmelden muss, um auf die Nachrichten zugreifen zu können, dürfen nur gelöscht werden, wenn sich der Empfänger auf diesem Authentisierungsniveau angemeldet hat. Dies gilt auch für Abholbestätigungen, da sie mit der Versandoption „persönlich“ gekennzeichnet sind, sowie für Nachrichten, für die eine Abholbestätigung ausgestellt wurde/werden soll. Eine Nachricht, für die eine Versand- oder Eingangsbestätigung erteilt worden ist, darf durch den Empfänger mit Authentisierungsniveau „normal“ erst 90 Tage nach ihrem Eingang gelöscht werden können. 

## **3.2 Versanddienst** 

Der Versanddienst stellt zusammen mit dem Postfachdienst sicher, dass Nachrichten von einem DeMail-Nutzer zu einem anderen De-Mail-Nutzer vertraulich und verbindlich übermittelt werden. Weiterhin ermöglichen beide Dienste, Bestätigungen darüber zu erlangen, ob die Nachricht versendet wurde oder im Postfach des Empfängers eingegangen ist (siehe Abschnitte 3.2.2). 

## **3.2.1 Benachrichtigung bei falscher Adressierung oder vollständiger Sperrung** 

Bei Empfang einer Nachricht an 

- eine nicht existierende De-Mail-Adresse oder 

- an ein vollständig gesperrtes De-Mail-Konto (vgl. [TR DM ACM FU]), 

sendet der Versanddienst eine Fehlermeldung an den Absender. Es darf keine Eingangsbestätigung ausgestellt werden. 

## **3.2.2 Transport von Nachrichten innerhalb von De-Mail** 

Die Übermittlung der Nachrichten vom Postfachdienst des Absenders zum Postfachdienst des Empfängers erfolgt innerhalb von De-Mail ausschließlich über sichere Transportkanäle (vgl. [TR DM IS GS] bzw. [TR DM IS 27001]). 

Bundesamt für Sicherheit in der Informationstechnik 

12 

3 Funktionale Anforderungen 


![](markdown/tr/TR_De_Mail_PVD_FU/TR_De_Mail_PVD_FU.pdf-0013-01.png)


_Abbildung  2: Transport von Nachrichten innerhalb von De-Mail_ 

Unmittelbar nach Entgegennahme der Nachricht vom Sender überprüft der Postfachdienst die Nachricht auf Schadsoftware und die übermittelten Metadaten auf Validität. Der DMDA ergänzt weitere Metadaten wie z. B. die aktuelle Zeit und versieht die Nachricht inklusive der Metadaten mit einer Integritätssicherung. Die Metadaten sind der Nachricht eindeutig zugeordnet. Anschließend wird die Nachricht sowohl für den Postfachdienst des Empfängers als auch für den Postfachdienst des Absenders verschlüsselt. Die so gesicherte Nachricht wird vom Postfachdienst sowohl in das Postfach des Absenders als auch an den Versanddienst des Absenders übertragen. 

Der Versanddienst des Absenders übermittelt die gesicherte Nachricht anschließend an den Versanddienst des Empfängers, der prüft, ob er die Nachricht zustellen kann. Im positiven Fall leitet er die Nachricht an den Postfachdienst weiter. Nach Entgegennahme durch den Postfachdienst wird die Nachricht wiederum temporär entschlüsselt und auf Schadsoftware geprüft. Die Nachricht wird im Postfach des Empfängers verschlüsselt abgelegt. 

Ein Abruf von Nachrichten durch den Empfänger erfolgt über einen sicheren Transportkanal. Der Postfachdienst prüft hierbei, ob das aktuelle Authentisierungsniveau des Empfängers für den Zugriff auf die konkrete Nachricht ausreicht. Nachfolgend entschlüsselt der Postfachdienst die abgerufene Nachricht, kontrolliert die Integritätssicherung und übermittelt sie an den lokalen Weboder Nachrichten-Client. 

## **3.3 Versandoptionen** 

Die Einführung elektronischer Versandoptionen mit einer definierten und standardisierten Anzahl von Produktausprägungen ist eine wesentliche Aufgabe von De-Mail. 

Bei dem Versand von Nachrichten innerhalb von De-Mail sind die folgenden Merkmale von wesentlicher Bedeutung: 

- Authentizität des Empfängers einer Nachricht 

- Authentizität des Absenders einer Nachricht 

- Bestätigungen über den jeweiligen Zustand einer Nachricht 

- Integritätssicherung von Nachrichten 

Bundesamt für Sicherheit in der Informationstechnik 

13 

## 3 Funktionale Anforderungen 

Die oben aufgeführten Merkmale sind in den nachfolgend beschriebenen Versandoptionen abgebildet. 

Alle Versandoptionen müssen vom DMDA angeboten werden. Die Versandoptionen können einzeln auswählbar sein. Der DMDA kann Kombinationen der Versandoptionen anbieten. 

In der Bezeichnung muss sichergestellt sein, dass alle Versandoptionen für den Nutzer klar erkennbar sind. Der Nutzer ist bei Kombinationen darüber zu informieren, welche Versandoptionen in diesen enthalten sind. 

## **3.3.1 Persönlich** 

Hiermit kann der Absender zum Ausdruck bringen, dass er besonderen Wert auf den sicheren Zugang seiner Nachricht beim Empfänger selbst legt. Hier muss das erforderliche Authentisierungsniveau des Empfängers „hoch“ sein, um die Nachricht lesen zu können. Um diese Option wählen zu können, muss das Authentisierungsniveau des Absenders ebenfalls „hoch“ sein. Verfügt der Empfänger nicht über das Authentisierungsniveau "hoch", wird die Nachricht von seinem Postfachdienst mit einer Fehlermeldung an den Absender zurückgeschickt. 

## **3.3.2 Absenderbestätigt** 

Hiermit kann der Absender gegenüber dem Empfänger zum Ausdruck bringen, dass er sich zum Absenden der Nachricht sicher angemeldet hat. Um diese Option wählen zu können, muss das Authentisierungsniveau des Absenders „hoch“ sein. Der DMDA des Absenders versieht die Nachricht und die Metadaten mit einer qualifizierten Signatur. 

Die Versandoption darf nicht von natürlichen Personen in Kombination mit einer PseudonymAdresse verwendet werden können. 

## **3.3.3 Versandbestätigung** 

Hiermit erhält der Absender einen Nachweis über den ordnungsgemäßen Versand seiner Nachricht. Die Versandbestätigung wird vom Versanddienst des Absenders erzeugt und diesem per Nachricht übermittelt. 

## **3.3.4 Eingangsbestätigung** 

Hiermit erhalten Absender und Empfänger einen Nachweis darüber, wann der DMDA des Empfängers die Nachricht im Postfach des Empfängers abgelegt hat. Die Eingangsbestätigung wird vom Postfachdienst des Empfängers erzeugt und dem Absender sowie dem Empfänger der ursprünglichen Nachricht per Nachricht übermittelt. 

## **3.3.5 Abholbestätigung** 

Hiermit erhalten Absender und Empfänger einen Nachweis darüber, wann der DMDA die Nachricht im Postfach des Empfängers abgelegt hat und dass sich der Empfänger nach dem Eingang der Nachricht an seinem De-Mail-Konto mit Authentisierungsniveau „hoch“ angemeldet hat. Die Abholbestätigung wird vom Postfachdienst des Empfängers erzeugt, wenn sich der Empfänger das erste Mal nach dem Ablegen der Nachricht in seinem Postfach mit Authentisierungsniveau „hoch“ anmeldet. Es ist die Nachrichtenoption „persönlich“ zu setzen. 

Die Abholbestätigung wird dem Absender sowie dem Empfänger der ursprünglichen Nachricht per Nachricht übermittelt. 

Diese Option steht beim Versand nur berechtigten öffentlichen Stellen zur Verfügung. Für den Versand muss der Versender mit dem Authentisierungsniveau „hoch“ angemeldet sein. 

Bundesamt für Sicherheit in der Informationstechnik 

14 

3 Funktionale Anforderungen 

Verfügt der Empfänger nicht über die Möglichkeit sich mit dem Authentisierungsniveau „hoch“ anzumelden, wird eine entsprechende Meldungsnachricht erzeugt. 

Bundesamt für Sicherheit in der Informationstechnik 

15 

4 Besondere nicht-funktionale Anforderungen 

## **4 Besondere nicht-funktionale Anforderungen** 

## **4.1 Speicherplatz** 

Jeder Nutzer eines De-Mail-Kontos hat einen Mindest-Speicherplatz (vgl. [TR DM]) zur Verfügung. Die Größenbegrenzung einer Nachricht darf in der Inter-DMDA-Kommunikation nicht unter 45 MiB (brutto) liegen. Dem Nutzer werden damit Nachrichten mit einer Maximalgröße von 20 MiB (netto) ermöglicht. 

Der Nutzer muss gewarnt werden, sobald der freie Speicherplatz seines Postfaches nur noch über weniger als 10% des maximalen Speicherplatzes verfügt. 

Wenn der Speicherplatz belegt ist, kann der DMDA den Versand weiterer Nachrichten unterbinden. Der Empfang von Nachrichten muss weiterhin möglich sein. 

## **4.2 Transportzeiten** 

Nachrichten, die über den PVD versendet werden, müssen spätestens acht Stunden nach Absendung beim DMDA des Empfängers im Postfach liegen und durch den Empfänger abgerufen werden können. Erfolgt der Versand von Nachrichten an einen Empfänger eines anderen DMDAs, muss der DMDA des Absenders die Nachricht spätestens nach 4 Stunden dem DMDA des Empfängers übermittelt haben. 

## **4.3 System-Adressen** 

In der nachfolgenden Tabelle werden die System-Adressen (siehe [TR DM ACM FU]) aufgelistet, die innerhalb des PVD verwendet werden müssen. 

|**_Verwendungszweck_**|**_De-Mail-Adresse_**|
|---|---|
|Versandbestätigung|Versandbestaetigung@<DMDA>|
|Eingangsbestätigung|Eingangsbestaetigung@<DMDA>|
|Abholbestätigung|Abholbestaetigung@<DMDA>|
|Warnungvor Schadsoftware|Schadsoftware-Warnung@<DMDA>|
|Meldung|Meldung@<DMDA>|



_Tabelle 1: Liste der in dem PVD verwendeten System-Adressen_ 

Weitere Adressen können durch den DMDA für eigene Verwendungszwecke selbst definiert werden. 

Bundesamt für Sicherheit in der Informationstechnik 

16 

5 Datenstrukturen 

## **5 Datenstrukturen** 

Im PVD sind insbesondere „Nachrichten“, „Bestätigungsnachrichten“ und „Meldungsnachrichten“ zu unterscheiden. 

## **5.1 Nachrichten** 

Konzeptuell ist von einer Nachricht ein Nachrichtenentwurf als Vorstufe zu einer Nachricht zu unterscheiden. Eine Nachricht, die noch nicht vom Postfachdienst vollständig entgegengenommen und für den Versand vorbereitet worden ist, gilt als Nachrichtenentwurf. Eine Nachricht ist für den Versand vorbereitet, wenn die Metadaten in der Nachricht durch den Postfachdienst (siehe Abschnitt 6, Schritt 29) gesetzt worden sind. 

Nachrichten bestehen aus Metadaten und dem Nachrichtentext. 

Die Metadaten werden zusammen mit der Nachricht übermittelt und an entsprechender Stelle im Kontrollfluss des PVD ausgewertet. In Abhängigkeit der eingestellten Werte werden die dazu vorgesehenen Aktivitäten ausgeführt. Die Metadaten einer Nachricht sind im folgenden aufgeführt: 

|**_Nr._**|**_Bezeichnung_**|**_Werte_**|**_Beschreibung_**|
|---|---|---|---|
|**1**|Versandbestätigung|ja / nein|Dieses Feld entspricht der Versandoption<br>„Versandbestätigung“. Es ist auf „ja“ gesetzt, falls<br>diese Option in Schritt 1 ausgewählt wurde. In<br>diesem Fall generiert der PVD des Absenders eine<br>Versandbestätigung, sobald diese Nachricht<br>versendet worden ist (Schritt 36 ff.).|
|2|Eingangsbestätigung|ja / nein|Dieses Feld entspricht der Versandoption<br>„Eingangsbestätigung“. Es ist auf „ja“ gesetzt,<br>falls diese Option in Schritt 1 ausgewählt wurde.<br>In diesem Fall generiert der PVD des Empfängers<br>eine Eingangsbestätigung, sobald diese Nachricht<br>im Postfach des Empfängers abgelegt worden ist<br>(Schritt 67 ff.).|
|3|Abholbestätigung|ja / nein|Dieses Feld entspricht der Versandoption<br>„Abholbestätigung“. Es ist auf „ja“ gesetzt, falls<br>diese Option in Schritt 1 ausgewählt wurde. Der<br>Absender muss zum Zeitpunkt des Versendens mit<br>Authentisierungsniveau „hoch“ am De-Mail-<br>Konto angemeldet sein (Prüfung erfolgt in Schritt<br>19). Eine Abholbestätigung darf nur durch<br>berechtigte öffentliche Stellen angefordert werden<br>(Prüfung erfolgt in Schritt 24).|



Bundesamt für Sicherheit in der Informationstechnik 

17 

5 Datenstrukturen 

|**_Nr._**|**_Bezeichnung_**|**_Werte_**|**_Beschreibung_**|
|---|---|---|---|
||||Ist diese Versandoption gesetzt, generiert der PVD<br>des Empfängers eine Abholbestätigung, nachdem<br>diese Nachricht in dessen Postfach abgelegt<br>worden ist und der Nutzer sich das nächste Mal an<br>seinem De-Mail-Konto mit<br>Authentisierungsniveau „hoch“ anmeldet.|
|4|Absenderbestätigt|ja / nein|Dieses Feld entspricht der Versandoption<br>„Absenderbestätigt“. Es ist auf „ja“ gesetzt, falls<br>diese Option ausgewählt wurde. Der Absender<br>muss zum Zeitpunkt des Versendens mit<br>Authentisierungsniveau „hoch“ am De-Mail-<br>Konto angemeldet sein (Prüfung erfolgt in Schritt<br>19).|
|5|Persönlich|ja / nein|Dieses Feld entspricht der Versandoption<br>„Persönlich“. Es ist auf „ja“ gesetzt, falls diese<br>Option ausgewählt wurde. Der Empfänger muss<br>zum Zeitpunkt des Abrufs mit<br>Authentisierungsniveau „hoch“ am De-Mail-<br>Konto angemeldet sein (Prüfung erfolgt in Schritt<br>78). Der Absender muss zum Zeitpunkt des<br>Versendens mit Authentisierungsniveau „hoch“<br>am De-Mail-Konto angemeldet sein (Prüfung<br>erfolgt in Schritt 19).|
|6|Absender-Adresse|De-Mail-<br>Adresse|Die vom Absender in Schritt 2 gewählte De-Mail-<br>Adresse, unter der die Nachricht versendet werden<br>soll (Prüfung der Gültigkeit erfolgt in Schritt 12).|
|7|Empfänger-<br>Adresse(n) (auch für<br>CC, BCC)|De-Mail-<br>Adresse|Die vom Absender in Schritt 3 gewählten<br>Empfänger-Adressen, an die die Nachricht<br>versendet werden soll (Prüfung auf Validität in<br>Schritt 15).<br>Hinweis: Nur die eigene BCC-Adresse wird für<br>den jeweiligen BCC-Empfänger innerhalb der<br>Metadaten auf der Empfänger-Seite belassen.|
|8|Betreff|Text|Der vom Absender in Schritt 4 angegebene<br>„Betreff“ zur Nachricht.|
|9|Nachrichten-<br>Kennung des<br>Absenders|Text|Die vom Absender in Schritt 4 angegebene<br>„Nachrichten-Kennung“ ermöglicht dem<br>Absender, einer Nachricht zusätzlich zum Betreff<br>eine Information mitzugeben. Anhand dieser|



Bundesamt für Sicherheit in der Informationstechnik 

18 

5 Datenstrukturen 

|**_Nr._**|**_Bezeichnung_**|**_Werte_**|**_Beschreibung_**|
|---|---|---|---|
||||Kennung kann er andere Nachrichten, die die<br>Nachrichten-Kennung referenzieren, wie z. B.<br>Bestätigungsnachrichten, einem internen Vorgang<br>zuordnen.|
|10|Antwort-Adresse|De-Mail-<br>Adresse|Optionale Angabe, an welche De-Mail-Adresse<br>eine Antwort auf diese Nachricht adressiert<br>werden soll (wird in Schritt 3 gesetzt). An diese<br>Adresse werden auch eventuell angeforderte<br>Bestätigungsnachrichten gesendet (Prüfung auf<br>Validität in Schritt 12).|
|11|Authentisierungs-<br>niveau|normal/hoch|Das Authentisierungsniveau, mit dem der<br>Absender zum Zeitpunkt des Versendens der<br>Nachricht am De-Mail-Konto angemeldet war<br>(wird in Schritt 29 gesetzt).|
|12|Authentisierungs-<br>Mechanismus|Text|Bezeichnung des Authentisierungsmechanismus,<br>mit dem der Absender sich zum Zeitpunkt des<br>Versendens der Nachricht am De-Mail-Konto<br>angemeldet hatte (wird in Schritt 29 gesetzt).<br>Hinweis: Dieses Feld wird im PVD nicht weiter<br>ausgewertet. Es soll jedoch Absendern und<br>Empfängern ermöglichen, sich bilateral auf einen<br>für ein bestimmtes Fachverfahren notwendigen<br>Authentisierungsmechanismus zu verständigen.|
|13|Versanddatum und -<br>zeit|Datum & Zeit|Datum und sekundengenaue Zeitangabe für den<br>Zeitpunkt, an dem der Postfachdienst die<br>Nachricht an den Versanddienst weiterleitet (wird<br>in Schritt 29 gesetzt).|
|14|Message-ID|Text|Eindeutige Kennung der Nachricht, die vom<br>Postfachdienst generiert wird. Mit dieser Kennung<br>soll es möglich sein, Nachrichten im Rahmen<br>einer Postfach-internen Verwaltung schnell zu<br>referenzieren (wird in Schritt 29 gesetzt).|
|15|De-Mail-Server|Text|Eindeutige Bezeichnung des DMDA-Servers, der<br>diese Metadaten erstellt (wird in Schritt 29<br>gesetzt).|
|16|Nachrichten-Typ|Bestätigungs-<br>nachricht/<br>Meldungs-|In diesem Feld können spezielle Nachrichten, die<br>automatisiert vom Empfänger-System behandelt<br>werden sollen, als solche gekennzeichnet werden|



Bundesamt für Sicherheit in der Informationstechnik 

19 

5 Datenstrukturen 

|**_Nr._**|**_Bezeichnung_**|**_Werte_**|**_Beschreibung_**|
|---|---|---|---|
|||nachricht/<br>nicht weiter<br>spezifizierte<br>De-Mail-<br>Nachricht|(siehe z. B. Schritt 29, Schritt 38, Schritt 56 und<br>Schritt 69). Damit soll verhindert werden, dass der<br>Inhalt aller Nachrichten aufwändig analysiert<br>werden muss, um die entsprechenden Nachrichten<br>zu identifizieren.<br>Innerhalb des PVD sind als spezielle Nachrichten<br>Bestätigungs- und Meldungsnachrichten<br>vorgesehen.|
|17|Hash-Wert / Signatur|Message<br>Digest /<br>Signatur|Message Digest, der über die Metadaten-Felder 1<br>bis 16, sowie über alle Abschnitte des<br>Nachrichtentexts berechnet wird. Der Message<br>Digest wird vom Postfachdienst des Absenders in<br>Schritt 29 erstellt.<br>Falls die Versandoption „Absenderbestätigt“ vom<br>Nutzer gewählt wurde und dieser auch mit<br>Authentisierungsniveau „hoch“ am De-Mail-<br>Konto zum Zeitpunkt des Nachrichtenversandes<br>angemeldet war, wird in Schritt 31 eine<br>qualifizierte Signatur erzeugt und in dem Feld<br>gespeichert.<br>Die Metadaten werden nach Versand durch den<br>Postfachdienst des Absenders im Kontrollfluss des<br>PVD nicht verändert.|
|18|Signaturzertifikat des<br>DMDA|Signatur|Dieses Feld wird durch den DMDA nur gesetzt<br>(Schritt 31), falls die Versandoption<br>„Absenderbestätigt„ vom Nutzer gewählt wurde<br>und dieser auch mit Authentisierungsniveau<br>„hoch“ am De-Mail-Konto zum Zeitpunkt des<br>Nachrichtenversandes angemeldet war.<br>Dieses Feld enthält das für die Signatur<br>verwendete Zertifikat des DMDA.|
|19|Empfänger-Adressen<br>für den Transport|De-Mail-<br>Adresse|Hinweis: Beim Transport können die Empfänger-<br>Adressen bei Weiterleitungen umgeschrieben<br>werden (vgl. Schritt 50 und Schritt 72). Im Initial-<br>Zustand müssen diese Adressen denen von Nr. 7<br>entsprechen (erfolgt in Schritt 29).|
|20|Weiterleitungs-<br>Absender|De-Mail-<br>Adresse|Dieses Feld wird durch den Postfachdienst des<br>Empfängers nur gesetzt (Schritt 72), falls eine|



Bundesamt für Sicherheit in der Informationstechnik 

20 

5 Datenstrukturen 

|**_Nr._**|**_Bezeichnung_**|**_Werte_**|**_Beschreibung_**|
|---|---|---|---|
||||automatische Weiterleitung eingerichtet wurde.<br>Das Feld wird auf die De-Mail-Adresse gesetzt,<br>von der die Nachricht weitergeleitet wird.|
|21|Vollständiger Name<br>des Kontoinhabers|Nat.Pers.:<br>vollständiger<br>Vor- und<br>Nachname /<br>PseudonymIn<br>stitution:<br>vollständiger<br>Name /<br>Bezeichnung<br>der Institution|Das Feld enthält bei nat. Personen den Namen und<br>die Vornamen bzw. nur das Pseudonym bei<br>Pseudonymadressen und bei Institutionen den<br>Namen oder die Bezeichnung des Kontoinhabers.|



## _Tabelle 2: Metadaten einer Nachricht_ 

Die Metadaten 1 bis 5 („Versandoptionen“) entsprechen den vom Absender einer Nachricht ausgewählten Versandoptionen (vgl. Abschnitt 3.3). Falls ein Nutzer eine Nachricht oder Nachrichtenanhänge (qualifiziert) signiert oder Ende-zu-Ende-verschlüsselt, so werden in diesem Fall die ausgewählten Nachrichten-Teile direkt signiert und/oder verschlüsselt, ohne dies in den Metadaten explizit zu speichern. 

Die Metadaten 6 bis 10 („Adressen und Betreff“) werden bei der Erstellung des Nachrichtenentwurfs (vgl. Abschnitt 6.1) durch den Nutzer spezifiziert. Die Metadaten 11 bis 19 („interne Verwaltungsdaten“) werden vom Postfachdienst des Absenders erstellt bzw. vordefiniert, wenn aus dem Nachrichtenentwurf eine Nachricht geworden ist (Schritt 29 und Schritt 31). Das Metadatum „Weiterleitungs-Absender“ (Feld 20) wird erst vom PVD des jeweiligen Empfängers gesetzt, von dem die Nachricht weitergeleitet wird. 

## **5.2 Bestätigungen und Bestätigungsnachrichten** 

Bestätigungsnachrichten sind Nachrichten, die vom PVD generiert werden, wenn eine Versand-, Eingangs- oder Abholbestätigung angefordert wurde. 

Die Inhalte der Bestätigungsnachrichten sind in [TR DM PVD IO] beschrieben. 

## **5.3 Meldungen und Meldungsnachrichten** 

Meldungen sind Informationen des DMDA an den Nutzer, um ihn über bestimmte Ereignisse zu informieren. 

Wenn in diesem Dokument von einer „Meldungsnachricht“ gesprochen wird, so ist die Meldung in Form einer Meldungsnachricht zu verschicken. Ist hingegen nur von „Meldung“ die Rede, so kann diese in Abhängigkeit von der Benutzerschnittstelle auch anders verschickt bzw. dargestellt werden. 

Bundesamt für Sicherheit in der Informationstechnik 

21 

5 Datenstrukturen 

Die Inhalte einer Meldungsnachricht sind in [TR DM PVD IO] spezifiziert. 

Bundesamt für Sicherheit in der Informationstechnik 

22 

6 Funktionale Beschreibung 

## **6 Funktionale Beschreibung** 

Im Folgenden werden die einzelnen Schritte für das Erstellen, Versenden, Empfangen und Abrufen von Nachrichten mit dem PVD von De-Mail beschrieben. Funktionen, die der Nutzer interaktiv aufrufen kann, wenn er an seinem Postfach angemeldet ist, werden in Abschnitt 7 dargestellt. Die referenzierten Funktionen des Accountmanagements, der Schadsoftwareprüfung und des Zeitdienstes werden in [TR DM ACM FU] und [TR DM IT-BInfra FU] erläutert. 

Im Kontrollfluss des PVD werden an verschiedenen Stellen neue Nachrichten, wie z. B. Bestätigungsnachrichten, automatisch erzeugt und an den Empfänger versendet. In diesen Fällen werden die in diesem Abschnitt beschriebenen Schritte für das Erstellen und Versenden von Nachrichten rekursiv durchlaufen. Die die Nachricht erzeugende Stelle wird damit zum Absender einer Nachricht. 

Es werden in den nachfolgenden Tabellen die wichtigsten Fehlerfälle dargestellt, die vom DMDA bei dem von ihm angebotenen PVD mindestens zu berücksichtigen sind. Weitere können durch den DMDA hinzugefügt werden. Die Darstellung der Fehlerfälle für den Nutzer kann durch den DMDA gewählt werden. 

## **6.1 Erstellen von Nachrichten durch den Absender** 

Die vorgegebene Reihenfolge für das Erstellen einer Nachricht (Schritt 1 bis Schritt 4) ist beispielhaft zu verstehen. 

|**Schritt 1**|**_Versandoption festlegen_**|
|---|---|
|Kurzbeschreibung|Der Absender erstellt einen neuen Nachrichtenentwurf und legt die<br>Versandoptionen der Nachricht fest (vgl. Abschnitt 3.3).|
|Akteure|Absender|
|Auslöser|Absender|
|Vorbedingung|Fall a)<br>Der Absender ist am De-Mail-Konto über Web-Schnittstelle<br>angemeldet.<br>Fall b)<br>Der Absender verwendet einen lokalen Nachrichten-Client.|
|Input|Werte der Versandoptionen (ja/nein)<br>**•**<br>Versand-, Eingangs- und/oder Abholbestätigungen<br>**•**<br>Persönlich<br>**•**<br>Absenderbestätigt|
|Ergebnis|Versandoptionen für den entsprechenden Nachrichtenentwurf festgelegt|
|Nachbedingung||
|Ablauf|**•**<br>Absender erstellt einen neuen Nachrichtenentwurf durch die<br>Funktionen „Neue Nachricht“, „Beantworten“oder „Weiterleiten“|



Bundesamt für Sicherheit in der Informationstechnik 

23 

## 6 Funktionale Beschreibung 

||**•**<br>Absender legt die Versandoptionen fest|
|---|---|
|Fehlerfälle||
|**Schritt 2**|**_Absender-Adresse auswählen_**|
|Kurzbeschreibung|Der Absender wählt aus, unter welcher zur Verfügung stehenden Absender-<br>Adresse die Nachricht versendet werden soll.|
|Akteure|Absender|
|Auslöser|Absender|
|Vorbedingung|Fall a)<br>Der Absender ist am De-Mail-Konto über Web-Schnittstelle<br>angemeldet.<br>Fall b)<br>Der Absender verwendet einen lokalen Nachrichten-Client.|
|Input|Default-Absender-Adresse oder Auswahl der ihm zur Verfügung stehenden<br>Absender-Adressen (primäre De-Mail-Adresse bzw. zum De-Mail-Konto<br>zugehörige und gültige Pseudonym-Adressen).|
|Ergebnis|Absender-Adresse festgelegt|
|Nachbedingung||
|Ablauf|Für Fall a)<br>**•**<br>Absender übernimmt die durch die Applikation angezeigte Default-<br>Absender-Adresse ohne Änderung, oder<br>**•**<br>Absender wählt aus den zur Verfügung stehenden Kennungen eine<br>Absender-Adresse aus.<br>Für Fall b)<br>**•**<br>Absender übernimmt die durch die Applikation angezeigte Default-<br>Absender-Adresse ohne Änderung, oder<br>**•**<br>Absender wählt aus den zur Verfügung stehenden Kennungen eine<br>Absender-Adresse aus, oder<br>**•**<br>Absender editiert die Absender-Adresse frei.<br>Hinweis: Nutzt der Absender einen lokalen Nachrichten-Client,<br>hängt es von diesem ab, ob die Absender-Adresse frei editiert<br>werden kann oder nur vorgegebene ausgewählt werden können.<br>**•**<br>Die ausgewählte Absender-Adresse wird in den Metadaten des<br>Nachrichtenentwurfs gespeichert.|
|Fehlerfälle|FC-01: Ungültiges Adressformat<br>FC-02: Keine De-Mail-Adresse|
|**Schritt 3**|**_Empfänger-Adressen und optionale Antwort-Adresse angeben_**|
|Kurzbeschreibung|Der Absender legt die Empfänger der Nachricht durch Angabe der<br>Empfänger-Adressen fest. Weiterhin kann er optional auch eine Antwort-<br>Adresse angeben.|



Bundesamt für Sicherheit in der Informationstechnik 

24 

6 Funktionale Beschreibung 

|Akteure|Absender|
|---|---|
|Auslöser|Absender|
|Vorbedingung||
|Input|Empfänger-Adressen (De-Mail-Adresse) und Antwort-Adresse (De-Mail-<br>Adresse)|
|Ergebnis|Empfänger-Adressen angegeben|
|Nachbedingung||
|Ablauf|**•**<br>Absender editiert die Empfängeradressen frei oder wählt sie aus<br>seinem persönlichen Adressbuch oder dem ÖVD (vgl. Funktion 7,<br>Abschnitt 7) aus<br>**•**<br>Empfänger-Adressen und Antwort-Adresse werden in den<br>Metadaten des Nachrichtenentwurfes gespeichert.|
|Fehlerfälle|FC-01: Ungültiges Adressformat|
|**Schritt 4**|<br>**_Nachrichteninhalt editieren und Anhänge hinzufügen_**|
|Kurzbeschreibung|Der Absender editiert den Betreff der Nachricht, den Nachrichteninhalt und<br>fügt ggf. Dateianhänge hinzu.|
|Akteure|Absender, DA (optional)|
|Auslöser|Absender|
|Vorbedingung||
|Input|Nachrichtentext, Dateianhänge|
|Ergebnis|Nachricht editiert und ggf. Dateianhänge hinzugefügt|
|Nachbedingung||
|Ablauf|**•**<br>Absender editiert<br>**◦**<br>den Betreff<br>**◦**<br>Nachrichten-Kennung (optional)<br>**◦**<br>Nachrichtentext<br>**•**<br>Absender fügt Anhänge hinzu<br>**◦**<br>von lokaler Festplatte<br>**◦**<br>aus der DA (optional)<br>**•**<br>Daten in Nachrichtenentwurf speichern|
|Fehlerfälle||
|**Schritt 5**|**_Entscheidungsknoten: Ende-zu-Ende Signatur erwünscht?_**|
|Kurzbeschreibung|Auswertung, ob der Absender den Nachrichtenentwurf elektronisch<br>signieren möchte.|



Bundesamt für Sicherheit in der Informationstechnik 

25 

6 Funktionale Beschreibung 

|ja|Schritt 6|
|---|---|
|nein|Schritt 7|
|**Schritt 6**|**_Elektronisch signieren_**|
|Kurzbeschreibung|Der Absender signiert den Nachrichtenentwurf und/oder Anhänge des<br>Nachrichtenentwurfs.|
|Akteure|Signaturanwendungskomponente (SAK)|
|Auslöser|Absender|
|Vorbedingung||
|Input|Nachrichtenentwurf|
|Ergebnis|Signierter Nachrichtenentwurf|
|Nachbedingung||
|Ablauf|**•**<br>Übergabe der zu signierenden Informationen an eine SAK<br>**•**<br>Signieren des Nachrichtenentwurfs innerhalb der SAK<br>**•**<br>Integration der signierten Nachrichtenbestandteile und der Signatur<br>in den Nachrichtenentwurf|
|Fehlerfälle|FC-01: Warnung: Versenden der Adresse unter einer Pseudonym-Adresse,<br>Zertifikatsinformationen können weitere Informationen zur Person<br>enthalten.<br>FC-02: Keine SAK gefunden<br>FC-03: Keine gültige SSEE gefunden|
|**Schritt 7**|<br>**_Entscheidungsknoten: Ende-zu-Ende-Verschlüsselung erwünscht?_**|
|Kurzbeschreibung|Auswertung, ob der Absender den Nachrichtenentwurf Ende-zu-Ende-<br>verschlüsseln möchte.|
|ja|Schritt 8|
|nein|Schritt 9|
|**Schritt 8**|**_Nachrichtenentwurf verschlüsseln_**|
|Kurzbeschreibung|Der Absender verschlüsselt den Nachrichtenentwurf für die Empfänger.|
|Akteure|Absender|
|Auslöser|Absender|
|Vorbedingung|Der Absender hat die Empfänger-Adressen angegeben und den<br>Nachrichtenentwurf ggf. signiert.<br>Die Zertifikate der Empfänger liegen dem Absender über das persönliche<br>Adressbuch oder den ÖVD vor.|
|Input|Nachrichtenentwurf|
|Ergebnis|Verschlüsselter Nachrichtenentwurf|



Bundesamt für Sicherheit in der Informationstechnik 

26 

6 Funktionale Beschreibung 

|Nachbedingung||
|---|---|
|Ablauf|**•**<br>Der zu verschlüsselnde Nachrichtenentwurf inklusive der<br>Dateianhänge wird an eine Verschlüsselungsfunktion übergeben.<br>**•**<br>Die Verschlüsselungsfunktion sucht die Zertifikate der Empfänger<br>im persönlichen Adressbuch und/oder dem ÖVD.<br>**•**<br>Die Zertifikate werden hinsichtlich der Vertrauenswürdigkeit und<br>der Gültigkeit verifiziert.<br>**•**<br>Es werden die symmetrischen Verschlüsselungsschlüssel generiert.<br>**•**<br>Der Nachrichtentext des Nachrichtenentwurfs wird mit dem<br>Verschlüsselungsschlüssel verschlüsselt.<br>**•**<br>Der Verschlüsselungsschlüssel wird mit den öffentlichen Schlüsseln<br>des Absenders und der Empfänger verschlüsselt.<br>**•**<br>Der symmetrische Verschlüsselungsschlüssel wird sicher gelöscht.<br>**•**<br>Die Verschlüsslungsinformationen und die verschlüsselten<br>Nachrichtenbestandteile werden in den Nachrichtenentwurf<br>eingebettet.<br>**•**<br>Der zu verschlüsselnde Inhalt wird verworfen.<br>Hinweis: Die Generierung des Verschlüsselungsschlüssels und die<br>Verschlüsselung des Nachrichtenentwurfs müssen auf dem System des<br>Nutzers erfolgen. Der zu verschlüsselnde Nachrichtenentwurf darf nicht auf<br>dem DMDA-Server temporär zwischengespeichert werden.|
|Fehlerfälle|FC-01:Kein Zertifikat gefunden<br>FC-02:Zertifikat nicht vertrauenswürdig<br>FC-03:Zertifikat ungültig|
|**Schritt 9**|<br>**_Nachrichtenentwurf an Postfachdienst Absender versenden_**|
|Kurzbeschreibung|Der Nachrichtenentwurf wird vom Web- oder Nachrichten-Client des<br>Absenders zu dessen Postfachdienst gesendet.|
|Akteure|Absender, Postfachdienst Absender|
|Auslöser|Absender|
|Vorbedingung|**•**<br>Absender an seinem De-Mail-Konto angemeldet<br>**•**<br>Sicherer Kanal zwischen Client des Nutzers und dem Postfachdienst<br>des Absenders aufgebaut|
|Input|Nachrichtenentwurf|
|Ergebnis|Nachrichtenentwurf ist zum Postfachdienst des Absenders abgeschickt|
|Nachbedingung||
|Ablauf|Nachrichtenentwurf wird vom zum Postfachdienst übermittelt|



Bundesamt für Sicherheit in der Informationstechnik 

27 

6 Funktionale Beschreibung 

|Fehlerfälle|FC-01: Nutzer nicht am De-Mail-Konto angemeldet<br>FC-02: Absender nicht autorisiert, Nachrichten zu verschicken (z.B. De-<br>Mail-Konto gesperrt)<br>FC-03: Postfachdienst hat Nachrichtenentwurf nicht vollständig<br>angenommen|
|---|---|



_Tabelle 3: Schritte zum Erstellen von Nachrichten_ 

## **6.2 Entgegennahme von Nachrichten durch Postfachdienst des Absenders** 

|**Schritt 10**|**_Nachrichtenentwurf vom Absender empfangen_**|
|---|---|
|Kurzbeschreibung|Der Postfachdienst des Absenders empfängt den Nachrichtenentwurf vom<br>System des Absenders.|
|Akteure|Postfachdienst Absender|
|Auslöser|Absender|
|Vorbedingung||
|Input|Nachrichtenentwurf|
|Ergebnis|Nachrichtenentwurf vom Postfachdienst angenommen|
|Nachbedingung||
|Ablauf|**•**<br>Nachrichtenentwurf wird vom Postfachdienst empfangen<br>**•**<br>Prüfen, ob Nachricht syntaktisch korrekt ist|
|Fehlerfälle|FC-01: Nachrichtenentwurf nicht vollständig übertragen<br>FC-02: Nachricht enthält syntaktische Fehler|
|**Schritt 11**|<br>**_Nachrichtenentwurf im Postausgang ablegen_**|
|Kurzbeschreibung|Der Nachrichtenentwurf wird vom Postfachdienst im Postausgang des<br>Absender-Postfaches abgelegt.|
|Akteure|Postfachdienst Absender|
|Auslöser|Postfachdienst Absender|
|Vorbedingung||
|Input|Nachrichtenentwurf|
|Ergebnis|Nachrichtenentwurf im Postausgang|
|Nachbedingung||
|Ablauf|Nachrichtenentwurf wird im Postausgang des Absender-Postfaches<br>abgelegt.|



Bundesamt für Sicherheit in der Informationstechnik 

28 

6 Funktionale Beschreibung 

|Fehlerfälle|FC-01: Kapazitätsgrenze des Absender-Postfaches erreicht|
|---|---|
|**Schritt 12**|<br>**_Prüfung Absender-Adresse_**|
|Kurzbeschreibung|Prüfung, ob die im Nachrichtenentwurf angegebene Absender-Adresse dem<br>De-Mail-Konto zugeordnet ist.|
|Akteure|Postfachdienst Absender, Account-Dienst|
|Auslöser|Postfachdienst Absender|
|Vorbedingung||
|Input|Nachrichtenentwurf|
|Ergebnis|Ergebnis der Prüfung (ok / nicht ok)|
|Nachbedingung||
|Ablauf|**•**<br>Unter Zuhilfenahme des De-Mail-Kontos, an dem der Absender<br>angemeldet ist, werden die dem De-Mail-Konto zugeordneten De-<br>Mail-Adresse ermittelt.<br>**•**<br>Absender-Adresse (Nr. 6) des Nachrichtenentwurfs prüfen, ob diese<br>dem De-Mail-Konto zugeordnet ist.<br>**•**<br>Prüfung, ob die optionale Antwort-Adresse (Nr. 10) eine De-Mail-<br>Adresse ist.|
|Fehlerfälle|FC-01: Antwort-Adresse ist keine De-Mail-Adresse|
|**Schritt 13**|**_Entscheidungsknoten: Prüfung OK?_**|
|Kurzbeschreibung|Ergebnis der Prüfung, ob Absender-Adresse dem De-Mail-Konto des<br>Absenders zugeordnet ist.|
|ja|Schritt 15|
|nein|Schritt 14|
|**Schritt 14**|**_Meldung an Absender_**|
|Kurzbeschreibung|Der Postfachdienst erzeugt eine Meldung für den Absender, dass in seinem<br>Nachrichtenentwurf eine ihm nicht zugeordnete Absender-Adresse<br>gefunden wurde.|
|Akteure|Postfachdienst Absender|
|Auslöser|Postfachdienst Absender|
|Vorbedingung||
|Input|Prüfergebnis aus Schritt 12|
|Ergebnis|Meldung|
|Nachbedingung|Anhalten|
|Ablauf|**•**<br>Meldung an den Nutzer<br>**•**<br>Nachrichtenentwurf löschen und aus Postausgang entfernen|



Bundesamt für Sicherheit in der Informationstechnik 

29 

6 Funktionale Beschreibung 

|Fehlerfälle|FC-01: Meldung konnte nicht abgesendet/dargestellt werden.|
|---|---|
|**Schritt 15**|<br>**_Prüfung der Empfänger-Adressen_**|
|Kurzbeschreibung|Prüfung des Nachrichtenentwurfs, ob die dort eingetragenen Empfänger-<br>Adressen De-Mail-Adressen sind.|
|Akteure|Postfachdienst Absender|
|Auslöser|Postfachdienst Absender|
|Vorbedingung|Es sind Empfänger im Nachrichtenentwurf angegeben.|
|Input|Nachrichtenentwurf|
|Ergebnis|Ergebnis der Prüfung (ok / nicht ok)|
|Nachbedingung||
|Ablauf|Prüfen, ob jede Empfänger-Adresse eine De-Mail-Adresse ist|
|Fehlerfälle||
|**Schritt 16**|**_Entscheidungsknoten: Prüfung OK?_**|
|Kurzbeschreibung|Ergebnis der Empfänger-Adressen-Prüfung auswerten|
|ja|Schritt 18|
|nein|Schritt 17|
|**Schritt 17**|**_Meldung an Absender_**|
|Kurzbeschreibung|Der Postfachdienst erzeugt eine Meldung für den Absender, dass in seinem<br>Nachrichtenentwurf Empfänger außerhalb von De-Mail adressiert sind.|
|Akteure|Postfachdienst Absender|
|Auslöser|Postfachdienst Absender|
|Vorbedingung||
|Input|Prüfergebnis aus Schritt 15|
|Ergebnis|Meldung|
|Nachbedingung|Anhalten|
|Ablauf|**•**<br>Meldung an den Nutzer<br>**•**<br>Nachrichtenentwurf löschen und aus Postausgang entfernen|
|Fehlerfälle|FC-01: Meldung konnte nicht abgesendet/dargestellt werden|
|**Schritt 18**|<br>**_Aktuelles Authentisierungsniveau des Absenders ermitteln_**|
|Kurzbeschreibung|Das aktuelle Authentisierungsniveau des Absenders wird ermittelt.|
|Akteure|Postfachdienst Absender, Account-Dienst|
|Auslöser|Postfachdienst Absender|
|Vorbedingung||



Bundesamt für Sicherheit in der Informationstechnik 

30 

6 Funktionale Beschreibung 

|Input|Nutzer-Kennung des De-Mail-Kontos, Nachrichtenentwurf|
|---|---|
|Ergebnis|Aktuelles Authentisierungsniveau des Absenders|
|Nachbedingung||
|Ablauf|**•**<br>De-Mail-Konto ermitteln<br>**•**<br>Anfrage an Account-Dienst, welches aktuelle<br>Authentisierungsniveau der Absender besitzt|
|Fehlerfälle||
|**Schritt 19**|**_Entscheidungsknoten: Authentisierungsniveau für Versandoptionen OK?_**|
|Kurzbeschreibung|Wert für Versandoption „Absenderbestätigt“ aus Metadaten des<br>Nachrichtenentwurfs ermitteln<br>Wert für Versandoption „Persönlich“ aus Metadaten des<br>Nachrichtenentwurfs ermitteln<br>Wert für Versandoption „Abholbestätigung“ aus Metadaten des<br>Nachrichtenentwurfs ermitteln<br>Prüfung, ob die Versandoption „Abholbestätigung“, „Absenderbestätigt“<br>und/oder „Persönlich“ im Nachrichtenentwurf gewählt wurde und ob in<br>diesem Fall das Authentisierungsniveau des Absenders „hoch“ist.|
|ja|Schritt 21|
|nein|Schritt 20|
|**Schritt 20**|**_Meldung an Absender: „Versandoptionen ‚Abholbestätigung’,_**<br>**_‚Absenderbestätigt’ und ‚Persönlich’ erfordern  Authentisierungsniveau_**<br>**_‚hoch’“_**|
|Kurzbeschreibung|Der Postfachdienst erzeugt eine Meldung für den Absender mit der<br>Aufforderung, sich mit Authentisierungsniveau „hoch“ am De-Mail-Konto<br>anzumelden.|
|Akteure|Postfachdienst Absender|
|Auslöser|Postfachdienst Absender|
|Vorbedingung|Prüfung Versandoption „Abholbestätigung“, „Absenderbestätigt“ /<br>„Persönlich“nicht ok|
|Input|Nachrichtenentwurf|
|Ergebnis|Meldung|
|Nachbedingung|Anhalten|
|Ablauf|**•**<br>Meldung an den Nutzer<br>**•**<br>Nachrichtenentwurf löschen und aus Postausgang entfernen|
|Fehlerfälle|FC-01: Meldung konnte nicht abgesendet/dargestellt werden|
|**Schritt 21**|<br>**_Entscheidungsknoten: Prüfung, ob Pseudonym-Adresse als Absender_**|



Bundesamt für Sicherheit in der Informationstechnik 

31 

## 6 Funktionale Beschreibung 

||**_gewählt und Versandoption „Absenderbestätigt“?_**|
|---|---|
|Kurzbeschreibung|Wert für Versandoption „Absenderbestätigt“ aus Metadaten des<br>Nachrichtenentwurfs ermitteln<br>Wert für Absenderadresse aus Metadaten des Nachrichtenentwurfs<br>ermitteln<br>Prüfung, ob Pseudonym-Adresse als Absender gewählt und Versandoption<br>„Absenderbestätigt“?|
|ja|Schritt 22|
|nein|Schritt 23|
|**Schritt 22**|**_Meldung an Absender: Versandoption „Absenderbestätigt“ kann nicht in_**<br>**_Kombination mit einer Pseudonymadresse verwendet werden._**|
|Kurzbeschreibung|Der Postfachdienst erzeugt eine Meldung für den Absender mit dem<br>Hinweis, dass die Versandoption „Absenderbestätigt“ nicht in Kombination<br>mit einer Pseudonymadresse verwendet werden kann.|
|Akteure|Postfachdienst Absender|
|Auslöser|Postfachdienst Absender|
|Vorbedingung|Pseudonym-Adresse als Absender gewählt und Versandoption<br>„Absenderbestätigt“|
|Input|Nachrichtenentwurf|
|Ergebnis|Meldung|
|Nachbedingung|Anhalten|
|Ablauf|**•**<br>Meldung an den Nutzer<br>**•**<br>Nachrichtenentwurf löschen und aus Postausgang entfernen|
|Fehlerfälle|FC-01: Meldung konnte nicht abgesendet/dargestellt werden|
|**Schritt 23**|<br>**_Prüfung der Berechtigung zur Nutzung Versandoption_**<br>**_„Abholbestätigung“_**|
|Kurzbeschreibung|Prüfung des Nachrichtenentwurfs, ob eine Berechtigung zur Nutzung der<br>Versandoption Abholbestätigung für den Nutzer besteht|
|Akteure|Postfachdienst Absender, Account-Dienst|
|Auslöser|Postfachdienst Absender|
|Vorbedingung|Es ist die Versandoption „Abholbestätigung“ im Nachrichtenentwurf<br>angegeben.|
|Input|Nachrichtenentwurf|
|Ergebnis|Ergebnis der Prüfung (ok / nicht ok)|
|Nachbedingung||



Bundesamt für Sicherheit in der Informationstechnik 

32 

6 Funktionale Beschreibung 

|Ablauf|Prüfen, ob die Nutzung der Versandoption „Abholbestätigung“ durch den<br>Nutzer möglich ist (vgl. [TR DM ACM FU])|
|---|---|
|Fehlerfälle||
|**Schritt 24**|**_Entscheidungsknoten: Berechtigung zur Nutzung der Versandoption_**<br>**_„Abholbestätigung“ OK?_**|
|Kurzbeschreibung|Ergebnis der Berechtigung zur Nutzung der Versandoption<br>„Abholbestätigung“auswerten.|
|ja|Schritt 26|
|nein|Schritt 25|
|**Schritt 25**|**_Meldung an Absender: „Versandoption ‚Abholbestätigung’ nicht_**<br>**_gestattet_**|
|Kurzbeschreibung|Der Postfachdienst erzeugt eine Meldung für den Absender, dass die<br>Nutzung der Versandoption „Abholbestätigung“ aufgrund der<br>Berechtigungen nicht möglich ist|
|Akteure|Postfachdienst Absender|
|Auslöser|Postfachdienst Absender|
|Vorbedingung|Berechtigung zur Nutzung der Versandoption „Abholbestätigung“nicht OK|
|Input|Nachrichtenentwurf|
|Ergebnis|Meldung|
|Nachbedingung|Anhalten|
|Ablauf|**•**<br>Meldung an den Nutzer<br>**•**<br>Nachrichtenentwurf löschen und aus Postausgang entfernen|
|Fehlerfälle|FC-01: Meldung konnte nicht abgesendet/dargestellt werden|
|**Schritt 26**|<br>**_Auf Nachrichtenbegrenzung und Schadsoftware prüfen_**|
|Kurzbeschreibung|Hat der Absender sich nur mit dem Authentisierungsniveau „normal“ am<br>Postfachdienst angemeldet, so kann er nur eine begrenzte Anzahl von<br>Nachrichten in einem bestimmten Zeitraum versenden (vgl. 3.1.1.1)<br>Danach erfolgt eine Prüfung auf Schadsoftware.|
|Akteure|Postfachdienst Absender, Account-Dienst, Schadsoftware-Dienst|
|Auslöser|Postfachdienst Absender|
|Vorbedingung|Prüfung der Berechtigung bei Nutzung der Versandoption<br>„Abholbestätigung“OK|
|Input|Nachrichtenentwurf|
|Ergebnis|Ergebnis der Schadsoftware-Prüfung|
|Nachbedingung||



Bundesamt für Sicherheit in der Informationstechnik 

33 

6 Funktionale Beschreibung 

|Ablauf|**•**<br>Falls Authentisierungsniveau des Absenders „normal“, dann<br>**◦**<br>Anzahl der versendeten Nachrichten für den vergangenen<br>Zeitraum bestimmen,<br>**◦**<br>Prüfen, ob noch weitere Nachrichten mit<br>Authentisierungsniveau „normal“ verschickt werden können<br>(vgl. Abschnitt 3.1.1.1).<br>**•**<br>Nachrichtenentwurf an Schadsoftware-Dienst übergeben (s. a.<br>Funktion 2, Abschnitt 7).|
|---|---|
|Fehlerfälle|FC-01: Nachrichtenentwurf nicht prüfbar|
|**Schritt 27**|<br>**_Entscheidungsknoten: Prüfung OK?_**|
|Kurzbeschreibung|Ergebnis der Schadsoftware-Prüfung auswerten|
|ja|Schritt 29|
|nein|Schritt 28|
|**Schritt 28**|**_Meldung an Absender_**|
|Kurzbeschreibung|Der Postfachdienst erzeugt eine Meldung dass<br>**•**<br>zum aktuellen Zeitpunkt keine Nachrichten mit<br>Authentisierungsniveau „normal“ versenden darf oder<br>**•**<br>in seinem Nachrichtenentwurf Schadsoftware gefunden wurde.|
|Akteure|Postfachdienst Absender|
|Auslöser|Postfachdienst Absender|
|Vorbedingung|Schadsoftware-Prüfung durchgeführt|
|Input|Ergebnis der Schadsoftware-Prüfung|
|Ergebnis|Meldung|
|Nachbedingung|Anhalten|
|Ablauf|**•**<br>Meldung an den Nutzer<br>**•**<br>Die Nachricht ist in einen dafür vorgesehenen Ordner zu<br>verschieben oder der Nachrichtenentwurf ist zu löschen und aus<br>dem Postausgang zu entfernen|
|Fehlerfälle|FC-01: Meldung konnte nicht abgesendet/dargestellt werden|
|**Schritt 29**|<br>**_Metadaten setzen und Integrität sichern_**|
|Kurzbeschreibung|Die Metadaten in dem Nachrichtenentwurf, die nicht durch den Nutzer<br>vorgegeben werden, werden durch den Postfachdienst ausgefüllt.<br>Anschließend wird der Hash-Wert zum Nachrichtenentwurf berechnet und<br>in den Metadaten gespeichert.|
|Akteure|Postfachdienst Absender, Zeitdienst, Account-Dienst|
|Auslöser|Postfachdienst Absender|



Bundesamt für Sicherheit in der Informationstechnik 

34 

6 Funktionale Beschreibung 

|Vorbedingung||
|---|---|
|Input|Nachrichtentwurf|
|Ergebnis|Aktuelle Metadaten in der Nachricht gesetzt|
|Nachbedingung||
|Ablauf|Falls Empfänger mit BCC adressiert werden, müssen in diesem Schritt<br>a) die BCC-Empfänger-Adressen aus Element <Empfänger-<br>Adresse(n)> (Nr. 7) und Element <Empfänger-Adressen für den<br>Transport> (Nr. 19) entfernt werden, sowie<br>b) für die BCC-Empfänger-Adressen jeweils eigene Nachrichten mit<br>eigener eindeutiger Message-ID in Element <Message-ID> (Nr. 14)<br>generiert werden (siehe nachfolgende Beschreibung).<br>Hinweis: Dieses Vorgehen ermöglicht, dass die BCC-Empfänger für die<br>über TO und CC adressierten Empfänger nicht erkennbar sind, und<br>trotzdem die Hash-Werte für jeden Nachrichten-Empfänger korrekt erstellt<br>werden.<br>Folgende Metadaten werden vom Postfachdienst in der Nachricht gesetzt:<br>**•**<br>Zeit in Element <Versanddatum und –Zeit> (Nr. 13) der Metadaten<br>schreiben.<br>**•**<br>Aktuelles Authentisierungsniveau in Element<br><Authentisierungsniveau> (Nr. 11) schreiben.<br>**•**<br>Aktuellen Authentisierungs-Mechanismus in Element<br><Authentisierungs-Mechanismus> (Nr. 12) schreiben.<br>**•**<br>Name des aktuellen Servers in Element <De-Mail-Server> (Nr. 15)<br>schreiben.<br>**•**<br>Empfänger-Adressen aus dem Element <Empfänger-Adresse(n)><br>(Nr. 7) in das Element <Empfänger-Adressen für den Transport><br>(Nr. 19) schreiben.<br>**•**<br>In Element <Nachrichten-Typ> (Nr. 16) den Typ der Nachricht<br>setzen.<br>**•**<br>Eindeutige Message-ID generieren und in Element <Message-ID><br>(Nr. 14) schreiben.<br>**•**<br>Hash-Wert über Metadaten Nr. 1 bis Nr. 16 und Nachrichtentext<br>berechnen und in Element <Hash-Wert> (Nr. 17) schreiben.<br>Hinweis: Mit dem Setzen der Metadaten innerhalb des<br>Nachrichtenentwurfes wird aus diesem eine Nachricht.|
|Fehlerfälle|FC-01: Keine De-Mail-Zeit ermittelbar|
|**Schritt 30**|**_Entscheidungsknoten: Nachricht signieren?_**|
|Kurzbeschreibung|Prüfung, ob die Nachricht signiert verschickt werden soll. Dies ist der Fall,|



Bundesamt für Sicherheit in der Informationstechnik 

35 

6 Funktionale Beschreibung 

||wenn<br>**•**<br>die Versandoption „absenderbestätigt“ gesetzt ist oder<br>**•**<br>es sich um eine Bestätigungsnachricht handelt|
|---|---|
|ja|Schritt 31|
|nein|Schritt 32|
|**Schritt 31**|**_Signatur durch DMDA_**|
|Kurzbeschreibung|Der DMDA signiert den Hash-Wert (Nr. 17) in den Metadaten. der<br>Nachricht, dass er diese Nachricht vom Absender unverändert<br>entgegengenommen hat, dieser mit Authentisierungsniveau „hoch“ am De-<br>Mail-Konto angemeldet war und die Versandoption „Absenderbestätigt“<br>gewählt hat.|
|Akteure|Postfachdienst Absender|
|Auslöser|Postfachdienst Absender|
|Vorbedingung|Versandoption „Absenderbestätigte“ Nachricht vom Absender gewählt oder<br>es handelt sich um eine Bestätigungsnachricht|
|Input|Nachricht|
|Ergebnis|Qualifizierte elektronische Signatur über Hash-Wert (Nr. 17) in Element<br><Signatur des DMDA>(Nr. 18) der Metadaten der Nachricht gespeichert.|
|Nachbedingung||
|Ablauf|**•**<br>Hash-Wert aus Metadaten (Nr. 17) der Nachricht mit einer<br>qualifizierten elektronischen Signatur signieren.<br>**•**<br>Signatur in Feld <Signatur des DMDA> (Nr. 18) der Metadaten der<br>Nachricht speichern.|
|Fehlerfälle|FC-01: Signatur konnte nicht erstellt werden.|
|**Schritt 32**|<br>**_Nachrichteninhalt verschlüsseln_**|
|Kurzbeschreibung|Die Nachricht wird ohne Metadaten an den eigenen (sendenden) und den<br>empfangenden DMDA verschlüsselt.|
|Akteure|Postfachdienst Absender|
|Auslöser|Postfachdienst Absender|
|Vorbedingung||
|Input|Nachricht, Verschlüsselungsschlüssel des eigenen und des empfangenden<br>DMDA|
|Ergebnis|Verschlüsselte Nachricht|
|Nachbedingung||
|Ablauf|**•**<br>Nachricht mit Verschlüsselungsschlüssel des Empfänger-DMDA<br>und des Absender-DMDA verschlüsseln|



Bundesamt für Sicherheit in der Informationstechnik 

36 

6 Funktionale Beschreibung 

||**•**<br>Nicht-verschlüsselte Nachricht wird durch verschlüsselte Nachricht<br>ersetzt<br>**•**<br>Löschen der nicht-verschlüsselten Nachricht|
|---|---|
|Fehlerfälle|FC-01: Verschlüsselung nicht durchführbar|
|**Schritt 33**|<br>**_Nachricht an Versanddienst Absender übermitteln_**|
|Kurzbeschreibung|Die (verschlüsselte) Nachricht wird vom Postfachdienst des Absenders zum<br>Versanddienst des Absenders übermittelt.|
|Akteure|Postfachdienst Absender, Versanddienst Absender|
|Auslöser|Postfachdienst Absender|
|Vorbedingung|Sicherer Kommunikationskanal zwischen Postfachdienst und Versanddienst|
|Input|Nachricht|
|Ergebnis|Nachricht zum Versanddienst gesendet|
|Nachbedingung|Anhalten|
|Ablauf|Nachricht wird vom Postfachdienst des Absenders zum Versanddienst des<br>Absenders übermittelt.|
|Fehlerfälle|FC-01: Versanddienst hat Nachricht nicht vollständig angenommen.|
|**Schritt 34**|<br>**_Nachricht als gesendet kennzeichnen_**|
|Kurzbeschreibung|Nach erfolgreicher Übermittlung der Nachricht vom Postfachdienst zum<br>Versanddienst wird sie im Postfach des Senders als „gesendet“<br>gekennzeichnet.|
|Akteure|Postfachdienst Absender|
|Auslöser|Postfachdienst Absender|
|Vorbedingung|Erfolgreiche Übermittlung der Nachricht vom Postfachdienst zum<br>Versanddienst.|
|Input|Nachricht|
|Ergebnis|Nachricht als gesendet gekennzeichnet|
|Nachbedingung|Anhalten|
|Ablauf|Nachricht als „gesendet“kennzeichnen|
|Fehlerfälle||



_Tabelle 4: Schritte zum Versenden von Nachrichten_ 

## **6.3 Transport von Nachrichten durch Versanddienst des Absenders** 

**Schritt 35** _**Nachricht vom Postfachdienst des Absenders entgegennehmen**_ 

Kurzbeschreibung Nachricht wird vom Postfachdienst des Absenders entgegengenommen. 

Bundesamt für Sicherheit in der Informationstechnik 

37 

6 Funktionale Beschreibung 

|Akteure|Versanddienst Absender, Postfachdienst Absender|
|---|---|
|Auslöser|Postfachdienst Absender|
|Vorbedingung|Schritt 33<br>sicherer Kommunikationskanal zwischen Postfachdienst und Versanddienst|
|Input|Nachricht|
|Ergebnis|Nachricht vom Postfachdienst des Absenders entgegennehmen|
|Nachbedingung||
|Ablauf|Nachricht wird entgegengenommen|
|Fehlerfälle|FC-01: Nachricht nicht vollständig übertragen|
|**Schritt 36**|<br>**_Prüfung, ob Versandbestätigung erstellt werden soll_**|
|Kurzbeschreibung|Metadaten der Nachricht auswerten, ob eine Versandbestätigung<br>angefordert wurde. Im Rahmen von automatisierten Weiterleitungen und<br>Nachsendeaufträgen darf keine erneute Versandbestätigung erstellt werden,<br>da eine Versandbestätigung nur vom ursprünglichen Absender angefordert<br>werden soll.|
|Akteure|Versanddienst Absender|
|Auslöser|Versanddienst Absender|
|Vorbedingung||
|Input|Nachricht|
|Ergebnis|Versandbestätigung erstellen / nicht erstellen|
|Nachbedingung||
|Ablauf|**•**<br>Wert für Versandoption „Versandbestätigung“ ermitteln<br>**•**<br>Prüfung, ob Empfänger-Adresse in den Elementen <Empfänger-<br>Adresse(n)> (Nr. ) und <Empfänger-Adressen für den Transport><br>(Nr. ) unterschiedlich sind,<br>**•**<br>dann ist Nachricht ein Nachsendeauftrag oder Weiterleitung und es<br>wird keine Versandbestätigung erstellt|
|Fehlerfall||
|**Schritt 37**|**_Entscheidungsknoten: Versandbestätigung?_**|
|Kurzbeschreibung|Metadaten der Nachricht auswerten, ob eine Versandbestätigung<br>angefordert wurde.<br>Hinweis: Im Rahmen von automatisierten Weiterleitungen (siehe Schritt<br>70) und Nachsendeaufträgen (siehe Schritt 50) darf keine erneute<br>Versandbestätigung erstellt werden, da eine Versandbestätigung nur vom<br>ursprünglichen Absender angefordert werden soll.|
|ja|Schritt 38|



Bundesamt für Sicherheit in der Informationstechnik 

38 

6 Funktionale Beschreibung 

|nein|Schritt 40|
|---|---|
|**Schritt 38**|**_Versandbestätigung erstellen_**|
|Kurzbeschreibung|Vom Versanddienst des Absenders wird eine Versandbestätigung erstellt.|
|Akteure|Versanddienst Absender|
|Auslöser|Versanddienst Absender|
|Vorbedingung||
|Input|Nachricht|
|Ergebnis|Bestätigungsnachricht|
|Nachbedingung||
|Ablauf|**•**<br>Versandbestätigung erzeugen (siehe Abschnitt 5)<br>**•**<br>Bestätigungsnachricht auf Grundlage der Versandbestätigung<br>erstellen<br>**•**<br>Es werden keine Versandoptionen gesetzt, nur falls in der<br>ursprünglichen Nachricht die Versandoption „Persönlich“ gesetzt<br>war, wird auch die Bestätigungsnachricht mit der Versandoption<br>„Persönlich“ versendet.<br>**•**<br>Empfänger-Adresse ist auf die Absender-Adresse bzw. falls<br>angegeben, auf die Antwort-Adresse, der ursprünglichen Nachricht<br>zu setzen<br>**•**<br>Element <Nachrichten-Kennung des Absenders> (Nr. 9) von der<br>ursprünglichen Nachricht in die Bestätigungsnachricht übernehmen.<br>**•**<br>Absender-Adresse ist auf die System-Adresse des DMDA für<br>Versandbestätigungen zu setzen<br>**•**<br>Die Bestätigung ist mit einer qualifizierten elektronischen Signatur<br>zu signieren|
|Fehlerfälle|FC-01: keine Signaturerstellung möglich|
|**Schritt 39**|<br>**_Bestätigungsnachricht an Absender versenden_**|
|Kurzbeschreibung|Eine Bestätigungsnachricht mit der Versandbestätigung wird zum Absender<br>versendet.|
|Akteure|Versanddienst Absender, Postfachdienst Absender|
|Auslöser|Versanddienst Absender|
|Vorbedingung||
|Input|Versandbestätigung|
|Ergebnis|Bestätigungsnachricht versendet|
|Nachbedingung||
|Ablauf|Die Bestätigungsnachricht versenden|



Bundesamt für Sicherheit in der Informationstechnik 

39 

## 6 Funktionale Beschreibung 

|Fehlerfälle|FC-01: Nachricht kann nicht versendet werden|
|---|---|
|**Schritt 40**|**_Nachricht an Versanddienst Empfänger übermitteln_**|
|Kurzbeschreibung|Die Nachricht wird, für Empfänger innerhalb von De-Mail, zum<br>Versanddienst des Empfängers übermittelt.|
|Akteure|Versanddienst Absender, Versanddienst Empfänger|
|Auslöser|Versanddienst Absender|
|Vorbedingung|Sicherer Kanal zwischen Versanddiensten von Absender und Empfänger<br>aufgebaut|
|Input|Transportgesicherte Nachricht|
|Ergebnis|Nachricht zum Versanddienst Empfänger übermittelt|
|Nachbedingung|Anhalten|
|Ablauf|**•**<br>Die Adresse des Versanddienst Empfänger aus Empfänger-Adresse<br>ermitteln<br>**•**<br>Nachricht zum Versanddienst Empfänger übermitteln|
|Fehlerfälle|FC-01: Nachricht vom Versanddienst Empfänger nicht vollständig<br>angenommen|



_Tabelle 5: Schritte zum Transport von Nachrichten durch Versanddienst des Absenders_ 

## **6.4 Transport von Nachrichten durch Versanddienst des Empfängers** 

|**Schritt 41**|**_Nachricht vom Versanddienst des Absenders entgegennehmen_**|
|---|---|
|Kurzbeschreibung|Der Versanddienst des Empfängers nimmt die Nachricht vom<br>Versanddienst des Absenders entgegen.|
|Akteure|Versanddienst Empfänger, Versanddienst Absender|
|Auslöser|Versanddienst Absender|
|Vorbedingung|Sicherer Kanal zwischen Versanddiensten des Absenders und Empfängers<br>aufgebaut|
|Input|Nachricht|
|Ergebnis|Nachricht vom Versanddienst des Empfängers entgegengenommen|
|Nachbedingung||
|Ablauf|**•**<br>Nachricht wird entgegengenommen.<br>**•**<br>Prüfen, ob Nachricht syntaktisch korrekt ist.|
|Fehlerfälle|FC-01: Nachricht nicht vollständig übertragen<br>FC-02: Nachricht enthält syntaktische Fehler<br>Meldungsnachrichten sind auch bei Auftreten syntaktischer Fehler|



Bundesamt für Sicherheit in der Informationstechnik 

40 

6 Funktionale Beschreibung 

||zuzustellen, sofern die folgenden Header syntaktisch korrekt befüllt sind:<br>**•**<br>X-de-mail-sender<br>**•**<br>X-de-mail-chosen-recipient<br>**•**<br>Subject<br>**•**<br>X-de-mail-originator-provider<br>**•**<br>X-de-mail-message-type<br>**•**<br>X-de-mail-actual-recipient<br>Für den Typ der Meldungsnachricht “X-de-mail-notification-type” kann<br>“other” angenommen werden, sofern kein anderer gültiger<br>Meldungsnachrichtentyp angegeben ist.|
|---|---|
|**Schritt 42**|<br>**_Zustellbarkeit prüfen_**|
|Kurzbeschreibung|Der Versanddienst des Empfängers überprüft, ob die Nachricht zustellbar<br>ist:<br>**•**<br>Der Empfänger muss existieren.<br>**•**<br>Bei Nachrichten mit gewählter Versandoption „Persönlich“:<br>**◦**<br>der Empfänger muss sich mit Authentisierungsniveau „hoch“<br>am De-Mail-Konto anmelden können.<br>**•**<br>Bei Nachrichten mit gewählter Versandoption „Abholbestätigung“:<br>**◦**<br>der Empfänger muss sich mit Authentisierungsniveau „hoch“<br>am De-Mail-Konto anmelden können.<br>**•**<br>Das De-Mail-Konto des Empfängers darf nicht vollständig gesperrt<br>sein.|
|Akteure|Versanddienst Empfänger, Account-Dienst Empfänger, Postfachdienst<br>Empfänger|
|Auslöser|Versanddienst Empfänger, Account-Dienst Empfänger|
|Vorbedingung||
|Input|Nachricht|
|Ergebnis|Prüfergebnis: Nachricht ist zustellbar oder nicht|
|Nachbedingung||
|Ablauf|**•**<br>Empfänger-Adresse aus Nachricht ermitteln<br>**•**<br>Anfrage beim Accountmanagement, ob Empfänger existiert<br>**◦**<br>Falls nein: nicht zustellbar<br>**•**<br>Anfrage beim Postfachdienst, ob Nachsendeauftrag aktiv<br>**◦**<br>falls nein, zusätzlich prüfen:<br>**▪**<br>Bei Versandoption „Persönlich“: Anfrage beim Account-|



Bundesamt für Sicherheit in der Informationstechnik 

41 

## 6 Funktionale Beschreibung 

||Dienst, ob Empfänger „persönliche“ Nachrichten abrufen<br>kann<br>**•**<br>Falls nein: nicht zustellbar<br>**•**<br>Anfrage beim Account-Dienst, ob das De-Mail-Konto vollständig<br>gesperrt ist<br>**◦**<br>Falls ja: nicht zustellbar<br>**•**<br>Anfragen auswerten|
|---|---|
|Fehlerfälle|FC-01: Account-Dienst nicht erreichbar<br>FC-02: Postfachdienst nicht erreichbar<br>FC-03: Versanddienst für Empfänger-Adresse nicht zuständig (weil z.B.<br>falscher DMDA)|
|**Schritt 43**|<br>**_Entscheidungsknoten: Zustellbarkeit OK?_**|
|Kurzbeschreibung|Das Ergebnis der Prüfung der Zustellbarkeit wird ausgewertet.<br>**•**<br>ja: bei Ergebnis „OK“<br>**•**<br>nein: bei Ergebnissen: „Empfänger unbekannt“, „Empfänger kann<br>keine Nachrichten mit Versandoption ‚Persönlich’ abrufen“ oder<br>„Empfänger-De-Mail-Konto vollständig gesperrt“|
|ja|Schritt 44|
|nein|Schritt 45|
|**Schritt 44**|**_Nachricht an den Postfachdienst Empfänger übermitteln_**|
|Kurzbeschreibung|Die Nachricht wird vom Versanddienst des Empfängers zum<br>Postfachdienst des Empfängers übermittelt.|
|Akteure|Versanddienst Empfänger, Postfachdienst Empfänger|
|Auslöser|Versanddienst Empfänger|
|Vorbedingung|Sicherer Kommunikationskanal zwischen Versanddienst und<br>Postfachdienst|
|Input|Nachricht|
|Ergebnis|Nachricht an den Postfachdienst des Empfängers übermittelt|
|Nachbedingung|Anhalten|
|Ablauf|Nachricht wird zum Postfachdienst des Empfängers übermittelt|
|Fehlerfälle|FC-01: Nachricht vom Postfachdienst des Empfängers nicht vollständig<br>angenommen.|
|**Schritt 45**|**_Meldungsnachricht an ursprünglichen Absender versenden_**|
|Kurzbeschreibung||
|Akteure|Versanddienst Empfänger|



Bundesamt für Sicherheit in der Informationstechnik 

42 

6 Funktionale Beschreibung 

|Auslöser|Versanddienst Empfänger|
|---|---|
|Vorbedingung||
|Input|Prüfergebnis, (ursprüngliche) Nachricht|
|Ergebnis|Meldungsnachricht an den Absender versendet|
|Nachbedingung|Anhalten|
|Ablauf|**•**<br>Absender-Adresse aus der ursprünglichen Nachricht ermitteln<br>**•**<br>Falls Absender-Adresse eine System-Adresse ist (d.h. die<br>ursprüngliche Nachricht ist i.d.R. eine Meldungs- oder<br>Bestätigungsnachricht), dann<br>**◦**<br>die ursprüngliche Nachricht löschen<br>**◦**<br>Anhalten<br>**•**<br>ansonsten:<br>**◦**<br>Meldungstext muss das Prüfergebnis und die entsprechende<br>Empfänger-Adresse beinhalten und der Meldungstext muss<br>ermöglichen, die ursprüngliche Nachricht zu referenzieren.<br>**◦**<br>Meldungsnachricht erstellen.<br>**◦**<br>Keine Versandoptionen werden gesetzt.<br>**◦**<br>Element <Nachrichten-Kennung des Absenders> (Nr. 9) von der<br>ursprünglichen Nachricht in die Meldungsnachricht<br>übernehmen.<br>**◦**<br>Prüfung, ob ein Element <Weiterleitungs-Absender> (Nr. 20)<br>gesetzt ist.<br>**▪**<br>Falls ja: Empfänger-Adresse ist auf Weiterleitungs-<br>Absender zu setzen.<br>**▪**<br>Falls nein: Empfänger-Adresse ist auf die Absender- bzw.<br>falls angegeben, auf die Antwort-Adresse, der<br>ursprünglichen Nachricht zu setzen.<br>**•**<br>Absender-Adresse ist auf die System-Adresse für<br>Meldungsnachrichten zu setzen.<br>**•**<br>Die Meldungsnachricht wird an den Versanddienst des Absenders<br>übermittelt<br>**•**<br>Ursprüngliche Nachricht, die nicht im Postfach des Empfängers<br>abgelegt werden kann, löschen|
|Fehlerfälle|FC-01: Meldungsnachricht kann nicht versendet werden.|



_Tabelle 6: Schritte zum Transport von Nachrichten durch Versanddienst des Empfängers_ 

Bundesamt für Sicherheit in der Informationstechnik 

43 

## 6 Funktionale Beschreibung 

## **6.5 Empfangen der Nachrichten durch Postfachdienst des Empfängers** 

|**Schritt 46**|**_Nachricht vom Versanddienst Empfänger entgegennehmen_**|
|---|---|
|Kurzbeschreibung|Die vom Versanddienst des Empfängers übermittelte Nachricht wird vom<br>Postfachdienst des Empfängers entgegengenommen.|
|Akteure|Versanddienst Empfänger, Postfachdienst Empfänger|
|Auslöser|Versanddienst Empfänger|
|Vorbedingung|Sicherer Kommunikationskanal zwischen Versanddienst und Postfachdienst<br>des Empfängers|
|Input|Nachricht|
|Ergebnis|Nachricht vom Postfachdienst des Empfängers entgegengenommen|
|Nachbedingung||
|Ablauf|Nachricht wird vom Postfachdienst Empfänger entgegengenommen.|
|Fehlerfälle|FC-01: Nachricht nicht vollständig übertragen.|
|**Schritt 47**|<br>**_Von Kopie der Nachrichten Domänen-Verschlüsselung entfernen_**|
|Kurzbeschreibung|Der Postfachdienst des Empfängers erstellt eine Kopie der empfangenen<br>Nachricht und entfernt von dieser die Domänen-Verschlüsselung.|
|Akteure|Postfachdienst Empfänger|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung||
|Input|Nachricht|
|Ergebnis|Entschlüsselte Nachrichten-Kopie|
|Nachbedingung|Spätestens nach Beendigung / Abbruch der Schritte zum „Empfang von<br>Nachrichten durch den Postfachdienst des Empfängers“ muss die<br>entschlüsselte Nachrichten-Kopie gelöscht werden.|
|Ablauf|Kopie der verschlüsselten Nachrichten erstellen und diese entschlüsseln.<br>Hinweis: Im weiteren Verlauf wird bis zur Ablage der Nachricht in das<br>Postfach des Empfänger mit der entschlüsselten Kopie weitergearbeitet<br>(sofern nicht anders angegeben).|
|Fehlerfälle|FC-01: Entschlüsselung konnte nicht durchgeführt werden.|
|**Schritt 48**|<br>**_Integritätssicherung prüfen_**|
|Kurzbeschreibung|Die Integritätsicherung der Nachricht wird geprüft.<br>Bei normalen Nachrichten handelt es sich um einen Hash-Wert.<br>Bei Nachrichten mit der Versandoption „Absenderbestätigt“und|



Bundesamt für Sicherheit in der Informationstechnik 

44 

6 Funktionale Beschreibung 

||Bestätigungsnachrichten handelt es sich um eine Signatur.|
|---|---|
|Akteure|Postfachdienst Empfänger|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung||
|Input|Nachricht, Signatur, Zertifikat (von DMDA des Absender)|
|Ergebnis|Prüfergebnis|
|Nachbedingung||
|Ablauf|**•**<br>Berechnung des Hash-Wertes und Vergleich mit dem in den<br>Metadaten der Nachricht gespeicherten Hash (Metadaten Nr. 17).<br>**•**<br>Bei Signatur durch DMDA (Metadaten Nr. 17)<br>**◦**<br>Mathematische Prüfung der Signatur mit Signaturprüfschlüssel<br>aus Zertifikat<br>**◦**<br>Prüfung der Gültigkeit des Zertifikates<br>**◦**<br>Prüfung Zertifikatskette<br>**◦**<br>Prüfung Status des Zertifikates<br>**•**<br>Aggregation der Prüfergebnisse|
|Fehlerfälle|FC-01: Integritätsverletzung<br>FC-02: Zertifikat ungültig<br>FC-03: Der Status des Zertifikates konnte nicht online geprüft werden<br>FC-04: Keine Signatur bei einer Nachricht mit Versandoption<br>„Absenderbestätigt“|
|**Schritt 49**|**_Entscheidungsknoten: Nachsendeauftrag aktiv?_**|
|Kurzbeschreibung|Überprüfung, ob vom Empfänger ein Nachsendeauftrag1(an eine andere<br>De-Mail-Adresse) verlangt wurde (siehe Funktion 3 in Abschnitt 7).|
|ja|Schritt 50|
|nein|Schritt 54|
|**Schritt 50**|**_Nachricht als Nachsendeauftrag aufbereiten_**|
|Kurzbeschreibung|Der Empfänger der Nachricht wird an die im Nachsendeauftrag angegebene<br>Adresse umgeschrieben.|
|Akteure|Postfachdienst Empfänger|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung|Nachsendeauftrag ist aktiv|



- 1 Von einem Nachsendeauftrag ist eine Weiterleitung (siehe Schritt 71) zu unterscheiden. Bei einem Nachsendeauftrag werden Eingangsbestätigungen erst durch den Postfachdienst ausgestellt, an den der Nachsendeauftrag gerichtet war. 

Bundesamt für Sicherheit in der Informationstechnik 

45 

6 Funktionale Beschreibung 

|Input|Nachricht, Nachsendeauftrag|
|---|---|
|Ergebnis|Nachricht mit geänderter Empfänger-Adresse|
|Nachbedingung||
|Ablauf|**•**<br>Prüfung auf Nachrichten-Schleife (_forwarding loop_)<br>**•**<br>Empfänger-Adresse aus Nachsendeauftrag ermitteln<br>**•**<br>Empfänger-Adresse aus Nachsendeauftrag in Element <Empfänger-<br>Adressen für den Transport>(Feld 19) schreiben.|
|Fehlerfälle|FC-01: Nachrichten-Schleife entdeckt|
|**Schritt 51**|**_Nachrichteninhalt an neuen Empfänger verschlüsseln_**|
|Kurzbeschreibung|Die Nachricht wird ohne Metadaten an den eigenen und den neuen<br>empfangenden DMDA verschlüsselt (s. a. Schritt 32).|
|Akteure|Postfachdienst Empfänger|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung||
|Input|Nachricht, Verschlüsselungsschlüssel des eigenen und des neuen<br>empfangenden DMDA|
|Ergebnis|Verschlüsselte Nachricht|
|Nachbedingung||
|Ablauf|Nachricht mit Verschlüsselungsschlüssel des eigenen DMDA und des neuen<br>Empfänger-DMDA verschlüsseln.|
|Fehlerfälle|FC-01: Verschlüsselung nicht durchführbar|
|**Schritt 52**|<br>**_Nachrichten-Kopie ohne Domänen-Verschlüsselung löschen_**|
|Kurzbeschreibung|Der Postfachdienst löscht die entschlüsselte Kopie der Nachricht.|
|Akteure|Postfachdienst Empfänger|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung||
|Input|Nachricht ohne Domänen-Verschlüsselung|
|Ergebnis|Entschlüsselte Nachricht ist gelöscht|
|Nachbedingung||
|Ablauf|Entschlüsselte Nachrichten löschen|
|Fehlerfälle||
|**Schritt 53**|**_Nachricht an neuen Empfänger versenden_**|
|Kurzbeschreibung|Die Nachricht wird über eigenen Versanddienst zum neuen Empfänger<br>versendet.|



Bundesamt für Sicherheit in der Informationstechnik 

46 

6 Funktionale Beschreibung 

|Akteure|Postfachdienst Empfänger, Versanddienst Empfänger|
|---|---|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung|Sicherer Kommunikationskanal zwischen Postfachdienst Empfänger und<br>Versanddienst Empfänger|
|Input|Nachricht|
|Ergebnis|Nachricht an Versanddienst Empfänger versendet|
|Nachbedingung|**•**<br>Aufgrund des Nachsendeauftrags darf der Versanddienst keine<br>Versandbestätigung ausstellen.<br>**•**<br>Anhalten|
|Ablauf|Nachricht an den neuen Empfänger ohne weitere Änderungen in den<br>Metadaten versenden<br>Hinweis: Eine ggf. angeforderte Versandbestätigung des ursprünglichen<br>Absenders wird an dieser Stelle nicht ausgestellt.|
|Fehlerfälle|FC-01: Versanddienst hat Nachricht nicht vollständig angenommen.|
|**Schritt 54**|<br>**_Auf Schadsoftware prüfen_**|
|Kurzbeschreibung|Nachricht wird auf Schadsoftware geprüft.|
|Akteure|Postfachdienst Empfänger, Schadsoftware-Dienst Empfänger|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung||
|Input|Nachricht|
|Ergebnis|Nachricht auf Schadsoftware geprüft|
|Nachbedingung||
|Ablauf|Wenn Nachricht nicht Ende-zu-Ende-verschlüsselt, Nachricht an<br>Schadsoftware-Dienst übergeben (s. a. Funktion 2, Abschnitt 7)|
|Fehlerfälle|FC-01: Schadsoftware-Prüfung konnte nicht durchgeführt werden.<br>FC-02: Nachricht für Empfänger verschlüsselt, nicht prüfbar.|
|**Schritt 55**|<br>**_Entscheidungsknoten: Schadsoftware-Prüfung OK?_**|
|Kurzbeschreibung|Ergebnis der Schadsoftware-Prüfung auswerten|
|ja|Schritt 58|
|nein|Schritt 56|
|**Schritt 56**|**_Meldungs-/Bestätigungnachricht über gefundene Schadsoftware_**<br>**_versenden_**|
|Kurzbeschreibung|Der Postfachdienst versendet eine Meldungsnachricht über gefundene<br>Schadsoftware an den Absender und Empfänger. Bei Nachrichten, die eine<br>Versand-und/oder Eingangsbestätigung angefordert haben, wird anstelle|



Bundesamt für Sicherheit in der Informationstechnik 

47 

## 6 Funktionale Beschreibung 

||der einfachen Meldungsnachricht eine Schadsoftware-<br>Bestätigungsnachricht an den Absender und Empfänger gesendet.<br>In der Schadsoftware-Meldungs- oder Bestätigungsnachricht wird zum<br>Ausdruck gebracht, dass eine Kenntnisnahme aufgrund der enthaltenen<br>Schadsoftware ggf. nicht möglich ist.|
|---|---|
|Akteure|Postfachdienst Empfänger|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung||
|Input|Nachricht, Ergebnis|
|Ergebnis|Meldung und/oder Bestätigung über gefundene Schadsoftware erstellt und<br>versendet|
|Nachbedingung||
|Ablauf|**•**<br>Prüfung, ob Nachricht eine Versand-, Eingangs- und/oder<br>Abholbestätigung erfordert<br>**•**<br>Falls nein:<br>**◦**<br>Eine Meldungsnachricht an den Absender (oder falls angegeben<br>an dessen Antwort-Adresse) und den Empfänger der<br>ursprünglichen Nachricht erzeugen, dass die empfangene<br>Nachricht Schadsoftware enthält.<br>**◦**<br>Element <Nachrichten-Kennung des Absenders> (Nr. 9) von der<br>ursprünglichen Nachricht in die Meldungsnachricht übernehmen<br>**◦**<br>Meldung versenden/darstellen<br>**•**<br>Falls ja:<br>**◦**<br>Schadsoftware-Bestätigung erzeugen mit dem expliziten<br>Hinweis, dass für die betreffende Nachricht eine Versand-,<br>Eingangs-und/oder Abholbestätigung angefordert worden ist.<br>**◦**<br>Schadsoftware-Bestätigung um den Hinweis ergänzen, dass<br>aufgrund der gefundenen Schadsoftware nicht von einer<br>Kenntnisnahme der Nachricht durch den Empfänger<br>ausgegangen werden kann.<br>**◦**<br>Die Bestätigung ist mit einer qualifizierten elektronischen<br>Signatur zu signieren.<br>**◦**<br>Bestätigungsnachricht auf Grundlage der Schadsoftware-<br>Bestätigung erstellen<br>**◦**<br>Keine Versandoptionen werden gesetzt<br>**◦**<br>Element <Nachrichten-Kennung des Absenders> (Nr. 9) von der<br>ursprünglichen Nachricht in die Schadsoftware-<br>Bestätigungsnachricht übernehmen.|



Bundesamt für Sicherheit in der Informationstechnik 

48 

6 Funktionale Beschreibung 

||**◦**<br>Empfänger-Adresse ist auf den Absender der ursprünglichen<br>Nachricht zu setzen (mit Absender- oder falls angegeben mit<br>seiner Antwort-Adresse)<br>**◦**<br>In Kopie (Carbon Copy, CC) ist der Empfänger der<br>ursprünglichen Nachricht zu setzen<br>**◦**<br>Absender-Adresse ist auf die System-Adresse des DMDA für<br>Schadsoftware-Warnung zu setzen<br>**•**<br>Die Bestätigungsnachricht versenden|
|---|---|
|Fehlerfälle|FC-01: Meldung konnte nicht abgesendet/dargestellt werden.<br>FC-02: Signatur konnte nicht erstellt werden.<br>FC-03: Bestätigungsnachricht konnte nicht versendet werden.|
|**Schritt 57**|<br>**_Nachricht mit Schadsoftware löschen_**|
|Kurzbeschreibung|Der Postfachdienst löscht die Nachricht mit der gefundenen Schadsoftware.|
|Akteure|Postfachdienst Empfänger|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung||
|Input|Nachricht mit Schadsoftware|
|Ergebnis|Nachricht ist gelöscht|
|Nachbedingung|Anhalten|
|Ablauf|Der Postfachdienst löscht die Nachricht mit der gefundenen Schadsoftware.|
|Fehlerfälle||
|**Schritt 58**|**_Entscheidungsknoten: Versandoption „Persönlich“ oder_**<br>**_Abholbestätigung?_**|
|Kurzbeschreibung|Metadaten der Nachricht auswerten, ob die Versandoption „Persönlich“<br>oder „Abholbestätigung“gewählt wurde.|
|ja|Schritt 59|
|nein|Schritt 60|
|**Schritt 59**|**_Meldung an Empfänger versenden_**|
|Kurzbeschreibung|Der Postfachdienst des Empfängers kann eine Meldung mit der Information<br>für den Empfänger erstellen, dass für ihn eine (andere) Nachricht mit der<br>Versandoption „Persönlich“ oder „Abholbestätigung“ vorliegt, die zum<br>Abruf und zum Lesen das Authentisierungsniveau „hoch“ erfordert. Die<br>Abholbestätigung hat die höhere Priorität, wenn beide Versandoptionen<br>gewählt wurden.|
|Akteure|Postfachdienst Empfänger|
|Auslöser|Postfachdienst Empfänger|



Bundesamt für Sicherheit in der Informationstechnik 

49 

6 Funktionale Beschreibung 

|Vorbedingung||
|---|---|
|Input||
|Ergebnis|Meldung an den Empfänger versendet|
|Nachbedingung|Anhalten|
|Ablauf|**•**<br>Meldung erstellen.<br>**•**<br>Informationstext einfügen, dass eine Nachricht vorliegt und mit dem<br>Authentisierungsniveau „hoch“ abgerufen werden muss. Bei<br>Nachrichten, für die eine Versand- und/oder eine<br>Eingangsbestätigung angefordert worden ist, ist explizit darauf<br>hinzuweisen.<br>**•**<br>Die Meldung an den Empfänger versenden.|
|Fehlerfälle|FC-01: Meldung kann nicht versendet werden.|
|**Schritt 60**|<br>**_Entscheidungsknoten: Spezieller Nachrichten-Typ?_**|
|Kurzbeschreibung|Feststellen, ob Nachricht ein spezieller Nachrichten-Typ (Metadaten Nr. 16)<br>ist, um Validitätsprüfungen durchzuführen.<br>Hinweis: Dieser Schritt, Schritt 61 und Schritt 62 sind optional und können<br>–müssen jedoch nicht–vom DMDA angeboten werden.|
|ja|Schritt 61|
|nein|Schritt 63|
|**Schritt 61**|**_Validitätsprüfung für spezielle Nachrichten-Typen durchführen_**|
|Kurzbeschreibung|Der Postfachdienst führt für spezielle Nachrichten-Typen2eine<br>Validitätsprüfung durch. Der Nachrichten-Typ ist in den Metadaten (Nr. 16)<br>einer Nachricht definiert.|
|Akteure|Postfachdienst Empfänger|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung|Spezieller Nachrichten-Typ|
|Input|Nachricht|
|Ergebnis|Prüfprotokoll der Validitätsprüfung|
|Nachbedingung||
|Ablauf|**•**<br>Bei Bestätigungsnachrichten:<br>**◦**<br>Prüfung, ob Nachrichten-spezifische Absender-Adresse des<br>DMDA für Versand-, Eingangs- und Abholbestätigung<br>verwendet wurde.<br>**◦**<br>Prüfung, ob Aussteller der Bestätigung auch zum Absender der|



2 Andere De-Mail-Dienste können neue Nachrichten-Typen definieren und damit auch neue spezifische Validitätsprüfungen für diesen Schritt erfordern. 

Bundesamt für Sicherheit in der Informationstechnik 

50 

6 Funktionale Beschreibung 

||Nachricht passt.<br>**•**<br>Bei Meldungsnachrichten:<br>**◦**<br>Prüfung, ob Nachrichten-spezifische Absender-Adresse<br>verwendet wurde.<br>**◦**<br>Prüfung, ob Aussteller der Meldung auch zum Absender der<br>Nachricht passt.|
|---|---|
|Fehlerfälle||
|**Schritt 62**|**_Ergebnis der Prüfung als Meldung versenden_**|
|Kurzbeschreibung|Das Ergebnis (Prüfprotokoll) der Validitätsprüfung wird als Meldung an<br>den Empfänger versendet.|
|Akteure|Postfachdienst Empfänger|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung||
|Input|Nachricht, Prüfprotokoll der Validitätsprüfung|
|Ergebnis|Prüfprotokoll als Meldung an Empfänger versendet|
|Nachbedingung||
|Ablauf|Aus dem Protokoll der Validitätsprüfung eine Meldung erzeugen.|
|Fehlerfälle|FC-01: Die Meldung konnte nicht versendet werden.|
|**Schritt 63**|<br>**_Nachricht signiert und nicht verschlüsselt?_**|
|Kurzbeschreibung|Feststellen, ob die Nachricht oder Nachrichtenanhänge durch den Absender<br>qualifiziert signiert wurden und nicht verschlüsselt sind.<br>Hinweis:Dieser Schritt, Schritt 64 und Schritt 65 sind optional und können<br>aber vom DMDA angeboten werden.|
|ja|Schritt 64|
|nein|Schritt 66|
|**Schritt 64**|**_Signatur- und Zertifikatsprüfung für Anhänge durchführen_**|
|Kurzbeschreibung|Der Postfachdienst führt eine Prüfung der qualifizierten Signatur(en) sowie<br>des Zertifikates für Nachrichtenanhänge durch.|
|Akteure|Postfachdienst Empfänger|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung|Nachricht qualifiziert signiert und nicht verschlüsselt|
|Input|Nachricht|
|Ergebnis|Prüfprotokoll der Signatur-und Zertifikatsprüfung|
|Nachbedingung||



Bundesamt für Sicherheit in der Informationstechnik 

51 

## 6 Funktionale Beschreibung 

|Ablauf|**•**<br>Mathematische Prüfung der qualifizierten Signatur(en) mit<br>Signaturprüfschlüssel aus Zertifikat<br>**•**<br>Prüfung der Gültigkeit des Zertifikates<br>**•**<br>Prüfung Zertifikatskette<br>**•**<br>Prüfung Status des Zertifikates<br>**•**<br>Prüfergebnisse zusammenfassen in Prüfprotokoll|
|---|---|
|Fehlerfälle|FC-01: Integritätsverletzung<br>FC-02: Zertifikat ungültig<br>FC-03: Der Status des Zertifikates konnte nicht online geprüft werden|
|**Schritt 65**|<br>**_Ergebnis der Prüfung als Meldung versenden_**|
|Kurzbeschreibung|Das Ergebnis (Prüfprotokoll) der Signatur- und Zertifikatsprüfung wird als<br>Meldung an den Empfänger versendet.|
|Akteure|Postfachdienst Empfänger|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung||
|Input|Nachricht, Prüfprotokoll|
|Ergebnis|Prüfprotokoll als Meldung versendet.|
|Nachbedingung||
|Ablauf|Aus dem Protokoll der Signatur- und Zertifikatsprüfung eine Meldung<br>erzeugen.|
|Fehlerfälle|FC-01: Meldung kann nicht versendet werden.|
|**Schritt 66**|<br>**_Nachricht mit Domänen-Sicherung ins Postfach des Empfängers ablegen_**|
|Kurzbeschreibung|Der Postfachdienst des Empfängers legt die empfangene Nachricht<br>verschlüsselt ins Postfach des Empfängers ab.<br>Hinweis: Ab diesem Schritt ist die Nachricht im Eingangsbereich des<br>Empfängers.|
|Akteure|Postfachdienst Empfänger|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung||
|Input|Nachricht mit Domänen-Sicherung|
|Ergebnis|Nachricht im Postfach des Empfängers abgelegt|
|Nachbedingung||
|Ablauf|**•**<br>Nachricht mit der nicht entfernten Domänen-Verschlüsselung im<br>Postfach des Empfängers ablegen|



Bundesamt für Sicherheit in der Informationstechnik 

52 

6 Funktionale Beschreibung 

||**•**<br>Aufruf Funktion 11 (siehe Abschnitt 7) zur automatischen<br>Sortierung von Nachrichten<br>**•**<br>Optional: Meldung versenden, dass eine neue Nachricht eingetroffen<br>ist3|
|---|---|
|Fehlerfälle|FC-01: Nachricht kann nicht ins Postfach des Empfängers abgelegt werden|
|**Schritt 67**|<br>**_Prüfung, ob Eingangsbestätigung erstellt werden soll_**|
|Kurzbeschreibung|Metadaten der Nachricht auswerten, ob eine Eingangsbestätigung<br>angefordert wurde. Im Rahmen von automatisierten Weiterleitungen (siehe<br>Schritt 70) darf keine erneute Eingangsbestätigung erstellt werden, da eine<br>Eingangsbestätigung nur vom ursprünglichen Empfänger verschickt werden<br>soll.|
|Akteure|Postfachdienst Empfänger|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung||
|Input|Nachricht|
|Ergebnis|Eingangsbestätigung erstellen / nicht erstellen|
|Nachbedingung||
|Ablauf|**•**<br>Wert für Versandoption „Eingangsbestätigung“ ermitteln<br>**•**<br>Prüfung, ob das Elemente <Weiterleitungs-Absender)> (Nr. ) und<br>gesetzt ist, dann handelt es sich um eine weitergeleitete Nachricht<br>und es wird keine Eingangsbestätigung erstellen|
|Fehlerfälle||
|**Schritt 68**|**_Entscheidungsknoten: Eingangsbestätigung?_**|
|Kurzbeschreibung|Metadaten der Nachricht auswerten, ob eine Eingangsbestätigung<br>gewünscht wird.|
|Ja|Schritt 69|
|Nein|Schritt 71|
|**Schritt 69**|**_Eingangsbestätigung erstellen_**|
|Kurzbeschreibung|Vom Postfachdienst des Empfängers wird eine Eingangsbestätigung erstellt.|
|Akteure|Postfachdienst Empfänger|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung||
|Input|Nachricht ohne Domänen-Verschlüsselung|
|Ergebnis|Eingangsbestätigung|



3 Diese Meldung kann bspw. genutzt werden, um den Nutzer auf seinen Wunsch hin über den Eingang neuer Nachrichten mittels SMS zu informieren. 

Bundesamt für Sicherheit in der Informationstechnik 

53 

6 Funktionale Beschreibung 

|Nachbedingung||
|---|---|
|Ablauf|**•**<br>Berechnung des Hash-Wertes und Vergleich mit dem in den<br>Metadaten der Nachricht gespeicherten (Metadatum Nr. 17)4.<br>**•**<br>Falls Vergleich der Hash-Werte OK:<br>**◦**<br>Eingangsbestätigung erstellen (siehe Abschnitt 5.2).<br>**◦**<br>Die Bestätigung ist mit einer qualifizierten elektronischen<br>Signatur zu signieren.<br>**•**<br>Falls Vergleich der Hash-Werte nicht OK:<br>**◦**<br>Es ist eine Meldung an den Empfänger und Absender der<br>Nachricht zu übermitteln.<br>**◦**<br>Die Meldung ist mit einer qualifizierten elektronischen Signatur<br>zu signieren.<br>**◦**<br>Bestätigungsnachricht auf Grundlage der Eingangsbestätigung<br>erstellen.<br>**•**<br>Es werden keine Versandoptionen gesetzt, nur falls in der<br>ursprünglichen Nachricht die Versandoption „Persönlich“ gesetzt<br>war, wird auch die Bestätigungsnachricht mit der Versandoption<br>„Persönlich“ versendet.<br>**•**<br>Element <Nachrichten-Kennung des Absenders> (Nr. 9) von der<br>ursprünglichen Nachricht in die Bestätigungsnachricht übernehmen.<br>**•**<br>Die Empfänger-Adresse ist auf die Absender- bzw. falls angegeben,<br>auf die Antwort-Adresse, der ursprünglichen Nachricht zu setzen.<br>**•**<br>In Kopie (Carbon Copy, CC) ist der Empfänger der ursprünglichen<br>Nachricht zu setzen.<br>**•**<br>Absender-Adresse ist auf die System-Adresse des DMDA für<br>Eingangsbestätigungen zu setzen.|
|Fehlerfälle|FC-01: Berechneter Hash-Wert stimmt nicht mit dem in den Metadaten<br>gespeicherten Hash-Wert überein.<br>FC-02: Keine Signaturerstellung möglich.|
|**Schritt 70**|<br>**_Bestätigungsnachricht an Absender und Empfänger versenden_**|
|Kurzbeschreibung|Die Bestätigungsnachricht wird an den Absender und den Empfänger der<br>Nachricht versendet.|
|Akteure|Postfachdienst Empfänger|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung||



4 Eine Prüfung des Hash-Wertes erfolgt auch bereits in Schritt 48. Das Ergebnis dieser Berechnung kann verwendet werden. 

Bundesamt für Sicherheit in der Informationstechnik 

54 

6 Funktionale Beschreibung 

|Input|Eingangsbestätigung|
|---|---|
|Ergebnis|Bestätigungsnachricht versendet|
|Nachbedingung||
|Ablauf|Die Bestätigungsnachricht versenden.|
|Fehlerfälle|FC-01: Nachricht kann nicht versendet werden.|
|**Schritt 71**|**_Entscheidungsknoten: Weiterleitung aktiv?_**|
|Kurzbeschreibung|Überprüfung, ob vom Empfänger eine automatische Weiterleitung5aktiviert<br>wurde (siehe Funktion 8 in Abschnitt 7).|
|Ja|Schritt 72|
|Nein|Schritt 75|
|**Schritt 72**|**_Nachricht zur Weiterleitung aufbereiten_**|
|Kurzbeschreibung|Der Empfänger der Nachricht wird an die im Weiterleitungsauftrag<br>angegebene Adresse umgeschrieben.|
|Akteure|Postfachdienst Empfänger|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung|Weiterleitung ist aktiv|
|Input|Nachricht, Weiterleitungsauftrag|
|Ergebnis|Nachricht mit geänderter Empfänger-Adresse|
|Nachbedingung||
|Ablauf|**•**<br>Prüfung auf Nachrichten-Schleife (forwarding loop).<br>**◦**<br>Wird eine Nachrichtenschleife festgestellt, wird die Nachricht<br>nicht weitergeleitet.<br>**•**<br>Empfänger-Adresse aus Weiterleitungsauftrag in Element<br><Empfänger-Adressen für den Transport> (Nr. 19) schreiben.<br>**•**<br>In Element <Weiterleitungs-Absender> (Nr. 20) die aktuelle De-<br>Mail-Adresse des Empfängers schreiben.<br>Hinweis: Alle anderen Metadaten bleiben erhalten. Insbesondere erfolgt<br>keine erneute Integritätssicherung.|
|Fehlerfälle|FC-01: Nachrichten-Schleife entdeckt.|
|**Schritt 73**|**_Nachrichteninhalt an neuen Empfänger verschlüsseln_**|
|Kurzbeschreibung|Die Nachricht wird ohne Metadaten an den neuen Empfänger-DMDA<br>verschlüsselt (s. a. Schritt 32).|
|Akteure|Postfachdienst Empfänger|
|Auslöser|Postfachdienst Empfänger|



5 Weiterleitungen sind von Nachsendeaufträgen zu unterscheiden (siehe 6.5). 

Bundesamt für Sicherheit in der Informationstechnik 

55 

6 Funktionale Beschreibung 

|Vorbedingung||
|---|---|
|Input|Nachricht, Verschlüsselungsschlüssel des neuen Empfänger-DMDA|
|Ergebnis|Verschlüsselte Nachricht|
|Nachbedingung||
|Ablauf|Nachricht mit Verschlüsselungsschlüssel des eigenen DMDA und des neuen<br>Empfänger-DMDA verschlüsseln|
|Fehlerfälle|FC-01: Verschlüsselung nicht durchführbar|
|**Schritt 74**|<br>**_Nachricht an neuen Empfänger versenden_**|
|Kurzbeschreibung|Die Nachricht wird über eigenen Versanddienst an neuen Empfänger<br>versendet.|
|Akteure|Postfachdienst Empfänger, Versanddienst Empfänger|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung|Sicherer Kommunikationskanal zwischen Postfachdienst Empfänger und<br>Versanddienst Empfänger aufgebaut|
|Input|Nachricht|
|Ergebnis|Nachricht an Versanddienst Empfänger versendet|
|Nachbedingung|Aufgrund der Weiterleitung darf der Versanddienst keine neue<br>Versandbestätigung ausstellen.|
|Ablauf|Nachricht an den neuen Empfänger versenden.|
|Fehlerfälle|FC-01: Versanddienst hat Nachricht nicht vollständig angenommen.|
|**Schritt 75**|<br>**_Nachrichten-Kopie ohne Domänen-Verschlüsselung löschen_**|
|Kurzbeschreibung|Der Postfachdienst löscht die entschlüsselte Kopie der Nachricht.|
|Akteure|Postfachdienst Empfänger|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung||
|Input|Nachricht ohne Domänen-Verschlüsselung|
|Ergebnis|Entschlüsselte Nachricht ist gelöscht|
|Nachbedingung|Anhalten|
|Ablauf|Entschlüsselte Nachrichten löschen.|
|Fehlerfälle||



_Tabelle 7: Schritte zum Empfangen der Nachrichten_ 

Bundesamt für Sicherheit in der Informationstechnik 

56 

6 Funktionale Beschreibung 

## **6.6 Abrufen der Nachrichten durch Empfänger** 

|**Schritt 76**|**_Empfänger greift auf Postfachdienst zu_**|
|---|---|
|Kurzbeschreibung|Der Empfänger greift auf den Postfachdienst zu, um eingegangene<br>Nachrichten abzurufen.|
|Akteure|Empfänger, Postfachdienst Empfänger|
|Auslöser|Empfänger|
|Vorbedingung|Empfänger an seinem De-Mail-Konto angemeldet<br>Sicherer Kommunikationskanal aufgebaut|
|Input||
|Ergebnis|Postfachdienst geöffnet|
|Nachbedingung||
|Ablauf|-<br>Autorisierung des Empfängers prüfen.|
|Fehlerfälle|FC-01: Nutzer nicht am De-Mail-Konto angemeldet.<br>FC-02: Empfänger nicht autorisiert, Nachrichten abzurufen.|
|**Schritt 77**|<br>**_Aktuelles Authentisierungsniveau des Empfängers ermitteln_**|
|Kurzbeschreibung|Das aktuelle Authentisierungsniveau des Empfängers wird ermittelt.|
|Akteure|Postfachdienst Empfänger, Account-Dienst Empfänger|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung||
|Input|Nutzer-Kennung des De-Mail-Kontos|
|Ergebnis|Aktuelles Authentisierungsniveau|
|Nachbedingung||
|Ablauf|De-Mail-Konto ermitteln.<br>Anfrage an Account-Dienst, welches aktuelle Authentisierungsniveau der<br>Empfänger besitzt.|
|Fehlerfälle|FC-01: Account-Dienst nicht erreichbar.|
|**Schritt 78**|**_Entscheidungsknoten: Aktuelles Authentisierungsniveau „hoch“_**|
|Kurzbeschreibung|Prüfen, ob das aktuelle Authentisierungsniveau des Empfängers „hoch“ist.|
|ja|Schritt 79|
|nein|Schritt 80|
|**Schritt 79**|**_Alle Nachrichten zum Abruf anbieten_**|
|Kurzbeschreibung|Alle Nachrichten werden zum Abruf angeboten.|



Bundesamt für Sicherheit in der Informationstechnik 

57 

## 6 Funktionale Beschreibung 

|Akteure|Postfachdienst Empfänger|
|---|---|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung||
|Input|Liste aller Nachrichten|
|Ergebnis|Alle vorhandenen Nachrichten aufgelistet.|
|Nachbedingung|Schritt 81|
|Ablauf|Nachrichten auflisten|
|Fehlerfälle||
|**Schritt 80**|**_Nur Nachrichten mit Authentisierungsniveau-Empfänger < „hoch“ zum_**<br>**_Abruf anbieten_**|
|Kurzbeschreibung|Nur Nachrichten, die mit Authentisierungsniveau “normal“ gelesen werden<br>dürfen, werden zum Abruf angeboten (d.h. keine Nachrichten mit der<br>Versandoption „Persönlich“und „Abholbestätigung“).|
|Akteure|Postfachdienst Empfänger|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung||
|Input|Liste aller Nachrichten|
|Ergebnis|Alle vorhandenen Nachrichten mit Authentisierungsniveau-Empfänger <<br>„hoch“aufgelistet|
|Nachbedingung||
|Ablauf|**•**<br>Nur Nachrichten anzeigen, für die die Versandoption „Persönlich“<br>und Abholbestätigung“ nicht gewählt wurden-<br>**•**<br>Falls Nachrichten vorhanden sind, die nur mit<br>Authentifizierungsniveau „hoch“ einsehbar sind, wird mit einer<br>Meldung auf diese Tatsache hingewiesen.|
|Fehlerfälle||
|**Schritt 81**|**_Nachrichten auswählen_**|
|Kurzbeschreibung|Der Empfänger wählt eine oder mehrere Nachrichten zum Abruf aus.|
|Akteure|Empfänger, Postfachdienst Empfänger|
|Auslöser|Empfänger|
|Vorbedingung|Liste von auswählbaren Nachrichten|
|Input|Nachrichtenliste|
|Ergebnis|Ausgewählte Nachrichten|
|Nachbedingung||



Bundesamt für Sicherheit in der Informationstechnik 

58 

6 Funktionale Beschreibung 

|Ablauf|Empfänger wählt Nachrichten aus Nachrichtenliste aus.|
|---|---|
|Fehlerfälle||
|**Schritt 82**|**_Nachrichteninhalt entschlüsseln_**|
|Kurzbeschreibung|Zum Abruf oder zum Lesen der Nachrichten entschlüsselt der<br>Postfachdienst die Nachrichten (s. a. Schritt 47).|
|Akteure|Postfachdienst Empfänger|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung||
|Input|Nachricht(en), Entschlüsselungsschlüssel|
|Ergebnis|Entschlüsselte Nachrichten-Kopie|
|Nachbedingung||
|Ablauf|**•**<br>Ursprünglich verschlüsselte Nachrichten verbleiben in Postfach des<br>Empfängers.<br>**•**<br>Kopie der verschlüsselten Nachrichten erstellen und diese<br>entschlüsseln.<br>Hinweis: Im weiteren Verlauf wird bis zum vollständigen Abruf der<br>Nachrichten durch den Empfänger mit den entschlüsselten Kopien<br>weitergearbeitet (sofern nicht anders angegeben).|
|Fehlerfälle|FC-01: Entschlüsselung konnte nicht durchgeführt werden.|
|**Schritt 83**|<br>**_Integritätssicherung prüfen_**|
|Kurzbeschreibung|Eine durch den Postfachdienst des Absenders angebrachte<br>Integritätssicherung (Hash-Wert und – sofern Versandoption<br>„Absenderbestätigt“ gewählt – die Signatur des DMDA) wird vom<br>Postfachdienst des Empfängers geprüft.|
|Akteure|Postfachdienst Empfänger|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung||
|Input|Nachricht, Signatur, Zertifikat (DMDA Absender)|
|Ergebnis|Prüfergebnis|
|Nachbedingung||
|Ablauf|**•**<br>Berechnung des Hash-Wertes und Vergleich mit dem in den<br>Metadaten der Nachricht gespeicherten Hash-Wertes (Metadatum<br>Nr. 17).<br>**•**<br>Bei Signatur durch DMDA (Metadatum Nr. 18)<br>**◦**<br>Mathematische Prüfung der Signatur mit Signaturprüfschlüssel<br>aus Zertifikat|



Bundesamt für Sicherheit in der Informationstechnik 

59 

6 Funktionale Beschreibung 

||**◦**<br>Prüfung der Gültigkeit des Zertifikates (sofern vorhanden)<br>**◦**<br>Prüfung Zertifikatskette (sofern vorhanden)<br>**◦**<br>Prüfung Status des Zertifikates (sofern vorhanden)<br>**•**<br>Aggregation der Prüfergebnisse<br>Hinweis: Eine Prüfung der Integritätssicherung erfolgte bereits bei der<br>Annahme der Nachricht durch den Versanddienst des Empfängers in Schritt<br>48. In Schritt 83 muss zumindest die Berechnung des Hash-Wertes inkl.<br>Vergleich mit dem Wert aus den Metadaten und die mathematische<br>Prüfung der Signatur des DMDA neu erfolgen, um zwischenzeitliche<br>Änderungen an der Nachricht erkennen zu können.|
|---|---|
|Fehlerfälle|FC-01: Integritätsverletzung<br>FC-02: Zertifikat ungültig<br>FC-03: Der Status des Zertifikates konnte nicht online geprüft werden<br>FC-04: Keine Signatur bei einer Nachricht mit Versandoption<br>„Absenderbestätigt“|
|**Schritt 84**|**_Nachricht zum Empfänger übertragen_**|
|Kurzbeschreibung|Die Nachricht wird vom Postfachdienst des Empfängers zum Client des<br>Empfängers übertragen.|
|Akteure|Empfänger, Postfachdienst Empfänger|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung|Sicherer Kanal zwischen Postfachdienst Empfänger und Client|
|Input|**•**<br>Nachricht<br>**•**<br>Parameter, ob Integritätssicherung zusammen mit der Nachricht<br>übertragen werden soll (vgl. Funktion 14 in Abschnitt 7)|
|Ergebnis|Nachricht übertragen|
|Nachbedingung||
|Ablauf|**•**<br>Ermittlung, ob die Integritätssicherung zusammen mit der Nachricht<br>übertragen werden soll.<br>**•**<br>Übertragung der Nachricht vom Postfachdienst zum Client des<br>Empfängers.|
|Fehlerfälle|FC-01: Client hat Nachricht nicht entgegengenommen.|
|**Schritt 85**|<br>**_Nachrichten-Kopie ohne Domänen-Verschlüsselung löschen_**|
|Kurzbeschreibung|Der Postfachdienst löscht die entschlüsselte Kopie der Nachricht.|
|Akteure|Postfachdienst Empfänger|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung||



Bundesamt für Sicherheit in der Informationstechnik 

60 

6 Funktionale Beschreibung 

|Input|Nachricht ohne Domänen-Verschlüsselung|
|---|---|
|Ergebnis|Entschlüsselte Nachricht ist gelöscht|
|Nachbedingung|Anhalten|
|Ablauf|Entschlüsselte Nachricht löschen.|
|Fehlerfälle||



_Tabelle 8: Schritte zum Abrufen und Lesen der Nachrichten_ 

## **6.7 Empfang und Lesen der Nachricht durch Empfänger** 

|**Schritt 86**|**_Nachricht vom Postfachdienst entgegennehmen_**|
|---|---|
|Kurzbeschreibung|Der Client des Empfängers nimmt die Nachricht vom Postfachdienst des<br>Empfängers entgegen.|
|Akteure|Empfänger, Postfachdienst Empfänger|
|Auslöser|Postfachdienst Empfänger|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input|Nachricht|
|Ergebnis|Nachricht vom Client des Empfängers entgegengenommen|
|Nachbedingung||
|Ablauf|Der Client des Empfängers nimmt die Nachricht vom Postfachdienst<br>entgegen.<br>Prüfen, ob Nachricht syntaktisch korrekt ist.|
|Fehlerfälle|FC-01: Nachricht nicht vollständig übertragen.<br>FC-02: Nachricht enthält syntaktische Fehler.<br>Meldungsnachrichten sind gemäß Schritt 41 auch bei Auftreten<br>syntaktischer Fehler zuzustellen.|
|**Schritt 87**|<br>**_Entscheidungsknoten: Nachricht-verschlüsselt?_**|
|Kurzbeschreibung|Feststellen, ob die Nachricht Ende-zu-Ende-verschlüsselt ist.|
|ja|Schritt 88|
|nein|Schritt 89|
|**Schritt 88**|**_Nachricht entschlüsseln_**|
|Kurzbeschreibung|Die Nachricht wird lokal beim Empfänger entschlüsselt.|
|Akteure|Empfänger|
|Auslöser|Empfänger|
|Vorbedingung|Nachricht ist verschlüsselt|



Bundesamt für Sicherheit in der Informationstechnik 

61 

6 Funktionale Beschreibung 

|Input|Nachricht, Entschlüsselungsschlüssel von Empfänger|
|---|---|
|Ergebnis|Entschlüsselte Nachricht|
|Nachbedingung||
|Ablauf|**•**<br>Die zu entschlüsselnde Nachricht inklusive der Anhänge wird an die<br>Entschlüsselungsfunktion übergeben.<br>**•**<br>Die Entschlüsselungsfunktion greift auf den privaten Schlüssel des<br>Empfängers zu.<br>**•**<br>Die Entschlüsselungsfunktion entschlüsselt mit dem privaten<br>Schlüssel des Empfängers den symmetrischen<br>Verschlüsselungsschlüssel der Nachricht.<br>**•**<br>Der Nachrichtentext der Nachricht inklusive der Dateianhänge wird<br>mit dem symmetrischen Verschlüsselungschlüssel entschlüsselt.<br>Hinweis: Die Entschlüsselung der Nachricht muss auf dem System des<br>Nutzers erfolgen. Die entschlüsselte Nachricht darf auf dem DMDA-Server<br>auch nicht temporär zwischengespeichert werden.|
|Fehlerfälle|FC-01: Nachricht konnte nicht entschlüsselt werden.|
|**Schritt 89**|**_Entscheidungsknoten: Signatur prüfen?_**|
|Kurzbeschreibung|Feststellen, ob eine Signatur vorhanden ist und der Empfänger die Signatur<br>prüfen möchte.|
|ja|Schritt 90|
|nein|Schritt 91|
|**Schritt 90**|**_Signatur- und Zertifikatsprüfung durchführen_**|
|Kurzbeschreibung|Der Client des Empfängers führt eine Prüfung der Signatur sowie des<br>Zertifikates durch.|
|Akteure|Empfänger|
|Auslöser|Empfänger|
|Vorbedingung|Nachricht signiert|
|Input|Nachricht|
|Ergebnis|Ergebnis der Prüfung|
|Nachbedingung||
|Ablauf|**•**<br>Mathematische Prüfung der Signatur mit Signaturprüfschlüssel aus<br>Zertifikat<br>**•**<br>Prüfung der Gültigkeit des Zertifikates<br>**•**<br>Prüfung Zertifikatskette<br>**•**<br>Prüfung Status des Zertifikates<br>**•**<br>Prüfergebnisse zusammenfassen in Prüfprotokoll|



Bundesamt für Sicherheit in der Informationstechnik 

62 

6 Funktionale Beschreibung 

|Fehlerfälle|FC-01: Integritätsverletzung<br>FC-02: Zertifikat ungültig<br>FC-03: Der Status des Zertifikates konnte nicht online geprüft werden.|
|---|---|
|**Schritt 91**|<br>**_Nachricht darstellen_**|
|Kurzbeschreibung|Die Nachricht, die Ergebnisse der Signatur- und Zertifikatsprüfung des<br>Clients, sowie die Prüfprotokolle vom Postfachdienst werden dargestellt.|
|Akteure|Empfänger|
|Auslöser|Empfänger|
|Vorbedingung||
|Input|Nachricht|
|Ergebnis|Nachricht dargestellt|
|Nachbedingung|Anhalten|
|Ablauf|Die Nachricht, die Ergebnisse der Signatur- und Zertifikatsprüfung des<br>Clients sowie ggf. vorhandene Prüfprotokolle vom Postfachdienst<br>darstellen.|
|Fehlerfälle||



Bundesamt für Sicherheit in der Informationstechnik 

63 

7 Weitere Funktionen 

## **7 Weitere Funktionen** 

Die in diesem Abschnitt beschriebenen Funktionen werden entweder vom System ausgeführt oder können vom Nutzer interaktiv aufgerufen werden, während dieser am De-Mail-Konto angemeldet ist. 

## **7.1 Durch das System ausgeführte Funktionen** 

|**Funktion 1**|**_Abholbestätigungen versenden_**|
|---|---|
|Kurzbeschreibung|Für alle Nachrichten in dem Postfach, die eine Abholbestätigung erfordern<br>und für die noch keine Abholbestätigung erstellt und versendet wurde, wird<br>jeweils eine Abholbestätigung erstellt und versendet.|
|Akteure|Postfachdienst Empfänger|
|Auslöser|Empfänger|
|Vorbedingung|Anmeldung am De-Mail-Konto mit Authentisierungsniveau „hoch“.<br>Nachrichten, die eine Abholbestätigung erfordern und für die noch keine<br>Abholbestätigung erstellt und versendet wurde|
|Input|Nachrichten, die eine Abholbestätigung erfordern|
|Ergebnis|**•**<br>Erfolgter Versand der Abholbestätigungen für Nachrichten, die mit<br>dieser Versandoption erstellt wurden<br>**•**<br>Nachrichten wurden gekennzeichnet, dass die Abholbestätigung<br>versendet wurde|
|Nachbedingung||
|Ablauf|**•**<br>Selektion der Nachrichten mit der Versandoption<br>„Abholbestätigung“, mit folgenden Bedingung:<br>**◦**<br>noch keine Abholbestätigung erstellt und versendet<br>**◦**<br>keine automatisch weitergeleiteten Nachrichten sind<br>**•**<br>Bestätigungsnachrichten auf Grundlage der Abholbestätigung<br>erstellen.<br>**•**<br>Es wird jeweils die Versandoption „Persönlich“ gesetzt.<br>**•**<br>Element <Nachrichten-Kennung des Absenders> (Nr. 9) von der<br>ursprünglichen Nachricht in die jeweilige Bestätigungsnachricht<br>übernehmen.<br>**•**<br>Die Empfänger-Adresse ist auf die Absender- bzw. falls angegeben,<br>auf die Antwort-Adresse, der jeweiligen ursprünglichen Nachricht<br>zu setzen.<br>**•**<br>In Kopie (Carbon Copy, CC) ist der Empfänger der jeweiligen<br>ursprünglichen Nachricht zu setzen.|



Bundesamt für Sicherheit in der Informationstechnik 

64 

7 Weitere Funktionen 

||**•**<br>Absender-Adresse ist auf die System-Adresse des DMDA für<br>Abholbestätigungen zu setzen.<br>**•**<br>Die Bestätigungsnachrichten versenden.<br>**•**<br>Kennzeichnung der Nachrichten, für die eine Abholbestätigung<br>erstellt wurden|
|---|---|
|Fehlerfälle|FC-01: Nachricht kann nicht versendet werden|



_Tabelle 9: Durch das System ausgeführte Funktionen_ 

## **7.2 Durch den Nutzer initiierte Funktionen** 

|**Funktion 2**|**_Schadsoftware-Dienst: Prüfung auf Schadsoftware_**|
|---|---|
|Kurzbeschreibung|Es erfolgt eine Prüfung der vom Nutzer ausgewählten Nachrichten auf<br>Schadsoftware (z.B. Viren, Würmer und Trojaner)|
|Akteure|Nutzer, Postfachdienst|
|Auslöser|Nutzer|
|Vorbedingung|Prüfprogramme mit aktuellen Prüfkonfigurationen|
|Input|Nachricht|
|Ergebnis|Warnung, wenn Inhalt Schadsoftware enthält|
|Nachbedingung|Auf Nachrichten mit Schadsoftware darf ein Nutzer nur nach expliziter<br>Warnung zugreifen, dass das Öffnen der Nachricht auf eigene Gefahr<br>erfolgt und er sich mit dem Absender in Verbindung setzen sollte.|
|Ablauf|**•**<br>Nachrichten werden zum Schadsoftware-Scanner übergeben<br>**•**<br>Bei Erkennung von Schadsoftware werden die Nachrichten<br>entsprechend gekennzeichnet. Auf Nachrichten mit Schadsoftware<br>darf der Nutzer nur nach expliziter Warnung zugreifen.|
|Fehlerfälle|FC-01: Dateianhang unbekannt und kann nicht auf Schadsoftware geprüft<br>werden.|
|**Funktion 3**|**_Nachsendeauftrag an eine andere De-Mail-Adresse einrichten_**|
|Kurzbeschreibung|Der Nutzer stellt einen Nachsendeauftrag an eine andere De-Mail-Adresse.<br>Alle empfangenen Nachrichten werden während einer festgelegten<br>Übergangszeit an diese weitergeleitet.<br>(siehe Abschnitt 3.1.3.2).|
|Akteure|Nutzer, Postfachdienst|
|Auslöser|Nutzer|
|Vorbedingung|Anmeldung am De-Mail-Konto mit Authentisierungsniveau „hoch“,<br>Antrag auf Vertragbeendigung des De-Mail-Kontos liegt vor (vgl. [TR DM|



Bundesamt für Sicherheit in der Informationstechnik 

65 

7 Weitere Funktionen 

||ACM FU]).|
|---|---|
|Input|Nachsendeauftrag|
|Ergebnis|Nachsendeauftrag aktiviert|
|Nachbedingung||
|Ablauf|**•**<br>Nutzer stellt einen Nachsendeauftrag.<br>**•**<br>DMDA prüft, ob eine Vertragsbeendigung des De-Mail-Kontos<br>beantragt wurde.<br>**•**<br>Nachsendeauftrag wird mit der Vertragsbeendigung des De-Mail-<br>Kontos aktiviert.<br>**•**<br>**•**<br>Nach einem vorgegebenem Zeitraum wird der Nachsendeauftrag<br>automatisch deaktiviert.|
|Fehlerfälle|FC-01: Keine Änderung möglich, da nicht hinreichendes<br>Authentisierungsniveau bei der Anmeldung genutzt.<br>FC-02: De-Mail-Konto-Vertragsbeendigung nicht beantragt<br>FC-03: Keine gültige De-Mail-Adresse.<br>FC-04: Zeitraum der Aktivierung nicht zulässig.<br>FC-05: Angegebene De-Mail-Adresse für den Nachsendeauftrag entspricht<br>der aktuellen De-Mail-Adresse|
|**Funktion 4**|**_Export von Nachrichten_**|
|Kurzbeschreibung|Der Nutzer exportiert Nachrichten aus seinem Postfach zu seinem lokalen<br>IT-System.|
|Akteure|Nutzer, Postfachdienst|
|Auslöser|Nutzer|
|Vorbedingung|Anmeldung am De-Mail-Konto|
|Input|Kennung(en) der zu exportierenden Nachricht(en)|
|Ergebnis|Nachricht(en) inkl. Anhänge und Metadaten; Bestätigungen; Signatur-<br>Prüfprotokolle sind in ein für Im- und Export standardisiertes De-Mail-<br>Format exportiert|
|Nachbedingung||
|Ablauf|**•**<br>Nachrichten werden durch entsprechende Kennungen (bspw.<br>Message-ID) ausgewählt.<br>**•**<br>Der Nutzer wählt einen Speicherort auf seinem lokalen IT-System<br>für die zu exportierenden Nachricht(en).<br>**•**<br>Die Nachricht(en) wird in ein für Im- und Export standardisiertes<br>De-Mail-Format konvertiert.|



Bundesamt für Sicherheit in der Informationstechnik 

66 

7 Weitere Funktionen 

||**•**<br>Die Nachricht mitsamt den Metadaten und der Integritätssicherung<br>wird zum lokalen IT-System des Nutzers übertragen und dort<br>gespeichert.|
|---|---|
|Fehlerfälle|FC-01: Authentisierungsniveau des Anfragenden ist kleiner als das<br>Authentisierungsniveau (Versandoption „Persönlich“ oder<br>„Abholbestätigung“) der Nachricht<br>FC-02: Keine Nachricht ausgewählt.|
|**Funktion 5**|<br>**_Import von Nachrichten (optional)_**|
|Kurzbeschreibung|Der Nutzer importiert Nachrichten von seinem lokalen IT-System zu<br>seinem Postfach.|
|Akteure|Nutzer, Postfachdienst|
|Auslöser|Nutzer|
|Vorbedingung|Anmeldung am De-Mail-Konto mit hinreichendem Authentisierungsniveau|
|Input|Importdatei in einem für Im-und Export standardisiertem De-Mail-Format|
|Ergebnis|Nachricht(en) (Nachricht(en) inkl. Anhänge und Metadaten; Bestätigungen;<br>Signatur-Prüfprotokolle) sind im Postfach.|
|Nachbedingung||
|Ablauf|**•**<br>Importdatei wird für den Import ausgewählt.<br>**•**<br>Die Datei wird zum DMDA versandt.<br>**•**<br>Die Nachrichten werden in das Postfach abgelegt, zuvor sollte eine<br>Schadsoftwareprüfung durchgeführt werden..|
|Fehlerfälle|FC-01: Keine Nachricht gefunden.<br>FC-02: Nachricht existiert bereits im Postfach.|
|**Funktion 6**|**_Zugriff auf persönliches Adressbuch_**|
|Kurzbeschreibung|Der Nutzer greift auf sein persönliches Adressbuch zu, um Kontakte<br>einzusehen, zu erfassen, zu ändern oder zu löschen (vgl. [TR DM IT-BInfra<br>FU]).|
|Akteure|Nutzer, Postfachdienst|
|Auslöser|Nutzer|
|Vorbedingung|Anmeldung am De-Mail-Konto|
|Input|Folgende Möglichkeiten zum Auffinden eines Kontakts existieren:<br>**•**<br>Liste der vorhandenen Kontakte<br>**•**<br>Suche über Bestandteile der Kontaktdaten<br>Lesen der Kontaktdaten<br>**•**<br>Darstellung mit Kopier- bzw. Übernahmemöglichkeit der<br>Kontaktdaten|



Bundesamt für Sicherheit in der Informationstechnik 

67 

7 Weitere Funktionen 

||Editieren der Kontaktdaten<br>**•**<br>Erfassung von neuen oder geänderten Daten zum Kontakt<br>Löschung des Kontaktes<br>**•**<br>Auswahl bzw. Angabe des zu löschenden Kontaktes|
|---|---|
|Ergebnis|Kontakt angelegt, geändert, gelöscht, gelesen|
|Nachbedingung||
|Ablauf|**•**<br>Adressbuch wird geöffnet<br>**•**<br>Bei Einsicht, Löschung oder Änderung eines Kontakts:<br>**◦**<br>Auffinden des entsprechenden Kontakts<br>**◦**<br>Darstellung des Kontakts<br>**◦**<br>Änderung oder Löschung des Kontakts<br>**•**<br>Bei Erfassung eines neuen Kontaktes:<br>**◦**<br>neu anlegen<br>**◦**<br>manuelle Erfassung<br>**▪**<br>Kontaktinformationen aus Nachricht entnehmen<br>**▪**<br>Kontaktinformationen vom ÖVD übernehmen<br>**•**<br>Speicherung|
|Fehlerfälle|FC-01: Kontakt enthält keine Daten<br>FC-02: Übernahme von Empfängeradresse und Zertifikat nicht möglich|
|**Funktion 7**|<br>**_Anfrage an ÖVD_**|
|Kurzbeschreibung|Der Nutzer greift auf den ÖVD seines DMDAs zu|
|Akteure|Nutzer, ÖVD|
|Auslöser|Nutzer|
|Vorbedingung|Anmeldung am De-Mail-Konto|
|Input|Suchbegriffe (Kombination [Vorname, Name, [Ort oder Unternehmen]]<br>oder De-Mail-Adresse)|
|Ergebnis|Informationen aus ÖVD (De-Mail-Adresse, Zertifikate, etc.)|
|Nachbedingung||
|Ablauf|**•**<br>ÖVD aufrufen<br>**•**<br>Suchbegriff(e) eingeben<br>**•**<br>Suchergebnisse des ÖVD auswerten<br>**•**<br>Suchergebnisse in Nachrichtenentwurf oder persönliches<br>Adressbuch übernehmen|



Bundesamt für Sicherheit in der Informationstechnik 

68 

7 Weitere Funktionen 

|Fehlerfälle|FC-01: Zu wenig Merkmal zur Suche<br>FC-02: Über 200 Treffer. Schränken Sie die Suche weiter ein.|
|---|---|
|**Funktion 8**|**_Automatisierte Weiterleitungen von Nachrichten verwalten (Erstellen,_**<br>**_Löschen, Ändern)_**|
|Kurzbeschreibung|Der Nutzer verwaltet eine Weiterleitung von Nachrichten. Hierbei kann die<br>automatisierte Weiterleitung erstellt, geändert oder auch gelöscht werden.<br>(siehe Abschnitt 3.1.3.2).|
|Akteure|Nutzer, Postfachdienst|
|Auslöser|Nutzer|
|Vorbedingung|Anmeldung am De-Mail-Konto mit Authentisierungsniveau „hoch“.<br>Nur bei Änderung oder Löschung: Weiterleitung existiert bereits|
|Input|a) Bei Erstellung: Angabe einer Weiterleitungsadresse (De-Mail-<br>Adresse)<br>b) Bei Änderung: andere Weiterleitungsadresse (De-Mail-Adresse)<br>c) Bei Löschung: Markierung der zu löschenden Weiterleitungsadresse|
|Ergebnis|a+b) Weiterleitungsfunktion definiert bzw. geändert<br>c) Angaben zur Weiterleitungsfunktion gelöscht|
|Nachbedingung|Ist eine Weiterleitungsfunktion aktiviert, muss der Nutzer bei jedem Zugriff<br>auf sein Postfach darauf hingewiesen werden|
|Ablauf|**•**<br>Bei Erstellung und Änderung:<br>**◦**<br>Nutzer definiert die Weiterleitungsadresse<br>**◦**<br>Nutzer bestätigt die editierte Adresse<br>**•**<br>Bei Löschung:<br>**◦**<br>Nutzer löscht die Angaben zur Weiterleitungsfunktion<br>**◦**<br>Nutzer bestätigt die Löschung|
|Fehlerfälle|FC-01: Weiterleitungsadresse ist keine De-Mail-Adresse<br>FC-02: Keine De-Mail-Adresse angegeben<br>FC-03: Weiterleitungsadresse entspricht der aktuellen De-Mail-Adresse|
|**Funktion 9**|<br>**_Verwaltung von Kategorien_**|
|Kurzbeschreibung|Der Nutzer legt beliebige eigene Kategorien in seinem Postfach an bzw.<br>benennt diese um oder löscht diese. Eine hierarchische Anordnung der<br>Kategorien ist optional möglich.|
|Akteure|Nutzer, Postfachdienst|
|Auslöser|Nutzer|



Bundesamt für Sicherheit in der Informationstechnik 

69 

7 Weitere Funktionen 

|Vorbedingung|Anmeldung am De-Mail-Konto<br>Bei Umbenennen oder Löschung: Vorhandensein von zu behandelnden<br>Kategorien|
|---|---|
|Input|a) Funktion Erstellen: Kategorie-Bezeichnung<br>b) Funktion Löschen: Kategorie-Bezeichnung<br>c) Funktion Umbenennung: Kategorie-Bezeichnung_alt, Kategorie-<br>Bezeichnung_neu|
|Ergebnis|a) Kategorie existiert<br>b) Kategorie existiert nicht mehr<br>c) Kategorie existiert mit neuem Namen (vorherige Zuordnungen von<br>Nachrichten bleiben bestehen)|
|Nachbedingung||
|Ablauf|a) Funktion Erstellen<br><br>Aufruf der Funktion zum Erstellen von Kategorien im<br>Postfach<br><br>Angabe der Bezeichnung (ggf. inklusive der übergeordneten<br>Kategorien)<br><br>Bestätigung und Anlegen der Kategorie<br>b) Funktion Löschen<br><br>Aufruf der Funktion zum Löschen von Kategorien im<br>Postfach<br><br>Angabe der Bezeichnung (ggf. inklusive der übergeordneten<br>Kategorien)<br><br>Bestätigung und Löschen der Kategorie<br>c) Funktion Umbenennung<br><br>Aufruf der Funktion zum Umbenennen von Kategorien im<br>Postfach<br><br>Auswahl der umzubenennenden Kategorie<br><br>Angabe der neuen Bezeichnung<br><br>Bestätigung und Umbenennung der Kategorie|
|Fehlerfälle|FC-01: Kategorie kann nicht gelöscht werden, da noch Nachrichten<br>zugeordnet sind<br>FC-02: Kategorie-Bezeichnung schon vorhanden|
|**Funktion 10**|<br>**_Manuelle Zuordnung von Nachrichten zu Kategorien_**|
|Kurzbeschreibung|Der Nutzer ordnet manuell Nachrichten den im Postfach angelegten|



Bundesamt für Sicherheit in der Informationstechnik 

70 

7 Weitere Funktionen 

||Kategorien zu.|
|---|---|
|Akteure|Nutzer, Postfachdienst|
|Auslöser|Nutzer|
|Vorbedingung|Anmeldung am De-Mail-Konto mit hinreichendem Authentisierungsniveau|
|Input|Nachrichten, Kategorien|
|Ergebnis|Nachrichten sind in Kategorien auffindbar|
|Nachbedingung||
|Ablauf|**•**<br>Markierung der entsprechenden Nachrichten<br>**•**<br>Aufruf der Funktion zur Zuordnung zu einer Kategorie<br>**•**<br>Wahl bzw. Anlegen der Kategorie<br>**•**<br>Bestätigung zum Verschieben (optional)|
|Fehlerfälle|FC-01: Keine Nachrichten zum Verschieben vorhanden/gewählt<br>FC-02: Kategorie nicht definiert|
|**Funktion 11**|<br>**_Verwaltung von Regeln zur automatische Zuordnung von Nachrichten zu_**<br>**_Kategorien_**|
|Kurzbeschreibung|Der Nutzer definiert, ändert oder löscht Regeln, nach denen Nachrichten<br>automatisch nach dem Empfang im Postfach vom Nutzer angegebenen<br>Kategorien zugeordnet werden.|
|Akteure|Nutzer, Postfachdienst|
|Auslöser|Nutzer|
|Vorbedingung|Anmeldung am De-Mail-Konto<br>Bei Löschung, Änderung: Vorhandensein einer Regel|
|Input|a) Erstellung<br><br>Definition zur Parametrisierung eines Regelwerkes zum<br>automatisierten Zuordnen von Nachrichten<br>Parameter sind dabei mindestens:<br>-<br>Zeichenkette im Betreff der Nachricht<br>-<br>Absender-Adresse bzw. Domäne des Absenders<br>-<br>Versandoption „Absenderbestätigt“ ja/nein<br>-<br>Versandoption „Persönlich“ ja/nein<br>-<br>Versandoption „Versandbestätigung ja/nein<br>-<br>Versandoption „Eingangsbestätigung ja/nein<br>-<br>Versandoption „Abholbestätigung ja/nein<br>-<br>Ende-zu-Ende-Verschlüsselung ja/nein|



Bundesamt für Sicherheit in der Informationstechnik 

71 

7 Weitere Funktionen 

||-<br>Signatur der Nachricht ja/nein<br>-<br>Dateianhänge (ja/nein, Speichergröße)<br>-<br>Nachrichten-Typ<br><br>Bezeichnung der Regel<br><br>Angabe der Abarbeitungsreihenfolge hinsichtlich bereits<br>existierender Regeln<br>b) Änderung<br><br>Angabe der Änderungen hinsichtlich Bezeichnung und/oder<br>Parameter der Regel<br>c) Löschung<br><br>Angabe der zu löschenden Regel|
|---|---|
|Ergebnis|a) Neue Regel erstellt<br>b) Definierte Regel geändert<br>c) Definierte Regel gelöscht|
|Nachbedingung||
|Ablauf|a) Regel erstellen<br><br>Angabe eines Bezeichners<br><br>Angabe der Parameter<br><br>Angabe der Abarbeitungsreihenfolge<br><br>Bestätigung der Regeldefinition (Bezeichnung und Parameter)<br>b) Regel ändern<br><br>Auswahl der Zu ändernden Regel<br><br>Angabe der zu ändernden Parameter<br><br>Bestätigung der Regeldefinition<br>c) Regel löschen<br><br>Auswahl der zu löschenden Regel<br><br>Bestätigung zum Löschen|
|Fehlerfälle|FC-01: Parameter der Regel nicht nutzbar<br>FC-02: Bezeichnung existiert bereits|
|**Funktion 12**|<br>**_Such- bzw. Filter-/Sortierfunktionen für Nachrichten_**|
|Kurzbeschreibung|Der Nutzer sucht anhand von Suchkriterien bzw. Filterdefinitionen oder<br>über Sortierungen nach Nachrichten in seinem Postfach.<br>Hinweis: Die Suche in Anhängen von Nachrichten ist optional.|



Bundesamt für Sicherheit in der Informationstechnik 

72 

7 Weitere Funktionen 

|Akteure|Nutzer, Postfachdienst|
|---|---|
|Auslöser|Nutzer|
|Vorbedingung|Anmeldung am De-Mail-Konto mit hinreichendem Authentisierungsniveau|
|Input|**•**<br>Filter- bzw. Sortierkriterien (Absender-/ Empfänger-Adresse,<br>Subjekt, Versanddatum, Versandoption, Signatur/Verschlüsselung,<br>Bestätigungen/Meldung)<br>und/oder<br>**•**<br>Suchkriterien (Wort bzw. Wortgruppen in Verbindung mit einer<br>Definition, über welche Felder/Attribute (Nachrichtentext,<br>Dateianhänge, Metadaten-Attribute) die Suchfunktion angewandt<br>wird<br>Hinweis: Es werden nur Nachrichten angezeigt, für die ein ausreichendes<br>Authentisierungsniveau vorliegt.|
|Ergebnis|Liste der gefundenen Nachrichten|
|Nachbedingung||
|Ablauf|**•**<br>Such- bzw. Filter-/Sortierkriterien angeben<br>**•**<br>Suche/Filterung bzw. Sortierung starten<br>**•**<br>Suchergebnisse darstellen|
|Fehlerfälle||
|**Funktion 13**|**_Löschen von Nachrichten_**|
|Kurzbeschreibung|Der Nutzer löscht Nachrichten aus seinen Postfach-Kategorien. Dabei ist zu<br>unterscheiden:<br>a) Löschen durch Zuordnung zu der Kategorie „Papierkorb“ und<br>b) Endgültiges und unwiederbringliches Löschen aus der Kategorie<br>„Papierkorb“<br>Versand- und Eingangsbestätigungen und Nachrichten für die eine<br>Versand- oder Eingangsbestätigung ausgestellt wurde, müssen mindestens<br>mit Authentisierungsniveau „hoch“ gelöscht werden oder älter als 90 Tage<br>sein.<br>Nachrichten mit der Versandoption „persönlich“ können nur mit dem<br>Authentisierungsniveau „hoch“ gelöscht werden.<br>Abholbestätigungen und Nachrichten, für die eine Abholbestätigung<br>ausgestellt wurde, können nur mit Authentisierungsniveau „hoch“ gelöscht<br>werden.|
|Akteure|Nutzer, Postfachdienst|
|Auslöser|Nutzer|
|Vorbedingung|Anmeldung am De-Mail-Konto|



Bundesamt für Sicherheit in der Informationstechnik 

73 

7 Weitere Funktionen 

|Input|Nachricht|
|---|---|
|Ergebnis|a) Nachricht in Papierkorb-Kategorie<br>b) Nachricht gelöscht|
|Nachbedingung||
|Ablauf|Zu löschende Nachricht(en) auswählen<br>a) Zuordnung der zu löschenden Nachricht zu der Kategorie<br>Papierkorb<br>b) endgültiges und unwiederbringliches Löschen aus dem Papierkorb<br>nach einer Bestätigung durch den Nutzer<br>Hinweis: Es können nur Nachrichten ausgewählt werden, für die ein<br>ausreichendes Authentisierungsniveau vorliegt.|
|Fehlerfälle|FC-01: Nicht löschbar, da aktuelles Authentisierungsniveau niedriger ist<br>als für ein Lesen der Nachricht benötigt wird (Versandoption<br>„Persönlich“).<br>FC-02: Nicht löschbar, da Nachricht mit Eingangs- bzw. Abholbestätigung<br>nur mit Authentisierungsniveau „hoch“ gelöscht werden kann oder älter als<br>90 Tage sein muss.<br>FC-03: Nicht löschbar, da Nachricht eine Bestätigungsnachricht ist und nur<br>mit Authentisierungsniveau „hoch“ gelöscht werden kann oder älter als 90<br>Tage sein muss.|
|**Funktion 14**|<br>**_Konfiguration der Übermittlung der Integritätssicherung_**|
|Kurzbeschreibung|Der Nutzer konfiguriert, bei welchen Protokollen die Integritätssicherung<br>der Nachrichten mit auf den lokalen PC des Nutzers übertragen werden<br>soll, da ggf. bei einigen Clients Probleme bei der Verarbeitung der<br>Integritätssicherung auftreten können.|
|Akteure|Nutzer, Postfachdienst|
|Auslöser|Nutzer|
|Vorbedingung|Anmeldung am De-Mail-Konto|
|Input|**•**<br>Angabe des Protokolls<br>**•**<br>Angabe ob Integritätssicherung übermittelt werden soll (Ja/Nein)|
|Ergebnis|Konfiguration der Übermittlung der Integritätssicherung bei ausgewählten<br>Protokoll|
|Nachbedingung||
|Ablauf|**•**<br>Nutzer öffnet entsprechenden Dialog<br>**•**<br>Nutzer wählt Aktivierung/Deaktivierung für Protokoll<br>**•**<br>Nutzer speichert die Änderung|
|Fehlerfälle||



Bundesamt für Sicherheit in der Informationstechnik 

74 

7 Weitere Funktionen 

_Tabelle 10: Durch den Nutzer initiierte Funktionen_ 

Bundesamt für Sicherheit in der Informationstechnik 

75 

8 Obligatorische und optionale Funktionalität 

## **8 Obligatorische und optionale Funktionalität** 

Die hier beschriebene Funktionalität des PVD ist obligatorisch, sofern sie in den vorherigen Abschnitten oder in der nachfolgenden Tabelle nicht explizit als optional gekennzeichnet ist. 

|**_Funktionalität_**|**_Referenz_**|**_Status6_**|
|---|---|---|
|Erstellen und Versenden von Nachrichten|Kap. 3.1.1|+|
|Empfang von Nachrichten|Kap. 3.1.2|+|
|Prüfung auf Schadsoftware|Kap. 3.1.3.1|+|
|Automatisierte Weiterleitung an eine andere De-Mail-Adresse|Kap. 3.1.3.2|+|
|Nachsendeauftrag an eine andere De-Mail-Adresse|Kap. 3.1.3.3|+|
|Export von Nachrichten und-inhalten|Kap. 3.1.3.4|+|
|Zugriff auf persönliches Adressbuch|Kap. 3.1.3.5|+|
|Zugriff auf ÖVD|Kap. 3.1.3.5|+|
|Weiterleiten und Beantworten von Nachrichten|Kap. 3.1.3.6|+|
|Ablage von Nachrichten in Kategorien|Kap. 3.1.3.7|+|
|Suchfunktionen für Nachrichten|Kap. 3.1.3.8|+|
|Löschen von Nachrichten|Kap. 3.1.3.9|+|
|Benachrichtigung bei falscher Adressierung|Kap. 3.2.1|+|
|Transport von Nachrichten innerhalb von De-Mail|Kap. 3.2.2|+|
|Durchleitung von Ende-zu-Ende gesicherten (signierten und/oder<br>verschlüsselten) Nachrichten|Kap. 3.2.2|+|
|Versandoptionen|Kap. 3.3|+|



_Tabelle 11: Obligatorische und optionale Funktionalität_ 

6 „+“ Funktionalität ist obligatorisch, „–“ Funktionalität ist optional 

Bundesamt für Sicherheit in der Informationstechnik 

76 


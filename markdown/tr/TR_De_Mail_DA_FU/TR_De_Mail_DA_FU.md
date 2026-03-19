
![](markdown/tr/TR_De_Mail_DA_FU/TR_De_Mail_DA_FU.pdf-0001-00.png)



![](markdown/tr/TR_De_Mail_DA_FU/TR_De_Mail_DA_FU.pdf-0001-01.png)


BSI – Technische Richtlinie Bezeichnung: Dokumentenablage Funktionalitätsspezifikation Anwendungsbereich: De-Mail Kürzel: BSI TR 01201 Teil 5.1 Version: 1.8 

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn Tel.: +49 22899 9582-0 E-Mail: de-mail@bsi.bund.de Internet: https://www.bsi.bund.de © Bundesamt für Sicherheit in der Informationstechnik 2024 

## **Inhaltsverzeichnis** 

|1|Einleitung....................................................................................................................................5|
|---|---|
|2|Funktionale Anforderungen........................................................................................................6|
|2.1|Zugriff auf Dokumente in der DA.......................................................................................................6|
|2.1.1|Authentisierung und Autorisierung................................................................................................6|
|2.1.2|Zugriffsoperationen........................................................................................................................6|
|2.2|Ablage von Dokumenten.....................................................................................................................7|
|2.2.1|Kategorien......................................................................................................................................7|
|2.2.2|Erstellung neuer Kategorien...........................................................................................................7|
|2.2.3|Einstellen neuer Dokumente...........................................................................................................7|
|2.2.4|Herunterladen von Dokumenten.....................................................................................................8|
|2.2.5|Umbenennen von Dokumenten und Kategorien............................................................................8|
|2.2.6|Löschen von Dokumenten..............................................................................................................8|
|2.2.7|Löschen von Kategorien.................................................................................................................8|
|2.2.8|Änderung der Berechtigungen für Dokumente und Kategorien.....................................................9|
|2.3|Suchen und Finden..............................................................................................................................9|
|2.4|Protokollierung der Aktivitäten.........................................................................................................10|
|2.5|Verschlüsselung.................................................................................................................................11|
|2.6|Konfiguration.....................................................................................................................................11|
|3|Nicht-funktionale Anforderungen.............................................................................................12|
|4|Datenstrukturen.........................................................................................................................13|
|4.1|Datei...................................................................................................................................................13|
|4.2|Kategorien..........................................................................................................................................14|
|4.3|Meldungen.........................................................................................................................................14|
|5|Aktivitätsdiagramm...................................................................................................................16|
|6|Funktionale Beschreibung.........................................................................................................23|
|6.1|Upload und Download von Dateien..................................................................................................23|
|6.1.1|Upload einer Datei in die DA.......................................................................................................23|
|6.1.2|Download von Dateien.................................................................................................................30|
|6.2|Verwaltung von Dateien/Kategorien.................................................................................................35|
|6.2.1|Erstellen einer Kategorie..............................................................................................................35|
|6.2.2|Umbenennen von Dateien/Kategorien.........................................................................................39|
|6.2.3|Löschen von Dateien/Kategorien.................................................................................................43|
|6.2.4|Ändern der Berechtigungen für Dokumente und Kategorien.......................................................47|
|6.3|Suche und Anzeige von Dokumenten und Kategorien......................................................................51|
|7|Weitere Funktionen...................................................................................................................56|
|7.1|Durch das System ausgeführte Funktionen.......................................................................................56|
|7.2|Durch den Nutzer initiierte Funktionen.............................................................................................57|
|8|Legende zum Aktivitätsdiagramm............................................................................................59|
|9|Legende zu Schritten der Ablaufbeschreibung.........................................................................61|



Bundesamt für Sicherheit in der Informationstechnik 

3 

## **Tabellenverzeichnis** 

Tabelle 1: Metadaten einer Datei........................................................................................................13 Tabelle 2: Daten der Kategorie (Teil 1)..............................................................................................14 Tabelle 3: Metadaten der Kategorie (Teil 2)......................................................................................14 Tabelle 4: Schritte zum Upload von Dateien.....................................................................................28 Tabelle 5: Schritte zum Download von Dateien.................................................................................33 Tabelle 6: Schritte zum Erstellen einer Kategorie..............................................................................37 Tabelle 7: Schritte zum Umbenennen................................................................................................41 Tabelle 8: Schritte zum Löschen........................................................................................................45 Tabelle 9: Schritte zur Änderung von Berechtigungen......................................................................49 Tabelle 10: Schritte zur Suche und Anzeige von Kategorien/ Dateien..............................................53 Tabelle 11: Durch das System ausgeführte Funktionen.....................................................................55 Tabelle 12: Durch den Nutzer initiierte Funktionen...........................................................................56 Tabelle 13: Legende zum Aktivitätsdiagramm..................................................................................58 Tabelle 14: Legende zu Schritten.......................................................................................................59 

Bundesamt für Sicherheit in der Informationstechnik 

4 

1 Einleitung 

## **1 Einleitung** 

Dieses Modul beinhaltet die funktionalen Spezifikationen der Dokumentenablage und ist Bestandteil von [TR DM DA M]. 

Bundesamt für Sicherheit in der Informationstechnik 

5 

2 Funktionale Anforderungen 

## **2 Funktionale Anforderungen** 

Nachfolgend werden die funktionalen Anforderungen beschrieben, die erfüllt werden müssen, damit ein Dienst zur Ablage und Verwaltung von elektronischen Dokumenten und anderen Dateien als De-Mail-Dienst anerkannt werden kann. 

Über den De-Mail-Versanddienst empfangene Dokumente kann der Nutzer von seinem De-MailPostfach in seine DA kopieren. Weiterhin kann der Nutzer Dokumente aus seiner DA über den PVD an Dritte verschicken (vgl. [TR DM PVD FU]). 

Alle Aktionen sind in geeigneter Weise zu protokollieren. 

## **2.1 Zugriff auf Dokumente in der DA** 

Ein Nutzer darf auf Dokumente in seiner DA nur Zugriff erhalten, wenn er sich vorher erfolgreich an seinem De-Mail-Konto angemeldet hat. 

## **2.1.1 Authentisierung und Autorisierung** 

Nach erfolgreicher Anmeldung am De-Mail-Konto hat der Nutzer Zugriff auf alle Dokumente und Kategorien in der seinem Konto zugeordneten DA (vgl. Abschnitt 2.2.1). 

Um auf den Inhalt und die Metadaten eines Dokumentes oder einer Kategorie zugreifen zu können, muss der Nutzer beim Einstellen festlegen können, für welche Zugriffsoperationen welches Authentisierungsniveau notwendig sein soll. Legt der Nutzer die Berechtigungen nicht fest, so wird automatisch das Authentisierungsniveau verwendet, mit dem der Nutzer zu diesem Zeitpunkt angemeldet ist. Ein Zugriff auf das Dokument erfordert sodann eine Anmeldung des Nutzers mit mindestens diesem Authentisierungsniveau. 

Das Authentisierungsniveau für einen Zugriff auf ein Dokument kann durch den Nutzer herabgestuft werden, wenn sein aktuelles Authentisierungsniveau einen Zugriff auf das Dokument erlaubt. Das minimale Authentisierungsniveau eines Dokuments kann durch den Nutzer bis auf das Niveau erhöht werden, das seinem aktuellen Authentisierungsniveau entspricht. 

## **2.1.2 Zugriffsoperationen** 

Folgende Zugriffsoperationen auf Dokumente müssen in Abhängigkeit von den jeweiligen Authentisierungsniveaus von der DA unterstützt werden: 

- Lesen 

- Schreiben (und Löschen) Unter „Schreiben“ fallen das Einstellen von neuen Dokumenten und das Ändern von vorhandenen Dokumenten. 

Bundesamt für Sicherheit in der Informationstechnik 

6 

2 Funktionale Anforderungen 

## **2.2 Ablage von Dokumenten** 

## **2.2.1 Kategorien** 

Um das spätere Suchen und Auffinden von Dokumenten zu erleichtern, muss es in der DA möglich sein, Dokumente bestimmten Kategorien zuzuordnen, die bspw. als Ordner in einer Hierarchie abgebildet werden können. Es müssen mindestens zwei vordefinierte Kategorien existieren. Eine Standardkategorie, der Dokumente zugeordnet werden, z.B. wenn vom Nutzer noch keine Kategorie erstellt wurde, sowie die Kategorie „Papierkorb“, der Dokumente zugeordnet werden, die gelöscht werden sollen. 

Kategorien können hierarchisch in mehreren Ebenen gestaffelt werden. 

## **2.2.2 Erstellung neuer Kategorien** 

Bei der Erstellung einer neuen Kategorie muss geprüft werden, ob in der übergeordneten Kategorie bereits eine Kategorie mit dem selben Namen existiert und ob für den Nutzer Schreibrechte bestehen. 

Das Authentisierungsniveau für die neue Kategorie muss mindestens dem der übergeordneten Kategorie entsprechen. In Unterkategorien kann das geforderte Authentisierungsniveau nur erhöht werden. 

## **2.2.3 Einstellen neuer Dokumente** 

Der Nutzer kann neue Dokumente 

- von seinem Rechnersystem in die DA hochladen, 

- eine Nachricht aus seinem Postfach in die DA speichern oder, 

- einen Anhang einer Nachricht aus dem Postfach in der DA ablegen. 

Die Dokumente können einer oder mehreren Kategorien zugeordnet werden. Wird für ein Dokument keine Kategorie ausgewählt, so wird es der Standardkategorie zugeordnet. Der Nutzer muss die notwendige Zugriffsberechtigung für die Kategorie(n) besitzen. 

Das Dokument wird durch den DMDA einer Prüfung auf Schadsoftware unterzogen. Bei einer positiven Prüfung wird das Dokument nicht gespeichert, der Nutzer erhält eine entsprechende Meldung. 

Wenn nicht genügend freier Speicherplatz verfügbar ist, muss der Nutzer per Meldung informiert werden. 

Für das Dokument wird standardmäßig folgende Berechtigung gesetzt: 

- Lesen: Dies ist gestattet für den angemeldeten Nutzer mit dem aktuellen Authentisierungsniveau, 

Bundesamt für Sicherheit in der Informationstechnik 

7 

2 Funktionale Anforderungen 

- Schreiben: Dies ist gestattet für den angemeldeten Nutzer mit dem aktuellen Authentisierungsniveau. Die Berechtigung des Dokuments muss mindestens dem geforderten Authentisierungsniveau der Kategorie entsprechen, der das Dokument zugeordnet wird. 

Es wird für jede eingestellte Datei ein Hashwert berechnet und gespeichert. 

## **2.2.4 Herunterladen von Dokumenten** 

Der Nutzer darf nur Dokumente herunterladen können, für die er die Zugriffsberechtigung zum Lesen besitzt. 

Vor dem Herunterladen muss der DMDA das Dokument auf Schadsoftware prüfen. Bei einer positiven Prüfung ist der Nutzer per Meldung zu informieren. 

Der DMDA muss den Hashwert des Dokumentes prüfen. Stimmt der neu berechnete Hashwert nicht mit dem ursprünglichen Wert überein, so ist der Nutzer per Meldung zu informieren. 

Danach ist das Herunterladen des Dokuments möglich. 

## **2.2.5 Umbenennen von Dokumenten und Kategorien** 

Dokumente und Kategorien müssen umbenannt werden können. 

Die Umbenennung findet statt, wenn der Nutzer schreibend auf das Dokument oder die Kategorie zugriffsberechtigt ist und der neue Name in der übergeordneten Kategorie noch nicht vorhanden ist. 

Der Nutzer kann Dokumente und Kategorien nur umbenennen, wenn er die notwendige Berechtigung besitzt. 

## **2.2.6 Löschen von Dokumenten** 

Der Nutzer kann Dokumente nur löschen, wenn er die notwendige Berechtigung besitzt. 

Für die Löschung von Dokumenten ist ein zweistufiges Verfahren vorzusehen. Im ersten Schritt werden die Dokumente in die Kategorie „Papierkorb“ verschoben. Alle Zuordnungen zu anderen Kategorien werden entfernt. Im zweiten Schritt können die Dokumente aus der Kategorie „Papierkorb“ endgültig gelöscht werden. 

Bei der endgültigen Löschung müssen die Dokumente sicher gelöscht werden. Alle Informationen zu den Dokumenten sind vollständig zu entfernen. Dies betrifft auch die Metadaten der Dokumente. 

Der Nutzer muss ein oder mehrere Dokumente löschen können. 

## **2.2.7 Löschen von Kategorien** 

Zur Löschung einer Kategorie muss der Nutzer die notwendige Berechtigung haben. 

Die zu löschende Kategorie darf keine untergeordneten Kategorien oder zugeordnete Dateien enthalten. 

Bundesamt für Sicherheit in der Informationstechnik 

8 

2 Funktionale Anforderungen 

Die vordefinierten Kategorien (Standardkategorie und„Papierkorb“) können nicht gelöscht werden. 

## **2.2.8 Änderung der Berechtigungen für Dokumente und Kategorien** 

Bei der Änderung einer Berechtigung muss geprüft werden, ob 

- das Authentisierungsniveau des Nutzers ausreichend ist, um die Dokumente oder Kategorie zu ändern. 

- das aktuelle Authentisierungsniveau des Nutzers mindestens dem Authentisierungsniveau entspricht, das gesetzt werden soll. 

Wenn die Bedingungen erfüllt sind, werden die Berechtigungen innerhalb der Metadaten entsprechend geändert. 

Bei der rekursiven Änderung von Berechtigungen (wenn eine Kategorie geändert wird, die weitere Kategorien oder Dateien enthält) gelten folgende Regeln: 

- Wird das Authentisierungsniveau einer Kategorie erhöht, so werden die Berechtigungen aller darin enthaltenen Dokumenten und Kategorien erhöht, für die das Authentisierungsniveau „normal“ benötigt wird. Die Berechtigungen aller anderen Dokumenten und Kategorien bleiben bestehen. 

- Wenn das Authentisierungsniveau herabgesetzt wird, können die Berechtigungen aller enthaltenen Dokumente und Kategorien bestehen bleiben oder auf Wunsch ebenfalls herabgesetzt werden. 

## **2.3 Suchen und Finden** 

Die Suchfunktion muss sowohl die Suche nach Kriterien wie Dateinamen und Kategorien als auch nach Dokumentinhalten von Standard-Dateiformaten in nicht durch den Nutzer zusätzlich verschlüsselten Dokumenten ermöglichen. 

Suchkriterien können sein: 

- Teile des Namens oder vollständiger Name der Datei, einschließlich Datei-Endung 

- Teile des Namens oder vollständiger Name der Kategorie 

- Datei-MIME-Typ (Format) 

- Inhalt der Datei (Text) 

- Einschränkungen hinsichtlich der Kategorien 

- Datum und Zeit der letzten Änderung in der DA 

Der Suchindex muss verschlüsselt gespeichert werden. 

Die Ergebnisliste muss beinhalten: 

Bundesamt für Sicherheit in der Informationstechnik 

9 

2 Funktionale Anforderungen 

- bei Kategorien: 

   - Kategorie-Pfad inkl. aller Kategoriebezeichnungen 

   - URL 

- bei Dokumenten 

   - Kategorie-Pfad inkl. aller Kategoriebezeichnungen 

   - Dateiname 

   - Datum der letzten Änderung in der DA 

   - URL 

Bei der Suche wird beachtet, dass ausschließlich die Dokumente oder Kategorien berücksichtigt werden, die für den Nutzer und seinem derzeitigen Authentisierungsniveau lesbar sind. 

Die Ergebnisliste muss nach Abschluss der Suche durch den DMDA sicher gelöscht werden. 

## **2.4 Protokollierung der Aktivitäten** 

Um Anwendungsfehler oder Missbrauch feststellen zu können, müssen alle Aktionen protokolliert werden, die Dokumente und Kategorien betreffen. 

Bei der Protokollierung der Aktionen ist sicher festzuhalten: 

- Nutzerkennung 

- Authentisierungsniveau des Nutzers 

- Neue Metadaten 

- Datum und Uhrzeit. 

Der Nutzer kann auf Wunsch ein Protokoll über die Aktivitäten in der DA anfordern, das mit einer qualifizierten Signatur des DMDA versehen ist. Das Protokoll kann dem Nutzer mittels Anhang einer De-Mail oder als Download zur Verfügung gestellt werden. 

Das Protokoll muss beinhalten: 

- eine Liste der eingestellten Dokumente mit dem jeweiligen Hashwert und dem Namen des Hashalgorithmus, 

- das aktuelle Authentisierungsniveau, 

- eine Änderungshistorie der Dokumente. 

Das Protokoll kann anhand folgender Merkmale eingeschränkt werden: 

- Kategorie, 

- Dateinamen, 

- Zeitraum. 

Bundesamt für Sicherheit in der Informationstechnik 

10 

2 Funktionale Anforderungen 

## **2.5 Verschlüsselung** 

Alle in der DA von De-Mail abgelegten Dokumente müssen durch den DMDA verschlüsselt abgelegt werden. Der DMDA hat zudem Sorge dafür zu tragen, dass vom Nutzer aus der DA angeforderten Dokumente entschlüsselt werden. 

Darüber hinaus muss der Nutzer bei Bedarf auch seinerseits zusätzlich verschlüsselte Dokumente ablegen können. Der DMDA sollte hierzu geeignete Software empfehlen oder kann diese selbst zur Verfügung stellen. 

## **2.6 Konfiguration** 

Die Konfiguration der DA sollte der Nutzer über eine Web-Oberfläche durchführen können. 

Folgende Merkmale müssen je Dokument bzw. je Kategorie konfigurierbar sein: 

- Erlaubte Zugriffsoperationen (vgl. Abschnitt 2.1.2) 

- Minimales Authentisierungsniveau für die jeweilige Zugriffsoperation (vgl. Abschnitt 2.1.1) 

Bundesamt für Sicherheit in der Informationstechnik 

11 

3 Nicht-funktionale Anforderungen 

## **3 Nicht-funktionale Anforderungen** 

Die in der DA eingestellten Dokumente müssen dem Nutzer vollständig und unverändert zur Verfügung gestellt werden, bis der Nutzer die betreffenden Dokumente selbst löscht oder das zugehörige De-Mail-Konto aufgelöst worden ist. 

Jeder Nutzer eines De-Mail-Kontos hat einen minimalen Speicherplatz pro Konto zur Verfügung. Ist dieser Speicher noch nicht durch Daten des Nutzers belegt, muss ein Dokument in der DA abgelegt werden können. Der Nutzer muss gewarnt werden, falls seine DA nur noch über 10% freien Speicher verfügt, gemessen am maximal vorgesehenen Speicherplatz des De-Mail-Kontos. 

Bundesamt für Sicherheit in der Informationstechnik 

12 

4 Datenstrukturen 

## **4 Datenstrukturen** 

In diesem Abschnitt werden die in der DA verwendeten Datenstrukturen beschrieben. Es werden die Elemente der Datenstrukturen bestimmt und abstrakt definiert. 

Die formale Definition der Datenstrukturen darf jeder DMDA selbst vornehmen. 

## **4.1 Datei** 

In der DA eines Nutzers können beliebige Dateien gespeichert werden. 

Zu jeder Datei werden die nachfolgend definierten Metadaten in der DA des Nutzers abgelegt. 

|<br>**_Nr_**|<br>**_Bezeichnung_**|<br>**_Werte_**|<br>**_Bemerkung_**|
|---|---|---|---|
|1|Nutzerkennung|Kennung und<br>zugehörige De-<br>Mail-Adresse|Kennzeichnung des Besitzers der<br>Datei|
|2|Verweis auf Datei|Dateiname|Dateiname ist in der zugehörigen<br>Kategorie eindeutig|
|3|Authentisierungs-Niveau|Normal/Hoch|Authentisierungsniveau des Nutzers<br>bei der letzten Änderung|
|4|Datum und Zeit der letzten<br>Änderung in der DA|Datum & Zeit|sekundengenau|
|5|Kategorie-Zuordnung|Numerische<br>Schlüsselwerte<br>(siehe 4.2)|Optional, Mehrfachbelegung|
|6|Hashwert der Datei|Message-Digest||
|7|Größe der Datei|Numerischer Wert||
|8|Autorisierter Nutzer|Kennung oder<br>zugehörige De-<br>Mail-Adresse||
|9|Mindest-Auth.-Niveau-Lesen|Normal/Hoch||
|10|Mindest-Auth.-Niveau –<br>Schreiben/Löschen|Normal/Hoch||



_Tabelle 1: Metadaten einer Datei_ 

Der autorisierte Nutzer ist immer identisch mit der Nutzerkennung aus Tabelle 1. Die Metadaten werden von der DA des Nutzers erzeugt. Für jede einzelne Datei werden neue Metadaten definiert. Bei Änderungen oder Löschung der Datei oder der zugehörigen Zugriffsrechte werden die Metadaten ebenfalls geändert bzw. gelöscht. 

Bundesamt für Sicherheit in der Informationstechnik 

13 

4 Datenstrukturen 

## **4.2 Kategorien** 

Kategorien sind eigene Objekte, die hierarchisch angeordnet werden können. Sie können beispielsweise als Ordner oder Verzeichnisse abgebildet werden. 

Jede Kategorie wird mindestens durch folgende Daten beschrieben: 

|**_Nr_**|**_Bezeichnung_**|**_Wert_**|**_Bemerkung_**|
|---|---|---|---|
|1|Schlüsselwert|Numerisch|Eindeutiger Wert in der DA des<br>Nutzers (für die Zuordnung zur<br>Datei)|
|2|Bezeichnung|Text||
|3|Übergeordnete Kategorie-<br>Ebene|Numerisch|Optional: Referenz zu Nr.1|



_Tabelle 2: Daten der Kategorie (Teil 1)_ 

Zusätzlich muss zu jedem Kategorie-Objekt folgende Ausprägung von Metadaten existieren: 

|**_Nr_**|**_Bezeichnung_**|**_Wert_**|**_Bemerkung_**|
|---|---|---|---|
|1|Nutzerkennung|Kennung und<br>zugehörige De-<br>Mail-Adresse|Kennzeichnung des Besitzers der<br>Kategorie|
|2|Authentisierungs-Niveau|Normal/Hoch|Authentisierungsniveau des Nutzers<br>bei der letzten Änderung|
|3|Datum und Zeit der letzten<br>Änderung|Datum & Zeit|Sekundengenau für jede Kategorie<br>(unabhängig von<br>Dateizuordnungen)|
|4|Autorisierter Nutzer|Kennung oder<br>zugehörige De-<br>Mail-Adresse||
|5|Mindest-Auth.-Niveau-Lesen|Normal/Hoch||
|6|Mindest-Auth.-Niveau –<br>Ändern/Löschen|Normal/Hoch||



_Tabelle 3: Metadaten der Kategorie (Teil 2)_ 

Der autorisierte Nutzer ist immer identisch mit der Nutzerkennung aus Tabelle 3. 

## **4.3 Meldungen** 

Meldungen sind Informationen der DA an den Nutzer und können in Abhängigkeit der Benutzerschnittstelle, die der Nutzer verwendet, unterschiedlich dargestellt und bekannt gemacht 

Bundesamt für Sicherheit in der Informationstechnik 

14 

4 Datenstrukturen 

werden. Bspw. können sie im Webbrowser dargestellt oder auch als Meldungs-Nachricht (siehe [TR DM FU PVD]) in das Postfach des Nutzers übermittelt werden. 

Bundesamt für Sicherheit in der Informationstechnik 

15 

5 Aktivitätsdiagramm 

## **5 Aktivitätsdiagramm** 

In diesem Abschnitt wird der funktionale Ablauf der DA für Upload, Download sowie zur Verwaltung und Suche von Dateien (in diesem Zusammenhang die Dokumente) in einem Aktivitätsdiagramm dargestellt. Eine Legende zu den Symbolen des Aktivitätsdiagramms findet sich in Abschnitt 8. Eine detaillierte technisch-funktionale Beschreibung der einzelnen Aktionen bzw. Schritte des Aktivitätsdiagramms erfolgt im Abschnitt 6. 

Bundesamt für Sicherheit in der Informationstechnik 

16 

5 Aktivitätsdiagramm 


![](markdown/tr/TR_De_Mail_DA_FU/TR_De_Mail_DA_FU.pdf-0017-01.png)


Bundesamt für Sicherheit in der Informationstechnik 

17 

## 5 Aktivitätsdiagramm 


![](markdown/tr/TR_De_Mail_DA_FU/TR_De_Mail_DA_FU.pdf-0018-01.png)


Bundesamt für Sicherheit in der Informationstechnik 

18 

5 Aktivitätsdiagramm 


![](markdown/tr/TR_De_Mail_DA_FU/TR_De_Mail_DA_FU.pdf-0019-01.png)


Bundesamt für Sicherheit in der Informationstechnik 

19 

5 Aktivitätsdiagramm 


![](markdown/tr/TR_De_Mail_DA_FU/TR_De_Mail_DA_FU.pdf-0020-01.png)


Bundesamt für Sicherheit in der Informationstechnik 

20 

5 Aktivitätsdiagramm 


![](markdown/tr/TR_De_Mail_DA_FU/TR_De_Mail_DA_FU.pdf-0021-01.png)


Bundesamt für Sicherheit in der Informationstechnik 

21 

## 5 Aktivitätsdiagramm 


![](markdown/tr/TR_De_Mail_DA_FU/TR_De_Mail_DA_FU.pdf-0022-01.png)


Bundesamt für Sicherheit in der Informationstechnik 

22 

6 Funktionale Beschreibung 

## **6 Funktionale Beschreibung** 

Im Folgenden werden die einzelnen Schritte des Aktivitätsdiagramms aus Abschnitt 5 für Upload, Download sowie zur Verwaltung und Suche von Dokumenten und Dateien beschrieben. Eine Beschreibung, wie die einzelnen Schritte strukturiert sind, findet sich in Abschnitt 9. Alternativ zu der unten dargestellten Schrittfolge kann eine Anmeldung auch vor Schritt 1 erfolgen, z.B. bei Web-basierten Anwendungen. Funktionen, die vom System wiederholt ausgeführt werden oder vom Nutzer interaktiv aufgerufen werden können, wenn er an seiner DA angemeldet ist, werden in Abschnitt 7 dargestellt. Die referenzierten Funktionen des Account-, Schadsoftware- und Zeitdienstes werden in [TR DM ACM FU] und [TR DM IT-BInfra FU] erläutert. 

## **6.1 Upload und Download von Dateien** 

## **6.1.1 Upload einer Datei in die DA** 

|**_Schritt 1_**|**_Datei(en) auswählen_**|
|---|---|
|Kurzbeschreibung|Der Nutzer wählt die Datei(en) im lokalen System, die er in der DA<br>speichern möchte.|
|Akteure|Nutzer|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Datei(en)<br>(Die ausgewählten Dateien können bereits durch den Nutzer<br>verschlüsselt worden sein)|
|Ergebnis|Datei(en) ausgewählt|
|Nachbedingung||
|Ablauf|Auswahl der Datei(en) in einem lokal verfügbaren Speicherbereich|
|Fehlerfälle|FC-01: Keine Auswahl getroffen|
|**_Schritt 2_**|<br>**_Entscheidungsknoten: Soll die Datei(en) verschlüsselt werden, bevor_**<br>**_sie auf dem Server gespeichert wird_**|
|Kurzbeschreibung|Durch den Nutzer wird entschieden, ob die Datei(en) verschlüsselt<br>werden soll.|
|ja|Schritt 3|
|nein|Schritt 4|
|**_Schritt 3_**|**_Datei(en) auf Nutzer-Seite verschlüsseln_**|
|Kurzbeschreibung|Die Datei(en) werden auf Seite des Nutzers verschlüsselt.|



Bundesamt für Sicherheit in der Informationstechnik 

23 

## 6 Funktionale Beschreibung 

|Akteure|Nutzer|
|---|---|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Verschlüsselungsmethode<br>Verschlüsselungsschlüssel des Nutzers<br>Datei(en)|
|Ergebnis|Verschlüsselte Datei(en)|
|Nachbedingung||
|Ablauf|Es wird mit einem auf dem Nutzer-System verfügbaren<br>Verschlüsselungstool eine Verschlüsselung der Datei vorgenommen.|
|Fehlerfälle|FC-01: kein geeigneter Verschlüsselungsschlüssel vorhanden<br>FC-02: Verschlüsselungsmethode wird nicht unterstützt|
|**_Schritt 4_**|<br>**_Kategorie(n) auswählen_**|
|Kurzbeschreibung|Es wird definiert, zu welchen Kategorie(n) und welcher Kategorie-<br>Ebene die Datei(en) zugeordnet werden sollen.<br>Hinweis: Welche Kategorien existieren, kann über die Suche-Funktion<br>in Abschnitt 6.3 erfahren werden.|
|Akteure|DA-Dienst|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Kategorie-Ebene<br>Kategorie(n)|
|Ergebnis|Zuordnung der Kategorie(n) bzw. der Kategorie-Ebene(n) getroffen.|
|Nachbedingung||
|Ablauf|Der Nutzer wählt die Kategorie(n) aus, die der heraufzuladenden<br>Datei(en) zugeordnet werden sollen.|
|Fehlerfälle|FC-01: Keine Kategorie(n) ausgewählt.<br>FC-02: Kategorie vom Typ Papierkorb kann nicht gewählt werden.|
|**_Schritt 5_**|<br>**_Datei(en) auf den De-Mail-Server übertragen_**|
|Kurzbeschreibung|Die Datei(en) werden an den DA-Dienst übertragen, der diese<br>entgegennimmt.|
|Akteure|Nutzer, DA-Dienst|
|Auslöser|Nutzer|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|



Bundesamt für Sicherheit in der Informationstechnik 

24 

6 Funktionale Beschreibung 

||Kategorie(n) und Datei(en) ausgewählt.|
|---|---|
|Input|Kategorie(n) und jeweilige Kategorie-Ebenen<br>Datei(en)|
|Ergebnis|Datei(en) auf Seite des Nutzers versendet.|
|Nachbedingung||
|Ablauf|Der Nutzer initiiert den Upload der Datei(en).<br>Der DA-Dienst nimmt die Daten entgegen.|
|Fehlerfälle|FC-01: DA hat die Datei(en) nicht angenommen.|
|**_Schritt 6_**|<br>**_Datei(en) auf dem De-Mail-Server empfangen_**|
|Kurzbeschreibung|Die Datei(en) werden durch den DA-Dienst empfangen.|
|Akteure|DA-Dienst|
|Auslöser|Nutzer|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut.|
|Input|Kategorie(n) und jeweilige Kategorie-Ebene<br>Datei(en)|
|Ergebnis|Datei(en) sind auf Seiten des DA-Dienstes entgegengenommen worden.|
|Nachbedingung||
|Ablauf|Der DA-Dienst nimmt die Daten entgegen.|
|Fehlerfälle|FC-01: Nutzer nicht am De-Mail-Konto angemeldet.|
|**_Schritt 7_**|<br>**_Prüfung zur Speicherung_**|
|Kurzbeschreibung|Der Upload wird hinsichtlich der Berechtigungen geprüft.|
|Akteure|DA-Dienst, Account-Dienst|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Kategorie(n) und zugehörige Kategorie-Ebenen<br>Datei(en)<br>Authentisierungsniveau des Nutzers|
|Ergebnis|Prüfungen sind abgeschlossen|
|Nachbedingung||
|Ablauf|**•**<br>Prüfung, ob die Kategorien in der jeweiligen Kategorie-Ebenen<br>existieren,<br>**•**<br>Prüfung, ob die Berechtigungen zum Schreiben gegeben sind,<br>**•**<br>Prüfung, ob die Datei(en) nicht bereits mit dem gleichen|



Bundesamt für Sicherheit in der Informationstechnik 

25 

## 6 Funktionale Beschreibung 

||Dateinamen in den Kategorien existieren,<br>**•**<br>Prüfung, ob ausreichend Speicher in der DA verfügbar ist,<br>**•**<br>Aufruf der Funktion 2.|
|---|---|
|Fehlerfälle|FC-01: Kategorien nicht existent<br>FC-02: Berechtigungen reichen nicht aus<br>FC-03: Dateiname ist bereits in einer der angegebenen Kategorien<br>existent<br>FC-04: Zu wenig Speicherplatz<br>FC-05: Datei(en) enthalten Malware|
|**_Schritt 8_**|<br>**_Entscheidungsknoten: positiv abgeschlossene Prüfung_**|
|Kurzbeschreibung|Existieren aus Schritt 7 keine Fehler, gilt die Prüfung als positiv<br>abgeschlossen.|
|ja|Schritt 10|
|nein|Schritt 9|
|**_Schritt 9_**|**_Fehlermeldung erstellen_**|
|Kurzbeschreibung|Es wird eine Fehlermeldung erstellt und an den Nutzer übermittelt.|
|Akteure|DA-Dienst|
|Auslöser|DA-Dienst|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input|Fehlercode|
|Ergebnis|Fehlermeldung ist erstellt und an den Nutzer gesandt.|
|Nachbedingung|Stopp|
|Ablauf|**•**<br>Der Fehlermeldung wird aus dem Fehlercode abgeleitet.<br>**•**<br>Die Fehlermeldung wird an den Nutzer gesandt.|
|Fehlerfälle||
|**_Schritt 10_**|**_Default-Berechtigungen setzen_**|
|Kurzbeschreibung|Für die Datei(en) werden die Default-Berechtigungen gesetzt.|
|Akteure|DA-Dienst, Account-Dienst|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Datei(en)<br>Authentisierungsniveau|
|Ergebnis|Default-Berechtigungen sind gesetzt.|



Bundesamt für Sicherheit in der Informationstechnik 

26 

6 Funktionale Beschreibung 

|Nachbedingung||
|---|---|
|Ablauf|Durch das System werden die Standard-Werte für die Berechtigungen<br>gesetzt:<br>**•**<br>Lesen – gestattet für angemeldeten Nutzer mit aktuellen<br>Authentisierungsniveau,<br>**•**<br>Schreiben – gestattet für angemeldeten Nutzer mit aktuellen<br>Authentisierungsniveau<br>**•**<br>Die Berechtigung des Dokuments muss mindestens dem<br>geforderten Authentisierungniveau der Kategorie entsprechen,<br>in die das Dokument eingefügt wird.|
|Fehlerfälle||
|**_Schritt 11_**|**_Hashwerte der Datei ermitteln_**|
|Kurzbeschreibung|Es werden die Hashwerte der Datei(en) ermittelt.|
|Akteure|DA-Dienst|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Datei(en)|
|Ergebnis|Ein Hashwert für die Metadaten wurde pro Datei ermittelt.|
|Nachbedingung||
|Ablauf|Es werden Hashwerte der Datei(en) ermittelt, der in den Metadaten der<br>jeweiligen Datei gespeichert wird.|
|Fehlerfälle||
|**_Schritt 12_**|**_Datei(en) durch den DMDA verschlüsseln_**|
|Kurzbeschreibung|Die Datei(en) werden mittels einem DMDA-Schlüssel verschlüsselt|
|Akteure|DA-Dienst|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Unverschlüsselte Datei(en), Verschlüsselungsschlüssel (DMDA)|
|Ergebnis|Die Datei(en) liegen nur noch als verschlüsselte Datei auf Seite des<br>DMDA vor.|
|Nachbedingung||
|Ablauf|**•**<br>Verschlüsselung der Datei(en)<br>**•**<br>Unverschlüsselte Datei(en) im Speicher löschen|
|Fehlerfälle|FC-01: kein DMDA-bezogenere Verschlüsselungsschlüssel vorhanden|



Bundesamt für Sicherheit in der Informationstechnik 

27 

## 6 Funktionale Beschreibung 

|**_Schritt 13_**|**_Datei(en) speichern_**|
|---|---|
|Kurzbeschreibung|Die verschlüsselten Datei(en) werden in der DA gespeichert.|
|Akteure|DA-Dienst|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Kategorie-Ebene, Kategorie(n)<br>Verschlüsselte Datei(en)|
|Ergebnis|Verschlüsselte Datei(en) im DA des Nutzers gespeichert.|
|Nachbedingung||
|Ablauf|**•**<br>Die Datei(en) werden im DA gespeichert.<br>**•**<br>Ist nur noch <10 % des Speicherplatzes innerhalb der DA frei,<br>ist eine Meldung an den Nutzer zu senden (Funktion 3).|
|Fehlerfälle||
|**_Schritt 14_**|**_Meta-Daten speichern_**|
|Kurzbeschreibung|Die Metadaten zu den Datei(en) werden gespeichert.|
|Akteure|DA-Dienst|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Dateizuordnung<br>Authentisierungsniveau<br>Berechtigungen<br>Datum und Zeit zum Zeitpunkt der Speicherung im De-Safe<br>Hashwerte der Datei(en)|
|Ergebnis|Die Metadaten wurden in der DA des Nutzers gespeichert und der<br>jeweiligen Datei(en) zugeordnet.|
|Nachbedingung|Funktion 1|
|Ablauf|**•**<br>Die einzelnen Attribute der Metadaten werden genommen und<br>als Metadatensatz gespeichert.<br>**•**<br>Es erfolgt eine Meldung an den Nutzer.|
|Fehlerfälle||
|**_Schritt 15_**|**_Meldung an den Nutzer_**|
|Kurzbeschreibung|Es wird eine Erfolgsmeldung an den Nutzer geschickt.|
|Akteure|DA-Dienst|



Bundesamt für Sicherheit in der Informationstechnik 

28 

6 Funktionale Beschreibung 

|Auslöser|DA-Dienst|
|---|---|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input|Erfolgsmeldung|
|Ergebnis|Eine Erfolgsmeldung wurde erstellt und an den Nutzer übermittelt.|
|Nachbedingung||
|Ablauf|**•**<br>Es wird eine Meldung erstellt.<br>**•**<br>Diese Meldung wird an den Nutzer übermittelt.|
|Fehlerfälle||
|**_Schritt 16_**|**_Meldung empfangen_**|
|Kurzbeschreibung|Eine Meldung wird auf Nutzerseite empfangen.|
|Akteure|Nutzer|
|Auslöser|DA-Dienst|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input|Meldung|
|Ergebnis|Die Meldung wurde auf Nutzerseite empfangen.|
|Nachbedingung||
|Ablauf|Die Meldung wird vom Nutzer entgegengenommen.|
|Fehlerfälle||
|**_Schritt 17_**|**_Meldung darstellen_**|
|Kurzbeschreibung|Die Meldung wird auf Seite des Nutzers dargestellt.|
|Akteure|Nutzer|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Meldung|
|Ergebnis|Die Darstellung der Meldung erfolgte.|
|Nachbedingung||
|Ablauf|**•**<br>Die Meldungsinformationen werden durch die Client-<br>Komponente interpretiert.<br>**•**<br>Die Darstellung erfolgt entsprechend den Inhalten der Meldung<br>(Fehler, Erfolg).|
|Fehlerfälle||



_Tabelle 4: Schritte zum Upload von Dateien_ 

Bundesamt für Sicherheit in der Informationstechnik 

29 

## 6 Funktionale Beschreibung 

## **6.1.2 Download von Dateien** 

|**_Schritt 18_**|**_Herunterzuladende Datei(en) auswählen_**|
|---|---|
|Kurzbeschreibung|Der Nutzer wählt die Dateien, die aus seiner DA auf den Speicher des<br>Nutzersystems als Kopie heruntergeladen werden sollen.|
|Akteure|Nutzer|
|Auslöser|Nutzer|
|Vorbedingung|Zusammenstellung der Liste, ggf. über die Suche-Funktion (siehe 6.3)|
|Input|Datei(en) und die zugehörigen Kategorie-Ebenen und Kategorien|
|Ergebnis|Liste der herunterzuladenden Dateien|
|Nachbedingung||
|Ablauf|Erstellung der Liste der herunterzuladenden Dateien mit Adressierung<br>(Kategorie)|
|Fehlerfälle|FC-01: Liste ist leer|
|**_Schritt 19_**|**_Liste der herunterzuladenden Dateien übermitteln_**|
|Kurzbeschreibung|Die Liste wird durch den Nutzer an den DA-Dienst übergeben.|
|Akteure|Nutzer, DA-Dienst|
|Auslöser|Nutzer|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input|Liste der herunterzuladenden Dateien mit Adressierung (Kategorie)|
|Ergebnis|Die Liste der herunterzuladenden Dateien wurde an den DA-Dienst<br>übergeben.|
|Nachbedingung||
|Ablauf|Der Nutzer übergibt die Liste an den DA-Dienst.|
|Fehlerfälle|FC-01: keine Liste übermittelt<br>FC-02: Liste ist leer|
|**_Schritt 20_**|**_Liste der herunterzuladenden Dateien empfangen_**|
|Kurzbeschreibung|Die Liste wird durch den DA-Dienst empfangen.|
|Akteure|DA-Dienst|
|Auslöser|Nutzer|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input|Liste der herunterzuladenden Dateien mit Adressierung (Kategorie)|
|Ergebnis|Die Liste der herunterzuladenden Dateien wurde vom DA-Dienst|



Bundesamt für Sicherheit in der Informationstechnik 

30 

6 Funktionale Beschreibung 

||empfangen.|
|---|---|
|Nachbedingung||
|Ablauf|Die Liste wird durch den DA-Dienst zur weiteren Verarbeitung<br>empfangen.|
|Fehlerfälle|FC-01: keine Liste übermittelt<br>FC-02: Liste ist leer<br>FC-03: Nutzer am De-Mail-Konto nicht angemeldet|
|**_Schritt 21_**|<br>**_Möglichkeit zum Herunterladen prüfen_**|
|Kurzbeschreibung|Die Liste zum Herunterladen von Dateien wird hinsichtlich der<br>Berechtigungen geprüft.|
|Akteure|DA-Dienst, Account-Dienst|
|Auslöser|Nutzer|
|Vorbedingung|Liste der herunterzuladenden Dateien wurde an den DA-Dienst<br>übertragen.|
|Input|Liste der herunterzuladenden Dateien<br>Authentisierungsniveau|
|Ergebnis|Prüfungen sind abgeschlossen.|
|Nachbedingung||
|Ablauf|**•**<br>Prüfung, ob die Dateien in den jeweiligen angegebenen<br>Kategorie-Ebene existieren<br>**•**<br>Prüfung, ob die Berechtigung zum Lesen mit dem<br>Authentisierungsniveau des angemeldeten Nutzers gegeben ist<br>**•**<br>Aufruf von Funktion 2|
|Fehlerfälle|FC-01: Datei nicht existent<br>FC-02: Berechtigungen reichen nicht aus<br>FC-03: Datei enthält Malware|
|**_Schritt 22_**|**_Entscheidungsknoten: positiv abgeschlossene Prüfung_**|
|Kurzbeschreibung|Existieren aus Schritt 21 keine Fehler, gilt die Prüfung als positiv<br>abgeschlossen.|
|ja|Schritt 24|
|nein|Schritt 23|
|**_Schritt 23_**|**_Fehler- bzw. Warnmeldung an den Nutzer_**|
|Kurzbeschreibung|Im Fall von FC-01 und FC-02 wird eine Fehlermeldung erstellt und an<br>den Nutzer übermittelt.<br>Im Fall von FC-03 Warnmeldung mit Auswahl für den Nutzer, ob die|



Bundesamt für Sicherheit in der Informationstechnik 

31 

## 6 Funktionale Beschreibung 

||Malware-infizierte Datei trotz der Gefahren heruntergeladen werden<br>soll.|
|---|---|
|Akteure|DA-Dienst|
|Auslöser|DA-Dienst|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input|Fehlercode|
|Ergebnis|Eine Meldung mit der Fehlerbeschreibung wurde erstellt.|
|Nachbedingung|Bei FC-01, FC-02 und bei Nutzer-bestätigten Abbruch bei FC-03:<br>Stopp<br>Bei Nutzer-bestätigten Fortführung des Downloads: Schritt 24|
|Ablauf|**•**<br>Bei FC01-, FC-02:<br>**◦**<br>Das System erstellt eine Fehlermeldung.<br>**◦**<br>Das System übermittelt diese Fehlermeldung an den Nutzer.<br>**•**<br>Bei FC-03:<br>**◦**<br>Das System erstellt eine Warnmeldung mit der Wahl zur<br>Fortführung des Downloads oder Abbruch des Downloads<br>durch den Nutzer<br>**◦**<br>Das System übermittelt diese Warnmeldung an den Nutzer.<br>**◦**<br>Das System wertet die Entscheidung des Nutzers aus.<br>**◦**<br>Das System führt die entsprechende Nachbedingung aus.|
|Fehlerfälle|FC-01: Fehlermeldung wird vom Nutzer-System nicht angenommen.|
|**_Schritt 24_**|<br>**_Entschlüsseln der Datei durch den DMDA_**|
|Kurzbeschreibung|Die durch den DMDA verschlüsselte Datei wird durch den DMDA<br>entschlüsselt.|
|Akteure|DA-Dienst|
|Auslöser|Nutzer|
|Vorbedingung|Positiv abgeschlossene Prüfung in Schritt 22|
|Input|Verschlüsselte Datei, Entschlüsselungsschlüssel des DMDA|
|Ergebnis|Entschlüsselte Datei für die Übermittlung an den Nutzer, die in der DA<br>gespeicherte Datei bleibt verschlüsselt|
|Nachbedingung||
|Ablauf|Entschlüsselung der Datei|
|Fehlerfälle|FC-01: Kein DMDA-bezogener Entschlüsselungsschlüssel vorhanden|
|**_Schritt 25_**|<br>**_Integrität prüfen_**|



Bundesamt für Sicherheit in der Informationstechnik 

32 

6 Funktionale Beschreibung 

|Kurzbeschreibung|Es wird geprüft, ob die Dateien dem Zustand entsprechen, in dem sie<br>bei der Speicherung durch den Nutzer übergeben wurden.|
|---|---|
|Akteure|DA-Dienst|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Herunterzuladende Dateien und zugehörige Metadaten|
|Ergebnis|Abgeschlossene Verifikation hinsichtlich der Integrität der Dateien|
|Nachbedingung||
|Ablauf|Das System erstellt den Hashwert der herunterzuladenden Datei und<br>vergleicht diesen mit dem Hashwert, der bei der Speicherung der Datei<br>in den Metadaten erfasst wurde.|
|Fehlerfälle|FC-01: Integrität nicht gegeben, Datei oder Metadaten-Eintrag wurde<br>geändert|
|**_Schritt 26_**|**_Dateien an den Nutzer-Client übermitteln_**|
|Kurzbeschreibung|Die Dateien, die zum Herunterladen angefragt sind, werden an den<br>Nutzer-Client übertragen.|
|Akteure|DA-Dienst, Nutzer|
|Auslöser|Nutzer|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input|Dateien und zugehörige Kategorie|
|Ergebnis|Dateien wurden an das Client-System transferiert.|
|Nachbedingung||
|Ablauf|Es werden die Dateien inkl. der Kategorien an das Client-System<br>transferiert.|
|Fehlerfälle|FC-01: Daten werden vom Client nicht angenommen|
|**_Schritt 27_**|<br>**_Dateien auf dem Nutzer-Client empfangen_**|
|Kurzbeschreibung|Die Dateien, die zum Herunterladen angefragt sind, werden auf Seite<br>des Nutzer-Client empfangen.|
|Akteure|Nutzer|
|Auslöser|Nutzer|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input|Dateien und zugehörige Kategorie|
|Ergebnis|Dateien wurden auf dem Client-System gespeichert|
|Nachbedingung||



Bundesamt für Sicherheit in der Informationstechnik 

33 

## 6 Funktionale Beschreibung 

|Ablauf|Das Client-System übernimmt die Daten oder Meldungen in den<br>Speicher.|
|---|---|
|Fehlerfälle||
|**_Schritt 28_**|**_Entscheidungsknoten: Ist die Datei auf dem Nutzer-Client_**<br>**_verschlüsselt worden_**|
|Kurzbeschreibung|Prüfung, ob die Datei durch den Nutzer vor der Übermittlung an den<br>DA-Dienst verschlüsselt wurde.|
|ja|Schritt 29|
|nein|Schritt 30|
|**_Schritt 29_**|**_Dateien auf dem Nutzer-Client entschlüsseln_**|
|Kurzbeschreibung|Die Dateien, die durch den Nutzer verschlüsselt an den DA-Dienst<br>übertragen worden sind, werden auf dem Client wieder entschlüsselt.|
|Akteure|Nutzer|
|Auslöser|Nutzer|
|Vorbedingung|Die Daten waren vor der Speicherung in der DA verschlüsselt.|
|Input|Zu entschlüsselnde Datei<br>Entschlüsselungsmethode<br>Entschlüsselungsschlüssel des Nutzers|
|Ergebnis|Dateien wurden wieder entschlüsselt und liegen unverschlüsselt vor|
|Nachbedingung||
|Ablauf|**•**<br>Entschlüsselung der verschlüsselten Datei<br>**•**<br>Löschen der verschlüsselten Datei|
|Fehlerfälle|FC-01: Ungültiger Nutzer-bezogener Entschlüsselungsschlüssel<br>FC-02: Nicht unterstützte Entschlüsselungsmethode|
|**_Schritt 30_**|<br>**_Dateien auf dem Datenträger des Nutzers speichern_**|
|Kurzbeschreibung|Die heruntergeladenen und unverschlüsselten Dateien werden auf dem<br>Datenträger des Nutzers gespeichert.|
|Akteure|Nutzer|
|Auslöser|Nutzer|
|Vorbedingung|Schritt 29 (bei verschlüsselten Dateien) oder Schritt 28 (bei<br>unverschlüsselten Dateien)|
|Input|Heruntergeladene Dateien und zugehörige Kategorien<br>Datenträger des Nutzers und Download-Verzeichnisses|
|Ergebnis|Dateien sind auf dem Datenträger innerhalb des Download-<br>Verzeichnisses des Nutzers gespeichert. (Wenn die Datei durch den|



Bundesamt für Sicherheit in der Informationstechnik 

34 

6 Funktionale Beschreibung 

||Nutzer vor dem Hochladen bereits verschlüsselt wurde, muss der<br>Nutzer die Datei noch entschlüsseln)|
|---|---|
|Nachbedingung||
|Ablauf|**•**<br>Der Nutzer gibt den Datenträger und das Download-Verzeichnis<br>an.<br>**•**<br>Das Client-System speichert die Dateien im Download-<br>Verzeichnis ab.|
|Fehlerfälle|FC-01: Datenträger existiert nicht<br>FC-02: Download-Verzeichnis existiert nicht<br>FC-03: Datei existiert bereits im entsprechenden Datenträger-<br>Verzeichnis|



_Tabelle 5: Schritte zum Download von Dateien_ 

## **6.2 Verwaltung von Dateien/Kategorien** 

## **6.2.1 Erstellen einer Kategorie** 

|**_Schritt 31_**|**_Antrag für eine neue Kategorie erstellen_**|
|---|---|
|Kurzbeschreibung|Der Nutzer beantragt eine beliebige neue Kategorie in seiner DA.|
|Akteure|Nutzer|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Kategorie-Bezeichnung<br>Kategorie-Ebene (Default: Wurzel im DA des Nutzers)|
|Ergebnis|Antrag für eine neue Kategorie wurde erstellt|
|Nachbedingung||
|Ablauf|**•**<br>Aufruf der Funktion zum Erstellen von Kategorien im DA<br>**•**<br>Angabe der Bezeichnung und weiterer Daten zur Kategorie|
|Fehlerfälle|FC-01: Keine Bezeichnung angegeben<br>FC-02: Ungültige Bezeichnung|
|**_Schritt 32_**|<br>**_Antrag für neue Kategorie übermitteln_**|
|Kurzbeschreibung|Der Antrag für neue Kategorie wurde übermittelt.|
|Akteure|Nutzer|
|Auslöser|Nutzer|



Bundesamt für Sicherheit in der Informationstechnik 

35 

6 Funktionale Beschreibung 

|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|---|---|
|Input|Antrag (Kategorie-Bezeichnung, Kategorie-Ebene)|
|Ergebnis|Antrag wurde an den DA-Dienst übergeben|
|Nachbedingung||
|Ablauf|Antrag wurde an den DA-Dienst übermittelt|
|Fehlerfälle|FC-01: Antrag wird vom DA-Dienst nicht angenommen|
|**_Schritt 33_**|<br>**_Antrag für neue Kategorie entgegengenommen_**|
|Kurzbeschreibung|Der DA-Dienst nimmt den Antrag für eine neue Kategorie entgegen.|
|Akteure|DA-Dienst|
|Auslöser|Nutzer|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input|Antrag (Kategorie-Bezeichnung, Kategorie-Ebene)|
|Ergebnis|Antrag wurde durch den DA-Dienst entgegengenommen.|
|Nachbedingung||
|Ablauf|Antrag wird durch den DA-Dienst entgegengenommen.|
|Fehlerfälle|FC-01: Nutzer nicht am De-Mail-Konto angemeldet|
|**_Schritt 34_**|<br>**_Beantragte Daten prüfen_**|
|Kurzbeschreibung|Der DA-Dienst prüft den Antrag.|
|Akteure|DA-Dienst, Account-Dienst|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Kategorie-Bezeichnung<br>Kategorie-Ebene<br>Authentisierungsniveau des Nutzers<br>Weitere Metadaten zur eigenen Berechtigung|
|Ergebnis|Kategorie verifiziert|
|Nachbedingung||
|Ablauf|**•**<br>Entgegennahme der Antragsdaten<br>**•**<br>Prüfung, ob die Kategorie-Ebene existiert<br>**•**<br>Prüfung, ob die Schreibrechte innerhalb der Kategorie-Ebene<br>bei genutztem Authentisierungsniveau ausreichen<br>**•**<br>Prüfung, ob bereits die gleiche Kategorie-Bezeichnung in der<br>Kategorie-Ebene existiert|



Bundesamt für Sicherheit in der Informationstechnik 

36 

6 Funktionale Beschreibung 

|Fehlerfälle|FC-01: Kategorie-Bezeichnung in der Kategorie-Ebene schon<br>vorhanden<br>FC-02: angegebene Kategorie-Ebene existiert nicht<br>FC-03: Keine Schreibberechtigung bei genutztem<br>Authentisierungsniveau|
|---|---|
|**_Schritt 35_**|**_Entscheidungsknoten: positiv abgeschlossene Prüfung_**|
|Kurzbeschreibung|Existieren aus Schritt 34 keine Fehler, gilt die Prüfung als positiv<br>abgeschlossen.|
|ja|Schritt 37|
|nein|Schritt 36|
|**_Schritt 36_**|**_Fehlermeldung an den Nutzer senden_**|
|Kurzbeschreibung|Es wird eine Fehlermeldung erstellt und an den Nutzer übermittelt.|
|Akteure|DA-Dienst|
|Auslöser|DA-Dienst|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input|Fehlercode|
|Ergebnis|Eine Meldung mit der Fehlerbeschreibung wurde erstellt.|
|Nachbedingung|Stopp|
|Ablauf|**•**<br>Das System erstellt eine Fehlermeldung.<br>**•**<br>Das System übermittelt diese Fehlermeldung an den Nutzer.|
|Fehlerfälle||
|**_Schritt 37_**|**_Kategorie erstellen_**|
|Kurzbeschreibung|Im DA wird eine neue Kategorie erstellt.|
|Akteure|DA-Dienst|
|Auslöser|Nutzer|
|Vorbedingung|Schritt 34 ohne Fehlermeldung|
|Input|Kategorie-Bezeichnung<br>Kategorie-Ebene<br>Authentisierungsniveau<br>Weitere Metadaten zur eigenen Berechtigung|
|Ergebnis|Kategorie existiert|
|Nachbedingung|Funktion 1|
|Ablauf|**•**<br>Erstellung der Meta-Daten|



Bundesamt für Sicherheit in der Informationstechnik 

37 

6 Funktionale Beschreibung 

||**•**<br>Anlegen der Kategorie<br>**•**<br>Das Authentisierungsniveau muss mindestens dem der<br>übergeordneten Kategorie entsprechen. In Unterkategorien kann<br>das geforderte Authentisierungsniveau nur erhöht werden.<br>**•**<br>Meldung an den Nutzer|
|---|---|
|Fehlerfälle||
|**_Schritt 38_**|**_Meldung an den Nutzer_**|
|Kurzbeschreibung|Es wird eine Meldung erstellt und an den Nutzer übermittelt.|
|Akteure|DA-Dienst|
|Auslöser|DA-Dienst|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input|Erfolgsmeldung|
|Ergebnis|Eine Meldung wurde erstellt.|
|Nachbedingung||
|Ablauf|**•**<br>Das System erstellt eine Meldung.<br>**•**<br>Das System übermittelt diese Meldung an den Nutzer.|
|Fehlerfälle||
|**_Schritt 39_**|**_Meldung empfangen_**|
|Kurzbeschreibung|Es wird eine Meldung durch den Nutzer empfangen.|
|Akteure|Nutzer|
|Auslöser|Nutzer|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input||
|Ergebnis|Meldung wurde auf Seite des Nutzers empfangen.|
|Nachbedingung||
|Ablauf|Empfang der Meldung des DA-Dienstes durch den Nutzer|
|Fehlerfälle||
|**_Schritt 40_**|**_Meldung darstellen_**|
|Kurzbeschreibung|Die Inhalte der Meldung|
|Akteure|Nutzer|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Meldungsinhalte|



Bundesamt für Sicherheit in der Informationstechnik 

38 

6 Funktionale Beschreibung 

|Ergebnis|Die Meldung wurde dem Nutzer dargestellt.|
|---|---|
|Nachbedingung||
|Ablauf|Die vom DA-Dienst empfangene Nachricht wird dem Benutzer nach<br>Aufarbeitung dargestellt.|
|Fehlerfälle||



_Tabelle 6: Schritte zum Erstellen einer Kategorie_ 

## **6.2.2 Umbenennen von Dateien/Kategorien** 

|**_Schritt 41_**|**_Antrag zum Umbenennen einer Datei/Kategorie erstellen_**|
|---|---|
|Kurzbeschreibung|Der Nutzer beantragt eine Umbenennung einer in seiner DA<br>existierenden Datei/Kategorie|
|Akteure|Nutzer|
|Auslöser|Nutzer|
|Vorbedingung|Kenntnis der umzubenennenden Datei/Kategorie und der Kategorie-<br>Ebene, ggf. über die Suche-Funktion (siehe 6.3)|
|Input|Datei/Kategorie-Bezeichnung_alt<br>Kategorie-Ebene<br>Datei/Kategorie-Bezeichnung_neu|
|Ergebnis|Antrag für die Umbenennung einer Datei/Kategorie wurde erstellt|
|Nachbedingung||
|Ablauf|**•**<br>Angabe der umzubenennenden Datei/Kategorie und der<br>Kategorie-Ebene<br>**•**<br>Angabe der neuen Bezeichnung|
|Fehlerfälle|FC-01: Fehlende neue Bezeichnung<br>FC-02: Fehlende Bezeichnung der umzubenennenden Datei/Kategorie|
|**_Schritt 42_**|<br>**_Antrag zum Umbenennen einer Datei/Kategorie übermitteln_**|
|Kurzbeschreibung|Antrag zum Umbenennen einer Datei/Kategorie an den DA-Dienst<br>übermitteln|
|Akteure|Nutzer|
|Auslöser|Nutzer|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input|Antrag|
|Ergebnis|Antrag wurde an den DA-Dienst übergeben.|



Bundesamt für Sicherheit in der Informationstechnik 

39 

## 6 Funktionale Beschreibung 

|Nachbedingung||
|---|---|
|Ablauf|Antrag wurde an den DA-Dienst übermittelt.|
|Fehlerfälle||
|**_Schritt 43_**|**_Antrag zum Umbenennen einer Datei/Kategorie empfangen_**|
|Kurzbeschreibung|Der Antrag zum Umbenennen einer Datei/Kategorie wird vom DA-<br>Dienst empfangen.|
|Akteure|DA-Dienst|
|Auslöser|Nutzer|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input|Antrag|
|Ergebnis|Antrag ist entgegengenommen.|
|Nachbedingung||
|Ablauf|Der Antrag wird vom DA-Dienst entgegengenommen.|
|Fehlerfälle|FC-01: Nutzer nicht am De-Mail-Konto angemeldet|
|**_Schritt 44_**|<br>**_Antrag zur Umbenennung einer Datei/Kategorie prüfen_**|
|Kurzbeschreibung|Es wird geprüft, ob der Antrag zur Umbenennung der Datei/Kategorie<br>angenommen werden kann.|
|Akteure|DA-Dienst, Account-Dienst|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Datei/Kategorie-Bezeichnung_alt<br>Kategorie-Ebene<br>Datei/Kategorie-Bezeichnung_neu<br>Authentisierungsniveau|
|Ergebnis|Antrag wurde geprüft|
|Nachbedingung||
|Ablauf|**•**<br>Prüfung der Berechtigung zur Umbenennung<br>**•**<br>Prüfung, ob die umzubenennende Datei/Kategorie existiert<br>**•**<br>Prüfung, ob die neue Datei/Kategorie bereits existiert<br>**•**<br>Prüfung, ob die umzubenennende Kategorie vom Typ<br>Papierkorb ist|
|Fehlerfälle|FC-01: die umzubenennende Datei/Kategorie existiert nicht<br>FC-02: der gewünschte Datei-/Kategoriename existiert bereits in der<br>Kategorieebene|



Bundesamt für Sicherheit in der Informationstechnik 

40 

6 Funktionale Beschreibung 

||FC-03: Funktion ist bei dem genutzten Authentisierungsniveau nicht<br>gestattet<br>FC-04: Kategorie vom Typ Papierkorb kann nicht umbenannt werden|
|---|---|
|**_Schritt 45_**|<br>**_Entscheidungsknoten: positiv abgeschlossene Prüfung_**|
|Kurzbeschreibung|Existieren aus Schritt 44 keine Fehler, gilt die Prüfung als positiv<br>abgeschlossen.|
|ja|Schritt 47|
|nein|Schritt 46|
|**_Schritt 46_**|**_Fehlermeldung an den Nutzer_**|
|Kurzbeschreibung|Es wird eine Fehlermeldung erstellt und an den Nutzer übermittelt.|
|Akteure|DA-Dienst|
|Auslöser|DA-Dienst|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input|Fehlercode|
|Ergebnis|Eine Meldung mit der Fehlerbeschreibung wurde erstellt.|
|Nachbedingung|Stopp|
|Ablauf|**•**<br>Das System erstellt eine Fehlermeldung.<br>**•**<br>Das System übermittelt diese Fehlermeldung an den Nutzer.|
|Fehlerfälle||
|**_Schritt 47_**|**_Aktivierung der Umbenennung einer Datei/Kategorie_**|
|Kurzbeschreibung|Die Datei / Kategorie wird umbenannt.|
|Akteure|DA-Dienst|
|Auslöser|Nutzer|
|Vorbedingung|Positiv abgeschlossenen Prüfung in Schritt 45|
|Input|Datei/Kategorie-Bezeichnung_alt<br>Kategorie-Ebene<br>Datei/Kategorie-Bezeichnung_neu<br>Authentisierungsniveau|
|Ergebnis|Datei/Kategorie existiert mit neuem Namen|
|Nachbedingung|Funktion 1|
|Ablauf|Die Metadaten zur Datei/Kategorie werden geändert.<br>Es erfolgt eine Meldung an den Nutzer.<br>Hinweis: Sollte der Dateiname der gespeicherten Datei nicht über Meta-|



Bundesamt für Sicherheit in der Informationstechnik 

41 

## 6 Funktionale Beschreibung 

||Daten, sondern direkt an der gespeicherten Datei geändert werden, ist<br>vor der Umbenennung eine DMDA-bezogenen Entschlüsselung der<br>Datei und nach der Umbenennung eine DMDA-bezogene<br>Verschlüsselung der Datei mit anschließender Löschung der<br>entschlüsselten Datei zu realisieren.|
|---|---|
|Fehlerfälle||
|**_Schritt 48_**|**_Meldung an den Nutzer_**|
|Kurzbeschreibung|Es wird eine Meldung erstellt und an den Nutzer übermittelt.|
|Akteure|DA-Dienst|
|Auslöser|DA-Dienst|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input|Erfolgsmeldung|
|Ergebnis|Eine Meldung wurde erstellt.|
|Nachbedingung||
|Ablauf|**•**<br>Das System erstellt eine Meldung.<br>**•**<br>Das System übermittelt diese Meldung an den Nutzer.|
|Fehlerfälle||
|**_Schritt 49_**|**_Meldung empfangen_**|
|Kurzbeschreibung|Es wird eine Meldung durch den Nutzer empfangen.|
|Akteure|Nutzer|
|Auslöser|Nutzer|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input||
|Ergebnis|Meldung wurde auf Seite des Nutzers empfangen.|
|Nachbedingung||
|Ablauf|Empfang der Meldung des DA-Dienstes durch den Nutzer|
|Fehlerfälle||
|**_Schritt 50_**|**_Meldung darstellen_**|
|Kurzbeschreibung|Die Inhalte der Meldung werden dem Nutzer dargestellt.|
|Akteure|Nutzer|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Meldungsinhalte|



Bundesamt für Sicherheit in der Informationstechnik 

42 

6 Funktionale Beschreibung 

|Ergebnis|Die Meldung wurde dem Nutzer dargestellt.|
|---|---|
|Nachbedingung||
|Ablauf|Die vom DA-Dienst empfangene Nachricht wird dem Benutzer nach<br>Aufarbeitung dargestellt.|
|Fehlerfälle||



_Tabelle 7: Schritte zum Umbenennen_ 

## **6.2.3 Löschen von Dateien/Kategorien** 

|**_Schritt 51_**|**_Antrag auf Löschung einer Datei/Kategorie erstellen_**|
|---|---|
|Kurzbeschreibung|Der Nutzer wählt die Dateien/Kategorien, die in seiner DA gelöscht<br>werden sollen.|
|Akteure|Nutzer|
|Auslöser|Nutzer|
|Vorbedingung|Zusammenstellung der Liste, ggf. über die Suche-Funktion (siehe 6.3)|
|Input|Bei Dateien: Datei(en) und die zugehörigen Kategorie-Ebenen und Bei<br>Kategorien: Kategorie-Bezeichnung und Kategorie-Ebene|
|Ergebnis|Liste der zu löschenden Dateien/Kategorien|
|Nachbedingung||
|Ablauf|Erstellung der Liste der zu löschenden Dateien bzw. Kategorien|
|Fehlerfälle|FC-01: Liste ist leer<br>FC-02: Keine Bezeichnung angegeben<br>FC-03: Ungültige Bezeichnung|
|**_Schritt 52_**|<br>**_Liste der zu löschenden Dateien/Kategorien übermitteln_**|
|Kurzbeschreibung|Antrag zum Löschen einer Kategorie an den DA-Dienst übermitteln|
|Akteure|Nutzer, DA-Dienst|
|Auslöser|Nutzer|
|Vorbedingung|Gegenseitig authentisierter und verschlüsselter Kommunikationskanal<br>aufgebaut|
|Input|Liste der zu löschenden Dateien/Kategorien|
|Ergebnis|Die Liste der zu löschenden Dateien/Kategorien wurde an den DA-<br>Dienst übergeben|
|Nachbedingung||
|Ablauf|Liste wurde an den DA-Dienst übermittelt.|



Bundesamt für Sicherheit in der Informationstechnik 

43 

## 6 Funktionale Beschreibung 

|Fehlerfälle||
|---|---|
|**_Schritt 53_**|**_Liste der zu löschenden Dateien/Kategorien empfangen_**|
|Kurzbeschreibung|Die Liste wird vom DA-Dienst empfangen.|
|Akteure|DA-Dienst|
|Auslöser|Nutzer|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input|Liste der zu löschenden Dateien/Kategorien|
|Ergebnis|Die Liste der zu löschenden Dateien/Kategorien wurde von dem DA-<br>Dienst empfangen.|
|Nachbedingung||
|Ablauf|Die Liste wird vom DA-Dienst entgegengenommen.|
|Fehlerfälle|FC-01: Nutzer nicht am De-Mail-Konto angemeldet<br>FC-02: Liste ist leer|
|**_Schritt 54_**|**_Antrag zum Löschen prüfen_**|
|Kurzbeschreibung|Die in der Liste angegebenen Dateien/Kategorien werden hinsichtlich<br>der Berechtigungen zum Löschen geprüft.|
|Akteure|DA-Dienst, Account-Dienst|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Liste der zu löschenden Dateien/Kategorien<br>Authentisierungsniveau des Nutzers|
|Ergebnis|Prüfungen sind abgeschlossen.|
|Nachbedingung||
|Ablauf|Für Dateien<br>**•**<br>Prüfung, ob die Datei(en) in der jeweiligen angegebenen<br>Kategorie-Ebene existiert.<br>**•**<br>Prüfung, ob die Berechtigung zum Löschen mit dem<br>Authentisierungsniveau des Nutzers gegeben ist.<br>Für Kategorien<br>**•**<br>Prüfung, ob die zu löschende Kategorie existiert.<br>**•**<br>Prüfung, ob die Löschung bei dem Authentisierungsniveau<br>gestattet ist.<br>**•**<br>Prüfung, ob keine weiteren Kategorien in der Kategorie<br>existieren.|



Bundesamt für Sicherheit in der Informationstechnik 

44 

6 Funktionale Beschreibung 

||**•**<br>Prüfung, ob der Kategorie keine Dateien zugeordnet sind.<br>**•**<br>Prüfung, ob die zu löschende Kategorie vom Typ Papierkorb ist.|
|---|---|
|Fehlerfälle|FC-01: Berechtigungen reichen nicht aus<br>FC-02: Kategorie/Datei existiert nicht<br>FC-03: Dateien sind der Kategorie zugeordnet<br>FC-04: Es gibt Kategorien in dieser Kategorie<br>FC-05: Kategorie vom Typ Papierkorb kann nicht gelöscht werden|
|**_Schritt 55_**|<br>**_Entscheidungsknoten: positiv abgeschlossene Prüfung_**|
|Kurzbeschreibung|Existieren aus Schritt 54 keine Fehler, gilt die Prüfung als positiv<br>abgeschlossen.|
|ja|Schritt 57|
|nein|Schritt 56|
|**_Schritt 56_**|**_Fehlermeldung an den Nutzer_**|
|Kurzbeschreibung|Es wird eine Fehlermeldung erstellt und an den Nutzer übermittelt.|
|Akteure|DA-Dienst|
|Auslöser|DA-Dienst|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input|Fehlercode|
|Ergebnis|Eine Meldung mit der Fehlerbeschreibung wurde erstellt.|
|Nachbedingung|Stopp|
|Ablauf|**•**<br>Das System erstellt eine Fehlermeldung.<br>**•**<br>Das System übermittelt diese Fehlermeldung an den Nutzer.|
|Fehlerfälle||
|**_Schritt 57_**|**_Dateien/Kategorien löschen_**|
|Kurzbeschreibung|Die Dateien, die in der Liste der zu löschenden Dateien enthalten sind,<br>und die zugehörigen Metadaten werden in die Kategorie Papierkorb<br>verschoben. Dateien der Kategorie Papierkorb werden<br>unwiederbringlich gelöscht. Zu löschende Kategorien werden entfernt.|
|Akteure|DA-Dienst|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Liste zu löschender Dateien/Kategorien|
|Ergebnis|Für Dateien: Dateien sind der Kategorie Papierkorb zugeordnet, oder<br>gelöscht und lassen sich nicht wiederherstellen.|



Bundesamt für Sicherheit in der Informationstechnik 

45 

6 Funktionale Beschreibung 

||Für Kategorien: Kategorie existiert nicht mehr.|
|---|---|
|Nachbedingung|Funktion 1|
|Ablauf|Für Dateien:<br>**•**<br>Das System löscht die in der Liste angegebenen Dateien<br>innerhalb des DA des angemeldeten Benutzers, wenn diese der<br>Kategorie  Papierkorb zugeordnet waren. Die zugehörigen<br>Metadaten der Dateien werden ebenfalls gelöscht.<br>oder<br>**•**<br>Das System setzt für die zu löschenden Dateien, die bisher nicht<br>der Kategorie Papierkorb zugeordnet waren, die Kategorie<br>Papierkorb und entfernt Zuordnungen zu anderen Kategorien.<br>Für Kategorien:<br>**•**<br>Die Kategorie wird mit den zugehörigen Metadaten gelöscht.|
|Fehlerfälle||
|**_Schritt 58_**|**_Meldung an den Nutzer_**|
|Kurzbeschreibung|Es wird eine Meldung erstellt und an den Nutzer übermittelt.|
|Akteure|DA-Dienst|
|Auslöser|DA-Dienst|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input|Erfolgsmeldung|
|Ergebnis|Eine Meldung wurde erstellt.|
|Nachbedingung||
|Ablauf|**•**<br>Das System erstellt eine Meldung.<br>**•**<br>Das System übermittelt diese Meldung an den Nutzer.|
|Fehlerfälle|FC-01: Meldung wird vom Nutzer-System nicht angenommen.|
|**_Schritt 59_**|<br>**_Meldung empfangen_**|
|Kurzbeschreibung|Es wird eine Meldung durch den Nutzer empfangen.|
|Akteure|Nutzer|
|Auslöser|Nutzer|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input||
|Ergebnis|Meldung wurde auf Seite des Nutzers empfangen.|
|Nachbedingung||
|Ablauf|Empfang der Meldung des DA-Dienstes durch den Nutzer.|



Bundesamt für Sicherheit in der Informationstechnik 

46 

6 Funktionale Beschreibung 

|Fehlerfälle||
|---|---|
|**_Schritt 60_**|**_Meldung darstellen_**|
|Kurzbeschreibung|Die Inhalte der Meldung werden dem Nutzer dargestellt.|
|Akteure|Nutzer|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Meldungsinhalte|
|Ergebnis|Die Meldung wurde dem Nutzer dargestellt.|
|Nachbedingung||
|Ablauf|Die vom DA-Dienst empfangene Nachricht wird dem Benutzer nach<br>Aufarbeitung dargestellt.|
|Fehlerfälle||



_Tabelle 8: Schritte zum Löschen_ 

## **6.2.4 Ändern der Berechtigungen für Dokumente und Kategorien** 

|**_Schritt 61_**|**_Antrag auf Änderung der Berechtigung erstellen_**|
|---|---|
|Kurzbeschreibung|Der Nutzer beantragt eine Änderung einer Berechtigung von Dateien/<br>Kategorien in seiner DA.|
|Akteure|Nutzer|
|Auslöser|Nutzer|
|Vorbedingung|Kenntnis der Dateien/Kategorien, für die die Änderung durchgeführt<br>werden soll, ggf. über die Suche-Funktion (siehe 6.3)|
|Input|Kategorie-Ebene<br>Kategorie-Bezeichnung<br>Unterkategorien rekursiv ändern<br>Datei (optional)<br>Neue Berechtigungsdaten|
|Ergebnis|Antrag auf Änderung der Berechtigung wurde erstellt|
|Nachbedingung||
|Ablauf|Angabe der Änderungen|
|Fehlerfälle|FC-01: Keine Änderung angegeben|
|**_Schritt 62_**|<br>**_Antrag zur Änderung von Berechtigungen übermitteln_**|
|Kurzbeschreibung|Antrag zur Änderung von Berechtigungen an den DA-Dienst<br>übermitteln|



Bundesamt für Sicherheit in der Informationstechnik 

47 

## 6 Funktionale Beschreibung 

|Akteure|Nutzer|
|---|---|
|Auslöser|Nutzer|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input|Antrag|
|Ergebnis|Antrag wurde an den DA-Dienst übergeben.|
|Nachbedingung||
|Ablauf|Antrag wurde an den DA-Dienst übermittelt.|
|Fehlerfälle||
|**_Schritt 63_**|**_Antrag zur Änderung von Berechtigungen empfangen_**|
|Kurzbeschreibung|Antrag zur Änderung von Berechtigungen durch den DA-Dienst<br>empfangen|
|Akteure|Nutzer|
|Auslöser|Nutzer|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input|Antrag|
|Ergebnis|Antrag wurde durch den DA-Dienst empfangen.|
|Nachbedingung||
|Ablauf|Empfang des Antrages|
|Fehlerfälle|FC-01: Nutzer am De-Mail-Konto nicht angemeldet|
|**_Schritt 64_**|<br>**_Antrag prüfen_**|
|Kurzbeschreibung|Der DA-Dienst prüft den Antrag zur Änderung der Berechtigungen.|
|Akteure|DA-Dienst, Account-Dienst|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Kategorie-Ebene<br>Kategorie-Bezeichnung<br>Unterkategorien rekursiv ändern<br>Datei (optional)<br>Neue Berechtigungsdaten<br>Für die Anmeldung genutztes Authentisierungsniveau|
|Ergebnis|Der Antrag wurde geprüft.|
|Nachbedingung||
|Ablauf|**•**<br>Prüfung, ob die Kategorie bzw. die Datei innerhalb der|



Bundesamt für Sicherheit in der Informationstechnik 

48 

6 Funktionale Beschreibung 

||Kategorie existiert.<br>**•**<br>Prüfung, ob das genutzte Authentisierungsniveau ausreicht.<br>**•**<br>Prüfung, ob das Authentisierungsniveau der Anmeldung gleich<br>oder höher dem zu setzenden Authentisierungsniveau in den<br>Berechtigungsdaten ist.<br>**•**<br>Prüfung, ob die Berechtigung zum Ändern der Kategorie oder<br>Datei vorhanden ist.<br>**•**<br>Prüfung, ob die Berechtigung in sich stimmig ist. Das<br>Authentisierungsniveau für die Datei/Kategorie muss<br>mindestens der übergeordneten Kategorie entsprechen.|
|---|---|
|Fehlerfälle|FC-01: Datei existiert nicht<br>FC-02: Kategorie existiert nicht<br>FC-03: Keine Berechtigungen zur Änderung<br>FC-04: Authentisierungsniveau zu niedrig<br>FC-05: Berechtigungen in sich nicht stimmig<br>FC-06: Authentisierungsniveau kann nicht zugeordnet werden|
|**_Schritt 65_**|<br>**_Entscheidungsknoten: positiv abgeschlossene Prüfung_**|
|Kurzbeschreibung|Existieren aus Schritt 64 keine Fehler, gilt die Prüfung als positiv<br>abgeschlossen.|
|ja|Schritt 67|
|nein|Schritt 66|
|**_Schritt 66_**|**_Fehlermeldung an den Nutzer_**|
|Kurzbeschreibung|Es wird eine Fehlermeldung erstellt und an den Nutzer übermittelt.|
|Akteure|DA-Dienst|
|Auslöser|DA-Dienst|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input|Fehlercode|
|Ergebnis|Eine Meldung mit der Fehlerbeschreibung wurde erstellt.|
|Nachbedingung|Stopp|
|Ablauf|**•**<br>Das System erstellt eine Fehlermeldung<br>**•**<br>Das System übermittelt diese Fehlermeldung an den Nutzer|
|Fehlerfälle||
|**_Schritt 67_**|**_Berechtigungen ändern_**|
|Kurzbeschreibung|Die beantragten Berechtigungen werden in der DA geändert.|



Bundesamt für Sicherheit in der Informationstechnik 

49 

## 6 Funktionale Beschreibung 

|Akteure|DA-Dienst|
|---|---|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Kategorie-Ebene<br>Kategorie-Bezeichnung<br>Unterkategorien rekursiv ändern<br>Datei (optional)<br>Neue Berechtigungsdaten<br>Für die Anmeldung genutztes Authentisierungsniveau|
|Ergebnis|Die Berechtigungen sind neu gesetzt.|
|Nachbedingung|Funktion 1|
|Ablauf|**•**<br>Die Berechtigungen werden innerhalb der Metadaten neu<br>erfasst.<br>**•**<br>Bei der rekursiven Änderung gelten folgende Regeln:<br>**◦**<br>Wenn das Authentisierungsniveau erhöht wird, bleiben<br>höhere Anforderungen bestehen<br>**◦**<br>Wenn das Authentisierungsniveau erniedrigt wird, werden<br>die Rechte komplett überschrieben.<br>**◦**<br>Die Datei/Kategorie hat das Mindest-Auth.-Niveau gleich<br>oder höher als seine Kategorie in der sie sich befindet.|
|Fehlerfälle||
|**_Schritt 68_**|**_Meldung an den Nutzer_**|
|Kurzbeschreibung|Es wird eine Meldung erstellt und an den Nutzer übermittelt.|
|Akteure|DA-Dienst|
|Auslöser|DA-Dienst|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input|Erfolgsmeldung|
|Ergebnis|Eine Meldung wurde erstellt.|
|Nachbedingung||
|Ablauf|**•**<br>Das System erstellt eine Meldung.<br>**•**<br>Das System übermittelt diese Meldung an den Nutzer.|
|Fehlerfälle||
|**_Schritt 69_**|**_Meldung empfangen_**|
|Kurzbeschreibung|Es wird eine Meldung durch den Nutzer empfangen.|



Bundesamt für Sicherheit in der Informationstechnik 

50 

6 Funktionale Beschreibung 

|Akteure|Nutzer|
|---|---|
|Auslöser|Nutzer|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input||
|Ergebnis|Meldung wurde auf Seite des Nutzers empfangen.|
|Nachbedingung||
|Ablauf|Empfang der Meldung des DA-Dienstes durch den Nutzer|
|Fehlerfälle||
|**_Schritt 70_**|**_Meldung darstellen_**|
|Kurzbeschreibung|Die Inhalte der Meldung werden dem Nutzer dargestellt.|
|Akteure|Nutzer|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Meldungsinhalte|
|Ergebnis|Die Meldung wurde dem Nutzer dargestellt.|
|Nachbedingung||
|Ablauf|Die vom DA-Dienst empfangene Nachricht wird dem Benutzer nach<br>Aufarbeitung dargestellt.|
|Fehlerfälle||



_Tabelle 9: Schritte zur Änderung von Berechtigungen_ 

## **6.3 Suche und Anzeige von Dokumenten und Kategorien** 

|**_Schritt 71_**|**_Erstellen einer Suchanfrage_**|
|---|---|
|Kurzbeschreibung|Der Nutzer erstellt eine Suchanfrage, in der die Suchkriterien enthalten<br>sind.|
|Akteure|Nutzer|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Suchkriterien können sein:<br>**•**<br>Teile des Namens oder vollständiger Name der Datei,<br>einschließlich Datei-Endung<br>**•**<br>Teile des Namens oder vollständige Bezeichnung der Kategorie|



Bundesamt für Sicherheit in der Informationstechnik 

51 

6 Funktionale Beschreibung 

||**•**<br>Datei-MIME-Typ (Format)<br>**•**<br>Inhalt der Datei (Text)<br>**•**<br>Einschränkungen hinsichtlich der Kategorien<br>**•**<br>Letztes Änderungsddatum der Datei<br>**•**|
|---|---|
|Ergebnis|Anfrage erstellt|
|Nachbedingung||
|Ablauf|Angabe der Suchkriterien|
|Fehlerfälle|FC-01: Keine Suchkriterien erfasst|
|**_Schritt 72_**|**_Suchanfrage übermitteln_**|
|Kurzbeschreibung|Suchanfrage an den DA-Dienst übermitteln|
|Akteure|Nutzer|
|Auslöser|Nutzer|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input|Suchanfrage|
|Ergebnis|Suchanfrage wurde an den DA-Dienst übergeben.|
|Nachbedingung||
|Ablauf|Suchanfrage wird an den DA-Dienst übermittelt.|
|Fehlerfälle|FC-01: Suchanfrage wurde vom DA-Dienst nicht angenommen.|
|**_Schritt 73_**|<br>**_Suchanfrage empfangen_**|
|Kurzbeschreibung|Suchanfrage wird vom DA-Dienst empfangen.|
|Akteure|DA-Dienst|
|Auslöser|Nutzer|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input|Suchanfrage|
|Ergebnis|Suchanfrage ist entgegengenommen|
|Nachbedingung||
|Ablauf|Suchanfrage wird vom DA-Dienst entgegengenommen.|
|Fehlerfälle|FC-01: Nutzer am De-Mail-Konto nicht angemeldet|
|**_Schritt 74_**|<br>**_Entschlüsseln der Dateien_**|
|Kurzbeschreibung|Die durch den DMDA verschlüsselten Dateien bzw. die<br>nutzerbezogenen Suchindex-Dateien werden durch den DMDA<br>entschlüsselt.|



Bundesamt für Sicherheit in der Informationstechnik 

52 

6 Funktionale Beschreibung 

|Akteure|DA-Dienst|
|---|---|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Verschlüsselte Dateien / Suchindex-Dateien, Entschlüsselungsschlüssel<br>des DMDA|
|Ergebnis|Entschlüsselte Dateien / Suchindex-Dateien für die Durchführung der<br>Suche, die im DA gespeicherte Dateien/Suchindex-Dateien bleibt<br>verschlüsselt.|
|Nachbedingung||
|Ablauf|Entschlüsselung der Dateien / Suchindex-Dateien|
|Fehlerfälle|FC-01: Kein DMDA-bezogener Entschlüsselungsschlüssel vorhanden|
|**_Schritt 75_**|<br>**_Suche durchführen_**|
|Kurzbeschreibung|Die Suche wird innerhalb der DA des angemeldeten Nutzers ausgeführt.<br>Eine Ergebnisliste wird erstellt.|
|Akteure|DA-Dienst|
|Auslöser|Nutzer|
|Vorbedingung||
|Input|Suchkriterien<br>Authentisierungsniveau|
|Ergebnis|Es wurde eine Liste mit den Ergebnissen der Suche erstellt und dem<br>Nutzer übermittelt.<br>Liste beinhaltet<br>**•**<br>bei Kategorie:<br>**◦**<br>Kategorie-Pfad inkl. aller Kategoriebezeichnungen<br>**◦**<br>URL<br>**•**<br>bei Dateien<br>**◦**<br>Kategorie-Pfad inkl. aller Kategoriebezeichnungen<br>**◦**<br>Dateiname<br>**◦**<br>Datum der letzten Änderung in der DA<br>**◦**<br>URL|
|Nachbedingung||
|Ablauf|Die auf der Basis der Suchkriterien definierte Suche wird ausgeführt.<br>Dabei wird beachtet, dass die Suche ausschließlich die Kategorien bzw.<br>Dateien berücksichtigt, die für den Nutzer und seinem derzeitigen<br>Authentisierungsniveau lesbar sind.|



Bundesamt für Sicherheit in der Informationstechnik 

53 

## 6 Funktionale Beschreibung 

|Fehlerfälle||
|---|---|
|**_Schritt 76_**|**_Löschung entschlüsselter Dateien_**|
|Kurzbeschreibung|Die für die Suchanfrage entschlüsselten Dateien /Suchindex-Dateien<br>werden sicher gelöscht.|
|Akteure|DA-Dienst|
|Auslöser|DA-Dienst|
|Vorbedingung||
|Input|Entschlüsselte Dateien / Suchindex-Dateien|
|Ergebnis|Entschlüsselte Dateien / Suchindex-Dateien sind gelöscht|
|Nachbedingung||
|Ablauf|Der DA-Dienst löscht die durch den DMDA entschlüsselten Dateien /<br>Suchindex-Dateien unwiederbringlich.|
|Fehlerfälle||
|**_Schritt 77_**|**_Liste an den Nutzer senden_**|
|Kurzbeschreibung|Es wird die Liste mit den Suchergebnissen an den Nutzer übermittelt.|
|Akteure|DA-Dienst, Nutzer|
|Auslöser|DA-Dienst|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input|Liste mit Suchergebnissen|
|Ergebnis|Eine Liste wurde an den Nutzer gesandt.|
|Nachbedingung|Die Ergebnisliste wird durch den DMDA sicher gelöscht.|
|Ablauf|Das System übermittelt die Liste an den Nutzer.|
|Fehlerfälle|FC-01: Suchergebnisse werden vom Nutzer-System nicht angenommen|
|**_Schritt 78_**|<br>**_Liste mit Suchergebnissen empfangen_**|
|Kurzbeschreibung|Es wird eine Liste durch den Nutzer empfangen.|
|Akteure|Nutzer|
|Auslöser|Nutzer, DA-Dienst|
|Vorbedingung|Sicherer Kanal zwischen Kommunikationspartnern aufgebaut|
|Input|Liste|
|Ergebnis|Liste wurde auf Seite des Nutzers empfangen.|
|Nachbedingung||
|Ablauf|Empfang der Liste des DA-Dienstes durch den Nutzer|
|Fehlerfälle||



Bundesamt für Sicherheit in der Informationstechnik 

54 

6 Funktionale Beschreibung 

|**_Schritt 79_**|**_Darstellung der Liste mit den Ergebnissen der Suche_**|
|---|---|
|Kurzbeschreibung|Der Nutzer sieht die List der Suchergebnisse ein.|
|Akteure|Nutzer|
|Auslöser|Nutzer|
|Vorbedingung||
|Input||
|Ergebnis|Es wurde eine Liste mit den Ergebnissen der Suche dargestellt.|
|Nachbedingung||
|Ablauf|Die Ergebnisliste wird für den Nutzer dargestellt.|
|Fehlerfälle||



_Tabelle 10: Schritte zur Suche und Anzeige von Kategorien/ Dateien_ 

Bundesamt für Sicherheit in der Informationstechnik 

55 

7 Weitere Funktionen 

## **7 Weitere Funktionen** 

Die in diesem Abschnitt beschriebenen Funktionen werden entweder vom System ausgeführt oder können vom Nutzer interaktiv aufgerufen werden, während er an seiner DA angemeldet ist. Eine Beschreibung, wie die einzelnen Funktionen dargestellt werden, findet sich in Abschnitt 9. 

## **7.1 Durch das System ausgeführte Funktionen** 

|**_Funktion 1_**|**_Protokollierung von Änderung_**|
|---|---|
|Kurzbeschreibung|Aktionen, die zur Änderung der Metadaten führen, werden<br>protokolliert.|
|Akteure|DA-Dienst|
|Auslöser|jede Änderung der Metadaten zu einer Kategorie bzw. einer Datei|
|Vorbedingung|Änderung eines Meta-Datums|
|Input|**•**<br>Nutzerkennung<br>**•**<br>Authentisierungsniveau<br>**•**<br>neue Metadaten<br>**•**<br>Datum und Zeit|
|Ergebnis|Revisionssichere Speicherung der Änderung von Metadaten|
|Nachbedingung|Auswertbarkeit der Protokolldaten muss zu jeder Zeit gegeben sein.|
|Ablauf|**•**<br>Erstellung des Logs<br>**•**<br>Revisionssichere Speicherung und Archivierung|
|Fehlerfälle||
|**_Funktion 2_**|**_Prüfung Schadsoftware_**|
|Kurzbeschreibung|Es wird eine Prüfung von zu speichernden Dateien hinsichtlich<br>Schadsoftware:<br>**•**<br>Viren,<br>**•**<br>Trojanern,<br>**•**<br>Würmer<br>vorgenommen.|
|Akteure|DA-Dienst, Schadsoftware-Dienst|
|Auslöser|Upload und Download von Dateien (siehe Abschnitt 6.1)|
|Vorbedingung|Prüfprogramme mit aktuellen Prüfkonfigurationen|
|Input|Datei|
|Ergebnis|Information, falls in der Datei Schadsoftware gefunden wird|



Bundesamt für Sicherheit in der Informationstechnik 

56 

7 Weitere Funktionen 

|Nachbedingung||
|---|---|
|Ablauf|**•**<br>Datei wird zum Schadsoftware-Scanner übergeben.<br>**•**<br>Datei wird vom Schadsoftware-Scanner entgegengenommen.<br>**•**<br>Datei wird an die Schadsoftware-Prüfung übergeben.|
|Fehlerfälle|FC-01: Dateiformat unbekannt und kann nicht auf  Schadsoftware<br>geprüft werden.|
|**_Funktion 3_**|<br>**_Benachrichtigung bei hohem verbrauchten Speicher_**|
|Kurzbeschreibung|Wenn der Nutzer nur noch 10 % seines Speichers in seinem DA frei<br>hat, meldet das System bei Übergang dieser Grenze diesen Zustand.|
|Akteure|DA-Dienst|
|Auslöser|Speicherung von Dateien (siehe Abschnitt 6.1.1)|
|Vorbedingung|10 % des zugeordnetes Speichers frei|
|Input||
|Ergebnis|Meldung erfolgte an den Nutzer.|
|Nachbedingung||
|Ablauf|**•**<br>DA-Dienst misst freien Speicher.<br>**•**<br>Bei Unterschreiten der Grenze von 11 nach 10 % des noch<br>verfügbaren freien Speicherplatzes wird eine Meldung erstellt.<br>**•**<br>Die Meldung wird an den Nutzer übermittelt.|
|Fehlerfälle||



_Tabelle 11: Durch das System ausgeführte Funktionen_ 

## **7.2 Durch den Nutzer initiierte Funktionen** 

|**_Funktion 4_**|**_Einsicht in das Protokoll_**|
|---|---|
|Kurzbeschreibung|Einsicht in das Protokoll der DA<br>Hinweis: Es werden nur Kategorien bzw. Dateien berücksichtigt, die<br>mit dem aktuellen Authentisierungsniveau des Nutzers lesbar sind.|
|Akteure|Nutzer|
|Auslöser|Nutzer|
|Vorbedingung|Anmeldung am De-Mail-Konto|
|Input|Kategorie-Ebene<br>Kategoriebezeichnung<br>Optional: [Dateiname] oder [Liste über alle in der Kategorie vorhanden|



Bundesamt für Sicherheit in der Informationstechnik 

57 

7 Weitere Funktionen 

||Dateien]<br>Zeitraum<br>Einschluss aller Sub-Kategorien<br>Bei der Anmeldung genutztes Authentisierungsniveau|
|---|---|
|Ergebnis|Logging-Protokoll|
|Nachbedingung||
|Ablauf|**•**<br>Der Nutzer stellt eine Anfrage für die Einsicht in das Protokoll.<br>**•**<br>In der Anfrage gibt er an: Kategorie-Ebene,<br>Kategoriebezeichnung, optional ein Dateiname, einen Zeitraum.<br>**•**<br>Der Antrag wird vom DA-Dienst entgegengenommen.<br>**•**<br>Der DA-Dienst erstellt über den Filter der im Antrag<br>angegebenen Daten und dem angemeldeten Nutzer inkl. dessen<br>genutztes Authentisierungsniveau ein Protokoll.<br>**•**<br>Der DA-Dienst signiert dieses Protokoll mit einer dauerhaft<br>überprüfbaren qualifizierten Signatur und stellt dem Nutzer das<br>Protokoll zur Verfügung (Download oder per<br>Meldungsnachricht)sendet dieses über den Versanddienst an das<br>Postfach des Nutzers.<br>Hinweis: Es werden nur Kategorien bzw. Dateien berücksichtigt, die<br>mit dem Authentisierungsniveau bei der Anmeldung lesbar sind.|
|Fehlerfälle|FC-01: Kein Protokoll für die Datei / Kategorie gefunden<br>FC-02: angegebene Kategorie nicht gefunden<br>FC-03: angegebene Datei nicht gefunden|



_Tabelle 12: Durch den Nutzer initiierte Funktionen_ 

Bundesamt für Sicherheit in der Informationstechnik 

58 

8 Legende zum Aktivitätsdiagramm 

## **8 Legende zum Aktivitätsdiagramm** 

||**Startknoten**|Startknoten<br>Der Startknoten ist der Startpunkt eines Prozesses. Ein Prozess darf<br>mehrere Startknoten haben, in diesem Fall beginnen beim Start des<br>Prozesses mehrere Abläufe. Es ist möglich, dass ein Prozess keinen<br>Startknoten besitzt, sondern von einem Ereignis angestoßen wird.|
|---|---|---|
||**Endknoten**|Endknoten<br>Der Endknoten gibt an, dass die Ausführung des Prozesses<br>abgeschlossen ist. Es kann in einem Prozessdiagramm mehrere<br>Ausgänge in Form dieser Endknoten geben. Gibt es zum Zeitpunkt<br>des Erreichens des Endknoten mehrere parallele Abläufe innerhalb des<br>Prozesses, werden beim Erreichen eines Endknoten alle Abläufe<br>gestoppt.|
||**Stopp**|Ablaufende<br>Das Ablaufende terminiert einen Ablauf. Im Unterschied zum<br>Endknoten, der einen ganzen Prozess beendet, hat das Erreichen des<br>Ablaufenden keinen Effekt auf andere parallele Abläufe, die zu<br>diesem Zeitpunkt innerhalb des Prozesses abgearbeitet werden. Auf<br>diese Weise lassen sich parallele Abläufe gezielt und einzeln beenden.|
|||Kante<br>Die als Pfeile dargestellten Kanten verbinden die einzelnen<br>Komponenten des Diagramms und stellen den Kontrollfluss dar.|
||Aktion|Aktion<br>Eine Aktion ist ein einzelner Schritt innerhalb eines Prozesses, der<br>nicht mehr weiter zerlegt wird. Das bedeutet nicht unbedingt, dass die<br>Aktion in der realen Welt nicht mehr weiter zerlegbar wäre, sondern<br>dass die Aktion in diesem Diagramm nicht mehr weiter verfeinert<br>wird. Die Aktion kann Ein- und Ausgabeinformationen besitzen. Der<br>Output einer Aktion kann der Input einer Folge-Aktion sein.|
||Aufruf einer<br>Aktivität|Aufruf einer Aktivität<br>Mit diesem Symbol kann aus einer Aktivität (Prozess) heraus eine<br>weitere Aktivität aufgerufen werden. Der Aufruf selbst ist eine<br>Aktion, der aufgerufene Ablauf eine weitere Aktivität.|
||Ereignis<br>empfangen|Empfang eines Ereignisses<br>Diese Aktion wartet auf das Eintreten eines Ereignisses. Nach dem<br>Empfang des Ereignisses wird der im Aktivitätsdiagramm definierte,<br>von dieser Aktion ausgehende Ablauf abgearbeitet.|



Bundesamt für Sicherheit in der Informationstechnik 

59 

8 Legende zum Aktivitätsdiagramm 

Senden von Signalen Das Senden von Signalen bedeutet, dass ein Signal an eine Signal senden empfangende Aktivität gesendet wird. Die empfangende Aktivität nimmt das Signal mit der Aktion „Ereignis empfangen“ entgegen und kann entsprechend darauf reagieren. Entscheidungsknoten Die Raute stellt eine Verzweigung im Kontrollfluss dar. Eine Entscheidungsknoten Verzweigung hat einen Eingang und zwei oder mehrere Ausgänge. Jeder Ausgang wird mit einer Bedingung versehen. Trifft eine Bedingung zu, wird am entsprechenden Ausgang weiter verfahren. Datenobjekt Datenobjekte gehören üblicherweise nicht zum Symbolumfang in Datenobjekt UML-Aktivitätsdiagrammen. Sie sind hier jedoch eingeführt worden, um an entscheidender Stelle zu verdeutlichen, welche Datenobjekte, insbesondere im Fokus der Schutzbedarfsanalyse, vorliegen. 

_Tabelle 13: Legende zum Aktivitätsdiagramm_ 

Bundesamt für Sicherheit in der Informationstechnik 

60 

9 Legende zu Schritten der Ablaufbeschreibung 

## **9 Legende zu Schritten der Ablaufbeschreibung** 

Schritte im Aktivitätsdiagramm bezeichnen im Kontrollfluss eingebundene einmalig ablaufende Aktionen. 

Schritte werden in diesem Modul als Aktionen auf folgende Art und Weise beschrieben: 

|<br>**_Schritt<Nr.>_**|<br>**_Eindeutiger Name der Aktion_**|
|---|---|
|Kurzbeschreibung|Innerhalb der Kurzbeschreibung erfolgt eine verbale Beschreibung der<br>wesentlichen Funktionalität der Aktion.|
|Akteure|Alle Rollen bzw. Dienste, die innerhalb der Aktion in irgendeiner Weise<br>beteiligt sind, werden aufgezählt.|
|Auslöser|Der Auslöser ist ein Akteur, durch den die Aktion aufgerufen bzw.<br>initialisiert wird.|
|Vorbedingung|Unter Vorbedingungen werden die Bedingungen verstanden, die nicht aus<br>einer unmittelbar vorhergehenden Aktion folgen, sondern asynchron erzielt<br>werden müssen. Diese Aktivitäten sind nicht unbedingt in diesem Dokument<br>beschrieben, die Ergebnisse sind jedoch als Vorbedingungen für die<br>Ausführung der hier beschriebenen Aktion notwendig. Auf die Erfüllung<br>dieser Vorbedingungen muss sich die nutzende Aktion verlassen können.|
|Input|Der Auslöser muss bei Initialisierung der Aktion die entsprechenden<br>Informationen an diese übergeben oder durch die Aktion abfragen lassen, so<br>dass eine Verarbeitung der Informationen innerhalb der Aktion erfolgen<br>kann.|
|Ergebnis|Nach Beendigung der Aktion muss eine bestimmte Information als Resultat<br>erarbeitet bzw. bereitgestellt werden.|
|Nachbedingung|Unter Nachbedingungen werden Bedingungen verstanden, die innerhalb<br>dieser Aktion nicht betrachtet werden und durch unmittelbar nachfolgende<br>Aktionen aufgegriffen und dort behandelt werden müssen.|
|Ablauf|Für die innerhalb der Aktion definierte Logik wird ein konkreter Ablauf<br>beschrieben. Die definierte Abfolge muss innerhalb der Aktion durchgeführt<br>und abgeschlossen werden.|
|Fehlerfälle|Als Fehlerfall wird ein Ergebnis einer Funktion bezeichnet, der innerhalb<br>der Funktionsspezifikation liegt, aber kein Standard-Ergebnis darstellt.<br>Die konkrete Behandlung eines Fehlerfalls ist implementierungsabhängig.<br>Je nach Fall können unterschiedliche Lösungsstrategien verwendet werden,<br>bspw. kann eine Aktion zu einem späteren Zeitpunkt wiederholt oder die<br>Aktion abgebrochen werden. Bei Abbruch einer Aktion ist der Nutzer<br>mindestens darüber zu informieren und alle bis zu diesem Schritt<br>generierten temporären Daten müssen gelöscht werden. In den<br>Beschreibungen der Fehlerfälle der Aktionen werden nur mögliche Fehler<br>beschrieben, die innerhalb der Funktionsspezifikation liegen.|



_Tabelle 14: Legende zu Schritten_ 

Bundesamt für Sicherheit in der Informationstechnik 

61 


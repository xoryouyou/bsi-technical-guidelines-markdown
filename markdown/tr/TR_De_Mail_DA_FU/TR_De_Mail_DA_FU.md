![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_2.jpeg)

### BSI – Technische Richtlinie

| Bezeichnung:       | Dokumentenablage<br>Funktionalitätsspezifikation |  |  |  |
|--------------------|--------------------------------------------------|--|--|--|
| Anwendungsbereich: | De-Mail                                          |  |  |  |
| Kürzel:            | BSI TR 01201 Teil 5.1                            |  |  |  |
| Version:           | 1.8                                              |  |  |  |

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn Tel.: +49 22899 9582-0 E-Mail: [de-mail@bsi.bund.de](mailto:de-mail@bsi.bund.de) Internet: [https://www.bsi.bund.de](https://www.bsi.bund.de/) © Bundesamt für Sicherheit in der Informationstechnik 2024

| 1                                                                                                       | Einleitung5                                                                                                                                                                                                                                                                                                                                                                                              |  |
|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| 2                                                                                                       | Funktionale Anforderungen6                                                                                                                                                                                                                                                                                                                                                                               |  |
| 2.1<br>2.1.1<br>2.1.2                                                                                   | Zugriff auf Dokumente in der DA6<br>Authentisierung und Autorisierung6<br>Zugriffsoperationen6                                                                                                                                                                                                                                                                                                           |  |
| 2.2<br>2.2.1<br>2.2.2<br>2.2.3<br>2.2.4<br>2.2.5<br>2.2.6<br>2.2.7<br>2.2.8<br>2.3<br>2.4<br>2.5<br>2.6 | Ablage von Dokumenten7<br>Kategorien7<br>Erstellung neuer Kategorien7<br>Einstellen neuer Dokumente7<br>Herunterladen von Dokumenten8<br>Umbenennen von Dokumenten und Kategorien8<br>Löschen von Dokumenten8<br>Löschen von Kategorien8<br>Änderung der Berechtigungen für Dokumente und Kategorien9<br>Suchen und Finden9<br>Protokollierung der Aktivitäten10<br>Verschlüsselung11<br>Konfiguration11 |  |
| 3                                                                                                       | Nicht-funktionale Anforderungen12                                                                                                                                                                                                                                                                                                                                                                        |  |
| 4<br>4.1<br>4.2<br>4.3                                                                                  | Datenstrukturen13<br>Datei13<br>Kategorien14<br>Meldungen14                                                                                                                                                                                                                                                                                                                                              |  |
| 5                                                                                                       | Aktivitätsdiagramm16                                                                                                                                                                                                                                                                                                                                                                                     |  |
| 6<br>6.1<br>6.1.1<br>6.1.2                                                                              | Funktionale Beschreibung23<br>Upload und Download von Dateien23<br>Upload einer Datei in die DA23<br>Download von Dateien30                                                                                                                                                                                                                                                                              |  |
| 6.2<br>6.2.1<br>6.2.2<br>6.2.3<br>6.2.4                                                                 | Verwaltung von Dateien/Kategorien35<br>Erstellen einer Kategorie35<br>Umbenennen von Dateien/Kategorien39<br>Löschen von Dateien/Kategorien43<br>Ändern der Berechtigungen für Dokumente und Kategorien47                                                                                                                                                                                                |  |
| 6.3                                                                                                     | Suche und Anzeige von Dokumenten und Kategorien51                                                                                                                                                                                                                                                                                                                                                        |  |
| 7<br>7.1<br>7.2                                                                                         | Weitere Funktionen56<br>Durch das System ausgeführte Funktionen56<br>Durch den Nutzer initiierte Funktionen57                                                                                                                                                                                                                                                                                            |  |
| 8                                                                                                       | Legende zum Aktivitätsdiagramm59                                                                                                                                                                                                                                                                                                                                                                         |  |
| 9                                                                                                       | Legende zu Schritten der Ablaufbeschreibung61                                                                                                                                                                                                                                                                                                                                                            |  |

### **Tabellenverzeichnis**

| Tabelle 1: Metadaten einer Datei13                                   |  |
|----------------------------------------------------------------------|--|
| Tabelle 2: Daten der Kategorie (Teil 1)14                            |  |
| Tabelle 3: Metadaten der Kategorie (Teil 2)14                        |  |
| Tabelle 4: Schritte zum Upload von Dateien28                         |  |
| Tabelle 5: Schritte zum Download von Dateien33                       |  |
| Tabelle 6: Schritte zum Erstellen einer Kategorie37                  |  |
| Tabelle 7: Schritte zum Umbenennen41                                 |  |
| Tabelle 8: Schritte zum Löschen45                                    |  |
| Tabelle 9: Schritte zur Änderung von Berechtigungen49                |  |
| Tabelle 10: Schritte zur Suche und Anzeige von Kategorien/ Dateien53 |  |
| Tabelle 11: Durch das System ausgeführte Funktionen55                |  |
| Tabelle 12: Durch den Nutzer initiierte Funktionen56                 |  |
| Tabelle 13: Legende zum Aktivitätsdiagramm58                         |  |
| Tabelle 14: Legende zu Schritten59                                   |  |

# <span id="page-4-0"></span>**1 Einleitung**

Dieses Modul beinhaltet die funktionalen Spezifikationen der Dokumentenablage und ist Bestandteil von [TR DM DA M].

# <span id="page-5-0"></span>**2 Funktionale Anforderungen**

Nachfolgend werden die funktionalen Anforderungen beschrieben, die erfüllt werden müssen, damit ein Dienst zur Ablage und Verwaltung von elektronischen Dokumenten und anderen Dateien als De-Mail-Dienst anerkannt werden kann.

Über den De-Mail-Versanddienst empfangene Dokumente kann der Nutzer von seinem De-Mail-Postfach in seine DA kopieren. Weiterhin kann der Nutzer Dokumente aus seiner DA über den PVD an Dritte verschicken (vgl. [TR DM PVD FU]).

Alle Aktionen sind in geeigneter Weise zu protokollieren.

### **2.1 Zugriff auf Dokumente in der DA**

Ein Nutzer darf auf Dokumente in seiner DA nur Zugriff erhalten, wenn er sich vorher erfolgreich an seinem De-Mail-Konto angemeldet hat.

#### <span id="page-5-1"></span>**2.1.1 Authentisierung und Autorisierung**

Nach erfolgreicher Anmeldung am De-Mail-Konto hat der Nutzer Zugriff auf alle Dokumente und Kategorien in der seinem Konto zugeordneten DA (vgl. Abschnitt [2.2.1\)](#page-6-0).

Um auf den Inhalt und die Metadaten eines Dokumentes oder einer Kategorie zugreifen zu können, muss der Nutzer beim Einstellen festlegen können, für welche Zugriffsoperationen welches Authentisierungsniveau notwendig sein soll. Legt der Nutzer die Berechtigungen nicht fest, so wird automatisch das Authentisierungsniveau verwendet, mit dem der Nutzer zu diesem Zeitpunkt angemeldet ist. Ein Zugriff auf das Dokument erfordert sodann eine Anmeldung des Nutzers mit mindestens diesem Authentisierungsniveau.

Das Authentisierungsniveau für einen Zugriff auf ein Dokument kann durch den Nutzer herabgestuft werden, wenn sein aktuelles Authentisierungsniveau einen Zugriff auf das Dokument erlaubt. Das minimale Authentisierungsniveau eines Dokuments kann durch den Nutzer bis auf das Niveau erhöht werden, das seinem aktuellen Authentisierungsniveau entspricht.

### <span id="page-5-2"></span>**2.1.2 Zugriffsoperationen**

Folgende Zugriffsoperationen auf Dokumente müssen in Abhängigkeit von den jeweiligen Authentisierungsniveaus von der DA unterstützt werden:

- **•** Lesen
- **•** Schreiben (und Löschen) Unter "Schreiben" fallen das Einstellen von neuen Dokumenten und das Ändern von vorhandenen Dokumenten.

### **2.2 Ablage von Dokumenten**

#### <span id="page-6-0"></span>**2.2.1 Kategorien**

Um das spätere Suchen und Auffinden von Dokumenten zu erleichtern, muss es in der DA möglich sein, Dokumente bestimmten Kategorien zuzuordnen, die bspw. als Ordner in einer Hierarchie abgebildet werden können. Es müssen mindestens zwei vordefinierte Kategorien existieren. Eine Standardkategorie, der Dokumente zugeordnet werden, z.B. wenn vom Nutzer noch keine Kategorie erstellt wurde, sowie die Kategorie "Papierkorb", der Dokumente zugeordnet werden, die gelöscht werden sollen.

Kategorien können hierarchisch in mehreren Ebenen gestaffelt werden.

#### **2.2.2 Erstellung neuer Kategorien**

Bei der Erstellung einer neuen Kategorie muss geprüft werden, ob in der übergeordneten Kategorie bereits eine Kategorie mit dem selben Namen existiert und ob für den Nutzer Schreibrechte bestehen.

Das Authentisierungsniveau für die neue Kategorie muss mindestens dem der übergeordneten Kategorie entsprechen. In Unterkategorien kann das geforderte Authentisierungsniveau nur erhöht werden.

#### **2.2.3 Einstellen neuer Dokumente**

Der Nutzer kann neue Dokumente

- **•** von seinem Rechnersystem in die DA hochladen,
- **•** eine Nachricht aus seinem Postfach in die DA speichern oder,
- **•** einen Anhang einer Nachricht aus dem Postfach in der DA ablegen.

Die Dokumente können einer oder mehreren Kategorien zugeordnet werden. Wird für ein Dokument keine Kategorie ausgewählt, so wird es der Standardkategorie zugeordnet. Der Nutzer muss die notwendige Zugriffsberechtigung für die Kategorie(n) besitzen.

Das Dokument wird durch den DMDA einer Prüfung auf Schadsoftware unterzogen. Bei einer positiven Prüfung wird das Dokument nicht gespeichert, der Nutzer erhält eine entsprechende Meldung.

Wenn nicht genügend freier Speicherplatz verfügbar ist, muss der Nutzer per Meldung informiert werden.

Für das Dokument wird standardmäßig folgende Berechtigung gesetzt:

**•** Lesen: Dies ist gestattet für den angemeldeten Nutzer mit dem aktuellen Authentisierungsniveau,

**•** Schreiben: Dies ist gestattet für den angemeldeten Nutzer mit dem aktuellen Authentisierungsniveau. Die Berechtigung des Dokuments muss mindestens dem geforderten Authentisierungsniveau der Kategorie entsprechen, der das Dokument zugeordnet wird.

Es wird für jede eingestellte Datei ein Hashwert berechnet und gespeichert.

#### **2.2.4 Herunterladen von Dokumenten**

Der Nutzer darf nur Dokumente herunterladen können, für die er die Zugriffsberechtigung zum Lesen besitzt.

Vor dem Herunterladen muss der DMDA das Dokument auf Schadsoftware prüfen. Bei einer positiven Prüfung ist der Nutzer per Meldung zu informieren.

Der DMDA muss den Hashwert des Dokumentes prüfen. Stimmt der neu berechnete Hashwert nicht mit dem ursprünglichen Wert überein, so ist der Nutzer per Meldung zu informieren.

Danach ist das Herunterladen des Dokuments möglich.

#### **2.2.5 Umbenennen von Dokumenten und Kategorien**

Dokumente und Kategorien müssen umbenannt werden können.

Die Umbenennung findet statt, wenn der Nutzer schreibend auf das Dokument oder die Kategorie zugriffsberechtigt ist und der neue Name in der übergeordneten Kategorie noch nicht vorhanden ist.

Der Nutzer kann Dokumente und Kategorien nur umbenennen, wenn er die notwendige Berechtigung besitzt.

#### **2.2.6 Löschen von Dokumenten**

Der Nutzer kann Dokumente nur löschen, wenn er die notwendige Berechtigung besitzt.

Für die Löschung von Dokumenten ist ein zweistufiges Verfahren vorzusehen. Im ersten Schritt werden die Dokumente in die Kategorie "Papierkorb" verschoben. Alle Zuordnungen zu anderen Kategorien werden entfernt. Im zweiten Schritt können die Dokumente aus der Kategorie "Papierkorb" endgültig gelöscht werden.

Bei der endgültigen Löschung müssen die Dokumente sicher gelöscht werden. Alle Informationen zu den Dokumenten sind vollständig zu entfernen. Dies betrifft auch die Metadaten der Dokumente.

Der Nutzer muss ein oder mehrere Dokumente löschen können.

#### **2.2.7 Löschen von Kategorien**

Zur Löschung einer Kategorie muss der Nutzer die notwendige Berechtigung haben.

Die zu löschende Kategorie darf keine untergeordneten Kategorien oder zugeordnete Dateien enthalten.

Die vordefinierten Kategorien (Standardkategorie und"Papierkorb") können nicht gelöscht werden.

#### **2.2.8 Änderung der Berechtigungen für Dokumente und Kategorien**

Bei der Änderung einer Berechtigung muss geprüft werden, ob

- **•** das Authentisierungsniveau des Nutzers ausreichend ist, um die Dokumente oder Kategorie zu ändern.
- **•** das aktuelle Authentisierungsniveau des Nutzers mindestens dem Authentisierungsniveau entspricht, das gesetzt werden soll.

Wenn die Bedingungen erfüllt sind, werden die Berechtigungen innerhalb der Metadaten entsprechend geändert.

Bei der rekursiven Änderung von Berechtigungen (wenn eine Kategorie geändert wird, die weitere Kategorien oder Dateien enthält) gelten folgende Regeln:

- **•** Wird das Authentisierungsniveau einer Kategorie erhöht, so werden die Berechtigungen aller darin enthaltenen Dokumenten und Kategorien erhöht, für die das Authentisierungsniveau "normal" benötigt wird. Die Berechtigungen aller anderen Dokumenten und Kategorien bleiben bestehen.
- **•** Wenn das Authentisierungsniveau herabgesetzt wird, können die Berechtigungen aller enthaltenen Dokumente und Kategorien bestehen bleiben oder auf Wunsch ebenfalls herabgesetzt werden.

### **2.3 Suchen und Finden**

Die Suchfunktion muss sowohl die Suche nach Kriterien wie Dateinamen und Kategorien als auch nach Dokumentinhalten von Standard-Dateiformaten in nicht durch den Nutzer zusätzlich verschlüsselten Dokumenten ermöglichen.

Suchkriterien können sein:

- **•** Teile des Namens oder vollständiger Name der Datei, einschließlich Datei-Endung
- **•** Teile des Namens oder vollständiger Name der Kategorie
- **•** Datei-MIME-Typ (Format)
- **•** Inhalt der Datei (Text)
- **•** Einschränkungen hinsichtlich der Kategorien
- **•** Datum und Zeit der letzten Änderung in der DA

Der Suchindex muss verschlüsselt gespeichert werden.

Die Ergebnisliste muss beinhalten:

- **•** bei Kategorien:
	- **◦** Kategorie-Pfad inkl. aller Kategoriebezeichnungen
	- **◦** URL
- **•** bei Dokumenten
	- **◦** Kategorie-Pfad inkl. aller Kategoriebezeichnungen
	- **◦** Dateiname
	- **◦** Datum der letzten Änderung in der DA
	- **◦** URL

Bei der Suche wird beachtet, dass ausschließlich die Dokumente oder Kategorien berücksichtigt werden, die für den Nutzer und seinem derzeitigen Authentisierungsniveau lesbar sind.

Die Ergebnisliste muss nach Abschluss der Suche durch den DMDA sicher gelöscht werden.

### **2.4 Protokollierung der Aktivitäten**

Um Anwendungsfehler oder Missbrauch feststellen zu können, müssen alle Aktionen protokolliert werden, die Dokumente und Kategorien betreffen.

Bei der Protokollierung der Aktionen ist sicher festzuhalten:

- **•** Nutzerkennung
- **•** Authentisierungsniveau des Nutzers
- **•** Neue Metadaten
- **•** Datum und Uhrzeit.

Der Nutzer kann auf Wunsch ein Protokoll über die Aktivitäten in der DA anfordern, das mit einer qualifizierten Signatur des DMDA versehen ist. Das Protokoll kann dem Nutzer mittels Anhang einer De-Mail oder als Download zur Verfügung gestellt werden.

Das Protokoll muss beinhalten:

- **•** eine Liste der eingestellten Dokumente mit dem jeweiligen Hashwert und dem Namen des Hashalgorithmus,
- **•** das aktuelle Authentisierungsniveau,
- **•** eine Änderungshistorie der Dokumente.

Das Protokoll kann anhand folgender Merkmale eingeschränkt werden:

- **•** Kategorie,
- **•** Dateinamen,
- **•** Zeitraum.

### **2.5 Verschlüsselung**

Alle in der DA von De-Mail abgelegten Dokumente müssen durch den DMDA verschlüsselt abgelegt werden. Der DMDA hat zudem Sorge dafür zu tragen, dass vom Nutzer aus der DA angeforderten Dokumente entschlüsselt werden.

Darüber hinaus muss der Nutzer bei Bedarf auch seinerseits zusätzlich verschlüsselte Dokumente ablegen können. Der DMDA sollte hierzu geeignete Software empfehlen oder kann diese selbst zur Verfügung stellen.

### **2.6 Konfiguration**

Die Konfiguration der DA sollte der Nutzer über eine Web-Oberfläche durchführen können.

Folgende Merkmale müssen je Dokument bzw. je Kategorie konfigurierbar sein:

- **•** Erlaubte Zugriffsoperationen (vgl. Abschnitt [2.1.2](#page-5-2))
- **•** Minimales Authentisierungsniveau für die jeweilige Zugriffsoperation (vgl. Abschnitt [2.1.1](#page-5-1))

# <span id="page-11-0"></span>**3 Nicht-funktionale Anforderungen**

Die in der DA eingestellten Dokumente müssen dem Nutzer vollständig und unverändert zur Verfügung gestellt werden, bis der Nutzer die betreffenden Dokumente selbst löscht oder das zugehörige De-Mail-Konto aufgelöst worden ist.

Jeder Nutzer eines De-Mail-Kontos hat einen minimalen Speicherplatz pro Konto zur Verfügung. Ist dieser Speicher noch nicht durch Daten des Nutzers belegt, muss ein Dokument in der DA abgelegt werden können. Der Nutzer muss gewarnt werden, falls seine DA nur noch über 10% freien Speicher verfügt, gemessen am maximal vorgesehenen Speicherplatz des De-Mail-Kontos.

# <span id="page-12-0"></span>**4 Datenstrukturen**

In diesem Abschnitt werden die in der DA verwendeten Datenstrukturen beschrieben. Es werden die Elemente der Datenstrukturen bestimmt und abstrakt definiert.

Die formale Definition der Datenstrukturen darf jeder DMDA selbst vornehmen.

### **4.1 Datei**

In der DA eines Nutzers können beliebige Dateien gespeichert werden.

|  |  |  |  |  |  |  | Zu jeder Datei werden die nachfolgend definierten Metadaten in der DA des Nutzers abgelegt. |  |
|--|--|--|--|--|--|--|---------------------------------------------------------------------------------------------|--|
|  |  |  |  |  |  |  |                                                                                             |  |
|  |  |  |  |  |  |  |                                                                                             |  |
|  |  |  |  |  |  |  |                                                                                             |  |

| Nr | Bezeichnung                                      | Werte                                         | Bemerkung                                                      |  |  |  |
|----|--------------------------------------------------|-----------------------------------------------|----------------------------------------------------------------|--|--|--|
| 1  | Nutzerkennung                                    | Kennung und<br>zugehörige De<br>Mail-Adresse  | Kennzeichnung des Besitzers der<br>Datei                       |  |  |  |
| 2  | Verweis auf Datei                                | Dateiname                                     | Dateiname ist in der zugehörigen<br>Kategorie eindeutig        |  |  |  |
| 3  | Authentisierungs-Niveau                          | Normal/Hoch                                   | Authentisierungsniveau des Nutzers<br>bei der letzten Änderung |  |  |  |
| 4  | Datum und Zeit der letzten<br>Änderung in der DA | Datum & Zeit                                  | sekundengenau                                                  |  |  |  |
| 5  | Kategorie-Zuordnung                              | Numerische<br>Schlüsselwerte<br>(siehe 4.2)   | Optional, Mehrfachbelegung                                     |  |  |  |
| 6  | Hashwert der Datei                               | Message-Digest                                |                                                                |  |  |  |
| 7  | Größe der Datei                                  | Numerischer Wert                              |                                                                |  |  |  |
| 8  | Autorisierter Nutzer                             | Kennung oder<br>zugehörige De<br>Mail-Adresse |                                                                |  |  |  |
| 9  | Mindest-Auth.-Niveau - Lesen                     | Normal/Hoch                                   |                                                                |  |  |  |
| 10 | Mindest-Auth.-Niveau –<br>Schreiben/Löschen      | Normal/Hoch                                   |                                                                |  |  |  |

<span id="page-12-1"></span>*Tabelle 1: Metadaten einer Datei*

Der autorisierte Nutzer ist immer identisch mit der Nutzerkennung aus [Tabelle 1.](#page-12-1) Die Metadaten werden von der DA des Nutzers erzeugt. Für jede einzelne Datei werden neue Metadaten definiert. Bei Änderungen oder Löschung der Datei oder der zugehörigen Zugriffsrechte werden die Metadaten ebenfalls geändert bzw. gelöscht.

### <span id="page-13-0"></span>**4.2 Kategorien**

Kategorien sind eigene Objekte, die hierarchisch angeordnet werden können. Sie können beispielsweise als Ordner oder Verzeichnisse abgebildet werden.

Jede Kategorie wird mindestens durch folgende Daten beschrieben:

| Nr | Bezeichnung                      | Wert      | Bemerkung                                                                  |
|----|----------------------------------|-----------|----------------------------------------------------------------------------|
| 1  | Schlüsselwert                    | Numerisch | Eindeutiger Wert in der DA des<br>Nutzers (für die Zuordnung zur<br>Datei) |
| 2  | Bezeichnung                      | Text      |                                                                            |
| 3  | Übergeordnete Kategorie<br>Ebene | Numerisch | Optional: Referenz zu Nr.1                                                 |

*Tabelle 2: Daten der Kategorie (Teil 1)*

Zusätzlich muss zu jedem Kategorie-Objekt folgende Ausprägung von Metadaten existieren:

| Nr | Bezeichnung                              | Wert                                          | Bemerkung                                                                |
|----|------------------------------------------|-----------------------------------------------|--------------------------------------------------------------------------|
| 1  | Nutzerkennung                            | Kennung und<br>zugehörige De<br>Mail-Adresse  | Kennzeichnung des Besitzers der<br>Kategorie                             |
| 2  | Authentisierungs-Niveau                  | Normal/Hoch                                   | Authentisierungsniveau des Nutzers<br>bei der letzten Änderung           |
| 3  | Datum und Zeit der letzten<br>Änderung   | Datum & Zeit                                  | Sekundengenau für jede Kategorie<br>(unabhängig von<br>Dateizuordnungen) |
| 4  | Autorisierter Nutzer                     | Kennung oder<br>zugehörige De<br>Mail-Adresse |                                                                          |
| 5  | Mindest-Auth.-Niveau - Lesen             | Normal/Hoch                                   |                                                                          |
| 6  | Mindest-Auth.-Niveau –<br>Ändern/Löschen | Normal/Hoch                                   |                                                                          |

<span id="page-13-1"></span>*Tabelle 3: Metadaten der Kategorie (Teil 2)*

Der autorisierte Nutzer ist immer identisch mit der Nutzerkennung aus Tabelle [3.](#page-13-1)

### **4.3 Meldungen**

Meldungen sind Informationen der DA an den Nutzer und können in Abhängigkeit der Benutzerschnittstelle, die der Nutzer verwendet, unterschiedlich dargestellt und bekannt gemacht werden. Bspw. können sie im Webbrowser dargestellt oder auch als Meldungs-Nachricht (siehe [TR DM FU PVD]) in das Postfach des Nutzers übermittelt werden.

<span id="page-15-0"></span>In diesem Abschnitt wird der funktionale Ablauf der DA für Upload, Download sowie zur Verwaltung und Suche von Dateien (in diesem Zusammenhang die Dokumente) in einem Aktivitätsdiagramm dargestellt. Eine Legende zu den Symbolen des Aktivitätsdiagramms findet sich in Abschnitt [8](#page-58-0). Eine detaillierte technisch-funktionale Beschreibung der einzelnen Aktionen bzw. Schritte des Aktivitätsdiagramms erfolgt im Abschnitt [6](#page-22-0).

![](_page_16_Figure_1.jpeg)

![](_page_17_Figure_1.jpeg)

![](_page_18_Figure_1.jpeg)

![](_page_19_Figure_1.jpeg)

![](_page_20_Figure_1.jpeg)

![](_page_21_Figure_1.jpeg)

<span id="page-22-0"></span>Im Folgenden werden die einzelnen Schritte des Aktivitätsdiagramms aus Abschnitt [5](#page-15-0) für Upload, Download sowie zur Verwaltung und Suche von Dokumenten und Dateien beschrieben. Eine Beschreibung, wie die einzelnen Schritte strukturiert sind, findet sich in Abschnitt [9.](#page-60-0) Alternativ zu der unten dargestellten Schrittfolge kann eine Anmeldung auch vor Schritt 1 erfolgen, z.B. bei Web-basierten Anwendungen. Funktionen, die vom System wiederholt ausgeführt werden oder vom Nutzer interaktiv aufgerufen werden können, wenn er an seiner DA angemeldet ist, werden in Abschnitt [7](#page-55-0) dargestellt. Die referenzierten Funktionen des Account-, Schadsoftware- und Zeitdienstes werden in [TR DM ACM FU] und [TR DM IT-BInfra FU] erläutert.

### <span id="page-22-2"></span>**6.1 Upload und Download von Dateien**

<span id="page-22-1"></span>

| Schritt 1        | Datei(en) auswählen                                                                                           |
|------------------|---------------------------------------------------------------------------------------------------------------|
| Kurzbeschreibung | Der Nutzer wählt die Datei(en) im lokalen System, die er in der DA<br>speichern möchte.                       |
| Akteure          | Nutzer                                                                                                        |
| Auslöser         | Nutzer                                                                                                        |
| Vorbedingung     |                                                                                                               |
| Input            | Datei(en)                                                                                                     |
|                  | (Die ausgewählten Dateien können bereits durch den Nutzer<br>verschlüsselt worden sein)                       |
| Ergebnis         | Datei(en) ausgewählt                                                                                          |
| Nachbedingung    |                                                                                                               |
| Ablauf           | Auswahl der Datei(en) in einem lokal verfügbaren Speicherbereich                                              |
| Fehlerfälle      | FC-01: Keine Auswahl getroffen                                                                                |
| Schritt 2        | Entscheidungsknoten:<br>Soll die Datei(en) verschlüsselt werden, bevor<br>sie auf dem Server gespeichert wird |
| Kurzbeschreibung | Durch den Nutzer wird entschieden, ob die Datei(en) verschlüsselt<br>werden soll.                             |
| ja               | Schritt 3                                                                                                     |
| nein             | Schritt 4                                                                                                     |
| Schritt 3        | Datei(en) auf Nutzer-Seite verschlüsseln                                                                      |
| Kurzbeschreibung | Die Datei(en) werden auf Seite des Nutzers verschlüsselt.                                                     |

#### <span id="page-22-3"></span>**6.1.1 Upload einer Datei in die DA**

<span id="page-23-0"></span>

| Akteure                             | Nutzer                                                                                                                  |  |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------|--|
| Auslöser                            | Nutzer                                                                                                                  |  |
| Vorbedingung                        |                                                                                                                         |  |
| Input                               | Verschlüsselungsmethode                                                                                                 |  |
|                                     | Verschlüsselungsschlüssel des Nutzers                                                                                   |  |
|                                     | Datei(en)                                                                                                               |  |
| Ergebnis                            | Verschlüsselte Datei(en)                                                                                                |  |
| Nachbedingung                       |                                                                                                                         |  |
| Ablauf                              | Es wird mit einem auf dem Nutzer-System verfügbaren<br>Verschlüsselungstool eine Verschlüsselung der Datei vorgenommen. |  |
| Fehlerfälle                         | FC-01: kein geeigneter Verschlüsselungsschlüssel vorhanden                                                              |  |
|                                     | FC-02: Verschlüsselungsmethode wird nicht unterstützt                                                                   |  |
| Schritt 4<br>Kategorie(n) auswählen |                                                                                                                         |  |
| Kurzbeschreibung                    | Es wird definiert, zu welchen Kategorie(n) und welcher Kategorie<br>Ebene die Datei(en) zugeordnet werden sollen.       |  |
|                                     | Hinweis: Welche Kategorien existieren, kann über die Suche-Funktion<br>in Abschnitt 6.3 erfahren werden.                |  |
| Akteure                             | DA-Dienst                                                                                                               |  |
| Auslöser                            | Nutzer                                                                                                                  |  |
| Vorbedingung                        |                                                                                                                         |  |
| Input                               | Kategorie-Ebene                                                                                                         |  |
|                                     | Kategorie(n)                                                                                                            |  |
| Ergebnis                            | Zuordnung der Kategorie(n) bzw. der Kategorie-Ebene(n) getroffen.                                                       |  |
| Nachbedingung                       |                                                                                                                         |  |
| Ablauf                              | Der Nutzer wählt die Kategorie(n) aus, die der heraufzuladenden<br>Datei(en) zugeordnet werden sollen.                  |  |
| Fehlerfälle                         | FC-01: Keine Kategorie(n) ausgewählt.                                                                                   |  |
|                                     | FC-02: Kategorie vom Typ Papierkorb kann nicht gewählt werden.                                                          |  |
| Schritt 5                           | Datei(en) auf den De-Mail-Server übertragen                                                                             |  |
| Kurzbeschreibung                    | Die Datei(en) werden an den DA-Dienst übertragen, der diese<br>entgegennimmt.                                           |  |
| Akteure                             | Nutzer, DA-Dienst                                                                                                       |  |
| Auslöser                            | Nutzer                                                                                                                  |  |
| Vorbedingung                        | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                                                                |  |

<span id="page-24-0"></span>

|                  | Kategorie(n) und Datei(en) ausgewählt.                                            |
|------------------|-----------------------------------------------------------------------------------|
| Input            | Kategorie(n) und jeweilige Kategorie-Ebenen                                       |
|                  | Datei(en)                                                                         |
| Ergebnis         | Datei(en) auf Seite des Nutzers versendet.                                        |
| Nachbedingung    |                                                                                   |
| Ablauf           | Der Nutzer initiiert den Upload der Datei(en).                                    |
|                  | Der DA-Dienst nimmt die Daten entgegen.                                           |
| Fehlerfälle      | FC-01: DA hat die Datei(en) nicht angenommen.                                     |
| Schritt 6        | Datei(en) auf dem De-Mail-Server empfangen                                        |
| Kurzbeschreibung | Die Datei(en) werden durch den DA-Dienst empfangen.                               |
| Akteure          | DA-Dienst                                                                         |
| Auslöser         | Nutzer                                                                            |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut.                         |
| Input            | Kategorie(n) und jeweilige Kategorie-Ebene                                        |
|                  | Datei(en)                                                                         |
| Ergebnis         | Datei(en) sind auf Seiten des DA-Dienstes entgegengenommen worden.                |
| Nachbedingung    |                                                                                   |
| Ablauf           | Der DA-Dienst nimmt die Daten entgegen.                                           |
| Fehlerfälle      | FC-01: Nutzer nicht am De-Mail-Konto angemeldet.                                  |
| Schritt 7        | Prüfung zur Speicherung                                                           |
| Kurzbeschreibung | Der Upload wird hinsichtlich der Berechtigungen geprüft.                          |
| Akteure          | DA-Dienst, Account-Dienst                                                         |
| Auslöser         | Nutzer                                                                            |
| Vorbedingung     |                                                                                   |
| Input            | Kategorie(n) und zugehörige Kategorie-Ebenen                                      |
|                  | Datei(en)                                                                         |
|                  | Authentisierungsniveau des Nutzers                                                |
| Ergebnis         | Prüfungen sind abgeschlossen                                                      |
| Nachbedingung    |                                                                                   |
| Ablauf           | Prüfung, ob die Kategorien in der jeweiligen Kategorie-Ebenen<br>•<br>existieren, |
|                  | Prüfung, ob die Berechtigungen zum Schreiben gegeben sind,<br>•                   |
|                  | Prüfung, ob die Datei(en) nicht bereits mit dem gleichen<br>•                     |

<span id="page-25-1"></span><span id="page-25-0"></span>

|                  | Dateinamen in den Kategorien existieren,                                              |  |
|------------------|---------------------------------------------------------------------------------------|--|
|                  | Prüfung, ob ausreichend Speicher in der DA verfügbar ist,<br>•                        |  |
|                  | Aufruf der Funktion 2.<br>•                                                           |  |
| Fehlerfälle      | FC-01: Kategorien nicht existent                                                      |  |
|                  | FC-02: Berechtigungen reichen nicht aus                                               |  |
|                  | FC-03: Dateiname ist bereits in einer der angegebenen Kategorien<br>existent          |  |
|                  | FC-04: Zu wenig Speicherplatz                                                         |  |
|                  | FC-05: Datei(en) enthalten Malware                                                    |  |
| Schritt 8        | Entscheidungsknoten:<br>positiv abgeschlossene Prüfung                                |  |
| Kurzbeschreibung | Existieren aus Schritt 7 keine Fehler, gilt die Prüfung als positiv<br>abgeschlossen. |  |
| ja               | Schritt 10                                                                            |  |
| nein             | Schritt 9                                                                             |  |
| Schritt 9        | Fehlermeldung erstellen                                                               |  |
| Kurzbeschreibung | Es wird eine Fehlermeldung erstellt und an den Nutzer übermittelt.                    |  |
| Akteure          | DA-Dienst                                                                             |  |
| Auslöser         | DA-Dienst                                                                             |  |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                              |  |
| Input            | Fehlercode                                                                            |  |
| Ergebnis         | Fehlermeldung ist erstellt und an den Nutzer gesandt.                                 |  |
| Nachbedingung    | Stopp                                                                                 |  |
| Ablauf           | Der Fehlermeldung wird aus dem Fehlercode abgeleitet.<br>•                            |  |
|                  | Die Fehlermeldung wird an den Nutzer gesandt.<br>•                                    |  |
| Fehlerfälle      |                                                                                       |  |
| Schritt 10       | Default-Berechtigungen setzen                                                         |  |
| Kurzbeschreibung | Für die Datei(en) werden die Default-Berechtigungen gesetzt.                          |  |
| Akteure          | DA-Dienst, Account-Dienst                                                             |  |
| Auslöser         | Nutzer                                                                                |  |
| Vorbedingung     |                                                                                       |  |
| Input            | Datei(en)                                                                             |  |
|                  | Authentisierungsniveau                                                                |  |
| Ergebnis         | Default-Berechtigungen sind gesetzt.                                                  |  |

| Nachbedingung    |                                                                                                                                                                |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ablauf           | Durch das System werden die Standard-Werte für die Berechtigungen<br>gesetzt:                                                                                  |
|                  | Lesen – gestattet für angemeldeten Nutzer mit aktuellen<br>•<br>Authentisierungsniveau,                                                                        |
|                  | Schreiben – gestattet für angemeldeten Nutzer mit aktuellen<br>•<br>Authentisierungsniveau                                                                     |
|                  | Die Berechtigung des Dokuments muss mindestens dem<br>•<br>geforderten Authentisierungniveau der Kategorie entsprechen,<br>in die das Dokument eingefügt wird. |
| Fehlerfälle      |                                                                                                                                                                |
| Schritt 11       | Hashwerte der Datei ermitteln                                                                                                                                  |
| Kurzbeschreibung | Es werden die Hashwerte der Datei(en) ermittelt.                                                                                                               |
| Akteure          | DA-Dienst                                                                                                                                                      |
| Auslöser         | Nutzer                                                                                                                                                         |
| Vorbedingung     |                                                                                                                                                                |
| Input            | Datei(en)                                                                                                                                                      |
| Ergebnis         | Ein Hashwert für die Metadaten wurde pro Datei ermittelt.                                                                                                      |
| Nachbedingung    |                                                                                                                                                                |
| Ablauf           | Es werden Hashwerte der Datei(en) ermittelt, der in den Metadaten der<br>jeweiligen Datei gespeichert wird.                                                    |
| Fehlerfälle      |                                                                                                                                                                |
| Schritt 12       | Datei(en) durch den DMDA verschlüsseln                                                                                                                         |
| Kurzbeschreibung | Die Datei(en) werden mittels einem DMDA-Schlüssel verschlüsselt                                                                                                |
| Akteure          | DA-Dienst                                                                                                                                                      |
| Auslöser         | Nutzer                                                                                                                                                         |
| Vorbedingung     |                                                                                                                                                                |
| Input            | Unverschlüsselte Datei(en), Verschlüsselungsschlüssel (DMDA)                                                                                                   |
| Ergebnis         | Die Datei(en) liegen nur noch als verschlüsselte Datei auf Seite des<br>DMDA vor.                                                                              |
| Nachbedingung    |                                                                                                                                                                |
| Ablauf           | Verschlüsselung der Datei(en)<br>•                                                                                                                             |
|                  | Unverschlüsselte Datei(en) im Speicher löschen<br>•                                                                                                            |
| Fehlerfälle      | FC-01: kein DMDA-bezogenere Verschlüsselungsschlüssel vorhanden                                                                                                |

| Schritt 13       | Datei(en) speichern                                                                                                          |
|------------------|------------------------------------------------------------------------------------------------------------------------------|
| Kurzbeschreibung | Die verschlüsselten Datei(en) werden in der DA gespeichert.                                                                  |
| Akteure          | DA-Dienst                                                                                                                    |
| Auslöser         | Nutzer                                                                                                                       |
| Vorbedingung     |                                                                                                                              |
| Input            | Kategorie-Ebene, Kategorie(n)                                                                                                |
|                  | Verschlüsselte Datei(en)                                                                                                     |
| Ergebnis         | Verschlüsselte Datei(en) im DA des Nutzers gespeichert.                                                                      |
| Nachbedingung    |                                                                                                                              |
| Ablauf           | Die Datei(en) werden im DA gespeichert.<br>•                                                                                 |
|                  | Ist nur noch <10 % des Speicherplatzes innerhalb der DA frei,<br>•<br>ist eine Meldung an den Nutzer zu senden (Funktion 3). |
| Fehlerfälle      |                                                                                                                              |
| Schritt 14       | Meta-Daten speichern                                                                                                         |
| Kurzbeschreibung | Die Metadaten zu den Datei(en) werden gespeichert.                                                                           |
| Akteure          | DA-Dienst                                                                                                                    |
| Auslöser         | Nutzer                                                                                                                       |
| Vorbedingung     |                                                                                                                              |
| Input            | Dateizuordnung                                                                                                               |
|                  | Authentisierungsniveau                                                                                                       |
|                  | Berechtigungen                                                                                                               |
|                  | Datum und Zeit zum Zeitpunkt der Speicherung im De-Safe                                                                      |
|                  | Hashwerte der Datei(en)                                                                                                      |
| Ergebnis         | Die Metadaten wurden in der DA des Nutzers gespeichert und der<br>jeweiligen Datei(en) zugeordnet.                           |
| Nachbedingung    | Funktion 1                                                                                                                   |
| Ablauf           | Die einzelnen Attribute der Metadaten werden genommen und<br>•<br>als Metadatensatz gespeichert.                             |
|                  | Es erfolgt eine Meldung an den Nutzer.<br>•                                                                                  |
| Fehlerfälle      |                                                                                                                              |
| Schritt 15       | Meldung an den Nutzer                                                                                                        |
| Kurzbeschreibung | Es wird eine Erfolgsmeldung an den Nutzer geschickt.                                                                         |
| Akteure          | DA-Dienst                                                                                                                    |

| Auslöser         | DA-Dienst                                                                               |
|------------------|-----------------------------------------------------------------------------------------|
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                                |
| Input            | Erfolgsmeldung                                                                          |
| Ergebnis         | Eine Erfolgsmeldung wurde erstellt und an den Nutzer übermittelt.                       |
| Nachbedingung    |                                                                                         |
| Ablauf           | Es wird eine Meldung erstellt.<br>•                                                     |
|                  | Diese Meldung wird an den Nutzer übermittelt.<br>•                                      |
| Fehlerfälle      |                                                                                         |
| Schritt 16       | Meldung empfangen                                                                       |
| Kurzbeschreibung | Eine Meldung wird auf Nutzerseite empfangen.                                            |
| Akteure          | Nutzer                                                                                  |
| Auslöser         | DA-Dienst                                                                               |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                                |
| Input            | Meldung                                                                                 |
| Ergebnis         | Die Meldung wurde auf Nutzerseite empfangen.                                            |
| Nachbedingung    |                                                                                         |
| Ablauf           | Die Meldung wird vom Nutzer entgegengenommen.                                           |
| Fehlerfälle      |                                                                                         |
| Schritt 17       | Meldung darstellen                                                                      |
| Kurzbeschreibung | Die Meldung wird auf Seite des Nutzers dargestellt.                                     |
| Akteure          | Nutzer                                                                                  |
| Auslöser         | Nutzer                                                                                  |
| Vorbedingung     |                                                                                         |
| Input            | Meldung                                                                                 |
| Ergebnis         | Die Darstellung der Meldung erfolgte.                                                   |
| Nachbedingung    |                                                                                         |
| Ablauf           | Die Meldungsinformationen werden durch die Client<br>•<br>Komponente interpretiert.     |
|                  | Die Darstellung erfolgt entsprechend den Inhalten der Meldung<br>•<br>(Fehler, Erfolg). |
| Fehlerfälle      |                                                                                         |

*Tabelle 4: Schritte zum Upload von Dateien*

#### **6.1.2 Download von Dateien**

| Schritt 18       | Herunterzuladende Datei(en) auswählen                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Kurzbeschreibung | Der Nutzer wählt die Dateien, die aus seiner DA auf den Speicher des<br>Nutzersystems als Kopie heruntergeladen werden sollen. |
| Akteure          | Nutzer                                                                                                                         |
| Auslöser         | Nutzer                                                                                                                         |
| Vorbedingung     | Zusammenstellung der Liste, ggf. über die Suche-Funktion (siehe 6.3)                                                           |
| Input            | Datei(en) und die zugehörigen Kategorie-Ebenen und Kategorien                                                                  |
| Ergebnis         | Liste der herunterzuladenden Dateien                                                                                           |
| Nachbedingung    |                                                                                                                                |
| Ablauf           | Erstellung der Liste der herunterzuladenden Dateien mit Adressierung<br>(Kategorie)                                            |
| Fehlerfälle      | FC-01: Liste ist leer                                                                                                          |
| Schritt 19       | Liste der herunterzuladenden Dateien übermitteln                                                                               |
| Kurzbeschreibung | Die Liste wird durch den Nutzer an den DA-Dienst übergeben.                                                                    |
| Akteure          | Nutzer, DA-Dienst                                                                                                              |
| Auslöser         | Nutzer                                                                                                                         |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                                                                       |
| Input            | Liste der herunterzuladenden Dateien mit Adressierung (Kategorie)                                                              |
| Ergebnis         | Die Liste der herunterzuladenden Dateien wurde an den DA-Dienst<br>übergeben.                                                  |
| Nachbedingung    |                                                                                                                                |
| Ablauf           | Der Nutzer übergibt die Liste an den DA-Dienst.                                                                                |
| Fehlerfälle      | FC-01: keine Liste übermittelt                                                                                                 |
|                  | FC-02: Liste ist leer                                                                                                          |
|                  |                                                                                                                                |
| Schritt 20       | Liste der herunterzuladenden Dateien empfangen                                                                                 |
| Kurzbeschreibung | Die Liste wird durch den DA-Dienst empfangen.                                                                                  |
| Akteure          | DA-Dienst                                                                                                                      |
| Auslöser         | Nutzer                                                                                                                         |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                                                                       |
| Input            | Liste der herunterzuladenden Dateien mit Adressierung (Kategorie)                                                              |
| Ergebnis         | Die Liste der herunterzuladenden Dateien wurde vom DA-Dienst                                                                   |

<span id="page-30-2"></span><span id="page-30-1"></span><span id="page-30-0"></span>

|                  | empfangen.                                                                                                         |
|------------------|--------------------------------------------------------------------------------------------------------------------|
| Nachbedingung    |                                                                                                                    |
| Ablauf           | Die Liste wird durch den DA-Dienst zur weiteren Verarbeitung<br>empfangen.                                         |
| Fehlerfälle      | FC-01: keine Liste übermittelt                                                                                     |
|                  | FC-02: Liste ist leer                                                                                              |
|                  | FC-03: Nutzer am De-Mail-Konto nicht angemeldet                                                                    |
| Schritt 21       | Möglichkeit zum Herunterladen prüfen                                                                               |
| Kurzbeschreibung | Die Liste zum Herunterladen von Dateien wird hinsichtlich der<br>Berechtigungen geprüft.                           |
| Akteure          | DA-Dienst, Account-Dienst                                                                                          |
| Auslöser         | Nutzer                                                                                                             |
| Vorbedingung     | Liste der herunterzuladenden Dateien wurde an den DA-Dienst<br>übertragen.                                         |
| Input            | Liste der herunterzuladenden Dateien                                                                               |
|                  | Authentisierungsniveau                                                                                             |
| Ergebnis         | Prüfungen sind abgeschlossen.                                                                                      |
| Nachbedingung    |                                                                                                                    |
| Ablauf           | Prüfung, ob die Dateien in den jeweiligen angegebenen<br>•<br>Kategorie-Ebene existieren                           |
|                  | Prüfung, ob die Berechtigung zum Lesen mit dem<br>•<br>Authentisierungsniveau des angemeldeten Nutzers gegeben ist |
|                  | Aufruf von Funktion 2<br>•                                                                                         |
| Fehlerfälle      | FC-01: Datei nicht existent                                                                                        |
|                  | FC-02: Berechtigungen reichen nicht aus                                                                            |
|                  | FC-03: Datei enthält Malware                                                                                       |
| Schritt 22       | Entscheidungsknoten:<br>positiv abgeschlossene Prüfung                                                             |
| Kurzbeschreibung | Existieren aus Schritt 21 keine Fehler, gilt die Prüfung als positiv<br>abgeschlossen.                             |
| ja               | Schritt 24                                                                                                         |
| nein             | Schritt 23                                                                                                         |
| Schritt 23       | Fehler- bzw. Warnmeldung an den Nutzer                                                                             |
| Kurzbeschreibung | Im Fall von FC-01 und FC-02 wird eine Fehlermeldung erstellt und an<br>den Nutzer übermittelt.                     |
|                  | Im Fall von FC-03 Warnmeldung mit Auswahl für den Nutzer, ob die                                                   |

<span id="page-31-0"></span>

|                  | Malware-infizierte Datei trotz der Gefahren heruntergeladen werden<br>soll.                                                            |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Akteure          | DA-Dienst                                                                                                                              |
| Auslöser         | DA-Dienst                                                                                                                              |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                                                                               |
| Input            | Fehlercode                                                                                                                             |
| Ergebnis         | Eine Meldung mit der Fehlerbeschreibung wurde erstellt.                                                                                |
| Nachbedingung    | Bei FC-01, FC-02 und bei Nutzer-bestätigten Abbruch bei FC-03:<br>Stopp                                                                |
|                  | Bei Nutzer-bestätigten Fortführung des Downloads: Schritt 24                                                                           |
| Ablauf           | Bei FC01-, FC-02:<br>•                                                                                                                 |
|                  | Das System erstellt eine Fehlermeldung.<br>◦                                                                                           |
|                  | Das System übermittelt diese Fehlermeldung an den Nutzer.<br>◦                                                                         |
|                  | Bei FC-03:<br>•                                                                                                                        |
|                  | Das System erstellt eine Warnmeldung mit der Wahl zur<br>◦<br>Fortführung des Downloads oder Abbruch des Downloads<br>durch den Nutzer |
|                  | Das System übermittelt diese Warnmeldung an den Nutzer.<br>◦                                                                           |
|                  | Das System wertet die Entscheidung des Nutzers aus.<br>◦                                                                               |
|                  | Das System führt die entsprechende Nachbedingung aus.<br>◦                                                                             |
| Fehlerfälle      | FC-01: Fehlermeldung wird vom Nutzer-System nicht angenommen.                                                                          |
| Schritt 24       | Entschlüsseln der Datei durch den DMDA                                                                                                 |
| Kurzbeschreibung | Die durch den DMDA verschlüsselte Datei wird durch den DMDA<br>entschlüsselt.                                                          |
| Akteure          | DA-Dienst                                                                                                                              |
| Auslöser         | Nutzer                                                                                                                                 |
| Vorbedingung     | Positiv abgeschlossene Prüfung in Schritt 22                                                                                           |
| Input            | Verschlüsselte Datei, Entschlüsselungsschlüssel des DMDA                                                                               |
| Ergebnis         | Entschlüsselte Datei für die Übermittlung an den Nutzer, die in der DA<br>gespeicherte Datei bleibt verschlüsselt                      |
| Nachbedingung    |                                                                                                                                        |
| Ablauf           | Entschlüsselung der Datei                                                                                                              |
| Fehlerfälle      | FC-01: Kein DMDA-bezogener Entschlüsselungsschlüssel vorhanden                                                                         |
| Schritt 25       | Integrität prüfen                                                                                                                      |

| Kurzbeschreibung | Es wird geprüft, ob die Dateien dem Zustand entsprechen, in dem sie<br>bei der Speicherung durch den Nutzer übergeben wurden.                                                 |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Akteure          | DA-Dienst                                                                                                                                                                     |
| Auslöser         | Nutzer                                                                                                                                                                        |
| Vorbedingung     |                                                                                                                                                                               |
| Input            | Herunterzuladende Dateien und zugehörige Metadaten                                                                                                                            |
| Ergebnis         | Abgeschlossene Verifikation hinsichtlich der Integrität der Dateien                                                                                                           |
| Nachbedingung    |                                                                                                                                                                               |
| Ablauf           | Das System erstellt den Hashwert der herunterzuladenden Datei und<br>vergleicht diesen mit dem Hashwert, der bei der Speicherung der Datei<br>in den Metadaten erfasst wurde. |
| Fehlerfälle      | FC-01: Integrität nicht gegeben, Datei oder Metadaten-Eintrag wurde<br>geändert                                                                                               |
| Schritt 26       | Dateien an den Nutzer-Client übermitteln                                                                                                                                      |
| Kurzbeschreibung | Die Dateien, die zum Herunterladen angefragt sind, werden an den<br>Nutzer-Client übertragen.                                                                                 |
| Akteure          | DA-Dienst, Nutzer                                                                                                                                                             |
| Auslöser         | Nutzer                                                                                                                                                                        |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                                                                                                                      |
| Input            | Dateien und zugehörige Kategorie                                                                                                                                              |
| Ergebnis         | Dateien wurden an das Client-System transferiert.                                                                                                                             |
| Nachbedingung    |                                                                                                                                                                               |
| Ablauf           | Es werden die Dateien inkl. der Kategorien an das Client-System<br>transferiert.                                                                                              |
| Fehlerfälle      | FC-01: Daten werden vom Client nicht angenommen                                                                                                                               |
| Schritt 27       | Dateien auf dem Nutzer-Client empfangen                                                                                                                                       |
| Kurzbeschreibung | Die Dateien, die zum Herunterladen angefragt sind, werden auf Seite<br>des Nutzer-Client empfangen.                                                                           |
| Akteure          | Nutzer                                                                                                                                                                        |
| Auslöser         | Nutzer                                                                                                                                                                        |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                                                                                                                      |
| Input            | Dateien und zugehörige Kategorie                                                                                                                                              |
| Ergebnis         | Dateien wurden auf dem Client-System gespeichert                                                                                                                              |
| Nachbedingung    |                                                                                                                                                                               |

<span id="page-33-2"></span><span id="page-33-1"></span><span id="page-33-0"></span>

| Ablauf           | Das Client-System übernimmt die Daten oder Meldungen in den<br>Speicher.                                                                |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Fehlerfälle      |                                                                                                                                         |
| Schritt 28       | Entscheidungsknoten:<br>Ist die Datei auf dem Nutzer-Client<br>verschlüsselt worden                                                     |
| Kurzbeschreibung | Prüfung, ob die Datei durch den Nutzer vor der Übermittlung an den<br>DA-Dienst verschlüsselt wurde.                                    |
| ja               | Schritt 29                                                                                                                              |
| nein             | Schritt 30                                                                                                                              |
| Schritt 29       | Dateien auf dem Nutzer-Client entschlüsseln                                                                                             |
| Kurzbeschreibung | Die Dateien, die durch den Nutzer verschlüsselt an den DA-Dienst<br>übertragen worden sind, werden auf dem Client wieder entschlüsselt. |
| Akteure          | Nutzer                                                                                                                                  |
| Auslöser         | Nutzer                                                                                                                                  |
| Vorbedingung     | Die Daten waren vor der Speicherung in der DA verschlüsselt.                                                                            |
| Input            | Zu entschlüsselnde Datei                                                                                                                |
|                  | Entschlüsselungsmethode                                                                                                                 |
|                  | Entschlüsselungsschlüssel des Nutzers                                                                                                   |
| Ergebnis         | Dateien wurden wieder entschlüsselt und liegen unverschlüsselt vor                                                                      |
| Nachbedingung    |                                                                                                                                         |
| Ablauf           | Entschlüsselung der verschlüsselten Datei<br>•                                                                                          |
|                  | Löschen der verschlüsselten Datei<br>•                                                                                                  |
| Fehlerfälle      | FC-01: Ungültiger Nutzer-bezogener Entschlüsselungsschlüssel                                                                            |
|                  | FC-02: Nicht unterstützte Entschlüsselungsmethode                                                                                       |
| Schritt 30       | Dateien auf dem Datenträger des Nutzers speichern                                                                                       |
| Kurzbeschreibung | Die heruntergeladenen und unverschlüsselten Dateien werden auf dem<br>Datenträger des Nutzers gespeichert.                              |
| Akteure          | Nutzer                                                                                                                                  |
| Auslöser         | Nutzer                                                                                                                                  |
| Vorbedingung     | Schritt 29 (bei verschlüsselten Dateien) oder Schritt 28 (bei<br>unverschlüsselten Dateien)                                             |
| Input            | Heruntergeladene Dateien und zugehörige Kategorien                                                                                      |
|                  | Datenträger des Nutzers und Download-Verzeichnisses                                                                                     |
| Ergebnis         | Dateien sind auf dem Datenträger innerhalb des Download<br>Verzeichnisses des Nutzers gespeichert. (Wenn die Datei durch den            |

|               | Nutzer vor dem Hochladen bereits verschlüsselt wurde, muss der<br>Nutzer die Datei noch entschlüsseln)                                                           |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nachbedingung |                                                                                                                                                                  |
| Ablauf        | Der Nutzer gibt den Datenträger und das Download-Verzeichnis<br>•<br>an.                                                                                         |
|               | Das Client-System speichert die Dateien im Download<br>•<br>Verzeichnis ab.                                                                                      |
| Fehlerfälle   | FC-01: Datenträger existiert nicht<br>FC-02: Download-Verzeichnis existiert nicht<br>FC-03: Datei existiert bereits im entsprechenden Datenträger<br>Verzeichnis |

*Tabelle 5: Schritte zum Download von Dateien*

### **6.2 Verwaltung von Dateien/Kategorien**

#### **6.2.1 Erstellen einer Kategorie**

| Schritt 31       | Antrag für eine neue Kategorie erstellen                         |
|------------------|------------------------------------------------------------------|
| Kurzbeschreibung | Der Nutzer beantragt eine beliebige neue Kategorie in seiner DA. |
| Akteure          | Nutzer                                                           |
| Auslöser         | Nutzer                                                           |
| Vorbedingung     |                                                                  |
| Input            | Kategorie-Bezeichnung                                            |
|                  | Kategorie-Ebene (Default: Wurzel im DA des Nutzers)              |
| Ergebnis         | Antrag für eine neue Kategorie wurde erstellt                    |
| Nachbedingung    |                                                                  |
| Ablauf           | Aufruf der Funktion zum Erstellen von Kategorien im DA<br>•      |
|                  | Angabe der Bezeichnung und weiterer Daten zur Kategorie<br>•     |
| Fehlerfälle      | FC-01: Keine Bezeichnung angegeben                               |
|                  | FC-02: Ungültige Bezeichnung                                     |
| Schritt 32       | Antrag für neue Kategorie übermitteln                            |
| Kurzbeschreibung | Der Antrag für neue Kategorie wurde übermittelt.                 |
| Akteure          | Nutzer                                                           |
| Auslöser         | Nutzer                                                           |

<span id="page-35-0"></span>

| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                                                            |
|------------------|---------------------------------------------------------------------------------------------------------------------|
| Input            | Antrag (Kategorie-Bezeichnung, Kategorie-Ebene)                                                                     |
| Ergebnis         | Antrag wurde an den DA-Dienst übergeben                                                                             |
| Nachbedingung    |                                                                                                                     |
| Ablauf           | Antrag wurde an den DA-Dienst übermittelt                                                                           |
| Fehlerfälle      | FC-01: Antrag wird vom DA-Dienst nicht angenommen                                                                   |
| Schritt 33       | Antrag für neue Kategorie entgegengenommen                                                                          |
| Kurzbeschreibung | Der DA-Dienst nimmt den Antrag für eine neue Kategorie entgegen.                                                    |
| Akteure          | DA-Dienst                                                                                                           |
| Auslöser         | Nutzer                                                                                                              |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                                                            |
| Input            | Antrag (Kategorie-Bezeichnung, Kategorie-Ebene)                                                                     |
| Ergebnis         | Antrag wurde durch den DA-Dienst entgegengenommen.                                                                  |
| Nachbedingung    |                                                                                                                     |
| Ablauf           | Antrag wird durch den DA-Dienst entgegengenommen.                                                                   |
| Fehlerfälle      | FC-01: Nutzer nicht am De-Mail-Konto angemeldet                                                                     |
|                  |                                                                                                                     |
| Schritt 34       | Beantragte Daten prüfen                                                                                             |
| Kurzbeschreibung | Der DA-Dienst prüft den Antrag.                                                                                     |
| Akteure          | DA-Dienst, Account-Dienst                                                                                           |
| Auslöser         | Nutzer                                                                                                              |
| Vorbedingung     |                                                                                                                     |
| Input            | Kategorie-Bezeichnung                                                                                               |
|                  | Kategorie-Ebene                                                                                                     |
|                  | Authentisierungsniveau des Nutzers                                                                                  |
|                  | Weitere Metadaten zur eigenen Berechtigung                                                                          |
| Ergebnis         | Kategorie verifiziert                                                                                               |
| Nachbedingung    |                                                                                                                     |
| Ablauf           | Entgegennahme der Antragsdaten<br>•                                                                                 |
|                  | Prüfung, ob die Kategorie-Ebene existiert<br>•                                                                      |
|                  | Prüfung, ob die Schreibrechte innerhalb der Kategorie-Ebene<br>•<br>bei genutztem Authentisierungsniveau ausreichen |

<span id="page-36-1"></span><span id="page-36-0"></span>

| Fehlerfälle      | FC-01: Kategorie-Bezeichnung in der Kategorie-Ebene schon<br>vorhanden                 |
|------------------|----------------------------------------------------------------------------------------|
|                  | FC-02: angegebene Kategorie-Ebene existiert nicht                                      |
|                  | FC-03: Keine Schreibberechtigung bei genutztem<br>Authentisierungsniveau               |
| Schritt 35       | Entscheidungsknoten:<br>positiv abgeschlossene Prüfung                                 |
| Kurzbeschreibung | Existieren aus Schritt 34 keine Fehler, gilt die Prüfung als positiv<br>abgeschlossen. |
| ja               | Schritt 37                                                                             |
| nein             | Schritt 36                                                                             |
| Schritt 36       | Fehlermeldung an den Nutzer senden                                                     |
| Kurzbeschreibung | Es wird eine Fehlermeldung erstellt und an den Nutzer übermittelt.                     |
| Akteure          | DA-Dienst                                                                              |
| Auslöser         | DA-Dienst                                                                              |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                               |
| Input            | Fehlercode                                                                             |
| Ergebnis         | Eine Meldung mit der Fehlerbeschreibung wurde erstellt.                                |
| Nachbedingung    | Stopp                                                                                  |
| Ablauf           | Das System erstellt eine Fehlermeldung.<br>•                                           |
|                  | Das System übermittelt diese Fehlermeldung an den Nutzer.<br>•                         |
| Fehlerfälle      |                                                                                        |
| Schritt 37       | Kategorie erstellen                                                                    |
| Kurzbeschreibung | Im DA wird eine neue Kategorie erstellt.                                               |
| Akteure          | DA-Dienst                                                                              |
| Auslöser         | Nutzer                                                                                 |
| Vorbedingung     | Schritt 34 ohne Fehlermeldung                                                          |
| Input            | Kategorie-Bezeichnung                                                                  |
|                  | Kategorie-Ebene                                                                        |
|                  | Authentisierungsniveau                                                                 |
|                  | Weitere Metadaten zur eigenen Berechtigung                                             |
| Ergebnis         | Kategorie existiert                                                                    |
| Nachbedingung    | Funktion 1                                                                             |
| Ablauf           | Erstellung der Meta-Daten<br>•                                                         |

|                  | Anlegen der Kategorie<br>•                                                                                                                                                           |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                  | Das Authentisierungsniveau muss mindestens dem der<br>•<br>übergeordneten Kategorie entsprechen. In Unterkategorien kann<br>das geforderte Authentisierungsniveau nur erhöht werden. |
|                  | Meldung an den Nutzer<br>•                                                                                                                                                           |
| Fehlerfälle      |                                                                                                                                                                                      |
| Schritt 38       | Meldung an den Nutzer                                                                                                                                                                |
| Kurzbeschreibung | Es wird eine Meldung erstellt und an den Nutzer übermittelt.                                                                                                                         |
| Akteure          | DA-Dienst                                                                                                                                                                            |
| Auslöser         | DA-Dienst                                                                                                                                                                            |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                                                                                                                             |
| Input            | Erfolgsmeldung                                                                                                                                                                       |
| Ergebnis         | Eine Meldung wurde erstellt.                                                                                                                                                         |
| Nachbedingung    |                                                                                                                                                                                      |
| Ablauf           | Das System erstellt eine Meldung.<br>•                                                                                                                                               |
|                  | Das System übermittelt diese Meldung an den Nutzer.<br>•                                                                                                                             |
| Fehlerfälle      |                                                                                                                                                                                      |
| Schritt 39       | Meldung empfangen                                                                                                                                                                    |
| Kurzbeschreibung | Es wird eine Meldung durch den Nutzer empfangen.                                                                                                                                     |
| Akteure          | Nutzer                                                                                                                                                                               |
| Auslöser         | Nutzer                                                                                                                                                                               |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                                                                                                                             |
| Input            |                                                                                                                                                                                      |
| Ergebnis         | Meldung wurde auf Seite des Nutzers empfangen.                                                                                                                                       |
| Nachbedingung    |                                                                                                                                                                                      |
| Ablauf           | Empfang der Meldung des DA-Dienstes durch den Nutzer                                                                                                                                 |
| Fehlerfälle      |                                                                                                                                                                                      |
| Schritt 40       |                                                                                                                                                                                      |
|                  | Meldung darstellen                                                                                                                                                                   |
| Kurzbeschreibung | Die Inhalte der Meldung                                                                                                                                                              |
| Akteure          | Nutzer                                                                                                                                                                               |
| Auslöser         | Nutzer                                                                                                                                                                               |
| Vorbedingung     |                                                                                                                                                                                      |

| Ergebnis      | Die Meldung wurde dem Nutzer dargestellt.                                                  |
|---------------|--------------------------------------------------------------------------------------------|
| Nachbedingung |                                                                                            |
| Ablauf        | Die vom DA-Dienst empfangene Nachricht wird dem Benutzer nach<br>Aufarbeitung dargestellt. |
| Fehlerfälle   |                                                                                            |

*Tabelle 6: Schritte zum Erstellen einer Kategorie*

#### **6.2.2 Umbenennen von Dateien/Kategorien**

| Schritt 41       | Antrag zum Umbenennen einer Datei/Kategorie erstellen                                                             |
|------------------|-------------------------------------------------------------------------------------------------------------------|
| Kurzbeschreibung | Der Nutzer beantragt eine Umbenennung einer in seiner DA<br>existierenden Datei/Kategorie                         |
| Akteure          | Nutzer                                                                                                            |
| Auslöser         | Nutzer                                                                                                            |
| Vorbedingung     | Kenntnis der umzubenennenden Datei/Kategorie und der Kategorie<br>Ebene, ggf. über die Suche-Funktion (siehe 6.3) |
| Input            | Datei/Kategorie-Bezeichnung_alt                                                                                   |
|                  | Kategorie-Ebene                                                                                                   |
|                  | Datei/Kategorie-Bezeichnung_neu                                                                                   |
| Ergebnis         | Antrag für die Umbenennung einer Datei/Kategorie wurde erstellt                                                   |
| Nachbedingung    |                                                                                                                   |
| Ablauf           | Angabe der umzubenennenden Datei/Kategorie und der<br>•<br>Kategorie-Ebene                                        |
|                  | Angabe der neuen Bezeichnung<br>•                                                                                 |
| Fehlerfälle      | FC-01: Fehlende neue Bezeichnung                                                                                  |
|                  | FC-02: Fehlende Bezeichnung der umzubenennenden Datei/Kategorie                                                   |
| Schritt 42       | Antrag zum Umbenennen einer Datei/Kategorie übermitteln                                                           |
| Kurzbeschreibung | Antrag zum Umbenennen einer Datei/Kategorie an den DA-Dienst<br>übermitteln                                       |
| Akteure          | Nutzer                                                                                                            |
| Auslöser         | Nutzer                                                                                                            |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                                                          |
| Input            | Antrag                                                                                                            |
| Ergebnis         | Antrag wurde an den DA-Dienst übergeben.                                                                          |

<span id="page-39-0"></span>

| Nachbedingung    |                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------|
| Ablauf           | Antrag wurde an den DA-Dienst übermittelt.                                                    |
| Fehlerfälle      |                                                                                               |
| Schritt 43       | Antrag zum Umbenennen einer Datei/Kategorie empfangen                                         |
| Kurzbeschreibung | Der Antrag zum Umbenennen einer Datei/Kategorie wird vom DA<br>Dienst empfangen.              |
| Akteure          | DA-Dienst                                                                                     |
| Auslöser         | Nutzer                                                                                        |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                                      |
| Input            | Antrag                                                                                        |
| Ergebnis         | Antrag ist entgegengenommen.                                                                  |
| Nachbedingung    |                                                                                               |
| Ablauf           | Der Antrag wird vom DA-Dienst entgegengenommen.                                               |
| Fehlerfälle      | FC-01: Nutzer nicht am De-Mail-Konto angemeldet                                               |
| Schritt 44       | Antrag zur Umbenennung einer Datei/Kategorie prüfen                                           |
| Kurzbeschreibung | Es wird geprüft, ob der Antrag zur Umbenennung der Datei/Kategorie<br>angenommen werden kann. |
| Akteure          | DA-Dienst, Account-Dienst                                                                     |
| Auslöser         | Nutzer                                                                                        |
| Vorbedingung     |                                                                                               |
| Input            | Datei/Kategorie-Bezeichnung_alt                                                               |
|                  | Kategorie-Ebene                                                                               |
|                  | Datei/Kategorie-Bezeichnung_neu                                                               |
|                  | Authentisierungsniveau                                                                        |
| Ergebnis         | Antrag wurde geprüft                                                                          |
| Nachbedingung    |                                                                                               |
| Ablauf           | Prüfung der Berechtigung zur Umbenennung<br>•                                                 |
|                  | Prüfung, ob die umzubenennende Datei/Kategorie existiert<br>•                                 |
|                  | Prüfung, ob die neue Datei/Kategorie bereits existiert<br>•                                   |
|                  | Prüfung, ob die umzubenennende Kategorie vom Typ<br>•<br>Papierkorb ist                       |
| Fehlerfälle      | FC-01: die umzubenennende Datei/Kategorie existiert nicht                                     |
|                  | FC-02: der gewünschte Datei-/Kategoriename existiert bereits in der<br>Kategorieebene         |

<span id="page-40-2"></span><span id="page-40-1"></span><span id="page-40-0"></span>

|                  | FC-03: Funktion ist bei dem genutzten Authentisierungsniveau nicht<br>gestattet        |
|------------------|----------------------------------------------------------------------------------------|
|                  | FC-04: Kategorie vom Typ Papierkorb kann nicht umbenannt werden                        |
| Schritt 45       | Entscheidungsknoten:<br>positiv abgeschlossene Prüfung                                 |
| Kurzbeschreibung | Existieren aus Schritt 44 keine Fehler, gilt die Prüfung als positiv<br>abgeschlossen. |
| ja               | Schritt 47                                                                             |
| nein             | Schritt 46                                                                             |
| Schritt 46       | Fehlermeldung an den Nutzer                                                            |
| Kurzbeschreibung | Es wird eine Fehlermeldung erstellt und an den Nutzer übermittelt.                     |
| Akteure          | DA-Dienst                                                                              |
| Auslöser         | DA-Dienst                                                                              |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                               |
| Input            | Fehlercode                                                                             |
| Ergebnis         | Eine Meldung mit der Fehlerbeschreibung wurde erstellt.                                |
| Nachbedingung    | Stopp                                                                                  |
| Ablauf           | Das System erstellt eine Fehlermeldung.<br>•                                           |
|                  | Das System übermittelt diese Fehlermeldung an den Nutzer.<br>•                         |
| Fehlerfälle      |                                                                                        |
| Schritt 47       | Aktivierung der Umbenennung einer Datei/Kategorie                                      |
| Kurzbeschreibung | Die Datei / Kategorie wird umbenannt.                                                  |
| Akteure          | DA-Dienst                                                                              |
| Auslöser         | Nutzer                                                                                 |
| Vorbedingung     | Positiv abgeschlossenen Prüfung in Schritt 45                                          |
| Input            | Datei/Kategorie-Bezeichnung_alt                                                        |
|                  | Kategorie-Ebene                                                                        |
|                  | Datei/Kategorie-Bezeichnung_neu                                                        |
|                  | Authentisierungsniveau                                                                 |
| Ergebnis         | Datei/Kategorie existiert mit neuem Namen                                              |
| Nachbedingung    | Funktion 1                                                                             |
| Ablauf           | Die Metadaten zur Datei/Kategorie werden geändert.                                     |
|                  | Es erfolgt eine Meldung an den Nutzer.                                                 |
|                  | Hinweis: Sollte der Dateiname der gespeicherten Datei nicht über Meta                  |

|                  | Daten, sondern direkt an der gespeicherten Datei geändert werden, ist<br>vor der Umbenennung eine DMDA-bezogenen Entschlüsselung der<br>Datei und nach der Umbenennung eine DMDA-bezogene<br>Verschlüsselung der Datei mit anschließender Löschung der<br>entschlüsselten Datei zu realisieren. |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Fehlerfälle      |                                                                                                                                                                                                                                                                                                 |
| Schritt 48       | Meldung an den Nutzer                                                                                                                                                                                                                                                                           |
| Kurzbeschreibung | Es wird eine Meldung erstellt und an den Nutzer übermittelt.                                                                                                                                                                                                                                    |
| Akteure          | DA-Dienst                                                                                                                                                                                                                                                                                       |
| Auslöser         | DA-Dienst                                                                                                                                                                                                                                                                                       |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                                                                                                                                                                                                                                        |
| Input            | Erfolgsmeldung                                                                                                                                                                                                                                                                                  |
| Ergebnis         | Eine Meldung wurde erstellt.                                                                                                                                                                                                                                                                    |
| Nachbedingung    |                                                                                                                                                                                                                                                                                                 |
| Ablauf           | Das System erstellt eine Meldung.<br>•                                                                                                                                                                                                                                                          |
|                  | Das System übermittelt diese Meldung an den Nutzer.<br>•                                                                                                                                                                                                                                        |
| Fehlerfälle      |                                                                                                                                                                                                                                                                                                 |
|                  |                                                                                                                                                                                                                                                                                                 |
| Schritt 49       | Meldung empfangen                                                                                                                                                                                                                                                                               |
| Kurzbeschreibung | Es wird eine Meldung durch den Nutzer empfangen.                                                                                                                                                                                                                                                |
| Akteure          | Nutzer                                                                                                                                                                                                                                                                                          |
| Auslöser         | Nutzer                                                                                                                                                                                                                                                                                          |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                                                                                                                                                                                                                                        |
| Input            |                                                                                                                                                                                                                                                                                                 |
| Ergebnis         | Meldung wurde auf Seite des Nutzers empfangen.                                                                                                                                                                                                                                                  |
| Nachbedingung    |                                                                                                                                                                                                                                                                                                 |
| Ablauf           | Empfang der Meldung des DA-Dienstes durch den Nutzer                                                                                                                                                                                                                                            |
| Fehlerfälle      |                                                                                                                                                                                                                                                                                                 |
| Schritt 50       | Meldung darstellen                                                                                                                                                                                                                                                                              |
| Kurzbeschreibung | Die Inhalte der Meldung werden dem Nutzer dargestellt.                                                                                                                                                                                                                                          |
| Akteure          | Nutzer                                                                                                                                                                                                                                                                                          |
| Auslöser         | Nutzer                                                                                                                                                                                                                                                                                          |
| Vorbedingung     |                                                                                                                                                                                                                                                                                                 |

| Ergebnis      | Die Meldung wurde dem Nutzer dargestellt.                                                  |
|---------------|--------------------------------------------------------------------------------------------|
| Nachbedingung |                                                                                            |
| Ablauf        | Die vom DA-Dienst empfangene Nachricht wird dem Benutzer nach<br>Aufarbeitung dargestellt. |
| Fehlerfälle   |                                                                                            |

*Tabelle 7: Schritte zum Umbenennen*

#### **6.2.3 Löschen von Dateien/Kategorien**

| Schritt 51       | Antrag auf Löschung einer Datei/Kategorie erstellen                                                                          |
|------------------|------------------------------------------------------------------------------------------------------------------------------|
| Kurzbeschreibung | Der Nutzer wählt die Dateien/Kategorien, die in seiner DA gelöscht<br>werden sollen.                                         |
| Akteure          | Nutzer                                                                                                                       |
| Auslöser         | Nutzer                                                                                                                       |
| Vorbedingung     | Zusammenstellung der Liste, ggf. über die Suche-Funktion (siehe 6.3)                                                         |
| Input            | Bei Dateien: Datei(en) und die zugehörigen Kategorie-Ebenen und Bei<br>Kategorien: Kategorie-Bezeichnung und Kategorie-Ebene |
| Ergebnis         | Liste der zu löschenden Dateien/Kategorien                                                                                   |
| Nachbedingung    |                                                                                                                              |
| Ablauf           | Erstellung der Liste der zu löschenden Dateien bzw. Kategorien                                                               |
| Fehlerfälle      | FC-01: Liste ist leer                                                                                                        |
|                  | FC-02: Keine Bezeichnung angegeben                                                                                           |
|                  | FC-03: Ungültige Bezeichnung                                                                                                 |
| Schritt 52       | Liste der zu löschenden Dateien/Kategorien übermitteln                                                                       |
| Kurzbeschreibung | Antrag zum Löschen einer Kategorie an den DA-Dienst übermitteln                                                              |
| Akteure          | Nutzer, DA-Dienst                                                                                                            |
| Auslöser         | Nutzer                                                                                                                       |
| Vorbedingung     | Gegenseitig authentisierter und verschlüsselter Kommunikationskanal<br>aufgebaut                                             |
| Input            | Liste der zu löschenden Dateien/Kategorien                                                                                   |
| Ergebnis         | Die Liste der zu löschenden Dateien/Kategorien wurde an den DA<br>Dienst übergeben                                           |
| Nachbedingung    |                                                                                                                              |
| Ablauf           | Liste wurde an den DA-Dienst übermittelt.                                                                                    |

<span id="page-43-0"></span>

| Fehlerfälle      |                                                                                                                |
|------------------|----------------------------------------------------------------------------------------------------------------|
| Schritt 53       | Liste der zu löschenden Dateien/Kategorien empfangen                                                           |
| Kurzbeschreibung | Die Liste wird vom DA-Dienst empfangen.                                                                        |
| Akteure          | DA-Dienst                                                                                                      |
| Auslöser         | Nutzer                                                                                                         |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                                                       |
| Input            | Liste der zu löschenden Dateien/Kategorien                                                                     |
| Ergebnis         | Die Liste der zu löschenden Dateien/Kategorien wurde von dem DA<br>Dienst empfangen.                           |
| Nachbedingung    |                                                                                                                |
| Ablauf           | Die Liste wird vom DA-Dienst entgegengenommen.                                                                 |
| Fehlerfälle      | FC-01: Nutzer nicht am De-Mail-Konto angemeldet                                                                |
|                  | FC-02: Liste ist leer                                                                                          |
| Schritt 54       | Antrag zum Löschen prüfen                                                                                      |
| Kurzbeschreibung | Die in der Liste angegebenen Dateien/Kategorien werden hinsichtlich<br>der Berechtigungen zum Löschen geprüft. |
| Akteure          | DA-Dienst, Account-Dienst                                                                                      |
| Auslöser         | Nutzer                                                                                                         |
| Vorbedingung     |                                                                                                                |
| Input            | Liste der zu löschenden Dateien/Kategorien                                                                     |
|                  | Authentisierungsniveau des Nutzers                                                                             |
| Ergebnis         | Prüfungen sind abgeschlossen.                                                                                  |
| Nachbedingung    |                                                                                                                |
| Ablauf           | Für Dateien                                                                                                    |
|                  | Prüfung, ob die Datei(en) in der jeweiligen angegebenen<br>•<br>Kategorie-Ebene existiert.                     |
|                  | Prüfung, ob die Berechtigung zum Löschen mit dem<br>•<br>Authentisierungsniveau des Nutzers gegeben ist.       |
|                  | Für Kategorien                                                                                                 |
|                  | Prüfung, ob die zu löschende Kategorie existiert.<br>•                                                         |
|                  | Prüfung, ob die Löschung bei dem Authentisierungsniveau<br>•<br>gestattet ist.                                 |
|                  | Prüfung, ob keine weiteren Kategorien in der Kategorie<br>•<br>existieren.                                     |

<span id="page-44-1"></span><span id="page-44-0"></span>

|                  | Prüfung, ob der Kategorie keine Dateien zugeordnet sind.<br>•                                                                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                  | Prüfung, ob die zu löschende Kategorie vom Typ Papierkorb ist.<br>•                                                                                                                                                                                                        |
| Fehlerfälle      | FC-01: Berechtigungen reichen nicht aus                                                                                                                                                                                                                                    |
|                  | FC-02: Kategorie/Datei existiert nicht                                                                                                                                                                                                                                     |
|                  | FC-03: Dateien sind der Kategorie zugeordnet                                                                                                                                                                                                                               |
|                  | FC-04: Es gibt Kategorien in dieser Kategorie                                                                                                                                                                                                                              |
|                  | FC-05: Kategorie vom Typ Papierkorb kann nicht gelöscht werden                                                                                                                                                                                                             |
| Schritt 55       | Entscheidungsknoten:<br>positiv abgeschlossene Prüfung                                                                                                                                                                                                                     |
| Kurzbeschreibung | Existieren aus Schritt 54 keine Fehler, gilt die Prüfung als positiv<br>abgeschlossen.                                                                                                                                                                                     |
| ja               | Schritt 57                                                                                                                                                                                                                                                                 |
| nein             | Schritt 56                                                                                                                                                                                                                                                                 |
| Schritt 56       | Fehlermeldung an den Nutzer                                                                                                                                                                                                                                                |
| Kurzbeschreibung | Es wird eine Fehlermeldung erstellt und an den Nutzer übermittelt.                                                                                                                                                                                                         |
| Akteure          | DA-Dienst                                                                                                                                                                                                                                                                  |
| Auslöser         | DA-Dienst                                                                                                                                                                                                                                                                  |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                                                                                                                                                                                                                   |
| Input            | Fehlercode                                                                                                                                                                                                                                                                 |
| Ergebnis         | Eine Meldung mit der Fehlerbeschreibung wurde erstellt.                                                                                                                                                                                                                    |
| Nachbedingung    | Stopp                                                                                                                                                                                                                                                                      |
| Ablauf           | Das System erstellt eine Fehlermeldung.<br>•                                                                                                                                                                                                                               |
|                  | Das System übermittelt diese Fehlermeldung an den Nutzer.<br>•                                                                                                                                                                                                             |
| Fehlerfälle      |                                                                                                                                                                                                                                                                            |
| Schritt 57       | Dateien/Kategorien löschen                                                                                                                                                                                                                                                 |
| Kurzbeschreibung | Die Dateien, die in der Liste der zu löschenden Dateien enthalten sind,<br>und die zugehörigen Metadaten werden in die Kategorie Papierkorb<br>verschoben. Dateien der Kategorie Papierkorb werden<br>unwiederbringlich gelöscht. Zu löschende Kategorien werden entfernt. |
| Akteure          | DA-Dienst                                                                                                                                                                                                                                                                  |
| Auslöser         | Nutzer                                                                                                                                                                                                                                                                     |
| Vorbedingung     |                                                                                                                                                                                                                                                                            |
| Input            | Liste zu löschender Dateien/Kategorien                                                                                                                                                                                                                                     |
| Ergebnis         | Für Dateien: Dateien sind der Kategorie Papierkorb zugeordnet, oder<br>gelöscht und lassen sich nicht wiederherstellen.                                                                                                                                                    |

|                  | Für Kategorien: Kategorie existiert nicht mehr.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nachbedingung    | Funktion 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Ablauf           | Für Dateien:<br>Das System löscht die in der Liste angegebenen Dateien<br>•<br>innerhalb des DA des angemeldeten Benutzers, wenn diese der<br>Kategorie Papierkorb zugeordnet waren. Die zugehörigen<br>Metadaten der Dateien werden ebenfalls gelöscht.<br>oder<br>Das System setzt für die zu löschenden Dateien, die bisher nicht<br>•<br>der Kategorie Papierkorb zugeordnet waren, die Kategorie<br>Papierkorb und entfernt Zuordnungen zu anderen Kategorien.<br>Für Kategorien: |
| Fehlerfälle      | Die Kategorie wird mit den zugehörigen Metadaten gelöscht.<br>•                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Schritt 58       | Meldung an den Nutzer                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Kurzbeschreibung | Es wird eine Meldung erstellt und an den Nutzer übermittelt.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Akteure          | DA-Dienst                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Auslöser         | DA-Dienst                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Input            | Erfolgsmeldung                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Ergebnis         | Eine Meldung wurde erstellt.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Nachbedingung    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Ablauf           | Das System erstellt eine Meldung.<br>•                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                  | Das System übermittelt diese Meldung an den Nutzer.<br>•                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Fehlerfälle      | FC-01: Meldung wird vom Nutzer-System nicht angenommen.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Schritt 59       | Meldung empfangen                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Kurzbeschreibung | Es wird eine Meldung durch den Nutzer empfangen.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Akteure          | Nutzer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Auslöser         | Nutzer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Input            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Ergebnis         | Meldung wurde auf Seite des Nutzers empfangen.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Nachbedingung    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Ablauf           | Empfang der Meldung des DA-Dienstes durch den Nutzer.                                                                                                                                                                                                                                                                                                                                                                                                                                  |

| Fehlerfälle      |                                                                                            |
|------------------|--------------------------------------------------------------------------------------------|
| Schritt 60       | Meldung darstellen                                                                         |
| Kurzbeschreibung | Die Inhalte der Meldung werden dem Nutzer dargestellt.                                     |
| Akteure          | Nutzer                                                                                     |
| Auslöser         | Nutzer                                                                                     |
| Vorbedingung     |                                                                                            |
| Input            | Meldungsinhalte                                                                            |
| Ergebnis         | Die Meldung wurde dem Nutzer dargestellt.                                                  |
| Nachbedingung    |                                                                                            |
| Ablauf           | Die vom DA-Dienst empfangene Nachricht wird dem Benutzer nach<br>Aufarbeitung dargestellt. |
| Fehlerfälle      |                                                                                            |

*Tabelle 8: Schritte zum Löschen*

#### **6.2.4 Ändern der Berechtigungen für Dokumente und Kategorien**

| Schritt 61       | Antrag auf Änderung der Berechtigung erstellen                                                                              |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Kurzbeschreibung | Der Nutzer beantragt eine Änderung einer Berechtigung von Dateien/<br>Kategorien in seiner DA.                              |
| Akteure          | Nutzer                                                                                                                      |
| Auslöser         | Nutzer                                                                                                                      |
| Vorbedingung     | Kenntnis der Dateien/Kategorien, für die die Änderung durchgeführt<br>werden soll, ggf. über die Suche-Funktion (siehe 6.3) |
| Input            | Kategorie-Ebene                                                                                                             |
|                  | Kategorie-Bezeichnung                                                                                                       |
|                  | Unterkategorien rekursiv ändern                                                                                             |
|                  | Datei (optional)                                                                                                            |
|                  | Neue Berechtigungsdaten                                                                                                     |
| Ergebnis         | Antrag auf Änderung der Berechtigung wurde erstellt                                                                         |
| Nachbedingung    |                                                                                                                             |
| Ablauf           | Angabe der Änderungen                                                                                                       |
| Fehlerfälle      | FC-01: Keine Änderung angegeben                                                                                             |
| Schritt 62       | Antrag zur Änderung von Berechtigungen übermitteln                                                                          |
| Kurzbeschreibung | Antrag zur Änderung von Berechtigungen an den DA-Dienst<br>übermitteln                                                      |

<span id="page-47-0"></span>

| Akteure          | Nutzer                                                                  |
|------------------|-------------------------------------------------------------------------|
| Auslöser         | Nutzer                                                                  |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                |
| Input            | Antrag                                                                  |
| Ergebnis         | Antrag wurde an den DA-Dienst übergeben.                                |
| Nachbedingung    |                                                                         |
| Ablauf           | Antrag wurde an den DA-Dienst übermittelt.                              |
| Fehlerfälle      |                                                                         |
| Schritt 63       | Antrag zur Änderung von Berechtigungen empfangen                        |
| Kurzbeschreibung | Antrag zur Änderung von Berechtigungen durch den DA-Dienst<br>empfangen |
| Akteure          | Nutzer                                                                  |
| Auslöser         | Nutzer                                                                  |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                |
| Input            | Antrag                                                                  |
| Ergebnis         | Antrag wurde durch den DA-Dienst empfangen.                             |
| Nachbedingung    |                                                                         |
| Ablauf           | Empfang des Antrages                                                    |
| Fehlerfälle      | FC-01: Nutzer am De-Mail-Konto nicht angemeldet                         |
| Schritt 64       | Antrag prüfen                                                           |
| Kurzbeschreibung | Der DA-Dienst prüft den Antrag zur Änderung der Berechtigungen.         |
| Akteure          | DA-Dienst, Account-Dienst                                               |
| Auslöser         | Nutzer                                                                  |
| Vorbedingung     |                                                                         |
| Input            | Kategorie-Ebene                                                         |
|                  | Kategorie-Bezeichnung                                                   |
|                  | Unterkategorien rekursiv ändern                                         |
|                  | Datei (optional)                                                        |
|                  | Neue Berechtigungsdaten                                                 |
|                  | Für die Anmeldung genutztes Authentisierungsniveau                      |
| Ergebnis         | Der Antrag wurde geprüft.                                               |
| Nachbedingung    |                                                                         |
| Ablauf           | Prüfung, ob die Kategorie bzw. die Datei innerhalb der<br>•             |

<span id="page-48-1"></span><span id="page-48-0"></span>

| Kurzbeschreibung | Die beantragten Berechtigungen werden in der DA geändert.                                                                                                |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schritt 67       | Berechtigungen ändern                                                                                                                                    |
| Fehlerfälle      |                                                                                                                                                          |
|                  | Das System übermittelt diese Fehlermeldung an den Nutzer<br>•                                                                                            |
| Ablauf           | Das System erstellt eine Fehlermeldung<br>•                                                                                                              |
| Nachbedingung    | Stopp                                                                                                                                                    |
| Ergebnis         | Eine Meldung mit der Fehlerbeschreibung wurde erstellt.                                                                                                  |
| Input            | Fehlercode                                                                                                                                               |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                                                                                                 |
| Auslöser         | DA-Dienst                                                                                                                                                |
| Akteure          | DA-Dienst                                                                                                                                                |
| Kurzbeschreibung | Es wird eine Fehlermeldung erstellt und an den Nutzer übermittelt.                                                                                       |
| Schritt 66       | Fehlermeldung an den Nutzer                                                                                                                              |
| nein             | Schritt 66                                                                                                                                               |
| ja               | Schritt 67                                                                                                                                               |
| Kurzbeschreibung | Existieren aus Schritt 64 keine Fehler, gilt die Prüfung als positiv<br>abgeschlossen.                                                                   |
| Schritt 65       | Entscheidungsknoten:<br>positiv abgeschlossene Prüfung                                                                                                   |
|                  | FC-06: Authentisierungsniveau kann nicht zugeordnet werden                                                                                               |
|                  | FC-05: Berechtigungen in sich nicht stimmig                                                                                                              |
|                  | FC-04: Authentisierungsniveau zu niedrig                                                                                                                 |
|                  | FC-03: Keine Berechtigungen zur Änderung                                                                                                                 |
|                  | FC-02: Kategorie existiert nicht                                                                                                                         |
| Fehlerfälle      | mindestens der übergeordneten Kategorie entsprechen.<br>FC-01: Datei existiert nicht                                                                     |
|                  | Prüfung, ob die Berechtigung in sich stimmig ist. Das<br>•<br>Authentisierungsniveau für die Datei/Kategorie muss                                        |
|                  | Prüfung, ob die Berechtigung zum Ändern der Kategorie oder<br>•<br>Datei vorhanden ist.                                                                  |
|                  | Prüfung, ob das Authentisierungsniveau der Anmeldung gleich<br>•<br>oder höher dem zu setzenden Authentisierungsniveau in den<br>Berechtigungsdaten ist. |
|                  | Prüfung, ob das genutzte Authentisierungsniveau ausreicht.<br>•                                                                                          |
|                  | Kategorie existiert.                                                                                                                                     |

| Akteure          | DA-Dienst                                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------------------------------|
| Auslöser         | Nutzer                                                                                                                   |
| Vorbedingung     |                                                                                                                          |
| Input            | Kategorie-Ebene                                                                                                          |
|                  | Kategorie-Bezeichnung                                                                                                    |
|                  | Unterkategorien rekursiv ändern                                                                                          |
|                  | Datei (optional)                                                                                                         |
|                  | Neue Berechtigungsdaten                                                                                                  |
|                  | Für die Anmeldung genutztes Authentisierungsniveau                                                                       |
| Ergebnis         | Die Berechtigungen sind neu gesetzt.                                                                                     |
| Nachbedingung    | Funktion 1                                                                                                               |
| Ablauf           | Die Berechtigungen werden innerhalb der Metadaten neu<br>•<br>erfasst.                                                   |
|                  | Bei der rekursiven Änderung gelten folgende Regeln:<br>•                                                                 |
|                  | Wenn das Authentisierungsniveau erhöht wird, bleiben<br>◦<br>höhere Anforderungen bestehen                               |
|                  | Wenn das Authentisierungsniveau erniedrigt wird, werden<br>◦<br>die Rechte komplett überschrieben.                       |
|                  | Die Datei/Kategorie hat das Mindest-Auth.-Niveau gleich<br>◦<br>oder höher als seine Kategorie in der sie sich befindet. |
| Fehlerfälle      |                                                                                                                          |
| Schritt 68       | Meldung an den Nutzer                                                                                                    |
| Kurzbeschreibung | Es wird eine Meldung erstellt und an den Nutzer übermittelt.                                                             |
| Akteure          | DA-Dienst                                                                                                                |
| Auslöser         | DA-Dienst                                                                                                                |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                                                                 |
| Input            | Erfolgsmeldung                                                                                                           |
| Ergebnis         | Eine Meldung wurde erstellt.                                                                                             |
| Nachbedingung    |                                                                                                                          |
| Ablauf           | Das System erstellt eine Meldung.<br>•                                                                                   |
|                  | Das System übermittelt diese Meldung an den Nutzer.<br>•                                                                 |
| Fehlerfälle      |                                                                                                                          |
| Schritt 69       | Meldung empfangen                                                                                                        |
| Kurzbeschreibung | Es wird eine Meldung durch den Nutzer empfangen.                                                                         |

| Akteure          | Nutzer                                                                                     |
|------------------|--------------------------------------------------------------------------------------------|
| Auslöser         | Nutzer                                                                                     |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                                   |
| Input            |                                                                                            |
| Ergebnis         | Meldung wurde auf Seite des Nutzers empfangen.                                             |
| Nachbedingung    |                                                                                            |
| Ablauf           | Empfang der Meldung des DA-Dienstes durch den Nutzer                                       |
| Fehlerfälle      |                                                                                            |
| Schritt 70       | Meldung darstellen                                                                         |
| Kurzbeschreibung | Die Inhalte der Meldung werden dem Nutzer dargestellt.                                     |
| Akteure          | Nutzer                                                                                     |
| Auslöser         | Nutzer                                                                                     |
| Vorbedingung     |                                                                                            |
| Input            | Meldungsinhalte                                                                            |
|                  |                                                                                            |
| Ergebnis         | Die Meldung wurde dem Nutzer dargestellt.                                                  |
| Nachbedingung    |                                                                                            |
| Ablauf           | Die vom DA-Dienst empfangene Nachricht wird dem Benutzer nach<br>Aufarbeitung dargestellt. |
| Fehlerfälle      |                                                                                            |

*Tabelle 9: Schritte zur Änderung von Berechtigungen*

### <span id="page-50-0"></span>**6.3 Suche und Anzeige von Dokumenten und Kategorien**

| Schritt 71       | Erstellen einer Suchanfrage                                                             |
|------------------|-----------------------------------------------------------------------------------------|
| Kurzbeschreibung | Der Nutzer erstellt eine Suchanfrage, in der die Suchkriterien enthalten<br>sind.       |
| Akteure          | Nutzer                                                                                  |
| Auslöser         | Nutzer                                                                                  |
| Vorbedingung     |                                                                                         |
| Input            | Suchkriterien können sein:                                                              |
|                  | Teile des Namens oder vollständiger Name der Datei,<br>•<br>einschließlich Datei-Endung |
|                  | Teile des Namens oder vollständige Bezeichnung der Kategorie<br>•                       |

|                  | Datei-MIME-Typ (Format)<br>•<br>Inhalt der Datei (Text)<br>•<br>Einschränkungen hinsichtlich der Kategorien<br>•<br>Letztes Änderungsddatum der Datei<br>•<br>• |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ergebnis         | Anfrage erstellt                                                                                                                                                |
| Nachbedingung    |                                                                                                                                                                 |
| Ablauf           | Angabe der Suchkriterien                                                                                                                                        |
| Fehlerfälle      | FC-01: Keine Suchkriterien erfasst                                                                                                                              |
| Schritt 72       | Suchanfrage übermitteln                                                                                                                                         |
| Kurzbeschreibung | Suchanfrage an den DA-Dienst übermitteln                                                                                                                        |
| Akteure          | Nutzer                                                                                                                                                          |
| Auslöser         | Nutzer                                                                                                                                                          |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                                                                                                        |
| Input            | Suchanfrage                                                                                                                                                     |
| Ergebnis         | Suchanfrage wurde an den DA-Dienst übergeben.                                                                                                                   |
| Nachbedingung    |                                                                                                                                                                 |
| Ablauf           | Suchanfrage wird an den DA-Dienst übermittelt.                                                                                                                  |
| Fehlerfälle      | FC-01: Suchanfrage wurde vom DA-Dienst nicht angenommen.                                                                                                        |
| Schritt 73       | Suchanfrage empfangen                                                                                                                                           |
| Kurzbeschreibung | Suchanfrage wird vom DA-Dienst empfangen.                                                                                                                       |
| Akteure          | DA-Dienst                                                                                                                                                       |
| Auslöser         | Nutzer                                                                                                                                                          |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                                                                                                        |
| Input            | Suchanfrage                                                                                                                                                     |
| Ergebnis         | Suchanfrage ist entgegengenommen                                                                                                                                |
| Nachbedingung    |                                                                                                                                                                 |
| Ablauf           | Suchanfrage wird vom DA-Dienst entgegengenommen.                                                                                                                |
| Fehlerfälle      | FC-01: Nutzer am De-Mail-Konto nicht angemeldet                                                                                                                 |
| Schritt 74       | Entschlüsseln der Dateien                                                                                                                                       |
| Kurzbeschreibung | Die durch den DMDA verschlüsselten Dateien bzw. die<br>nutzerbezogenen Suchindex-Dateien werden durch den DMDA<br>entschlüsselt.                                |

| Akteure          | DA-Dienst                                                                                                                                                                                                                                                   |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Auslöser         | Nutzer                                                                                                                                                                                                                                                      |
| Vorbedingung     |                                                                                                                                                                                                                                                             |
| Input            | Verschlüsselte Dateien / Suchindex-Dateien, Entschlüsselungsschlüssel<br>des DMDA                                                                                                                                                                           |
| Ergebnis         | Entschlüsselte Dateien / Suchindex-Dateien für die Durchführung der<br>Suche, die im DA gespeicherte Dateien/Suchindex-Dateien bleibt<br>verschlüsselt.                                                                                                     |
| Nachbedingung    |                                                                                                                                                                                                                                                             |
| Ablauf           | Entschlüsselung der Dateien / Suchindex-Dateien                                                                                                                                                                                                             |
| Fehlerfälle      | FC-01: Kein DMDA-bezogener Entschlüsselungsschlüssel vorhanden                                                                                                                                                                                              |
| Schritt 75       | Suche durchführen                                                                                                                                                                                                                                           |
| Kurzbeschreibung | Die Suche wird innerhalb der DA des angemeldeten Nutzers ausgeführt.<br>Eine Ergebnisliste wird erstellt.                                                                                                                                                   |
| Akteure          | DA-Dienst                                                                                                                                                                                                                                                   |
| Auslöser         | Nutzer                                                                                                                                                                                                                                                      |
| Vorbedingung     |                                                                                                                                                                                                                                                             |
| Input            | Suchkriterien                                                                                                                                                                                                                                               |
|                  | Authentisierungsniveau                                                                                                                                                                                                                                      |
| Ergebnis         | Es wurde eine Liste mit den Ergebnissen der Suche erstellt und dem<br>Nutzer übermittelt.                                                                                                                                                                   |
|                  | Liste beinhaltet                                                                                                                                                                                                                                            |
|                  | bei Kategorie:<br>•                                                                                                                                                                                                                                         |
|                  | Kategorie-Pfad inkl. aller Kategoriebezeichnungen<br>◦                                                                                                                                                                                                      |
|                  | URL<br>◦                                                                                                                                                                                                                                                    |
|                  | bei Dateien<br>•                                                                                                                                                                                                                                            |
|                  | Kategorie-Pfad inkl. aller Kategoriebezeichnungen<br>◦                                                                                                                                                                                                      |
|                  | Dateiname<br>◦                                                                                                                                                                                                                                              |
|                  | Datum der letzten Änderung in der DA<br>◦                                                                                                                                                                                                                   |
|                  | URL<br>◦                                                                                                                                                                                                                                                    |
| Nachbedingung    |                                                                                                                                                                                                                                                             |
| Ablauf           | Die auf der Basis der Suchkriterien definierte Suche wird ausgeführt.<br>Dabei wird beachtet, dass die Suche ausschließlich die Kategorien bzw.<br>Dateien berücksichtigt, die für den Nutzer und seinem derzeitigen<br>Authentisierungsniveau lesbar sind. |

| Fehlerfälle      |                                                                                                           |
|------------------|-----------------------------------------------------------------------------------------------------------|
| Schritt 76       | Löschung entschlüsselter Dateien                                                                          |
| Kurzbeschreibung | Die für die Suchanfrage entschlüsselten Dateien /Suchindex-Dateien<br>werden sicher gelöscht.             |
| Akteure          | DA-Dienst                                                                                                 |
| Auslöser         | DA-Dienst                                                                                                 |
| Vorbedingung     |                                                                                                           |
| Input            | Entschlüsselte Dateien / Suchindex-Dateien                                                                |
| Ergebnis         | Entschlüsselte Dateien / Suchindex-Dateien sind gelöscht                                                  |
| Nachbedingung    |                                                                                                           |
| Ablauf           | Der DA-Dienst löscht die durch den DMDA entschlüsselten Dateien /<br>Suchindex-Dateien unwiederbringlich. |
| Fehlerfälle      |                                                                                                           |
| Schritt 77       | Liste an den Nutzer senden                                                                                |
| Kurzbeschreibung | Es wird die Liste mit den Suchergebnissen an den Nutzer übermittelt.                                      |
| Akteure          | DA-Dienst, Nutzer                                                                                         |
| Auslöser         | DA-Dienst                                                                                                 |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                                                  |
| Input            | Liste mit Suchergebnissen                                                                                 |
| Ergebnis         | Eine Liste wurde an den Nutzer gesandt.                                                                   |
| Nachbedingung    | Die Ergebnisliste wird durch den DMDA sicher gelöscht.                                                    |
| Ablauf           | Das System übermittelt die Liste an den Nutzer.                                                           |
| Fehlerfälle      | FC-01: Suchergebnisse werden vom Nutzer-System nicht angenommen                                           |
| Schritt 78       | Liste mit Suchergebnissen empfangen                                                                       |
| Kurzbeschreibung | Es wird eine Liste durch den Nutzer empfangen.                                                            |
| Akteure          | Nutzer                                                                                                    |
| Auslöser         | Nutzer, DA-Dienst                                                                                         |
| Vorbedingung     | Sicherer Kanal zwischen Kommunikationspartnern aufgebaut                                                  |
| Input            | Liste                                                                                                     |
| Ergebnis         | Liste wurde auf Seite des Nutzers empfangen.                                                              |
| Nachbedingung    |                                                                                                           |
| Ablauf           | Empfang der Liste des DA-Dienstes durch den Nutzer                                                        |
| Fehlerfälle      |                                                                                                           |

| Schritt 79       | Darstellung der Liste mit den Ergebnissen der Suche            |
|------------------|----------------------------------------------------------------|
| Kurzbeschreibung | Der Nutzer sieht die List der Suchergebnisse ein.              |
| Akteure          | Nutzer                                                         |
| Auslöser         | Nutzer                                                         |
| Vorbedingung     |                                                                |
| Input            |                                                                |
| Ergebnis         | Es wurde eine Liste mit den Ergebnissen der Suche dargestellt. |
| Nachbedingung    |                                                                |
| Ablauf           | Die Ergebnisliste wird für den Nutzer dargestellt.             |
| Fehlerfälle      |                                                                |

*Tabelle 10: Schritte zur Suche und Anzeige von Kategorien/ Dateien*

# <span id="page-55-0"></span>**7 Weitere Funktionen**

Die in diesem Abschnitt beschriebenen Funktionen werden entweder vom System ausgeführt oder können vom Nutzer interaktiv aufgerufen werden, während er an seiner DA angemeldet ist. Eine Beschreibung, wie die einzelnen Funktionen dargestellt werden, findet sich in Abschnitt [9](#page-60-0).

### **7.1 Durch das System ausgeführte Funktionen**

<span id="page-55-2"></span><span id="page-55-1"></span>

| Funktion 1       | Protokollierung von Änderung                                                    |
|------------------|---------------------------------------------------------------------------------|
| Kurzbeschreibung | Aktionen, die zur Änderung der Metadaten führen, werden<br>protokolliert.       |
| Akteure          | DA-Dienst                                                                       |
| Auslöser         | jede Änderung der Metadaten zu einer Kategorie bzw. einer Datei                 |
| Vorbedingung     | Änderung eines Meta-Datums                                                      |
| Input            | Nutzerkennung<br>•                                                              |
|                  | Authentisierungsniveau<br>•                                                     |
|                  | neue Metadaten<br>•                                                             |
|                  | Datum und Zeit<br>•                                                             |
| Ergebnis         | Revisionssichere Speicherung der Änderung von Metadaten                         |
| Nachbedingung    | Auswertbarkeit der Protokolldaten muss zu jeder Zeit gegeben sein.              |
| Ablauf           | Erstellung des Logs<br>•                                                        |
|                  | Revisionssichere Speicherung und Archivierung<br>•                              |
| Fehlerfälle      |                                                                                 |
| Funktion 2       | Prüfung Schadsoftware                                                           |
| Kurzbeschreibung | Es wird eine Prüfung von zu speichernden Dateien hinsichtlich<br>Schadsoftware: |
|                  | Viren,<br>•                                                                     |
|                  | Trojanern,<br>•                                                                 |
|                  | Würmer<br>•                                                                     |
|                  | vorgenommen.                                                                    |
| Akteure          | DA-Dienst, Schadsoftware-Dienst                                                 |
| Auslöser         | Upload und Download von Dateien (siehe Abschnitt 6.1)                           |
| Vorbedingung     | Prüfprogramme mit aktuellen Prüfkonfigurationen                                 |
| Input            | Datei                                                                           |
| Ergebnis         | Information, falls in der Datei Schadsoftware gefunden wird                     |

<span id="page-56-0"></span>

| Nachbedingung    |                                                                                                                                       |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Ablauf           | Datei wird zum Schadsoftware-Scanner übergeben.<br>•                                                                                  |
|                  | Datei wird vom Schadsoftware-Scanner entgegengenommen.<br>•                                                                           |
|                  | Datei wird an die Schadsoftware-Prüfung übergeben.<br>•                                                                               |
| Fehlerfälle      | FC-01: Dateiformat unbekannt und kann nicht auf Schadsoftware<br>geprüft werden.                                                      |
| Funktion 3       | Benachrichtigung bei hohem verbrauchten Speicher                                                                                      |
| Kurzbeschreibung | Wenn der Nutzer nur noch 10 % seines Speichers in seinem DA frei<br>hat, meldet das System bei Übergang dieser Grenze diesen Zustand. |
| Akteure          | DA-Dienst                                                                                                                             |
| Auslöser         | Speicherung von Dateien (siehe Abschnitt 6.1.1)                                                                                       |
| Vorbedingung     | 10 % des zugeordnetes Speichers frei                                                                                                  |
| Input            |                                                                                                                                       |
| Ergebnis         | Meldung erfolgte an den Nutzer.                                                                                                       |
| Nachbedingung    |                                                                                                                                       |
| Ablauf           | DA-Dienst misst freien Speicher.<br>•                                                                                                 |
|                  | Bei Unterschreiten der Grenze von 11 nach 10 % des noch<br>•<br>verfügbaren freien Speicherplatzes wird eine Meldung erstellt.        |
|                  | Die Meldung wird an den Nutzer übermittelt.<br>•                                                                                      |
| Fehlerfälle      |                                                                                                                                       |

*Tabelle 11: Durch das System ausgeführte Funktionen*

### **7.2 Durch den Nutzer initiierte Funktionen**

| Funktion 4       | Einsicht in das Protokoll                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Kurzbeschreibung | Einsicht in das Protokoll der DA                                                                                                        |
|                  | Hinweis: Es werden nur Kategorien bzw. Dateien berücksichtigt, die<br>mit dem aktuellen Authentisierungsniveau des Nutzers lesbar sind. |
| Akteure          | Nutzer                                                                                                                                  |
| Auslöser         | Nutzer                                                                                                                                  |
| Vorbedingung     | Anmeldung am De-Mail-Konto                                                                                                              |
| Input            | Kategorie-Ebene                                                                                                                         |
|                  | Kategoriebezeichnung                                                                                                                    |
|                  | Optional: [Dateiname] oder [Liste über alle in der Kategorie vorhanden                                                                  |

#### 7 Weitere Funktionen

|               | Dateien]                                                                                                                                                                                                                                                                    |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|               | Zeitraum                                                                                                                                                                                                                                                                    |
|               | Einschluss aller Sub-Kategorien                                                                                                                                                                                                                                             |
|               | Bei der Anmeldung genutztes Authentisierungsniveau                                                                                                                                                                                                                          |
| Ergebnis      | Logging-Protokoll                                                                                                                                                                                                                                                           |
| Nachbedingung |                                                                                                                                                                                                                                                                             |
| Ablauf        | Der Nutzer stellt eine Anfrage für die Einsicht in das Protokoll.<br>•                                                                                                                                                                                                      |
|               | In der Anfrage gibt er an: Kategorie-Ebene,<br>•<br>Kategoriebezeichnung, optional ein Dateiname, einen Zeitraum.                                                                                                                                                           |
|               | Der Antrag wird vom DA-Dienst entgegengenommen.<br>•                                                                                                                                                                                                                        |
|               | Der DA-Dienst erstellt über den Filter der im Antrag<br>•<br>angegebenen Daten und dem angemeldeten Nutzer inkl. dessen<br>genutztes Authentisierungsniveau ein Protokoll.                                                                                                  |
|               | Der DA-Dienst signiert dieses Protokoll mit einer dauerhaft<br>•<br>überprüfbaren qualifizierten Signatur und stellt dem Nutzer das<br>Protokoll zur Verfügung (Download oder per<br>Meldungsnachricht)sendet dieses über den Versanddienst an das<br>Postfach des Nutzers. |
|               | Hinweis: Es werden nur Kategorien bzw. Dateien berücksichtigt, die<br>mit dem Authentisierungsniveau bei der Anmeldung lesbar sind.                                                                                                                                         |
| Fehlerfälle   | FC-01: Kein Protokoll für die Datei / Kategorie gefunden                                                                                                                                                                                                                    |
|               | FC-02: angegebene Kategorie nicht gefunden                                                                                                                                                                                                                                  |
|               | FC-03: angegebene Datei nicht gefunden                                                                                                                                                                                                                                      |

*Tabelle 12: Durch den Nutzer initiierte Funktionen*

## <span id="page-58-0"></span>**8 Legende zum Aktivitätsdiagramm**

|                           | Startknoten                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Startknoten               | Der Startknoten ist der Startpunkt eines Prozesses. Ein Prozess darf<br>mehrere Startknoten haben, in diesem Fall beginnen beim Start des<br>Prozesses mehrere Abläufe. Es ist möglich, dass ein Prozess keinen<br>Startknoten besitzt, sondern von einem Ereignis angestoßen wird.                                                                                                                                          |
| Endknoten                 | Endknoten                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                           | Der Endknoten gibt an, dass die Ausführung des Prozesses<br>abgeschlossen ist. Es kann in einem Prozessdiagramm mehrere<br>Ausgänge in Form dieser Endknoten geben. Gibt es zum Zeitpunkt<br>des Erreichens des Endknoten mehrere parallele Abläufe innerhalb des<br>Prozesses, werden beim Erreichen eines Endknoten alle Abläufe<br>gestoppt.                                                                              |
| Stopp                     | Ablaufende                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                           | Das Ablaufende terminiert einen Ablauf. Im Unterschied zum<br>Endknoten, der einen ganzen Prozess beendet, hat das Erreichen des<br>Ablaufenden keinen Effekt auf andere parallele Abläufe, die zu<br>diesem Zeitpunkt innerhalb des Prozesses abgearbeitet werden. Auf<br>diese Weise lassen sich parallele Abläufe gezielt und einzeln beenden.                                                                            |
|                           | Kante                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                           | Die als Pfeile dargestellten Kanten verbinden die einzelnen<br>Komponenten des Diagramms und stellen den Kontrollfluss dar.                                                                                                                                                                                                                                                                                                  |
| Aktion                    | Aktion                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                           | Eine Aktion ist ein einzelner Schritt innerhalb eines Prozesses, der<br>nicht mehr weiter zerlegt wird. Das bedeutet nicht unbedingt, dass die<br>Aktion in der realen Welt nicht mehr weiter zerlegbar wäre, sondern<br>dass die Aktion in diesem Diagramm nicht mehr weiter verfeinert<br>wird. Die Aktion kann Ein- und Ausgabeinformationen besitzen. Der<br>Output einer Aktion kann der Input einer Folge-Aktion sein. |
| Aufruf einer<br>Aktivität | Aufruf einer Aktivität                                                                                                                                                                                                                                                                                                                                                                                                       |
|                           | Mit diesem Symbol kann aus einer Aktivität (Prozess) heraus eine<br>weitere Aktivität aufgerufen werden. Der Aufruf selbst ist eine<br>Aktion, der aufgerufene Ablauf eine weitere Aktivität.                                                                                                                                                                                                                                |
| Ereignis<br>empfangen     | Empfang eines Ereignisses                                                                                                                                                                                                                                                                                                                                                                                                    |
|                           | Diese Aktion wartet auf das Eintreten eines Ereignisses. Nach dem<br>Empfang des Ereignisses wird der im Aktivitätsdiagramm definierte,<br>von dieser Aktion ausgehende Ablauf abgearbeitet.                                                                                                                                                                                                                                 |

| Signal senden       | Senden von Signalen<br>Das Senden von Signalen bedeutet, dass ein Signal an eine<br>empfangende Aktivität gesendet wird. Die empfangende Aktivität<br>nimmt das Signal mit der Aktion "Ereignis empfangen" entgegen und                                                                                                       |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Entscheidungsknoten | kann entsprechend darauf reagieren.<br>Entscheidungsknoten<br>Die Raute stellt eine Verzweigung im Kontrollfluss dar. Eine<br>Verzweigung hat einen Eingang und zwei oder mehrere Ausgänge.<br>Jeder Ausgang wird mit einer Bedingung versehen. Trifft eine<br>Bedingung zu, wird am entsprechenden Ausgang weiter verfahren. |
| Datenobjekt         | Datenobjekt<br>Datenobjekte gehören üblicherweise nicht zum Symbolumfang in<br>UML-Aktivitätsdiagrammen. Sie sind hier jedoch eingeführt worden,<br>um an entscheidender Stelle zu verdeutlichen, welche Datenobjekte,<br>insbesondere im Fokus der Schutzbedarfsanalyse, vorliegen.                                          |

*Tabelle 13: Legende zum Aktivitätsdiagramm*

# <span id="page-60-0"></span>**9 Legende zu Schritten der Ablaufbeschreibung**

Schritte im Aktivitätsdiagramm bezeichnen im Kontrollfluss eingebundene einmalig ablaufende Aktionen.

Schritte werden in diesem Modul als Aktionen auf folgende Art und Weise beschrieben:

| Schritt <Nr.>    | Eindeutiger Name der Aktion                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Kurzbeschreibung | Innerhalb der Kurzbeschreibung erfolgt eine verbale Beschreibung der<br>wesentlichen Funktionalität der Aktion.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Akteure          | Alle Rollen bzw. Dienste, die innerhalb der Aktion in irgendeiner Weise<br>beteiligt sind, werden aufgezählt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Auslöser         | Der Auslöser ist ein Akteur, durch den die Aktion aufgerufen bzw.<br>initialisiert wird.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Vorbedingung     | Unter Vorbedingungen werden die Bedingungen verstanden, die nicht aus<br>einer unmittelbar vorhergehenden Aktion folgen, sondern asynchron erzielt<br>werden müssen. Diese Aktivitäten sind nicht unbedingt in diesem Dokument<br>beschrieben, die Ergebnisse sind jedoch als Vorbedingungen für die<br>Ausführung der hier beschriebenen Aktion notwendig. Auf die Erfüllung<br>dieser Vorbedingungen muss sich die nutzende Aktion verlassen können.                                                                                                                            |
| Input            | Der Auslöser muss bei Initialisierung der Aktion die entsprechenden<br>Informationen an diese übergeben oder durch die Aktion abfragen lassen, so<br>dass eine Verarbeitung der Informationen innerhalb der Aktion erfolgen<br>kann.                                                                                                                                                                                                                                                                                                                                              |
| Ergebnis         | Nach Beendigung der Aktion muss eine bestimmte Information als Resultat<br>erarbeitet bzw. bereitgestellt werden.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Nachbedingung    | Unter Nachbedingungen werden Bedingungen verstanden, die innerhalb<br>dieser Aktion nicht betrachtet werden und durch unmittelbar nachfolgende<br>Aktionen aufgegriffen und dort behandelt werden müssen.                                                                                                                                                                                                                                                                                                                                                                         |
| Ablauf           | Für die innerhalb der Aktion definierte Logik wird ein konkreter Ablauf<br>beschrieben. Die definierte Abfolge muss innerhalb der Aktion durchgeführt<br>und abgeschlossen werden.                                                                                                                                                                                                                                                                                                                                                                                                |
| Fehlerfälle      | Als Fehlerfall wird ein Ergebnis einer Funktion bezeichnet, der innerhalb<br>der Funktionsspezifikation liegt, aber kein Standard-Ergebnis darstellt.                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                  | Die konkrete Behandlung eines Fehlerfalls ist implementierungsabhängig.<br>Je nach Fall können unterschiedliche Lösungsstrategien verwendet werden,<br>bspw. kann eine Aktion zu einem späteren Zeitpunkt wiederholt oder die<br>Aktion abgebrochen werden. Bei Abbruch einer Aktion ist der Nutzer<br>mindestens darüber zu informieren und alle bis zu diesem Schritt<br>generierten temporären Daten müssen gelöscht werden. In den<br>Beschreibungen der Fehlerfälle der Aktionen werden nur mögliche Fehler<br>beschrieben, die innerhalb der Funktionsspezifikation liegen. |

*Tabelle 14: Legende zu Schritten*
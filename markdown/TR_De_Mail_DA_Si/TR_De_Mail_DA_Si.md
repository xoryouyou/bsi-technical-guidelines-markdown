![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_2.jpeg)

## BSI – Technische Richtlinie

| Bezeichnung:       | Dokumentenablage<br>IT-Sicherheit |
|--------------------|-----------------------------------|
| Anwendungsbereich: | De-Mail                           |
| Kürzel:            | BSI TR 01201 Teil 5.3             |
| Version:           | 1.8                               |

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn Tel.: +49 22899 9582-0 E-Mail: [de-mail@bsi.bund.de](mailto:de-mail@bsi.bund.de) Internet: [https://www.bsi.bund.de](https://www.bsi.bund.de/) © Bundesamt für Sicherheit in der Informationstechnik 2024

| 1   | Einleitung4                  |  |
|-----|------------------------------|--|
| 2   | IT-Strukturanalyse5          |  |
| 2.1 | Erfassung des IT-Verbundes5  |  |
| 3   | Bedrohungen6                 |  |
| 3.1 | Verlust der Vertraulichkeit6 |  |
| 3.2 | Verlust der Integrität6      |  |
| 3.3 | Verlust der Verfügbarkeit6   |  |
| 4   | Sicherheitsziele7            |  |
| 5   | Anforderungen8               |  |
| 5.1 | Kryptokonzept8               |  |
| 5.2 | Backup-Konzept8              |  |

## <span id="page-3-0"></span>**1 Einleitung**

Dieses Modul beinhaltet die IT-Sicherheitsanforderungen, die über die generellen Anforderungen aus dem Modul [TR DM IS M] hinausgehen und speziell für die DA anzuwenden sind, und ist Bestandteil von [TR DM DA M]. Dies gilt, sofern die DA angeboten wird.

## <span id="page-4-0"></span>**2 IT-Strukturanalyse**

Die Grundlage für die Erarbeitung dieses Moduls bildet die in [TR DM IS GS] angenommene Netzinfrastruktur eines DMDA.

Bei der Erstellung des realen IT-Sicherheitskonzeptes sind die hier enthaltenen Bedrohungen, Sicherheitsziele, zwingenden Anforderungen und Empfehlungen zu berücksichtigen. Näheres regelt das Modul [TR DM IS M].

### **2.1 Erfassung des IT-Verbundes**

In diesem Modul wird auf den IT-Verbund verwiesen, der bereits in der [TR DM IS GS] skizziert ist.

# <span id="page-5-0"></span>**3 Bedrohungen**

Es gelten die im Modul [TR DM IS M] formulierten Bedrohungen, sowie weitere speziell für die DA geltenden Aspekte.

#### **3.1 Verlust der Vertraulichkeit**

Der Verlust der Vertraulichkeit wird bereits im Modul [TR DM IS M] berücksichtigt. Die Gefahr des Verlustes der Vertraulichkeit besteht im Fall der Dokumentenablage auf unterschiedlichen Ebenen:

- **–** durch den Zugriff von Administratoren, auf die Daten oder auf die Suchindizes, die eine Suche in den Daten ermöglichen,
- **–** durch den Diebstahl von Speichermedien.

#### **3.2 Verlust der Integrität**

Der Verlust der Integrität betrifft in diesem Zusammenhang zum einen die Manipulation von Daten durch Unbefugte und zum anderen die Veränderung der Daten durch technisches Versagen.

#### **3.3 Verlust der Verfügbarkeit**

Der Verlust der Verfügbarkeit betrifft in diesem Zusammenhang zum einen die Nicht-Erreichbarkeit des Dienstes insgesamt sowie die Verfügbarkeit der in der Dokumentenablage abgelegten Daten. Eine unberechtigte Löschung der Daten kann z. B. dazu führen, dass der Nutzer nicht mehr auf seine Daten zugreifen kann.

## <span id="page-6-0"></span>**4 Sicherheitsziele**

Es gelten die Sicherheitsziele, die im Modul [TR DM IS M] formuliert wurden.

# <span id="page-7-0"></span>**5 Anforderungen**

## **5.1 Kryptokonzept**

Da die Speicherung personenbezogener Daten durch den Nutzer ein wesentlicher Zweck der Dokumentenablage ist, sind besondere Maßnahmen bei der Speicherung zu ergreifen. Es sind daher neben den Anforderungen aus dem Modul [TR DM IS M] zum Kryptokonzept die nachfolgenden Anforderungen an die Dokumentenablage umzusetzen.

#### **5.1.1 Vertrauliche Speicherung der Daten**

Die Speicherung sämtlicher vom Nutzer eingestellter Daten auf den Systemen des DMDA hat verschlüsselt zu erfolgen.

Die Verschlüsselung der Daten hat so früh wie möglich nach Eingang auf den Systemen des DMDA zu erfolgen.

Danach darf eine Entschlüsselung der Daten nur automatisiert erfolgen und ausschließlich

- **•** zur Prüfung auf Viren oder Schadsoftware und
- **•** zur Auslieferung an den Nutzer.

Die Verschlüsselung kann mit einem Schlüssel für alle Nutzer erfolgen.

Es gelten folgende Regelungen für die Daten hinsichtlich

- **•** langfristiger Speicherung (z.B. Daten in der DA):
	- **◦** Die Daten müssen einzeln oder in einem Container verschlüsselt gespeichert werden.
- **•** kurzfristiger Speicherung (z.B. in Warteschlange bei Virenscanner):
	- **◦** Das Dateisystem, auf dem die Daten abgelegt werden, muss verschlüsselt sein.

Bei der Erstellung von Suchindizes, für die Suche innerhalb der in der DA abgelegten Daten sind diese ebenfalls verschlüsselt abzulegen.

#### **5.1.2 Integere Speicherung der Daten**

Die Speicherung der Daten auf den Systemen des DMDA hat unverfälscht zu erfolgen.

Dazu muss die Integritätssicherung der Daten so früh wie möglich nach Eingang auf den Systemen des DMDA erfolgen.

Die Integritätsprüfung erfolgt bei der Speicherung sowie beim Abruf der Daten.

#### **5.2 Backup-Konzept**

Maßnahmen zur Sicherung der Daten sind zu berücksichtigen (vgl. Modul [TR DM IS M]).
![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_2.jpeg)

# **NET.1.2 Netzmanagement**

# **1. Beschreibung**

# **1.1. Einleitung**

Ein zuverlässiges Netzmanagement ist Grundvoraussetzung für den sicheren und effizienten Betrieb moderner Netze. Dazu ist es erforderlich, dass das Netzmanagement alle Netzkomponenten umfassend integriert. Außerdem müssen geeignete Maßnahmen umgesetzt werden, um die Netzmanagement-Kommunikation und -infrastruktur zu schützen.

Das Netzmanagement umfasst viele wichtige Funktionen wie z. B. die Netzüberwachung, die Konfiguration der Komponenten, die Behandlung von Ereignissen und die Protokollierung. Eine weitere wichtige Funktion ist das Reporting, das als gemeinsame Plattform für Netz und IT-Systeme angelegt werden kann. Alternativ kann es dediziert als einheitliche Plattform oder als Bestandteil der einzelnen Netzmanagement-Komponenten realisiert werden.

Die Netzmanagement-Infrastruktur besteht aus zentralen Management-Systemen, wie z. B. einem SNMP-Server, Administrations-Endgeräten mit Software für Managementzugriffe und dezentralen Managementagenten. Außerdem gehören dedizierte Managementwerkzeuge, wie z. B. Probes bzw. spezifische Messgeräte sowie Managementprotokolle, wie z. B. SNMP oder SSH, dazu. Auch Managementschnittstellen, wie dedizierte Ethernet-Ports oder Konsolen-Ports, sind Bestandteil einer Netzmanagement-Infrastruktur.

# **1.2. Zielsetzung**

Ziel dieses Bausteins ist es, die Informationssicherheit als integralen Bestandteil des Netzmanagements zu etablieren.

# **1.3. Abgrenzung und Modellierung**

Der Baustein NET.1.2 *Netzmanagement* ist auf jedes Netzmanagement-System (Management-System und zu verwaltende IT-System) anzuwenden, das im Informationsverbund eingesetzt wird. Bei den zu verwaltenden IT-Systemen handelt es sich üblicherweise um einzelne Clients, Server oder aktive Netzkomponenten (Netzkoppelelemente).

Dieser Baustein betrachtet die notwendigen Komponenten und konzeptionellen Aufgaben zum Netzmanagement. Anforderungen zum Systemmanagement für vernetzte Clients und Server werden hier nicht beschrieben.

Der vorliegende Baustein beschreibt, wie das Netzmanagement aufgebaut und abgesichert sowie die zugehörige Kommunikation geschützt werden können. Details bezüglich der Absicherung von Netzkomponenten, insbesondere deren Management-Schnittstellen, werden in den Bausteinen der Schichten NET.2 *Funknetze* und NET.3 *Netzkomponenten* behandelt.

Die in diesem Baustein thematisierte Protokollierung sollte in ein übergreifendes Protokollierungsund Archivierungskonzept eingebunden sein (siehe OPS.1.1.5 *Protokollierung* und OPS.1.2.2 *Archivierung*).

Die Daten des Netzmanagements müssen im Datensicherungskonzept berücksichtigt werden. Anforderungen dazu sind im Baustein CON.3 *Datensicherungskonzept* enthalten.

# **2. Gefährdungslage**

Da IT-Grundschutz-Bausteine nicht auf individuelle Informationsverbünde eingehen können, werden zur Darstellung der Gefährdungslage typische Szenarien zugrunde gelegt. Die folgenden spezifischen Bedrohungen und Schwachstellen sind für den Baustein NET.1.2 *Netzmanagement* von besonderer Bedeutung.

### **2.1. Unberechtigter Zugriff auf zentrale Netzmanagement-Komponenten**

Wenn es bei einem Angriff gelingt, auf Netzmanagement-Lösungen zuzugreifen, z. B. durch ungepatchte Sicherheitslücken oder eine ungenügende Netztrennung, können alle dort angeschlossenen Netzkomponenten kontrolliert und neu konfiguriert werden. So kann z. B. auf schützenswerte Informationen zugegriffen, der Netzverkehr umgeleitet oder auch das gesamte Netz nachhaltig gestört werden.

## **2.2. Unberechtigter Zugriff auf einzelne Netzkomponenten**

Wenn es bei einem Angriff gelingt, auf einzelne Netzkomponenten zuzugreifen, kann die jeweilige Komponente kontrolliert und manipuliert werden. Jeder über die Netzkomponente geleitete Datenverkehr kann somit kompromittiert werden. Darüber hinaus können weiterführende Angriffe vorbereitet werden, um tiefer in das Netz der Institution einzudringen.

# **2.3. Unberechtigte Eingriffe in die Netzmanagement-Kommunikation**

Wird die Netzmanagement-Kommunikation abgehört und manipuliert, können auf diesem Weg aktive Netzkomponenten fehlkonfiguriert bzw. kontrolliert werden. Dadurch kann die Netzintegrität verletzt und die Verfügbarkeit der Netzinfrastruktur eingeschränkt werden. Außerdem können die übertragenen Daten mitgeschnitten und eingesehen werden.

# **2.4. Unzureichende Zeitsynchronisation der Netzmanagement-Komponenten**

Wird die Systemzeit der Netzmanagement-Komponenten unzureichend synchronisiert, können die Protokollierungsdaten eventuell nicht miteinander korreliert werden. Auch kann die Korrelation eventuell zu fehlerhaften Aussagen führen, da die unterschiedlichen Zeitstempel von Ereignissen keine gemeinsame Basis aufweisen. So kann nicht geeignet auf Ereignisse reagiert werden. Probleme können zudem nicht beseitigt werden. Dadurch können beispielsweise Sicherheitsvorfälle und Datenabflüsse unerkannt bleiben.

# **3. Anforderungen**

Im Folgenden sind die spezifischen Anforderungen des Bausteins NET.1.2 *Netzmanagement* aufgeführt. Der oder die Informationssicherheitsbeauftragte (ISB) ist dafür zuständig, dass alle Anforderungen gemäß dem festgelegten Sicherheitskonzept erfüllt und überprüft werden. Bei strategischen Entscheidungen ist der oder die ISB stets einzubeziehen.

Im IT-Grundschutz-Kompendium sind darüber hinaus weitere Rollen definiert. Sie sollten besetzt werden, insofern dies sinnvoll und angemessen ist.

| Zuständigkeiten         | Rollen                |
|-------------------------|-----------------------|
| Grundsätzlich zuständig | IT-Betrieb            |
| Weitere Zuständigkeiten | Planende, Vorgesetzte |

Genau eine Rolle sollte *Grundsätzlich zuständig* sein. Darüber hinaus kann es noch *Weitere Zuständigkeiten* geben. Falls eine dieser weiteren Rollen für die Erfüllung einer Anforderung vorrangig zuständig ist, dann wird diese Rolle hinter der Überschrift der Anforderung in eckigen Klammern aufgeführt. Die Verwendung des Singulars oder Plurals sagt nichts darüber aus, wie viele Personen diese Rollen ausfüllen sollen.

# **3.1. Basis-Anforderungen**

Die folgenden Anforderungen MÜSSEN für diesen Baustein vorrangig erfüllt werden.

#### **NET.1.2.A1 Planung des Netzmanagements (B)**

Die Netzmanagement-Infrastruktur MUSS geeignet geplant werden. Dabei SOLLTEN alle in der Sicherheitsrichtlinie und Anforderungsspezifikation für das Netzmanagement genannten Punkte berücksichtigt werden. Es MÜSSEN mindestens folgende Themen berücksichtigt werden:

- zu trennende Bereiche für das Netzmanagement,
- Zugriffsmöglichkeiten auf die Management-Server,
- Kommunikation für den Managementzugriff,
- eingesetzte Protokolle, z. B. IPv4 und IPv6,
- Anforderungen an Management-Werkzeuge,
- Schnittstellen, um erfasste Ereignis- oder Alarmmeldungen weiterzuleiten,
- Protokollierung, inklusive erforderlicher Schnittstellen zu einer zentralen Protokollierungslösung,
- Reporting und Schnittstellen zu übergreifenden Lösungen sowie
- korrespondierende Anforderungen an die einzubindenden Netzkomponenten.

#### **NET.1.2.A2 Anforderungsspezifikation für das Netzmanagement (B)**

Ausgehend von NET.1.2.A1 *Planung des Netzmanagements* MÜSSEN Anforderungen an die Netzmanagement-Infrastruktur und -Prozesse spezifiziert werden. Dabei MÜSSEN alle wesentlichen Elemente für das Netzmanagement berücksichtigt werden. Auch SOLLTE die Richtlinie für das Netzmanagement beachtet werden.

#### **NET.1.2.A3 ENTFALLEN (B)**

Diese Anforderung ist entfallen.

#### **NET.1.2.A4 ENTFALLEN (B)**

Diese Anforderung ist entfallen.

#### **NET.1.2.A5 ENTFALLEN (B)**

Diese Anforderung ist entfallen.

#### **NET.1.2.A6 Regelmäßige Datensicherung (B)**

Bei der Datensicherung des Netzmanagements MÜSSEN mindestens die Systemdaten für die Einbindung der zu verwaltenden Komponenten bzw. Objekte, Ereignismeldungen, Statistikdaten sowie vorgehaltene Daten für das Konfigurationsmanagement gesichert werden.

#### **NET.1.2.A7 Grundlegende Protokollierung von Ereignissen (B)**

Mindestens folgende Ereignisse MÜSSEN protokolliert werden:

- unerlaubte Zugriffe bzw. Zugriffsversuche,
- Leistungs- oder Verfügbarkeitsschwankungen des Netzes,
- Fehler in automatischen Prozessen (z. B. bei der Konfigurationsverteilung) sowie
- eingeschränkte Erreichbarkeit von Netzkomponenten.

#### **NET.1.2.A8 Zeit-Synchronisation (B)**

Alle Komponenten des Netzmanagements, inklusive der eingebundenen Netzkomponenten, MÜSSEN eine synchrone Uhrzeit nutzen. Die Uhrzeit SOLLTE an jedem Standort innerhalb des lokalen Netzes mittels NTP-Service synchronisiert werden. Ist ein separates Managementnetz eingerichtet, SOLLTE eine NTP-Instanz in diesem Managementnetz positioniert werden.

#### **NET.1.2.A9 Absicherung der Netzmanagement-Kommunikation und des Zugriffs auf Netz-Management-Werkzeuge (B)**

Erfolgt die Netzmanagement-Kommunikation über die produktive Infrastruktur, MÜSSEN dafür sichere Protokolle verwendet werden. Ist dies nicht möglich, MUSS ein eigens dafür vorgesehenes Administrationsnetz (Out-of-Band-Management) verwendet werden (siehe NET.1.1 *Netzarchitektur und -design*).

Falls von einem Netz außerhalb der Managementnetze auf Netzmanagement-Werkzeuge zugegriffen wird, MÜSSEN als sicher geltende Authentisierungs- und Verschlüsselungsmethoden realisiert werden.

#### **NET.1.2.A10 Beschränkung der SNMP-Kommunikation (B)**

Grundsätzlich DÜRFEN im Netzmanagement KEINE unsicheren Versionen des Simple Network Management Protocol (SNMP) eingesetzt werden. Werden dennoch unsichere Protokolle verwendet und nicht über andere sichere Netzprotokolle (z. B. VPN oder TLS) abgesichert, MUSS ein separates Managementnetz genutzt werden. Grundsätzlich SOLLTE über SNMP nur mit den minimal erforderlichen Zugriffsrechten zugegriffen werden. Die Zugangsberechtigung SOLLTE auf dedizierte Management-Server eingeschränkt werden.

## **3.2. Standard-Anforderungen**

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik für diesen Baustein. Sie SOLLTEN grundsätzlich erfüllt werden.

#### **NET.1.2.A11 Festlegung einer Sicherheitsrichtlinie für das Netzmanagement (S)**

Für das Netzmanagement SOLLTE eine Sicherheitsrichtlinie erstellt und nachhaltig gepflegt werden. Die Sicherheitsrichtlinie SOLLTE allen Personen, die am Netzmanagement beteiligt sind, bekannt sein. Die Sicherheitsrichtlinie SOLLTE zudem grundlegend für ihre Arbeit sein. Es SOLLTE regelmäßig und nachvollziehbar überprüft werden, dass die in der Sicherheitsrichtlinie geforderten Inhalte umgesetzt werden. Die Ergebnisse SOLLTEN sinnvoll dokumentiert werden.

Die Sicherheitsrichtlinie SOLLTE festlegen, welche Bereiche des Netzmanagements über zentrale Management-Werkzeuge und -Dienste realisiert werden. Auch SOLLTE sie definieren, inwieweit Aufgaben im Netzmanagement der Institution automatisiert realisiert werden sollen.

Darüber hinaus SOLLTEN Rahmenbedingungen und Vorgaben für die Netztrennung, die Zugriffskontrolle, die Protokollierung sowie für den Schutz der Kommunikation spezifiziert werden. Auch für das eingesetzte Netzmanagement-Werkzeug und für die operativen Grundregeln des Netzmanagements SOLLTEN Rahmenbedingungen und Vorgaben spezifiziert werden.

#### **NET.1.2.A12 Ist-Aufnahme und Dokumentation des Netzmanagements (S)**

Es SOLLTE eine Dokumentation erstellt werden, die beschreibt, wie die Management-Infrastruktur des Netzes aufgebaut ist. Darin SOLLTEN die initiale Ist-Aufnahme sowie alle durchgeführten Änderungen im Netzmanagement enthalten sein. Insbesondere SOLLTE dokumentiert werden, welche Netzkomponenten mit welchen Management-Werkzeugen verwaltet werden. Außerdem SOLLTEN alle für das Netzmanagement benutzten IT-Arbeitsplätze und -Endgeräte sowie alle Informationsbestände, Management-Daten und Informationen über den Betrieb des Netzmanagements erfasst werden. Letztlich SOLLTEN sämtliche Schnittstellen zu Anwendungen und Diensten außerhalb des Netzmanagements dokumentiert werden.

Der so dokumentierte Ist-Zustand der Management-Infrastruktur SOLLTE mit der Dokumentation der Netz-Infrastruktur abgeglichen werden (siehe Baustein NET.1.1 *Netz-Architektur- und Design).*

Die Dokumentation SOLLTE vollständig und immer aktuell sein.

#### **NET.1.2.A13 Erstellung eines Netzmanagement-Konzepts (S)**

Ausgehend von der Sicherheitsrichtlinie für das Netzmanagement SOLLTE ein Netzmanagement-Konzept erstellt und nachhaltig gepflegt werden. Dabei SOLLTEN mindestens folgende Aspekte bedarfsgerecht berücksichtigt werden:

- Methoden, Techniken und Werkzeuge für das Netzmanagement,
- Absicherung des Zugangs und der Kommunikation,
- Netztrennung, insbesondere Zuordnung von Netzmanagement-Komponenten zu Zonen,
- Umfang des Monitorings und der Alarmierung je Netzkomponente,
- Protokollierung,
- Automatisierung, insbesondere zentrale Verteilung von Konfigurationsdateien auf Switches,
- Meldeketten bei Störungen und Sicherheitsvorfällen,
- Bereitstellung von Netzmanagement-Informationen für andere Betriebsbereiche sowie
- Einbindung des Netzmanagements in die Notfallplanung.

#### **NET.1.2.A14 Fein- und Umsetzungsplanung (S)**

Es SOLLTE eine Fein- und Umsetzungsplanung für die Netzmanagement-Infrastruktur erstellt werden. Dabei SOLLTEN alle in der Sicherheitsrichtlinie und im Netzmanagement-Konzept adressierten Punkte berücksichtigt werden.

#### **NET.1.2.A15 Konzept für den sicheren Betrieb der Netzmanagement-Infrastruktur (S)**

Ausgehend von der Sicherheitsrichtlinie für das Netzmanagement und dem Netzmanagement-Konzept SOLLTE ein Konzept für den sicheren Betrieb der Netzmanagement-Infrastruktur erstellt werden. Darin SOLLTE der Anwendungs- und Systembetrieb für die Netzmanagement-Werkzeuge berücksichtigt werden. Auch SOLLTE geprüft werden, wie sich die Leistungen anderer operativer Einheiten einbinden und steuern lassen.

#### **NET.1.2.A16 Einrichtung und Konfiguration von Netzmanagement-Lösungen (S)**

Lösungen für das Netzmanagement SOLLTEN anhand der Sicherheitsrichtlinie, der spezifizierten Anforderungen (siehe NET1.2.A2 *Anforderungsspezifikation für das Netzmanagement*) und der Feinund Umsetzungsplanung aufgebaut, sicher konfiguriert und in Betrieb genommen werden. Danach SOLLTEN die spezifischen Prozesse für das Netzmanagement eingerichtet werden.

#### **NET.1.2.A17 Regelmäßiger Soll-Ist-Vergleich im Rahmen des Netzmanagements (S)**

Es SOLLTE regelmäßig und nachvollziehbar geprüft werden, inwieweit die Netzmanagement-Lösung dem Sollzustand entspricht. Dabei SOLLTE geprüft werden, ob die bestehende Lösung noch die Sicherheitsrichtlinie und Anforderungsspezifikation erfüllt. Auch SOLLTE geprüft werden, inwieweit die umgesetzte Management-Struktur und die genutzten Prozesse dem aktuellen Stand entsprechen. Weiter SOLLTE verglichen werden, ob die Management-Infrastruktur aktuell ist.

#### **NET.1.2.A18 Schulungen für Management-Lösungen (S) [Vorgesetzte]**

Für die eingesetzten Netzmanagement-Lösungen SOLLTEN Schulungs- und Trainingsmaßnahmen konzipiert und durchgeführt werden. Die Maßnahmen SOLLTEN die individuellen Gegebenheiten im Configuration-, Availability- und Capacity-Management sowie typische Situationen im Fehlermanagement abdecken. Die Schulungen und Trainings SOLLTEN regelmäßig wiederholt werden, mindestens jedoch, wenn sich größere technische oder organisatorische Änderungen innerhalb der Netzmanagement-Lösung ergeben.

#### **NET.1.2.A19 ENTFALLEN (S)**

Diese Anforderung ist entfallen.

#### **NET.1.2.A20 ENTFALLEN (S)**

Diese Anforderung ist entfallen.

#### **NET.1.2.A21 Entkopplung der Netzmanagement-Kommunikation (S)**

Direkte Management-Zugriffe von Administrierenden von einem IT-System außerhalb der Managementnetze auf eine Netzkomponente SOLLTEN vermieden werden. Ist ein solcher Zugriff ohne zentrales Management-Werkzeug notwendig, SOLLTE die Kommunikation entkoppelt werden. Solche Sprungserver SOLLTEN im Management-Netz integriert und in einem getrennten Zugangssegment positioniert sein.

#### **NET.1.2.A22 Beschränkung der Management-Funktionen (S)**

Es SOLLTEN NUR die benötigten Management-Funktionen aktiviert werden.

#### **NET.1.2.A23 ENTFALLEN (S)**

Diese Anforderung ist entfallen.

#### **NET.1.2.A24 Zentrale Konfigurationsverwaltung für Netzkomponenten (S)**

Software bzw. Firmware und Konfigurationsdaten für Netzkomponenten SOLLTEN automatisch über das Netz verteilt und ohne Betriebsunterbrechung installiert und aktiviert werden können. Die dafür benötigten Informationen SOLLTEN an zentraler Stelle sicher verfügbar sein sowie in die Versionsverwaltung und die Datensicherung eingebunden werden. Die zentrale Konfigurationsverwaltung SOLLTE nachhaltig gepflegt und regelmäßig auditiert werden.

#### **NET.1.2.A25 Statusüberwachung der Netzkomponenten (S)**

Die grundlegenden Performance- und Verfügbarkeitsparameter der zentralen Netzkomponenten SOLLTEN kontinuierlich überwacht werden. Dafür SOLLTEN vorab die jeweiligen Schwellwerte ermittelt werden (Baselining).

#### **NET.1.2.A26 Alarming und Logging (S)**

Wichtige Ereignisse auf Netzkomponenten und auf den Netzmanagement-Werkzeugen SOLLTEN automatisch an ein zentrales Management-System übermittelt und dort protokolliert werden (siehe OPS.1.1.5 *Protokollierung*). Das zuständige Personal SOLLTE zusätzlich automatisch benachrichtigt werden. Das Alarming und Logging SOLLTE mindestens folgende Punkte beinhalten:

- Ausfall bzw. Nichterreichbarkeit von Netz- oder Management-Komponenten,
- Hardware-Fehlfunktionen,
- fehlerhafte Anmeldeversuche sowie
- kritische Zustände oder Überlastung von IT-Systemen.

Ereignismeldungen bzw. Logging-Daten SOLLTEN einem zentralen Management-System entweder kontinuierlich oder gebündelt übermittelt werden. Alarmmeldungen SOLLTEN sofort wenn sie auftreten übermittelt werden.

#### **NET.1.2.A27 Einbindung des Netzmanagements in die Notfallplanung (S)**

Die Netzmanagement-Lösungen SOLLTEN in die Notfallplanung der Institution eingebunden werden. Dazu SOLLTEN die Netzmanagement-Werkzeuge und die Konfigurationen der Netzkomponenten gesichert und in die Wiederanlaufpläne integriert sein.

#### **NET.1.2.A28 Platzierung der Management-Clients für das In-Band-Management (S)**

Für die Administration sowohl der internen als auch der externen IT-Systeme SOLLTEN dedizierte Management-Clients eingesetzt werden. Dafür SOLLTE mindestens ein Management-Client am äußeren Netzbereich (für die Administration am Internet anliegender IT-Systeme) und ein weiterer im internen Bereich (für die Administration interner IT-Systeme) platziert werden.

#### **NET.1.2.A29 Einsatz von VLANs im Management-Netz (S)**

Werden Managementnetze durch VLANs getrennt, SOLLTE darauf geachtet werden, dass der äußere Paketfilter sowie die daran angeschlossenen Geräte in einem eigenen Teilnetz stehen. Zudem SOLLTE sichergestellt werden, dass das ALG dabei nicht umgangen wird.

## **3.3. Anforderungen bei erhöhtem Schutzbedarf**

Im Folgenden sind für diesen Baustein exemplarische Vorschläge für Anforderungen aufgeführt, die über dasjenige Schutzniveau hinausgehen, das dem Stand der Technik entspricht. Die Vorschläge SOLLTEN bei erhöhtem Schutzbedarf in Betracht gezogen werden. Die konkrete Festlegung erfolgt im Rahmen einer individuellen Risikoanalyse.

#### **NET.1.2.A30 Hochverfügbare Realisierung der Management-Lösung (H)**

Zentrale Management-Lösungen SOLLTEN hochverfügbar betrieben werden. Dazu SOLLTEN die Server bzw. Werkzeuge inklusive der Netzanbindungen redundant ausgelegt sein. Auch die einzelnen Komponenten SOLLTEN hochverfügbar bereitgestellt werden.

#### **NET.1.2.A31 Grundsätzliche Nutzung von sicheren Protokollen (H)**

Für das Netzmanagement SOLLTEN ausschließlich sichere Protokolle benutzt werden. Es SOLLTEN alle Sicherheitsfunktionen dieser Protokolle verwendet werden.

#### **NET.1.2.A32 Physische Trennung des Managementnetzes (H) [Planende]**

Das Managementnetz SOLLTE physisch von den produktiven Netzen getrennt werden.

#### **NET.1.2.A33 Physische Trennung von Management-Segmenten (H) [Planende]**

Es SOLLTEN physisch getrennte Zonen mindestens für das Management von LAN-Komponenten, Sicherheitskomponenten und Komponenten zur Außenanbindung eingerichtet werden.

#### **NET.1.2.A34 ENTFALLEN (H)**

Diese Anforderung ist entfallen.

#### **NET.1.2.A35 Festlegungen zur Beweissicherung (H)**

Die erhobenen Protokollierungsdaten SOLLTEN für forensische Analysen gesetzeskonform und revisionssicher archiviert werden (siehe auch DER.2.2 *Vorsorge für die IT-Forensik*).

#### **NET.1.2.A36 Einbindung der Protokollierung des Netzmanagements in eine SIEM-Lösung (H)**

Die Protokollierung des Netzmanagements SOLLTE in eine Security-Information-and-Event-Management (SIEM)-Lösung eingebunden werden. Dazu SOLLTEN die Anforderungskataloge zur Auswahl von Netzmanagement-Lösungen hinsichtlich der erforderlichen Unterstützung von Schnittstellen und Übergabeformaten angepasst werden (siehe NET.1.2.A2 *Anforderungsspezifikation für das Netzmanagement*).

#### **NET.1.2.A37 Standortübergreifende Zeitsynchronisation (H)**

Die Zeitsynchronisation SOLLTE über alle Standorte der Institution sichergestellt werden. Dafür SOLLTE eine gemeinsame Referenzzeit benutzt werden.

#### **NET.1.2.A38 Festlegung von Notbetriebsformen für die Netzmanagement-Infrastruktur (H)**

Für eine schnelle Wiederherstellung der Sollzustände von Software bzw. Firmware sowie der Konfiguration der Komponenten in der Netzmanagement-Infrastruktur SOLLTEN hinreichend gute Ersatzlösungen festgelegt werden.

# **4. Weiterführende Informationen**

# **4.1. Wissenswertes**

Die International Organization for Standardization (ISO) formuliert in der Norm ISO/IEC 27033 "Information technology - Security techniques - Network security - Part 1: Overview and concepts bis Part 3: Reference networking scenarios - Threats, design techniques and control issues" Vorgaben für die Absicherung von Netzen.

Das BSI hat das weiterführende Dokument "Sichere Anbindung von lokalen Netzen an das Internet (ISi-LANA)" zum Themenfeld Netzmanagement veröffentlicht.
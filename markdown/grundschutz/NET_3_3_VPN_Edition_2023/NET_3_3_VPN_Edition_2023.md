![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_2.jpeg)

# **NET.3.3 VPN**

# **1. Beschreibung**

## **1.1. Einleitung**

Mithilfe von Virtuellen Privaten Netzen (VPNs) können schutzbedürftige Daten über nichtvertrauenswürdige Netze, wie das Internet, übertragen werden. Ein VPN ist ein virtuelles Netz, das innerhalb eines anderen Netzes betrieben wird, jedoch logisch von diesem Netz getrennt ist. Das VPN nutzt das Netz hierbei lediglich als Transportmedium, ist aber selber unabhängig von der Struktur und dem Aufbau des verwendeten Netzes. VPNs können mithilfe kryptografischer Verfahren die Integrität und Vertraulichkeit von Daten schützen. VPNs ermöglichen auch dann die sichere Authentisierung der Kommunikationspunkte, wenn mehrere Netze oder IT-Systeme über gemietete Leitungen oder öffentliche Netze miteinander verbunden sind.

## **1.2. Zielsetzung**

Der Baustein definiert Anforderungen, mit denen sich ein VPN zielgerichtet und sicher planen, umsetzen und betreiben lässt.

## **1.3. Abgrenzung und Modellierung**

Der vorliegende Baustein ist für jede Zugriffsmöglichkeit auf das Netz der Institution über einen VPN-Endpunkt anzuwenden.

Der Baustein geht nicht auf Grundlagen für sichere Netze und deren Aufbau ein (siehe dazu NET.1.1 *Netzarchitektur und -design*). Auch deckt dieser Baustein nicht alle mit dem Betrieb eines VPN zusammenhängenden Prozesse ab. VPNs sollten grundsätzlich im Rahmen der Bausteine ORP.4 *Identitäts- und Berechtigungsmanagement*, OPS.1.1.3 *Patch- und Änderungsmanagement*, OPS.1.2.5 *Fernwartung*, OPS.1.1.2 *Ordnungsgemäße IT-Administration* sowie CON.1 *Kryptokonzept* mit berücksichtigt werden.

Empfehlungen, wie die Betriebssysteme der VPN-Endpunkte konfiguriert werden können, sind ebenfalls nicht Bestandteil dieses Bausteins. Entsprechende Anforderungen sind im Baustein SYS.1.1 *Allgemeiner Server* beziehungsweise SYS.2.1 *Allgemeiner Client* sowie in den jeweiligen betriebssystemspezifischen Bausteinen des IT-Grundschutz-Kompendiums zu finden.

# **2. Gefährdungslage**

Da IT-Grundschutz-Bausteine nicht auf individuelle Informationsverbünde eingehen können, werden zur Darstellung der Gefährdungslage typische Szenarien zugrunde gelegt. Die folgenden spezifischen Bedrohungen und Schwachstellen sind für den Baustein NET.3.3 *VPN* von besonderer Bedeutung.

## **2.1. Fehlende oder unzureichende Planung des VPN-Einsatzes**

Bei einem nicht sorgfältig geplanten, aufgebauten oder konfigurierten VPN können Sicherheitslücken entstehen, die alle IT-Systeme betreffen könnten, die mit dem VPN verbunden sind. Angreifenden kann es so möglich sein, auf vertrauliche Informationen der Institution zuzugreifen.

So ist es durch eine unzureichende VPN-Planung beispielsweise möglich, dass die Benutzenden nicht ordnungsgemäß geschult wurden. Dadurch könnten sie das VPN in einer unsicheren Umgebung benutzen oder sich von unsicheren Clients aus einwählen. Dies ermöglicht es Angreifenden eventuell, auf das gesamte Institutionsnetz zuzugreifen.

Auch wenn die regelmäßige Kontrolle der Zugriffe auf das VPN unzureichend geplant wurde, könnten Angriffe nicht rechtzeitig erkannt werden. Somit kann nicht zeitnah reagiert werden und Angreifende unbemerkt Daten stehlen oder ganze Prozesse sabotieren.

## **2.2. Unsichere VPN-Dienstleistende**

Hat eine Institution seine VPN-Dienstleistenden nicht sorgfältig ausgewählt, könnte dadurch das gesamte Netz der Institution unsicher werden. So könnte beispielsweise ein von den Dienstleistenden unsicher angebotener VPN-Zugang für Angriffe genutzt werden, um gezielt Informationen zu stehlen.

## **2.3. Unsichere Konfiguration der VPN-Clients für den Fernzugriff**

Wird ein VPN-Client nicht sicher konfiguriert, könnten die Benutzenden dessen Sicherheitsmechanismen falsch oder gar nicht benutzen. Auch verändern sie eventuell die Konfiguration des VPN-Clients. Ebenso ist es durch eine unsichere Konfiguration möglich, dass von den Benutzenden installierte Software auch die Sicherheit des VPN-Clients gefährdet.

## **2.4. Unsichere Standard-Einstellungen auf VPN-Komponenten**

In der Standard-Einstellung sind VPN-Komponenten meist ohne oder nur mit unzureichenden Sicherheitsmechanismen vorkonfiguriert. Oft wird mehr auf Nutzungsfreundlichkeit und problemlose Integration in bestehende IT-Systeme als auf Sicherheit geachtet. Werden VPN-Komponenten nicht oder nur mangelhaft an die konkreten Sicherheitsbedürfnisse der Institution angepasst, können Schwachstellen und somit gefährliche Angriffspunkte entstehen. Werden beispielsweise werksseitig voreingestellte Passwörter nicht geändert, könnte das gesamte VPN und damit das interne Netz der Institution angegriffen werden.

## **3. Anforderungen**

Im Folgenden sind die spezifischen Anforderungen des Bausteins NET.3.3 *VPN* aufgeführt. Der oder die Informationssicherheitsbeauftragte (ISB) ist dafür zuständig, dass alle Anforderungen gemäß dem festgelegten Sicherheitskonzept erfüllt und überprüft werden. Bei strategischen Entscheidungen ist der oder die ISB stets einzubeziehen.

Im IT-Grundschutz-Kompendium sind darüber hinaus weitere Rollen definiert. Sie sollten besetzt werden, insofern dies sinnvoll und angemessen ist.

| Zuständigkeiten         | Rollen     |
|-------------------------|------------|
| Grundsätzlich zuständig | IT-Betrieb |
| Weitere Zuständigkeiten | Keine      |

Genau eine Rolle sollte Grundsätzlich zuständig sein. Darüber hinaus kann es noch Weitere Zuständigkeiten geben. Falls eine dieser weiteren Rollen für die Erfüllung einer Anforderung vorrangig zuständig ist, dann wird diese Rolle hinter der Überschrift der Anforderung in eckigen Klammern aufgeführt. Die Verwendung des Singulars oder Plurals sagt nichts darüber aus, wie viele Personen diese Rollen ausfüllen sollen.

## **3.1. Basis-Anforderungen**

Die folgenden Anforderungen MÜSSEN für diesen Baustein vorrangig erfüllt werden.

#### **NET.3.3.A1 Planung des VPN-Einsatzes (B)**

Die Einführung eines VPN MUSS sorgfältig geplant werden. Dabei MÜSSEN die Verantwortlichkeiten für den VPN-Betrieb festgelegt werden. Es MÜSSEN für das VPN zudem Benutzendengruppen und deren Berechtigungen geplant werden. Ebenso MUSS definiert werden, wie erteilte, geänderte oder entzogene Zugriffsberechtigungen zu dokumentieren sind.

#### **NET.3.3.A2 Auswahl von VPN-Dienstleistenden (B)**

Falls VPN-Dienstleistende eingesetzt werden, MÜSSEN mit diesen Service Level Agreements (SLAs) ausgehandelt und schriftlich dokumentiert werden. Es MUSS regelmäßig kontrolliert werden, ob die VPN-Dienstleistenden die vereinbarten SLAs einhalten.

#### **NET.3.3.A3 Sichere Installation von VPN-Endgeräten (B)**

Wird eine Appliance eingesetzt, die eine Wartung benötigt, MUSS es dafür einen gültigen Wartungsvertrag geben. Es MUSS sichergestellt werden, dass nur qualifiziertes Personal VPN-Komponenten installiert. Die Installation der VPN-Komponenten sowie eventuelle Abweichungen von den Planungsvorgaben SOLLTEN dokumentiert werden. Die Funktionalität und die gewählten Sicherheitsmechanismen des VPN MÜSSEN vor Inbetriebnahme geprüft werden.

#### **NET.3.3.A4 Sichere Konfiguration eines VPN (B)**

Für alle VPN-Komponenten MUSS eine sichere Konfiguration festgelegt werden. Diese SOLLTE geeignet dokumentiert werden. Auch MUSS die für die Administration zuständige Person regelmäßig kontrollieren, ob die Konfiguration noch sicher ist und sie eventuell für alle IT-Systeme anpassen.

#### **NET.3.3.A5 Sperrung nicht mehr benötigter VPN-Zugänge (B)**

Es MUSS regelmäßig geprüft werden, ob ausschließlich berechtigte IT-Systeme und Benutzende auf das VPN zugreifen können. Nicht mehr benötigte VPN-Zugänge MÜSSEN zeitnah deaktiviert werden. Der VPN-Zugriff MUSS auf die benötigten Benutzungszeiten beschränkt werden.

#### **3.2. Standard-Anforderungen**

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik für diesen Baustein. Sie SOLLTEN grundsätzlich erfüllt werden.

#### **NET.3.3.A6 Durchführung einer VPN-Anforderungsanalyse (S)**

Eine Anforderungsanalyse SOLLTE durchgeführt werden, um für das jeweilige VPN die Einsatzszenarien zu bestimmen und daraus Anforderungen an die benötigten Hard- und Software-Komponenten ableiten zu können. In der Anforderungsanalyse SOLLTEN folgende Punkte betrachtet werden:

• Geschäftsprozesse beziehungsweise Fachaufgaben,

- Zugriffswege,
- Identifikations- und Authentisierungsverfahren,
- Benutzende und ihre Berechtigungen,
- Zuständigkeiten sowie
- Meldewege.

#### **NET.3.3.A7 Planung der technischen VPN-Realisierung (S)**

Neben der allgemeinen Planung (siehe NET.3.3.A1 *Planung des VPN-Einsatzes*) SOLLTEN die technischen Aspekte eines VPN sorgfältig geplant werden. So SOLLTEN für das VPN die Verschlüsselungsverfahren, VPN-Endpunkte, erlaubten Zugangsprotokolle, Dienste und Ressourcen festgelegt werden. Zudem SOLLTEN die Teilnetze definiert werden, die über das VPN erreichbar sind. (siehe NET.1.1 *Netzarchitektur und -design).*

#### **NET.3.3.A8 Erstellung einer Sicherheitsrichtlinie zur VPN-Nutzung (S)**

Eine Sicherheitsrichtlinie zur VPN-Nutzung SOLLTE erstellt werden. Diese SOLLTE allen Mitarbeitenden bekannt gegeben werden. Die in der Sicherheitsrichtlinie beschriebenen Sicherheitsmaßnahmen SOLLTEN im Rahmen von Schulungen erläutert werden. Wird für Mitarbeitende ein VPN-Zugang eingerichtet, SOLLTE diesen ein Merkblatt mit den wichtigsten VPN-Sicherheitsmechanismen ausgehändigt werden. Alle VPN-Benutzende SOLLTEN verpflichtet werden, die Sicherheitsrichtlinien einzuhalten.

#### **NET.3.3.A9 Geeignete Auswahl von VPN-Produkten (S)**

Bei der Auswahl von VPN-Produkten SOLLTEN die Anforderungen der Institutionen an die Vernetzung unterschiedlicher Standorte und die Anbindung von mobilen Mitarbeitenden oder Telearbeitsplätzen berücksichtigt werden.

#### **NET.3.3.A10 Sicherer Betrieb eines VPN (S)**

Für VPNs SOLLTE ein Betriebskonzept erstellt werden. Darin SOLLTEN die Aspekte Qualitätsmanagement, Überwachung, Wartung, Schulung und Autorisierung beachtet werden.

#### **NET.3.3.A11 Sichere Anbindung eines externen Netzes (S)**

Es SOLLTE sichergestellt werden, dass VPN-Verbindungen NUR zwischen den dafür vorgesehenen IT-Systemen und Diensten aufgebaut werden. Die dabei eingesetzten Tunnel-Protokolle SOLLTEN für den Einsatz geeignet sein.

#### **NET.3.3.A12 Konten- und Zugriffsverwaltung bei Fernzugriff-VPNs (S)**

Für Fernzugriff-VPNs SOLLTE eine zentrale und konsistente Konten- und Zugriffsverwaltung gewährleistet werden.

#### **NET.3.3.A13 Integration von VPN-Komponenten in eine Firewall (S)**

Die VPN-Komponenten SOLLTEN in die Firewall integriert werden. Dies SOLLTE dokumentiert werden.

## **3.3. Anforderungen bei erhöhtem Schutzbedarf**

Für diesen Baustein sind keine Anforderungen für einen erhöhten Schutzbedarf definiert.

# **4. Weiterführende Informationen**

#### **4.1. Wissenswertes**

Die International Organization for Standardization (ISO) macht in der Norm ISO/IEC 27033-5:2013 "Information technology - Security techniques - Network security - Part 5: Securing communications across networks using Virtual Private Networks (VPNs)" Vorgaben für den Einsatz von VPNs.

Das National Institute of Standards and Technology (NIST) macht in seiner Special Publication 800-77 "Guide to IPsec VPNs" generelle Vorgaben zum Einsatz von VPNs.
![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_2.jpeg)

# **SYS.3.1 Laptops**

# **1. Beschreibung**

## **1.1. Einleitung**

Ein Laptop (auch Notebook genannt) ist ein PC, der mobil genutzt werden kann. Er hat eine kompakte Bauform, integriert Peripheriegeräte wie Tastatur und Bildschirm, ist über Akkus zeitweise unabhängig von einer externen Stromversorgung und besteht oft aus speziell für den mobilen Einsatz konzipierten Hardware-Komponenten. Laptops sind in den meisten Institutionen verbreitet und ersetzen häufig den klassischen Desktop-PC.

Laptops werden in der Regel mit verbreiteten Desktop-Betriebssystemen wie Microsoft Windows, Apple macOS oder Linux betrieben. Die Grenzen zu Tablets und ähnlichen Geräten sind heutzutage fließend. So gibt es Tablets mit Desktop-Betriebssystemen wie Windows 10, aber auch Tastaturzubehör für Mobilgeräte wie iPads mit iPadOS, die so als Laptops genutzt werden können.

Da Laptops häufig auch mobil genutzt werden, sind sie oft nicht permanent am LAN der Institution angeschlossen. Stattdessen können sie sich in der Regel per Virtual Private Network (VPN) z. B. über das Internet mit dem Netz der Institution verbinden. Auch die Infrastruktur einer klassischen Büroumgebung, die kontrollierbare Umwelteinflüsse, eine stabile Stromversorgung oder zutrittsgeschützte Bereiche bietet, kann beim mobilen Einsatz von Laptops nicht vorausgesetzt werden.

## **1.2. Zielsetzung**

Ziel des Bausteins ist es, Institutionen einen sicheren Einsatz von Laptops zu ermöglichen sowie für die spezifischen Gefährdungen dieser Geräteklasse zu sensibilisieren.

## **1.3. Abgrenzung und Modellierung**

Der Baustein SYS.3.1 *Laptops* ist auf alle Laptops anzuwenden, die mobil oder stationär genutzt werden.

Wie bei allen IT-Systemen müssen auch bei Laptops die Betriebssystem- und Software-Komponenten sorgfältig ausgewählt und installiert werden. Die hier zu erfüllenden Anforderungen sind abhängig vom Betriebssystem des Laptops und werden daher in den Client-spezifischen Bausteinen beschrieben, beispielsweise SYS.2.2.3 *Clients unter Windows,* SYS 2.3 *Clients unter Linux und Unix* oder SYS.2.4 *Clients unter macOS*. Ebenso sind Anforderungen, die für alle Arten von Clients gelten, nicht Bestandteil dieses Bausteins. Diese sind im Baustein SYS.2.1 *Allgemeiner Client* zu finden.

Auch wird in diesem Baustein nicht behandelt, wie die jeweilige Datenübertragung einzurichten ist, wie z. B. die WLAN-Konfiguration (siehe NET.2.2 *WLAN-Nutzung*) oder eine VPN-Anbindung (siehe NET.3.3 *VPN*).

Da Laptops oft längere Zeit außerhalb einer Institution eingesetzt werden, müssen sie besonders bei der Datensicherung berücksichtigt werden. Weiterführende Anforderungen dazu finden sich in Baustein CON.3 *Datensicherungskonzept*.

# **2. Gefährdungslage**

Da IT-Grundschutz-Bausteine nicht auf individuelle Informationsverbünde eingehen können, werden zur Darstellung der Gefährdungslage typische Szenarien zugrunde gelegt. Die folgenden spezifischen Bedrohungen und Schwachstellen sind für den Baustein *SYS.3.1 Laptops* von besonderer Bedeutung.

## **2.1. Beeinträchtigung durch wechselnde Einsatzumgebung**

Laptops werden in sehr unterschiedlichen Umgebungen eingesetzt und sind dadurch vielen Gefährdungen ausgesetzt. Dazu gehören beispielsweise schädigende Umwelteinflüsse wie zu hohe oder zu niedrige Temperaturen, ebenso Staub oder Feuchtigkeit. Bei Laptops besteht auch stets die Gefahr von Transportschäden. Außerdem kommunizieren Laptops vor allem unterwegs oft mit unbekannten IT-Systemen oder Netzen, was immer ein Gefährdungspotenzial für das eigene Gerät mit sich bringt. So können dabei beispielsweise Schadprogramme übertragen oder schützenswerte Informationen kopiert werden.

## **2.2. Diebstahl und Verlust von Laptops**

Mitarbeitende nutzen ihre Laptops oftmals auch außerhalb der Institution. Die Geräte werden etwa in privaten Kraftfahrzeugen oder in öffentlichen Verkehrsmitteln transportiert, in fremden Büroräumen in Pausen zurückgelassen oder in Hotelzimmern unbewacht aufgestellt. Somit sind Laptops einem höheren Diebstahlrisiko ausgesetzt und können zudem leicht vergessen oder verloren werden. Kommt ein Laptop abhanden, entstehen Kosten und Aufwand für die Wiederbeschaffung. Nicht gesicherte Daten sind zudem verloren. Ebenso könnten Unbefugte auf schützenswerte Daten zugreifen, wodurch es zu weiteren Schäden kommen kann. Diese wiegen in vielen Fällen deutlich schwerer als der rein materielle Verlust des Laptops.

## **2.3. Ungeordnete Weitergabe von Laptops**

Wenn Mitarbeitende nur in Ausnahmefällen mobile IT-Systeme benötigen, wie beispielsweise für selten durchgeführte Dienstreisen, ist es oft zweckmäßiger, nur wenige Laptops zentral vorzuhalten. Diese können dann untereinander weitergereicht werden. Wird jedoch der Laptop einfach an den nächsten Mitarbeitenden übergeben, besteht die Gefahr, dass noch auf dem Gerät befindliche schutzbedürftige Daten weitergegeben werden. Außerdem ist es möglich, dass der Laptop mit Schadsoftware infiziert ist. Ohne eine geeignete Regelung kann schwer nachvollziehbar sein, wer den Laptop wann benutzt hat oder wer ihn zurzeit benutzt.

# **3. Anforderungen**

Im Folgenden sind die spezifischen Anforderungen des Bausteins SYS.3.1 *Laptops* aufgeführt. Der oder die Informationssicherheitsbeauftragte (ISB) ist dafür zuständig, dass alle Anforderungen gemäß dem festgelegten Sicherheitskonzept erfüllt und überprüft werden. Bei strategischen Entscheidungen ist der oder die ISB stets einzubeziehen.

Im IT-Grundschutz-Kompendium sind darüber hinaus weitere Rollen definiert. Sie sollten besetzt werden, insofern dies sinnvoll und angemessen ist.

| Zuständigkeiten         | Rollen                         |
|-------------------------|--------------------------------|
| Grundsätzlich zuständig | IT-Betrieb                     |
| Weitere Zuständigkeiten | Benutzende, Beschaffungsstelle |

Genau eine Rolle sollte *Grundsätzlich zuständig* sein. Darüber hinaus kann es noch *Weitere Zuständigkeiten* geben. Falls eine dieser weiteren Rollen für die Erfüllung einer Anforderung vorrangig zuständig ist, dann wird diese Rolle hinter der Überschrift der Anforderung in eckigen Klammern aufgeführt. Die Verwendung des Singulars oder Plurals sagt nichts darüber aus, wie viele Personen diese Rollen ausfüllen sollen.

## **3.1. Basis-Anforderungen**

Die folgenden Anforderungen MÜSSEN für diesen Baustein vorrangig erfüllt werden.

#### **SYS.3.1.A1 Regelungen zur mobilen Nutzung von Laptops (B)**

Es MUSS klar geregelt werden, was Mitarbeitende bei der mobilen Nutzung von Laptops berücksichtigen müssen. Es MUSS insbesondere festgelegt werden, welche Laptops mobil genutzt werden dürfen, wer sie mitnehmen darf und welche grundlegenden Sicherheitsmaßnahmen dabei zu beachten sind. Die Benutzenden MÜSSEN auf die Regelungen hingewiesen werden.

#### **SYS.3.1.A2 ENTFALLEN (B)**

Diese Anforderung ist entfallen.

#### **SYS.3.1.A3 Einsatz von Personal Firewalls (B)**

Auf Laptops MUSS eine Personal Firewall aktiv sein, wenn sie außerhalb von Netzen der Institution eingesetzt werden. Die Filterregeln der Firewall MÜSSEN so restriktiv wie möglich sein. Die Filterregeln MÜSSEN regelmäßig getestet werden. Die Personal Firewall MUSS so konfiguriert werden, dass die Benutzenden nicht durch Warnmeldungen belästigt werden, die sie nicht interpretieren können.

#### **SYS.3.1.A4 ENTFALLEN (B)**

Diese Anforderung ist entfallen.

#### **SYS.3.1.A5 ENTFALLEN (B)**

Diese Anforderung ist entfallen.

#### **SYS.3.1.A9 Sicherer Fernzugriff mit Laptops (B)**

Aus öffentlich zugänglichen Netzen DARF NUR über einen sicheren Kommunikationskanal auf das interne Netz der Institution zugegriffen werden.

#### **3.2. Standard-Anforderungen**

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik für diesen Baustein. Sie SOLLTEN grundsätzlich erfüllt werden.

#### **SYS.3.1.A6 Sicherheitsrichtlinien für Laptops (S)**

Für Laptops SOLLTE eine Sicherheitsrichtlinie erstellt werden, die regelt, wie die Geräte benutzt werden dürfen. Die Benutzenden SOLLTEN hinsichtlich des Schutzbedarfs von Laptops und der dort gespeicherten Daten sensibilisiert werden. Auch SOLLTEN sie auf die spezifischen Gefährdungen bzw. die entsprechenden Anforderungen für die Nutzung aufmerksam gemacht werden. Sie SOLLTEN außerdem darüber informiert werden, welche Art von Informationen sie auf Laptops verarbeiten dürfen.

#### **SYS.3.1.A7 Geregelte Übergabe und Rücknahme eines Laptops (S) [Benutzende]**

Wenn Laptops von verschiedenen Personen abwechselnd genutzt werden, SOLLTE geregelt werden, wie sie sicher übergeben werden können. Auch SOLLTE geregelt werden, wie sie wieder sicher zurückzunehmen sind. Vor der Weitergabe eines Laptops SOLLTEN eventuell vorhandene schützenswerte Daten sicher gelöscht werden. Falls der Laptop vor der Weitergabe nicht neu aufgesetzt wird, SOLLTE sichergestellt sein, dass sich auf dem IT-System und allen damit verbundenen Datenträgern keine Schadsoftware befindet. Gemeinsam mit einem Laptop SOLLTE ein Merkblatt für den sicheren Umgang mit dem Gerät ausgehändigt werden.

#### **SYS.3.1.A8 Sicherer Anschluss von Laptops an Datennetze (S) [Benutzende]**

Es SOLLTE geregelt werden, wie Laptops sicher an eigene oder fremde Datennetze und an das Internet angeschlossen werden. Nur zugelassene Laptops SOLLTEN sich am internen Netz der Institution anmelden können.

#### **SYS.3.1.A10 Abgleich der Datenbestände von Laptops (S) [Benutzende]**

Es SOLLTE geregelt werden, wie Daten von Laptops in den Informationsverbund der Institution übernommen werden. Wenn ein Synchronisationstool benutzt wird, SOLLTE sichergestellt sein, dass Synchronisationskonflikte aufgelöst werden können. Der Synchronisationsvorgang SOLLTE protokolliert werden. Außerdem SOLLTEN die Benutzenden angewiesen werden, die Synchronisationsprotokolle zu prüfen.

#### **SYS.3.1.A11 Sicherstellung der Energieversorgung von Laptops (S) [Benutzende]**

Alle Benutzenden SOLLTEN darüber informiert werden, wie sie die Energieversorgung von Laptops im mobilen Einsatz optimal sicherstellen können. Vorhandene Ersatzakkus SOLLTEN in geeigneten Hüllen gelagert und transportiert werden.

#### **SYS.3.1.A12 Verlustmeldung für Laptops (S) [Benutzende]**

Benutzende SOLLTEN umgehend melden, wenn ein Laptop verloren gegangen ist oder gestohlen wurde. Dafür SOLLTE es in der Institution klare Meldewege geben. Wenn verlorene Laptops wieder auftauchen, SOLLTE untersucht werden, ob sie eventuell manipuliert wurden. Die darauf eingesetzte Software inklusive des Betriebssystems SOLLTE komplett neu installiert werden.

#### **SYS.3.1.A13 Verschlüsselung von Laptops (S)**

In Laptops verbaute Datenträger wie Festplatten oder SSDs SOLLTEN verschlüsselt werden.

#### **SYS.3.1.A14 Geeignete Aufbewahrung von Laptops (S) [Benutzende]**

Alle Benutzenden SOLLTEN darauf hingewiesen werden, wie Laptops außerhalb der Institution sicher aufzubewahren sind. Abhängig vom Schutzbedarf der darauf gespeicherten Daten SOLLTEN Laptops auch in den Räumen der Institution außerhalb der Nutzungszeiten gegen Diebstahl gesichert bzw. verschlossen aufbewahrt werden.

#### **SYS.3.1.A15 Geeignete Auswahl von Laptops (S) [Beschaffungsstelle]**

Bevor Laptops beschafft werden, SOLLTE eine Anforderungsanalyse durchgeführt werden. Anhand der Ergebnisse SOLLTEN alle infrage kommenden Geräte bewertet werden. Die Beschaffungsentscheidung SOLLTE mit dem IT-Betrieb abgestimmt sein.

## **3.3. Anforderungen bei erhöhtem Schutzbedarf**

Im Folgenden sind für diesen Baustein exemplarische Vorschläge für Anforderungen aufgeführt, die über dasjenige Schutzniveau hinausgehen, das dem Stand der Technik entspricht. Die Vorschläge

SOLLTEN bei erhöhtem Schutzbedarf in Betracht gezogen werden. Die konkrete Festlegung erfolgt im Rahmen einer individuellen Risikoanalyse.

#### **SYS.3.1.A16 Zentrale Administration und Verwaltung von Laptops (H)**

Es SOLLTE eine geeignete Regelung definiert werden, wie Laptops zentral zu administrieren und verwalten sind. Ein Tool zum zentralen Laptop-Management SOLLTE möglichst alle eingesetzten Betriebssysteme unterstützen.

#### **SYS.3.1.A17 Sammelaufbewahrung von Laptops (H)**

Nicht benutzte Laptops SOLLTEN in einem geeignet abgesicherten Raum vorgehalten werden. Der dafür genutzte Raum SOLLTE den Anforderungen aus dem Baustein INF.5 *Raum sowie Schrank für technische Infrastruktur* entsprechen.

#### **SYS.3.1.A18 Einsatz von Diebstahl-Sicherungen (H)**

Es SOLLTE geregelt werden, welche Diebstahlsicherungen für Laptops eingesetzt werden sollen. Bei mechanischen Sicherungen SOLLTE besonders auf ein gutes Schloss geachtet werden.

## **4. Weiterführende Informationen**

#### **4.1. Wissenswertes**

Für den Baustein SYS.3.1 *Laptops* sind keine weiterführenden Informationen vorhanden.
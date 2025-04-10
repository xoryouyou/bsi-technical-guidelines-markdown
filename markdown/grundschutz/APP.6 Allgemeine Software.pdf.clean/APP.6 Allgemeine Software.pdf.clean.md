![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_2.jpeg)

# **APP.6 Allgemeine Software**

# **1. Beschreibung**

## **1.1. Einleitung**

Dieser Baustein fasst jegliche Software unter dem Begriff Allgemeine Software zusammen, unabhängig davon, ob es sich um eine Textverarbeitung, ein Betriebssystem, eine mobile Kommunikations-App, eine individuell entwickelte Software oder ein verteiltes Content-Management-System handelt.

Dabei durchläuft in der Regel jegliche Software einen Lebenszyklus, der die Planung, Anforderungserhebung, Beschaffung, Software-Tests inklusive Freigabe, Installation in Produktivumgebung, Schulung, Betrieb, Updates und Änderungsmanagement sowie Außerbetriebnahme mitsamt Deinstallation umfasst. Dieser Lebenszyklus kann je nach Anwendungskontext variieren, sodass bei einzelnen Anwendungen noch weitere individuelle Zwischenschritte dazu kommen können und auch der Umfang der einzelnen Schritte schwankt.

Allerdings treten bei den aufgeführten Zwischenschritten immer wiederkehrende Aspekte der Informationssicherheit auf, die auf jegliche Art von Software angewendet werden können.

## **1.2. Zielsetzung**

Der Baustein zeigt auf, welche Sicherheitsanforderungen zu erfüllen sind, damit allgemeine Software über den gesamten Lebenszyklus hinweg sicher eingesetzt werden kann. Übergeordnetes Ziel ist dabei, die Software und die hiermit verarbeiteten Informationen zu schützen.

## **1.3. Abgrenzung und Modellierung**

Der Baustein APP.6 *Allgemeine Software* ist grundsätzlich für jede Software, die im Informationsverbund eingesetzt wird, anzuwenden. Ausgenommen hiervon sind Betriebssysteme, die auf geschlossenen Systemen wie IoT-Geräten, Routern, Druckern oder eingebetteten Systemen ausgeführt werden. Häufig wird Software gebündelt ausgeliefert (z. B. Office Suites oder Betriebssysteme mit umfangreich integrierten Boardwerkzeugen) oder um Plug-ins, Add-ons oder vergleichbare erweitert. In solchen Fällen kann der Baustein auf das gesamte Softwarebündel einmal angewendet werden.

Dieser Baustein befasst sich nur mit standardisierten und generischen Verfahrensweisen im Lebenszyklus von Software. Es werden keine konkreten Empfehlungen beschrieben, wie Software im Einzelnen konfiguriert und wie sie durch individuelle Schutzmechanismen auf den eingesetzten IT-

Systemen abgesichert werden soll. Hierzu sind die spezifischen Bausteine der APP-Schicht anzuwenden.

Die Zwischenschritte Freigabe (inklusive Software-Tests) sowie Patch- und Änderungsmanagement werden nicht in diesem Baustein behandelt, sondern in den Bausteinen OPS.1.1.6 *Software-Tests und - Freigaben* sowie OPS.1.1.3 *Patch- und Änderungsmanagement.*

Können Anforderungen an Software nicht von einem fertigen Softwareprodukt erfüllt werden, indem z. B. die Konfiguration angepasst wird, sondern es wird ein individuell entwickeltes Produkt benötigt, dann muss der Baustein APP.7 *Entwicklung von Individualsoftwar*e ergänzend modelliert werden.

Software und die damit verbundenen Daten müssen häufig auch in Notfällen verfügbar sein. Erste Überlegungen hierzu zeigt der Baustein DER.4 *Notfallmanagement* auf.

# **2. Gefährdungslage**

Da IT-Grundschutz-Bausteine nicht auf individuelle Informationsverbünde eingehen können, werden zur Darstellung der Gefährdungslage typische Szenarien zugrunde gelegt. Die folgenden spezifischen Bedrohungen und Schwachstellen sind für den Baustein APP.6 *Allgemeine Software* von besonderer Bedeutung.

## **2.1. Ungeeignete Auswahl von Software**

Für viele Anwendungszwecke und Einsatzmöglichkeiten werden die unterschiedlichsten Software-Lösungen auf dem Markt angeboten. Wird eine unpassende Software, die nicht den Anforderungen der Institution entspricht, ausgewählt, dann kann der Betrieb erheblich gestört werden. Dateiformate könnten zum Beispiel nicht mit bereits eingesetzten Programmen kompatibel sein oder neue Produkte einen zu geringen Funktionsumfang haben. Das kann zu Leistungsverlusten, Störungen oder Fehlern innerhalb der Geschäftsprozesse führen.

Insbesondere wenn die Software nicht die Sicherheitsanforderungen der Institution erfüllt, könnten die mit der Software verarbeiteten Daten offengelegt oder manipuliert werden, z. B. wenn Login-Funktionen von Anwendungen nicht für die geplante Einsatzumgebung in einem offenen Datennetz konzeptioniert worden sind.

## **2.2. Offenlegung schützenswerter Informationen durch fehlerhafte Konfiguration**

Ist eine Software fehlerhaft konfiguriert, können unbeabsichtigt schützenswerte Informationen offengelegt werden, z. B. wenn nicht benötigte Funktionen noch aktiviert sind, wie Cloud-Backup-Funktionen, die Daten ungewollt in eine Cloud synchronisieren. Hierdurch könnten sensible Daten von unbefugten Dritten eingesehen und offengelegt werden.

Das kann zu finanziellen Einbußen führen oder die Reputation einer Institution schädigen. Zusätzlich könnte die Institution auch gegen geltendes Recht verstoßen, z. B. wenn personenbezogene Daten offengelegt werden.

## **2.3. Bezug von Software aus unzuverlässiger Quelle**

Wird Software aus unzuverlässigen Quellen bezogen, ist nicht sichergestellt, dass eine unveränderte Originalversion der Software eingesetzt wird. Anstelle dessen könnte eine defekte oder kompromittierte Version der Software bezogen worden sein. Dies gilt auch für Erweiterungen, wie Plug-ins oder Add-ons. Wird kompromittierte Software installiert, kann Schadcode in der Institution verteilt werden. Außerdem ist es möglich, dass die Software nicht wie vorgesehen funktioniert. Darüber hinaus kann die Integrität und Verfügbarkeit von IT-Systemen beeinträchtigt werden.

## **2.4. Sicherheitslücken durch mangelhafte Wartung**

Sicherheitslücken und Software-Schwachstellen können prinzipiell über den gesamten Nutzungszeitraum von Software auftreten. Das kann dazu führen, dass die Informationssicherheit der mit der Software verarbeiten Daten gefährdet ist, indem z. B. Login-Funktionen umgangen oder Verschlüsselungen gebrochen werden können.

Sicherheitslücken und Schwachstellen können insbesondere dann nicht zeitnah behoben werden, wenn kein geeigneter Wartungsvertrag mit dem herstellenden oder anbietenden Unternehmen geschlossen wurde oder die Software schlicht über den Wartungszeitraum hinaus verwendet wird. Auch können Verstöße gegen die Lizenzbestimmungen dazu führen, dass z. B. (Auto-)Update-Mechanismen deaktiviert werden und somit die Software nicht mehr gewartet wird.

## **2.5. Datenverlust durch fehlerhafte Nutzung von Software**

Durch falsch benutzte Software können Mitarbeitende Daten versehentlich löschen oder so verändern, dass diese unbrauchbar werden. Dadurch können ganze Geschäftsprozesse blockiert werden. Auch wenn Funktionen zur Verschlüsselung fehlerhaft benutzt werden, könnten die Daten zwar noch vorhanden sein, aber nicht mehr entschlüsselt werden. In diesem Fall können die Daten nicht mehr oder nur noch mit erhöhtem Aufwand wiederhergestellt werden.

## **2.6. Mangelhafte Ressourcen für die Ausführung von Software**

Falls IT-Systeme über ungenügend Ressourcen verfügen, um die Software auszuführen, kann das die Bearbeitungs- und Reaktionszeit für die Benutzende erheblich erhöhen. Im schlimmsten Fall kann die Software auf solch einem System nicht ausgeführt werden. Das kann Geschäftsprozesse erheblich unterbrechen.

## **2.7. Nichtbeachtung von Anforderungen der Benutzenden**

Unabhängig davon, ob eine Software die funktionalen Anforderungen erfüllt, kann sie von den Benutzenden nicht akzeptiert werden, wenn sie z. B. umständlich und kompliziert zu bedienen ist. Dies kann wiederum dazu führen, dass Benutzende auf alternative Formen der Bearbeitung zurückgreifen und dafür anderweitige IT-Systeme oder Software zweckentfremden. So könnten z. B. private IT-Systeme ohne Abstimmung mit dem IT-Betrieb eingesetzt werden. Diese alternativen Formen der Bearbeitung entstehen dabei selten unter Gesichtspunkten der Informationssicherheit und stellen somit ein erhöhtes Risiko dar.

# **3. Anforderungen**

Im Folgenden sind die spezifischen Anforderungen des Bausteins APP.6 *Allgemeine Software*  aufgeführt. Der oder die Informationssicherheitsbeauftragte (ISB) ist dafür zuständig, dass alle Anforderungen gemäß dem festgelegten Sicherheitskonzept erfüllt und überprüft werden. Bei strategischen Entscheidungen ist der oder die ISB stets einzubeziehen.

Im IT-Grundschutz-Kompendium sind darüber hinaus weitere Rollen definiert. Sie sollten besetzt werden, insofern dies sinnvoll und angemessen ist.

| Zuständigkeiten         | Rollen                                  |
|-------------------------|-----------------------------------------|
| Grundsätzlich zuständig | IT-Betrieb                              |
| Weitere Zuständigkeiten | Fachverantwortliche, Beschaffungsstelle |

Genau eine Rolle sollte *Grundsätzlich zuständig* sein. Darüber hinaus kann es noch *Weitere Zuständigkeiten* geben. Falls eine dieser weiteren Rollen für die Erfüllung einer Anforderung vorrangig zuständig ist, dann wird diese Rolle hinter der Überschrift der Anforderung in eckigen Klammern

aufgeführt. Die Verwendung des Singulars oder Plurals sagt nichts darüber aus, wie viele Personen diese Rollen ausfüllen sollen.

## **3.1. Basis-Anforderungen**

Die folgenden Anforderungen MÜSSEN für diesen Baustein vorrangig erfüllt werden.

#### **APP.6.A1 Planung des Software-Einsatzes (B) [Fachverantwortliche]**

Bevor eine Institution eine (neue) Software einführt, MUSS sie entscheiden,

- wofür die Software genutzt und welche Informationen damit verarbeitet werden sollen,
- wie die Benutzenden bei der Anforderungserhebung beteiligt und bei der Einführung unterstützt werden sollen,
- wie die Software an weitere Anwendungen und IT-Systeme über welche Schnittstellen angebunden wird,
- auf welchen IT-Systemen die Software ausgeführt werden soll und welche Ressourcen zur Ausführung der Software erforderlich sind, sowie
- ob sich die Institution in Abhängigkeit zu einem Hersteller oder einer Herstellerin begibt, wenn sie diese Software einsetzt.

Hierbei MÜSSEN bereits Sicherheitsaspekte berücksichtigt werden. Zusätzlich MUSS die Institution die Zuständigkeiten für fachliche Betreuung, Freigabe und betriebliche Administration schon im Vorfeld klären und festlegen. Die Zuständigkeiten MÜSSEN dokumentiert und bei Bedarf aktualisiert werden.

#### **APP.6.A2 Erstellung eines Anforderungskatalogs für Software (B) [Fachverantwortliche]**

Auf Basis der Ergebnisse der Planung MÜSSEN die Anforderungen an die Software in einem Anforderungskatalog erhoben werden. Der Anforderungskatalog MUSS dabei die grundlegenden funktionalen Anforderungen umfassen. Darüber hinaus MÜSSEN die nichtfunktionalen Anforderungen und hier insbesondere die Sicherheitsanforderungen in den Anforderungskatalog integriert werden.

Hierbei MÜSSEN sowohl die Anforderungen von den Fachverantwortlichen als auch vom IT-Betrieb berücksichtigt werden. Insbesondere MÜSSEN auch die rechtlichen Anforderungen, die sich aus dem Kontext der zu verarbeitenden Daten ergeben, berücksichtigt werden.

Der fertige Anforderungskatalog SOLLTE mit allen betroffenen Fachabteilungen abgestimmt werden.

#### **APP.6.A3 Sichere Beschaffung von Software (B) [Beschaffungsstelle]**

Wenn Software beschafft wird, MUSS auf Basis des Anforderungskatalogs eine geeignete Software ausgewählt werden. Die ausgewählte Software MUSS aus vertrauenswürdigen Quellen beschafft werden. Die vertrauenswürdige Quelle SOLLTE eine Möglichkeit bereitstellen, die Software auf Integrität zu überprüfen.

Darüber hinaus SOLLTE die Software mit einem geeigneten Wartungsvertrag oder einer vergleichbaren Zusage des herstellenden oder anbietenden Unternehmens beschafft werden. Diese Verträge oder Zusagen SOLLTEN insbesondere garantieren, dass auftretende Sicherheitslücken und Schwachstellen der Software während des gesamten Nutzungszeitraums zeitnah behoben werden.

#### **APP.6.A4 Regelung für die Installation und Konfiguration von Software (B) [Fachverantwortliche]**

Die Installation und Konfiguration der Software MUSS durch den IT-Betrieb so geregelt werden, dass

- die Software nur mit dem geringsten notwendigen Funktionsumfang installiert und ausgeführt wird,
- die Software mit den geringsten möglichen Berechtigungen ausgeführt wird,
- die datensparsamsten Einstellungen (in Bezug auf die Verarbeitung von personenbezogenen Daten) konfiguriert werden sowie
- alle relevanten Sicherheitsupdates und -patches installiert sind, bevor die Software produktiv eingesetzt wird.

Hierbei MÜSSEN auch abhängige Komponenten (unter anderem Laufzeitumgebungen, Bibliotheken, Schnittstellen sowie weitere Programme) mitbetrachtet werden. Der IT-Betrieb MUSS in Abstimmung mit den Fachverantwortlichen festlegen, wer die Software wie installieren darf. Idealerweise SOLLTE Software immer zentral durch den IT-Betrieb installiert werden. Ist es erforderlich, dass die Software (teilweise) manuell installiert wird, dann MUSS der IT-Betrieb eine Installationsanweisung erstellen, in der klar geregelt wird, welche Zwischenschritte zur Installation durchzuführen und welche Konfigurationen vorzunehmen sind.

Darüber hinaus MUSS der IT-Betrieb regeln, wie die Integrität der Installationsdateien überprüft wird. Falls zu einem Installationspaket digitale Signaturen oder Prüfsummen verfügbar sind, MÜSSEN mit diesen die Integrität überprüft werden.

Sofern erforderlich, SOLLTE der IT-Betrieb eine sichere Standardkonfiguration der Software festlegen, mit der die Software konfiguriert wird. Die Standardkonfiguration SOLLTE dokumentiert werden.

#### **APP.6.A5 Sichere Installation von Software (B)**

Software MUSS entsprechend der Regelung für die Installation auf den IT-Systemen installiert werden. Dabei MÜSSEN ausschließlich unveränderte Versionen der freigegebenen Software verwendet werden.

Wird von diesen Anweisungen abgewichen, MUSS dies durch Vorgesetzte und den IT-Betrieb genehmigt werden und entsprechend dokumentiert werden.

#### **3.2. Standard-Anforderungen**

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik für diesen Baustein. Sie SOLLTEN grundsätzlich erfüllt werden.

#### **APP.6.A6 Berücksichtigung empfohlener Sicherheitsanforderungen (S)**

Die Institution SOLLTE die nachfolgenden Sicherheitsanforderungen im Anforderungskatalog für die Software berücksichtigen:

- Die Software SOLLTE generelle Sicherheitsfunktionen wie Protokollierung und Authentifizierung umfassen, die im Anwendungskontext erforderlich sind.
- Die Software SOLLTE es ermöglichen, die Härtungsfunktionen der Einsatzumgebung zu nutzen. Hierbei SOLLTEN insbesondere die Härtungsfunktionen des geplanten Betriebssystems und der geplanten Ausführungsumgebung berücksichtigt werden.
- Wenn durch die Software Informationen über ungesicherte, öffentliche Netze übertragen werden, dann SOLLTE die Software sichere Verschlüsselungsfunktionen einsetzen, die dem Stand der Technik entsprechen. Darüber hinaus SOLLTEN die übertragenen Daten auf Integrität überprüft werden, indem Prüfsummen oder digitale Signaturen eingesetzt werden.
- Verwendet die Software Zertifikate, dann SOLLTE sie die Möglichkeit bieten, die Zertifikate transparent darzustellen. Zudem SOLLTE es möglich sein, Zertifikate zu sperren, ihnen das Vertrauen zu entziehen oder eigene Zertifikate zu ergänzen.

Die sich aus den Sicherheitsanforderungen ergebenden Funktionen der Software SOLLTEN im Betrieb verwendet werden.

#### **APP.6.A7 Auswahl und Bewertung potentieller Software (S) [Fachverantwortliche, Beschaffungsstelle]**

Anhand des Anforderungskatalogs SOLLTEN die am Markt erhältlichen Produkte gesichtet werden. Sie SOLLTEN mithilfe einer Bewertungsskala miteinander verglichen werden. Danach SOLLTE untersucht werden, ob die Produkte aus der engeren Wahl die Anforderungen der Institution erfüllen. Gibt es mehrere Alternativen für Produkte, SOLLTEN auch die Akzeptanz der Benutzenden und der zusätzliche Aufwand für z. B. Schulungen oder die Migration berücksichtigt werden. Fachverantwortliche SOLLTEN gemeinsam mit dem IT-Betrieb anhand der Bewertungen und Testergebnisse ein geeignetes Softwareprodukt auswählen.

#### **APP.6.A8 Regelung zur Verfügbarkeit der Installationsdateien (S)**

Der IT-Betrieb SOLLTE die Verfügbarkeit der Installationsdateien sicherstellen, um die Installation reproduzieren zu können. Hierzu SOLLTE der IT-Betrieb

- die Installationsdateien geeignet sichern oder
- die Verfügbarkeit der Installationsdateien durch die Bezugsquelle (z. B. App-Store) sicherstellen.

Zusätzlich SOLLTE sichergestellt werden, dass Software reproduzierbar konfiguriert werden kann. Hierzu SOLLTEN die Konfigurationsdateien gesichert werden. Alternativ SOLLTE geeignet dokumentiert werden, wie die Software konfiguriert wird.

Diese Regelung SOLLTE in das Datensicherungskonzept der Institution integriert werden.

#### **APP.6.A9 Inventarisierung von Software (S)**

Software SOLLTE inventarisiert werden. In einem Bestandsverzeichnis SOLLTE dokumentiert werden, auf welchen Systemen die Software unter welcher Lizenz eingesetzt wird. Bei Bedarf SOLLTEN zusätzlich die sicherheitsrelevanten Einstellungen miterfasst werden. Software SOLLTE nur mit Lizenzen eingesetzt werden, die dem Einsatzzweck und den vertraglichen Bestimmungen entsprechen. Die Lizenz SOLLTE den gesamten vorgesehenen Benutzungszeitraum der Software abdecken.

Wird von einer Standardkonfiguration abgewichen, SOLLTE dies dokumentiert werden. Das Bestandsverzeichnis SOLLTE anlassbezogen durch den IT-Betrieb aktualisiert werden, insbesondere wenn Software installiert wird.

Das Bestandsverzeichnis SOLLTE so aufgebaut sein, dass bei Sicherheitsvorfällen eine schnelle Gesamtübersicht mit den notwendigen Details ermöglicht wird.

#### **APP.6.A10 Erstellung einer Sicherheitsrichtlinie für den Einsatz der Software (S)**

Die Institution SOLLTE die Regelungen, die festlegen, wie die Software eingesetzt und betrieben wird, in einer Sicherheitsrichtlinie zusammenfassen. Die Richtlinie SOLLTE allen relevanten Verantwortlichen, Zuständigen und Mitarbeitenden der Institution bekannt sein und die Grundlage für ihre Arbeit und ihr Handeln bilden. Inhaltlich SOLLTE die Richtlinie auch ein Benutzenden-Handbuch umfassen, dass erläutert, wie die Software zu benutzen und zu administrieren ist.

Es SOLLTE regelmäßig und stichprobenartig überprüft werden, ob die Mitarbeitenden sich an die Richtlinie halten. Die Richtlinie SOLLTE regelmäßig aktualisiert werden.

#### **APP.6.A11 Verwendung von Plug-ins und Erweiterungen (S)**

Es SOLLTEN nur unbedingt notwendige Plug-ins und Erweiterungen installiert werden. Werden Erweiterungen eingesetzt, SOLLTE die Software die Möglichkeit bieten, Erweiterungen zu konfigurieren und abzuschalten.

#### **APP.6.A12 Geregelte Außerbetriebnahme von Software (S) [Fachverantwortliche]**

Wenn Software außer Betrieb genommen wird, SOLLTE der IT-Betrieb mit den Fachverantwortlichen regeln, wie dies im Detail durchzuführen ist. Ebenfalls SOLLTE geregelt werden, wie die Benutzenden hierüber zu informieren sind. Hierbei SOLLTE geklärt werden, ob die funktionalen Anforderungen fortbestehen (z. B. zur Bearbeitung von Fachaufgaben). Ist dies der Fall, dann SOLLTE geregelt werden, wie die benötigten Funktionen der betroffenen Software weiter verfügbar sein werden.

#### **APP.6.A13 Deinstallation von Software (S)**

Wird Software deinstalliert, SOLLTEN alle angelegten und nicht mehr benötigten Dateien entfernt werden. Alle Einträge in Systemdateien, die für das Produkt vorgenommen wurden und nicht länger benötigt werden, SOLLTEN rückgängig gemacht werden.

## **3.3. Anforderungen bei erhöhtem Schutzbedarf**

Im Folgenden sind für diesen Baustein exemplarische Vorschläge für Anforderungen aufgeführt, die über dasjenige Schutzniveau hinausgehen, das dem Stand der Technik entspricht. Die Vorschläge SOLLTEN bei erhöhtem Schutzbedarf in Betracht gezogen werden. Die konkrete Festlegung erfolgt im Rahmen einer individuellen Risikoanalyse.

#### **APP.6.A14 Nutzung zertifizierter Software (H)**

Bei der Beschaffung von Software SOLLTE festgelegt werden, ob Zusicherungen des herstellenden oder anbietenden Unternehmens über implementierte Sicherheitsfunktionen als ausreichend vertrauenswürdig anerkannt werden können. Ist dies nicht der Fall, SOLLTE eine Zertifizierung der Anwendung z. B. nach Common Criteria als Entscheidungskriterium herangezogen werden. Stehen mehrere Produkte zur Auswahl, SOLLTEN insbesondere dann Sicherheitszertifikate berücksichtigt werden, wenn der evaluierte Funktionsumfang die Mindestfunktionalität (weitestgehend) umfasst und die Mechanismenstärke dem Schutzbedarf entspricht.

# **4. Weiterführende Informationen**

## **4.1. Wissenswertes**

Die International Organization for Standardization (ISO) gibt in der Norm ISO/IEC 27001:2013 im Annex A.14 "Security requirements of information systems" Anforderungen an die Informationssicherheit von IT-Systemen, die auch bei der Auswahl und dem Einsatz von Software berücksichtigt werden sollten.

Die Common Criteria for Information Technology Security Evaluation (CC) stellen die Basis für international anerkannte Produktzertifizierungen dar. Eine CC-Zertifizierung kann somit als Nachweis für die Informationssicherheit eines Softwareproduktes herangezogen werden.

Das National Institute of Standardisation and Technology formuliert in der NIST Special Publication 800-53 im Appendix F "Family System and Service Acquisition" unter anderem Anforderungen an die Anschaffung von IT-Produkten, hierunter auch Software.

Das Information Security Forum (ISF) stellt in seinem Standard "The Standard of Good Practice for Information Security" in dem Kapitel "Business Application Management" unter anderem Best Practices zur Absicherung von Software vor.
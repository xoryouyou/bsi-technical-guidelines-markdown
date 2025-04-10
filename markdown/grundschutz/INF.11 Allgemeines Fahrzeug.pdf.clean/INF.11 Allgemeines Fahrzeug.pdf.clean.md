![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_2.jpeg)

# **INF.11 Allgemeines Fahrzeug**

# **1. Beschreibung**

# **1.1. Einleitung**

Institutionen nutzen in vielen Situationen die unterschiedlichsten Fahrzeuge im Nah- und Fernbereich. Als Fahrzeug werden im Kontext dieses Bausteins motorisierte Fortbewegungsmittel bezeichnet, die sich in der Regel auf Land- und Luftstraßen, Seewegen sowie Wasserstraßen bewegen und über eine Fahrzeugkabine oder Vergleichbares verfügen. Beispiele hierfür sind PKW, LKW, Flugzeuge oder Schiffe. Im folgenden Text wird nur noch der Oberbegriff Fahrzeug verwendet, außer es ist eine bestimmte Art von Fahrzeug gemeint.

Nahezu alle modernen Fahrzeuge verfügen über integrierte IT-Komponenten, wie zum Beispiel Infotainmentsysteme oder interne Analysesysteme, die im Rahmen der Informationssicherheit ganzheitlich betrachtet werden müssen. Darüber hinaus werden dienstliche Aufgaben häufig nicht nur in den Räumen und Gebäuden einer Institution erledigt, sondern auch innerhalb von Fahrzeugen, die sich an wechselnden Standorten und in verschiedenen Umgebungen befinden können. Ein Fahrzeug ist somit auch eine eigenständige mobile Arbeitsumgebung, die durch die Institution angemessen abgesichert werden muss.

## **1.2. Zielsetzung**

Der Baustein beschreibt spezifische Gefährdungen, die zu beachten sind, wenn Institutionen Fahrzeuge mit IT-Komponenten einsetzen oder Fahrzeuge im Allgemeinen als IT-Arbeitsplätze verwenden. Darauf aufbauend legt der Baustein fest, welche Anforderungen von Fahrzeugnutzenden und haltenden zu erfüllen sind, um den optimalen Betrieb eines Fahrzeugs aus Sicht der Informationssicherheit zu gewährleisten.

# **1.3. Abgrenzung und Modellierung**

Der Baustein INF.11 *Allgemeines Fahrzeug* ist grundsätzlich auf jedes von der Institution eingesetztes Land-, Luft- und Wasserfahrzeug einmal anzuwenden.

Adressaten des Bausteins sind Benutzende und Betreibende von Fahrzeugen. Autonom fahrende oder ferngesteuerte Fahrzeuge, Schienenfahrzeuge und Raumfahrzeuge sind von diesem Baustein ausgenommen.

Die Art, die Ausstattung, der Einsatzort und das Aufgabenfeld von Fahrzeugen können sich je nach Institution voneinander unterscheiden. In dem Baustein INF.11 *Allgemeines Fahrzeu*g werden nur die typischen Einsatzszenarien von Fahrzeugen berücksichtigt, sodass spezielle Einsatzzwecke, wie etwa Rettungseinsätze von Rettungshubschraubern oder Kampfeinsätze von Militärfahrzeugen, ergänzend individuell betrachtet werden müssen.

Daher wird nicht abschließend auf nachträglich eingebaute, einsatzspezifische IT-Systeme oder fahrzeugspezifische Fachanwendungen eingegangen, wie sie zum Beispiel bei Einsatzfahrzeugen oder Führungsfahrzeugen üblich sind. Die Ausstattung und die damit verbundenen Fachanwendungen dieser Fahrzeuge sind individuell ergänzend zu behandeln.

Außerdem werden die fahrzeugeigenen Netze über Kommunikationsbusse wie CAN, LIN oder Flexray, auch IVN (In-Vehicle-Network) genannt, nicht betrachtet, da diese in der Regel nicht durch die Anwendenden verändert werden.

Um die mitgeführten und nachträglich eingebauten IT-Komponenten abzusichern, müssen alle relevanten Bausteine, wie SYS.3.1 *Laptops*, SYS.3.2 *Allgemeine Smartphones und Tablets*, NET.3.3 *VPN* und die Bausteinschichten NET.4 *Telekommunikation* sowie NET.2 *Funknetze* gesondert berücksichtigt werden.

Darüber hinaus muss, bevor das Fahrzeug entsorgt, bzw. ausgesondert wird, der Baustein CON.6 *Löschen und Vernichten* angewendet werden, damit keine schützenswerten Informationen im Fahrzeug verbleiben.

Dieser Baustein behandelt alle infrastrukturellen Aspekte, sodass INF.9 *Mobiler Arbeitsplatz* nicht zusätzlich zu modellieren ist.

# **2. Gefährdungslage**

Da IT-Grundschutz-Bausteine nicht auf individuelle Informationsverbünde eingehen können, werden zur Darstellung der Gefährdungslage typische Szenarien zugrunde gelegt. Die folgenden spezifischen Bedrohungen und Schwachstellen sind für den Baustein INF.11 *Allgemeines Fahrzeug* von besonderer Bedeutung.

## **2.1. Fehlende oder unzureichende Regelungen für Fahrzeuge**

Wird nicht oder nur unzureichend geregelt, welche Informationen über die von Fahrzeugen für Benutzende zur Verfügung gestellten Netze wie WLAN oder Bluetooth übertragen und verarbeitet werden dürfen und welche Schutzvorkehrungen dabei zu treffen sind, können vertrauliche Informationen offengelegt werden. Wird nicht hinreichend geregelt, wie diese abzusichern und zu benutzen sind, könnten schützenswerte Informationen wie personenbezogene Daten offengelegt werden.

Wenn Fahrzeuge gestohlen werden oder integrierte IT-Komponenten ausfallen und es hierfür keine Regelungen und festgelegte Abläufe gibt, kann dies gravierende Folgen haben. Es besteht die Gefahr, dass schützenswerte Informationen im Fahrzeug verbleiben und unbefugte Dritte Zugang zu diesen erhalten.

Wenn Fahrzeuge oder die darin verbauten IT-Komponenten unsachgemäß in Betrieb genommen werden, kann dies zu umfangreichen Gefährdungen der Informationssicherheit führen. Es könnten relevante Einstellungen, wie die automatische Synchronisation von Telefonbüchern, falsch konfiguriert sein oder es könnten Funktionstest bei Flugzeugen übersprungen oder unsachgemäß durchgeführt werden. Dies wiederum kann dazu führen, dass die Systeme des Flugzeuges während des Einsatzes nicht wie vorgesehen funktionieren und schlimmstenfalls zu einem Totalverlust des Flugzeugs führen.

Genauso kann aber auch die Funktion der integrierten IT-Komponenten und des gesamten Fahrzeuges gefährdet werden, wenn das Fahrzeug unsachgemäß ausgeschaltet oder temporär außer Betrieb genommen wird. Ein Beispiel hierfür sind Einsatzfahrzeuge. Werden diese für einen längeren Zeitraum ausgeschaltet, so droht aufgrund der umfangreichen Ausstattung, dass sich die Fahrzeugbatterie

vollständig entlädt. Infolgedessen kann das Fahrzeug nicht mehr starten und in den integrierten IT-Komponenten könnten Daten verloren gehen.

# **2.2. Fehlendes Sicherheitsbewusstsein und Sorglosigkeit beim Umgang mit dem Fahrzeug**

Fehlendes Sicherheitsbewusstsein und Sorglosigkeit beim Umgang mit den Fahrzeugen und deren Komponenten stellen eine ernstzunehmende Gefahr dar. Sind Mitarbeitende beispielsweise nicht ausreichend geschult, wie sie mit den Fahrzeugen und den IT-Komponenten umgehen sollen und sind sich der möglichen Risiken nicht bewusst, könnten Fahrzeuge und die darin verbauten IT-Komponenten falsch oder unsorgfältig benutzt werden. So werden zum Beispiel IT-Systeme auf Brücken von Schiffen von unterschiedlichen Personen benutzt. Werden nun wesentliche Einstellungen von einem Benutzenden verändert, ohne die weiteren Benutzenden darüber zu informieren, dann könnten Fehlfunktionen auftreten, die die weiteren Benutzenden nicht nachvollziehen können.

Eine weitere Gefahr kann darin bestehen, dass Fahrzeuge unzuverlässig abgeschlossen werden. Hierdurch könnten unbefugte Dritte einfach die Fahrzeugkabine betreten und alle dort vorhandenen IT-Komponenten und abgelegten Informationen einsehen oder entwenden.

Weiterhin könnten schlecht geschulte Mitarbeitende unangemessen auf Störungen reagieren und durch eine falsche Reaktion die Situation verschlimmern. Wird z. B. bei einer Störung der integrierten IT-Systeme des Fahrzeugs nicht die hierfür zuständige Stelle der Institution kontaktiert, sondern vom Benutzenden versucht, die Störung selbst zu beheben, können hieraus unabsehbare Folgen resultieren. Es könnten beispielsweise relevante Einstellungen für die Sicherheit oder den Datenschutz verändert werden.

# **2.3. Ungeregelte Datenübertragung an Dritte und unsichere Kommunikationsschnittstellen**

Viele moderne Fahrzeuge verfügen nicht nur über die für die Benutzenden relevanten bzw. direkt ersichtlichen drahtlosen Kommunikationsschnittstellen, wie z. B. Bluetooth oder WLAN. Viele interne Systeme des Fahrzeugs kommunizieren direkt über integrierte Mobilfunkschnittstellen mit IT-Systemen der herstellenden Unternehmen, wobei dieser Informationsaustausch von den Anwendenden in der Regel nicht beeinflusst werden kann. Hiermit sind nicht nur gesetzlich vorgeschriebene und für den Anwendenden transparente Systeme wie der eCall gemeint, sondern insbesondere auch solche, die nicht für den Benutzenden direkt ersichtlich sind. Beispielsweise übertragen viele fahrzeugherstellende Unternehmen Daten, um detaillierte Informationen über den Standort und die Kilometerzahl des Fahrzeugs oder über das Verhalten der Fahrzeugführenden zu sammeln. Dadurch könnten umfangreich personenbezogene Daten über die Fahrzeugnutzenden erhoben werden, ohne dass diese darüber Kenntnis haben oder dieser Datenerhebung und verarbeitung explizit zugestimmt haben.

Eine weitere Gefahr sind unsichere Kommunikationsschnittstellen der Fahrzeuge. Durch mangelnde Schutzmechanismen können so sensible Daten ausgelesen werden. Lässt beispielsweise das Infotainmentsystem eine Bluetooth-Koppelung ohne Sicherheitsmechanismen zu, könnten unbefugte Dritte ihr Smartphone unbemerkt damit koppeln und Adressbücher synchronisieren.

## **2.4. Unsachgemäße Veränderungen am Fahrzeug**

Während herkömmliche PKW sehr selten durch den Fahrzeugbetreibenden verändert werden, müssen Fahrzeuge für spezialisierte Einsatzzwecke sehr häufig noch durch die Betreibenden oder spezialisierten Unternehmen nachträglich angepasst werden. Ein Beispiel hierfür sind Einsatzfahrzeuge oder nachträglich modernisierte oder umfunktionierte Schiffe. Wird in diesen Fällen

ein Fahrzeug unsachgemäß verändert, indem z. B. zusätzliche Kabel ungeeignet verlegt werden, kann dies zu erheblichen Schäden bis hin zum Totalverlust des Fahrzeugs führen.

Auch anderweitige Veränderungen können die Einsatzfähigkeit der Fahrzeuge beeinträchtigen. Wird z. B das Infotainmentsystem manipuliert, um neue bzw. gesperrte Funktionen freizuschalten, könnten die Updates des herstellenden Unternehmens nicht mehr eingespielt und damit verbunden potentielle Sicherheitslücken nicht mehr geschlossen werden.

# **2.5. Manipulation, unbefugter Zutritt und Diebstahl bei Fahrzeugen**

Offen in Fahrzeugen liegende Informationen können häufig von außerhalb der Fahrzeuge eingesehen werden, wenn kein oder nur ein unzureichender Sichtschutz vorhanden ist. Dies kann Begehrlichkeiten wecken, die zu Angriffen führen.

Fahrzeuge werden häufig auf öffentlich zugänglichen Parkplätzen abgestellt oder an Bootsanlegern vertäut, die nicht durch zentrale Schutzmaßnahmen der Institution, wie Sicherheitsdienste oder verschlossene Garagen, geschützt werden. Sie sind somit prinzipiell einem erhöhten Risiko ausgesetzt, von Unbefugten betreten zu werden. Unsichere Schließsysteme können hierbei eine Schwachstelle sein. Zum Beispiel können sogenannte schlüssellose Schließsysteme an Fahrzeugen unter Umständen leicht durch Relay-Angriffe umgangen werden.

Somit können IT-Systeme, Zubehör, Informationen und Software häufig einfacher manipuliert, zerstört oder gestohlen werden, wenn sie in Fahrzeugen statt in Räumlichkeiten der Institution unbeaufsichtigt aufbewahrt werden. Werden IT-Systeme, Zubehör, Informationen oder Software manipuliert oder zerstört, sind die Mitarbeitenden in Fahrzeugen oft nur noch eingeschränkt arbeitsfähig. Die betroffenen IT-Systeme könnten sogar in der Art manipuliert werden, dass z. B. die darauf verarbeiteten Daten durch Schadsoftware an unbefugte Dritte weitergeleitet werden. Des Weiteren müssen womöglich zerstörte IT-Komponenten ersetzt werden, was sowohl finanzielle als auch personelle Ressourcen erfordert.

## **2.6. Gefahren im Zusammenhang mit Wartung, Reparatur und Updates**

Werden Fahrzeuge und die verwendeten IT-Komponenten nicht oder nur unzureichend gewartet und gepflegt oder ihre Funktionsfähigkeit nicht regelmäßig überprüft, kann das dazu führen, dass sie im Bedarfsfall nicht oder nur eingeschränkt einsatzfähig sind.

Eine große Herausforderung hierbei ist, dass Updates für die in den Fahrzeugen integrierten IT-Systeme nicht unbedingt zu den regelmäßigen Wartungszyklen der Fahrzeuge bereitstehen. Dadurch könnten Updates beispielsweise nur unregelmäßig und verzögert eingespielt werden.

In institutionseigenen Werkstätten können die Fahrzeuge und die verbauten IT-Komponenten in der Regel nicht vollständig gewartet oder repariert werden, weshalb Fahrzeuge häufig an Fremdfirmen übergeben werden. In den Räumlichkeiten der Fremdfirmen sind die Fahrzeuge meist unbeobachtet und Dritte können umfassend auf das Fahrzeug und die verwendeten IT-Komponenten zugreifen. Dadurch besteht ein erhöhtes Risiko, dass die IT-Komponenten missbraucht oder schützenswerte Informationen entwendet werden.

## **2.7. Gefahren bei der Aussonderung**

Werden Fahrzeuge ausgesondert, können diese mit allen verbauten IT-Komponenten oder mit einem Teil davon veräußert werden. Hierdurch können Fremdpersonen auf die IT-Komponenten zugreifen und so auf interne Informationen oder personenbezogene Daten rückschließen, wie zum Beispiel gespeicherte Telefonnummern. Außerdem können institutionseigene Komponenten wie SIM-Karten oder Kryptomodule in den Fahrzeugen verbleiben. Somit würden die nachfolgenden Besitzenden

ungewollt Zugang zu diesen erhalten und könnten beispielsweise Informationen aus diesen Komponenten auslesen (wie z. B. Telefonnummern von der SIM-Karte) und widerrechtlich verwenden.

# **2.8. Unzulässige Temperatur und Luftfeuchte in Fahrzeugen**

Jedes Gerät hat einen Temperaturbereich, innerhalb dessen es ordnungsgemäß funktioniert. Überoder unterschreitet die Raumtemperatur die Grenzen dieses Bereiches, können Geräte sowie IT-Komponenten ausfallen und der Betrieb kann gestört werden. Ähnliches gilt für die Luftfeuchtigkeit. In Fahrzeugen liegen unterschiedliche Voraussetzungen vor, die genau zu solchen Situationen führen können. So kann der Innenraum von in der Sonne abgestellten Fahrzeugen bis zu 70 Grad erreichen und somit den üblichen Temperaturbereich von z. B. Lithium-Ionen-Akkus überschreiten.

# **3. Anforderungen**

Im Folgenden sind die spezifischen Anforderungen des Bausteins INF.11 *Allgemeines Fahrzeug*  aufgeführt. Der oder die Informationssicherheitsbeauftragte (ISB) ist dafür zuständig, dass alle Anforderungen gemäß dem festgelegten Sicherheitskonzept erfüllt und überprüft werden. Bei strategischen Entscheidungen ist der oder die ISB stets einzubeziehen.

Im IT-Grundschutz-Kompendium sind darüber hinaus weitere Rollen definiert. Sie sollten besetzt werden, insofern dies sinnvoll und angemessen ist.

| Zuständigkeiten         | Rollen                                                      |
|-------------------------|-------------------------------------------------------------|
| Grundsätzlich zuständig | Informationssicherheitsbeauftragte                          |
| Weitere Zuständigkeiten | Mitarbeitende, Fachverantwortliche, Datenschutzbeauftragte, |
|                         | Benutzende, Beschaffungsstelle, IT-Betrieb                  |

Genau eine Rolle sollte *Grundsätzlich zuständig* sein. Darüber hinaus kann es noch *Weitere Zuständigkeiten* geben. Falls eine dieser weiteren Rollen für die Erfüllung einer Anforderung vorrangig zuständig ist, dann wird diese Rolle hinter der Überschrift der Anforderung in eckigen Klammern aufgeführt. Die Verwendung des Singulars oder Plurals sagt nichts darüber aus, wie viele Personen diese Rollen ausfüllen sollen.

# **3.1. Basis-Anforderungen**

Die folgenden Anforderungen MÜSSEN für diesen Baustein vorrangig erfüllt werden.

#### **INF.11.A1 Planung und Beschaffung (B) [Fachverantwortliche, Beschaffungsstelle, Datenschutzbeauftragte]**

Bevor Fahrzeuge beschafft werden, MUSS der Einsatzzweck geplant werden. Die funktionalen Anforderungen an die Fahrzeuge und insbesondere die Anforderungen an die Informationssicherheit, sowie den Datenschutz der verbauten IT-Komponenten MÜSSEN erhoben werden. Hierbei MÜSSEN folgende Aspekte berücksichtigt werden:

- Einsatzszenarien der Fahrzeuge,
- nähere Einsatzumgebung der Fahrzeuge sowie
- der gesamte Lebenszyklus der Fahrzeuge.

Die Fahrzeuge MÜSSEN außerdem über angemessene Schließsysteme verfügen, sofern die Fahrzeuge nicht durchgehend durch andere Maßnahmen oder Regelungen gesichert werden können. Während der Planung SOLLTE berücksichtigt werden, dass viele Fahrzeuge Daten an die fahrzeugherstellenden Unternehmen und weitere Dritte übermitteln können.

#### **INF.11.A2 Wartung, Inspektion und Updates (B) [Fachverantwortliche, IT-Betrieb]**

Die Fahrzeuge und die dazugehörenden IT-Komponenten MÜSSEN nach den Vorgaben des herstellenden Unternehmens gewartet werden. Hierbei MUSS beachtet werden, dass die Intervalle der herkömmlichen Wartung und von Updates der integrierten IT-Komponenten voneinander abweichen können. Es MUSS klar geregelt werden, wer in welcher Umgebung die Updates installieren darf. Auch "Over-the-Air" (OTA) Updates MÜSSEN geregelt eingespielt werden.

Wartungs- und Reparaturarbeiten MÜSSEN von befugtem und qualifiziertem Personal in einer sicheren Umgebung durchgeführt werden. Dabei SOLLTE schon vor der Wartung geklärt werden, wie mit Fremdfirmen umgegangen wird. Werden Fahrzeuge in fremden Institutionen gewartet, SOLLTE geprüft werden, ob alle nicht benötigten, zum Fahrzeug dazugehörigen portablen IT-Systeme entfernt werden.

Werden die Fahrzeuge wieder in den Einsatzbetrieb integriert, MUSS mittels Checkliste geprüft werden, ob alle Beanstandungen und Mängel auch behoben wurden. Es MUSS auch geprüft werden, ob die vorhandenen IT-Komponenten einsatzfähig sind.

#### **INF.11.A3 Regelungen für die Fahrzeugbenutzung (B) [IT-Betrieb, Fachverantwortliche, Benutzende, Datenschutzbeauftragte]**

Für alle Tätigkeiten, die sich auf die Sicherheit der in den Fahrzeugen verarbeiteten Informationen auswirken können, MUSS vorher geregelt werden, ob sie in den Fahrzeugen durchgeführt werden dürfen. Hierbei MUSS klar geregelt werden, welche Informationen dabei transportiert und bearbeitet werden dürfen. Ergänzend MUSS festgelegt werden, welche Schutzvorkehrungen dabei zu treffen sind. Dies MUSS für jede Art von Information gelten, auch für Gespräche in den Fahrzeugen. Es MUSS geklärt werden, unter welchen Rahmenbedingungen Mitarbeitende auf welche Art von Informationen ihrer Institution zugreifen dürfen.

Außerdem MUSS geregelt werden, in welchem Umfang Infotainmentsysteme, Anwendungen und sonstige Services der Fahrzeuge genutzt werden dürfen. Des Weiteren MUSS festgelegt werden, wie Schnittstellen abzusichern sind. In bestehende Geschäfts- bzw. Dienstanweisungen MUSS beschrieben werden, wie mitgeführte IT in den Fahrzeugen verwendet und aufbewahrt werden darf.

# **3.2. Standard-Anforderungen**

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik für diesen Baustein. Sie SOLLTEN grundsätzlich erfüllt werden.

#### **INF.11.A4 Erstellung einer Sicherheitsrichtlinie (S) [Fachverantwortliche, IT-Betrieb]**

Alle relevanten Sicherheitsanforderungen für die IT innerhalb der Fahrzeuge SOLLTEN in einer für Mitarbeitende verpflichtenden Sicherheitsrichtlinie dokumentiert werden. Die Richtlinie SOLLTE allen relevanten Mitarbeitenden der Institution bekannt sein und die Grundlage für ihren Umgang mit Fahrzeugen darstellen. In der Richtlinie SOLLTEN die Zuständigkeiten für einzelne Aufgaben klar geregelt sein. Die Sicherheitsrichtlinie SOLLTE regelmäßig überprüft und anlassbezogen aktualisiert werden.

#### **INF.11.A5 Erstellung einer Inventarliste (S)**

Für jedes Fahrzeug SOLLTE eine Inventarliste über

- die im Fahrzeug fest verbauten oder zugehörigen IT-Komponenten (z. B. Handfunkgeräte bei Einsatzfahrzeugen),
- die Fachverfahren, die auf den integrierten IT-Komponenten ausgeführt werden,
- Handlungsanweisungen und Betriebsdokumentationen sowie
- die mit dem Infotainmentsystem gekoppelten Mobilgeräte

geführt werden. Die Inventarliste SOLLTE regelmäßig und anlassbezogen aktualisiert werden. Dabei SOLLTE überprüft werden, ob noch alle inventarisierten zum Fahrzeug gehörenden IT-Komponenten vorhanden sind. Zusätzlich SOLLTE anhand der Inventarliste überprüft werden, ob keine mobilen Endgeräte unerlaubt mit dem Infotainmentsystem gekoppelt worden sind.

#### **INF.11.A6 Festlegung von Handlungsanweisungen (S) [Fachverantwortliche, Benutzende]**

Für alle wesentlichen Situationen, die die Informationssicherheit von Fahrzeugen betreffen, SOLLTEN Handlungsanweisungen in Form von Checklisten vorliegen. Die Handlungsanweisungen SOLLTEN dabei in die Sicherheitsrichtlinie integriert werden und in geeigneter Form als Checklisten verfügbar sein, während das Fahrzeug benutzt wird. Hierbei SOLLTE auch der Fall berücksichtigt werden, dass das Fahrzeug selbst gestohlen wird. Die Handlungsanweisungen SOLLTEN insbesondere nachfolgende Szenarien behandeln:

- Ausfall von IT-Komponenten der Fahrzeuge,
- Notfallsituationen wie Unfälle,
- unerlaubtes Betreten der Fahrzeuge sowie
- Diebstahl der Fahrzeuge oder darin abgelegter Gegenstände mit Relevanz für die Informationssicherheit.

Die Zuständigkeiten für die einzelnen Aufgaben SOLLTEN in der Checkliste dokumentiert sein. Die Anweisungen SOLLTEN von den Fahrzeugbenutzenden in den entsprechenden Situationen angewendet werden. Anhand der Checkliste SOLLTE dokumentiert werden, wie sie in diesen Situationen vorgegangen sind.

#### **INF.11.A7 Sachgerechter Umgang mit Fahrzeugen und schützenswerten Informationen (S) [Fachverantwortliche, Benutzende]**

Die Institution SOLLTE die Handlungsanweisungen zur Fahrzeugbenutzung um Aspekte ergänzen, wann, wie und wo Fahrzeuge sachgerecht abgestellt bzw. angedockt werden dürfen. Hierbei SOLLTE primär die Frage beantwortet werden, welche Umgebungen die Fahrzeuge angemessenen vor unerlaubten Zutritt oder Sachbeschädigung schützen. Des Weiteren SOLLTE hierbei berücksichtigt werden, welche Informationen und IT-Systeme in den Fahrzeugen aufbewahrt werden dürfen. Ausreichende Maßnahmen zum Zutrittsschutz SOLLTEN ergriffen werden.

Die Ladung der Fahrzeuge SOLLTE sicher verstaut werden. Es SOLLTE sichergestellt werden, dass schützenswerte Informationen nicht von außerhalb der Fahrzeuge von Unbefugten eingesehen, mitgehört oder entwendet werden können. Die Mitarbeitenden SOLLTEN mit der grundlegenden Funktionsweise der Fahrzeuge und den betreffenden IT-Komponenten vertraut gemacht werden. Die Mitarbeitenden SOLLTEN auch über die bestehenden Sicherheitsrisiken informiert werden.

#### **INF.11.A8 Schutz vor witterungsbedingten Einflüssen (S) [Benutzende, Fachverantwortliche]**

Fahrzeuge und die darin verbauten IT-Komponenten SOLLTEN vor witterungsbedingten Einflüssen ausreichend geschützt werden. Je nach Fahrzeugart, Einsatzort und Einsatzumgebung SOLLTEN zusätzliche Schutzmaßnahmen ergriffen werden. Für kurzfristig auftretende extreme Wettererscheinungen SOLLTEN entsprechende Schutzmaßnahmen getroffen werden.

Diese Schutzmaßnahmen SOLLTEN in den Handlungsanweisungen zur Fahrzeugbenutzung in Form von Checklisten dokumentiert werden.

#### **INF.11.A9 Sicherstellung der Versorgung (S) [Fachverantwortliche]**

Bevor Fahrzeuge eingesetzt werden, SOLLTE geplant werden, wie diese mit Betriebsstoffen während des Einsatzes versorgt werden. Die Fahrzeuge SOLLTEN dabei während des Einsatzes immer ausreichend mit Betriebsstoffen versorgt werden.

#### **INF.11.A10 Aussonderung (S) [IT-Betrieb, Fachverantwortliche]**

Werden Fahrzeuge ausgesondert, SOLLTEN keine schützenswerten Informationen in den Fahrzeugen verbleiben. Bevor Fahrzeuge endgültig ausgesondert werden, SOLLTE anhand der Inventarliste geprüft werden, ob keine inventarisierten Gegenstände und darüber hinaus relevanten Gegenstände zurückgelassen worden sind.

# **3.3. Anforderungen bei erhöhtem Schutzbedarf**

Im Folgenden sind für diesen Baustein exemplarische Vorschläge für Anforderungen aufgeführt, die über dasjenige Schutzniveau hinausgehen, das dem Stand der Technik entspricht. Die Vorschläge SOLLTEN bei erhöhtem Schutzbedarf in Betracht gezogen werden. Die konkrete Festlegung erfolgt im Rahmen einer individuellen Risikoanalyse.

#### **INF.11.A11 Ersatzvorkehrungen bei Ausfällen (H) [Fachverantwortliche]**

Für den Fall, dass Fahrzeuge oder Fahrzeugführende ausfallen, SOLLTEN innerhalb der Institution vorbereitende Maßnahmen getroffen werden. Abhängig von der Bedeutung der Fahrzeuge SOLLTEN Ersatzfahrzeuge bereitstehen oder alternativ ein Rahmenvertrag mit einer geeigneten Fremdinstitution geschlossen werden. Zusätzlich dazu SOLLTEN Ersatzfahrzeugführende verfügbar sein.

#### **INF.11.A12 Diebstahlsicherung bzw. Bewachung (H) [Fachverantwortliche, Mitarbeitende]**

Eine Alarmanlage SOLLTE vorhanden sein. Bei Bodenfahrzeugen SOLLTE darüber hinaus eine Wegfahrsperre vorhanden sein. Wird das Fahrzeug verlassen, SOLLTEN die Alarmanlage und Wegfahrsperre aktiviert werden. Alternativ SOLLTEN die Fahrzeuge bewacht werden.

#### **INF.11.A13 Schädigende Fremdeinwirkung (H) [Fachverantwortliche]**

Je nach Art der Fahrzeuge SOLLTEN geeignete Maßnahmen ergriffen werden, um die Fahrzeuge vor potentieller Fremdeinwirkung in der geplanten Einsatzumgebung zu schützen, wie z. B. störenden Funkstrahlen.

#### **INF.11.A14 Schutz sensibler Informationen vor unbefugtem Zugriff und Kenntnisnahme (H) [IT-Betrieb, Fachverantwortliche]**

Fahrzeuge und die dazugehörigen IT-Komponenten SOLLTEN so abgesichert werden, dass sensible Informationen durch Unbefugte nicht ausgelesen bzw. manipuliert oder gelöscht werden können. Hierbei SOLLTEN die vorhandenen Schutzvorkehrungen der herstellenden Unternehmen überprüft und bei Bedarf angepasst werden.

#### **INF.11.A15 Physische Absicherung der Schnittstellen (H) [IT-Betrieb, Fachverantwortliche]**

Alle physischen internen und externen Schnittstellen der Fahrzeuge SOLLTEN physisch gegen unbefugte Benutzung und äußere Einflüsse abgesichert werden.

#### **INF.11.A16 Brandlöschanlage (H) [Fachverantwortliche]**

Die Fahrzeuge SOLLTEN über eine Brandlöschanlage verfügen, die einen Brand von außen und innen löschen kann. Alternativ SOLLTEN geeignete Mittel zur Brandbekämpfung mitgeführt werden.

#### **INF.11.A17 Netztrennung des In-Vehicle-Network mit einem Sonderfahrzeugnetz über Gateways (H)**

Generell SOLLTE die Institution sicherstellen, dass keine Informationen unerlaubt und undefiniert zwischen

- dem In-Vehicle-Network (IVN), das wiederum an die Netze der fahrzeugherstellenden Unternehmen angebunden ist und
- den einsatzspezifischen IT-Komponenten

ausgetauscht werden. Hierzu SOLLTEN Gateways mit standardisierten Protokollen (z. B. nach Standard CiA 447) eingesetzt werden. Die Gateways SOLLTEN dabei vom fahrzeugherstellenden Unternehmen freigegeben sein.

# **4. Weiterführende Informationen**

### **4.1. Wissenswertes**

Der wissenschaftliche Artikel "IT-Sicherheit und Datenschutz im vernetzten Fahrzeug" des Fraunhofer Instituts (DOI: 10.1007/s11623-015-0434-4) gibt einen generellen Überblick über vernetzte Fahrzeuge, mögliche Anwendungen, die benötigten Daten und die sich daraus ergebenden Bedrohungen.

Der wissenschaftliche Artikel "Security Issues and Vulnerabilities in Connected Car Systems" von der IEEE Konferenz 2015 zeigt auf, welche neuen Bedrohungen durch die Fahrzeugvernetzung entstehen.
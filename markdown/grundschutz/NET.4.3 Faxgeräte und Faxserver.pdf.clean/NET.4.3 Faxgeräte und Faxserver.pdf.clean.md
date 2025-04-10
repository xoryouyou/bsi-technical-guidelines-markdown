![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_2.jpeg)

# **NET.4.3 Faxgeräte und Faxserver**

# **1. Beschreibung**

## **1.1. Einleitung**

In diesem Baustein werden die Sicherheitsaspekte der Informationsübermittlung über marktübliche Faxgeräte sowie Faxserver betrachtet. Die übermittelten Informationen werden als Fax (Kurzform von Telefax) oder seltener auch als Telefaksimile oder Fernkopie bezeichnet. Bei einem herkömmlichen Faxgerät werden von einer Vorlage die darauf aufgezeichneten Inhalte vom Sendegerät Punkt für Punkt abgetastet und zu den Empfangsgeräten übertragen. Das Empfangsgerät baut diese Inhalte wieder Punkt für Punkt auf und gibt sie in der Regel direkt auf Papier aus.

Ein Faxserver hingegen ist ein Dienst, der auf einem Server installiert wird und so anderen IT-Systemen in einem Datennetz ermöglicht, Faxe zu versenden und zu empfangen. Faxserver werden häufig in bereits bestehende E-Mail- oder Groupware-Systeme integriert. So ist es möglich, dass eingehende Fax-Dokumente durch den Faxserver per E-Mail an die Benutzenden zugestellt werden. Abzusendende Dokumente werden entweder über eine Druckerwarteschlange oder per E-Mail an den Faxserver übergeben. In der Regel wird das Dokument zwischen Faxserver und den Clients im Datennetz als Bild-Datei gesendet oder empfangen. Die übermittelte Bild-Datei kann nicht unmittelbar in Textverarbeitungssystemen weiterverarbeitet werden. Hierzu ist in der Regel zunächst eine Texterkennung (OCR, Optical Character Recognition) erforderlich. Von einem Faxserver empfangene und verarbeitete Dokumente lassen sich für gewöhnlich einfach archivieren, beispielsweise durch den Faxserver-Dienst selber, durch Dokumentenmanagementsysteme oder durch die Groupware, die direkt an den Faxserver-Dienst angebunden sind.

## **1.2. Zielsetzung**

Ein Ziel dieses Bausteins ist der Schutz der Informationen, die mithilfe von Faxsendungen übermittelt und verarbeitet werden. Ein weiteres Ziel ist der Schutz der Faxgeräte und Faxserver vor Manipulationen durch Unbefugte. Das Übertragungsmedium spielt bei der Anwendung des Bausteins keine Rolle, sodass die Anforderungen des Bausteins auch für Fax over IP (FoIP) umgesetzt werden sollten.

## **1.3. Abgrenzung und Modellierung**

Der Baustein NET.4.3 *Faxgeräte und Faxserver* ist für jedes Faxgerät und jeden Faxserver im Informationsverbund anzuwenden.

In diesem Baustein werden als technische Basis des Faxversandes marktübliche Stand-Alone-Faxgeräte und Faxserver betrachtet. Zusätzliche Aspekte zu Faxgeräten, die in einem Multifunktionsgerät (All-inone-Gerät) zu finden sind, werden gesondert in dem Baustein SYS.4.1 *Drucker, Kopierer und Multifunktionsgeräte* behandelt. Zum Schutz der Informationen, die auf Faxservern verarbeitet, angeboten, gespeichert und darüber übertragen werden, sollten der Baustein SYS.1.1 *Allgemeiner Server* sowie die jeweiligen betriebssystemspezifischen Bausteine betrachtet werden. Informationen zur richtigen Archivierung können dem Baustein OPS.1.2.2 *Archivierung* entnommen werden.

# **2. Gefährdungslage**

Da IT-Grundschutz-Bausteine nicht auf individuelle Informationsverbünde eingehen können, werden zur Darstellung der Gefährdungslage typische Szenarien zugrunde gelegt. Die folgenden spezifischen Bedrohungen und Schwachstellen sind für den Baustein NET.4.3 *Faxgeräte und Faxserver* von besonderer Bedeutung.

## **2.1. Unzureichende oder falsche Versorgung mit Verbrauchsgütern**

Faxgeräte empfangen Dokumente und drucken diese in der Regel direkt auf Papier aus. Für einen reibungslosen und unterbrechungsfreien Betrieb eines Faxgerätes müssen Verbrauchsgüter wie Papier und Toner in ausreichender Menge vorhanden sein. Ist dies nicht gegeben, können oft keine Fax-Dokumente empfangen werden. Außerdem können keine Sendebestätigungen ausgedruckt werden, die eventuell zwingend benötigt werden.

## **2.2. Fehlerhafte Faxübertragung**

Auf dem Übertragungsweg zwischen Sendegerät und Empfangsgerät eines Fax-Dokuments können zahlreiche Störungen auftreten. Dies kann dazu führen, dass die zu übermittelnden Fax-Dokumente unvollständig oder unlesbar sind oder gar nicht bei den Empfangenden ankommen. Entscheidungen, die von diesen Informationen abhängig sind, können fehlerhaft sein und somit hohe Schäden verursachen.

Zeitverzögerungen, die entstehen, weil die Probleme erst erkannt werden müssen und das Dokument neu gesendet werden muss, können zu weiteren Komplikationen führen. Oft haben die Sendenden oder Empfangenden gar keine Möglichkeiten, den Übertragungsweg zu beeinflussen, sodass sie warten müssen, bis die Störung durch Dritte behoben wurde. Häufig glauben die Absendenden sogar, dass das Fax-Dokument ordnungsgemäß an die gewünschten Adressaten übermittelt wurden und die hierdurch entstehenden Probleme werden erst sehr spät erkannt.

Zusätzlich kann nicht ausgeschlossen werden, dass ein Fax-Dokument an das falsche Empfangsgerät übermittelt wurde, beispielsweise weil eine Fehlschaltung im öffentlichen Telekommunikationsnetz vorliegt. Ebenso ist denkbar, dass bei Faxgeräten Rufnummern falsch gewählt oder Zielwahltasten falsch programmiert werden. Wird ein Faxserver verwendet, können die Rufnummern ebenfalls falsch eingegeben oder falsch im Adressbuch abgespeichert werden. Dadurch können unter Umständen vertrauliche Informationen an unbefugte Personen übermittelt werden.

## **2.3. Manipulation von Adressbüchern und Verteilerlisten**

In Faxgeräten können häufig Adressbücher und Verteilerlisten geführt werden. Wird ein Faxserver genutzt, können in der Regel über die Groupware ähnliche Adressbücher und Verteilerlisten an einer zentralen Stelle geführt werden, die von mehreren Benutzenden verwendet werden können. In den Adressbüchern können Nummern von Empfangenden gespeichert werden, sodass diese nicht bei jedem Faxversand neu eingegeben werden müssen. Zudem ist es möglich, über Verteilerlisten eine Gruppe von Empfangenden anzulegen und so Faxsendungen an mehrere Personen gleichzeitig zu verschicken.

Häufig werden einmal programmierte Nummern von Empfangenden oder Verteilerlisten nicht mehr kontrolliert, wenn ein Fax-Dokument versendet werden soll. Wenn Unbefugte die Adressbücher oder die Verteilerlisten am Faxgerät oder in der Groupware ändern, können so vertrauliche Informationen an die falschen Empfangenden gelangen. Außerdem kann es passieren, dass die vorgesehenen Empfangenden dringend benötigte Informationen nicht erhalten. Beispielsweise könnte eine Faxnummer im Adressbuch ausgetauscht oder weitere Empfangende in die Verteilerliste aufgenommen werden, ohne dass dies von den Verantwortlichen in der jeweiligen Institution bemerkt wird.

## **2.4. Unbefugtes Lesen von Faxsendungen**

In fast allen Fällen ist es am wirtschaftlichsten, wenn sich mehrere Benutzende ein Faxgerät teilen. Daher werden diese in der Regel in Räumen aufgestellt, die alle Mitarbeitenden einer Institution betreten können, wie beispielsweise in Druckerräumen. Da hierdurch die Faxgeräte für alle Mitarbeitenden frei zugänglich sind, können auch alle Mitarbeitenden die empfangenen Faxsendungen lesen und so an vertrauliche Informationen gelangen.

## **2.5. Auswertung von Restinformationen in Faxgeräten und Faxservern**

Abhängig vom technischen Verfahren, mit dem Faxgeräte Informationen speichern, weiterverarbeiten oder drucken, können nach dem Faxversand und -empfang Restinformationen unterschiedlichen Umfangs im Faxgerät verbleiben. Unbefugte, die in den Besitz des Gerätes oder der entsprechenden Bauteile kommen, können diese Informationen unter Umständen wiederherstellen.

Auf der Festplatte eines Faxservers werden Faxsendungen mindestens so lange gespeichert, bis sie an das Ziel zugestellt werden können. Weiterhin arbeiten moderne Betriebssysteme mit Auslagerungsdateien, die auch Restinformationen enthalten können. Diese Informationen könnten beim Zugriff auf diesen Faxserver unerlaubt ausgewertet werden.

## **2.6. Vortäuschen eines falschen Absendenden bei Faxsendungen**

Faxsendungen sind ein beliebtes Medium, um Dokumente, die nur mit einer Unterschrift gültig sind, zu übertragen. Doch auf die gleiche Weise, wie mit einem falschen Namen und einem falschen Briefkopf falsche Absendende vorgetäuscht werden kann, kann auch eine Faxsendung manipuliert werden. So können beispielsweise Unterschriften von anderen Schriftstücken eingescannt und auf das Fax-Dokument kopiert werden. Ein Unterschied, ob es sich um eine tatsächlich getätigte Unterschrift oder um eine reproduzierte Grafikdatei handelt, ist generell nicht zu erkennen. Schäden entstehen dann, wenn Empfangende die darin enthaltenen Informationen als authentisch oder sogar als rechtsverbindlich ansehen.

## **3. Anforderungen**

Im Folgenden sind die spezifischen Anforderungen des Bausteins NET:4.3 *Faxgeräte und Faxserver* aufgeführt. Der oder die Informationssicherheitsbeauftragte (ISB) ist dafür zuständig, dass alle Anforderungen gemäß dem festgelegten Sicherheitskonzept erfüllt und überprüft werden. Bei strategischen Entscheidungen ist der oder die ISB stets einzubeziehen.

Im IT-Grundschutz-Kompendium sind darüber hinaus weitere Rollen definiert. Sie sollten besetzt werden, insofern dies sinnvoll und angemessen ist.

| Zuständigkeiten         | Rollen                                                  |
|-------------------------|---------------------------------------------------------|
| Grundsätzlich zuständig | Fachverantwortliche                                     |
| Weitere Zuständigkeiten | Benutzende, Beschaffungsstelle, IT-Betrieb, Haustechnik |

Genau eine Rolle sollte *Grundsätzlich zuständig* sein. Darüber hinaus kann es noch *Weitere Zuständigkeiten* geben. Falls eine dieser weiteren Rollen für die Erfüllung einer Anforderung vorrangig zuständig ist, dann wird diese Rolle hinter der Überschrift der Anforderung in eckigen Klammern aufgeführt. Die Verwendung des Singulars oder Plurals sagt nichts darüber aus, wie viele Personen diese Rollen ausfüllen sollen.

## **3.1. Basis-Anforderungen**

Die folgenden Anforderungen MÜSSEN für diesen Baustein vorrangig erfüllt werden.

#### **NET.4.3.A1 Geeignete Aufstellung eines Faxgerätes (B) [Haustechnik]**

Faxgeräte MÜSSEN so aufgestellt werden, dass eingegangene Faxsendungen nicht von Unberechtigten eingesehen oder entnommen werden können. Der Aufstellungsort SOLLTE zudem danach ausgewählt werden, dass ausreichend dimensionierte Telekommunikationsleitungen bzw. -kanäle vorhanden sind. Der Aufstellungsort MUSS über einen geeigneten Netzanschluss für das Faxgerät verfügen. Faxgeräte DÜRFTEN NICHT an nicht dafür vorgesehene Netzanschlüsse angeschlossen werden.

#### **NET.4.3.A2 Informationen für Mitarbeitende über die Faxnutzung (B)**

Alle Mitarbeitenden MÜSSEN auf die Besonderheiten der Informationsübermittlung per Fax hingewiesen werden. Sie MÜSSEN auch darüber informiert sein, dass die Rechtsverbindlichkeit einer Faxsendung stark eingeschränkt ist. Eine verständliche Bedienungsanleitung MUSS am Faxgerät ausliegen. Die Benutzenden SOLLTEN mindestens eine Kurzanleitung zur eingesetzten Faxclient-Software des Faxservers erhalten. Außerdem MUSS eine Anweisung zur korrekten Faxnutzung ausliegen.

#### **NET.4.3.A3 Sicherer Betrieb eines Faxservers (B) [IT-Betrieb]**

Bevor ein Faxserver in Betrieb genommen wird, SOLLTE eine Testphase erfolgen. Konfigurationsparameter sowie alle Änderungen an der Konfiguration eines Faxservers SOLLTEN dokumentiert werden. Die Archivierung und Löschung von Faxdaten SOLLTEN geregelt sein. Außerdem MUSS regelmäßig die Verbindung vom Faxserver zur TK-Anlage beziehungsweise zum öffentlichen Telefonnetz auf ihre Funktion geprüft werden. Es MUSS außerdem sichergestellt werden, dass der Faxserver ausschließlich Fax-Dienste anbietet und nicht für weitere Dienste genutzt wird. Alle nicht benötigten Leistungsmerkmale und Zugänge der eingesetzten Kommunikationsschnittstellen MÜSSEN deaktiviert werden.

## **3.2. Standard-Anforderungen**

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik für diesen Baustein. Sie SOLLTEN grundsätzlich erfüllt werden.

#### **NET.4.3.A4 Erstellung einer Sicherheitsrichtlinie für die Faxnutzung (S)**

Vor der Freigabe eines Gerätes SOLLTE eine Sicherheitsrichtlinie für die Faxnutzung erstellt werden. Dort SOLLTE die Einsatzart festgelegt sein. Außerdem SOLLTE geregelt werden, wie mit Faxeingängen und -ausgängen umzugehen ist. Zudem SOLLTE eine Regelung zur Behandlung von nicht zustellbaren Faxsendungen erstellt werden. Außerdem SOLLTE die Richtlinie Informationen und Anweisungen zur Notfallvorsorge und Ausfallsicherheit des Faxbetriebes enthalten.

#### **NET.4.3.A5 ENTFALLEN (S)**

Diese Anforderung ist entfallen.

#### **NET.4.3.A6 Beschaffung geeigneter Faxgeräte und Faxserver (S) [Beschaffungsstelle]**

Bevor Faxgeräte oder Faxserver beschafft werden, SOLLTE eine Anforderungsliste erstellt werden. Anhand dieser Liste SOLLTEN die infrage kommenden Systeme oder Komponenten bewertet werden. Die Anforderungsliste für Faxgeräte SOLLTE auch sicherheitsrelevante Aspekte umfassen, wie den Austausch einer Teilnehmererkennung, die Ausgabe von Sendeberichten sowie eine Fehlerprotokollierung und Journalführung. Zudem SOLLTEN angemessene zusätzliche Sicherheitsfunktionen anhand des Schutzbedarfs berücksichtigt werden.

Bei einem Faxserver SOLLTEN alle Anforderungen an das IT-System einschließlich Betriebssystem, Kommunikationskomponenten und Applikationssoftware erhoben und berücksichtigt werden. Die Möglichkeit, dass ein Faxserver in ein bestehendes Datennetz und in ein Groupware-System integriert werden kann, SOLLTE bei Bedarf berücksichtigt werden.

#### **NET.4.3.A7 Geeignete Kennzeichnung ausgehender Faxsendungen (S) [Benutzende]**

Quelle und Ziel jeder Faxsendung SOLLTEN auf allen ausgehenden Faxsendungen ersichtlich sein. Wenn diese Informationen nicht aus dem versendeten Dokument ermittelt werden können, SOLLTE ein standardisiertes Faxdeckblatt benutzt werden. Generell SOLLTE das Faxdeckblatt mindestens den Namen der Institution des Absendenden, den Namen des Ansprechpartners bzw. der Ansprechpartnerin, das Datum, die Seitenanzahl sowie einen Dringlichkeitsvermerk auflisten. Außerdem SOLLTE es die Namen und die Institution der Empfangenden enthalten. Wenn notwendig, SOLLTE das Faxdeckblatt für jedes ausgehende Fax angepasst werden.

#### **NET.4.3.A8 Geeignete Entsorgung von Fax-Verbrauchsgütern und - Ersatzteilen (S)**

Alle Fax-Verbrauchsgüter, aus denen Informationen über die versendeten und empfangenen Fax-Dokumente gewonnen werden können, SOLLTEN vor der Entsorgung unkenntlich gemacht werden oder durch eine zuverlässige Fachfirma entsorgt werden. Die gleiche Vorgehensweise SOLLTE auch bei ausgetauschten informationstragenden Ersatzteilen erfolgen. Wartungsfirmen, die Faxgeräte überprüfen oder reparieren, SOLLTEN zu einer entsprechenden Handhabung verpflichtet werden. Es SOLLTE regelmäßig kontrolliert werden, ob diese Handhabung eingehalten wird.

#### **NET.4.3.A9 Nutzung von Sende- und Empfangsprotokollen (S)**

Die Übertragungsvorgänge ein- und ausgehender Faxsendungen SOLLTEN protokolliert werden. Dazu SOLLTEN die Kommunikationsjournale marktüblicher Faxgeräte genutzt werden. Verfügen die Faxgeräte über Protokollierungsfunktionen, SOLLTEN diese aktiviert werden. Bei einem Faxserver SOLLTE die Protokollierung ebenso aktiviert werden. Auch SOLLTE entschieden werden, welche Informationen protokolliert werden sollen.

Die Kommunikationsjournale der Faxgeräte und die Protokollierungsdateien SOLLTEN regelmäßig ausgewertet und archiviert werden. Sie SOLLTEN stichprobenartig auf Unregelmäßigkeiten geprüft werden. Unbefugte SOLLTEN nicht auf die Kommunikationsjournale sowie die protokollierten Informationen zugreifen können.

#### **NET.4.3.A10 Kontrolle programmierbarer Zieladressen, Protokolle und Verteilerlisten (S)**

Programmierbare Kurzwahltasten oder gespeicherte Zieladressen SOLLTEN regelmäßig daraufhin überprüft werden, ob die gewünschte Faxnummer mit der einprogrammierten Nummer übereinstimmt. Nicht mehr benötige Faxnummern SOLLTEN gelöscht werden. Es SOLLTE in geeigneter Weise dokumentiert werden, wenn ein neuer Eintrag aufgenommen oder eine Zielnummer geändert wird.

# **3.3. Anforderungen bei erhöhtem Schutzbedarf**

Im Folgenden sind für diesen Baustein exemplarische Vorschläge für Anforderungen aufgeführt, die über dasjenige Schutzniveau hinausgehen, das dem Stand der Technik entspricht. Die Vorschläge SOLLTEN bei erhöhtem Schutzbedarf in Betracht gezogen werden. Die konkrete Festlegung erfolgt im Rahmen einer individuellen Risikoanalyse.

#### **NET.4.3.A11 Schutz vor Überlastung des Faxgerätes (H) [IT-Betrieb]**

Es SOLLTEN ausreichend Kommunikationsleitungen bzw. -kanäle verfügbar sein. Bei einem Faxserver SOLLTE das voraussichtliche Faxvolumen abgeschätzt werden. Es SOLLTEN entsprechend leistungsfähige Komponenten ausgewählt werden. Die Protokolle von Faxservern SOLLTEN regelmäßig kontrolliert werden, um Engpässen durch Überlastungen rechtzeitig entgegenzuwirken. Nicht mehr benötigte Faxdaten SOLLTEN zeitnah vom Faxserver gelöscht werden.

#### **NET.4.3.A12 Sperren bestimmter Quell- und Ziel-Faxnummern (H)**

Unerwünschte Faxadressen, SOLLTEN blockiert werden. Alternativ SOLLTEN nur bestimmte Rufnummern zugelassen werden. Es SOLLTE geprüft werden, welcher Ansatz in welcher Situation geeignet ist.

#### **NET.4.3.A13 Festlegung berechtigter Faxbedienenden (H) [Benutzende]**

Es SOLLTEN nur wenige Mitarbeitende ausgewählt werden, die auf das Faxgerät zugreifen dürfen. Diese Mitarbeitenden SOLLTEN ankommende Faxsendungen an die Empfangenden verteilen. Den Mitarbeitenden SOLLTE vermittelt werden, wie sie mit dem Gerät umgehen und wie sie die erforderlichen Sicherheitsmaßnahmen umsetzen können. Jeder berechtigte Benutzende SOLLTE darüber unterrichtet werden, wer das Faxgerät bedienen darf und wer für das Gerät zuständig ist.

#### **NET.4.3.A14 Fertigung von Kopien eingehender Faxsendungen (H) [Benutzende]**

Auf Thermopapier gedruckte Faxsendungen, die länger benötigt werden, SOLLTEN auf Normalpapier kopiert oder eingescannt werden. Es SOLLTE berücksichtigt werden, dass auf Thermopapier die Farbe schneller verblasst und somit unkenntlich wird. Die Kopien oder eingescannten Faxsendungen SOLLTEN in geeigneter Weise archiviert werden.

#### **NET.4.3.A15 Ankündigung und Rückversicherung im Umgang mit Faxsendungen (H) [Benutzende]**

Wichtige Faxsendungen SOLLTEN den Empfangenden angekündigt werden, bevor sie versendet werden. Dazu SOLLTE festgelegt werden, welche Dokumente vorab angemeldet werden sollen. Mitarbeitende, die vertrauliche Fax-Dokumente versenden möchten, SOLLTEN angewiesen werden, sich den vollständigen Erhalt von den Empfangenden bestätigen zu lassen. Bei wichtigen oder ungewöhnlichen Faxsendungen SOLLTEN sich wiederum Empfangende von den Absendenden bestätigen lassen, dass das Fax-Dokument von ihnen stammt und nicht gefälscht wurde. Es SOLLTE eine geeignete Kommunikationsform ausgewählt werden, mit dem die Fax-Dokumente angekündigt oder bestätigt werden, beispielsweise per Telefon.

# **4. Weiterführende Informationen**

### **4.1. Wissenswertes**

Für den Baustein NET:4.3 *Faxgeräte und Faxserver* sind keine weiterführenden Informationen vorhanden.
![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_2.jpeg)

# **INF.2 Rechenzentrum sowie Serverraum**

# **1. Beschreibung**

# **1.1. Einleitung**

Heute werden fast alle strategischen und operativen Funktionen und Aufgaben durch Informationstechnik (IT) maßgeblich unterstützt oder sind ohne IT nicht ausführbar. Dadurch steigen die Anforderungen an die Leistungsfähigkeit und Verfügbarkeit der IT-Systeme und deren Anbindung an die Netzumgebung stetig. Um diesem Leistungsbedarf gerecht zu werden, um entsprechende Reserven vorzuhalten und um die IT auch wirtschaftlich betreiben zu können, konzentrieren Institutionen jeglicher Größe ihre IT-Landschaft in Rechenzentren.

Ein Rechenzentrum (RZ) ist wie folgt definiert:

- 1. Hat eine IT-nutzende Institution nur einen zentralen IT-Betriebsbereich, ist dieser gemeinsam mit den erforderlichen Supportbereichen grundsätzlich immer wie ein RZ entsprechend dem Schutzbedarf zu behandeln. Unter "IT-Betriebsbereich" sind Räume zu verstehen, in denen die Hardware aufgebaut ist und betrieben wird, die der Bereitstellung von Diensten und Daten dient. Das RZ umfasst neben dem IT-Betriebsbereich alle weiteren technischen Supportbereiche (z. B. Stromversorgung, Kälteversorgung, Löschtechnik, Sicherheitstechnik), die dem bestimmungsgemäßen Betrieb und der Sicherheit des IT-Betriebsbereichs dienen.
- 2. Wird die IT der Institution innerhalb eines Gebäudes oder einer Liegenschaft verteilt in mehreren Bereichen betrieben und sind diese Bereiche untereinander und zu den IT-Benutzenden hin durch hauseigene LAN-Verbindungen angeschlossen, ist mindestens der funktional bedeutendste dieser Bereiche als RZ zu behandeln. Des Weiteren sind Bereiche, von deren ordnungsgemäßem Betrieb 50 % und mehr IT-Benutzenden abhängig sind oder aus denen heraus 50 % und mehr an Diensten und Daten (gemessen an der Gesamtheit der Bereiche) bereitgestellt werden, als RZ zu behandeln.
- 3. Ist die IT-nutzende Institution an mehreren räumlich voneinander getrennten Standorten angesiedelt und sind diese durch andere als hauseigene LAN-Verbindungen miteinander gekoppelt, ist jeder der Standorte entsprechend (1) separat zu betrachten und zu behandeln.
- 4. Ein IT-Betriebsbereich, in dem für kritische Geschäftsprozesse (Prozesse, deren Störung oder Ausfall zu wesentlichen Beeinträchtigungen der Erledigung primärer Aufgaben einer Institution führen) erforderliche IT angesiedelt ist, ist immer als RZ zu behandeln, unabhängig von Größe oder Anteilsregeln aus Nummer (2).
- 5. IT-Betriebsbereiche, aus denen heraus Dienste oder Dienstleistungen für Dritte erbracht werden, sind immer als Teil eines RZ zu betrachten. Dabei ist es unerheblich, ob dies gegen Entgelt erfolgt oder nicht.
- 6. Besteht ein begründetes Interesse, einen IT-Betriebsbereich gemeinsam mit seinem Supportbereich abweichend von den vorgenannten Regelungen als Serverraum zu behandeln, ist dies samt den sich daraus ergebenden Reduzierungen von Sicherheitsanforderungen zu begründen.

Die Auflistung der sechs Punkte bedeutet nicht, dass alle Punkte gemeinsam erfüllt sein müssen, damit ein Bereich als Rechenzentrum betrachtet wird. Vielmehr werden verschiedene Möglichkeiten beschrieben, wann ein Bereich als RZ anzusehen ist. Weicht ein Rechenzentrum von dieser Definition ab, wird der betrachtete IT-Betriebsbereich als Serverraum bezeichnet. Diese Definition orientiert sich ausschließlich an der Bedeutung der IT-Struktur für die Aufgabenerfüllung der nutzenden Institution und steht damit im methodischen Einklang mit der DIN EN 50600.

Soll ein Serverraum abgesichert werden, können die Anforderungen dieses Bausteins entsprechend reduziert werden. Dies muss jedoch stichhaltig und nachvollziehbar begründet werden (6) und es müssen mindestens die Basis-Anforderungen umgesetzt werden.

# **1.2. Zielsetzung**

Dieser Baustein richtet sich einerseits an Institutionen, die ein Rechenzentrum betreiben und im Rahmen einer Revision prüfen möchten, ob sie geeignete Sicherheitsmaßnahmen umgesetzt haben. Andererseits kann der Baustein auch dazu benutzt werden, die Sicherheitsmaßnahmen abzuschätzen, die umgesetzt werden müssen, wenn die IT in einem Rechenzentrum zentralisiert werden soll. Das oberste Ziel der in diesem Baustein beschriebenen Anforderungen ist es, den sicheren Betrieb des Rechenzentrums zu gewährleisten.

# **1.3. Abgrenzung und Modellierung**

Der Baustein INF.2 *Rechenzentrum sowie Serverraum* ist auf jedes Rechenzentrum und jeden Serverraum anzuwenden.

Der vorliegende Baustein eignet sich nicht für kleine Informationsverbünde mit z. B. nur einem oder sehr wenigen Servern oder IT-Systemen. Ein Beispiel dafür ist eine kleine Institution mit wenigen IT-Arbeitsplätzen und einem Server, der in einem separaten Raum betrieben wird. In solchen Fällen genügt es oft, den Baustein INF.5 *Raum sowie Schrank für technische Infrastruktur* umzusetzen.

Anforderungen an Gebäude und die Verkabelung im Allgemeinen sind nicht Teil dieses Bausteins. Diese sind in den Bausteinen INF.1 *Allgemeines Gebäude* und INF.12 *Verkabelung* zu finden, die immer auf Räume und Gebäude bzw. die Verkabelung anzuwenden sind.

Um den Baustein überschaubar zu halten, wurde bewusst auf technische Details und planerische Größen verzichtet. Nähere Informationen liefern einschlägige Normen und weitere Veröffentlichungen des BSI.

# **2. Gefährdungslage**

Da IT-Grundschutz-Bausteine nicht auf individuelle Informationsverbünde eingehen können, werden zur Darstellung der Gefährdungslage typische Szenarien zugrunde gelegt. Die folgenden spezifischen Bedrohungen und Schwachstellen sind für den Baustein INF.2 *Rechenzentrum sowie Serverraum* von besonderer Bedeutung.

# **2.1. Fehlerhafte Planung**

Wenn ein Rechenzentrum konzipiert und dabei nicht berücksichtigt wird, es gegen elementare Gefährdungen abzusichern, besteht ein sehr hohes Ausfallrisiko. So können z. B. Standortrisiken wie Luftverkehr, Erdbeben oder Hochwasser die Betriebssicherheit und Verfügbarkeit gefährden. Ebenso massiv kann es sich auf den Betrieb eines Rechenzentrums auswirken, wenn durch eine fehlerhafte Konzeptionierung nicht genügend Bandbreite verfügbar ist oder die Energieversorgung am gewählten Standort nicht ausreicht.

# **2.2. Fehlende oder fehlerhafte Zutrittskontrollen**

Fehlen Zutrittskontrollen oder sind diese unzureichend, erhöht sich die Gefahr, dass unberechtigte Personen das Rechenzentrum betreten und dort fahrlässig, z. B. aufgrund mangelnder Fachkenntnisse, oder vorsätzlich Schaden anrichten. Angreifende können so z. B. schützenswerte Daten entwenden, Geräte stehlen oder Server manipulieren. Unzureichende Zutrittskontrollen wirken sich somit auf die Verfügbarkeit, Vertraulichkeit und die Integrität von Daten und IT-Komponenten aus.

# **2.3. Unzureichende Überwachung**

Wird die im Rechenzentrum betriebene IT und Infrastruktur unzureichend überwacht und betreut, können Komponenten unbemerkt ausfallen. Dadurch wird eventuell die Verfügbarkeit und fehlerfreie Funktion des Rechenzentrums stark beeinträchtigt. Ausfälle treten zudem oftmals schleichend ein. Ohne eine aktive Überwachung könnten diese zu spät bemerkt werden. Es ist dann oft nicht mehr möglich, rechtzeitig zu reagieren.

# **2.4. Unzureichende Klimatisierung im Rechenzentrum**

IT-Komponenten benötigen bestimmte Betriebsbedingungen, um zuverlässig zu funktionieren. Auch setzen sie die von ihnen aufgenommene elektrische Leistung in zusätzliche Wärme um. Wenn in einem IT-Betriebsbereich die Temperatur, die Luftfeuchte oder der Schwebestoffanteil nicht innerhalb der von den Geräteherstellenden vorgegebenen Grenzwerte gehalten werden, kann dies dazu führen, dass technische Komponenten nicht mehr richtig funktionieren oder ausfallen.

# **2.5. Feuer**

Feuer ist zwar eine Gefahr, die eher selten eintritt. Entsteht aber tatsächlich ein Brand, hat dieser meist schwerwiegende Auswirkungen. Denn durch Feuer und Rauch können große Schäden entstehen. Während innerhalb des IT-Betriebsbereichs Elektrobrände die häufigste Ursache für Feuer sind, kann ein Feuer außerhalb des IT-Betriebsbereichs und insbesondere in Supportbereichen, wie der Energieversorgung (inklusive NEA und USV) oder der Klimaanlage, zahlreiche weitere Ursachen haben. Haben der IT-Betriebsbereich oder die Supportbereiche sowie andere Nachbarbereiche keinen oder nur einen unzureichenden Brandschutz, kann sich ein Feuer schnell ausbreiten. Zudem könnten außerhalb entstehende Brände auf das Rechenzentrum übergreifen.

## **2.6. Wasser**

Durch undichte Wasserleitungen, Hochwasser, Rohrbruch, defekte Sprinkler- oder Klimaanlagen kann Wasser in das Rechenzentrum eintreten. Hierdurch können Geräte beschädigt werden und nicht mehr funktionieren. Es kann auch ein Kurzschluss ausgelöst werden, durch den einzelne Bereiche des Rechenzentrums ausfallen oder ein Brand entstehen könnte.

# **2.7. Fehlender oder unzureichender Einbruchschutz**

Selbst wenn eine gut funktionierende Zutrittskontrolle eingerichtet ist, können unbefugte Personen in ein Rechenzentrum eindringen, sofern es nicht ausreichend vor Einbrüchen geschützt wird. Täter und Täterinnen könnten so z. B. IT-Komponenten stehlen oder manipulieren und an vertrauliche Informationen gelangen. Auch könnten sie die Geräte zerstören oder das Rechenzentrum insgesamt beschädigen.

# **2.8. Ausfall der Stromversorgung**

Wenn der Strom ausfällt, kann der Betriebsablauf eines Rechenzentrums und damit der Institution erheblich gestört werden. So sind bei einem Stromausfall eventuell die vom Rechenzentrum bereitgestellten IT-Services plötzlich nicht mehr erreichbar. Ebenso können Daten verloren gehen. Zudem ist es möglich, dass durch einen plötzlichen Stromausfall IT-Systeme, TK-Systeme oder Überwachungstechnik beschädigt werden.

# **2.9. Verschmutzung**

Staub und andere Verschmutzungen in einem Rechenzentrum können dazu führen, dass technische Komponenten (z. B. Lüfter) nicht mehr funktionieren. Durch Verschmutzungen verschleißen Geräte früher und fallen häufiger aus.

# **3. Anforderungen**

Im Folgenden sind die spezifischen Anforderungen des Bausteins INF.2 *Rechenzentrum sowie Serverraum* aufgeführt. Der oder die Informationssicherheitsbeauftragte (ISB) ist dafür zuständig, dass alle Anforderungen gemäß dem festgelegten Sicherheitskonzept erfüllt und überprüft werden. Bei strategischen Entscheidungen ist der oder die ISB stets einzubeziehen.

Im IT-Grundschutz-Kompendium sind darüber hinaus weitere Rollen definiert. Sie sollten besetzt werden, insofern dies sinnvoll und angemessen ist.

| Zuständigkeiten         | Rollen                                                        |
|-------------------------|---------------------------------------------------------------|
| Grundsätzlich zuständig | IT-Betrieb                                                    |
| Weitere Zuständigkeiten | Mitarbeitende, Planende, Datenschutzbeauftragte, Haustechnik, |
|                         | Wartungspersonal                                              |

Genau eine Rolle sollte *Grundsätzlich zuständig* sein. Darüber hinaus kann es noch *Weitere Zuständigkeiten* geben. Falls eine dieser weiteren Rollen für die Erfüllung einer Anforderung vorrangig zuständig ist, dann wird diese Rolle hinter der Überschrift der Anforderung in eckigen Klammern aufgeführt. Die Verwendung des Singulars oder Plurals sagt nichts darüber aus, wie viele Personen diese Rollen ausfüllen sollen.

# **3.1. Basis-Anforderungen**

Die folgenden Anforderungen MÜSSEN für diesen Baustein vorrangig erfüllt werden.

## **INF.2.A1 Festlegung von Anforderungen (B) [Haustechnik, Planende]**

Für ein Rechenzentrum MÜSSEN angemessene technische und organisatorische Vorgaben definiert und umgesetzt werden.

Wenn ein Rechenzentrum geplant wird oder geeignete Räumlichkeiten ausgewählt werden, MÜSSEN auch geeignete Sicherheitsmaßnahmen unter Berücksichtigung des Schutzbedarfs der IT-Komponenten (insbesondere der Verfügbarkeit) mit geplant werden.

Ein Rechenzentrum MUSS insgesamt als geschlossener Sicherheitsbereich konzipiert werden. Es MUSS zudem unterschiedliche Sicherheitszonen aufweisen. Dafür MÜSSEN z. B. Verwaltungs-, Logistik-, IT-Betriebs- und Support-Bereiche klar voneinander getrennt werden. Im Falle eines Serverraums SOLLTE geprüft werden, ob unterschiedliche Sicherheitszonen eingerichtet werden können.

## **INF.2.A2 Bildung von Brandabschnitten (B) [Planende]**

Es MÜSSEN geeignete Brand- und Rauchabschnitte für die Räumlichkeiten eines Rechenzentrums festgelegt werden. Die Brand- und Rauchabschnitte MÜSSEN über den baurechtlich vorgeschriebenen Rahmen hinaus auch Schutz für die darin befindlichen technischen Einrichtungen und deren Verfügbarkeit bieten. Es MUSS verhindert werden, dass sich Brand und Rauch ausbreiten. Im Falle eines Serverraums SOLLTE geprüft werden, ob geeignete Brand- und Rauchabschnitte für die Räumlichkeiten umsetzbar sind.

#### **INF.2.A3 Einsatz einer unterbrechungsfreien Stromversorgung (B) [Haustechnik]**

Für alle betriebsrelevanten Komponenten des Rechenzentrums MUSS eine unterbrechungsfreie Stromversorgung (USV) installiert werden. Da der Leistungsbedarf von Klimaanlagen oft zu hoch für eine USV ist, MUSS mindestens die Steuerung der Anlagen an die unterbrechungsfreie Stromversorgung angeschlossen werden. Im Falle eines Serverraums SOLLTE je nach Verfügbarkeitsanforderungen der IT-Systeme geprüft werden, ob der Betrieb einer USV notwendig ist.

Die USV MUSS ausreichend dimensioniert sein. Bei relevanten Änderungen an den Verbrauchern MUSS überprüft werden, ob die vorhandenen USV-Systeme noch ausreichend dimensioniert sind.

Bei USV-Systemen mit Batterie als Energiespeicher MUSS die Batterie im erforderlichen Temperaturbereich gehalten werden. Sie SOLLTE dazu vorzugsweise räumlich getrennt von der Leistungselektronik der USV platziert werden. Die USV MUSS regelmäßig gewartet und auf Funktionsfähigkeit getestet werden. Dafür MÜSSEN die vom herstellenden Unternehmen vorgesehenen Wartungsintervalle eingehalten werden.

# **INF.2.A4 Notabschaltung der Stromversorgung (B) [Haustechnik]**

Es MUSS geeignete Möglichkeiten geben, elektrische Verbraucher im Rechenzentrum spannungsfrei zu schalten. Dabei MUSS darauf geachtet werden, ob und wie eine vorhandene USV räumlich und funktional in die Stromversorgung eingebunden ist. Werden klassische Not-Aus-Schalter eingesetzt, MUSS darauf geachtet werden, dass darüber nicht das komplette Rechenzentrum abgeschaltet wird. Die Notabschaltung MUSS sinnvoll parzelliert und zielgerichtet erfolgen. Alle Not-Aus-Schalter MÜSSEN so geschützt sein, dass sie nicht unbeabsichtigt oder unbefugt betätigt werden können.

# **INF.2.A5 Einhaltung der Lufttemperatur und -feuchtigkeit (B) [Haustechnik]**

Es MUSS sichergestellt werden, dass die Lufttemperatur und Luftfeuchtigkeit im IT-Betriebsbereich innerhalb der vorgeschriebenen Grenzwerte liegen. Die tatsächliche Wärmelast in den gekühlten Bereichen MUSS in regelmäßigen Abständen und nach größeren Umbauten überprüft werden.

Eine vorhandene Klimatisierung MUSS regelmäßig gewartet werden. Die Parameter Temperatur und Feuchtigkeit MÜSSEN mindestens so aufgezeichnet werden, dass sich rückwirkend erkennen lässt, ob Grenzwerte überschritten wurden, und dass sie bei der Lokalisierung der Ursache der Abweichung sowie bei der Beseitigung der Ursache unterstützend genutzt werden können.

## **INF.2.A6 Zutrittskontrolle (B) [Haustechnik]**

Der Zutritt zum Rechenzentrum MUSS kontrolliert werden. Zutrittsrechte MÜSSEN gemäß der Vorgaben des Bausteins ORP.4 *Identitäts- und Berechtigungsmanagement* vergeben werden. Für im Rechenzentrum tätige Personen MUSS sichergestellt werden, dass diese keinen Zutritt zu IT-Systemen außerhalb ihres Tätigkeitsbereiches erhalten.

Alle Zutrittsmöglichkeiten zum Rechenzentrum MÜSSEN mit Zutrittskontrolleinrichtungen ausgestattet sein. Jeder Zutritt zum Rechenzentrum MUSS von der Zutrittskontrolle individuell erfasst werden. Im Falle eines Serverraums SOLLTE geprüft werden, ob eine Überwachung aller Zutrittsmöglichkeiten sinnvoll ist.

Es MUSS regelmäßig kontrolliert werden, ob die Regelungen zum Einsatz einer Zutrittskontrolle eingehalten werden.

Die Anforderungen der Institution an ein Zutrittskontrollsystem MÜSSEN in einem Konzept ausreichend detailliert dokumentiert werden.

#### **INF.2.A7 Verschließen und Sichern (B) [Mitarbeitende, Haustechnik]**

Alle Türen des Rechenzentrums MÜSSEN stets verschlossen gehalten werden. Fenster MÜSSEN möglichst schon bei der Planung vermieden werden. Falls sie doch vorhanden sind, MÜSSEN sie ebenso wie die Türen stets verschlossen gehalten werden. Türen und Fenster MÜSSEN einen dem Sicherheitsniveau angemessenen Schutz gegen Angriffe und Umgebungseinflüsse bieten. Sie MÜSSEN mit einem Sichtschutz versehen sein. Dabei MUSS beachtet werden, dass die bauliche Ausführung aller raumbildenden Elemente in Bezug auf die erforderliche Schutzwirkung gleichwertig sein muss.

#### **INF.2.A8 Einsatz einer Brandmeldeanlage (B) [Planende]**

In einem Rechenzentrum MUSS eine Brandmeldeanlage installiert sein. Diese MUSS alle Flächen überwachen. Alle Meldungen der Brandmeldeanlage MÜSSEN geeignet weitergeleitet werden (siehe dazu auch INF.2.A13 *Planung und Installation von Gefahrenmeldeanlagen*). Die Brandmeldeanlage MUSS regelmäßig gewartet werden. Es MUSS sichergestellt werden, dass in Räumen des Rechenzentrums keine besonderen Brandlasten vorhanden sind.

#### **INF.2.A9 Einsatz einer Lösch- oder Brandvermeidungsanlage (B) [Haustechnik]**

In einem Rechenzentrum MUSS entweder eine Lösch- oder Brandvermeidungsanlage nach aktuellem Stand der Technik installiert sein oder durch technische (insbesondere durch eine flächendeckende Brandfrüherkennung, siehe INF.2.A17 *Brandfrüherkennung*) und organisatorische Maßnahmen (geschultes Personal und Reaktionspläne für Meldungen der Brandfrüherkennung) sichergestellt sein, dass unmittelbar (innerhalb von maximal 3 Minuten) auf Meldungen der Brandfrüherkennung mit schadensminimierenden Maßnahmen reagiert wird.

In Serverräumen ohne Lösch- oder Brandvermeidungsanlage MÜSSEN Handfeuerlöscher mit geeigneten Löschmitteln in ausreichender Zahl und Größe vorhanden sein. Es MUSS beachtet werden, dass darüber hinausgehende baurechtliche Anforderungen hinsichtlich der Ausstattung mit Handfeuerlöschern davon unberührt bleiben. Die Feuerlöscher MÜSSEN so angebracht werden, dass sie im Brandfall leicht zu erreichen sind. Jeder Feuerlöscher MUSS regelmäßig geprüft und gewartet werden. Alle Mitarbeitenden, die ein Rechenzentrum oder einen Serverraum betreten dürfen, MÜSSEN in die Benutzung der Handfeuerlöscher eingewiesen werden.

#### **INF.2.A10 Inspektion und Wartung der Infrastruktur (B) [Wartungspersonal, Haustechnik]**

Für alle Komponenten der baulich-technischen Infrastruktur MÜSSEN mindestens die vom herstellenden Unternehmen empfohlenen oder durch Normen festgelegten Intervalle und Vorschriften für Inspektion und Wartung eingehalten werden. Inspektionen und Wartungsarbeiten MÜSSEN protokolliert werden. Brandschotten MÜSSEN daraufhin geprüft werden, ob sie unversehrt sind. Die Ergebnisse MÜSSEN dokumentiert werden.

#### **INF.2.A11 Automatische Überwachung der Infrastruktur (B) [Haustechnik]**

Alle Einrichtungen der Infrastruktur, wie z. B. Leckageüberwachung, Klima-, Strom- und USV-Anlagen, MÜSSEN automatisch überwacht werden. Erkannte Störungen MÜSSEN schnellstmöglich in geeigneter Weise weitergeleitet und bearbeitet werden.

Im Falle eines Serverraums SOLLTEN IT- und Supportgeräte, die nicht oder nur selten von einer Person bedient werden müssen, mit einer Fernanzeige für Störungen ausgestattet werden. Die verantwortlichen Mitarbeitenden MÜSSEN zeitnah alarmiert werden.

# **INF.2.A17 Einsatz einer Brandfrüherkennung (B) [Planende, Haustechnik]**

Ein Rechenzentrum MUSS mit einer Brandfrüherkennungsanlage ausgestattet werden. Ein Serverraum SOLLTE mit einer Brandfrüherkennungsanlage ausgestattet werden. Die Meldungen der Brandfrüherkennung MÜSSEN an eine ständig besetzte Stelle geleitet werden, die eine Kontrolle und Schutzreaktion innerhalb von maximal 3 Minuten veranlassen kann. Alternativ MUSS eine automatische Schutzreaktion erfolgen. Um ein ausgewogenes Verhältnis zwischen Brandschutz und Verfügbarkeit zu erreichen, MUSS sichergestellt werden, dass sich einander Redundanz gebende Einrichtungen nicht gemeinsam im Wirkungsbereich der gleichen Spannungsfreischaltung befinden.

## **INF.2.A29 Vermeidung und Überwachung nicht erforderlicher Leitungen (B) [Haustechnik, Planende]**

In einem Rechenzentrum DÜRFEN NUR Leitungen verlegt werden, die der unmittelbaren Versorgung der im Rechenzentrum aufgebauten Technik (in der Regel IT- und gegebenenfalls Kühltechnik) dienen. Ist es aus baulichen Gründen unabwendbar, Leitungen durch das Rechenzentrum zu führen, um andere Bereiche als die des Rechenzentrums zu versorgen, MUSS dies einschließlich Begründung dokumentiert werden. Die Risiken, die von solchen Leitungen ausgehen, MÜSSEN durch geeignete Maßnahmen minimiert werden, z. B. durch Einhausung und Überwachung.

Durch Serverräume dürfen vorgenannte Leitungen geführt werden, ohne zu begründen, warum dies unabwendbar ist, diese MÜSSEN aber genauso behandelt werden, wie für das Rechenzentrum beschrieben.

Meldungen aus der Überwachung der Leitungen MÜSSEN unverzüglich hinsichtlich der Gefährdungsrelevanz geprüft und bewertet werden. Gegenmaßnahmen MÜSSEN entsprechend der erkannten Gefährdungsrelevanz zeitgerecht umgesetzt werden (siehe auch INF.2.A13 *Planung und Installation von Gefahrenmeldeanlagen)*.

# **3.2. Standard-Anforderungen**

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik für diesen Baustein. Sie SOLLTEN grundsätzlich erfüllt werden.

## **INF.2.A12 Perimeterschutz für das Rechenzentrum (S) [Planende, Haustechnik]**

Für Rechenzentren SOLLTE ein Perimeterschutz existieren. Je nach festgelegtem Schutzbedarf für das Rechenzentrum und abhängig vom Gelände SOLLTE der Perimeterschutz aus folgenden Komponenten bestehen:

- äußere Umschließung oder Umfriedung,
- Sicherungsmaßnahmen gegen unbeabsichtigtes Überschreiten einer Grundstücksgrenze,
- Sicherungsmaßnahmen gegen beabsichtigtes gewaltloses Überwinden der Grundstücksgrenze,
- Sicherungsmaßnahmen gegen beabsichtigtes gewaltsames Überwinden der Grundstücksgrenze,
- Freiland-Sicherungsmaßnahmen,
- äußere Personen- und Fahrzeugdetektion,
- Maßnahmen zur Beweissicherung (beispielsweise Videoaufzeichnung) sowie
- automatische Alarmierung.

## **INF.2.A13 Planung und Installation von Gefahrenmeldeanlagen (S) [Haustechnik]**

Basierend auf dem Sicherheitskonzept des Gebäudes SOLLTE geplant werden, welche Gefahrenmeldeanlagen für welche Bereiche des Rechenzentrums benötigt und installiert werden. Hierüber hinaus SOLLTE festgelegt werden, wie mit Alarmmeldungen umzugehen ist. Das Konzept SOLLTE immer angepasst werden, wenn sich die Nutzung der Gebäudebereiche verändert.

Es SOLLTE eine zum jeweiligen Einsatzzweck passende Gefahrenmeldeanlage (GMA) installiert werden. Die Meldungen der GMA SOLLTEN unter Beachtung der dafür geltenden Technischen Anschlussbedingungen (TAB) auf eine Alarmempfangsstelle aufgeschaltet werden. Die ausgewählte Alarmempfangsstelle MUSS jederzeit erreichbar sein. Sie MUSS technisch sowie personell in der Lage sein, geeignet auf die gemeldete Gefährdung zu reagieren. Der Übertragungsweg zwischen eingesetzter GMA und Alarmempfangsstelle SOLLTE entsprechend den TAB und nach Möglichkeit redundant ausgelegt werden. Alle vorhandenen Übertragungswege MÜSSEN regelmäßig getestet werden.

#### **INF.2.A14 Einsatz einer Netzersatzanlage (S) [Planende, Haustechnik]**

Die Energieversorgung eines Rechenzentrums aus dem Netz eines Energieversorgungsunternehmens SOLLTE um eine Netzersatzanlage (NEA) ergänzt werden. Wird eine NEA verwendet, MUSS sie regelmäßig gewartet werden. Bei diesen Wartungen MÜSSEN auch Belastungs- und Funktionstests sowie Testläufe unter Last durchgeführt werden.

Der Betriebsmittelvorrat einer NEA MUSS regelmäßig daraufhin überprüft werden, ob er ausreichend ist. Außerdem MUSS regelmäßig kontrolliert werden, ob die Vorräte noch verwendbar sind, vor allem um die sogenannte Dieselpest zu vermeiden. Nach Möglichkeit SOLLTE statt Diesel-Kraftstoff schwefelarmes Heizöl verwendet werden. Die Tankvorgänge von Brennstoffen MÜSSEN protokolliert werden. Aus dem Protokoll MUSS die Art des Brennstoffs, die genutzten Additive, das Tankdatum und die getankte Menge hervorgehen.

Wenn für einen Serverraum auf den Einsatz einer NEA verzichtet wird, SOLLTE alternativ zur NEA eine USV mit einer dem Schutzbedarf angemessenen Autonomiezeit realisiert werden.

## **INF.2.A15 Überspannungsschutzeinrichtung (S) [Planende, Haustechnik]**

Es SOLLTE auf Basis der aktuell gültigen Norm (DIN EN 62305 Teil 1 bis 4) ein Blitz- und Überspannungsschutzkonzept erstellt werden. Dabei sind die für den ordnungsgemäßen Betrieb des RZ erforderlichen Blitzschutzzonen (LPZ) festzulegen. Für alle für den ordnungsgemäßen Betreib des RZ und dessen Dienstleistungsbereitstellung erforderlichen Einrichtungen SOLLTE das mindestens die LPZ 2 sein. Alle Einrichtungen des Überspannungsschutzes SOLLTEN gemäß DIN EN 62305-3, Tabelle E.2 ein Mal im Jahr einer Umfassenden Prüfung unterzogen werden.

#### **INF.2.A16 Klimatisierung im Rechenzentrum (S) [Planende]**

Es SOLLTE sichergestellt werden, dass im Rechenzentrum geeignete klimatische Bedingungen geschaffen und aufrechterhalten werden. Die Klimatisierung SOLLTE für das Rechenzentrum ausreichend dimensioniert sein. Alle relevanten Werte SOLLTEN ständig überwacht werden. Weicht ein Wert von der Norm ab, SOLLTE automatisch alarmiert werden.

Die Klimaanlagen SOLLTEN in IT-Betriebsbereichen möglichst ausfallsicher sein.

#### **INF.2.A18 ENTFALLEN (S)**

Diese Anforderung ist entfallen.

#### **INF.2.A19 Durchführung von Funktionstests der technischen Infrastruktur (S) [Haustechnik]**

Die technische Infrastruktur eines Rechenzentrums SOLLTE regelmäßig (zumindest ein- bis zweimal jährlich) sowie nach Systemumbauten und umfangreichen Reparaturen getestet werden. Die Ergebnisse SOLLTEN dokumentiert werden. Besonders ganze Reaktionsketten SOLLTEN einem echten Funktionstest unterzogen werden.

#### **INF.2.A20 ENTFALLEN (S)**

Diese Anforderung ist entfallen.

## **INF.2.A30 Anlagen zur, Löschung oder Vermeidung von Bränden (S) [Haustechnik, Planende]**

Ein Rechenzentrum SOLLTE mit einer automatischen Lösch- oder Brandvermeidungsanlage ausgestattet werden.

# **3.3. Anforderungen bei erhöhtem Schutzbedarf**

Im Folgenden sind für diesen Baustein exemplarische Vorschläge für Anforderungen aufgeführt, die über dasjenige Schutzniveau hinausgehen, das dem Stand der Technik entspricht. Die Vorschläge SOLLTEN bei erhöhtem Schutzbedarf in Betracht gezogen werden. Die konkrete Festlegung erfolgt im Rahmen einer individuellen Risikoanalyse.

# **INF.2.A21 Ausweichrechenzentrum (H)**

Es SOLLTE ein geografisch separiertes Ausweichrechenzentrum aufgebaut werden. Das Ausweichrechenzentrum SOLLTE so dimensioniert sein, dass alle Prozesse der Institution aufrechterhalten werden können. Auch SOLLTE es ständig einsatzbereit sein. Alle Daten der Institution SOLLTEN regelmäßig ins Ausweichrechenzentrum gespiegelt werden. Der Schwenk auf das Notfallrechenzentrum SOLLTE regelmäßig getestet und geübt werden. Die Übertragungswege in das Ausweichrechenzentrum SOLLTEN geeignet abgesichert und entsprechend redundant ausgelegt sein.

# **INF.2.A22 Durchführung von Staubschutzmaßnahmen (H) [Haustechnik]**

Bei Baumaßnahmen in einem Rechenzentrum SOLLTEN geeignete Staubschutzmaßnahmen definiert, geplant und umgesetzt werden. Personen, die selbst nicht an den Baumaßnahmen beteiligt sind, SOLLTEN in ausreichend engen Zeitabständen kontrollieren, ob die Staubschutzmaßnahmen ordnungsgemäß funktionieren und die Regelungen zum Staubschutz eingehalten werden.

#### **INF.2.A23 Zweckmäßiger Aufbau der Verkabelung im Rechenzentrum (H) [Haustechnik]**

Kabeltrassen in Rechenzentren SOLLTEN sorgfältig geplant und ausgeführt werden. Trassen SOLLTEN hinsichtlich Anordnung und Dimensionierung so ausgelegt sein, dass eine Trennung der Spannungsebenen sowie eine sinnvolle Verteilung von Kabeln auf den Trassen möglich ist und dass auch für zukünftige Bedarfsmehrung ausreichend Platz zur Verfügung steht. Zur optimalen Versorgung von IT-Hardware, die über zwei Netzteile verfügt, SOLLTE ab der Niederspannungshauptverteilung für die IT-Betriebsbereiche eine zweizügige sogenannte A-B-Versorgung aufgebaut werden. Einander Redundanz gebende Leitungen SOLLTEN über getrennte Trassen verlegt werden.

## **INF.2.A24 Einsatz von Videoüberwachungsanlagen (H) [Datenschutzbeauftragte, Haustechnik, Planende]**

Die Zutrittskontrolle und die Einbruchmeldung SOLLTEN durch Videoüberwachungsanlagen ergänzt werden. Eine Videoüberwachung SOLLTE in das gesamte Sicherheitskonzept eingebettet werden. Bei der Planung, Konzeption und eventuellen Auswertung von Videoaufzeichnungen MUSS der Datenschutzbeauftragte immer mit einbezogen werden.

Die für eine Videoüberwachung benötigten zentralen Technikkomponenten SOLLTEN in einer geeigneten Umgebung geschützt aufgestellt werden. Es SOLLTE regelmäßig überprüft werden, ob die Videoüberwachungsanlage korrekt funktioniert und ob die mit dem oder der Datenschutzbeauftragten abgestimmten Blickwinkel eingehalten werden.

#### **INF.2.A25 Redundante Auslegung von unterbrechungsfreien Stromversorgungen (H) [Planende]**

USV-Systeme SOLLTEN modular und so aufgebaut sein, dass der Ausfall durch ein redundantes Modul unterbrechungsfrei kompensiert wird. Sofern für die IT-Betriebsbereiche eine zweizügige sogenannte A-B-Versorgung aufgebaut ist, SOLLTE jeder der beiden Strompfade mit einem eigenständigen USV-System ausgestattet sein.

#### **INF.2.A26 Redundante Auslegung von Netzersatzanlagen (H) [Planende]**

Netzersatzanlagen SOLLTEN redundant ausgelegt werden. Hinsichtlich der Wartung MÜSSEN auch redundante NEAs entsprechend INF.2.A14 *Einsatz einer Netzersatzanlage* behandelt werden.

#### **INF.2.A27 ENTFALLEN (H)**

Diese Anforderung ist entfallen.

#### **INF.2.A28 Einsatz von höherwertigen Gefahrenmeldeanlagen (H) [Planende]**

Für Rechenzentrumsbereiche mit erhöhtem Schutzbedarf SOLLTEN ausschließlich Gefahrenmeldeanlagen der VdS-Klasse C (gemäß VDS-Richtlinie 2311) eingesetzt werden.

# **4. Weiterführende Informationen**

# **4.1. Wissenswertes**

Das BSI stellt unter https://www.bsi.bund.de/dok/RZ-Sicherheit unter anderem Dokumente zu "Rechenzentrums-Definition", "Standort-Kriterien für Rechenzentren", "Verfügbarkeitsmaßnahmen für Rechenzentren", "Redundanz - Modularität - Skalierbarkeit" und "Brennstofflagerung für Netzersatzanlagen" zur Verfügung.

Das Deutsche Institut für Normung e. V. (DIN) beschreibt in der Norm "DIN EN 50600-1:2019-08 Informationstechnik - Einrichtungen und Infrastrukturen von Rechenzentren: Teil 1: Allgemeine Konzepte", allgemeine Prinzipien zur Auslegung von Rechenzentren.

Das Deutsche Institut für Normung e. V. (DIN) behandelt in der Norm "DIN EN 62305-4:2011-10 Blitzschutz: Teil 4: Elektrische und elektronische Systeme in baulichen Anlagen", das Thema Blitzschutz.

Der Bundesverband Informationswirtschaft, Telekommunikation und neue Medien e. V. (Bitkom) gibt in seinem Leitfaden "Betriebssicheres Rechenzentrum", Hilfestellung zu Planung und Aufbau eines Rechenzentrums.

Der Gesamtverband der Deutschen Versicherungswirtschaft e. V. (GDV) beschreibt in seiner Publikation "Sicherungsleitfaden Perimeter", Perimetersicherungsmaßnahmen, die als Hilfestellung zur Objektabsicherung herangezogen werden können.
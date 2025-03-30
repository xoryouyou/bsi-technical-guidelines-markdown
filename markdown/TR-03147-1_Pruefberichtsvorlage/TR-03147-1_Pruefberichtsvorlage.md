![](_page_0_Picture_0.jpeg)

# Prüfberichtsvorlage zur Prüfung von Identifikationsverfahren gemäß TR-03147 in Version 1.0.6

Version 1.0.0 28.12.2021

![](_page_0_Picture_4.jpeg)

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn Tel.: +49 22899 9582-0 E-Mail: eid@bsi.bund.de Internet: https://www.bsi.bund.de © Bundesamt für Sicherheit in der Informationstechnik 2021

| 1    | Einleitung 7                                                                                                             |  |
|------|--------------------------------------------------------------------------------------------------------------------------|--|
| 1.1  | Übersicht 7                                                                                                              |  |
| 1.2  | Begutachtungsgegenstand 8                                                                                                |  |
| 1.3  | Werkzeuge 8                                                                                                              |  |
| 1.4  | Beteiligte Personen und Stellen 8                                                                                        |  |
| 2    | Übersicht der Anforderungen und Ergebnisse 9                                                                             |  |
| 3    | Vertrauenswürdige ID-Dokumente 13                                                                                        |  |
| 3.1  | Relevanz 13                                                                                                              |  |
| 3.2  | Mehrere zugelassene ID-Dokumente 13                                                                                      |  |
| 3.3  | Gültiges ID-Dokument 13                                                                                                  |  |
| 3.4  | Verlässliche Quelle 14                                                                                                   |  |
| 3.5  | Enthält eine hinreichende Menge an ID-Attributen17                                                                       |  |
| 3.6  | Manipulations- und fälschungssicher17                                                                                    |  |
| 3.7  | Sicherheitsmerkmale sind bekannt und effektiv überprüfbar18                                                              |  |
| 3.8  | Ermöglicht einen zuverlässigen Abgleich mit dem Verwender18                                                              |  |
| 3.9  | ID-Attribute sind aktuell 19                                                                                             |  |
| 3.10 | Verfügbare Sperrmeldungen werden überprüft19                                                                             |  |
| 3.11 | Regelmäßige Prüfung der Menge der zulässigen ID-Dokumente20                                                              |  |
| 4    | Sicherheit der Übertragungskanäle 22                                                                                     |  |
| 4.1  | Relevanz 22                                                                                                              |  |
| 4.2  | Video-/Informationstechnische Manipulationen biometrischer Daten der zu identifizierenden<br>Person werden erkannt 22    |  |
| 4.3  | Informationstechnische Manipulationen vom ID-Dokument übertragener Informationen werden<br>erkannt 22                    |  |
| 4.4  | Physikalische Manipulationen biometrischer Charakteristika der zu identifizierenden Person<br>werden erkannt 23          |  |
| 4.5  | Physikalische Manipulationen am ID-Dokument werden erkannt23                                                             |  |
| 4.6  | Liveübertragung sämtlicher Daten ist gewährleistet24                                                                     |  |
| 4.7  | Ein Austausch des präsentierten ID-Dokuments oder der zu identifizierenden Person während der<br>Prüfung wird erkannt 24 |  |
| 5    | Prüfung der ID-Nachweise 26                                                                                              |  |
| 5.1  | Relevanz 26                                                                                                              |  |
| 5.2  | Mehrere ID-Nachweise 26                                                                                                  |  |
| 5.3  | Typ des verwendeten ID-Dokuments lässt sich ermitteln26                                                                  |  |
| 5.4  | ID-Dokument ist gültig 27                                                                                                |  |
| 5.5  | Gefälschte Sicherheitsmerkmale werden erkannt27                                                                          |  |
| 5.6  | Fälschungen der personalisierten Daten werden erkannt28                                                                  |  |
| 6    | Abgleich von Personen mit ID-Nachweisen 29                                                                               |  |
| 6.1  | Vertrauliche Wissensfaktoren werden ausschließlich dem legitimen Inhaber mitgeteilt29                                    |  |
| 6.2  | Sicherheit der verwendeten Authentisierungsmittel29                                                                      |  |

| 6.3 | Die tatsächliche Verfügungsgewalt der zu identifizierenden Person über das ID-Dokument wird<br>sichergestellt 29        |  |
|-----|-------------------------------------------------------------------------------------------------------------------------|--|
| 6.4 | Abzugleichende ID-Attribute werden in hinreichender Qualität erfasst30                                                  |  |
| 6.5 | Zuverlässiger Abgleich relevanter biometrischer ID-Attribute zwischen ID-Dokument und zu<br>identifizierender Person 31 |  |
| 7   | Korrekte Erfassung der benötigten ID-Attribute32                                                                        |  |
| 7.1 | Relevanz 32                                                                                                             |  |
| 7.2 | Zu erfassende ID-Attribute erlauben eine eindeutige Identifizierung32                                                   |  |
| 7.3 | Spezifische Sachkenntnis der Prüfer und ggf. zu verwendende Hilfsmittel sind vorhanden32                                |  |
| 7.4 | ID-Attribute werden vollständig und fehlerfrei in das Erfassungssystem übertragen33                                     |  |
| 7.5 | Erfasste Daten werden auf Aktualität, Konsistenz und Plausibilität geprüft34                                            |  |
| 8   | Sicherung der Integrität der Prozesse 35                                                                                |  |
| 8.1 | Relevanz 35                                                                                                             |  |
| 8.2 | Die Einhaltung der vorgeschriebenen Prüfkriterien ist sichergestellt35                                                  |  |
| 8.3 | ISMS 36                                                                                                                 |  |
| 9   | Übergreifende Angriffsszenarien gegen ID-Verfahren38                                                                    |  |
| 9.1 | Relevanz 38                                                                                                             |  |
| 9.2 | Globale Angriffsszenarien 38                                                                                            |  |
|     | Literaturverzeichnis 39                                                                                                 |  |

### <span id="page-5-0"></span>1 Einleitung

Die Technische Richtlinie TR-03147 [TR-03147] beschreibt Bedrohungen und Anforderungen für Verfahren zur (initialen) Identitätsprüfung natürlicher Personen anhand von ID-Dokumenten wie z.B. dem Personalausweis (PA) oder Reisepass (RP). Die [TR-03147] ermöglicht es, eine Einstufung verschiedener ID-Verfahren hinsichtlich ihres Vertrauensniveaus ("normal", "substantiell" oder "hoch") vorzunehmen und diese somit hinsichtlich ihrer Sicherheit zu vergleichen. Mit der [TR-03147] steht insbesondere eine Grundlage zur systematischen und fundierten Bewertung von Vertrauensniveaus von ID-Verfahren zur Verfügung.

Beispiele für solche ID-Verfahren sind

- "Videoidentifizierungsverfahren",
- "Photoidentifizierungsverfahren",
- Verfahren mit unmittelbarer Anwesenheit der zu identifizierenden Person sowie einer prüfenden Person und
- Verfahren, die auf der Anwendung der Online-Ausweisfunktion des deutschen Personalausweises (PA), der eID-Karte für Bürgerinnen und Bürger der EU und des EWR (eID-Karte) oder des elektronischen Aufenthaltstitels (eAT) basieren.

Das vorliegende Dokument ist die Prüfberichtsvorlage (Template), die für eine Bewertung des Vertrauensniveaus eines ID-Verfahrens anhand der [TR-03147] zu verwenden ist. Dabei sind die in der TR gestellten Anforderungen in einzelne, atomare Prüfkriterien aufgeteilt, um eine systematische Prüfung zu unterstützen und eine Reproduzierbarkeit von Ergebnissen unterschiedlicher Prüfer bestmöglich zu dokumentieren und zu gewährleisten. Das gesamte Ergebnis zu einer Anforderung der TR und letztendlich dem gesamten Verfahren leitet sich dann ab aus den Bewertungen der einzelnen Prüfkriterien unter Anwendung des Minimumprinzips (Abweichungen hiervon werden explizit erwähnt).

Ergänzt wird die Prüfberichtsvorlage durch den zugehörigen Anforderungskatalog [AnfKat], der für den Prüfer für jedes Prüfkriterium eine Leitlinie für seine vorzunehmende Bewertung gibt und grundsätzlich erläutert, wie die Prüfberichtsvorlage zu verwenden ist.

Die vorliegende Prüfberichtsvorlage enthält in den weiteren Abschnitten dieses Kapitels ([1.1](#page-5-1) bis [1.4](#page-6-0)) allgemeine Informationen zum Verfahren und zur Prüfung, die durch den Prüfer bzw. das prüfende Unternehmen anzugeben sind.

In Kapitel [2](#page-7-0) sollen die erzielten Ergebnisse in tabellarischer Form zusammengefasst werden. Sofern Anforderungen aus dieser Prüfberichtsvorlage für ein konkretes Verfahren nicht relevant sind und deshalb nicht geprüft werden, so sind sie dennoch im Prüfbericht als nicht anwendbar aufzuführen.

In den Kapiteln [3](#page-11-0) bis [8](#page-33-0) werden die einzelnen, aus den Anforderungen der [TR-03147] abgeleiteten Prüfkriterien aufgeführt. Diese sind durch den Prüfer zu bearbeiten und die zugehörigen Tabelleneinträge sind geeignet auszufüllen. Die Gliederung der Prüfberichtsvorlage sowie auch die des Anforderungskatalogs folgen der Gliederung der TR, um eine parallele Handhabung dieser Dokumente so gut wie möglich zu unterstützen.

#### <span id="page-5-1"></span>1.1 Übersicht

| Begutachter:                         |  |
|--------------------------------------|--|
| Name des Verfahrens:                 |  |
| Versionsnummer:                      |  |
| Anbieter / Betreiber des Verfahrens: |  |

1 Einleitung

| Kategorie des Verfahrens                | <direkt>   <indirekt>   <elektronisch> |
|-----------------------------------------|----------------------------------------|
| Begutachtungszeitraum:                  | vom TT.MM.JJJJ bis zum TT.MM.JJJJ      |
| Begutachtungsgrundlage:                 | [TR-03147]<br>[AnfKat]                 |
| Gültigkeitszeitraum:                    |                                        |
| Ergebnis der Vertrauensniveaubewertung: |                                        |

#### 1.2 Begutachtungsgegenstand

Das Funktionsprinzip des zu begutachtenden Verfahrens sowie dessen Anwendungskontext sind kurz zu beschreiben. An dieser Stelle ist auch der Begutachtungsgegenstand genau zu definieren. Er ist eindeutig von seiner Umgebung abzugrenzen, die für den Betrieb notwendig ist, jedoch nicht Teil der Begutachtung ist. Auch in welcher Form der Begutachtungsgegenstand vom Anbieter bereitgestellt wird, ist an dieser Stelle zu erläutern, ebenso wie eventuelle Zusatzmaterialien und Dokumentation. Alle Objekte müssen eindeutig identifizierbar sein.

#### 1.3 Werkzeuge

Es sind alle zur Begutachtung verwendeten Werkzeuge eindeutig zu identifizieren (Hard- und Software). Handelt es sich um nicht-kommerziell oder frei erhältliche Produkte, so ist dies explizit zu erwähnen.

| Ref. | Bezeichnung | Hersteller | Lizenz | Beschreibung des Werkzeugs |
|------|-------------|------------|--------|----------------------------|
|      |             |            |        |                            |
|      |             |            |        |                            |
|      |             |            |        |                            |
|      |             |            |        |                            |

#### <span id="page-6-0"></span>1.4 Beteiligte Personen und Stellen

Alle an der Begutachtung beteiligte Personen (inklusive der Kontaktpersonen des Herstellers eines Verfahrens) sind namentlich zu nennen, zusammen mit Angabe der übernommenen Aufgaben.

| Ref. | Name | Firma | Titel/Funktion/Aufgabe |
|------|------|-------|------------------------|
|      |      |       |                        |
|      |      |       |                        |
|      |      |       |                        |
|      |      |       |                        |

### <span id="page-7-0"></span>2 Übersicht der Anforderungen und Ergebnisse

| ID   | Anforderung                                                                              | Ergebnis |
|------|------------------------------------------------------------------------------------------|----------|
| A1   | Vertrauenswürdige ID-Dokumente<br>Kapitel 4 in [TR-03147]                                |          |
|      | A1.G-1                                                                                   |          |
|      | A1.G-2                                                                                   |          |
| A1.1 | Verlässliche Quelle<br>Kapitel 4.2.1 in [TR-03147]                                       |          |
|      | A1.1-1                                                                                   |          |
|      | A1.1-2                                                                                   |          |
|      | A1.1-3                                                                                   |          |
|      | A1.1-4                                                                                   |          |
|      | A1.1-5                                                                                   |          |
|      | A1.1-6                                                                                   |          |
|      | A1.1-7                                                                                   |          |
|      | A1.1-8                                                                                   |          |
|      | A1.1-9                                                                                   |          |
|      | A1.1-10                                                                                  |          |
| A1.2 | Enthält eine hinreichende Menge an ID-Attributen<br>Kapitel 4.2.2 in [TR-03147]          |          |
|      | A1.2-1                                                                                   |          |
|      | A1.2-2                                                                                   |          |
| A1.3 | Manipulations- und fälschungssicher<br>Kapitel 4.2.3 in [TR-03147]                       |          |
|      | A1.3-1                                                                                   |          |
|      | A1.3-2                                                                                   |          |
| A1.4 | Sicherheitsmerkmale sind bekannt und effektiv überprüfbar<br>Kapitel 4.2.4 in [TR-03147] |          |
|      | A1.4-1                                                                                   |          |
| A1.5 | Ermöglicht einen zuverlässigen Abgleich mit dem Verwender<br>Kapitel 4.2.5 in [TR-03147] |          |
|      | A1.5-1                                                                                   |          |
|      | A1.5-2                                                                                   |          |
| A1.6 | ID-Attribute sind aktuell<br>Kapitel 4.2.6 in [TR-03147]                                 |          |
|      | A1.6-1                                                                                   |          |
| A1.7 | Verfügbare Sperrmeldungen werden überprüft<br>Kapitel 4.2.7 in [TR-03147]                |          |

| ID   | Anforderung                                                                                                                                          | Ergebnis |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
|      | A1.7-1                                                                                                                                               |          |
|      | A1.7-2                                                                                                                                               |          |
| A1.8 | Regelmäßige Prüfung der Menge der zulässigen ID-Dokumente<br>Kapitel 4.2.8 in [TR-03147]                                                             |          |
|      | A1.8-1                                                                                                                                               |          |
|      | A1.8-2                                                                                                                                               |          |
| A2   | Sicherheit der Übertragungskanäle<br>Kapitel 5 in [TR-03147]                                                                                         |          |
| A2.1 | Video-/Informationstechnische Manipulationen biometrischer Daten<br>der zu identifizierenden Person werden erkannt<br>Kapitel 5.2.1 in [TR-03147]    |          |
|      | A2.1-1                                                                                                                                               |          |
| A2.2 | Informationstechnische<br>Manipulationen<br>vom<br>ID-Dokument<br>übertragener Informationen werden erkannt<br>Kapitel 5.2.2 in [TR-03147]           |          |
|      | A2.2-1                                                                                                                                               |          |
|      | A2.2-2                                                                                                                                               |          |
| A2.3 | Physikalische Manipulationen biometrischer Charakteristika der zu<br>identifizierenden Person werden erkannt<br>Kapitel 5.2.3 in [TR-03147]          |          |
|      | A2.3-1                                                                                                                                               |          |
| A2.4 | Physikalische Manipulationen am präsentierten ID-Dokument werden<br>erkannt<br>Kapitel 5.2.4 in [TR-03147]                                           |          |
|      | A2.4-1                                                                                                                                               |          |
| A2.5 | Liveübertragung sämtlicher Daten ist gewährleistet<br>Kapitel 5.2.5 in [TR-03147]                                                                    |          |
|      | A2.5-1                                                                                                                                               |          |
| A2.6 | Ein Austausch des präsentierten ID-Dokuments oder der zu<br>identifizierenden Person während der Prüfung wird erkannt<br>Kapitel 5.2.6 in [TR-03147] |          |
|      | A2.6-1                                                                                                                                               |          |
| A3   | Prüfung der ID-Nachweise<br>Kapitel 6 in [TR-03147]                                                                                                  |          |
|      | A3.G-1                                                                                                                                               |          |
| A3.1 | Typ des verwendeten ID-Dokuments lässt sich ermitteln<br>Kapitel 6.4.1 in [TR-03147]                                                                 |          |
|      | A3.1-1                                                                                                                                               |          |
| A3.2 | ID-Dokument ist gültig<br>Kapitel 6.4.2 in [TR-03147]                                                                                                |          |
|      | A3.2-1                                                                                                                                               |          |

| ID   | Anforderung                                                                                                                                         | Ergebnis |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| A3.3 | Gefälschte Sicherheitsmerkmale werden erkannt<br>Kapitel 6.4.3 in [TR-03147]                                                                        |          |
|      | A3.3-1                                                                                                                                              |          |
|      | A3.3-2                                                                                                                                              |          |
| A3.4 | Fälschungen der personalisierten Daten werden erkannt<br>Kapitel 6.4.4 in [TR-03147]                                                                |          |
|      | A3.4-1                                                                                                                                              |          |
|      | A3.4-2                                                                                                                                              |          |
| A4   | Zuverlässiger Abgleich zwischen der zu identifizierenden Person und<br>dem ID-Dokument (Integrität des ID-Nachweises)<br>Kapitel 7 in [TR-03147]    |          |
| A4.1 | Vertrauliche Wissensfaktoren werden ausschließlich dem legitimen<br>Inhaber mitgeteilt<br>Kapitel 7.2.1 in [TR-03147]                               |          |
|      | A4.1-1                                                                                                                                              |          |
| A4.2 | Sicherheit der verwendeten Authentisierungsmittel<br>Kapitel 7.2.2 in [TR-03147]                                                                    |          |
|      | A4.2-1                                                                                                                                              |          |
| A4.3 | Die tatsächliche Verfügungsgewalt der zu identifizierenden Person über<br>das ID-Dokument ist sichergestellt<br>Kapitel 7.2.3 in [TR-03147]         |          |
|      | A4.3-1                                                                                                                                              |          |
| A4.4 | Abzugleichende ID-Attribute werden in hinreichender Qualität erfasst<br>Kapitel 7.2.4 in [TR-03147]                                                 |          |
|      | A4.4-1                                                                                                                                              |          |
|      | A4.4-2                                                                                                                                              |          |
| A4.5 | Zuverlässiger Abgleich relevanter biometrischer ID-Attribute zwischen<br>ID-Dokument und zu identifizierender Person<br>Kapitel 7.2.5 in [TR-03147] |          |
|      | A4.5-1                                                                                                                                              |          |
| A5   | Korrekte Erfassung der benötigten ID-Attribute<br>Kapitel 8 in [TR-03147]                                                                           |          |
| A5.1 | Zu erfassende ID-Attribute erlauben eine eindeutige Identifizierung<br>Kapitel 8.2.1 in [TR-03147]                                                  |          |
|      | A5.1-1                                                                                                                                              |          |
| A5.2 | Spezifische Sachkenntnis der Prüfer und ggf. zu verwendende<br>Hilfsmittel sind vorhanden<br>Kapitel 8.2.2 in [TR-03147]                            |          |
|      | A5.2-1                                                                                                                                              |          |
|      | A5.2-2                                                                                                                                              |          |
| A5.3 | ID-Attribute werden vollständig und fehlerfrei in das Erfassungssystem                                                                              |          |

| ID   | Anforderung                                                                                                  | Ergebnis |
|------|--------------------------------------------------------------------------------------------------------------|----------|
|      | übertragen<br>Kapitel 8.2.3 in [TR-03147]                                                                    |          |
|      | A5.3-1                                                                                                       |          |
|      | A5.3-2                                                                                                       |          |
| A5.4 | Erfasste Daten werden auf Aktualität, Konsistenz und Plausibilität<br>geprüft<br>Kapitel 8.2.4 in [TR-03147] |          |
|      | A5.4-1                                                                                                       |          |
|      | A5.4-2                                                                                                       |          |
|      | A5.4-3                                                                                                       |          |
| A6   | Sicherung der Integrität aller Prozessschritte<br>Kapitel 9 in [TR-03147]                                    |          |
| A6.1 | Die Einhaltung der vorgeschriebenen Prüfkriterien ist sichergestellt<br>Kapitel 9.2.1 in [TR-03147]          |          |
|      | A6.1-1                                                                                                       |          |
|      | A6.1-2                                                                                                       |          |
|      | A6.1-3                                                                                                       |          |
|      | A6.1-4                                                                                                       |          |
|      | A6.1-5                                                                                                       |          |
| A6.2 | ISMS<br>Kapitel 9.2.2 in [TR-03147]                                                                          |          |
|      | A6.2-1                                                                                                       |          |
| A7.G | Globale Angriffsszenarien<br>ergänzend zur [TR-03147]                                                        |          |
|      | A7.G-1                                                                                                       |          |

### <span id="page-11-0"></span>3 Vertrauenswürdige ID-Dokumente

#### 3.1 Relevanz

| Schutzziele:                   | Existenz<br>Legitimität                                                                                                                                                                                                                  |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Beispiele für Verfahrenstypen: | "VideoIdent"<br>"PhotoIdent"<br>Verfahren mit unmittelbarer Anwesenheit ("vor-Ort" Identifizierung z.B.<br>in einer Filiale, einschließlich "Vor-Ort-Auslesen" des PA oder eAT )<br>Verfahren mit Online-Ausweisfunktion des PA oder eAT |

#### 3.2 Mehrere zugelassene ID-Dokumente

<span id="page-11-2"></span>

| PrüfKrit-ID               | A1.G-1                                                                                                                                         |        |      |     |               |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|
| PrüfKrit<br>Beschreibung: | Wie lautet das Vertrauensniveau desjenigen für das ID-Verfahren zugelassenen ID<br>Dokuments, welches das niedrigste Vertrauensniveau besitzt? |        |      |     |               |
| Referenz                  | Kapitel 4                                                                                                                                      |        |      |     |               |
| Prüfaktivität:            | Bestimmung des Vertrauensniveaus über alle ID-Dokumente gemäß dem<br>Minimumprinzip.                                                           |        |      |     |               |
| Analyse:                  |                                                                                                                                                |        |      |     |               |
| Bewertung:                | Normal                                                                                                                                         | Subst. | Hoch | N/A | Nicht erfüllt |
|                           |                                                                                                                                                |        |      |     |               |

#### 3.3 Gültiges ID-Dokument

<span id="page-11-1"></span>

| PrüfKrit-ID               | A1.G-2                                                                                                                     |        |      |     |               |  |  |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|--|--|
| PrüfKrit<br>Beschreibung: | Wird bei der Anwendung des ID-Verfahrens überprüft, ob das verwendete ID<br>Dokument zum Zeitpunkt der Prüfung gültig ist? |        |      |     |               |  |  |
| Referenz                  | Kapitel 4.2                                                                                                                |        |      |     |               |  |  |
| Dokumentation:            |                                                                                                                            |        |      |     |               |  |  |
| Interviewpartner:         |                                                                                                                            |        |      |     |               |  |  |
| Prüfaktivität:            |                                                                                                                            |        |      |     |               |  |  |
| Analyse:                  |                                                                                                                            |        |      |     |               |  |  |
| Bewertung:                | Normal                                                                                                                     | Subst. | Hoch | N/A | Nicht erfüllt |  |  |
|                           |                                                                                                                            |        |      |     |               |  |  |

#### 3.4 Verlässliche Quelle

<span id="page-12-2"></span>

| PrüfKrit-ID               | A1.1-1                                                                                        |        |      |     |               |  |
|---------------------------|-----------------------------------------------------------------------------------------------|--------|------|-----|---------------|--|
| PrüfKrit<br>Beschreibung: | Sind die für die Ausstellung des jeweiligen ID-Dokuments verantwortlichen Stellen<br>bekannt? |        |      |     |               |  |
| Referenz                  | Kapitel 4.2.1                                                                                 |        |      |     |               |  |
| Dokumentation:            |                                                                                               |        |      |     |               |  |
| Interviewpartner:         |                                                                                               |        |      |     |               |  |
| Prüfaktivität:            |                                                                                               |        |      |     |               |  |
| Analyse:                  |                                                                                               |        |      |     |               |  |
| Bewertung:                | Normal                                                                                        | Subst. | Hoch | N/A | Nicht erfüllt |  |
|                           |                                                                                               |        |      |     |               |  |

<span id="page-12-1"></span>

| PrüfKrit-ID               | A1.1-2                                                                                                                                                                               |        |      |     |               |  |  |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|--|--|
| PrüfKrit<br>Beschreibung: | Werden über die verantwortlichen Stellen öffentlich verfügbare Informationen über<br>Kompromittierungen (z.B. Medienberichte zur Kompromittierung von solchen<br>Stellen) gesammelt? |        |      |     |               |  |  |
| Referenz                  | Kapitel 4.2.1                                                                                                                                                                        |        |      |     |               |  |  |
| Dokumentation:            |                                                                                                                                                                                      |        |      |     |               |  |  |
| Interviewpartner:         |                                                                                                                                                                                      |        |      |     |               |  |  |
| Prüfaktivität:            |                                                                                                                                                                                      |        |      |     |               |  |  |
| Analyse:                  |                                                                                                                                                                                      |        |      |     |               |  |  |
| Bewertung:                | Normal                                                                                                                                                                               | Subst. | Hoch | N/A | Nicht erfüllt |  |  |
|                           |                                                                                                                                                                                      |        |      |     |               |  |  |

<span id="page-12-0"></span>

| PrüfKrit-ID               | A1.1-3                                                                                                                                                                                      |        |      |     |               |  |  |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|--|--|
| PrüfKrit<br>Beschreibung: | Werden die über die verantwortlichen Stellen gesammelten Informationen über<br>Kompromittierungen (z.B. Medienberichte zur Kompromittierung von solchen<br>Stellen) zeitnah berücksichtigt? |        |      |     |               |  |  |
| Referenz                  | Kapitel 4.2.1                                                                                                                                                                               |        |      |     |               |  |  |
| Dokumentation:            |                                                                                                                                                                                             |        |      |     |               |  |  |
| Interviewpartner:         |                                                                                                                                                                                             |        |      |     |               |  |  |
| Prüfaktivität:            |                                                                                                                                                                                             |        |      |     |               |  |  |
| Analyse:                  |                                                                                                                                                                                             |        |      |     |               |  |  |
| Bewertung:                | Normal                                                                                                                                                                                      | Subst. | Hoch | N/A | Nicht erfüllt |  |  |
|                           |                                                                                                                                                                                             |        |      |     |               |  |  |

<span id="page-13-3"></span>

| PrüfKrit-ID               | A1.1-4                |                                                                          |      |     |               |  |
|---------------------------|-----------------------|--------------------------------------------------------------------------|------|-----|---------------|--|
| PrüfKrit<br>Beschreibung: | Dokumenten gesammelt? | Werden aktuelle Informationen über Manipulationen und Fälschungen bei ID |      |     |               |  |
| Referenz                  | Kapitel 4.2.1         |                                                                          |      |     |               |  |
| Dokumentation:            |                       |                                                                          |      |     |               |  |
| Interviewpartner:         |                       |                                                                          |      |     |               |  |
| Prüfaktivität:            |                       |                                                                          |      |     |               |  |
| Analyse:                  |                       |                                                                          |      |     |               |  |
| Bewertung:                | Normal                | Subst.                                                                   | Hoch | N/A | Nicht erfüllt |  |
|                           |                       |                                                                          |      |     |               |  |

<span id="page-13-2"></span>

| PrüfKrit-ID               | A1.1-5                                                                                                                |        |      |     |               |  |  |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|--|--|
| PrüfKrit<br>Beschreibung: | Werden die gesammelten Informationen über Manipulationen und Fälschungen bei<br>ID-Dokumenten zeitnah berücksichtigt? |        |      |     |               |  |  |
| Referenz                  | Kapitel 4.2.1                                                                                                         |        |      |     |               |  |  |
| Dokumentation:            |                                                                                                                       |        |      |     |               |  |  |
| Interviewpartner:         |                                                                                                                       |        |      |     |               |  |  |
| Prüfaktivität:            |                                                                                                                       |        |      |     |               |  |  |
| Analyse:                  |                                                                                                                       |        |      |     |               |  |  |
| Bewertung:                | Normal                                                                                                                | Subst. | Hoch | N/A | Nicht erfüllt |  |  |
|                           |                                                                                                                       |        |      |     |               |  |  |

<span id="page-13-1"></span>

| PrüfKrit-ID               | A1.1-6                                                                                                                                                            |        |      |     |               |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|
| PrüfKrit<br>Beschreibung: | Wird beim Prozess der Erstellung und Aushändigung des verwendeten ID-Dokuments<br>die Berechtigung und Identität eines Antragstellers hinreichend sicher geprüft? |        |      |     |               |
| Referenz                  | Kapitel 4.2.1                                                                                                                                                     |        |      |     |               |
| Dokumentation:            |                                                                                                                                                                   |        |      |     |               |
| Interviewpartner:         |                                                                                                                                                                   |        |      |     |               |
| Prüfaktivität:            |                                                                                                                                                                   |        |      |     |               |
| Analyse:                  |                                                                                                                                                                   |        |      |     |               |
| Bewertung:                | Normal                                                                                                                                                            | Subst. | Hoch | N/A | Nicht erfüllt |
|                           |                                                                                                                                                                   |        |      |     |               |

<span id="page-13-0"></span>

| PrüfKrit-ID               | A1.1-7                                                                                                                            |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| PrüfKrit<br>Beschreibung: | Prüft das ID-Verfahren, ob das verwendete ID-Dokument zu einer explizit begrenzten<br>Menge an zugelassenen ID-Dokumenten gehört? |
| Referenz                  | Kapitel 4.2.1                                                                                                                     |

| Dokumentation:    |        |        |      |     |               |
|-------------------|--------|--------|------|-----|---------------|
| Interviewpartner: |        |        |      |     |               |
| Prüfaktivität:    |        |        |      |     |               |
| Analyse:          |        |        |      |     |               |
| Bewertung:        | Normal | Subst. | Hoch | N/A | Nicht erfüllt |
|                   |        |        |      |     |               |

<span id="page-14-2"></span>

| PrüfKrit-ID               | A1.1-8                 |        |      |                                                                    |               |
|---------------------------|------------------------|--------|------|--------------------------------------------------------------------|---------------|
| PrüfKrit<br>Beschreibung: |                        |        |      | Handelt es sich bei dem ID-Dokument um ein explizites ID-Dokument? |               |
| Referenz                  | Kapitel 4.2, Tabelle 4 |        |      |                                                                    |               |
| Dokumentation:            |                        |        |      |                                                                    |               |
| Interviewpartner:         |                        |        |      |                                                                    |               |
| Prüfaktivität:            |                        |        |      |                                                                    |               |
| Analyse:                  |                        |        |      |                                                                    |               |
| Bewertung:                | Normal                 | Subst. | Hoch | N/A                                                                | Nicht erfüllt |
|                           |                        |        |      |                                                                    |               |

<span id="page-14-1"></span>

| PrüfKrit-ID               | A1.1-9                                                |        |      |     |               |
|---------------------------|-------------------------------------------------------|--------|------|-----|---------------|
| PrüfKrit<br>Beschreibung: | Erfüllt das ID-Dokument die Ausweispflicht im Inland? |        |      |     |               |
| Referenz                  | Kapitel 4.2, Tabelle 4                                |        |      |     |               |
| Dokumentation:            |                                                       |        |      |     |               |
| Interviewpartner:         |                                                       |        |      |     |               |
| Prüfaktivität:            |                                                       |        |      |     |               |
| Analyse:                  |                                                       |        |      |     |               |
| Bewertung:                | Normal                                                | Subst. | Hoch | N/A | Nicht erfüllt |
|                           |                                                       |        |      |     |               |

<span id="page-14-0"></span>

| PrüfKrit-ID               | A1.1-10                                                                                                                                                                                   |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PrüfKrit<br>Beschreibung: | Verfügt das ID-Dokument über ein inländischen Ausweisdokumenten gleichwertiges<br>Sicherheitsniveau von Merkmalen und deren Prüfbarkeit zum Schutz vor Fälschungen<br>und Manipulationen? |
| Referenz                  | Kapitel 4.2, Tabelle 4                                                                                                                                                                    |
| Dokumentation:            |                                                                                                                                                                                           |
| Interviewpartner:         |                                                                                                                                                                                           |
| Prüfaktivität:            |                                                                                                                                                                                           |
| Analyse:                  |                                                                                                                                                                                           |

| Bewertung: | Normal | Subst. | Hoch | N/A | Nicht erfüllt |
|------------|--------|--------|------|-----|---------------|
|            |        |        |      |     |               |

#### 3.5 Enthält eine hinreichende Menge an ID-Attributen

<span id="page-15-2"></span>

| PrüfKrit-ID               | A1.2-1                                                   |        |      |     |               |  |
|---------------------------|----------------------------------------------------------|--------|------|-----|---------------|--|
| PrüfKrit<br>Beschreibung: | Ist eine hinreichende Menge von ID-Attributen vorhanden? |        |      |     |               |  |
| Referenz                  | Kapitel 4.2.2                                            |        |      |     |               |  |
| Dokumentation:            |                                                          |        |      |     |               |  |
| Interviewpartner:         |                                                          |        |      |     |               |  |
| Prüfaktivität:            |                                                          |        |      |     |               |  |
| Analyse:                  |                                                          |        |      |     |               |  |
| Bewertung:                | Normal                                                   | Subst. | Hoch | N/A | Nicht erfüllt |  |
|                           |                                                          |        |      |     |               |  |

<span id="page-15-1"></span>

| PrüfKrit-ID               | A1.2-2                                                                        |        |      |     |               |
|---------------------------|-------------------------------------------------------------------------------|--------|------|-----|---------------|
| PrüfKrit<br>Beschreibung: | Ist eine eindeutige Identifizierung durch die gegebenen ID-Attribute möglich? |        |      |     |               |
| Referenz                  | Kapitel 4.2.2                                                                 |        |      |     |               |
| Dokumentation:            |                                                                               |        |      |     |               |
| Interviewpartner:         |                                                                               |        |      |     |               |
| Prüfaktivität:            |                                                                               |        |      |     |               |
| Analyse:                  |                                                                               |        |      |     |               |
| Bewertung:                | Normal                                                                        | Subst. | Hoch | N/A | Nicht erfüllt |
|                           |                                                                               |        |      |     |               |

#### 3.6 Manipulations- und fälschungssicher

<span id="page-15-0"></span>

| PrüfKrit-ID               | A1.3-1                                                                                                                                                                                                                                   |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PrüfKrit<br>Beschreibung: | Ist das betrachtete ID-Dokument ein deutscher Personalausweis, ein EU<br>Aufenthaltstitel oder ein EU- oder EFTA-Reisepass und entspricht es damit bezüglich<br>der Manipulations- und Fälschungssicherheit dem Vertrauensniveau "hoch"? |
| Referenz                  | Kapitel 4.2.3                                                                                                                                                                                                                            |
| Dokumentation:            |                                                                                                                                                                                                                                          |
| Interviewpartner:         |                                                                                                                                                                                                                                          |
| Prüfaktivität:            |                                                                                                                                                                                                                                          |

| Analyse:   |        |        |      |     |               |
|------------|--------|--------|------|-----|---------------|
| Bewertung: | Normal | Subst. | Hoch | N/A | Nicht erfüllt |
|            |        |        |      |     |               |

<span id="page-16-2"></span>

| PrüfKrit-ID               | A1.3-2                                                                                                                                                                                                 |        |      |     |               |  |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|--|
| PrüfKrit<br>Beschreibung: | Welches Vertrauensniveau besitzt das betrachtete ID-Dokument in Bezug auf das<br>Angriffspotential, um dieses unter Berücksichtigung der Kategorie des Verfahrens zu<br>fälschen oder zu manipulieren? |        |      |     |               |  |
| Referenz                  | Kapitel 4.2.3                                                                                                                                                                                          |        |      |     |               |  |
| Dokumentation:            |                                                                                                                                                                                                        |        |      |     |               |  |
| Interviewpartner:         |                                                                                                                                                                                                        |        |      |     |               |  |
| Prüfaktivität:            |                                                                                                                                                                                                        |        |      |     |               |  |
| Analyse:                  |                                                                                                                                                                                                        |        |      |     |               |  |
| Bewertung:                | Normal                                                                                                                                                                                                 | Subst. | Hoch | N/A | Nicht erfüllt |  |
|                           |                                                                                                                                                                                                        |        |      |     |               |  |

#### 3.7 Sicherheitsmerkmale sind bekannt und effektiv überprüfbar

<span id="page-16-1"></span>

| PrüfKrit-ID               | A1.4-1                                                                                                                                |        |      |     |               |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|
| PrüfKrit<br>Beschreibung: | Sind alle im Rahmen des ID-Verfahren genutzten Sicherheitsmerkmale der<br>zugelassenen ID-Dokumente bekannt und effektiv überprüfbar? |        |      |     |               |
| Referenz                  | Kapitel 4.2.4                                                                                                                         |        |      |     |               |
| Dokumentation:            |                                                                                                                                       |        |      |     |               |
| Interviewpartner:         |                                                                                                                                       |        |      |     |               |
| Prüfaktivität:            |                                                                                                                                       |        |      |     |               |
| Analyse:                  |                                                                                                                                       |        |      |     |               |
| Bewertung:                | Normal                                                                                                                                | Subst. | Hoch | N/A | Nicht erfüllt |
|                           |                                                                                                                                       |        |      |     |               |

#### 3.8 Ermöglicht einen zuverlässigen Abgleich mit dem Verwender

<span id="page-16-0"></span>

| PrüfKrit-ID               | A1.5-1                                                                                                                                      |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| PrüfKrit<br>Beschreibung: | Wie hoch ist das Vertrauensniveau der auf dem ID-Dokument zur Verfügung<br>stehenden wissensbasierten Daten zum Abgleich mit dem Verwender? |
| Referenz                  | Kapitel 4.2.5                                                                                                                               |
| Dokumentation:            |                                                                                                                                             |
| Interviewpartner:         |                                                                                                                                             |

| Prüfaktivität: |        |        |      |     |               |
|----------------|--------|--------|------|-----|---------------|
| Analyse:       |        |        |      |     |               |
| Bewertung:     | Normal | Subst. | Hoch | N/A | Nicht erfüllt |
|                |        |        |      |     |               |

<span id="page-17-1"></span>

| PrüfKrit-ID               | A1.5-2                                                                                                                                   |        |      |     |               |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|
| PrüfKrit<br>Beschreibung: | Wie hoch ist das Vertrauensniveau der auf dem ID-Dokument zur Verfügung<br>stehenden biometrischen Daten zum Abgleich mit dem Verwender? |        |      |     |               |
| Referenz                  | Kapitel 4.2.5                                                                                                                            |        |      |     |               |
| Dokumentation:            |                                                                                                                                          |        |      |     |               |
| Interviewpartner:         |                                                                                                                                          |        |      |     |               |
| Prüfaktivität:            |                                                                                                                                          |        |      |     |               |
| Analyse:                  |                                                                                                                                          |        |      |     |               |
| Bewertung:                | Normal                                                                                                                                   | Subst. | Hoch | N/A | Nicht erfüllt |
|                           |                                                                                                                                          |        |      |     |               |

#### 3.9 ID-Attribute sind aktuell

<span id="page-17-0"></span>

| PrüfKrit-ID               | A1.6-1         |        |      |                                                                                 |               |
|---------------------------|----------------|--------|------|---------------------------------------------------------------------------------|---------------|
| PrüfKrit<br>Beschreibung: | gewährleistet? |        |      | Ist die Aktualität der ID-Attribute auf dem verwendeten ID-Dokument hinreichend |               |
| Referenz                  | Kapitel 4.2.6  |        |      |                                                                                 |               |
| Dokumentation:            |                |        |      |                                                                                 |               |
| Interviewpartner:         |                |        |      |                                                                                 |               |
| Prüfaktivität:            |                |        |      |                                                                                 |               |
| Analyse:                  |                |        |      |                                                                                 |               |
| Bewertung:                | Normal         | Subst. | Hoch | N/A                                                                             | Nicht erfüllt |
|                           |                |        |      |                                                                                 |               |

#### 3.10 Verfügbare Sperrmeldungen werden überprüft

<span id="page-17-2"></span>

| PrüfKrit-ID               | A1.7-1                                                       |
|---------------------------|--------------------------------------------------------------|
| PrüfKrit<br>Beschreibung: | Wird die maximale Gültigkeitsdauer des ID-Dokuments geprüft? |
| Referenz                  | Kapitel 4.2.7                                                |
| Dokumentation:            |                                                              |

| Interviewpartner: |        |        |      |     |               |
|-------------------|--------|--------|------|-----|---------------|
| Prüfaktivität:    |        |        |      |     |               |
| Analyse:          |        |        |      |     |               |
| Bewertung:        | Normal | Subst. | Hoch | N/A | Nicht erfüllt |
|                   |        |        |      |     |               |

<span id="page-18-2"></span>

| PrüfKrit-ID               | A1.7-2        |        |      |     |  |                                                                           |
|---------------------------|---------------|--------|------|-----|--|---------------------------------------------------------------------------|
| PrüfKrit<br>Beschreibung: | abgefragt?    |        |      |     |  | Werden zur Feststellung der Gültigkeit Sperrmeldungen für das ID-Dokument |
| Referenz                  | Kapitel 4.2.7 |        |      |     |  |                                                                           |
| Dokumentation:            |               |        |      |     |  |                                                                           |
| Interviewpartner:         |               |        |      |     |  |                                                                           |
| Prüfaktivität:            |               |        |      |     |  |                                                                           |
| Analyse:                  |               |        |      |     |  |                                                                           |
| Bewertung:                | Normal        | Subst. | Hoch | N/A |  | Nicht erfüllt                                                             |
|                           |               |        |      |     |  |                                                                           |

#### 3.11 Regelmäßige Prüfung der Menge der zulässigen ID-Dokumente

<span id="page-18-1"></span>

| PrüfKrit-ID               | A1.8-1                                                                                                                    |        |      |     |               |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|
| PrüfKrit<br>Beschreibung: | Wie oft werden die für das ID-Verfahren zugelassenen ID-Dokumente gemäß der<br>Anforderungen A1.7-1 und A1.7-2 überprüft? |        |      |     |               |
| Referenz                  | Kapitel 4.2, Tabelle 4; Kapitel 4.2.8                                                                                     |        |      |     |               |
| Dokumentation:            |                                                                                                                           |        |      |     |               |
| Interviewpartner:         |                                                                                                                           |        |      |     |               |
| Prüfaktivität:            |                                                                                                                           |        |      |     |               |
| Analyse:                  |                                                                                                                           |        |      |     |               |
| Bewertung:                | Normal                                                                                                                    | Subst. | Hoch | N/A | Nicht erfüllt |
|                           |                                                                                                                           |        |      |     |               |

<span id="page-18-0"></span>

| PrüfKrit-ID               | A1.8-2                                                                                                                     |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------|
| PrüfKrit<br>Beschreibung: | Werden neue, aus den Anforderungen A1.8-1 gewonnene Erkenntnisse bei der<br>Durchführung des ID-Verfahrens berücksichtigt? |
| Referenz                  | Kapitel 4.2.8                                                                                                              |
| Dokumentation:            |                                                                                                                            |
| Interviewpartner:         |                                                                                                                            |

| Prüfaktivität: |        |        |      |     |               |
|----------------|--------|--------|------|-----|---------------|
| Analyse:       |        |        |      |     |               |
| Bewertung:     | Normal | Subst. | Hoch | N/A | Nicht erfüllt |
|                |        |        |      |     |               |

## <span id="page-20-0"></span>4 Sicherheit der Übertragungskanäle

#### 4.1 Relevanz

| Schutzziele:                   | Existenz<br>Legitimität                                                              |
|--------------------------------|--------------------------------------------------------------------------------------|
| Beispiele für Verfahrenstypen: | "VideoIdent"<br>"PhotoIdent"<br>Verfahren mit Online-Ausweisfunktion des PA oder eAT |

#### 4.2 Video-/Informationstechnische Manipulationen biometrischer Daten der zu identifizierenden Person werden erkannt

<span id="page-20-2"></span>

| PrüfKrit-ID               | A2.1-1             |                                                              |                               |                                                                                |               |
|---------------------------|--------------------|--------------------------------------------------------------|-------------------------------|--------------------------------------------------------------------------------|---------------|
| PrüfKrit<br>Beschreibung: | Angriffspotential, | um<br>eine<br>biometrischer Daten erfolgreich durchzuführen? | video-/informationstechnische | Welches Vertrauensniveau besitzt das betrachtete ID-Verfahren in Bezug auf das | Manipulation  |
| Referenz                  | Kapitel 5.2.1      |                                                              |                               |                                                                                |               |
| Dokumentation:            |                    |                                                              |                               |                                                                                |               |
| Interviewpartner:         |                    |                                                              |                               |                                                                                |               |
| Prüfaktivität:            |                    |                                                              |                               |                                                                                |               |
| Analyse:                  |                    |                                                              |                               |                                                                                |               |
| Bewertung:                | Normal             | Subst.                                                       | Hoch                          | N/A                                                                            | Nicht erfüllt |
|                           |                    |                                                              |                               |                                                                                |               |

#### 4.3 Informationstechnische Manipulationen vom ID-Dokument übertragener Informationen werden erkannt

<span id="page-20-1"></span>

| PrüfKrit-ID               | A2.2-1                                                                                                                                                                        |        |      |     |               |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|
| PrüfKrit<br>Beschreibung: | Wie lautet das Vertrauensniveau desjenigen für das ID-Verfahren verwendeten ID<br>Nachweises, für welchen das niedrigste Angriffspotential zur Kompromittierung<br>ausreicht? |        |      |     |               |
| Referenz                  | Kapitel 5.2.2                                                                                                                                                                 |        |      |     |               |
| Prüfaktivität:            | Bestimmung des niedrigsten Angriffspotentials über alle ID-Nachweise gemäß dem<br>Minimumprinzip und Festlegung des erreichten Vertrauensniveaus.                             |        |      |     |               |
| Analyse:                  |                                                                                                                                                                               |        |      |     |               |
| Bewertung:                | Normal                                                                                                                                                                        | Subst. | Hoch | N/A | Nicht erfüllt |

<span id="page-21-2"></span>

| PrüfKrit-ID               | A2.2-2                                                                                                                                                                                                                        |        |      |     |               |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|
| PrüfKrit<br>Beschreibung: | Welches Vertrauensniveau besitzt das betrachtete ID-Verfahren in Bezug auf das<br>Angriffspotential, um eine informationstechnische Manipulation einer vom ID<br>Dokument übertragenen Information erfolgreich durchzuführen? |        |      |     |               |
| Referenz                  | Kapitel 5.2.2                                                                                                                                                                                                                 |        |      |     |               |
| Dokumentation:            |                                                                                                                                                                                                                               |        |      |     |               |
| Interviewpartner:         |                                                                                                                                                                                                                               |        |      |     |               |
| Prüfaktivität:            |                                                                                                                                                                                                                               |        |      |     |               |
| Analyse:                  |                                                                                                                                                                                                                               |        |      |     |               |
| Bewertung:                | Normal                                                                                                                                                                                                                        | Subst. | Hoch | N/A | Nicht erfüllt |
|                           |                                                                                                                                                                                                                               |        |      |     |               |

#### 4.4 Physikalische Manipulationen biometrischer Charakteristika der zu identifizierenden Person werden erkannt

<span id="page-21-1"></span>

| PrüfKrit-ID               | A2.3-1                                                                                                                                                                                                                              |        |      |     |               |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|
| PrüfKrit<br>Beschreibung: | Welches Vertrauensniveau besitzt das betrachtete ID-Verfahren in Bezug auf das<br>Angriffspotential, um eine physikalische Manipulation biometrischer Charakteristika<br>der zu identifizierenden Person erfolgreich durchzuführen? |        |      |     |               |
| Referenz                  | Kapitel 5.2.3                                                                                                                                                                                                                       |        |      |     |               |
| Dokumentation:            |                                                                                                                                                                                                                                     |        |      |     |               |
| Interviewpartner:         |                                                                                                                                                                                                                                     |        |      |     |               |
| Prüfaktivität:            |                                                                                                                                                                                                                                     |        |      |     |               |
| Analyse:                  |                                                                                                                                                                                                                                     |        |      |     |               |
| Bewertung:                | Normal                                                                                                                                                                                                                              | Subst. | Hoch | N/A | Nicht erfüllt |
|                           |                                                                                                                                                                                                                                     |        |      |     |               |

#### 4.5 Physikalische Manipulationen am ID-Dokument werden erkannt

<span id="page-21-0"></span>

| PrüfKrit-ID               | A2.4-1                                                                                                                                                                                         |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PrüfKrit<br>Beschreibung: | Welches Vertrauensniveau besitzt das betrachtete ID-Verfahren in Bezug auf das<br>Angriffspotential, um in diesem eine physikalische Manipulation am ID-Dokument<br>erfolgreich durchzuführen? |

| Referenz          | Kapitel 5.2.4 |        |      |     |               |
|-------------------|---------------|--------|------|-----|---------------|
| Dokumentation:    |               |        |      |     |               |
| Interviewpartner: |               |        |      |     |               |
| Prüfaktivität:    |               |        |      |     |               |
| Analyse:          |               |        |      |     |               |
| Bewertung:        | Normal        | Subst. | Hoch | N/A | Nicht erfüllt |
|                   |               |        |      |     |               |

#### 4.6 Liveübertragung sämtlicher Daten ist gewährleistet

<span id="page-22-1"></span>

| PrüfKrit-ID               | A2.5-1                                                                                                                                                                                          |        |      |     |               |  |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|--|
| PrüfKrit<br>Beschreibung: | Welches Vertrauensniveau besitzt das betrachtete ID-Verfahren in Bezug auf das<br>Angriffspotential, um in diesem eine Wiederverwendung von aufgezeichneten Daten<br>erfolgreich durchzuführen? |        |      |     |               |  |
| Referenz                  | Kapitel 5.2.5                                                                                                                                                                                   |        |      |     |               |  |
| Dokumentation:            |                                                                                                                                                                                                 |        |      |     |               |  |
| Interviewpartner:         |                                                                                                                                                                                                 |        |      |     |               |  |
| Prüfaktivität:            |                                                                                                                                                                                                 |        |      |     |               |  |
| Analyse:                  |                                                                                                                                                                                                 |        |      |     |               |  |
| Bewertung:                | Normal                                                                                                                                                                                          | Subst. | Hoch | N/A | Nicht erfüllt |  |
|                           |                                                                                                                                                                                                 |        |      |     |               |  |

#### 4.7 Ein Austausch des präsentierten ID-Dokuments oder der zu identifizierenden Person während der Prüfung wird erkannt

<span id="page-22-0"></span>

| PrüfKrit-ID               | A2.6-1         |                                                                                                                                                                  |      |     |                                                                      |
|---------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|-----|----------------------------------------------------------------------|
| PrüfKrit<br>Beschreibung: | durchzuführen? | Welches Vertrauensniveau besitzt das betrachtete ID-Verfahren in Bezug auf das<br>Angriffspotential, um in diesem einen Austausch des präsentierten ID-Dokuments |      |     | oder der zu identifizierenden Person während der Prüfung erfolgreich |
| Referenz                  | Kapitel 5.2.6  |                                                                                                                                                                  |      |     |                                                                      |
| Dokumentation:            |                |                                                                                                                                                                  |      |     |                                                                      |
| Interviewpartner:         |                |                                                                                                                                                                  |      |     |                                                                      |
| Prüfaktivität:            |                |                                                                                                                                                                  |      |     |                                                                      |
| Analyse:                  |                |                                                                                                                                                                  |      |     |                                                                      |
| Bewertung:                | Normal         | Subst.                                                                                                                                                           | Hoch | N/A | Nicht erfüllt                                                        |

### <span id="page-24-0"></span>5 Prüfung der ID-Nachweise

#### 5.1 Relevanz

| Schutzziele:                   | Eindeutigkeit                                                            |
|--------------------------------|--------------------------------------------------------------------------|
| Beispiele für Verfahrenstypen: | "VideoIdent"                                                             |
|                                | "PhotoIdent"<br>Verfahren mit unmittelbarer Anwesenheit (z.B. PostIdent) |
|                                | Verfahren mit Online-Ausweisfunktion des PA oder eAT                     |

#### 5.2 Mehrere ID-Nachweise

<span id="page-24-2"></span>

| PrüfKrit-ID               | A3.G-1                                                                                                                                                                        |        |      |     |               |  |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|--|
| PrüfKrit<br>Beschreibung: | Wie lautet das Vertrauensniveau desjenigen für das ID-Verfahren verwendeten ID<br>Nachweises, für welchen das niedrigste Angriffspotential zur Kompromittierung<br>ausreicht? |        |      |     |               |  |
| Referenz                  | Kapitel 6                                                                                                                                                                     |        |      |     |               |  |
| Prüfaktivität:            | Bestimmung des Vertrauensniveaus über alle ID-Dokumente gemäß dem<br>Minimumprinzip.                                                                                          |        |      |     |               |  |
| Analyse:                  |                                                                                                                                                                               |        |      |     |               |  |
| Bewertung:                | Normal                                                                                                                                                                        | Subst. | Hoch | N/A | Nicht erfüllt |  |
|                           |                                                                                                                                                                               |        |      |     |               |  |

#### 5.3 Typ des verwendeten ID-Dokuments lässt sich ermitteln

<span id="page-24-1"></span>

| PrüfKrit-ID               | A3.1-1        |        |  |      |                                                                             |               |  |
|---------------------------|---------------|--------|--|------|-----------------------------------------------------------------------------|---------------|--|
| PrüfKrit<br>Beschreibung: | überprüfen?   |        |  |      | Lässt sich der Typ des zur Prüfung vorgelegten ID-Dokuments feststellen und |               |  |
| Referenz                  | Kapitel 6.4.1 |        |  |      |                                                                             |               |  |
| Dokumentation:            |               |        |  |      |                                                                             |               |  |
| Interviewpartner:         |               |        |  |      |                                                                             |               |  |
| Prüfaktivität:            |               |        |  |      |                                                                             |               |  |
| Analyse:                  |               |        |  |      |                                                                             |               |  |
| Bewertung:                | Normal        | Subst. |  | Hoch | N/A                                                                         | Nicht erfüllt |  |
|                           |               |        |  |      |                                                                             |               |  |

### 5.4 ID-Dokument ist gültig

<span id="page-25-0"></span>

| PrüfKrit-ID               | A3.2-1                                                                             |        |      |     |               |  |
|---------------------------|------------------------------------------------------------------------------------|--------|------|-----|---------------|--|
| PrüfKrit<br>Beschreibung: | Lässt sich die Gültigkeit des vorgelegten ID-Dokuments feststellen und überprüfen? |        |      |     |               |  |
| Referenz                  | Kapitel 6.4.2                                                                      |        |      |     |               |  |
| Dokumentation:            |                                                                                    |        |      |     |               |  |
| Interviewpartner:         |                                                                                    |        |      |     |               |  |
| Prüfaktivität:            |                                                                                    |        |      |     |               |  |
| Analyse:                  |                                                                                    |        |      |     |               |  |
| Bewertung:                | Normal                                                                             | Subst. | Hoch | N/A | Nicht erfüllt |  |
|                           |                                                                                    |        |      |     |               |  |

#### 5.5 Gefälschte Sicherheitsmerkmale werden erkannt

<span id="page-25-2"></span>

| PrüfKrit-ID               | A3.3-1                                                                                                |        |      |     |               |  |
|---------------------------|-------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|--|
| PrüfKrit<br>Beschreibung: | Welche verbindlichen Prüfvorgaben sind für die im ID-Verfahren zulässigen ID<br>Dokumente festgelegt? |        |      |     |               |  |
| Referenz                  | Kapitel 6.4.3                                                                                         |        |      |     |               |  |
| Dokumentation:            |                                                                                                       |        |      |     |               |  |
| Interviewpartner:         |                                                                                                       |        |      |     |               |  |
| Prüfaktivität:            |                                                                                                       |        |      |     |               |  |
| Analyse:                  |                                                                                                       |        |      |     |               |  |
| Bewertung:                | Normal                                                                                                | Subst. | Hoch | N/A | Nicht erfüllt |  |
|                           |                                                                                                       |        |      |     |               |  |

<span id="page-25-1"></span>

| PrüfKrit-ID               | A3.3-2                                                                                                                                                         |        |      |     |               |  |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|--|
| PrüfKrit<br>Beschreibung: | Welches Vertrauensniveau besitzt das betrachtete ID-Verfahren in Bezug auf das<br>Angriffspotential, um in diesem Sicherheitsmerkmale erfolgreich zu fälschen? |        |      |     |               |  |
| Referenz                  | Kapitel 6.4.3                                                                                                                                                  |        |      |     |               |  |
| Dokumentation:            |                                                                                                                                                                |        |      |     |               |  |
| Interviewpartner:         |                                                                                                                                                                |        |      |     |               |  |
| Prüfaktivität:            |                                                                                                                                                                |        |      |     |               |  |
| Analyse:                  |                                                                                                                                                                |        |      |     |               |  |
| Bewertung:                | Normal                                                                                                                                                         | Subst. | Hoch | N/A | Nicht erfüllt |  |
|                           |                                                                                                                                                                |        |      |     |               |  |

#### 5.6 Fälschungen der personalisierten Daten werden erkannt

<span id="page-26-1"></span>

| PrüfKrit-ID               | A3.4-1                                                                   |        |      |     |               |  |  |
|---------------------------|--------------------------------------------------------------------------|--------|------|-----|---------------|--|--|
| PrüfKrit<br>Beschreibung: | Wird eine Konsistenzprüfung der verschiedenen ID-Attribute durchgeführt? |        |      |     |               |  |  |
| Referenz                  | Kapitel 6.4.4                                                            |        |      |     |               |  |  |
| Dokumentation:            |                                                                          |        |      |     |               |  |  |
| Interviewpartner:         |                                                                          |        |      |     |               |  |  |
| Prüfaktivität:            |                                                                          |        |      |     |               |  |  |
| Analyse:                  |                                                                          |        |      |     |               |  |  |
| Bewertung:                | Normal                                                                   | Subst. | Hoch | N/A | Nicht erfüllt |  |  |
|                           |                                                                          |        |      |     |               |  |  |

<span id="page-26-0"></span>

| PrüfKrit-ID               | A3.4-2                                                                                                                                                                                 |        |      |     |               |  |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|--|
| PrüfKrit<br>Beschreibung: | Welches Vertrauensniveau besitzt das betrachtete ID-Verfahren in Bezug auf das<br>Angriffspotential, um in diesem Fälschungen von personalisierten Daten erfolgreich<br>durchzuführen? |        |      |     |               |  |
| Referenz                  | Kapitel 6.4.4                                                                                                                                                                          |        |      |     |               |  |
| Dokumentation:            |                                                                                                                                                                                        |        |      |     |               |  |
| Interviewpartner:         |                                                                                                                                                                                        |        |      |     |               |  |
| Prüfaktivität:            |                                                                                                                                                                                        |        |      |     |               |  |
| Analyse:                  |                                                                                                                                                                                        |        |      |     |               |  |
| Bewertung:                | Normal                                                                                                                                                                                 | Subst. | Hoch | N/A | Nicht erfüllt |  |
|                           |                                                                                                                                                                                        |        |      |     |               |  |

### <span id="page-27-0"></span>6 Abgleich von Personen mit ID-Nachweisen

### 6.1 Vertrauliche Wissensfaktoren werden ausschließlich dem legitimen Inhaber mitgeteilt

<span id="page-27-3"></span>

| PrüfKrit-ID               | A4.1-1                                                                                                          |        |      |     |               |
|---------------------------|-----------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|
| PrüfKrit<br>Beschreibung: | Welches Vertrauensniveau erreicht die Übertragung des vertraulichen Wissensfaktors<br>an den legitimen Inhaber? |        |      |     |               |
| Referenz                  | Kapitel 7.2.1                                                                                                   |        |      |     |               |
| Dokumentation:            |                                                                                                                 |        |      |     |               |
| Interviewpartner:         |                                                                                                                 |        |      |     |               |
| Prüfaktivität:            |                                                                                                                 |        |      |     |               |
| Analyse:                  |                                                                                                                 |        |      |     |               |
| Bewertung:                | Normal                                                                                                          | Subst. | Hoch | N/A | Nicht erfüllt |
|                           |                                                                                                                 |        |      |     |               |

#### 6.2 Sicherheit der verwendeten Authentisierungsmittel

<span id="page-27-2"></span>

| PrüfKrit-ID               | A4.2-1                                                                     |        |      |     |               |
|---------------------------|----------------------------------------------------------------------------|--------|------|-----|---------------|
| PrüfKrit<br>Beschreibung: | Welches Vertrauensniveau erreichen die verwendeten Authentisierungsmittel? |        |      |     |               |
| Referenz                  | Kapitel 7.2.2                                                              |        |      |     |               |
| Dokumentation:            |                                                                            |        |      |     |               |
| Interviewpartner:         |                                                                            |        |      |     |               |
| Prüfaktivität:            |                                                                            |        |      |     |               |
| Analyse:                  |                                                                            |        |      |     |               |
| Bewertung:                | Normal                                                                     | Subst. | Hoch | N/A | Nicht erfüllt |
|                           |                                                                            |        |      |     |               |

#### 6.3 Die tatsächliche Verfügungsgewalt der zu identifizierenden Person über das ID-Dokument wird sichergestellt

<span id="page-27-1"></span>

| PrüfKrit-ID               | A4.3-1                                                                                                                      |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| PrüfKrit<br>Beschreibung: | Besitzt die zu identifizierende Person während des ID-Verfahrens die tatsächliche<br>Verfügungsgewalt über ihr ID-Dokument? |
| Referenz                  | Kapitel 7.2.3                                                                                                               |

| Dokumentation:    |        |        |      |     |               |
|-------------------|--------|--------|------|-----|---------------|
| Interviewpartner: |        |        |      |     |               |
| Prüfaktivität:    |        |        |      |     |               |
| Analyse:          |        |        |      |     |               |
| Bewertung:        | Normal | Subst. | Hoch | N/A | Nicht erfüllt |
|                   |        |        |      |     |               |

#### 6.4 Abzugleichende ID-Attribute werden in hinreichender Qualität erfasst

<span id="page-28-1"></span>

| PrüfKrit-ID               | A4.4-1                                                                                                                                                                                                                                                                                                       |        |      |     |               |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|
| PrüfKrit<br>Beschreibung: | Welches Vertrauensniveau hat die Qualität der Erfassung der abzugleichenden<br>biometrischen oder verhaltensbasierten ID-Attribute beim Enrolment (erstmalige<br>Registrierung einer Person am biometrischen System), bei dem die Erfassung der ID<br>Attribute für die Erzeugung der Referenzdaten erfolgt? |        |      |     |               |
| Referenz                  | Kapitel 7.2.4                                                                                                                                                                                                                                                                                                |        |      |     |               |
| Dokumentation:            |                                                                                                                                                                                                                                                                                                              |        |      |     |               |
| Interviewpartner:         |                                                                                                                                                                                                                                                                                                              |        |      |     |               |
| Prüfaktivität:            |                                                                                                                                                                                                                                                                                                              |        |      |     |               |
| Analyse:                  |                                                                                                                                                                                                                                                                                                              |        |      |     |               |
| Bewertung:                | Normal                                                                                                                                                                                                                                                                                                       | Subst. | Hoch | N/A | Nicht erfüllt |
|                           |                                                                                                                                                                                                                                                                                                              |        |      |     |               |

<span id="page-28-0"></span>

| PrüfKrit-ID               | A4.4-2                                                                                                                                                                                                                                                                |        |      |     |               |  |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|--|
| PrüfKrit<br>Beschreibung: | Welches Vertrauensniveau hat die Qualität der Erfassung der abzugleichenden<br>biometrischen<br>oder<br>verhaltensbasierten<br>ID-Attribute<br>beim<br>Capture<br>(Erfassungsprozess), bei dem die Erfassung der ID-Attribute im Rahmen des ID<br>Verfahrens erfolgt? |        |      |     |               |  |
| Referenz                  | Kapitel 7.2.4                                                                                                                                                                                                                                                         |        |      |     |               |  |
| Dokumentation:            |                                                                                                                                                                                                                                                                       |        |      |     |               |  |
| Interviewpartner:         |                                                                                                                                                                                                                                                                       |        |      |     |               |  |
| Prüfaktivität:            |                                                                                                                                                                                                                                                                       |        |      |     |               |  |
| Analyse:                  |                                                                                                                                                                                                                                                                       |        |      |     |               |  |
| Bewertung:                | Normal                                                                                                                                                                                                                                                                | Subst. | Hoch | N/A | Nicht erfüllt |  |
|                           |                                                                                                                                                                                                                                                                       |        |      |     |               |  |

### 6.5 Zuverlässiger Abgleich relevanter biometrischer ID-Attribute zwischen ID-Dokument und zu identifizierender Person

<span id="page-29-0"></span>

| PrüfKrit-ID               | A4.5-1                   |        |      |                                                                     |               |
|---------------------------|--------------------------|--------|------|---------------------------------------------------------------------|---------------|
| PrüfKrit<br>Beschreibung: | biometrischen Verfahren? |        |      | Welches Vertrauensniveau erreichen die vom ID-Verfahren verwendeten |               |
| Referenz                  | Kapitel 7.2.5            |        |      |                                                                     |               |
| Dokumentation:            |                          |        |      |                                                                     |               |
| Interviewpartner:         |                          |        |      |                                                                     |               |
| Prüfaktivität:            |                          |        |      |                                                                     |               |
| Analyse:                  |                          |        |      |                                                                     |               |
| Bewertung:                | Normal                   | Subst. | Hoch | N/A                                                                 | Nicht erfüllt |
|                           |                          |        |      |                                                                     |               |

## <span id="page-30-0"></span>7 Korrekte Erfassung der benötigten ID-Attribute

#### 7.1 Relevanz

| Schutzziele:                   | Eindeutigkeit                                                                                                                                    |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Beispiele für Verfahrenstypen: | "VideoIdent"<br>"PhotoIdent"<br>Verfahren mit unmittelbarer Anwesenheit (z.B. PostIdent)<br>Verfahren mit Online-Ausweisfunktion des PA oder eAT |

#### 7.2 Zu erfassende ID-Attribute erlauben eine eindeutige Identifizierung

<span id="page-30-2"></span>

| PrüfKrit-ID               | A5.1-1                                                                       |        |      |     |               |
|---------------------------|------------------------------------------------------------------------------|--------|------|-----|---------------|
| PrüfKrit<br>Beschreibung: | Ist mit den erfassten ID-Attributen eine eindeutige Identifizierung möglich? |        |      |     |               |
| Referenz                  | Kapitel 8.2.1                                                                |        |      |     |               |
| Dokumentation:            |                                                                              |        |      |     |               |
| Interviewpartner:         |                                                                              |        |      |     |               |
| Prüfaktivität:            |                                                                              |        |      |     |               |
| Analyse:                  |                                                                              |        |      |     |               |
| Bewertung:                | Normal                                                                       | Subst. | Hoch | N/A | Nicht erfüllt |
|                           |                                                                              |        |      |     |               |

### 7.3 Spezifische Sachkenntnis der Prüfer und ggf. zu verwendende Hilfsmittel sind vorhanden

<span id="page-30-1"></span>

| PrüfKrit-ID               | A5.2-1                                                                                                                                          |        |      |     |               |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|
| PrüfKrit<br>Beschreibung: | Liegt für das an der Interpretation und Erfassung der ID-Attribute beteiligte Personal<br>für alle ID-Nachweise ein Nachweis der Sachkunde vor? |        |      |     |               |
| Referenz                  | Kapitel 8.2.2                                                                                                                                   |        |      |     |               |
| Dokumentation:            |                                                                                                                                                 |        |      |     |               |
| Interviewpartner:         |                                                                                                                                                 |        |      |     |               |
| Prüfaktivität:            |                                                                                                                                                 |        |      |     |               |
| Analyse:                  |                                                                                                                                                 |        |      |     |               |
| Bewertung:                | Normal                                                                                                                                          | Subst. | Hoch | N/A | Nicht erfüllt |
|                           |                                                                                                                                                 |        |      |     |               |

<span id="page-31-0"></span>

| PrüfKrit-ID               | A5.2-2                                                                                                 |        |      |     |               |
|---------------------------|--------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|
| PrüfKrit<br>Beschreibung: | Stehen die vorgesehenen Hilfsmittel stets für den Erfassungsvorgang der ID-Attribute<br>zur Verfügung? |        |      |     |               |
| Referenz                  | Kapitel 8.2.2                                                                                          |        |      |     |               |
| Dokumentation:            |                                                                                                        |        |      |     |               |
| Interviewpartner:         |                                                                                                        |        |      |     |               |
| Prüfaktivität:            |                                                                                                        |        |      |     |               |
| Analyse:                  |                                                                                                        |        |      |     |               |
| Bewertung:                | Normal                                                                                                 | Subst. | Hoch | N/A | Nicht erfüllt |
|                           |                                                                                                        |        |      |     |               |

#### 7.4 ID-Attribute werden vollständig und fehlerfrei in das Erfassungssystem übertragen

<span id="page-31-2"></span>

| PrüfKrit-ID               | A5.3-1                                                                                                                                                          |        |      |     |               |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|
| PrüfKrit<br>Beschreibung: | Welche Maßnahmen existieren zur vollständigen und fehlerfreien Übernahme von<br>ID-Attributen in das Erfassungssystem (System zur Erfassung von ID-Attributen)? |        |      |     |               |
| Referenz                  | Kapitel 8.2.3                                                                                                                                                   |        |      |     |               |
| Dokumentation:            |                                                                                                                                                                 |        |      |     |               |
| Interviewpartner:         |                                                                                                                                                                 |        |      |     |               |
| Prüfaktivität:            |                                                                                                                                                                 |        |      |     |               |
| Analyse:                  |                                                                                                                                                                 |        |      |     |               |
| Bewertung:                | Normal                                                                                                                                                          | Subst. | Hoch | N/A | Nicht erfüllt |
|                           |                                                                                                                                                                 |        |      |     |               |

<span id="page-31-1"></span>

| PrüfKrit-ID               | A5.3-2                                                                                                          |        |      |     |               |
|---------------------------|-----------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|
| PrüfKrit<br>Beschreibung: | Ist das Erfassungssystem technisch geeignet, alle relevanten ID-Attribute vollständig<br>und exakt aufzunehmen? |        |      |     |               |
| Referenz                  | Kapitel 8.2.3                                                                                                   |        |      |     |               |
| Dokumentation:            |                                                                                                                 |        |      |     |               |
| Interviewpartner:         |                                                                                                                 |        |      |     |               |
| Prüfaktivität:            |                                                                                                                 |        |      |     |               |
| Analyse:                  |                                                                                                                 |        |      |     |               |
| Bewertung:                | Normal                                                                                                          | Subst. | Hoch | N/A | Nicht erfüllt |
|                           |                                                                                                                 |        |      |     |               |

### 7.5 Erfasste Daten werden auf Aktualität, Konsistenz und Plausibilität geprüft

<span id="page-32-2"></span>

| PrüfKrit-ID               | A5.4-1                                                                  |        |      |     |               |
|---------------------------|-------------------------------------------------------------------------|--------|------|-----|---------------|
| PrüfKrit<br>Beschreibung: | Erfolgt eine Prüfung der ID-Attribute auf Konsistenz und Plausibilität? |        |      |     |               |
| Referenz                  | Kapitel 8.2.4                                                           |        |      |     |               |
| Dokumentation:            |                                                                         |        |      |     |               |
| Interviewpartner:         |                                                                         |        |      |     |               |
| Prüfaktivität:            |                                                                         |        |      |     |               |
| Analyse:                  |                                                                         |        |      |     |               |
| Bewertung:                | Normal                                                                  | Subst. | Hoch | N/A | Nicht erfüllt |
|                           |                                                                         |        |      |     |               |

<span id="page-32-1"></span>

| PrüfKrit-ID               | A5.4-2                                                                            |        |      |     |               |
|---------------------------|-----------------------------------------------------------------------------------|--------|------|-----|---------------|
| PrüfKrit<br>Beschreibung: | Wird die ID-Prüfung bei offenen Pflichtfeldern während der Erfassung abgebrochen? |        |      |     |               |
| Referenz                  | Kapitel 8.2.4                                                                     |        |      |     |               |
| Dokumentation:            |                                                                                   |        |      |     |               |
| Interviewpartner:         |                                                                                   |        |      |     |               |
| Prüfaktivität:            |                                                                                   |        |      |     |               |
| Analyse:                  |                                                                                   |        |      |     |               |
| Bewertung:                | Normal                                                                            | Subst. | Hoch | N/A | Nicht erfüllt |
|                           |                                                                                   |        |      |     |               |

<span id="page-32-0"></span>

| PrüfKrit-ID               | A5.4-3                                                                                                                                       |        |      |     |               |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|
| PrüfKrit<br>Beschreibung: | Wie lautet das Vertrauensniveau der Prüfung der ID-Attribute auf Aktualität,<br>Konsistenz und Plausibilität bei Erfassung dieser Attribute? |        |      |     |               |
| Referenz                  | Kapitel 8.2.4                                                                                                                                |        |      |     |               |
| Dokumentation:            |                                                                                                                                              |        |      |     |               |
| Interviewpartner:         |                                                                                                                                              |        |      |     |               |
| Prüfaktivität:            |                                                                                                                                              |        |      |     |               |
| Analyse:                  |                                                                                                                                              |        |      |     |               |
| Bewertung:                | Normal                                                                                                                                       | Subst. | Hoch | N/A | Nicht erfüllt |
|                           |                                                                                                                                              |        |      |     |               |

### <span id="page-33-0"></span>8 Sicherung der Integrität der Prozesse

#### 8.1 Relevanz

| Schutzziele:                   | Die Anforderung "Sicherung der Integrität der Prozesse" definiert<br>organisationsübergreifende Sicherheitsmaßnahmen und gewährleistet<br>die Umsetzung der notwendigen Anforderungen zur Erreichung aller<br>Sicherheitsziele, d.h. Existenz, Legitimität und Eindeutigkeit. |  |  |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
| Beispiele für Verfahrenstypen: | "VideoIdent"<br>"PhotoIdent"<br>Verfahren mit unmittelbarer Anwesenheit (z.B. PostIdent)<br>Verfahren mit Online-Ausweisfunktion des PA oder eAT                                                                                                                              |  |  |

#### 8.2 Die Einhaltung der vorgeschriebenen Prüfkriterien ist sichergestellt

<span id="page-33-3"></span>

| PrüfKrit-ID               | A6.1-1                                                                                                                                   |        |      |     |               |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|
| PrüfKrit<br>Beschreibung: | Ist die Einhaltung der ID-Prüfkriterien durch technische und organisatorische<br>Maßnahmen bzw. einer Kombination daraus sichergestellt? |        |      |     |               |
| Referenz                  | Kapitel 9.2.1                                                                                                                            |        |      |     |               |
| Dokumentation:            |                                                                                                                                          |        |      |     |               |
| Interviewpartner:         |                                                                                                                                          |        |      |     |               |
| Prüfaktivität:            |                                                                                                                                          |        |      |     |               |
| Analyse:                  |                                                                                                                                          |        |      |     |               |
| Bewertung:                | Normal                                                                                                                                   | Subst. | Hoch | N/A | Nicht erfüllt |
|                           |                                                                                                                                          |        |      |     |               |

<span id="page-33-2"></span>

| PrüfKrit-ID               | A6.1-2                                                                       |        |      |     |               |
|---------------------------|------------------------------------------------------------------------------|--------|------|-----|---------------|
| PrüfKrit<br>Beschreibung: | Werden die für jedes ID-Dokument zu prüfenden Sicherheitsmerkmale definiert? |        |      |     |               |
| Referenz                  | Kapitel 9.2.1                                                                |        |      |     |               |
| Dokumentation:            |                                                                              |        |      |     |               |
| Interviewpartner:         |                                                                              |        |      |     |               |
| Prüfaktivität:            |                                                                              |        |      |     |               |
| Analyse:                  |                                                                              |        |      |     |               |
| Bewertung:                | Normal                                                                       | Subst. | Hoch | N/A | Nicht erfüllt |
|                           |                                                                              |        |      |     |               |

<span id="page-33-1"></span>

| PrüfKrit-ID | A6.1-3 |
|-------------|--------|
|             |        |

| PrüfKrit<br>Beschreibung: | prüfenden Sicherheitsmerkmale? | Wie lautet das Vertrauensniveau für die Aktualisierung der Definitionen der zu |      |     |               |  |
|---------------------------|--------------------------------|--------------------------------------------------------------------------------|------|-----|---------------|--|
| Referenz                  | Kapitel 9.2.1                  |                                                                                |      |     |               |  |
| Dokumentation:            |                                |                                                                                |      |     |               |  |
| Interviewpartner:         |                                |                                                                                |      |     |               |  |
| Prüfaktivität:            |                                |                                                                                |      |     |               |  |
| Analyse:                  |                                |                                                                                |      |     |               |  |
| Bewertung:                | Normal                         | Subst.                                                                         | Hoch | N/A | Nicht erfüllt |  |
|                           |                                |                                                                                |      |     |               |  |

<span id="page-34-2"></span>

| PrüfKrit-ID               | A6.1-4                                                                                                                                       |        |      |     |               |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|
| PrüfKrit<br>Beschreibung: | Wie lautet das Vertrauensniveau der Fachkunde und Vertrauenswürdigkeit des für<br>manuell durchgeführte Prüfschritte eingesetzten Personals? |        |      |     |               |
| Referenz                  | Kapitel 9.2.1                                                                                                                                |        |      |     |               |
| Dokumentation:            |                                                                                                                                              |        |      |     |               |
| Interviewpartner:         |                                                                                                                                              |        |      |     |               |
| Prüfaktivität:            |                                                                                                                                              |        |      |     |               |
| Analyse:                  |                                                                                                                                              |        |      |     |               |
| Bewertung:                | Normal                                                                                                                                       | Subst. | Hoch | N/A | Nicht erfüllt |
|                           |                                                                                                                                              |        |      |     |               |

<span id="page-34-1"></span>

| PrüfKrit-ID               | A6.1-5                                                                                                                                                                                                                   |        |      |     |               |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|
| PrüfKrit<br>Beschreibung: | Welches Gesamtvertrauensniveau besitzt das betrachtete ID-Verfahren in Bezug<br>darauf, ob die Einhaltung der vorgeschriebenen Prüfkriterien sichergestellt ist, unter<br>Berücksichtigung der Punkte A6.1-1 bis A6.1-4? |        |      |     |               |
| Referenz                  | Kapitel 9.2.1                                                                                                                                                                                                            |        |      |     |               |
| Dokumentation:            |                                                                                                                                                                                                                          |        |      |     |               |
| Interviewpartner:         |                                                                                                                                                                                                                          |        |      |     |               |
| Prüfaktivität:            |                                                                                                                                                                                                                          |        |      |     |               |
| Analyse:                  |                                                                                                                                                                                                                          |        |      |     |               |
| Bewertung:                | Normal                                                                                                                                                                                                                   | Subst. | Hoch | N/A | Nicht erfüllt |
|                           |                                                                                                                                                                                                                          |        |      |     |               |

#### 8.3 ISMS

<span id="page-34-0"></span>

| PrüfKrit-ID | A6.2-1                                                                  |
|-------------|-------------------------------------------------------------------------|
| PrüfKrit-   | Ist zur generischen Sicherung der Integrität der Prozesse ein ISMS nach |

| Beschreibung:     | ISO / IEC 27001 und ISO / IEC 27002 oder gleichwertig implementiert, das alle IT<br>Komponenten und IT-Prozesse umfasst, die für die Identitätsprüfung bzw.<br>Speicherung oder Übertragung hierbei erfasster Daten verwendet werden? |        |      |     |               |  |  |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|--|--|
| Referenz          | Kapitel 9.2.2                                                                                                                                                                                                                         |        |      |     |               |  |  |
| Dokumentation:    |                                                                                                                                                                                                                                       |        |      |     |               |  |  |
| Interviewpartner: |                                                                                                                                                                                                                                       |        |      |     |               |  |  |
| Prüfaktivität:    |                                                                                                                                                                                                                                       |        |      |     |               |  |  |
| Analyse:          |                                                                                                                                                                                                                                       |        |      |     |               |  |  |
| Bewertung:        | Normal                                                                                                                                                                                                                                | Subst. | Hoch | N/A | Nicht erfüllt |  |  |
|                   |                                                                                                                                                                                                                                       |        |      |     |               |  |  |

### <span id="page-36-0"></span>9 Übergreifende Angriffsszenarien gegen ID-Verfahren

#### 9.1 Relevanz

| Schutzziele:                   | Existenz<br>Legitimität<br>Eindeutigkeit                                                                                                         |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Beispiele für Verfahrenstypen: | "VideoIdent"<br>"PhotoIdent"<br>Verfahren mit unmittelbarer Anwesenheit (z.B. PostIdent)<br>Verfahren mit Online-Ausweisfunktion des PA oder eAT |

#### 9.2 Globale Angriffsszenarien

<span id="page-36-1"></span>

| PrüfKrit-ID               | A7.G-1                                                                                                                                                             |        |      |     |               |  |  |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------|-----|---------------|--|--|
| PrüfKrit<br>Beschreibung: | Wie lautet das minimale Vertrauensniveau für das gesamte ID-Verfahren, welches sich<br>aus der Bewertung der Angriffspotentiale globaler Angriffsszenarien ergibt? |        |      |     |               |  |  |
| Referenz                  | ergänzend zur [TR-03147]                                                                                                                                           |        |      |     |               |  |  |
| Dokumentation:            |                                                                                                                                                                    |        |      |     |               |  |  |
| Interviewpartner:         |                                                                                                                                                                    |        |      |     |               |  |  |
| Prüfaktivität:            |                                                                                                                                                                    |        |      |     |               |  |  |
| Analyse:                  |                                                                                                                                                                    |        |      |     |               |  |  |
| Bewertung:                | Normal                                                                                                                                                             | Subst. | Hoch | N/A | Nicht erfüllt |  |  |
|                           |                                                                                                                                                                    |        |      |     |               |  |  |

### <span id="page-37-0"></span>Literaturverzeichnis

TR-03147 Bundesamt für Sicherheit in der Informationstechnik: Technische Richtlinie TR-03147 Vertrauensniveaubewertung von Verfahren zur Identitätsprüfung natürlicher Personen, Version 1.0.6 AnfKat Bundesamt für Sicherheit in der Informationstechnik: Anforderungskatalog zur Prüfung

von Identifikationsverfahren gemäß TR-03147 in Version 1.0.6
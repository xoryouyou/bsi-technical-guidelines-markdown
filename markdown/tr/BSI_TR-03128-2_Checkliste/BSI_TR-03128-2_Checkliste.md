Prüfanforderungen für Konformitätsprüfungen nach BSI TR-03128-2 in Version 1.0.0 vom 25.10.2017 

07.02.2018 

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn Tel.: +49 22899 9582-0 E-Mail: eid@bsi.bund.de Internet: https://www.bsi.bund.de © Bundesamt für Sicherheit in der Informationstechnik 2018 

Inhaltsverzeichnis 

## Inhaltsverzeichnis 

|1|Einleitung............................................................................................................................................................................................... 5|
|---|---|
|2|Prüfanforderungen aus [TR-03128-2].......................................................................................................................................6|
|2.1|Allgemeine Prüfanforderungen für alle Diensteanbieter...........................................................................6|
|2.2|Besondere Prüfanforderungen für Vor-Ort-Anbieter......................................................................................7|
|2.3|Besondere Prüfanforderungen für Identifzierungsdiensteanbieter...................................................8|
||Literaturverzeichnis........................................................................................................................................................................ 10|



Bundesamt für Sicherheit in der Informationstechnik 

3 

Einleitung 1 

## 1 Einleitung 

Dieses Dokument gibt einen informativen Überblick über die Prüfanforderungen aus [TR-03128-2] in tabellarischer Form. Unmittelbare gesetzliche Anforderungen für Diensteanbieter für die eID-Funktion, insbesondere aus [PAuswG] / [PAuswV] und [BDSG] / [DSGVO] sind nicht zusätzlich aufgeführt. 

Im Rahmen der Prüfanforderungen in diesem Dokument sind bei der „eID-Infrastruktur“ genau alle Komponenten und Schnittstellen zu betrachten, die bei der zu prüfenden Stelle selbst oder Unterauftragnehmern der zu prüfenden Stelle betrieben werden. Dies schließt alle Schnittstellen zu externen Stellen ein. 

Zertifizierungen nach [TR-03128-2] haben eine Gültigkeitsdauer von 3 Jahren. Ferner erlischt die Gültigkeit eines ausgestellten Zertifikats, falls für das geforderte ISMS keine gültige Zertifizierung nach [ISO27001] oder ISO 27001 auf Basis IT-Grundschutz ([IT-GS]) mehr vorliegt. Erfolgt Anlassbezogen oder nach Ablauf von 3 Jahren eine Rezertifizierung, so ist diese nach den selben Anforderungen wie für eine initiale Zertifizierung nach [TR-03128-2] durchzuführen. 

Bundesamt für Sicherheit in der Informationstechnik 

5 

## 2 Prüfanforderungen aus [TR-03128-2] 

## 2.1 Allgemeine Prüfanforderungen für alle Diensteanbieter 

|**Referenz in**<br>**[TR-03128-2]**|**Prüfanforderung**|**Relevante Dokumente, die**<br>**bei der Prüfung**<br>**herangezogen wurden**|**Prüfmethode und weitere**<br>**Erläuterungen**|**Prüfergebnis**|
|---|---|---|---|---|
|2.1.1<br>Sicherheitskonzept|Es ist ein Sicherheitskonzept vorhanden.||||
|2.1.1<br>Sicherheitskonzept|Das Sicherheitskonzept berücksichtigt alle<br>Prozesse und Komponenten der eID-<br>Infrastruktur.||||
|2.1.3<br>eID-Server Betrieb|Die im Sicherheitskonzept beschriebenen<br>Maßnahmen zum sicheren Betrieb des<br>eID-Servers berücksichtigen die<br>Mindestanforderungen aus [TR-03130] Teil<br>2 und die Vorgaben aus [CP CVCA-eID].||||
|2.1.2<br>Informations-<br>sicherheits-<br>managementsystem|Das Sicherheitskonzept ist Bestandteil<br>eines ISMS.||||
|2.1.2<br>Informations-<br>sicherheits-<br>managementsystem;<br>2.1.4<br>Ausgelagerter Betrieb|Das ISMS umfasst alle<br>Organisationseinheiten, die operativ am<br>Betrieb der eID-Infrastruktur beteiligt<br>sind.<br>**Hinweis:**Die Anforderung gilt<br>gleichermaßen für alle Komponenten<br>deren operativer Betrieb (ganz oder<br>teilweise) an Dritte ausgelagert ist.||||
|2.1.2<br>Informations-<br>sicherheits-|Das ISMS ist nach [ISO27001] oder ISO<br>27001 auf Basis IT-Grundschutz [IT-GS]<br>zertifziert.||||



|**Referenz in**<br>**[TR-03128-2]**|**Prüfanforderung**|**Relevante Dokumente, die**<br>**bei der Prüfung**<br>**herangezogen wurden**|**Prüfmethode und weitere**<br>**Erläuterungen**|**Prüfergebnis**|
|---|---|---|---|---|
|managementsystem<br>2.1.4<br>Ausgelagerter Betrieb|**Hinweis**: Die Anforderung der<br>Zertifzierung gilt für jedes ISMS das<br>gemäß [TR-03128-2] gefordert ist.||||
|2.1.5<br>Vertraulichkeit und<br>Integrität der<br>Kommunikations-<br>schnittstellen|Für personenbezogene oder<br>personenbeziehbare Daten, die über<br>öffentliche Netze übermittelt werden, ist<br>die Vertraulichkeit und Integrität gemäß<br>den Anforderungen aus [TR-03116]<br>geschützt.||||



## 2.2 Besondere Prüfanforderungen für Vor-Ort-Anbieter 

|**Referenz in**<br>**[TR-03128-2]**|**Prüfanforderung**|**Relevante Dokumente**|**Prüfmethode und weitere**<br>**Erläuterungen**|**Prüfergebnis**|
|---|---|---|---|---|
|2.2.1<br>Identifzierung|Vor dem Auslesen des Ausweises<br>identifziert der Vor-Ort-Anbieter den<br>Ausweisinhaber sicher mittels des auf dem<br>Ausweis aufgedruckten Lichtbilds.||||
|2.2.2<br>Zustimmung|Der Vor-Ort-Anbieter holt vor dem<br>Auslesen des Ausweises die Zustimmung<br>des Ausweisinhabers dazu ein.||||
|2.2.3<br>Zugriffs-<br>beschränkung|Der Vor-Ort-Anbieter hat technisch und<br>organisatorisch sichergestellt, dass die<br>technische Funktion des Vor-Ort-<br>Auslesens nicht durch unberechtigte<br>Dritte genutzt werden kann.<br>**•**<br>Die Nutzbarkeit von Vor-Ort-<br>Zertifkaten ist auf autorisierte<br>Clients eingeschränkt<br>**•**<br>Jeder Client muss durch den eID-<br>Server eindeutig und sicher||||



|**Referenz in**<br>**[TR-03128-2]**|**Prüfanforderung**|**Relevante Dokumente**|**Prüfmethode und weitere**<br>**Erläuterungen**|**Prüfergebnis**|
|---|---|---|---|---|
||identifziert sein, bevor er<br>technisch für das Vor-Ort-<br>Auslesen genutzt werden kann||||



## 2.3 Besondere Prüfanforderungen für Identifizierungsdiensteanbieter 

|**Referenz in**<br>**[TR-03128-2]**|**Prüfanforderung**|**Relevante Dokumente**|**Prüfmethode und weitere**<br>**Erläuterungen**|**Prüfergebnis**|
|---|---|---|---|---|
|2.3.1<br>Identifzierte<br>Auftraggeber|Der Identifzierungsdiensteanbieter<br>identifziert und registriert den<br>Auftraggeber (Endverwender der Daten)<br>mit einem „hohen“ Vertrauensniveau<br>gemäß [TR-03107] Teil 1, bevor er Daten<br>an den Auftraggeber übermittelt.||||
|2.3.2<br>Datenminimierung|Der Identifzierungsdiensteanbieter gibt<br>dem Auftraggeber die Möglichkeit, die<br>abgefragten Daten auf das notwendige<br>Maß für die Anwendung zu beschränken.||||
|2.3.3<br>Sichere<br>Kommunikation<br>zum Endverwender|Der Identifzierungsdiensteanbieter stellt<br>technisch sicher, dass nur die angefragten<br>Daten an den Auftraggeber übermittelt<br>werden.||||
|2.3.3<br>Sichere<br>Kommunikation<br>zum Endverwender|Die Mechanismen für die Kommunikation<br>zwischen Identifzierungsdiensteanbieter<br>und Auftraggebern erfüllen in jedem Fall<br>Sicherheitsniveau „hoch“ gemäß [TR-<br>03107] Teil 1.<br>Falls hierbei Verfahren eingesetzt werden,<br>die in [TR-03116] Teil 4 beschrieben sind,<br>so sind die dort beschriebenen Vorgaben<br>verpfichtend umgesetzt.||||
|2.3.4|Eine Protokollierung personenbezogener||||



|**Referenz in**<br>**[TR-03128-2]**|**Prüfanforderung**|**Relevante Dokumente**|**Prüfmethode und weitere**<br>**Erläuterungen**|**Prüfergebnis**|
|---|---|---|---|---|
|Protokollierung<br>personenbezogener<br>oder<br>personenbeziehbarer<br>Daten|oder personenbeziehbarer Daten erfolgt<br>ausschließlich dann, wenn dies für den<br>Zweck der Identifzierung notwendig ist.||||
|2.3.4<br>Protokollierung<br>personenbezogener<br>oder<br>personenbeziehbarer<br>Daten|Personenbezogene oder<br>personenbeziehbare Daten aus der Online-<br>Ausweisfunktion werden nur insoweit und<br>nur solange wie technisch notwendig mit<br>Protokolldaten verknüpft.||||
|2.3.5<br>Löschpfichten für<br>Identifzierungs-<br>diensteanbieter|Personenbezogene Daten aus der Online-<br>Ausweisfunktion werden gelöscht, sobald<br>die Identifzierung abgeschlossen und<br>gegebenenfalls das elektronische Formular<br>sowie die auf Grund gesetzlicher<br>Aufzeichnungspfichten aufgezeichneten<br>Daten an den Auftraggeber übermittelt<br>wurden.||||



Literaturverzeichnis 

## Literaturverzeichnis 

BDSG Bundesdatenschutzgesetz in der Fassung der Bekanntmachung vom 14. Januar 2003 (BGBl. I S. 66), das zuletzt durch Artikel 7 des Gesetzes vom 30. Juni 2017 (BGBl. I S. 2097) geändert worden ist CP CVCA-eID BSI: Certificate Policy für die Country Verifying Certification Authority eID-Anwendung. Elektronischer Identitätsnachweis mit hoheitlichen Ausweisdokumenten DSGVO Datenschutz Grundverordnung - VERORDNUNG (EU) 2016/679 DES EUROPÄISCHEN PARLAMENTS UND DES RATES, gültig ab 25. Mai 2018 ISO27001 ISO/IEC: ISO/IEC 27001:2013 Information technology - Security techniques - Information security management systems - Requirements IT-GS BSI: IT-Grundschutz-Kataloge PAuswG Personalausweisgesetz vom 18. Juni 2009 (BGBl. I S. 1346), das zuletzt durch Artikel 4 des Gesetzes vom 18. Juli 2017 (BGBl. I S. 2745) geändert worden ist PAuswV Verordnung über Personalausweise und den elektronischen Identitätsnachweis (Personalausweisverordnung) TR-03107 BSI: TR-03107, Elektronische Identitäten und Vertrauensdienste im E-Government TR-03116 BSI: TR-03116, Kryptographische Vorgaben für Projekte der Bundesregierung TR-03128-2 BSI: TR-03128, Diensteanbieter für die eID-Funktion TR-03130 BSI: TR-03130, eID-Server 

Bundesamt für Sicherheit in der Informationstechnik 

10 


# BSI Technical Guidelines Markdown

> [!NOTE]  
> All copyright remains with the respective authors of the documents, this repoository is just a format shift to Markdown.

This repository contains all BSI technical guidelines  which are published [here](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/technische-richtlinien_node.html)

It was created out of necessity to have all TRs in one place searchable and usable in tools like (obsidian)[https://github.com/obsidianmd]

The PDFs were converted using [marker](https://github.com/VikParuchuri/marker) and [ollama](https://github.com/ollama/ollama) to markdown.



## Procedure

The python scripts can be run using `https://github.com/astral-sh/uv`
0. `uv sync`
1. `uv run scrape_pdf_links.py`
2. `uv run download_pdfs.py`
3. start an ollama server of your choice
4. `./convert.sh`

## Details
* `scrape_pdf_links.py` was used to loop over all TR pages from `data/tr-list.txt` and extract links for the PDFs on them and store them in `data/pdf_links.txt`
* `download_pdfs.py` well ... downloaded them into the `/pdf` folder.
* `convert.sh` was used to loop over all PDFs and convert them using marker and ollama

## List of all TRs contained as of `09.04.2025`
* BSI TR-01201 De-Mail
* BSI TR-02102 Kryptographische Verfahren: Empfehlungen und Schlüssellängen
* BSI TR-02103 X.509-Zertifikate und Zertifizierungspfadvalidierung
* BSI TR-03104 Produktionsdatenerfassung, -qualitätsprüfung und Übermittlung für hoheitliche Dokumente
* BSI TR-03105 Conformity Tests for Official Electronic ID Documents
* BSI TR-03106 eHealth - Zertifizierungskonzept für Karten der Generation G2
* BSI TR-03107 Elektronische Identitäten und Vertrauensdienste im E-Government
* BSI TR-03108 Sicherer E-Mail-Transport
* BSI TR-03109 Technische Vorgaben für intelligente Messsysteme und deren sicherer Betrieb
* BSI TR-03110 Advanced Security Mechanisms for Machine Readable Travel Documents and eIDAS token
* BSI TR-03111 Elliptische-Kurven-Kryptographie (ECC)
* BSI TR-03112 Das eCard-API-Framework
* BSI TR-03114 Stapelsignatur mit dem Heilberufsausweis (archiviert)
* BSI TR-03115 Komfortsignatur mit dem Heilberufsausweis (archiviert)
* BSI TR-03116 Kryptographische Vorgaben für Projekte der Bundesregierung
* BSI TR-03117 eCards mit kontaktloser Schnittstelle als sichere Signaturerstellungseinheit
* BSI TR-03118 Prüfspezifikation zur TR-PDÜ--Technische Richtlinie zur Produktionsdatenerfassung, -qualitätsprüfung und -übermittlung für Pässe
* BSI TR-03119 Requirements for Smart Card Readers Supporting eID and eSign Based on Extended Access Control
* BSI TR-03120 sichere Kartenterminalidentität (Betriebskonzept)
* BSI TR-03121 Biometrie in hoheitlichen Anwendungen
* BSI TR-03122 Konformitätstestspezifikation zur Technischen Richtlinie TR-03121 Biometrie in hoheitlichen Anwendungen
* BSI TR-03123 XML-Datenaustauschformat für hoheitliche Dokumente
* BSI TR-03124 eID-Client
* BSI TR-03125 Beweiswerterhaltung kryptographisch signierter Dokumente
* BSI TR-03126 sicherer RFID-Einsatz (TR RFID) (archiviert)
* BSI TR-03127 eID-Dokumente basierend auf Extended Access Control, Version 1.40
* BSI TR-03128 Diensteanbieter für die eID-Funktion
* BSI TR-03129 Protocols for the Management of Certificates and CRLs in Public-Key-Infrastructures (PKIs)
* BSI TR-03130 eID-Server
* BSI TR-03131 EAC--Extended Access Control-Box Architektur und Schnittstellen
* BSI TR-03132 Sichere Szenarien für Kommunikationsprozesse im Bereich hoheitlicher Dokumente
* BSI TR-03133 Prüfspezifikation zur Technischen Richtlinie BSI-TR-03132
* BSI TR-03135 Machine Authentication of MRTDs for Public Sector Applications
* BSI TR-03137
* BSI TR-03138 Ersetzendes Scannen (RESISCAN)
* BSI TR-03139 Common Certificate Policy for the Extended Access Control Infrastructure for Passports and Travel Documents issued by EU Member States
* BSI TR-03140 Conformity assessment according to the satellite data security act (TR-SatDSiG)
* BSI TR-03143 eHealth G2-COS Konsistenz-Prüftool
* BSI TR-03144 eHealth – Konformitätsnachweis für Karten-Produkte der Kartengeneration G2
* BSI TR-03145 Secure Certification Authority operation
* BSI TR-03146 Elektronische Bildübermittlung zur Beantragung hoheitlicher Dokumente (E-Bild hD)
* BSI TR-03147 Vertrauensniveaubewertung von Verfahren zur Identitätsprüfung natürlicher Personen
* BSI TR-03148 Sichere Breitband Router
* BSI TR-03150 Plan for Testing of Contactless Media and Readers for Conformance with CEN/TS 16794:2017
* BSI TR-03151 Secure Element API (SE API)
* BSI TR-03153 Technische Sicherheitseinrichtung für elektronische Aufzeichnungssysteme
* BSI TR-03154 Technische Richtlinie – BSI TR-03154 Konnektor – Prüfspezifikation für das Fachmodul NFDM
* BSI TR-03155 Technische Richtlinie – BSI TR-03155 Konnektor – Prüfspezifikation für das Fachmodul AMTS
* BSI TR-03156 Hoheitliches Identitätsmanagement mit EU-Informationssystemen
* BSI TR-03157 Konnektor – Prüfspezifikation für das Fachmodul ePA
* BSI TR-03159 Mobile Identities
* BSI TR-03160 Servicekonten
* BSI TR-03161 Anforderungen an Anwendungen im Gesundheitswesen
* BSI TR-03162 IT-sicherheitstechnische Anforderungen zur Durchführung einer Online-Wahl im Rahmen des Modellprojekts nach § 194a Fünftes Buch Sozialgesetzbuch (Online-Wahl)
* BSI TR-03163 Sicherheit in TK-Infrastrukturen
* BSI TR-03164 Guidance for Cooperative Intelligent Transport Systems (C-ITS)
* BSI TR-03165 Trusted Service Management System
* BSI TR-03166 Technical Guideline for Biometric Authentication Components in Devices for Authentication
* BSI TR-03169 IT-sicherheitstechnische Anforderungen zur Durchführung von nicht-politischen Online-Wahlen und –Abstimmungen
* BSI TR-03170 Sichere elektronische Übermittlung von Lichtbildern an die Pass-, Personalausweis- oder Ausländerbehörden
* BSI TR-03171 Optisch verifizierbarer kryptographischer Schutz von Verwaltungsdokumenten (Digitale Siegel)
* BSI TR-03172 Portalverbund
* BSI TR-03173 Amendments for Conformance Assessments based on ETSI EN--Europäische Norm 303 645/TS 103 701
* BSI TR-03174 Anforderungen an Anwendungen im Finanzwesen
* BSI TR-03175 Infrastruktur zur Absicherung von Dokumenten mit digitalen Siegeln
* BSI TR-03176 IT-Sicherheitsanforderungen an die Datenübermittlung im NOOTS
* BSI TR-03180 Kriterien- und Anforderungskatalog zur Bewertung des IT-Sicherheitsniveaus von Smartphones & Tablets
* BSI TR-03181 Cryptographic Service Provider 2 (CSP2)
* BSI TR-03182 E-Mail-Authentifizierung
* BSI TR-03183 Cyber-Resilienz-Anforderungen
* BSI TR-03184 Informationssicherheit für Weltraumsysteme
* BSI TR-03185 Sicherer Software-Lebenszyklus
* BSI TR-03191 Common Security Advisory Framework (CSAF)
* BSI TR-03209 Elektromagnetische Schirmung von Gebäuden
* BSI TR-03179-1 Central Bank Digital Currency

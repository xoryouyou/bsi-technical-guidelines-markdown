# BSI Technical Guidelines Markdown

> [!NOTE]  
> All copyright remains with the respective authors of the documents, this repoository is just a format shift to Markdown.

This repository contains all BSI technical guidelines  which are published [here](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/technische-richtlinien_node.html)

It was created out of necessity to have all TRs in one place searchable and usable in tools like [obsidian](https://github.com/obsidianmd)

The PDFs were converted using [marker](https://github.com/VikParuchuri/marker) and [ollama](https://github.com/ollama/ollama) to markdown.



## Procedure

The python env is setup using `https://github.com/astral-sh/uv`

```bash
usage: scraper.py [-h] [--scrape-pdf-list] [--output OUTPUT] [--fetch-tr-pdf-links] [--fetch-grundschutz-pdf-links]

Scraping and Conversion for BSI Technical Guidelines

options:
  -h, --help            show this help message and exit
  --scrape-pdf-list     Scrape PDF links from TR list and save to data/pdf_links.txt
  --output OUTPUT       Output directory for downloaded PDFs
  --fetch-tr-pdf-links  Extracts all the TR pages from main page and scrape the sub pages for PDF links
  --fetch-grundschutz-pdf-links
                        Fetch all the Grundschutz PDF links from the overview page
  --download-pdfs       Download all PDFs from the lists in /data

```


0. use `uv sync` - setup dependencies
1. use `uv run scraper.py --fetch-tr-pdf-links` to populate `data/tr-pdf-links.txt`
2. use `uv run scraper.py --fetch-grundschutz-pdf-links` to populate `data/grundschutz-pdf-links.txt`
3. use `uv run scraper.py --download-pdfs` to download all pdfs (note: this should do nothing since they are all present in the repo already)
4. start an ollama server of your choice
5. run `./convert.sh`
6. use `uv run generate_table.py` to generate a markdown overview at `/markdown/README.md`

## Details
* `scrape_pdf_links.py` was used to loop over all TR pages from `data/tr-list.txt` and extract links for the PDFs on them and store them in `data/pdf_links.txt`
* `download_pdfs.py` well ... downloaded them into the `/pdf` folder.
* `convert.sh` was used to loop over all PDFs and convert them using marker and ollama

## List of all IT-Grundschutz documents contained as of `10.04.2025`
* APP.1.1 Office-Produkte.pdf.clean.pdf
* APP.1.2 Webbrowser.pdf.clean.pdf
* APP.1.4 Mobile Anwendungen (Apps).pdf.clean.pdf
* APP.2.1 Allgemeiner Verzeichnisdienst.pdf.clean.pdf
* APP.2.2 Active Directory Domain Services.pdf.clean.pdf
* APP.2.3 OpenLDAP.pdf.clean.pdf
* APP.3.1 Webanwendungen und Webservices.pdf.clean.pdf
* APP.3.2 Webserver.pdf.clean.pdf
* APP.3.3 Fileserver.pdf.clean.pdf
* APP.3.4 Samba.pdf.clean.pdf
* APP.3.6 DNS-Server.pdf.clean.pdf
* APP.4.2 SAP-ERP-System.pdf.clean.pdf
* APP.4.3 Relationale Datenbanken.pdf.clean.pdf
* APP.4.4 Kubernetes.pdf.clean.pdf
* APP.4.6 SAP ABAP-Programmierung.pdf.clean.pdf
* APP.5.2 Microsoft Exchange und Outlook.pdf.clean.pdf
* APP.5.3 Allgemeiner E-Mail-Client und -Server.pdf.clean.pdf
* APP.5.4 Unified Communications und Collaboration (UCC).pdf.clean.pdf
* APP.6 Allgemeine Software.pdf.clean.pdf
* APP.7 Entwicklung von Individualsoftware.pdf.clean.pdf
* CCON.10 Entwicklung von Webanwendungen.pdf.clean.pdf
* CCON.11.1 Geheimschutz VS-NUR FÜR DEN DIENSTGEBRAUCH (VS-NfD).pdf.clean.pdf
* CCON.1 Kryptokonzept.pdf.clean.pdf
* CCON.2 Datenschutz.pdf.clean.pdf
* CCON.3 Datensicherungskonzept.pdf.clean.pdf
* CCON.6 Löschen und Vernichten.pdf.clean.pdf
* CCON.7 Informationssicherheit auf Auslandsreisen.pdf.clean.pdf
* CCON.8 Software-Entwicklung.pdf.clean.pdf
* CCON.9 Informationsaustausch.pdf.clean.pdf
* DER.1 Detektion von sicherheitsrelevanten Ereignissen.pdf.clean.pdf
* DER.2.1 Behandlung von Sicherheitsvorfällen.pdf.clean.pdf
* DER.2.2 Vorsorge für die IT-Forensik.pdf.clean.pdf
* DER.2.3 Bereinigung weitreichender Sicherheitsvorfälle.pdf.clean.pdf
* DER.3.1 Audits und Revisionen.pdf.clean.pdf
* DER.3.2 Revisionen auf Basis des Leitfadens IS-Revision.pdf.clean.pdf
* DER.4 Notfallmanagement.pdf.clean.pdf
* IND.1 Prozessleit- und Automatisierungstechnik.pdf.clean.pdf
* IND.2.1 Allgemeine ICS-Komponente.pdf.clean.pdf
* IND.2.2 Speicherprogrammierbare Steuerung (SPS).pdf.clean.pdf
* IND.2.3 Sensoren und Aktoren.pdf.clean.pdf
* IND.2.4 Maschine.pdf.clean.pdf
* IND.2.7 Safety Instrumented Systems.pdf.clean.pdf
* IND.3.2 Fernwartung im industriellen Umfeld.pdf.clean.pdf
* INF.10 Besprechungs-, Veranstaltungs- und Schulungsräume.pdf.clean.pdf
* INF.11 Allgemeines Fahrzeug.pdf.clean.pdf
* INF.12 Verkabelung.pdf.clean.pdf
* INF.13 Technisches Gebäudemanagement.pdf.clean.pdf
* INF.14 Gebäudeautomation.pdf.clean.pdf
* INF.1 Allgemeines Gebäude.pdf.clean.pdf
* INF.2 Rechenzentrum sowie Serverraum.pdf.clean.pdf
* INF.5 Raum sowie Schrank für technische Infrastruktur.pdf.clean.pdf
* INF.6 Datenträgerarchiv.pdf.clean.pdf
* INF.7 Büroarbeitsplatz.pdf.clean.pdf
* INF.8 Häuslicher Arbeitsplatz.pdf.clean.pdf
* INF.9 Mobiler Arbeitsplatz.pdf.clean.pdf
* ISMS.1 Sicherheitsmanagement.pdf.clean.pdf
* IT_Grundschutz_Kompendium_Edition2023.pd
* NET.1.1 Netzarchitektur und -design.pdf.clean.pdf
* NET.1.2 Netzmanagement.pdf.clean.pdf
* NET.2.1 WLAN-Betrieb.pdf.clean.pdf
* NET.2.2 WLAN-Nutzung.pdf.clean.pdf
* NET.3.1 Router und Switches.pdf.clean.pdf
* NET.3.2 Firewall.pdf.clean.pdf
* NET.3.3 VPN.pdf.clean.pdf
* NET.3.4 Network Access Control.pdf.clean.pdf
* NET.4.1 TK-Anlagen.pdf.clean.pdf
* NET.4.2 VoIP.pdf.clean.pdf
* NET.4.3 Faxgeräte und Faxserver.pdf.clean.pdf
* OPS.1.1.1 Allgemeiner IT-Betrieb.pdf.clean.pdf
* OPS.1.1.2 Ordnungsgemäße IT-Administration.pdf.clean.pdf
* OPS.1.1.3 Patch- und Änderungsmanagement.pdf.clean.pdf
* OPS.1.1.4 Schutz vor Schadprogrammen.pdf.clean.pdf
* OPS.1.1.5 Protokollierung.pdf.clean.pdf
* OPS.1.1.6 Software-Tests und -Freigaben.pdf.clean.pdf
* OPS.1.1.7 Systemmanagement.pdf.clean.pdf
* OPS.1.2.2 Archivierung.pdf.clean.pdf
* OPS.1.2.4 Telearbeit.pdf.clean.pdf
* OPS.1.2.5 Fernwartung.pdf.clean.pdf
* OPS.1.2.6 NTP-Zeitsynchronisation.pdf.clean.pdf
* OPS.2.2 Cloud-Nutzung.pdf.clean.pdf
* OPS.2.3 Nutzung von Outsourcing.pdf.clean.pdf
* OPS.3.2 Anbieten von Outsourcing.pdf.clean.pdf
* ORP.1 Organisation.pdf.clean.pdf
* ORP.2 Personal.pdf.clean.pdf
* ORP.3 Sensibilisierung und Schulung zur Informationssicherheit.pdf.clean.pdf
* ORP.4 Identitäts- und Berechtigungsmanagement.pdf.clean.pdf
* ORP.5 Compliance Management (Anforderungsmanagement).pdf.clean.pdf
* SYS.1.1 Allgemeiner Server.pdf.clean.pdf
* SYS.1.2.2 Windows Server 2012.pdf.clean.pdf
* SYS.1.2.3 Windows Server.pdf.clean.pdf
* SYS.1.3 Server unter Linux und Unix.pdf.clean.pdf
* SYS.1.5 Virtualisierung.pdf.clean.pdf
* SYS.1.6 Containerisierung.pdf.clean.pdf
* SYS.1.7 IBM Z.pdf.clean.pdf
* SYS.1.8 Speicherlösungen.pdf.clean.pdf
* SYS.1.9 Terminalserver.pdf.clean.pdf
* SYS.2.1 Allgemeiner Client.pdf.clean.pdf
* SYS.2.2.3 Clients unter Windows.pdf.clean.pdf
* SYS.2.3 Clients unter Linux und Unix.pdf.clean.pdf
* SYS.2.4 Clients unter macOS.pdf.clean.pdf
* SYS.2.5 Client-Virtualisierung.pdf.clean.pdf
* SYS.2.6 Virtual Desktop Infrastructure.pdf.clean.pdf
* SYS.3.1 Laptops.pdf.clean.pdf
* SYS.3.2.1 Allgemeine Smartphones und Tablets.pdf.clean.pdf
* SYS.3.2.2 Mobile Device Management (MDM).pdf.clean.pdf
* SYS.3.2.3 iOS (for Enterprise).pdf.clean.pdf
* SYS.3.2.4 Android.pdf.clean.pdf
* SYS.3.3 Mobiltelefon.pdf.clean.pdf
* SYS.4.1 Drucker, Kopierer und Multifunktionsgeräte.pdf.clean.pdf
* SYS.4.3 Eingebettete Systeme.pdf.clean.pdf
* SYS.4.4 Allgemeines IoT-Gerät.pdf.clean.pdf
* SYS.4.5 Wechseldatenträger.pdf.clean.pdf

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

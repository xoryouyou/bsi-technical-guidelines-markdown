# BSI Technical Guidelines Markdown

> [!NOTE]  
> All copyrights remain unchanged for each document as their content is unaltered, including copyright notices in these documents; this repository merely provides their format conversion from PDF to Markdown.

This repository contains all BSI technical guidelines (TRs) which are published [here](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/technische-richtlinien_node.html).

It was created out of necessity to provide all BSI TRs at a single location which can be adapted arbitrarily for them to become searchable and usable in tools like [obsidian](https://github.com/obsidianmd).  This also requires converting BSI TRs to a simple, text-based format (Markdown).

The PDFs are converted using [Marker](https://github.com/VikParuchuri/marker) and [Ollama](https://github.com/ollama/ollama) to Markdown.


## Setup

The Python env is setup using [`https://github.com/astral-sh/uv`](https://github.com/astral-sh/uv).

```bash
usage: scraper.py [-h] [--fetch-tr-pdf-links] [--fetch-grundschutz-pdf-links]
                  [--hash-pdfs] [--export-tr-links] [--sync]
                  [--sync-tr] [--sync-grundschutz] [--force]

Scraping and Conversion for BSI Technical Guidelines

options:
  -h, --help            show this help message and exit
  --fetch-tr-pdf-links  Extracts all the TR pages from main page and scrape the sub pages for PDF links
  --fetch-grundschutz-pdf-links
                        Fetch all the Grundschutz PDF links from the overview page
  --hash-pdfs           Hash all PDFs in the repository and store the checksum
  --export-tr-links     Export all TR PDF links to data/tr-pdf-links.txt
  --sync                Sync local PDFs with BSI website (check for updates and download new files)
  --sync-tr             Sync only TR PDFs with BSI website
  --sync-grundschutz    Sync only Grundschutz PDFs with BSI website
  --force               Force re-download even if file exists and checksum matches
```


### Initial Setup
```bash
# 1. Install dependencies
uv sync

# 2. Fetch PDF links from BSI website
uv run scraper.py --fetch-tr-pdf-links
uv run scraper.py --fetch-grundschutz-pdf-links

# 3. Download all PDFs
uv run scraper.py --sync

# 4. (Optional) Export TR links to text file
uv run scraper.py --export-tr-links
```

### Syncing / Mirroring
The scraper maintains a local repository (`data/repository.json`) that tracks a version history with checksums and timestamps for each change

To keep your local PDFs in sync with BSI (must have run the fetch commands from above before):
```bash
# Sync everything (TR + Grundschutz)
uv run scraper.py --sync

# Sync only TR documents
uv run scraper.py --sync-tr

# Sync only Grundschutz documents  
uv run scraper.py --sync-grundschutz

# Force re-download all files
uv run scraper.py --sync --force
```

The sync process:
1. Checks if the file exists locally
2. If not, downloads it and stores the checksum
3. If it exists, downloads from BSI and compares checksums
4. If checksums differ, adds the old version to history and saves the new file ( old version is in git history)
5. Updates `retrieved_at` timestamp on changes

#### Additional Commands
```bash
# Hash all existing local PDFs and update repository checksums
uv run scraper.py --hash-pdfs
```

### Conversion (PDF to Markdown)
After varios llm approaches using [marker](https://github.com/datalab-to/marker), [docling](https://github.com/docling-project/docling), [mineru](https://github.com/opendatalab/mineru) and others.

I chose to  [pymupdf4llm](https://github.com/pymupdf/pymupdf4llm) for now.

Simply run  `uv run convert.py` and all PDFs will be converted to markdown with extracted images next to them.

### Repository Structure
```
data/
  repository.json    # Main repository tracking all documents, checksums, and timestamps
  tr-pdf-links.txt   # Exported list of TR PDF links (URL, filename, title)
pdf/
  tr/                # Downloaded TR PDFs
  grundschutz/       # Downloaded Grundschutz PDFs
markdown/            # Converted Markdown files
```

## IT-Grundschutz Bausteine

| ID | Title | PDF | Markdown |
|:---|:------|:---:|:--------:|
| APP.1.1 | Office Produkte | [PDF](pdf/grundschutz/APP_1_1_Office_Produkte_Edition_2023.pdf) | [MD](markdown/grundschutz/APP_1_1_Office_Produkte_Edition_2023) |
| APP.1.2 | Webbrowser | [PDF](pdf/grundschutz/APP_1_2_Webbrowser_Edition_2023.pdf) | [MD](markdown/grundschutz/APP_1_2_Webbrowser_Edition_2023) |
| APP.1.4 | Mobile Anwendungen | [PDF](pdf/grundschutz/APP_1_4_Mobile_Anwendungen_Edition_2023.pdf) | [MD](markdown/grundschutz/APP_1_4_Mobile_Anwendungen_Edition_2023) |
| APP.2.1 | Allgemeiner Verzeichnisdienst | [PDF](pdf/grundschutz/APP_2_1_Allgemeiner_Verzeichnisdienst_Edition_2023.pdf) | [MD](markdown/grundschutz/APP_2_1_Allgemeiner_Verzeichnisdienst_Edition_2023) |
| APP.2.2 | Active Directory Domain Services | [PDF](pdf/grundschutz/APP_2_2_Active_Directory_Domain_Services_Edition_2023.pdf) | [MD](markdown/grundschutz/APP_2_2_Active_Directory_Domain_Services_Edition_2023) |
| APP.2.3 | OpenLDAP | [PDF](pdf/grundschutz/APP_2_3_OpenLDAP_Edition_2023.pdf) | [MD](markdown/grundschutz/APP_2_3_OpenLDAP_Edition_2023) |
| APP.3.1 | Webanwendungen und Webservices | [PDF](pdf/grundschutz/APP_3_1_Webanwendungen_und_Webservices_Edition_2023.pdf) | [MD](markdown/grundschutz/APP_3_1_Webanwendungen_und_Webservices_Edition_2023) |
| APP.3.2 | Webserver | [PDF](pdf/grundschutz/APP_3_2_Webserver_Edition_2023.pdf) | [MD](markdown/grundschutz/APP_3_2_Webserver_Edition_2023) |
| APP.3.3 | Fileserver | [PDF](pdf/grundschutz/APP_3_3_Fileserver_Edition_2023.pdf) | [MD](markdown/grundschutz/APP_3_3_Fileserver_Edition_2023) |
| APP.3.4 | Samba | [PDF](pdf/grundschutz/APP_3_4_Samba_Edition_2023.pdf) | [MD](markdown/grundschutz/APP_3_4_Samba_Edition_2023) |
| APP.3.6 | DNS Server | [PDF](pdf/grundschutz/APP_3_6_DNS_Server_Edition_2023.pdf) | [MD](markdown/grundschutz/APP_3_6_DNS_Server_Edition_2023) |
| APP.4.2 | SAP ERP System | [PDF](pdf/grundschutz/APP_4_2_SAP_ERP_System_Edition_2023.pdf) | [MD](markdown/grundschutz/APP_4_2_SAP_ERP_System_Edition_2023) |
| APP.4.3 | Relationale Datenbanksysteme | [PDF](pdf/grundschutz/APP_4_3_Relationale_Datenbanksysteme_Edition_2023.pdf) | [MD](markdown/grundschutz/APP_4_3_Relationale_Datenbanksysteme_Edition_2023) |
| APP.4.4 | Kubernetes | [PDF](pdf/grundschutz/APP_4_4_Kubernetes_Edition_2023.pdf) | [MD](markdown/grundschutz/APP_4_4_Kubernetes_Edition_2023) |
| APP.4.6 | SAP ABAP Programmierung | [PDF](pdf/grundschutz/APP_4_6_SAP_ABAP_Programmierung_Edition_2023.pdf) | [MD](markdown/grundschutz/APP_4_6_SAP_ABAP_Programmierung_Edition_2023) |
| APP.5.2 | Microsoft Exchange und Outlook | [PDF](pdf/grundschutz/APP_5_2_Microsoft_Exchange_und_Outlook_Edition_2023.pdf) | [MD](markdown/grundschutz/APP_5_2_Microsoft_Exchange_und_Outlook_Edition_2023) |
| APP.5.3 | Allgemeiner E-Mail Client und Server | [PDF](pdf/grundschutz/APP_5_3_Allgemeiner_E-Mail_Client_und_Server_Edition_2023.pdf) | [MD](markdown/grundschutz/APP_5_3_Allgemeiner_E-Mail_Client_und_Server_Edition_2023) |
| APP.5.4 | Unified Communications und Collaboration | [PDF](pdf/grundschutz/APP_5_4_Unified_Communications_und_Collaboration_Edition_2023.pdf) | [MD](markdown/grundschutz/APP_5_4_Unified_Communications_und_Collaboration_Edition_2023) |
| APP.6 | Allgemeine Software | [PDF](pdf/grundschutz/APP_6_Allgemeine_Software_Edition_2023.pdf) | [MD](markdown/grundschutz/APP_6_Allgemeine_Software_Edition_2023) |
| APP.7 | Entwicklung von Individualsoftware | [PDF](pdf/grundschutz/APP_7_Entwicklung_von_Individualsoftware_Edition_2023.pdf) | [MD](markdown/grundschutz/APP_7_Entwicklung_von_Individualsoftware_Edition_2023) |
| CON.10 | Entwicklung von Webanwendungen | [PDF](pdf/grundschutz/CON_10_Entwicklung_von_Webanwendungen_Edition_2023.pdf) | [MD](markdown/grundschutz/CON_10_Entwicklung_von_Webanwendungen_Edition_2023) |
| CON.11.1 | Geheimschutz | [PDF](pdf/grundschutz/CON_11_1_Geheimschutz_Edition_2023.pdf) | [MD](markdown/grundschutz/CON_11_1_Geheimschutz_Edition_2023) |
| CON.1 | Kryptokonzept | [PDF](pdf/grundschutz/CON_1_Kryptokonzept_Edition_2023.pdf) | [MD](markdown/grundschutz/CON_1_Kryptokonzept_Edition_2023) |
| CON.2 | Datenschutz | [PDF](pdf/grundschutz/CON_2_Datenschutz_Edition_2023.pdf) | [MD](markdown/grundschutz/CON_2_Datenschutz_Edition_2023) |
| CON.3 | Datensicherungskonzept | [PDF](pdf/grundschutz/CON_3_Datensicherungskonzept_Edition_2023.pdf) | [MD](markdown/grundschutz/CON_3_Datensicherungskonzept_Edition_2023) |
| CON.6 | Loeschen und Vernichten | [PDF](pdf/grundschutz/CON_6_Loeschen_und_Vernichten_Edition_2023.pdf) | [MD](markdown/grundschutz/CON_6_Loeschen_und_Vernichten_Edition_2023) |
| CON.7 | Informationssicherheit auf Auslandsreisen | [PDF](pdf/grundschutz/CON_7_Informationssicherheit_auf_Auslandsreisen_Edition_2023.pdf) | [MD](markdown/grundschutz/CON_7_Informationssicherheit_auf_Auslandsreisen_Edition_2023) |
| CON.8 | Software Entwicklung | [PDF](pdf/grundschutz/CON_8_Software_Entwicklung_Edition_2023.pdf) | [MD](markdown/grundschutz/CON_8_Software_Entwicklung_Edition_2023) |
| CON.9 | Informationsaustausch | [PDF](pdf/grundschutz/CON_9_Informationsaustausch_Edition_2023.pdf) | [MD](markdown/grundschutz/CON_9_Informationsaustausch_Edition_2023) |
| DER.1 | Detektion von sicherheitsrelevanten Ereignissen | [PDF](pdf/grundschutz/DER_1_Detektion_von_sicherheitsrelevanten_Ereignissen_Edition_2023.pdf) | [MD](markdown/grundschutz/DER_1_Detektion_von_sicherheitsrelevanten_Ereignissen_Edition_2023) |
| DER.2.1 | Behandlung von Sicherheitsvorfaellen | [PDF](pdf/grundschutz/DER_2_1_Behandlung_von_Sicherheitsvorfaellen_Edition_2023.pdf) | [MD](markdown/grundschutz/DER_2_1_Behandlung_von_Sicherheitsvorfaellen_Edition_2023) |
| DER.2.2 | Vorsorge fuer die IT Forensik | [PDF](pdf/grundschutz/DER_2_2_Vorsorge_fuer_die_IT_Forensik_2023.pdf) | [MD](markdown/grundschutz/DER_2_2_Vorsorge_fuer_die_IT_Forensik_2023) |
| DER.2.3 | Bereinigung weitreichender Sicherheitsvorfaelle | [PDF](pdf/grundschutz/DER_2_3_Bereinigung_weitreichender_Sicherheitsvorfaelle_Edition_2023.pdf) | [MD](markdown/grundschutz/DER_2_3_Bereinigung_weitreichender_Sicherheitsvorfaelle_Edition_2023) |
| DER.3.1 | Audits und Revisionen | [PDF](pdf/grundschutz/DER_3_1_Audits_und_Revisionen_Edition_2023.pdf) | [MD](markdown/grundschutz/DER_3_1_Audits_und_Revisionen_Edition_2023) |
| DER.3.2 | Revisionen auf Basis des Leitfadens IS Revision | [PDF](pdf/grundschutz/DER_3_2_Revisionen_auf_Basis_des_Leitfadens_IS_Revision_Edition_2023.pdf) | [MD](markdown/grundschutz/DER_3_2_Revisionen_auf_Basis_des_Leitfadens_IS_Revision_Edition_2023) |
| DER.4 | Notfallmanagement | [PDF](pdf/grundschutz/DER_4_Notfallmanagement_Edition_2023.pdf) | [MD](markdown/grundschutz/DER_4_Notfallmanagement_Edition_2023) |
| IND.1 | Prozessleit und Automatisierungstechnik | [PDF](pdf/grundschutz/IND_1_Prozessleit_und_Automatisierungstechnik_Edition_2023.pdf) | [MD](markdown/grundschutz/IND_1_Prozessleit_und_Automatisierungstechnik_Edition_2023) |
| IND.2.1 | Allgemeine ICS Komponente | [PDF](pdf/grundschutz/IND_2_1_Allgemeine_ICS_Komponente_Edition_2023.pdf) | [MD](markdown/grundschutz/IND_2_1_Allgemeine_ICS_Komponente_Edition_2023) |
| IND.2.2 | Speicherprogrammierbare Steuerung | [PDF](pdf/grundschutz/IND_2_2_Speicherprogrammierbare_Steuerung_Edition_2023.pdf) | [MD](markdown/grundschutz/IND_2_2_Speicherprogrammierbare_Steuerung_Edition_2023) |
| IND.2.3 | Sensoren und Aktoren | [PDF](pdf/grundschutz/IND_2_3_Sensoren_und_Aktoren_Edition_2023.pdf) | [MD](markdown/grundschutz/IND_2_3_Sensoren_und_Aktoren_Edition_2023) |
| IND.2.4 | Maschine | [PDF](pdf/grundschutz/IND_2_4_Maschine_Edition_2023.pdf) | [MD](markdown/grundschutz/IND_2_4_Maschine_Edition_2023) |
| IND.2.7 | Safety Instrumented Systems | [PDF](pdf/grundschutz/IND_2_7_Safety_Instrumented_Systems_Edition_2023.pdf) | [MD](markdown/grundschutz/IND_2_7_Safety_Instrumented_Systems_Edition_2023) |
| IND.3.2 | Fernwartung im industriellen Umfeld | [PDF](pdf/grundschutz/IND_3_2_Fernwartung_im_industriellen_Umfeld_Edition_2023.pdf) | [MD](markdown/grundschutz/IND_3_2_Fernwartung_im_industriellen_Umfeld_Edition_2023) |
| INF.10 | Besprechungs Veranstaltungs und Schulungsraeume | [PDF](pdf/grundschutz/INF_10_Besprechungs_Veranstaltungs_und_Schulungsraeume_Edition_2023.pdf) | [MD](markdown/grundschutz/INF_10_Besprechungs_Veranstaltungs_und_Schulungsraeume_Edition_2023) |
| INF.11 | Allgemeines Fahrzeug | [PDF](pdf/grundschutz/INF_11_Allgemeines_Fahrzeug_2023.pdf) | [MD](markdown/grundschutz/INF_11_Allgemeines_Fahrzeug_2023) |
| INF.12 | Verkabelung | [PDF](pdf/grundschutz/INF_12_Verkabelung_2023.pdf) | [MD](markdown/grundschutz/INF_12_Verkabelung_2023) |
| INF.13 | Technisches Gebaeudemanagement | [PDF](pdf/grundschutz/INF_13_Technisches_Gebaeudemanagement_Edition_2023.pdf) | [MD](markdown/grundschutz/INF_13_Technisches_Gebaeudemanagement_Edition_2023) |
| INF.14 | Gebaeudeautomation | [PDF](pdf/grundschutz/INF_14_Gebaeudeautomation_Edition_2023.pdf) | [MD](markdown/grundschutz/INF_14_Gebaeudeautomation_Edition_2023) |
| INF.1 | Allgemeines Gebaeude | [PDF](pdf/grundschutz/INF_1_Allgemeines_Gebaeude_Edition_2023.pdf) | [MD](markdown/grundschutz/INF_1_Allgemeines_Gebaeude_Edition_2023) |
| INF.2 | Rechenzentrum sowie Serverraum | [PDF](pdf/grundschutz/INF_2_Rechenzentrum_sowie_Serverraum_Edition_2023.pdf) | [MD](markdown/grundschutz/INF_2_Rechenzentrum_sowie_Serverraum_Edition_2023) |
| INF.5 | Raum sowie Schrank fuer technische Infrastruktur | [PDF](pdf/grundschutz/INF_5_Raum_sowie_Schrank_fuer_technische_Infrastruktur_Edition_2023.pdf) | [MD](markdown/grundschutz/INF_5_Raum_sowie_Schrank_fuer_technische_Infrastruktur_Edition_2023) |
| INF.6 | Datentraegerarchiv | [PDF](pdf/grundschutz/INF_6_Datentraegerarchiv_Edition_2023.pdf) | [MD](markdown/grundschutz/INF_6_Datentraegerarchiv_Edition_2023) |
| INF.7 | Bueroarbeitsplatz | [PDF](pdf/grundschutz/INF_7_Bueroarbeitsplatz_Edition_2023.pdf) | [MD](markdown/grundschutz/INF_7_Bueroarbeitsplatz_Edition_2023) |
| INF.8 | Haeuslicher Arbeitsplatz | [PDF](pdf/grundschutz/INF_8_Haeuslicher_Arbeitsplatz_Edition_2023.pdf) | [MD](markdown/grundschutz/INF_8_Haeuslicher_Arbeitsplatz_Edition_2023) |
| INF.9 | IT Mobiler Arbeitsplatz | [PDF](pdf/grundschutz/INF_9_IT_Mobiler_Arbeitsplatz_Edition_2023.pdf) | [MD](markdown/grundschutz/INF_9_IT_Mobiler_Arbeitsplatz_Edition_2023) |
| ISMS.1 | Sicherheitsmanagement | [PDF](pdf/grundschutz/ISMS_1_Sicherheitsmanagement_Edition_2023.pdf) | [MD](markdown/grundschutz/ISMS_1_Sicherheitsmanagement_Edition_2023) |
| NET.1.1 | Netzarchitektur und design | [PDF](pdf/grundschutz/NET_1_1_Netzarchitektur_und_design_Edition_2023.pdf) | [MD](markdown/grundschutz/NET_1_1_Netzarchitektur_und_design_Edition_2023) |
| NET.1.2 | Netzmanagement | [PDF](pdf/grundschutz/NET_1_2_Netzmanagement_Edition_2023.pdf) | [MD](markdown/grundschutz/NET_1_2_Netzmanagement_Edition_2023) |
| NET.2.1 | WLAN Betrieb | [PDF](pdf/grundschutz/NET_2_1_WLAN_Betrieb_Edition_2023.pdf) | [MD](markdown/grundschutz/NET_2_1_WLAN_Betrieb_Edition_2023) |
| NET.2.2 | WLAN Nutzung | [PDF](pdf/grundschutz/NET_2_2_WLAN_Nutzung_Edition_2023.pdf) | [MD](markdown/grundschutz/NET_2_2_WLAN_Nutzung_Edition_2023) |
| NET.3.1 | Router und Switches | [PDF](pdf/grundschutz/NET_3_1_Router_und_Switches_Edition_2023.pdf) | [MD](markdown/grundschutz/NET_3_1_Router_und_Switches_Edition_2023) |
| NET.3.2 | Firewall | [PDF](pdf/grundschutz/NET_3_2_Firewall_Edition_2023.pdf) | [MD](markdown/grundschutz/NET_3_2_Firewall_Edition_2023) |
| NET.3.3 | VPN | [PDF](pdf/grundschutz/NET_3_3_VPN_Edition_2023.pdf) | [MD](markdown/grundschutz/NET_3_3_VPN_Edition_2023) |
| NET.3.4 | Network Access Control | [PDF](pdf/grundschutz/NET_3_4_Network_Access_Control_Edition_2023.pdf) | [MD](markdown/grundschutz/NET_3_4_Network_Access_Control_Edition_2023) |
| NET.4.1 | TK Anlagen | [PDF](pdf/grundschutz/NET_4_1_TK_Anlagen_Edition_2023.pdf) | [MD](markdown/grundschutz/NET_4_1_TK_Anlagen_Edition_2023) |
| NET.4.2 | VoIP | [PDF](pdf/grundschutz/NET_4_2_VoIP_Edition_2023.pdf) | [MD](markdown/grundschutz/NET_4_2_VoIP_Edition_2023) |
| NET.4.3 | Faxgeraete und Faxserver | [PDF](pdf/grundschutz/NET_4_3_Faxgeraete_und_Faxserver_Edition_2023.pdf) | [MD](markdown/grundschutz/NET_4_3_Faxgeraete_und_Faxserver_Edition_2023) |
| OPS.1.1.1 | Allgemeiner IT Betrieb | [PDF](pdf/grundschutz/OPS_1_1_1_Allgemeiner_IT_Betrieb_Edition_2023.pdf) | [MD](markdown/grundschutz/OPS_1_1_1_Allgemeiner_IT_Betrieb_Edition_2023) |
| OPS.1.1.2 | Ordnungsgemaesse IT Administration | [PDF](pdf/grundschutz/OPS_1_1_2_Ordnungsgemaesse_IT_Administration_Edition_2023.pdf) | [MD](markdown/grundschutz/OPS_1_1_2_Ordnungsgemaesse_IT_Administration_Edition_2023) |
| OPS.1.1.3 | Patch und Aenderungsmanagement | [PDF](pdf/grundschutz/OPS_1_1_3_Patch_und_Aenderungsmanagement_Edition_2023.pdf) | [MD](markdown/grundschutz/OPS_1_1_3_Patch_und_Aenderungsmanagement_Edition_2023) |
| OPS.1.1.4 | Schutz vor Schadprogrammen | [PDF](pdf/grundschutz/OPS_1_1_4_Schutz_vor_Schadprogrammen_Edition_2023.pdf) | [MD](markdown/grundschutz/OPS_1_1_4_Schutz_vor_Schadprogrammen_Edition_2023) |
| OPS.1.1.5 | Protokollierung | [PDF](pdf/grundschutz/OPS_1_1_5_Protokollierung_Edition_2023.pdf) | [MD](markdown/grundschutz/OPS_1_1_5_Protokollierung_Edition_2023) |
| OPS.1.1.6 | Software Tests und Freigaben | [PDF](pdf/grundschutz/OPS_1_1_6_Software_Tests_und_Freigaben_Edition_2023.pdf) | [MD](markdown/grundschutz/OPS_1_1_6_Software_Tests_und_Freigaben_Edition_2023) |
| OPS.1.1.7 | Systemmanagement | [PDF](pdf/grundschutz/OPS_1_1_7_Systemmanagement_Edition_2023.pdf) | [MD](markdown/grundschutz/OPS_1_1_7_Systemmanagement_Edition_2023) |
| OPS.1.2.2 | Archivierung | [PDF](pdf/grundschutz/OPS_1_2_2_Archivierung_Edition_2023.pdf) | [MD](markdown/grundschutz/OPS_1_2_2_Archivierung_Edition_2023) |
| OPS.1.2.4 | Telearbeit | [PDF](pdf/grundschutz/OPS_1_2_4_Telearbeit_Edition_2023.pdf) | [MD](markdown/grundschutz/OPS_1_2_4_Telearbeit_Edition_2023) |
| OPS.1.2.5 | Fernwartung | [PDF](pdf/grundschutz/OPS_1_2_5_Fernwartung_Edition_2023.pdf) | [MD](markdown/grundschutz/OPS_1_2_5_Fernwartung_Edition_2023) |
| OPS.1.2.6 | NTP Zeitsynchronisation | [PDF](pdf/grundschutz/OPS_1_2_6_NTP_Zeitsynchronisation_Edition_2023.pdf) | [MD](markdown/grundschutz/OPS_1_2_6_NTP_Zeitsynchronisation_Edition_2023) |
| OPS.2.2 | Cloud-Nutzung | [PDF](pdf/grundschutz/OPS_2_2_Cloud-Nutzung_Edition_2023.pdf) | [MD](markdown/grundschutz/OPS_2_2_Cloud-Nutzung_Edition_2023) |
| OPS.2.3 | Nutzung von Outsourcing | [PDF](pdf/grundschutz/OPS_2_3_Nutzung_von_Outsourcing_Edition_2023.pdf) | [MD](markdown/grundschutz/OPS_2_3_Nutzung_von_Outsourcing_Edition_2023) |
| OPS.3.2 | Anbieten von Outsourcing | [PDF](pdf/grundschutz/OPS_3_2_Anbieten_von_Outsourcing_Edition_2023.pdf) | [MD](markdown/grundschutz/OPS_3_2_Anbieten_von_Outsourcing_Edition_2023) |
| ORP.1 | Organisation | [PDF](pdf/grundschutz/ORP_1_Organisation_Edition_2023.pdf) | [MD](markdown/grundschutz/ORP_1_Organisation_Edition_2023) |
| ORP.2 | Personal | [PDF](pdf/grundschutz/ORP_2_Personal_Editon_2023.pdf) | [MD](markdown/grundschutz/ORP_2_Personal_Editon_2023) |
| ORP.3 | Sensibilisierung und Schulung | [PDF](pdf/grundschutz/ORP_3_Sensibilisierung_und_Schulung_Editon_2023.pdf) | [MD](markdown/grundschutz/ORP_3_Sensibilisierung_und_Schulung_Editon_2023) |
| ORP.4 | Identitaets und Berechtigungsmanagement | [PDF](pdf/grundschutz/ORP_4_Identitaets_und_Berechtigungsmanagement_Editon_2023.pdf) | [MD](markdown/grundschutz/ORP_4_Identitaets_und_Berechtigungsmanagement_Editon_2023) |
| ORP.5 | Compliance Management | [PDF](pdf/grundschutz/ORP_5_Compliance_Management_Editon_2023.pdf) | [MD](markdown/grundschutz/ORP_5_Compliance_Management_Editon_2023) |
| SYS.1.1 | Allgemeiner Server | [PDF](pdf/grundschutz/SYS_1_1_Allgemeiner_Server_Edition_2023.pdf) | [MD](markdown/grundschutz/SYS_1_1_Allgemeiner_Server_Edition_2023) |
| SYS.1.2.2 | Windows Server 2012 | [PDF](pdf/grundschutz/SYS_1_2_2_Windows_Server_2012_Edition_2023.pdf) | [MD](markdown/grundschutz/SYS_1_2_2_Windows_Server_2012_Edition_2023) |
| SYS.1.2.3 | Windows Server | [PDF](pdf/grundschutz/SYS_1_2_3_Windows_Server_Edition_2023.pdf) | [MD](markdown/grundschutz/SYS_1_2_3_Windows_Server_Edition_2023) |
| SYS.1.3 | Server unter Linux und Unix | [PDF](pdf/grundschutz/SYS_1_3_Server_unter_Linux_und_Unix_Edition_2023.pdf) | [MD](markdown/grundschutz/SYS_1_3_Server_unter_Linux_und_Unix_Edition_2023) |
| SYS.1.5 | Virtualisierung | [PDF](pdf/grundschutz/SYS_1_5_Virtualisierung_Edition_2023.pdf) | [MD](markdown/grundschutz/SYS_1_5_Virtualisierung_Edition_2023) |
| SYS.1.6 | Containerisierung | [PDF](pdf/grundschutz/SYS_1_6_Containerisierung_Edition_2023.pdf) | [MD](markdown/grundschutz/SYS_1_6_Containerisierung_Edition_2023) |
| SYS.1.7 | IBM Z | [PDF](pdf/grundschutz/SYS_1_7_IBM_Z_Edition_2023.pdf) | [MD](markdown/grundschutz/SYS_1_7_IBM_Z_Edition_2023) |
| SYS.1.8 | Speicherloesungen | [PDF](pdf/grundschutz/SYS_1_8_Speicherloesungen_Edition_2023.pdf) | [MD](markdown/grundschutz/SYS_1_8_Speicherloesungen_Edition_2023) |
| SYS.1.9 | Terminalserver | [PDF](pdf/grundschutz/SYS_1_9_Terminalserver_Edition_2023.pdf) | [MD](markdown/grundschutz/SYS_1_9_Terminalserver_Edition_2023) |
| SYS.2.1 | Allgemeiner Client | [PDF](pdf/grundschutz/SYS_2_1_Allgemeiner_Client_Edition_2023.pdf) | [MD](markdown/grundschutz/SYS_2_1_Allgemeiner_Client_Edition_2023) |
| SYS.2.2.3 | Clients unter Windows | [PDF](pdf/grundschutz/SYS_2_2_3_Clients_unter_Windows_Edition_2023.pdf) | [MD](markdown/grundschutz/SYS_2_2_3_Clients_unter_Windows_Edition_2023) |
| SYS.2.3 | Clients unter Linux und Unix | [PDF](pdf/grundschutz/SYS_2_3_Clients_unter_Linux_und_Unix_Edition_2023.pdf) | [MD](markdown/grundschutz/SYS_2_3_Clients_unter_Linux_und_Unix_Edition_2023) |
| SYS.2.4 | Clients unter macOS | [PDF](pdf/grundschutz/SYS_2_4_Clients_unter_macOS_Edition_2023.pdf) | [MD](markdown/grundschutz/SYS_2_4_Clients_unter_macOS_Edition_2023) |
| SYS.2.5 | Client Virtualisierung | [PDF](pdf/grundschutz/SYS_2_5_Client_Virtualisierung_Edition_2023.pdf) | [MD](markdown/grundschutz/SYS_2_5_Client_Virtualisierung_Edition_2023) |
| SYS.2.6 | Virtual Desktop Infrastructure | [PDF](pdf/grundschutz/SYS_2_6_Virtual_Desktop_Infrastructure_Edition_2023.pdf) | [MD](markdown/grundschutz/SYS_2_6_Virtual_Desktop_Infrastructure_Edition_2023) |
| SYS.3.1 | Laptops | [PDF](pdf/grundschutz/SYS_3_1_Laptops_Edition_2023.pdf) | [MD](markdown/grundschutz/SYS_3_1_Laptops_Edition_2023) |
| SYS.3.2.1 | Allgemeine Smartphones und Tablets | [PDF](pdf/grundschutz/SYS_3_2_1_Allgemeine_Smartphones_und_Tablets_Edition_2023.pdf) | [MD](markdown/grundschutz/SYS_3_2_1_Allgemeine_Smartphones_und_Tablets_Edition_2023) |
| SYS.3.2.2 | Mobile Device Management | [PDF](pdf/grundschutz/SYS_3_2_2_Mobile_Device_Management_Edition_2023.pdf) | [MD](markdown/grundschutz/SYS_3_2_2_Mobile_Device_Management_Edition_2023) |
| SYS.3.2.3 | iOS for Enterprise | [PDF](pdf/grundschutz/SYS_3_2_3_iOS_for_Enterprise_2023.pdf) | [MD](markdown/grundschutz/SYS_3_2_3_iOS_for_Enterprise_2023) |
| SYS.3.2.4 | Android | [PDF](pdf/grundschutz/SYS_3_2_4_Android_Edition_2023.pdf) | [MD](markdown/grundschutz/SYS_3_2_4_Android_Edition_2023) |
| SYS.3.3 | Mobiltelefon | [PDF](pdf/grundschutz/SYS_3_3_Mobiltelefon_Edition_2023.pdf) | [MD](markdown/grundschutz/SYS_3_3_Mobiltelefon_Edition_2023) |
| SYS.4.1 | Drucker Kopierer und Multifunktionsgeraete | [PDF](pdf/grundschutz/SYS_4_1_Drucker_Kopierer_und_Multifunktionsgeraete_Edition_2023.pdf) | [MD](markdown/grundschutz/SYS_4_1_Drucker_Kopierer_und_Multifunktionsgeraete_Edition_2023) |
| SYS.4.3 | Eingebettete Systeme | [PDF](pdf/grundschutz/SYS_4_3_Eingebettete_Systeme_Edition_2023.pdf) | [MD](markdown/grundschutz/SYS_4_3_Eingebettete_Systeme_Edition_2023) |
| SYS.4.4 | Allgemeines IoT Geraet | [PDF](pdf/grundschutz/SYS_4_4_Allgemeines_IoT_Geraet_Edition_2023.pdf) | [MD](markdown/grundschutz/SYS_4_4_Allgemeines_IoT_Geraet_Edition_2023) |
| SYS.4.5 | Wechseldatentraeger | [PDF](pdf/grundschutz/SYS_4_5_Wechseldatentraeger_Edition_2023.pdf) | [MD](markdown/grundschutz/SYS_4_5_Wechseldatentraeger_Edition_2023) |

## Technical Guidelines (TRs)

| TR | Title | PDF | Markdown |
|:---|:------|:---:|:--------:|
| TR-01201 | Technische Richtline De-Mail | [PDF](pdf/tr/TR_De_Mail.pdf) | [MD](markdown/tr/TR_De_Mail) |
| TR-01201 | Technische Richtlinie De-Mail IT-Basisinfrastruktur Modul | [PDF](pdf/tr/TR_De_Mail_IT-Binfra_M.pdf) | [MD](markdown/tr/TR_De_Mail_IT-Binfra_M) |
| TR-01201 | Technische Richtlinie De-Mail IT-Basisinfrastruktur Funktionalitätsspezifikation | [PDF](pdf/tr/TR_De_Mail_IT-Binfra_FU.pdf) | [MD](markdown/tr/TR_De_Mail_IT-Binfra_FU) |
| TR-01201 | Technische Richlinie De-Mail IT-Basisinfrastruktur IT-Sicherheit | [PDF](pdf/tr/TR_De_Mail_IT-Binfra_Si.pdf) | [MD](markdown/tr/TR_De_Mail_IT-Binfra_Si) |
| TR-01201 | Technische Richlinie De-Mail IT-Basisinfrastruktur Interoperabilitätsspezifikation | [PDF](pdf/tr/TR_De_Mail_IT-Binfra_IO.pdf) | [MD](markdown/tr/TR_De_Mail_IT-Binfra_IO) |
| TR-01201 | Technische Richtlinie De-Mail Postfach- und Versanddienst Modul | [PDF](pdf/tr/TR_De_Mail_PVD_M.pdf) | [MD](markdown/tr/TR_De_Mail_PVD_M) |
| TR-01201 | Technische Richtlinie De-Mail Postfach- und Versanddienst Funktionalitätsspezifikation | [PDF](pdf/tr/TR_De_Mail_PVD_FU.pdf) | [MD](markdown/tr/TR_De_Mail_PVD_FU) |
| TR-01201 | Technische Richlinie De-Mail Postfach- und Versanddienst IT-Sicherheit | [PDF](pdf/tr/TR_De_Mail_PVD_Si.pdf) | [MD](markdown/tr/TR_De_Mail_PVD_Si) |
| TR-01201 | Technische Richtlinie De-Mail Postfach- und Versanddienst Interoperabilitätsspezifikation | [PDF](pdf/tr/TR_De_Mail_PVD_IO.pdf) | [MD](markdown/tr/TR_De_Mail_PVD_IO) |
| TR-01201 | Technische Richtlinie De-Mail Accountmanagement Modul | [PDF](pdf/tr/TR_De_Mail_ACM_M.pdf) | [MD](markdown/tr/TR_De_Mail_ACM_M) |
| TR-01201 | Technische Richtlinie De-Mail Accountmanagement Funktionalitätsspezifikation | [PDF](pdf/tr/TR_De_Mail_ACM_FU.pdf) | [MD](markdown/tr/TR_De_Mail_ACM_FU) |
| TR-01201 | Technische Richtline De-Mail Accountmanagement IT-Sicherheit | [PDF](pdf/tr/TR_De_Mail_ACM_Si.pdf) | [MD](markdown/tr/TR_De_Mail_ACM_Si) |
| TR-01201 | Technische Richtlinie De-Mail Dokumentenablage Modul | [PDF](pdf/tr/TR_De_Mail_DA_M.pdf) | [MD](markdown/tr/TR_De_Mail_DA_M) |
| TR-01201 | Technische Richtlinie De-Mail Dokumentenablage Funktionalitätsspezifikation | [PDF](pdf/tr/TR_De_Mail_DA_FU.pdf) | [MD](markdown/tr/TR_De_Mail_DA_FU) |
| TR-01201 | Technische Richtlinie De-Mail Dokumentenablage IT-Sicherheit | [PDF](pdf/tr/TR_De_Mail_DA_Si.pdf) | [MD](markdown/tr/TR_De_Mail_DA_Si) |
| TR-01201 | Technische Richtlinie De-Mail Identitätsbestätigungsdienst Modul | [PDF](pdf/tr/TR_De_Mail_ID_M.pdf) | [MD](markdown/tr/TR_De_Mail_ID_M) |
| TR-01201 | Technische Richtlinie De-Mail Identitätsbestätigungsdienst Funktionalitätsspezifikation | [PDF](pdf/tr/TR_De_Mail_ID_FU.pdf) | [MD](markdown/tr/TR_De_Mail_ID_FU) |
| TR-01201 | Technische Richtlinie De-Mail IT-Sicherheit Identitätsbestätigungsdienst | [PDF](pdf/tr/TR_De_Mail_ID_Si.pdf) | [MD](markdown/tr/TR_De_Mail_ID_Si) |
| TR-01201 | Technische Richtlinie De-Mail Identitätsbestätigungsdienst Interoperabilitätsspezifikation | [PDF](pdf/tr/TR_De_Mail_ID_IO.pdf) | [MD](markdown/tr/TR_De_Mail_ID_IO) |
| TR-01201 | Technische Richtlinie De-Mail Sicherheit Modulübergreifend | [PDF](pdf/tr/TR_De_Mail_IS_M.pdf) | [MD](markdown/tr/TR_De_Mail_IS_M) |
| TR-01201 | Technische Richtlinie De-Mail Informationssicherheit nach ISO27001 auf der Basis von IT-Grundschutz | [PDF](pdf/tr/TR_De_Mail_IS_GS.pdf) | [MD](markdown/tr/TR_De_Mail_IS_GS) |
| TR-01201 | Technische Richtlinie De-Mail Informationssicherheit auf Basis von ISO/IEC 27001 | [PDF](pdf/tr/TR_De_Mail_IS_27001.pdf) | [MD](markdown/tr/TR_De_Mail_IS_27001) |
| TR-02102 | Kryptographische Verfahren: Empfehlungen und Schlüssellängen, Version 2026-01 | [PDF](pdf/tr/BSI-TR-02102.pdf) | [MD](markdown/tr/BSI-TR-02102) |
| TR-02102 | Technische Richtlinie TR-02102-2: Verwendung von Transport Layer Security (TLS) | [PDF](pdf/tr/BSI-TR-02102-2.pdf) | [MD](markdown/tr/BSI-TR-02102-2) |
| TR-02102 | Technische Richtlinie TR-02102-3: Verwendung von Internet Protocol Security (IPsec) und Internet Key Exchange (IKEv2) | [PDF](pdf/tr/BSI-TR-02102-3.pdf) | [MD](markdown/tr/BSI-TR-02102-3) |
| TR-02102 | Technische Richtlinie TR-02102-4: Verwendung von Secure Shell (SSH) | [PDF](pdf/tr/BSI-TR-02102-4.pdf) | [MD](markdown/tr/BSI-TR-02102-4) |
| TR-02103 | BSI Technische Richtlinie TR-02103: X.509 Zertifikate und Zertifizierungspfadvalidierung | [PDF](pdf/tr/BSI-TR-02103.pdf) | [MD](markdown/tr/BSI-TR-02103) |
| TR-02103 | Kryptographische Verfahren: Empfehlungen und Schlüssellängen, Version 2026-01 | [PDF](pdf/tr/BSI-TR-02102.pdf) | [MD](markdown/tr/BSI-TR-02102) |
| TR-02103 | Technische Richtlinie TR-02102-2: Verwendung von Transport Layer Security (TLS) | [PDF](pdf/tr/BSI-TR-02102-2.pdf) | [MD](markdown/tr/BSI-TR-02102-2) |
| TR-02103 | Technische Richtlinie TR-02102-3: Verwendung von Internet Protocol Security (IPsec) und Internet Key Exchange (IKEv2) | [PDF](pdf/tr/BSI-TR-02102-3.pdf) | [MD](markdown/tr/BSI-TR-02102-3) |
| TR-03104 | BSI TR-03104 (TR PDÜ hD) - V3.3.0 | [PDF](pdf/tr/BSI_TR-03104-PDUhD_Version-3-3-0.pdf) | [MD](markdown/tr/BSI_TR-03104-PDUhD_Version-3-3-0) |
| TR-03104 | Elektronische Bildübermittlung unter Nutzung von De-Mail | [PDF](pdf/tr/Ergebnisdokumentation_elektr_Bilduebermittlung.pdf) | [MD](markdown/tr/Ergebnisdokumentation_elektr_Bilduebermittlung) |
| TR-03104 | Studie zur elektronischen Bildübermittlung | [PDF](pdf/tr/Studie_elek_Bilduebermittlung.pdf) | [MD](markdown/tr/Studie_elek_Bilduebermittlung) |
| TR-03105 | BSI TR-03105 Part 1.1 | [PDF](pdf/tr/TR-03105_Part1.1_V1.04.1.pdf) | [MD](markdown/tr/TR-03105_Part1.1_V1.04.1) |
| TR-03105 | BSI TR-03105 Part 1.2 | [PDF](pdf/tr/TR-03105_Part1.2_V1.02.1.pdf) | [MD](markdown/tr/TR-03105_Part1.2_V1.02.1) |
| TR-03105 | Test Plan for Official Electronic ID Documents with Secure Contactless Integrated Circuit - Part 2 | [PDF](pdf/tr/TR-03105_Part2.pdf) | [MD](markdown/tr/TR-03105_Part2) |
| TR-03105 | Test plan for eMRTD Application Protocol and Logical Data Structure - Part 3.1 | [PDF](pdf/tr/TR-03105_Part3.1.pdf) | [MD](markdown/tr/TR-03105_Part3.1) |
| TR-03105 | BSI TR-03105 Part 3.1 Version 1.2.1 | [PDF](pdf/tr/TR-03105_Part3-1_V-1-2-1.pdf) | [MD](markdown/tr/TR-03105_Part3-1_V-1-2-1) |
| TR-03105 | Test plan for eMRTDs with EACv1 - Part 3.2, V1.3 | [PDF](pdf/tr/TR-03105_Part3_2_V1_3.pdf) | [MD](markdown/tr/TR-03105_Part3_2_V1_3) |
| TR-03105 | MACHINE READABLE TRAVEL DOCUMENTS, ADVANCED SECURITY MECHANISMS FOR MACHINE READABLE TRAVEL DOCUMENTS – EXTENDED ACCESS CONTROL (EACv1), TESTS FOR SECURITY IMPLEMENTATION - Part 3.2, V1.4 | [PDF](pdf/tr/TR-03105_Part3_2_V1_4.pdf) | [MD](markdown/tr/TR-03105_Part3_2_V1_4) |
| TR-03105 | Technical Guideline TR-03105 - Conformity Tests for Official Electronic ID Documents - Part 3.2, V1.5 | [PDF](pdf/tr/TR-03105_Part3_2_V1_5.pdf) | [MD](markdown/tr/TR-03105_Part3_2_V1_5) |
| TR-03105 | Test plan for eMRTDs with Advanced Security Mechanisms – EAC 1 - Part 3.2, V1.5.1 | [PDF](pdf/tr/TR-03105_Part3_2_V1_5_1.pdf) | [MD](markdown/tr/TR-03105_Part3_2_V1_5_1) |
| TR-03105 | BSI TR-03105 Part 3.3 | [PDF](pdf/tr/TR-03105_Part3.3_V1.0.pdf) | [MD](markdown/tr/TR-03105_Part3.3_V1.0) |
| TR-03105 | Amendment to BSI TR-03105 Part 3.3 | [PDF](pdf/tr/Amendment_to_BSI_TR-03105_Part_3.3.pdf) | [MD](markdown/tr/Amendment_to_BSI_TR-03105_Part_3.3) |
| TR-03105 | Technical Guideline TR-03105 - Part 3.3 | [PDF](pdf/tr/Conformity_Tests_TR-03105_Part_3-3.pdf) | [MD](markdown/tr/Conformity_Tests_TR-03105_Part_3-3) |
| TR-03105 | BSI TR-03105 Part 3.3 Version 1.2 | [PDF](pdf/tr/Conformity_Tests_TR-03105_Part_3-3_V1-2.pdf) | [MD](markdown/tr/Conformity_Tests_TR-03105_Part_3-3_V1-2) |
| TR-03105 | Technical Guideline TR-03105 - Part 3.3, V1.4 | [PDF](pdf/tr/Conformity_Tests_TR-03105_Part_3-3_V1-4.pdf) | [MD](markdown/tr/Conformity_Tests_TR-03105_Part_3-3_V1-4) |
| TR-03105 | eSign Test Specification - Part 3.4, V1 | [PDF](pdf/tr/TR-03105_Part3.4_V1.pdf) | [MD](markdown/tr/TR-03105_Part3.4_V1) |
| TR-03105 | Technical Guideline TR-03105 - Test Plan for ICAO-compliant Proximity Coupling Devices (PCD) on Layers 1-4 - Part 4 - - Version 3.1.1 | [PDF](pdf/tr/TR-03105_Part4_V3-1.pdf) | [MD](markdown/tr/TR-03105_Part4_V3-1) |
| TR-03105 | Test Specification Comparison - ISO/IEC 10373-6:2011 vs. NFC Forum Test Specifications | [PDF](pdf/tr/TR-03105_ISO-IECvsNFC.pdf) | [MD](markdown/tr/TR-03105_ISO-IECvsNFC) |
| TR-03105 | BSI TR-03105 Part 5.1 Version 1.5 | [PDF](pdf/tr/TR-03105_Part5-1.pdf) | [MD](markdown/tr/TR-03105_Part5-1) |
| TR-03105 | Test plan for eID and eSign compliant smart card readers with integrated EACv2 - Part 5.2, V2.0 | [PDF](pdf/tr/TR-03105_Part5.2_V2.0.pdf) | [MD](markdown/tr/TR-03105_Part5.2_V2.0) |
| TR-03105 | Test plan for eID and eSign compliant terminal software with EACv2 - Part 5.3, V2.0 | [PDF](pdf/tr/TR-03105_Part5.3_V2.0.pdf) | [MD](markdown/tr/TR-03105_Part5.3_V2.0) |
| TR-03106 | Technische Richtlinie BSI TR-03106 - eHealth – Zertifizierungskonzept für Karten der Generation G2, Version 1.2 - V1.2 | [PDF](pdf/tr/TR-03106v1_2.pdf) | [MD](markdown/tr/TR-03106v1_2) |
| TR-03106 | Technische Richtlinie BSI TR-03106 - eHealth – Zertifizierungskonzept für Karten der Generation G2, Version 1.1 - V1.1 | [PDF](pdf/tr/TR-03106v1_1.pdf) | [MD](markdown/tr/TR-03106v1_1) |
| TR-03106 | Technische Richtlinie BSI TR-03106 - eHealth – Zertifizierungskonzept für Karten der Generation G2 | [PDF](pdf/tr/TR-03106.pdf) | [MD](markdown/tr/TR-03106) |
| TR-03107 | Technische Richtlinie TR-03107-1: Elektronische Identitäten und Vertrauensdienste im E-Government | [PDF](pdf/tr/TR-03107-1.pdf) | [MD](markdown/tr/TR-03107-1) |
| TR-03107 | Bewertung von Authentisierungslösungen gemäß TR-03107 in Version | [PDF](pdf/tr/TR-03107-1_Anforderungen.pdf) | [MD](markdown/tr/TR-03107-1_Anforderungen) |
| TR-03107 | Ergebnisse der Prüfung gemäß TR-03107-1 in Version | [PDF](pdf/tr/TR-03107-1_Pruefberichtsvorlage.pdf) | [MD](markdown/tr/TR-03107-1_Pruefberichtsvorlage) |
| TR-03107 | Electronic Identities and Trust Services in E-Government - Part 1 | [PDF](pdf/tr/TR03107-1.pdf) | [MD](markdown/tr/TR03107-1) |
| TR-03107 | Technische Richtlinie TR-03107-2: Elektronische Identitäten und Vertrauensdienste im E-Government | [PDF](pdf/tr/TR-03107-2.pdf) | [MD](markdown/tr/TR-03107-2) |
| TR-03108 | BSI TR-03108-1: Secure E-Mail Transport | [PDF](pdf/tr/TR03108-1.pdf) | [MD](markdown/tr/TR03108-1) |
| TR-03108 | BSI TR-03108-2: Testspecification | [PDF](pdf/tr/TR03108-2.pdf) | [MD](markdown/tr/TR03108-2) |
| TR-03108 | TR-03108 Secure Email Transport | [PDF](pdf/tr/TR03108.pdf) | [MD](markdown/tr/TR03108) |
| TR-03108 | TR-03108-P: Testspecification | [PDF](pdf/tr/TR-03108-P.pdf) | [MD](markdown/tr/TR-03108-P) |
| TR-03109 | Antrag auf Anerkennung als Prüfstelle / Zertifizierung als IT- Sicherheitsdienstleister | [PDF](pdf/tr/Antrag-Anerkennung_Zertifizierung_Stellen.pdf) | [MD](markdown/tr/Antrag-Anerkennung_Zertifizierung_Stellen) |
| TR-03110 | Advanced Security Mechanisms for Machine Readable Travel Documents and eIDAS Token - Part 1 | [PDF](pdf/tr/BSI_TR-03110_Part-1_V2-2.pdf) | [MD](markdown/tr/BSI_TR-03110_Part-1_V2-2) |
| TR-03110 | Advanced Security Mechanisms for Machine Readable Travel Documents and eIDAS Token - Part 2 | [PDF](pdf/tr/BSI_TR-03110_Part-2-V2_2.pdf) | [MD](markdown/tr/BSI_TR-03110_Part-2-V2_2) |
| TR-03110 | Advanced Security Mechanisms for Machine Readable Travel Documents and eIDAS Token - Part 3 | [PDF](pdf/tr/BSI_TR-03110_Part-3-V2_2.pdf) | [MD](markdown/tr/BSI_TR-03110_Part-3-V2_2) |
| TR-03110 | Advanced Security Mechanisms for Machine Readable Travel Documents and eIDAS Token - Part 4 | [PDF](pdf/tr/BSI_TR-03110_Part-4_V2-2.pdf) | [MD](markdown/tr/BSI_TR-03110_Part-4_V2-2) |
| TR-03110 | Technical Guideline TR-03110 | [PDF](pdf/tr/BSI_TR-03110_Amendment-Protocol-extensions_specifications.pdf) | [MD](markdown/tr/BSI_TR-03110_Amendment-Protocol-extensions_specifications) |
| TR-03110 | Advanced Security Mechanisms for Machine Readable Travel Documents - Part 1, V2.1 | [PDF](pdf/tr/BSI_TR-03110_Part-1_V2-1.pdf) | [MD](markdown/tr/BSI_TR-03110_Part-1_V2-1) |
| TR-03110 | Advanced Security Mechanisms for Machine Readable Travel Documents - Part 3, V2.1 | [PDF](pdf/tr/BSI_TR-03110_Part-3_V2-1.pdf) | [MD](markdown/tr/BSI_TR-03110_Part-3_V2-1) |
| TR-03111 | Elliptic Curve Cryptography - V2.1 | [PDF](pdf/tr/BSI-TR-03111_V-2-1_pdf.pdf) | [MD](markdown/tr/BSI-TR-03111_V-2-1_pdf) |
| TR-03111 | Elliptic Curve Cryptography - V2.0 | [PDF](pdf/tr/BSI-TR-03111_V-2-0_pdf.pdf) | [MD](markdown/tr/BSI-TR-03111_V-2-0_pdf) |
| TR-03112 | Technical Guideline TR-03112-2 | [PDF](pdf/tr/TR-03112-api_teil2.pdf) | [MD](markdown/tr/TR-03112-api_teil2) |
| TR-03112 | Technical Guideline TR-03112-3 | [PDF](pdf/tr/TR-03112-api_teil3.pdf) | [MD](markdown/tr/TR-03112-api_teil3) |
| TR-03112 | Technical Guideline TR-03112-4 | [PDF](pdf/tr/TR-03112-api_teil4.pdf) | [MD](markdown/tr/TR-03112-api_teil4) |
| TR-03112 | Technical Guideline TR-03112-7 | [PDF](pdf/tr/TR-03112-api_teil7.pdf) | [MD](markdown/tr/TR-03112-api_teil7) |
| TR-03112 | Technical Guideline TR-03112-5 | [PDF](pdf/tr/TR-03112-api_teil5.pdf) | [MD](markdown/tr/TR-03112-api_teil5) |
| TR-03112 | Technical Guideline TR-03112-6 | [PDF](pdf/tr/TR-03112-api_teil6.pdf) | [MD](markdown/tr/TR-03112-api_teil6) |
| TR-03112 | Technical Guideline TR-03112-1 | [PDF](pdf/tr/TR-03112-api_teil1.pdf) | [MD](markdown/tr/TR-03112-api_teil1) |
| TR-03112 | Technical Guideline TR-03112-1 | [PDF](pdf/tr/TR-03112-api_teil1.pdf) | [MD](markdown/tr/TR-03112-api_teil1) |
| TR-03112 | Technical Guideline TR-03112-2 | [PDF](pdf/tr/TR-03112-api_teil2.pdf) | [MD](markdown/tr/TR-03112-api_teil2) |
| TR-03112 | Technical Guideline TR-03112-3 | [PDF](pdf/tr/TR-03112-api_teil3.pdf) | [MD](markdown/tr/TR-03112-api_teil3) |
| TR-03112 | Technical Guideline TR-03112-4 | [PDF](pdf/tr/TR-03112-api_teil4.pdf) | [MD](markdown/tr/TR-03112-api_teil4) |
| TR-03112 | Technical Guideline TR-03112-5 | [PDF](pdf/tr/TR-03112-api_teil5.pdf) | [MD](markdown/tr/TR-03112-api_teil5) |
| TR-03112 | Technical Guideline TR-03112-6 | [PDF](pdf/tr/TR-03112-api_teil6.pdf) | [MD](markdown/tr/TR-03112-api_teil6) |
| TR-03112 | Technical Guideline TR-03112-7 | [PDF](pdf/tr/TR-03112-api_teil7.pdf) | [MD](markdown/tr/TR-03112-api_teil7) |
| TR-03112 | Technical Guideline TR-03112-6 - eCard-API-Framework | [PDF](pdf/tr/TR-03112-api_teil6_ergaenzung.pdf) | [MD](markdown/tr/TR-03112-api_teil6_ergaenzung) |
| TR-03112 | Technical Guideline TR-03112-7 - eCard-API-Framework | [PDF](pdf/tr/TR-03112-api_teil7_ergaenzung.pdf) | [MD](markdown/tr/TR-03112-api_teil7_ergaenzung) |
| TR-03114 | BSI TR-03114 Stapelsignatur mit dem Heilberufsausweis | [PDF](pdf/tr/BSI-TR-03114.pdf) | [MD](markdown/tr/BSI-TR-03114) |
| TR-03115 | Komfortsignatur mit dem Heilberufsausweis BSI-TR-03115 | [PDF](pdf/tr/BSI-TR-03115.pdf) | [MD](markdown/tr/BSI-TR-03115) |
| TR-03116 | BSI TR-03116-1, Kryptographische Vorgaben für Projekte der Bundesregierung, Teil 1: Telematikinfrastruktur | [PDF](pdf/tr/BSI-TR-03116.pdf) | [MD](markdown/tr/BSI-TR-03116) |
| TR-03116 | Kryptographische Vorgaben für Projekte der Bundesregierung - Teil 2 | [PDF](pdf/tr/BSI-TR-03116-2.pdf) | [MD](markdown/tr/BSI-TR-03116-2) |
| TR-03116 | TR-03116 Kryptographische Vorgaben für Projekte der Bundesregierung - Teil 3 | [PDF](pdf/tr/BSI-TR-03116-3.pdf) | [MD](markdown/tr/BSI-TR-03116-3) |
| TR-03116 | Technische Richtlinie BSI TR-03116-4 | [PDF](pdf/tr/BSI-TR-03116-4.pdf) | [MD](markdown/tr/BSI-TR-03116-4) |
| TR-03116 | TLS-Checkliste 2023 | [PDF](pdf/tr/TLS-Checkliste.pdf) | [MD](markdown/tr/TLS-Checkliste) |
| TR-03116 | Kryptographische Vorgaben für Projekte der Bundesregierung - Teil 5 | [PDF](pdf/tr/BSI-TR-03116-5.pdf) | [MD](markdown/tr/BSI-TR-03116-5) |
| TR-03116 | Technische Richtlinie BSI TR-03116-6 | [PDF](pdf/tr/BSI-TR-03116-6.pdf) | [MD](markdown/tr/BSI-TR-03116-6) |
| TR-03116 | Technical Guideline TR-03116-TS - V1 | [PDF](pdf/tr/BSI-TR-03116-TS_v1.pdf) | [MD](markdown/tr/BSI-TR-03116-TS_v1) |
| TR-03116 | Technical Guideline TR-03116-TS | [PDF](pdf/tr/BSI-TR-03116-TS_Annex.pdf) | [MD](markdown/tr/BSI-TR-03116-TS_Annex) |
| TR-03117 | Technische Richtlinie TR-03117 | [PDF](pdf/tr/BSI-TR-03117.pdf) | [MD](markdown/tr/BSI-TR-03117) |
| TR-03118 | Prüfspezifikationen zur Technische Richtlinie zur Produktionsdatenerfassung, -qualitätsprüfung und -übermittlung für Pässe Prüfspezifikation Biometrie I: Hardwarekomponenten | [PDF](pdf/tr/BSI_TR_03118-1_V2_1.pdf) | [MD](markdown/tr/BSI_TR_03118-1_V2_1) |
| TR-03118 | PS Biometrie II Prüfspezifikationen zur Technische Richtlinie zur Produktionsdatenerfassung, -qualitätsprüfung und -übermittlung für PässePrüfspezifikation Biometrie II: Softwarekomponenten BSI TR-03118-2 (PS Biometrie II)Version 2.1 | [PDF](pdf/tr/BSI_TR_03118-2_V2_1.pdf) | [MD](markdown/tr/BSI_TR_03118-2_V2_1) |
| TR-03118 | TR-PDÜ: Konformitätsprüfung XPass Prüfspezifikationen zur Technische Richtlinie zur Produktionsdatenerfassung, -qualitätsprüfung und -übermittlung für PässePrüfspezifikation XPass und Transport BSI TR-03118-3 (PS XPass) Version 2.1 | [PDF](pdf/tr/BSI_TR_03118-3_V2_1.pdf) | [MD](markdown/tr/BSI_TR_03118-3_V2_1) |
| TR-03119 | Requirements for Smart Card Readers Supporting eID and eSign based on EAC - V1 | [PDF](pdf/tr/BSI-TR-03119_V1_pdf.pdf) | [MD](markdown/tr/BSI-TR-03119_V1_pdf) |
| TR-03120 | Sichere Kartenterminalidentität, Technische Richtlinie BSI TR-03120 - V1.1 | [PDF](pdf/tr/BSI-TR-03120_V1-1.pdf) | [MD](markdown/tr/BSI-TR-03120_V1-1) |
| TR-03120 | Sichere Kartenterminalidentität (Betriebskonzept) BSI-TR-03120 - V1.0 | [PDF](pdf/tr/BSI-TR-03120_V1-0.pdf) | [MD](markdown/tr/BSI-TR-03120_V1-0) |
| TR-03121 | BSI Technical Guideline TR-03121-1 - Biometrics for Public Sector Applications - Part 1: Framework - Version 7.0 | [PDF](pdf/tr/TR-03121-1_Biometrics_7_0.pdf) | - |
| TR-03121 | BSI Technical Guideline TR-03121-2 - Biometrics for Public Sector Applications - Part 2: Software Architecture - Volume 2: High Level Biometric Services (HLBS) - Version 7.0 | [PDF](pdf/tr/TR-03121-2-2_Biometrics_7_0.pdf) | - |
| TR-03121 | BSI Technical Guideline TR-03121-3 - Biometrics for Public Sector Applications - Part 3: Application Profiles, Function Modules and Processes - Volume 1: Border Control (BCL) - Version 7.0 | [PDF](pdf/tr/TR-03121-3_1_Biometrics_7_0.pdf) | - |
| TR-03121 | BSI Technical Guideline TR-03121-3 - Biometrics for Public Sector Applications - Part 3: Application Profiles, Function Modules and Processes - Volume 2: German Identity Documents (GID) - Version 7.0 | [PDF](pdf/tr/TR-03121-3_2_Biometrics_GID_7_0.pdf) | - |
| TR-03121 | BSI Technical Guideline TR-03121-3 - Biometrics for Public Sector Applications - Part 3: Application Profiles, Function Modules and Processes - Volume 4: Alien Register Enrolment (ARE) - Version 7.0 | [PDF](pdf/tr/TR-03121-3_4_Biometrics_7_0.pdf) | - |
| TR-03121 | BSI Technical Guideline TR-03121-3 - Biometrics for Public Sector Applications - Part 3: Application Profiles, Function Modules and Processes - Volume 6: Immigration Authorities (IMA) - Version 7.0 | [PDF](pdf/tr/TR-03121-3-6_Biometrics_7_0.pdf) | - |
| TR-03121 | BSI Technical Guideline TR-03121-1 - Biometrics for Public Sector Applications - Part 1: Framework - Version 6.0 | [PDF](pdf/tr/TR-03121-1_Biometrics_6_0.pdf) | [MD](markdown/tr/TR-03121-1_Biometrics_6_0) |
| TR-03121 | BSI Technical Guideline TR-03121-2 - Biometrics for Public Sector Applications - Part 2: Software Architecture - Volume 2: High Level Biometric Services (HLBS) - Version 6.0 | [PDF](pdf/tr/TR-03121-2-2_Biometrics_6_0.pdf) | [MD](markdown/tr/TR-03121-2-2_Biometrics_6_0) |
| TR-03121 | BSI Technical Guideline TR-03121-3 - Biometrics for Public Sector Applications - Part 3: Application Profiles, Function Modules and Processes - Volume 1: Border Control (BCL) - Version 6.0 | [PDF](pdf/tr/TR-03121-3_1_Biometrics_6_0.pdf) | [MD](markdown/tr/TR-03121-3_1_Biometrics_6_0) |
| TR-03121 | BSI Technical Guideline TR-03121-3 - Biometrics for Public Sector Applications - Part 3: Application Profiles, Function Modules and Processes - Volume 2: German Identity Documents (GID) - Version 6.0 | [PDF](pdf/tr/TR-03121-3_2_Biometrics_GID_6_0.pdf) | [MD](markdown/tr/TR-03121-3_2_Biometrics_GID_6_0) |
| TR-03121 | BSI Technical Guideline TR-03121-3 - Biometrics for Public Sector Applications - Part 3: Application Profiles, Function Modules and Processes - Volume 4: Alien Register Enrolment (ARE) - Version 6.0 | [PDF](pdf/tr/TR-03121-3_4_Biometrics_6_0.pdf) | [MD](markdown/tr/TR-03121-3_4_Biometrics_6_0) |
| TR-03121 | BSI Technical Guideline TR-03121-3 - Biometrics for Public Sector Applications - Part 3: Application Profiles, Function Modules and Processes - Volume 6: Immigration Authorities (IMA) - Version 6.0 | [PDF](pdf/tr/TR-03121-3-6_Biometrics_6_0.pdf) | [MD](markdown/tr/TR-03121-3-6_Biometrics_6_0) |
| TR-03122 | Technical Guideline TR-03122-1 - Conformance Test Specification for BSI TR-03121 Biometrics for Public Sector Applications - Part 1: Framework - Version 7.0 | [PDF](pdf/tr/TR-03122-1_v7_0.pdf) | - |
| TR-03122 | Technical Guideline TR-03122-2 - Conformance Test Specification for BSI TR-03121 Biometrics for Public Sector Applications - Part 2: Test Cases for High Level Biometric Services (HLBS) - Version 7.0 | [PDF](pdf/tr/TR-03122-2_v7_0.pdf) | - |
| TR-03122 | Technical Guideline TR-03122-3 - Conformance Test Specification for BSI TR-03121 Biometrics for Public Sector Applications - Part 3: Test Cases for Function Modules and Processes - Version 7.0 | [PDF](pdf/tr/TR-03122-3_v7_0.pdf) | - |
| TR-03122 | Technical Guideline TR-03122-1 - Conformance Test Specification for BSI TR-03121 Biometrics for Public Sector Applications - Part 1: Framework - Version 6.0 | [PDF](pdf/tr/TR-03122-1_v6_0.pdf) | [MD](markdown/tr/TR-03122-1_v6_0) |
| TR-03122 | Technical Guideline TR-03122-2 - Conformance Test Specification for BSI TR-03121 Biometrics for Public Sector Applications - Part 2: Test Cases for High Level Biometric Services (HLBS) - Version 6.0 | [PDF](pdf/tr/TR-03122-2_v6_0.pdf) | [MD](markdown/tr/TR-03122-2_v6_0) |
| TR-03122 | Technical Guideline TR-03122-3 - Conformance Test Specification for BSI TR-03121 Biometrics for Public Sector Applications - Part 3: Test Cases for Function Modules and Processes - Version 6.0 | [PDF](pdf/tr/TR-03122-3_v6_0.pdf) | [MD](markdown/tr/TR-03122-3_v6_0) |
| TR-03122 | Technical Guideline TR-03122-3 - Conformance Test Specification for BSI TR-03121 Biometrics for Public Sector Applications - Addendum Part 3: Additional Test Cases for FM AH-FI-DC2 - Version 6.0 | [PDF](pdf/tr/TR-03122-3-Addendum.pdf) | [MD](markdown/tr/TR-03122-3-Addendum) |
| TR-03122 | Technical Guideline TR-03122-3 - Conformance Test Specification for BSI TR-03121 Biometrics for Public Sector Applications - Second Addendum Part 3: Additional Test Cases for FM AS-FI-ICS2 - Version 6.0 | [PDF](pdf/tr/TR-03122-3-Addendum-2.pdf) | - |
| TR-03123 | Technische Richtlinie TR-03123 XML-Datenaustauschformat für hoheitliche Dokumente (TR XhD) - Teil 1 - Rahmenwerk | [PDF](pdf/tr/TR-03123-1-XhD-1_v161.pdf) | [MD](markdown/tr/TR-03123-1-XhD-1_v161) |
| TR-03123 | Technische Richtlinie TR-03123 XML-Datenaustauschformat für hoheitliche Dokumente (TR XhD) - Teil 2 - Dokumentenprofile | [PDF](pdf/tr/TR-03123-2-XhD-1_v161.pdf) | [MD](markdown/tr/TR-03123-2-XhD-1_v161) |
| TR-03123 | Technische Richtlinie TR-03123 XML-Datenaustauschformat für hoheitliche Dokumente (TR XhD) - Teil 3 - Funktionsmodule | [PDF](pdf/tr/TR-03123-3-XhD-1_v161.pdf) | [MD](markdown/tr/TR-03123-3-XhD-1_v161) |
| TR-03123 | Technische Richtlinie TR-03123 XML-Datenaustauschformat für hoheitliche Dokumente (TR XhD) - V152 | [PDF](pdf/tr/TR-03123-1-XhD-1_v152.pdf) | [MD](markdown/tr/TR-03123-1-XhD-1_v152) |
| TR-03123 | BSI TR-03123-2 Dokumentenprofile | [PDF](pdf/tr/TR-03123-2-XhD-1_v152.pdf) | [MD](markdown/tr/TR-03123-2-XhD-1_v152) |
| TR-03123 | Technische Richtlinie – XML-Datenaustauschformat für hoheitliche Dokumente (TR XhD) - Technische Richtlinie – XML-Datenaustauschformat für hoheitliche Dokumente (TR XhD) - V152 | [PDF](pdf/tr/TR-03123-3-XhD-1_v152.pdf) | [MD](markdown/tr/TR-03123-3-XhD-1_v152) |
| TR-03123 | Technische Richtlinie TR-03123 XML-Datenaustauschformat für hoheitliche Dokumente (TR XhD) | [PDF](pdf/tr/TR-03123-1-XhD-1_2019.pdf) | [MD](markdown/tr/TR-03123-1-XhD-1_2019) |
| TR-03123 | BSI TR-03123-2 Dokumentenprofile | [PDF](pdf/tr/TR-03123-2-XhD-1_2019.pdf) | [MD](markdown/tr/TR-03123-2-XhD-1_2019) |
| TR-03123 | BSI TR-03123-3 Technische Richtlinie – XML-Datenaustauschformat für hoheitliche Dokumente (TR XhD) 3 - Funktionsmodule Version 1.5 | [PDF](pdf/tr/TR-03123-3-XhD-1_0_2019.pdf) | [MD](markdown/tr/TR-03123-3-XhD-1_0_2019) |
| TR-03124 | Technical Guideline BSI TR-03124 - Part 1 | [PDF](pdf/tr/TR-03124-1.pdf) | [MD](markdown/tr/TR-03124-1) |
| TR-03124 | Technical Guideline TR-03124-2 | [PDF](pdf/tr/TR-03124-2.pdf) | [MD](markdown/tr/TR-03124-2) |
| TR-03124 | Übergangsregelungen für die Zertifizierung von eID-Clients nach TR-03124-2 | [PDF](pdf/tr/TR-03124-2-eID-Clients.pdf) | [MD](markdown/tr/TR-03124-2-eID-Clients) |
| TR-03125 | SR 019 510 - V1.1.1 - Electronic Signatures and Infrastructures (ESI); Scoping study and framework for standardization of long-term data preservation services, including preservation of/with digital signatures | [PDF](pdf/tr/sr_019510v010101p.pdf) | [MD](markdown/tr/sr_019510v010101p) |
| TR-03125 | TS 119 511 - V1.1.1 - Electronic Signatures and Infrastructures (ESI); Policy and security requirements for trust service providers providing long-term preservation of digital signatures or general data using digital signature techniques | [PDF](pdf/tr/ts_119511v010101p.pdf) | [MD](markdown/tr/ts_119511v010101p) |
| TR-03125 | TS 119 512 - V1.1.1 - Electronic Signatures and Infrastructures (ESI); Protocols for trust service providers providing long-term data preservation services | [PDF](pdf/tr/ts_119512v010101p.pdf) | [MD](markdown/tr/ts_119512v010101p) |
| TR-03125 | EN 319 162-1 - V1.1.1 - Electronic Signatures and Infrastructures (ESI); Associated Signature Containers (ASiC); Part 1: Building blocks and ASiC baseline containers | [PDF](pdf/tr/en_31916201v010101p.pdf) | [MD](markdown/tr/en_31916201v010101p) |
| TR-03125 | TS 119 512 - V1.1.2 - Electronic Signatures and Infrastructures (ESI); Protocols for trust service providers providing long-term data preservation services | [PDF](pdf/tr/ts_119512v010102p.pdf) | [MD](markdown/tr/ts_119512v010102p) |
| TR-03125 | BSI Technische Richtlinie 03125 Beweiswerterhaltung kryptographisch signierter Dokumente - V1.3.1 | [PDF](pdf/tr/BSI_TR_03125_V1_3_1.pdf) | [MD](markdown/tr/BSI_TR_03125_V1_3_1) |
| TR-03125 | BSI Technische Richtlinie 03125 Beweiswerterhaltung kryptographisch signierter Dokumente - V1.3, Anlage M1 V1 3 | [PDF](pdf/tr/BSI_TR_03125_Anlage_M1_V1_3.pdf) | [MD](markdown/tr/BSI_TR_03125_Anlage_M1_V1_3) |
| TR-03125 | BSI Technische Richtlinie 03125 Beweiswerterhaltung kryptographisch signierter Dokumente - V1.3, Anlage M2 V1 3 | [PDF](pdf/tr/BSI_TR_03125_Anlage_M2_V1_3.pdf) | [MD](markdown/tr/BSI_TR_03125_Anlage_M2_V1_3) |
| TR-03125 | BSI Technische Richtlinie 03125 Beweiswerterhaltung kryptographisch signierter Dokumente - V1.3, Anlage M3 V1 3 | [PDF](pdf/tr/BSI_TR_03125_Anlage_M3_V1_3.pdf) | [MD](markdown/tr/BSI_TR_03125_Anlage_M3_V1_3) |
| TR-03125 | BSI TR-ESOR-E Konkretierung der Schnittstellen auf Basis des eCard-API-Frameworks - V1.3, Anlage E V1 3 | [PDF](pdf/tr/BSI_TR_03125_Anlage_E_V1_3.pdf) | [MD](markdown/tr/BSI_TR_03125_Anlage_E_V1_3) |
| TR-03125 | BSI Technische Richtlinie 03125 Beweiswerterhaltung kryptographisch signierter Dokumente - V1.3, Anlage F V1 3 | [PDF](pdf/tr/BSI_TR_03125_Anlage_F_V1_3.pdf) | [MD](markdown/tr/BSI_TR_03125_Anlage_F_V1_3) |
| TR-03125 | BSI TR-ESOR-VR: Verification Reports for Selected Data Structures | [PDF](pdf/tr/BSI_TR_03125_Anlage_VR_V1_3.pdf) | [MD](markdown/tr/BSI_TR_03125_Anlage_VR_V1_3) |
| TR-03125 | BSI TR-ESOR-ERS Profilierung der Evidence Recordes gemäß RFC 4998 und RFC 6283 - V1.3, Anlage ERS V1 3 | [PDF](pdf/tr/BSI_TR_03125_Anlage_ERS_V1_3.pdf) | [MD](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_3) |
| TR-03125 | TR-03125 TR-ESOR ENC: Profil für die Aufbewahrung von verschlüsselten Inhalten | [PDF](pdf/tr/BSI_TR_03125_Anlage_TR-ESOR-ENC_1_3.pdf) | - |
| TR-03125 | BSI TR-ESOR-C.1 V1.3: Conformity Test Specification (Level 1 ‑ Functional Conformity) | [PDF](pdf/tr/BSI_TR_03125_Anlage_C1_V1_3.pdf) | [MD](markdown/tr/BSI_TR_03125_Anlage_C1_V1_3) |
| TR-03125 | Annex TR-ESOR-C.2: Conformity Test Specification (Level 2 Technical Conformity) | [PDF](pdf/tr/BSI_TR_03125_Anlage_C2_V1_3.pdf) | [MD](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3) |
| TR-03125 | Annex TR-ESOR-PEPT: Preservation Evidence Policy Template for TR-ESOR (PEPT) | [PDF](pdf/tr/BSI_TR_03125_Anlage_PEPT_V1_2_1_higher.pdf) | [MD](markdown/tr/BSI_TR_03125_Anlage_PEPT_V1_2_1_higher) |
| TR-03125 | TR-ESOR einfach erklärt | [PDF](pdf/tr/BSI_TR-ESOR-einfach-erklaert.pdf) | [MD](markdown/tr/BSI_TR-ESOR-einfach-erklaert) |
| TR-03125 | Leitlinie für die langfristige Beweiswerterhaltung von digitalen Signaturen oder elektronischen Dokumenten oder Daten entsprechend BSI TR-03125 TR-ESOR | [PDF](pdf/tr/BSI_TR-ESOR-leitlinie_1_3.pdf) | [MD](markdown/tr/BSI_TR-ESOR-leitlinie_1_3) |
| TR-03125 | Part 1: Assessment Criteria for all TSP - ETSI EN 319 401 V1.0 | [PDF](pdf/tr/Assessment-Handbuch_ETSI_319_401.pdf) | [MD](markdown/tr/Assessment-Handbuch_ETSI_319_401) |
| TR-03125 | Part 2: Criteria for Assessing Trust Service Providers against ETSI Policy Requirements - ETSI TS 119 511 | [PDF](pdf/tr/Assessment-Handbuch_ETSI_319_511.pdf) | [MD](markdown/tr/Assessment-Handbuch_ETSI_319_511) |
| TR-03125 | BSI TR 03125 TR-ESOR: Beweiswerterhaltung kryptographisch signierter Dokumente V1.2.2 | [PDF](pdf/tr/BSI_TR_03125_V1_2_2.pdf) | [MD](markdown/tr/BSI_TR_03125_V1_2_2) |
| TR-03125 | BSI TR-ESOR M.1 - V1.2.1, Anlage M1 V1 2 1 | [PDF](pdf/tr/BSI_TR_03125_Anlage_M1_V1_2_1.pdf) | [MD](markdown/tr/BSI_TR_03125_Anlage_M1_V1_2_1) |
| TR-03125 | BSI TR-ESOR M.2 - V1.2.1, Anlage M2 V1 2 1 | [PDF](pdf/tr/BSI_TR_03125_Anlage_M2_V1_2_1.pdf) | [MD](markdown/tr/BSI_TR_03125_Anlage_M2_V1_2_1) |
| TR-03125 | BSI TR-ESOR-M.3 ArchiSig-Modul - V1.2.1, Anlage M3 V1 2 1 | [PDF](pdf/tr/BSI_TR_03125_Anlage_M3_V1_2_1.pdf) | [MD](markdown/tr/BSI_TR_03125_Anlage_M3_V1_2_1) |
| TR-03125 | BSI TR-ESOR-E Konkretierung der Schnittstellen auf Basis des eCard-API-Frameworks - V1.2.2, Anlage E V1 2 2 | [PDF](pdf/tr/BSI_TR_03125_Anlage_E_V1_2_2.pdf) | [MD](markdown/tr/BSI_TR_03125_Anlage_E_V1_2_2) |
| TR-03125 | Appendix zu TR-ESOR-E: Grobkonzept ETSI TS119512 TR-ESOR Transformator | [PDF](pdf/tr/BSI_TR_03125_Anlage_TRANS_V1_2_2-Appendix.pdf) | [MD](markdown/tr/BSI_TR_03125_Anlage_TRANS_V1_2_2-Appendix) |
| TR-03125 | BSI TR-ESOR F Formate - V1.2.2, Anlage F V1 2 2 | [PDF](pdf/tr/BSI_TR_03125_Anlage_F_V1_2_2.pdf) | [MD](markdown/tr/BSI_TR_03125_Anlage_F_V1_2_2) |
| TR-03125 | BSI TR-ESOR-VR - V1.2.1, Anlage VR V1 2 1 | [PDF](pdf/tr/BSI_TR_03125_Anlage_VR_V1_2_1.pdf) | [MD](markdown/tr/BSI_TR_03125_Anlage_VR_V1_2_1) |
| TR-03125 | BSI TR-ESOR-ERS Profilierung der Evidence Recordes gemäß RFC 4998 und RFC 6283 - V1.2.1, Anlage ERS V1 2 1 | [PDF](pdf/tr/BSI_TR_03125_Anlage_ERS_V1_2_1.pdf) | [MD](markdown/tr/BSI_TR_03125_Anlage_ERS_V1_2_1) |
| TR-03125 | BSI TR-ESOR-B Profilierung für Bundesbehörden - V1.2.1, Anlage B V1 2 1 | [PDF](pdf/tr/BSI_TR_03125_Anlage_B_V1_2_1.pdf) | [MD](markdown/tr/BSI_TR_03125_Anlage_B_V1_2_1) |
| TR-03125 | Anlage TR-ESOR: Profil XAIP mit XBARCH und XDOMEA | [PDF](pdf/tr/BSI_TR_03125_Anlage_XBDP_V1_2_1.pdf) | [MD](markdown/tr/BSI_TR_03125_Anlage_XBDP_V1_2_1) |
| TR-03125 | BSI TR-ESOR-C.1 Conformity Test Specification (Level 1 ‑ Functional Conformity) - V1.2.2, Anlage C1 V1 2 2 | [PDF](pdf/tr/BSI_TR_03125_Anlage_C1_V1_2_2.pdf) | [MD](markdown/tr/BSI_TR_03125_Anlage_C1_V1_2_2) |
| TR-03125 | Anlage TR-ESOR-Profil-APP: Appendix für TR-ESOR V1.2.1 und V1.2.2 - Profilierung einiger TR-ESOR-Assessment-Kriterien zur ETSI TS 119 511 Prüferleichterung | [PDF](pdf/tr/BSI_TR_03125_Anlage_APP.pdf) | [MD](markdown/tr/BSI_TR_03125_Anlage_APP) |
| TR-03125 | Standalone Schemata TR-ESOR V 1.2.2 | [PDF](pdf/tr/BSI_TR_03125_Schemata-1_2_2.pdf) | [MD](markdown/tr/BSI_TR_03125_Schemata-1_2_2) |
| TR-03125 | Leitlinie für digitale Signatur-/Siegel-, Zeitstempelformate sowie technische Beweisdaten (Evidence Records) | [PDF](pdf/tr/BSI_TR_03125_Leitlinie_fuer_digitale_Signatur-Siegel-Zeitstempelformate.pdf) | [MD](markdown/tr/BSI_TR_03125_Leitlinie_fuer_digitale_Signatur-Siegel-Zeitstempelformate) |
| TR-03125 | BSI TR-ESOR Leitlinie für die Beweiswerterhaltende Aufbewahrung gemäß TR-ESOR - eine Handlungshilfe für Behörden und Unternehmen | [PDF](pdf/tr/BSI_TR-ESOR-LEIT.pdf) | [MD](markdown/tr/BSI_TR-ESOR-LEIT) |
| TR-03125 | Part 1: Assessment Criteria for all TSP - ETSI EN 319 401 V1.0 | [PDF](pdf/tr/Assessment-Handbuch_ETSI_319_401.pdf) | [MD](markdown/tr/Assessment-Handbuch_ETSI_319_401) |
| TR-03125 | Part 2: Criteria for Assessing Trust Service Providers against ETSI Policy Requirements - ETSI TS 119 511 | [PDF](pdf/tr/Assessment-Handbuch_ETSI_319_511.pdf) | [MD](markdown/tr/Assessment-Handbuch_ETSI_319_511) |
| TR-03126 | TR 03126 - Technische Richtlinie für den sicheren RFID-Einsatz – öffentlicher Personenverkehr - Part 1 | [PDF](pdf/tr/BSI-TR-03126-1.pdf) | [MD](markdown/tr/BSI-TR-03126-1) |
| TR-03126 | TG 03126 - Technical Guidelines for the Secure Use of RFID | [PDF](pdf/tr/TG_03126_1_TG_for_the_Secure_Use_of_RFID.pdf) | [MD](markdown/tr/TG_03126_1_TG_for_the_Secure_Use_of_RFID) |
| TR-03126 | TR 03126 - Technische Richtlinie für den sicheren RFID-Einsatz - Veranstaltungen - Part 2 | [PDF](pdf/tr/BSI-TR-03126-2.pdf) | [MD](markdown/tr/BSI-TR-03126-2) |
| TR-03126 | TG 03126 - Technical Guidelines for the Secure Use of RFID | [PDF](pdf/tr/TG_03126_2_application_area_Event_Ticketing.pdf) | [MD](markdown/tr/TG_03126_2_application_area_Event_Ticketing) |
| TR-03126 | TR 03126 - Technische Richtlinie für den sicheren RFID-Einsatz - Part 3 | [PDF](pdf/tr/BSI-TR-03126-3.pdf) | [MD](markdown/tr/BSI-TR-03126-3) |
| TR-03126 | TG 03126 - Technical Guidelines for the Secure Use of RFID | [PDF](pdf/tr/TG_03126_3_Application_area_NFC_based_eTicketing.pdf) | [MD](markdown/tr/TG_03126_3_Application_area_NFC_based_eTicketing) |
| TR-03126 | TR 03126-4 Technische Richtlinie für den sicheren RFID-Einsatz Einsatzgebiet Handelslogistik - Part 4 | [PDF](pdf/tr/BSI-TR-03126-4.pdf) | [MD](markdown/tr/BSI-TR-03126-4) |
| TR-03126 | TG 03126 - Technical Guidelines for the Secure Use of RFID | [PDF](pdf/tr/TG_03126_4_Application_area_eTicketing_in_public_transport.pdf) | [MD](markdown/tr/TG_03126_4_Application_area_eTicketing_in_public_transport) |
| TR-03126 | TR 03126 - Technische Richtlinie für den sicheren RFID-Einsatz - Part 5 | [PDF](pdf/tr/BSI-TR-03126-5_2.pdf) | [MD](markdown/tr/BSI-TR-03126-5_2) |
| TR-03126 | TR03126-5-P - Technische Richtlinie für den sicheren RFID-Einsatz | [PDF](pdf/tr/BSI-TR-03126-5_2_P.pdf) | [MD](markdown/tr/BSI-TR-03126-5_2_P) |
| TR-03126 | Technische Richtlinie für den sicheren RFID-Einsatz - Part 5 | [PDF](pdf/tr/BSI-TR-03126-5.pdf) | [MD](markdown/tr/BSI-TR-03126-5) |
| TR-03126 | Technical Guidelines for the Secure Use of RFID (TG RFID) | [PDF](pdf/tr/TG_03126_5_Application_area_Electronic_Employee_ID_Card.pdf) | [MD](markdown/tr/TG_03126_5_Application_area_Electronic_Employee_ID_Card) |
| TR-03126 | Technical Guidelines RFID as Templates for the PIA-Framework | [PDF](pdf/tr/TG_RFID_Templates_for_PIA_Framework_pdf.pdf) | [MD](markdown/tr/TG_RFID_Templates_for_PIA_Framework_pdf) |
| TR-03126 | TG 03126 - Technical Guidelines for the Secure Use of RFID | [PDF](pdf/tr/TG_03126_1_TG_for_the_Secure_Use_of_RFID.pdf) | [MD](markdown/tr/TG_03126_1_TG_for_the_Secure_Use_of_RFID) |
| TR-03126 | TG 03126 - Technical Guidelines for the Secure Use of RFID | [PDF](pdf/tr/TG_03126_2_application_area_Event_Ticketing.pdf) | [MD](markdown/tr/TG_03126_2_application_area_Event_Ticketing) |
| TR-03126 | TG 03126 - Technical Guidelines for the Secure Use of RFID | [PDF](pdf/tr/TG_03126_3_Application_area_NFC_based_eTicketing.pdf) | [MD](markdown/tr/TG_03126_3_Application_area_NFC_based_eTicketing) |
| TR-03126 | TG 03126 - Technical Guidelines for the Secure Use of RFID | [PDF](pdf/tr/TG_03126_4_Application_area_eTicketing_in_public_transport.pdf) | [MD](markdown/tr/TG_03126_4_Application_area_eTicketing_in_public_transport) |
| TR-03126 | Technical Guidelines for the Secure Use of RFID (TG RFID) | [PDF](pdf/tr/TG_03126_5_Application_area_Electronic_Employee_ID_Card.pdf) | [MD](markdown/tr/TG_03126_5_Application_area_Electronic_Employee_ID_Card) |
| TR-03126 | Technical Guidelines RFID as Templates for the PIA-Framework | [PDF](pdf/tr/TG_RFID_Templates_for_PIA_Framework_pdf.pdf) | [MD](markdown/tr/TG_RFID_Templates_for_PIA_Framework_pdf) |
| TR-03127 | Technische Richtlinie TR-03127 - Part 1 | [PDF](pdf/tr/BSI-TR-03127_1-40.pdf) | [MD](markdown/tr/BSI-TR-03127_1-40) |
| TR-03127 | Technical Guideline TR-03127 | [PDF](pdf/tr/BSI-TR-03127_en.pdf) | [MD](markdown/tr/BSI-TR-03127_en) |
| TR-03128 | TR-03128 Diensteanbieter für die eID-Funktion Teil 1 | [PDF](pdf/tr/BSI_TR-03128_Teil1.pdf) | [MD](markdown/tr/BSI_TR-03128_Teil1) |
| TR-03128 | Technische Richtlinie TR-03128-2 Diensteanbieter für die eID-Funktion | [PDF](pdf/tr/BSI_TR-03128_Teil2.pdf) | [MD](markdown/tr/BSI_TR-03128_Teil2) |
| TR-03128 | Technische Richtlinie TR-03128 Diensteanbieter für die eID-Funktion - Teil 3 | [PDF](pdf/tr/BSI_TR-03128_Teil3.pdf) | [MD](markdown/tr/BSI_TR-03128_Teil3) |
| TR-03128 | TR-03128 Diensteanbieter für die eID-Funktion Teil 1 | [PDF](pdf/tr/BSI_TR-03128_Teil1.pdf) | [MD](markdown/tr/BSI_TR-03128_Teil1) |
| TR-03128 | Technische Richtlinie TR-03128-2 Diensteanbieter für die eID-Funktion | [PDF](pdf/tr/BSI_TR-03128_Teil2.pdf) | [MD](markdown/tr/BSI_TR-03128_Teil2) |
| TR-03128 | Technische Richtlinie TR-03128 Diensteanbieter für die eID-Funktion - Teil 3 | [PDF](pdf/tr/BSI_TR-03128_Teil3.pdf) | [MD](markdown/tr/BSI_TR-03128_Teil3) |
| TR-03128 | BSI_TR-03128_2_V1.0_Checkliste_Prüfanforderungen | [PDF](pdf/tr/BSI_TR-03128-2_Checkliste.pdf) | [MD](markdown/tr/BSI_TR-03128-2_Checkliste) |
| TR-03129 | PKIs for Machine Readable Travel Documments | [PDF](pdf/tr/BSI_TR_03129.pdf) | [MD](markdown/tr/BSI_TR_03129) |
| TR-03129 | Technical Guideline TR 03129-1 - Part 1 | [PDF](pdf/tr/BSI_TR_03129-1.pdf) | [MD](markdown/tr/BSI_TR_03129-1) |
| TR-03129 | BSI Technical Guideline TR-03129-2 - Protocols for the Management of Certificates and CRLs in Public-Key-Infrastructures (PKIs) - Part 2: Supplemental specifications for public and official authorities - Version 1.4.2 | [PDF](pdf/tr/BSI-TR-03129-2_V1_4_2.pdf) | - |
| TR-03129 | BSI Technical Guideline TR-03129-2 - Protocols for the Management of Certificates and CRLs in Public-Key-Infrastructures (PKIs) - Part 2: Supplemental specifications for public and official authorities - Version 1.4.1 | [PDF](pdf/tr/BSI-TR-03129-2_V1_4_1.pdf) | [MD](markdown/tr/BSI-TR-03129-2_V1_4_1) |
| TR-03129 | BSI Technical Guideline TR-03129-2 - Protocols for the Management of Certificates and CRLs in Public-Key-Infrastructures (PKIs) - Part 2: Supplemental specifications for public and official authorities - Version 1.4 | [PDF](pdf/tr/BSI_TR_03129-2_V1_4.pdf) | [MD](markdown/tr/BSI_TR_03129-2_V1_4) |
| TR-03129 | PKIs for Machine Readable Travel Documents - V1.3 | [PDF](pdf/tr/BSI_TR_03129-2_V1_3.pdf) | [MD](markdown/tr/BSI_TR_03129-2_V1_3) |
| TR-03129 | Technical Guideline TR 03129-3 - Part 3 | [PDF](pdf/tr/BSI_TR_03129-3.pdf) | [MD](markdown/tr/BSI_TR_03129-3) |
| TR-03129 | Annex to BSI TR-03129 | [PDF](pdf/tr/BSI_TR_03129-Annex.pdf) | [MD](markdown/tr/BSI_TR_03129-Annex) |
| TR-03129 | Technical Guideline TR-03129-4 Protocols for the Management of Certificates and CRLs in Public-Key-Infrastructures (PKIs) | [PDF](pdf/tr/BSI_TR_03129-4.pdf) | [MD](markdown/tr/BSI_TR_03129-4) |
| TR-03130 | Technical Guideline TR-03130 eID-Server - Part 1 | [PDF](pdf/tr/TR-03130_TR-eID-Server_Part1.pdf) | [MD](markdown/tr/TR-03130_TR-eID-Server_Part1) |
| TR-03130 | Technical Guideline TR-03130 eID-Server - Part 2 | [PDF](pdf/tr/TR-03130_TR-eID-Server_Part2.pdf) | [MD](markdown/tr/TR-03130_TR-eID-Server_Part2) |
| TR-03130 | Technical Guideline TR-03130 eID-Server - Part 3 | [PDF](pdf/tr/TR-03130_TR-eID-Server_Part3.pdf) | [MD](markdown/tr/TR-03130_TR-eID-Server_Part3) |
| TR-03130 | BSI TR-03130 eID-Server - Part 4 | [PDF](pdf/tr/TR-03130_TR-eID-Server_Part4.pdf) | [MD](markdown/tr/TR-03130_TR-eID-Server_Part4) |
| TR-03131 | Technical Guideline TR-03131 EAC-Box | [PDF](pdf/tr/BSI_TR03131.pdf) | [MD](markdown/tr/BSI_TR03131) |
| TR-03132 | Technische Richtlinie TR-03132: Sichere Szenarien für Kommunikationsprozesse im Bereich hoheitlicher Dokumente | [PDF](pdf/tr/TR-03132_Version-1-8-3.pdf) | [MD](markdown/tr/TR-03132_Version-1-8-3) |
| TR-03132 | Technische Richtlinie TR-03132: Sichere Szenarien für Kommunikationsprozesse im Bereich hoheitlicher Dokumente | [PDF](pdf/tr/TR-03132_Version-1-8-2.pdf) | [MD](markdown/tr/TR-03132_Version-1-8-2) |
| TR-03132 | Technische Richtlinie TR-03132 Sichere Szenarien für Kommunikationsprozesse im Bereich hoheitlicher Dokumente - V1.8.1.2020.10.13 | [PDF](pdf/tr/TR-03132_Version-1-8-1_2020-10-13.pdf) | [MD](markdown/tr/TR-03132_Version-1-8-1_2020-10-13) |
| TR-03133 | Technische Richtlinie TR-03133 Prüfspezifikation zur Technischen Richtlinie BSI TR-03132 SiSKo-hD | [PDF](pdf/tr/TR-03133-Pruefspez_zu_TR-03132.pdf) | [MD](markdown/tr/TR-03133-Pruefspez_zu_TR-03132) |
| TR-03133 | Technische Richtlinie TR-03133 | [PDF](pdf/tr/TR-03133-Pruefspez_zu_TR-03132_1_8_1.pdf) | [MD](markdown/tr/TR-03133-Pruefspez_zu_TR-03132_1_8_1) |
| TR-03133 | Technische Richtlinie TR-03133 | [PDF](pdf/tr/TR-03133-Pruefspez_zu_TR-03132_1_8_2.pdf) | [MD](markdown/tr/TR-03133-Pruefspez_zu_TR-03132_1_8_2) |
| TR-03133 | Technische Richtlinie TR-03133 | [PDF](pdf/tr/TR-03133-Pruefspez_zu_TR-03132_1_8_3.pdf) | [MD](markdown/tr/TR-03133-Pruefspez_zu_TR-03132_1_8_3) |
| TR-03135 | BSI Technical Guideline TR-03135-1 - Machine Authentication of MRTDs for Public Sector Applications - Part 1: Overview and Functional Requirements - Version 5.0.0 | [PDF](pdf/tr/BSI-TR-03135-1-v5.pdf) | - |
| TR-03135 | BSI Technical Guideline TR-03135-2 - Machine Authentication of MRTDs for Public Sector Applications - Part 2: Application profiles for official document inspection systems - Version 5.0.0 | [PDF](pdf/tr/BSI-TR-03135-2-v5.pdf) | - |
| TR-03135 | BSI Technical Guideline TR-03135-3 - Machine Authentication of MRTDs for Public Sector Applications - Part 3: High Level Document Check Interface Specification - Version 5.0.0 | [PDF](pdf/tr/BSI-TR-03135-3-v5.pdf) | - |
| TR-03135 | BSI Technical Guideline TR-03135-1 - Machine Authentication of MRTDs for Public Sector Applications - Part 1: Overview and Functional Requirements - Version 2.5 | [PDF](pdf/tr/BSI-TR-03135-1-v2-5.pdf) | [MD](markdown/tr/BSI-TR-03135-1-v2-5) |
| TR-03135 | BSI Technical Guideline TR-03135-2 - Machine Authentication of MRTDs for Public Sector Applications - Part 2: Application profiles for official document inspection systems - Version 2.5 | [PDF](pdf/tr/BSI-TR-03135-2-v2-5.pdf) | [MD](markdown/tr/BSI-TR-03135-2-v2-5) |
| TR-03135 | BSI Technical Guideline TR-03135-3 - Machine Authentication of MRTDs for Public Sector Applications - Part 3: High Level Document Check Interface Specification - Version 2.5 | [PDF](pdf/tr/BSI-TR-03135-3-v2-5.pdf) | [MD](markdown/tr/BSI-TR-03135-3-v2-5) |
| TR-03135 | BSI Technical Guideline BSI TR-03135 Part 1 - Version 2.4.0 | [PDF](pdf/tr/BSI-TR-03135-1-v2-4.pdf) | [MD](markdown/tr/BSI-TR-03135-1-v2-4) |
| TR-03135 | BSI Technical Guideline TR-03135 Part 2 - Version 2.4.0 | [PDF](pdf/tr/BSI-TR-03135-2-v2-4.pdf) | [MD](markdown/tr/BSI-TR-03135-2-v2-4) |
| TR-03135 | BSI Technical Guideline TR-03135 Part 3 - Version 2.4.0 | [PDF](pdf/tr/BSI-TR-03135-3-v2-4.pdf) | [MD](markdown/tr/BSI-TR-03135-3-v2-4) |
| TR-03135 | Technical Guideline BSI TR-03135 Part 1 | [PDF](pdf/tr/BSI-TR-03135-1-v2-3.pdf) | [MD](markdown/tr/BSI-TR-03135-1-v2-3) |
| TR-03135 | Technical Guideline TR-03135 Part-2 - V2.3 | [PDF](pdf/tr/BSI-TR-03135-2-v2-3.pdf) | [MD](markdown/tr/BSI-TR-03135-2-v2-3) |
| TR-03135 | High Level Document Check Interface Specification - V2.3 | [PDF](pdf/tr/BSI-TR-03135-3-v2-3.pdf) | [MD](markdown/tr/BSI-TR-03135-3-v2-3) |
| TR-03137 | BSI TR-03137 Optically Verifiable Cryptographic Protection of non-electronic Documents (Digital Seal) - Part 1 | [PDF](pdf/tr/BSI-TR-03137_Part1.pdf) | [MD](markdown/tr/BSI-TR-03137_Part1) |
| TR-03137 | JAB Code (Just Another Bar Code) color bar code symbology specification - Part 2 | [PDF](pdf/tr/BSI-TR-03137_Part2.pdf) | [MD](markdown/tr/BSI-TR-03137_Part2) |
| TR-03138 | BSI Technische Richtlinie 03138 - V1.5 | [PDF](pdf/tr/TR-03138_V1_5.pdf) | [MD](markdown/tr/TR-03138_V1_5) |
| TR-03138 | BSI Technische Richtlinie 03138 Ersetzendes Scannen - Anhang P | [PDF](pdf/tr/TR-03138-Anlage-P_V1_5.pdf) | [MD](markdown/tr/TR-03138-Anlage-P_V1_5) |
| TR-03138 | BSI 03138 Technische Richtline 03138 Ersetzendes Scannen - Hauptdokument | [PDF](pdf/tr/TR-03138.pdf) | [MD](markdown/tr/TR-03138) |
| TR-03138 | BSI TR 03138 "Ersetzendes Scannen" (RESISCAN) - Anlage P - Prüfspezifikation | [PDF](pdf/tr/TR-03138-Anlage-P_V1_4.pdf) | [MD](markdown/tr/TR-03138-Anlage-P_V1_4) |
| TR-03138 | BSI TR 03138 RESISCAN - Ersetzendes Scannen | [PDF](pdf/tr/TR-03138-Flyer.pdf) | [MD](markdown/tr/TR-03138-Flyer) |
| TR-03138 | Ersetzendes Scannen leichtgemacht | [PDF](pdf/tr/TR-03138-Handlungshilfe.pdf) | [MD](markdown/tr/TR-03138-Handlungshilfe) |
| TR-03138 | Generisches Scankonzept gemäß BSI TR-03138 | [PDF](pdf/tr/TR-03138-generisches_Scankonzept.pdf) | [MD](markdown/tr/TR-03138-generisches_Scankonzept) |
| TR-03138 | BSI Technische Richtlinie 03138 Ersetzendes Scannen - Anhang A | [PDF](pdf/tr/TR-03138-Anwendungshinweis-A.pdf) | [MD](markdown/tr/TR-03138-Anwendungshinweis-A) |
| TR-03138 | BSI Technische Richtlinie 03138 Ersetzendes Scannen - Anwendungshinweis R: Unverbindliche rechtliche Hinweise | [PDF](pdf/tr/TR-03138-Anwendungshinweis-R.pdf) | [MD](markdown/tr/TR-03138-Anwendungshinweis-R) |
| TR-03138 | BSI Technische Richtlinie 03138 Ersetzendes Scannen - Anwendungshinweis V: Exemplarische Verfahrensanweisung | [PDF](pdf/tr/TR-03138-Anwendungshinweis-V.pdf) | [MD](markdown/tr/TR-03138-Anwendungshinweis-V) |
| TR-03138 | BSI Technische Richtlinie 03138 Ersetzendes Scannen | [PDF](pdf/tr/TR-03138-Anwendungshinweis-F.pdf) | [MD](markdown/tr/TR-03138-Anwendungshinweis-F) |
| TR-03138 | Transfervermerk für Scanprodukte | [PDF](pdf/tr/Transfervermerk_Deutsche_RV_Inhalt.pdf) | [MD](markdown/tr/Transfervermerk_Deutsche_RV_Inhalt) |
| TR-03139 | BSI TR-03139 COMMON CERTIFICATE POLICY FOR THE EXTENDED ACCESS CONTROL INFRASTRUCTURE FOR PASSPORTS AND TRAVEL DOCUMENTS ISSUED BY EU MEMBER STATES - V2.4 | [PDF](pdf/tr/BSI-TR-03139_v2_4.pdf) | [MD](markdown/tr/BSI-TR-03139_v2_4) |
| TR-03139 | BSI TR-03139 COMMON CERTIFICATE POLICY FOR THE EXTENDED ACCESS CONTROL INFRASTRUCTURE FOR PASSPORTS AND TRAVEL DOCUMENTS ISSUED BY EU MEMBER STATES - V2.2 | [PDF](pdf/tr/BSI-TR-03139_v2_2_pdf.pdf) | [MD](markdown/tr/BSI-TR-03139_v2_2_pdf) |
| TR-03140 | Technical Guideline SatDSiG - BSI TR-03140 | [PDF](pdf/tr/TR03140.pdf) | [MD](markdown/tr/TR03140) |
| TR-03143 | Technische Richtlinie BSI TR-03143 eHealth - G2-COS Konsistenz-Prüftool, Version 1.1 - V1.1 | [PDF](pdf/tr/TR-03143_v1-1.pdf) | [MD](markdown/tr/TR-03143_v1-1) |
| TR-03143 | Technische Richtlinie BSI TR-03143 "eHealth G2-COS Konsistenz-Prüftool" | [PDF](pdf/tr/TR-03143.pdf) | [MD](markdown/tr/TR-03143) |
| TR-03144 | Technische Richtlinie BSI TR-03144 - eHealth – Konformitätsnachweis für Karten-Produkte der Kartengeneration G2, Version 1.2 - V1.2 | [PDF](pdf/tr/TR-03144v1_2.pdf) | [MD](markdown/tr/TR-03144v1_2) |
| TR-03144 | Technische Richtlinie BSI TR-03144 Anhang - eHealth – Sicherungsmechanismen im Umfeld der TR-Zertifizierung von G2-Karten-Produkten, Version 1.2 | [PDF](pdf/tr/TR-03144v1_2_Anhang.pdf) | [MD](markdown/tr/TR-03144v1_2_Anhang) |
| TR-03144 | Technische Richtlinie BSI TR-03144 - eHealth – Konformitätsnachweis für Karten-Produkte der Kartengeneration G2, Version 1.1 - V1.1 | [PDF](pdf/tr/TR-03144v1_1.pdf) | [MD](markdown/tr/TR-03144v1_1) |
| TR-03144 | Technische Richtlinie BSI TR-03144 Anhang - eHealth – Sicherungsmechanismen im Umfeld der TR-Zertifizierung von G2-Karten-Produkten, Version 1.1 | [PDF](pdf/tr/TR-03144v1_1_Anhang.pdf) | [MD](markdown/tr/TR-03144v1_1_Anhang) |
| TR-03144 | Technische Richtlinie BSI TR-03144 - eHealth – Konformitätsnachweis für Karten-Produkte der Kartengeneration G2 | [PDF](pdf/tr/TR-03144.pdf) | [MD](markdown/tr/TR-03144) |
| TR-03144 | Technische Richtlinie BSI TR-03144 Anhang - eHealth – Sicherungsmechanismen im Umfeld der TR-Zertifizierung von G2-Karten-Produkten | [PDF](pdf/tr/TR-03144_Anhang.pdf) | [MD](markdown/tr/TR-03144_Anhang) |
| TR-03145 | Technical Guideline BSI TR-03145 Secure CA operation | [PDF](pdf/tr/TR03145-1_2_0_0.pdf) | - |
| TR-03145 | Inspection Specification BSI TR-03145-TS - Part 2 | [PDF](pdf/tr/TR03145-2.pdf) | [MD](markdown/tr/TR03145-2) |
| TR-03145 | Technical Guideline BSI TR-03145 Secure CA operation | [PDF](pdf/tr/TR03145-4_2_0_0.pdf) | - |
| TR-03145 | Technical Guideline BSI TR-03145 Secure CA Operation Part 5 | [PDF](pdf/tr/TR03145-5.pdf) | [MD](markdown/tr/TR03145-5) |
| TR-03145 | Inspection Specification BSI TR-03145-TS - Part 1.4.2.0.0 | [PDF](pdf/tr/TR03145-part1-4_2-0-0-specification.pdf) | - |
| TR-03145 | BSI TR-03145-1 Secure CA operation, Part1 | [PDF](pdf/tr/TR03145.pdf) | [MD](markdown/tr/TR03145) |
| TR-03145 | BSI TR-03145-4 Secure CA operation, Part4 | [PDF](pdf/tr/TR03145-4.pdf) | [MD](markdown/tr/TR03145-4) |
| TR-03145 | Key Lifecycle Security Requirements | [PDF](pdf/tr/KeyLifecycleSecurityRequirements.pdf) | [MD](markdown/tr/KeyLifecycleSecurityRequirements) |
| TR-03147 | Assurance Level Assessment of Procedures for Identity Verification of Natural Persons | [PDF](pdf/tr/TR03147.pdf) | [MD](markdown/tr/TR03147) |
| TR-03147 | Assurance Level Assessment of Procedures for Identity Verification of Natural Persons | [PDF](pdf/tr/TR03147.pdf) | [MD](markdown/tr/TR03147) |
| TR-03147 | Anforderungskatalog zur Prüfung von Identifikationsverfahren gemäß TR-03147 | [PDF](pdf/tr/TR-03147-1_Anforderungen.pdf) | [MD](markdown/tr/TR-03147-1_Anforderungen) |
| TR-03148 | BSI TR-03148:Secure Broadband Router | [PDF](pdf/tr/TR03148.pdf) | [MD](markdown/tr/TR03148) |
| TR-03148 | BSI TR-03148-P: Test Specification | [PDF](pdf/tr/TR03148-P_Testspezifikation.pdf) | [MD](markdown/tr/TR03148-P_Testspezifikation) |
| TR-03148 | Kompetenzfeststellung: Programm im Bereich Technischer Richtlinien (TR) TR-Prüfer | [PDF](pdf/tr/TR-Pruefer.pdf) | [MD](markdown/tr/TR-Pruefer) |
| TR-03151 | Technische Richtlinie BSI TR-03151-1 | [PDF](pdf/tr/TR03151-1.pdf) | [MD](markdown/tr/TR03151-1) |
| TR-03151 | Technische Richtlinie BSI TR-03151-2 | [PDF](pdf/tr/TR03151-2.pdf) | [MD](markdown/tr/TR03151-2) |
| TR-03151 | Technical Guideline BSI TR-03151 Part 2 Appendix C | [PDF](pdf/tr/TR03151-2_Appendix_ANSI_C.pdf) | [MD](markdown/tr/TR03151-2_Appendix_ANSI_C) |
| TR-03151 | Technical Guideline BSI TR 03151 Part 2 Appendix Java | [PDF](pdf/tr/TR03151-2_Appendix_Java.pdf) | [MD](markdown/tr/TR03151-2_Appendix_Java) |
| TR-03151 | BSI TR-03151 | [PDF](pdf/tr/TR-03151.pdf) | [MD](markdown/tr/TR-03151) |
| TR-03151 | Amendment to BSI TR-03151 Secure Element API (SE API) | [PDF](pdf/tr/TR-03151-amendment.pdf) | [MD](markdown/tr/TR-03151-amendment) |
| TR-03153 | Technische Richtlinie BSI TR-03153 Teil 1 | [PDF](pdf/tr/TR-03153-1_Version1-1-1.pdf) | [MD](markdown/tr/TR-03153-1_Version1-1-1) |
| TR-03153 | Technische Richtlinie BSI TR-03153 Teil 1 Anhang A | [PDF](pdf/tr/TR-03153-1-Anhang-A_Version1-1-1.pdf) | [MD](markdown/tr/TR-03153-1-Anhang-A_Version1-1-1) |
| TR-03153 | Technische Richtlinie BSI TR-03153-1 Anhang B | [PDF](pdf/tr/TR-03153-1-Anhang-B.pdf) | [MD](markdown/tr/TR-03153-1-Anhang-B) |
| TR-03153 | BSI TR-03153 | [PDF](pdf/tr/TR-03153.pdf) | [MD](markdown/tr/TR-03153) |
| TR-03153 | Ergänzung der Technischen Richtlinie TR-03153 | [PDF](pdf/tr/TR-03153_Ergaenzung.pdf) | [MD](markdown/tr/TR-03153_Ergaenzung) |
| TR-03153 | Klarstellungen und Anwendungshinweise zu BSI TR-03153 und BSI-CC-PP-0105-V2-2020 | [PDF](pdf/tr/TR-03153_Anwendungshinweise.pdf) | [MD](markdown/tr/TR-03153_Anwendungshinweise) |
| TR-03153 | Technische Richtlinie BSI TR-03153 Teil 1 Testspezifikation | [PDF](pdf/tr/TR-03153-TS_Version1-1-1.pdf) | [MD](markdown/tr/TR-03153-TS_Version1-1-1) |
| TR-03153 | Technische Sicherheitseinrichtung BSI TR-03153 Teil 1 Anhang A Testspezifikation | [PDF](pdf/tr/TR-03153-TS_Version1-1-0_Anhang-A.pdf) | [MD](markdown/tr/TR-03153-TS_Version1-1-0_Anhang-A) |
| TR-03153 | BSI TR-03153-TS | [PDF](pdf/tr/TR-03153-TS.pdf) | [MD](markdown/tr/TR-03153-TS) |
| TR-03153 | Ergänzung der Technischen Richtlinie TR-03153 | [PDF](pdf/tr/TR-03153-TS-Ergaenzung.pdf) | [MD](markdown/tr/TR-03153-TS-Ergaenzung) |
| TR-03153 | Klarstellungen und Anwendungshinweise zu BSI TR-03153-TS und BSI-CC-PP-0105-V2-2020 | [PDF](pdf/tr/TR-03153-TS-Ergaenzungen.pdf) | [MD](markdown/tr/TR-03153-TS-Ergaenzungen) |
| TR-03153 | Technische Richtlinie BSI TR-03153-2 | [PDF](pdf/tr/TR-03153_2.pdf) | [MD](markdown/tr/TR-03153_2) |
| TR-03153 | Technische Richtlinie BSI TR-03153-2 Testspezifikation | [PDF](pdf/tr/TR-03153_2_TS.pdf) | [MD](markdown/tr/TR-03153_2_TS) |
| TR-03154 | TR-03154 - Fachmodul NFDM | [PDF](pdf/tr/TR-03154.pdf) | [MD](markdown/tr/TR-03154) |
| TR-03155 | TR-03155 - Fachmodul AMTS | [PDF](pdf/tr/TR-03155.pdf) | [MD](markdown/tr/TR-03155) |
| TR-03156 | BSI Technische Richtlinie TR-03156 - Hoheitliches Identitätsmanagement mit EU-Informationssystemen - Teil 2: XML Schema Dokumentation - Band 1: Erstregistrierung von Drittstaatsangehörigen - Version 2.0.0 | [PDF](pdf/tr/BSI-TR-03156-2_1.pdf) | [MD](markdown/tr/BSI-TR-03156-2_1) |
| TR-03157 | TR-03157 Fachmodul ePA | [PDF](pdf/tr/TR-03157.pdf) | [MD](markdown/tr/TR-03157) |
| TR-03159 | Technical Guideline TR-03159 Mobile Identities - Part 1 | [PDF](pdf/tr/TR-03159-1.pdf) | [MD](markdown/tr/TR-03159-1) |
| TR-03159 | BSI TR-03159 Mobile Identities - Part 2 | [PDF](pdf/tr/TR-03159-2.pdf) | [MD](markdown/tr/TR-03159-2) |
| TR-03159 | Technische Richtlinie TR-03100 Formatvorlage TR | [PDF](pdf/tr/TR-03159-2_Amendment-A.pdf) | [MD](markdown/tr/TR-03159-2_Amendment-A) |
| TR-03160 | Technische Richtlinie TR-03160-1 Servicekonten - Teil 1: Identifizierung und Authentisierung | [PDF](pdf/tr/BSI-TR-03160-1.pdf) | [MD](markdown/tr/BSI-TR-03160-1) |
| TR-03160 | Technische Richtlinie TR-03160-2 Servicekonten - Teil 2: Interoperables Identitätsmanagement für Bürgerkonten | [PDF](pdf/tr/BSI-TR-03160-2.pdf) | [MD](markdown/tr/BSI-TR-03160-2) |
| TR-03161 | Anforderungen an Anwendungen im Gesundheitswesen - Part 1 | [PDF](pdf/tr/BSI-TR-03161-1.pdf) | [MD](markdown/tr/BSI-TR-03161-1) |
| TR-03161 | Anforderungen an Anwendungen im Gesundheitswesen - Part 2 | [PDF](pdf/tr/BSI-TR-03161-2.pdf) | [MD](markdown/tr/BSI-TR-03161-2) |
| TR-03161 | Anforderungen an Anwendungen im Gesundheitswesen - Part 3 | [PDF](pdf/tr/BSI-TR-03161-3.pdf) | [MD](markdown/tr/BSI-TR-03161-3) |
| TR-03161 | Anforderungen an Anwendungen im Gesundheitswesen - Part 1 | [PDF](pdf/tr/BSI-TR-03161-1.pdf) | [MD](markdown/tr/BSI-TR-03161-1) |
| TR-03161 | Anforderungen an Anwendungen im Gesundheitswesen - Part 2 | [PDF](pdf/tr/BSI-TR-03161-2.pdf) | [MD](markdown/tr/BSI-TR-03161-2) |
| TR-03161 | Anforderungen an Anwendungen im Gesundheitswesen - Part 3 | [PDF](pdf/tr/BSI-TR-03161-3.pdf) | [MD](markdown/tr/BSI-TR-03161-3) |
| TR-03162 | Bundesgesetzblatt Teil I Nr. 43 | [PDF](pdf/tr/Online-Wahl-VO_Bgbl.pdf) | [MD](markdown/tr/Online-Wahl-VO_Bgbl) |
| TR-03162 | Technische Richtlinie TR-03162 | [PDF](pdf/tr/BSI-TR-03162.pdf) | [MD](markdown/tr/BSI-TR-03162) |
| TR-03163 | TR-03163 | [PDF](pdf/tr/BSI-TR-03163.pdf) | [MD](markdown/tr/BSI-TR-03163) |
| TR-03163 | Technische Richtlinie BSI TR-03163: Sicherheit in TK-Infrastrukturen - Anhang A | [PDF](pdf/tr/BSI-TR-03163_Anlage_A.pdf) | [MD](markdown/tr/BSI-TR-03163_Anlage_A) |
| TR-03164 | BSI TR-03164-1 Guidance for Cooperative Intelligent Transport Systems, Part1 | [PDF](pdf/tr/BSI-TR-03164_Part1.pdf) | [MD](markdown/tr/BSI-TR-03164_Part1) |
| TR-03164 | TR-03164-2 Guidance for Cooperative Intelligent Transport Systems, Part 2 | [PDF](pdf/tr/BSI-TR-03164_Part2.pdf) | [MD](markdown/tr/BSI-TR-03164_Part2) |
| TR-03165 | TR-03165 TSMS | [PDF](pdf/tr/BSI-TR-03165.pdf) | [MD](markdown/tr/BSI-TR-03165) |
| TR-03166 | BSI TR-03166 Technical Guideline for Biometric Authentication Systems | [PDF](pdf/tr/BSI-TR-03166.pdf) | [MD](markdown/tr/BSI-TR-03166) |
| TR-03166 | Technical Guideline BSI TR-03166 | [PDF](pdf/tr/BSI-TR-03166_Evaluation-Guidance.pdf) | [MD](markdown/tr/BSI-TR-03166_Evaluation-Guidance) |
| TR-03166 | Certified Security for Biometric Devices | [PDF](pdf/tr/BSI-TR-03166_Flyer_Security_Biometric_Devices.pdf) | [MD](markdown/tr/BSI-TR-03166_Flyer_Security_Biometric_Devices) |
| TR-03166 | BSI TR-03166 Technical Guideline for Biometric Authentication Systems | [PDF](pdf/tr/BSI-TR-03166.pdf) | [MD](markdown/tr/BSI-TR-03166) |
| TR-03166 | Technical Guideline BSI TR-03166 | [PDF](pdf/tr/BSI-TR-03166_Evaluation-Guidance.pdf) | [MD](markdown/tr/BSI-TR-03166_Evaluation-Guidance) |
| TR-03169 | TR-03169 | [PDF](pdf/tr/BSI-TR-03169.pdf) | [MD](markdown/tr/BSI-TR-03169) |
| TR-03170 | Technische Richtlinie TR-03170 - Rahmen TR | [PDF](pdf/tr/BSI_TR_03170_Rahmendokument.pdf) | [MD](markdown/tr/BSI_TR_03170_Rahmendokument) |
| TR-03170 | Technische Richtlinie TR-03170 - Teil 1 | [PDF](pdf/tr/BSI_TR_03170_Teil_1.pdf) | [MD](markdown/tr/BSI_TR_03170_Teil_1) |
| TR-03170 | Technische Richtlinie TR-03170 - Teil 2 | [PDF](pdf/tr/BSI_TR_03170_Teil_2.pdf) | [MD](markdown/tr/BSI_TR_03170_Teil_2) |
| TR-03170 | Prüfspezifikation zur Technischen Richtlinie TR-03170 | [PDF](pdf/tr/BSI-TR-03170_Pruefstellenspezifikation.pdf) | [MD](markdown/tr/BSI-TR-03170_Pruefstellenspezifikation) |
| TR-03171 | Technische Richtlinie TR-03171 | [PDF](pdf/tr/BSI-TR-03171.pdf) | [MD](markdown/tr/BSI-TR-03171) |
| TR-03172 | Technische Richtlinie TR-03172 Portalverbund | [PDF](pdf/tr/BSI-TR-03172_Rahmendokument.pdf) | [MD](markdown/tr/BSI-TR-03172_Rahmendokument) |
| TR-03172 | Technische Richtlinie TR-03172-1 Portalverbund Teil 1: Onlinegateway | [PDF](pdf/tr/BSI-TR-03172_1_Onlinegateway.pdf) | - |
| TR-03172 | Technische Richtlinie TR-03172-3 Portalverbund Teil 3: Onlinedienst | [PDF](pdf/tr/BSI-TR-03172_3_Onlinedienst.pdf) | [MD](markdown/tr/BSI-TR-03172_3_Onlinedienst) |
| TR-03172 | Technische Richtlinie TR-03172-4 Portalverbund Teil 4: Antragsrouting | [PDF](pdf/tr/BSI-TR-03172_4_Antragsrouting.pdf) | [MD](markdown/tr/BSI-TR-03172_4_Antragsrouting) |
| TR-03172 | Technische Richtlinie TR-03172 Portalverbund | [PDF](pdf/tr/BSI-TR-03172_Rahmendokument.pdf) | [MD](markdown/tr/BSI-TR-03172_Rahmendokument) |
| TR-03172 | Technische Richtlinie TR-03172-1 Portalverbund Teil 1: Onlinegateway | [PDF](pdf/tr/BSI-TR-03172_1_Onlinegateway.pdf) | - |
| TR-03172 | Technische Richtlinie TR-03172-3 Portalverbund Teil 3: Onlinedienst | [PDF](pdf/tr/BSI-TR-03172_3_Onlinedienst.pdf) | [MD](markdown/tr/BSI-TR-03172_3_Onlinedienst) |
| TR-03172 | Technische Richtlinie TR-03172-4 Portalverbund Teil 4: Antragsrouting | [PDF](pdf/tr/BSI-TR-03172_4_Antragsrouting.pdf) | [MD](markdown/tr/BSI-TR-03172_4_Antragsrouting) |
| TR-03173 | BSI TR-03173: Amendments for Conformance Assessments based on ETSI EN 303 645/TS 103 701 | [PDF](pdf/tr/TR-03173_V111.pdf) | - |
| TR-03173 | BSI TR-03173 v1.0 | [PDF](pdf/tr/TR-03173.pdf) | [MD](markdown/tr/TR-03173) |
| TR-03174 | Anforderungen an Anwendungen im Gesundheitswesen - Part 1 | [PDF](pdf/tr/BSI-TR-03174-1.pdf) | [MD](markdown/tr/BSI-TR-03174-1) |
| TR-03174 | Anforderungen an Anwendungen im Gesundheitswesen - Part 2 | [PDF](pdf/tr/BSI-TR-03174-2.pdf) | [MD](markdown/tr/BSI-TR-03174-2) |
| TR-03174 | Technische Richtlinie TR-03174: Anforderungen an Anwendungen im Finanzwesen | [PDF](pdf/tr/BSI-TR-03174-3.pdf) | [MD](markdown/tr/BSI-TR-03174-3) |
| TR-03174 | Anforderungen an Anwendungen im Gesundheitswesen - Part 1 | [PDF](pdf/tr/BSI-TR-03174-1.pdf) | [MD](markdown/tr/BSI-TR-03174-1) |
| TR-03174 | Anforderungen an Anwendungen im Gesundheitswesen - Part 2 | [PDF](pdf/tr/BSI-TR-03174-2.pdf) | [MD](markdown/tr/BSI-TR-03174-2) |
| TR-03174 | Technische Richtlinie TR-03174: Anforderungen an Anwendungen im Finanzwesen | [PDF](pdf/tr/BSI-TR-03174-3.pdf) | [MD](markdown/tr/BSI-TR-03174-3) |
| TR-03175 | Infrastruktur zur Absicherung von Dokumenten mit digitalen Siegeln | [PDF](pdf/tr/BSI-TR-03175.pdf) | [MD](markdown/tr/BSI-TR-03175) |
| TR-03176 | Technische Richtlinie BSI TR-03176: IT-Sicherheitsanforderungen an die Datenübermittlung in der Registermodernisierung | [PDF](pdf/tr/BSI-TR-03176.pdf) | [MD](markdown/tr/BSI-TR-03176) |
| TR-03176 | Technische Richtlinie BSI TR-03190: IT-Sicherheitsanforderungen für die Anbindung an das NOOTS | [PDF](pdf/tr/BSI-TR-03190.pdf) | - |
| TR-03179 | BSI TR-03179-1: Central Bank Digital Currency - Part 1: Requirements on backend systems | [PDF](pdf/tr/TR03179-1.pdf) | [MD](markdown/tr/TR03179-1) |
| TR-03179 | Technical Guideline BSI TR-03179-2: | [PDF](pdf/tr/TR03179-2.pdf) | - |
| TR-03180 | TR-03180 - Kriterienkatalog zur Bewertung des IT-Sicherheitsniveaus von Smartphones & Tablets für den Einsatz im Verbraucherkontext | [PDF](pdf/tr/BSI-TR-03180.pdf) | [MD](markdown/tr/BSI-TR-03180) |
| TR-03180 | TR-03180 A - Mobile Devices: Requirements catalogue for the IT Security Label | [PDF](pdf/tr/BSI-TR-03180_A_1.1.0.pdf) | [MD](markdown/tr/BSI-TR-03180_A_1.1.0) |
| TR-03180 | TR-03180 A - Mobile Devices: Requirements catalogue for the IT Security Label | [PDF](pdf/tr/BSI-TR-03180_A_1.0.0.pdf) | [MD](markdown/tr/BSI-TR-03180_A_1.0.0) |
| TR-03181 | Technical Guideline BSI TR-03181 CSP2 | [PDF](pdf/tr/BSI-TR-03181.pdf) | [MD](markdown/tr/BSI-TR-03181) |
| TR-03182 | BSI TR-03182 Email Authentication | [PDF](pdf/tr/BSI-TR-03182.pdf) | [MD](markdown/tr/BSI-TR-03182) |
| TR-03182 | BSI TR-03182-P: Testspecification | [PDF](pdf/tr/BSI-TR-03182-P.pdf) | [MD](markdown/tr/BSI-TR-03182-P) |
| TR-03183 | Technical Guideline TR-03183: Cyber Resilience Requirements for Manufacturers and Products | [PDF](pdf/tr/BSI-TR-03183-1_v0_10_0.pdf) | - |
| TR-03183 | Technical Guideline BSI TR-03183: Cyber Resilience Requirements for Manufacturers and Products - Part 2: Software Bill of Materials (SBOM) Version 2.1.0 | [PDF](pdf/tr/BSI-TR-03183-2_v2_1_0.pdf) | - |
| TR-03183 | Technical Guideline BSI TR-03183: Cyber Resilience Requirements for Manufacturers and Products - Part 3: Vulnerability Reports and Notifications Version 1.0.0 | [PDF](pdf/tr/BSI-TR-03183-3_v1_0_0.pdf) | - |
| TR-03183 | Technical Guideline TR-03183: Cyber Resilience Requirements for Manufacturers and Products | [PDF](pdf/tr/BSI-TR-03183-1_v0_10_0.pdf) | - |
| TR-03183 | Technical Guideline BSI TR-03183: Cyber Resilience Requirements for Manufacturers and Products - Part 2: Software Bill of Materials (SBOM) Version 2.1.0 | [PDF](pdf/tr/BSI-TR-03183-2_v2_1_0.pdf) | - |
| TR-03183 | Technical Guideline BSI TR-03183: Cyber Resilience Requirements for Manufacturers and Products - Part 3: Vulnerability Reports and Notifications Version 1.0.0 | [PDF](pdf/tr/BSI-TR-03183-3_v1_0_0.pdf) | - |
| TR-03183 | Technische Richtlinie TR-03183: Cyber-Resilienz-Anforderungen an Hersteller und Produkte | [PDF](pdf/tr/BSI-TR-03183-2.pdf) | [MD](markdown/tr/BSI-TR-03183-2) |
| TR-03183 | Technical Guideline TR-03183: Cyber Resilience Requirements for Manufacturers and Products | [PDF](pdf/tr/BSI-TR-03183-2_v2_2_0.pdf) | - |
| TR-03183 | Technical Guideline TR-03183: Cyber Resilience Requirements for Manufacturers and Products | [PDF](pdf/tr/BSI-TR-03183-2_v2_0_0.pdf) | - |
| TR-03183 | Technical Guideline TR-03183: Cyber Resilience Requirements for Manufacturers and Products | [PDF](pdf/tr/BSI-TR-03183-3_v0_9_0.pdf) | - |
| TR-03184 | Technische Richtlinie BSI TR-03184 Informationssicherheit für Weltraumsysteme - Part 1 | [PDF](pdf/tr/BSI-TR-03184-1.pdf) | - |
| TR-03184 | Technische Richtlinie BSI TR-03184-2 Informationssicherheit für Weltraumsysteme | [PDF](pdf/tr/BSI-TR-03184-2.pdf) | - |
| TR-03184 | Technical Guideline BSI TR-03184 Information Security for Space Systems - Part 1: Space segment | [PDF](pdf/tr/BSI-TR-03184_part1.pdf) | [MD](markdown/tr/BSI-TR-03184_part1) |
| TR-03184 | Technical Guideline BSI TR-03184-2 Information Security for Space Systems | [PDF](pdf/tr/BSI-TR-03184_EN.pdf) | - |
| TR-03185 | Technical Guideline TR-03185: Secure Software Lifecycle Version 1.0 | [PDF](pdf/tr/BSI-TR-03185.pdf) | [MD](markdown/tr/BSI-TR-03185) |
| TR-03185 | BSI TR-03185-2 | [PDF](pdf/tr/BSI-TR-03185-2.pdf) | - |
| TR-03185 | Technical Guideline TR-03185: Secure Software Lifecycle Version 1.0 | [PDF](pdf/tr/BSI-TR-03185.pdf) | [MD](markdown/tr/BSI-TR-03185) |
| TR-03185 | Technical Guideline TR-03185: Secure Software Lifecycle Version 1.0 | [PDF](pdf/tr/BSI-TR-03185.pdf) | [MD](markdown/tr/BSI-TR-03185) |
| TR-03185 | BSI TR-03185-2 | [PDF](pdf/tr/BSI-TR-03185-2.pdf) | - |
| TR-03191 | Technical Guideline TR-03191: Common Security Advisory Framework (CSAF) | [PDF](pdf/tr/BSI-TR-03191.pdf) | [MD](markdown/tr/BSI-TR-03191) |
| TR-03209 | Elektromagnetische Schirmung von Gebäuden -Theoretische Grundlagen - - Part 1 | [PDF](pdf/tr/BSI-TR-03209-1.pdf) | [MD](markdown/tr/BSI-TR-03209-1) |
| TR-03209 | Elektromagnetische Schirmung von Gebäuden - Praktische Messungen - - Part 2 | [PDF](pdf/tr/BSI-TR-03209-2.pdf) | [MD](markdown/tr/BSI-TR-03209-2) |

![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_2.jpeg)

Dokument ist noch aktuell. (Stand 2020)

# TG 03126 - Technical Guidelines for the Secure Use of RFID

TG 03126-4 Application area "trade logistics"

Authors:

Cord Bartels, NXP Harald Kelter, BSI Rainer Oberweis, BSI Birger Rosenberg, NXP

Federal Office for Information Security P.O. Box 20 03 63 53133 Bonn, Germany Tel.: +49 (0)1888 9582 5331 Email: rfid@bsi.bund.de Website: https://www.bsi.bund.de © Federal Office for Information Security 2008

# **Contents**

| 1     | Description of the application area "trade logistics"                    |    |
|-------|--------------------------------------------------------------------------|----|
| 1.1   | Introduction                                                             | 13 |
| 1.2   | Delineation of this Guideline                                            |    |
| 1.3   | Interaction between processes                                            | 14 |
| 2     | Process changes brought about by EPC/RFID                                | 15 |
| 2.1   | The logistics process chain up to the retail outlet                      | 15 |
| 2.1.1 | Initial situation                                                        | 15 |
| 2.1.2 | Scope of analyses                                                        | 15 |
| 2.1.3 | Analysis of selected logistics modules                                   |    |
| 2.1.4 | The ranges, technologies and logistical levels under examination         | 16 |
| 2.1.5 | Assumptions                                                              | 17 |
| 2.1.6 | Summary of results                                                       | 18 |
| 2.1.7 | Conclusions                                                              | 20 |
| 2.2   | The retailer–consumer process chain                                      | 21 |
| 2.2.1 | EPC/RFID application for fresh goods                                     | 22 |
| 2.2.2 | EPC/RFID application for textiles and clothing                           |    |
| 2.2.3 | EPC/RFID use for durable electronic goods                                |    |
| 2.3   | Technological interaction – The GS1 System                               |    |
| 2.3.1 | Orientation of the GS1 system                                            |    |
| 2.3.2 | The components of the GS1 system                                         |    |
|       | 2.3.2.1<br>Identification systems                                        | 26 |
|       | 2.3.2.2<br>Data carriers                                                 | 28 |
|       | 2.3.2.3<br>Data communication                                            | 31 |
|       | 2.3.2.4<br>Summary                                                       | 34 |
| 3     | Agreements                                                               | 36 |
| 3.1   | Definition of terms                                                      | 36 |
| 3.2   | Allocation of roles and entities in the trade logistics application area | 38 |
| 3.2.1 | The logistics process chain up to the retail outlet                      | 38 |
| 4     | General requirements                                                     | 42 |
| 4.1   | Functional requirements                                                  | 42 |
| 4.1.1 | Product-specific use of transponders at the POS                          |    |
| 4.1.2 | Preventing product counterfeiting                                        |    |
| 4.2   | Economy                                                                  |    |
| 4.3   | Security                                                                 |    |

| 5     | Method of determining security requirements              | 44 |
|-------|----------------------------------------------------------|----|
| 5.1   | Objectives                                               | 44 |
| 5.2   | Method                                                   | 44 |
| 5.2.1 | Scope of system considerations                           | 44 |
| 5.2.2 | Scalability and flexibility                              | 45 |
| 5.2.3 | Structure of the Technical Guidelines                    | 47 |
| 5.2.4 | Explanation of the security concept                      | 48 |
| 6     | Generic business processes                               | 50 |
| 6.1   | Generic description of the supply chain                  | 50 |
| 6.2   | Applying for and delivering the EPC Manager              | 50 |
| 6.3   | Individualising the transponder                          | 51 |
| 6.4   | Attaching the transponder to an object                   | 52 |
| 6.5   | Receipt of goods                                         | 53 |
| 6.6   | Warehousing                                              | 53 |
| 6.7   | Shipment preparation                                     | 54 |
| 6.8   | Despatch of goods                                        | 55 |
| 6.9   | Cross-docking                                            | 56 |
| 6.10  | Use at stationery retailers (no mail order)              | 56 |
| 6.11  | Sales process                                            | 57 |
| 6.12  | After-sales services                                     | 58 |
| 6.13  | Disposal                                                 | 60 |
| 7     | Use cases                                                | 61 |
| 7.1   | Manufacture and delivery of the chips                    | 61 |
| 7.2   | Manufacture and delivery of the transponder              | 62 |
| 7.2.1 | Manufacturing the inlay                                  | 62 |
| 7.2.2 | Manufacturing the transponder                            | 63 |
| 7.3   | Producing and issuing the EPC Manager                    | 64 |
| 7.4   | Individualising the transponder                          | 64 |
| 7.5   | Setting the kill password                                | 66 |
| 7.6   | Attaching the transponder to the product                 | 67 |
| 7.7   | Reading the data stored in the transponder               | 67 |
| 7.8   | Activating the kill command                              | 69 |
| 7.9   | Authenticating the transponder for verifying genuineness | 69 |
| 7.10  | Key management                                           | 70 |
| 8     | Security considerations                                  | 72 |
| 8.1   | Definitions relating to security and privacy             | 72 |
| 8.2   | Definition of the security targets                       | 74 |
| 8.2.1 | Specific security targets for the customer               | 74 |

|        | 8.2.1.1<br>Safety                                                                        | 74  |  |
|--------|------------------------------------------------------------------------------------------|-----|--|
|        | 8.2.1.2<br>Information security                                                          | 75  |  |
|        | 8.2.1.3<br>Protection of privacy                                                         | 75  |  |
| 8.2.2  | Specific security targets for the retailer                                               | 75  |  |
|        | 8.2.2.1<br>Safety                                                                        | 76  |  |
|        | 8.2.2.2<br>Information security                                                          | 76  |  |
|        | 8.2.2.3<br>Protection of privacy                                                         | 77  |  |
| 8.2.3  | Specific security targets for the issuer                                                 | 77  |  |
|        | 8.2.3.1<br>Safety                                                                        | 77  |  |
|        | 8.2.3.2<br>Information security                                                          | 78  |  |
|        | 8.2.3.3<br>Protection of privacy                                                         | 79  |  |
| 8.2.4  | Summary of the entities' security targets                                                | 79  |  |
| 8.2.5  | Formation of protection demand categories                                                | 80  |  |
| 8.3    | Threats                                                                                  | 82  |  |
| 8.3.1  | Threats to the contactless interface                                                     | 84  |  |
| 8.3.2  | Threats to the transponder                                                               |     |  |
| 8.3.3  | Threats to the reader                                                                    | 86  |  |
| 8.3.4  | Threats to the key management system                                                     | 87  |  |
| 8.3.5  | Threats to backend systems                                                               | 88  |  |
| 8.3.6  | Threats to customer data systems                                                         | 89  |  |
| 8.4    | Safeguards                                                                               |     |  |
| 8.4.1  | Safeguards for the protection of the system as a whole                                   | 91  |  |
| 8.4.2  | Safeguards relating to the transponder                                                   | 99  |  |
| 8.4.3  | Safeguards relating to the readers                                                       | 105 |  |
| 8.4.4  | Safeguards relating to the key management system                                         | 108 |  |
| 8.4.5  | Safeguards relating to customer data systems                                             | 115 |  |
| 8.4.6  | Examples of non-standardised safeguards for systems compliant with<br>EPCglobal          | 117 |  |
|        | 8.4.6.1<br>Examples of diversification and of safeguards for passwords                   | 117 |  |
|        | 8.4.6.2<br>Example of how data is encrypted in the transponder's extended<br>memory area | 117 |  |
| 9      | Definition of specific application scenarios                                             | 119 |  |
| 9.1    | The "Fast-moving consumer goods" application scenario                                    | 119 |  |
| 9.2    | The "consumer electronics" application scenario                                          | 120 |  |
| 9.3    | The "brand-name clothing" application scenario                                           | 121 |  |
| 10     | Suggestions on implementing the system as a whole                                        | 122 |  |
| 10.1   | Suggestions on implementing the infrastructure                                           | 123 |  |
| 10.1.1 |                                                                                          |     |  |
|        | Determining the protection demand for the logistics infrastructure<br>123                |     |  |

| 10.1.2<br>Interfaces in the system as a whole                                             |     |
|-------------------------------------------------------------------------------------------|-----|
| 10.1.2.1<br>Threats relevant to the logistics infrastructure                              | 126 |
| 10.1.2.2<br>Definition of safeguards for the interfaces of the system as a whole          | 128 |
| 10.1.2.3<br>Residual risks                                                                | 129 |
| 10.1.3<br>Reader                                                                          |     |
| 10.1.3.1<br>Threats relevant to the readers                                               | 130 |
| 10.1.3.2<br>Definition of safeguards for the reader                                       | 131 |
| 10.1.3.3<br>Residual risks                                                                | 132 |
| 10.1.4<br>Backend systems                                                                 | 132 |
| 10.1.4.1<br>Threats relevant to the backend systems                                       | 132 |
| 10.1.4.2<br>Definition of safeguards for the backend systems                              | 134 |
| 10.1.4.3<br>Residual risks                                                                | 135 |
| 10.1.5<br>Customer data systems                                                           | 135 |
| 10.1.5.1<br>Threats relevant to the customer data system                                  | 136 |
| 10.1.5.2<br>Definition of safeguards for the customer data system                         | 137 |
| 10.1.5.3<br>Residual risks                                                                | 138 |
| 10.1.6<br>Key management                                                                  | 138 |
| 10.1.6.1<br>Threats relevant to the key management system                                 | 139 |
| 10.1.6.2<br>Definition of safeguards for the key management system                        | 140 |
| 10.1.6.3<br>Residual risks                                                                | 141 |
| 10.2<br>Transponders                                                                      | 141 |
| 10.2.1<br>Initialising transponders                                                       | 141 |
| 10.2.2<br>Determining the protection demand for the transponder                           | 142 |
| 10.2.3<br>Threats to the transponder                                                      | 142 |
| 10.2.4<br>Definition of specific safeguards                                               | 143 |
| 11<br>Suggestions on executing the product-specific application scenarios                 | 144 |
| 11.1<br>The "Fast-moving consumer goods" application scenario                             | 144 |
| 11.1.1<br>Determining the protection demand category                                      | 144 |
| 11.1.2<br>Relevant threats                                                                | 146 |
| 11.1.3<br>Definition of specific safeguards                                               | 148 |
| 11.1.4<br>Residual risks                                                                  | 150 |
| 11.2<br>The "consumer electronics" application scenario                                   | 151 |
| 11.2.1<br>Determining the protection demand category                                      | 151 |
| 11.2.2<br>Relevant threats                                                                | 153 |
| 11.2.3<br>Definition of specific safeguards                                               | 155 |
| 11.2.4<br>Residual risks                                                                  | 157 |
| 11.2.4.1<br>Residual risks arising from "unauthorised deactivation of the<br>transponder" | 157 |

| 11.3<br>The "brand-name clothing" application scenario |                                                                                           | 158 |
|--------------------------------------------------------|-------------------------------------------------------------------------------------------|-----|
| 11.3.1                                                 | Determining the protection demand category                                                | 158 |
| 11.3.2                                                 | Relevant threats                                                                          | 161 |
| 11.3.3                                                 | Definition of specific safeguards                                                         | 163 |
| 11.3.4<br>Residual risks                               |                                                                                           | 165 |
|                                                        | 11.3.4.1<br>Residual risks arising from "unauthorised deactivation of the<br>transponder" | 165 |
|                                                        | 11.3.4.2<br>Residual risks arising from "tracking"                                        | 166 |
|                                                        |                                                                                           |     |
| 12                                                     | List of references                                                                        | 168 |
| 13                                                     | List of abbreviations                                                                     | 170 |

# **List of Tables**

| Table 8–1  | Coding scheme of security targets                                                                      | 74 |
|------------|--------------------------------------------------------------------------------------------------------|----|
| Table 8–2  | Customer specific security targets for safety                                                          | 75 |
| Table 8–3  | Customer specific security targets for information security                                            | 75 |
| Table 8–4  | Customer specific security targets for protection of privacy                                           | 75 |
| Table 8–5  | Retailer specific security targets for safety                                                          | 76 |
| Table 8–6  | Retailer specific security targets for safety information security                                     | 77 |
| Table 8–7  | Retailer specific security targets for protection of privacy                                           | 77 |
| Table 8–8  | Issuer specific security targets for safety                                                            | 78 |
| Table 8–9  | Issuer specific security targets for information security                                              | 79 |
| Table 8–10 | Service provider specific security targets for protection of privacy                                   | 79 |
| Table 8–11 | Overview of the entities' security targets                                                             | 80 |
| Table 8–12 | Definition of protection demand categories                                                             | 82 |
| Table 8–13 | Coding scheme of threats                                                                               | 83 |
| Table 8–14 | Threats to the contact-less interface                                                                  | 84 |
| Table 8–14 | Threats to the transponder                                                                             | 86 |
| Table 8–16 | Threats to the reader                                                                                  | 87 |
| Table 8–17 | Threats to the key management system                                                                   | 88 |
| Table 8–18 | Threats to the backend system                                                                          | 89 |
| Table 8–19 | Threats to the customer data system                                                                    | 90 |
| Table 8–20 | Coding scheme of safeguard measures                                                                    | 91 |
| Table 8–21 | Protection of the system as a whole through introduction of interface<br>tests and approval procedures | 92 |
| Table 8–22 | Protection of the system as a whole through preventing<br>eavesdropping                                | 92 |
| Table 8–23 | Protection of the system as a whole through assuring reliable<br>transmission                          | 93 |
| Table 8–24 | Protection of the system as a whole through definition of fallback<br>solutions                        | 93 |
| Table 8–25 | Protection of the system as a whole through securing the<br>confidentiality of data                    | 94 |
| Table 8–26 | Protection of the system as a whole through confidential storage of<br>data                            | 94 |
| Table 8–27 | Protection of the system as a whole through securing the data<br>integrity when transmitting data      | 95 |
| Table 8–28 | Protection of the system as a whole through securing data integrity<br>when storing data               | 95 |
| Table 8–29 | Protection of the system as a whole through securing the system's<br>functions against DoS attacks     | 96 |

| Table 8–30 | Protection of the system as a whole through securing the function of<br>the system against incorrect operation   | 96  |
|------------|------------------------------------------------------------------------------------------------------------------|-----|
| Table 8–31 | Protection of the system as a whole through securing the function of<br>the system to prevent technical failures | 97  |
| Table 8–32 | Protection of the system as a whole through specification of the<br>system and the components                    | 97  |
| Table 8–33 | Protection of the system as a whole through ergonomic user<br>instructions                                       | 98  |
| Table 8–34 | Protection of the system as a whole through support                                                              | 98  |
| Table 8–35 | Protection of the system as a whole through EPC usage against<br>product counterfeiting                          | 99  |
| Table 8–36 | Protection of the transponder through access protection for the EPC                                              | 100 |
| Table 8–37 | Protection of the transponder against cloning                                                                    | 100 |
| Table 8–38 | Protection of the transponder against emulation                                                                  | 101 |
| Table 8–39 | Protection of the transponder against removal                                                                    | 101 |
| Table 8–40 | Protection of the transponder against unauthorised attachment                                                    | 102 |
| Table 8–41 | Protection of the transponder against unauthorised deactivation                                                  | 102 |
| Table 8–42 | Protection of the transponder against DoS attacks                                                                | 103 |
| Table 8–43 | Protection of the transponder by defining characteristics                                                        | 104 |
| Table 8–44 | Protection through fallback solution for transponder malfunction                                                 | 104 |
| Table 8–45 | Protection by preventing of movement profile generation                                                          | 105 |
| Table 8–46 | Protection by preventing the assignment of movement profile to<br>people                                         | 105 |
| Table 8–47 | Protection of readers through introduction of interface tests                                                    | 106 |
| Table 8–48 | Protection of readers through protection of reference information                                                | 107 |
| Table 8–49 | Protection of the reader against malfunction                                                                     | 108 |
| Table 8–50 | Protection through secure generation and import of keys                                                          | 110 |
| Table 8–51 | Protection through introduction of key management                                                                | 111 |
| Table 8–52 | Protection through access protection for cryptographic keys                                                      | 112 |
| Table 8–53 | Protection through securing the function of security components                                                  | 112 |
| Table 8–54 | Protection through availability of a key management system                                                       | 113 |
| Table 8–55 | Protection through definition of actions when keys are compromised                                               | 114 |
| Table 8–56 | Protection through client-specific separation of keys                                                            | 114 |
| Table 8–57 | Protection through securing the authenticity and integrity when<br>loading keys                                  | 115 |
| Table 8–58 | Protection of personal data by identification of customers                                                       | 116 |
| Table 8–59 | Protection of personal data by data minimisation                                                                 | 116 |
| Table 8–60 | Protection of personal data by separation of personal data and<br>logistical data                                | 117 |
| Table 10–1 | Protection demand of the entire system of logistical infrastructure                                              | 126 |
| Table 10–2 | Threats relevant to the contactless interface                                                                    | 127 |

| Table 10–3  | Threats relevant to the system interfaces                                         | 127 |
|-------------|-----------------------------------------------------------------------------------|-----|
| Table 10–4  | Safeguards for the interfaces of the system as a whole                            | 129 |
| Table 10–5  | Threats relevant to the contactless interface in the reader                       | 130 |
| Table 10–6  | Threats relevant to the reader                                                    | 131 |
| Table 10–7  | Safeguards for the reader and its applications                                    | 132 |
| Table 10–8  | Threats relevant to the backend systems                                           | 134 |
| Table 10–9  | Safeguards for the backend systems                                                | 135 |
| Table 10–10 | Threats relevant to the customer data system                                      | 137 |
| Table 10–11 | Safeguards for the customer data system                                           | 138 |
| Table 10–12 | Threats relevant to the key management system                                     | 140 |
| Table 10–13 | Safeguards for the key management system                                          | 141 |
| Table 10–14 | Categorisation of transponders for logistics and trade                            | 141 |
| Table 10–15 | Threats relevant to the transponder                                               | 143 |
| Table 11–1  | Protection demand in the "Fast-moving consumer goods" application<br>scenario     | 146 |
| Table 11–2  | Threats relevant to the "Fast-moving consumer goods" application<br>scenario      | 148 |
| Table 11–3  | Use cases relevant to the "Fast-moving consumer goods" application<br>scenario    | 149 |
| Table 11–4  | Safeguards for the "Fast-moving consumer goods" application<br>scenario           | 150 |
| Table 11–5  | Protection demand in the "consumer electronics" application scenario              | 153 |
| Table 11–6  | Threats relevant to the "consumer electronics" application scenario               | 155 |
| Table 11–7  | Use cases relevant to the "consumer electronics" application scenario             | 155 |
| Table 11–8  | Safeguards for the "consumer electronics" application scenario                    | 157 |
| Table 11–9  | Remaining risks for the "consumer electronics" application scenario               | 158 |
| Table 11–10 | Protection demand in the "brand-name clothing" application scenario               | 161 |
| Table 11–11 | Threats relevant to the "brand-name clothing" application scenario                | 162 |
| Table 11–12 | Use cases relevant to the "brand-name clothing" application scenario              | 163 |
| Table 11–13 | Safeguards for the "brand-name clothing" application scenario                     | 165 |
| Table 11–14 | Remaining risks for the "brand-name clothing" application scenario                | 166 |
| Table 11–15 | Remaining risks by tracking for the "brand-name clothing" application<br>scenario | 167 |

# **List of illustrations**

| Figure 1–1  | Forecast of the use of data carrier technology [GS1-1]                                                                      | 13 |
|-------------|-----------------------------------------------------------------------------------------------------------------------------|----|
| Figure 1–2  | Typical examples of process chains in trade logistics [GS1-4]                                                               | 14 |
| Figure 2–1  | Schematic illustration of the process chain under discussion                                                                | 15 |
| Figure 2–2  | Multi-dimensional factors taken into account in process analysis                                                            | 16 |
| Figure 2–3  | Process variations examined, including major features                                                                       | 17 |
| Figure 2–4  | Changes and effects in the "receipt of goods" and "warehousing"<br>logistics modules in comparison with process variation 1 | 18 |
| Figure 2–5  | Changes and effects in the "preparation of shipment" logistical<br>module in comparison with process variation 1            | 19 |
| Figure 2–6  | Changes and effects in the "goods despatch" logistical module in<br>comparison with process variation 1                     | 20 |
| Figure 2–7  | Usage scenarios at the POS (source: GS1 Germany)                                                                            | 22 |
| Figure 2–8  | The GS1 identification system: an overview                                                                                  | 27 |
| Figure 2–9  | Three examples of how the EAN is employed in different<br>technological settings                                            | 27 |
| Figure 2–10 | EPC structure                                                                                                               | 28 |
| Figure 2–11 | GS1 key identification provides access to additional information                                                            | 28 |
| Figure 2–12 | Storage areas in a second generation EPC transponder                                                                        | 30 |
| Figure 2–13 | The GS1 application identifier concept                                                                                      | 31 |
| Figure 2–14 | The GS1 standard portfolio for electronic data interchange –<br>mediators between data processing systems                   | 32 |
| Figure 2–15 | Smooth business processes using EANCOM®                                                                                     | 32 |
| Figure 2–16 | Paradigm-change from outside- to self-management of logistical<br>processes                                                 | 33 |
| Figure 2–17 | The EPCglobal Network: real-time information on request                                                                     | 34 |
| Figure 2–18 | The GS1 system                                                                                                              | 35 |
| Figure 3–1  | Entities in the trade logistics application area                                                                            | 39 |
| Figure 5–1  | Example: identification of RFID-relevant use cases for eTicketing                                                           | 45 |
| Figure 5–2  | Example of application scenarios and relevant use cases for<br>eTicketing in public transport                               | 46 |
| Figure 5–3  | Hierarchical concept for media, applications and tickets in eTicketing                                                      | 46 |
| Figure 5–4  | Concept for security considerations                                                                                         | 49 |
| Figure 5–5  | Generic security targets                                                                                                    | 49 |
| Figure 6–1  | Supply chain                                                                                                                | 50 |
| Figure 6–2  | Process P1, "Applying for and delivering the EPC Manager"                                                                   | 51 |
| Figure 6–3  | Process P2, "Individualising the transponder"                                                                               | 52 |
| Figure 6–4  | Process P3, "Attaching the transponder to an object"                                                                        | 52 |

| Figure 6–5  | Process P4, "Receipt of goods"                                 | 53  |
|-------------|----------------------------------------------------------------|-----|
| Figure 6–6  | Process P5, "Warehousing"                                      | 54  |
| Figure 6–7  | Process P6, "Shipment preparation"                             | 55  |
| Figure 6–8  | Process P7, "Goods despatch"                                   | 56  |
| Figure 6–9  | Process P8, "Stock management"                                 | 57  |
| Figure 6–10 | Process P9, "Sales"                                            | 58  |
| Figure 6–11 | Processes P10.1 "Guarantee" and P10.2 "Maintenance"            | 59  |
| Figure 6–12 | Process P11, "Disposal"                                        | 60  |
| Figure 7–1  | Use Case "Manufacture and delivery of the chip"                | 61  |
| Figure 7–2  | Use Case "Manufacturing the inlay"                             | 62  |
| Figure 7–3  | Use Case "Manufacturing the transponder"                       | 63  |
| Figure 7–4  | Use Case "Individualising the transponder"                     | 65  |
| Figure 7–5  | Use case "Setting the kill password"                           | 66  |
| Figure 7–6  | Use case "Reading the EPC data stored in transponder"          | 68  |
| Figure 7–7  | Use case "Activating the kill command"                         | 69  |
| Figure 7–8  | Use case "Example of authenticity check using EPC transponder" | 70  |
| Figure 7–9  | Use case "Key management"                                      | 71  |
| Figure 8–1  | Example of how security-related information is encrypted       | 118 |
| Figure 10–1 | Differentiation between different IT systems                   | 122 |
| Figure 10–2 | System view of the logistical supply chain                     | 123 |
| Figure 10–3 | Data exchange between entities in the logistical supply chain  | 123 |

# <span id="page-12-0"></span>**1 Description of the application area "trade logistics"[1](#page-12-1)**

# **1.1 Introduction**

Radio frequency identification (RFID) is currently developing into one of the key technologies in trade logistics, aimed at making the flow of goods faster and more transparent, and therefore more efficient and secure.[2](#page-12-2) An increasing number of transport containers and logistics units are being fitted with RFID transponders. In the future we can also expect RFID transponders to be fitted to exterior packaging. Product-related tagging (end consumer units) using RFID will become more significant in the long term. Relevant information is stored on a microchip connected to an antenna (known as a transponder), and this information is transmitted to a reader by means of electromagnetic waves. Because radio waves can penetrate materials, the transponders can be attached behind adhesive films, or even inside the packaging or in the product itself. Visual contact with the reader is therefore not necessary.

RFID is expected to supersede the currently widespread bar codes in these areas of use. The long-term parallel use of various automatic ID technologies would lead to a disproportionate relationship between expense and benefit. In open application environments, people would not know which automatic ID technology was being used at which point, which would necessitate precautionary duplication (transponders and bar codes used on the data carrier side, and RFID readers and bar code scanners on the recording side). If RFID technology is reliable enough, then a bar code backup solution will not be necessary. For isolated cases in which backups are required, the more economical option would be to provide the information in plain text. However, while the technology is being migrated, both technologies will have to be operated in parallel, and bar codes will need to serve as backups to transponders.

![](_page_12_Figure_5.jpeg)

![](_page_12_Figure_6.jpeg)

**Figure 1–1 Forecast of the use of data carrier technology [GS1-1][3](#page-12-3)** 

<span id="page-12-1"></span><sup>1</sup> See [GS1-1] and [GS1-2].

<span id="page-12-2"></span><sup>2</sup> For a categorisation of RFID applications fields, see http://www.rfid-in-action.eu/public/workpackages/rfidreference-model-1/.

<span id="page-12-3"></span><sup>3</sup> The level of usage of different automatic ID technologies in relation to one another is shown as predicted by business experts across the industry. In logistics, for instance, linear bar codes are the most commonly used form. It is assumed that RFID will continue to replace the linear bar code. The function linear bar codes fulfil in backing up RFID will be taken over more and more by 2D codes.

# <span id="page-13-0"></span>**1.2 Delineation of this Guideline**

Because this Guideline only discusses the secure use of RFID-based systems in the processes of trade, other automatic ID technologies, such as various forms of bar code, will not be discussed in any more detail. All of our considerations about RFID use in the area of trade logistics will be based on the example of EPCglobal, although, of course, systems structured in a similar way can also be used. Furthermore, the EPCglobal system can also be used in areas similar to, but not the same as, trade logistics. Another restriction is that we will only be looking at applications that are already in use today. Future applications will be integrated into this Guideline as it is updated.

# **1.3 Interaction between processes**

From the point of view of the consumer, two basic process chains can be distinguished in the field of goods supply: the first is the retail process chain with which the consumer comes into contact when he or she buys products; the second is the logistics process chain which comes before it.

![](_page_13_Figure_5.jpeg)

**Figure 1–2 Typical examples of process chains in trade logistics [GS1-4]** 

In the next section we will analyse these two process chains more closely using selected application scenarios.

# <span id="page-14-0"></span>**2 Process changes brought about by EPC/RFID**

# **2.1 The logistics process chain up to the retail outlet[4](#page-14-1)**

The following information is based on an examination of the affect which EPC/RFID has on the trade logistics processes of GS1 Germany (centralised warehouse supply).

### **2.1.1 Initial situation**

How will EPC/RFID change the processes in the logistics chains?

Experience so far in international and German pilot projects and roll-outs has given people high expectations of the potential benefits of this technology. The retail trade in particular, faced with small profit margins and fierce cost rivalry, is expecting significant increases in efficiency in its logistics procedures, as well as new ways of supporting what is referred to as "smart shopping".

According to the latest findings, the cross-company use of EPC/RFID in the processes of the consumer goods industry offers numerous potential applications – from the receiving of goods and the making-out of production orders, to quality assurance and inventory management, all the way to goods despatch. Furthermore, tagging with RFID transponders is possible across all logistical levels. Generally speaking we differentiate between pallet level, case level and item level.

### **2.1.2 Scope of analyses**

The process analyses cover the logistical chain from the supplier to the manufacturer (upstream) and from the manufacturer to retail (downstream). They are based on a simplified, central-warehouse-oriented process which is illustrated in the following diagram.

![](_page_14_Figure_10.jpeg)

#### **Figure 2–1 Schematic illustration of the process chain under discussion**

The dark coloured areas indicate the process modules which are included in the analyses. The analyses do not include drop shipment business or direct supplying, or the crossdocking process.

It is important to take into account the various factors which impact on the RFID processes.

<span id="page-14-1"></span><sup>4</sup> See [GS1-3].

<span id="page-15-0"></span>The exact form which RFID-based logistics and information processes take depends on the particular area of use concerned. The following factors are important:

- the product ranges and groups involved because of their physical characteristics and their compatibility with RFID;
- the processes which are to be supported because of their specific requirements;
- the logistical level tagged with transponders because of the differences in the types of data content required for the processing of different levels.

Different combinations of these criteria may produce variations in procedural organisation, as well as varying demands on the information processes and RFID technology used.

This gives us a multi-dimensional construct made up of the various factors, which forms a further foundation for our comparative process analyses.

![](_page_15_Figure_7.jpeg)

#### **Figure 2–2 Multi-dimensional factors taken into account in process analysis**

#### **2.1.3 Analysis of selected logistics modules**

Because various core processes always appear and reappear within the value-added chain, the following four logistics modules have been selected from the process chain to form a further basis for our analysis:

- Receipt of goods
- Warehousing
- Making-out of production orders
- Despatch of goods

This approach prevents unnecessary duplication in the description of processes.

#### **2.1.4 The ranges, technologies and logistical levels under examination**

The process examinations carried out focus on product ranges which can be transported on pallets and which, because of their physical characteristics, are easy to tag using RFID (such as textiles, leather goods and dry food ranges).

<span id="page-16-0"></span>The various processes examined differ in particular as follows:

- In relation to the technology used and the data content:
	- Bar code technologies in conjunction with electronic data interchange (EDI) and the use of an SSCC (serial shipping container code) for the identification of logistical units.
	- RFID technologies in conjunction with electronic data interchange (EDI) and the use of an SSCC for the identification of logistical units, or a serial EAN for the identification of retail units (secondary packaging).
- In relation to logistical hierarchies:
	- Goods carrier / pallet (or tertiary packaging)
	- Box / outside packaging (or secondary packaging)

The matrix below provides an overview of all the process variations examined. Each variation differs in its combination of technology type, coded data content, and tagged logistical level. All of these variations assume the electronic exchange of master data and movement data by means of electronic data interchange (EDI).

![](_page_16_Figure_9.jpeg)

**Figure 2–3 Process variations examined, including major features** 

In process versions (2) and (4) it is assumed that logistical units are tagged and identified with RFID transponders (i.e. the goods, including the container or pallet carrying the goods). The logistical units are identified using an SSCC (serial shipping container code). If goods are removed or added to the container or pallet, then a new logistical unit is formed for which a new SSCC must be issued.

Furthermore, it is also possible to tag the object on which the goods are loaded (for example when managing a pool of re-useable transport packaging units). This approach is not considered in the results of our analysis.

#### **2.1.5 Assumptions**

The following assumptions have been made for the comparative analysis of the aforementioned process scenarios:

- <span id="page-17-0"></span>• Focus
	- The discussion centres around the consumer goods industry.
	- Cross-company transport processes are not considered in the analyses.
- Conditions relating to the processes
	- The process variations are described in terms of best-practice scenarios, which means that EAN 128 transport labels, serial shipping container codes (SSCC) and electronic data interchange (EDI) are already being used.
	- The availability of an electronic despatch device (DESADV) is assumed.
	- The EANs of the delivery units are the same as the EANs of the ordered units.
	- Received goods are subject to manual quantity control (in relation to the number of secondary packaging units), especially mixed pallets.
- Conditions relating to technology
	- The EPC data standard is used to determine the data content in process variations 2, 3 and 4 (use of RFID technology).
	- It is assumed that defined filter values for logistical hierarchies are available.
	- 100 per cent legibility is aimed for in all process variations.
	- It is assumed that there is a working connection between the RFID hardware and software and the internal systems.

### **2.1.6 Summary of results**

The following overviews provide summaries of the results of the process analyses. They depict the effects and changes which RFID-based processes bring about in comparison with bar code-based process variation (1)

Because of the similarity of the results from process variation (3) (use of tagged boxes or secondary packaging units) and process variation (4) (combined use of tagged goods carriers and tagged boxes), only process variation (4) is taken into account in the results summaries.

The "receipt of goods" and "warehousing" logistics modules

![](_page_17_Figure_18.jpeg)

**Figure 2–4 Changes and effects in the "receipt of goods" and "warehousing" logistics modules in comparison with process variation 1** 

<span id="page-18-0"></span>In process variation (2) (tagged goods carriers / logistical units), there are no significant changes from the bar code-based process variation (1) in the modules "receipt of goods" and "warehousing". In both cases, the serial shipping container unit (SSCC) encoded in the bar code or transponder is recorded and utilised to identify the logistical units involved. The RFID-based process offers the advantage that the scanning procedure can be done in one movement (that is, the goods carrier is moved through an RFID gate and brought directly to its destination). Furthermore it is possible to read the data stored in the transponder without visual contact between the reader and the transponder.

In process variation (4), fundamental changes to the process were identified which involve significant benefits additional to those of variation (2). For example, detailed manual inspection of the packaging units on the goods carrier is no longer necessary, since every secondary packaging unit is clearly identified by scanning its RFID transponder. In this way, the goods received can be automatically registered following the procedure of fully automatically comparing them with the electronic despatch advice (DESADV). If discrepancies are identified during this comparison, rules can be defined about what to do (exception management).

![](_page_18_Figure_3.jpeg)

The "preparation of shipment" logistical module

#### **Figure 2–5 Changes and effects in the "preparation of shipment" logistical module in comparison with process variation 1**

In process variation (2) (handling of goods carriers tagged with RFID transponders), as in the "receipt of goods" and "warehousing" logistics modules, there were no significant changes from the bar code-based process variation (1).

Variation (4) offers advantages when it comes to preparing mixed pallets. It allows the packaging units assembled for shipment to be recorded precisely without manual intervention being necessary; for instance, this can be done when the goods are placed onto the pallet using a reader fitted to the forklift. Manual confirmation of the picking procedure is no longer necessary, and the risk of undetected errors during shipment preparation (such as scanning the right product number but picking the wrong product) is minimised. Quality assurance takes place during the shipment preparation process, which only has to be interrupted in the event of an error in preparation.

There are no particular benefits in the process of preparing shipments of a single type of product on single pallets or goods carriers. Generally speaking, the whole pallet is prepared for loading without a change in logistical unit.

<span id="page-19-0"></span>The "goods despatch" logistical module

![](_page_19_Figure_2.jpeg)

#### **Figure 2–6 Changes and effects in the "goods despatch" logistical module in comparison with process variation 1**

In process variation (2) (handling of goods carriers tagged with RFID transponders), as in the previous logistics modules, there were no significant changes from the bar code-based process variation (1).

Process variation (4) offers the option of identifying accurately every single secondary packaging unit on the goods carrier, in addition to the SSCC of the logistical unit. This information can be used for a final comparison with the transport order and shipment preparation details, or it can be given to the recipient.

#### Summary

The comparative process analyses revealed that fundamental process changes and affects can be expected in particular when secondary packaging is used that has been tagged with RFID transponders. The possibility of capturing data in bulk (in other words, all of the packing units on a pallet can be recorded in one scanning process without visual contact) means a new level of quality in automated counting and registering processes. This benefit is particularly effective when handling mixed pallets.

#### **2.1.7 Conclusions**

The results of the investigation of the processes produce the following conclusions about conditions required for the use of RFID technology in the logistical chain, and the consequences of that use:

#### Conditions

- A considerable period of time will be required during which RFID and bar code technology are used in parallel.
- Organisational backup solutions are required (such as plain text information or databased precautions).
- IT architecture will have to be expanded, and solutions provided for depicting the electronic product code (EPC)

<span id="page-20-0"></span>• RFID should be seen as part of a broader context, because its isolated use in scattered application areas will not produce any real benefits in the long run. It is possible, however, to begin with individual areas.

Effects

- Communication structures may change.
- The benefits would probably be much greater if we were to compare an RFID-based process with a process which is not yet supported by EDI or EAN 128.
- The use of RFID and electronic product codes (EPC) opens up a new level of data management which will enable users to respond more effectively to new and future requirements and regulations (such as the ability to trace the origins of food).
- It can basically be assumed that considerable benefits will be gained by extending tagging to the product or item level.

# <span id="page-20-1"></span>**2.2 The retailer–consumer process chain**

The benefits of using RFID at product level in retail outlets can be roughly divided into the following categories: cost reduction, qualitative process improvements, enabling more sales through new services, and protection against counterfeit products and brand piracy. Examples within these categories are as follows:

Cost reduction, e.g. through

- Securing goods
- Simplified inventory management

Process improvements, e.g. through

- Shelf management
- Accurate tracing in the event of goods recalls

New services

- Information terminals
- Intelligent shelves
- Cross-selling services
- Self-checkout
- Paperless goods exchange
- Paperless guarantee services

Protection against counterfeit products and brand piracy

- Prevents loss of sales
- Protects brand image
- Protects against product liability problems, etc.

<span id="page-21-0"></span>![](_page_21_Figure_1.jpeg)

**Figure 2–7 Usage scenarios at the POS (source: GS1 Germany)** 

An important element in the successful introduction of RFID labels at product level is that the customer perceives a direct benefit. In addition to the new services listed above, one example of such a benefit is the ability to verify the authenticity of a product.

These applications imply that RFID technology will have to fulfil the following requirements:

- 1 Transponders always relate to goods and never to people. Personal data is never stored in a transponder.
- 2 AutoID which means automatic, reliable identification using RFID technology is required. The range may be up to several metres.
- 3 Only very limited amounts of data are stored in the chip, and this data does not have to be modified.
- 4 Product-related use of transponders demands an extremely cost-effective transponder solution in order to be economically viable.

Depending on the product and the area of application, the use of RFID can have a range of implications. In the following, three exemplary scenarios are used to illustrate as many of these as possible.

#### **2.2.1 EPC/RFID application for fresh goods**

Fresh goods are goods which are highly perishable. They are food items which are consumed within a few days. Products or packages fitted with a transponder, if not removed or deactivated during purchasing, would only remain for a short time with the consumer and would be disposed of in the household waste.

RFID can be used in the following different areas:

• In the sales area

The speed benefits of RFID when registering and handling goods mean that the goods can reach retail outlets more quickly, thereby increasing their freshness and availability.

Trust in the quality of goods also plays a very important role. Information terminals coupled with the EPCglobal Network can provide consumers with full documentation of a product's origins. In the case of temperature-controlled logistics, the combination of

<span id="page-22-0"></span>RFID and sensors can prove to customers that the correct refrigeration temperature has been maintained throughout the whole supply chain.

• At the checkout

If the sell-by date is encoded on the transponder in addition to the EPC, or if it can be accessed from background systems when the EPC is read, then a discount system can be set up involving reductions for food with less time remaining on it.

• Use after purchase

Provided the transponder is not removed or deactivated when the product is purchased, intelligent electronic household appliances such as RFID-compatible refrigerators can automatically provide consumers with information, such as a warning when best-before dates are about to lapse – provided this date is saved in the transponder or made available by the manufacturer through the EPCglobal Network.

#### **2.2.2 EPC/RFID application for textiles and clothing**

Textiles means fashion products. With these products it is important that the consumer likes them and that they fit properly; more assistance is required when purchasing these products.

Transponders can either be attached to the product label or woven into the material. Transponders fitted to goods, provided they are not removed or deactivated during purchasing, would be removed by the customer at home (in the case of labels) and disposed of in the rubbish. If woven into the fabric, the transponder will remain in the product permanently, although it could be deactivated at a later stage.

Again there are several areas in which RFID can support the purchasing process:

• In the sales area

If shelf areas are equipped with RFID, then inventories can be maintained permanently. Then, for example, it is easy to find out whether the products of the required size are on the shelves or in the stock-room. It is also easier to notice if the products are not in the right place, and this can then be rectified more easily.

Using displays, customers can obtain information about products they are interested in (size, price, care instructions, and so on), which means that they do not have to look for this information on the products themselves. RFID changing rooms can also provide customers with advisory information when they try on the clothes, such as different available colours and combinations with the products they are choosing. Furthermore, the EP-Cglobal Network can be used to provide consumers with full documentation of origin, thus certifying that branded goods are authentic.

• At the checkout

Goods can be registered more quickly, meaning high service levels can be maintained.

• Use after purchase

A transponder on a product could be used as proof of purchase. If a customer does not like a product after all, or if it does not fit, then the process of exchange could be simplified. If a customer asks about exchanging a product, EPC could be used to determine whether the product was really bought there or not.

In this respect it is important to decide whether the transponder is to be fitted to a removable product label which is taken off before use, or whether the transponder remains in the product. If (and only if) the transponder remains in the product, and the product is worn after purchasing, then the RFID tag could be scanned again at the exit when the customer leaves the shop. Under current laws about privacy and consumer protection, it would only be legal at this point to ascertain whether the EPC is or is not part of current stocks; if it is, then this could indicate shoplifting. Without the permission of the cus<span id="page-23-0"></span>tomer, the EPC cannot be stored in such cases, which prevents the creation of movement profiles.

A transponder permanently attached to an article of clothing can be used in conjunction with intelligent electronic household appliances. An RFID-compatible washing machine could, for example, warn users if items of clothing are in the machine which should not be washed together, or not at the selected temperature – provided the transponders have not been deactivated. This is also provided that the additional information is either stored in the transponder, or made available by the manufacturer as part of the EP-Cglobal Network for retrieval via an Internet link.

The EPC concept does not envisage the storage of personal data on the transponder.

#### **2.2.3 EPC/RFID use for durable electronic goods**

More durable electronic goods, such as flat-screen televisions, usually already carry a serial number which is attached to the product as a bar code, in order to enable the product to be registered automatically not only during manufacture, but also, if required, during subsequent repair work (and in some products also during servicing).

• Use in the sales area

The EPCglobal Network combined with information terminals could be used to provide consumers with full documentation of origin, thus certifying that branded goods are authentic.

• Use after purchase

A transponder on a product could be used as proof of purchase. If the product does not work properly, a transponder which has not been deactivated can be used to facilitate guarantee claims since it is evidence of purchase.

# **2.3 Technological interaction – The GS1 System**

Information technology systems can only be used smoothly and efficiently to send and receive information between different operational centres if all of the computers which "talk to each other" within an industry, a branch of trade or an information chain support the same organisational model. This means, for example, the same structure of data sets, key variables and content, and so on. In addition to agreements between different operations, it is also important that certain working processes and organisational instruments are standardised.

More than one million companies throughout the world utilise the GS1 standards for identification and communication purposes in commercial processes. They are the most widely accepted standards in trade logistics. The rules of the system have been defined as binding by GS1. Developments which complement and supplement the system are actioned collaboratively by those involved in the project.

### **2.3.1 Orientation of the GS1 system**

The GS1 system provides the technological foundation for countless inter-firm electronic data transactions throughout the world. The philosophy of the system creates a link between the recording and transmitting of data.

• Automatic data capture (ADC) is used to identify goods or services at a particular place in the company (e.g. where the goods are received or in the warehouse).

Automatic data capture makes checkout processes in modern retail operations more rational, faster, and cheaper. It also simplifies the handling of products in warehouses across the market, and on the transport routes between those warehouses. The most important components of this process are clear, unique product and package identification numbers in conjunction with standardised bar code and radio frequency technology.

- Automated electronic data interchange (EDI) is a suitable method of exchanging master and movement data between large numbers of users; this means data which initiates physical processes, accompanies them, and is sent in advance of them and after them. In electronic data interchange, the message generated in the originating computer system – such as an order or an invoice – is sent directly to the recipient computer system. This information does not have to be inputted again in order to be processed, provided the companies involved in this kind of data exchange agree on certain rules of presentation and syntax. Once again, the use of standardised numbering systems for products and locations is an important precondition for the success of rationalisation measures.
- The combination is in this case greater than the sum of its parts. Scanning and radiofrequency reading at numerous points of the entire logistical chain, and electronic communication, must be used in conjunction with one another as part of a comprehensive and sustainable rationalisation approach. Business data can be exchanged quickly, efficiently and securely using this combination of modern recording and transmitting technology.
- The GS1 system therefore places emphasis on the flexibility and openness of applications in a way which can only be achieved on the basis of this system philosophy. This is what differentiates EAN from attempts to overload the identification itself with other information, which in the end leads to restrictions and hindrances (isolated solutions)
- The GS1 system is a widely recognised standard in cross-border applications. It defines scanning technology and data content as well as a clear numbering system. The numbers allocated are globally unique, which enables their use in wide areas of application. These standards have become established internationally for open communication in many sectors.
- The technical GS1 standards are being supplemented steadily by organisational standards governing operational procedures as part of the ECR initiative (ECR = Efficient Consumer Response). These process agreements can aid the application of the standards considerably.

The four basic principles of the GS1 systems are:

1 Open Standards

The aim is to create an open, demand-oriented, integrated system of technical standards for identification and for the transfer of information, in order to facilitate effective supply chain management in any company and any industry, anywhere in the world.

2 Differentiation

The system is based on rules, which, if followed, enable the global, non-duplicating and unique identification of completely different things such as products, transport units, containers, objects and locations.

3 Transparency

GS1 standards have to be relevant and applicable to every supply chain, regardless of who applies, receives or works with the standards. The idea is to make processes uniform, thereby creating potential savings for the benefit of everyone involved. New features are only included in a standard if they open up new areas of application or lead to an improvement in existing applications.

4 Non-Significance

Globally unique EAN identification can only be guaranteed if the standard numbers are handled as a whole. For example, product characteristics or features should not be en<span id="page-25-0"></span>coded in the number itself, but rather the EAN number should be used as an access key to obtain that information from a file or another data source.

The GS1 system, therefore, is a comprehensive system of regulations, which:

- is international
- is not industry-specific (multi-industry standard)
- is beneficial at every stage of the value-added chain (raw material supplier, supplier, shipper, wholesale, retail, all the way to the consumer)
- helps to optimise the flow of information and the flow of goods
- utilises a wide range of media to transport its data.

It is possible but not essential to adapt a company's organisation completely to these regulations. The components of the GS1 system can also be seen as a "translation" of the company's internal language into a form of understanding which is not specific to any company, and which can be adopted by business partners into their own corporate worlds.

# **2.3.2 The components of the GS1 system**

The GS1 system is related to RFID in several ways: the electronic product code (EPC) is used for identification, an EPC transponder is used to carry data, and the EPCglobal Network is used for data communication; all these are complimentary elements within the GS1 system as a whole.

### **2.3.2.1 Identification systems**

The GS1 identification system is based on the principle that an object is best identified using a short, globally non-duplicating, non-significant number. This number can be used in turn as an access code for obtaining further information stored in databases under this number – in other words information about the object concerned.

This concept makes identification processes simple, secure and fast, and has proven itself and caught on over recent decades for that reason.

Because there are many different kinds of objects (such as locations, goods carriers, service products), and because these objects have to be identified in very different quantities and contexts by different users, GS1 has created a set of identification numbers with varying capacities.

#### Identification numbers – an overview

All GS1 identification numbers have the same uniform structure. This centres around the GS1 basic number, which GS1 provides to users. To that, the user adds either an object reference, a serial section, or both components.

<span id="page-26-0"></span>![](_page_26_Figure_1.jpeg)

#### **Figure 2–8 The GS1 identification system: an overview**

The international location number (ILN) is used to identify places and addresses; the international article number (EAN) identifies goods and services; the serial shipping container code (SSCC) identifies logistical units; the global returnable asset identifier (GRAI) identifies reusable goods carriers; and the EAN container number (GIAI) identifies any kind of container. Any of these numbers can also be incorporated into the EPC.

All of these numbers can be incorporated into the EAN, EAN 128, GS1 DataBar, EAN Composite, EAN Data Matrix bar codes, and in the EPC transponder, and can be protected against mistaken identification. The international number allocations are managed by members of GS1, which in Germany means GS1 Germany.

#### Different formats – identical content

Just as "1.0", "100%" and "1/1" are three different ways of presenting the same information, so too are different formats required at different points in the value-added chain in order to facilitate technologically effective use. This simply means that the information is translated into a language which the individual technical equipment understands. GS1 bar codes are based primarily on an application identifier concept, EDI messages from GS1 on a qualifier concept, and EPCglobal Network information is based on a uniform resource identifier concept.

This enables the same information – which is primarily the GS1 key identifier – to be communicated across different technological and company-related interfaces between different business partners. The following diagram shows some examples of this:

![](_page_26_Figure_8.jpeg)

#### **Figure 2–9 Three examples of how the EAN is employed in different technological settings**

The following structure is used to store the EPC on a transponder

<span id="page-27-0"></span>![](_page_27_Figure_1.jpeg)

**Figure 2–10 EPC structure** 

The structure of the EPC, which begins with a defined header, enables different coding schemes to be made unique for all EPC-compliant transponders. A filter variable which is not part of the actual EPC identification, can enable selective and therefore faster filtering during reading and writing processes.

Differentiating between key identifiers and additional information

Dealing with the flow of goods and data at the different process stages requires relevant information which is accessible via a range of information sources (internal/external sources). The GS1 identification numbers act as access keys to enable this information to be addressed accurately.

Important basic rule**:** the best approach, regardless of company, is always the philosophy of "as much information as necessary, but as little as possible, in the data carrier." This means that the identification is encoded in the bar code or transponder, whereas all other information, if at all possible, is held in the master data, in the information which precedes the goods, or is available in real time by data query. This is the only way to guarantee the maximum possible flexibility in communication between applications and companies.

![](_page_27_Figure_7.jpeg)

![](_page_27_Figure_8.jpeg)

#### **2.3.2.2 Data carriers**

The GS1 system includes bar code and transponder solutions.

• EAN 13 bar code

The EAN 13 bar code is the oldest of the GS1 data carriers. Almost every consumer product carries one. It always contains an EAN article number, and it does not include any other GS1 identifier or any other additional information. The EAN 13 is scanned omnidirectionally – in other words, the direction of scanning is important.

• EAN 128 bar code

The EAN 128 bar code was introduced in the 1990s primarily to enable logistical processes to be automated. The application identifier concept was also developed for this bar code. The EAN 128 standard in conjunction with the application identifier, offered – and still offers – the utmost flexibility. Alongside a unique identification, such as the SSCC or the EAN, it allows additional information to be applied to a product or its packaging in standardised bar code form to accompany the goods – even if only for an interim period until EDI begins to be used and the necessary information is exchanged electronically in advance.[5](#page-28-0) 

EAN 128 has grown enormously in importance in recent years, in particular on account of more stringent demands on the traceability of products.

• GS1 DataBar[6](#page-28-1)

The GS1 DataBar was developed and introduced by GS1 as a worldwide standard because EAN 13 and EAN 128 bar codes take up a relatively large amount of space on a label, especially when identifying products, and because certain applications can therefore not be covered by EAN 13 or EAN 128. The GS1 DataBar also closes gaps in the system of coding consumer units which require, in addition to the EAN article number, additional information in order to enable an efficient process – for example, clear identification of products of varying weight, such as meat.

• EAN Data Matrix

The EAN Data Matrix is the most recent GS1 code. Unlike previous GS1 symbols, the EAN Data Matrix is a two-dimensional symbol in which a very large amount of information can be encoded in a very small space. But because it is a 2D code, the EAN Data Matrix is only suitable for applications in which the appropriate scanning systems are being used. These systems are based on modern image processing technologies, which is why they are also referred to as image scanners.

• EPC/RFID

RFID is an alternative data carrier to the bar code. The electronic product code (EPC) is the generic term for the serialised identification of products, packages, locations, and so on, which is attached to the goods or to another object using a transponder which is compliant with EPC specifications. That in turn is based on the GS1 identification codes ILN, EAN and SSCC.

RFID technology and the EPC offer the following benefits:

- Very quick to read (time saving).
- Visual contact with the reader is not required.
- Highly reliable, even under extreme conditions such as low temperatures or direct sunlight.
- Enables permanent inventory by permanently scanning goods.

<span id="page-28-0"></span><sup>5</sup> The identification number placed on the goods can basically always be used as a reference to master data

or to the information provided in advance by EDI.

<span id="page-28-1"></span><sup>6</sup> See also ISO/IEC 24724

- <span id="page-29-0"></span>• Enables clear exchange of information in real time in combination with cross-company information systems.
- Bulk registering features (fast recording, high level of detail).
- Position of goods can be determined precisely, and the timing of goods despatch can be optimised.
	- The identification function can easily be extended to include additional electronic features such electronic theft prevention and sensors.

While the technology is being migrated, and for backup reasons, it is assumed that RFID and bar codes will be used in parallel for a considerable period of time.

The logical storage allocation in a transponder can be divided into the following segments:

![](_page_29_Figure_7.jpeg)

![](_page_29_Figure_8.jpeg)

 The reserved storage area can be used to store an access password and a kill password which prevents the kill command from being executed without authorisation.

As well as the actual identification number, or electronic product code (EPC), the EPC storage area contains a checksum for assessing correct data transfer (CRC-16) and protocol control bits which specify variables such as the length of the data stored.

The transponder identification number (Unique Tag ID) is for purely technical purposes, such as the manufacture of integrated circuits. It is also used in certain types of anti-collision process. It is allocated when the chip is manufactured and should be unalterable thereafter.

The application data area can be used to store other data. Standards do not yet exist for this storage area, whose size depends on the transponder used.

RFID systems are radio systems governed by the regulations of the *Bundesnetzagentur für Elektrizität, Gas, Telekommunikation, Post und Eisenbahnen* (German Network Agency for Electricity, Gas, Telecommunications, Post and Railways). Only a small number of frequency bandwidths can be used, and these are distributed across the spectrum from short to ultrashort, all the way to microwave wavelengths. The use of ultra-high frequency (UHF) has proved particularly suitable for trade logistics. The UHF bandwidth upon which the standardisation of EPCglobal is based is between 860 and 960 MHz.

#### The GS1 application identifier concept

An exact definition of data elements enables a wide range of information requirements to be depicted in a structured and automatically recordable form in a variety of EAN bar code and EPC transponder standards. This relates mainly to data which goes beyond pure identification, and which offers many benefits all along the logistical chain – such as batch number, sell-by date, and so on. There are now more than 60 data elements available in the fields of identification, goods tracking, dating, units of measurement, and address information.

<span id="page-30-0"></span>The GS1 application identifier concept is based on three pillars:

- Exact definition of data elements (data content).
- Definition of their data formats (field length, available characters).
- The allocation of qualifying application identifiers.

Each application identifier serves to indicate the information which will follow it – in other words, the data element and its format. In this way it forms a basis for the fault-free processing of information. Internationally standardised in ISO/IEC 15418, and incorporated into the protected EAN bar code symbology, the application identifier concept offers the utmost interpretation precision along with maximum data quality.

All modern GS1 data carriers – i.e. bar codes and transponders – utilise a uniform procedure in the form of the application identifier concept described here, to automatically differentiate between GS1 identifiers and the necessary additional information. This concept defines which data is to be encoded in the bar code or transponder. The data content is always processed in the same way, regardless of the data carrier technology. The globally nonduplicating numbering systems ILN, EAN, SSCC, and the EPC developed for their encoding in the transponder, are utilised as references to electronically transmitted messages and data enquiries, such as electronic orders and delivery advices sent by EANCOM® and event management via the EPCglobal Network. The application identifier concept connects together the various information elements in the GS1 data carriers.

This means, conversely, that EPC/RFID data carriers do not include any information which is not already used in bar codes.

![](_page_30_Figure_8.jpeg)

**Figure 2–13 The GS1 application identifier concept** 

#### **2.3.2.3 Data communication**

Electronic data interchange (EDI) – the connecting element between automated identification scanning and the flow of goods

The GS1 identification systems and data carrier portfolio are completed by a set of standards for the electronic exchange of data. These standards help companies to streamline their business transactions to the maximum possible extent. Identification systems are often the starting point of an automated procedure, since they are attached to the goods and transmitted electronically to the business partner together with all the relevant accompanying information.

Electronic data interchange (EDI) means the exchange of structured data between computer systems in a standardised format which computers can read. Because it avoids interruptions

<span id="page-31-0"></span>in media, EDI makes the communication process faster and also increases the reliability of the content of the messages being sent. One of the factors which makes it economically superior is that it eliminates multiple data entries and the mistakes that can be made when members of the logistics chain enter information manually.

![](_page_31_Figure_2.jpeg)

#### **Figure 2–14 The GS1 standard portfolio for electronic data interchange – mediators between data processing systems**

EANCOM® provides users with a standard catalogue of messages with which complete business transactions can be performed electronically.

![](_page_31_Figure_5.jpeg)

**Figure 2–15 Smooth business processes using EANCOM®** 

The EPCglobal Network: exchanging real-time information over the Internet

The purpose of the EPCglobal Network is to make large amounts of highly granular information about goods movements and statuses available to all business partners. What it does not include is the exchange of forecast data, invitations to tender, acquisition processes, invoicing procedures, and so on. These are all handled as before using established EDI procedures. This means that the Network is used to initiate data queries about products, transport units, or other objects. In this way the EPCglobal Network represents an ideal supplement to EDI by offering more of the benefits of electronic communication.

The basic principle of the EPCglobal Network is to make product information available at all times using the Internet. It therefore represents a specific application of a concept which is generally referred to as the "Internet of Things". The EPCglobal Network connects peripheral servers containing all of the relevant EPC information (that is, all of the master and movement data relating to a particular EPC). Authorised data transmission is executed over the

<span id="page-32-0"></span>Internet. Various Network service components control the servers and authorise access to the information.

![](_page_32_Figure_2.jpeg)

#### **Figure 2–16 Paradigm-change from outside- to self-management of logistical processes**

The EPCglobal Network works on the basis of interaction between a range of components for which EPCglobal provides standardised interfaces, including ones for internal company use. The key to the EPCglobal Network is the EPC. The object name service (ONS) is used to find an EPC within the EPCglobal Network. It enables authorised users to locate product information about an EPC in databases. In addition to interfaces for RFID applications, other interfaces belonging to the Network also work using GS1 bar code models.

The benefits of the EPCglobal Network are:

- It provides real-time information.
- It provides clear information all along the entire value-added chain. Without the Network, information transparency is only partially achieved between "neighbouring" interfaces.
- It provides standardised interfaces at *all* data transition points, which means from the transponder to the reader, from the reader to the middleware, from the middleware to the internal application, and from the internal application to the cross-company application.
- It provides a granular representation of the flow of goods.

<span id="page-33-0"></span>![](_page_33_Figure_1.jpeg)

**Figure 2–17 The EPCglobal Network: real-time information on request** 

All of the other potential benefits associated with the use of RFID (such as prevention of theft and brand piracy, seamless tracking, time-saving, and so on) are derived from the availability of real-time information and improved transparency. This means that the potential benefits of RFID technology can only be fully utilised on the basis of a global communication and information network in which authorised users are able to exchange the data they need.

#### **2.3.2.4 Summary**

The GS1 system is a modular "toolbox" for optimising the flow of information and goods between companies. This system revolves around the GS1 identification systems which are supplemented by data carriers such as bar codes and RFID, along with processes for the electronic exchange of data. All of the tools in this system are compatible with one another, and can be brought together and implemented gradually to create a comprehensive, integrative overall solution for smooth and efficient business transactions.

It is important to note that GS1 provides not only the basic elements such as data content, data carriers and data exchange, but also other services based on these basic elements. These include, for example, the activities associated with EDIINT AS2, which makes EDI more secure over the Internet; and it also includes standardisation services in the field of classification.

Using these instruments as a foundation, recommendations are drawn up to facilitate efficient business processes. Of particular interest among these are the process recommendations which are being produced as part of the Efficient Consumer Response (ECR) initiative.

<span id="page-34-0"></span>![](_page_34_Figure_1.jpeg)

**Figure 2–18 The GS1 system** 

The GS1 system is continuously being developed by means of new technologies and in response to the demands of industry. But whatever improvements are made to the system, the compatibility between its various standards is preserved.

# <span id="page-35-0"></span>**3 Agreements**

# **3.1 Definition of terms**

#### Application

The application provides specific functions and structures to enable a transponder to receive and make available an EPC, and for the EPC to be used in a background system. In this particular area of use, the application is defined by GS1/EPCglobal in the data specifications for the electronic product code (EPC) and the air interface specification EPCglobal Gen2 (equivalent to ISO 18000-6 Rev1.2). The application owner is GS1, which is the provider of EPCglobal.

#### Operating process

A complete set of operational procedures. One example is the way the logistical supply chain is depicted.

#### Cross-selling

Cross-references to other products and product categories.

#### EAN product number (GTIN, Global Trade Item Number)

This international product number is a globally coordinated, standardised, internationally non-duplicating 8, 13 or 14 figure number given to products and services. It forms the basis for the use of scanner technology.

#### EANCOM®

EANCOM® is an invented word combining EAN and COMmunication. It refers to a standard of electronic data exchange which is an official subset of UN/EDIFACT. The standard was developed and evolved by GS1. EANCOM® is the recommended EDI standard for ECR.

#### Efficient Consumer Response (ECR)

ECR is a joint initiative of manufacturers, wholesalers and retailers and other members of the supply chain who have collaborated to improve processes and thus provide consumers with the best possible quality, service and product diversity.

#### Application area

The area in which the Technical Guidelines are intended to apply. The highest unit in the terminological structure. Incorporates one or more applications, the products and application aims supported by those applications, and the application scenarios that result from that.

Application scenario

A particular mode of looking at the application area in terms of how specific application aims are supported.

#### Electronic product code (EPC)

The EPC is a numerical code for the unique identification of objects. The EPC is stored on a transponder which is attached to a product or other goods. Links in the EPCglobal network enable other data belonging to that object to be accessed via the Internet. In trade and logistics, the EPC is based primarily on the GS1 numerical identifiers.

#### EPCglobal

EPCglobal was founded by GS1. This non-profit organisation develops commer-

cial and technical standards for the EPC network and introduces them onto the global market. On a national level, EPCglobal is represented by each country's national GS1 organisation (in Germany's case that means GS1 Germany).

#### EPC Information Services

(EPCIS = EPC Information Services)

EPC Information Services provide a connection between a company and the EPCglobal network. They store the EPC information generated within the company and exchange data between system applications of network members and certain network components. Product information and events can be saved via standard interfaces and made available to network members.

#### EPCglobal network

The EPCglobal network is an infrastructure which enables peripherally stored information about EPCs and the objects associated with them to be made available globally via the Internet. Components of the EPCglobal network include EPC Information Services, EPC Security Services, EPC Discovery Services, and the ONS.

#### EPC manager

The EPC manager provides a globally unique identifier to an entity issuing EPCs, and is given to the company by a national EPCglobal representative institution (GS1 member organisation).

#### Risk transfer

The logistical point at which products are passed from one company to another.

#### GS1

International organisation based in Brussels which promotes and develops the GS1 standards (EAN, ILN, NVE, EANCOM®). Includes more than 100 national GS1 organisations throughout the world, including GS1 Germany.

#### GS1 standards

GS1 standards are globally established, standardised identification and communication processes. The basic elements of the EAN system are:

#### **Identification systems**

(e.g. the identification numbers ILN, EAN, SSCC)

#### **Auto-ID systems**

(automatic data capture based on EAN 13, EAN 128, RSS bar codes and RFID radio frequency technology, etc.)

#### **Electronic communication standards**

(e.g. EANCOM®, WebEDI, XML, etc.)

#### Interoperability

Interoperability means that every transponder will work in every environment that can occur as part of the operating processes defined for a particular implementation of a solution.

#### Delivery advice (DESADV)

EANCOM® message type. The delivery advice contains details of goods sent on agreed terms. Its purpose is to provide the recipient of goods with details of what the shipment contains. The message includes a reference to the place of despatch and one or more places of delivery, and can contain numerous different items, packages and orders. It tells the recipient which goods were sent and when, and enables the recipient to prepare to receive the goods and to compare the delivery details with the details of the order placed.

#### <span id="page-37-0"></span>Logistics data

Data generated in conjunction with the use of RFID as part of operating processes defined for a specific logistical implementation. It can include information such as the status and position of a particular item, which is acquired by reading the RFID transponder.

#### Object

In this sense 'object' refers to an item fitted with a transponder and relevant to the trade logistics process. It may be the product itself, or something goods are carried in, a pallet, packaging, a reusable container, and so on.

#### Self-checkout

A checkout till operated by the customer.

#### Serial Shipping Container Code (SSCC)

The Serial Shipping Container Code (SSCC) identifies a transport unit clearly and unmistakably with a standardised 18-figure numerical structure.

#### Statistical data

Statistical data provides information about the general usage of a system.

#### Tracking & tracing

A system for following the movements of a shipment. Tracking refers to determining the current status, tracing follows the ex post progress of the shipment.

#### Transponder

A system comprising a passive RFID chip and an antenna as described in the air interface specification EPCglobal Gen2 (corresponds to ISO 18000-6 Rev1.2). The antenna can be implemented in a variety of ways, and may even be part of the product. The transponder can be attached to a range of materials, and may take a variety of forms.

#### Use case

Detailed description of a series of activities that constitute part of an operating process. One example is the initialisation of a transponder.

## **3.2 Allocation of roles and entities in the trade logistics application area**

#### **3.2.1 The logistics process chain up to the retail outlet**

The roles and responsibilities shall be described on the basis of the specifications and recommendations of GS1.

<span id="page-38-0"></span>![](_page_38_Figure_1.jpeg)

#### **Figure 3–1 Entities in the trade logistics application area**

Actor

An entity that operates in accord with the role assigned to it.

Application owner

In the trade logistics area, the EPCglobal application is used in the transponder and in the other components of the system as a whole (readers, background systems, etc.). The application owner is GS1, which is the provider of EPCglobal. The application owner markets the application.

#### Chip manufacturer

The chip manufacturer makes the chip used in the transponder, and does so in compliance with the EPCglobal specifications. The chip manufacturer allocates the chip's unique serial number and, where necessary, keys and passwords to protect the chip.

#### Transponder manufacturer

The transponder manufacturer makes the transponders. The transponder manufacturer allocates, where necessary, keys and passwords to protect the chip

Issuer

The issuer brings the transponders into the supply chain. Any of the entities of the supply chain (packaging manufacturer, product manufacturer, wholesaler, retailer) can assume the role of the issuer. The transponder manufacturer supplies the issuer.

#### EPC issuer

Describes the issuer in the terminology of GS1/EPCglobal. Within the numerical range allocated to him on request by GS1, the EPC issuer allocates the EPC to the object being identified (e.g. a product or logistical unit). The general rule is: the company which owns the product's brand name is responsible for allocating the EPC, regardless of who manufactures it and where. The EPC issuer can therefore be

- ... the manufacturer or supplier, if the product is sold under a brand name which the manufacturer or supplier owns.
- ... the importer or wholesaler, if the product is manufactured for that entity and sold under a brand name which it owns, or if the product is modified by the importer or wholesaler (e.g. the packaging)
- ... the retailer themselves, if the product is manufactured for that company and sold under a brand name owned by the company (retailer brand)
- ... (more generally) a customer, if the product is manufactured especially for the customer and can only be ordered by that customer.

#### Exceptions:

- 1 Items that have not yet received EPCs from the brand issuer. Example: if an importer/wholesaler purchases goods which, for whatever reason, have not yet been coded with EPCs on the manufacturer side, then it is possible to form an EPC (temporarily) using the importer/wholesaler's basic number. If the manufacturer/brand owner introduces the GS1 system at a later stage, then the importer/wholesaler's transitional EPC is replaced by the manufacturer's EPC.
- 2 Items without brand names, and generic products. Items without brand names and generic products are given EPCs "at source", i.e. by the manufacturer. This can lead to situations in which items that look identical have different EPCs, especially in the case of generic products, something which can have implications for the structure of databases. Examples of products of this kind include: candles, drinking glasses, etc.

#### Packaging manufacturer

Manufactures the packaging of a product. If the transponder is to be connected to the packaging and not the product itself, then the packaging manufacturer may attach the transponder, and may also load it with the EPC and other information such as a kill password.

#### Manufacturer

Manufactures the product. If the transponder is to be connected to the product itself, then the manufacturer normally attaches the transponder and also loads it with the EPC and other information such as a kill password.

#### Logistics provider

The logistics provider transports, stores and/or distributes the product. It may also provide other services. More than one logistics provider may be used in a product's supply chain in order to connect up the various sections.

#### Wholesaler

The wholesaler sells the product to a range of retailers. The wholesaler is often also the importer of a product and, given this position, can also issue the EPC at the product level.

#### Employee

Employees of the various entities in the supply chain.

#### Retailer

Sells the product to the consumer and arranges customer service.

#### Consumer

Buyer and/or user of the product. Receives the product from the retailer in return for payment; the product may include a transponder.

#### Disposer

At the end of their life cycle, the transponder and products fitted with transponders are sent to the disposer. This entity is responsible for making correct use of the waste products.

#### System manager

GS1 is the system manager and establishes the rules for the use of the system (such as those governing the issuing of EPCs), and also binds the entities involved in the system to abide by those roles. To this end he draws on the functional entities of security manager and registrar.

#### Registrar

As the registrar, GS1 manages and allocates numerical contingents so as to ensure that the identification system is clear and non-duplicating.

#### Security manager

GS1 is the security manager and provides security functions as well as security rules. System participants are responsible for monitoring those rules and applying them properly.

# <span id="page-41-1"></span><span id="page-41-0"></span>**4 General requirements**

The following two sections deal with particular aspects of special relevance to security when using transponders for specific products.

# **4.1 Functional requirements**

### **4.1.1 Product-specific use of transponders at the POS**

If products at the POS are tagged with transponders, and also if special after-sales services are offered, then facilities should be put in place that allow the transponders to be deactivated or removed after the product is sold, should the consumer so wish.

Technical deactivation of the transponder is only necessary if it is not attached to a removable label or to the packaging, both of which are removed before use.

One method of technical deactivation is the use of what is known as a "kill command". The kill command is a non-reversible procedure which disables the RFID chip from further communication with a reader. Once completed, the transponder can no longer be read by a reader and the product can no longer be identified by it. Consequently, after-sales services (such as paperless returns and guarantee services) are no longer available either.

The kill command should only be used if the end-customer or retailer wishes to deactivate the transponder. In certain cases the kill command can also be used earlier on, if the transponder is no longer needed in the subsequent supply chain or if there is no guarantee that the command can be executed during the sale.

Damage can be caused if the kill command is initiated by unauthorised persons in the supply chain or at the POS. Executing it too early can prevent subsequent processes from taking place, such as inventories, self-service checkouts and theft prevention. A further complicating factor is that the relatively long range of the RFID technology means that a large number of labels can be destroyed very quickly.

#### **4.1.2 Preventing product counterfeiting**

Product piracy is a widespread, growing and complex problem. An obvious example is that of counterfeit handbags on a street market. But there are also licensed production sites which produce and sell more "original products" than allowed, in what are known as "ghost shifts". Products manufactured in that way can be re-routed through the supply chain if, for instance, country-specific prices apply.

Verification of authenticity aims to ensure that the right products are supplied in the right quantities via the right supply chains, to the right retailers. These checks can be performed automatically in the supply chain if the products are scanned along the way. Controllers can also perform random sampling using mobile readers. Alternatively, the end-consumers themselves can verify the authenticity of a product using suitable scanning devices.

To the owner of a brand name it is worth ensuring:

- that only original/authorised products are sold, and
- that the products produced for a particular market are actually sold there.

<span id="page-42-0"></span>To the end-customer it is worth ensuring:

- that a product sold as genuine really is genuine,
- that a product is approved in the country in which it is sold,
- that things like the sell-by date have not been manipulated,
- that a product purchased as "new" really is new.

# **4.2 Economy**

For the system to be operated economically, the commercial benefit must be greater than the cost of the processes, systems and security, regardless of how extensively the system is installed. This must apply to all of the actors who invest in the setting-up of the system.

The system as a whole, and its components, should therefore be designed such that the requirements of the relevant application scenarios are met as efficiently as possible. For this reason it is necessary to begin by defining these requirements as accurately as possible.

# **4.3 Security**

This document will deal with the requirements of security separately, from section [8](#page-71-1) onwards.

# <span id="page-43-0"></span>**5 Method of determining security requirements**

# **5.1 Objectives**

The RFID Technical Guidelines should fulfil the following objectives

- Provide system suppliers and system users with an introductory guide on the correct implementation of specific RFID system solutions, in terms of safety, information security and privacy.
- Raise awareness of and achieve transparency in aspects of security.
- Provide a basis for the system supplier's or operator's declaration of conformity, and for the issuing of quality seals by certification authorities.

The following information is required in order to achieve these aims:

- A definition of the security requirements that must be fulfilled by an RFID system for a given application area.
- A description of the specific risks, appropriate counter-measures, and potential remaining risks.
- A definition of the criteria for a declaration of conformity and for certification.

It is not only security aspects that are relevant to the definition of measures and to proposed systems. All of the requirements described in section [4](#page-41-1) must be taken into account.

# **5.2 Method**

### **5.2.1 Scope of system considerations**

RFID-based systems can be very complex. In most cases, many components not equipped with RFID are part of the system solution. On the other hand it is not sufficient to look only at the media/tags and readers in order to safeguard the system's security.

The Technical Guidelines must cover in detail every aspect of security relevant to RFID. These aspects depend a lot on the application area and the way the system solution is implemented in it. These Technical Guidelines therefore contain detailed descriptions of the application area and the related operational processes (including the sales channels and processes). The processes cover the entire life cycle of an RFID medium or transponder. Based on these processes, use cases are defined which are relevant to discussion of the RFID system's security. These use cases are then used as a foundation for the evaluation of threats and a detailed, system-specific security assessment of the areas of the system associated with RFID. [Figure 5–1](#page-44-1) shows this procedure using the example of eTicketing in public transport.

<span id="page-44-0"></span>![](_page_44_Figure_1.jpeg)

**Figure 5–1 Example: identification of RFID-relevant use cases for eTicketing** 

<span id="page-44-1"></span>All the other system components are considered only in a general manner. The proposed safeguards are based on open standards of IT security.

This concept focuses on those parts of the system that are relevant to RFID, yet still makes sure that all aspects of security are considered. On the other hand the Technical Guidelines leave space for individual and proprietary IT implementations (back-offices, sales systems, logistics systems, etc). This supports in particular the enhancement of existing systems with RFID technology.

# **5.2.2 Scalability and flexibility**

These Technical Guidelines are intended primarily to address security issues. At the same time, any system based on these Guidelines must be economically viable. This means that the following requirements have to be covered by the Guidelines' approach:

- 1 It must be possible to implement systems in a way that achieves a balance between the costs and benefits. This means in practice that the safeguards must fulfil but not exceed the protection demand. Example: if only low-cost products are involved, which require relatively little protection, then precautions should be designed accordingly. This may allow the use of low-cost media, reducing in turn the cost of implementing and operating the system.
- 2 The application scenarios that have been chosen for the Technical Guidelines cover a wide range, from small to nationwide and even international systems. It is important that the concept discussed in the Guidelines can be used for system solutions of any size and complexity.
- 3 In many cases a system solution can be made economically viable much more easily if you are able to cooperate with other companies. This applies in particular to eTicketing applications, where it can be very beneficial if media already available to customers

<span id="page-45-0"></span>(such as multi-application cards and NFC-enabled phones) can be used for additional applications, products and related services.

The following diagrams provide examples of eTicketing for the cross-system and crossapplication utilisation of customer media and infrastructure.

[Figure 5–2](#page-45-1) shows that various products and application scenarios may have to be supported in one system. Furthermore, these products may be hosted by various types of RFID media.

![](_page_45_Figure_4.jpeg)

#### **Figure 5–2 Example of application scenarios and relevant use cases for eTicketing in public transport**

<span id="page-45-1"></span>[Figure 5–3](#page-45-2) gives an example of a customer medium for eTicketing that supports applications from two application areas.

![](_page_45_Figure_8.jpeg)

#### **Figure 5–3 Hierarchical concept for media, applications and tickets in eTicketing**

<span id="page-45-2"></span>The following concept is used in these Technical Guidelines in order to address the aforementioned requirements:

- 1 A feasible role model and the structure of certain key components (products, applications and media) are defined in section 3. This model supports a scalable, extendable approach.
- 2 The Technical Guidelines have to offer security concepts that cover every combination of application scenarios and media used in an infrastructure. This is achieved by individual security assessments based on the relevant use cases.
- <span id="page-46-0"></span>3 Identical application areas (in particular in eTicketing) that provide opportunities for cross-application partnerships will be addressed by the respective Technical Guidelines with as much communality as possible. The security assessments are based on similar security objectives, and the safeguards make use of the same mechanisms wherever possible.
- 4 A special challenge to system security exists in partnerships across systems and applications. It must be ensured that the security of one system is not undermined by the weaknesses of another. Normally this requires extensive security assessments in both systems.

The Technical Guidelines address this problem by introducing a scalable and transparent concept for employing safeguards against identified threats; these are called "protection demand categories". A total of three categories from 1 (normal demand) to 3 (very high demand) are applied. All of the safeguards are divided accordingly into three levels, from normal to advanced protection.

For every individual system implementation, the protection demand category will be defined to begin with, for every security target. These findings will be used to select the appropriate level for the safeguards involved.

This concept provides an easy way to establish secure system cooperation. It remains only to ensure that the protection demand categories of both systems match up.

## **5.2.3 Structure of the Technical Guidelines**

| Chapter                             | Contents                                                                                             |  |
|-------------------------------------|------------------------------------------------------------------------------------------------------|--|
| Description of the application area | Description of the application area: struc<br>ture, services, special peripheral conditions,<br>etc. |  |
| Products and services               | Description of products, services and sales<br>channels                                              |  |
| Definitions                         | Role model, definition of terms                                                                      |  |
| Introduction to the methodology     | Introduction to the concept and methods<br>that are applied to the security considera<br>tions.      |  |
| General requirements                | General requirements of the parties in<br>volved, important points, etc.                             |  |
| Operational processes               | Description of operational processes rele<br>vant to the life-cycle of RFID media                    |  |
| Use cases                           | Definition of RFID-relevant uses cases                                                               |  |
| Security considerations             | Introduction to IT security                                                                          |  |
|                                     | Definition of specific security targets, protec<br>tion demand categories, and threats.              |  |
|                                     | Proposed safeguards                                                                                  |  |
| Definition of application scenarios | Definition of examples for application sce<br>narios. These examples cover the entire                |  |

Table 5-1 shows the structure of all the sections of the Technical Guidelines that have so far been drawn up.

<span id="page-47-0"></span>

| Chapter                                                   | Contents                                                                                                                                                                           |
|-----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                           | range of relevant parameters that may oc<br>cur in this specific application area. Users of<br>the Technical Guidelines may adapt these<br>scenarios according to their own needs. |
| Proposed implementation of the system so<br>lution        | Generic system description including exam<br>ples of how to perform a threat analysis and<br>arrive at feasible safeguards to protect the<br>system components.                    |
| Implementation proposal for each applica<br>tion scenario | Examples of applying the concept to Secu<br>rity considerations in an application-specific<br>way.                                                                                 |

| Table 5–1 | Structure of the Technical Guidelines |
|-----------|---------------------------------------|
|           |                                       |

### **5.2.4 Explanation of the security concept**

The Technical Guidelines contain complete examples of how security considerations should be applied to specific application scenarios. These can be adapted to the requirements and peripheral conditions of the particular system implementation in hand.

[Figure 5–4](#page-48-1) shows the concept for the Security considerations used in all sections of the Technical Guidelines.

<span id="page-48-0"></span>![](_page_48_Figure_1.jpeg)

![](_page_48_Figure_2.jpeg)

<span id="page-48-1"></span>All considerations are based on the conventional definition of security targets defined in [Figure 5–5.](#page-48-2)

![](_page_48_Figure_4.jpeg)

<span id="page-48-2"></span>**Figure 5–5 Generic security targets** 

# <span id="page-49-1"></span><span id="page-49-0"></span>**6 Generic business processes**

# **6.1 Generic description of the supply chain**

![](_page_49_Figure_3.jpeg)

**Figure 6–1 Supply chain** 

# **6.2 Applying for and delivering the EPC Manager**

The EPC Manager is an item of data by which an issuer can be identified uniquely worldwide. This EPC Manager is issued and managed by the application owner; in the EPCglobal system, this is GS1. The issuer – which is the EPC number issuer in the EPCglobal system – applies for his own EPC Manager from his local GS1 organisation, which sends it to him.

The EPC Manager is part of the EPC which the EPC number issuer allocates to the transponders he puts into circulation. The EPC Manager therefore determines the numerical range available to the EPC number issuer.

<span id="page-50-0"></span>![](_page_50_Figure_1.jpeg)

**Figure 6–2 Process P1, "Applying for and delivering the EPC Manager"** 

# **6.3 Individualising the transponder**

The chip integrated into the transponder is configured in the factory to receive an EPC, passwords, and so on, in accordance with the specifications of EPCglobal. This data, however, is not yet in the transponder.

Putting transponder-specific data into the chip is known as individualising. Individualising is performed by the EPC number issuer or his agents.

<span id="page-51-0"></span>![](_page_51_Figure_1.jpeg)

| Figure 6–3 | Process P2, "Individualising the transponder" |  |
|------------|-----------------------------------------------|--|
|            |                                               |  |

# **6.4 Attaching the transponder to an object**

![](_page_51_Figure_4.jpeg)

![](_page_51_Figure_5.jpeg)

**Figure 6–4 Process P3, "Attaching the transponder to an object"** 

Figure 6.4 illustrates the process of attaching a transponder to an object. This object can be a product, an article of packaging, or a pallet.

The transponders are already initialised and carry an EPC, which should correspond with the packaging hierarchy involved. The issuer, or his agents, attaches the transponder to the logistical unit concerned (pallet, packaging or product).

# <span id="page-52-0"></span>**6.5 Receipt of goods**

![](_page_52_Figure_2.jpeg)

#### **Figure 6–5 Process P4, "Receipt of goods"**

In the "receipt of goods" process, the objects tagged with transponders and listed in the electronically transmitted despatch advice, are delivered. These objects can be grouped together at a product, packaging or pallet level. The data is gathered using an RFID reading system, which enables large amounts of data to be collected quickly.

This process is monitored by comparing the data collected by RFID with the electronic despatch advice. Should a discrepancy exist between the scanned products and the despatch advice, then corrective measures are set in motion. The actors involved in this procedure include the product manufacturer, wholesaler, retailer, and logistics service provider.

# **6.6 Warehousing**

In warehousing, the use of RFID enables stocks to be registered in real time, which enables real-time monitoring. The data gathered by RFID readers is treated as an "actual" value. The "target" value is calculated as the difference between goods received and goods despatched. This basically eliminates differences between the actual and target figures.

The use of RFID reading systems in this area enables the inventory to be taken electronically instead of physically. The actors involved in the warehousing process include the product manufacturer, wholesaler, retailer, and logistics service provider.

<span id="page-53-0"></span>![](_page_53_Figure_1.jpeg)

**Figure 6–6 Process P5, "Warehousing"** 

# **6.7 Shipment preparation**

The process of preparing shipment takes place after the logistical process of receiving goods and before that of despatching goods. [Figure 6–7](#page-54-1) defines shipment preparation as part of the goods despatch process.

In the shipment preparation process, certain products are retrieved from the warehouse for the subsequent actors in the supply chain in accordance with a shipment preparation list. A shipment prepared for a downstream entity in the supply chain can consist of a combination of complete pallets, boxes and individual products. It is normally placed in a separate area ready for transport (HGV, containers, and so on).

The actors that can be involved in the shipment preparation process are the product manufacturer, wholesaler, retailer, and logistics service provider.

<span id="page-54-0"></span>![](_page_54_Figure_1.jpeg)

**Figure 6–7 Process P6, "Shipment preparation"** 

# <span id="page-54-1"></span>**6.8 Despatch of goods**

In the goods despatch process, objects are gathered together in accordance with the shipment preparation list for the next actor in the supply chain; this list may originate from a retailer or from a wholesaler. The objects can be products, packages, or even whole pallets. Scanning data by RFID enables mistakes to be detected quickly. If the data gathered does not correspond with the shipment preparation list, corrections can be made before despatch.

The actors that can be involved in the goods despatch process are the product manufacturer, wholesaler and logistics service provider.

<span id="page-55-0"></span>![](_page_55_Figure_1.jpeg)

**Figure 6–8 Process P7, "Goods despatch"** 

# **6.9 Cross-docking**

In terms of its process, cross-docking involves the same stages as the shipment preparation process described in [Figure 6–7](#page-54-1). We differentiate between single and dual (multiple) stage cross-docking.

In single-stage cross-docking the supplier prepares the goods in logistical units relating to the end-recipient (retailer or consumer). These logistical units are transported unchanged via one or more cross-docking points to the end-recipient.

In dual-stage cross-docking the supplier prepares the goods in logistical units relating to a cross-docking point. These logistical units are then transported unchanged only to the next cross-docking point, where a further preparation takes place to form new logistical units which relate to the end-recipient (retailer or consumer). Additional preparation stages are also possible at additional cross-docking points (multi-stage cross-docking)

# **6.10 Use at stationery retailers (no mail order)**

The use of RFID at product level (item level tagging – ILT) opens up a series of new possibilities for retailers and consumers.

Benefits for the retailer:

1 Real-time stock-taking. An intelligent RFID infrastructure can inform a retailer about his stock levels and product availabilities at any time. If the quantity of a particular product decreases, then the database-based system in the background can automatically order the necessary amounts.

- <span id="page-56-0"></span>2 Guaranteed freshness. In the case of perishable goods, it is possible to store the sell-by date in the transponder memory in addition to the EPC number. This, combined with a database system, can help ensure the goods are sold within the proper time.
- 3 Theft protection. An EAS solution integrated into the transponder, combined with an RFID reading system at the exit, can trigger an alarm in the case of goods that have not been paid for.

Benefits for the consumer:

- 1 Product information: if a consumer is interested in a product, then more information can quickly be provided about its use, any accessories, and the availability of similar models (different colours, sizes).
- 2 Guarantee (handling customer returns): if the customer wishes, the RFID transponder can be left on the product after purchase and not destroyed. Additional information such as the date of purchase can be programmed into the IC, thus enabling the customer to return the goods without a receipt as guarantee.

![](_page_56_Figure_6.jpeg)

**Figure 6–9 Process P8, "Stock management"** 

<span id="page-56-1"></span>[Figure 6–9](#page-56-1) shows an example of a stock management process. Stocks are monitored regularly by RFID reading systems. This can be done by systems installed permanently in the sales areas, or by the store personnel using manual readers. The retailer's computer infrastructure then checks the actual stock against the expected stock using the amount of goods sold so far. In the event of a discrepancy (e.g. shrinkage or wrongly registered goods), corrective measures can be put in motion. Re-orders can also be activated as part of a smartshelf concept, if the quantity of a particular product in the sales area falls below a defined threshold.

# **6.11 Sales process**

The products on the consumer's shopping list are placed into a suitable means of transport and registered by an RFID reading system at the checkout, either individually or in bulk (automatic recording of all the products in the trolley)

The transponder may be deactivated after the goods have been paid for.

<span id="page-57-0"></span>Payment is made using the usual methods (cash or cash-free). The principle actors in the process of sale are the consumer and the retailer.

|                                           | P9.1<br>Sales                                                                                          | Actors   |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------|----------|
| Register goods                            | Item-by-item registering using RFID<br>Bulk registering using RFID reading<br>reading system<br>system | Retailer |
|                                           |                                                                                                        |          |
| Pay value of goods                        | Payment by customer                                                                                    | Consumer |
|                                           |                                                                                                        |          |
| Optional de-individualisation of<br>goods | Deactivate RFID tag                                                                                    | Retailer |
|                                           |                                                                                                        |          |
|                                           | End                                                                                                    |          |

**Figure 6–10 Process P9, "Sales"** 

# **6.12 After-sales services**

After-sales services include the following areas:

- 1 Intelligent household appliances can, for example, selectively activate, deactivate and optimise their functions on the basis of product information (the temperature at which clothes are washed, for instance).
- 2 Guarantee and warranty

Additional information such as the date of purchase can be programmed into the transponder, thus enabling the customer to return the goods without a receipt as guarantee.

3 Maintenance

Information about maintenance contracts associated with the products can also be stored in the product's data memory, enabling anonymous servicing of the product.

<span id="page-58-0"></span>![](_page_58_Figure_1.jpeg)

**Figure 6–11 Processes P10.1 "Guarantee" and P10.2 "Maintenance"** 

<span id="page-58-1"></span>An example of the maintenance and guarantee business process is depicted in [Figure 6–11.](#page-58-1) Following the payment procedure, the transponder is programmed with guarantee and maintenance information. This enables to consumer to return the goods at a later date and claim guarantee or maintenance services. If a guarantee claim is made, then the information in the transponder has to be changed accordingly. This, of course, is only possible if the transponder was not deactivated after payment.

# <span id="page-59-0"></span>**6.13 Disposal**

![](_page_59_Figure_2.jpeg)

#### **Figure 6–12 Process P11, "Disposal"**

<span id="page-59-1"></span>RFID transponder technology enables an anonymous product disposal process. This process allows consumers to return the product, receive an optional return bonus, and for the product to be fed into environmentally acceptable disposal processes afterwards.

An example of this business process is depicted in [Figure 6–12](#page-59-1). Firstly the EPC in the transponder is read and the product's authenticity verified. The returns information is then retrieved either from the EPC database or from the transponder's data memory. The returns process can then be initiated, and a bonus paid where applicable.

# <span id="page-60-1"></span><span id="page-60-0"></span>**7 Use cases**

# **7.1 Manufacture and delivery of the chips**

The use case "manufacture and delivery of the chips" describes the procedure of configuring the chip and sending the chip products and object-related data to the transponder manufacturer.

The following process stages are especially important for the subsequent security assessment:

- 1 Generating, issuing, programming, and the permanent blocking of a unique ID (TID, UID) on the chip.
- 2 Transmission of the wafer data (wafermap) needed for assembly to the transponder manufacturer.

![](_page_60_Figure_7.jpeg)

**Figure 7–1 Use Case "Manufacture and delivery of the chip"** 

# <span id="page-61-0"></span>**7.2 Manufacture and delivery of the transponder**

The use case "manufacture and delivery of the transponder" incorporates the following stages:

- 1 Manufacturing the inlay
- 2 Manufacturing the transponder

It can also include the transponder manufacturer individualising the transponder and setting the kill command. The transponder manufacturer then acts as the issuer, or on behalf of the issuer. This case is described in sections [7.4](#page-63-1) and [7.5](#page-65-1).

Manufacturing the inlay basically means assembling the chip together with an antenna suited to the application on a suitable carrier substrate.

Manufacturing the transponder includes fitting the inlay into a suitable physical transponder setting, which, depending on the specific end-application, can mean paper or plastic packaging, or incorporation in the form of an adhesive label (wet inlay).

![](_page_61_Figure_8.jpeg)

## **7.2.1 Manufacturing the inlay**

**Figure 7–2 Use Case "Manufacturing the inlay"** 

Manufacturing the inlay begins by choosing the type of inlay suited to the application. Different applications (such as a packaging box or clothing label) require different antenna configu<span id="page-62-0"></span>rations in order to achieve the best possible reading rates. The basis material for an inlay is usually a plastic (e.g. PET) onto which the antenna is applied either by etching a copper layer, printing with silver ink, or stamping (aluminium or copper). This basis material is usually supplied in roles. When the inlay is being manufactured, the chip is applied to the antenna contacts. Alternatively, the chip can be supplied on a carrier substrate together with copper contacts (strap format). The strap with the contacts is then stuck to the antenna in a roll-to-roll process, or mechanically connected (crimping). Once assembled, the inlay is tested, during which an RFID reader is used to verify the transponder's response. Dysfunctional inlays are marked so that they can be separated out in subsequent steps. During this stage of processing, the transponders are usually loaded with a temporary test EPC in order to enable testing. The finished inlays are supplied to the transponder manufacturer in roll form. Because of the different process conditions, inlay production (requires clean-room conditions) and transponder production are usually done in different production facilities.

## <span id="page-62-1"></span>**7.2.2 Manufacturing the transponder**

![](_page_62_Figure_3.jpeg)

**Figure 7–3 Use Case "Manufacturing the transponder"** 

Once the inlays have been manufactured, they are made into the finished physical format by the transponder manufacturer. Common formats include non-adhesive paper labels (dry labels; e.g. for clothing), plastic labels, and adhesive labels (especially for boxes and individual products). This processing is done using a roll-to-roll method. The transponders may be loaded with a temporary test EPC in order to facilitate subsequent functional testing.

# <span id="page-63-0"></span>**7.3 Producing and issuing the EPC Manager**

The issuer applies for an EPC Manager from GS1/EPCglobal. Once EPCglobal has identified the applicant and checked the application, it issues a unique EPC Manager for the issuer.

The issuer receives an EPC Manager from GS1/EPCglobal, enabling him to generate the EPCs which he requires. He issues an EPC from the numerical range allocated to him, to every object tagged with RFID (pallets, boxes, items). The issuer communicates these EPCs and any information relating to them to his business associates in the value-added chain, wherever relevant.

# <span id="page-63-1"></span>**7.4 Individualising the transponder**

The "load EPC" use case describes the individualisation of the transponder using a unique EPC. Individualising can be performed by various entities in the system. The variation used by the transponder manufacturer is described in section [7.2.2](#page-62-1). Normally speaking, a transponder is individualised when it is attached to the product or a package. The issuer is responsible for doing this. However, it may be that a transponder manufacturer or packing manufacturer acts on behalf of the issuer.

[Figure 7–4](#page-64-1) shows the use case of loading an EPC into a transponder. Loading an EPC is obligatory under EPCglobal regulations.

Once the UID has been read (optional) the EPC is allocated from the issuer's database for the products involved. The EPC is then programmed into the relevant area of the transponder's memory.

<span id="page-64-0"></span>![](_page_64_Figure_1.jpeg)

**Figure 7–4 Use Case "Individualising the transponder"** 

<span id="page-64-1"></span>In the following, optional steps, the kill password is set (see section [7.5](#page-65-1)), and any other data required is written to the programmable memory area of the transponder.

There are many application scenarios which can benefit greatly by using the free memory area in the EPC chip for storing product-specific information and additional safeguards. There are many ideas on how to go about this, although these Guidelines will not discuss them in detail at the moment because EPCglobal has not incorporated them into their standard, and existing solutions are therefore to be considered proprietary.

# <span id="page-65-1"></span><span id="page-65-0"></span>**7.5 Setting the kill password**

![](_page_65_Figure_2.jpeg)

**Figure 7–5 Use case "Setting the kill password"** 

EPCglobal-compliant transponders are equipped with a kill command in order to enable them to be deactivated once the product has been purchased. The triggering of the kill command is normally protected using a 32-bit password in order to prevent unauthorised persons from activating the command and deactivating the transponder. This kill password is stored in the transponder's chip. According to ISO18000-6, activation of the kill command assumes that the kill password has been set to a value other than 0.

The kill password is stored in the EPC chip's "reserved memory". The "reserved memory" can be irreversibly protected against reading and overwriting.

The use cases covering the generation, storage and transmission of passwords and keys are described in section [7.10.](#page-69-1)

# <span id="page-66-0"></span>**7.6 Attaching the transponder to the product**

There are basically three different ways of applying a transponder to a product: either directly to the outside of the product (e.g. in the form of an adhesive label), inside the packaging, or by integrating it physically into the product.

If the transponder is applied directly to the product, it is firstly individualised. It is then separated out (e.g. cut from a roll), and dysfunctional transponders, which have been marked during individualisation, are sorted out from the rest. The transponders are then applied physically to the product either by sticking (wet inlay), sewing (in a piece of clothing, for example), or shooting (e.g. labels in clothing). The transponder can be applied to the product at the product manufacturer, the manufacturer of the packaging, or at a later stage in the supply chain.

Alternatively, it may be useful to integrate the transponder physically into the product (e.g. by embedding it into an electronic appliance's PCB, or sewing it into a piece of clothing). It must, however, be remembered that mistakes made during integration, and faulty transponders, can lead to higher levels of rejects when producing the product. The "individualising the transponder" and "setting the kill password" use cases are then performed on the integrated transponder – i.e., the product.

# **7.7 Reading the data stored in the transponder**

This use case describes the way the EPC stored in the transponder is read, and the way the logistical data linked to this is processed in accordance with EPCIS.

<span id="page-67-0"></span>![](_page_67_Figure_0.jpeg)

![](_page_67_Figure_2.jpeg)

**Figure 7–6 Use case "Reading the EPC data stored in transponder"** 

<span id="page-67-1"></span>[Figure 7–6](#page-67-1) shows an example of how the information stored in the transponder is read. All communication, such as reading the EPC, is performed in compliance with the EPCglobal Class 1 Generation 2 specification.

Additional data can also be stored in the EPC chip's additional storage area. The principle of reading described for the EPC also applies to the reading of data stored in the additional storage area of the EPC chip. An access password may be required to obtain access. Other than that there are no regulations governing the extent and the form in which this data can be made accessible to the system as a whole.

# <span id="page-68-0"></span>**7.8 Activating the kill command**

The transponder is normally deactivated in a special place (such as the point of sale) at the request of the consumer, once payment has been made. Deactivation is done using a reader as shown in [Figure 7–7.](#page-68-1)

Once the kill password has been generated, the reader sends a command to establish communication. The tag sends a corresponding communication code (handle) back, by which subsequent communication takes place. The reader then sends the kill command together with the password to the transponder. After this the transponder becomes inactive and no longer responds to commands from a reader.

![](_page_68_Figure_4.jpeg)

**Figure 7–7 Use case "Activating the kill command"** 

<span id="page-68-1"></span>In practice, key management processes may be used in order, for example, to diversify keys. In this case, processes for deriving the specific keys from the key management system and the readers would have to be depicted.

# **7.9 Authenticating the transponder for verifying genuineness**

The authentication of the transponder is one of the main processes used to prevent the counterfeiting of products and for identifying products that have ended up in the wrong channels (not for the correct market). By issuing a UID during the chip manufacture, which is globally unique and cannot be overwritten, this code can be compared with a suitable database to determine the authenticity of the transponder at the point of sale. The UID can be relied upon in addition to the EPC for its unambiguity.

<span id="page-69-0"></span>[Figure 7–8](#page-69-2) depicts an example of a use case for assessing authenticity. The assessment is based on comparing the EPC retrieved from the transponder with logistical data available in a background system. The transponder is considered authentic if the EPC is contained in the background system for the correct issuer and target product. Another step involves checking whether the logistical data stored in the background system for that EPC is plausible.

![](_page_69_Figure_2.jpeg)

**Figure 7–8 Use case "Example of authenticity check using EPC transponder"** 

<span id="page-69-2"></span>If this assessment reveals any doubt about the authenticity of the EPC, then the process can be repeated using, for example, the UID.

# <span id="page-69-1"></span>**7.10 Key management**

In accordance with the latest EPCglobal specifications, passwords are used to protect the kill command and the additional data storage area. The security and functionality of the system as a whole is therefore to a large degree dependent on the secure provision and storage of these keys. This is a task which must be performed by the key management system and the processes related to it.

In the following use cases, **Secure Authentication Modules** (**SAMs**) are used as secure storage for key information, security mechanisms and diversification algorithms. In principle, other methods may also be feasible.

[Figure 7–9](#page-70-1) shows an example of a use case for the key management used in individualising transponders.

<span id="page-70-0"></span>![](_page_70_Figure_1.jpeg)

<span id="page-70-1"></span>**Figure 7–9 Use case "Key management"** 

# <span id="page-71-1"></span><span id="page-71-0"></span>**8 Security considerations**

# **8.1 Definitions relating to security and privacy**

Security can be divided into three aspects or categories, all of which this document intends to examine. They are:

- Safety
- Information security
- Privacy

These categories can be subdivided as follows:

1 Safety

Safety is not to be confused with reliability/correctness or quality of service. Reliability means that the system works correctly according to its specifications. Experience shows that every technical system is sometimes subject to failure. Safety is understood as the capacity of a system, when it does fail, not to enter uncontrollable states that would endanger the system itself or its environment (fail-safe). At the same time, the system should also continue to respond as far as possible in compliance with its specification (fault tolerance). Safety, therefore, basically implies protection against unintended incidents.

2 Information security

Unlike safety, information security offers protection against intentional attacks. In the field of information security, security targets can be formulated as belonging to the following categories:

- a Confidentiality: confidentiality means protection against the unauthorised disclosure of information. Confidential data and information may only be accessible to authorised people in an authorised manner. Formulated as a protection target this means: stored information and information that is to be communicated is to be protected against access by unauthorised persons.
- b Integrity: integrity means ensuring that data is correct (intact) and that systems function properly. Formulated as a protection target this means: stored information and information that is to be communicated is to be protected against unauthorised modification.
- c Availability: the availability of services, of the functions of an IT system, IT applications and IT networks – and also of information – exists if these things are always available to their users when required. Formulated as a protection target this means: information and operating systems are to be protected against being withheld improperly.
- d Unlinkability: if two communication elements within a system are unlinkable, it means they are not any more or less related to one another than is already known and established. Within the system, no further information about the relationship between these communication elements can be obtained. In practical terms this means that a single user can make use of services and resources more than one time, without third parties being able to see that these access events (in the communication model: messages) are related through the user.
- e Unobservability: an event is unobservable if it cannot be determined whether it has happened or not. Sender unobservability means that anything that has been sent cannot be seen; recipient unobservability is the same: it is not possible to ascertain

that something has been received. Relationship unobservability means that anything sent from the group of possible senders to the group of possible recipients cannot be seen.

- f Anonymity: anonymity is the condition of being unidentifiable within one's anonymity group. Using the term unlinkability, anonymity can be more precisely defined as the unlinkability of the identity of a user and an event initiated by that user. Sender anonymity is therefore unlinkability of sender and message, and recipient anonymity is the unlinkability of message and recipient.
- g Authenticity: the term authenticity designates a situation in which the partner in a communication process is actually the person he claims to be. Authentic information is information that genuinely comes from the stated source. The term is not only used when people's identity is being checked, but also for IT components and applications.
- h Non-repudiation: protection should exist against the possibility of denying that messages have been sent and received by persons whose authenticity has been determined.
- i Binding validity: binding validity joins together the IT security targets of authenticity and non-repudiation. When transmitting information this means that the source of the information has proven its identity, and that the receipt of the message cannot be disputed.
- 3 Privacy

The purpose of privacy is to protect against infringements of the personal rights of the individual through the handling of his personal data.

Privacy refers to the protection of personal data against possible misuse by third parties (not to be confused with data security).

The following additional terms will also be used throughout:

4 Security targets

Security targets are the security-related and safety-related objectives undertaken when setting up an IT system. This document lays down specific security targets within the areas of use and application scenarios. Infringing upon the security targets causes direct damage to the entity whose security target is violated.

5 Threats

Threats are immediate risks to the security targets of an application.

These may be the result of an active attack on one or more security targets, or they may take the form of potential vulnerabilities in the system such as the lack of a fallback solution.

6 Safeguards

Safeguards are actual recommended actions that counter one or more threats. The safeguards described in this document are intended to be applied meaningfully and according to need, which means they are suggested on the basis of economic feasibility and resistance to manipulation: how expensive is a safeguard, and what are the financial damages that it can limit or prevent?

7 Residual risk

Generally speaking it is not possible to counteract every single threat in such a way that a system offers perfect security. The residual risk is thus the risk of potential attack that remains after a series of safeguards have been put in place. The extent of this risk depends on the countermeasures that can be applied, how complex they are, and, above all, what the costs are in relation to the benefits for the entity involved. The entity has to take explicit liability for the residual risk.

# <span id="page-73-1"></span><span id="page-73-0"></span>**8.2 Definition of the security targets**

It would be very unusual for all of the safety aspects relating to safety, information security and privacy within a given application scenario to be of equal importance, or indeed for every single one of them to be relevant at all. The first challenge when designing a secure RFID system is therefore to formulate specific security targets.

Within the areas of use relating to trade logistics, certain *higher level* security targets specific to the application area can be recognised, based on the generic security targets mentioned earlier:

- 1 Protection of electronic object recognition (EPC) (represents the protection targets integrity and authenticity)
- 2 Safety of the RFID system
- 3 Protection of the customer's privacy (represents the protection targets confidentiality, unlinkability, unobservability, anonymity, and privacy as a general requirement)

The lower level security targets listed in section [0](#page-78-1) can be derived from the assessments of the entities' security targets contained in the following sections.

| field num<br>ber | 1                   | 2                                       | 3                                                             | 4                |
|------------------|---------------------|-----------------------------------------|---------------------------------------------------------------|------------------|
| field            | security tar<br>get | associated role and<br>its abbreviation | associated generic<br>security target and its<br>abbreviation | index num<br>ber |
|                  |                     | C := customer                           | S := safety                                                   |                  |
| content          | S                   | R := retailer                           | I := information secu<br>rity                                 | 1,  , n          |
|                  |                     | I := issuer                             | P := privacy                                                  |                  |

The following table shows the scheme of security target codes and used abbreviations.

**Table 8–1 Coding scheme of security targets** 

#### **8.2.1 Specific security targets for the customer**

The customer's specific security targets are listed in the following sections.

#### **8.2.1.1 Safety**

| Security target code<br>and name |                                                          | Description of security target                                                                                                                                                  |
|----------------------------------|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SCS1                             | Fallback solu<br>tion in the<br>event of mal<br>function | Authorised persons must be able to use the service (e.g. check<br>out, guarantee proof, deactivation) even when the transponder<br>or infrastructure are not working perfectly. |

<span id="page-74-0"></span>

| and name | Security target code                       | Description of security target                                                                                                                                                                                                                                                                             |  |
|----------|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| SCS2     | Intuitive, fault<br>tolerant opera<br>tion | 1<br>The kill function must be self-explanatory where possible,<br>and/or easy to learn.<br>2<br>The self-checkout must be self-explanatory where possible,<br>and/or easy to learn.<br>3<br>The customer should be informed after deactivation that the<br>transponder has been deactivated successfully. |  |

#### **Table 8–2 Customer specific security targets for safety**

#### **8.2.1.2 Information security**

| Security target code<br>and name |                                                                      | Description of security target                                                                                                                                                                                                                                                                                                                                                                                                                            |
|----------------------------------|----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SCI1                             | Protection of<br>personal data<br>in the cus<br>tomer data<br>system | Personal data is not stored on transponders allocated to objects.<br>The retailer's customer data system may store customer data<br>used to process special methods of payment (e.g. invoice), to<br>deliver products, and so on. This data needs to be protected<br>against unauthorised use and against access by unauthorised<br>persons. Misuse, manipulation and the passing on of data to un<br>authorised persons could carry risks for customers. |
| SCI2                             | Protection of<br>object code                                         | Object codes must be protected against DoS attacks and ma<br>nipulation by unauthorised persons.                                                                                                                                                                                                                                                                                                                                                          |

| Table 8–3 | Customer specific security targets for information security |
|-----------|-------------------------------------------------------------|
|           |                                                             |

#### **8.2.1.3 Protection of privacy**

| Security target code<br>and name |                                                                   | Description of security target                                                                                                    |
|----------------------------------|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| SCP1                             | Protection of<br>personal data                                    | Personal data submitted to the retailer must be treated by the<br>retailer as confidential and only used for the agreed purposes. |
| SCP2                             | Protection<br>against the<br>creation of<br>movement pro<br>files | Third parties must be prevented from utilising RFID technology<br>to generate personal movement profiles.                         |

**Table 8–4 Customer specific security targets for protection of privacy** 

#### **8.2.2 Specific security targets for the retailer**

The retailer's specific security targets are listed in the following sections.

| Security target code<br>and name |                                                          | Description of security target                                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SRS1                             | Technical<br>compatibility                               | The interaction between transponders and readers must function<br>as specified. This must apply to all of the approved transponders<br>at all readers in the entire system infrastructure. It must take into<br>account the fact that transponders and infrastructure may be<br>supplied by different manufacturers and run by different entities<br>in the supply chain worldwide. |
|                                  |                                                          | If read-errors cannot be avoided, they must be compensated for<br>using suitable measures.                                                                                                                                                                                                                                                                                          |
| SRS2                             | Fallback solu<br>tion in the<br>event of mal<br>function | The availability and integrity of logistical data must be guaran<br>teed even if the transponder or parts of the system infrastructure<br>are not working perfectly.                                                                                                                                                                                                                |
| SRS3                             | Intuitive, fault<br>tolerant opera<br>tion               | 1<br>The kill function must be self-explanatory where possible,<br>and/or easy to learn.<br>2<br>The self-checkout must be self-explanatory where possible,<br>and/or easy to learn.<br>3<br>The customer should be informed after deactivation that the<br>transponder has been deactivated successfully.                                                                          |

#### <span id="page-75-0"></span>**8.2.2.1 Safety**

| Table 8–5 | Retailer specific security targets for safety |
|-----------|-----------------------------------------------|
|-----------|-----------------------------------------------|

#### **8.2.2.2 Information security**

| Security target code<br>and name |                                                                      | Description of security target                                                                                                                                                                                                                                                                                                               |
|----------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SRI1                             | Protection of<br>personal data<br>in the cus<br>tomer data<br>system | Personal data is not stored on transponders allocated to objects.<br>The retailer's customer data system may store customer data<br>used to process special methods of payment (e.g. invoice), to<br>deliver products, and so on. This data needs to be protected<br>against unauthorised use and against access by unauthorised<br>persons. |
| SRI2                             | Protection of<br>object code                                         | Manipulation and, in particular, falsification of object codes could<br>cause considerable commercial damage to the retailer, the is<br>suer and other entities in the supply chain.<br>Security against counterfeiting object codes is an important ob<br>jective for the retailer.                                                         |
| SRI3                             | Protecting the<br>allocation of<br>object and ob<br>ject code        | The removal of the correct allocation of object codes to objects<br>could cause considerable commercial damage to the retailer, the<br>issuer and other entities in the supply chain.<br>Correct allocation of object and object codes is an important ob<br>jective for the retailer.                                                       |
| SRI4                             | Protection of                                                        | The availability and integrity of logistical data is very important to<br>the retailer and issuer. It is used for monitoring the supply chain,                                                                                                                                                                                               |

<span id="page-76-0"></span>

| Security target code<br>and name |                                                                          | Description of security target                                                                                                                                                                                                                                                                    |
|----------------------------------|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                  | logistical data                                                          | invoicing, and planning capacities.                                                                                                                                                                                                                                                               |
| SRI5                             | Protection<br>against DoS<br>attacks on the<br>RFID system<br>components | RFID system components must be protected against DoS at<br>tacks. Typical DoS attacks include.<br>•<br>Kill command<br>•<br>Jamming transmitters<br>•<br>Blocker tags<br>•<br>EMP<br>•<br>Mechanical destruction<br>•<br>Impairing the function of readers                                        |
| SRI6                             | Protection<br>against spying<br>on goods flow<br>information             | Retailers and issuers rely on the confidentiality of goods flow<br>information. Unauthorised persons must not be given access.                                                                                                                                                                    |
| SRI7                             | Availability of<br>EPC data                                              | The availability of the data must be assured. The following are<br>some of the requirements that must be met:<br>•<br>Sufficient reading rates<br>•<br>Sufficient transponder reliability and durability. This applies<br>especially if the transponder is to be used for post-sales<br>services. |

**Table 8–6 Retailer specific security targets for information security** 

#### **8.2.2.3 Protection of privacy**

| Security target code<br>and name |                                | Description of security target                                                                                                    |
|----------------------------------|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| SRP1                             | Protection of<br>personal data | Personal data submitted to the retailer must be treated by the<br>retailer as confidential and only used for the agreed purposes. |
| SRP2                             | Data minimisa<br>tion          | Only the data required for the specified purpose should be gath<br>ered and stored, no more.                                      |

**Table 8–7 Retailer specific security targets for protection of privacy** 

#### **8.2.3 Specific security targets for the issuer**

The issuer's specific security targets are listed in the following sections.

#### **8.2.3.1 Safety**

| Security target code<br>and name |                            | Description of security target                                                                                                      |
|----------------------------------|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| SIS1                             | Technical<br>compatibility | The interaction between transponders and readers must function<br>as specified. This must apply to all of the approved transponders |

<span id="page-77-0"></span>

| Security target code<br>and name |                                                          | Description of security target                                                                                                                                                                                                                                                                                                             |
|----------------------------------|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                  |                                                          | at all readers in the entire system infrastructure. It must take into<br>account the fact that transponders and infrastructure may be<br>supplied by different manufacturers and run by different entities<br>in the supply chain worldwide.<br>If read-errors cannot be avoided, they must be compensated for<br>using suitable measures. |
| SIS2                             | Fallback solu<br>tion in the<br>event of mal<br>function | The availability and integrity of logistical data must be guaran<br>teed even if the transponder or parts of the system infrastructure<br>are not working perfectly.                                                                                                                                                                       |

| Table 8–8 | Issuer specific security targets for safety |
|-----------|---------------------------------------------|
|           |                                             |

#### **8.2.3.2 Information security**

| Security target code<br>and name |                                                                          | Description of security target                                                                                                                                                                                                                                                       |
|----------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SII1                             | Protection of<br>personal data<br>in the cus<br>tomer data<br>system     | Personal data is not stored on the transponders.<br>This security target is only relevant in cases where the issuer<br>and retailer are one and the same. The objectives are then the<br>same as SRI1.                                                                               |
| SII2                             | Protection of<br>object code                                             | Manipulation and, in particular, falsification of object codes could<br>cause considerable commercial damage to the retailer, the is<br>suer and other entities in the supply chain.<br>Security against counterfeiting object codes is an important ob<br>jective for the issuer.   |
| SII3                             | Protecting the<br>allocation of<br>object and ob<br>ject code            | The removal of the correct allocation of object codes to objects<br>could cause considerable commercial damage to the retailer, the<br>issuer and other entities in the supply chain.<br>Correct allocation of object and object codes is an important ob<br>jective for the issuer. |
| SII4                             | Protection of<br>logistical data                                         | The availability and integrity of logistical data is very important to<br>the retailer and issuer. It is used for monitoring the supply chain,<br>invoicing, and planning capacities.                                                                                                |
| SII5                             | Protection<br>against DoS<br>attacks on the<br>RFID system<br>components | RFID system components must be protected against DoS at<br>tacks. Typical DoS attacks include:<br>•<br>Kill command<br>•<br>Jamming transmitters<br>•<br>Blocker tags<br>•<br>EMP<br>•<br>Mechanical destruction<br>•<br>Impairing the function of readers                           |

<span id="page-78-0"></span>

| Security target code<br>and name |                                                              | Description of security target                                                                                                                                                                                                                                                                    |  |
|----------------------------------|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| SII6                             | Protection<br>against spying<br>on goods flow<br>information | Retailers and issuers rely on the confidentiality of product and<br>goods flow information. Unauthorised persons must not be given<br>access.                                                                                                                                                     |  |
| SII7                             | Availability of<br>EPC data                                  | The availability of the data must be assured. The following are<br>some of the requirements that must be met:<br>•<br>Sufficient reading rates<br>•<br>Sufficient transponder reliability and durability. This applies<br>especially if the transponder is to be used for post-sales<br>services. |  |

#### **8.2.3.3 Protection of privacy**

| Security target code<br>and name |                                | Description of security target                                                                                                                       |
|----------------------------------|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| SIP1                             | Protection of<br>personal data | Personal data submitted to the retailer by the consumer must be<br>treated by the retailer as confidential and only used for the<br>agreed purposes. |
| SIP2                             | Data minimisa<br>tion          | Only the data required for the specified purpose should be gath<br>ered and stored, no more.                                                         |

**Table 8–10 Service provider specific security targets for protection of privacy** 

#### <span id="page-78-1"></span>**8.2.4 Summary of the entities' security targets**

The following table sums up the aforementioned security targets of the various actors involved.

| Security objective |                                                            | Consumer<br>objective | Retailer ob<br>jective | Issuer ob<br>jective |
|--------------------|------------------------------------------------------------|-----------------------|------------------------|----------------------|
| SS1                | Technical compatibility                                    |                       | SRS1                   | SIS1                 |
| SS2                | Fallback solution in the event of<br>malfunction           | SCS1                  | SRS2                   | SIS2                 |
| SS3                | Intuitive, fault-tolerant operation                        | SCS2                  | SRS3                   |                      |
| SI1                | Protection of personal data in the<br>customer data system | SCI1                  | SRI1                   | SII1                 |
| SI2                | Protection of object code                                  | SCI2                  | SRI2                   | SII2                 |
| SI3                | Protecting the allocation of object<br>and object code     |                       | SRI3                   | SII3                 |
| SI4                | Protection of logistical data                              |                       | SRI4                   | SII4                 |

<span id="page-79-0"></span>

| Security objective |                                                               | Consumer<br>objective | Retailer ob<br>jective | Issuer ob<br>jective |
|--------------------|---------------------------------------------------------------|-----------------------|------------------------|----------------------|
| SI5                | Protection against DoS attacks on<br>the RF system components |                       | SRI5                   | SII5                 |
| SI6                | Protection against spying on goods<br>flow information        |                       | SRI6                   | SII6                 |
| SI7                | Availability of EPC data                                      |                       | SRI7                   | SII7                 |
| SP1                | Protection of personal data                                   | SCI1, SCP1            | SRI1, SRP1             | SRI1, SIP1           |
| SP2                | Data minimisation                                             |                       | SRP2                   | SIP2                 |
| SP3                | Protection against the creation of<br>movement profiles       | SCP2                  |                        |                      |

#### **Table 8–11 Overview of the entities' security targets**

### <span id="page-79-1"></span>**8.2.5 Formation of protection demand categories**

Three protection demand categories are formed on the basis of the security targets described in section [0](#page-78-1). Category 1 represents the lowest protection demand, category 3 the highest.

The following table lists the criteria for allocating protection requirements to protection demand categories, these criteria being based on the assumption that no protective measures have been put in place.

| Security objective |                                                     | Protection<br>demand<br>category | Criteria for allocating to protection demand cate<br>gories                                                                                                    |
|--------------------|-----------------------------------------------------|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SS1                | Technical com<br>patibility                         | 1                                | All system components are from the same sup<br>plier. The supplier ensures that they are compati<br>ble.                                                       |
|                    |                                                     | 2                                | The system has to function with components from<br>a small number of defined suppliers. The system<br>manager or a system integrator ensure compati<br>bility. |
|                    |                                                     | 3                                | Open system that has to function with compo<br>nents from any company in the market.                                                                           |
| SS2                | Fallback solution<br>in the event of<br>malfunction | 1                                | Malfunction affects only a few transponders.                                                                                                                   |
|                    |                                                     | 2                                | Malfunction affects many transponders.                                                                                                                         |
|                    |                                                     | 3                                | Malfunction affects most or all transponders.                                                                                                                  |
| SS3                | Intuitive, fault<br>tolerant opera<br>tion          | 1                                | A few consumers cannot operate it intuitively.                                                                                                                 |
|                    |                                                     | 2                                | Many consumers cannot operate it intuitively.                                                                                                                  |
|                    |                                                     | 3                                | A large proportion of consumers cannot operate it<br>intuitively.                                                                                              |

<span id="page-80-0"></span>

| Security objective |                                                                          | Protection<br>demand<br>category | Criteria for allocating to protection demand cate<br>gories                                                                                                        |
|--------------------|--------------------------------------------------------------------------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SI1                | Protection of<br>personal data in<br>the customer<br>data system         | 1                                | Personal data is not gathered during the sales<br>process.                                                                                                         |
|                    |                                                                          | 2                                | A personal link is set up during the sales process<br>by means of a customer card number, but prod<br>uct-related logistical data is not used.                     |
|                    |                                                                          | 3                                | Personal data relating to special methods of pay<br>ment (e.g. invoice) is used during the sales proc<br>ess.                                                      |
| SI2                | Protection of ob<br>ject code                                            | 1                                | Low risk of product counterfeiting, manipulation,<br>DoS, etc.                                                                                                     |
|                    |                                                                          | 2                                | Product counterfeiting, manipulation, DoS, etc.<br>causes limited damage amounting to < 1% of<br>goods value.                                                      |
|                    |                                                                          | 3                                | Product counterfeiting, manipulation, DoS, etc.<br>causes massive damage (danger to people, large<br>losses of sales and image, and so on).                        |
| SI3                | Protecting the<br>allocation of ob<br>ject and object<br>code            | 1                                | No risk of product counterfeiting, DoS, etc.                                                                                                                       |
|                    |                                                                          | 2                                | Product counterfeiting, DoS, etc. causes limited<br>damage amounting to < 1% of goods value.                                                                       |
|                    |                                                                          | 3                                | Product counterfeiting, DoS, etc. causes massive<br>damage (danger to people, large losses of sales<br>and image, and so on).                                      |
| SI4                | Protection of lo<br>gistical data                                        | 1                                | Low dependency on logistical data                                                                                                                                  |
|                    |                                                                          | 2                                | Incorrect or missing logistical data causes limited<br>damage amounting to < 1% of goods value.                                                                    |
|                    |                                                                          | 3                                | Incorrect or missing logistical data causes mas<br>sive damage amounting to > 1% of goods value<br>or danger to persons, significant loss of image,<br>and so on.  |
| SI5                | Protection<br>against DoS at<br>tacks on the RF<br>system compo<br>nents | 1                                | Low risk of DoS attacks                                                                                                                                            |
|                    |                                                                          | 2                                | Medium risk of DoS attacks / DoS attacks cause<br>limited damage amounting to < 1% of goods<br>value.                                                              |
|                    |                                                                          | 3                                | High risk of DoS attacks / DoS attacks cause<br>massive damage amounting to > 1% of goods<br>value or danger to persons, significant loss of im<br>age, and so on. |
| SI6                | Protection<br>against spying<br>on goods flow                            | 1                                | Low risk of spying                                                                                                                                                 |
|                    |                                                                          | 2                                | Medium risk of spying / spying causes limited                                                                                                                      |

| Security objective |                                                                 | Protection<br>demand<br>category | Criteria for allocating to protection demand cate<br>gories                                                                                                                  |
|--------------------|-----------------------------------------------------------------|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| information        |                                                                 |                                  | damage amounting to < 1% of goods value.                                                                                                                                     |
|                    |                                                                 | 3                                | High risk of spying / spying causes massive dam<br>age amounting to > 1% of goods value or danger<br>to persons, significant loss of image, and so on.                       |
| SI7                | Availability of<br>EPC data                                     | 1                                | Low risk of non-availability                                                                                                                                                 |
|                    |                                                                 | 2                                | Medium risk of non-availability / non-availability<br>causes limited damage amounting to < 1% of<br>goods value.                                                             |
|                    |                                                                 | 3                                | High risk of non-availability / non-availability<br>causes massive damage amounting to > 1% of<br>goods value or danger to persons, significant loss<br>of image, and so on. |
| SP1                | Protection of<br>personal data                                  | 1                                | Customer's reputation is damaged.                                                                                                                                            |
|                    |                                                                 | 2                                | Customer's social existence is damaged.                                                                                                                                      |
|                    |                                                                 | 3                                | Customer's physical existence is damaged.                                                                                                                                    |
| SP2                | Data minimisa<br>tion                                           | 1                                | Personal data is not gathered during the sales<br>process.                                                                                                                   |
|                    |                                                                 | 2                                | A personal link is set up during the sales process<br>by means of a customer card number, but prod<br>uct-related logistical data is not used.                               |
|                    |                                                                 | 3                                | Personal data relating to special methods of pay<br>ment (e.g. invoice) is used during the sales proc<br>ess.                                                                |
| SP3                | Protection<br>against the crea<br>tion of move<br>ment profiles | 1                                | Customer's reputation is damaged.                                                                                                                                            |
|                    |                                                                 | 2                                | Customer's social existence is damaged.                                                                                                                                      |
|                    |                                                                 | 3                                | Customer's physical existence is damaged.                                                                                                                                    |

**Table 8–12 Definition of protection demand categories** 

# <span id="page-81-0"></span>**8.3 Threats**

This section deals with potential threats to the security targets described in section [8.2.](#page-73-1) Threats to the following system components are considered:

| field number | 1      | 2                                         | 3                |
|--------------|--------|-------------------------------------------|------------------|
| field        | threat | associated component and its abbreviation | index num<br>ber |

<span id="page-82-0"></span>

| field number | 1 | 2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 3       |
|--------------|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
|              |   | C := contact-less interface according<br>ISO/IEC18000-6C                                                                                                                                                                                                                                                                                                                                                                                                                             | 1,  , n |
|              |   | T := Transponder (passiv)<br>RFID-Transponder according to EPCglobal<br>Gen2                                                                                                                                                                                                                                                                                                                                                                                                         |         |
|              |   | R := Reader<br>Reader will be used for communication<br>with the transponder during the whole life<br>cycle of the transponder and by all entities<br>in the supply chain.                                                                                                                                                                                                                                                                                                           |         |
|              |   | K := key management<br>Key and password management is neces<br>sary as soon as passwords are used to<br>e.g. secure kill commands or check au<br>thentication for cryptographic methods.                                                                                                                                                                                                                                                                                             |         |
|              |   | S := Background systems                                                                                                                                                                                                                                                                                                                                                                                                                                                              |         |
| Content      | T | 1<br>IT systems of the trade logistic which<br>ensure the flow of logistic data be<br>tween all entities according to the re<br>quirements of the specific application.<br>To this belongs implementation of<br>functionality according EPCIS, man<br>agement of terminals and locations,<br>functions to correct read errors and<br>supply of information to detect product<br>counterfeits.<br>2<br>IT systems of the retailer, which does<br>not process and store personal data. |         |
|              |   | V := Customer data systems of the retailer<br>The customer data systems of the retailer<br>are the only components in the system,<br>which process and store in some cases<br>personal data. Therefore special threats<br>appear which shall be compensated by<br>special countermeasures.                                                                                                                                                                                           |         |
|              |   | In the special implementation these are<br>e.g. CRM systems (e.g. with loyalty cards),<br>systems for controlling and delivery of in<br>voices, check of creditworthiness, etc.                                                                                                                                                                                                                                                                                                      |         |

**Table 8–13 Coding scheme of threats** 

The potential threats and security targets relating to each system component are described in the following tables.

#### <span id="page-83-0"></span>**8.3.1 Threats to the contactless interface**

| Code and name of threat |                                                               | Security<br>targets<br>threatened | Description of threat                                                                                                                                                                                                                              |
|-------------------------|---------------------------------------------------------------|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TC1                     | Lack of com<br>patibility be<br>tween the inter<br>faces      | SS1                               | Lack of compatibility between the interfaces of<br>the transponder and reader. The result is simi<br>lar to a DoS attack on the system. It may not<br>be possible to gather logistical data, perform<br>self-checkouts or deactivate transponders. |
| TC2                     | Eavesdropping                                                 | SI4, SI6                          | Unauthorised listening-in to communication<br>between a transponder and a reader.                                                                                                                                                                  |
| TC3                     | DoS attack on<br>the RF interface                             | SI5                               | DoS attacks can take various forms<br>1<br>Abuse of the kill command<br>2<br>Jamming<br>3<br>Blocker tags<br>4<br>EMP<br>It may not be possible to gather logistical data,<br>perform self-checkouts or deactivate trans<br>ponders.               |
| TC4                     | Outside influ<br>ence over other<br>existing applica<br>tions | SI7                               | Some other RF applications use the same or<br>neighbouring working frequencies. This can<br>impair function.                                                                                                                                       |

**Table 8–14 Threats to the contact-less interface** 

### **8.3.2 Threats to the transponder**

| Code and name of threat |                                                              | Security<br>targets<br>threatened | Description of threat                                                                                                                                                         |
|-------------------------|--------------------------------------------------------------|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TT1                     | Unauthorised<br>retrieval of ob<br>ject code                 | SI4, SI6                          | No direct threat. Indirect threats caused by the<br>unauthorised retrieval of object codes are de<br>scribed in TT2, TT3, TT4 and TT10.                                       |
| TT2                     | Unauthorised<br>writing / ma<br>nipulation of<br>object code | SI2, SI3,<br>SI4                  |                                                                                                                                                                               |
| TT3                     | Cloning of<br>transponder                                    | SI2, SI3,<br>SI4                  | High-precision copy of tags, labels, etc.                                                                                                                                     |
| TT4                     | Emulation of<br>transponder                                  | SI2, SI3,<br>SI4                  | Emulating the electrical function of the trans<br>ponder using a programmable device. This<br>could, for example, be used to simulate the<br>checking-out of a tagged object. |

<span id="page-84-0"></span>

| Code and name of threat |                                                                           | Security<br>targets<br>threatened | Description of threat                                                                                                                                                                                                                                                                                                                                                    |
|-------------------------|---------------------------------------------------------------------------|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TT5                     | Removal of<br>transponder                                                 | SI3, SI3,<br>SI4                  | Removing the transponder can remove the as<br>sociation between the object and the object<br>code. A combination of TT5 and TT6 could en<br>able the swapping of object codes.                                                                                                                                                                                           |
| TT6                     | Unauthorised<br>attachment of a<br>transponder                            | SI3, SI4                          | Attaching a new transponder to an object<br>would enable a new code to be given to that<br>object. A combination of TT5 and TT6 could<br>enable the swapping of object codes.                                                                                                                                                                                            |
| TT7                     | Unauthorised<br>deactivation                                              | SI2, SI3,<br>SI4, SI5,<br>SI7     | The unauthorised use of the kill function can<br>permanently deactivate the transponder.                                                                                                                                                                                                                                                                                 |
| TT8                     | DoS attacks                                                               | SI5                               | In addition to the scenario in TT7, a trans<br>ponder can also be destroyed mechanically or<br>by EMP.                                                                                                                                                                                                                                                                   |
| TT9                     | Transponder<br>malfunction                                                | SS1, SS2,<br>SI5, SI7             | Transponder malfunctions can be caused in a<br>range of scenarios by technical faults, incorrect<br>operation, or DoS attacks:<br>1<br>Fault in contactless interface<br>2<br>Fault in reference information (keys, etc.)<br>3<br>Fault in application implementation<br>4<br>Fault in object code                                                                       |
| TT10                    | Tracking by<br>means of unau<br>thorised scan<br>ning by third<br>parties | SP3                               | The anti-collision mechanism in the trans<br>ponder sends a non-encrypted identifier to<br>every reader that sends out a request. This<br>can be used by unauthorised persons to re<br>trieve the transponder's identifier, and possibly<br>to generate movement profiles based on that<br>identifier.                                                                   |
| TT11                    | Lack of fallback<br>solution in the<br>event of mal<br>function           | SS2, SI7                          | 1<br>Logistical data about the object may not<br>be available.<br>2<br>Self-checkout and transponder deactiva<br>tion may not work.<br>3<br>The lack of a fail-safe method of assessing<br>the genuineness or identity of the trans<br>ponder in the event of a defective chip can<br>cause difficulties when it comes to deter<br>mining the authenticity of an object. |
| TT12                    | Manipulation of<br>UID                                                    | SI3, SI4                          | Manipulations to or faults in the UID or the UID<br>function can threaten the integrity of the logisti<br>cal data, and in particular threaten any protec<br>tion against transponder cloning.                                                                                                                                                                           |
| TT13                    | Incorrectly gen<br>erated UID                                             | SI3, SI4                          | A wrongly allocated UID can threaten the in<br>tegrity of the logistical data, and in particular<br>threaten any protection against transponder                                                                                                                                                                                                                          |

| Code and name of threat |                                                                | Security<br>targets<br>threatened | Description of threat                                                                                                                          |
|-------------------------|----------------------------------------------------------------|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
|                         |                                                                |                                   | cloning. Threats can arise from things like:<br>1<br>Non-unique UID allocation<br>2<br>Incorrect structure<br>3<br>Incorrect manufacturer code |
| TT14                    | Unauthorised<br>scanning of per<br>sonal data                  | SI1, SP1                          | Not relevant, since personal data is not stored<br>on the transponder.                                                                         |
| TT15                    | Unauthorised<br>writing / ma<br>nipulation of<br>personal data | SI1, SP1                          | Not relevant, since personal data is not stored<br>on the transponder.                                                                         |

**Table 8–15 Threats to the transponder** 

### **8.3.3 Threats to the reader**

| Code and name of threat |                                                              | Security<br>targets<br>threatened | Description of threat                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------|--------------------------------------------------------------|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TR1                     | Unauthorised<br>manipulation of<br>reference in<br>formation | SI2, SI3,<br>SI4, SI5,<br>SI7     | Manipulation of reference information (keys,<br>evaluation algorithms, blacklists and whitelists)<br>can be employed for unauthorised use and for<br>DoS.                                                                                                                                                                                                                                                                                                                                                                                               |
| TR2                     | Unauthorised<br>scanning of ref<br>erence informa<br>tion    | SI2, SI4,<br>SI5, SI7             | Scanning of reference information (keys,<br>evaluation algorithms, blacklists and whitelists)<br>can be employed for unauthorised use (e.g.<br>counterfeiting of logistical data) and for DoS.                                                                                                                                                                                                                                                                                                                                                          |
| TR3                     | Reader mal<br>function                                       | SS1, SS2,<br>SI5, SI7             | Reader malfunctions can be caused in a range<br>of scenarios by technical faults, incorrect op<br>eration, or DoS attacks:<br>1<br>Fault in contactless interface<br>2<br>Fault in reference information (keys, black<br>lists, etc.)<br>3<br>Fault in application implementation<br>4<br>Fault in evaluation algorithms for object<br>codes<br>5<br>Interruption in power supply<br>6<br>Jamming<br>7<br>Blocker tag<br>8<br>Interruption of the link to the central sys<br>tem<br>9<br>Physical destruction<br>10 Fault in user instruction functions |

<span id="page-86-0"></span>

| Code and name of threat |                              | Security<br>targets<br>threatened | Description of threat                                                                                      |
|-------------------------|------------------------------|-----------------------------------|------------------------------------------------------------------------------------------------------------|
| TR4                     | Lack of user<br>instructions | SS3                               | A lack of user-friendliness at checkout or kill<br>terminals can cause considerable operative<br>problems. |

**Table 8–16 Threats to the reader** 

#### **8.3.4 Threats to the key management system**

| Code and name of threat |                                          | Security<br>targets<br>threatened | Description of threat                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-------------------------|------------------------------------------|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TK1                     | Quality of key<br>data                   | SI2, SI3,<br>SI4, SI5,<br>SI6     | Deficient key quality increases the chances of<br>successful attacks.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| TK2                     | Unauthorised<br>scanning of key<br>data  | SI2, SI3,<br>SI4, SI5,<br>SI6     | The retrieval of key data by unauthorised per<br>sons can discredit the system and facilitate at<br>tacks, e.g. on any cryptographically protected<br>data or functions.                                                                                                                                                                                                                                                                                                                                                    |
| TK3                     | Manipulation of<br>key data              | SI2, SI3,<br>SI4, SI5,<br>SI6     | The manipulation of key data can discredit the<br>system's security concept and facilitate at<br>tacks, e.g. on any cryptographically protected<br>data or functions. Manipulation can affect the<br>generation of keys, the production of key<br>carriers, the transmission of keys and the local<br>use of keys.                                                                                                                                                                                                          |
| TK4                     | Key manage<br>ment system<br>malfunction | SS1, SS2                          | Key management system malfunctions can be<br>caused in a variety of scenarios by technical<br>faults, incorrect operation or DoS attacks:<br>1<br>Fault in local and central systems<br>2<br>Lack of availability of local and central sys<br>tems<br>3<br>Fault in data storage<br>4<br>Fault in specific application implementa<br>tion<br>5<br>Fault in evaluation algorithms for entitle<br>ments<br>6<br>Fault in power supply<br>7<br>Interruption of the link to the central sys<br>tem<br>8<br>Physical destruction |

<span id="page-87-0"></span>

| Code and name of threat |                              | Security<br>targets<br>threatened | Description of threat                                                                                                                                                                                                                                       |
|-------------------------|------------------------------|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TK5                     | Lack of fallback<br>solution | SS2                               | The availability of the necessary key informa<br>tion is essential if the system as a whole is to<br>work at all. If the key management system mal<br>functions and there is no fallback solution, the<br>function of the entire system will be threatened. |

### **8.3.5 Threats to backend systems**

| Code and name of threat |                                                          | Security<br>targets<br>threatened | Description of threat                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------|----------------------------------------------------------|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TS1                     | Lack of fallback<br>solution                             | SS2, SI4,<br>SI7                  | The lack of a fallback solution when system<br>components fail can lead to a complete break<br>down of services (acquisition and distribution<br>of logistical data, etc.).                                                                                                                                                                                                                                |
| TS2                     | Unauthorised<br>scanning of<br>data in the sys<br>tem    | SS1, SI2,<br>SI3, SI4,<br>SI6     | The backend systems store information about<br>the objects, object codes, readers, warehouse<br>locations and so on. The retrieval of this data<br>by unauthorised persons would discredit the<br>system and enable attacks.                                                                                                                                                                               |
| TS3                     | Manipulation of<br>data in the sys<br>tem                | SS1, SI2,<br>SI3, SI4             | The backend systems store information about<br>the objects, object codes, readers, warehouse<br>locations and so on. The manipulation of this<br>data by unauthorised persons represents a se<br>rious attack.                                                                                                                                                                                             |
| TS4                     | System mal<br>function                                   | SS1, SS2                          | Individual system component malfunctions can<br>be caused in a range of scenarios by technical<br>faults, incorrect operation or DoS attacks:<br>1<br>Fault in local and central systems<br>2<br>Lack of availability of local and central sys<br>tems<br>3<br>Fault in data storage<br>4<br>Fault in power supply<br>5<br>Interruption of the link to the central sys<br>tem<br>6<br>Physical destruction |
| TS5                     | Lack of com<br>patibility be<br>tween the inter<br>faces | SS1                               | Lack of compatibility between interfaces<br>causes malfunctions. The result is similar to a<br>DoS attack on the system. Many objects<br>and/or object codes may be affected.                                                                                                                                                                                                                              |
| TS6                     | Unauthorised<br>retrieval of lo                          | SI4, SI6                          | Unauthorised active retrieval of logistical data.                                                                                                                                                                                                                                                                                                                                                          |

<span id="page-88-0"></span>

| Code and name of threat |                                                                      | Security<br>targets<br>threatened | Description of threat                                                                                                                                                                                                                                                                                            |
|-------------------------|----------------------------------------------------------------------|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                         | gistical data                                                        |                                   |                                                                                                                                                                                                                                                                                                                  |
| TS7                     | Unauthorised<br>writing / ma<br>nipulation of<br>logistical data     | SI4                               | Unauthorised writing of logistical data into the<br>backend system for the purpose of manipulat<br>ing or compromising data. This threatens in<br>particular the header, which contains the type<br>of data among other things.                                                                                  |
| TS8                     | Protection of<br>client-specific<br>applications and<br>object codes | SI2, SI3,<br>SI4, SI6             | If multiple entities are supported by the sys<br>tems with objects and applications, then<br>threats may be caused by entities in the sys<br>tem (e.g. rival data may be obtained). It must<br>be assured that the confidentiality, integrity and<br>availability of data is preserved from client to<br>client. |
| TS9                     | Product coun<br>terfeiting                                           | SI2, SI3,<br>SI4                  | Product counterfeiting can cause considerable<br>commercial damage and may even threaten<br>the safety and health of customers.                                                                                                                                                                                  |

**Table 8–18 Threats to the backend system** 

| 8.3.6 |  | Threats to customer data systems |  |  |
|-------|--|----------------------------------|--|--|
|-------|--|----------------------------------|--|--|

| Code and name of threat |                                                          | Security<br>targets<br>threatened | Description of threat                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------|----------------------------------------------------------|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TV1                     | Lack of fallback<br>solution                             | SS2                               | The lack of a fallback solution in the event of a<br>malfunction can lead to a complete breakdown<br>of services (sales, invoicing, bonus calculation,<br>guarantee processing, product delivery, and so<br>on.).                                                                                                                                                                                     |
| TV2                     | System mal<br>function                                   | SS1, SS2                          | Customer data system malfunctions can be<br>caused in a variety of scenarios by technical<br>faults, incorrect operation or DoS attacks:<br>1<br>Fault in local and central systems<br>2<br>Lack of availability of local and central sys<br>tems<br>3<br>Fault in data storage<br>4<br>Fault in power supply<br>5<br>Interruption of the link to the central sys<br>tem<br>6<br>Physical destruction |
| TV3                     | Lack of com<br>patibility be<br>tween the inter<br>faces | SS1                               | Lack of compatibility between interfaces<br>causes malfunctions. The result is similar to a<br>DoS attack on the system. Many customers<br>could be affected.                                                                                                                                                                                                                                         |

<span id="page-89-0"></span>

| Code and name of threat |                                                                                          | Security<br>targets<br>threatened | Description of threat                                                                                                                                                                                                           |
|-------------------------|------------------------------------------------------------------------------------------|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TV4                     | Unauthorised<br>scanning of<br>sales and in<br>voicing informa<br>tion                   | SI1, SP1                          | Unauthorised active retrieval of invoicing data.                                                                                                                                                                                |
| TV7                     | Unauthorised<br>writing / ma<br>nipulating of<br>sales and in<br>voicing informa<br>tion | SI1, SP1                          | Unauthorised writing of invoicing data into the<br>customer data system for the purpose of ma<br>nipulating or compromising data.                                                                                               |
| TV8                     | Unauthorised<br>scanning of per<br>sonal data                                            | SI1, SP1                          | Disclosure of customer data.                                                                                                                                                                                                    |
| TV9                     | Unauthorised<br>writing / ma<br>nipulation of<br>personal data                           | SI1, SP1                          | Manipulation of customer data.                                                                                                                                                                                                  |
| TV10                    | Falsification of<br>identity data                                                        | SI1, SP1                          | Recipients may have to identify themselves<br>when objects are delivered or collected. Pro<br>ducing a false identity could allow products and<br>services to be obtained at the expense of other<br>customers or the retailer. |
| TV11                    | Unauthorised<br>collection and<br>storage of data                                        | SP2                               | Gathering and storing data without justification<br>infringes the stipulation on data minimisation.                                                                                                                             |
| TV12                    | Unauthorised<br>linking of data                                                          | SP2                               | Unauthorised linking of personal data with in<br>voicing and/or logistical data.                                                                                                                                                |

**Table 8–19 Threats to the customer data system** 

# <span id="page-89-1"></span>**8.4 Safeguards**

This section describes the safeguards that can be used to counter the threats detailed in section [8.3.](#page-81-0) These safeguards are defined in such a way that, when built successively upon each other, they afford increasing levels of security in cases where different levels are possible. Level 1 represents the lowest security category, level 3 the highest.

Level 3+ is used to denote additional safeguards that increase the security of a system, but whose expense may disproportionately exceed the value of the extra security gained.

The security levels are oriented around the system's protection demand categories. A threat to a security target that has been allocated to protection demand category 3 should be countered by safeguards of security level 3.

The following safeguards are generally not defined as isolated measures, but rather are to be understood as "safeguard packages". As a rule, the security of components and interfaces,

<span id="page-90-0"></span>and of the system as a whole, can only be increased in a meaningful way if safeguards are employed across the board as packages. Furthermore, alternative possibilities are defined within the security levels; for instance, a secure environment (which generally does not exist) can replace the encrypted storage of data.

| field number | 1                      | 2                                                 | 3                |
|--------------|------------------------|---------------------------------------------------|------------------|
| field        | safeguard /<br>measure | associated component and its abbreviation         | index num<br>ber |
| content      | M                      | C := contact-less interface                       | 1,  , n          |
|              |                        | M := carrier medium                               |                  |
|              |                        | R := reader                                       |                  |
|              |                        | K := key management system                        |                  |
|              |                        | S := sales, inspection and background sys<br>tems |                  |
|              |                        | V = customer data systems                         |                  |

**Table 8–20 Coding scheme of safeguard measures** 

#### <span id="page-90-1"></span>**8.4.1 Safeguards for the protection of the system as a whole**

The following safeguards relate to the system as a whole, and can basically be applied to all system components. The focus is on the RF interface and the backend systems, including their interfaces.

Separate sections will deal with the readers, key management systems and customer data systems.

| MS1     | Code and name of safeguard                                                                                                                                                                                                                                                                      | Threats addressed |  |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|         | Introduction of interface tests and approval<br>procedures                                                                                                                                                                                                                                      | TS5, TC1, TV3     |  |
| General | The aim of introducing interface-based test specifications and performing these<br>tests on all components is to achieve compatibility between components and to<br>enable this to be verified. This process should include all levels of the interfaces<br>(OSI model), including fault cases. |                   |  |
|         | Interface test                                                                                                                                                                                                                                                                                  |                   |  |
| 1       | •<br>Apply existing test regulations for contactless interfaces as defined by<br>ISO/IEC18000-6C.                                                                                                                                                                                               |                   |  |
|         | •<br>Draw up and apply specific test regulations for the application-specific func<br>tions of the interfaces between transponders and readers.                                                                                                                                                 |                   |  |
|         | •<br>Draw up and apply specific test regulations for the protocols and applica<br>tion-specific functions of the interfaces between the rest of the system com<br>ponents.                                                                                                                      |                   |  |
| 2       | Component approval                                                                                                                                                                                                                                                                              |                   |  |
|         | See above, additional component approval (transponders, readers, key man<br>agement).                                                                                                                                                                                                           |                   |  |

<span id="page-91-0"></span>

| MS1 | Code and name of safeguard                                                                                                            | Threats addressed |  |
|-----|---------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|     | Introduction of interface tests and approval<br>procedures                                                                            | TS5, TC1, TV3     |  |
|     | Certification                                                                                                                         |                   |  |
| 3   | See above, additional certification by an independent institute, for transponders,<br>readers and, where necessary, other components. |                   |  |

| Table 8–21 | Protection of the system as a whole through introduction of interface |
|------------|-----------------------------------------------------------------------|
|            | tests and approval procedures                                         |

| MS2     | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Threats addressed |  |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|         | Preventing eavesdropping on data exchange<br>between transponder and reader                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | TC2               |  |
| General | This safeguard applies to every implementation of a contactless interface that<br>exists between the transponder and the readers, such as the ones installed in<br>warehouses, checkout terminals and kill terminals. The current EPCglobal<br>specifications do not provide a means of preventing eavesdropping by means of<br>cryptographic safeguards, since these mechanisms have not yet been specified<br>for transponders in the field of trade logistics. For this reason the safeguards<br>must be infrastructural, personnel-related or organisational, such as:<br>•<br>forbidding the use of RFID readers on the business premises in the opera<br>tor's terms and conditions of business;<br>•<br>checking business premises for readers installed without permission;<br>•<br>fitting suitable shielding around the reader–transponder communication<br>area, where this is structurally possible (both architecturally and from a |                   |  |
|         | functional point of view).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                   |  |
|         | Data is sent unencrypted between the terminal and EPCglobal transponder.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                   |  |
| 1       | Infrastructural, personnel-related and organisational measures prevent the op<br>eration of enemy systems within a range of five metres of the reader.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                   |  |
| 2       | Data is sent unencrypted between the terminal and EPCglobal transponder.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                   |  |
|         | Infrastructural, personnel-related and organisational measures prevent the op<br>eration of enemy systems within a range of twenty metres of the reader.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                   |  |
| 3       | Data is sent unencrypted between the terminal and EPCglobal transponder.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                   |  |
|         | Infrastructural, personnel-related and organisational measures prevent the op<br>eration of enemy systems within a range of fifty metres of the reader.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                   |  |

#### **Table 8–22 Protection of the system as a whole through preventing eavesdropping**

| MS3 | Code and name of safeguard                                                                                                                                          | Threats addressed |  |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|     | Assuring reliable transmission between termi<br>nal and transponder                                                                                                 | TC2, TC3, TC4     |  |
| 1   | Long-term testing and organisational safeguards                                                                                                                     |                   |  |
|     | •<br>Perform a reality-based, long-term test before assuming working operation.<br>•<br>The location is regularly checked for readers and jammers installed without |                   |  |

<span id="page-92-0"></span>

| MS3 | Code and name of safeguard                                                                                                                                                              | Threats addressed |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|     | Assuring reliable transmission between termi<br>nal and transponder                                                                                                                     | TC2, TC3, TC4     |
|     | permission.                                                                                                                                                                             |                   |
|     | •<br>Employees and visitors are not permitted to carry devices that could be<br>used for DoS attacks. Customers are not permitted to use devices that<br>could be used for DoS attacks. |                   |
| 2   | Surveying                                                                                                                                                                               |                   |
| 3   | In addition to the safeguards from MS3.1, the location is surveyed with an eye to<br>jamming, before operation is assumed.                                                              |                   |
|     | Use of field detectors                                                                                                                                                                  |                   |
| 3+  | In addition to the safeguards from MS3.2, field detectors are used to detect<br>temporary jamming devices and DoS attacks.                                                              |                   |

| Table 8–23 | Protection of the system as a whole through assuring reliable trans<br>mission |
|------------|--------------------------------------------------------------------------------|
|            |                                                                                |

| MS4 | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Threats addressed  |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
|     | Definition of fallback solutions in the event of<br>system interface or system component failure                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | TS1, TS4, TV1, TV2 |
| 1   | Definition of suitable operating processes, offline capability and backup                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                    |
| 2   | •<br>System components must in principle (at least temporarily) be able to func<br>tion autonomously without a backend system or if system interfaces fail.<br>•<br>Data must be backed up regularly in order to exclude the possibility of a to<br>tal loss.<br>•<br>The replacement of defective components must be regulated.<br>•<br>All components and interfaces must have fallback processes that employ<br>operative safeguards to rectify or moderate the operative problems that can<br>arise following the failure of a component.<br>•<br>Fallback solutions must be specified in the contractual arrangements be<br>tween customers, service operators and suppliers, and their consequences<br>taken into account. |                    |
| 3   | Implementation according to fallback concept:<br>In addition to MS4.1, 2:<br>•<br>A system and process concept must be developed that defines the avail<br>ability and fallback solutions explicitly with availability periods and fallback<br>intervals.<br>•<br>Critical components must have an uninterruptible power supply (UPS) and<br>other security mechanisms (such as a RAID), so that the failure of sub<br>components does not impair the availability of the system as a whole.<br>•<br>If necessary, enough replacement system components must be provided to<br>enable the required availability to be upheld.                                                                                                    |                    |

| Table 8–24 | Protection of the system as a whole through definition of fallback solu |
|------------|-------------------------------------------------------------------------|
|            | tions                                                                   |

<span id="page-93-0"></span>

| MS5 | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                         | Threats addressed  |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
|     | Securing the confidentiality of data when<br>communicating within the system                                                                                                                                                                                                                                                                                                                                                                                       | TS2, TS6, TV4, TV8 |
| 1   | Encryption for internal communication:                                                                                                                                                                                                                                                                                                                                                                                                                             |                    |
| 2   | •<br>Data is transmitted in encrypted form. Alternatively, instead of general data<br>encryption, data can be sent via dedicated networks (closed solution), in<br>which only authorised users are administered and allowed. This network<br>would need to be protected against physical attacks from the outside by<br>means of appropriate safeguards (e.g. basic protective measures), and then<br>operated in accordance with an appropriate security concept. |                    |
| 3   | Secure communication channel:<br>•<br>Communication between the components of the system is via VPNs or a<br>similar (shielded) solution. Before communication, authentication is per<br>formed by negotiating a key between sender and receiver. The negotiated<br>key is then used for communication.                                                                                                                                                            |                    |

| Table 8–25 | Protection of the system as a whole through securing the confidential |
|------------|-----------------------------------------------------------------------|
|            | ity of data                                                           |

| MS6                        | Code and name of safeguard                                                                                                                                                                                                        | Threats addressed                              |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
|                            | Confidential storage of data                                                                                                                                                                                                      | TS2, TS3, TS6, TS7, TS8,<br>TV4, TV7, TV8, TV9 |
| 1                          | Introduction of multi-tenant access protection:                                                                                                                                                                                   |                                                |
|                            | •<br>Only a certain, legitimised group of people can access stored data (per<br>sonal data, sales data, usage data, invoicing data, blacklists, approval lists,<br>etc.).                                                         |                                                |
| 2                          | •<br>Data is stored in an environment protected against unauthorised access. If<br>access protection cannot be guaranteed, then the data should be stored on<br>an encrypted data carrier (hard drive encryption tools are used). |                                                |
|                            | Alternatively, other equally effective encryption mechanisms can be used. The<br>algorithm strength must be at least that of the 3DES algorithm.                                                                                  |                                                |
|                            | The type and strength of the mechanism should be adapted to future develop<br>ments in accordance with[ALGK_BSI].                                                                                                                 |                                                |
|                            | Introduction of multi-tenant access protection with a defined role model.                                                                                                                                                         |                                                |
| See 1–2, furthermore:<br>3 |                                                                                                                                                                                                                                   |                                                |
|                            | •<br>A client concept in the form of a role model is to be established.                                                                                                                                                           |                                                |

#### **Table 8–26 Protection of the system as a whole through confidential storage of data**

|     | Code and name of safeguard                                                                                          | Threats addressed  |
|-----|---------------------------------------------------------------------------------------------------------------------|--------------------|
| MS7 | Securing the data integrity in order to protect<br>against manipulation when transmitting data<br>within the system | TS3, TS7, TV7, TV9 |
| 1   | Cryptographic integrity safeguards:                                                                                 |                    |

<span id="page-94-0"></span>

| MS7 | Code and name of safeguard                                                                                                                                                                                                                                                                                                     | Threats addressed  |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
|     | Securing the data integrity in order to protect<br>against manipulation when transmitting data<br>within the system                                                                                                                                                                                                            | TS3, TS7, TV7, TV9 |
| 2   | •<br>The integrity of data transmission is guaranteed using MAC protection. The<br>algorithms must be chosen in accordance with [ALGK_BSI].<br>•<br>The type and strength of the mechanism should be adapted to future devel<br>opments in accordance with[ALGK_BSI].                                                          |                    |
| 3   | MAC or signatures:<br>•<br>The integrity of data transmission is guaranteed using MAC protection or by<br>signatures. MAC and signature processes are to be chosen in accordance<br>with [ALGK_BSI].<br>•<br>The type and strength of the mechanism should be adapted to future devel<br>opments in accordance with[ALGK_BSI]. |                    |

| Table 8–27 | Protection of the system as a whole through securing the data integrity |
|------------|-------------------------------------------------------------------------|
|            | when transmitting data                                                  |

| MS8 | Code and name of safeguard                                                                                                                                                                 | Threats addressed  |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
|     | Securing data integrity when storing data                                                                                                                                                  | TS3, TS7, TV7, TV9 |
| 1   | Data is stored in a secure environment with access protection as defined in<br>MS6.                                                                                                        |                    |
| 2   |                                                                                                                                                                                            |                    |
| 3   | Checksums:<br>•<br>A checksum is used to protect against technically related integrity failures<br>(CRC, hamming codes, ); this can also be provided by the operating sys<br>tem involved. |                    |

#### **Table 8–28 Protection of the system as a whole through securing data integrity when storing data**

| MS9     | Code and name of safeguard                                                                                                                                                                                                                                                                                                                  | Threats addressed |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|         | Securing the system's functions against DoS<br>attacks at the interfaces                                                                                                                                                                                                                                                                    | TS4, TV2          |
| General | The system can be secured against DoS attacks at the interfaces or on the<br>transmission routes by means of structural, technical and organisational safe<br>guards. Various safeguards can be used, depending on the security level.                                                                                                      |                   |
| 1       | Simple structural, technical and organisational safeguards:<br>•<br>Structural safeguards: protect the transmission routes against wanton de<br>struction, e.g. by using indestructible materials and shielding data lines.<br>Create secure areas.<br>•<br>Organisational safeguards: simple access control to secure areas (photo<br>ID). |                   |
| 2       | Extended structural, technical and organisational safeguards:<br>•<br>Additional organisational safeguards, such as the introduction of a role<br>model with an accompanying entitlement concept. More thorough mechani-                                                                                                                    |                   |

<span id="page-95-0"></span>

| MS9 | Code and name of safeguard                                                                   | Threats addressed |  |
|-----|----------------------------------------------------------------------------------------------|-------------------|--|
|     | Securing the system's functions against DoS<br>attacks at the interfaces                     | TS4, TV2          |  |
|     | cal protection.                                                                              |                   |  |
| 3   | Security concept                                                                             |                   |  |
|     | See 1, furthermore:                                                                          |                   |  |
|     | •<br>Implement structural and technical safeguards in accordance with a security<br>concept. |                   |  |
|     | Technical safeguards: technical safeguarding of access control.                              |                   |  |

#### **Table 8–29 Protection of the system as a whole through securing the system's functions against DoS attacks**

| MS10 | Code and name of safeguard                                                                | Threats addressed |
|------|-------------------------------------------------------------------------------------------|-------------------|
|      | Securing the function of the system against<br>incorrect operation by employees and users | TS4               |
| 1    | Tests, personnel and user instructions:                                                   |                   |
| 2    | •<br>Define the requirements for user instructions; check the components using            |                   |
| 3    | these requirements; empirical tests; employ knowledgeable staff.                          |                   |

#### **Table 8–30 Protection of the system as a whole through securing the function of the system against incorrect operation**

|      | Code and name of safeguard                                                                                          | Threats addressed  |
|------|---------------------------------------------------------------------------------------------------------------------|--------------------|
| MS11 | Secure the function of the system to prevent<br>the technical failure of components and<br>transmission routes      | TS4, TS5, TV2, TV3 |
|      | Manufacturer's declaration:                                                                                         |                    |
| 1    | •<br>Guarantee safety in accordance with specifications, by means of manufac<br>turer's internal quality assurance. |                    |
|      | Testing in accordance with test specifications:                                                                     |                    |
| 2    | •<br>Draw up test specifications for the various system components.                                                 |                    |
|      | •<br>Technical checking of components in accordance with the relevant test<br>specifications.                       |                    |
|      | •<br>Specification and execution of integration tests in test and actual environ<br>ments.                          |                    |

<span id="page-96-0"></span>

|      | Code and name of safeguard                                                                                                      | Threats addressed  |
|------|---------------------------------------------------------------------------------------------------------------------------------|--------------------|
| MS11 | Secure the function of the system to prevent<br>the technical failure of components and<br>transmission routes                  | TS4, TS5, TV2, TV3 |
|      | Evaluation of components:                                                                                                       |                    |
| 3    | See 2, furthermore:                                                                                                             |                    |
|      | •<br>The relevant system components (at least the readers and carrier media)<br>are tested by independent testing laboratories. |                    |
|      | •<br>An independent institute certifies the relevant system components.                                                         |                    |
|      | •<br>An approval process is established for the system components.                                                              |                    |

#### **Table 8–31 Protection of the system as a whole through securing the function of the system to prevent technical failures**

| MS12    | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Threats addressed |  |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|         | Specifications for system concept and re<br>quirements for components                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | TS5, TV3          |  |
| General | The characteristics of a system in relation to its fundamental operating proc<br>esses must be specified and assured. Take note: existing components often<br>have to be integrated, yet the fundamental parameters and characteristics of the<br>system as a whole must be specified and achieved. This applies in particular to<br>the performance and availability of certain processes. To enable this integration<br>into the system as a whole, the requirements for each system component's in<br>teraction with the system as a whole must be specified and upheld.<br>Special attention should be paid to the incorporation of new applications and<br>objects. |                   |  |
|         | Manufacturer's declaration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                   |  |
| 1       | •<br>The manufacturer guarantees that the specifications are adhered to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                   |  |
|         | Integration test and declaration of conformity:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                   |  |
| 2       | •<br>Draw up and perform integration tests (see MS11).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                   |  |
|         | •<br>Establish an approval procedure.<br>•<br>Conformity must be proven by integration tests.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                   |  |
|         | Interoperability tests according to test concept, evaluation:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                   |  |
| 3       | •<br>Draw up and perform integration tests (see MS11).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                   |  |
|         | •<br>Establish an approval procedure.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                   |  |
|         | •<br>Components evaluated by independent test laboratories.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                   |  |
|         | •<br>Certification of components.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                   |  |

#### **Table 8–32 Protection of the system as a whole through specification of the system and the components**

<span id="page-97-0"></span>

| MS13    | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Threats addressed |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|         | Ergonomic user instructions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | TS4, TR4, TV2     |
| General | The design of all hardware components must fulfil certain ergonomic require<br>ments. Alongside visual demands (recollection, colour of keypads, legibility of<br>displays ), these include requirements relating to operation (including for the<br>severely disabled), and safety against injury.                                                                                                                                                                                                                                           |                   |
| 1       | Manufacturer's declaration<br>•<br>Manufacturer declares that ergonomic principles have been applied.<br>•<br>The relevant use cases from the generic operating processes (e.g. sale,<br>self-checkout, deactivation at the kill desk and so on) are illustrated by the<br>manufacturer to help instruct customers and staff.                                                                                                                                                                                                                 |                   |
| 2       | Practical testing<br>•<br>Manufacturer declares that ergonomic principles have been applied.<br>•<br>User acceptance is gauged in a practical test.                                                                                                                                                                                                                                                                                                                                                                                           |                   |
| 3       | Specification, implementation and testing of an overall concept for ergonomics<br>and user instruction:<br>•<br>System-wide definitions must be laid down relating to ergonomics and user<br>instructions, and these must guarantee that all of the components within the<br>system satisfy the same standards. Gradual introduction is possible.<br>•<br>Implement uniform user instructions for each application.<br>•<br>Practical testing to assess user acceptance.<br>•<br>Approval procedure for overall and component specifications. |                   |

| Table 8–33 | Protection of the system as a whole through ergonomic user instruc<br>tions |
|------------|-----------------------------------------------------------------------------|
|            |                                                                             |

| MS14 | Code and name of safeguard                                                                                                                                                                                                                                                                                                              | Threats addressed  |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
|      | Support                                                                                                                                                                                                                                                                                                                                 | TS4, TS5, TV2, TV3 |
| 1    | Manufacturer support<br>•<br>The manufacturer of system components must put measures in place that<br>assist service operators when operating the system (e.g. help desk, 1st,<br>2nd, 3rd-level support, …). This support is subject to bilateral contractual<br>regulations (SLAs) between the manufacturer and the service operator. |                    |
| 2    | Entity-wide support<br>•<br>Define a support concept for the system belonging to an entity (e.g. manu<br>facturer, retailer).                                                                                                                                                                                                           |                    |
| 3    | System-wide support<br>•<br>Define an umbrella support concept that covers the systems belonging to<br>the various entities (see 2) and also identifies defined interfaces to the other<br>entities. The aim is to be able to solve system-wide problems within a de<br>fined time-frame.                                               |                    |

#### **Table 8–34 Protection of the system as a whole through support**

<span id="page-98-0"></span>

| MS15    | Code and name of safeguard                                                                                                                                                                                                                                                                                               | Threats addressed |  |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|         | Using the EPC to secure against counterfeit<br>products                                                                                                                                                                                                                                                                  | TS9               |  |
| General | In the EPCglobal model, preventing product counterfeiting is one of RFID's fun<br>damental use cases. The unique EPC can be used to this end. It should be<br>noted that the EPC can be applied freely to any commercially available trans<br>ponder by any user – and that also means any attacker. See also [CFP_GS1]. |                   |  |
|         | Additional safeguards must be added in order to assure security against coun<br>terfeiting when the protection demand is higher.                                                                                                                                                                                         |                   |  |
| 1       | Using the chip's EPC                                                                                                                                                                                                                                                                                                     |                   |  |
|         | The authenticity of any transponder can be checked using its unique EPC. This<br>requires the following preconditions:                                                                                                                                                                                                   |                   |  |
|         | •<br>The EPC must be generated in accordance with the EPCglobal regulations<br>for every product that needs protecting.                                                                                                                                                                                                  |                   |  |
|         | •<br>The EPC is not generated consecutively, but instead randomly from a large<br>numerical range. This prevents counterfeiters from guessing valid EPCs.                                                                                                                                                                |                   |  |
| 2       | •<br>The product's logistical data is made available by the backend system at<br>every stage in the supply chain.                                                                                                                                                                                                        |                   |  |
|         | The authenticity of the product is checked by checking the authenticity of the<br>EPC.                                                                                                                                                                                                                                   |                   |  |
|         | •<br>Check whether the product's EPC exists in the logistical data.                                                                                                                                                                                                                                                      |                   |  |
|         | •<br>Check whether the EPC exists in a meaningful way in all the major stages<br>of the supply chain.                                                                                                                                                                                                                    |                   |  |
|         | If both conditions are fulfilled, then the EPC is considered authentic.                                                                                                                                                                                                                                                  |                   |  |
| 3       | Additional use of UID:                                                                                                                                                                                                                                                                                                   |                   |  |
|         | The following safeguards should be applied in addition to those of MS15.1, 2:                                                                                                                                                                                                                                            |                   |  |
|         | •<br>Check the authenticity of the UID in the same way that the EPC is checked<br>in MS15.1, 2.                                                                                                                                                                                                                          |                   |  |
|         | •<br>The UID is generated and implemented as described in MT2.                                                                                                                                                                                                                                                           |                   |  |

**Table 8–35 Protection of the system as a whole through EPC usage against product counterfeiting** 

#### **8.4.2 Safeguards relating to the transponder**

| MT1     | Code and name of safeguard                                                                                                                                                                                                                                                                                                                 | Threats addressed |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|         | Hardware and software access protection for<br>the EPC (write access)                                                                                                                                                                                                                                                                      | TT2, TT3          |
| General | The current EPCglobal specifications do not allow access protection or crypto<br>graphic protection of the EPC. Advanced safeguards are only possible using<br>proprietary solutions. For this reason, EPCglobal reference implementation for<br>all protection demand categories can only currently be done using the safeguard<br>below. |                   |

<span id="page-99-0"></span>

| MT1 | Code and name of safeguard                                                        | Threats addressed |
|-----|-----------------------------------------------------------------------------------|-------------------|
|     | Hardware and software access protection for<br>the EPC (write access)             | TT2, TT3          |
| 1   | Write protection for EPC                                                          |                   |
| 2   | •<br>Once written to the specified memory area, the EPC is protected irreversibly |                   |
| 3   | against overwriting. There is no read-protection.                                 |                   |

| Table 8–36 | Protection of the transponder through access protection for the EPC |
|------------|---------------------------------------------------------------------|
|            |                                                                     |

| MT2 | Code and name of safeguard                                                                                                                                                                                                                                              | Threats addressed |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|     | Protection against cloning of transponder                                                                                                                                                                                                                               | TT3, TT12, TT13   |
|     | Use of the chip's UID to prevent cloning of transponders                                                                                                                                                                                                                |                   |
| 1   | A unique UID belonging to the chip is used to prevent the transponder from be<br>ing cloned. The EPC is not sufficient for this purpose, since it can be applied<br>freely to any commercially available transponder by any user – and that also<br>means any attacker. |                   |
|     | •<br>The chip manufacturer generates the UID in accordance with [ISO18000-6].                                                                                                                                                                                           |                   |
|     | •<br>The UID is loaded by the chip manufacturer during the wafer test. This is<br>done in a secure, certified environment in accordance with Common Crite<br>ria.                                                                                                       |                   |
|     | •<br>Once written to the specified memory area, the UID is protected irreversibly<br>against overwriting.                                                                                                                                                               |                   |
|     | •<br>Introduce a zero-balance procedure when manufacturing and delivering the<br>chip.                                                                                                                                                                                  |                   |
|     | •<br>Rejects are destroyed or marked.                                                                                                                                                                                                                                   |                   |
|     | •<br>The valid UID of the original transponder must be available in addition to the<br>EPC in order to allow cloned transponders to be found.                                                                                                                           |                   |
|     | Protection against cloning of transponder:                                                                                                                                                                                                                              |                   |
|     | The following safeguards should be applied in addition to those of MT2.1:                                                                                                                                                                                               |                   |
| 2   | •<br>Introduce a zero-balance procedure when manufacturing and delivering the<br>transponder.                                                                                                                                                                           |                   |
|     | •<br>Rejects are destroyed                                                                                                                                                                                                                                              |                   |
|     | •<br>The list of UIDs of non-rejects is delivered to the issuer together with<br>the delivery of chips.                                                                                                                                                                 |                   |
|     | •<br>Use simple visual security features on the transponder.                                                                                                                                                                                                            |                   |
|     | Advanced protection against cloning of transponder:                                                                                                                                                                                                                     |                   |
| 3   | The following safeguards should be applied in addition to those of MT2.2:                                                                                                                                                                                               |                   |
|     | •<br>Use simple visual security features on the transponder (e.g. holograms).                                                                                                                                                                                           |                   |

| Table 8–37 | Protection of the transponder against cloning |
|------------|-----------------------------------------------|
|            |                                               |

<span id="page-100-0"></span>

| MT3     | Code and name of safeguard                                                                                                                                                                                                          | Threats addressed |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|         | Protection against emulation                                                                                                                                                                                                        | TT4               |
| General | The functions of a transponder and an entitlement can theoretically be emulated<br>by programmable devices (e.g. PDAs) that use contactless interfaces.                                                                             |                   |
|         | Emulation requires that the full function of the transponder, including the UID,<br>can be copied.                                                                                                                                  |                   |
|         | It is impossible to emulate a simple memory chip using programmable contact<br>less chips, since chips whose UIDs can be programmed after manufacture are<br>not currently available on the market.                                 |                   |
|         | EPCglobal specifications do not yet include cryptographic emulation protection<br>for transponders. Non-standard safeguards could be applied to a limited extent.                                                                   |                   |
| 1       | Simple emulation protection using UID                                                                                                                                                                                               |                   |
| 2       | •<br>Implementation of safeguards from MT2.1                                                                                                                                                                                        |                   |
|         | Advanced emulation protection                                                                                                                                                                                                       |                   |
| 3       | •<br>Use the access-protected, optional memory area in available EPC trans<br>ponders to implement simple cryptographic safeguards (encryption using<br>derived keys based on the UID, application of electronic signatures, etc.). |                   |

| Table 8–38 | Protection of the transponder against emulation |
|------------|-------------------------------------------------|
|            |                                                 |

| MT4     | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                   | Threats addressed |  |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|         | Protection against removal of transponder                                                                                                                                                                                                                                                                                                                                    | TT5               |  |
| General | Depending on the application scenario, the transponder is more or less perma<br>nently attached to the object. Good protection against removing the transponder<br>is necessary, especially where there is a risk of product counterfeiting and rela<br>belling.                                                                                                             |                   |  |
| 1       | Low-level protection:<br>•<br>The transponder is hung on (e.g. on clothing) or placed loose in the packag<br>ing.<br>•<br>The transponder is made into a label and attached using a particularly<br>strong thread or wire.                                                                                                                                                   |                   |  |
| 2       | Permanent attachment:<br>•<br>The transponder is stuck on                                                                                                                                                                                                                                                                                                                    |                   |  |
| 3       | Specially safeguarded attachment:<br>•<br>The transponder is permanently integrated into the product. Removing the<br>transponder is impossible without damaging the transponder or the product.<br>For example:<br>•<br>Transponder integrated into a device casing;<br>•<br>Transponder sewn into a piece of clothing;<br>•<br>Transponder stuck on as described in MT2.3. |                   |  |

#### **Table 8–39 Protection of the transponder against removal**

<span id="page-101-0"></span>

| MT5     | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                                                                 | Threats addressed |  |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|         | Protection against unauthorised attachment of<br>a transponder                                                                                                                                                                                                                                                                                                                                                                             | TT6               |  |
| General | The unauthorised attachment of a transponder in conjunction with the removal<br>or deactivation of the original transponder can represent a threat.                                                                                                                                                                                                                                                                                        |                   |  |
| 1       | Low-level protection:<br>•<br>The original transponder is connected to the object as described in MT4.1.<br>•<br>The object is inspected visually to see whether more than one transponder<br>is attached to it.                                                                                                                                                                                                                           |                   |  |
| 2       | Simple protection:<br>•<br>The original transponder is as described in MT2.2.<br>•<br>The original transponder is connected to the object as described in MT4.2.<br>•<br>The object is inspected visually to see whether more than one transponder<br>is attached to it.                                                                                                                                                                   |                   |  |
| 3       | High-level protection:<br>•<br>The original transponder is as described in MT2.3.<br>•<br>The original transponder is connected to the object as described in MT4.3.<br>•<br>The object is inspected visually to see whether more than one transponder<br>is attached to it. If the original transponder is integrated into the product,<br>then what has to be looked out for is an additional transponder that is stuck<br>or tagged on. |                   |  |

| Table 8–40 | Protection of the transponder against unauthorised attachment |
|------------|---------------------------------------------------------------|
|            |                                                               |

| MT6     | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                             | Threats addressed |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|         | Protection against the unauthorised deactiva<br>tion of a transponder                                                                                                                                                                                                                                                                                                                                                                                                  | TT7               |
| General | According to the latest specifications, EPC chips are protected against the unau<br>thorised activation of the kill command by 32-bit passwords. These passwords<br>are transmitted in unprotected form between terminal and transponder. Ad<br>vanced safeguards are only possible using proprietary solutions. For this rea<br>son, EPCglobal reference implementation for all protection demand categories<br>can only currently be done using the safeguard below. |                   |
| 1       | Password protection for the kill command:                                                                                                                                                                                                                                                                                                                                                                                                                              |                   |
| 2       | •<br>Implementing password protection in accordance with EPCglobal.                                                                                                                                                                                                                                                                                                                                                                                                    |                   |
|         | •<br>Diversification of the kill password.                                                                                                                                                                                                                                                                                                                                                                                                                             |                   |
|         | •<br>Apply key management safeguards MK1, MK3, MK4, MK5, MK6, MK7,<br>MK8, MK9 in the appropriate protection demand categories.                                                                                                                                                                                                                                                                                                                                        |                   |
| 3       | •<br>Infrastructural, personnel-related and organisational safeguards such as:                                                                                                                                                                                                                                                                                                                                                                                         |                   |
|         | •<br>forbidding the use of RFID readers on the business premises in the op<br>erator's terms and conditions of business;                                                                                                                                                                                                                                                                                                                                               |                   |
|         | •<br>checking business premises for readers installed without permission.                                                                                                                                                                                                                                                                                                                                                                                              |                   |

<span id="page-102-0"></span>

| MT7     | Code and name of safeguard                                                                                                                                                                                                                                                                                                                             | Threats addressed |  |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|         | Protection against DoS attacks on the trans<br>ponder                                                                                                                                                                                                                                                                                                  | TT8, TT11         |  |
| General | DoS attacks can take various forms:<br>•<br>Mechanical destruction of the antenna or chip.<br>•<br>Electrical destruction by means of strong RF fields.<br>•<br>Disruption of communication between transponder and reader.<br>•<br>Disruption of backend systems, key management, etc.                                                                |                   |  |
| 1       | Basic protection against DoS attacks on the transponder:<br>•<br>Implementation of safeguards from MT8.1.<br>•<br>EMC and mechanical testing of transponder.<br>•<br>Definition of fallback processes.                                                                                                                                                 |                   |  |
| 2       | Additional protection against DoS attacks on the transponder:<br>The following safeguards should be applied in addition to those of MT7.1:<br>•<br>Implementation of safeguards from MT8.2.<br>•<br>Use of transponders that make mechanical destruction more difficult (e.g.<br>chip position not visible).<br>•<br>Definition of fallback processes. |                   |  |
| 3       | Advanced protection against DoS attacks on the transponder:<br>•<br>Implementation of safeguards from MT8.3.<br>•<br>Transponder integrated into the product.<br>•<br>Definition of fallback processes.                                                                                                                                                |                   |  |

#### **Table 8–42 Protection of the transponder against DoS attacks**

| MT8     | Code and name of safeguard                                                                                                                                                                               | Threats addressed |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|         | Specifications defining transponder character<br>istics                                                                                                                                                  | TT8, TT9          |
|         | The characteristics of the transponder in relation to the application scenarios<br>and operating processes that are to be supported must be specified and guaran<br>teed. This applies in particular to: |                   |
| General | •<br>Performance                                                                                                                                                                                         |                   |
|         | •<br>Durability under mechanical wear                                                                                                                                                                    |                   |
|         | •<br>Protection against DoS attacks                                                                                                                                                                      |                   |
| 1       | Manufacturer's declaration                                                                                                                                                                               |                   |
|         | The manufacturer guarantees that the specifications are adhered to.                                                                                                                                      |                   |
| 2       | Tests and declaration of conformity:                                                                                                                                                                     |                   |
|         | •<br>Testing regulations are drawn up and tests performed.                                                                                                                                               |                   |
|         | •<br>Establish an approval procedure.                                                                                                                                                                    |                   |

<span id="page-103-0"></span>

| MT8 | Code and name of safeguard                                      | Threats addressed |
|-----|-----------------------------------------------------------------|-------------------|
|     | Specifications defining transponder character<br>istics         | TT8, TT9          |
| 3   | Interoperability tests according to test concept, evaluation:   |                   |
|     | Draw up testing regulations.<br>•                               |                   |
|     | Establish an approval procedure.<br>•                           |                   |
|     | •<br>Transponder evaluated by independent test laboratories.    |                   |
|     | •<br>Certification of components by an independent institution. |                   |

| Table 8–43 | Protection of the transponder by defining characteristics |  |
|------------|-----------------------------------------------------------|--|
|            |                                                           |  |

| MT9     | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Threats addressed |  |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|         | Fallback solution for transponder malfunction                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | TT11              |  |
| General | In the event of a malfunction, electronic safeguards in the transponder cannot<br>take effect in an emergency, since the retrieval of the chip data can no longer be<br>guaranteed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                   |  |
| 1       | Introduction of appropriate fallback solutions:<br>•<br>Specification and implementation of specific operative fallback processes<br>that can be employed in the event of defective transponders and reading<br>difficulties. Examples of these are:<br>•<br>The use of bar code or plain text information as a fallback solution.<br>•<br>The use of stored logistical data to compensate for reading errors.<br>•<br>Fallback solutions must be specified in the contractual arrangements be<br>tween the entities, and their consequences taken into account.<br>•<br>The capacity of the fallback solution must be sufficient to prevent a DoS at<br>tack consisting of overloading the fallback solution. |                   |  |
| 2       | Visual security features:<br>•<br>In addition to MT9.1, visual security features should be used to check the<br>authenticity of a transponder in the event of a defective chip.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                   |  |
| 3       | Implementation according to fallback concept:<br>In addition to MT9.1, 2:<br>•<br>A system concept must be developed that explicitly defines the fallback so<br>lutions and availability periods.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                   |  |

#### **Table 8–44 Protection through fallback solution for transponder malfunction**

| MT10    | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Threats addressed |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|         | Preventing the generation of movement profiles                                                                                                                                                                                                                                                                                                                                                                                                                                                   | TT10              |
| General | According to current specifications, EPC chips can include a command (the kill<br>command) which irreversibly deactivates the chip. For this reason, the safe<br>guard below is currently stipulated by EPCglobal in reference implementations<br>for all protection demand categories. Other proprietary methods are conceiv<br>able, these being similarly suitable for preventing the generation of movement<br>profiles. These, however, have not yet been specified by EPCglobal and imple- |                   |

<span id="page-104-0"></span>

| MT10 | Code and name of safeguard                                                  | Threats addressed |
|------|-----------------------------------------------------------------------------|-------------------|
|      | Preventing the generation of movement profiles                              | TT10              |
|      | mented in the EPC chips.                                                    |                   |
| 1    | Preventing retrieval of data from the transponder                           |                   |
| 2    | •<br>Deactivate the transponder using the kill command when the tagged prod |                   |
| 3    | uct is sold, or use a similarly secure technical method.                    |                   |

| MT11    | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                 | Threats addressed |  |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|         | Preventing the assignment of movement pro<br>files to people                                                                                                                                                                                                                                                                                                                               | TT10              |  |
| General | The tracking of a transponder after it has been given to the customer is only to<br>be considered a threat if the movement profile can be linked to a particular per<br>son. It should be noted that from a large volume of anonymous movement data<br>that has been suitably aggregated, data can be generated that can be, or in<br>some cases already is, related to particular people. |                   |  |
| 1       | Guaranteed anonymity of sale:<br>•<br>Anonymous sale and handing-over of the product to the customer (anony<br>mous payment procedure, no use of discount or customer cards, no product<br>delivery).<br>•<br>General ban on linking products and personal data in retailers' IT systems.<br>This also applies when customer cards are used.                                               |                   |  |
|         | Certification:                                                                                                                                                                                                                                                                                                                                                                             |                   |  |
| 2       | •<br>Implementation of safeguards from MT11.1. The implementation of these<br>safeguards is also checked and certified by an independent authority.                                                                                                                                                                                                                                        |                   |  |
| 3       | Preventing the generation of movement profiles                                                                                                                                                                                                                                                                                                                                             |                   |  |
|         | •<br>Sufficient protective safeguards cannot be suggested for protection demand<br>category 3. In such cases MT10.3 should be used to prevent the generation<br>of movement profiles.                                                                                                                                                                                                      |                   |  |

#### **Table 8–45 Protection by preventing of movement profile generation**

**Table 8–46 Protection by preventing the assignment of movement profile to people** 

#### **8.4.3 Safeguards relating to the readers**

| MR1 | Code and name of safeguard                                                                                                                                     | Threats addressed |  |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|     | Introduction of interface tests and approval<br>procedures                                                                                                     | TC1               |  |
|     | Interface test                                                                                                                                                 |                   |  |
| 1   | •<br>Apply existing test regulations for contactless interfaces in terminals as de<br>fined by ISO/IEC18000-6 Rev1.2.                                          |                   |  |
|     | •<br>Draw up and apply specific test regulations for the application-specific func<br>tions of the reader interface, e.g. those of the European EPC Competence |                   |  |

<span id="page-105-0"></span>

| MR1 | Code and name of safeguard                                                                         | Threats addressed |
|-----|----------------------------------------------------------------------------------------------------|-------------------|
|     | Introduction of interface tests and approval<br>procedures                                         | TC1               |
|     | Center (EECC).                                                                                     |                   |
| 2   | Component approval                                                                                 |                   |
|     | See above, additional component approval (transponders, readers, key man<br>agement).              |                   |
| 3   | Certification                                                                                      |                   |
|     | See above, additional certification of transponders and readers by an independ<br>ent institution. |                   |

| Table 8–47<br>Protection of readers through introduction of interface tests |
|-----------------------------------------------------------------------------|
|-----------------------------------------------------------------------------|

| MR2     | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Threats addressed |  |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|         | Protection of reference information against<br>retrieval, data errors and manipulation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | TR1, TR2          |  |
| General | Reference information is needed for processes such as counterfeit monitoring,<br>access protection, and initialising and executing the kill command. Reference<br>information includes:<br>•<br>Identifiers (ID)<br>•<br>Key<br>•<br>Blacklists and whitelists<br>•<br>Algorithms for evaluation<br>Reference information and usage data can differ depending on the application<br>scenario.                                                                                                                                                                                               |                   |  |
| 1       | Checksum and physical protection:<br>•<br>Appropriate physical access protection for the devices (e.g. encapsulated<br>casing, mechanical separation of LAN cables).<br>•<br>Use checksums for data transfer to avoid transmission errors – does not<br>protect against manipulation, since checksums can be calculated automati<br>cally by almost any software and do not rely on secrets.<br>•<br>Save cryptographic keys and algorithms in a SAM or in a protected area of<br>the software.<br>•<br>Introduce access protection for the reader's data and administration func<br>tions. |                   |  |
| 2       | Authentication, secure transmission:<br>•<br>Mechanisms for detecting data manipulation in the device, such as MAC<br>secured saving (if performance permits).<br>•<br>Data should only be transferred from backend systems into the reader after<br>mutual authentication, or at least one-sided authentication of the source<br>transmitting to the reader.<br>•<br>Scenario-specific separation of algorithms, reference data, usage data and<br>keys.                                                                                                                                   |                   |  |

<span id="page-106-0"></span>

| MR2 | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Threats addressed |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|     | Protection of reference information against<br>retrieval, data errors and manipulation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | TR1, TR2          |
|     | •<br>Save keys in a SAM or in a protected area of the software.<br>•<br>Introduce scenario-specific access protection for the reader's data and ad<br>ministration functions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                   |
| 3   | Advanced protection<br>•<br>Mechanisms for detecting data manipulation in the device, such as MAC<br>secured saving (if performance permits).<br>•<br>Data should only be transferred from backend systems into the reader after<br>mutual authentication between the reader and the source with which it is<br>communicating.<br>•<br>Scenario-specific separation of algorithms, reference data, usage data and<br>keys.<br>•<br>Save the keys in application-specific SAMs.<br>•<br>Save and execute cryptographic algorithms in specific SAMs.<br>•<br>Introduce multi-tenant, specific access protection for the reader's data and<br>administrative functions in accordance with the role model. |                   |

| Table 8–48 | Protection of readers through protection of reference information |
|------------|-------------------------------------------------------------------|
|            |                                                                   |

| MR3     | Code and name of safeguard                                                                                                                                                                                                                                | Threats addressed |  |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|         | Protection of the reader against malfunction                                                                                                                                                                                                              | TR3               |  |
|         | The general safeguards are:                                                                                                                                                                                                                               |                   |  |
| General | •<br>Draw up specifications describing the characteristics of the reader in terms<br>of performance, availability, procedural management and function.                                                                                                    |                   |  |
|         | •<br>Draw up test specifications.                                                                                                                                                                                                                         |                   |  |
|         | •<br>Offline capability wherever a data network connection is not guaranteed.                                                                                                                                                                             |                   |  |
|         | •<br>It must be possible to store reference data and usage data locally. Ca<br>pacity must be designed to suit the scenario in which it will be used.                                                                                                     |                   |  |
|         | •<br>Introduce uninterruptible power supply (UPS) wherever an external power<br>supply is not guaranteed.                                                                                                                                                 |                   |  |
|         | •<br>The UPS must at least be capable of bridging a specific period of time.                                                                                                                                                                              |                   |  |
|         | Execution as per specifications:                                                                                                                                                                                                                          |                   |  |
| 1       | •<br>Design the system characteristics in accordance with the specifications,<br>with particular regard to performance, availability, procedural management<br>and function (this requires the availability of sufficiently detailed specifica<br>tions). |                   |  |
|         | •<br>Simple integrity security for system software to detect manipulation of soft<br>ware modules (e.g. of entitlement test).                                                                                                                             |                   |  |
|         | •<br>Physical protection of devices (e.g. encapsulated casing, mechanical sepa<br>ration of LAN cables).                                                                                                                                                  |                   |  |
|         | •<br>Simple access protection in the form of passwords and IDs in readers for<br>sensitive tasks such as loading new software versions.                                                                                                                   |                   |  |
|         | •<br>Specification and implementation of a process for supporting new entitle-                                                                                                                                                                            |                   |  |

<span id="page-107-0"></span>

| MR3 | Code and name of safeguard                                                                                                                                                                                           | Threats addressed |  |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|     | Protection of the reader against malfunction                                                                                                                                                                         | TR3               |  |
|     | ments and carrier media.                                                                                                                                                                                             |                   |  |
|     | Proof of execution:                                                                                                                                                                                                  |                   |  |
|     | •<br>Integrity security for system software to detect manipulation of software<br>modules (e.g. of entitlement test).                                                                                                |                   |  |
|     | •<br>Physical protection of devices (e.g. encapsulated casing, mechanical sepa<br>ration of LAN cables).                                                                                                             |                   |  |
| 2   | •<br>Access protection in the form of passwords and IDs in readers for sensitive<br>tasks such as loading new software versions.                                                                                     |                   |  |
|     | •<br>Specification and implementation of a process for supporting new trans<br>ponders, applications and data formats.                                                                                               |                   |  |
|     | •<br>Document the correct implementation of the specifications defining per<br>formance, availability, procedural management and function, using tests<br>that provoke specific malfunctions and operational errors. |                   |  |
|     | Evaluation:                                                                                                                                                                                                          |                   |  |
|     | •<br>Agree on service levels and ensure support in the event of failure so as to<br>limit the effects of malfunctions.                                                                                               |                   |  |
|     | •<br>Integrity security for system software to detect manipulation of software<br>modules (e.g. of entitlement test); signatures or MACs with appropriate<br>mechanism strength and key length.                      |                   |  |
| 3   | •<br>Physical protection of devices (e.g. encapsulated casing, mechanical sepa<br>ration of LAN cables).                                                                                                             |                   |  |
|     | •<br>Access to the terminal's administration functions, such as software updates,<br>only after authentication of the source of the request.                                                                         |                   |  |
|     | •<br>Specification and implementation of a process for supporting new trans<br>ponders, applications and data formats.                                                                                               |                   |  |
|     | •<br>Have independent test laboratories evaluate and certify system software<br>and hardware according to defined criteria.                                                                                          |                   |  |

**Table 8–49 Protection of the reader against malfunction** 

Other safeguards relating to the readers are described in section [0](#page-90-1).

#### **8.4.4 Safeguards relating to the key management system**

| MK1     | Code and name of safeguard                                                                                                                                                                       | Threats addressed |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|         | Secure generation and import of keys                                                                                                                                                             | TK1               |
| General | Specification of the necessary keys and key attributes in relation to transpond<br>ers and the specific application scenarios being supported, taking into account<br>the applicable role model. |                   |
| 1       | Keys generated according to specification                                                                                                                                                        |                   |
|         | •<br>Use a suitable key generator as defined in [GSHB].                                                                                                                                          |                   |

<span id="page-108-0"></span>

| MK1 | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Threats addressed |  |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|     | Secure generation and import of keys                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | TK1               |  |
|     | •<br>All keys are to be generated in a secure environment, stored under crypto<br>graphic protection, and – apart from defined exceptions involving special<br>additional protective measures – loaded onto the transponder in a secure<br>environment.<br>•<br>Specific keys are to be generated with defined attributes in accordance with<br>the specifications.<br>•<br>Develop and use procedures for the secure transport of keys to their place<br>of use. The role model should be observed.<br>•<br>Develop and use procedures for the secure use of keys at their place of<br>use. |                   |  |
|     | Evaluation by a testing laboratory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                   |  |
|     | •<br>Use a suitable key generator as defined in [GSHB].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                   |  |
|     | •<br>All keys are to be generated in a secure environment, stored under crypto<br>graphic protection, and – apart from defined exceptions involving special<br>additional protective measures – loaded onto the transponder in a secure<br>environment.                                                                                                                                                                                                                                                                                                                                      |                   |  |
|     | •<br>Specific keys are to be generated with defined attributes in accordance with<br>the specifications.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                   |  |
| 2   | •<br>Support the diversification of keys for the application with carrier media, and<br>the information stored there (specification, implementation, testing and pro<br>vision of specific algorithms).                                                                                                                                                                                                                                                                                                                                                                                      |                   |  |
|     | •<br>Import the keys to specific SAMs:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                   |  |
|     | •<br>SAMs are based on secure chip hardware in accordance with CC<br>EAL5+.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                   |  |
|     | •<br>Data cannot be retrieved from SAMs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                   |  |
|     | •<br>Authentication is required to activate a SAM.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                   |  |
|     | The quality of the key generator should be confirmed by an independent testing<br>laboratory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                   |  |
|     | Evaluate and certify in accordance with CC or a process of the same standard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                   |  |
|     | •<br>Use a suitable key generator as defined in [GSHB].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                   |  |
| 3   | •<br>All keys are to be generated in a secure environment, stored under crypto<br>graphic protection, and loaded onto the transponder in a secure environ<br>ment.                                                                                                                                                                                                                                                                                                                                                                                                                           |                   |  |
|     | •<br>Specific keys are to be generated with defined attributes in accordance with<br>the specifications.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                   |  |
|     | •<br>Support the diversification of keys for the application with carrier media, and<br>the information stored there (specification, implementation, testing and pro<br>vision of specific algorithms).                                                                                                                                                                                                                                                                                                                                                                                      |                   |  |
|     | •<br>Import the keys to specific SAMs:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                   |  |
|     | •<br>SAMs are based on secure chip hardware in accordance with CC<br>EAL5+.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                   |  |
|     | •<br>Data cannot be retrieved from SAMs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                   |  |
|     | •<br>Authentication is required to activate a SAM.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                   |  |

| MK1 | Code and name of safeguard                                                                                                                 | Threats addressed |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|     | Secure generation and import of keys                                                                                                       | TK1               |
|     | All of the requirements must be evaluated and certified in accordance with CC,<br>EAL4 mechanism strength high, or a comparable procedure. |                   |

#### **Table 8–50 Protection through secure generation and import of keys**

| MK2     | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                    | Threats addressed |  |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|         | Introduction of key management for symmetric<br>and asymmetric keys with sufficient key length                                                                                                                                                                                                                                                                                                | All TKs           |  |
|         | A key management system is defined by the following parameters:                                                                                                                                                                                                                                                                                                                               |                   |  |
|         | •<br>Key length                                                                                                                                                                                                                                                                                                                                                                               |                   |  |
|         | •<br>Algorithm used                                                                                                                                                                                                                                                                                                                                                                           |                   |  |
| General | •<br>Key storage (see also MK7)                                                                                                                                                                                                                                                                                                                                                               |                   |  |
|         | •<br>Generation of keys (see MK1)                                                                                                                                                                                                                                                                                                                                                             |                   |  |
|         | •<br>Key distribution                                                                                                                                                                                                                                                                                                                                                                         |                   |  |
|         | •<br>Identification of keys                                                                                                                                                                                                                                                                                                                                                                   |                   |  |
|         | •<br>Technical and organisational intermeshing of safeguards                                                                                                                                                                                                                                                                                                                                  |                   |  |
|         | Key management concept and implementation                                                                                                                                                                                                                                                                                                                                                     |                   |  |
|         | •<br>Keys are given unique IDs.                                                                                                                                                                                                                                                                                                                                                               |                   |  |
|         | •<br>The purpose of the key and the entity to which it belongs is uniquely identi<br>fied.                                                                                                                                                                                                                                                                                                    |                   |  |
|         | •<br>Algorithms for generating keys are to be selected in accordance with<br>[ALGK_BSI].                                                                                                                                                                                                                                                                                                      |                   |  |
|         | •<br>Static keys can only be used in bordered-off, clearly manageable areas<br>where it is easy for the main components to exchange keys, and where the<br>number of transponders no longer usable after the exchange is low.                                                                                                                                                                 |                   |  |
|         | •<br>We therefore recommend the use of derived keys and unique identification<br>numbers (e.g. UID and a master key). This generates unique keys for each<br>component.                                                                                                                                                                                                                       |                   |  |
| 1       | •<br>The key length used is chosen and specified separately for each function.<br>[ALGK_BSI] should generally be applied.                                                                                                                                                                                                                                                                     |                   |  |
|         | •<br>Keys in readers should always be stored in encapsulated security modules<br>(SAMs). This applies especially to terminals with offline capability. Keys in<br>backend systems should also preferably be stored in security modules such<br>as SAMs.                                                                                                                                       |                   |  |
|         | •<br>Keys can be distributed in two ways:                                                                                                                                                                                                                                                                                                                                                     |                   |  |
|         | a<br>personalisation of keys in carrier media and components in a secure<br>environment, and                                                                                                                                                                                                                                                                                                  |                   |  |
|         | b<br>reloading keys (see MK8 – reloading process)                                                                                                                                                                                                                                                                                                                                             |                   |  |
|         | •<br>The key management system is designed by the system manager. The enti<br>ties involved apply a key management concept. This includes nominating<br>people responsible for key management who ensure that it is performed<br>correctly, and who keep abreast of the latest cryptographic developments<br>so as to be able to counteract threats to the system as a whole in good<br>time. |                   |  |

<span id="page-110-0"></span>

| MK2 | Code and name of safeguard                                                                                                                                                                                                                                                | Threats addressed |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|     | Introduction of key management for symmetric<br>and asymmetric keys with sufficient key length                                                                                                                                                                            | All TKs           |
|     | Key management concept and implementation (higher-level method)                                                                                                                                                                                                           |                   |
| 2   | In addition to the points defined in 1, the following is usually done in level 2:                                                                                                                                                                                         |                   |
|     | •<br>As well as generating unique keys for each component, communication<br>session keys can also be negotiated that are made dynamic on the basis of<br>adjustable data (e.g. random numbers). This effectively prevents messages<br>from being eavesdropped or re-sent. |                   |
|     | Secure, flexible key management concept                                                                                                                                                                                                                                   |                   |
| 3   | In level 3 the following may be useful in addition to the points defined in 1 and 2:                                                                                                                                                                                      |                   |
|     | •<br>A complex asymmetric key management process is used, with a root CA,<br>multiple sub-CAs and certified authentication and encryption keys.                                                                                                                           |                   |
|     | •<br>The lengths of the asymmetric keys should generally accord with<br>[ALGK_BSI] (preferential) and [TR_ECARD].                                                                                                                                                         |                   |
|     | The type and strength of the mechanism used for reloading should be adapted<br>to future developments in accordance with [ALGK_BSI].                                                                                                                                      |                   |

| Table 8–51 | Protection through introduction of key management |
|------------|---------------------------------------------------|
|------------|---------------------------------------------------|

| MK3     | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                      | Threats addressed |  |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|         | Access protection for cryptographic keys (read<br>and write access)                                                                                                                                                                                                                                                                                                                                                                                             | TK2, TK3          |  |
| General | Specification of the requirements regarding access protection for all the places<br>where keys are used, taking into account the applicable role model.                                                                                                                                                                                                                                                                                                         |                   |  |
| 1       | Manufacturer's declaration:<br>•<br>Keys and passwords on the transponders are protected against retrieval<br>and manipulation attacks.<br>•<br>Once stored in a SAM or other secure memory for keys in system compo<br>nents, a key becomes irrevocably irretrievable using software.<br>•<br>New keys are loaded into SAMs, terminals or other system components in<br>accordance with MK8.<br>Access protection is certified by manufacturer's declarations. |                   |  |
| 2       | Evaluation by a testing laboratory:<br>•<br>Keys and passwords on the carrier media are protected against retrieval<br>and manipulation attacks.<br>•<br>Once stored in a SAM or other secure memory for keys in system compo<br>nents, a key becomes irrevocably irretrievable using software.<br>•<br>New keys are loaded into SAMs in accordance with MK8.<br>Access protection is certified by test reports from independent testing laborato<br>ries.      |                   |  |
| 3       | Evaluate and certify in accordance with CC or a process of the same standard:                                                                                                                                                                                                                                                                                                                                                                                   |                   |  |

<span id="page-111-0"></span>

| MK3 | Code and name of safeguard                                                                                                                                                       | Threats addressed |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|     | Access protection for cryptographic keys (read<br>and write access)                                                                                                              | TK2, TK3          |
|     | •<br>Keys and passwords on the carrier media are protected against retrieval<br>and manipulation attacks.                                                                        |                   |
|     | •<br>Once stored in a SAM or other secure memory for keys in system compo<br>nents, a key becomes irrevocably irretrievable using software.                                      |                   |
|     | •<br>New keys are loaded into SAMs in accordance with MK8.                                                                                                                       |                   |
|     | Access protection is certified by test reports from independent testing laborato<br>ries. Hardware is certified in accordance with CC EAL5+ for carrier media, keys<br>and SAMs. |                   |

| Table 8–52 | Protection through access protection for cryptographic keys |
|------------|-------------------------------------------------------------|
|            |                                                             |

| MK4     | Code and name of safeguard                                                                                                                                                                                                                                | Threats addressed |  |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|         | Securing the function of security components                                                                                                                                                                                                              | TK4               |  |
| General | Components used for saving and processing keys – referred to in the following<br>as security components – must be checked to ensure they are trustworthy.<br>There are various safeguards available for this purpose, depending on the level<br>involved. |                   |  |
| 1       | Manufacturer's declarations                                                                                                                                                                                                                               |                   |  |
|         | •<br>Guarantee safety in accordance with specifications, by means of manufac<br>turer's internal quality assurance.                                                                                                                                       |                   |  |
| 2       | Testing in accordance with test specifications:                                                                                                                                                                                                           |                   |  |
|         | •<br>Draw up test specifications for each security component.                                                                                                                                                                                             |                   |  |
|         | •<br>Technical checking of components in accordance with the relevant test<br>specifications.                                                                                                                                                             |                   |  |
|         | •<br>Specification and execution of integration tests in test and actual environ<br>ments.                                                                                                                                                                |                   |  |
| 3       | Evaluation:                                                                                                                                                                                                                                               |                   |  |
|         | See 2, furthermore:                                                                                                                                                                                                                                       |                   |  |
|         | •<br>Security components are tested by independent test laboratories.<br>•<br>An independent institute certifies the relevant security components.<br>•<br>An approval process is established for the security components.                                |                   |  |

**Table 8–53 Protection through securing the function of security components** 

| MK5 | Code and name of safeguard                                    | Threats addressed |
|-----|---------------------------------------------------------------|-------------------|
|     | Availability of key management system (fall<br>back solution) | TK4, TK5          |
| 1   | Offline capability and secure backup                          |                   |

<span id="page-112-0"></span>

| MK5 | Code and name of safeguard                                                                                                                                                                                                      | Threats addressed |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|     | Availability of key management system (fall<br>back solution)                                                                                                                                                                   | TK4, TK5          |
| 2   | •<br>Keys must in principle (at least temporarily) be available autonomously<br>without a backend system or if system interfaces fail.                                                                                          |                   |
|     | •<br>System-wide keys must be stored in at least two spatially separate places<br>(original and backup), and in secure environments.7                                                                                           |                   |
|     | •<br>It must be ensured that the backup copy fulfils the same security require<br>ments as the original.                                                                                                                        |                   |
|     | •<br>The replacement of defective key components must be regulated.                                                                                                                                                             |                   |
| 3   | Implementation according to fallback concept and backup of keys in the Trust<br>Centre                                                                                                                                          |                   |
|     | See 1, furthermore:                                                                                                                                                                                                             |                   |
|     | •<br>A system concept must be drawn up which explicitly defines the availability<br>and fallback solutions together with availability periods, as well as agree<br>ments between the entities.                                  |                   |
|     | •<br>Critical components must have an uninterruptible power supply (UPS) and<br>other security mechanisms (such as a RAID), so that the failure of sub<br>components does not impair the availability of the system as a whole. |                   |
|     | •<br>A sufficient number of replacement system components must be kept avail<br>able (in cold or warm standby) so as to ensure the required level of avail<br>ability.                                                          |                   |
|     | •<br>The Trust Centre must back up the system-wide keys.                                                                                                                                                                        |                   |

| Table 8–54 | Protection through availability of a key management system |
|------------|------------------------------------------------------------|
|------------|------------------------------------------------------------|

| MK6                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Code and name of safeguard                                                                                        | Threats addressed      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|------------------------|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Definition of action in the event of keys being<br>compromised                                                    | TK5, general procedure |
| General                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | This safeguard is to be treated independently from any safeguards used to pre<br>vent compromises from occurring. |                        |
| 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Compromise of diversified keys:                                                                                   |                        |
| 2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | The transponder concerned is withdrawn or deactivated. No other safeguards<br>required.                           |                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Compromise of non-diversified keys:                                                                               |                        |
| If the keys or security modules are altogether compromised and an emergency<br>version of the keys is not available, then the keys in the security modules and in<br>3<br>new transponders must be replaced immediately with new keys. The data in the<br>system cannot be considered trustworthy until all the keys have been replaced.<br>Particularly if there is a danger of product counterfeiting, fallback solutions must<br>be implemented which would reveal activities such as the unauthorised deacti<br>vation of transponders: |                                                                                                                   |                        |

<span id="page-112-1"></span><sup>7</sup> System-wide keys means all symmetric keys, as well as asymmetric keys not specific to particular cards.

<span id="page-113-0"></span>

| MK6 | Code and name of safeguard                                                                                                                                                       | Threats addressed      |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
|     | Definition of action in the event of keys being<br>compromised                                                                                                                   | TK5, general procedure |
|     | •<br>No use of self-checkout.<br>•<br>In the case of products that are liable to counterfeiting, sales personnel<br>visually monitor the transponders' visual security features. |                        |

#### **Table 8–55 Protection through definition of actions when keys are compromised**

| MK7 | Code and name of safeguard                                                                                         | Threats addressed |
|-----|--------------------------------------------------------------------------------------------------------------------|-------------------|
|     | Client-specific separation of keys                                                                                 | TK2, TK3          |
| 1   | Separate storage and handling of keys                                                                              |                   |
| 2   | •<br>Keys originating from different key generators in all of the components of                                    |                   |
| 3   | the system must be separated from one another in order to prevent mal<br>functions and the misuse of key material. |                   |

| Table 8–56 | Protection through client-specific separation of keys |
|------------|-------------------------------------------------------|
|            |                                                       |

| MK8     |                                                                                                                                                                                                                                                                            | Code and name of safeguard                                                                                                                                                                                              | Threats addressed |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|         |                                                                                                                                                                                                                                                                            | Loading new keys – securing the authenticity<br>and integrity of entitlements                                                                                                                                           | TK3               |
| General | Keys should be associated clearly with an application scenario, and they should<br>be imported into the transponder from the SAM during initialisation. An autono<br>mous process for loading new keys is especially relevant for SAMs and is ad<br>visable at all levels. |                                                                                                                                                                                                                         |                   |
| 1       | Simple authentication concept                                                                                                                                                                                                                                              |                                                                                                                                                                                                                         |                   |
|         | 1                                                                                                                                                                                                                                                                          | Keys must each have a unique identifier containing information on the issu<br>ing organisation, a unique ID, and a version number.                                                                                      |                   |
| 2       | 2                                                                                                                                                                                                                                                                          | There should be ways of deleting or blocking keys that have been used up.                                                                                                                                               |                   |
|         | 3                                                                                                                                                                                                                                                                          | New keys are loaded from a key management system into the SAM by the<br>system manager or someone appointed by him; this requires an online con<br>nection.                                                             |                   |
|         | 4                                                                                                                                                                                                                                                                          | Keys must always be loaded under confidential conditions, for which a de<br>cryption key is required in the SAM.                                                                                                        |                   |
|         | 5                                                                                                                                                                                                                                                                          | A symmetric procedure is used for loading new keys, for which the key is<br>suer has a symmetric master key (KM_Storekey); derived from that, keys<br>that are particular to each card are stored in the SAMs (see II). |                   |
|         | Complex authentication concept                                                                                                                                                                                                                                             |                                                                                                                                                                                                                         |                   |
|         |                                                                                                                                                                                                                                                                            | I. Preliminary remarks                                                                                                                                                                                                  |                   |
| 3       | 1                                                                                                                                                                                                                                                                          | Keys must each have a unique identifier containing information on the issu<br>ing organisation, a unique ID, and a version number.                                                                                      |                   |
|         | 2                                                                                                                                                                                                                                                                          | There should be ways of deleting or blocking keys that have been used up.                                                                                                                                               |                   |
|         | 3                                                                                                                                                                                                                                                                          | New keys are loaded from a key management system into the SAM by the<br>system manager or someone appointed by him; this requires an online con<br>nection.                                                             |                   |

<span id="page-114-0"></span>

| MK8 |                                                                                                             | Code and name of safeguard                                                                                                                                                                                                                                                                               | Threats addressed |
|-----|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|     |                                                                                                             | Loading new keys – securing the authenticity<br>and integrity of entitlements                                                                                                                                                                                                                            | TK3               |
|     | 4<br>5                                                                                                      | Keys must always be loaded under confidential conditions, for which a de<br>cryption key is required in the SAM.<br>An asymmetric procedure is used for loading new keys into a SAM, for<br>which a PKI with a CA must be established with which to certify all asym<br>metric keys.                     |                   |
|     | II. General procedure                                                                                       |                                                                                                                                                                                                                                                                                                          |                   |
|     | New keys can be loaded using a procedure such as the following:                                             |                                                                                                                                                                                                                                                                                                          |                   |
|     | 1<br>The key issuer (or key management system) sends its public key certified<br>by the CA to the terminal. |                                                                                                                                                                                                                                                                                                          |                   |
|     | 2                                                                                                           | The SAM verifies the certificate (e.g. with Verify Certificate) and<br>stores the key issuer's public key temporarily.                                                                                                                                                                                   |                   |
|     | 3                                                                                                           | The key issuer encrypts the key that is to be loaded, as well as the other<br>information associated with it (key ID, key version, operating counter, …)<br>using the SAM's public encrypting key, signs the cryptogram using its own<br>private key, and sends the cryptogram and signature to the SAM. |                   |
|     | 4                                                                                                           | The SAM checks the signature using the key issuer's public signature key.<br>If that is successful it decrypts the cryptogram using its own private decryp<br>tion key and saves the key and additional information permanently.                                                                         |                   |

**Table 8–57 Protection through securing the authenticity and integrity when loading keys** 

#### **8.4.5 Safeguards relating to customer data systems**

Customer data systems are the only components in the system that may in certain cases use and store personal data. For that reason, special threats may affect them.

General safeguards that address threats to the customer data system are described in section [0.](#page-90-1) The following additional safeguards are stipulated which encourage in particular the secure and legally compliant handling of personal data.

| MV1     | Code and name of safeguard                                                                                                                                  | Threats addressed |  |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|         | Identifying the customer when selling and<br>handing over products                                                                                          | TV10              |  |
| General | The identity of the customer must be established when setting up a customer<br>account and when delivering or collecting products.                          |                   |  |
| 1       | Declaration by customer:                                                                                                                                    |                   |  |
|         | •<br>The customer submits the details of his or her identity verbally or on the<br>Internet.                                                                |                   |  |
| 2       | Application form when setting up a customer account and issuing a customer<br>card:                                                                         |                   |  |
|         | •<br>The customer identifies himself in writing and signs to confirm his identity.<br>The product retailer checks the information using conventional means: |                   |  |

<span id="page-115-0"></span>

| MV1 | Code and name of safeguard                                                                       | Threats addressed |
|-----|--------------------------------------------------------------------------------------------------|-------------------|
|     | Identifying the customer when selling and<br>handing over products                               | TV10              |
|     | •<br>Address check.<br>•<br>Sending a confirmation or the customer card to the address given.    |                   |
|     | Identity document check when setting up a customer account and issuing a cus<br>tomer card:      |                   |
| 3   | •<br>Secure photo ID is presented.                                                               |                   |
|     | •<br>The identity data is taken into the system from a secure electronic identity<br>card (eID). |                   |

**Table 8–58 Protection of personal data by identification of customers** 

| MV2                | Code and name of safeguard                                                                                                                                                                                                                                                                 | Threats addressed |  |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|                    | Satisfying the data minimisation obligation                                                                                                                                                                                                                                                | TV11              |  |
| General            | Data minimisation must be satisfied in accordance with the applicable legal<br>regulations on privacy.                                                                                                                                                                                     |                   |  |
| 1                  | Satisfying legal requirements:                                                                                                                                                                                                                                                             |                   |  |
| 2                  | •<br>When the processes and system within the overall system are being de<br>fined, the principle of data minimisation is applied in accordance with the le<br>gal foundations. This includes, in particular, the definition of deadlines for<br>deleting data that is no longer required. |                   |  |
| Special safeguards |                                                                                                                                                                                                                                                                                            |                   |  |
| 3                  | The following safeguards are applied in addition to those specified in MV2.2:                                                                                                                                                                                                              |                   |  |
|                    | •<br>Precise, purpose-related definition of the data content, the acquisition and<br>storage of data, and access and usage rights using the role model of the<br>overall system.                                                                                                           |                   |  |
|                    | •<br>The customer is informed about the purpose-related acquisition, storage<br>and use of personal data.                                                                                                                                                                                  |                   |  |

| Table 8–59 | Protection of personal data by data minimisation |
|------------|--------------------------------------------------|
|------------|--------------------------------------------------|

| MV3     | Code and name of safeguard                                                                                                                                                                      | Threats addressed |  |  |  |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|--|--|
|         | Separation of personal data and logistical data                                                                                                                                                 | TV12              |  |  |  |
| General | The allocation of personal customer data to information about the objects fitted<br>with transponders is only permitted with the express approval of the customer<br>and for a defined purpose. |                   |  |  |  |
| 1       | Implementing the separation of personal data and logistical data                                                                                                                                |                   |  |  |  |
| 2       |                                                                                                                                                                                                 |                   |  |  |  |
| 3       | Special safeguards                                                                                                                                                                              |                   |  |  |  |
|         | The following safeguards are applied in addition to those specified in MV3.2:                                                                                                                   |                   |  |  |  |
|         | •<br>The customer is informed about the content of the logistical data used, the                                                                                                                |                   |  |  |  |

<span id="page-116-0"></span>

| MV3 | Code and name of safeguard                                                                                                                                                                                                                                                                                                                     | Threats addressed |  |  |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|--|
|     | Separation of personal data and logistical data                                                                                                                                                                                                                                                                                                | TV12              |  |  |
|     | way in which it is linked to personal data, the purpose for which it is used,<br>and the length of time for which it will be stored and used.<br>•<br>The customer is informed about the purpose-related acquisition, storage,<br>duration of storage and use of personal data.<br>•<br>This implementation requires the customer's agreement. |                   |  |  |

#### **Table 8–60 Protection of personal data by separation of personal data and logistical data**

#### **8.4.6 Examples of non-standardised safeguards for systems compliant with EPCglobal**

#### **8.4.6.1 Examples of diversification and of safeguards for passwords**

Passwords are to be generated in relation to each product on the basis of a code which includes the UID and EPC. If required, the transponder's user memory can be protected permanently against overwriting. This prevents any subsequent changes to the user memory. The password can be stored again in encrypted form as an additional safeguard. Encryption takes place offline and the encrypted text is transferred to the memory. The kill command can only be executed if the encrypted text corresponds with the stored password in plain text. Conventional encryption methods (such as RSA, ECC) can be used for offline encryption. At the time this survey was compiled, a generic solution had not yet been approved and released. This procedure is described in more detail in section [8.4.6.2.](#page-116-1)

#### <span id="page-116-1"></span>**8.4.6.2 Example of how data is encrypted in the transponder's extended memory area**

As a security measure, the UID can be encrypted and stored in the memory as a signature, thus making it more difficult to copy or clone the user memory. Furthermore, the user memory containing data relating to manufacture can also be optionally stored in encrypted form. In addition, the complete user memory including the encrypted UID can be protected against unauthorised reading using a read-protection password. In a further stage of encryption, a new key (transaction counter) can be generated for each transaction and this key can be stored in encrypted form in the memory and in the database, which can help to counter unmonitored replication of the chip (user memory including UID). At each logistical stage (e.g. shipment preparation -> goods despatch), the transaction counter can be regenerated and stored in the tag memory and in the database. At the next logistical stage (e.g. goods received by retailer), this signature is compared with the database entry and checked. This makes it considerably more difficult to duplicate transponders that are to be used in a longer supply chain. All of these levels rely on the encryption taking place offline within the computer systems of the logistical unit involved. Conventional processes can be used for encryption (such as RSA, ECC), while striving to minimise the key length on account of the limited size of user memory in passive transponders.

<span id="page-117-0"></span>![](_page_117_Figure_1.jpeg)

**Figure 8–1 Example of how security-related information is encrypted** 

# <span id="page-118-0"></span>**9 Definition of specific application scenarios**

We will now examine the processes described in sections [6](#page-49-1) and [7](#page-60-1) to provide examples of how particular products can be implemented.

The aim is to analyse use cases that are important to the security and function of RFID transponders, and on that basis to lay down in the Technical Guidelines suggestions of how the overall system, and its associated operating processes, might be implemented technically.

The following products will be discussed in relation to the use of RFID transponders:

1 The "Fast-moving consumer goods" application scenario

The product is a consumer item which does not demand security against counterfeiting (such as toilet paper). The purpose of using RFID technology is to optimise logistical processes, provide quality assurance, manage stocks at the POS, and facilitate sales processes. Transponders can also be used to secure goods, although this case will not be discussed at this stage.

- 2 The "consumer electronics" application scenario The appliance (such as a flat-screen TV) needs to be protected against counterfeiting in order to protect the consumer. Product piracy is to be expected. Furthermore, RFID technology will be used for post-sales services such as proof of guarantee, proof of purchase, identification for product service (firmware updates and so on).
- 3 The "brand-name clothing" application scenario The product is a highly priced men's suit made by a well known brand. The aim is to protect it against counterfeiting. Product piracy is to be expected. Furthermore, RFID technology will be used for post-sales services such as proof of guarantee and proof of purchase.

It is technically possible to use the transponder as a safeguard against theft. However, the processes involved have not yet been standardised in EPCglobal. The following discussions will not cover the subject of theft protection, which will, however, be included in future updates or revisions to the Guidelines.

The following sections will describe the selected application scenarios for these products in more detail.

# <span id="page-118-1"></span>**9.1 The "Fast-moving consumer goods" application scenario**

#### Description

A package containing eight rolls of toilet paper is fitted with a transponder.

#### Requirements

The journey taken by the product from the manufacturer, through the entire supply chain, all the way to the retail outlet, must be controllable and trackable. Its storage in the warehouse and in the retail outlet, in particular, must be able to be monitored and controlled. Additional services such as product information and cross-selling are to be provided in the retail outlet using RFID technology (see section [2.2\)](#page-20-1).

<span id="page-119-0"></span>The packaging is generally only used for a few days or weeks. The transponder is not needed after purchase.

Commercial value, risk of product counterfeiting

The sales value is €3. The profit margin is small. There is almost no risk of product counterfeiting.

Use of product

Consumers are expected in the future to purchase this product using self-checkout.

The product and the transponder attached to the packaging will only be carried by the consumer on the way home.

# <span id="page-119-1"></span>**9.2 The "consumer electronics" application scenario**

#### Description

A high-quality, flat-screen TV made by a brand-name manufacturer is fitted with a transponder.

#### Requirements

The journey taken by the flat-screen TV from the manufacturer, through the entire supply chain, all the way to the retail outlet, must be controllable and trackable.

Furthermore, its storage in the warehouse and in the retail outlet must be able to be monitored and controlled. Additional services such as product information and cross-selling are to be provided in the retail outlet using RFID technology (see section [2.2](#page-20-1)). Stock monitoring and the additional services provided may relate to the entire retail area or warehouse, or smaller areas thereof (shelves and so on)

Following purchase, the RFID technology must support paperless guarantee handling and paperless exchange procedures, and provide a proof of purchase. The transponder should also serve to identify the appliance after sale for the purpose of firmware updates, identifying the right accessories, and so on.

How long the transponder has to last depends on the length of time for which the appliance will be used; in this case a number of years.

Commercial value, risk of product counterfeiting

The sales value is more than €1,000. There is a considerable risk of product counterfeiting.

#### Use of product

Consumers are not expected to check this product out themselves without any interaction with the sales personnel.

The product and the attached transponder is transported to the customer, where it remains.

# <span id="page-120-1"></span><span id="page-120-0"></span>**9.3 The "brand-name clothing" application scenario**

#### Description

A high-quality men's suit made by a brand-name manufacturer is fitted with a transponder.

#### Requirements

The journey taken by the men's suit from the manufacturer, through the entire supply chain, all the way to the retail outlet, must be controllable and trackable. Furthermore, its storage in the warehouse and in the retail outlet must be able to be monitored and controlled. It is especially important to be able to distinguish the type (size, colour, cut), and control availability separately.

Additional services such as product information and cross-selling are to be provided in the retail outlet using RFID technology (see section [2.2\)](#page-20-1).

Following purchase, the RFID technology must support paperless guarantee handling and paperless exchange procedures, and provide a proof of purchase. The availability of different sizes and colours can be made clearer to customers.

How long the transponder has to last depends on the length of time for which the suit will be used; this could be a number of years.

#### Commercial value, risk of product counterfeiting

The sales value is several hundred euros. There is a considerable risk of product counterfeiting because of the manufacturer's brand image.

#### Use of product

Consumers are not expected to check this product out themselves without any interaction with the sales personnel.

The product and the transponder attached to it will be carried around by the consumer for a long period of time. The transponder is integrated into the label, which may be sewn onto the product. Generally speaking the transponder is removed from the product at home and no later. The customer can keep the label at home for paperless guarantee claims.

# <span id="page-121-1"></span><span id="page-121-0"></span>**10 Suggestions on implementing the system as a whole**

This section describes, as an example, the entire system for the "trade logistics" application area.

There is a fundamental distinction between the IT systems used in logistics and in retail. Logistics involve primarily the flow of goods and the resulting arrival and departure of products (receipt of goods, preparation of shipment, goods despatch) and the management of warehouses (storage place management), whereas in the field of retail the focus is on drawing up invoices and on the subsequent payment procedure. Warehouse systems are generally supplied with information by EDI (such as electronic despatch advices). In the field of retail, the existing checkout system is often complemented by an additional customer relation management (CRM) system, in which information is stored with the permission of the customer and used for marketing, and for transactions relating to that customer (such as orders).

![](_page_121_Figure_4.jpeg)

**Figure 10–1 Differentiation between different IT systems** 

The basic principle of the EPCglobal Network is to make product information available at all times using the Internet. The EPCglobal Network connects peripheral servers containing all of the relevant EPC information (that is, all of the master and logistical data relating to a particular EPC). Data transmission is done via the Internet. Various network service components control the servers and authorise access to the information. The EPCglobal Network is in the process of being set up and initial instances of it are already on the market. The focus of the Network is in the field of logistics (see diagrams below).

These Guidelines discuss the IT systems used in logistics and trade in terms of the security of those systems. The physical and functional implementation of those systems is only relevant inasmuch as it is necessary for the analysis of their security and the definition of safeguards. It is especially important to differentiate between systems which save, process and transmit personal data, and systems which do not come into contact with personal data at all:

- 1 None of the IT systems in logistics handle personal data.
- 2 Some of the backend systems in retail may contain personal data. Retail checkout systems typically contain, including in the case of customer cards, a reference to the customer data set in the retailer's backend system, but not any customer details as such.

<span id="page-122-0"></span>![](_page_122_Figure_1.jpeg)

**Figure 10–2 System view of the logistical supply chain** 

![](_page_122_Figure_3.jpeg)

![](_page_122_Figure_4.jpeg)

# <span id="page-122-1"></span>**10.1 Suggestions on implementing the infrastructure**

#### <span id="page-122-2"></span>**10.1.1 Determining the protection demand for the logistics infrastructure**

The following assumptions apply to the logistics infrastructure, and these should be included when determining the protection requirements:

- 1 The systems described in section [10.1](#page-122-1) should support all of the proposed application scenarios simultaneously. This includes, in particular, supporting safeguards against counterfeiting.
- 2 Personal data should be managed and processed exclusively in backend systems (CRM systems). Customer cards are used.
- 3 Logistical data is generated and must be communicated and processed.

On the basis of the criteria described in section [8.2.5](#page-79-1), the logistics infrastructure can be assigned to the following protection demand categories:

| Security objective |                                                                      | Protec<br>tion de<br>mand<br>category | Criteria for allocating to protection demand categories                                                                                       |
|--------------------|----------------------------------------------------------------------|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| SS1                | Technical<br>compatibility                                           | 1                                     | All system components are from the same supplier.<br>The supplier ensures that they are compatible.                                           |
|                    |                                                                      | 2                                     | The system has to function with components from a<br>small number of defined suppliers. The system man<br>ager or an SI ensure compatibility. |
|                    |                                                                      | 3                                     | Open system that has to function with components<br>from any company in the market.                                                           |
| SS2                | Fallback solu<br>tion in the<br>event of mal                         | 1                                     | Malfunction affects only a few transponders.                                                                                                  |
|                    |                                                                      | 2                                     | Malfunction affects many transponders.                                                                                                        |
|                    | function                                                             | 3                                     | Malfunction affects most or all transponders.                                                                                                 |
| SS3                | Intuitive, fault<br>tolerant op<br>eration                           | 1                                     | A few consumers cannot operate it intuitively.                                                                                                |
|                    |                                                                      | 2                                     | Many consumers cannot operate it intuitively.                                                                                                 |
|                    |                                                                      | 3                                     | A large proportion of consumers cannot operate it intui<br>tively.                                                                            |
| SI1                | Protection of<br>personal data<br>in the cus<br>tomer data<br>system | 1                                     | Personal data is not gathered during the sales process.                                                                                       |
|                    |                                                                      | 2                                     | A personal link is set up during the sales process by<br>means of a customer card number, but product-related<br>logistical data is not used. |
|                    |                                                                      | 3                                     | Personal data relating to special methods of payment<br>(e.g. invoice) is used during the sales process.                                      |
| SI2                | Protection of<br>object code                                         | 1                                     | No risk of product counterfeiting, manipulation, DoS,<br>etc.                                                                                 |
|                    |                                                                      | 2                                     | Product counterfeiting, manipulation, DoS, etc. causes<br>limited damage amounting to < 1% of goods value.                                    |
|                    |                                                                      | 3                                     | Product counterfeiting, manipulation, DoS, etc. causes<br>massive damage (danger to people, large losses of<br>sales and image, and so on).   |
| SI3                | Protecting the<br>allocation of<br>object and                        | 1                                     | No risk of product counterfeiting, DoS, etc.                                                                                                  |
|                    |                                                                      | 2                                     | Product counterfeiting, DoS, etc. causes limited dam                                                                                          |

<span id="page-124-0"></span>

| Security objective |                                                                   | Protec<br>tion de<br>mand<br>category | Criteria for allocating to protection demand categories                                                                                                                   |  |  |
|--------------------|-------------------------------------------------------------------|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                    | object code                                                       |                                       | age amounting to < 1% of goods value.                                                                                                                                     |  |  |
|                    |                                                                   | 3                                     | Product counterfeiting, DoS, etc. causes massive dam<br>age (danger to people, large losses of sales and im<br>age, and so on).                                           |  |  |
| SI4                | Protection of<br>logistical data                                  | 1                                     | Low dependency on logistical data                                                                                                                                         |  |  |
|                    |                                                                   | 2                                     | Incorrect or missing logistical data causes limited dam<br>age amounting to < 1% of goods value.                                                                          |  |  |
|                    |                                                                   | 3                                     | Incorrect or missing logistical data causes massive<br>damage amounting to > 1% of goods value or danger<br>to persons, significant loss of image, and so on.             |  |  |
| SI5                | Protection                                                        | 1                                     | Low risk of DoS attacks                                                                                                                                                   |  |  |
|                    | against DoS<br>attacks on the<br>RF system<br>components          | 2                                     | Medium risk of DoS attacks / DoS attacks cause limited<br>damage amounting to < 1% of goods value.                                                                        |  |  |
|                    |                                                                   | 3                                     | High risk of DoS attacks / DoS attacks cause massive<br>damage amounting to > 1% of goods value or danger<br>to persons, significant loss of image, and so on.            |  |  |
| SI6                | Protection<br>against spy<br>ing on goods<br>flow informa<br>tion | 1                                     | Low risk of spying                                                                                                                                                        |  |  |
|                    |                                                                   | 2                                     | Medium risk of spying / spying causes limited damage<br>amounting to < 1% of goods value.                                                                                 |  |  |
|                    |                                                                   | 3                                     | High risk of spying / spying causes massive damage<br>amounting to > 1% of goods value or danger to per<br>sons, significant loss of image, and so on.                    |  |  |
| SI7                | Availability of<br>EPC data                                       | 1                                     | Low risk of non-availability                                                                                                                                              |  |  |
|                    |                                                                   | 2                                     | Medium risk of non-availability / non-availability causes<br>limited damage amounting to < 1% of goods value.                                                             |  |  |
|                    |                                                                   | 3                                     | High risk of non-availability / non-availability causes<br>massive damage amounting to > 1% of goods value or<br>danger to persons, significant loss of image, and so on. |  |  |
| SP1                | Protection of<br>personal data                                    | 1                                     | Customer's reputation is damaged.                                                                                                                                         |  |  |
|                    |                                                                   | 2                                     | Customer's social existence is damaged.                                                                                                                                   |  |  |
|                    |                                                                   | 3                                     | Customer's physical existence is damaged.                                                                                                                                 |  |  |
| SP2                | Data minimi<br>sation                                             | 1                                     | Personal data is not gathered during the sales process.                                                                                                                   |  |  |
|                    |                                                                   | 2                                     | A personal link is set up during the sales process by<br>means of a customer card number, but product-related<br>logistical data is not used.                             |  |  |
|                    |                                                                   | 3                                     | Personal data relating to special methods of payment                                                                                                                      |  |  |

<span id="page-125-0"></span>

| Security objective |                                                                  | Protec<br>tion de<br>mand<br>category | Criteria for allocating to protection demand categories |
|--------------------|------------------------------------------------------------------|---------------------------------------|---------------------------------------------------------|
|                    |                                                                  |                                       | (e.g. invoice) is used during the sales process.        |
| SP3                | Protection<br>against the<br>creation of<br>movement<br>profiles | 1                                     | Customer's reputation is damaged.                       |
|                    |                                                                  | 2                                     | Customer's social existence is damaged.                 |
|                    |                                                                  | 3                                     | Customer's physical existence is damaged.               |

**Table 10–1 Protection demand of the entire system of logistical infrastructure** 

#### **10.1.2 Interfaces in the system as a whole**

The system shown in section [10.1](#page-122-1) is reliant on interaction between all the system components. In order to facilitate the business processes described in section [6,](#page-49-1) the technical interfaces and operative interaction between the components have to be specified.

Furthermore, agreements must be made between the entities to regulate the responsibilities and the operational procedures.

#### **10.1.2.1 Threats relevant to the logistics infrastructure**

The following threats relevant to the interfaces of the system as a whole can be deduced from the security targets used to determine the protection demand in section [10.1.1.](#page-122-2)

| Threats to the contactless<br>interface |                                                                                          | Protection<br>demand | Comments                                                                                                                                                                                                                                                                                   |
|-----------------------------------------|------------------------------------------------------------------------------------------|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TC1                                     | Lack of compatibil<br>ity between the in<br>terfaces of the<br>transponder and<br>reader | 3                    | A lack of compatibility between interfaces pre<br>vents the system from working when reading,<br>writing data, and deactivating. The result is<br>similar to a successful DoS attack on the entire<br>system. The logistical infrastructure could not<br>be guaranteed to function.        |
| TC2                                     | Eavesdropping                                                                            | 3                    | Unauthorised listening-in to communication<br>between a transponder and a reader can be<br>used for purposes such as attacking product<br>codes, passwords and authentication data.                                                                                                        |
| TC3                                     | DoS attack on the<br>RF interface                                                        | 1                    | Interference in RF communication (jamming).<br>Interference in the anti-collision mechanism for<br>selecting the transponder (blocker tag)<br>Blocking the electromagnetic field of the reader<br>(shielding)<br>Altering the resonance frequency of reader or<br>transponder (de-tuning). |

<span id="page-126-0"></span>

| Threats to the contactless<br>interface |                                                          | Protection<br>demand | Comments                                                                                                                              |
|-----------------------------------------|----------------------------------------------------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| TC4                                     | Outside influence<br>over other existing<br>applications | 3                    | Some other RF applications use the same or<br>neighbouring working frequencies. This can<br>limit the availability of logistics data. |

| Table 10–2 | Threats relevant to the contactless interface |
|------------|-----------------------------------------------|

| Threats to the system as a<br>whole |                                                               | Protection<br>demand | Comments                                                                                                                                                                                                                                                                                      |
|-------------------------------------|---------------------------------------------------------------|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TS1                                 | Lack of fallback so<br>lution                                 | 3                    | The lack of a fallback solution in the event of a<br>failure of system interfaces can lead to a com<br>plete breakdown of the logistics infrastructure.                                                                                                                                       |
| TS2                                 | Unauthorised scan<br>ning of data                             | 3                    | The backend systems store information about<br>the objects, object codes, readers, warehouse<br>locations and so on. Furthermore, customer<br>data systems can contain personal data. The<br>retrieval of this data by unauthorised persons<br>would discredit the system and enable attacks. |
| TS3                                 | Manipulation of<br>data                                       | 3                    | Information about the objects, object codes,<br>readers, warehouse locations and so on is<br>transmitted via the system interfaces. The ma<br>nipulation of this data by unauthorised persons<br>represents a serious attack.                                                                 |
| TS4                                 | System malfunction                                            | 3                    | Malfunctions in the interfaces between the sys<br>tems can be caused in a variety of scenarios<br>by technical faults, incorrect operation or DoS<br>attacks:                                                                                                                                 |
|                                     |                                                               |                      | 1. Fault in interfaces                                                                                                                                                                                                                                                                        |
|                                     |                                                               |                      | 2. Lack of availability of interfaces                                                                                                                                                                                                                                                         |
|                                     |                                                               |                      | 3. Fault in power supply                                                                                                                                                                                                                                                                      |
|                                     |                                                               |                      | 4. Interruption in network connection                                                                                                                                                                                                                                                         |
|                                     |                                                               |                      | 5. Physical destruction                                                                                                                                                                                                                                                                       |
| TS5                                 | Lack of compatibil<br>ity between the in<br>terfaces          | 3                    | Lack of compatibility between interfaces<br>causes malfunctions. The result is similar to a<br>DoS attack on the system. The logistical infra<br>structure would become largely dysfunctional.                                                                                                |
| TS6                                 | Unauthorised re<br>trieval of logistical<br>data              | 3                    | Unauthorised active retrieval of logistical data                                                                                                                                                                                                                                              |
| TS7                                 | Unauthorised writ<br>ing / manipulation<br>of logistical data | 3                    | Unauthorised writing of logistical data into the<br>backend system for the purpose of manipulat<br>ing or compromising data. This threatens in<br>particular the header, which contains the type<br>of data among other things.                                                               |

**Table 10–3 Threats relevant to the system interfaces** 

#### <span id="page-127-0"></span>**10.1.2.2 Definition of safeguards for the interfaces of the system as a whole**

Based on the relevant threats in the preceding section, this section defines general execution proposals and safeguards for the system as a whole and the system components. These safeguards are described in detail in section [0.](#page-89-1)

| Threat |                                                                                         | Safeguards                                             | Safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------|-----------------------------------------------------------------------------------------|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TC1    | Lack of compati<br>bility between the<br>interfaces of the<br>transponder and<br>reader | MS1.3                                                  | 1<br>Introduction of interface tests and ap<br>proval procedures – certification                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| TC2    | Eavesdropping                                                                           | MS2.3<br>MS3.3                                         | 2<br>Preventing eavesdropping on data ex<br>change between transponder and<br>reader – advanced safeguards<br>3<br>Assuring reliable data transmission be<br>tween terminal and transponder – sur<br>veying                                                                                                                                                                                                                                                                                                                                                                |
| TC3    | DoS attack on the<br>RF interface                                                       | MS3.1                                                  | 1<br>Assuring reliable data transmission be<br>tween terminal and transponder – long<br>term testing and organisational safe<br>guards                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| TC4    | Outside influence<br>over other exist<br>ing applications                               | MS3.3                                                  | 1<br>Assuring reliable data transmission be<br>tween terminal and transponder – sur<br>veying                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| TS1    | Lack of fallback<br>solution                                                            | MS4.3                                                  | 1<br>Definition of fallback solutions in the<br>event of system interface or system<br>component failure – implementation ac<br>cording to fallback concept                                                                                                                                                                                                                                                                                                                                                                                                                |
| TS2    | Unauthorised<br>scanning of data                                                        | MS5.3                                                  | 1<br>Securing the confidentiality of data<br>when communicating within the system<br>– secure communications channel                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| TS3    | Manipulation of<br>data                                                                 | MS7.3                                                  | 1<br>Securing the data integrity in order to<br>protect against manipulation when<br>transmitting data within the system –<br>MAC or signatures                                                                                                                                                                                                                                                                                                                                                                                                                            |
| TS4    | System malfunc<br>tion                                                                  | MS4.3<br>MS9.3<br>MS10.3<br>MS11.3<br>MS13.3<br>MS14.3 | 1<br>Definition of a fallback solution in the<br>event of system interface or system<br>component failure – implementation ac<br>cording to failure concept<br>2<br>Securing the system's functions against<br>DoS attacks at the interfaces – security<br>concept<br>3<br>Securing the function of the system<br>against incorrect operation by employ<br>ees and users – tests, personnel and<br>user instructions<br>4<br>Secure the function of the system to<br>prevent the technical failure of compo<br>nents and transmission routes –<br>evaluation of components |

<span id="page-128-0"></span>

| Threat |                                                                  | Safeguards                | Safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------|------------------------------------------------------------------|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        |                                                                  |                           | 5<br>Ergonomic user instructions<br>6<br>Support – system-wide support                                                                                                                                                                                                                                                                                                                                                                       |
| TS5    | Lack of compati<br>bility between the<br>interfaces              | MS1.3<br>MS11.3<br>MS12.3 | 1<br>Introduction of interface tests and ap<br>proval procedures – certification<br>2<br>Secure the function of the system to<br>prevent the technical failure of compo<br>nents and transmission routes –<br>evaluation of components<br>3<br>Specifications for system concept and<br>requirements for components with the<br>aim of integration and interoperability –<br>interoperability tests according to test<br>concept, evaluation |
| TS6    | Unauthorised re<br>trieval of logistical<br>data                 | MS5.3                     | 1<br>Securing the confidentiality of data<br>when communicating within the system<br>– secure communications channel                                                                                                                                                                                                                                                                                                                         |
| TS7    | Unauthorised<br>writing / manipu<br>lation of logistical<br>data | MS7.3                     | 1<br>Securing the data integrity in order to<br>protect against manipulation when<br>transmitting data within the system –<br>MAC or signatures                                                                                                                                                                                                                                                                                              |

**Table 10–4 Safeguards for the interfaces of the system as a whole** 

#### **10.1.2.3 Residual risks**

For technical and commercial reasons, it is not always possible to eliminate threats completely using safeguards. In such cases a certain risk remains.

#### **10.1.3 Reader**

Readers control the flow of information for reading from and writing to the transponder using a contactless communication protocol. The reader assumes the active role (master), while the transponder is passive (slave).

Readers are integrated into various system components:

- 1 Stationary readers for goods flow monitoring
- 2 Mobile readers
- 3 Readers for monitoring stock levels
- 4 Kill terminals
- 5 Self-checkout points

The readers have to have the following features:

- 1 Contactless reading and writing device with interface as defined in ISO/IEC18000-6C.
- 2 Connection to central system or network as per EPCIS.
- 3 Capacity to store all logistical data until the next data exchange with the central system.
- 4 Basic cryptographic functions.
- 5 Defined reading speed and reading probability.

<span id="page-129-0"></span>6 Special code as defined by EPCglobal.

#### **10.1.3.1 Threats relevant to the readers**

The following threats relevant to the interfaces of the system as a whole can be deduced from the assumptions used to determine the protection demand in section [10.1.1.](#page-122-2)

| Threats to the contactless<br>interface in the reader |                                                                                          | Protection<br>demand | Comments                                                                                                                                                                                                                                                                                                               |
|-------------------------------------------------------|------------------------------------------------------------------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TC1                                                   | Lack of compatibil<br>ity between the in<br>terfaces of the<br>transponder and<br>reader | 3                    | A lack of compatibility between interfaces pre<br>vents the system from working when reading,<br>writing data, and deactivating. The result is<br>similar to a successful DoS attack on the entire<br>system. The logistical infrastructure could not<br>be guaranteed to function.                                    |
| TC2                                                   | Eavesdropping                                                                            | 3                    | Unauthorised listening-in to communication<br>between a transponder and a reader can be<br>used for purposes such as attacking product<br>codes, passwords and authentication data.                                                                                                                                    |
| TC3                                                   | DoS attack on the<br>RF interface                                                        | 1                    | 1<br>Interference in RF communication (jam<br>ming).<br>2<br>Interference in the anti-collision mecha<br>nism for selecting the transponder (blocker<br>tag)<br>3<br>Blocking the electromagnetic field of the<br>reader (shielding)<br>4<br>Altering the resonance frequency of reader<br>or transponder (de-tuning). |
| TC4                                                   | Outside influence<br>over other existing<br>applications                                 | 3                    | Some other RF applications use the same or<br>neighbouring working frequencies. This can<br>limit the availability of logistics data.                                                                                                                                                                                  |

**Table 10–5 Threats relevant to the contactless interface in the reader** 

| Threats to the reader |                                                            | Protection<br>demand | Comments                                                                                                                                                                                         |
|-----------------------|------------------------------------------------------------|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TR1                   | Unauthorised ma<br>nipulation of refer<br>ence information | 3                    | Manipulation of reference information (keys,<br>evaluation algorithms, blacklists and whitelists)<br>can be employed for unauthorised use and for<br>DoS.                                        |
| TR2                   | Unauthorised scan<br>ning of reference<br>information      | 3                    | The retrieval of reference information (keys,<br>evaluation algorithms, blacklists and whitelists)<br>can be employed for unauthorised use (e.g.<br>counterfeiting of entitlements) and for DoS. |
| TR3                   | Reader malfunction                                         | 3                    | Reader malfunctions can be caused in a range<br>of scenarios by technical faults, incorrect op<br>eration, or DoS attacks:                                                                       |
|                       |                                                            |                      | 1<br>Fault in contactless interface<br>2<br>Fault in reference information (keys, black                                                                                                          |

<span id="page-130-0"></span>

| Threats to the reader |                                                      | Protection<br>demand | Comments                                                                                                                                                                                                                                                                                                                                    |
|-----------------------|------------------------------------------------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                       |                                                      |                      | lists, etc.)<br>3<br>Fault in application implementation<br>4<br>Fault in evaluation algorithms for object<br>codes and authentications<br>5<br>Fault in power supply<br>6<br>Jamming<br>7<br>Blocker tag<br>8<br>Interruption of the link to the central sys<br>tem<br>9<br>Physical destruction<br>10 Fault in user instruction functions |
| TR4                   | Lack of user in<br>structions                        | 2                    | A lack of user-friendliness at checkout or kill<br>terminals can cause considerable operative<br>problems.                                                                                                                                                                                                                                  |
| TS1                   | Lack of fallback so<br>lution                        | 3                    | The lack of a fallback solution in the event of a<br>failure of readers can limit the availability of<br>logistics data and cause limited or even wide<br>spread damage.                                                                                                                                                                    |
| TS5                   | Lack of compatibil<br>ity between the in<br>terfaces | 3                    | Lack of compatibility between interfaces<br>causes malfunctions. The result is similar to a<br>DoS attack on the system. The logistical infra<br>structure would become largely dysfunctional.                                                                                                                                              |

| Table 10–6<br>Threats relevant to the reader |
|----------------------------------------------|
|----------------------------------------------|

#### **10.1.3.2 Definition of safeguards for the reader**

Based on the relevant threats in the preceding section, this section defines general execution proposals and safeguards for the reader and its applications. These safeguards are described in detail in section [0](#page-89-1).

| Threat |                                                                                         | Safeguards     | Safeguard                                                                                                                                                                                                   |
|--------|-----------------------------------------------------------------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TC1    | Lack of compati<br>bility between the<br>interfaces of the<br>transponder and<br>reader | MS1.3<br>MR1.3 | 1<br>Introduction of interface tests and ap<br>proval procedures – certification                                                                                                                            |
| TC2    | Eavesdropping                                                                           | MS2.3<br>MS3.3 | 1<br>Preventing eavesdropping on data ex<br>change between transponder and<br>reader – advanced safeguards<br>2<br>Assuring reliable data transmission be<br>tween terminal and transponder – sur<br>veying |
| TC3    | DoS attack on the<br>RF interface                                                       | MS3.1          | 1<br>Assuring reliable data transmission be<br>tween terminal and transponder – long<br>term testing and organisational safe-                                                                               |

<span id="page-131-0"></span>

| Threat |                                                              | Safeguards       | Safeguard                                                                                                                                                   |
|--------|--------------------------------------------------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        |                                                              |                  | guards                                                                                                                                                      |
| TC4    | Outside influence<br>over other exist<br>ing applications    | MS3.3            | 1<br>Assuring reliable data transmission be<br>tween terminal and transponder – sur<br>veying                                                               |
| TR1    | Unauthorised<br>manipulation of<br>reference infor<br>mation | MR2.3            | 1<br>Protection of reference information<br>against retrieval, data errors and ma<br>nipulation – advanced protection                                       |
| TR2    | Unauthorised<br>scanning of refer<br>ence information        | MR2.3            | 1<br>Protection of reference information<br>against retrieval, data errors and ma<br>nipulation – advanced protection                                       |
| TR3    | Reader malfunc<br>tion                                       | MR3.3            | 1<br>Protection of the reader against mal<br>function – evaluation                                                                                          |
| TR4    | Lack of user in<br>structions                                | MS13.2           | 1<br>Ergonomic user instructions                                                                                                                            |
| TS1    | Lack of fallback<br>solution                                 | MS4.3            | 1<br>Definition of fallback solutions in the<br>event of system interface or system<br>component failure – implementation ac<br>cording to fallback concept |
| TS5    | Lack of compati<br>bility between the<br>interfaces          | MS1.3            | 1<br>Introduction of interface tests and ap<br>proval procedures – certification                                                                            |
|        |                                                              | MS11.3<br>MS12.3 | 2<br>Secure the function of the system to<br>prevent the technical failure of compo<br>nents and transmission routes –<br>evaluation of components          |
|        |                                                              |                  | 3<br>Specifications for system concept and<br>requirements for components – evalua<br>tion                                                                  |

**Table 10–7 Safeguards for the reader and its applications** 

#### **10.1.3.3 Residual risks**

For technical and commercial reasons, it is not always possible to eliminate threats completely using safeguards. In such cases a certain risk remains.

### **10.1.4 Backend systems**

This discussion relates to every IT system in logistics and all the backend systems in trade that do not store or handle personal data.

#### **10.1.4.1 Threats relevant to the backend systems**

The following threats relevant to the backend systems can be deduced from the security targets used to determine the protection demand in section [10.1.1.](#page-122-2)

| Threats to backend systems |                                                                       | Protection<br>demand | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------------------|-----------------------------------------------------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TS1                        | Lack of fallback so<br>lution                                         | 3                    | The lack of a fallback solution when system<br>components fail can lead to a complete break<br>down of services (acquisition and distribution<br>of logistical data, etc.).                                                                                                                                                                                                                                                                              |
| TS2                        | Unauthorised scan<br>ning of data in the<br>system                    | 3                    | The backend systems store information about<br>the objects, object codes, readers, warehouse<br>locations and so on. The retrieval of this data<br>by unauthorised persons would discredit the<br>system and enable attacks.                                                                                                                                                                                                                             |
| TS3                        | Manipulation of<br>data in the system                                 | 3                    | The backend systems store information about<br>the objects, object codes, readers, warehouse<br>locations and so on. The manipulation of this<br>data by unauthorised persons represents a se<br>rious attack.                                                                                                                                                                                                                                           |
| TS4                        | System malfunction                                                    | 3                    | Individual system component malfunctions can<br>be caused in a range of scenarios by technical<br>faults, incorrect operation or DoS attacks:<br>1<br>Fault in local and central systems<br>2<br>Lack of availability of local and central sys<br>tems<br>3<br>Fault in data storage<br>4<br>Fault in power supply<br>5<br>Interruption of the link to the central sys<br>tem<br>6<br>Protection against physical attacks (dis<br>mantling, destruction) |
| TS5                        | Lack of compatibil<br>ity between the in<br>terfaces                  | 3                    | Lack of compatibility between interfaces cau<br>ses malfunctions. The result is similar to a DoS<br>attack on the system. Many customers and/or<br>entitlements may be affected.                                                                                                                                                                                                                                                                         |
| TS6                        | Unauthorised re<br>trieval of logistical<br>data                      | 3                    | Unauthorised active retrieval of logistical data                                                                                                                                                                                                                                                                                                                                                                                                         |
| TS7                        | Unauthorised writ<br>ing / manipulation<br>of logistical data         | 3                    | Unauthorised writing of logistical data into the<br>backend system for the purpose of manipulat<br>ing or compromising data. This threatens in<br>particular the header, which contains the type<br>of data among other things.                                                                                                                                                                                                                          |
| TS8                        | Protection of client<br>specific applica<br>tions and object<br>codes | 3                    | If the systems support multiple entities which<br>allocate specific information to the objects,<br>then it must be assured that the confidentiality,<br>integrity and availability of data is preserved<br>from client to client.                                                                                                                                                                                                                        |

<span id="page-133-0"></span>

| Threats to backend systems |                            | Protection<br>demand | Comments                                                                                                                                             |
|----------------------------|----------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| TS9                        | Product counterfeit<br>ing | 3                    | It is assumed that products subject to a high<br>risk of counterfeiting are supported by the sys<br>tem. This risk applies to the entities involved. |

| Table 10–8 | Threats relevant to the backend systems |  |
|------------|-----------------------------------------|--|
|            |                                         |  |

#### **10.1.4.2 Definition of safeguards for the backend systems**

Based on the relevant threats in the preceding section, this section defines general execution proposals and safeguards. These safeguards are described in detail in section [0](#page-89-1).

| Threat |                                                     | Safeguards                                             | Safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |  |
|--------|-----------------------------------------------------|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| TS1    | Lack of fallback<br>solution                        | MS4.3                                                  | 1<br>Definition of fallback solutions in the<br>event of system interface or system<br>component failure – implementation ac<br>cording to fallback concept                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |  |
| TS2    | Unauthorised<br>scanning of data<br>in the system   | MS6.3                                                  | 1<br>Confidential storage of data – introduc<br>tion of multi-tenant access protection<br>with a defined role model                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |  |
| TS3    | Manipulation of<br>data in the sys<br>tem           | MS6.3<br>MS8.3                                         | 1<br>Confidential storage of data – introduc<br>tion of multi-tenant access protection<br>with a defined role model<br>2<br>Securing data integrity when storing<br>data                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  |
| TS4    | System malfunc<br>tion                              | MS4.3<br>MS9.3<br>MS10.3<br>MS11.3<br>MS13.3<br>MS14.3 | 1<br>Definition of a fallback solution in the<br>event of system interface or system<br>component failure – implementation ac<br>cording to failure concept<br>2<br>Securing the system's functions against<br>DoS attacks at the interfaces – security<br>concept<br>3<br>Securing the function of the system<br>against incorrect operation by employ<br>ees and users – tests, personnel and<br>user instructions<br>4<br>Secure the function of the system to<br>prevent the technical failure of compo<br>nents and transmission routes –<br>evaluation of components<br>5<br>Ergonomic user instructions<br>6<br>Support – system-wide support |  |
| TS5    | Lack of compati<br>bility between the<br>interfaces | MS1.3<br>MS11.3<br>MS12.3                              | 1<br>Introduction of interface tests and ap<br>proval procedures – certification<br>2<br>Secure the function of the system to<br>prevent the technical failure of compo<br>nents and transmission routes –<br>evaluation of components                                                                                                                                                                                                                                                                                                                                                                                                               |  |

<span id="page-134-0"></span>

| Threat |                                                                         | Safeguards     | Safeguard                                                                                                                                                                                          |  |
|--------|-------------------------------------------------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
|        |                                                                         |                | 3<br>Specifications for system concept and<br>requirements for components with the<br>aim of integration and interoperability –<br>interoperability tests according to test<br>concept, evaluation |  |
| TS6    | Unauthorised re<br>trieval of logistical<br>data                        | MS6.3          | 1<br>Confidential storage of data – introduc<br>tion of multi-tenant access protection<br>with a defined role model                                                                                |  |
| TS7    | Unauthorised<br>writing / manipu<br>lation of logistical<br>data        | MS6.3<br>MS8.3 | 1<br>Confidential storage of data – introduc<br>tion of multi-tenant access protection<br>with a defined role model<br>2<br>Securing data integrity when storing<br>data                           |  |
| TS8    | Protection of cli<br>ent-specific appli<br>cations and ob<br>ject codes | MS6.3          | 1<br>Confidential storage of data – introduc<br>tion of multi-tenant access protection<br>with a defined role model                                                                                |  |
| TS9    | Product counter<br>feiting                                              | MS15.3         | 1<br>Using the EPC to secure against coun<br>terfeit products – additional use of UID                                                                                                              |  |

**Table 10–9 Safeguards for the backend systems** 

#### **10.1.4.3 Residual risks**

For technical and commercial reasons, it is not always possible to eliminate threats completely using safeguards. In such cases a certain risk remains. This section describes the residual risk for the relevant cases.

#### <span id="page-134-1"></span>**10.1.5 Customer data systems**

Retailers use IT systems to help conduct the sale of products to consumers. These systems all support the anonymous sale of, and anonymous payment for, the products purchased. As described in section [10](#page-121-1), retailers may also use customer data systems that may in turn support optional, customer-specific services:

- 1 Delivery of purchased products to customers
- 2 Archiving guarantee information about purchased products
- 3 Processing guarantee claims
- 4 Customer-related bonus and discount schemes.

Personal data is not stored on transponders allocated to objects. The aforementioned optional features of a customer data system, however, may require the use of personal data. The customer data system is therefore the only system component which generates personal data, and which has to be protected against misuse such as the unauthorised linking of the personal data on a customer card with logistics data. If customer cards are used, then only the card number, not personal details, is employed for the payment procedure. The generating of invoices containing customer details takes place in the systems situated behind that system.

#### <span id="page-135-0"></span>**10.1.5.1 Threats relevant to the customer data system**

The following threats relevant to the interfaces of the system as a whole can be deduced from the assumptions used to determine the protection demand in section [10.1.1.](#page-122-2)

| Threats to customer data<br>systems |                                                                                   | Protection<br>demand | Comments                                                                                                                                                                                                                                                  |
|-------------------------------------|-----------------------------------------------------------------------------------|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TV1                                 | Lack of fallback so<br>lution                                                     | 3                    | The lack of a fallback solution in the event of a<br>customer data system malfunction can lead to<br>a complete breakdown of services (sales, in<br>voicing, bonus calculation, guarantee process<br>ing, product delivery, and so on.).                  |
| TV2                                 | System malfunction                                                                | 3                    | Customer data system malfunctions can be<br>caused in a variety of scenarios by technical<br>faults, incorrect operation or DoS attacks:                                                                                                                  |
|                                     |                                                                                   |                      | 1<br>Fault in local and central systems<br>2<br>Lack of availability of local and central sys<br>tems<br>3<br>Fault in data storage<br>4<br>Fault in power supply<br>5<br>Interruption of the link to the central sys<br>tem<br>6<br>Physical destruction |
| TV3                                 | Lack of compatibil<br>ity between the in<br>terfaces                              | 3                    | Lack of compatibility between interfaces cau<br>ses malfunctions. The result is similar to a DoS<br>attack on the system. Many customers could<br>be affected.                                                                                            |
| TV4                                 | Unauthorised scan<br>ning of sales and<br>invoicing informa<br>tion               | 3                    | Unauthorised active retrieval of invoicing data                                                                                                                                                                                                           |
| TV7                                 | Unauthorised writ<br>ing / manipulating<br>of sales and invoic<br>ing information | 3                    | Unauthorised writing of invoicing data into the<br>customer data system for the purpose of ma<br>nipulating or compromising data.                                                                                                                         |
| TV8                                 | Unauthorised scan<br>ning of personal<br>data                                     | 3                    | Disclosure of customer data                                                                                                                                                                                                                               |
| TV9                                 | Unauthorised writ<br>ing / manipulation<br>of personal data                       | 3                    | Manipulation of customer data                                                                                                                                                                                                                             |
| TV10                                | Falsification of<br>identity data                                                 | 3                    | Recipients may have to identify themselves<br>when objects are delivered or collected. Pro<br>ducing a false identity could allow products and<br>services to be obtained at the expense of other<br>customers or the retailer.                           |
| TV11                                | Unauthorised col-                                                                 | 1                    | Gathering and storing personal data without                                                                                                                                                                                                               |

<span id="page-136-0"></span>

| Threats to customer data<br>systems |                                  | Protection<br>demand | Comments                                                                                                                              |
|-------------------------------------|----------------------------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------------|
|                                     | lection and storage<br>of data   |                      | justification infringes the stipulation on data<br>minimisation.                                                                      |
| TV12                                | Unauthorised link<br>ing of data | 3                    | Unauthorised linking of personal data with in<br>voicing and/or logistical data. It is assumed<br>that customer cards are being used. |

#### **Table 10–10 Threats relevant to the customer data system**

#### **10.1.5.2 Definition of safeguards for the customer data system**

Based on the relevant threats in the preceding section, this section defines general execution proposals and safeguards. These safeguards are described in detail in section [0](#page-89-1).

| Threat |                                                     | Safeguards                                             | Safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |  |
|--------|-----------------------------------------------------|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| TV1    | Lack of fallback<br>solution                        | MS4.3                                                  | 1<br>Definition of fallback solutions in the<br>event of system interface or system<br>component failure – implementation ac<br>cording to fallback concept                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |  |
| TV2    | System malfunc<br>tion                              | MS4.3<br>MS9.3<br>MS10.3<br>MS11.3<br>MS13.3<br>MS14.3 | 1<br>Definition of a fallback solution in the<br>event of system interface or system<br>component failure – implementation ac<br>cording to failure concept<br>2<br>Securing the system's functions against<br>DoS attacks at the interfaces – security<br>concept<br>3<br>Securing the function of the system<br>against incorrect operation by employ<br>ees and users – tests, personnel and<br>user instructions<br>4<br>Secure the function of the system to<br>prevent the technical failure of compo<br>nents and transmission routes –<br>evaluation of components<br>5<br>Ergonomic user instructions<br>6<br>Support – system-wide support |  |
| TV3    | Lack of compati<br>bility between the<br>interfaces | MS1.3<br>MS11.3<br>MS12.3                              | 1<br>Introduction of interface tests and ap<br>proval procedures – certification<br>2<br>Secure the function of the system to<br>prevent the technical failure of compo<br>nents and transmission routes –<br>evaluation of components<br>3<br>Specifications for system concept and<br>requirements for components with the<br>aim of integration and interoperability –<br>interoperability tests according to test<br>concept, evaluation                                                                                                                                                                                                         |  |
| TV4    | Unauthorised<br>scanning of sales                   | MS6.3                                                  | 1<br>Confidential storage of data – introduc<br>tion of multi-tenant access protection                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |  |

<span id="page-137-0"></span>

| Threat |                                                                                      | Safeguards     | Safeguard                                                                                                                                                                |  |
|--------|--------------------------------------------------------------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
|        | and invoicing in<br>formation                                                        |                | with a defined role model                                                                                                                                                |  |
| TV7    | Unauthorised<br>writing / manipu<br>lating of sales<br>and invoicing in<br>formation | MS6.3<br>MS8.3 | 1<br>Confidential storage of data – introduc<br>tion of multi-tenant access protection<br>with a defined role model<br>2<br>Securing data integrity when storing<br>data |  |
| TV8    | Unauthorised<br>scanning of per<br>sonal data                                        | MS6.3          | 1<br>Confidential storage of data – introduc<br>tion of multi-tenant access protection<br>with a defined role model                                                      |  |
| TV9    | Unauthorised<br>writing / manipu<br>lation of personal<br>data                       | MS6.3<br>MS8.3 | 1<br>Confidential storage of data – introduc<br>tion of multi-tenant access protection<br>with a defined role model<br>2<br>Securing data integrity when storing<br>data |  |
| TV10   | Falsification of<br>identity data                                                    | MV1.3          | 1<br>Identifying the customer when selling<br>and handing over products – customer<br>declaration                                                                        |  |
| TV11   | Unauthorised col<br>lection and stor<br>age of data                                  | MV2.3          | 1<br>Satisfying the data minimisation obliga<br>tion – special safeguards                                                                                                |  |
| TV12   | Unauthorised<br>linking of data                                                      | MV3.3          | 1<br>Separation of personal data and logisti<br>cal data                                                                                                                 |  |

**Table 10–11 Safeguards for the customer data system** 

#### **10.1.5.3 Residual risks**

For technical and commercial reasons, it is not always possible to eliminate threats completely using safeguards. In such cases a certain risk remains. This section describes the residual risk for the relevant cases.

### **10.1.6 Key management**

The job of the key management system is to provide keys used by multiple entities for all of the carrier media, applications and products used in the system, and to do so securely and reliably. Key management is the responsibility of the security manager. [GSHB] can be used as a general guideline for implementation.

Keys are generated individually for each purpose. As far as possible, a distinct key is allocated to each form of interaction (e.g. initialisation, writing authentication data, setting passwords, reading access-protected data, activating the kill command and so on). The precise characteristics have to be ascertained for each application scenario as part of the creation of a specific security concept that harmonises with the role model.

The keys are generated in a secure environment and stored in a secure database. The various forms of SAM are also produced in this secure environment. The documentation of the life cycle of the SAMs that are produced and issued is another of the key management system's tasks.

<span id="page-138-0"></span>The SAMs and keys are generated by the security manager or his agents as and when users need them. The following types of SAM are basically supported:

- Initialiser SAMs Initialiser SAMs are required to initialise transponders and load protected information (e.g. authentication data, setting passwords).
- User SAMs Depending on the function required in the application scenario, user SAMs can be needed by the various entities in the supply chain to read and evaluate the data stored in transponders.

Key information is normally loaded onto a SAM as and when the user requires it. The aim of an initialiser is, for example, to enable all of the transponders that occur in its area to be initialised with the necessary applications without changing the SAM.

This kind of user-specific SAM must be configured under an agreement between the user and the system manager.

The SAM should support the secure loading of new keys via a network. Ideally, updating can be done by the security manager directly.

#### **10.1.6.1 Threats relevant to the key management system**

The following threats relevant to the interfaces of the system as a whole can be deduced from the assumptions used to determine the protection demand in section [10.1.1.](#page-122-2)

| Threats to the key man<br>agement system |                                       | Protection<br>demand | Comments                                                                                                                                                                                                                                                                                                                                                                                              |  |
|------------------------------------------|---------------------------------------|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| TK1                                      | Insufficient key<br>data quality      | 3                    | Deficient key quality increases the chances of<br>successful attacks.                                                                                                                                                                                                                                                                                                                                 |  |
| TK2                                      | Unauthorised scan<br>ning of key data | 3                    | The retrieval of key data by unauthorised per<br>sons can discredit the system and facilitate at<br>tacks, e.g. on any cryptographically protected<br>data or functions.                                                                                                                                                                                                                              |  |
| TK3                                      | Manipulation of key<br>data           | 3                    | The manipulation of key data can discredit the<br>system's security concept and facilitate at<br>tacks, e.g. on any cryptographically protected<br>data or functions. Manipulation can affect the<br>generation of keys, the production of key<br>carriers, the transmission of keys and the local<br>use of keys.                                                                                    |  |
| TK4                                      | Key management<br>system malfunction  | 3                    | Key management system malfunctions can be<br>caused in a variety of scenarios by technical<br>faults, incorrect operation or DoS attacks:<br>1<br>Fault in local and central systems<br>2<br>Lack of availability of local and central sys<br>tems<br>3<br>Fault in data storage<br>4<br>Fault in specific application implementa<br>tion<br>5<br>Fault in evaluation algorithms for entitle<br>ments |  |

<span id="page-139-0"></span>

| Threats to the key man<br>agement system |                               | Protection<br>demand | Comments                                                                                                                                                                                                                                                    |
|------------------------------------------|-------------------------------|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                          |                               |                      | 6<br>Fault in power supply<br>7<br>Interruption of the link to the central sys<br>tem<br>8<br>Physical destruction                                                                                                                                          |
| TK5                                      | Lack of fallback so<br>lution | 3                    | The availability of the necessary key informa<br>tion is essential if the system as a whole is to<br>work at all. If the key management system mal<br>functions and there is no fallback solution, the<br>function of the entire system will be threatened. |

#### **Table 10–12 Threats relevant to the key management system**

#### **10.1.6.2 Definition of safeguards for the key management system**

Based on the relevant threats in the preceding section, this section defines general execution proposals and safeguards. These safeguards are described in detail in section [0](#page-89-1).

| Threat |                                          | Safeguards              | Safeguard                                                                                                                                                                                                                                                                                                                                                         |
|--------|------------------------------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TK1    | Insufficient key<br>data quality         | MK1.3<br>MK2.3          | 1<br>Secure generation and import of keys –<br>evaluate and certify using CC or a<br>process of the same standard<br>2<br>Introduction of key management for<br>symmetric and asymmetric keys with<br>sufficient key length – secure, flexible<br>key management concept                                                                                          |
| TK2    | Unauthorised<br>scanning of key<br>data  | MK3.3<br>MK7.3          | 1<br>Access protection for cryptographic<br>keys (read and write access) – evaluate<br>and certify using CC or a process of the<br>same standard<br>2<br>Separation of keys – separate storage<br>and handling of keys                                                                                                                                            |
| TK3    | Manipulation of<br>key data              | MK3.3<br>MK7.3<br>MK8.3 | 1<br>Access protection for cryptographic<br>keys (read and write access) – evaluate<br>and certify using CC or a process of the<br>same standard<br>2<br>Client-specific separation of keys –<br>separate storage and handling of keys<br>3<br>Loading new keys – securing the au<br>thenticity and integrity of entitlements –<br>complex authentication concept |
| TK4    | Key management<br>system malfunc<br>tion | MK4.3<br>MK5.3          | 1<br>Specifying the performance and the<br>necessary securing of the function of<br>security components – evaluation<br>2<br>Availability of key management system<br>(fallback solution) – implementation ac<br>cording to failure concept and backup<br>of keys in the Trust Centre                                                                             |

<span id="page-140-0"></span>

| Threat |                              | Safeguards     | Safeguard                                                                                                                                                                                                                                                                     |
|--------|------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TK5    | Lack of fallback<br>solution | MK5.3<br>MK6.3 | 1<br>Availability of key management system<br>(fallback solution) – implementation ac<br>cording to fallback concept and backup<br>of keys in the Trust Centre<br>2<br>Definition of action in the event of keys<br>being compromised – compromise of<br>non-diversified keys |

| Table 10–13 | Safeguards for the key management system |
|-------------|------------------------------------------|
|             |                                          |

#### **10.1.6.3 Residual risks**

For technical and commercial reasons, it is not always possible to eliminate threats completely using safeguards. In such cases a certain risk remains. This section describes the residual risk for the relevant cases.

The technical specifications of chips compatible with EPCglobal only permit limited key lengths, which may not provide secure protection against attacks. It should be considered, for each application scenario, which risks actually apply to which entities.

# **10.2 Transponders**

| Chip category                                             | Security functions                                                                                                                                                                                          | Transponder security<br>functions                                                                                                                                                                                                    | Functions                                                                                                                                                                   |
|-----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Logistics IC<br>based on<br>EPCglobal<br>Class 1 Gen<br>2 | UID (read only)<br>Write protection for<br>memory area<br>Access protection for<br>certain areas of mem<br>ory<br>Optional password pro<br>tection for writing func<br>tion<br>Password-protected<br>"Kill" | Simple visual security<br>features, such as secu<br>rity fibres, fluorescent<br>inks<br>More advanced visual<br>security features, such<br>as holograms and<br>microprint;<br>Optional: tamper<br>proofing – "peel off"<br>disabling | Working frequency<br>860–960 MHz<br>Unique identifier (UID)<br>Read/write area organ<br>ised in fixed blocks.<br>Data stored for 2 to 10<br>years<br>Data rate max. 640kbit |

| Table 10–14 | Categorisation of transponders for logistics and trade |
|-------------|--------------------------------------------------------|
|-------------|--------------------------------------------------------|

#### **10.2.1 Initialising transponders**

The initialisation of transponders follows the use case described in section [7.](#page-60-1) There are different ways of facilitating this:

- 1 Initialisation by a special service operator.
- 2 Initialisation by one of the entities in the supply chain (e.g. manufacturer).

The actual procedures and processes have to be implemented in the initialisation systems in accordance with the specifications of the transponders and the applications. Initialiser SAMs

<span id="page-141-0"></span>are often used for key management, and these have to be integrated into the initialisation system.

#### **10.2.2 Determining the protection demand for the transponder**

The choice of protection demand category is dependent on the application scenario, so it will be dealt with in section [11](#page-143-1).

#### **10.2.3 Threats to the transponder**

The following table lists threats to the transponder. The allocation of protection categories is highly dependent on the product being supported, and therefore on the application scenario concerned, so it will be dealt with in section [11.](#page-143-1)

| Threat |                                                                      | Transponder protec<br>tion demand     | Comments                                                                                                                                                                                        |
|--------|----------------------------------------------------------------------|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TT1    | Unauthorised re<br>trieval of object code                            | 1                                     | According to the EPCglobal speci<br>fications, the EPC is not protected<br>against reading. Threats that de<br>pend on reading the EPC should<br>be countered using appropriate sa<br>feguards. |
| TT2    | Unauthorised writing<br>/ manipulation of ob<br>ject code            | Dependent on appli<br>cation scenario |                                                                                                                                                                                                 |
| TT3    | Cloning of trans<br>ponder                                           | Dependent on appli<br>cation scenario |                                                                                                                                                                                                 |
| TT4    | Emulation of trans<br>ponder                                         | Dependent on appli<br>cation scenario |                                                                                                                                                                                                 |
| TT5    | Removal of trans<br>ponder                                           | Dependent on appli<br>cation scenario |                                                                                                                                                                                                 |
| TT6    | Unauthorised at<br>tachment of a trans<br>ponder                     | Dependent on appli<br>cation scenario |                                                                                                                                                                                                 |
| TT7    | Unauthorised deac<br>tivation                                        | Dependent on appli<br>cation scenario |                                                                                                                                                                                                 |
| TT8    | DoS attacks                                                          | Dependent on appli<br>cation scenario |                                                                                                                                                                                                 |
| TT9    | Transponder mal<br>function                                          | Dependent on appli<br>cation scenario |                                                                                                                                                                                                 |
| TT10   | Tracking by means<br>of unauthorised<br>scanning by third<br>parties | Dependent on appli<br>cation scenario |                                                                                                                                                                                                 |
| TT11   | Lack of fallback so<br>lution in the event of                        | Dependent on appli<br>cation scenario |                                                                                                                                                                                                 |

<span id="page-142-0"></span>

| Threat |                               | Transponder protec<br>tion demand     | Comments |
|--------|-------------------------------|---------------------------------------|----------|
|        | malfunction                   |                                       |          |
| TT12   | Manipulation of UID           | Dependent on appli<br>cation scenario |          |
| TT13   | Incorrectly gener<br>ated UID | Dependent on appli<br>cation scenario |          |

**Table 10–15 Threats relevant to the transponder** 

### **10.2.4 Definition of specific safeguards**

The allocation of safeguards is dependent on the application scenario, so it will be dealt with in section [11.](#page-143-1)

# <span id="page-143-1"></span><span id="page-143-0"></span>**11 Suggestions on executing the product-specific application scenarios**

# **11.1 The "Fast-moving consumer goods" application scenario**

#### **11.1.1 Determining the protection demand category**

The "Fast-moving consumer goods" application scenario is defined in section [9.1.](#page-118-1) A package containing eight rolls of toilet paper is fitted with a transponder and passes through the processes and use cases described in sections [6](#page-49-1) and [7](#page-60-1) in a complete system compliant with EP-Cglobal specifications.

The following aspects are of special importance when considering the system security and determining the protection demand category.

#### Requirements

- 1 The journey taken by the product from the manufacturer, through the entire supply chain, all the way to the retail outlet, must be controllable and trackable.
- 2 Its storage in the warehouse and in the retail outlet, in particular, must be able to be monitored and controlled.
- 3 The packaging generally only lasts for a few days or weeks.
- 4 Product information and post-sales services based on the transponder are not envisaged.

Commercial value, risk of product counterfeiting

The sales value is €3. The profit margin is small. There is no risk of product counterfeiting.

Use of product

- 1 Consumers are expected in the future to check this product out themselves without any interaction with the sales personnel.
- 2 The product and the transponder attached to it will only be carried by consumers on their way home.

On the basis of the criteria described in section [8.2.5](#page-79-1), the application scenario can be assigned to the following protection demand categories:

|     | Security objective         | Protection<br>demand<br>category | Criteria for allocating to protection demand categories                                                                                       |
|-----|----------------------------|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| SS1 | Technical<br>compatibility | 1                                | All system components are from the same supplier.<br>The supplier ensures that they are compatible.                                           |
|     |                            | 2                                | The system has to function with components from a<br>small number of defined suppliers. The system man<br>ager or an SI ensure compatibility. |

<span id="page-144-0"></span>

| Security objective |                                                                        | Protection<br>demand<br>category | Criteria for allocating to protection demand categories                                                                                                       |  |
|--------------------|------------------------------------------------------------------------|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
|                    |                                                                        | 3                                | Open system that has to function with components<br>from any company in the market.                                                                           |  |
| SS2                | Fallback solu                                                          | 1                                | Malfunction affects only a few transponders.                                                                                                                  |  |
|                    | tion in the<br>event of mal                                            | 2                                | Malfunction affects many transponders.                                                                                                                        |  |
|                    | function                                                               | 3                                | Malfunction affects most or all transponders.                                                                                                                 |  |
| SS3                | Intuitive, fault<br>tolerant op<br>eration                             | 1                                | A few consumers cannot operate it intuitively.                                                                                                                |  |
|                    |                                                                        | 2                                | Many consumers cannot operate it intuitively.                                                                                                                 |  |
|                    |                                                                        | 3                                | A large proportion of consumers cannot operate it in<br>tuitively.                                                                                            |  |
| SI1                | Protection of                                                          | 1                                | Only relevant for customer data systems. Will be han                                                                                                          |  |
|                    | personal data<br>in the cus                                            | 2                                | dled in chapter 10.1.5                                                                                                                                        |  |
|                    | tomer data<br>system                                                   | 3                                |                                                                                                                                                               |  |
| SI2                | Protection of<br>object code                                           | 1                                | No risk of product counterfeiting, manipulation, DoS,<br>etc.                                                                                                 |  |
|                    |                                                                        | 2                                | Product counterfeiting, manipulation, DoS, etc. causes<br>limited damage amounting to < 1% of goods value.                                                    |  |
|                    |                                                                        | 3                                | Product counterfeiting, manipulation, DoS, etc. causes<br>massive damage (danger to people, large losses of<br>sales and image, and so on).                   |  |
| SI3                | Protecting the<br>allocation of<br>object and<br>object code           | 1                                | No risk of product counterfeiting, DoS, etc.                                                                                                                  |  |
|                    |                                                                        | 2                                | Product counterfeiting, DoS, etc. causes limited dam<br>age amounting to < 1% of goods value.                                                                 |  |
|                    |                                                                        | 3                                | Product counterfeiting, DoS, etc. causes massive<br>damage (danger to people, large losses of sales and<br>image, and so on).                                 |  |
| SI4                | Protection of<br>logistical data                                       | 1                                | Low dependency on logistical data                                                                                                                             |  |
|                    |                                                                        | 2                                | Incorrect or missing logistical data causes limited<br>damage amounting to < 1% of goods value.                                                               |  |
|                    |                                                                        | 3                                | Incorrect or missing logistical data causes massive<br>damage amounting to > 1% of goods value or danger<br>to persons, significant loss of image, and so on. |  |
| SI5                | Protection<br>against DoS<br>attacks on the<br>RF system<br>components | 1                                | Low risk of DoS attacks                                                                                                                                       |  |
|                    |                                                                        | 2                                | Medium risk of DoS attacks / DoS attacks cause lim<br>ited damage amounting to < 1% of goods value.                                                           |  |
|                    |                                                                        | 3                                | High risk of DoS attacks / DoS attacks cause massive<br>damage amounting to > 1% of goods value or danger                                                     |  |

<span id="page-145-0"></span>

| Security objective |                                                                   | Protection<br>demand<br>category | Criteria for allocating to protection demand categories                                                                                                                      |  |
|--------------------|-------------------------------------------------------------------|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
|                    |                                                                   |                                  | to persons, significant loss of image, and so on.                                                                                                                            |  |
| SI6                | Protection<br>against spy<br>ing on goods<br>flow informa<br>tion | 1                                | Low risk of spying                                                                                                                                                           |  |
|                    |                                                                   | 2                                | Medium risk of spying / spying causes limited damage<br>amounting to < 1% of goods value.                                                                                    |  |
|                    |                                                                   | 3                                | High risk of spying / spying causes massive damage<br>amounting to > 1% of goods value or danger to per<br>sons, significant loss of image, and so on.                       |  |
| SI7                | Availability of<br>EPC data                                       | 1                                | Low risk of non-availability                                                                                                                                                 |  |
|                    |                                                                   | 2                                | Medium risk of non-availability / non-availability<br>causes limited damage amounting to < 1% of goods<br>value.                                                             |  |
|                    |                                                                   | 3                                | High risk of non-availability / non-availability causes<br>massive damage amounting to > 1% of goods value or<br>danger to persons, significant loss of image, and so<br>on. |  |
| SP1                | Protection of<br>personal data                                    | 1                                | Only relevant for customer data systems. Will be han                                                                                                                         |  |
|                    |                                                                   | 2                                | dled in chapter 10.1.5                                                                                                                                                       |  |
|                    |                                                                   | 3                                |                                                                                                                                                                              |  |
| SP2                | Data minimi<br>sation                                             | 1                                | Only relevant for customer data systems. Will be han                                                                                                                         |  |
|                    |                                                                   | 2                                | dled in chapter 10.1.5                                                                                                                                                       |  |
|                    |                                                                   | 3                                |                                                                                                                                                                              |  |
| SP3                | Protection<br>against the<br>creation of<br>movement<br>profiles  | 1                                | In this application scenario not relevant. A single<br>transport of the product to the place of use does not<br>allow the creation of a movement profile.                    |  |
|                    |                                                                   | 2                                |                                                                                                                                                                              |  |
|                    |                                                                   | 3                                |                                                                                                                                                                              |  |

**Table 11–1 Protection demand in the "Fast-moving consumer goods" application scenario** 

### <span id="page-145-1"></span>**11.1.2 Relevant threats**

The following table lists the threats particular to this application scenario.

| Threat |                                              | Trans<br>ponder<br>protection<br>demand | Comments                                                                                                                                    |
|--------|----------------------------------------------|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| TT1    | Unauthorised re<br>trieval of object<br>code | 2                                       | According to the EPCglobal specifications, the<br>EPC is not protected against reading. Threats<br>that depend on reading the EPC should be |

| Threat |                                                                      | Trans<br>ponder<br>protection<br>demand | Comments                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------|----------------------------------------------------------------------|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        |                                                                      |                                         | countered using appropriate safeguards.                                                                                                                                                                                                                                                                                                                                                                               |
| TT2    | Unauthorised writ<br>ing / manipulation<br>of object code            | 2                                       |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| TT3    | Cloning of trans<br>ponder                                           | 2                                       | Unauthorised cloning of genuine transponders<br>would permit activities such as putting counter<br>feit products into circulation, simulating the ex<br>istence of goods in a warehouse or retail out<br>let, redeeming guarantee services illegitimately<br>and so on. If a genuine transponder can be<br>removed or deactivated (TT5, TT6, TT7) then<br>"relabelling" is also possible.                             |
| TT4    | Emulation of trans<br>ponder                                         | 2                                       | The emulation of genuine transponders per<br>mits activities such as simulating the existence<br>of goods in a warehouse or retail outlet. If a<br>genuine transponder can be removed or deac<br>tivated (TT5, TT7) then "relabelling" may also<br>be possible. Unlike in TT3, counterfeit products<br>cannot be put into circulation by emulation.<br>That is why the protection demand is reduced<br>to category 1. |
| TT5    | Removal of trans<br>ponder                                           | 2                                       | Removing the transponder can remove the as<br>sociation between the object and the object<br>code. A combination of TT5 and TT6 could en<br>able the swapping of object codes.                                                                                                                                                                                                                                        |
| TT6    | Unauthorised at<br>tachment of a<br>transponder                      | 2                                       | Attaching a new transponder to an object<br>would enable a new code to be given to that<br>object. A combination of TT5 and TT6 could<br>enable the swapping of object codes.                                                                                                                                                                                                                                         |
| TT7    | Unauthorised deac<br>tivation                                        | 2                                       | The unauthorised use of the kill function can<br>permanently deactivate the transponder. Me<br>chanical destruction is another conceivable<br>method of attack. The deactivation or removal<br>(TT5) of a genuine transponder is the prereq<br>uisite for attacks TT6, TT4 and TT3.                                                                                                                                   |
| TT8    | DoS attacks                                                          | 1                                       | In addition to the scenario in TT7, a trans<br>ponder can also be destroyed mechanically or<br>by EMP.                                                                                                                                                                                                                                                                                                                |
| TT9    | Transponder mal<br>function                                          | 3                                       |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| TT10   | Tracking by means<br>of unauthorised<br>scanning by third<br>parties | -                                       | Threat not relevant in this application scenario.<br>Transporting the product to its place of use<br>does not allow a profile to be generated.                                                                                                                                                                                                                                                                        |

<span id="page-147-0"></span>

| Threat |                                                              | Trans<br>ponder<br>protection<br>demand | Comments                                                                                                                         |
|--------|--------------------------------------------------------------|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| TT11   | Lack of fallback so<br>lution in the event<br>of malfunction | 2                                       |                                                                                                                                  |
| TT12   | Manipulation of UID                                          | 2                                       | The possibility of writing or manipulating the<br>UID of a transponder is the prerequisite for<br>creating a cloned transponder. |
| TT13   | Incorrectly gener<br>ated UID                                | 2                                       | See TT12                                                                                                                         |

#### **Table 11–2 Threats relevant to the "Fast-moving consumer goods" application scenario**

### **11.1.3 Definition of specific safeguards**

Based on the relevant threats in the preceding section, this section defines specific safeguards. It discusses the threats described for the following use cases:

| Use cases                                                        | Trans<br>ponder<br>type | Comments                                                      |
|------------------------------------------------------------------|-------------------------|---------------------------------------------------------------|
| Manufacture and delivery<br>of the chip                          | EPC<br>global           | relevant                                                      |
| Manufacture and delivery<br>of the transponder                   | EPC<br>global           | Relevant                                                      |
| Producing and issuing the<br>EPC Manager                         | EPC<br>global           | Relevant                                                      |
| Individualising the trans<br>ponder                              | EPC<br>global           | Relevant                                                      |
| Setting the kill password                                        | EPC<br>global           | Relevant if EPC chip is to be used with the kill<br>function. |
| Attaching transponder to<br>object                               | EPC<br>global           | Relevant                                                      |
| Reading the data stored in<br>the transponder                    | EPC<br>global           | Not relevant to EPC. There is no other data.                  |
| Activating the kill com<br>mand                                  | EPC<br>global           | Relevant if the kill function is to be used.                  |
| Authenticating the trans<br>ponder for verifying genu<br>ineness | EPC<br>global           | Not relevant                                                  |

<span id="page-148-0"></span>

| Use cases            | Trans<br>ponder<br>type | Comments                                         |
|----------------------|-------------------------|--------------------------------------------------|
| Key and password man | EPC                     | Relevant if EPC chip is to be used with the kill |
| agement              | global                  | function.                                        |

| Table 11–3 | Use cases relevant to the "Fast-moving consumer goods" application |
|------------|--------------------------------------------------------------------|
|            | scenario                                                           |

The following sub-sections will define safeguards for the transponder and other system components, on the basis of the threats described and the relevant use cases.

#### Definition of safeguards

In the following table, safeguards are assigned to the threats in [Table 11–1.](#page-145-1) These safeguards are intended to compensate for those threats. These safeguards are described in section [0.](#page-89-1)

| Threat |                                                              | Safeguards     | Description of threat                                                                                                                                                                           |
|--------|--------------------------------------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TT1    | Unauthorised re<br>trieval of object<br>code                 |                | 1<br>A read access protection is not avail<br>able for EPC according to actual EP<br>Cglobal specification.                                                                                     |
| TT2    | Unauthorised<br>writing / manipu<br>lation of object<br>code | MT1.2          | 1<br>Hardware and software access protec<br>tion for the EPC (write access) – write<br>protection for EPC                                                                                       |
| TT3    | Cloning of trans<br>ponder                                   | MT1.2<br>MT2.2 | 1<br>Hardware and software access protec<br>tion for the EPC (write access) – write<br>protection for EPC                                                                                       |
|        |                                                              |                | 2<br>Protection against cloning of trans<br>ponder – simple emulation protection<br>using UID                                                                                                   |
| TT4    | Emulation of<br>transponder                                  | MT3.2          | 1<br>Hardware and software access protec<br>tion for the EPC (write access) – write<br>protection for EPC                                                                                       |
|        |                                                              |                | 2<br>Protection against emulation – simple<br>emulation protection using UID                                                                                                                    |
| TT5    | Removal of trans<br>ponder                                   | MT4.2          | 1<br>Protection against removal of trans<br>ponder – low-level protection                                                                                                                       |
| TT6    | Unauthorised at<br>tachment of a<br>transponder              | MT5.2          | 1<br>Protection against unauthorised at<br>tachment of a transponder – low-level<br>protection                                                                                                  |
| TT7    | Unauthorised de<br>activation                                | MT6.2<br>MK6.2 | 1<br>Protection against the unauthorised de<br>activation of a transponder – password<br>protection for the kill command<br>2<br>Definition of action in the event of keys<br>being compromised |
| TT8    | DoS attacks                                                  | MT7.1          | 1<br>Protection against DoS attacks on the                                                                                                                                                      |

<span id="page-149-0"></span>

| Threat |                                                                       | Safeguards     | Description of threat                                                                                                                                                                                                                |  |
|--------|-----------------------------------------------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
|        |                                                                       | MT8.1          | transponder – basic protection of the<br>transponder against DoS attacks<br>2<br>Specifications defining transponder<br>characteristics – manufacturer's decla<br>ration                                                             |  |
| TT9    | Transponder mal<br>function                                           | MT8.3          | 1<br>Specifications defining transponder<br>characteristics – manufacturer's decla<br>ration                                                                                                                                         |  |
| TT10   | Tracking by<br>means of unau<br>thorised scanning<br>by third parties | --             | 1<br>Threat not relevant in this application<br>scenario. Transporting the product to its<br>place of use does not allow a profile to<br>be generated.                                                                               |  |
| TT11   | Lack of fallback<br>solution in the<br>event of malfunc<br>tion       | MT7.2<br>MT9.2 | 1<br>Protection against DoS attacks on the<br>transponder – basic protection of the<br>transponder against DoS attacks<br>2<br>Fallback solution for transponder mal<br>function – introduction of appropriate<br>fallback solutions |  |
| TT12   | Manipulation of<br>UID                                                | MT2.2          | 1<br>Protection against cloning of trans<br>ponder – protection of the transponder<br>against cloning                                                                                                                                |  |
| TT13   | Incorrectly gener<br>ated UID                                         | MT2.2          | 1<br>Protection against cloning of trans<br>ponder – protection of the transponder<br>against cloning                                                                                                                                |  |

#### **Table 11–4 Safeguards for the "Fast-moving consumer goods" application scenario**

<span id="page-149-1"></span>The grey highlight means that, even after the safeguards have been applied, a risk remains which must be considered.

Note: [Table 11–4](#page-149-1) shows that safeguards are not needed against the generation of movement profiles and their allocation to people. MT10 and MT11 are not used. The chip can remain active after the sale. A chip without a kill function is therefore sufficient in this case; in fact, using a chip of this kind has the advantage of avoiding threat TT7 altogether. Furthermore, key management would then also be unnecessary in this application scenario.

### **11.1.4 Residual risks**

For technical and commercial reasons, it is not always possible to eliminate threats completely using safeguards. In such cases a certain risk remains. This section describes the residual risk for the relevant cases.

# <span id="page-150-0"></span>**11.2 The "consumer electronics" application scenario**

#### **11.2.1 Determining the protection demand category**

The "consumer electronics" application scenario is defined in section [9.2.](#page-119-1) A high-value, flatscreen TV is fitted with a transponder and passes through the processes and use cases described in sections [6](#page-49-1) and [7](#page-60-1) in a complete system compliant with EPCglobal specifications.

The following aspects are of special importance when considering the system security and determining the protection demand category.

Requirements

- 1 The journey taken by the flat-screen TV from the manufacturer, through the entire supply chain, all the way to the retail outlet, must be controllable and trackable.
- 2 Its storage in the warehouse and in the retail outlet must be able to be monitored and controlled.
- 3 Additional services such as product information and cross-selling are to be provided in the retail outlet using RFID technology (see section [2.2](#page-20-1)).
- 4 Following purchase, the RFID technology must support paperless guarantee handling and paperless exchange procedures, and provide a proof of purchase. The transponder should also serve to identify the appliance after sale for the purpose of firmware updates, identifying the right accessories, and so on.
- 5 How long the transponder has to last depends on the length of time for which the suit will be used; this could be more than 10 years.

Commercial value, risk of product counterfeiting

The sales value is €1,000–4,000. There is a considerable risk of product counterfeiting.

Use of product

- 1 Consumers are not expected to check this product out themselves without any interaction with the sales personnel.
- 2 The product and the attached transponder is transported to the customer, where it remains.

On the basis of the criteria described in section [8.2.5](#page-79-1), the application scenario can be assigned to the following protection demand categories:

|     | Security objective         | Protection<br>demand<br>category | Criteria for allocating to protection demand categories                                                                                                     |
|-----|----------------------------|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SS1 | Technical<br>compatibility | 1                                | All system components are from the same supplier.<br>The supplier ensures that they are compatible.                                                         |
|     |                            | 2                                | The system has to function with components from a<br>small number of defined suppliers. The system man<br>ager or a system integrator ensure compatibility. |
|     |                            | 3                                | Open system that has to function with components<br>from any company in the market.                                                                         |

| Security objective                                                            |                             | Protection<br>demand<br>category                                                                                                                               | Criteria for allocating to protection demand categories                                                                                                       |
|-------------------------------------------------------------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SS2                                                                           | Fallback solu               | 1                                                                                                                                                              | Malfunction affects only a few transponders.                                                                                                                  |
| tion in the<br>event of mal                                                   |                             | 2                                                                                                                                                              | Malfunction affects many transponders.                                                                                                                        |
|                                                                               | function                    | 3                                                                                                                                                              | Malfunction affects most or all transponders.                                                                                                                 |
| SS3                                                                           | Intuitive, fault            | 1                                                                                                                                                              | A few consumers cannot operate it intuitively.                                                                                                                |
|                                                                               | tolerant op<br>eration      | 2                                                                                                                                                              | Many consumers cannot operate it intuitively.                                                                                                                 |
|                                                                               |                             | 3                                                                                                                                                              | A large proportion of consumers cannot operate it in<br>tuitively.                                                                                            |
| SI1                                                                           | Protection of               | 1                                                                                                                                                              | Only relevant for customer data systems. Will be han                                                                                                          |
|                                                                               | personal data<br>in the cus | 2                                                                                                                                                              | dled in chapter 10.1.5                                                                                                                                        |
| tomer data<br>system                                                          | 3                           |                                                                                                                                                                |                                                                                                                                                               |
| SI2<br>Protection of<br>object code                                           | 1                           | No risk of product counterfeiting, manipulation, DoS,<br>etc.                                                                                                  |                                                                                                                                                               |
|                                                                               |                             | 2                                                                                                                                                              | Product counterfeiting, manipulation, DoS, etc. causes<br>limited damage amounting to < 1% of goods value.                                                    |
|                                                                               |                             | 3                                                                                                                                                              | Product counterfeiting, manipulation, DoS, etc. causes<br>massive damage (danger to people, large losses of<br>sales and image, and so on).                   |
| SI3                                                                           | Protecting the              | 1                                                                                                                                                              | No risk of product counterfeiting, DoS, etc.                                                                                                                  |
| allocation of<br>object and<br>object code                                    | 2                           | Product counterfeiting, DoS, etc. causes limited dam<br>age amounting to < 1% of goods value.                                                                  |                                                                                                                                                               |
|                                                                               |                             | 3                                                                                                                                                              | Product counterfeiting, DoS, etc. causes massive<br>damage (danger to people, large losses of sales and<br>image, and so on).                                 |
| SI4<br>Protection of<br>logistical data                                       | 1                           | Low dependency on logistical data                                                                                                                              |                                                                                                                                                               |
|                                                                               | 2                           | Incorrect or missing logistical data causes limited<br>damage amounting to < 1% of goods value.                                                                |                                                                                                                                                               |
|                                                                               |                             | 3                                                                                                                                                              | Incorrect or missing logistical data causes massive<br>damage amounting to > 1% of goods value or danger<br>to persons, significant loss of image, and so on. |
| SI5<br>Protection<br>against DoS<br>attacks on the<br>RF system<br>components |                             | 1                                                                                                                                                              | Low risk of DoS attacks                                                                                                                                       |
|                                                                               |                             | 2                                                                                                                                                              | Medium risk of DoS attacks / DoS attacks cause lim<br>ited damage amounting to < 1% of goods value.                                                           |
|                                                                               | 3                           | High risk of DoS attacks / DoS attacks cause massive<br>damage amounting to > 1% of goods value or danger<br>to persons, significant loss of image, and so on. |                                                                                                                                                               |

<span id="page-152-0"></span>

| Security objective |                                                                   | Protection<br>demand<br>category | Criteria for allocating to protection demand categories                                                                                                                      |  |
|--------------------|-------------------------------------------------------------------|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| SI6                | Protection<br>against spy<br>ing on goods<br>flow informa<br>tion | 1                                | Low risk of spying                                                                                                                                                           |  |
|                    |                                                                   | 2                                | Medium risk of spying / spying causes limited damage<br>amounting to < 1% of goods value.                                                                                    |  |
|                    |                                                                   | 3                                | High risk of spying / spying causes massive damage<br>amounting to > 1% of goods value or danger to per<br>sons, significant loss of image, and so on.                       |  |
| SI7                | Availability of<br>EPC data                                       | 1                                | Low risk of non-availability                                                                                                                                                 |  |
|                    |                                                                   | 2                                | Medium risk of non-availability / non-availability<br>causes limited damage amounting to < 1% of goods<br>value.                                                             |  |
|                    |                                                                   | 3                                | High risk of non-availability / non-availability causes<br>massive damage amounting to > 1% of goods value or<br>danger to persons, significant loss of image, and so<br>on. |  |
| SP1                | Protection of<br>personal data                                    | 1                                | Only relevant for customer data systems. Will be han                                                                                                                         |  |
|                    |                                                                   | 2                                | dled in chapter 10.1.5                                                                                                                                                       |  |
|                    |                                                                   | 3                                |                                                                                                                                                                              |  |
| SP2                | Data minimi<br>sation                                             | 1                                | Only relevant for customer data systems. Will be han                                                                                                                         |  |
|                    |                                                                   | 2                                | dled in chapter 10.1.5                                                                                                                                                       |  |
|                    |                                                                   | 3                                |                                                                                                                                                                              |  |
| SP3                | Protection<br>against the<br>creation of<br>movement<br>profiles  | 1                                | In this application scenario not relevant. A single<br>transport of the product to the place of use does not<br>allow the creation of a movement profile.                    |  |
|                    |                                                                   | 2                                |                                                                                                                                                                              |  |
|                    |                                                                   | 3                                |                                                                                                                                                                              |  |

| Table 11–5 | Protection demand in the "consumer electronics" application scenario |  |
|------------|----------------------------------------------------------------------|--|
|            |                                                                      |  |

### <span id="page-152-1"></span>**11.2.2 Relevant threats**

The following table lists the threats particular to this application scenario.

| Threat |                                              | Trans<br>ponder<br>protection<br>demand | Comments                                                                                                                                                                               |
|--------|----------------------------------------------|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TT1    | Unauthorised re<br>trieval of object<br>code | 2                                       | According to the EPCglobal specifications, the<br>EPC is not protected against reading. Threats<br>that depend on reading the EPC should be<br>countered using appropriate safeguards. |

| Threat |                                                                      | Trans<br>ponder<br>protection<br>demand | Comments                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------|----------------------------------------------------------------------|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TT2    | Unauthorised writ<br>ing / manipulation<br>of object code            | 3                                       |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| TT3    | Cloning of trans<br>ponder                                           | 3                                       | Unauthorised cloning of genuine transponders<br>would permit activities such as putting counter<br>feit products into circulation, simulating the ex<br>istence of goods in a warehouse or retail out<br>let, redeeming guarantee services illegitimately<br>and so on. If a genuine transponder can be<br>removed or deactivated (TT5, TT6, TT7) then<br>"relabelling" is also possible.                             |
| TT4    | Emulation of trans<br>ponder                                         | 3                                       | The emulation of genuine transponders per<br>mits activities such as simulating the existence<br>of goods in a warehouse or retail outlet. If a<br>genuine transponder can be removed or deac<br>tivated (TT5, TT7) then "relabelling" may also<br>be possible. Unlike in TT3, counterfeit products<br>cannot be put into circulation by emulation.<br>That is why the protection demand is reduced<br>to category 1. |
| TT5    | Removal of trans<br>ponder                                           | 3                                       | Removing the transponder can remove the as<br>sociation between the object and the object<br>code. A combination of TT5 and TT6 could en<br>able the swapping of object codes.                                                                                                                                                                                                                                        |
| TT6    | Unauthorised at<br>tachment of a<br>transponder                      | 3                                       | Attaching a new transponder to an object<br>would enable a new code to be given to that<br>object. A combination of TT5 and TT6 could<br>enable the swapping of object codes.                                                                                                                                                                                                                                         |
| TT7    | Unauthorised deac<br>tivation                                        | 3                                       | The unauthorised use of the kill function can<br>permanently deactivate the transponder. Me<br>chanical destruction is another conceivable<br>method of attack. The deactivation or removal<br>(TT5) of a genuine transponder is the prereq<br>uisite for attacks TT6, TT4 and TT3.                                                                                                                                   |
| TT8    | DoS attacks                                                          | 3                                       | In addition to the scenario in TT7, a trans<br>ponder can also be destroyed mechanically or<br>by EMP.                                                                                                                                                                                                                                                                                                                |
| TT9    | Transponder mal<br>function                                          | 3                                       |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| TT10   | Tracking by means<br>of unauthorised<br>scanning by third<br>parties | --                                      | Threat not relevant in this application scenario.<br>Transporting the product to its place of use<br>does not allow a profile to be generated.                                                                                                                                                                                                                                                                        |
| TT11   | Lack of fallback so-                                                 | 2                                       |                                                                                                                                                                                                                                                                                                                                                                                                                       |

<span id="page-154-0"></span>

| Threat |                                       | Trans<br>ponder<br>protection<br>demand | Comments                                                                                                                         |
|--------|---------------------------------------|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
|        | lution in the event<br>of malfunction |                                         |                                                                                                                                  |
| TT12   | Manipulation of UID                   | 3                                       | The possibility of writing or manipulating the<br>UID of a transponder is the prerequisite for<br>creating a cloned transponder. |
| TT13   | Incorrectly gener<br>ated UID         | 3                                       | See TT12                                                                                                                         |

**Table 11–6 Threats relevant to the "consumer electronics" application scenario** 

### **11.2.3 Definition of specific safeguards**

Based on the relevant threats in the preceding section, this section defines specific safeguards. It discusses the threats described for the following use cases:

| Use cases                                                        | Trans<br>ponder<br>type | Comments                                                      |
|------------------------------------------------------------------|-------------------------|---------------------------------------------------------------|
| Manufacture and delivery<br>of the chip                          | EPC<br>global           | Relevant                                                      |
| Manufacture and delivery<br>of the transponder                   | EPC<br>global           | Relevant                                                      |
| Producing and issuing the<br>EPC Manager                         | EPC<br>global           | Relevant                                                      |
| Individualising the trans<br>ponder                              | EPC<br>global           | Relevant                                                      |
| Setting the kill password                                        | EPC<br>global           | Relevant if EPC chip is to be used with the kill<br>function. |
| Attaching transponder to<br>object                               | EPC<br>global           | Relevant                                                      |
| Reading the data stored in<br>the transponder                    | EPC<br>global           | Relevant                                                      |
| Activating the kill com<br>mand                                  | EPC<br>global           | Relevant if the kill function is to be used.                  |
| Authenticating the trans<br>ponder for verifying genu<br>ineness | EPC<br>global           | Relevant                                                      |
| Key and password man<br>agement                                  | EPC<br>global           | Relevant if EPC chip is to be used with the kill<br>function. |

**Table 11–7 Use cases relevant to the "consumer electronics" application scenario** 

The following sub-sections will define safeguards for the transponder and other system components, on the basis of the threats described and the relevant use cases.

#### Definition of safeguards

In the following table, safeguards are assigned to the threats in [Table 11–5.](#page-152-1) These safeguards are intended to compensate for those threats. These safeguards are described in section [0.](#page-89-1)

| Threat |                                                              | Safeguards     | Description of threat                                                                                                                                                                                                                                      |  |
|--------|--------------------------------------------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| TT1    | Unauthorised re<br>trieval of object<br>code                 |                | 1<br>A read access protection is not avail<br>able for EPC according to actual EP<br>Cglobal specification.                                                                                                                                                |  |
| TT2    | Unauthorised<br>writing / manipu<br>lation of object<br>code | MT1.3          | 1<br>Hardware and software access protec<br>tion for the EPC (write access) – write<br>protection for EPC                                                                                                                                                  |  |
| TT3    | Cloning of trans<br>ponder                                   | MT1.3<br>MT2.3 | 1<br>Hardware and software access protec<br>tion for the EPC (write access) – write<br>protection for EPC                                                                                                                                                  |  |
|        |                                                              |                | 2<br>Protection against cloning of trans<br>ponder – advanced protection of the<br>transponder against cloning                                                                                                                                             |  |
| TT4    | Emulation of<br>transponder                                  | MT3.3          | 1<br>Hardware and software access protec<br>tion for the EPC (write access) – write<br>protection for EPC                                                                                                                                                  |  |
|        |                                                              |                | 2<br>Protection against emulation – simple<br>emulation protection using UID                                                                                                                                                                               |  |
| TT5    | Removal of trans<br>ponder                                   | MT4.3          | 1<br>Protection against removal of trans<br>ponder – specially safeguarded at<br>tachment                                                                                                                                                                  |  |
| TT6    | Unauthorised at<br>tachment of a<br>transponder              | MT5.3          | 1<br>Protection against unauthorised at<br>tachment of a transponder – high-level<br>protection                                                                                                                                                            |  |
| TT7    | Unauthorised de<br>activation                                | MT6.3<br>MK6.3 | 1<br>Protection against the unauthorised de<br>activation of a transponder – password<br>protection for the kill command<br>2<br>Definition of action in the event of keys<br>being compromised                                                            |  |
| TT8    | DoS attacks                                                  | MT7.3<br>MT8.3 | 1<br>Protection against DoS attacks on the<br>transponder – advanced protection of<br>the transponder against DoS attacks<br>2<br>Specifications defining transponder<br>characteristics – interoperability tests<br>according to test concept, evaluation |  |
| TT9    | Transponder mal<br>function                                  | MT8.3          | 1<br>Specifications defining transponder<br>characteristics – manufacturer's decla<br>ration                                                                                                                                                               |  |

<span id="page-156-0"></span>

| Threat |                                                                       | Safeguards     | Description of threat                                                                                                                                                                                                                |
|--------|-----------------------------------------------------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TT10   | Tracking by<br>means of unau<br>thorised scanning<br>by third parties | --             | 1<br>Threat not relevant in this application<br>scenario. Transporting the product to its<br>place of use does not allow a profile to<br>be generated.                                                                               |
| TT11   | Lack of fallback<br>solution in the<br>event of malfunc<br>tion       | MT7.2<br>MT9.2 | 1<br>Protection against DoS attacks on the<br>transponder – basic protection of the<br>transponder against DoS attacks<br>2<br>Fallback solution for transponder mal<br>function – introduction of appropriate<br>fallback solutions |
| TT12   | Manipulation of<br>UID                                                | MT2.3          | 1<br>Protection against cloning of trans<br>ponder – advanced protection of the<br>transponder against cloning                                                                                                                       |
| TT13   | Incorrectly gener<br>ated UID                                         | MT2.3          | 1<br>Protection against cloning of trans<br>ponder – advanced protection of the<br>transponder against cloning                                                                                                                       |

#### **Table 11–8 Safeguards for the "consumer electronics" application scenario**

The grey highlight means that, even after the safeguards have been applied, a risk remains which must be considered.

Note: [Table 11–4](#page-149-1) shows that safeguards are not needed against the generation of movement profiles and their allocation to people. MT10 and MT11 are not used. The chip can remain active after the sale. A chip without a kill function is therefore sufficient in this case; in fact, using a chip of this kind has the advantage of avoiding threat TT7 altogether. Furthermore, key management would then also be unnecessary in this application scenario.

#### **11.2.4 Residual risks**

For technical and commercial reasons, it is not always possible to eliminate threats completely using safeguards. In such cases a certain risk remains. This section describes the residual risk for the relevant cases.

In this application scenario, risks still exist after applying the safeguards mentioned in [Table](#page-164-1)  [11–13](#page-164-1) to compensate for threats TT7 and TT10. These are described in the following.

#### **11.2.4.1 Residual risks arising from "unauthorised deactivation of the transponder"**

#### Description of risk

The transponders currently available on the market and compliant with EPCglobal specifications include 32-bit passwords or similar. When the kill command is set and activated, this password is transmitted unprotected between the reader and the transponder. An attacker also has the following possibilities of gaining access to the password:

- 1 Eavesdropping on communication between reader and transponder when the password is loaded and when the kill command is used.
- 2 Brute-force attacks on the transponder, which involve trying out possible passwords until the kill command is successfully activated. The transponder is then deactivated. Be-

<span id="page-157-0"></span>cause of the read-times of currently available transponders, a brute-force attack can take more than a whole year.

- 3 Attacks on the key management system or other system components (such as readers) which store and handle passwords.
- 4 Attacks on individualised EPC chips.

#### Potential effects

- 1 Successful attack on the availability of logistics data. This would also compromise protection against counterfeiting.
- 2 Successful attack on the availability of post-sales services.

| Entities that could be<br>affected                                   | Security objectives<br>which could be affected                                                                                                      | Assessment                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| All of the entities in the<br>supply chain, especially<br>retailers. | A successful unauthor<br>ised deactivation of the<br>transponder would im<br>pair information security<br>by blocking the avail<br>ability of data. | There is only a risk if passwords are<br>not diversified, since if they are not<br>then more than one transponder could<br>be deactivated with the knowledge of<br>one single password                                                      |
| Customers, if post<br>sales services are<br>agreed on.               | Privacy is not impaired.                                                                                                                            | All in all, however, the risk is low,<br>since an attacker is unlikely to be able<br>to draw commercial benefit from a<br>DoS attack of this kind. There is,<br>however, the risk of isolated attacks<br>aimed at gaining public attention. |

Overview

**Table 11–9 Remaining risks for the "consumer electronics" application scenario** 

# **11.3 The "brand-name clothing" application scenario**

#### **11.3.1 Determining the protection demand category**

The "brand-name clothing" application scenario is defined in section [9.3](#page-120-1). A high-value men's suit made by a brand-name manufacturer is fitted with a transponder and passes through the processes and use cases described in sections [6](#page-49-1) and [7](#page-60-1) in a complete system compliant with EPCglobal specifications.

The following aspects are of special importance when considering the system security and determining the protection demand category.

Requirements

1 The journey taken by the men's suit from the manufacturer, through the entire supply chain, all the way to the retail outlet, must be controllable and trackable. Furthermore, its storage in the warehouse and in the retail outlet must be able to be monitored and controlled.

- 2 Additional services such as product information and cross-selling are to be provided in the retail outlet using RFID technology (see section 2.2).
- 3 Following purchase, the RFID technology must support paperless guarantee handling and paperless exchange procedures, and provide a proof of purchase.
- 4 How long the transponder has to last depends on the length of time for which the suit will be used; this could be more than ten years.

Commercial value, risk of product counterfeiting

The sales value is €700–1,000. There is a considerable risk of product counterfeiting.

Use of product

- 1 Consumers are not expected to check this product out themselves without any interaction with the sales personnel.
- 2 The product and the transponder attached to it will be carried around by the consumer for a long period of time.

On the basis of the criteria described in section [8.2.5](#page-79-1), the application scenario can be assigned to the following protection demand categories:

| Security objective |                                                                     | Protec<br>tion de<br>mand<br>category | Criteria for allocating to protection demand catego<br>ries                                                                                  |
|--------------------|---------------------------------------------------------------------|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| SS1                | Technical<br>compatibility                                          | 1                                     | All system components are from the same supplier.<br>The supplier ensures that they are compatible.                                          |
|                    |                                                                     | 2                                     | The system has to function with components from a<br>small number of defined suppliers. The system<br>manager or an SI ensure compatibility. |
|                    |                                                                     | 3                                     | Open system that has to function with components<br>from any company in the market.                                                          |
| SS2                | Fallback so<br>lution in the<br>event of mal<br>function            | 1                                     | Malfunction affects only a few transponders.                                                                                                 |
|                    |                                                                     | 2                                     | Malfunction affects many transponders.                                                                                                       |
|                    |                                                                     | 3                                     | Malfunction affects most or all transponders.                                                                                                |
| SS3                | Intuitive,<br>fault-tolerant<br>operation                           | 1                                     | A few consumers cannot operate it intuitively.                                                                                               |
|                    |                                                                     | 2                                     | Many consumers cannot operate it intuitively.                                                                                                |
|                    |                                                                     | 3                                     | A large proportion of consumers cannot operate it<br>intuitively.                                                                            |
| SI1                | Protection of<br>personal<br>data in the<br>customer<br>data system | 1                                     | Only relevant for customer data systems. Will be<br>handled in chapter 10.1.5                                                                |
|                    |                                                                     | 2                                     |                                                                                                                                              |
|                    |                                                                     | 3                                     |                                                                                                                                              |
| SI2                | Protection of<br>object code                                        | 1                                     | No risk of product counterfeiting, manipulation, DoS,<br>etc.                                                                                |

<span id="page-159-0"></span>

| Security objective |                                                                             | Protec<br>tion de<br>mand<br>category | Criteria for allocating to protection demand catego<br>ries                                                                                                        |
|--------------------|-----------------------------------------------------------------------------|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                    |                                                                             | 2                                     | Product counterfeiting, manipulation, DoS, etc.<br>causes limited damage amounting to < 1% of goods<br>value.                                                      |
|                    |                                                                             | 3                                     | Product counterfeiting, manipulation, DoS, etc.<br>causes massive damage (danger to people, large<br>losses of sales and image, and so on).                        |
| SI3                | Protecting<br>the allocation<br>of object and<br>object code                | 1                                     | No risk of product counterfeiting, DoS, etc.                                                                                                                       |
|                    |                                                                             | 2                                     | Product counterfeiting, DoS, etc. causes limited<br>damage amounting to < 1% of goods value.                                                                       |
|                    |                                                                             | 3                                     | Product counterfeiting, DoS, etc. causes massive<br>damage (danger to people, large losses of sales<br>and image, and so on).                                      |
| SI4                | Protection of                                                               | 1                                     | Low dependency on logistical data                                                                                                                                  |
|                    | logistical<br>data                                                          | 2                                     | Incorrect or missing logistical data causes limited<br>damage amounting to < 1% of goods value.                                                                    |
|                    |                                                                             | 3                                     | Incorrect or missing logistical data causes massive<br>damage amounting to > 1% of goods value or dan<br>ger to persons, significant loss of image, and so on.     |
| SI5                | Protection<br>against DoS<br>attacks on<br>the RF sys<br>tem compo<br>nents | 1                                     | Low risk of DoS attacks                                                                                                                                            |
|                    |                                                                             | 2                                     | Medium risk of DoS attacks / DoS attacks cause<br>limited damage amounting to < 1% of goods value.                                                                 |
|                    |                                                                             | 3                                     | High risk of DoS attacks / DoS attacks cause mas<br>sive damage amounting to > 1% of goods value or<br>danger to persons, significant loss of image, and so<br>on. |
| SI6                | Protection<br>against spy<br>ing on goods<br>flow informa<br>tion           | 1                                     | Low risk of spying                                                                                                                                                 |
|                    |                                                                             | 2                                     | Medium risk of spying / spying causes limited dam<br>age amounting to < 1% of goods value.                                                                         |
|                    |                                                                             | 3                                     | High risk of spying / spying causes massive dam<br>age amounting to > 1% of goods value or danger to<br>persons, significant loss of image, and so on.             |
| SI7                | Availability of<br>EPC data                                                 | 1                                     | Low risk of non-availability                                                                                                                                       |
|                    |                                                                             | 2                                     | Medium risk of non-availability / non-availability<br>causes limited damage amounting to < 1% of goods<br>value.                                                   |
|                    |                                                                             | 3                                     | High risk of non-availability / non-availability causes<br>massive damage amounting to > 1% of goods value<br>or danger to persons, significant loss of image, and |

<span id="page-160-0"></span>

| Security objective |                                                                  | Protec<br>tion de<br>mand<br>category | Criteria for allocating to protection demand catego<br>ries                   |
|--------------------|------------------------------------------------------------------|---------------------------------------|-------------------------------------------------------------------------------|
|                    |                                                                  |                                       | so on.                                                                        |
| SP1                | Protection of<br>personal<br>data                                | 1                                     | Only relevant for customer data systems. Will be<br>handled in chapter 10.1.5 |
|                    |                                                                  | 2                                     |                                                                               |
|                    |                                                                  | 3                                     |                                                                               |
| SP2                | Data minimi<br>sation                                            | 1                                     | Only relevant for customer data systems. Will be<br>handled in chapter 10.1.5 |
|                    |                                                                  | 2                                     |                                                                               |
|                    |                                                                  | 3                                     |                                                                               |
| SP3                | Protection<br>against the<br>creation of<br>movement<br>profiles | 1                                     | Customer's reputation is damaged.                                             |
|                    |                                                                  | 2                                     | Customer's social existence is damaged.                                       |
|                    |                                                                  | 3                                     | Customer's physical existence is damaged.                                     |

**Table 11–10 Protection demand in the "brand-name clothing" application scenario** 

### <span id="page-160-1"></span>**11.3.2 Relevant threats**

The following table lists the threats particular to this application scenario.

| Threat |                                                           | Trans<br>ponder<br>protec<br>tion de<br>mand | Comments                                                                                                                                                                                                                                                                                                                                                                                  |
|--------|-----------------------------------------------------------|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TT1    | Unauthorised re<br>trieval of object code                 | 2                                            | According to the EPCglobal specifications, the<br>EPC is not protected against reading. Threats<br>that depend on reading the EPC should be<br>countered using appropriate safeguards.                                                                                                                                                                                                    |
| TT2    | Unauthorised writing<br>/ manipulation of ob<br>ject code | 3                                            |                                                                                                                                                                                                                                                                                                                                                                                           |
| TT3    | Cloning of trans<br>ponder                                | 3                                            | Unauthorised cloning of genuine transponders<br>would permit activities such as putting counter<br>feit products into circulation, simulating the ex<br>istence of goods in a warehouse or retail out<br>let, redeeming guarantee services illegitimately<br>and so on. If a genuine transponder can be<br>removed or deactivated (TT5, TT6, TT7) then<br>"relabelling" is also possible. |
| TT4    | Emulation of trans<br>ponder                              | 3                                            | The emulation of genuine transponders per<br>mits activities such as simulating the existence<br>of goods in a warehouse or retail outlet. If a                                                                                                                                                                                                                                           |

<span id="page-161-0"></span>

| Threat |                                                                      | Trans<br>ponder<br>protec<br>tion de<br>mand | Comments                                                                                                                                                                                                                                                                            |
|--------|----------------------------------------------------------------------|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        |                                                                      |                                              | genuine transponder can be removed or deac<br>tivated (TT5, TT7) then "relabelling" may also<br>be possible. Unlike in TT3, counterfeit products<br>cannot be put into circulation by emulation.<br>That is why the protection demand is reduced<br>to category 1.                  |
| TT5    | Removal of trans<br>ponder                                           | 3                                            | Removing the transponder can remove the as<br>sociation between the object and the object<br>code. A combination of TT5 and TT6 could en<br>able the swapping of object codes.                                                                                                      |
| TT6    | Unauthorised at<br>tachment of a trans<br>ponder                     | 3                                            | Attaching a new transponder to an object<br>would enable a new code to be given to that<br>object. A combination of TT5 and TT6 could<br>enable the swapping of object codes.                                                                                                       |
| TT7    | Unauthorised deac<br>tivation                                        | 3                                            | The unauthorised use of the kill function can<br>permanently deactivate the transponder. Me<br>chanical destruction is another conceivable<br>method of attack. The deactivation or removal<br>(TT5) of a genuine transponder is the prereq<br>uisite for attacks TT6, TT4 and TT3. |
| TT8    | DoS attacks                                                          | 3                                            | In addition to the scenario in TT7, a trans<br>ponder can also be destroyed mechanically or<br>by EMP.                                                                                                                                                                              |
| TT9    | Transponder mal<br>function                                          | 3                                            |                                                                                                                                                                                                                                                                                     |
| TT10   | Tracking by means<br>of unauthorised<br>scanning by third<br>parties | 1                                            | Relevant threat. Commercially available read<br>ers can detect someone who is wearing a suit<br>fitted with a transponder.                                                                                                                                                          |
| TT11   | Lack of fallback so<br>lution in the event of<br>malfunction         | 2                                            |                                                                                                                                                                                                                                                                                     |
| TT12   | Manipulation of UID                                                  | 3                                            | The possibility of writing or manipulating the<br>UID of a transponder is the prerequisite for<br>creating a cloned transponder.                                                                                                                                                    |
| TT13   | Incorrectly gener<br>ated UID                                        | 3                                            | See TT12                                                                                                                                                                                                                                                                            |

**Table 11–11 Threats relevant to the "brand-name clothing" application scenario** 

## <span id="page-162-0"></span>**11.3.3 Definition of specific safeguards**

Based on the relevant threats in the preceding section, this section defines specific safeguards. It discusses the threats described for the following use cases:

| Use cases                                                        | Trans<br>ponder<br>type | Comments                                                      |
|------------------------------------------------------------------|-------------------------|---------------------------------------------------------------|
| Manufacture and delivery<br>of the chip                          | EPC<br>global           | Relevant                                                      |
| Manufacture and delivery<br>of the transponder                   | EPC<br>global           | Relevant                                                      |
| Producing and issuing the<br>EPC Manager                         | EPC<br>global           | Relevant                                                      |
| Individualising the trans<br>ponder                              | EPC<br>global           | Relevant                                                      |
| Setting the kill password                                        | EPC<br>global           | Relevant if EPC chip is to be used with the kill<br>function. |
| Attaching transponder to<br>object                               | EPC<br>global           | Relevant                                                      |
| Reading the data stored in<br>the transponder                    | EPC<br>global           | Relevant                                                      |
| Activating the kill com<br>mand                                  | EPC<br>global           | Relevant if the kill function is to be used.                  |
| Authenticating the trans<br>ponder for verifying genu<br>ineness | EPC<br>global           | Relevant                                                      |
| Key and password man<br>EPC<br>agement<br>global                 |                         | Relevant if EPC chip is to be used with the kill<br>function. |

#### **Table 11–12 Use cases relevant to the "brand-name clothing" application scenario**

The following sub-sections will define safeguards for the transponder and other system components, on the basis of the threats described and the relevant use cases.

#### Definition of safeguards

In the following table, safeguards are assigned to the threats in [Table 11–10.](#page-160-1) These safeguards are intended to compensate for those threats. These safeguards are described in section [0.](#page-89-1)

| Threat |                                              | Safeguards | Description of threat                                                                                     |  |
|--------|----------------------------------------------|------------|-----------------------------------------------------------------------------------------------------------|--|
| TT1    | Unauthorised re<br>trieval of object<br>code | MT1.3      | 1<br>Hardware and software access protec<br>tion for the EPC (write access) – write<br>protection for EPC |  |
| TT2    | Unauthorised<br>writing / manipu             | MT1.3      | 1<br>Hardware and software access protec<br>tion for the EPC (write access) – write                       |  |

| Threat |                                                                       | Safeguards       | Description of threat                                                                                                                                                                                                                                      |
|--------|-----------------------------------------------------------------------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        | lation of object<br>code                                              |                  | protection for EPC                                                                                                                                                                                                                                         |
| TT3    | Cloning of trans<br>ponder                                            | MT1.3<br>MT2.3   | 1<br>Hardware and software access protec<br>tion for the EPC (write access) – write<br>protection for EPC<br>2<br>Protection against cloning of trans<br>ponder – advanced protection of the<br>transponder against cloning                                |
| TT4    | Emulation of<br>transponder                                           | MT3.3            | 1<br>Hardware and software access protec<br>tion for the EPC (write access) – write<br>protection for EPC<br>2<br>Protection against emulation – simple<br>emulation protection using UID                                                                  |
| TT5    | Removal of trans<br>ponder                                            | MT4.3            | 1<br>Protection against removal of trans<br>ponder – specially safeguarded at<br>tachment                                                                                                                                                                  |
| TT6    | Unauthorised at<br>tachment of a<br>transponder                       | MT5.3            | 1<br>Protection against unauthorised at<br>tachment of a transponder – high-level<br>protection                                                                                                                                                            |
| TT7    | Unauthorised de<br>activation                                         | MT6.3<br>MK6.3   | 1<br>Protection against the unauthorised de<br>activation of a transponder – password<br>protection for the kill command<br>2<br>Definition of action in the event of keys<br>being compromised                                                            |
| TT8    | DoS attacks                                                           | MT7.3<br>MT8.3   | 1<br>Protection against DoS attacks on the<br>transponder – advanced protection of<br>the transponder against DoS attacks<br>2<br>Specifications defining transponder<br>characteristics – interoperability tests<br>according to test concept, evaluation |
| TT9    | Transponder mal<br>function                                           | MT8.3            | 1<br>Specifications defining transponder<br>characteristics – manufacturer's decla<br>ration                                                                                                                                                               |
| TT10   | Tracking by<br>means of unau<br>thorised scanning<br>by third parties | MT10.1<br>MT11.1 | 1<br>Preventing the assignment of move<br>ment profiles to people – anonymity of<br>sale                                                                                                                                                                   |
| TT11   | Lack of fallback<br>solution in the<br>event of malfunc<br>tion       | MT7.2<br>MT9.2   | 1<br>Protection against DoS attacks on the<br>transponder – basic protection of the<br>transponder against DoS attacks<br>2<br>Fallback solution for transponder mal<br>function – introduction of appropriate<br>fallback solutions                       |
| TT12   | Manipulation of<br>UID                                                | MT2.3            | 1<br>Protection against cloning of trans<br>ponder – advanced protection of the<br>transponder against cloning                                                                                                                                             |

<span id="page-164-0"></span>

| Threat |                               | Safeguards | Description of threat                                                                                          |
|--------|-------------------------------|------------|----------------------------------------------------------------------------------------------------------------|
| TT13   | Incorrectly gener<br>ated UID | MT2.3      | 1<br>Protection against cloning of trans<br>ponder – advanced protection of the<br>transponder against cloning |

**Table 11–13 Safeguards for the "brand-name clothing" application scenario** 

<span id="page-164-1"></span>The grey highlight means that, even after the safeguards have been applied, a risk remains which must be considered.

#### **11.3.4 Residual risks**

For technical and commercial reasons, it is not always possible to eliminate threats completely using safeguards. In such cases a certain risk remains. This section describes the residual risk for the relevant cases.

In this application scenario, risks still exist after applying the safeguards mentioned in [Table](#page-164-1)  [11–13](#page-164-1) to compensate for threats TT7 and TT10. These are described in the following.

#### **11.3.4.1 Residual risks arising from "unauthorised deactivation of the transponder"**

#### Description of risk

The transponders currently available on the market and compliant with EPCglobal specifications include 32-bit passwords or similar. When the kill command is set and activated, this password is transmitted unprotected between the reader and the transponder. An attacker also has the following possibilities of gaining access to the password:

- 1 Eavesdropping on communication between reader and transponder when the password is loaded and when the kill command is used.
- 2 Brute-force attacks on the transponder, which involve trying out possible passwords until the kill command is successfully activated. The transponder is then deactivated. Because of the read-times of currently available transponders, a brute-force attack can take more than a whole year.
- 3 Attacks on the key management system or other system components (such as readers) which store and handle passwords.
- 4 Attacks on individualised EPC chips.

#### Potential effects

- 1 Successful attack on the availability of logistics data. This would also compromise protection against counterfeiting.
- 2 Successful attack on the availability of post-sales services.

| Entities that could be<br>affected                     | Security objectives<br>which could be affected                            | Assessment                                                                                                              |
|--------------------------------------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| All of the entities in the<br>supply chain, especially | A successful unauthor<br>ised deactivation of the<br>transponder would im | There is only a risk if passwords are<br>not diversified, since if they are not<br>then more than one transponder could |

#### Overview

<span id="page-165-0"></span>

| Entities that could be<br>affected                     | Security objectives<br>which could be affected                         | Assessment                                                                                                                                                                                                                                  |
|--------------------------------------------------------|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| retailers.                                             | pair information security<br>by blocking the avail<br>ability of data. | be deactivated with the knowledge of<br>one single password.                                                                                                                                                                                |
| Customers, if post<br>sales services are<br>agreed on. | Privacy is not impaired.                                               | All in all, however, the risk is low,<br>since an attacker is unlikely to be able<br>to draw commercial benefit from a<br>DoS attack of this kind. There is,<br>however, the risk of isolated attacks<br>aimed at gaining public attention. |

#### **Table 11–14 Remaining risks for the "brand-name clothing" application scenario**

#### **11.3.4.2 Residual risks arising from "tracking"**

#### Description of risk

EPCglobal transponders can be read from distances of up to several metres if they have not been deactivated by physical destruction or using the kill command. The EPC is not accessprotected, and can be retrieved using commercially available readers. The same also applies to the UID, which otherwise plays a minor role in the EPCglobal concept. This means it is technically possible to detect transponders that are not deactivated during sale, and to generate movement profiles for those transponders.

According to privacy laws it is illegal to generate movement profiles without a person's assent.

From the point of view of IT security, movement profiles created for objects (such as a men's suit with a transponder sewn into it) are not critical as such. However, privacy laws can be threatened if, for example, the movement profile of a men's suit can be ascribed to a natural person. It should be mentioned at this point that currently available high-quality clothing is only ever fitted with removable transponders. The scenario described here is hypothetical, since sewn-in versions are only used for clothing rentals and not for end-consumer applications.

If it is neither necessary nor intended to use the transponder after the product is sold, then it can be deactivated during sale, which would prevent the potential illegal creation of movement profiles. In this application scenario, the transponder needs to be used after sale. For this reason, safeguards are applied which prevent the allocation of any illegally created movement profiles to any personal data which may be stored in the retailer's customer data system.

There is a lot of public discussion about data collection systems such as cameras, customer data systems and RFID readers which could potentially be used to generate movement profiles. And indeed, even if safeguard MT11.1 is used, the risk remains that a retailer, or someone else with EPC-compliant readers, could create movement profiles illegally and use other channels to obtain information which could link the transponder's profile to a particular person. For instance, a transponder's movement profile could be compared with movement profiles generated using a camera-based surveillance system incorporating facial recognition. The personal link could then potentially be created by asking other people about the recorded facial image.

Potential effects

<span id="page-166-0"></span>Allocation of illegally generated movement profiles to people using information from outside the system.

| Entities that could be<br>affected | Security objectives<br>which could be affected | Assessment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------------------------|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Customer                           | Privacy                                        | The allocation of movement profiles to<br>people using information from outside<br>the system would involve, in each<br>separate instance, considerable tech<br>nical effort and manpower. If the re<br>quired safeguards are applied, then<br>scenarios involving automated alloca<br>tion are not conceivable. Whatever<br>the case, such an activity would vio<br>late existing privacy laws.                                                                                                                                                                                                                                                                                                                                                    |
|                                    |                                                | The possibility of isolated attacks<br>cannot be excluded, but they are<br>unlikely because of the difficulty and<br>expense involved, and because of the<br>legal deterrents. Widespread use for<br>purposes such as commercial gain is<br>not to be expected. This is illustrated<br>by the example of a retailer: the<br>lengths to which the retailer would<br>have to go would greatly exceed any<br>benefits that could be gained by rec<br>ognising customers. In addition, there<br>are more effective and simpler ways<br>of achieving the same thing; well<br>trained staff can judge a new cus<br>tomer's potential interest as he or she<br>enters the shop, by observing simple<br>attributes such as clothing, age and<br>appearance. |

#### **Table 11–15 Remaining risks by tracking for the "brand-name clothing" application scenario**

# <span id="page-167-0"></span>**12 List of references**

#### [RIKCHA]

Federal Office for Information Security: RFID – Security Aspects and Prospective Applications of RFID Systems, [https://www.bsi.bund.de/cln\\_174/ContentBSI/EN/publications/](https://www.bsi.bund.de/cln_174/ContentBSI/EN/publications/%0Brfid/RIKCHA_en_htm.html) [rfid/RIKCHA\\_en\\_htm.html](https://www.bsi.bund.de/cln_174/ContentBSI/EN/publications/%0Brfid/RIKCHA_en_htm.html), download from Sept. 15th 2009

#### [GSHB]

Federal Office for Information Security: IT Basic Protection Manual, [https://www.bsi.bund.de/](https://www.bsi.bund.de/%0Bcln_174/ContentBSI/grundschutz/intl/intl.html) [cln\\_174/ContentBSI/grundschutz/intl/intl.html,](https://www.bsi.bund.de/%0Bcln_174/ContentBSI/grundschutz/intl/intl.html) download from Sept. 15th 2009

#### [ISO 18000-6]

International Organization for Standardization: ISO 18000-6:2004 Information technology - Radio frequency identification for item management - Part 6: Parameters for air interface communications at 860 MHz to 960 MHz, [http://www.iso.org/iso/iso\\_catalogue.htm,](http://www.iso.org/iso/iso_catalogue.htm) download from Sept. 15th 2008

#### [CFP\_GS1]

Fälschungssicherheit mit EPC (German only), [http://www.gs1-germany.de/content/e39/e466/](http://www.gs1-germany.de/content/e39/e466/%0Be468/datei/epc_rfid/mip_faelschungssicherheit.pdf) [e468/datei/epc\\_rfid/mip\\_faelschungssicherheit.pdf](http://www.gs1-germany.de/content/e39/e466/%0Be468/datei/epc_rfid/mip_faelschungssicherheit.pdf)

#### [EPCIS]

EPC Informationsservice (EPCIS) und Umsetzung im EPCShowcase (German only), [http://www.gs1-germany.de/content/standards/epc\\_rfid/epc\\_informationsservices/](http://www.gs1-germany.de/content/standards/epc_rfid/epc_informationsservices/%0Bepc_showcase/index_ger.html) [epc\\_showcase/index\\_ger.html,](http://www.gs1-germany.de/content/standards/epc_rfid/epc_informationsservices/%0Bepc_showcase/index_ger.html) download from Sept. 15th 2008

#### [ALGK\_BSI]

Federal Office for Information Security: Technische Richtlinie Kryptographische Verfahren: Empfehlungen und Schlüssellängen (BSI TR-02102, German), [https://www.bsi.bund.de/](https://www.bsi.bund.de/%0Bcln_174/ContentBSI/Publikationen/TechnischeRichtlinien/tr02102/index_htm.html) [cln\\_174/ContentBSI/Publikationen/TechnischeRichtlinien/tr02102/index\\_htm.html,](https://www.bsi.bund.de/%0Bcln_174/ContentBSI/Publikationen/TechnischeRichtlinien/tr02102/index_htm.html) download from Sept. 15th 2009

#### [GS1-1]

GS1 Standards – Ein Lösungsportfolio weist in die Zukunft (German only), [http://www.gs1](http://www.gs1-germany.de/internet/content/e39/e466/e468/datei/ean/loesungsportfolio.pdf) [germany.de/internet/content/e39/e466/e468/datei/ean/loesungsportfolio.pdf](http://www.gs1-germany.de/internet/content/e39/e466/e468/datei/ean/loesungsportfolio.pdf), download from Sept. 15th 2008

#### [GS1-2]

GS1 Germany: AutoID-Kompendium Version 7.0 (German only), http://shop.gs1-germany.de/cgi/shop. cgi?ID=0000000000003D0000000000000000005300000000000000000000000000, download from Sept. 15th 2008

#### [GS1-3]

GS1 Germany: Prozessveränderungen durch EPC/RFID in der Supply Chain (Zentrallagerbelieferung) (German only), http://www.gs1-germany.de/internet/content/produkte/ epcglobal/downloads\_service/downloads/index\_ger.html, download from Sept. 15th 2008

[GS1-4]

GS1 Germany & IBM Deutschland: RFID-Kalkulator (German only), [http://www.gs1](http://www.gs1-germany.de/internet/content/e6/e156/e160/index_ger.html) [germany.de/internet/content/e6/e156/e160/index\\_ger.html](http://www.gs1-germany.de/internet/content/e6/e156/e160/index_ger.html), download from Sept. 15th 2008

# <span id="page-169-0"></span>**13 List of abbreviations**

| CRM    | Customer relationship management                                                      |
|--------|---------------------------------------------------------------------------------------|
| DESADV | Despatch advice                                                                       |
| DoS    | Denial of Service, attack on the availability of a service or func<br>tion.           |
| EPC    | Electronic Product Code                                                               |
| RFID   | Radio frequency identification                                                        |
| TID    | A transponder's unique identifier (Transponder Identifier), iden<br>tical to the UID. |
| UID    | Unique Identifier (of a chip)                                                         |
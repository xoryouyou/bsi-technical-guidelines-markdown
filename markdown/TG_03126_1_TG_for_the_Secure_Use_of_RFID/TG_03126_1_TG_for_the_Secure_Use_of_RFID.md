![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_2.jpeg)

Dokument ist noch aktuell. (Stand 2020)

# TG 03126 - Technical Guidelines for the Secure Use of RFID

# TG 03126-1 Application area "eTicketing in public transport"

Authors:

Cord Bartels, NXP Harald Kelter, BSI Rainer Oberweis, BSI Birger Rosenberg, NXP

Federal Office for Information Security P.O. Box 20 03 63 53133 Bonn, Germany Tel.: +49 (0) 228 99 9582 0 E-mail: rfid@bsi.bund.de Website: https://www.bsi.bund.de © Federal Office for Information Security 2009

# **Contents**

| 1     | Description of the application area for "eTicketing in public transport"                      | 12 |
|-------|-----------------------------------------------------------------------------------------------|----|
| 2     | Description of services, products and carrier media                                           | 14 |
| 3     | Agreements                                                                                    | 18 |
| 3.1   | Definition of terms                                                                           | 18 |
| 3.2   | Generic modelling of roles and entities                                                       | 19 |
| 3.3   | Allocation of roles and entities in the "eTicketing for public transport" application<br>area | 21 |
| 3.4   | Relationship between carrier media, applications and entitlements                             | 22 |
| 4     | General requirements                                                                          | 24 |
| 4.1   | Function                                                                                      | 24 |
| 4.1.1 | Customer requirements                                                                         | 24 |
| 4.1.2 | Requirements of the product provider and service provider                                     | 24 |
| 4.2   | Economy                                                                                       | 25 |
| 4.3   | Security                                                                                      | 25 |
| 5     | Method of determining security requirements                                                   | 26 |
| 5.1   | Objectives                                                                                    | 26 |
| 5.2   | Method                                                                                        | 26 |
| 5.2.1 | Scope of system considerations                                                                | 26 |
| 5.2.2 | Scalability and flexibility                                                                   | 27 |
| 5.2.3 | Structure of the Technical Guidelines                                                         | 29 |
| 5.2.4 | Explanation of the security concept                                                           | 30 |
| 6     | Generic business processes                                                                    | 32 |
| 6.1   | Process P1 "registering and ordering"                                                         | 32 |
| 6.1.1 | Setting up a customer account, purchasing personalised customer media and<br>entitlements     | 32 |
| 6.1.2 | Purchasing non-personalised carrier media and entitlements                                    | 34 |
| 6.2   | Process P2 "producing and delivering products"                                                | 35 |
| 6.2.1 | Process P2A "producing and delivering personalised carrier media and<br>entitlements"         | 35 |
| 6.2.2 | Process P2B "producing and delivering non-personalised carrier media and<br>entitlements"     | 36 |
| 6.3   | Process P3 "using an entitlement"                                                             | 37 |
| 6.4   | Process P4 "blocking entitlements, applications and carrier media"                            | 39 |
| 7     | Use cases                                                                                     | 41 |
| 7.1   | Use case "Identification when registering and ordering"                                       | 41 |
|       |                                                                                               |    |

| 7.2    | Use case "Carrier medium initialisation"                             | 41 |
|--------|----------------------------------------------------------------------|----|
| 7.3    | Use case "Application loading"                                       | 42 |
| 7.4    | Use case "Entitlement loading"                                       | 43 |
| 7.5    | Use case "Delivery"                                                  | 44 |
| 7.6    | Use case "Check-in"                                                  | 44 |
| 7.7    | Use case "Check-out"                                                 | 45 |
| 7.8    | Use case "Entitlement check"                                         | 46 |
| 7.9    | Use case "Blocking"                                                  | 47 |
| 7.10   | Use cases "Key management"                                           | 48 |
| 7.10.1 | Key management for the initialisation of carrier media<br>49         |    |
| 7.10.2 | Key management for loading and personalising applications            | 49 |
| 7.10.3 | Key management for loading entitlements                              | 50 |
| 7.10.4 | Key management for use with the service provider                     | 51 |
| 8      | Security considerations                                              | 52 |
| 8.1    | Definitions relating to security and privacy                         | 52 |
| 8.2    | Definition of the security targets                                   | 54 |
| 8.2.1  | Specific security targets for the customer                           | 54 |
|        | 8.2.1.1<br>Safety                                                    | 54 |
|        | Information security<br>8.2.1.2                                      | 55 |
|        | 8.2.1.3<br>Protection of privacy                                     | 56 |
| 8.2.2  | Specific security targets for the product provider (e.g. for CA CCP) | 56 |
|        | 8.2.2.1<br>Safety                                                    | 56 |
|        | 8.2.2.2<br>Information security                                      | 56 |
|        | 8.2.2.3<br>Protection of privacy                                     | 57 |
| 8.2.3  | Specific security targets for the service provider                   | 58 |
|        | 8.2.3.1<br>Safety                                                    | 58 |
|        | 8.2.3.2<br>Information security                                      | 58 |
|        | 8.2.3.3<br>Protection of privacy                                     | 59 |
| 8.2.4  | Summary of the entities' security targets                            | 59 |
| 8.2.5  | Formation of protection demand categories                            | 60 |
| 8.3    | Threats                                                              | 62 |
| 8.3.1  | Threats to the contact-less interface                                | 62 |
| 8.3.2  | Threats to the carrier medium                                        | 63 |
| 8.3.3  | Threats to the reader<br>64                                          |    |
| 8.3.4  | Threats to the key management system<br>65                           |    |
| 8.3.5  | Threats to the sales, inspection and backend systems                 |    |
| 8.4    | Safeguards<br>67                                                     |    |
| 8.4.1  | Selection of cryptographic methods and key length                    | 68 |

| 8.4.2  | Safeguards for the protection of the system as a whole                                            | 68  |
|--------|---------------------------------------------------------------------------------------------------|-----|
| 8.4.3  | Safeguards relating to the carrier medium                                                         | 77  |
| 8.4.4  | Safeguards relating to the readers                                                                | 89  |
| 8.4.5  | Safeguards relating to the key management system                                                  | 92  |
| 9      | Definition of product-specific application scenarios                                              | 100 |
| 9.1    | Application scenario: "Local multi-journey entitlement"                                           | 100 |
| 9.2    | Application scenario: "Electronic season ticket"                                                  | 102 |
| 9.3    | Application scenario: "Interoperable unceasing entitlement with automatic fare<br>calculation"    | 103 |
| 10     | Suggestions on implementing the system as a whole                                                 | 106 |
| 10.1   | Suggestions on executing the eTicketing infrastructure                                            | 107 |
| 10.1.1 | Determining the protection demand for the eTicketing infrastructure                               | 107 |
| 10.1.2 | Interfaces in the system as a whole                                                               | 109 |
|        | 10.1.2.1<br>Threats relevant to the eTicketing infrastructure                                     | 109 |
|        | 10.1.2.2<br>Definition of safeguards for the interfaces of the system as a whole                  | 111 |
|        | 10.1.2.3<br>Residual risks                                                                        | 112 |
| 10.1.3 | Readers                                                                                           | 113 |
|        | 10.1.3.1<br>Threats relevant to the readers                                                       | 114 |
|        | 10.1.3.2<br>Definition of safeguards for the reader and its applications                          | 115 |
|        | 10.1.3.3<br>Residual risks                                                                        | 116 |
| 10.1.4 | Sale, inspection and management systems                                                           | 116 |
|        | 10.1.4.1<br>Sales systems                                                                         | 116 |
|        | 10.1.4.2<br>Ticket system                                                                         | 119 |
|        | 10.1.4.3<br>Central verification system                                                           | 120 |
|        | 10.1.4.4<br>Terminals                                                                             | 121 |
|        | 10.1.4.5<br>Service desks                                                                         | 122 |
|        | 10.1.4.6<br>Management system for carrier media and applications                                  | 122 |
|        | 10.1.4.7<br>Threats relevant to sale, inspection and management systems                           | 123 |
|        | 10.1.4.8<br>Definition of safeguards for sale, inspection and management systems                  | 124 |
|        | 10.1.4.9<br>Residual risks                                                                        | 126 |
| 10.1.5 | Key management                                                                                    | 126 |
|        | 10.1.5.1<br>Key management for public transport service providers / SAMs for<br>service providers | 127 |
|        | 10.1.5.2<br>Threats relevant to the key management system                                         | 128 |
|        | 10.1.5.3<br>Definition of safeguards for the key management system                                | 128 |
|        | 10.1.5.4<br>Residual risks                                                                        | 129 |
| 10.2   | Suggestions on executing the carrier media                                                        | 130 |
| 10.2.1 | Initialising carrier media and applications                                                       | 132 |

| 10.2.2 | Personalising carrier media and applications                                            | 133 |
|--------|-----------------------------------------------------------------------------------------|-----|
| 10.2.3 | Determining the protection demand for the carrier media                                 | 133 |
| 10.2.4 | Threats to the carrier medium                                                           | 133 |
| 10.2.5 | Definition of specific safeguards                                                       | 134 |
| 11     | Suggestions on executing the product-specific application scenarios                     | 135 |
| 11.1   | The "Local multi-journey entitlement" application scenario                              | 135 |
| 11.1.1 | Determining the protection demand category                                              | 135 |
| 11.1.2 | Relevant threats                                                                        | 137 |
| 11.1.3 | Definition of specific safeguards                                                       | 138 |
|        | 11.1.3.1<br>Safeguards when utilising the "Smart Ticket" carrier medium                 | 139 |
|        | 11.1.3.2<br>Residual risks when utilising the "Smart Ticket" carrier medium             | 141 |
|        | 11.1.3.3<br>Safeguards when utilising the "multi-application card" carrier medium       | 141 |
|        | 11.1.3.4<br>Residual risks when utilising the "multi-application card" carrier medium   | 143 |
|        | 11.1.3.5<br>Safeguards when utilising the "NFC mobile device" carrier medium            | 143 |
|        | 11.1.3.6<br>Residual risks when utilising the "NFC mobile device" carrier medium        | 145 |
| 11.2   | Electronic season ticket                                                                | 145 |
| 11.2.1 | Determining the protection demand category                                              | 145 |
| 11.2.2 | Relevant threats                                                                        | 148 |
| 11.2.3 | Definition of specific safeguards                                                       | 149 |
|        | 11.2.3.1<br>Safeguards when utilising the "secure chip card" carrier medium             | 150 |
|        | 11.2.3.2<br>Residual risks when utilising the "secure chip card" carrier medium         | 152 |
|        | 11.2.3.3<br>Safeguards when utilising the "multi-application card" carrier medium       | 152 |
|        | 11.2.3.4<br>Residual risks when utilising the "multi-application card" carrier medium   | 155 |
|        | 11.2.3.5<br>Safeguards when utilising the "NFC mobile device" carrier medium            | 155 |
|        | 11.2.3.6<br>Residual risks when utilising the "NFC mobile device" carrier medium        | 158 |
| 11.3   | The "Interoperable entitlement with automatic fare calculation" application<br>scenario | 158 |
| 11.3.1 | Determining the protection demand category                                              | 158 |
| 11.3.2 | Relevant threats                                                                        | 161 |
| 11.3.3 | Definition of specific safeguards                                                       | 162 |
|        | 11.3.3.1<br>Safeguards when utilising the "multi-application card" carrier medium       | 163 |
|        | 11.3.3.2<br>Residual risks when utilising the "multi-application card" carrier medium   | 165 |
|        | 11.3.3.3<br>Safeguards when utilising the "NFC mobile device" carrier medium            | 165 |
|        | 11.3.3.4<br>Residual risks when utilising the "NFC mobile device" carrier medium        | 168 |
| 12     | Reference system "VDV Kernapplikation"                                                  | 169 |
| 13     | List of references                                                                      | 170 |
| 14     | List of abbreviations                                                                   | 172 |

# **List of Tables**

| Table 2–1  | Overview of sales channels and their features                                                                    | 16 |
|------------|------------------------------------------------------------------------------------------------------------------|----|
| Table 8–1  | Coding scheme of security targets                                                                                | 54 |
| Table 8–2  | Customer specific security targets for safety                                                                    | 55 |
| Table 8–3  | Customer specific security targets for information security                                                      | 55 |
| Table 8–4  | Customer specific security targets for protection of privacy                                                     | 56 |
| Table 8–5  | Product provider specific security targets for safety                                                            | 56 |
| Table 8–6  | Product provider specific security targets for safety information<br>security                                    | 57 |
| Table 8–7  | Product provider specific security targets for protection of privacy                                             | 57 |
| Table 8–8  | Service provider specific security targets for safety                                                            | 58 |
| Table 8–9  | Service provider specific security targets for information security                                              | 59 |
| Table 8–10 | Service provider specific security targets for protection of privacy                                             | 59 |
| Table 8–11 | Overview of the entities' security targets                                                                       | 60 |
| Table 8-12 | Definition of protection demand categories                                                                       | 62 |
| Table 8–13 | Coding scheme of threats                                                                                         | 62 |
| Table 8–14 | Threats to the contact-less interface                                                                            | 63 |
| Table 8–15 | Threats to the carrier medium                                                                                    | 64 |
| Table 8–16 | Threats to the reader                                                                                            | 65 |
| Table 8–17 | Threats to the key management system                                                                             | 66 |
| Table 8–18 | Threats to the sales, inspection and backend systems                                                             | 67 |
| Table 8–19 | Coding scheme of safeguard measures                                                                              | 68 |
| Table 8–20 | Protection of the system as a whole through introduction of interface<br>tests and approval procedures           | 69 |
| Table 8–21 | Protection of the system as a whole through ensuring the<br>confidentiality of communication                     | 70 |
| Table 8–22 | Protection of the system as a whole through introduction of contact<br>less interface as defined by ISO/IEC14443 | 70 |
| Table 8–23 | Protection of the system as a whole through definition of fallback<br>solutions                                  | 71 |
| Table 8–24 | Protection of the system as a whole through securing the<br>confidentiality of data                              | 71 |
| Table 8–25 | Protection of the system as a whole through confidential storage of<br>data                                      | 72 |
| Table 8–26 | Protection of the system as a whole through securing the data<br>integrity when transmitting data                | 72 |
| Table 8–27 | Protection of the system as a whole through securing data integrity<br>when storing data                         | 72 |

| Table 8–28 | Protection of the system as a whole through securing the system's<br>functions against DoS attacks               | 73 |
|------------|------------------------------------------------------------------------------------------------------------------|----|
| Table 8–29 | Protection of the system as a whole through securing the function of<br>the system against incorrect operation   | 73 |
| Table 8–30 | Protection of the system as a whole through securing the function of<br>the system to prevent technical failures | 74 |
| Table 8–31 | Protection of the system as a whole through specification of the<br>system and the components                    | 75 |
| Table 8–32 | Protection of the system as a whole through ergonomic user<br>instructions                                       | 75 |
| Table 8–33 | Protection of the system as a whole through support                                                              | 76 |
| Table 8–34 | Protection of the system as a whole through separation of<br>applications                                        | 76 |
| Table 8–35 | Protection of the system as a whole through identifying the customer                                             | 77 |
| Table 8–36 | Protection of the system as a whole through satisfying the data<br>minimization obligation                       | 77 |
| Table 8–37 | Protection of the transponder through access protection for the EPC                                              | 78 |
| Table 8–38 | Protection of the transponder against cloning                                                                    | 79 |
| Table 8–39 | Protection of the transponder against emulation                                                                  | 80 |
| Table 8–40 | Protection of personal data on the transponder                                                                   | 81 |
| Table 8–41 | Protection of settlement data on the transponder                                                                 | 82 |
| Table 8–42 | Protection through separation of applications on the transponder                                                 | 82 |
| Table 8–43 | Protection through specification of carrier medium                                                               | 83 |
| Table 8–44 | Protection through introduction of proximity technology as defined by<br>ISO/IEC14443                            | 83 |
| Table 8–45 | Protection through fallback solution for carrier medium malfunction                                              | 84 |
| Table 8–46 | Protection through securing the authenticity and integrity when<br>loading applications                          | 86 |
| Table 8–47 | Protection through securing the confidentiality when loading<br>applications                                     | 87 |
| Table 8–48 | Protection through securing the authenticity and integrity when<br>loading entitlements                          | 88 |
| Table 8–49 | Protection through securing the confidentiality when loading<br>entitlements                                     | 89 |
| Table 8–50 | Protection of readers through introduction of interface tests                                                    | 90 |
| Table 8–51 | Protection of readers through protection of reference information                                                | 91 |
| Table 8–52 | Protection of the reader against malfunction                                                                     | 92 |
| Table 8–53 | Protection through secure generation and import of keys                                                          | 94 |
| Table 8–54 | Protection through introduction of key management                                                                | 95 |
| Table 8–55 | Protection through access protection for cryptographic keys                                                      | 96 |
| Table 8–56 | Protection through securing the function of security components                                                  | 96 |
| Table 8–57 | Protection through availability of a key management system                                                       | 97 |

| Table 8–58  | Protection through definition of actions when keys are compromised                   | 98  |
|-------------|--------------------------------------------------------------------------------------|-----|
| Table 8–59  | Protection through separation of keys                                                | 98  |
| Table 8–60  | Protection through securing the authenticity and integrity when<br>loading keys      | 99  |
| Table 9–1   | Carrier media used for local multi-journey entitlements                              | 101 |
| Table 9–2   | Relevant processes                                                                   | 101 |
| Table 9–3   | Carrier media for electronic season tickets                                          | 103 |
| Table 9–4   | Relevant processes                                                                   | 103 |
| Table 9–5   | Carrier media for "Interoperable entitlement with AFC"                               | 104 |
| Table 9–6   | Relevant processes                                                                   | 105 |
| Table 10–1  | The system's protection requirements                                                 | 109 |
| Table 10–2  | Threats relevant to the contact-less interface                                       | 110 |
| Table 10–3  | Threats relevant to the systems                                                      | 111 |
| Table 10–4  | Safeguards for the system as a whole                                                 | 112 |
| Table 10–5  | Threats relevant to the contact-less interface                                       | 114 |
| Table 10–6  | Threats relevant to the reader                                                       | 115 |
| Table 10–7  | Safeguards for the reader and its applications                                       | 116 |
| Table 10–8  | Threats relevant to sales, inspection and management systems                         | 124 |
| Table 10–9  | Safeguards for sale, inspection and management systems                               | 126 |
| Table 10–10 | Threats relevant to the key management system                                        | 128 |
| Table 10–11 | Safeguards for the key management system                                             | 129 |
| Table 10–12 | Categorisations of carrier media                                                     | 131 |
| Table 10–13 | Categorisations of chip products                                                     | 132 |
| Table 10–14 | Threats relevant to the carrier medium                                               | 134 |
| Table 11–1  | Protection demand for the "Local multi-journey entitlement"<br>application scenario  | 137 |
| Table 11–2  | Threats relevant to the "Local multi-journey entitlement" application<br>scenario    | 138 |
| Table 11–3  | Use cases relevant to the "Local multi-journey entitlement" application<br>scenario  | 139 |
| Table 11–4  | Safeguards when utilising Smart Tickets                                              | 141 |
| Table 11–5  | Safeguards when utilising multi-application cards                                    | 143 |
| Table 11–6  | Safeguards when utilising NFC mobile device                                          | 145 |
| Table 11–7  | Protection demand for the "electronic season ticket" application<br>scenario         | 148 |
| Table 11–8  | Relevant threats in the "electronic season ticket" application scenario              | 149 |
| Table 11–9  | Use cases relevant to the "electronic season ticket" application<br>scenario         | 150 |
| Table 11–10 | Safeguards for the "electronic season ticket" entitlement on a "secure<br>chip card" | 152 |

| Table 11–11 | Safeguards for the "electronic season ticket" entitlement on a "multi<br>application card"        | 155 |
|-------------|---------------------------------------------------------------------------------------------------|-----|
| Table 11–12 | Safeguards for the "electronic season ticket" entitlement on an "NFC<br>mobile device"            | 158 |
| Table 11–13 | Protection demand for the "Interoperable entitlement with AFC"<br>application scenario            | 160 |
| Table 11–14 | Relevant threats in the "Interoperable entitlement with AFC"<br>application scenario              | 162 |
| Table 11–15 | Use cases relevant to the "Interoperable entitlement withcalculation<br>AFC" application scenario | 162 |
| Table 11–16 | Safeguards for a "Interoperable entitlement with AFC" on a "multi<br>application card"            | 165 |
| Table 11–17 | Safeguards for a "Interoperable entitlement with AFC" on an "NFC<br>mobile device"                | 168 |
|             |                                                                                                   |     |

# **List of Illustrations**

| Figure 3–1  | Entities in an application area as defined by ISO 24014 (but extended<br>to include customer medium entities) | 19  |
|-------------|---------------------------------------------------------------------------------------------------------------|-----|
| Figure 3–2  | Entities in the "eTicketing for public transport" application area                                            | 22  |
| Figure 3–3  | Entities in the "VDV Core Application" application scenario                                                   | 22  |
| Figure 3–4  | Carrier media, applications and entitlements                                                                  | 23  |
| Figure 5–1  | Example: Identification of RFID-relevant use cases for eTicketing                                             | 27  |
| Figure 5–2  | Example of application scenarios and RFID-relevant use cases for<br>eTicketing in public transport            | 28  |
| Figure 5–3  | Hierarchical concept for media, applications and entitlements in<br>eTicketing                                | 28  |
| Figure 5–4  | Concept for security considerations                                                                           | 30  |
| Figure 5–5  | Generic security targets                                                                                      | 31  |
| Figure 6–1  | Process P1A "registering and ordering"                                                                        | 33  |
| Figure 6–2  | Process P1B "purchasing non-personalised carrier media and<br>entitlements"                                   | 35  |
| Figure 6–3  | Process P2A "producing and delivering personalised carrier media<br>and entitlements"                         | 36  |
| Figure 6–4  | Process P2B "producing and delivering non-personalised carrier<br>media and entitlements"                     | 37  |
| Figure 6–5  | Process P3 "using a CICO entitlement"                                                                         | 39  |
| Figure 7–1  | Use case "Carrier medium initialisation"                                                                      | 42  |
| Figure 7–2  | Use case "Application loading"                                                                                | 43  |
| Figure 7–3  | Use case "Entitlement loading"                                                                                | 44  |
| Figure 7–4  | Use case "Check-in"                                                                                           | 45  |
| Figure 7–5  | Use case "Check-out"                                                                                          | 46  |
| Figure 7–6  | Use case "Entitlement check"                                                                                  | 47  |
| Figure 7–7  | Use case "Blocking"                                                                                           | 48  |
| Figure 7–8  | Use case "Key management for carrier media"                                                                   | 49  |
| Figure 7–9  | Use case "Key management for applications"                                                                    | 50  |
| Figure 7–10 | Use case "Key management for products/entitlements"                                                           | 51  |
| Figure 10–1 | System as a whole                                                                                             | 106 |
| Figure 10–2 | Example of a reader with Smart Card or Smart Label                                                            | 113 |
| Figure 10–3 | An example of a ticket system with possible process flows                                                     | 120 |

# <span id="page-11-0"></span>**1 Description of the application area for "eTicketing in public transport"**

In order to use public transport a passenger requires an entitlement, otherwise known as a ticket. This entitlement is traditionally in the form of a paper ticket, to which the passenger gives validity (stamps, validates) when issued or when the journey begins, and which may be checked by a controller in the vehicle or on the platform.

In Germany, access barriers in railway stations were dismantled at the end of the 1950s for reasons of cost, whereas in many other parts of the world electro-mechanical access equipment has been introduced. There you can only access the platform via access barriers which evaluate an entitlement. Simple techniques were used at first such as tokens (e.g. New York) and magnetic stripe cards (Singapore, London). Nowadays many of these initial implementations have been replaced by contact-less proximity chip technology. Other important references have emerged such as Peking, Seoul, Moscow, Paris, Warsaw and Oslo. The contactless chip technology defined in ISO/IEC14443 has proved the most reliable, powerful and cost-efficient solution for mass applications in public transport, and the worldwide acceptance of the ISO/IEC14443 standard is mainly a result of the positive experience gleaned from these projects.

Currently, almost all large-scale international implementations utilise relatively inexpensive chip cards with contact-less memory chips. Many of these projects are the sole responsibility of a single transport company. If more than one transport company is involved then there is a contractually regulated relationship between the providers, and on that basis there is an organisational collaboration governing in detail themes such as products, fares and clearing.

In Germany the situation is somewhat different at the moment. There is no implementation yet that is using electro-mechanical access barriers in stations.

Furthermore, approximately 360 public and 4,500 private transport companies are active in Germany. There are no heavily used areas of transport that are served by just one single transport company. Since the *Verkehrsverbünde*, or regional transport associations, were introduced in the 1970s, the general situation for most passengers is that they draw on the services of several companies using just one single interoperable entitlement. This implies the need to remunerate the companies fairly for the transport they provide – a process known as "Clearing".

For passengers, this mixed service situation comes with difficulties that hinder the use of public transport. Every regional transport association has a different, complex fare system and its own tickets. With the exception of certain long-distance train tickets, it is impossible to book a journey that includes local public transport on one single ticket. Instead passengers usually have to get to grips with complex fare systems and unfamiliar automatic ticket machines when they arrive.

It was against this background that the *Verband Deutscher Verkehrsunternehmen* (VDV, or Association of German Transport Companies) began to develop an IFM (Interoperable Electronic Fare Management System) based on contact-less chip technology and known as the VDV Core Application (CA). This has become the standard in Germany for interoperable electronic fare management. The CA pursues the following aims:

- 1 Improve the attractiveness of public transport for the customer by introducing the following features and services:
	- a Introduce an interoperable customer medium throughout Germany which customers can use with every transport company and association provided it operates CA-compliant systems.
- b Automatic fare calculation that takes into account the transport services used.
- 2 Strengthen transport companies by:
	- a Counteracting counterfeit fraud.
	- b Helping to divide up takings among the companies.
	- c Increasing competition: create an interoperable service platform offering the companies flexibility in their fare policies.

The first implementation of the CA is beginning to be put into place. Media using the interface defined in ISO/IEC14443 are being used.

European standardisation authorities have so far introduced three standards to support the emerging IFM system:

- 1 The functional system architecture and the application scenarios of IFM systems are described in the standard ISO EN 24014-1. This standard was drawn up by the CEN TC 278 WG3 SG5 Work Group.
- 2 The description of the data elements to be used in the medium, and the structure of the data elements (application), are contained in CEN TC 224 WG11 SG1.
- 3 The EN 1545 standard describes the data elements and EN 15320 describes the data structuring (IOPTA, InterOperable Public Transport Application).

The VDV Core Application implements the existing international system standards into one overall set of technical system specifications.

This is to be the basis for our discussions henceforth.

# <span id="page-13-1"></span><span id="page-13-0"></span>**2 Description of services, products and carrier media**

This discussion of products and carrier media intends initially – as also does IOPTA – to delineate the current and predicted state of affairs in Europe. However, emphasis will be placed on the check-in/check-out variation of the CA (CICO), since this is the most highly developed, powerful and flexible of the IOPTA application scenarios. In a CICO-system, the passenger actively registers to the systems at the start and at the end of the journey by using his electronic customer media.

Customers are provided with services by transport companies, and the following ticketing products are offered in that connection:

- 1 Electronic ticket (individual ticket, day, month, year and network tickets with defined regional validity, and tickets for regional and long-distance travel).
- 2 Multi-journey entitlements.
- 3 Upgrading with additional entitlements.
- 4 Unceasing tickets (automatic fare calculation, CICO, electronic ticket subscription contract).

The products differ in terms of particular features and characteristics:

- 1 Interoperable or non-interoperable usage.
- 2 Value of entitlement:
	- E-ticket approx. €1 €15,000; e.g. VRR: €6,000, DB AG: €15,000,
	- Stored value … €150
	- Unceasing or season tickets … >€1,000
- 3 Non-transferable personalised, transferable personalised, anonymous.
- 4 Validity in terms of time and region / non-regulated entitlements.
- 5 Charging variations (account entitlements {pre-/postpaid}, credit entitlements, …)
- 6 Time of fare calculation (pre-pricing, trip-pricing and post-pricing).

In all this, interoperability is defined as when two or more companies accept an entitlement/product (acceptance terminal interfaces have to be standardised; in the VDV CA this means ISO-14443 and the specified data interfaces) and calculate between themselves which services were used and how the takings are shared out. Every transport company association in Germany now operates like this. From the customer's point of view interoperability means that they can use their media and entitlements to travel with different service providers.

Automatic fare calculation requires a check-in at the start of the journey and a check-out at the end, and this in turn requires CICO (check-in/check-out) infrastructure. Systems that use access barriers can use these for checking in and out. In systems without access barriers (Germany for example), a CICO infrastructure comprising check-in and check-out terminals must be installed on the platforms and in the vehicles.

The following carrier media are generally considered for use in public transport:

- 1 Paper ticket
- 2 Magnetic stripe card
- 3 Smart Ticket with contact-less proximity interface as defined by ISO/IEC14443
- 4 Contact-less chip card with proximity interface as defined by ISO/IEC14443
- 5 Contact-less, high-security multi-application card with proximity interface as defined by ISO/IEC14443

6 Secure NFC mobile device

The products are sold through the following channels:

- 1 Direct sales by the product provider:
	- a Customer centre, vending machine, local sales point e.g. at a railway station
	- b Internet sales
- 2 Sales through retailers:
	- a Travel agencies, hotels, etc.
	- b Internet sales

The following table describes the various sales channels and their features:

| Sales<br>channel                                                               | mer<br>Setting up a custo<br>account | Reliable identification | me<br>mer<br>Initialise custo<br>dia on site | Direct output of cus<br>media<br>mer<br>to | Media delivered by<br>post | ments onto<br>media<br>mer<br>Load entitle<br>ex. custo | Production and issue<br>of paper tickets | ment<br>Methods of pay                                                                  | Sales staff present | Sale in secure area | Mobile operation | Online link to sales and<br>ms<br>ment syste<br>manage |
|--------------------------------------------------------------------------------|--------------------------------------|-------------------------|----------------------------------------------|--------------------------------------------|----------------------------|---------------------------------------------------------|------------------------------------------|-----------------------------------------------------------------------------------------|---------------------|---------------------|------------------|--------------------------------------------------------|
| Customer<br>centre                                                             | +                                    | +                       | +                                            | +                                          | +                          | +                                                       | +                                        | m-specific                                                                              | +                   | +                   | –                | +                                                      |
| Local sales<br>point                                                           | +                                    | +                       | –                                            | +                                          | +                          | +                                                       | +                                        | ments with syste                                                                        | +                   | –                   | +<br>/<br>–      | +/–                                                    |
| Travel<br>agent, ho<br>tel, etc.                                               | +                                    | +                       | –                                            | +                                          | +                          | +                                                       | +                                        |                                                                                         | +                   | –                   | +<br>/<br>–      | +/–                                                    |
| Static vend<br>ing machine                                                     | –                                    | –                       | +                                            | –/+                                        | –                          | +                                                       | +                                        |                                                                                         | –                   | –                   | –                | +/–                                                    |
| Static vend<br>ing machine<br>with reader<br>for cus<br>tomer- /<br>eID-medium | +                                    | +                       | –                                            | +                                          | +                          | +                                                       | +                                        | Cash, cards, direct debit, acceptance of entitle<br>ment procedures (e.g. stored value) | –                   | –                   | –                | +                                                      |
| Sale by<br>driver                                                              | –                                    | –                       | –                                            | –/+                                        | –                          | +                                                       | +                                        | pay                                                                                     | +                   | +                   | +                | –                                                      |

<span id="page-15-0"></span>

| Sales<br>channel                                          | mer<br>Setting up a custo<br>account | Reliable identification | me<br>mer<br>Initialise custo<br>dia on site | Direct output of cus<br>media<br>mer<br>to | Media delivered by<br>post | ments onto<br>media<br>mer<br>Load entitle<br>ex. custo | Production and issue<br>of paper tickets | ment<br>Methods of pay                                                                  | Sales staff present | Sale in secure area | Mobile operation | Online link to sales and<br>ms<br>ment syste<br>manage |
|-----------------------------------------------------------|--------------------------------------|-------------------------|----------------------------------------------|--------------------------------------------|----------------------------|---------------------------------------------------------|------------------------------------------|-----------------------------------------------------------------------------------------|---------------------|---------------------|------------------|--------------------------------------------------------|
| Sale by<br>conductor                                      | –                                    | –                       | –                                            | –/+                                        | –                          | +                                                       | +                                        | ments<br>ment procedures<br>m-specific                                                  | +                   | –                   | +                | –                                                      |
| Vending<br>machine in<br>vehicle                          | –                                    | –                       | –                                            | –/+                                        | –                          | +                                                       | +                                        | Cash, cards, accep<br>tance of entitle<br>with syste<br>pay                             | –                   | –                   | +                | –                                                      |
| Internet                                                  | +                                    | –                       | –                                            | –                                          | +                          | –                                                       | +                                        | ments with<br>ment                                                                      | –                   | –                   | +                | +                                                      |
| Internet with<br>home<br>reader /<br>NFC mobile<br>device | +                                    | +                       | +                                            | –                                          | +                          | +                                                       | +                                        | Cards, direct debit, accep<br>m-specific pay<br>tance of entitle<br>procedures<br>syste | –                   | –                   | +                | +                                                      |

**Table 2–1 Overview of sales channels and their features** 

"+" indicates that the feature applies to the respective sales channel

"–" indicates that the relation has not to be considered

"+" a symbol highlighted in grey denotes developments expected in the future

1 Sale by personnel

Sales through customer centres, local sales points, guards and drivers involve a direct interaction between the customer and the personnel of the product provider (CCP). What these sales channels have in common is that the personnel can identify the customer (e.g. by checking the customer's identity card) and that several payment methods etc. may be used in a flexible way.

Differences arise from the various technical possibilities.

Customer media can only be initialised if there is online access to the relevant background systems and if the necessary equipment is available on site. At the moment this is not always the case. Customer media are often ordered at customer centres and sales points and then delivered by post. Alternatively, the finished medium can be kept for collection at the customer centre. This process cannot take place with mobile sales (i.e. in vehicles), since customer accounts cannot be set up due to time constraints or lacking connection to the required systems.

In the future there will be methods for loading applications and personalising in customer centres and also via the Internet using home readers, and over-the-air using NFC mobile devices.

Loading entitlements onto existing personalised and non-personalised media requires direct communication between the customer medium and the sales system via a suitable

reader. This is currently supported in customer centres and local sales points for personalised and non-personalised products. Non-personalised products can also be sold offline using Secure Authentication Modules (SAMs). This is also possible when the reader is offline (e.g. in vehicles or in other places where no online-connection is available).

### 2 Static and mobile vending machines

Vending machines are nowadays very widespread. There are static installations in railway stations or at bus stops, or readers that are implemented in vehicles.

Static vending machines can be connected to sales and management systems via an online link. This means that vending machines could even be used to initialise and personalise customer media. In contrary to that, continuous online links do not exist in vehicles.

At the moment customers do not have the option of registering at vending machines, since a reliable means of identification does not exist. This also means that customer accounts cannot be set up, and personalised media cannot be applied for.

That is why vending machines only sell products anonymously at present. Loading entitlements onto existing customer media is technically possible if the vending machine is equipped with an appropriate reader with SAM.

Soon customers will be able to enjoy secure, convenient methods of identification and authentication using – for example – electronic identity cards. This can also enable registering at vending machines.

3 Internet

The customer submits personal details, the order, and payment information to a service centre via the Internet (web page). The availability of the product and, where applicable, seat reservations can normally be dealt with straight away when ordering on the Internet. Payment is by credit card, direct debit, or similar. Products and customer media are delivered by post or can be made available for collection at a customer centre.

Personal and address information submitted through a web page is not necessarily considered trustworthy. Checking it reliably involves considerable extra effort. Normally it is checked solely against a current address database, and a credit check is performed.

4 Internet using card-readers / over-the-air and possibly secure proof of identity (e.g. eID) In future there may be another way in which customers can register and place orders.

It will involve the customer submitting the order and payment information to a service centre via the Internet (web page). Data relating to the customer's person (where necessary) will be identified and transmitted online by means of direct communication between the ticket issuer's application server and a secure identity card (electronic identity card, eID).

The availability of the product and, where applicable, seat reservations can normally be dealt with straight away when ordering on the Internet. Payment is by credit card, direct debit, or similar. Products and customer media are delivered by post or can be made available for collection (sales point, vending machine).

The personal and address information received by communicating with the eID are to be considered trustworthy and reliable. Additional checking is not required.

Anonymous use of public transport can also be offered via this sales channel, in which case an anonymous medium is used and a non-personalised entitlement loaded onto it. The service is paid for by means of credits stored on the medium. These credits can be purchased through the sales infrastructure using anonymous payment methods.

# <span id="page-17-0"></span>**3 Agreements**

## **3.1 Definition of terms**

#### Application area

the area in which the Technical Guidelines are intended to apply; the highest unit in the terminological structure; incorporates one or more applications, the products/services that belong to those applications and the application scenarios that result from that

#### Application scenario

a particular way of looking at the application area in terms of the implementation of specific products and services

#### Operating process

a comprehensive operational procedure in an application area like eTicketing; examples are the sales process, the use of an entitlement, clearing, and so on

#### Use case

detailed description of a series of activities that constitute part of an operating process; examples include initialising a carrier medium and loading an entitlement

#### Check-in / check-out (CICO)

when using the "automatic fare calculation" product, the passenger must check in at the start of the journey and check out at the end. This requires an appropriate infrastructure, known as a CICO infrastructure. Systems that use access barriers can use these for checking in and out. Otherwise a CICO infrastructure comprising check-in and check-out terminals (CICO terminals) must be installed on the platforms, at bus stops and in vehicles.

### Interoperability

Interoperability means that the customer can redeem his entitlement with more than one service provider. The service provider is remunerated for the services provided by the product owner. Interoperability is required between transport company associations and also between transport companies within such associations. Accounting accuracy is a central aspect of this, since it determines the money received by the service providers. In the past, money was shared out within transport company associations on the basis of traffic flow analyses, statistics and estimates. Technical accounting accuracy can be achieved with the introduction of CICO technology.

#### Usage data

the calculation process in the "automatic fare calculation" product is based on data gathered when the customer uses the service. To enable this, the customer checks in at a terminal using his customer medium and then checks out again when he has finished using the service. The usage data acquired is stored in the terminal and the customer medium. Its reliability is fundamental to the reliable invoicing of customers and to interoperability between service providers.

#### Calculation data

the usage data which is used for accounting purposes is referred to as calculation data. Calculation data contains, for example, information about the entitlement, the product owner, the service provider, and the place and time of check-in <span id="page-18-0"></span>and check-out. This data may or may not be able to be assigned to the customer, depending on whether personalised or anonymous entitlement is being used. The calculation data is passed on to the product owner by the service provider, who gathers it at the CICO terminals. The authenticity, integrity and confidentiality of the calculation data are extremely important to customers and service providers alike.

Statistical data

Statistical data provides information about the general use of a product, a line, a vehicle and so on. With an "automatic fare calculation" entitlement, the statistical data can be derived from the usage data. With other products, usage data can be gathered when the entitlement is assessed before entry. Statistical data is stored and utilised in an anonymised and statistically processed form. Statistical data is not used for invoicing customers for services, but rather for the service provider's or product owner's planning purposes, which is why it is only held in anonymised form. Statistical data can, however, be used for a general division of takings between service providers.

## <span id="page-18-1"></span>**3.2 Generic modelling of roles and entities**

The roles and responsibilities shall be described on the basis of the ISO 24014 standard.

![](_page_18_Figure_6.jpeg)

#### **Figure 3–1 Entities in an application area as defined by ISO 24014 (but extended to include customer medium entities)**

ISO 24014 defines entities and assigns roles and responsibilities to them. The implementation for the eTicketing areas of use is described in the following:

Actor

An entity that operates in accord with the role assigned to it.

Customer

The purchaser of a product and user of the services associated with it. The customer pays money and receives from the product provider an entitlement to use services. This entitlement is redeemed at the service provider.

#### Customer medium

The customer medium is a data carrier in which an electronic entitlement can be stored. The customer medium is held by the customer, and is required by the customer in order to use the entitlement. Other common names for the customer medium are user medium and carrier medium. Examples of customer media include Smart Tickets, chip cards and NFC mobile devices.

#### Issuer of customer medium

The issuer of the customer medium configures it for further use. The issuer may market the customer medium through customer media providers (such as transport companies). Close coordination and a contractual relationship are required between the issuer of the customer medium, the application issuer and the system manager.

#### Provider of customer medium

The provider of the customer medium (e.g. a transport company or mobile phone service provider) markets the customer medium which it has received from the customer medium issuer. The provider of the customer medium normally implements with the issuing of the customer medium.

#### Application

The application supports one or more products by providing functions and structures – such as those needed to store entitlements on the carrier medium, in the sales system and in the backend system. The implementation follows the application specification, which normally belongs to the issuer of the application. The issuer of the application may market the application through application providers (such as a regional transport association). As well as the products, the application may also contain customer-specific information.

#### Application issuer

The application issuer is the owner of the application specification. The application issuer may market the application through application providers (e.g. a transport company).

#### Application provider

The application provider (e.g. a transport company or stadium operator) implements and markets the application which it has received from an application issuer (e.g. in licensed form). The application provider also normally issues the carrier medium in conjunction with implementing the application, making him, for instance, the contractual partner to the customer in the eTicketing application area.

#### Product/entitlement/service

The product is a service or object provided by a product owner and which the customer can use in return for payment. The product belongs to the product owner (e.g. a concert organiser) and is offered to customers directly or through a product provider (e.g. travel agent or advance ticket office). When he purchases the product, the customer receives an entitlement to use a service, which he can then redeem at the service provider (e.g. transport company).

#### Product owner

The owner of the product (e.g. a single entry to a Bundesliga football match). The product owner defines and markets the product, sometimes through a product provider (e.g. an advance ticket office). In simple scenarios, however, it is quite normal for the product owner to be the product provider as well. The product owner must follow the specifications of the application issuer when he defines his product, in order to ensure that the application can support the product. Furthermore, close collaboration is required between the product owner and the service provider who is to provide the service promised by the product. A contractual relationship is required between the product owner, product provider and service provider.

<span id="page-20-0"></span>Product provider

Markets the product on behalf of the product owner in return for a fee. The product provider receives the customer's payment and is therefore the only interface for payments. This demands direct coordination and a contractual relationship with the product owner. The product provider places the product (e.g. an entitlement) into the application on the carrier medium. The product provider is the contractual partner to the customer in terms of the entitlements he has purchased to utilise services. In organisational terms the product owner often takes on the role of product provider as well.

#### Service provider

Examples include stadium operators and public transport service operators. Provides the customer with a service if he presents an entitlement purchased from a product provider (e.g. entry to a stadium). This requires direct coordination and a contractual relationship between the product provider and product owner.

#### System manager

The system manager ensures that the rules of the system are upheld. To this end he draws on the functional entities of security manager and registrar.

#### Registrar

The registrar ensures that unique identifying characteristics are allocated throughout the system. This is necessary in order to clearly identify the entities, carrier media, applications and products/entitlements.

#### Security manager

Establishes and coordinates the security regulations in the system. Responsible for approving the components of the system. Monitors the performance of security-related functions (e.g. key management).

### <span id="page-20-1"></span>**3.3 Allocation of roles and entities in the "eTicketing for public transport" application area**

Making the services available which are described in Chapter [2](#page-13-1) demands, in a fully developed configuration, the interaction of diverse and changing entities. For instance, it must be made possible for a service provider to handle products from various different product owners and providers, and to support the invoicing accordingly.

The assignment of entities in this application area is identical to the generic description in section [3.2](#page-18-1). In the following diagram, the main entities defined in the VDV Core Application are also shown to provide an example:

<span id="page-21-0"></span>![](_page_21_Figure_1.jpeg)

![](_page_21_Figure_2.jpeg)

<span id="page-21-1"></span>The specifications of the VDV Core Application combine some of the roles together:

- 1 The customer contract partner (CCP) takes on the role of providing the customer medium, application and product.
- 2 VDV KA GmbH takes on the roles of system manager (including security manager and registrar) and application issuer.

Given these facts, the generic diagram in [Figure 3–2](#page-21-1) is modified to produce the following specific plan:

![](_page_21_Figure_7.jpeg)

**Figure 3–3 Entities in the "VDV Core Application" application scenario** 

## **3.4 Relationship between carrier media, applications and entitlements**

The model described in sections [3.2](#page-18-1) and [3.3](#page-20-1) supports several product providers, service providers, application issuers and so on.

This means that a large number of different carrier media, applications and products would be conceivable.

<span id="page-22-0"></span>The customer or carrier medium is the customer's data carrier on which he stores his entitlements and with the help of which he makes use of the associated services.

Applications provide the structures and functions required to load entitlements onto carrier media, and to make use of the entitlements. The implementation of applications must therefore take account of the features of specific carrier media and entitlements.

The customer can exchange entitlements for services at the service provider.

The following rules apply to the relationships between carrier media, applications and entitlements:

- 1 A carrier medium can contain at least one application. If more than one application can be stored on it, then it is referred to as a multi-application-compatible carrier medium.
- 2 An application can store at least one entitlement. The VDV Core Application simultaneously supports different entitlements of different types, which may originate from different product providers. Personal data and check-in / check-out data may also be stored in the application.
- 3 Applications on one carrier medium can originate from different application issuers and providers.
- 4 Entitlements in one application may originate from different product owners and providers.
- 5 Entitlements of the same type can be stored in different applications.

The following diagram illustrates an example of the relationship between carrier media, applications and entitlements.

![](_page_22_Figure_11.jpeg)

**Figure 3–4 Carrier media, applications and entitlements** 

# <span id="page-23-1"></span><span id="page-23-0"></span>**4 General requirements**

The requirements which must be met by the system as a whole and its processes and components can be divided into three categories.

## **4.1 Function**

### **4.1.1 Customer requirements**

Below are some of the features which are required from the customer's point of view:

- The customer media and systems must be easy to use.
- The customer medium must be durable and reliable, and must perform at a the required speed.
- The entitlement and the customer medium must be easy and reliable to use, including with different service providers.
- The way the "automatic fare calculation" product is invoiced must be reliable and easy to follow.
- It should be possible to replace lost entitlements for an administration fee. The same should apply to exchanging entitlements.
- It must also be possible to purchase anonymous entitlements.
- Reasonable protection must be provided for personal data (where applicable).

Whenever contact-less chip technology is used, the customer should always be kept properly informed of the personal data used, how it is employed, what is done to protect the data, and any risks that remain.

### **4.1.2 Requirements of the product provider and service provider**

Functionality

- It should be easy to explain to customers and personnel how the customer medium and systems are used.
- The way the system components and processes are executed must take into account the conditions particular to public transport. For example, permanent data access to the overall system cannot be guaranteed in vehicles, so it has to be possible to purchase entitlements, redeem them, check-in / check-out and monitor entitlements even when the terminals involved are not online.
- It must be possible to block personalised entitlements and customer media, and to issue replacements.
- Access barriers and check-in/check-out systems must allow enough people through in a given period. A typical requirement for permanently installed systems is a processing time of 300 ms.

Technical compatibility

• The compatibility of system components must be assured even if carrier media, systems and components come from different manufacturers and providers and are used for different service providers.

# <span id="page-24-0"></span>**4.2 Economy**

For an eTicketing system to be operated economically, the commercial benefit must be greater than the cost of the processes, systems and security, regardless of how extensively the system is installed. This must apply to all of the entities who invest in the setting-up of the system.

The system as a whole, and its components, should be designed such that the requirements of the relevant application scenarios are met as efficiently as possible. For this reason it is necessary to define these requirements as accurately as possible to begin with.

# **4.3 Security**

This document will deal with the requirements of security separately, from section [8.2](#page-53-1) onwards.

# <span id="page-25-0"></span>**5 Method of determining security requirements**

## **5.1 Objectives**

The Technical Guideline on secure use of RFID should fulfil the following objectives:

- Provide system suppliers and system users with an introductory guide on the correct implementation of specific RFID system solutions, in terms of safety, information security and privacy.
- Raise awareness of and achieve transparency in aspects of security.
- Provide a basis for the system supplier's or operator's declaration of conformity, and for the issuing of quality seals by certification authorities.

The following information is required in order to achieve these aims:

- A definition of the security requirements that must be fulfilled by an RFID system for a given application area.
- A description of the specific risks, appropriate counter-measures, and potential remaining risks, in following called residual risks.
- A definition of the criteria for a declaration of conformity and for certification.

It is not just security aspects that are relevant to the definition of activities and proposed systems; all of the requirements described in Chapter [4](#page-23-1) also have to be taken into consideration.

## **5.2 Method**

### **5.2.1 Scope of system considerations**

RFID-based systems can be very complex. In most cases, a lot of IT components that have no direct relation to RFID are part of the system solution. On the other hand it is not sufficient to look only at the media/tag and reader in order to safeguard the system's security.

The Technical Guidelines must consider every aspect of security in detail that is relevant to RFID. These aspects depend heavily on the application area and the relative implementation of the system solution. These Technical Guidelines therefore contain detailed descriptions of the application area, and the related operations processes (including, for example, sales channels and processes). Based on this information, use cases are identified that are relevant to RFID. Processes and use cases cover the entire life-cycle of RFID media or RFID tags. These use cases are then used as a basis for the identification of threats, and for a detailed system-specific security assessment of RFID-related parts of the system. [Figure 5–1](#page-26-1) shows this approach for the example of eTicketing in public transport.

<span id="page-26-0"></span>![](_page_26_Figure_1.jpeg)

**Figure 5–1 Example: Identification of RFID-relevant use cases for eTicketing** 

<span id="page-26-1"></span>All the other system components are considered only in a fairly general manner. Proposed safeguards follow open standards of IT security.

This concept helps to focus on those parts of the system that are relevant to RFID, and makes sure that all aspects of security are considered. On the other hand the Technical Guidelines leave room for individual and proprietary IT implementations (back-offices, sales systems, logistic systems and so on), which supports the enhancement of existing systems using RFID technology.

## **5.2.2 Scalability and flexibility**

The Technical Guidelines have to address security issues. At the same time, any system based on these Guidelines must be economically viable. This means that the following requirements have to be covered by the Guidelines' approach:

- 1 It must be possible to scale systems in such a way that the costs and benefits are balanced. This means in practice that precautionary measures must be proportional to the need for protection. For example: if only low-cost products are used, which require relatively little protection, then precautions should be designed accordingly. This may allow the use of low-cost media, reducing in turn the cost of implementation and operation of the system.
- 2 The application scenarios that have been chosen for the Technical Guidelines cover a wide range, from small to nationwide and even international systems. It is important that the concept discussed in the Guidelines can be used for system solutions of any size and complexity.
- 3 In many cases a system solution can be made economically viable much more easily if you are able to cooperate with other companies. This applies in particular to eTicketing applications, where it can be very beneficial if media already available to customers

<span id="page-27-0"></span>(such as multi-application cards and NFC-enabled phones) can be used for additional applications, products and related services.

The following diagrams provide examples from eTicketing for the cross-system and crossapplication utilisation of customer media and infrastructure.

[Figure 5–2](#page-27-1) shows that various products and application scenarios may have to be supported in one system. Furthermore, these products may be hosted by various types of RFID media.

![](_page_27_Figure_4.jpeg)

![](_page_27_Figure_5.jpeg)

#### **Figure 5–2 Example of application scenarios and RFID-relevant use cases for eTicketing in public transport**

<span id="page-27-1"></span>[Figure 5–3](#page-27-2) gives an example of a customer medium for eTicketing that supports applications from two areas of use.

![](_page_27_Figure_8.jpeg)

#### **Figure 5–3 Hierarchical concept for media, applications and entitlements in eTicketing**

<span id="page-27-2"></span>The following concept is used in these Technical Guidelines in order to address the aforementioned requirements:

- 1 A feasible role model and the structure of key components (products, applications and media) are defined in chapter 3. These models support a granular and scalable approach.
- 2 The Technical Guidelines offer security plans that also cover combinations of application scenarios and media used on the same infrastructure. This is achieved by itemised security assessments based on the RFID-relevant use cases.
- <span id="page-28-0"></span>3 Areas of use similar to eTicketing that provide opportunities for cross-application partnerships will be addressed by the respective Technical Guidelines with as much communality as possible. The security considerations and precautionary measures in particular will employ the same technical basis.
- 4 A special challenge to system security exists in partnerships across systems and applications. It must be ensured that the security of one system is not undermined by leakages coming from the other. Normally this requires extensive security assessments in both systems.

The Technical Guidelines address this by introducing a scalable and transparent concept for applying precautions to the identified threats, called "protection demand categories". A total of three categories from 1 (normal demand) to 3 (very high demand) are applied. All of the safeguards are divided accordingly into three levels, from normal to advanced protection.

For every individual system implementation, the protection demand category will be defined to begin with, for every security target. These findings will be used to select the appropriate level for the safeguards involved.

This concept provides an easy way to establish secure system cooperation. It remains only to ensure that the protection demand categories of both systems match up.

## **5.2.3 Structure of the Technical Guidelines**

Table 5-1 shows the structure of all the sections of the Technical Guidelines that have so far been drawn up.

| Chapter                             | Contents                                                                                                                          |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Description of the application area | Description of the application area: struc<br>ture, services, special peripheral conditions,<br>etc.                              |
| Products and services               | Description of products, services and sales<br>channels                                                                           |
| Definitions                         | Role model, definition of terms                                                                                                   |
| Introduction to the methodology     | Introduction to the concept and methods<br>that are applied to the security considera<br>tions.                                   |
| General requirements                | General requirements of the parties in<br>volved, important points, etc.                                                          |
| Operational processes               | Description of operational processes rele<br>vant to the life-cycle of RFID media                                                 |
| Use cases                           | Definition of RFID-relevant uses cases                                                                                            |
| Security considerations             | Introduction to IT security                                                                                                       |
|                                     | Definition of specific security targets, protec<br>tion demand categories, and threats.                                           |
|                                     | Proposed safeguards                                                                                                               |
| Definition of application scenarios | Definition of examples for application sce<br>narios. These examples cover the entire<br>range of relevant parameters that may oc |

<span id="page-29-0"></span>

| Chapter                                                   | Contents                                                                                                                                                        |
|-----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                           | cur in this specific application area. Users of<br>the Technical Guidelines may adapt these<br>scenarios according to their own needs.                          |
| Proposed implementation of the system<br>solution         | Generic system description including exam<br>ples of how to perform a threat analysis and<br>arrive at feasible safeguards to protect the<br>system components. |
| Implementation proposal for each applica<br>tion scenario | Examples of applying the concept to Secu<br>rity considerations in an application-specific<br>way.                                                              |

**Table 5–1 Structure of the Technical Guidelines** 

### **5.2.4 Explanation of the security concept**

The Technical Guidelines contain complete examples of how security considerations should be applied to specific application scenarios. These can be adapted to the requirements and peripheral conditions of the particular system implementation in hand.

[Figure 5–4](#page-29-1) shows the concept for the Security considerations used in all sections of the Technical Guidelines.

![](_page_29_Figure_6.jpeg)

<span id="page-29-1"></span>**Figure 5–4 Concept for security considerations** 

<span id="page-30-0"></span>All considerations are based on the classic definition of security targets that is given in [Figure](#page-30-1)  [5–5](#page-30-1).

![](_page_30_Figure_2.jpeg)

<span id="page-30-1"></span>**Figure 5–5 Generic security targets** 

# <span id="page-31-1"></span><span id="page-31-0"></span>**6 Generic business processes**

# **6.1 Process P1 "registering and ordering"**

### **6.1.1 Setting up a customer account, purchasing personalised customer media and entitlements**

To set up a customer account and purchase a personalised or non-personalised entitlement, the customer applies to the product provider (i.e. the customer contract partner in the VDV Core Application). If the customer does not possess a carrier medium containing a suitable application, then he can purchase one from the product provider[1](#page-31-0) . To facilitate this, the product provider works together with the providers of the application and the customer medium.

Purchasing customer-related entitlements, applications and carrier media requires that the customer registers. To do this the customer provides the necessary personal information (e.g. name, postal address, payment information) and orders the product required.

It is normally up to the product provider to decide which information is required of the customer for the purposes of determining his identity and address and conducting a credit check.

Let us examine the following processes as examples of registering and ordering:

1 Ordering at a customer centre or a local sales point

The customer visits the sales point (e.g. the customer centre of a transport company, a sales point at a railway station or a travel agent), and orders the product. Payment is made there and then. Ideally, the sales point will have direct access to the eTicketing system and will be able to issue products and customer media on site. If not, they are delivered by post. Personal data is only required if a customer-specific product or a product with a CA payment method by direct debit is ordered, or if postal delivery is required.

Where necessary, identity and personal data is checked by proving the identity by means of an identity card.

2 Service centre

The customer submits the necessary personal information, the order and the payment information to a service centre by fax, written application or telephone. The availability of the product and factors such as seat reservations can normally be dealt with straight away when ordering by telephone. Payment is by credit card, by direct debit, etc. Products and customer media are delivered by post or put aside for collection (sales point, vending machine).

Personal and address information submitted by fax or phone is not necessarily considered trustworthy. Checking it reliably involves extra effort. Normally it is checked solely against a current address database, and a credit check is performed.

An example of ordering from a service centre using an order form can be seen at: <http://www.kolibricard.de/bestellung.html> .

<sup>1</sup> The case of a customer who only wants to purchase a customer medium with an application, but no product, is considered irrelevant and is not discussed here.

<span id="page-32-0"></span>3 Internet

The customer submits the necessary personal information, the order and the payment information to a service centre by Internet (web page). The availability of the product and factors such as seat reservations can normally be dealt with straight away when ordering by Internet. Payment is by credit card, by direct debit, etc. Products and customer media are delivered by post or put aside for collection at a customer centre.

Personal and address information submitted via the Internet is not necessarily considered trustworthy. Checking it reliably involves extra effort. Normally it is checked solely against a current address database, and a credit check is performed.

4 Internet using card-readers and secure proof of identity (e.g. eID)

In future there may be another way for customers to register and place orders.

It will involve the customer submitting the order and payment information to a service centre via the Internet (web page). Personal data (where necessary) will be identified and transmitted online by means of direct communication between the ticket issuer's application server and a secure electronic identity card.

The availability of the product and factors such as seat reservations can normally be dealt with straight away when ordering by Internet. Payment is by credit card, by direct debit, etc. Products and customer media are delivered by post or put aside for collection (sales point, vending machine).

The personal and address information received by communicating with the eID are to be considered trustworthy and reliable. Additional checking is not required.

![](_page_32_Figure_9.jpeg)

The following diagram shows Process P1A, registering and ordering:

**Figure 6–1 Process P1A "registering and ordering"** 

### <span id="page-33-0"></span>**6.1.2 Purchasing non-personalised carrier media and entitlements**

Anonymous sales and the sale of non-personalised products are especially important in public transport. In such cases, customer accounts are not set up. The product is supplied on a specially produced, non-personalised carrier medium or loaded anonymously onto an existing customer card.

The customer must always pay before the product is handed over.

Anonymous sales require that payment is made immediately, that the entitlement is produced immediately, and that the customer can take it away on his existing customer medium.

The following sales channels can be used:

1 Sales point/customer centre, travel agent

The sale of non-personalised tickets at sales points is common practice for paper tickets. In the future, non-personalised customer media will be able to be produced on site and entitlements loaded onto existing customer media. Payment is in cash or by card.

2 Driver / guard

The sale of tickets by drivers and guards is common practice for paper tickets. In the future it will be possible to load entitlements onto existing customer media this way. Payment is in cash or by card.

3 Vending machine

The sale of tickets by vending machines is common practice for paper tickets. Non-personalised customer media can also be produced by vending machines, and entitlements loaded onto existing customer media.

Payment is in cash or by card.

4 Internet using card-readers and secure proof of identity (e.g. eID)

Even when non-personalised carrier media or the ticket is ordered on the Internet and, for instance, delivered by post, the name and address of the customer still has to be submitted to the product provider. An additional option for registering and ordering can be provided to this end.

It will involve the customer submitting the order and payment information to a service centre via the Internet (web page). Personal data (where necessary) will be identified and transmitted online by means of direct communication between the ticket issuer's application server and a secure electronic identity card.

The availability of the product and factors such as seat reservations can normally be dealt with straight away when ordering by Internet. Payment is by credit card, by direct debit, etc. Products and customer media are delivered by post or put aside for collection (sales point, vending machine). The product and carrier medium themselves do not contain any personal data.

The personal and address information received by communicating with the eID are to be considered fundamentally trustworthy and reliable. Additional checking is not required.

<span id="page-34-0"></span>The following diagram shows Process P1B, purchasing non-personalised carrier media and entitlements:

![](_page_34_Figure_2.jpeg)

**Figure 6–2 Process P1B "purchasing non-personalised carrier media and entitlements"** 

## <span id="page-34-1"></span>**6.2 Process P2 "producing and delivering products"**

### **6.2.1 Process P2A "producing and delivering personalised carrier media and entitlements"**

Two basic cases are to be considered when describing this process:

- 1 Producing and delivering an entitlement together with a specially produced carrier medium.
- 2 Loading an entitlement onto a customer-related medium already in the possession of the customer (e.g. secure multi-application card, NFC mobile device).

<span id="page-35-0"></span>The following diagram, [Figure 6–3](#page-35-1), shows Process P2A with 4 sub-processes representing the possible ways in which a product may be delivered.

![](_page_35_Figure_2.jpeg)

#### **Figure 6–3 Process P2A "producing and delivering personalised carrier media and entitlements"**

<span id="page-35-1"></span>In Processes P2A.1 to P2A.3, the entitlement ordered is delivered to the customer on a specially produced carrier medium.

In Process P2A.4 it is assumed that the customer already has a suitable customer medium. This may be a secure chip card, a multi-application card or an NFC mobile device.

The customer medium is used in the first instance to identify and authenticate the customer electronically. If the customer medium does not contain a suitable application, then one must be loaded onto it before the entitlement is loaded on.

### **6.2.2 Process P2B "producing and delivering non-personalised carrier media and entitlements"**

Two basic cases are to be considered when describing this process:

- 1 Producing and delivering an entitlement together with a specially produced carrier medium.
- 2 Loading an entitlement onto a customer-related medium already in the possession of the customer (e.g. secure multi-application card, NFC mobile device).

<span id="page-36-0"></span>The following diagram, [Figure 6–4](#page-36-1), shows Process P2B with 3 sub-processes representing the possible ways in which a product may be delivered.

![](_page_36_Figure_2.jpeg)

#### **Figure 6–4 Process P2B "producing and delivering non-personalised carrier media and entitlements"**

<span id="page-36-1"></span>In Process P2B.1, the entitlement ordered is delivered to the customer on a specially produced carrier medium. Provided data that can be related to a person is clearly separated on the carrier medium and application, a non-personalised entitlement can be loaded onto a personalised carrier medium.

In Process P2B.2 it is assumed that the customer already has a suitable customer medium. This may be a secure chip card, a multi-application card or an NFC mobile device. If the customer medium does not contain a suitable application, then one must be loaded onto it before the entitlement is loaded on.

Process P2B.3 is the same as P2B.2, except that applications cannot be loaded onto the carrier medium. The customer medium must be fully configured to accept the entitlement as a precondition for the customer to use this process.

# **6.3 Process P3 "using an entitlement"**

The customer must have a carrier medium with an approved application and valid entitlement in order to use the transport. The entitlement is redeemed by the customer in exchange for a service.

Depending on the product, the entitlement is activated at the start of the journey, or the customer checks in when he begins the journey and checks out at the end (CICO). The infrastructure required for this is the responsibility of the service provider.

The public transport service provider must first do a number of things so as to guarantee the operation of this function:

- 1 The local inspection infrastructure must be adapted to the accepted applications and entitlements.
- 2 The specific key information for reading the entitlements and writing the usage data must be integrated into the key management system.
- 3 The list of blocked media, applications and entitlements (blacklist) must be transferred from the ticket system into the inspection infrastructure, which requires the approval and installation of a data interface to the service provider's inspection infrastructure (an interface which enables the data to be updated at sensible intervals).

A journey begins by checking in at a static or mobile terminal. Alternatively, it is possible to use mobile inspection units carried in the vehicles by the ticket-checking staff. The terminals should work even if the data connection to the server fails, which means that all terminals have to work offline as well as online (some of them possibly only temporarily).

When beginning the journey, the entitlement has to be checked and validated. If an "automatic fare calculation" product is being used, then the user must also check out at the end of the journey. At both these points, data relating to the fare is stored in the terminal and the carrier medium.

![](_page_38_Figure_1.jpeg)

<span id="page-38-0"></span>The following diagram shows Process P3:

**Figure 6–5 Process P3 "using a CICO entitlement"** 

Fault cases are not dealt with here.

### **6.4 Process P4 "blocking entitlements, applications and carrier media"**

Because of the high level of counterfeit security that can be achieved with correct implementations of chip-based carrier media, it is possible to block entitlements, applications and carrier media securely. This helps the processes of cancelling and exchanging carrier media and entitlements, and enables lost media to be replaced.

The following are possible scenarios:

- 1 Defective carrier media are withdrawn and destroyed. Before issuing a replacement medium it is important to ascertain that a counterfeit has not been presented for replacement, and that a medium has not been declared as defective and submitted.
- 2 In practice, mislaid carrier media can only be blocked and replaced if they are personalised and assigned to a customer account (see registration) with a product provider. If this is the case, then the owner can identify himself to the product provider from which he obtained the medium, and state which carrier medium is to be blocked. The same procedure can be used to cancel entitlements.
- 3 Mislaid personalised carrier media and the entitlements stored on them can be replaced provided that all the entitlements on them have been blocked. It is important to remember that the carrier medium may contain more than one application, and that these may themselves contain entitlements from various product issuers and providers.

# <span id="page-40-1"></span><span id="page-40-0"></span>**7 Use cases**

The following sections contain descriptions of use cases that are relevant as we look further at contact-less chip technology in this application area. These use cases have been derived from the generic operating processes in Chapter [6](#page-31-1).

The descriptions of the use cases are based on an illustrative system architecture which is discussed in more detail in Chapter [10](#page-105-1).

# **7.1 Use case "Identification when registering and ordering"**

The quality of the process of authenticating and identifying the customer is crucial to the reliability of the data upon which Process P1, "Registering and ordering", is based. Process descriptions P1A.1 – P1A.4 can be used for elucidating this. Using a reliable process, such as one involving a secure personalised customer medium or an electronic identification medium (e.g. an eID), will mean an increase in security and functionality.

## <span id="page-40-2"></span>**7.2 Use case "Carrier medium initialisation"**

The "Carrier medium initialisation" use case depicted in [Figure 7–1](#page-41-1) incorporates the following steps:

- 1 Carrier medium initialisation
	- a Default settings relating to function and security
	- b Setting specific keys
	- c Setting an ID which uniquely identifies the carrier medium
- 2 Loading the applications
	- a Loading the software specific to the applications concerned
	- b Allocating the resources of the carrier medium (setting up file systems and so on)
	- c Setting specific keys for each application
- 3 Loading the application-specific data
	- a Loading customer data (where required)
	- b Loading the ID of the application provider

As the stages of initialising the carrier medium progress, the information in the management system for carrier media and applications has to be updated.

The various keys, certificates and so on that are used are generated and fed in by a key management system. This system is the responsibility of the system manager (more precisely the security manager and registrar). If the carrier medium's chip is to generate public keys during initialisation, then these also have to be fed into the key management system.

Carrier medium initialisation normally takes place in a secure environment (e.g. in a mass personaliser or in a vending machine).

<span id="page-41-0"></span>

| Use Case "Carrier medium initialisation"    |                                                                                                                                                                                                                                                                                                                          |                                                      |                                                                                 |                                                                                                            |                                |
|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|--------------------------------|
| Criteria                                    | Initialisation procedure                                                                                                                                                                                                                                                                                                 | Carrier medium                                       | Carrier and application<br>management                                           | Key management                                                                                             | Ticket sales system            |
| Initialise<br>medium                        | Carrier medium in<br>Reading range<br>Detect carrier medium<br>Invalid<br>medium<br>OK?<br>END<br>Valid<br>medium<br>Carrier medium known?<br>Known<br>medium<br>Valid application present?<br>Application<br>present<br>END<br>Load<br>application<br>"Load new<br>application"<br>process                              | Carrier medium type<br>identifier                    | Carrier medium ID<br>and allocated<br>applications<br>Allocated applications    |                                                                                                            |                                |
| Criterion:<br>Authentication<br>successful? | Authenticate carrier<br>medium<br>Invalid<br>Medium<br>OK?<br>end<br>Valid<br>medium<br>Initialise carried medium<br>Set key<br>Load carrier ID<br>Load application<br>Load application<br>Set application-specific<br>key<br>Load application-specific<br>data<br>Customer data<br>ID of application<br>provider<br>END | Carrier medium ID<br>Application<br>Application data | Carrier medium ID<br>Register application<br>(in relation to carrier<br>medium) | Platform key<br>Specific key<br>Platform key<br>Application-specific<br>key<br>Application-specific<br>key | Customer data<br>Provider data |

**Figure 7–1 Use case "Carrier medium initialisation"** 

# <span id="page-41-2"></span><span id="page-41-1"></span>**7.3 Use case "Application loading"**

The "Application loading" use case shown in [Figure 7–2](#page-42-1) illustrates the procedure for loading an application onto a carrier medium already in the possession of a customer. This may be a contact-less chip card or an NFC mobile device.

There are various possible scenarios for loading a new application onto an existing carrier medium:

- 1 Loading the application via a contact-less interface in a trustworthy environment
- 2 Loading the application via a contact-less interface in an insecure environment. For instance, this may occur when loading an application onto a contact-less chip card via a reader on a home computer or in an advance ticket office.
- 3 Loading an application "over-the-air" onto an NFC mobile device.

<span id="page-42-0"></span>![](_page_42_Figure_1.jpeg)

**Figure 7–2 Use case "Application loading"** 

# <span id="page-42-2"></span><span id="page-42-1"></span>**7.4 Use case "Entitlement loading"**

As soon as the carrier medium has been initialised and the applications installed, entitlements can be loaded onto the applications.

The sale of a product is directly dependent on this use case being performed securely and in a way which is easy for customers. The use case is therefore an absolutely crucial one for providers and customers alike. All of the sales channels discussed in the descriptions of Processes P2A and P2B (Section [6.2](#page-34-1)) must be taken into consideration when dealing with the "Entitlement loading" use case depicted in [Figure 7–3](#page-43-1).

<span id="page-43-0"></span>![](_page_43_Figure_1.jpeg)

**Figure 7–3 Use case "Entitlement loading"** 

<span id="page-43-1"></span>A distinction must be made between the loading of entitlements when the carrier medium is first issued and the loading of entitlements later on. The latter can be done via the Internet using a home reader, "over-the-air" onto an NFC mobile device, or locally at a sales point or vending machine.

# **7.5 Use case "Delivery"**

Carrier media that have been initialised and loaded with entitlements must then be passed to the delivery point or the customer as described in P2A.1 and P2A.2.

When delivering, the product provider must also record security-relevant information about the delivery in the ticket system. This includes:

- 1 Addressee,
- 2 ID of carrier media, ID of products,
- 3 Sender,
- 4 Delivery point, special arrangements relating to handing-over,

## **7.6 Use case "Check-in"**

The "Check-in" use case represents the first part of Process P3.2 in detail. The exact way this is executed depends on the application involved and the data models and algorithms associated with it. The following diagram shows the procedure.

<span id="page-44-0"></span>![](_page_44_Figure_1.jpeg)

**Figure 7–4 Use case "Check-in"** 

In the event of a fault the customer is referred to a service desk, which normally means visiting a customer centre. There, a defective carrier medium can be exchanged if necessary.

# **7.7 Use case "Check-out"**

The "Check-out" use case represents the second part of Process P3.2 in detail. The exact way this is executed depends on the application involved and the data models and algorithms associated with it. The following diagram shows the procedure.

<span id="page-45-0"></span>![](_page_45_Figure_1.jpeg)

**Figure 7–5 Use case "Check-out"** 

In the event of a fault the customer is referred to a service desk, which normally means visiting a customer centre. There, a defective carrier medium can be exchanged if necessary.

# **7.8 Use case "Entitlement check"**

The "Entitlement check" use case represents the technical process of a ticket inspector checking the customer's entitlement to travel. This technical process is largely identical to the "Check-in" use case. The exact way it is executed depends on the application involved and the data models and algorithms associated with it. The following diagram shows the procedure.

An entitlement check is normally performed using a mobile inspector's terminal loaded with the necessary SAM and blacklists.

<span id="page-46-0"></span>![](_page_46_Figure_1.jpeg)

**Figure 7–6 Use case "Entitlement check"** 

If a fault occurs, the entitlement is normally checked visually.

## **7.9 Use case "Blocking"**

Carrier media that have been mislaid must be blocked. The same applies to defective media and products, assuming they cannot be withdrawn and destroyed.

The blocking of a medium and/or the entitlement stored on it is a precondition for the issuing of a replacement medium, or for the transfer of an entitlement to a new owner with a different customer medium.

Blocking can only be performed if it is sufficiently certain that the customer requesting it is the rightful owner of the medium or entitlement. That is why customers may only block media or entitlements in either of the following cases:

- 1 The customer's details were stored when purchasing. Blocking is then performed following reliable identification and a legally binding declaration that the customer agrees to the procedure.
- 2 The medium containing the entitlement is presented. Its authenticity can be determined securely.

<span id="page-47-0"></span>As well as customers performing blocks, other entities in the system can apply for blocking. To this end, responsibilities and processes are defined for these entities in the system as a whole.

![](_page_47_Figure_2.jpeg)

**Figure 7–7 Use case "Blocking"** 

# **7.10 Use cases "Key management"**

For performance reasons, entitlements on carrier media are usually protected using procedures involving symmetric keys. The security and proper function of the system as a whole is therefore highly dependent on the secure provision and storage of the keys, a job which has to be done by the key management system and the processes assigned to it.

In the following use cases, Secure Authentication Modules (SAMs) are used as secure storage for key information, security mechanisms and diversification algorithms. In principle, other methods may also be feasible.

Carrier medium initialisation and the loading of entitlements require a key management system that recognises the hierarchical relationship between carrier media, applications and products/entitlements.

### <span id="page-48-0"></span>**7.10.1 Key management for the initialisation of carrier media**

[Figure 7–8](#page-48-1) illustrates the use case of key management for the initialisation of carrier media. The keys and procedures defined here are also required for the loading of applications.

![](_page_48_Figure_3.jpeg)

**Figure 7–8 Use case "Key management for carrier media"** 

### <span id="page-48-2"></span><span id="page-48-1"></span>**7.10.2 Key management for loading and personalising applications**

In order to secure applications that are loaded when carrier media are produced, or afterwards, special keys and identifiers must be generated for the applications.

[Figure 7–9](#page-49-1) shows the corresponding use cases. The key management system for carrier media also has to be available when the application is loaded onto the carrier medium.

<span id="page-49-0"></span>![](_page_49_Figure_1.jpeg)

**Figure 7–9 Use case "Key management for applications"** 

### <span id="page-49-2"></span><span id="page-49-1"></span>**7.10.3 Key management for loading entitlements**

In order to secure entitlements that are loaded when carrier media are produced, or afterwards, special keys and identifiers must be generated for the products.

[Figure 7–10](#page-50-1) shows the corresponding use cases. The key management system for applications also has to be available when the entitlement is loaded onto the application.

<span id="page-50-0"></span>![](_page_50_Figure_1.jpeg)

**Figure 7–10 Use case "Key management for products/entitlements"** 

### <span id="page-50-1"></span>**7.10.4 Key management for use with the service provider**

Providers and issuers require a key management system to initialise carrier media, load applications and issue entitlements.

The public transport service provider requires the keys and other information necessary to read and evaluate entitlements.

This information has to be available in the verification system.

To this end, the security manager normally generates specific SAMs (service provider SAMs) for the service provider using the key management system. Service provider SAMs can contain key information from multiple providers of products, applications and carrier media. A selection is put together by the security manager in accordance with the needs of the service provider.

# <span id="page-51-0"></span>**8 Security considerations**

## **8.1 Definitions relating to security and privacy**

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
- e Unobservability: an event is unobservable if it cannot be determined whether it has happened or not. Sender-unobservability means it cannot be seen that anything has been sent; recipient-unobservability is the same: it is not possible to ascertain

that something has been received. Relationship-unobservability means that it cannot be seen that anything is sent from the group of possible senders to the group of possible recipients.

- f Anonymity: anonymity is the condition of being unidentifiable within one's anonymity group. Using the term unlinkability, anonymity can be more precisely defined as the unlinkability of the identity of a user and an event initiated by that user. Senderanonymity is therefore unlinkability of sender and message, and recipientanonymity is the unlinkability of message and recipient.
- g Authenticity: the term authenticity designates a situation in which the partner in a communication process is actually the person he claims to be. Authentic information is information that genuinely comes from the stated source. The term is not only used when people's identity is being checked, but also for IT components and applications.
- h Non-repudiation: protection should exist against the possibility of denying that messages have been sent and received by persons whose authenticity has been determined.
- i Accountability: binding validity joins together the IT security targets of authenticity and non-repudiation. When transmitting information this means that the source of the information has proven its identity, and that the receipt of the message cannot be disputed.
- 3 Privacy

The purpose of privacy is to protect against infringements of the personal rights of the individual through the handling of his personal data.

Privacy refers to the protection of personal data against possible misuse by third parties (not to be confused with data security) [EU\_REF].

The following additional terms will also be used throughout:

1 Security targets

Security targets are the security-related and safety-related objectives undertaken when setting up an IT system. This document lays down specific security targets within the areas of use and application scenarios. Infringing upon the security targets causes direct damage to the entity whose security target is violated.

2 Threats

Threats are immediate risks to the security targets of an application.

These may be the result of an active attack on one or more security targets by exploiting the systems weakness, or they may take the form of potential vulnerabilities in the system such as the lack of a fallback solution.

3 Safeguards

Safeguards are actual recommended actions that counter one or more threats. The safeguards described in this document are intended to be applied meaningfully and according to need, which means they are suggested on the basis of economic feasibility and resistance to manipulation: how expensive is a safeguard, and what are the financial damages that it can limit or prevent?

4 Residual risk

Generally speaking it is not possible to counteract every single threat in such a way that a system offers perfect security. The residual risk is thus the risk of potential threat that remains after a series of safeguards have been put in place. The extent of this risk depends on the counter-measures that can be applied, how complex they are, and, above all, what the costs are in relation to the benefits for the entity involved. The entity has to take explicit liability for the residual risk.

# <span id="page-53-1"></span><span id="page-53-0"></span>**8.2 Definition of the security targets**

It would be very unusual indeed for all of the safety aspects relating to safety, information security and privacy within a given application scenario to be of equal importance, or indeed for every single one of them to be relevant at all. The first challenge when designing a secure RFID system is therefore to formulate specific security targets.

Within the areas of use relating to eTicketing, certain superior security targets specific to the application area can be recognised, based on the generic security targets mentioned earlier:

- 1 Protection of electronic entitlements (represents the protection targets integrity and authenticity)
- 2 Safety of the RFID system
- 3 Protection of the customer's privacy (a general requirement representing the protection targets confidentiality, unlinkability, unobservability, anonymity and privacy)

The subsidiary security targets listed in Section [8.2.4](#page-58-1) can be derived from the assessments of the entities' security targets contained in the following sections.

| field num<br>ber | 1                   | 2                                       | 3                                                             | 4                |
|------------------|---------------------|-----------------------------------------|---------------------------------------------------------------|------------------|
| field            | security tar<br>get | associated role and<br>its abbreviation | associated generic<br>security target and its<br>abbreviation | index num<br>ber |
|                  |                     | C := customer                           | S := safety                                                   |                  |
| content          | S                   | P := product provider                   | I := information secu<br>rity                                 | 1,  , n          |
|                  |                     | S := service provider                   | P := privacy                                                  |                  |

The following table shows the scheme of security target codes and used abbreviations.

**Table 8–1 Coding scheme of security targets** 

### **8.2.1 Specific security targets for the customer**

The customer's specific security targets are listed in the following sections.

### **8.2.1.1 Safety**

| and name | Security target code         | Description of security target                                                                                                                                                                                                                                                                                                                                                     |
|----------|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SCS1     | Technical<br>compatibility   | The interaction between customer medium and reader must<br>function as specified. This must apply to all of the approved cus<br>tomer media and all of the readers in the entire system infra<br>structure. It must take into account the fact that carrier media<br>and infrastructure may be supplied by different manufacturers<br>and operated by different service providers. |
| SCS2     | Fallback solu<br>tion in the | Authorised persons must be able to use the service even when<br>the customer medium or system infrastructure is not working                                                                                                                                                                                                                                                        |

<span id="page-54-0"></span>

| and name | Security target code                       | Description of security target                                                                                                                                              |
|----------|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          | event of mal<br>function                   | perfectly.                                                                                                                                                                  |
| SCS3     | Intuitive, fault<br>tolerant opera<br>tion | Operation must be self-explanatory where possible, and/or easy<br>to learn.<br>The customer should know at any given time which stage of the<br>operation process he is at. |

### **8.2.1.2 Information security**

| Security target code<br>and name |                                                       | Description of security target                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------------------|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SCI1                             | Protection of<br>personal data                        | The customer data stored in the system and/or customer me<br>dium is used to identify the customer, make payments, deliver<br>entitlements, and so on.                                                                                                                                                                                                                                                                                                               |
|                                  |                                                       | Misuse, manipulation or passing-on to unauthorised persons<br>could incur commercial damage to the customer along with the<br>loss of safety, and should be prevented.                                                                                                                                                                                                                                                                                               |
| SCI2                             | Protection of<br>entitlements                         | Entitlements may be exposed to DoS attacks and manipulation<br>by third parties. This would cause inconvenience and possibe<br>damage to the customer. The damage would normally be lim<br>ited, since usually the service can still be used provided the cus<br>tomer can prove that he purchased a valid entitlement. Manipu<br>lation of the entitlement by unauthorised persons should be pre<br>vented.                                                         |
| SCI3                             | Protection of<br>usage data                           | Usage data is used to invoice the use of the "automatic fare cal<br>culation" product. This data must therefore be reliable.                                                                                                                                                                                                                                                                                                                                         |
| SCI4                             | Reliable in<br>voicing                                | When a service has been used, the customer must be able to<br>see the time of activation and, in the case of check-in / check<br>out, the time, place and service provider.                                                                                                                                                                                                                                                                                          |
|                                  |                                                       | Calculation data (pricing) must be traceable and reliable.                                                                                                                                                                                                                                                                                                                                                                                                           |
| SCI5                             | Protection of<br>applications<br>and entitle<br>ments | Customer media can accommodate more than one application,<br>and these applications may belong to different application issu<br>ers. Furthermore, one application can hold multiple entitlements<br>supplied by different product owners. It must be ensured that<br>applications and entitlements are reliably separated from a tech<br>nical point of view, or that agreements exist between the entities<br>that regulate multiple usage and conflict resolution. |

**Table 8–3 Customer specific security targets for information security** 

| Security target code<br>and name |                                                                  | Description of security target                                                                                                                                                       |
|----------------------------------|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SCP1                             | Protection of<br>personal data                                   | Personal data given to the product provider (CCP) must be<br>treated confidentially, and only used for the agreed purposes.                                                          |
| SCP2                             | Protection of<br>usage data                                      | Non-anonymised, personal data about the use of a service may<br>only be employed for the purposes of the product provider or<br>service provider with the agreement of the customer. |
| SCP3                             | Protection<br>against the<br>creation of<br>movement<br>profiles | Third parties must be prevented from utilising RFID technology<br>to generate personal movement profiles.                                                                            |

### <span id="page-55-0"></span>**8.2.1.3 Protection of privacy**

**Table 8–4 Customer specific security targets for protection of privacy** 

### **8.2.2 Specific security targets for the product provider (e.g. for CA CCP)**

The product provider's specific security targets are listed in the following sections.

### **8.2.2.1 Safety**

| Security target code<br>and name |                                                          | Description of security target                                                                                                                                                                                                                                                                                                                                                     |
|----------------------------------|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SPS1                             | Technical<br>compatibility                               | The interaction between customer medium and reader must<br>function as specified. This must apply to all of the approved cus<br>tomer media and all of the readers in the entire system infra<br>structure. It must take into account the fact that carrier media<br>and infrastructure may be supplied by different manufacturers<br>and operated by different service providers. |
| SPS2                             | Fallback solu<br>tion in the<br>event of mal<br>function | The customer must be able to use the service even when the<br>customer medium or system infrastructure is not working per<br>fectly.                                                                                                                                                                                                                                               |
| SPS3                             | Intuitive, fault<br>tolerant opera<br>tion               | Little explanation must be required in order to enable the cus<br>tomer to use the service without difficulty.<br>The customer should know at any given time which stage of the<br>operation process he is at.                                                                                                                                                                     |

#### **Table 8–5 Product provider specific security targets for safety**

### **8.2.2.2 Information security**

| Security target code<br>and name |               | Description of security target                                                                                           |
|----------------------------------|---------------|--------------------------------------------------------------------------------------------------------------------------|
| SPI1                             | Protection of | The customer data stored in the system and in the customer<br>medium is used to identify the customer, make payments, de |

<span id="page-56-0"></span>

| Security target code<br>and name |                                                       | Description of security target                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------------------|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                  | personal data                                         | liver entitlements, and so on.<br>Misuse, manipulation or passing-on to unauthorised persons<br>could incur commercial damage to the product provider and a<br>loss of customer acceptance, and could be punished as a viola<br>tion of the law. This must be avoided.                                                                                                                                                                                               |
| SPI2                             | Protection of<br>entitlements                         | The manipulation of, damage to and in particular the counterfeit<br>ing of entitlements could incur considerable commercial damage<br>to the product provider, product owner and service provider.<br>Securing entitlements against counterfeiting is an important ob<br>jective for the product owner.                                                                                                                                                              |
| SPI3                             | Protection of<br>usage data                           | The availability and integrity of usage data is of great value to<br>the product provider, the product owner and the service pro<br>vider. This data is used for invoicing, planning products and ca<br>pacities, and increasing customer loyalty.                                                                                                                                                                                                                   |
| SPI4                             | Reliable in<br>voicing                                | It must be ensured that earnings from the sale of entitlements by<br>the product provider can be allocated correctly to the transport<br>services provided by the service provider.                                                                                                                                                                                                                                                                                  |
| SPI5                             | Protection of<br>applications<br>and entitle<br>ments | Customer media can accommodate more than one application,<br>and these applications may belong to different application issu<br>ers. Furthermore, one application can hold multiple entitlements<br>supplied by different product owners. It must be ensured that<br>applications and entitlements are reliably separated from a tech<br>nical point of view, or that agreements exist between the entities<br>that regulate multiple usage and conflict resolution. |

### **Table 8–6 Product provider specific security targets for information security**

### **8.2.2.3 Protection of privacy**

| Security target code<br>and name |                                | Description of security target                                                                                                                                                                                                                                                                                  |
|----------------------------------|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SPP1                             | Protection of<br>personal data | Misuse, manipulation or passing-on to unauthorised persons<br>could incur commercial risks for the customer contract partner<br>and result in a loss of customer acceptance, and could also be<br>punished as a violation of the law.                                                                           |
| SPP2                             | Protection of<br>usage data    | Non-anonymised, personal data about the use of a service may<br>only be employed for the purposes of the product provider with<br>the agreement of the customer. The aim for certain products<br>(automatic fare calculation, CICO, etc) is to obtain this consent,<br>so as, for example, to enable invoicing. |
| SPP4                             | Data minimiza<br>tion          | Only the data required for the specified purpose should be gath<br>ered and stored, no more.                                                                                                                                                                                                                    |

| Table 8–7 | Product provider specific security targets for protection of privacy |
|-----------|----------------------------------------------------------------------|
|-----------|----------------------------------------------------------------------|

### <span id="page-57-0"></span>**8.2.3 Specific security targets for the service provider**

The service provider's specific security targets are listed in the following sections.

### **8.2.3.1 Safety**

| Security target code<br>and name |                                                          | Description of security target                                                                                                                                                                                                                                                                                                         |
|----------------------------------|----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SSS1                             | Technical in<br>teroperability                           | The entitlements stored in the various customer media must<br>function as specified. This must apply to all of the approved cus<br>tomer media and all of the readers in the service provider's en<br>tire system infrastructure. It must take into account the fact that<br>carrier media may be supplied by different manufacturers. |
| SSS2                             | Fallback solu<br>tion in the<br>event of mal<br>function | It must be possible to provide the service even when the cus<br>tomer medium or system infrastructure is not working perfectly.<br>It must be possible to prove the existence of an entitlement.                                                                                                                                       |
| SSS3                             | Intuitive, fault<br>tolerant opera<br>tion               | There must be a low incidence of problems when customers use<br>the system.<br>The customer should know at any given time which stage of the<br>operation process he is at.                                                                                                                                                            |

#### **Table 8–8 Service provider specific security targets for safety**

### **8.2.3.2 Information security**

| Security target code<br>and name |                                | Description of security target                                                                                                                                                                                                      |
|----------------------------------|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SSI1                             | Protection of<br>personal data | The customer data stored in the system and in the customer<br>medium is used to identify the customer, make payments, de<br>liver entitlements, and so on.                                                                          |
|                                  |                                | Misuse, manipulation or passing-on to unauthorised persons<br>could incur commercial damage to the service provider and a<br>loss of customer acceptance, and could be punished as a viola<br>tion of the law.                      |
| SSI2                             | Protection of<br>entitlements  | The manipulation of, damage to and in particular the counterfeit<br>ing of entitlements could incur considerable commercial damage<br>to the product provider, product owner and service provider.                                  |
|                                  |                                | Securing entitlements against counterfeiting is an important ob<br>jective for the service provider. Entitlements are also used in the<br>service provider's system infrastructure, and they must be safe<br>guarded there as well. |
| SSI3                             | Protection of<br>usage data    | Usage data is of great value to the service provider. It is used for<br>invoicing and for planning capacities.                                                                                                                      |
|                                  |                                | From the point of view of the customer and for legal reasons,<br>customer-specific usage data must be treated confidentially by<br>the service provider. Contravention of this would cause a loss of                                |

<span id="page-58-0"></span>

| Security target code<br>and name |                                                       | Description of security target                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------------------|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                  |                                                       | customer acceptance and could be punished as a violation of<br>the law.                                                                                                                                                                                                                                                                                                                                                                                              |
| SSI4                             | Reliable in<br>voicing                                | It must be ensured that earnings from the sale of entitlements by<br>the product provider can be allocated correctly to the transport<br>services provided by the service provider.                                                                                                                                                                                                                                                                                  |
| SSI5                             | Protection of<br>applications<br>and entitle<br>ments | Customer media can accommodate more than one application,<br>and these applications may belong to different application issu<br>ers. Furthermore, one application can hold multiple entitlements<br>supplied by different product owners. It must be ensured that<br>applications and entitlements are reliably separated from a tech<br>nical point of view, or that agreements exist between the entities<br>that regulate multiple usage and conflict resolution. |

### **8.2.3.3 Protection of privacy**

| Security target code<br>and name |                                | Description of security target                                                                                                                                                                                                                                                                                  |
|----------------------------------|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SSP1                             | Protection of<br>personal data | Misuse, manipulation or passing-on to unauthorised persons<br>could incur commercial risks for the service provider and result<br>in a loss of customer acceptance, and could also be punished as<br>a violation of the law.                                                                                    |
| SSP2                             | Protection of<br>usage data    | Non-anonymised, personal data about the use of a service may<br>only be employed for the purposes of the service provider with<br>the agreement of the customer. The aim for certain products<br>(automatic fare calculation, CICO, etc) is to obtain this consent,<br>so as, for example, to enable invoicing. |
| SSP4                             | Data minimiza<br>tion          | Only the data required for the specified purpose should be gath<br>ered and stored, no more.                                                                                                                                                                                                                    |

**Table 8–10 Service provider specific security targets for protection of privacy** 

### <span id="page-58-1"></span>**8.2.4 Summary of the entities' security targets**

The following table sums up the aforementioned security targets of the various entities involved. Role-specific security targets have been summarised to specific security targets associated to the generic security targets safety, information security and privacy. Used abbreviations are:

- SS := specific security target regarding to the generic security target safety
- SI := specific security target regarding to the generic security target information security
- SP := specific security target regarding to the generic security target privacy

<span id="page-59-0"></span>

| Security target |                                                           | Customer<br>targets | Product<br>provider<br>targets | Service<br>provider<br>targets |
|-----------------|-----------------------------------------------------------|---------------------|--------------------------------|--------------------------------|
| SS1             | Technical compatibility                                   | SCS1                | SPS1                           | SSS1                           |
| SS2             | Fallback solution in the event of<br>malfunction          | SCS2                | SPS2                           | SSS2                           |
| SS3             | Intuitive, fault-tolerant operation                       | SCS3                | SPS3                           | SSS3                           |
| SI1             | Protection of personal data                               | SCI1, SCP1          | SPI1, SPP1                     | SSI1, SSP1                     |
| SI2             | Protection of entitlements                                | SCI2                | SPI2                           | SSI2                           |
| SI3             | Protection of logistical data (ano<br>nymised usage data) |                     | SPI3                           | SSI3                           |
| SI4             | Reliable invoicing                                        | SCI3, SCI4,<br>SCP2 | SPI3, SPI4,<br>SPP2            | SSI3, SSI4,<br>SSP2            |
| SI5             | Protection of applications and enti<br>tlements           | SCI5                | SPI5                           | SSI5                           |
| SP3             | Protection against the creation of<br>movement profiles   | SCP3                |                                |                                |
| SP4             | Data minimization                                         |                     | SPP4                           | SSP4                           |

**Table 8–11 Overview of the entities' security targets** 

### <span id="page-59-1"></span>**8.2.5 Formation of protection demand categories**

Three protection demand categories are formed on the basis of the security targets described in Section [8.2.4](#page-58-1). Category 1 represents the lowest protection demand, category 3 the highest.

The following table lists the criteria for allocating protection requirements to protection demand categories, these criteria being based on the assumption that no protective measures have been put in place.

| Security target                    |                   | Protection<br>demand<br>category | Criteria for allocating to protection demand cate<br>gory                                                                                                       |
|------------------------------------|-------------------|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SS1<br>Technical com<br>patibility |                   | 1                                | All of the system components come from the<br>same supplier. The supplier ensures that they are<br>compatible.                                                  |
|                                    |                   | 2                                | The system has to function with components from<br>a small number of defined suppliers. The system<br>manager or a system integrator ensures compati<br>bility. |
|                                    |                   | 3                                | Open system that has to function with compo<br>nents from any company in the market.                                                                            |
| SS2                                | Fallback solution | 1                                | Malfunction affects only a few customers.                                                                                                                       |

<span id="page-60-0"></span>

| Security target                |                                                                                       | Protection<br>demand<br>category | Criteria for allocating to protection demand cate<br>gory                                                                                                                                                                                                                      |  |
|--------------------------------|---------------------------------------------------------------------------------------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| in the event of<br>malfunction |                                                                                       | 2                                | Malfunction affects many customers.                                                                                                                                                                                                                                            |  |
|                                |                                                                                       | 3                                | Malfunction affects a large proportion of custom<br>ers.                                                                                                                                                                                                                       |  |
| SS3                            | Intuitive, fault<br>tolerant opera<br>tion                                            | 1                                | A few customers cannot operate it intuitively.                                                                                                                                                                                                                                 |  |
|                                |                                                                                       | 2                                | Many customers cannot operate it intuitively.                                                                                                                                                                                                                                  |  |
|                                |                                                                                       | 3                                | A large proportion of customers cannot operate it<br>intuitively.                                                                                                                                                                                                              |  |
| SI1                            | Protection of                                                                         | 1                                | Customer's reputation is damaged.                                                                                                                                                                                                                                              |  |
|                                | personal data<br>(including per                                                       | 2                                | Customer's social existence is damaged.                                                                                                                                                                                                                                        |  |
|                                | sonal usage<br>data) – data<br>become known<br>to third parties                       | 3                                | Customer's physical existence is damaged.                                                                                                                                                                                                                                      |  |
| SI2                            | Protection of<br>entitlements                                                         | 1                                | Predicted product-related loss of sales through<br>counterfeiting, damage or manipulation <0.5%.                                                                                                                                                                               |  |
|                                |                                                                                       | 2                                | Predicted product-related loss of sales through<br>counterfeiting, damage or manipulation <3%.                                                                                                                                                                                 |  |
|                                |                                                                                       | 3                                | Predicted product-related loss of sales through<br>counterfeiting, damage or manipulation >3%.                                                                                                                                                                                 |  |
| SI3                            | Protection of<br>logistical data<br>(anonymised<br>usage data) in<br>ternal invoicing | 1                                | Data becomes known to third parties.                                                                                                                                                                                                                                           |  |
|                                |                                                                                       | 2                                | Data is lost.                                                                                                                                                                                                                                                                  |  |
|                                |                                                                                       | 3                                | Data is falsified.                                                                                                                                                                                                                                                             |  |
| SI4                            | Reliable invoic<br>ing                                                                | 1                                | Data is not available.                                                                                                                                                                                                                                                         |  |
|                                |                                                                                       | 2                                | Data is lost.                                                                                                                                                                                                                                                                  |  |
|                                |                                                                                       | 3                                | Data is falsified, misused, etc.                                                                                                                                                                                                                                               |  |
| SI5                            | Protection of<br>applications and<br>entitlements                                     | 1                                | Applications are issued by the same application<br>issuer and entitlements by the same product<br>owner.                                                                                                                                                                       |  |
|                                |                                                                                       | 2                                | Applications are issued by a single application<br>issuer but different application providers, and enti<br>tlements come from different product owners,<br>product providers and service providers. Several<br>companies collaborate and "trust" each other in<br>the process. |  |
|                                |                                                                                       | 3                                | Applications are issued by different application<br>providers, and entitlements by different product<br>owners, product providers and service providers.<br>Several companies collaborate but do not "trust"                                                                   |  |

| Security target |                                                                 | Protection<br>demand<br>category | Criteria for allocating to protection demand cate<br>gory                                            |
|-----------------|-----------------------------------------------------------------|----------------------------------|------------------------------------------------------------------------------------------------------|
|                 |                                                                 |                                  | each other in the process.                                                                           |
| SP3             | Protection<br>against the crea<br>tion of move<br>ment profiles | 1                                | Customer's reputation is damaged.                                                                    |
|                 |                                                                 | 2                                | Customer's social existence is damaged.                                                              |
|                 |                                                                 | 3                                | Customer's physical existence is damaged.                                                            |
| SP4             | Data minimiza<br>tion                                           | 1                                | Personal data, and data that can be linked to par<br>ticular people, is not used.                    |
|                 |                                                                 | 2                                | Personal data is used, but no usage data is col<br>lected.                                           |
|                 |                                                                 | 3                                | Personal data is used, as is usage and calculation<br>data that can be related to particular people. |

**Table 8-12 Definition of protection demand categories** 

# <span id="page-61-0"></span>**8.3 Threats**

This section deals with potential threats to the security targets described in Section [8.2.](#page-53-1) It differentiates between threats to the carrier medium, the reader, the contact-less interface and the system as a whole. The following table shows the scheme of threat codes and used abbreviations.

| field number | 1      | 2                                                | 3                |
|--------------|--------|--------------------------------------------------|------------------|
| field        | threat | associated component and its abbreviation        | index num<br>ber |
|              | T      | C := contact-less interface                      | 1,  , n          |
|              |        | M := carrier medium                              |                  |
| Content      |        | R := reader                                      |                  |
|              |        | K := key management system                       |                  |
|              |        | S := sales, inspection and background<br>systems |                  |

**Table 8–13 Coding scheme of threats** 

### **8.3.1 Threats to the contact-less interface**

| Threat code and name |                                                 | Security<br>targets<br>threatened | Description of threat                                                                                                                        |
|----------------------|-------------------------------------------------|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| TC1                  | Lack of com<br>patibility be<br>tween the inter | SS1                               | Lack of compatibility between interfaces pre<br>vents the system from working when loading<br>and using entitlements, checking entitlements, |

<span id="page-62-0"></span>

| Threat code and name |                                              | Security<br>targets<br>threatened | Description of threat                                                                                                                                                                                                                                                                                                       |
|----------------------|----------------------------------------------|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                      | faces of the<br>carrier medium<br>and reader |                                   | and so on. The result is similar to a DoS attack<br>on the system. Many customers and/or enti<br>tlements may be affected.                                                                                                                                                                                                  |
| TC2                  | Eavesdropping                                | SI1, SI2,<br>SI5                  | Unauthorised listening-in to communication<br>between a carrier medium and a reader.                                                                                                                                                                                                                                        |
| TC3                  | DoS attack on<br>the RF interface            | SS1, SS2,<br>SS3                  | 1<br>Interference in RFID communication<br>(jamming)<br>2<br>Interference in the anti-collision mecha<br>nism for selecting the carrier medium<br>(blocker tag)<br>3<br>Blocking the electromagnetic field of the<br>reader (shielding)<br>4<br>Altering the resonance frequency of reader<br>or carrier medium (de-tuning) |

**Table 8–14 Threats to the contact-less interface** 

### **8.3.2 Threats to the carrier medium**

| Threat code and name |                                                                   | Security<br>targets<br>threatened | Description of threat                                                                                                                                               |
|----------------------|-------------------------------------------------------------------|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TM1                  | Unauthorised<br>scanning of<br>entitlement                        | SI2, SI5                          | Unauthorised, active retrieval of data from car<br>rier medium.                                                                                                     |
| TM2                  | Unauthorised<br>overwriting /<br>manipulation of<br>entitlement   | SI2, SI5,<br>SI4                  | Unauthorised writing of data to carrier medium.                                                                                                                     |
| TM3                  | Cloning of me<br>dium including<br>entitlement                    | SI2, SI5,<br>SI4                  | High-precision copy of carrier media, applica<br>tions or entitlements                                                                                              |
| TM4                  | Emulation of<br>application or<br>entitlement                     | SI2, SI5,<br>SI4                  | Emulating the electrical function of the carrier<br>medium using a programmable device.                                                                             |
| TM5                  | Unauthorised<br>scanning of<br>personal data                      | SI1                               | Unauthorised, active retrieval of personal data<br>stored in the application on a carrier medium.                                                                   |
| TM6                  | Unauthorised<br>overwriting /<br>manipulation of<br>personal data | SI1                               | Unauthorised writing of personal data onto the<br>carrier medium. Also includes the usage data<br>that can be stored in the medium (automatic<br>fare calculation). |
| TM7                  | Unauthorised<br>scanning of                                       | SI4                               | Unauthorised, active retrieval of calculation                                                                                                                       |

<span id="page-63-0"></span>

| Threat code and name |                                                                                                       | Security<br>targets<br>threatened | Description of threat                                                                                                                                                                                                                                                                                                                 |
|----------------------|-------------------------------------------------------------------------------------------------------|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                      | calculation data                                                                                      |                                   | data.                                                                                                                                                                                                                                                                                                                                 |
| TM8                  | Unauthorised<br>overwriting /<br>manipulation of<br>calculation data                                  | SI4                               | Unauthorised writing of calculation data onto<br>the carrier medium for the purpose of manipu<br>lation and/or compromise of data.                                                                                                                                                                                                    |
| TM9                  | Threat through<br>insufficient pro<br>tection of addi<br>tional applica<br>tions and enti<br>tlements | SI5                               | If multiple entitlements and applications are on<br>one carrier medium, these may be influenced<br>or damaged when used together.                                                                                                                                                                                                     |
| TM10                 | Carrier medium<br>malfunction                                                                         | SS1, SS2                          | Carrier medium malfunctions can be caused in<br>a range of scenarios by technical faults, incor<br>rect operation, or DoS attacks:<br>1<br>Fault in contact-less interface<br>2<br>Fault in reference information (keys, etc.)<br>3<br>Fault in application implementation<br>4<br>Fault in entitlements<br>5<br>Physical destruction |
| TM11                 | Tracking by<br>means of unau<br>thorised scan<br>ning by third<br>parties                             | SP3                               | The anti-collision mechanism in the carrier<br>medium sends a non-encrypted identifier to<br>every reader that sends out a request. This<br>can be used by unauthorised persons to re<br>trieve the carrier medium's identifier, and pos<br>sibly to generate movement profiles based on<br>that identifier.                          |
| TM12                 | Lack of fallback<br>solution in the<br>event of mal<br>function                                       | SS2                               | The lack of a failsafe method of assessing the<br>genuineness or identity of the medium in the<br>event of a defective chip can cause difficulties<br>when it comes to blocking and replacing.                                                                                                                                        |

**Table 8–15 Threats to the carrier medium** 

### **8.3.3 Threats to the reader**

| Threat code and name |                                                              | Security<br>targets<br>threatened | Description of threat                                                                                                                                     |
|----------------------|--------------------------------------------------------------|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| TR1                  | Unauthorised<br>manipulation of<br>reference in<br>formation | SI1, SI2,<br>SI3, SI4,<br>SI5     | Manipulation of reference information (keys,<br>evaluation algorithms, blacklists and whitelists)<br>can be employed for unauthorised use and for<br>DoS. |
| TR2                  | Unauthorised<br>scanning of                                  | SI1, SI2,<br>SI4, SI5             | The retrieval of reference information (keys,<br>evaluation algorithms, blacklists and whitelists)                                                        |

<span id="page-64-0"></span>

| Threat code and name |                              | Security<br>targets<br>threatened | Description of threat                                                                                                                                                                  |
|----------------------|------------------------------|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                      | reference in<br>formation    |                                   | can be employed for unauthorised use (e.g.<br>counterfeiting of entitlements) and for DoS.                                                                                             |
| TR3                  | Reader mal<br>function       | SS1, SS2                          | Reader malfunctions can be caused in a range<br>of scenarios by technical faults, incorrect op<br>eration or DoS attacks:                                                              |
|                      |                              |                                   | 1<br>Fault in contact-less interface                                                                                                                                                   |
|                      |                              |                                   | 2<br>Fault in reference information (keys, black<br>lists, etc)                                                                                                                        |
|                      |                              |                                   | 3<br>Fault in application implementation                                                                                                                                               |
|                      |                              |                                   | 4<br>Fault in evaluation algorithms for entitle<br>ments                                                                                                                               |
|                      |                              |                                   | 5<br>Fault in power supply                                                                                                                                                             |
|                      |                              |                                   | 6<br>Interruption of the link to the central sys<br>tem                                                                                                                                |
|                      |                              |                                   | 7<br>Physical destruction                                                                                                                                                              |
|                      |                              |                                   | 8<br>Fault in operational instruction functions                                                                                                                                        |
| TR4                  | Lack of user<br>instructions | SS3                               | A lack of user-friendliness at vending machines<br>and the terminals used for activating entitle<br>ments and checking-in / checking-out can<br>cause considerable operative problems. |

**Table 8–16 Threats to the reader** 

### **8.3.4 Threats to the key management system**

| Threat code and name |                                         | Security<br>targets<br>threatened | Description of threat                                                                                                                                                                                                                                                                                              |
|----------------------|-----------------------------------------|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TK1                  | Quality of key<br>data                  | SI1, SI2,<br>SI3, SI4,<br>SI5     | Deficient key quality increases the chances of<br>successful attacks.                                                                                                                                                                                                                                              |
| TK2                  | Unauthorised<br>scanning of key<br>data | SI1, SI2,<br>SI3, SI4,<br>SI5     | The retrieval of key data by unauthorised per<br>sons can discredit the system and facilitate<br>attacks, e.g. on any cryptographically protected<br>data or functions.                                                                                                                                            |
| TK3                  | Manipulation of<br>key data             | SI1, SI2,<br>SI3, SI4,<br>SI5     | The manipulation of key data can discredit the<br>system's security concept and facilitate at<br>tacks, e.g. on any cryptographically protected<br>data or functions. Manipulation can affect the<br>generation of keys, the production of key<br>carriers, the transmission of keys and the local<br>use of keys. |
| TK4                  | Key manage<br>ment system               | SS1, SS2                          | Key management system malfunctions can be<br>caused in a variety of scenarios by technical                                                                                                                                                                                                                         |

<span id="page-65-0"></span>

| Threat code and name |                              | Security<br>targets<br>threatened | Description of threat                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------|------------------------------|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                      | malfunction                  |                                   | faults, incorrect operation or DoS attacks:<br>1<br>Fault in local and central systems<br>2<br>Lack of availability of local and central<br>systems<br>3<br>Fault in data storage<br>4<br>Fault in specific application implementa<br>tion<br>5<br>Fault in evaluation algorithms for entitle<br>ments<br>6<br>Fault in power supply<br>7<br>Interruption of the link to the central sys<br>tem<br>8<br>Physical destruction |
| TK5                  | Lack of fallback<br>solution | SS2                               | The availability of the necessary key informa<br>tion is essential if the system as a whole is to<br>work at all. If the key management system mal<br>functions and there is no fallback solution, the<br>function of the entire system will be threatened.                                                                                                                                                                  |

| Table 8–17 | Threats to the key management system |
|------------|--------------------------------------|
|------------|--------------------------------------|

### **8.3.5 Threats to the sales, inspection and backend systems**

| Threat code and name |                                                    | Security<br>targets<br>threatened  | Description of threat                                                                                                                                                                                                                                                               |
|----------------------|----------------------------------------------------|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TS1                  | Lack of fallback<br>solution                       | SS2, SI4                           | The lack of a fallback solution when system<br>components fail, such as the ticket sales sys<br>tem, administration system for carrier media<br>and entitlements, and verification system, can<br>lead to a complete breakdown of services<br>(sales, invoicing, acceptance, etc.). |
| TS2                  | Unauthorised<br>scanning of<br>reference data      | SS1, SI1,<br>SI2, SI3,<br>SI4, SI5 | The background systems store information<br>about the media, entitlements and usage, and<br>sometimes personal data and calculation data.<br>The retrieval of this data by unauthorised per<br>sons would discredit the system and enable<br>attacks.                               |
| TS3                  | Manipulation of<br>reference data<br>in the system | SS1, SI1,<br>SI2, SI3,<br>SI4, SI5 | The background systems store information<br>about the media, entitlements and usage, and<br>sometimes personal data and calculation data.<br>The manipulation of this data by unauthorised<br>persons represents a serious threat.                                                  |
| TS4                  | System mal<br>function                             | SS1, SS2                           | Individual system component malfunctions can<br>be caused in a range of scenarios by technical                                                                                                                                                                                      |

<span id="page-66-0"></span>

| Threat code and name |                                                                                    | Security<br>targets<br>threatened | Description of threat                                                                                                                                                                                                                                                                                   |
|----------------------|------------------------------------------------------------------------------------|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                      |                                                                                    |                                   | faults, incorrect operation or DoS attacks:<br>1<br>Fault in local and central systems<br>2<br>Lack of availability of local and central<br>systems<br>3<br>Fault in data storage<br>4<br>Fault in power supply<br>5<br>Interruption of the link to the central sys<br>tem<br>6<br>Physical destruction |
| TS5                  | Lack of com<br>patibility be<br>tween inter<br>faces                               | SS1                               | Lack of compatibility between interfaces<br>causes malfunctions. The result is similar to a<br>DoS attack on the system. Many customers<br>and/or entitlements may be affected.                                                                                                                         |
| TS6                  | Unauthorised<br>scanning of<br>sales and calcu<br>lation data                      | SI4                               | Unauthorised, active retrieval of calculation<br>data.                                                                                                                                                                                                                                                  |
| TS7                  | Unauthorised<br>overwriting /<br>manipulation of<br>sales and calcu<br>lation data | SI4                               | Unauthorised writing of calculation data onto<br>the carrier medium or into background systems<br>for the purpose of manipulating or compromis<br>ing data.                                                                                                                                             |
| TS8                  | Protection of<br>client-specific<br>applications and<br>entitlements               | SI5                               | If multiple entities are supported by the system<br>with sales data, entitlements and applications,<br>these may be influenced or damaged when<br>used mutually.                                                                                                                                        |
| TS9                  | Falsification of<br>identity data                                                  | SI2                               | Identification may be required when purchas<br>ing or collecting a product. Using a false iden<br>tity would allow someone to obtain benefits<br>such as entitlements to the detriment of other<br>customers or the product provider.                                                                   |
| TS10                 | Unjustified<br>gathering and<br>storing of data                                    | SP4                               | Gathering and storing data without justification<br>infringes the stipulation on data minimization.                                                                                                                                                                                                     |

**Table 8–18 Threats to the sales, inspection and backend systems** 

# <span id="page-66-1"></span>**8.4 Safeguards**

This section describes the safeguards that can be used to counter the threats detailed in Section [8.3.](#page-61-0) These safeguards are defined in such a way that, when built successively upon each other, they afford increasing levels of security – in cases where different levels are possible. Level 1 represents the lowest security category, level 3 the highest.

<span id="page-67-0"></span>Level 3+ is used to denote additional safeguards that increase the security of a system, but whose expense may exceed the value of the extra security gained disproportionately.

The security levels are oriented around the system's protection demand categories. A threat to a security target that has been allocated to protection demand category 3 should be countered by safeguards of security level 3. Generally threats of a specific protection demad category can be countered by safeguards of the same or higher protection demand categories.

The following safeguards are generally not defined as isolated measures, but rather are to be understood as "safeguard packages". As a rule, the security of components and interfaces, and of the system as a whole, can only be increased in a meaningful way if safeguards are employed across the board as packages. Furthermore, alternative possibilities are defined within the security levels; for instance, a secure environment (which generally does not exist) can replace the encrypted storage of data.

The following table shows the scheme of safeguard or measure codes and used abbreviations.

| field number | 1                      | 2                                                | 3                |
|--------------|------------------------|--------------------------------------------------|------------------|
| field        | safeguard /<br>measure | associated component and its abbreviation        | index num<br>ber |
|              | M                      | C := contact-less interface                      | 1,  , n          |
|              |                        | M := carrier medium                              |                  |
| content      |                        | R := reader                                      |                  |
|              |                        | K := key management system                       |                  |
|              |                        | S := sales, inspection and background<br>systems |                  |

**Table 8–19 Coding scheme of safeguard measures** 

### <span id="page-67-2"></span>**8.4.1 Selection of cryptographic methods and key length**

The following safeguards generally require cryptographic methods that shall follow the rules given in [ALGK\_BSI]. [ALGK\_BSI] defines methods, key length and the useful life of those. [ALGK\_BSI] will be updated made available to the public by BSI on a regular basis.

Existing implementations shall comply to the rules given in [ALGK\_BSI] or [TR\_eCARD]. With the next evolution step existing systems shall be migrated in order to comply to [ALGK\_BSI]. This update has to be carried out in an appropriate period of time. Under this precondition, the utilization of the TDES algorithm is allowed for authentication, encryption and generation of MAC.

### <span id="page-67-1"></span>**8.4.2 Safeguards for the protection of the system as a whole**

The following safeguards relate to the system as a whole, the focus being on the sales, inspection and management systems, including the associated interfaces.

Separate sections will deal with the RF interface; readers installed in terminals, vending machines and so on; carrier media; and the key management system.

<span id="page-68-0"></span>

| MS1     | Code and name of safeguard                                                                                                                                                                                                                                                                      | Threats addressed |  |  |  |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|--|--|
|         | Introduction of interface tests and approval<br>procedures                                                                                                                                                                                                                                      | TS5, TC1          |  |  |  |
| General | The aim of introducing interface-based test specifications and performing these<br>tests on all components is to achieve compatibility between components and to<br>enable this to be verified. This process should include all levels of the interfaces<br>(OSI model), including fault cases. |                   |  |  |  |
|         | Interface test                                                                                                                                                                                                                                                                                  |                   |  |  |  |
| 1       | •<br>Apply existing test regulations (in particular [BSI_PICC_TestSpec] and<br>[BSI_PCD_TestSpec]) for contact-less interfaces as defined by<br>ISO/IEC14443.                                                                                                                                   |                   |  |  |  |
|         | •<br>Draw up and apply specific test regulations for the application-specific func<br>tions of carrier media and reader interfaces.                                                                                                                                                             |                   |  |  |  |
|         | •<br>Draw up and apply specific test regulations for the protocols and applica<br>tion-specific functions of the interfaces between the rest of the system com<br>ponents.                                                                                                                      |                   |  |  |  |
| 2       | Component approval                                                                                                                                                                                                                                                                              |                   |  |  |  |
|         | •<br>See above, additional component approval (carrier medium, readers, key<br>management).                                                                                                                                                                                                     |                   |  |  |  |
| 3       | Certification                                                                                                                                                                                                                                                                                   |                   |  |  |  |
|         | •<br>See above, additional certification by an independent institution, for carrier<br>media, readers and, where necessary, other components.                                                                                                                                                   |                   |  |  |  |

#### **Table 8–20 Protection of the system as a whole through introduction of interface tests and approval procedures**

| MS2     | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                                | Threats addressed |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|         | Ensuring the confidentiality of communication<br>between carrier medium and reader in order to<br>prevent eavesdropping                                                                                                                                                                                                                                                                                   | TC2               |
| General | This safeguard applies to every implementation of a contact-less interface that<br>exists between the carrier medium and readers such as the ones installed in<br>vending machines, sales terminals, ticket printers and CICO terminals.                                                                                                                                                                  |                   |
| 1       | Transmission security:                                                                                                                                                                                                                                                                                                                                                                                    |                   |
|         | •<br>If a secure channel compliant with MS2.2 or MS2.3 cannot be established,<br>then the data is encrypted by the terminal and sent to the carrier media.                                                                                                                                                                                                                                                |                   |
|         | •<br>The carrier media can be simple storage media.                                                                                                                                                                                                                                                                                                                                                       |                   |
|         | Mutual authentication during transmission:                                                                                                                                                                                                                                                                                                                                                                |                   |
| 2       | •<br>Before data is transmitted, both sides are authenticated using permanent<br>symmetric keys in order to negotiate a common encrypting key. The en<br>crypting key negotiated is used to encrypt the data by means of AES128, T<br>DES or a comparable open encryption algorithm. The type and strength of<br>the mechanism should be adapted to future developments in accordance<br>with [ALGK_BSI]. |                   |

<span id="page-69-0"></span>

| MS2 | Code and name of safeguard                                                                                                                                                                                                                                   | Threats addressed |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|     | Ensuring the confidentiality of communication<br>between carrier medium and reader in order to<br>prevent eavesdropping                                                                                                                                      | TC2               |
|     | Mutual, dynamic authentication during transmission:                                                                                                                                                                                                          |                   |
| 3   | •<br>Implementation of a dynamic encryption procedure.<br>Here, before data is transmitted between the carrier medium and reader, a<br>shared key is negotiated using a suitable challenge and response process;<br>this key is then used for communication. |                   |
|     | •<br>The algorithms and key lengths should be chosen in accordance with the<br>latest technology. The following can be used currently: TDES encryption,<br>AES128, RSA with at least 1024 bit, ECC or comparable.                                            |                   |
|     | •<br>The type and strength of the mechanism should be adapted to future devel<br>opments in accordance with [ALGK_BSI].                                                                                                                                      |                   |

| Table 8–21 | Protection of the system as a whole through ensuring the confidential |
|------------|-----------------------------------------------------------------------|
|            | ity of communication                                                  |

|     | Code and name of safeguard                                                                            | Threats addressed |
|-----|-------------------------------------------------------------------------------------------------------|-------------------|
| MS3 | Introduction of contact-less interface as de<br>fined by ISO/IEC14443, or use of field detec<br>tors. | TC2, TC3          |
| 1   |                                                                                                       |                   |
| 2   | Introduction of contact-less proximity interface as defined by ISO/IEC14443.                          |                   |
| 3   |                                                                                                       |                   |
| 3+  | Additional field detectors are used.                                                                  |                   |

#### **Table 8–22 Protection of the system as a whole through introduction of contactless interface as defined by ISO/IEC14443**

| MS4 | Code and name of safeguard                                                                                                                                                                                | Threats addressed |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|     | Definition of fallback solutions in the event of<br>system interface or system component failure                                                                                                          | TS1, TS4          |
| 1   | Definition of suitable operating processes, offline capability and backup:                                                                                                                                |                   |
| 2   | •<br>System components must in principle (at least temporarily) be able to func<br>tion autonomously without a background system, and if system interfaces<br>fail.                                       |                   |
|     | •<br>Data must be backed up regularly in order to exclude the possibility of a<br>total loss.                                                                                                             |                   |
|     | •<br>The replacement of defective components must be regulated.                                                                                                                                           |                   |
|     | •<br>All components and interfaces must have fallback processes that employ<br>operative safeguards to rectify or moderate the operative problems that can<br>arise following the failure of a component. |                   |
|     | •<br>Fallback solutions must be specified in the contractual arrangements be<br>tween customers, service providers and suppliers, and their consequences<br>taken into account.                           |                   |

<span id="page-70-0"></span>

| MS4 | Code and name of safeguard                                                                                                                                                                                                                                                | Threats addressed |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|     | Definition of fallback solutions in the event of<br>system interface or system component failure                                                                                                                                                                          | TS1, TS4          |
|     | Implementation according to fallback concept:                                                                                                                                                                                                                             |                   |
| 3   | In addition to 1, 2:                                                                                                                                                                                                                                                      |                   |
|     | •<br>A system concept must be developed that defines the availability and fall<br>back solutions explicitly with availability periods and fallback intervals.                                                                                                             |                   |
|     | •<br>Critical components must have an uninterruptible power supply (UPS) and<br>other security mechanisms, such as a redundand array of inexpensive disks<br>(RAID), so that the failure of sub-components does not impair the availabil<br>ity of the system as a whole. |                   |
|     | •<br>If necessary enough replacement carrier media must be provided to enable<br>the required availability to be upheld.                                                                                                                                                  |                   |

#### **Table 8–23 Protection of the system as a whole through definition of fallback solutions**

| MS5 | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Threats addressed |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|     | Securing the confidentiality of data when<br>communicating within the system                                                                                                                                                                                                                                                                                                                                                                                                                                   | TS2, TS6          |
| 1   | Static encryption for internal communication:                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                   |
| 2   | •<br>Data is transmitted in encrypted form; static encryption processes are used.<br>Alternatively, instead of general data encryption, data can be sent via dedi<br>cated networks (closed solution), in which only authorised users are admin<br>istered and allowed. This network would need to be protected against<br>physical attacks from the outside by means of appropriate safeguards (e.g.<br>basic protective measures), and then operated in accordance with an ap<br>propriate security concept. |                   |
| 3   | Secure communication channel:<br>•<br>Communication between the components of the system is via VPNs or simi<br>lar (shielded) solutions. Before communication, authentication is performed<br>by negotiating a key between sender and receiver. The negotiated key is<br>then used for communication.                                                                                                                                                                                                         |                   |

#### **Table 8–24 Protection of the system as a whole through securing the confidentiality of data**

| MS6 | Code and name of safeguard                                                                                                                                                                                                        | Threats addressed       |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
|     | Confidential storage of data                                                                                                                                                                                                      | TS2, TS3, TS6, TS7, TS8 |
| 1   | Introduction of multi-tenant access protection:                                                                                                                                                                                   |                         |
|     | •<br>Only a certain, legitimised group of people can access stored data (per<br>sonal data, sales data, usage data, calculation data, blacklists, approval<br>lists, etc.).                                                       |                         |
| 2   | •<br>Data is stored in an environment protected against unauthorised access. If<br>access protection cannot be guaranteed, then the data should be stored on<br>an encrypted data carrier (hard drive encryption tools are used). |                         |

<span id="page-71-0"></span>

| MS6 | Code and name of safeguard                                                                                                                                                                                                                                                     | Threats addressed       |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
|     | Confidential storage of data                                                                                                                                                                                                                                                   | TS2, TS3, TS6, TS7, TS8 |
|     | Alternatively, other equally effective encryption mechanisms can be used. The<br>algorithm strength must be at least that of the TDES algorithm. The type and<br>strength of the mechanism must be adjusted in line with future developments in<br>accordance with [ALGK_BSI]. |                         |
|     | Introduction of multi-tenant access protection with a defined role model.                                                                                                                                                                                                      |                         |
| 3   | See 1-2, and also:                                                                                                                                                                                                                                                             |                         |
|     | •<br>A client concept in the form of a role model is established.                                                                                                                                                                                                              |                         |

| Table 8–25 | Protection of the system as a whole through confidential storage of |
|------------|---------------------------------------------------------------------|
|            | data                                                                |

|     | Code and name of safeguard                                                                                                                                                                                                                                                                                                        | Threats addressed |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| MS7 | Securing the data integrity in order to protect<br>against manipulation when transmitting data<br>within the system                                                                                                                                                                                                               | TS3, TS7          |
| 1   | Cryptographic integrity safeguards:                                                                                                                                                                                                                                                                                               |                   |
| 2   | •<br>The integrity of data transmission is guaranteed using MAC protection. The<br>algorithm shall be selected in accordance with [ALGK_BSI].<br>•<br>The type and strength of the mechanism must be adjusted in line with future<br>developments in accordance with [ALGK_BSI].                                                  |                   |
| 3   | MAC or signatures:<br>•<br>The integrity of data transmission is guaranteed by MAC protection or by<br>signatures. MAC- and signature mechanisms shall be selected according to<br>[ALGK_BSI].<br>•<br>The type and strength of the mechanism must be adjusted in line with future<br>developments in accordance with [ALGK_BSI]. |                   |

**Table 8–26 Protection of the system as a whole through securing the data integrity when transmitting data** 

| MS8 | Code and name of safeguard                                                                                                                                                                               | Threats addressed |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|     | Securing data integrity when storing data                                                                                                                                                                | TS3, TS7          |
| 1   | Data is stored in a secure environment where unauthorised persons cannot ac<br>cess it.                                                                                                                  |                   |
| 2   |                                                                                                                                                                                                          |                   |
| 3   | Checksums:<br>•<br>A checksum is used to protect (CRC, hamming codes, ) against integrity<br>errors that are caused by technical reasons; this can also be provided by<br>the operating system involved. |                   |

**Table 8–27 Protection of the system as a whole through securing data integrity when storing data** 

<span id="page-72-0"></span>

| MS9     | Code and name of safeguard                                                                                                                                                                                                                                                                                                                    | Threats addressed |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|         | Securing the system's functions against DoS<br>attacks at the interfaces                                                                                                                                                                                                                                                                      | TS4               |
| General | The system can be secured against DoS attacks at the interfaces or on the<br>transmission routes by means of structural, technical and organisational safe<br>guards. Various safeguards can be used, depending on the security level.                                                                                                        |                   |
| 1       | Advanced structural, technical and organisational safeguards:<br>•<br>Structural safeguards: protect the transmission routes against wanton de<br>struction, e.g. by using indestructible materials and shielding data lines.<br>Create secure areas.<br>•<br>Organisational safeguards: simple access control to secure areas (photo<br>ID). |                   |
| 2       | Extended structural, technical and organisational safeguards:<br>•<br>Additional organisational safeguards, such as the introduction of a role<br>model with an accompanying entitlement concept. More thorough mechani<br>cal protection.                                                                                                    |                   |
| 3       | Security concept<br>See 1, enhanced by:<br>•<br>Implement structural and technical safeguards in accordance with a security<br>concept.<br>Technical safeguards: technical safeguarding of access control.                                                                                                                                    |                   |

#### **Table 8–28 Protection of the system as a whole through securing the system's functions against DoS attacks**

| MS10 | Code and name of safeguard                                                                                                                          | Threats addressed |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|      | Securing the function of the system against<br>incorrect operation by employees and users                                                           | TS4               |
| 1    | Tests, personnel and user introductions:                                                                                                            |                   |
| 2    | •<br>Define the requirements for user introductions; check the components using<br>these requirements; empirical tests; employ knowledgeable staff. |                   |
| 3    |                                                                                                                                                     |                   |

#### **Table 8–29 Protection of the system as a whole through securing the function of the system against incorrect operation**

| MS11 | Code and name of safeguard                                                                                          | Threats addressed |
|------|---------------------------------------------------------------------------------------------------------------------|-------------------|
|      | Securing the function of the system to prevent<br>technical failures of components and trans<br>mission routes      | TS4, TS5          |
|      | Manufacturer's declaration:                                                                                         |                   |
| 1    | •<br>Guarantee safety in accordance with specifications, by means of manufac<br>turer's internal quality assurance. |                   |

<span id="page-73-0"></span>

|      | Code and name of safeguard                                                                                                                                                                                                                                                                                                          | Threats addressed |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| MS11 | Securing the function of the system to prevent<br>technical failures of components and trans<br>mission routes                                                                                                                                                                                                                      | TS4, TS5          |
| 2    | Testing in accordance with test specifications:<br>•<br>Draw up test specifications for the various system components.<br>•<br>Technical checking of components in accordance with the relevant test<br>specifications.<br>•<br>Specification and execution of integration tests in test and actual environ<br>ments.               |                   |
| 3    | Evaluation of components:<br>See 2, and also:<br>•<br>The relevant system components (at least the readers and carrier media)<br>are tested by independent testing laboratories.<br>•<br>An independent institution certifies the relevant system components.<br>•<br>An approval process is established for the system components. |                   |

| Table 8–30 | Protection of the system as a whole through securing the function of |
|------------|----------------------------------------------------------------------|
|            | the system to prevent technical failures                             |

| MS12    | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Threats addressed |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|         | Specifications for system concept and re<br>quirements for components                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | TS4, TS5          |
| General | The characteristics of a system in relation to its fundamental operating proc<br>esses must be specified and assured. Take note: existing components often<br>have to be integrated, yet the fundamental parameters and characteristics of the<br>system as a whole must be specified and achieved. This applies in particular to<br>the performance and availability of certain processes. To enable this integration<br>into the system as a whole, the requirements for each system component's in<br>teraction with the system as a whole must be specified and upheld.<br>Special attention should be paid to the incorporation of new applications and<br>products. |                   |
| 1       | Manufacturer's declaration:<br>•<br>The manufacturer guarantees that the specifications are adhered to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                   |
|         | Integration test and declaration of conformity:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                   |
| 2       | •<br>Draw up and perform integration tests (see MS11).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                   |
|         | •<br>Establish an approval procedure.<br>•<br>Conformity must be proven by integration tests.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                   |
|         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                   |

<span id="page-74-0"></span>

| MS12 | Code and name of safeguard                                            | Threats addressed |
|------|-----------------------------------------------------------------------|-------------------|
|      | Specifications for system concept and re<br>quirements for components | TS4, TS5          |
|      | Interoperability tests according to test concept, evaluation:         |                   |
| 3    | •<br>Draw up and perform integration tests (see MS11).                |                   |
|      | •<br>Establish an approval procedure.                                 |                   |
|      | •<br>Components evaluated by independent test laboratories.           |                   |
|      | •<br>Certification of components.                                     |                   |

| Table 8–31 | Protection of the system as a whole through specification of the sys |
|------------|----------------------------------------------------------------------|
|            | tem and the components                                               |

| MS13    | Code and name of safeguard                                                                                                                                                                                                                                                                             | Threats addressed |  |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|         | Ergonomic user instructions                                                                                                                                                                                                                                                                            | TS4, TR4          |  |
| General | The design of all hardware components must fulfil certain ergonomic require<br>ments. These include, as well as visual demands (recollection, colour of key<br>pads, legibility of displays ), requirements relating to operation (including for<br>the severely disabled), and safety against injury. |                   |  |
|         | Manufacturer's declaration:                                                                                                                                                                                                                                                                            |                   |  |
| 1       | •<br>Manufacturer declares that ergonomic principles have been applied.                                                                                                                                                                                                                                |                   |  |
|         | •<br>The relevant use cases from the generic operating processes (e.g. sale,<br>check-in, and so on) are illustrated by the manufacturer to help instruct cus<br>tomers and staff.                                                                                                                     |                   |  |
|         | Practical testing:                                                                                                                                                                                                                                                                                     |                   |  |
|         |                                                                                                                                                                                                                                                                                                        |                   |  |
| 2       | •<br>Manufacturer declares that ergonomic principles have been applied.                                                                                                                                                                                                                                |                   |  |
|         | •<br>User acceptance is gauged in a practical test.                                                                                                                                                                                                                                                    |                   |  |
|         | Specification, implementation and testing of an overall concept for ergonomics<br>and user instruction:                                                                                                                                                                                                |                   |  |
| 3       | •<br>System-wide definitions must be laid down relating to ergonomics and user<br>instructions, and these must guarantee that all of the components within the<br>system satisfy the same standards. Gradual introduction is possible.                                                                 |                   |  |
|         | •<br>Implement uniform user instructions for each application.                                                                                                                                                                                                                                         |                   |  |
|         | •<br>Practical testing for assessing user acceptance.<br>•<br>Approval procedure for overall and component specifications.                                                                                                                                                                             |                   |  |

| Table 8–32 | Protection of the system as a whole through ergonomic user instruc |
|------------|--------------------------------------------------------------------|
|            | tions                                                              |

| MS14 | Code and name of safeguard                                                                                                                                                                                                            | Threats addressed |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|      | Support                                                                                                                                                                                                                               | TS4, TS5          |
|      | Manufacturer support:                                                                                                                                                                                                                 |                   |
| 1    | •<br>The manufacturer of system components must put measures in place that<br>assist users when operating the system (e.g. help desk, 1st, 2nd, 3rd-level<br>support, …). This support is subject to bilateral contractual regulation |                   |

<span id="page-75-0"></span>

| MS14 | Code and name of safeguard                                                                                                                                                                                                                             | Threats addressed |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|      | Support                                                                                                                                                                                                                                                | TS4, TS5          |
|      | (SLAs) between the manufacturer and the service provider.                                                                                                                                                                                              |                   |
|      | Entity-wide support:                                                                                                                                                                                                                                   |                   |
| 2    | •<br>Define a support concept for the system belonging to an entity (e.g. service<br>provider, product provider).                                                                                                                                      |                   |
|      | System-wide support:                                                                                                                                                                                                                                   |                   |
| 3    | •<br>Define an umbrella support concept that covers the systems belonging to<br>the various entities (see 2) and also defines interfaces to the other entities.<br>The aim is to be able to solve system-wide problems within a defined time<br>frame. |                   |

| Table 8–33 |  | Protection of the system as a whole through support |
|------------|--|-----------------------------------------------------|
|            |  |                                                     |

| MS15 | Code and name of safeguard                                                                                                                        | Threats addressed       |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
|      | Separation of applications                                                                                                                        | TS2, TS3, TS6, TS7, TS8 |
| 1    | Separate storing and processing of data                                                                                                           |                         |
| 2    | •<br>In order to prevent the malfunction and misuse of key materials and data,                                                                    |                         |
| 3    | the applications must be separated in all of the system's components. Chip<br>based components (carrier media, SAM) will be discussed separately. |                         |

#### **Table 8–34 Protection of the system as a whole through separation of applications**

| MS16    | Code and name of safeguard                                                                                                                                                       | Threats addressed |  |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|         | Identifying the customer when selling and<br>handing over products                                                                                                               | TS9               |  |
| General | The identity of the customer must be established when setting up a customer<br>account, ordering and collecting personalised products, and blocking.                             |                   |  |
| 1       | Declaration by customer:                                                                                                                                                         |                   |  |
|         | •<br>The customer submits the details of his or her identity verbally or on the<br>Internet.                                                                                     |                   |  |
| 2       | Application form, customer cards:                                                                                                                                                |                   |  |
|         | •<br>The customer declares himself in writing and signs to confirm his identity.<br>The product provider checks the information using conventional means:<br>•<br>Address check. |                   |  |
|         | •<br>Sending the customer medium to the address given.                                                                                                                           |                   |  |
|         | •<br>Identity data is passed into the system (Internet, vending machine) from an<br>existing secure customer medium.                                                             |                   |  |
| 3       | Identity document check when setting up a customer account and handing over<br>entitlements                                                                                      |                   |  |
|         | •<br>Secure identification with photograph is presented.                                                                                                                         |                   |  |
|         | •<br>The identity data is taken into the system from a secure electronic identity                                                                                                |                   |  |

<span id="page-76-0"></span>

| MS16 | Code and name of safeguard                                         | Threats addressed |
|------|--------------------------------------------------------------------|-------------------|
|      | Identifying the customer when selling and<br>handing over products | TS9               |
|      | card (eID).                                                        |                   |

**Table 8–35 Protection of the system as a whole through identifying the customer** 

| MS17    | Code and name of safeguard                                                                                                                                                                                                                                                 | Threats addressed |  |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|         | Satisfying the data minimization obligation                                                                                                                                                                                                                                | TS10              |  |
| General | Data minimization must be satisfied in accordance with the applicable legal<br>regulations on privacy.                                                                                                                                                                     |                   |  |
| 1       | Satisfying legal requirements:                                                                                                                                                                                                                                             |                   |  |
| 2       | •<br>When the processes and system as a whole are being defined, the principle<br>of data minimization is applied in accordance with the legal foundations.<br>This requires in particular the definition of deadlines for deletion of data that<br>isn't needed any more. |                   |  |
|         | Special safeguards                                                                                                                                                                                                                                                         |                   |  |
| 3       | In addition to those given in MS17.2, the following measures will be deployed:                                                                                                                                                                                             |                   |  |
|         | •<br>Precise, purpose-related definition of data content; data and access/usage<br>rights are acquired and stored using the role model of the system as a<br>whole.                                                                                                        |                   |  |
|         | •<br>The customer is informed about the purpose-related acquisition, storage<br>and use of personal data and data that can be related to particular people.                                                                                                                |                   |  |

| Table 8–36 | Protection of the system as a whole through satisfying the data mini |
|------------|----------------------------------------------------------------------|
|            | mization obligation                                                  |

### **8.4.3 Safeguards relating to the carrier medium**

| MM1 | Code and name of safeguard                                                                                                                                                        | Threats addressed                               |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
|     | Hardware and software access protection<br>(read and write access)                                                                                                                | TM1, TM2, TM3, TM4, TM5,<br>TM6, TM7, TM8, TM10 |
| 1   | Write protection:                                                                                                                                                                 |                                                 |
|     | •<br>Once imported into the relevant storage areas, the entitlement data and<br>activation data is protected irreversibly against overwriting. Read protection<br>is not applied. |                                                 |
|     | Simple access protection:                                                                                                                                                         |                                                 |
|     | •<br>Alternatively, or additionally, simple access protection is used. The access<br>protection employs password protection or an authentication mechanism.                       |                                                 |
|     | Specific access protection                                                                                                                                                        |                                                 |
| 2   | •<br>Perform mutual authentication with the reader before every access, using<br>random numbers and secret keys stored in the carrier medium.                                     |                                                 |
|     | •<br>Introduce access rights and keys specific to applications and entitlements.                                                                                                  |                                                 |

<span id="page-77-0"></span>

| MM1 | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                                                                           | Threats addressed                               |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
|     | Hardware and software access protection<br>(read and write access)                                                                                                                                                                                                                                                                                                                                                                                   | TM1, TM2, TM3, TM4, TM5,<br>TM6, TM7, TM8, TM10 |
|     | •<br>Utilise diversified keys.<br>•<br>Possible authentication methods include TDES, AES128, or comparable<br>open methods. The type and strength of the mechanism must be adjusted                                                                                                                                                                                                                                                                  |                                                 |
|     | in line with future developments in accordance with [ALGK_BSI].                                                                                                                                                                                                                                                                                                                                                                                      |                                                 |
| 3   | Advanced access protection:<br>•<br>Perform mutual authentication with the reader before every access, using<br>random numbers and secret keys stored in the carrier medium.<br>•<br>Introduce hierarchical access rights and keys specific to applications and<br>entitlements.<br>•<br>Utilise diversified keys.                                                                                                                                   |                                                 |
|     | Possible authentication mechanisms include standardised symmetric methods<br>(TDES, AES128 or comparable open methods) and asymmetric mechanisms<br>(RSA, ECC). RSA and ECC have to be implemented according to the valid ver<br>sion of [ALGK_BSI]. The type and strength of the mechanism must be adjusted<br>in line with future developments in accordance with [ALGK_BSI].<br>•<br>Protection mechanisms against hardware attacks are required. |                                                 |
|     | •<br>The chip should be security-certified according to [HW_PP1] or [HW_PP2].                                                                                                                                                                                                                                                                                                                                                                        |                                                 |

| Table 8–37 | Protection of the transponder through access protection |
|------------|---------------------------------------------------------|
|------------|---------------------------------------------------------|

| MM2                                                                    | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Threats addressed |
|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|                                                                        | Protection against cloning of carrier medium<br>with entitlement                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | TM3               |
| 1                                                                      | Simple protection against cloning of carrier medium:<br>•<br>Implementation of access protection in accordance with MM1.1 to prevent<br>the data content from being retrieved.<br>•<br>Use an UID – a globally unique, unchangeable identifier for the chip, which<br>prevents the carrier medium and entitlement from being duplicated; the UID<br>is integrated into the encryption of the entitlement.<br>•<br>Optional introduction of authentication based on a non-retrievable, secret<br>key.<br>•<br>Use simple visual security features (e.g. hologram). |                   |
|                                                                        | •<br>Introduce a zero-balance procedure when managing non-personalised,<br>printed carrier media.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                   |
| 2                                                                      | Protection against cloning of carrier medium and data content:<br>•<br>Implementation of access protection in accordance with MM1.2 to prevent<br>the data content from being retrieved.<br>•<br>Use an UID – a globally unique, unchangeable identifier for the chip, which<br>prevents the carrier medium, applications and entitlement from being dupli<br>cated; the UID is integrated into the access protection concept.                                                                                                                                    |                   |
| •<br>Use simple visual security features when designing the card body. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                   |

<span id="page-78-0"></span>

| MM2 | Code and name of safeguard                                                                                                                                                                                                         | Threats addressed |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|     | Protection against cloning of carrier medium<br>with entitlement                                                                                                                                                                   | TM3               |
|     | •<br>Introduce authentication based on a non-retrievable, secret key to protect<br>against copying.                                                                                                                                |                   |
|     | •<br>Introduce a zero-balance procedure when managing non-personalised,<br>printed carrier media.                                                                                                                                  |                   |
|     | Advanced protection against cloning of carrier medium:                                                                                                                                                                             |                   |
| 3   | •<br>Implementation of access protection in accordance with MM1.3 to prevent<br>the data content from being retrieved.                                                                                                             |                   |
|     | •<br>Use an UID – a globally unique, unchangeable identifier for the chip, which<br>prevents the carrier medium, applications and entitlement from being dupli<br>cated; the UID is integrated into the access protection concept. |                   |
|     | •<br>Use advanced simple visual security features when designing the card<br>body.                                                                                                                                                 |                   |
|     | •<br>Introduce a zero-balance procedure when managing non-personalised,<br>printed carrier media.                                                                                                                                  |                   |

| Table 8–38 | Protection of the transponder against cloning |
|------------|-----------------------------------------------|
|            |                                               |

| MM3     | Code and name of safeguard                                                                                                                                                                                                                                                            | Threats addressed |  |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|         | Protection against emulation                                                                                                                                                                                                                                                          | TM4               |  |
| General | The functions of the carrier medium and entitlement can theoretically be emu<br>lated by programmable devices (e.g. PDAs) that use contact-less interfaces.                                                                                                                           |                   |  |
|         | Emulation requires that the complete data content and the full function of the<br>carrier medium, including UID, can be retrieved.                                                                                                                                                    |                   |  |
|         | Emulating simple memory chips by using commercially available programmable<br>contact-less chips with card operating system (COS) is not possible since the<br>UID of the controller chips cannot be programmed. An emulation by using spe<br>cially developed hardware is thinkable. |                   |  |
|         | Simple emulation protection:                                                                                                                                                                                                                                                          |                   |  |
|         | •<br>Password protection to prevent data from being retrieved, or,                                                                                                                                                                                                                    |                   |  |
| 1       | •<br>Introduce authentication based on a non-retrievable, secret key to prevent<br>emulation -> authentication of the emulated medium fails because the se<br>cret key is missing.                                                                                                    |                   |  |
|         | •<br>Prevent applications and entitlements from being transferred onto a pro<br>grammable chip card by integrating the UID into the access protection con<br>cept.                                                                                                                    |                   |  |
|         | •<br>Operative safeguards for checking the carrier medium: e.g. inspection by<br>staff, use of carrier medium within view of the driver. Does not work if, for<br>example, NFC mobile devices are allowed as a legal carrier medium.                                                  |                   |  |
|         | Emulation protection:                                                                                                                                                                                                                                                                 |                   |  |
| 2       | •<br>Implementation of access protection in accordance with MM1.2 to prevent<br>the data content from being retrieved.                                                                                                                                                                |                   |  |
|         | •<br>Utilise secret, non-retrievable keys for authentication.                                                                                                                                                                                                                         |                   |  |

<span id="page-79-0"></span>

| MM3 | Code and name of safeguard                                                                                                                                                                                                                 | Threats addressed |  |  |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|--|
|     | Protection against emulation                                                                                                                                                                                                               | TM4               |  |  |
|     | •<br>Prevent applications and entitlements from being transferred onto a pro<br>grammable chip card by integrating the UID into the access protection con<br>cept.                                                                         |                   |  |  |
|     | •<br>Monitor the carrier media in system operation.                                                                                                                                                                                        |                   |  |  |
|     | •<br>Apply operative safeguards for checking the carrier medium: e.g. inspection<br>by staff, use of carrier medium within view of the driver. Does not work if, for<br>example, NFC mobile devices are allowed as a legal carrier medium. |                   |  |  |
|     | Advanced emulation protection:                                                                                                                                                                                                             |                   |  |  |
| 3   | •<br>Implementation of access protection in accordance with MM1.3 to prevent<br>the data content from being retrieved.                                                                                                                     |                   |  |  |
|     | •<br>Utilise secret, non-retrievable keys for authentication.                                                                                                                                                                              |                   |  |  |
|     | •<br>Prevent applications and entitlements from being transferred onto a pro<br>grammable chip card by integrating the UID into the access protection con<br>cept.                                                                         |                   |  |  |
|     | •<br>Monitoring the carrier media in system operation.                                                                                                                                                                                     |                   |  |  |
|     | •<br>Operative safeguards for checking the carrier medium: e.g. inspection by<br>staff, use of carrier medium within view of the driver. Does not work if, for<br>example, NFC mobile devices are allowed as a legal carrier medium.       |                   |  |  |

#### **Table 8–39 Protection of the transponder against emulation**

| MM4     | Code and name of safeguard                                                                                                                                                                                                                                                                                                                   | Threats addressed |  |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|         | Protection of personal data against retrieval<br>and overwriting/manipulation                                                                                                                                                                                                                                                                | TM5, TM6          |  |
|         | Personal data is:                                                                                                                                                                                                                                                                                                                            |                   |  |
| General | •<br>Information about a person,                                                                                                                                                                                                                                                                                                             |                   |  |
|         | •<br>Calculation data, or                                                                                                                                                                                                                                                                                                                    |                   |  |
|         | •<br>Other personal usage data that is generated using the entitlement and<br>sometimes stored in the application on the carrier medium.                                                                                                                                                                                                     |                   |  |
|         | Protection of personal data:                                                                                                                                                                                                                                                                                                                 |                   |  |
| 1       | •<br>Write protection or access protection in accordance with MM1.1.                                                                                                                                                                                                                                                                         |                   |  |
|         | •<br>If the chip is to have write protection only, then, as it stands today, the<br>mechanism that is employed to protect personal information must be TDES,<br>AES128 or an open method of similar strength. The type and strength of the<br>mechanism must be adjusted in line with future developments in accor<br>dance with [ALGK_BSI]. |                   |  |
|         | •<br>Data is transmitted in encrypted form in accordance with MM2.1, and stored<br>in the chip. Personal data and entitlements are protected using various<br>keys.                                                                                                                                                                          |                   |  |
|         | •<br>Diversification of keys.                                                                                                                                                                                                                                                                                                                |                   |  |
| 2       | Specific access protection for personal data:                                                                                                                                                                                                                                                                                                |                   |  |
|         | •<br>Access protection in accordance with MM1.2.                                                                                                                                                                                                                                                                                             |                   |  |

<span id="page-80-0"></span>

| MM4 | Code and name of safeguard                                                                                                                                                                         | Threats addressed |  |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|     | Protection of personal data against retrieval<br>and overwriting/manipulation                                                                                                                      | TM5, TM6          |  |
|     | •<br>Data is transmitted in secured form in accordance with MS2.2, and stored in<br>the chip specifically for the application. Personal data and entitlements are<br>protected using various keys. |                   |  |
|     | •<br>The data may need to be protected against manipulation on the system side<br>(e.g. using MAC).                                                                                                |                   |  |
|     | •<br>Diversification of keys.                                                                                                                                                                      |                   |  |
|     | Advanced access protection for personal data, interoperability:                                                                                                                                    |                   |  |
|     | •<br>Access protection in accordance with MM1.3.                                                                                                                                                   |                   |  |
| 3   | •<br>Data is transmitted in secured form in accordance with MS2.3, and stored in<br>the chip specifically for the application. Personal data and entitlements are<br>protected using various keys. |                   |  |
|     | •<br>The data may need to be protected against manipulation on the system side<br>(e.g. using MAC, signatures). This applies in particular to calculation data if<br>interoperability is required. |                   |  |
|     | •<br>Diversification of keys.                                                                                                                                                                      |                   |  |

| Table 8–40 | Protection of personal data on the transponder |
|------------|------------------------------------------------|
|            |                                                |

| MM5     | Code and name of safeguard                                                                                                                                                                                                                    | Threats addressed |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|         | Protection of settlement data against retrieval<br>and overwriting/manipulation                                                                                                                                                               | TM7, TM8          |
| General | Settlement data is generated using personal usage data, and is used to invoice<br>the services of the service provider. In the case of products with automatic fare<br>calculation, the settlement data is also used to invoice the customer. |                   |
|         | In the case of simpler products, the validation information about the entitlement<br>stored in the carrier medium can also be treated as the invoicing date.                                                                                  |                   |
|         | Settlement data is stored in the carrier medium and the terminal when beginning<br>a journey or when checking in or out.                                                                                                                      |                   |
|         | If interoperability is required, then settlement data must also be protected<br>against internal attacks.                                                                                                                                     |                   |
|         | Protection of settlement data:                                                                                                                                                                                                                |                   |
| 1       | •<br>Write protection or access protection in accordance with MM1.1.                                                                                                                                                                          |                   |
|         | •<br>Data is transmitted in encrypted form in accordance with MS2.1, and stored<br>in the chip. Settlement data and entitlements are protected using various<br>keys.                                                                         |                   |
|         | •<br>Diversification of keys.                                                                                                                                                                                                                 |                   |
| 2       | Specific access and manipulation protection:                                                                                                                                                                                                  |                   |
|         | •<br>Access protection in accordance with MM1.2.                                                                                                                                                                                              |                   |
|         | •<br>Data is transmitted in secured form in accordance with MS2.2, and stored in<br>the chip specifically for the application. Settlement data and entitlements<br>are protected using various keys.                                          |                   |

<span id="page-81-0"></span>

| MM5 | Code and name of safeguard                                                                                                                                                                                                                                                              | Threats addressed |  |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|     | Protection of settlement data against retrieval<br>and overwriting/manipulation                                                                                                                                                                                                         | TM7, TM8          |  |
|     | •<br>The data may need to be protected against manipulation on the system side<br>(e.g. using MAC).                                                                                                                                                                                     |                   |  |
|     | •<br>Diversification of keys.                                                                                                                                                                                                                                                           |                   |  |
|     | Access and manipulation protection in the case of interoperability:                                                                                                                                                                                                                     |                   |  |
|     | •<br>Access protection in accordance with MM1.3.                                                                                                                                                                                                                                        |                   |  |
| 3   | •<br>Data is transmitted in secured form in accordance with MS2.3, and stored in<br>the chip specifically for the application. The various types of settlement data<br>are protected in accordance with a defined role model using defined access<br>rights and specific, varying keys. |                   |  |
|     | •<br>If interoperability is required in the system, then settlement data must be<br>protected against manipulation on the system side (e.g. using MAC, signa<br>tures).                                                                                                                 |                   |  |
|     | •<br>Diversification of keys.                                                                                                                                                                                                                                                           |                   |  |

| Table 8–41 | Protection of settlement data on the transponder |  |
|------------|--------------------------------------------------|--|
|            |                                                  |  |

| MM6 | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                             | Threats addressed |  |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|     | Separation of applications<br>TM6, TM9                                                                                                                                                                                                                                                                                                                                                 |                   |  |
| 1   | No particular separation of applications is supported.                                                                                                                                                                                                                                                                                                                                 |                   |  |
| 2   | Separation of applications:<br>•<br>Applications are loaded in a secure environment.<br>•<br>Implementation of an application-specific access concept in accordance<br>with MM1.2. Keys and rights are allocated in accordance with the role<br>model of entities in the system as a whole.<br>•<br>Diversification of keys.                                                           |                   |  |
| 3   | Secure separation of applications:<br>•<br>Implementation of an application-specific access concept in accordance<br>with MM1.3. Keys and rights are allocated in accordance with the role<br>model of entities in the system as a whole.<br>•<br>Safeguard MM10a.3 (and possibly MM10b.3) is employed for the secure<br>loading of new applications.<br>•<br>Diversification of keys. |                   |  |

| Table 8–42 | Protection through separation of applications on the transponder |
|------------|------------------------------------------------------------------|
|            |                                                                  |

| MM7     | Code and name of safeguard                                                                                                                                                                                             | Threats addressed |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|         | Specification of carrier medium characteristics                                                                                                                                                                        | TM10              |
| General | The characteristics of the carrier medium in relation to the applications and op<br>erating processes that are to be supported must be specified and guaranteed.<br>This applies in particular to:<br>•<br>Performance |                   |

<span id="page-82-0"></span>

| MM7 | Code and name of safeguard                                               | Threats addressed |  |
|-----|--------------------------------------------------------------------------|-------------------|--|
|     | Specification of carrier medium characteristics                          | TM10              |  |
|     | •<br>Durability under mechanical wear                                    |                   |  |
|     | •<br>Protection against DoS attacks                                      |                   |  |
|     | Manufacturer's declaration:                                              |                   |  |
| 1   | •<br>The manufacturer guarantees that the specifications are adhered to. |                   |  |
|     | Tests and declaration of conformity:                                     |                   |  |
| 2   | •<br>Testing regulations are drawn up, tests performed.                  |                   |  |
|     | •<br>Establish an approval procedure.                                    |                   |  |
|     | Interoperability tests according to test concept, evaluation:            |                   |  |
| 3   | •<br>Draw up testing regulations.                                        |                   |  |
|     | •<br>Establish an approval procedure.                                    |                   |  |
|     | •<br>Carrier medium evaluated by independent test laboratories.          |                   |  |
|     | •<br>Certification of components by an independent institution.          |                   |  |

| Table 8–43 | Protection through specification of carrier medium |
|------------|----------------------------------------------------|
|------------|----------------------------------------------------|

| MM8 | Code and name of safeguard                                                                                                       | Threats addressed |
|-----|----------------------------------------------------------------------------------------------------------------------------------|-------------------|
|     | Introduce proximity technology as defined by<br>ISO/IEC14443                                                                     | TM11              |
| 1   | Introduce proximity technology as defined by ISO/IEC14443.                                                                       |                   |
| 2   |                                                                                                                                  |                   |
|     | Increased protection:                                                                                                            |                   |
| 3   | •<br>Utilise random anti-collision code (random UID).<br>•<br>Deactivate the RF interface in the presence of NFC mobile devices. |                   |

**Table 8–44 Protection through introduction of proximity technology as defined by ISO/IEC14443** 

| MM9     | Code and name of safeguard                                                                                                                                                       | Threats addressed |  |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|         | Fallback solution for carrier medium malfunc<br>tion                                                                                                                             | TM12              |  |
| General | In the event of a malfunction, electronic safeguards in the carrier medium cannot<br>take effect in an emergency, since the chip data can no longer necessarily be<br>retrieved. |                   |  |
|         | To ensure that the security targets are not endangered, it must first be deter<br>mined whether the customer is in possession of a valid entitlement.                            |                   |  |
| 1       | Introduction of appropriate fallback solutions:                                                                                                                                  |                   |  |
| 2       | •<br>Introduce visual security features for checking the genuineness of the me<br>dium if chip is defective.                                                                     |                   |  |
|         | •<br>In the case of personalised carrier media: visual personalisation.                                                                                                          |                   |  |

<span id="page-83-0"></span>

| MM9 | Code and name of safeguard                                                                                                                                                     | Threats addressed |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|     | Fallback solution for carrier medium malfunc<br>tion                                                                                                                           | TM12              |
|     | •<br>Provide an operative fallback process (e.g. regulations for using the service,<br>service desk for the customer).                                                         |                   |
|     | •<br>Fallback solutions must be specified in the contractual arrangements be<br>tween customers, service providers and suppliers, and their consequences<br>taken into account |                   |
|     | •<br>The capacity of the fallback solution must be sufficient to prevent a DoS<br>attack consisting of overloading the fallback solution.                                      |                   |
|     | •<br>Store the usage and calculation data in the system.                                                                                                                       |                   |
|     | •<br>Back up the applications and entitlements stored in the carrier medium (in<br>cluding the personal data) in the system.                                                   |                   |
|     | Implementation according to fallback concept, in addition to 1, 2:                                                                                                             |                   |
| 3   | •<br>A system concept must be developed that explicitly defines the fallback so<br>lutions and availability periods.                                                           |                   |
|     | •<br>If necessary, enough replacement carrier media must be provided to enable<br>the required availability to be upheld.                                                      |                   |

| Table 8–45 | Protection through fallback solution for carrier medium malfunction |  |
|------------|---------------------------------------------------------------------|--|
|            |                                                                     |  |

| MM10a | Code and name of safeguard                                                                                                                                                                                                                                                                   | Threats addressed |  |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|       | Loading new applications – securing the au<br>thenticity and integrity of applications                                                                                                                                                                                                       | TM9               |  |
|       | No reloading mechanism:                                                                                                                                                                                                                                                                      |                   |  |
| 1     | •<br>A mechanism for loading new applications is not offered. Applications are<br>only issued individually. There is no multi-application compatibility.                                                                                                                                     |                   |  |
| 2     | Implementation of a reloading mechanism as defined by ISO 7816-13 with Se<br>cure Messaging:                                                                                                                                                                                                 |                   |  |
|       |                                                                                                                                                                                                                                                                                              |                   |  |
|       | I. Preliminary remarks                                                                                                                                                                                                                                                                       |                   |  |
|       | When new applications are loaded, the following must also be loaded:                                                                                                                                                                                                                         |                   |  |
|       | •<br>data structures for the application data and customer data<br>•<br>application keys                                                                                                                                                                                                     |                   |  |
| 3     | The necessary separation of applications requires carrier media that are able to<br>support this separation (security boundaries). To do this the carrier medium<br>must contain an appropriate card management application that is able to proc<br>ess the commands defined in ISO 7816-13. |                   |  |
|       | An application can only be loaded if in the possession of the application pro<br>vider. It should be transferred securely, after checking for version, integrity and<br>authenticity.                                                                                                        |                   |  |
|       | II. Loading the new application                                                                                                                                                                                                                                                              |                   |  |

<span id="page-84-0"></span>

|       | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Threats addressed |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| MM10a | Loading new applications – securing the au<br>thenticity and integrity of applications                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | TM9               |
|       | The process of loading new applications uses command sequences defined in<br>the ISO 7816-13 standard. This standard defines the following commands:                                                                                                                                                                                                                                                                                                                                                                                                                 |                   |
|       | •<br>Application management request<br>•<br>Load application<br>•<br>Remove application                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                   |
|       | The Application management request and Load application commands are<br>therefore required in order to load a new application.                                                                                                                                                                                                                                                                                                                                                                                                                                       |                   |
|       | ISO 7816-13 commands must be executed using secure messaging. This en<br>sures that the new application is authentic when loaded, and can be operated<br>securely. The following section looks more closely at the application of this ISO<br>standard to this use case.                                                                                                                                                                                                                                                                                             |                   |
|       | Note:<br>New applications can also be loaded without SM. This will not influence the se<br>curity of the existing applications, but it will not secure the authenticity of the<br>new application.<br>Since the standard ISO7816-13 only provides a general framework in which<br>applications can be loaded onto suitable carrier media, the following specific<br>factors must be taken into account for this use case:                                                                                                                                            |                   |
|       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                   |
|       | •<br>Every application must be given an application ID in order to ensure separa<br>tion between the applications.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                   |
|       | •<br>Furthermore, all organisations must be given unique organisation IDs to<br>enable clear allocation of keys and application data.                                                                                                                                                                                                                                                                                                                                                                                                                                |                   |
|       | •<br>Applications are only issued by the application issuer, and not from any<br>other number of sources.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                   |
|       | •<br>The secure messaging key required for secure messaging must be stored<br>in the carrier medium (for all applications) the first time it is personalised so<br>that it is possible to execute the commands. The application provider (or<br>application issuer) must also be in possession of this key. Carrier media<br>that do not have this key cannot negotiate session keys with the application<br>provider, which means that data will not be able to be sent in response to<br>the Load application command.                                             |                   |
|       | III. Note on checking the applications for authenticity and integrity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                   |
|       | •<br>Using the secure messaging mechanism requires an online connection to<br>the application provider (or application issuer), or to the source that pos<br>sesses the SM key for downloading the application. A secure operating en<br>vironment is not required for this.                                                                                                                                                                                                                                                                                         |                   |
|       | •<br>As part of the key management system for the use case described in this<br>document, it must be ensured that the authentication process can take<br>place between the application provider (i.e. the source of the loaded appli<br>cation) and the carrier medium. One way of ensuring this is for the applica<br>tion issuer to give the application provider the SM key for loading new appli<br>cations (unless issuer and provider are one and the same); another is that a<br>trustworthy third source generates this key, and it is put into the security |                   |

| MM10a | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Threats addressed |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|       | Loading new applications – securing the au<br>thenticity and integrity of applications                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | TM9               |
|       | modules and carrier media beforehand.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                   |
|       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                   |
|       | IV. Sample command sequence:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                   |
|       | 1<br>Select <<card manager AID>>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                   |
|       | Select the card manager application using the AID                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                   |
|       | 2<br>Get Data <<management service template>>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                   |
|       | Retrieve the card management service template, which contains information<br>about which status of its life-cycle the application is in, and about which<br>other status it may enter.                                                                                                                                                                                                                                                                                                                                                                                                           |                   |
|       | 3<br>Select <<AID superordinate application>>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                   |
|       | 4<br>Authenticate                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                   |
|       | Mutual authentication can then take place, depending on the security level<br>(of the application).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                   |
|       | 5<br>Application Management Request                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                   |
|       | Possible passing of the AID of the application being managed, together with<br>the certificate and hash value of the application data, provided by the card<br>issuer. Other data such as application issuer ID, card issuer ID and so on<br>can also be sent to the card.                                                                                                                                                                                                                                                                                                                       |                   |
|       | 6<br>Load Application                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                   |
|       | Multi-part command which actually loads the application. The Load Applica<br>tion<br>command contains commands in its data field for setting up the appli<br>cation structure. Since the applications that are to be loaded may have dif<br>ferent definitions as well as different security and entitlement requirements<br>and so on, the command may contain a variety of data contents (or chip<br>card commands) depending on the application. The way this command is<br>executed is heavily dependent on the operating system being used, and on<br>the type of application being loaded. |                   |
|       | 7<br>Application Management Request                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                   |
|       | Sets the status to "operational activated" to enable the application to begin<br>operation, and for the associated specific security states to be set in the<br>carrier medium.                                                                                                                                                                                                                                                                                                                                                                                                                  |                   |
|       | The same procedure can be followed when removing applications on cards that<br>have already been issued. To this end the standard defines the command Re<br>move Application, which is embedded in the aforementioned sequences.                                                                                                                                                                                                                                                                                                                                                                 |                   |

| Table 8–46 | Protection through securing the authenticity and integrity when load |
|------------|----------------------------------------------------------------------|
|            | ing applications                                                     |

| MM10b                                                                                                                                                                                                                                                | Code and name of safeguard                                                  | Threats addressed |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|-------------------|
|                                                                                                                                                                                                                                                      | Loading new applications – securing the con<br>fidentiality of applications | TM9               |
|                                                                                                                                                                                                                                                      | No reloading mechanism:                                                     |                   |
| 1<br>•<br>A mechanism for loading new applications is not offered. Applications are<br>only issued individually. There is no multi-application compatibility. Since<br>the single application is loaded in a secure environment, the confidentiality |                                                                             |                   |

<span id="page-86-0"></span>

| MM10b | Code and name of safeguard                                                                                                                                                                                                                                                                                         | Threats addressed |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|       | Loading new applications – securing the con<br>fidentiality of applications                                                                                                                                                                                                                                        | TM9               |
|       | of the application data is automatically assured.                                                                                                                                                                                                                                                                  |                   |
| 2     | Implementation of a reloading mechanism as defined by ISO 7816-13 with SM                                                                                                                                                                                                                                          |                   |
|       | •<br>See MM10a. In secure messaging, not only is authenticity assured by<br>MACs, but confidentiality is guaranteed by encryption.                                                                                                                                                                                 |                   |
| 3     | Note:<br>When new applications are loaded, cryptographic secrets are generally transmit<br>ted along with public data. For this reason, safeguards MM10a and MM10b are<br>normally deployed together (secure messaging with negotiation of one session<br>key for authentication security and one for encryption). |                   |

| Table 8–47 | Protection through securing the confidentiality when loading applica |
|------------|----------------------------------------------------------------------|
|            | tions                                                                |

| MM11a   | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                          | Threats addressed |  |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|         | Loading new entitlements – securing the au<br>thenticity and integrity of entitlements                                                                                                                                                                                                                                                                                                              | TM2, TM9          |  |
|         | Notes on levels 2 and 3:                                                                                                                                                                                                                                                                                                                                                                            |                   |  |
| General | •<br>It is assumed that the application for which the new entitlements are to be<br>loaded already exists. If it does not yet exist, then "Loading new entitle<br>ments" can be deferred back to "Loading new applications".<br>•<br>It must be ensured that entitlements carry unique references when stored<br>on the carrier medium.                                                             |                   |  |
|         | •<br>If entitlement keys are to be loaded on the carrier medium, then the data<br>must be encrypted in every case (see MM11b).                                                                                                                                                                                                                                                                      |                   |  |
|         | No reloading mechanism:                                                                                                                                                                                                                                                                                                                                                                             |                   |  |
| 1       | •<br>A mechanism for loading new entitlements is not offered; entitlements are<br>only issued individually.                                                                                                                                                                                                                                                                                         |                   |  |
|         | Loading process secured by cryptographic method:                                                                                                                                                                                                                                                                                                                                                    |                   |  |
| 2       | •<br>The integrity of the transmission of entitlement data is guaranteed using<br>MAC protection with static MAC keys. The integrity of data transmission is<br>supported by MAC protection. The algorithm shall be selected in accor<br>dance with [ALGK_BSI]. The type and strength of the mechanism must be<br>adjusted in line with future developments in accordance with [ALGK_BSI].          |                   |  |
| 3       | Complex symmetric authentication concept with session key negotiation:                                                                                                                                                                                                                                                                                                                              |                   |  |
|         | •<br>The integrity of data transmission is guaranteed using MAC protection with<br>a symmetric MAC key negotiated between the loading terminal and the car<br>rier medium in a highly standardised authentication procedure. Communica<br>tion between terminal and carrier medium can, for instance, use secure<br>messaging-secured standard commands such as Update Record and<br>Update Binary. |                   |  |
|         | •<br>Possible symmetric algorithms: standardised symmetric authentication us<br>ing session key negotiation according to [ALGK_BSI]. MAC algorithms have                                                                                                                                                                                                                                            |                   |  |

<span id="page-87-0"></span>

| MM11a | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                                                       | Threats addressed |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|       | Loading new entitlements – securing the au<br>thenticity and integrity of entitlements                                                                                                                                                                                                                                                                                                                                           | TM2, TM9          |
|       | to be selected according to [ALGK_BSI] as well.                                                                                                                                                                                                                                                                                                                                                                                  |                   |
|       | •<br>The type and strength of the mechanism used for loading should be<br>adapted to future developments in accordance with [ALGK_BSI].                                                                                                                                                                                                                                                                                          |                   |
|       | Complex asymmetric authentication concept in session key negotiation, intro<br>duction of Public Key Infrastructure (PKI):                                                                                                                                                                                                                                                                                                       |                   |
| 3+    | •<br>Every entity in the public transport system is given its own asymmetric au<br>thentication key which has been certified by a certification authority (CA).<br>The system as a whole is subject to a common Root CA.                                                                                                                                                                                                         |                   |
|       | •<br>Prior to authentication, the carrier medium and the security module (SAM) in<br>the system of the application provider must exchange the certificates of<br>their public authentication keys, verify them (e.g. using Verify Certifi<br>cate), and import the public key of the other entity involved. Authentication<br>is then done using a standardised asymmetric authentication procedure.                             |                   |
|       | •<br>As in level 3, entitlement data is MAC-secured using session keys negoti<br>ated between the parties.                                                                                                                                                                                                                                                                                                                       |                   |
|       | •<br>Selection of algorithms: authentication using RSA or ECC (Key length ac<br>cording to [ALGK_BSI]) for authentication and CA keys; MAC protection ac<br>cording to [ALGK_BSI].                                                                                                                                                                                                                                               |                   |
|       | •<br>In level 3+, the type and strength of the mechanism used for loading should<br>also be adapted to future developments in accordance with [ALGK_BSI].                                                                                                                                                                                                                                                                        |                   |
|       | Example VDV Core Application:                                                                                                                                                                                                                                                                                                                                                                                                    |                   |
|       | •<br>The VDV Core Application is based on a complex PKI in which every entity<br>(which can mean every VDV SAM and every user medium) has its own cer<br>tificate for its authentication key signed by a CA.                                                                                                                                                                                                                     |                   |
|       | •<br>When an entitlement is issued, a single- or multi-stage certificate verification<br>process is performed, followed by asymmetric authentication between the<br>VDV user medium and the VDV SAM, in which shared session keys are<br>negotiated for MAC protection and encryption.                                                                                                                                           |                   |
|       | •<br>An entitlement then consists of unique entitlement data and symmetric enti<br>tlement keys. These are stored securely (by secure messaging) on the car<br>rier medium after authentication using the standard command Put Data.<br>The VDV SAM is capable of generating the command messages required<br>for the user media. See also the specifications of the customer medium in<br>the VDV Core Application in [VDV_KM]. |                   |

| Table 8–48 | Protection through securing the authenticity and integrity when load |
|------------|----------------------------------------------------------------------|
|            | ing entitlements                                                     |

| MM11b   | Code and name of safeguard                                                                                                                           | Threats addressed |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|         | Loading new entitlements – securing the con<br>fidentiality of entitlements                                                                          | TM2, TM9          |
| General | Notes on levels 2 and 3:                                                                                                                             |                   |
|         | •<br>When new entitlements are loaded, cryptographic secrets are often trans<br>mitted along with public data. For this reason, safeguards MM11a and |                   |

<span id="page-88-0"></span>

| MM11b | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                             | Threats addressed |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|       | Loading new entitlements – securing the con<br>fidentiality of entitlements                                                                                                                                                                                                                                                                                            | TM2, TM9          |
|       | MM11b are normally deployed together.                                                                                                                                                                                                                                                                                                                                  |                   |
| 1     | No reloading mechanism:                                                                                                                                                                                                                                                                                                                                                |                   |
|       | •<br>A mechanism for loading new entitlements is not offered. Entitlements are<br>only issued individually. Since the entitlement is already stored on the car<br>rier medium, its confidentiality is automatically assured.                                                                                                                                           |                   |
| 2     | Loading process secured by proprietary cryptographic method:<br>•<br>See MM11a; in communication between the carrier medium and the external<br>component, not only is authenticity assured by MACs, but confidentiality is<br>also guaranteed by encryption.<br>•<br>Possible symmetric algorithms: encryption using TDES, AES128 or a com<br>parable open mechanism. |                   |
|       | Complex symmetric authentication concept with session key negotiation:                                                                                                                                                                                                                                                                                                 |                   |
| 3     | •<br>See MM11a; as part of authentication between carrier medium and external<br>component, an encrypting key is negotiated as well as the MAC key, thus<br>setting up a secure channel.                                                                                                                                                                               |                   |
|       | •<br>Possible symmetric algorithms: standardised symmetric authentication with<br>session key negotiation by using TDES, AES128 or a comparable open<br>mechanism; encryption by using TDES, AES128 or a comparable standard<br>ised method.                                                                                                                           |                   |
|       | •<br>The type and strength of the mechanism used for loading should be<br>adapted to future developments in accordance with [ALGK_BSI].                                                                                                                                                                                                                                |                   |

| Table 8–49 | Protection through securing the confidentiality when loading entitle |
|------------|----------------------------------------------------------------------|
|            | ments                                                                |

### **8.4.4 Safeguards relating to the readers**

| MR1 | Code and name of safeguard                                                                                           | Threats addressed |
|-----|----------------------------------------------------------------------------------------------------------------------|-------------------|
|     | Introduction of interface tests and approval<br>procedures                                                           | TC1               |
| 1   | Interface test:                                                                                                      |                   |
|     | •<br>Testing of the PCD's contact-less interface according to<br>[BSI_PCD_TestSpec].                                 |                   |
|     | •<br>Draw up and apply specific test regulations for the application-specific func<br>tions of the reader interface. |                   |
| 2   | Component approval:                                                                                                  |                   |
|     | •<br>See above, and also component approval (carrier medium, readers, key<br>management).                            |                   |

<span id="page-89-0"></span>

| MR1 | Code and name of safeguard                                                                              | Threats addressed |
|-----|---------------------------------------------------------------------------------------------------------|-------------------|
|     | Introduction of interface tests and approval<br>procedures                                              | TC1               |
| 3   | Certification:                                                                                          |                   |
|     | •<br>See above, and also certification of carrier medium and readers by an inde<br>pendent institution. |                   |

| Table 8–50 | Protection of readers through introduction of interface tests |
|------------|---------------------------------------------------------------|
|------------|---------------------------------------------------------------|

| MR2     | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Threats addressed |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|         | Protection of reference information against<br>retrieval, data errors and manipulation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | TR1, TR2          |
| General | Reference information is needed for processes such as communication with the<br>carrier media, for loading and evaluating entitlements, and for generating and<br>storing usage data (CICO data, sales data):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                   |
|         | •<br>Identifiers (ID)<br>•<br>Keys<br>•<br>Blacklists and whitelists<br>•<br>Algorithms for evaluation<br>Reference information and usage data can differ depending on the applications<br>and entitlements.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                   |
| 1       | Checksum and physical protection:<br>•<br>Appropriate physical access protection for the devices (e.g. encapsulated<br>casing, mechanical separation of LAN cables).<br>•<br>Use checksums for data transfer to avoid transmission errors – does not<br>protect against manipulation, since checksums can be calculated automati<br>cally by almost any software and do not rely on secrets.<br>•<br>Save cryptographic keys and algorithms in a SAM or in a protected area of<br>the software.<br>•<br>Introduce access protection for the reader's data and administration func<br>tions.                                                                                                                                                                                             |                   |
| 2       | Authentication, secure transmission:<br>•<br>Mechanisms for detecting data manipulation in the device, such as MAC<br>secured saving (provided this is possible from a performance point of view).<br>•<br>Data should only be transferred from background systems into the reader<br>after mutual authentication, or at least one-sided authentication of the<br>source transmitting to the reader.<br>•<br>Protected data transmission to the carrier medium, where data is to be ac<br>cepted.<br>•<br>Application-specific separation of algorithms, reference data, usage data<br>and keys.<br>•<br>Save the keys in a SAM or in a protected area of the software.<br>•<br>Introduce application-specific access protection for the reader's data and<br>administration functions. |                   |

<span id="page-90-0"></span>

| MR2 | Code and name of safeguard                                                                                                                                                       | Threats addressed |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|     | Protection of reference information against<br>retrieval, data errors and manipulation                                                                                           | TR1, TR2          |
|     | Advanced protection:                                                                                                                                                             |                   |
| 3   | •<br>Mechanisms for detecting data manipulation in the device, such as MAC<br>secured saving (provided this is possible from a performance point of view).                       |                   |
|     | •<br>Data should only be transferred from background systems into the reader<br>after mutual authentication between the reader and the source with which it<br>is communicating. |                   |
|     | •<br>Protected data transmission to the carrier medium.                                                                                                                          |                   |
|     | •<br>Application-specific separation of algorithms, reference data, usage data<br>and keys.                                                                                      |                   |
|     | •<br>Save the keys in a SAM or in a protected area of the application software                                                                                                   |                   |
|     | •<br>Introduce multi-tenant, application-specific access protection for the<br>reader's data and administrative functions in accordance with the role<br>model.                  |                   |

| Table 8–51 | Protection of readers through protection of reference information |
|------------|-------------------------------------------------------------------|

| MR3     | Code and name of safeguard                                                                                                                                                                                   | Threats addressed |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|         | Protection of the reader against malfunction                                                                                                                                                                 | TR3               |
|         | The general safeguards are:                                                                                                                                                                                  |                   |
| General | •<br>Draw up specifications describing the characteristics of the reader in terms<br>of performance, availability, procedural management and function.                                                       |                   |
|         | •<br>Draw up test specifications.                                                                                                                                                                            |                   |
|         | •<br>Offline capability wherever a data network connection is not guaranteed.                                                                                                                                |                   |
|         | •<br>Reference data and usage data must be able to be stored securely.<br>Capacity must be designed to suit the scenario in which it will be used.                                                           |                   |
|         | •<br>Introduce uninterruptible power supply (UPS) wherever an external power<br>supply is not guaranteed.                                                                                                    |                   |
|         | •<br>The UPS must at least be capable of bridging a specific period of time.                                                                                                                                 |                   |
|         | Execution to specifications:                                                                                                                                                                                 |                   |
| 1       | •<br>Design the system characteristics to accord with the specifications defining<br>performance, availability, procedural management and function (this re<br>quires sufficiently detailed specifications). |                   |
|         | •<br>Simple integrity security for system software to detect manipulation of soft<br>ware modules (e.g. of entitlement test).                                                                                |                   |
|         | •<br>Physical protection of devices (e.g. encapsulated casing, mechanical sepa<br>ration of LAN cables).                                                                                                     |                   |
|         | •<br>Simple access protection in the form of passwords and IDs in readers for<br>sensitive tasks such as loading new software versions.                                                                      |                   |
|         | •<br>Specification and implementation of a process for supporting new entitle<br>ments and carrier media.                                                                                                    |                   |
| 2       | Proof of execution:                                                                                                                                                                                          |                   |

<span id="page-91-0"></span>

| MR3 | Code and name of safeguard                                                                                                                                                                                           | Threats addressed |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|     | Protection of the reader against malfunction                                                                                                                                                                         | TR3               |
|     | •<br>Integrity security for system software to detect manipulation of software<br>modules (e.g. of entitlement test)                                                                                                 |                   |
|     | •<br>Physical protection of devices (e.g. encapsulated casing, mechanical sepa<br>ration of LAN cables).                                                                                                             |                   |
|     | •<br>Access protection in the form of passwords and IDs in readers for sensitive<br>tasks such as loading new software versions.                                                                                     |                   |
|     | •<br>Specification and implementation a process for supporting new carrier me<br>dia, applications and entitlements.                                                                                                 |                   |
|     | •<br>Document the correct implementation of the specifications defining per<br>formance, availability, procedural management and function, using tests<br>that provoke specific malfunctions and operational errors. |                   |
|     | Evaluation:                                                                                                                                                                                                          |                   |
|     | •<br>Agree on service levels and ensure support in the event of failure so as to<br>limit the effects of malfunctions.                                                                                               |                   |
|     | •<br>Integrity security for system software to detect manipulation of software<br>modules (e.g. of entitlement test); signatures or MAC with appropriate<br>mechanism strength and key length.                       |                   |
| 3   | •<br>Physical protection of devices (e.g. encapsulated casing, mechanical sepa<br>ration of LAN cables).                                                                                                             |                   |
|     | •<br>Access to the terminal's administration functions, such as software updates,<br>only after authentication of the source of the request.                                                                         |                   |
|     | •<br>Specification and implementation a process for supporting new carrier me<br>dia, applications and entitlements.                                                                                                 |                   |
|     | •<br>Have independent test laboratories evaluate and certify system software<br>and hardware according to defined criteria.                                                                                          |                   |

**Table 8–52 Protection of the reader against malfunction** 

Other safeguards relating to the readers are described in Section [8.4.2.](#page-67-1)

### **8.4.5 Safeguards relating to the key management system**

| MK1     | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                          | Threats addressed |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|         | Secure generation and import of keys                                                                                                                                                                                                                                                                                                                                | TK1               |
| General | Specification of the necessary keys and key attributes in relation to carrier me<br>dia, applications and entitlements, taking into account the applicable role model.                                                                                                                                                                                              |                   |
| 1       | Keys generated according to specification:<br>•<br>Use a suitable key generator as defined in [GSHB].<br>•<br>All keys are to be generated in a secure environment, stored under crypto<br>graphic protection, and –apart from defined exceptions involving special<br>additional protective measures – loaded onto the carrier medium in a se<br>cure environment. |                   |

<span id="page-92-0"></span>

| MK1 | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Threats addressed |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|     | Secure generation and import of keys                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | TK1               |
|     | •<br>Specific keys are to be generated with defined attributes in accordance with<br>the specifications.<br>•<br>Support the diversification of keys for the application with carrier media, and<br>the information stored there (specification, implementation, testing and pro<br>vision of specific algorithms).<br>•<br>Import the keys to specific SAMs:<br>•<br>SAMs are based on secure chip hardware as defined by CC EAL5+<br>•<br>Data cannot be retrieved from SAMs<br>•<br>Authentication is required to activate a SAM                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                   |
| 2   | Evaluation by a testing laboratory:<br>•<br>Use a suitable key generator as defined in [GSHB].<br>•<br>All keys are to be generated in a secure environment, stored under crypto<br>graphic protection, and –apart from defined exceptions involving special<br>additional protective measures – loaded onto the carrier medium in a se<br>cure environment.<br>•<br>Specific keys are to be generated with defined attributes in accordance with<br>the specifications.<br>•<br>Support the diversification of keys for the application with carrier media, and<br>the information stored there (specification, implementation, testing and pro<br>vision of specific algorithms).<br>•<br>Import the keys to specific SAMs:<br>•<br>SAMs are based on secure chip hardware as defined by CC EAL5+<br>•<br>Data cannot be retrieved from SAMs<br>•<br>Authentication is required to activate a SAM<br>The quality of the key generator should be confirmed by an independent testing<br>laboratory.               |                   |
| 3   | Evaluate and certify using CC or a process of the same standard:<br>•<br>Use a suitable key generator as defined in [GSHB].<br>•<br>All keys are to be generated in a secure environment, stored under crypto<br>graphic protection, and –apart from defined exceptions involving special<br>additional protective measures – loaded onto the carrier medium in a se<br>cure environment.<br>•<br>Specific keys are to be generated with defined attributes in accordance with<br>the specifications.<br>•<br>Support the diversification of keys for the application with carrier media, and<br>the information stored there (specification, implementation, testing and pro<br>vision of specific algorithms).<br>•<br>Import the keys to specific SAMs:<br>•<br>SAMs are based on secure chip hardware as defined by CC EAL5+<br>•<br>Data cannot be retrieved from SAMs<br>•<br>Authentication is required to activate a SAM<br>All of the requirements must be evaluated and certified in accordance with CC, |                   |

| MK1 | Code and name of safeguard                               | Threats addressed |
|-----|----------------------------------------------------------|-------------------|
|     | Secure generation and import of keys                     | TK1               |
|     | EAL4 mechanism strength high, or a comparable procedure. |                   |

**Table 8–53 Protection through secure generation and import of keys** 

| MK2     | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Threats addressed |  |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|         | Introduction of key management for symmetric<br>and asymmetric keys with sufficient key length                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | All TK            |  |
|         | A key management system is defined by the following parameters:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                   |  |
|         | •<br>Key length                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                   |  |
|         | •<br>Algorithm used                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                   |  |
| General | •<br>Key storage (see also MK7)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                   |  |
|         | •<br>Generation of keys (see MK1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                   |  |
|         | •<br>Key distribution                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                   |  |
|         | •<br>Identification of keys                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                   |  |
|         | •<br>Technical and organisational intermeshing of safeguards                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                   |  |
|         | Key management concept and implementation:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                   |  |
|         | •<br>Keys are given unique IDs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                   |  |
|         | •<br>The purpose of the key and the entity to which it belongs is uniquely identi<br>fied (e.g. product provider ID, application ID, service provider ID).                                                                                                                                                                                                                                                                                                                                                                                                                            |                   |  |
|         | •<br>Key algorithms have to be selected according to [ALGK_BSI] (with priority)<br>and [TR_ECARD].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                   |  |
|         | •<br>Static keys can only be used in bordered-off, clearly manageable areas<br>where it is easy for the main components to exchange keys, and where the<br>number of carrier media is no longer usable after the exchange is low. If a<br>static method is used, then a secure key reloading process must be defined<br>at the same time which enables keys on the carrier medium to be replaced.<br>We therefore recommend the use of derived keys and unique identification<br>numbers (e.g. chip card ID, UID and a master key). This generates unique<br>keys for each component. |                   |  |
| 1       | •<br>The key length used is chosen and specified separately for each function in<br>compliance with [ALGK_BSI].                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                   |  |
|         | •<br>Keys in readers should always be stored in encapsulated security modules<br>(SAMs). This applies especially to terminals, inspection units and vending<br>machines that can work offline. Keys in background systems should also<br>preferably be stored in security modules such as e.g. SAMs.                                                                                                                                                                                                                                                                                  |                   |  |
|         | •<br>Keys can be distributed in two ways:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                   |  |
|         | a<br>personalisation of keys in carrier media and components in a secure<br>environment, and                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                   |  |
|         | b<br>loading new keys (see MK8 – reloading process)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                   |  |
|         | •<br>The key management system is designed by the system manager. The enti<br>ties involved apply a key management concept. This includes nominating<br>people responsible for key management who ensure that it is performed<br>correctly, and who keep abreast of the latest cryptographic developments<br>so as to be able to counteract threats to the system as a whole in good                                                                                                                                                                                                  |                   |  |

<span id="page-94-0"></span>

| MK2                                                                                                                                                                                                                                                                            | Code and name of safeguard                                                                                                                                                                                                                                   | Threats addressed |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|                                                                                                                                                                                                                                                                                | Introduction of key management for symmetric<br>and asymmetric keys with sufficient key length                                                                                                                                                               | All TK            |
|                                                                                                                                                                                                                                                                                | time.                                                                                                                                                                                                                                                        |                   |
|                                                                                                                                                                                                                                                                                | Key management concept and implementation (higher-level method)                                                                                                                                                                                              |                   |
|                                                                                                                                                                                                                                                                                | In addition to the points defined in 1, the following is usually done in level 2:                                                                                                                                                                            |                   |
| 2<br>•<br>As well as generating unique keys for each component, communication<br>session keys can also be negotiated that are made dynamic on the basis of<br>adjustable data (e.g. random numbers). This effectively prevents messages<br>from being eavesdropped or re-sent. |                                                                                                                                                                                                                                                              |                   |
| Secure, flexible key management concept:                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                              |                   |
| 3                                                                                                                                                                                                                                                                              | In level 3 the following may be useful in addition to the points defined in 1 and 2:                                                                                                                                                                         |                   |
|                                                                                                                                                                                                                                                                                | •<br>A complex asymmetric key management process with a root CA, multiple<br>sub-CAs and certified authentications and encrypting keys.<br>•<br>The lengths of asymmetric keys has to be selected according to<br>[ALGK_BSI] (with priority) and [TR_ECARD]. |                   |
|                                                                                                                                                                                                                                                                                | The length of all keys should be adapted to future developments in accordance<br>with [ALGK_BSI].                                                                                                                                                            |                   |

**Table 8–54 Protection through introduction of key management** 

| MK3     | Code and name of safeguard                                                                                                                              | Threats addressed |  |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|         | Access protection for cryptographic keys (read<br>and write access)                                                                                     | TK2, TK3          |  |
| General | Specification of the requirements regarding access protection for all the places<br>where keys are used, taking into account the applicable role model. |                   |  |
|         | Manufacturer's declaration:                                                                                                                             |                   |  |
| 1       | •<br>Keys and passwords on the carrier media are protected against retrieval<br>and manipulation attacks.                                               |                   |  |
|         | •<br>Once stored in a SAM or other secure memory for keys in system compo<br>nents, a key becomes irrevocably irretrievable using software.             |                   |  |
|         | •<br>New keys are loaded in accordance with MK8.                                                                                                        |                   |  |
|         | The access protection is certified by manufacturer's declarations.                                                                                      |                   |  |
|         | Evaluation by testing laboratory:                                                                                                                       |                   |  |
|         | •<br>Keys and passwords on the carrier media are protected against retrieval<br>and manipulation attacks.                                               |                   |  |
| 2       | •<br>Once stored in a SAM or other secure memory for keys in system compo<br>nents, a key becomes irrevocably irretrievable using software.             |                   |  |
|         | •<br>New keys are loaded in accordance with MK8.                                                                                                        |                   |  |
|         | The access protection is certified by test reports from independent testing labo<br>ratories.                                                           |                   |  |

<span id="page-95-0"></span>

| MK3 | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                                      | Threats addressed |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|     | Access protection for cryptographic keys (read<br>and write access)                                                                                                                                                                                                                                                                                                                                             | TK2, TK3          |
|     | Evaluation and certification in accordance with CC or a procedure of the same<br>standard:<br>•<br>Keys and passwords on the carrier media are protected against retrieval<br>and manipulation attacks.<br>3<br>•<br>Once stored in a SAM or other secure memory for keys in system compo<br>nents, a key becomes irrevocably irretrievable using software.<br>•<br>New keys are loaded in accordance with MK8. |                   |
|     |                                                                                                                                                                                                                                                                                                                                                                                                                 |                   |
|     | The access protection is certified by test reports from independent testing labo<br>ratories. Carrier media and SAMs are certified in accordance with CC EAL5+.                                                                                                                                                                                                                                                 |                   |

| Table 8–55 |  | Protection through access protection for cryptographic keys |
|------------|--|-------------------------------------------------------------|
|            |  |                                                             |

| MK4     | Code and name of safeguard                                                                                                                                                                                                                                | Threats addressed |  |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
|         | Securing the function of security components                                                                                                                                                                                                              | TK4               |  |
| General | Components used for saving and processing keys – referred to in the following<br>as security components – must be checked to ensure they are trustworthy.<br>There are various safeguards available for this purpose, depending on the level<br>involved. |                   |  |
|         | Manufacturer's declarations:                                                                                                                                                                                                                              |                   |  |
| 1       | •<br>Apply manufacturer's internal quality assurance to guarantee the safety in<br>accordance with specifications.                                                                                                                                        |                   |  |
|         | Testing in accordance with test specifications:                                                                                                                                                                                                           |                   |  |
|         | •<br>Draw up test specifications for each security component.                                                                                                                                                                                             |                   |  |
| 2       | •<br>Technical checking of components in accordance with the relevant test<br>regulations.                                                                                                                                                                |                   |  |
|         | •<br>Specification and execution of integration tests in test environments and<br>practical environments.                                                                                                                                                 |                   |  |
|         | Evaluation:                                                                                                                                                                                                                                               |                   |  |
| 3       | See 2, and also:                                                                                                                                                                                                                                          |                   |  |
|         | •<br>Security components are tested by independent test laboratories.                                                                                                                                                                                     |                   |  |
|         | •<br>The relevant security components are certified by an independent institu<br>tion.                                                                                                                                                                    |                   |  |
|         | •<br>Establish an approval procedure for the security components.                                                                                                                                                                                         |                   |  |

**Table 8–56 Protection through securing the function of security components** 

| MK5 | Code and name of safeguard                                    | Threats addressed |
|-----|---------------------------------------------------------------|-------------------|
|     | Availability of key management system (fall<br>back solution) | TK4, TK5          |
| 1   | Offline capability and secure backup:                         |                   |

<span id="page-96-0"></span>

| MK5 | Code and name of safeguard                                                                                                                                                                     | Threats addressed |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|     | Availability of key management system (fall<br>back solution)                                                                                                                                  | TK4, TK5          |
| 2   | •<br>Keys must in principle be available autonomously (at least temporarily),<br>without the background system, or if system interfaces fail.                                                  |                   |
|     | •<br>System-wide keys must be stored in at least two spatially separate places<br>(original and backup), and in secure environments.2                                                          |                   |
|     | •<br>It must be ensured that the backup copy fulfils the same security require<br>ments as the original.                                                                                       |                   |
|     | •<br>The replacement of defective key components must be regulated.                                                                                                                            |                   |
|     | Implementation according to fallback concept and backup of keys in a Trust<br>Centre:                                                                                                          |                   |
| 3   | See 1, and also:                                                                                                                                                                               |                   |
|     | •<br>A system concept must be drawn up which explicitly defines the availability<br>and fallback solutions together with availability periods, as well as agree<br>ments between the entities. |                   |
|     | •<br>Critical components must have a UPS and other security mechanisms (such<br>as RAID) so that the failure of sub-components does not impair the avail<br>ability of the system as a whole.  |                   |
|     | •<br>A sufficient number of replacement system components must be kept avail<br>able (in cold or warm standby) so as to ensure the required level of avail<br>ability.                         |                   |
|     | •<br>The Trust Centre must back up the system-wide keys.                                                                                                                                       |                   |

| Table 8–57 | Protection through availability of a key management system |
|------------|------------------------------------------------------------|
|            |                                                            |

| MK6     | Code and name of safeguard                                                                                                                                                                                                            | Threats addressed      |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
|         | Definition of actions in the event of keys being<br>compromised                                                                                                                                                                       | TK5, general procedure |
| General | This safeguard is to be treated independently from any safeguards used to pre<br>vent compromises from occurring.                                                                                                                     |                        |
| 1       | Compromise of diversified keys:                                                                                                                                                                                                       |                        |
|         | •<br>The customer medium concerned is withdrawn and blocked.                                                                                                                                                                          |                        |
| 2       | Compromise of non-diversified keys:                                                                                                                                                                                                   |                        |
| 3       | •<br>Regular and emergency versions of every key are stored in the SAMs and<br>carrier media. If compromised, the keys on the security modules are<br>switched so that from that point on, only the emergency version can be<br>used. |                        |
|         | •<br>Every time an RFID carrier medium communicates with the terminal, the<br>emergency version is used instead of the regular version – assuming this<br>has not already happened. To this end, suitable mechanisms must be main-    |                        |

<sup>2</sup> System-wide keys mean all symmetric keys as well as any asymmetric keys not specific to particular cards.

<span id="page-97-0"></span>

| MK6 | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                                                                 | Threats addressed      |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
|     | Definition of actions in the event of keys being<br>compromised                                                                                                                                                                                                                                                                                                                                                                            | TK5, general procedure |
|     | tained in the carrier medium that prevent the regular version from being<br>used later.<br>•<br>If the security modules are altogether compromised and an emergency ver<br>sion of the key is not available, then the security modules and therefore the<br>carrier media must be replaced immediately. The data in the system cannot<br>be considered trustworthy until all the security modules and carrier media<br>have been replaced. |                        |
|     |                                                                                                                                                                                                                                                                                                                                                                                                                                            |                        |

| Table 8–58 | Protection through definition of actions when keys are compromised |  |
|------------|--------------------------------------------------------------------|--|
|            |                                                                    |  |

| MK7 | Code and name of safeguard                                                                                                                                             | Threats addressed |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|     | Separation of keys                                                                                                                                                     | TK2, TK3          |
| 1   | Separate storage and handling of keys:                                                                                                                                 |                   |
| 2   | •<br>The applications in all of the components of the system must be separated<br>from one another in order to prevent malfunctions and the misuse of key<br>material. |                   |
| 3   |                                                                                                                                                                        |                   |

**Table 8–59 Protection through separation of keys** 

| MK8     | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Threats addressed |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|         | Loading new keys – securing the authenticity<br>and integrity of entitlements                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | TK3               |
| General | Keys should be associated clearly with an application or an entitlement, and<br>when the application or entitlement is loaded, they should be imported into the<br>carrier medium from the SAM. An autonomous process for loading new keys is<br>especially relevant for SAMs, and is advisable at all levels.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                   |
| 1       | Simple authentication concept:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                   |
| 2       | I. Preliminary remarks<br>1<br>Keys must each have a unique identifier containing information on the issu<br>ing organisation, a unique ID, and a version number.<br>2<br>There should be a way of deleting or blocking keys that have been used up.<br>3<br>New keys are loaded from a key management system into the SAM by the<br>system manager or someone appointed by him; this requires an online con<br>nection.<br>4<br>Keys must always be loaded under confidential conditions, for which a de<br>cryption key is required in the SAM.<br>5<br>A symmetric procedure is used for loading new keys, for which the key is<br>suer has a symmetric master key (KM_Storekey); derived from that, keys<br>that are particular to each card are stored in the SAMs (see II.)<br>II. General procedure<br>New keys are loaded using the following procedure: |                   |

<span id="page-98-0"></span>

|     | Code and name of safeguard                                                                                                                                                                                                                                                                                                                                                                     | Threats addressed |  |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
| MK8 | Loading new keys – securing the authenticity<br>and integrity of entitlements                                                                                                                                                                                                                                                                                                                  | TK3               |  |
|     | 1<br>The carrier medium sends its ID to the terminal, which passes it on to the<br>SAM.                                                                                                                                                                                                                                                                                                        |                   |  |
|     | 2<br>The SAM uses this to derive the card's specific key, K_Storekey, from the<br>master key (KM_Storekey).                                                                                                                                                                                                                                                                                    |                   |  |
|     | 3<br>The K_Storekey is used to perform authentication between the SAM and<br>customer medium. A shared session key is negotiated for this purpose.                                                                                                                                                                                                                                             |                   |  |
|     | 4<br>Once authentication has been completed successfully, the keys are en<br>crypted using the session key, and stored in the SAM.                                                                                                                                                                                                                                                             |                   |  |
|     | Complex authentication concept:                                                                                                                                                                                                                                                                                                                                                                |                   |  |
|     | I. Preliminary remarks                                                                                                                                                                                                                                                                                                                                                                         |                   |  |
|     | 1<br>Keys must each have a unique identifier containing information on the issu<br>ing organisation, a unique ID, and a version number.<br>2<br>There should be a way of deleting or blocking keys that have been used up.<br>3<br>New keys are loaded from a key management system into the SAM by the<br>system manager or someone appointed by him; this requires an online con<br>nection. |                   |  |
|     |                                                                                                                                                                                                                                                                                                                                                                                                |                   |  |
|     |                                                                                                                                                                                                                                                                                                                                                                                                |                   |  |
|     | 4<br>Keys must always be loaded under confidential conditions, for which a de<br>cryption key is required in the SAM.                                                                                                                                                                                                                                                                          |                   |  |
| 3   | 5<br>A symmetric procedure is used for loading new keys into a SAM, for which a<br>PKI with a CA must be established with which to certify all asymmetric keys.                                                                                                                                                                                                                                |                   |  |
|     | II. General procedure                                                                                                                                                                                                                                                                                                                                                                          |                   |  |
|     | New keys are loaded using a procedure such as the following:                                                                                                                                                                                                                                                                                                                                   |                   |  |
|     | 1<br>The key issuer (or key management system) sends a public key certified by<br>the CA to the terminal.                                                                                                                                                                                                                                                                                      |                   |  |
|     | 2<br>The SAM verifies the certificate (e.g. with Verify Certificate) and<br>stores the key issuer's public key temporarily.                                                                                                                                                                                                                                                                    |                   |  |
|     | 3<br>The key issuer encrypts the keys that are to be loaded, as well as the other<br>information associated with them (key ID, key version, operating counter …)<br>using the SAM's public encrypting key, signs the cryptogram using its own<br>private key, and sends the cryptogram and signature to the SAM.                                                                               |                   |  |
|     | 4<br>The SAM checks the signature using the key issuer's public signature key,<br>and if that is successful it decrypts the cryptogram using its own private de<br>cryption key, and saves the key and additional information permanently.                                                                                                                                                     |                   |  |
|     |                                                                                                                                                                                                                                                                                                                                                                                                |                   |  |

**Table 8–60 Protection through securing the authenticity and integrity when loading keys** 

# <span id="page-99-0"></span>**9 Definition of product-specific application scenarios**

We will now examine the processes described in Chapters [6](#page-31-1) and [7](#page-40-1) to provide examples of how particular products can be handled.

We have chosen the kind of product mix that is common among regional transport associations.

The following products will be discussed:

- 1 Local multi-journey entitlement (value of max. €20, non-interoperable)
- 2 E-ticket (interoperable and non-interoperable)
- 3 Interoperable fare calculation and multi-application compatibility

This combination covers most possible scenarios.

The selected application scenarios will be discussed for these products in more detail in Chapter [10](#page-105-1) and [11](#page-134-1).

## **9.1 Application scenario: "Local multi-journey entitlement"**

#### Entitlement

Purchasing this product entitles the customer to multiple use for single journeys on local transport. Interoperability is not required in this case. The entitlement is non-personalised.

#### Commercial value

The commercial value is normally less than €20. If this value is exceeded, then appropriate solutions should be used for the components.

#### Carrier media

The following carrier media are normally employed when using entitlements:

| Carrier medium                   | Usage model                                                                                                                                                                                                                                  | Characteristics                                                                                                                                                         |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Smart Ticket                     | Single electronic ticket. Used<br>universally for single entitle<br>ments and multiple entitlements<br>provided the value or system<br>security do not demand a se<br>cure chip card.                                                        | Data stored:<br>1 application, 1 entitlement,<br>Printed data:<br>area and duration of validity                                                                         |
| Secure multi<br>application card | The customer already has a<br>secure multi-application<br>compatible carrier medium (e.g.<br>CA chip card)<br>Personalised applications and<br>entitlements are loaded in a<br>secure memory. New applica<br>tions can be loaded at customer | Data stored:<br>Application including personal<br>data, 1 entitlement, seating<br>info, etc. Other applications ex<br>ist -> multi-application<br>Printed data:<br>Name |

<span id="page-100-0"></span>

| Carrier medium        | Usage model                                                                                                                               | Characteristics                                                                                                                                                                                              |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                       | centres and over the Internet.<br>New products can also be<br>loaded at a vending machine or<br>in the vehicle.                           |                                                                                                                                                                                                              |
| NFC mobile de<br>vice | Personalised applications, enti<br>tlements and any seating infor<br>mation are normally loaded<br>over-the-air into a secure mem<br>ory. | Data stored:<br>Application including personal<br>data, 1 entitlement.<br>Other applications may exist -><br>multi-application<br>Data shown on the display:<br>area and duration of validity,<br>activation |

**Table 9–1 Carrier media used for local multi-journey entitlements** 

The cost of carrier media is of great importance to the product provider. The cost of the carrier must be commensurate with the value of the entitlement. In the case of carriers that can only accommodate one application, their cost must be covered in full.

Loading applications and entitlements onto customer media that already exist eliminates the cost of the medium altogether. However, loading an additional application onto a multiapplication card does require special security precautions and a special infrastructure.

### Relevant processes

The following processes from Chapter [6](#page-31-1) must be taken into account for each carrier medium:

| Carrier medium                   | Process numbers                                           | Comments                                                                                                                                                                                         |
|----------------------------------|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Smart Ticket                     | P1B.1, P1B.2, P1B.3, P1B.4<br>P2B.1, P2B.2, P2B.3<br>P3.2 | Issuing of a non-personalised<br>Smart Ticket together with the enti<br>tlement.                                                                                                                 |
| NFC mobile de<br>vice            | P1B.1, P1B.2, P1B.3, P1B.4<br>P2B.2, P2B.3<br>P3.2        | Existing personalised NFC mobile<br>device. Application loading and<br>entitlement as described in P2B.2<br>"Over-the-air" or via NFC. New<br>entitlements can be loaded via<br>NFC using P2B.3. |
| Secure multi<br>application card | P1B.1, P1B.2, P1B.3, P1B.4<br>P2B.2, P2B.3<br>P3.2        | Existing personalised customer<br>card. Application loading and enti<br>tlement in accordance with P2B.2.<br>New entitlements can be loaded<br>using P2B.3.                                      |

**Table 9–2 Relevant processes** 

# <span id="page-101-0"></span>**9.2 Application scenario: "Electronic season ticket"**

We will examine this application scenario for an interoperable as well as a non-interoperable, personalised product.

### Entitlement

Purchasing this product entitles the customer, within a defined time period, to make use of transport services within a certain area or on a particular route. The transport is within the zone of a service provider or service providers that are already associated with each other. An example of this is a student's monthly travel card.

### Commercial value

The commercial value of a single entitlement can range from €20 and €500; depending on the product (see Chapter [2\)](#page-13-1). In the interoperable version, the damages incurred between the different partners of the IFM should be considered when analysing the commercial impact of a successful attack.

#### Carrier media

The following carrier media can be employed when using the entitlement:

| Carrier medium                    | Usage model                                                                                                                                                                                                                                                                                                                                                   | Characteristics                                                                                                                                                   |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Contact-less se<br>cure chip card | Specially produced customer<br>card including application and<br>entitlement. New entitlements of<br>the same type (e.g. monthly<br>entitlements) can be loaded.                                                                                                                                                                                              | Data stored:<br>Application including personal<br>data, entitlement, other appli<br>cations may be able to be<br>loaded before issuance.<br>Printed data:<br>Name |
| Secure multi<br>application card  | The customer owns a secure<br>multi-application-compatible<br>carrier medium (e.g. CA chip<br>card).<br>Personalised applications and<br>entitlements are loaded in a<br>secure memory. New applica<br>tions can be loaded at customer<br>centres and over the Internet.<br>New entitlements can also be<br>loaded at a vending machine or<br>in the vehicle. | Data stored:<br>Application including personal<br>data, 1 entitlement, etc. Other<br>applications may exist -> multi<br>application<br>Printed data:<br>Name      |

<span id="page-102-0"></span>

| Carrier medium        | Usage model                                                                                                                                                                                                                      | Characteristics                                                                                                                                                                                              |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFC mobile de<br>vice | The personalised applications,<br>entitlements and any seating<br>information are loaded into a<br>secure memory. New applica<br>tions and entitlements are nor<br>mally loaded over-the-air, but<br>also via the NFC interface. | Data stored:<br>Application including personal<br>data, 1 entitlement.<br>Other applications may exist -><br>multi-application<br>Data shown on the display:<br>area and duration of validity,<br>activation |

**Table 9–3 Carrier media for electronic season tickets** 

Relevant processes

The following processes from Chapter [6](#page-31-1) must be taken into account for each carrier medium:

| Carrier medium   | Process numbers            | Comments                                                                                                                            |  |
|------------------|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------|--|
| Secure chip card | P1A.1, P1A.2, P1A.3, P1A.4 | Personalised customer card. New<br>entitlements can be loaded, but not<br>new applications.                                         |  |
|                  | P2A.1, P2A.2, P2A.3, P2A.4 |                                                                                                                                     |  |
|                  | P3.2                       |                                                                                                                                     |  |
| Secure multi     | P1A.1, P1A.2, P1A.3, P1A.4 | Personalised customer card. New<br>entitlements and applications can<br>be loaded.                                                  |  |
| application card | P2A.1, P2A.2, P2A.3, P2A.4 |                                                                                                                                     |  |
|                  | P3.2                       |                                                                                                                                     |  |
| Secure NFC mo    | P1A.1, P1A.2, P1A.3, P1A.4 | New applications and products are<br>loaded "over-the-air" or via the<br>NFC interface.                                             |  |
| bile device      | P2A.1, P2A.2, P2A.3, P2A.4 |                                                                                                                                     |  |
|                  | P3.2                       | Processes P2A.1 – P2A.3 are only<br>relevant if the NFC mobile device is<br>supplied initialised and loaded with<br>an entitlement. |  |

**Table 9–4 Relevant processes** 

## **9.3 Application scenario: "Interoperable unceasing entitlement with automatic fare calculation"**

### Product

Purchasing this personalised product entitles the customer to utilise any transport service in any area and on any route. The entitlement is interoperable, which means it is valid at all times and with every service provider that supports this special application. The customer has to register at the beginning of his journey using his customer medium at a terminal, and de-register, or check out, at the end of the journey. The fare is calculated automatically on the basis of the local fares.

<span id="page-103-0"></span>The VDV Core Application provides an implementation example of how this product is handled. Without having to know the fares or zones, the customer can use the services of any public transport service provider that employs compatible inspection equipment.

#### Commercial value

The commercial value of the entitlement can range from tens of euros to several thousand euros.

#### Carrier media

The following carrier media can be employed when using the entitlement:

| Carrier medium                   | Usage model                                                                                                                                                                                                                                               | Characteristics                                                                                                                                                                                              |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Secure multi<br>application card | The customer receives a secure<br>multi-application-compatible<br>carrier medium (e.g. CA chip<br>card) with the special application<br>and entitlement.<br>New applications and products<br>can be loaded at customer cen<br>tres and over the Internet. | Data stored:<br>Application including personal<br>data, 1 entitlement, etc. Other<br>applications may exist -> multi<br>application<br>Printed data:<br>Name, application                                    |
| NFC mobile de<br>vice            | The personalised application,<br>entitlement and any seating in<br>formation are loaded into a se<br>cure memory. New applications<br>and products must be loaded in<br>the field.                                                                        | Data stored:<br>Application including personal<br>data, 1 entitlement.<br>Other applications may exist -><br>multi-application<br>Data shown on the display:<br>area and duration of validity,<br>activation |

**Table 9–5 Carrier media for "Interoperable entitlement with AFC"** 

#### Relevant processes

The following processes from Chapter [6](#page-31-1) must be taken into account for each carrier medium:

| Carrier medium   | Relevant processes         | Comments                                                                           |  |
|------------------|----------------------------|------------------------------------------------------------------------------------|--|
| Secure multi     | P1A.1, P1A.2, P1A.3, P1A.4 | Personalised customer card. New<br>entitlements and applications can<br>be loaded. |  |
| application card | P2A.1, P2A.2, P2A.3, P2A.4 |                                                                                    |  |
|                  | P3.2                       |                                                                                    |  |

<span id="page-104-0"></span>

| Carrier medium               | Relevant processes         | Comments                                                                                                                            |
|------------------------------|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Secure NFC mo<br>bile device | P1A.1, P1A.2, P1A.3, P1A.4 | New applications and products are                                                                                                   |
|                              | P2A.1, P2A.2, P2A.3, P2A.4 | loaded "over-the-air" or via the<br>NFC interface.                                                                                  |
|                              | P3.2                       | Processes P2A.1 – P2A.3 are only<br>relevant if the NFC mobile device is<br>supplied initialised and loaded with<br>an entitlement. |

**Table 9–6 Relevant processes** 

# <span id="page-105-1"></span><span id="page-105-0"></span>**10 Suggestions on implementing the system as a whole**

This Chapter describes, as an example, the entire system for the "eTicketing for public transport" application area.

The overall system is made up of the eTicketing infrastructure and the carrier media. The term eTicketing infrastructure refers collectively to all of the system components and associated interfaces installed by the product providers, service providers and system manager.

The solution presented here can cover the aforementioned role descriptions, processes and application scenarios in their maximum complexity. Variations on it are conceivable in the case of specialised implementations in actual use. In particular, simplification of the role model, and reductions in the number of different media, applications, products, and of the public transport entities involved, would also enable simplifications of the system and the processes.

The focus of these considerations and of the suggestions regarding safeguards is on the implementation of the RFID interface and the directly connected components, carrier medium and reader. The safeguards for the carrier media are highly dependent on the application scenario concerned, and are described in Chapter [11](#page-134-1) in their various manifestations. General information about the carrier media can be found in Section [10.2.](#page-129-1)

<span id="page-105-2"></span>![](_page_105_Figure_6.jpeg)

The following diagram shows the system as a whole and its principal components.

# <span id="page-106-0"></span>**10.1 Suggestions on executing the eTicketing infrastructure**

### <span id="page-106-1"></span>**10.1.1 Determining the protection demand for the eTicketing infrastructure**

The following general considerations apply to the eTicketing infrastructure, and these should be included when determining the protection requirements:

- 1 The systems in [Figure 10–1](#page-105-2) should simultaneously support a range of different products and carrier media, as defined in the proposed application scenarios.
- 2 Data relating to particular persons must be managed and processed.
- 3 Usage data will be generated and must be processed.
- 4 Calculation data must be logged and forwarded if "automatic fare calculation" applications and products are to be supported. Interoperability is required.
- 5 The case of interoperability being assured by agreements between the entities can also be examined as an option.

On the basis of the criteria described in Section [8.2.5](#page-59-1), the eTicketing infrastructure can be assigned to the following protection demand categories:

| Security target |                                                              | Protection<br>demand<br>category | Criteria for allocating to protection demand category                                                                                                        |
|-----------------|--------------------------------------------------------------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SS1             | Technical<br>compatibility                                   | 1                                | All of the system components are from the same sup<br>plier. The supplier ensures that they are compatible.                                                  |
|                 |                                                              | 2                                | The system has to function with components from a<br>small number of defined suppliers. The system man<br>ager or a system integrator ensures compatibility. |
|                 |                                                              |                                  | Open system that has to function with components<br>from any company in the market.                                                                          |
|                 |                                                              | 3                                | System normally acquired by offering out for public<br>tender.                                                                                               |
| SS2             | Fallback solu<br>tion in the<br>event of mal<br>function     | 1                                | Malfunction affects only a few customers.                                                                                                                    |
|                 |                                                              | 2                                | Malfunction affects many customers.                                                                                                                          |
|                 |                                                              |                                  | Malfunction affects a large proportion of customers.                                                                                                         |
|                 |                                                              | 3                                | System malfunctions (sales system, readers, verifica<br>tion system, key management system) affect a large<br>number of customers and entitlements.          |
| SS3             | Intuitive, fault<br>tolerant op<br>eration                   | 1                                | A few customers cannot operate it intuitively.                                                                                                               |
|                 |                                                              | 2                                | Many customers cannot operate it intuitively.                                                                                                                |
|                 |                                                              | 3                                | A large proportion of customers cannot operate it intui<br>tively.                                                                                           |
| SI1             | Protection of<br>personal data<br>(including<br>personal us- | 1                                | Customer's reputation is damaged.                                                                                                                            |
|                 |                                                              |                                  | Customer's social existence is damaged.                                                                                                                      |
|                 |                                                              | 2                                | If person-related invoicing information or payment de                                                                                                        |

| Security target |                                                       | Protection<br>demand<br>category | Criteria for allocating to protection demand category                                                                                                                                                                                        |  |
|-----------------|-------------------------------------------------------|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
|                 | age data)                                             |                                  | tails stored in the system are stolen or manipulated, the<br>customer may suffer considerable commercial and so<br>cial consequences.                                                                                                        |  |
|                 |                                                       | 3                                | Customer's physical existence is damaged.                                                                                                                                                                                                    |  |
| SI2             | Protection of<br>entitlements                         | 1                                | Predicted product-related loss of sales through coun<br>terfeiting, damage or manipulation <1%                                                                                                                                               |  |
|                 |                                                       | 2                                | Predicted product-related loss of sales through coun<br>terfeiting, damage or manipulation <3%                                                                                                                                               |  |
|                 |                                                       | 3                                | Predicted product-related loss of sales through coun<br>terfeiting, damage or manipulation >3%                                                                                                                                               |  |
|                 |                                                       |                                  | DoS attacks on the system can lead to a total opera<br>tional breakdown, thus causing considerable commer<br>cial loss.                                                                                                                      |  |
|                 |                                                       | 1                                | Data becomes known to third parties.                                                                                                                                                                                                         |  |
|                 | Protection of                                         | 2                                | Data is lost.                                                                                                                                                                                                                                |  |
| SI3             | logistical data<br>(anonymised<br>usage data)         |                                  | The loss of logistical data can also occur through tech<br>nical defects and can cause operational difficulties.                                                                                                                             |  |
|                 |                                                       | 3                                | Data is falsified.                                                                                                                                                                                                                           |  |
|                 | Reliable in<br>voicing (per<br>sonalised)             | 1                                | Data is temporarily unavailable.                                                                                                                                                                                                             |  |
|                 |                                                       | 2                                | Data is lost.                                                                                                                                                                                                                                |  |
| SI4             |                                                       | 3                                | Data is falsified, misused, etc.                                                                                                                                                                                                             |  |
|                 |                                                       |                                  | Invoicing fraud is a possibility in a system with multiple<br>entities that do not trust one another.                                                                                                                                        |  |
| SI5             | Protection of<br>applications<br>and entitle<br>ments | 1                                | Applications are issued by the same application issuer<br>and entitlements by the same product owner.                                                                                                                                        |  |
|                 |                                                       | 2                                | Applications are issued by different application issuers<br>and entitlements by different product owners, product<br>providers and service providers. Several companies<br>collaborate and "trust" each other in the process.                |  |
|                 |                                                       | 3                                | Applications are issued by different application provid<br>ers, and entitlements by different product owners,<br>product providers and service providers. Several com<br>panies collaborate and do not "trust" each other in the<br>process. |  |
|                 |                                                       |                                  | When entitlements are loaded onto multi-application<br>cards or NFC mobile devices, it must always be as<br>sumed that applications from other entities may be pre<br>sent on the customer medium.                                           |  |

<span id="page-108-0"></span>

| Security target |                                                                  | Protection<br>demand<br>category | Criteria for allocating to protection demand category       |
|-----------------|------------------------------------------------------------------|----------------------------------|-------------------------------------------------------------|
| SP3             | Data minimi<br>zation                                            | 1                                | Personal data is not used.                                  |
|                 |                                                                  | 2                                | Personal data is used, but no usage data is collected.      |
|                 |                                                                  | 3                                | Personal data is used, as is usage and calculation<br>data. |
| SP4             | Protection<br>against the<br>creation of<br>movement<br>profiles | 1                                | Customer's reputation is damaged.                           |
|                 |                                                                  | 2                                | Customer's social existence is damaged.                     |
|                 |                                                                  | 3                                | Customer's physical existence is damaged.                   |

**Table 10–1 The system's protection requirements** 

### **10.1.2 Interfaces in the system as a whole**

The system shown in [Figure 10–1](#page-105-2) is reliant on interaction between all the system components. In order to facilitate the business processes described in Chapter [6](#page-31-1), the technical interfaces and operative interaction between the components have to be specified.

Furthermore, agreements must be made between the entities to regulate the responsibilities and the operational procedures.

### **10.1.2.1 Threats relevant to the eTicketing infrastructure**

The following threats relevant to the interfaces of the system as a whole can be deduced from the security targets used to determine the protection demand in Section [10.1.1.](#page-106-1)

| Threats to the contact-less<br>interface |                                                                                            | Protection<br>demand | Comments                                                                                                                                                                                                                                                                     |
|------------------------------------------|--------------------------------------------------------------------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TC1                                      | Lack of compatibil<br>ity between the<br>interfaces of the<br>carrier medium and<br>reader | 3                    | A lack of compatibility between interfaces pre<br>vents the system from working when loading<br>and using entitlements, checking entitlements,<br>and so on. The result is similar to a DoS attack<br>on the system. Many customers and/or enti<br>tlements may be affected. |
| TC2                                      | Eavesdropping                                                                              | 3                    | Unauthorised listening-in to communication<br>between a carrier medium and a reader.                                                                                                                                                                                         |

<span id="page-109-0"></span>

| Threats to the contact-less<br>interface |                                   | Protection<br>demand | Comments                                                                                                                                                                                                                                                                                                                       |
|------------------------------------------|-----------------------------------|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TC3                                      | DoS attack on the<br>RF interface | 1                    | 1<br>Interference in RFID communication<br>(jamming).<br>2<br>Interference in the anti-collision mecha<br>nism for selecting the carrier medium<br>(blocker tag)<br>3<br>Blocking the electromagnetic field of the<br>reader (shielding).<br>4<br>Altering the resonance frequency of reader<br>or carrier medium (de-tuning). |

**Table 10–2 Threats relevant to the contact-less interface** 

| Threats to the system as a<br>whole |                                                    | Protection<br>demand | Comments                                                                                                                                                                                                                                                                                                                               |
|-------------------------------------|----------------------------------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TS1                                 | Lack of fallback<br>solution                       | 3                    | The lack of a fallback solution when system<br>interfaces fail, such as the ticket sales system,<br>administration system for carrier media and<br>entitlements, or verification system, can lead to<br>a complete breakdown of services (sales, in<br>voicing, acceptance, etc.).                                                     |
| TS2                                 | Unauthorised<br>scanning of refer<br>ence data     | 3                    | Keys, as well as information about the media,<br>entitlements and usage, and sometimes per<br>sonal data and calculation data, are passed<br>between the system components via inter<br>faces. The retrieval of this data by unauthor<br>ised persons would discredit the system and<br>enable attacks.                                |
| TS3                                 | Manipulation of<br>reference data in<br>the system | 3                    | Keys, as well as information about the media,<br>entitlements and usage, and sometimes per<br>sonal data and calculation data, are passed<br>between the system components via inter<br>faces. The manipulation of this data by unau<br>thorised persons represents a serious threat.                                                  |
| TS4                                 | System malfunction                                 | 3                    | Malfunctions in the interfaces between the sys<br>tems can be caused in a range of scenarios by<br>technical faults, incorrect operation or DoS<br>attacks:<br>1<br>Fault in interfaces<br>2<br>Lack of availability of interfaces<br>3<br>Fault in power supply<br>4<br>Interruption in power connection<br>5<br>Physical destruction |
| TS5                                 | Lack of compatibil<br>ity between inter<br>faces   | 3                    | A lack of compatibility between interfaces<br>causes malfunctions. The result is similar to a<br>DoS attack on the system. Many customers<br>and/or entitlements may be affected.                                                                                                                                                      |

<span id="page-110-0"></span>

| Threats to the system as a<br>whole |                                                  | Protection<br>demand | Comments                                                                                                          |
|-------------------------------------|--------------------------------------------------|----------------------|-------------------------------------------------------------------------------------------------------------------|
| TS10                                | Unjustified gather<br>ing and storing of<br>data | 3                    | The automatic fare calculation concept makes<br>use of personal and person-related usage and<br>calculation data. |

| Table 10–3 | Threats relevant to the systems |
|------------|---------------------------------|
|            |                                 |

#### **10.1.2.2 Definition of safeguards for the interfaces of the system as a whole**

Based on the relevant threats in the preceding section, this section defines general execution proposals and safeguards for the system as a whole and the system components. These safeguards are described in detail in Section [8.4.](#page-66-1)

| Threat |                                                                                            | Safeguard       | Safeguard                                                                                                                                                                                                                                                                       |
|--------|--------------------------------------------------------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TC1    | Lack of compati<br>bility between the<br>interfaces of the<br>carrier medium<br>and reader | MS1.3           | 1<br>Introduction of interface tests and ap<br>proval procedures – Certification                                                                                                                                                                                                |
| TC2    | Eavesdropping                                                                              | MS2.3<br>MS3.3  | 1<br>Ensuring the confidentiality of commu<br>nication between RFID carrier medium<br>and terminal in order to prevent eaves<br>dropping – Mutual, dynamic authentica<br>tion during transmission.<br>2<br>Introduction of contact-less interface as<br>defined by ISO/IEC14443 |
| TC3    | DoS attack on the<br>RF interface                                                          | MS3.1           | 1<br>Introduction of contact-less interface as<br>defined by ISO/IEC14443                                                                                                                                                                                                       |
| TS1    | Lack of fallback<br>solution                                                               | MS4.3           | 1<br>Definition of fallback solutions in the<br>event of system interface or system<br>component failure – Implementation<br>according to fallback concept                                                                                                                      |
| TS2    | Unauthorised<br>scanning of refer<br>ence data                                             | MS5.3<br>MS6.3  | 1<br>Securing the confidentiality of data<br>when communicating within the system<br>– Secure communication channel                                                                                                                                                             |
|        |                                                                                            | MS15.3          | 2<br>Confidential storage of data – Maintain<br>ing privacy using multi-tenant access<br>protection                                                                                                                                                                             |
|        |                                                                                            |                 | 3<br>Separation of applications – Separate<br>storing and processing of data                                                                                                                                                                                                    |
| TS3    | Manipulation of<br>reference data in<br>the system                                         | MS6.3<br>MS7.3  | 1<br>Confidential storage of data – Multi<br>tenant access protection, role model<br>2<br>Securing data integrity in order to pro                                                                                                                                               |
|        |                                                                                            | MS8.3<br>MS15.3 | tect against manipulation when trans<br>mitting data within the system – MAC or<br>signatures                                                                                                                                                                                   |
|        |                                                                                            |                 | 3<br>Securing data integrity when storing<br>data – Checksums                                                                                                                                                                                                                   |

<span id="page-111-0"></span>

| Threat      |                                                                     | Safeguard                                                        | Safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |  |
|-------------|---------------------------------------------------------------------|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
|             |                                                                     |                                                                  | 4<br>Separation of applications – Separate<br>storing and processing of data                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |  |
| TS4         | System malfunc<br>tion                                              | MS4.3<br>MS9.3<br>MS10.3<br>MS11.3<br>MS12.3<br>MS13.3<br>MS14.3 | 1<br>Definition of fallback solutions in the<br>event of system interface or system<br>component failure – Implementation<br>according to fallback concept<br>2<br>Securing system functions against DOS<br>attacks to the interfaces – Security con<br>cept<br>3<br>Securing the function of the system<br>against incorrect operation by employ<br>ees and users – Tests, personnel and<br>user introductions.<br>4<br>Secure the function of the system to<br>prevent the technical failure of compo<br>nents and transmission routes –<br>Evaluation of components<br>5<br>Specifications for system concept and<br>requirements for components with the<br>aim of integration and interoperability –<br>interoperability tests in accordance with<br>test concept, evaluation<br>6<br>Ergonomic user instructions<br>7<br>Support – System-wide support |  |
| TS5<br>TS10 | Lack of compati<br>bility between<br>interfaces<br>Unjustified gath | MS1.3<br>MS11.3<br>MS12.3<br>MS17.3                              | 1<br>Introduction of interface tests and ap<br>proval procedures – Certification<br>2<br>Secure the function of the system to<br>prevent the technical failure of compo<br>nents and transmission routes –<br>Evaluation of components<br>3<br>Specifications for system concept and<br>requirements for components with the<br>aim of integration and interoperability –<br>interoperability tests in accordance with<br>test concept, evaluation<br>1<br>Satisfying the data minimization obliga                                                                                                                                                                                                                                                                                                                                                           |  |
|             | ering and storing<br>of data                                        |                                                                  | tion – Special safeguards                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |  |

**Table 10–4 Safeguards for the system as a whole** 

### **10.1.2.3 Residual risks**

For technical and commercial reasons, it is not always possible to eliminate threats completely using safeguards. In such cases a certain risk remains.

The residual risk should be determined and documented as part of the planning of the actual implementation.

### <span id="page-112-0"></span>**10.1.3 Readers**

Readers control the flow of information for reading from and writing to the carrier medium, using a contact-less communication protocol. The reader (PCD as defined by ISO/IEC14443) has the active role (master), while the carrier medium (PICC as defined by ISO/IEC14443) is passive (slave).

Readers are integrated into various system components:

- 1 Sales systems at sales points
- 2 Vending machines
- 3 Service desks
- 4 CICO and activation terminals for checking in and out when using electronic tickets.
- 5 Mobile inspection units

The CICO and activation terminals must have the following features:

- 1 Contact-less read/write unit with interface as defined by ISO/IEC14443A/B Part 1-4.
- 2 Capacity to store all usage data until the next data exchange with the central system.
- 3 Parallel support of multiple carrier media, applications and products (selection using ID).
- 4 Basic cryptographic functions.
- 5 Support for SAMs. Multiple SAM slots should be available (four is currently standard).
- 6 The result of the validation should be displayed visually.
- 7 At turnstiles, the length of time taken to read the media, validate the entitlement and signal authorisation or open the barrier should not exceed 300 ms. The reader, and the other components involved, must be designed to perform accordingly.

![](_page_112_Figure_17.jpeg)

**Figure 10–2 Example of a reader with Smart Card or Smart Label** 

### <span id="page-113-0"></span>**10.1.3.1 Threats relevant to the readers**

The following threats relevant to the interfaces of the system as a whole can be deduced from the assumptions used to determine the protection demand in Section [10.1.1.](#page-106-1)

| interface | Threats to the contact-less                                                                  | Protection<br>demand | Comments                                                                                                                                                                                                                                                                                                                        |
|-----------|----------------------------------------------------------------------------------------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TC1       | Lack of compatibil<br>ity between the in<br>terfaces of the car<br>rier medium and<br>reader | 3                    | A lack of compatibility between interfaces pre<br>vents the system from working when loading<br>and using entitlements, checking entitlements,<br>and so on. The result is similar to a DoS attack<br>on the system. Many customers and/or entitle<br>ments may be affected.                                                    |
| TC2       | Eavesdropping                                                                                | 3                    | Unauthorised listening-in to communication be<br>tween a carrier medium and a reader.                                                                                                                                                                                                                                           |
| TC3       | DoS attack on the<br>RF interface                                                            | 3                    | 1<br>Interference in RFID communication (jam<br>ming).<br>2<br>Interference in the anti-collision mechanism<br>for selecting the carrier medium (blocker<br>tag).<br>3<br>Blocking the electromagnetic field of the<br>reader (shielding).<br>4<br>Altering the resonance frequency of reader<br>or carrier medium (de-tuning). |

| Table 10–5 | Threats relevant to the contact-less interface |  |
|------------|------------------------------------------------|--|
|            |                                                |  |

|     | Threats to the reader                                      | Protection<br>demand | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----|------------------------------------------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TR1 | Unauthorised ma<br>nipulation of refer<br>ence information | 3                    | The manipulation of reference information<br>(keys, evaluation algorithms, blacklists and<br>whitelists) can be employed for unauthorised<br>use or for DoS.                                                                                                                                                                                                                                                                                                   |
| TR2 | Unauthorised scan<br>ning of reference<br>information      | 3                    | The retrieval of reference information (keys,<br>evaluation algorithms, blacklists and whitelists)<br>can be employed for unauthorised use (e.g.<br>counterfeiting of entitlements) and for DoS.                                                                                                                                                                                                                                                               |
| TR3 | Reader malfunction                                         | 3                    | Reader malfunctions can be caused in a range<br>of scenarios by technical faults, incorrect opera<br>tion or DoS attacks:<br>1<br>Fault in contact-less interface<br>2<br>Fault in reference information (keys, black<br>lists, etc)<br>3<br>Fault in application implementation<br>4<br>Fault in evaluation algorithms for entitle<br>ments<br>5<br>Fault in power supply<br>6<br>Interruption of the link to the central system<br>7<br>Physical destruction |

<span id="page-114-0"></span>

| Threats to the reader |                                                  | Protection<br>demand | Comments                                                                                                                                                                                                                                                                     |
|-----------------------|--------------------------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                       |                                                  |                      | 8<br>Fault in operational instruction functions                                                                                                                                                                                                                              |
| TR4                   | Lack of user in<br>structions                    | 3                    | A lack of user-friendliness at vending machines<br>and the terminals used for activating entitle<br>ments and checking-in / checking-out can cause<br>considerable operative problems.                                                                                       |
| TS1                   | Lack of fallback<br>solution                     | 3                    | The lack of a fallback solution when system<br>interfaces fail, such as the ticket sales system,<br>administration system for carrier media and<br>entitlements, or verification system, can lead to<br>a complete breakdown of services (sales, in<br>voicing, CICO, etc.). |
| TS5                   | Lack of compatibil<br>ity between inter<br>faces | 3                    | A lack of compatibility between interfaces<br>causes malfunction. The result is similar to a<br>DoS attack on the system. Many customers<br>and/or entitlements may be affected.                                                                                             |

**Table 10–6 Threats relevant to the reader** 

### <span id="page-114-1"></span>**10.1.3.2 Definition of safeguards for the reader and its applications**

Based on the relevant threats in the preceding section, this section defines general execution proposals and safeguards for the reader and its applications. These safeguards are described in detail in Section [8.4](#page-66-1).

| Threat |                                                                                            | Safeguard      | Safeguard                                                                                                                                                                                                                                                                     |
|--------|--------------------------------------------------------------------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TC1    | Lack of compati<br>bility between the<br>interfaces of the<br>carrier medium<br>and reader | MS1.3<br>MR1.3 | 1<br>Introduction of interface tests and ap<br>proval procedures – Certification                                                                                                                                                                                              |
| TC2    | Eavesdropping                                                                              | MS2.3<br>MS3.3 | 1<br>Ensure the confidentiality of communi<br>cation between RFID carrier medium<br>and terminal in order to prevent eaves<br>dropping – Mutual, dynamic authentica<br>tion during transmission.<br>2<br>Introduction of contact-less interface as<br>defined by ISO/IEC14443 |
| TC3    | DoS attack on the<br>RF interface                                                          | MS3.1          | 1<br>Introduction of contact-less interface as<br>defined by ISO/IEC14443                                                                                                                                                                                                     |
| TR1    | Unauthorised<br>manipulation of<br>reference infor<br>mation                               | MR2.3          | 1<br>Protection of reference information<br>against retrieval, data errors and ma<br>nipulation – Advanced protection                                                                                                                                                         |
| TR2    | Unauthorised<br>scanning of refer<br>ence information                                      | MR2.3          | 1<br>Protection of reference information<br>against retrieval, data errors and ma<br>nipulation – Advanced protection                                                                                                                                                         |

<span id="page-115-0"></span>

| Threat |                                                 | Safeguard                 | Safeguard                                                                                                                                                                                                                                                                                                                 |
|--------|-------------------------------------------------|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TR3    | Reader malfunc<br>tion                          | MR3.3                     | 1<br>Protection of the reader against mal<br>function – Evaluation                                                                                                                                                                                                                                                        |
| TR4    | Lack of user in<br>structions                   | MS13.3                    | 1<br>Ergonomic user instructions                                                                                                                                                                                                                                                                                          |
| TS1    | Lack of fallback<br>solution                    | MS4.3                     | 1<br>Definition of fallback solutions in the<br>event of system interface or system<br>component failure – Implementation<br>according to fallback concept                                                                                                                                                                |
| TS5    | Lack of compati<br>bility between<br>interfaces | MS1.3<br>MS11.3<br>MS12.3 | 1<br>Introduction of interface tests and ap<br>proval procedures – Certification<br>2<br>Secure the function of the system to<br>prevent the technical failure of compo<br>nents and transmission routes –<br>Evaluation of components<br>3<br>Specification of system concept and<br>component requirements – Evaluation |

**Table 10–7 Safeguards for the reader and its applications** 

### **10.1.3.3 Residual risks**

For technical and commercial reasons, it is not always possible to eliminate threats completely using safeguards. In such cases a certain risk remains.

The residual risk should be determined and documented as part of the planning of the actual implementation.

### **10.1.4 Sale, inspection and management systems**

### **10.1.4.1 Sales systems**

Access to the products must be easy and inexpensive for all potential customers, which is why a range of points of sale should be supported. These are described in the following:

### **Sales point**

This could be, for instance, the office of a transport company (e.g. *CA customer contract partner*) or a travel agent.

#### Sales procedure

The customer visits the sales point in person and purchases the product there:

- Identification, if required, is by identity card.
- The booking is done in dialogue with the customer at the sales point.
- Payment is made at the sales point.

If the carrier medium can be produced there and then, or the entitlement can be loaded onto an existing customer medium (see "*Technical equipment*"), then the customer can take the

product away with him straight away. If not, then the product and the carrier medium are sent by post or held at the sales point, ready for subsequent collection.

#### Technical equipment

The sales point has direct access to the ticket sales system. This is a precondition for services such as seat reservation.

In many instances it makes commercial sense to install equipment such as an RFID ticket printer which can initialise and load entitlements onto certain carrier media. Furthermore, a simple contact-less reader at the sales point can provide a cost-effective way of loading entitlements onto an existing customer medium. If such a contact-less reader exists, then in future it could become possible to utilise an electronic proof of identity as a means of securely and automatically transferring personal data into the ticket system (e.g. for setting up a customer account), or for secure identification.

Personal and IT infrastructure at the sales point is not always trustworthy.

#### **Vending and collection machines**

At vending machines, products are sold and issued in a direct interaction between the vending machine and the customer.

Vending machines are installed in customer centres, railway stations, bus and tram stops, and also inside vehicles. They are especially suitable for selling high-demand products which do not require complex procedures to order or produce.

Vending machines that are used in vehicles must be able to work offline. The exchange of data with a sales system is only possible at certain intervals.

#### Selling personalised Products

At present there is no method of identifying a customer for the first time, securely and automatically. This means that registration as defined in Process P1A cannot take place at a vending machine, and customer accounts cannot be set up. This may change in future with the introduction of the electronic identity card (eID).

It is however possible to load new entitlements onto media belonging to known customers who already possess a known personalised customer medium. In this case, identification is done using the existing customer medium itself.

#### Selling anonymous products

In the simplest case, anonymous carrier media and entitlements are sold through vending machines.

The customer purchases or collects the product at a vending machine:

- Booking is done at a vending machine.
- Payment is made directly using methods such as Maestro or credit cards.
- When collecting, the customer identifies himself using his own customer medium, or in future an eID or other electronic means of identification.

The carrier medium for the product purchased is produced by the vending machine. Alternatively, the entitlement can be loaded onto an existing customer medium (see "*Technical equipment*"). The customer can then take the product away.

#### Collecting pre-ordered products

Vending machines can serve as issuing points for products ordered by Internet or telephone.

If the vending machine is used for collecting pre-ordered entitlements, then the customer must always identify himself. If the customer possesses his own customer medium then this can be used for identification and for receiving the entitlement. If not, then other processes must be used for identification (e.g. credit card).

#### Technical equipment

The vending machine requires direct access to the ticket sales system, at least for some of the time. Another condition is that it must incorporate a ticket printer with an in-built reader which can initialise the carrier media issued, and load entitlements onto them.

If the machine is to be able to load entitlements onto existing customer media, then uninterrupted access is required to the ticket sales system and the management system for carrier media and applications. A compatible reader must also be installed in the vending machine.

#### **Internet, call centres, ordering by post**

#### Sales procedure

The customer places the order by telephone, Internet or fax from any location:

- The booking, choice of seat etc. can be made in a direct interaction when using the Internet or telephone. Written orders do not allow this.
- Payment is made by Maestro, credit card or direct debit.
- For secure identification, the personal data sent by the customer may have to be checked.

The carrier medium and product are produced centrally and sent by post. Alternatively it can be agreed that the product will be collected somewhere such as an issuing point or vending machine (see Vending and collection machines).

#### Technical equipment

The product provider operates an Internet sales platform or a call centre. The customer does not require any particular technical equipment.

The carrier medium and product can be produced using a mass personaliser in a secure environment.

#### **Internet**

#### Sales procedure

The customer places the order interactively by Internet from any location (e.g. at home).

If the customer has a customer medium which already contains the necessary application, then the required product can be loaded onto it. If a chip card is being used, then a contactless reader is required – such as one that works with a home computer, for example. If an NFC mobile device is to be used as the customer medium, then the product can also be loaded "Over the Air":

- <span id="page-118-0"></span>• Booking, seat reservation and so on can be done in a direct interaction when using the Internet.
- Identification is done using the customer medium and the personal data stored in the application.
- Payment is made using Maestro, credit card or direct debit.

The entitlement is loaded directly into the application on the customer medium.

If the customer does not yet have a customer medium but does have a contact-less reader, then secure identification of the customer will in future be able to take place using a eID, thus enabling the customer medium to be ordered securely and conveniently.

#### Technical equipment

The product provider operates an Internet sales platform, which is connected to the key, carrier and application management systems. The customer requires a customer medium containing the appropriate application, and – if a chip card or eID is being used – a contact-less home reader device.

Provided suitable media, readers and protocols are used, there will be no weak-spots in the process of loading new products onto an existing customer medium, or registering and ordering (see Process P1A.4).

#### **10.1.4.2 Ticket system**

The ticket system supports the primary selling and handling processes:

- 1 Registering and ordering
- 2 Creating the entitlement
- 3 Payment, and checking creditworthiness
- 4 Managing the entitlements sold
- 5 Forwarding the necessary data to the verification system

Customer data and orders are stored in the ticket system. Provided the transport service and product support it, seating can also be allocated using seating plans which are also stored there. The ticket system also incorporates a procedural management system which performs actions such as address comparisons and payment processing including credit checks, and which also initiates the production and dispatch of carrier media and entitlements.

<span id="page-119-0"></span>![](_page_119_Figure_1.jpeg)

**Figure 10–3 An example of a ticket system with possible process flows** 

A ticket system has interfaces to the key management system and the system which administers the carrier media and applications. All of the information required to enter a special event (apart from the information transferred in the key management system) is gathered together by the ticket system and sent to the service provider via a defined interface.

There are other interfaces to the sales points and the places where the carrier media are produced. This also includes sales and distribution, and the management of loading applications and products onto existing media via the Internet.

It can be assumed that a ticket system will be housed in a secure environment. Personaliser SAMs must be connected to it in order to be able to produce entitlements and load them onto carrier media.

From the point of view of the service provider, more than one ticket system can be used.

### **10.1.4.3 Central verification system**

The verification system helps the service provider to check the customers' journey entitlements, and to gather and pass on information relevant to invoicing. This requires the following functions:

1 Support of Process P3 for checking in, checking out and if necessary activation.

- <span id="page-120-0"></span>2 Support for the particular carrier media, applications and products.
	- a Implementation of the technical procedures required to support the carrier media, applications and products.
	- b Implementation and management of SAMs.
- 3 Control of terminals (CICO terminals, access barriers, mobile conductor's terminals, etc).
- 4 Receiving, distributing and utilising the information provided by the ticket systems.
- 5 Receiving, distributing and utilising the keys and identifiers provided by the system manager and registrar.
- 6 Reporting invoicing-related data and usage history to the ticket systems.

The terminals in public transport systems are not usually connected permanently to a data network. This applies especially to terminals in vehicles. That means all of the information required for entry, evaluation and activation of entitlements, and where applicable fare calculation, has to be stored locally in the terminals.

#### **10.1.4.4 Terminals**

The job of a terminal is to read, evaluate and if necessary activate the entitlement when the customer checks in or out. A contact-less reader is integrated into the terminal.

In normal operation, stationary terminals connect daily for at least a certain amount of time to the central verification system via a data network (LAN or WLAN) or by exchanging memory media. Information required to evaluate the entitlements is updated in this way. CICO data is also sent by that means from the terminal to the central system. In the case of mobile devices and devices in vehicles, longer intervals may lapse between connections, and data may be exchanged using physical data carriers.

Since the terminals are connected only temporarily to the backend system, all of the functions required to communicate with the carrier medium and application must be supported locally in the terminal. This can mean considerable expense when introducing new technologies. It is therefore sensible, when defining applications, to base communication protocols, cryptographic methods etc. on open, standardised processes and to rely on flexible, hardware-independent methods of implementation.

As well as the application-specific functions, all of the information specific to particular events that is required to evaluate the entitlement must be stored locally in the terminal (service provider ID, blacklists, carrier medium ID, application ID, product IP, various levels of keys, and so on). It must also be possible to store the access history temporarily in the terminal.

The security-related safeguards for the reader incorporated into the terminal are detailed in Section [10.1.3.2](#page-114-1).

We can differentiate between permanently installed and mobile devices.

1 Permanently installed devices

Some CICO terminals are installed permanently on platforms or at tram or bus stops. These devices are usually connected to the central verification system via a LAN.

Some European cities utilise permanent turnstiles to regulate access to the platform. These turnstiles have terminals with readers integrated into them, and are connected to the central verification system via a LAN. Once the entitlement has been evaluated successfully, access is granted by unlocking the turnstile and allowing it to rotate. The turnstiles are situated at the entrances to the platform.

- 2 Mobile devices
	- a Mobile terminals

<span id="page-121-0"></span>Some CICO terminals are installed in vehicles. These devices can only exchange data with the central verification system temporarily. They are equipped with service provider SAMs.

b Monitoring units

There are also portable inspection units used by conductors and similar personnel to inspect tickets and also for sales purposes. These must also be fully operational when offline. They are fitted with personaliser SAMs and service provider SAMs.

#### **10.1.4.5 Service desks**

In real-life operation, a certain amount of defective customer media, incorrect operations, attacks on security and fraud attempts is inevitable. The service desk is the point of contact if problems occur when checking in.

Valid entitlements do not expire when the inspection equipment or customer medium fails, or if the customer does something incorrect. At the service desk, which is run by the service provider or product provider, the customer can receive a replacement entitlement or a refund.

For this to happen it must be possible to perform Process P4, "Blocking entitlements and carrier media", and to issue a replacement medium, quickly and efficiently.

The following tasks are undertaken at the service desk:

- 1 Check the function of the carrier medium and the status of the entitlement.
- If a fault occurs, then:

2 Check whether the medium is genuine and/or check the identity of the customer. If positive, then:

- 3 Block the medium and entitlement presented.
- 4 Issue a replacement medium with a new entitlement.
- 5 Update the information in the ticket system and the carrier and application management systems.
- 6 Transfer the information from the ticket system to the verification system.

Emergency scenarios for a verification system that uses access barriers malfunctions are based on the personnel who keep order, and the service desk. Both are therefore of key importance to system security. If an attacker succeeds in causing a malfunction which overburdens the personnel and the service desk, it is equivalent to a successful DoS attack on the entire verification system.

#### **10.1.4.6 Management system for carrier media and applications**

For the processes of loading applications and entitlements, and for the processes in which the customer medium is used for identification and for utilising transport services, it is important to know the status of the carrier medium and the applications on it.

For this reason, the life-cycle of any carrier medium used in the system must be documented reliably. To this end a database is used which is connected via interfaces to the ticket system and the key management system. It contains information such as the following for every carrier medium:

- ID of carrier medium
- Type, version
- Provider of carrier medium (ID via registrar)
- <span id="page-122-0"></span>• Issuer of carrier medium (ID via registrar)
- Customer
- Status (e.g. new/active/blocked)
- Stored applications (see below)
- etc.

Similarly, the life-cycle of the applications stored on the carrier medium must also be documented. Several different applications can be stored.

- ID of application
- Type, version
- Application provider (ID via registrar)
- Application issuer (ID via registrar)
- Customer
- Status (e.g. new/active/blocked/delete)
- Stored entitlements including ID of product provider
- Active entitlements / deletable entitlements

#### **10.1.4.7 Threats relevant to sale, inspection and management systems**

The following threats relevant to the interfaces of the system as a whole can be deduced from the assumptions used to determine the protection demand in Section [10.1.1.](#page-106-1)

| Threats to the sales, inspec<br>tion and management sys<br>tems |                                                    | Protection<br>demand | Comments                                                                                                                                                                                                                                                                   |
|-----------------------------------------------------------------|----------------------------------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TS1                                                             | Lack of fallback<br>solution                       | 3                    | The lack of a fallback solution when system<br>components fail, such as the ticket sales sys<br>tem, administration system for carrier media<br>and entitlements, or verification system, can<br>lead to a complete breakdown of services<br>(sales, invoicing, CICO, etc) |
| TS2                                                             | Unauthorised<br>scanning of refer<br>ence data     | 3                    | The background systems store information<br>about the media, entitlements and usage, and<br>sometimes personal data and calculation data.<br>The retrieval of this data by unauthorised per<br>sons would discredit the system and enable<br>attacks.                      |
| TS3                                                             | Manipulation of<br>reference data in<br>the system | 3                    | The background systems store information<br>about the media, entitlements and usage, and<br>sometimes personal data and calculation data.<br>The manipulation of this data by unauthorised<br>persons represents a serious threat.                                         |
| TS4                                                             | System malfunction                                 | 3                    | Individual system component malfunctions can<br>be caused in a range of scenarios by technical<br>faults, incorrect operation or DoS attacks:<br>1<br>Fault in local and central systems<br>2<br>Lack of availability of local and central<br>systems                      |

<span id="page-123-0"></span>

| Threats to the sales, inspec<br>tion and management sys<br>tems |                                                                                    | Protection<br>demand | Comments                                                                                                                                                                                                                                                                         |
|-----------------------------------------------------------------|------------------------------------------------------------------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                 |                                                                                    |                      | 3<br>Fault in data storage<br>4<br>Fault in power supply<br>5<br>Interruption of the link to the central sys<br>tem<br>6<br>Protection against physical attacks (dis<br>mantling, destruction)                                                                                   |
| TS5                                                             | Lack of compatibil<br>ity between inter<br>faces                                   | 3                    | A lack of compatibility between interfaces<br>causes malfunctions. The result is similar to a<br>DoS attack on the system. Many customers<br>and/or entitlements may be affected.                                                                                                |
| TS6                                                             | Unauthorised<br>scanning of sales<br>and calculation<br>data                       | 3                    | Unauthorised, active retrieval of calculation<br>data                                                                                                                                                                                                                            |
| TS7                                                             | Unauthorised<br>overwriting / ma<br>nipulation of sales<br>and calculation<br>data | 3                    | Unauthorised writing of calculation data onto<br>the carrier medium for the purpose of manipu<br>lating or compromising data.                                                                                                                                                    |
| TS8                                                             | Protection of client<br>specific applica<br>tions and entitle<br>ments             | 3                    | If multiple entities are supported by the system<br>with sales data, entitlements and applications,<br>these may be influenced or damaged when<br>used mutually.                                                                                                                 |
| TS9                                                             | Falsification of<br>identity data                                                  | 2                    | The customer may need to be identified when<br>setting up a customer account, or purchasing<br>or collecting a product. Using a false identity<br>would allow someone to obtain benefits such<br>as entitlements to the detriment of other cus<br>tomers or the product provider |
|                                                                 |                                                                                    |                      | The protection demand relating to protection of<br>entitlements is categorised as 2 in this case,<br>since attacks only affect individual entitle<br>ments.                                                                                                                      |
| TS10                                                            | Unjustified gather<br>ing and storing of<br>data                                   | 3                    | Gathering and storing data without justification<br>infringes the stipulation on data minimization.                                                                                                                                                                              |

### **Table 10–8 Threats relevant to sales, inspection and management systems**

### **10.1.4.8 Definition of safeguards for sale, inspection and management systems**

Based on the relevant threats in the preceding section, this section defines general execution proposals and safeguards. These safeguards are described in detail in Section [8.4](#page-66-1).

<span id="page-124-0"></span>

| Threat |                                                    | Safeguard       | Safeguard                                                                                                                                                   |  |
|--------|----------------------------------------------------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| TS1    | Lack of fallback<br>solution                       | MS4.3           | 1<br>Definition of a fallback solution in the<br>event of system interface or system<br>component failure – Implementation<br>according to fallback concept |  |
| TS2    | Unauthorised<br>scanning of refer<br>ence data     | MS5.3           | 1<br>Securing the confidentiality of data                                                                                                                   |  |
|        |                                                    | MS6.3           | when communicating within the system<br>– Secure communication channel                                                                                      |  |
|        |                                                    | MS15.3          | 2<br>Confidential storage of data – Introduc<br>tion of multi-tenant access protection,<br>role model                                                       |  |
|        |                                                    |                 | 3<br>Separation of applications – Separate<br>storing and processing of data                                                                                |  |
| TS3    | Manipulation of<br>reference data in<br>the system | MS6.3           | 1<br>Confidential storage of data – Maintain<br>ing privacy using multi-tenant access                                                                       |  |
|        |                                                    | MS7.3           | protection, role model                                                                                                                                      |  |
|        |                                                    | MS8.3           | 2<br>Securing the data integrity in order to<br>protect against manipulation when                                                                           |  |
|        |                                                    | MS15.3          | transmitting data within the system –<br>MAC or signatures                                                                                                  |  |
|        |                                                    |                 | 3<br>Securing data integrity when storing<br>data – Checksums                                                                                               |  |
|        |                                                    |                 | 4<br>Separation of applications – Separate<br>storing and processing of data                                                                                |  |
| TS4    | System malfunc<br>tion                             | MS4.3           | 1<br>Definition of a fallback solution in the                                                                                                               |  |
|        |                                                    | MS9.3           | event of system interface or system<br>component failure – Implementation                                                                                   |  |
|        |                                                    | MS10.3          | according to fallback concept<br>2<br>Securing system functions against DOS                                                                                 |  |
|        |                                                    | MS11.3          | attacks to the interfaces – Security con<br>cept                                                                                                            |  |
|        |                                                    | MS13.3          | 3<br>Securing the function of the system                                                                                                                    |  |
|        |                                                    | MS14.3          | against incorrect operation by employ<br>ees and users – Tests, personnel and<br>user introductions.                                                        |  |
|        |                                                    |                 | 4<br>Secure the function of the system to<br>prevent the technical failure of compo<br>nents and transmission routes –<br>Evaluation of components          |  |
|        |                                                    |                 | 5<br>Ergonomic user instructions                                                                                                                            |  |
|        |                                                    |                 | 6<br>Support – System-wide support                                                                                                                          |  |
| TS5    | Lack of compati<br>bility between<br>interfaces    | MS1.3<br>MS11.3 | 1<br>Introduction of interface tests and ap<br>proval procedures – Certification                                                                            |  |
|        |                                                    | MS12.3          | 2<br>Secure the function of the system to<br>prevent the technical failure of compo                                                                         |  |
|        |                                                    |                 | nents and transmission routes –<br>Evaluation of components                                                                                                 |  |
|        |                                                    |                 | 3<br>Specifications for system concept and<br>requirements for components with the<br>aim of integration and interoperability –                             |  |

<span id="page-125-0"></span>

| Threat |                                                                                    | Safeguard                         | Safeguard                                                                                                                                                                                                                                                                                                                                                                                                                   |  |
|--------|------------------------------------------------------------------------------------|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
|        |                                                                                    |                                   | interoperability tests in accordance with<br>test concept, evaluation                                                                                                                                                                                                                                                                                                                                                       |  |
| TS6    | Unauthorised<br>scanning of sales<br>and calculation<br>data                       | MS5.3<br>MS6.3<br>MS15.3          | 1<br>Securing the confidentiality of data<br>when communicating within the system<br>– VPN or similar<br>2<br>Confidential storage of data – Introduc<br>tion of multi-tenant access protection in<br>accordance with role model<br>3<br>Separation of applications – Separate<br>storing and processing of data                                                                                                            |  |
| TS7    | Unauthorised<br>overwriting / ma<br>nipulation of sales<br>and calculation<br>data | MS6.3<br>MS7.3<br>MS8.3<br>MS15.3 | 1<br>Confidential storage of data – Introduc<br>tion of multi-tenant access protection in<br>accordance with role model<br>2<br>Securing the data integrity in order to<br>protect against manipulation when<br>transmitting data within the system –<br>MAC or signatures<br>3<br>Securing data integrity when storing<br>data – Checksums<br>4<br>Separation of applications – Separate<br>storing and processing of data |  |
| TS8    | Protection of cli<br>ent-specific appli<br>cations and enti<br>tlements            | MS6.3<br>MS15.3                   | 1<br>Confidential storage of data – Maintain<br>ing privacy using multi-tenant access<br>protection, role model<br>2<br>Separation of applications – Separate<br>storing and processing of data                                                                                                                                                                                                                             |  |
| TS9    | Falsification of<br>identity data                                                  | MS16.2                            | 1<br>Customer identification – Application<br>form, customer medium                                                                                                                                                                                                                                                                                                                                                         |  |
| TS10   | Unjustified gath<br>ering and storing<br>of data                                   | MS17.3                            | 1<br>Gathering and storing data without justi<br>fication infringes the stipulation on data<br>minimization.                                                                                                                                                                                                                                                                                                                |  |

**Table 10–9 Safeguards for sale, inspection and management systems** 

### **10.1.4.9 Residual risks**

For technical and commercial reasons, it is not always possible to eliminate threats completely using safeguards. In such cases a certain risk remains.

The residual risk should be determined and documented as part of the planning of the actual implementation.

## **10.1.5 Key management**

The job of the key management system is to provide keys used by multiple entities for all of the carrier media, applications and products in the system, and to do so securely and reliably. Key management is the responsibility of the security manager. A number of use cases are described in Section [7.3](#page-41-2). [GSHB] can be used as a general guideline for implementation. <span id="page-126-0"></span>Keys are generated individually for each purpose. As far as possible, a distinct key is allocated to each form of interaction (e.g. loading applications, writing entitlements, reading entitlements, writing usage data). The precise characteristics have to be ascertained for each application scenario as part of the creation of a specific security concept that harmonises with the role model.

The keys are generated in a secure environment and stored in a secure database. The various forms of SAM are also produced in this secure environment. The documentation of the life-cycle of the SAMs that are produced and issued is another of the key management system's tasks.

The SAMs and keys are generated by the security manager or his agents as and when users need them. The following types of SAM are basically supported:

| Initialiser SAMs      | Initialiser SAMs are required to initialise carrier media and load<br>applications.                                                                                 |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Personaliser SAMs     | Personaliser SAMs are required to load entitlements in the ap<br>propriate applications.                                                                            |
| Service provider SAMs | Service provider SAMs are required by the service provider to<br>read and activate entitlements, and in some cases to send the<br>usage data to the carrier medium. |

Where required there may also be special SAMs that help transmit the product ID of the suppliers of carrier media, applications and entitlements securely onto the carrier medium.

Key information is normally loaded onto a SAM when the user requires it. The aim of an initialiser is, for example, to enable all of the carrier media that occur in its area to be initialised with the necessary applications without changing the SAM.

This kind of user-specific SAM must be configured under an agreement between the user of the SAM and the system manager.

The SAM should support the secure loading of new keys via a network. Ideally, updating can be done by the security manager directly.

#### **10.1.5.1 Key management for public transport service providers / SAMs for service providers**

Specific key information is required to evaluate entitlements. The reliability and security of the key management system involved in this is of critical importance to the overall concept. If the keys held by the service provider do not correspond with those in the carrier media and entitlements used for entry, then the evaluation of entitlements will not work. If keys are lost or made public, then the entire security concept will be discredited.

In this proposal, special SAMs are issued to the service provider as the operator of the verification system. These service provider SAMs contain the key information relevant to the services offered, and must be integrated into the terminals.

When service provider SAMs are used key management is restricted to the handing-over, handling and management of the SAMs. Since the keys are protected against unauthorized reading when using SAMs, the risk – and therefore the extent of the protection required – is limited. The use of standardised SAMs also reduces the expense of adapting to new applications.

### <span id="page-127-0"></span>**10.1.5.2 Threats relevant to the key management system**

The following threats relevant to the interfaces of the system as a whole can be deduced from the assumptions used to determine the protection demand in Section [10.1.1.](#page-106-1)

| Threats to the key man<br>agement system |                                         | Protection<br>demand | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |
|------------------------------------------|-----------------------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| TK1                                      | Lack of key data<br>quality             | 3                    | Deficient key quality increases the chances of<br>successful attacks.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |
| TK2                                      | Unauthorised<br>scanning of key<br>data | 3                    | The retrieval of key data by unauthorised per<br>sons can discredit the system and facilitate<br>attacks, e.g. on any cryptographically protected<br>data or functions.                                                                                                                                                                                                                                                                                                                                                    |  |
| TK3                                      | Manipulation of key<br>data             | 3                    | The manipulation of key data can discredit the<br>system's security concept and facilitate at<br>tacks, e.g. on any cryptographically protected<br>data or functions. Manipulation can affect the<br>generation of keys, the production of key<br>carriers, the transmission of keys and the local<br>use of keys.                                                                                                                                                                                                         |  |
| TK4                                      | Key management<br>system malfunction    | 3                    | Key management system malfunctions can be<br>caused in a variety of scenarios by technical<br>faults, incorrect operation or DoS attacks:<br>1<br>Fault in local and central systems<br>2<br>Lack of availability of local and central<br>systems<br>3<br>Fault in data storage<br>4<br>Fault in specific application implementa<br>tion<br>5<br>Fault in evaluation algorithms for entitle<br>ments<br>6<br>Fault in power supply<br>7<br>Interruption of the link to the central sys<br>tem<br>8<br>Physical destruction |  |
| TK5                                      | Lack of fallback<br>solution            | 3                    | The availability of the necessary key informa<br>tion is essential if the system as a whole is to<br>work at all. If the key management system mal<br>functions and there is no fallback solution, the<br>function of the entire system will be threatened.                                                                                                                                                                                                                                                                |  |

### **Table 10–10 Threats relevant to the key management system**

### **10.1.5.3 Definition of safeguards for the key management system**

Based on the relevant threats in the preceding section, this section defines general execution proposals and safeguards. These safeguards are described in detail in Section [8.4](#page-66-1).

<span id="page-128-0"></span>

| Threat |                                          | Safeguard               | Safeguard                                                                                                                                                                                                                                                                                                                                                         |  |
|--------|------------------------------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| TK1    | Lack of key data<br>quality              | MK1.3<br>MK2.3          | 1<br>Secure generation and import of keys –<br>Evaluation and certification according to<br>CC or a process of the same standard<br>2<br>Introduction of key management for<br>symmetric and asymmetric keys with<br>sufficient key length – Secure, flexible<br>key management concept                                                                           |  |
| TK2    | Unauthorised<br>scanning of key<br>data  | MK3.3<br>MK7.3          | 1<br>Access protection for cryptographic<br>keys (read and write access) – Evalua<br>tion and certification according to CC or<br>a process of the same standard<br>2<br>Separation of keys – Separate storage<br>and handling of keys                                                                                                                            |  |
| TK3    | Manipulation of<br>key data              | MK3.3<br>MK7.3<br>MK8.3 | 1<br>Access protection for cryptographic<br>keys (read and write access) – Evalua<br>tion and certification according to CC or<br>a process of the same standard<br>2<br>Separation of keys – Separate storage<br>and handling of keys<br>3<br>Loading new keys – Securing the au<br>thenticity and integrity of entitlements –<br>Complex authentication concept |  |
| TK4    | Key management<br>system malfunc<br>tion | MK4.3<br>MK5.3          | 1<br>Specification of performance and the<br>required securing of the function of se<br>curity components – Evaluation<br>2<br>Availability of key management system<br>(fallback solution) – Implementation ac<br>cording to fallback concept and back-up<br>of keys in Trust Centre                                                                             |  |
| TK5    | Lack of fallback<br>solution             | MK5.3<br>MK6.3          | 1<br>Availability of key management system<br>(fallback solution) – Implementation ac<br>cording to fallback concept and back-up<br>of keys in Trust Centre<br>2<br>Definition of actions in the event of keys<br>being compromised – Compromise of<br>non-diversified keys                                                                                       |  |

| Table 10–11 | Safeguards for the key management system |
|-------------|------------------------------------------|
|-------------|------------------------------------------|

### **10.1.5.4 Residual risks**

For technical and commercial reasons, it is not always possible to eliminate threats completely using safeguards. In such cases a certain risk remains.

The residual risk should be determined and documented as part of the planning of the actual implementation.

# <span id="page-129-1"></span><span id="page-129-0"></span>**10.2 Suggestions on executing the carrier media**

The diverse products involved in eTicketing for public transport can be offered on a variety of carrier media. Furthermore, a range of different chips are available for these carrier media.

|  |  | The following two tables categorise the carrier media and chip products. |
|--|--|--------------------------------------------------------------------------|
|  |  |                                                                          |

| Category                                                    | Characteristics of the carrier<br>medium                                                                                                                                                                                                                                                                   | Security features of the card<br>itself                                                                                                                                                                                                                                                                                 | Matching<br>chip<br>category                                                      |
|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Contact<br>less<br>Smart<br>Ticket                          | •<br>Multi-layered, laminated<br>paper ticket. Choice of for<br>mats: IATA, ID1, etc with<br>ID1 antenna<br>•<br>Cost: < €0.20 not including<br>chip<br>•<br>Typical useful life: approx. 3<br>months                                                                                                      | •<br>Simple visual security fea<br>tures such as security fi<br>bres, fluorescent inks for<br>access control<br>•<br>Visual personalisation<br>•<br>Option: tear off to activate<br>manually as a fallback solu<br>tion                                                                                                 | Low-cost<br>memory<br>chip,<br>conven<br>tional<br>memory<br>chip                 |
| Contact<br>less se<br>cure chip<br>card                     | •<br>Contact-less PVC chip card.<br>Choice of formats: normally<br>ID1 with ID1 antenna<br>•<br>Cost: < €1 not including<br>chip<br>•<br>Typical useful life: approx. 3<br>years                                                                                                                           | •<br>More advanced visual secu<br>rity features such as holo<br>grams and microprint;<br>•<br>Visual personalisation<br>•<br>Visible activation not possi<br>ble, since used more than<br>once                                                                                                                          | Secure,<br>flexible<br>memory<br>chip                                             |
| Contact<br>less se<br>cure<br>multi<br>applica<br>tion card | •<br>Contact-less PVC or PC<br>chip card. Choice of for<br>mats: normally ID1, ID1 an<br>tenna<br>•<br>Cost:<br>•<br>< €1 not including chip for<br>standard design, or < €3 not<br>including chip for card with<br>high-level visual security<br>features<br>•<br>Typical useful life: approx. 3<br>years | •<br>The actual card can be like<br>the "Contact-less secure<br>chip card" or a high-quality<br>card (e.g. PC) with visual<br>security features (e.g. guil<br>loche, OVI, embossing).<br>•<br>Visual personalisation<br>•<br>Optional display<br>•<br>Visible activation not possi<br>ble, since used more than<br>once | Secure<br>controller<br>chip with<br>operating<br>and ap<br>plication<br>software |

<span id="page-130-0"></span>

| Category                  | Characteristics of the carrier<br>medium                                                                                                                                                                                                                                                   | Security features of the card<br>itself                                                                                                                                                                 | Matching<br>chip<br>category                                                      |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| NFC mo<br>bile de<br>vice | •<br>Mobile device with NFC<br>interface:<br>•<br>Display (shows relevant<br>information)<br>•<br>Keyboard<br>•<br>User can modify application<br>data<br>•<br>Over-the-air application<br>management (loading, per<br>sonalising, deleting, version<br>management) by service<br>provider | •<br>Contact-less interface can<br>be switched on and off by<br>user<br>•<br>SIM card used for identifica<br>tion and authentication<br>•<br>Service provider can block<br>the application over-the-air | Secure<br>controller<br>chip with<br>operating<br>and ap<br>plication<br>software |

### **Table 10–12 Categorisations of carrier media**

Chip products in the following categories can be used in the carrier media listed above:

| Chip category<br>Security features |                                                                                                                                                                                                                                                                                             | Functions                                                                                                                                                                                                                                                          | Commercial aspects                                                                                                                                                                                                                                                                                                    |  |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| Low-cost<br>memory chip            | •<br>Unique identifier<br>(UID)<br>•<br>OTP memory<br>•<br>Write protection in<br>certain areas of<br>memory<br>•<br>Access protection<br>for certain areas of<br>memory                                                                                                                    | •<br>Interface as de<br>fined by ISO14443<br>Parts 1-3<br>•<br>Unique identifier<br>(UID)<br>•<br>Read/write area<br>organised in fixed<br>blocks. Total <<br>1 kByte<br>•<br>Data stored for<br>max. 2 years                                                      | •<br>Chip cost < €0.50<br>•<br>Proprietary inter<br>face and applica<br>tion commands ><br>reader may re<br>quire adjustment<br>•<br>Proprietary, fixed<br>memory divisions<br>> adjustment may<br>be necessary for<br>entitlements.<br>•<br>Minimal time re<br>quired for initialisa<br>tion and personal<br>isation |  |
| Secure mem<br>ory chip             | •<br>Unique identifier<br>(UID)<br>•<br>Symmetric cryp<br>tography (TDES,<br>AES).<br>•<br>Mutual authenti<br>cate<br>•<br>Secure communi<br>cation (protected<br>by MAC and/or<br>encrypted)<br>•<br>Access protection,<br>individual protec<br>tion for particular<br>files and file sys- | •<br>Interface as de<br>fined by ISO14443<br>Parts 1-4<br>•<br>Data secured<br>when transmitted<br>via contact-less in<br>terface<br>•<br>Read/write area 1<br>kB – 8 kB<br>•<br>Flexible file han<br>dling<br>•<br>Fixed command<br>set with high per<br>formance | •<br>Chip cost < 1 €<br>•<br>Proprietary appli<br>cation commands<br>> reader may re<br>quire adjustment<br>•<br>Flexible file for<br>mats > enable<br>standardised for<br>mats for entitle<br>ments.<br>•<br>Moderate amount<br>of time required for<br>initialisation and<br>personalisation                        |  |

<span id="page-131-0"></span>

| Chip category                          | Security features                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Commercial aspects                                                                                                                                                                                                                                                                                      |  |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
|                                        | tems                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | •<br>Multi-application<br>•<br>Data stored for<br>min. 10 years                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                         |  |
| Secure con<br>troller chip<br>with COS | •<br>Unique identifier<br>(UID)<br>•<br>Random UID<br>•<br>Symmetric cryp<br>tography (TDES,<br>AES)<br>•<br>Asymmetric cryp<br>tography (RSA,<br>ECC)<br>•<br>Mutual authenti<br>cate<br>•<br>Secure communi<br>cation (protected<br>by MAC and/or<br>encrypted)<br>•<br>Access protection,<br>individual protec<br>tion for particular<br>files and file sys<br>tems<br>•<br>Sensors protect<br>against hardware<br>attacks<br>•<br>Secure hardware<br>design<br>•<br>CC EAL5+ – certi<br>fication of chip<br>hardware in ac<br>cordance with<br>[PP_HW1],<br>[PP_HW2] or<br>comparable speci<br>fications. | •<br>Interface as de<br>fined by ISO14443<br>Parts 1-4<br>•<br>Unique identifier<br>(UID)<br>•<br>Read/write area<br>approx. 10 kB –<br>150 kB<br>•<br>Flexible file han<br>dling<br>•<br>COS/application<br>software in ROM<br>or EEPROM<br>•<br>Command set can<br>be defined with<br>COS<br>•<br>Multi-application,<br>including secure<br>loading of applica<br>tions in the field<br>(e.g. as defined by<br>[ISO 7816-13])<br>•<br>Data stored for<br>min. 10 years | •<br>Chip cost < €3 (not<br>including software<br>licensing costs)<br>•<br>Cost of COS and<br>application soft<br>ware<br>•<br>Command set<br>defined by COS,<br>allows flexibility<br>•<br>Flexible memory<br>division<br>•<br>High initial ex<br>pense for initialisa<br>tion and personal<br>isation |  |

**Table 10–13 Categorisations of chip products** 

### **10.2.1 Initialising carrier media and applications**

The initialisation of carrier media is by Process P2 and the use cases described in Sections [7.2](#page-40-2), [7.3](#page-41-2) and [7.10.2.](#page-48-2) There are different ways of facilitating this:

- 1 Initialisation by a special service provider. This is used particularly in cases where large numbers of chip cards are issued.
- 2 Initialisation controlled from the ticket system, in vending machines or ticket printers.
- 3 Applications are loaded onto existing customer media under the management of the ticket system.

<span id="page-132-0"></span>The actual procedures and processes have to be implemented in the initialisation systems in accordance with the specifications of the carrier medium and the applications. Initialiser SAMs are often used for key management, and these have to be integrated into the initialisation system.

### **10.2.2 Personalising carrier media and applications**

Loading entitlements is by Process P2 and the use cases described in Sections [7.4](#page-42-2) and [7.10.3.](#page-49-2) There are different ways of facilitating this:

- 1 The entitlement is loaded by a special service provider during the initialisation process. This is used particularly in cases where large numbers of chip cards are issued.
- 2 Entitlement loading in vending machines or ticket printers, controlled from the ticket system.
- 3 Entitlements are loaded onto existing applications and customer media under the management of the ticket system.

The actual procedures and processes have to be implemented in the personalisation systems in accordance with the specifications of the carrier medium and the applications. Initialiser SAMs are used for key management, and these have to be integrated into the personalisation system.

### **10.2.3 Determining the protection demand for the carrier media**

The choice of protection demand category is dependent on the application scenario, so it will be dealt with in Chapter [11.](#page-134-1)

### **10.2.4 Threats to the carrier medium**

The following table lists the threats to the carrier medium. The allocation of protection categories is highly dependent on the product being supported, and therefore on the application scenario concerned, so it will be dealt with in Chapter [11](#page-134-1).

|        |                                                                                         | Carrier medium  |                        |                               |                         |                                          |
|--------|-----------------------------------------------------------------------------------------|-----------------|------------------------|-------------------------------|-------------------------|------------------------------------------|
| Threat |                                                                                         | Smart<br>Ticket | Secure<br>chip<br>card | Multi<br>applica<br>tion card | NFC<br>mobile<br>device | Comments                                 |
| TC1    | Lack of compatibility<br>between the inter<br>faces of the carrier<br>medium and reader | 1               | 1                      | 1                             | 1                       |                                          |
| TC2    | Eavesdropping                                                                           |                 |                        |                               |                         | Dependent on<br>application sce<br>nario |
| TM1    | Unauthorised scan<br>ning of entitlement                                                |                 |                        |                               |                         | Dependent on<br>application sce<br>nario |
| TM2    | Unauthorised over<br>writing / manipulation                                             |                 |                        |                               |                         | Dependent on<br>application sce          |

<span id="page-133-0"></span>

|        |                                                                    | Carrier medium  |                        |                               |                         |                                          |
|--------|--------------------------------------------------------------------|-----------------|------------------------|-------------------------------|-------------------------|------------------------------------------|
| Threat |                                                                    | Smart<br>Ticket | Secure<br>chip<br>card | Multi<br>applica<br>tion card | NFC<br>mobile<br>device | Comments                                 |
|        | of entitlement                                                     |                 |                        |                               |                         | nario                                    |
| TM3    | Cloning of medium<br>including entitlement                         |                 |                        |                               |                         | Dependent on<br>application sce<br>nario |
| TM4    | Emulation of applica<br>tion or entitlement                        |                 |                        |                               |                         | Dependent on<br>application sce<br>nario |
| TM5    | Unauthorised scan<br>ning of personal data                         |                 |                        |                               |                         | Dependent on<br>application sce<br>nario |
| TM6    | Unauthorised over<br>writing / manipulation<br>of personal data    |                 |                        |                               |                         | Dependent on<br>application sce<br>nario |
| TM7    | Unauthorised scan<br>ning of calculation<br>data                   |                 |                        |                               |                         | Dependent on<br>application sce<br>nario |
| TM8    | Unauthorised over<br>writing / manipulation<br>of calculation data |                 |                        |                               |                         | Dependent on<br>application sce<br>nario |
| TM9    | Protection of addi<br>tional applications<br>and entitlements      |                 |                        |                               |                         | Dependent on<br>application sce<br>nario |
| TM10   | Carrier medium mal<br>function                                     |                 |                        |                               |                         | Dependent on<br>application sce<br>nario |
| TM11   | Tracking by means of<br>unauthorised scan<br>ning of UID           | 1               | 1                      | 1                             | 1                       |                                          |
| TM12   | Lack of fallback solu<br>tion in the event of<br>malfunction       |                 |                        |                               |                         | Dependent on<br>application sce<br>nario |

**Table 10–14 Threats relevant to the carrier medium** 

### **10.2.5 Definition of specific safeguards**

The allocation of safeguards is dependent on the application scenario, so it will be dealt with in Chapter [11.](#page-134-1)

# <span id="page-134-1"></span><span id="page-134-0"></span>**11 Suggestions on executing the product-specific application scenarios**

# **11.1 The "Local multi-journey entitlement" application scenario**

### **11.1.1 Determining the protection demand category**

The following conditions apply to the "Local multi-journey entitlement" application scenario and must be taken into consideration when determining the protection demand:

- 1 Low commercial value (< €20)
- 2 No personal data
- 3 No usage data
- 4 No calculation data
- 5 These entitlements are used more than once, and the medium is carried around between uses.
- 6 They may be combined with other application scenarios and products. The product can be combined with higher-value products in the same application area. When determining the protection demand it must be borne in mind that this scenario may endanger other products with a higher value.

For reasons of minimization, it is usually only the Smart Ticket which can be produced specially for this product and issued with an entitlement. In the case of all other carrier media, only the loading of the application and entitlement onto an existing customer medium is advisable, for reasons of cost. Only these cases will be examined in further detail in the following.

On the basis of the criteria discussed in Section [8.2.5](#page-59-1), the application scenario can be allocated to the following protection demand categories:

| Security target |                                                          | Protection<br>demand<br>category | Criteria for allocating to protection demand category                                                                                                        |  |  |
|-----------------|----------------------------------------------------------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
| SS1             | Technical<br>compatibility                               | 1                                | All of the system components are from the same sup<br>plier. The supplier ensures that they are compatible.                                                  |  |  |
|                 |                                                          | 2                                | The system has to function with components from a<br>small number of defined suppliers. The system man<br>ager or a system integrator ensures compatibility. |  |  |
|                 |                                                          | 3                                | Open system that has to function with components<br>from any company in the market.                                                                          |  |  |
|                 |                                                          |                                  | System and carrier media are normally acquired by<br>offering out for public tender.                                                                         |  |  |
| SS2             | Fallback solu<br>tion in the<br>event of mal<br>function |                                  | Malfunction affects only a few customers.                                                                                                                    |  |  |
|                 |                                                          | 1                                | Malfunctions of a large number of media are not to be<br>expected. It is assumed that the system will remain                                                 |  |  |

<span id="page-135-0"></span>

| Security target |                                                                | Protection<br>demand<br>category | Criteria for allocating to protection demand category                                                                                                                                  |  |  |  |
|-----------------|----------------------------------------------------------------|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|
|                 |                                                                |                                  | sufficiently available.                                                                                                                                                                |  |  |  |
|                 |                                                                | 2                                | Malfunction affects many customers.                                                                                                                                                    |  |  |  |
|                 |                                                                | 3                                | Malfunction affects a large proportion of customers.                                                                                                                                   |  |  |  |
|                 | Intuitive, fault                                               | 1                                | A few customers cannot operate it intuitively.                                                                                                                                         |  |  |  |
|                 |                                                                |                                  | Only activation is necessary.                                                                                                                                                          |  |  |  |
| SS3             | tolerant op<br>eration                                         | 2                                | Many customers cannot operate it intuitively.                                                                                                                                          |  |  |  |
|                 |                                                                | 3                                | A large proportion of customers cannot operate it intui<br>tively.                                                                                                                     |  |  |  |
|                 | Protection of                                                  | 1                                | Not relevant. No personal data.                                                                                                                                                        |  |  |  |
| SI1             | personal data<br>(including                                    | 2                                |                                                                                                                                                                                        |  |  |  |
|                 | personal us<br>age data)                                       | 3                                |                                                                                                                                                                                        |  |  |  |
| SI2             | Protection of<br>entitlements                                  |                                  | Predicted product-related loss of sales through coun<br>terfeiting, damage or manipulation <1%                                                                                         |  |  |  |
|                 |                                                                | 1                                | From the point of view of an attacker, the expense of<br>counterfeiting must be well below the value of the enti<br>tlement (< €20). This can be prevented using simple<br>safeguards. |  |  |  |
|                 |                                                                | 2                                | Predicted product-related loss of sales through coun<br>terfeiting, damage or manipulation <3%                                                                                         |  |  |  |
|                 |                                                                | 3                                | Predicted product-related loss of sales through coun<br>terfeiting, damage or manipulation >3%                                                                                         |  |  |  |
|                 | Protection of<br>logistical data<br>(anonymised<br>usage data) | 1                                | Not relevant. No usage data.                                                                                                                                                           |  |  |  |
| SI3             |                                                                | 2                                |                                                                                                                                                                                        |  |  |  |
|                 |                                                                | 3                                |                                                                                                                                                                                        |  |  |  |
|                 | Reliable in<br>voicing (per<br>sonalised)                      | 1                                | Not relevant. No calculation data.                                                                                                                                                     |  |  |  |
| SI4             |                                                                | 2                                |                                                                                                                                                                                        |  |  |  |
|                 |                                                                | 3                                |                                                                                                                                                                                        |  |  |  |
|                 | Protection of<br>applications<br>and entitle<br>ments          | 1                                | Applications are issued by the same application issuer<br>and entitlements by the same product owner.                                                                                  |  |  |  |
| SI5             |                                                                | 2                                | Applications are issued by different application issuers<br>and entitlements by different product owners. The enti<br>ties trust one another.                                          |  |  |  |
|                 |                                                                | 3                                | Applications are issued by different application issuers<br>and entitlements by different product owners. The enti<br>ties do not trust one another.                                   |  |  |  |

<span id="page-136-0"></span>

| Security target |                                                                  | Protection<br>demand<br>category | Criteria for allocating to protection demand category                                                                                                                                      |  |  |
|-----------------|------------------------------------------------------------------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                 |                                                                  |                                  | When loading the entitlement onto multi-application<br>cards or NFC mobile devices, it must always be as<br>sumed that applications from other entities will be on<br>the customer medium. |  |  |
| SP3             | Data minimi<br>zation                                            | 1                                | Not relevant for the carrier medium.                                                                                                                                                       |  |  |
|                 |                                                                  | 2                                |                                                                                                                                                                                            |  |  |
|                 |                                                                  | 3                                |                                                                                                                                                                                            |  |  |
|                 | Protection<br>against the<br>creation of<br>movement<br>profiles | 1                                | Customer's reputation may be damaged, but nothing<br>more.                                                                                                                                 |  |  |
| SP4             |                                                                  | 2                                | Customer's social existence is damaged.                                                                                                                                                    |  |  |
|                 |                                                                  | 3                                | Customer's physical existence is damaged.                                                                                                                                                  |  |  |

**Table 11–1 Protection demand for the "Local multi-journey entitlement" application scenario** 

## **11.1.2 Relevant threats**

The following table lists the threats specific to this application scenario:

|        |                                                                                         | Carrier medium  |                        |                               |                         |                                                                              |
|--------|-----------------------------------------------------------------------------------------|-----------------|------------------------|-------------------------------|-------------------------|------------------------------------------------------------------------------|
| Threat |                                                                                         | Smart<br>Ticket | Secure<br>chip<br>card | Multi<br>applica<br>tion card | NFC<br>mobile<br>device | Comments                                                                     |
| TC1    | Lack of compatibility<br>between the inter<br>faces of the carrier<br>medium and reader | 3               | -                      | 3                             | 3                       |                                                                              |
| TC2    | Eavesdropping                                                                           | 1               | -                      | 1                             | 1                       |                                                                              |
| TM1    | Unauthorised scan<br>ning of entitlement                                                | 1               | -                      | 3                             | 3                       | Category 3 be<br>cause other<br>applications and<br>entitlements are<br>used |
| TM2    | Unauthorised over<br>writing / manipulation<br>of entitlement                           | 1               | -                      | 3                             | 3                       | Category 3 be<br>cause other<br>applications and<br>entitlements are<br>used |
| TM3    | Cloning of medium<br>including entitlement                                              | 1               | -                      | 3                             | 3                       | Category 3 be<br>cause other<br>applications and<br>entitlements are         |

<span id="page-137-0"></span>

| Threat |                                                                    | Carrier medium  |                        |                               |                         |                                                                              |
|--------|--------------------------------------------------------------------|-----------------|------------------------|-------------------------------|-------------------------|------------------------------------------------------------------------------|
|        |                                                                    | Smart<br>Ticket | Secure<br>chip<br>card | Multi<br>applica<br>tion card | NFC<br>mobile<br>device | Comments                                                                     |
|        |                                                                    |                 |                        |                               |                         | used                                                                         |
| TM4    | Emulation of applica<br>tion or entitlement                        | 1               |                        | 1                             | 1                       |                                                                              |
| TM5    | Unauthorised scan<br>ning of personal data                         | -               | -                      | -                             | -                       |                                                                              |
| TM6    | Unauthorised over<br>writing / manipulation<br>of personal data    | -               | -                      | -                             | -                       |                                                                              |
| TM7    | Unauthorised scan<br>ning of calculation<br>data                   | -               | -                      | -                             | -                       |                                                                              |
| TM8    | Unauthorised over<br>writing / manipulation<br>of calculation data | -               | -                      | -                             | -                       |                                                                              |
| TM9    | Protection of addi<br>tional applications<br>and entitlements      | -               | -                      | 3                             | 3                       | Category 3 be<br>cause other<br>applications and<br>entitlements are<br>used |
| TM10   | Carrier medium mal<br>function                                     | 1               | -                      | 1                             | 1                       |                                                                              |
| TM11   | Tracking by unauthor<br>ised scanning of UID                       | 1               | -                      | 1                             | 1                       |                                                                              |
| TM12   | Lack of fallback solu<br>tion in the event of<br>malfunction       | 1               | -                      | 1                             | 1                       |                                                                              |

**Table 11–2 Threats relevant to the "Local multi-journey entitlement" application scenario** 

### <span id="page-137-1"></span>**11.1.3 Definition of specific safeguards**

This section defines specific safeguards on the basis of the relevant threats described in the section above. The threats listed will be discussed for the following use cases:

|                                                    | Carrier medium  |                        |                               |                         |          |  |
|----------------------------------------------------|-----------------|------------------------|-------------------------------|-------------------------|----------|--|
| Use case                                           | Smart<br>Ticket | Secure<br>chip<br>card | Multi<br>applica<br>tion card | NFC<br>mobile<br>device | Comments |  |
| Identification when<br>registering and<br>ordering | -               | -                      | -                             | -                       |          |  |

<span id="page-138-0"></span>

|                                           | Carrier medium                    |                        |                               |                         |                                                                                                                           |
|-------------------------------------------|-----------------------------------|------------------------|-------------------------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Use case                                  | Smart<br>Ticket                   | Secure<br>chip<br>card | Multi<br>applica<br>tion card | NFC<br>mobile<br>device | Comments                                                                                                                  |
| Carrier medium<br>initialisation          | +                                 | -                      | -                             | -                       |                                                                                                                           |
| Post-issuance load<br>ing of application  | -                                 | -                      | +                             | +                       | Smart Ticket is produced<br>when the entitlement is<br>issued. With other media<br>the entitlement is loaded<br>on later. |
| Entitlement loading                       | +                                 | -                      | -                             | -                       |                                                                                                                           |
| Post-issuance load<br>ing of entitlements | -                                 | -                      | +                             | +                       |                                                                                                                           |
| Delivery                                  | +                                 | -                      | -                             | -                       |                                                                                                                           |
| Check-in                                  | Validation                        |                        |                               |                         |                                                                                                                           |
| Check-out                                 | Only in the case of exit barriers |                        |                               |                         |                                                                                                                           |
| Entitlement check                         | +                                 | -                      | +                             | +                       |                                                                                                                           |
| Blocking                                  | +                                 | -                      | +                             | +                       |                                                                                                                           |
| Key management                            | +                                 | -                      | +                             | +                       |                                                                                                                           |

#### **Table 11–3 Use cases relevant to the "Local multi-journey entitlement" application scenario**

The following sub-sections will define safeguards for each carrier medium, on the basis of the threats described and the relevant use cases.

### **11.1.3.1 Safeguards when utilising the "Smart Ticket" carrier medium**

### Conditions particular to this case

Entitlements of product type "Local multi-journey entitlement" are issued on carrier media of type "Smart Ticket". The carrier medium is initialised with an application which can contain one or more entitlements. The chip's security mechanisms are limited to the blocking of certain memory sectors and possibly simple access protection (see Section [10.2](#page-129-1)).

The initialisation of the carrier medium is done together with the personalisation of the entitlement in a mass personaliser, at the sales point or in a vending machine.

When using the entitlement, the customer must validate it before or straight after entering the vehicle. In systems with barriers, activation is upon entry. You also leave the blocked-off area using the carrier medium and the entitlement.

In the system as a whole, the "Local multi-journey entitlement" product is used together with higher-value products such as "automatic fare calculation". It must be ensured that attacks on these higher-value products are not made possible by means of attacks on the "Local multi-journey entitlement" product. This possibility can be discounted if the cost of cloning, counterfeiting or emulating a usable entitlement is greater than the purchase price. This

means there is a need to protect against counterfeiting, cloning and emulating, especially with the "Smart Ticket" carrier medium.

In this application scenario, customer media are allowed that potentially may enable entitlements to be emulated (NFC mobile device). This means there is a need to protect against emulation of the "Smart Ticket".

#### Definition of safeguards

In the following table, safeguards are assigned to the threats in [Table 11–2.](#page-137-1) These safeguards are intended to compensate for those threats. The safeguards are described in Section [8.4.](#page-66-1)

| Threat |                                                                                     | Safeguard      | Safeguard                                                                                                                                                                                                                              |  |
|--------|-------------------------------------------------------------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| TC1    | Lack of compati<br>bility between<br>interfaces in car<br>rier medium and<br>reader | MS1.3<br>MR1.3 | 1<br>Introduction of interface tests and ap<br>proval procedures – Certification                                                                                                                                                       |  |
| TC2    | Eavesdropping                                                                       | MS2.1<br>MS3.1 | 1<br>Ensuring the confidentiality of commu<br>nication between carrier medium and<br>reader in order to prevent eavesdrop<br>ping – Transmission security<br>2<br>Introduction of contact-less interface as<br>defined by ISO/IEC14443 |  |
| TM1    | Unauthorised<br>scanning of enti<br>tlement                                         | MM1.1          | 1<br>Hardware and software access protec<br>tion (read and write access) – Simple<br>access protection                                                                                                                                 |  |
| TM2    | Unauthorised<br>overwriting / ma<br>nipulation of enti<br>tlement                   | MM1.1          | 1<br>Hardware and software access protec<br>tion (read and write access) – Simple<br>access protection                                                                                                                                 |  |
| TM3    | Cloning of me<br>dium including<br>entitlement                                      | MM1.1<br>MM2.1 | 1<br>Hardware and software access protec<br>tion (read and write access) – Simple<br>access protection<br>2<br>Protection against cloning of carrier<br>medium with entitlement – Simple pro<br>tection                                |  |
| TM4    | Emulation of ap<br>plication or enti<br>tlement                                     | MM1.1<br>MM3.1 | 1<br>Hardware and software access protec<br>tion (read and write access)<br>2<br>Protection against emulation – Simple<br>emulation protection authentication                                                                          |  |
| TM10   | Carrier medium<br>malfunction                                                       | MM1.1<br>MM7.1 | 1<br>Hardware and software access protec<br>tion (read and write access)<br>2<br>Specification of carrier medium charac<br>teristics – Manufacturer's declaration                                                                      |  |
| TM11   | Tracking by unau<br>thorised scanning<br>of UID                                     | MM8.1          | 1<br>Introduce proximity technology as de<br>fined by ISO/IEC14443                                                                                                                                                                     |  |

<span id="page-140-0"></span>

| Threat |                                                                 | Safeguard | Safeguard                                                                                                     |  |  |
|--------|-----------------------------------------------------------------|-----------|---------------------------------------------------------------------------------------------------------------|--|--|
| TM12   | Lack of fallback<br>solution in the<br>event of malfunc<br>tion | MM9.1     | 1<br>Fallback solution for carrier medium<br>malfunction – Introduction of appropri<br>ate fallback solutions |  |  |

#### **Table 11–4 Safeguards when utilising Smart Tickets**

### **11.1.3.2 Residual risks when utilising the "Smart Ticket" carrier medium**

For technical and commercial reasons, it is not always possible to eliminate threats completely using safeguards. In such cases a certain risk remains.

The residual risk should be determined and documented as part of the planning of the actual implementation.

### **11.1.3.3 Safeguards when utilising the "multi-application card" carrier medium**

#### Conditions particular to this case

The issuing of the "multi-application card" carrier medium type is basically impossible to depict with this entitlement for reasons of cost. In this application scenario we have therefore assumed that entitlements of product type "Local multi-journey entitlement" will be loaded at a later stage onto carrier media of type "multi-application card", which are already in the possession of the customer. This means that – assuming it is not yet there – the appropriate application will also have to be loaded later onto the card.

When using an existing "multi-application card", it must always be assumed that other applications and entitlements may already exist on the card. These other applications and entitlements may originate from different entities who have not necessarily agreed on common rules of usage and behaviour.

The entitlement and, where relevant, the application are loaded on at the sales point, a vending machine or via the Internet, provided a suitable reader is available.

When using the entitlement, the customer must validate it before or straight after entering the vehicle. In systems with barriers, activation is upon entry. You also leave the blocked-off area using the carrier medium and the entitlement.

### Definition of safeguards

In the following table, safeguards are assigned to the threats in [Table 11–2.](#page-137-1) These safeguards are intended to compensate for those threats. The safeguards are described in Section[8.4.](#page-66-1)

| Threat |                                                                                     | Safeguard      | Safeguard                                                                         |  |
|--------|-------------------------------------------------------------------------------------|----------------|-----------------------------------------------------------------------------------|--|
| TC1    | Lack of compati<br>bility between<br>interfaces in car<br>rier medium and<br>reader | MS1.3<br>MR1.3 | 1<br>Introduction of interface tests and ap<br>proval procedures – Certification  |  |
| TC2    | Eavesdropping                                                                       | MS2.1          | 1<br>Ensuring the confidentiality of commu<br>nication between carrier medium and |  |

| Threat |                                                                    | Safeguard                                         | Safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |  |  |
|--------|--------------------------------------------------------------------|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|        |                                                                    | MS3.1                                             | reader in order to prevent eavesdrop<br>ping – Transmission security<br>2<br>Introduction of contact-less interface as<br>defined by ISO/IEC14443                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |  |  |
| TM1    | Unauthorised<br>scanning of enti<br>tlement                        | MM1.3                                             | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |  |  |
| TM2    | Unauthorised<br>overwriting / ma<br>nipulation of enti<br>tlement  | MM1.3<br>MM11a.3<br>MM11b.3                       | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection<br>2<br>Loading new entitlements – Securing<br>the authenticity and integrity of the enti<br>tlement – Complex authentication con<br>cept.<br>3<br>Loading new entitlements – Securing<br>the confidentiality of the entitlement –<br>Complex authentication concept                                                                                                                                                                                                                                                                                                                                                                                                     |  |  |
| TM3    | Cloning of me<br>dium including<br>entitlement                     | MM1.3<br>MM2.3                                    | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection<br>2<br>Protection against cloning of carrier<br>medium with entitlement – Advanced<br>protection                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |  |
| TM4    | Emulation of ap<br>plication or enti<br>tlement                    | MM1.1<br>MM3.1                                    | 1<br>Hardware and software access protec<br>tion (read and write access)<br>2<br>Protection against emulation – Simple<br>emulation protection authentication                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |  |
| TM9    | Protection of ad<br>ditional applica<br>tions and entitle<br>ments | MM6.3<br>MM10a.3<br>MM10b.3<br>MM11a.3<br>MM11b.3 | 1<br>Separation of applications – Secure<br>separation of applications<br>2<br>Loading new applications – Securing<br>the authenticity and integrity of applica<br>tions – Implemention of a reloading<br>mechanism as defined by ISO 7816-13<br>with SM<br>3<br>Loading new applications – Securing<br>the confidentiality of applications – Im<br>plementation of a reloading mechanism<br>as defined by ISO 7816-13 with SM<br>4<br>Loading new entitlements – Securing<br>the authenticity and integrity of entitle<br>ments – Complex symmetric authenti<br>cation concept with session key nego<br>tiation<br>5<br>Loading new entitlements – Securing<br>the confidentiality of entitlements –<br>Complex symmetric authentication con<br>cept with session key negotiation |  |  |

<span id="page-142-0"></span>

| Threat |                                                                 | Safeguard | Safeguard |                                                                                                          |  |
|--------|-----------------------------------------------------------------|-----------|-----------|----------------------------------------------------------------------------------------------------------|--|
| TM10   | Carrier medium<br>malfunction                                   | MM7.1     | 1         | Specification of carrier medium charac<br>teristics – Manufacturer's declaration                         |  |
| TM11   | Tracking by unau<br>thorised scanning<br>of UID                 | MM8.1     | 1         | Introduce proximity technology as de<br>fined by ISO/IEC14443                                            |  |
| TM12   | Lack of fallback<br>solution in the<br>event of malfunc<br>tion | MM9.1     | 1         | Fallback solution for carrier medium<br>malfunction – Introduction of appropri<br>ate fallback solutions |  |

#### **Table 11–5 Safeguards when utilising multi-application cards**

### **11.1.3.4 Residual risks when utilising the "multi-application card" carrier medium**

For technical and commercial reasons, it is not always possible to eliminate threats completely using safeguards. In such cases a certain risk remains.

The residual risk should be determined and documented as part of the planning of the actual implementation.

### **11.1.3.5 Safeguards when utilising the "NFC mobile device" carrier medium**

#### Conditions particular to this case

The issuing of the "NFC mobile device" carrier medium type is impossible to depict for reasons of cost and for operative reasons. In this application scenario we have therefore assumed that entitlements of product type "Local multi-journey entitlement" will be loaded at a later stage onto carrier media of type "NFC mobile device", which are already in the possession of the customer. This means that – assuming it is not yet there – the relevant application will also have to be loaded into the secure memory of the NFC mobile device.

When an existing "NFC mobile device" is being used, it must always be assumed that other applications and entitlements may already exist on the carrier medium. These other applications and entitlements may originate from different entities who have not necessarily agreed on common rules of usage and behaviour.

The entitlement and, where relevant, the application are loaded on over-the-air, at a sales point or at a vending machine.

When using the entitlement, the customer must validate it before or straight after entering the vehicle. In systems with barriers, activation is upon entry. You also leave the blocked-off area using the carrier medium and the entitlement.

#### Definition of safeguards

In the following table, safeguards are assigned to the threats in [Table 11–2.](#page-137-1) These safeguards are intended to compensate for those threats. The safeguards are described in Section [8.4.](#page-66-1)

<span id="page-143-0"></span>

| Threat |                                                                                | Safeguard                                         | Safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |  |  |
|--------|--------------------------------------------------------------------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
| TC1    | Lack of compatibility<br>between interfaces in<br>carrier medium and<br>reader | MS1.3<br>MR1.3                                    | 1<br>Introduction of interface tests and ap<br>proval procedures – Certification                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |  |
| TC2    | Eavesdropping                                                                  | MS2.1<br>MS3.1                                    | 1<br>Ensuring the confidentiality of commu<br>nication between carrier medium and<br>reader in order to prevent eavesdrop<br>ping – Transmission security<br>2<br>Introduction of contact-less interface as<br>defined by ISO/IEC14443                                                                                                                                                                                                                                                                                  |  |  |
| TM1    | Unauthorised scanning<br>of entitlement                                        | MM1.3                                             | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection                                                                                                                                                                                                                                                                                                                                                                                                               |  |  |
| TM2    | Unauthorised overwrit<br>ing / manipulation of<br>entitlement                  | MM1.3<br>MM11a.3<br>MM11b.3                       | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection<br>2<br>Loading new entitlements – Securing<br>the authenticity and integrity of the enti<br>tlement – Complex symmetric authen<br>tication concept with session key nego<br>tiation<br>3<br>Loading new entitlements – Securing<br>the confidentiality of the entitlement –<br>Complex symmetric authentication<br>concept with session key negotiation                                                      |  |  |
| TM3    | Cloning of medium<br>including entitlement                                     | MM1.3<br>MM2.3                                    | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection<br>2<br>Protection against cloning of carrier<br>medium with entitlement – Advanced<br>protection                                                                                                                                                                                                                                                                                                             |  |  |
| TM4    | Emulation of applica<br>tion or entitlement                                    | MM1.1<br>MM3.1                                    | 1<br>Hardware and software access protec<br>tion (read and write access)<br>2<br>Protection against emulation – Simple<br>emulation protection authentication                                                                                                                                                                                                                                                                                                                                                           |  |  |
| TM9    | Insufficient protection<br>of additional applica<br>tions and entitlements     | MM6.3<br>MM10a.3<br>MM10b.3<br>MM11a.3<br>MM11b.3 | 1<br>Separation of applications – Secure<br>separation of applications<br>2<br>Loading new applications – Securing<br>the authenticity and integrity of applica<br>tions – Implemention of a reloading<br>mechanism as defined by ISO 7816-13<br>with SM<br>3<br>Loading new applications – Securing<br>the confidentiality of applications – Im<br>plementation of a reloading mechanism<br>as defined by ISO 7816-13 with SM<br>4<br>Loading new entitlements – Securing<br>the authenticity and integrity of entitle |  |  |

<span id="page-144-0"></span>

| Threat |                                                               | Safeguard | Safeguard                                                                                                                                                                                                                                              |  |  |
|--------|---------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|        |                                                               |           | ments – Complex symmetric authenti<br>cation concept with session key nego<br>tiation<br>5<br>Loading new entitlements – Securing<br>the confidentiality of entitlements –<br>Complex symmetric authentication<br>concept with session key negotiation |  |  |
| TM10   | Carrier medium mal<br>function                                | MM7.1     | 1<br>Specification of carrier medium charac<br>teristics – Manufacturer's declaration                                                                                                                                                                  |  |  |
| TM11   | Tracking by unauthor<br>ised scanning of UID                  | MM8.1     | 1<br>Introduce proximity technology as de<br>fined by ISO/IEC14443                                                                                                                                                                                     |  |  |
| TM12   | Lack of fallback solu<br>tion in the event of mal<br>function | MM9.1     | 1<br>Fallback solution for carrier medium<br>malfunction – Introduction of appropri<br>ate fallback solutions                                                                                                                                          |  |  |

#### **Table 11–6 Safeguards when utilising NFC mobile device**

### **11.1.3.6 Residual risks when utilising the "NFC mobile device" carrier medium**

For technical and commercial reasons, it is not always possible to eliminate threats completely using safeguards. In such cases a certain risk remains.

The residual risk should be determined and documented as part of the planning of the actual implementation.

## **11.2 Electronic season ticket**

### **11.2.1 Determining the protection demand category**

The following conditions apply to the "electronic season ticket" application scenario and must be taken into consideration when determining the protection demand:

- 1 High commercial value (€20 < electronic season ticket < €500). Extreme case: German Railway railcard (> €3000)
- 2 Personal data
- 3 No usage data
- 4 No calculation data
- 5 These tickets are used constantly, and the medium is carried around between uses as well.
- 6 They may be combined with other application scenarios and products. The product can be combined with higher-value products in the same application area. When determining the protection demand it must be borne in mind that this scenario may endanger other products with a higher value.

The "electronic season ticket" product is normally issued on a "secure chip card" or "multiapplication card" carrier medium, or loaded onto existing "multi-application card" or "NFC mobile device" carrier media. Only these cases will be examined in further detail in the following.

If interoperability has to be assured technically between the service providers and product providers, then the product is normally issued on the "multi-application card" carrier medium. If not, then the "secure chip card" is the carrier medium most often used in practice.

On the basis of the criteria discussed in Section [8.2.5](#page-59-1), the application scenario can be allocated to the following protection demand categories:

| Security target |                                                                          | Protection<br>demand<br>category | Criteria for allocating to protection demand category                                                                                                                                         |  |  |  |
|-----------------|--------------------------------------------------------------------------|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|
| SS1             | Technical<br>compatibility                                               | 1                                | All of the system components are from the same sup<br>plier. The supplier ensures that they are compatible.                                                                                   |  |  |  |
|                 |                                                                          | 2                                | The system has to function with components from a<br>small number of defined suppliers. The system man<br>ager or a system integrator ensures compatibility.                                  |  |  |  |
|                 |                                                                          | 3                                | Open system that has to function with components<br>from any company in the market.                                                                                                           |  |  |  |
|                 |                                                                          |                                  | System and carrier media are normally acquired by<br>offering out for public tender.                                                                                                          |  |  |  |
|                 |                                                                          |                                  | Malfunction affects only a few customers.                                                                                                                                                     |  |  |  |
| SS2             | Fallback solu<br>tion in the<br>event of mal<br>function                 | 1                                | Malfunctions of a large number of media are not to be<br>expected. It is assumed that the system will remain<br>sufficiently available.                                                       |  |  |  |
|                 |                                                                          | 2                                | Malfunction affects many customers.                                                                                                                                                           |  |  |  |
|                 |                                                                          | 3                                | Malfunction affects a large proportion of customers.                                                                                                                                          |  |  |  |
| SS3             | Intuitive,<br>fault-tolerant<br>operation                                | 1                                | A few customers cannot operate it intuitively.                                                                                                                                                |  |  |  |
|                 |                                                                          |                                  | Only used upon inspection and – dependent on the<br>product – for checking in.                                                                                                                |  |  |  |
|                 |                                                                          | 2                                | Many customers cannot operate it intuitively.                                                                                                                                                 |  |  |  |
|                 |                                                                          | 3                                | A large proportion of customers cannot operate it intui<br>tively.                                                                                                                            |  |  |  |
|                 | Protection of<br>personal data<br>(including<br>personal us<br>age data) | 1                                | Customer's reputation is damaged / Data is lost.                                                                                                                                              |  |  |  |
| SI1             |                                                                          |                                  | Customer's social existence is damaged / Data be<br>comes known to third parties.                                                                                                             |  |  |  |
|                 |                                                                          | 2                                | If person-related invoicing information or payment de<br>tails stored in the system are stolen or manipulated,<br>the customer may suffer considerable commercial and<br>social consequences. |  |  |  |
|                 |                                                                          | 3                                | Customer's physical existence is damaged / Data is<br>misused.                                                                                                                                |  |  |  |
| SI2             | Protection of<br>entitlements                                            | 1                                | Predicted product-related loss of sales through coun<br>terfeiting, damage or manipulation <1%                                                                                                |  |  |  |
|                 |                                                                          | 2                                | Predicted product-related loss of sales through coun-                                                                                                                                         |  |  |  |
|                 |                                                                          |                                  |                                                                                                                                                                                               |  |  |  |

| Security target |                                                       | Protection<br>demand<br>category | Criteria for allocating to protection demand category                                                                                                                                      |  |  |
|-----------------|-------------------------------------------------------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|                 |                                                       |                                  | terfeiting, damage or manipulation <3%                                                                                                                                                     |  |  |
|                 |                                                       |                                  | From the point of view of an attacker, the expense of<br>counterfeiting must be well below the value of the enti<br>tlement (< €500). This can be prevented using level 2<br>safeguards.   |  |  |
|                 |                                                       | 3                                | Predicted product-related loss of sales through coun<br>terfeiting, damage or manipulation >3%                                                                                             |  |  |
|                 | Protection of                                         | 1                                | Data becomes known to third parties.                                                                                                                                                       |  |  |
| SI3             | logistical data<br>(anonymised                        | 2                                | Data is lost.                                                                                                                                                                              |  |  |
|                 | usage data)                                           | 3                                | Data is misused.                                                                                                                                                                           |  |  |
|                 |                                                       | 1                                |                                                                                                                                                                                            |  |  |
|                 |                                                       | 2                                |                                                                                                                                                                                            |  |  |
|                 | Reliable in                                           |                                  | Data is misused, modified, etc.                                                                                                                                                            |  |  |
| SI4             | voicing                                               | 3                                | Only relevant if interoperability is required:                                                                                                                                             |  |  |
|                 |                                                       |                                  | In a system involving multiple entities who do not trust<br>one another, the possibility of invoicing fraud between<br>the entities cannot be discounted.                                  |  |  |
|                 | Protection of<br>applications<br>and entitle<br>ments | 1                                | Applications are issued by the same application issuer<br>and entitlements by the same product owner.                                                                                      |  |  |
| SI5             |                                                       | 2                                | Applications are issued by different application issuers<br>and entitlements by different product owners. The enti<br>ties trust one another.                                              |  |  |
|                 |                                                       |                                  | Applications are issued by different application issuers<br>and entitlements by different product owners. The enti<br>ties do not trust one another.                                       |  |  |
|                 |                                                       | 3                                | When loading the entitlement onto multi-application<br>cards or NFC mobile devices, it must always be as<br>sumed that applications from other entities will be on<br>the customer medium. |  |  |
|                 |                                                       | 1                                | Not relevant for carrier medium.                                                                                                                                                           |  |  |
| SP3             | Data minimi<br>zation                                 | 2                                |                                                                                                                                                                                            |  |  |
|                 |                                                       | 3                                |                                                                                                                                                                                            |  |  |

<span id="page-147-0"></span>

| Security target |                                                                  | Protection<br>demand<br>category | Criteria for allocating to protection demand category |  |  |
|-----------------|------------------------------------------------------------------|----------------------------------|-------------------------------------------------------|--|--|
| SP4             | Protection<br>against the<br>creation of<br>movement<br>profiles | 1                                | Customer's reputation is damaged.                     |  |  |
|                 |                                                                  | 2                                | Customer's social existence is damaged.               |  |  |
|                 |                                                                  | 3                                | Customer's physical existence is damaged.             |  |  |

**Table 11–7 Protection demand for the "electronic season ticket" application scenario** 

### **11.2.2 Relevant threats**

The following table lists the threats specific to this application scenario:

| Threat |                                                                                         | Carrier medium  |                        |                               |                         |                                                                              |
|--------|-----------------------------------------------------------------------------------------|-----------------|------------------------|-------------------------------|-------------------------|------------------------------------------------------------------------------|
|        |                                                                                         | Smart<br>Ticket | Secure<br>chip<br>card | Multi<br>applica<br>tion card | NFC<br>mobile<br>device | Comments                                                                     |
| TC1    | Lack of compatibility<br>between the inter<br>faces of the carrier<br>medium and reader | -               | 3                      | 3                             | 3                       |                                                                              |
| TC2    | Eavesdropping                                                                           | -               | 2                      | 2                             | 2                       |                                                                              |
| TM1    | Unauthorised scan<br>ning of entitlement                                                | -               | 2                      | 3                             | 3                       | Category 3 be<br>cause other<br>applications and<br>entitlements are<br>used |
| TM2    | Unauthorised over<br>writing / manipulation<br>of entitlement                           | -               | 2                      | 3                             | 3                       | Category 3 be<br>cause other<br>applications and<br>entitlements are<br>used |
| TM3    | Cloning of medium<br>including entitlement                                              | -               | 2                      | 3                             | 3                       | Category 3 be<br>cause other<br>applications and<br>entitlements are<br>used |
| TM4    | Emulation of applica<br>tion or entitlement                                             | -               | 2                      | 2                             | 2                       |                                                                              |
| TM5    | Unauthorised scan<br>ning of personal data                                              | -               | 2                      | 2                             | 2                       |                                                                              |
| TM6    | Unauthorised over<br>writing / manipulation<br>of personal data                         | -               | 2                      | 2                             | 2                       |                                                                              |

<span id="page-148-0"></span>

| Threat |                                                                    | Carrier medium  |                        |                               |                         |                                                                              |
|--------|--------------------------------------------------------------------|-----------------|------------------------|-------------------------------|-------------------------|------------------------------------------------------------------------------|
|        |                                                                    | Smart<br>Ticket | Secure<br>chip<br>card | Multi<br>applica<br>tion card | NFC<br>mobile<br>device | Comments                                                                     |
| TM7    | Unauthorised scan<br>ning of calculation<br>data                   | -               | 3                      | 3                             | 3                       | Only relevant if<br>interoperability<br>is required                          |
| TM8    | Unauthorised over<br>writing / manipulation<br>of calculation data | -               | 3                      | 3                             | 3                       | Only relevant if<br>interoperability<br>is required                          |
| TM9    | Protection of addi<br>tional applications<br>and entitlements      | -               | -                      | 3                             | 3                       | Category 3 be<br>cause other<br>applications and<br>entitlements are<br>used |
| TM10   | Carrier medium mal<br>function                                     | -               | 1                      | 1                             | 1                       |                                                                              |
| TM11   | Tracking by unauthor<br>ised scanning of UID                       | -               | 1                      | 1                             | 1                       |                                                                              |
| TM12   | Lack of fallback solu<br>tion in the event of<br>malfunction       | -               | 1                      | 1                             | 1                       |                                                                              |

**Table 11–8 Relevant threats in the "electronic season ticket" application scenario** 

### <span id="page-148-1"></span>**11.2.3 Definition of specific safeguards**

This section defines specific safeguards on the basis of the relevant threats described in the section above. The threats listed will be discussed for the following use cases:

|                                                    | Carrier medium  |                        |                               |                         |          |  |
|----------------------------------------------------|-----------------|------------------------|-------------------------------|-------------------------|----------|--|
| Use case                                           | Smart<br>Ticket | Secure<br>chip<br>card | Multi<br>applica<br>tion card | NFC<br>mobile<br>device | Comments |  |
| Identification when<br>registering and<br>ordering | -               | -                      | -                             | -                       |          |  |
| Carrier medium<br>initialisation                   | -               | +                      | +                             | -                       |          |  |
| Application loading                                | -               | -                      | +                             | +                       |          |  |
| Entitlement loading                                | -               | +                      | +                             | -                       |          |  |
| Loading new enti<br>tlements                       | -               | +                      | +                             | +                       |          |  |
| Delivery                                           | -               | +                      | +                             | -                       |          |  |

<span id="page-149-0"></span>

|                   | Carrier medium                  |                        |                               |                         |          |  |
|-------------------|---------------------------------|------------------------|-------------------------------|-------------------------|----------|--|
| Use case          | Smart<br>Ticket                 | Secure<br>chip<br>card | Multi<br>applica<br>tion card | NFC<br>mobile<br>device | Comments |  |
| Check-in          | If interoperability is required |                        |                               |                         |          |  |
| Check-out         | If interoperability is required |                        |                               |                         |          |  |
| Entitlement check | -                               | +                      | +                             | +                       |          |  |
| Blocking          | -                               | +                      | +                             | +                       |          |  |
| Key management    | -                               | +                      | +                             | +                       |          |  |

#### **Table 11–9 Use cases relevant to the "electronic season ticket" application scenario**

The following sub-sections will define safeguards for each carrier medium, on the basis of the threats described and the relevant use cases.

### **11.2.3.1 Safeguards when utilising the "secure chip card" carrier medium**

#### Conditions particular to this case

Entitlements of product type "electronic season ticket" are issued on carrier media of type "secure chip card" or "multi-application card". The carrier medium is initialised with an application which can contain one or more entitlements. The chip's security mechanisms normally include authentication, access protection and secure transmission (see Section [10.2](#page-129-1)).

The initialisation of the carrier medium is done together with the personalisation of the entitlement in a mass personaliser, at the sales point or in a vending machine.

Furthermore, in this application scenario it is assumed that entitlements of product type "electronic season ticket" will be loaded at a later stage onto carrier media of type "secure chip card", which are already in the customers' possession. The application needed for this must already be on the card. It is not necessary to load new applications in the field.

The entitlement is loaded on at the sales point, a vending machine or via the Internet, provided a suitable reader is available.

Checking in and out is necessary only if interoperability is required when using the entitlement, so as to facilitate invoicing between the service providers.

In systems with barriers, access to and from the blocked-off area is by means of the carrier medium and entitlement.

#### Definition of safeguards

In the following table, safeguards are assigned to the threats in [Table 11–8.](#page-148-1) These safeguards are intended to compensate for those threats. The safeguards are described in Section [8.4.](#page-66-1)

| Threat |                                   | Safeguard | Safeguard                                                                        |  |  |
|--------|-----------------------------------|-----------|----------------------------------------------------------------------------------|--|--|
| TC1    | Lack of compati<br>bility between | MS1.3     | 1<br>Introduction of interface tests and ap<br>proval procedures – Certification |  |  |

<span id="page-150-0"></span>

| Threat |                                                        | Safeguard        | Safeguard                                                                                                                                                                                                                                                                                          |  |  |
|--------|--------------------------------------------------------|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|        | interfaces in car<br>rier medium and<br>reader         | MR1.3            |                                                                                                                                                                                                                                                                                                    |  |  |
| TC2    | Eavesdropping                                          | MS2.2<br>MS3.2   | 1<br>Ensuring the confidentiality of commu<br>nication between carrier medium and<br>reader in order to prevent eavesdrop<br>ping – Mutual implicit authentication<br>during transmission (proof of secret<br>status)<br>2<br>Introduction of contact-less interface as<br>defined by ISO/IEC14443 |  |  |
| TM1    | Unauthorised<br>scanning of enti<br>tlement            | MM1.2            | 1<br>Hardware and software access protec<br>tion (read and write access) – Specific<br>access protection                                                                                                                                                                                           |  |  |
| TM2    | Unauthorised<br>overwriting / ma<br>nipulation of enti | MM1.2<br>MM11a.2 | 1<br>Hardware and software access protec<br>tion (read and write access) – Specific<br>access protection                                                                                                                                                                                           |  |  |
|        | tlement                                                | MM11b.2          | 2<br>Loading a new entitlement – Securing<br>the authenticity and integrity of the enti<br>tlement – Proprietary securing of load<br>ing process                                                                                                                                                   |  |  |
|        |                                                        |                  | 3<br>Loading a new entitlement – Securing<br>the confidentiality of the entitlement –<br>Loading process secured by proprietary<br>cryptographic method                                                                                                                                            |  |  |
| TM3    | Cloning of me<br>dium including<br>entitlement         | MM1.2<br>MM2.2   | 1<br>Hardware and software access protec<br>tion (read and write access) – Specific<br>access protection                                                                                                                                                                                           |  |  |
|        |                                                        |                  | 2<br>Protection against cloning of carrier<br>medium with entitlement – Protection<br>against cloning of carrier medium and<br>data content                                                                                                                                                        |  |  |
| TM4    | Emulation of ap<br>plication or enti                   | MM1.2            | 1<br>Hardware and software access protec<br>tion (read and write access) – Specific                                                                                                                                                                                                                |  |  |
|        | tlement                                                | MM3.2            | access protection<br>2<br>Protection against emulation – Emula<br>tion protection                                                                                                                                                                                                                  |  |  |
| TM5    | Unauthorised<br>scanning of per                        | MM1.2            | 1<br>Hardware and software access protec<br>tion (read and write access) – Specific                                                                                                                                                                                                                |  |  |
|        | sonal data                                             | MM4.2            | access protection<br>2<br>Protection of personal data against re<br>trieval and overwriting/manipulation –<br>Specific access protection for personal<br>data                                                                                                                                      |  |  |
| TM6    | Unauthorised<br>overwriting / ma<br>nipulation of per  | MM1.2<br>MM4.2   | 1<br>Hardware and software access protec<br>tion (read and write access) – Specific<br>access protection                                                                                                                                                                                           |  |  |

<span id="page-151-0"></span>

| Threat |                                                                        | Safeguard      | Safeguard                                                                                                                                                                                                                                                                     |  |  |
|--------|------------------------------------------------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
|        | sonal data                                                             |                | 2<br>Protection of personal data against re<br>trieval and overwriting/manipulation –<br>Specific access protection for personal<br>data                                                                                                                                      |  |  |
| TM7    | Unauthorised<br>scanning of cal<br>culation data                       | MM1.3<br>MM5.3 | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection<br>2<br>Protection of calculation data against<br>retrieval and overwriting/manipulation –<br>Access and manipulation protection in<br>the case of interoperability |  |  |
| TM8    | Unauthorised<br>overwriting / ma<br>nipulation of cal<br>culation data | MM1.3<br>MM5.3 | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection<br>2<br>Protection of calculation data against<br>retrieval and overwriting/manipulation –<br>Access and manipulation protection in<br>the case of interoperability |  |  |
| TM9    | Protection of ad<br>ditional applica<br>tions and entitle<br>ments     |                | Not relevant                                                                                                                                                                                                                                                                  |  |  |
| TM10   | Carrier medium<br>malfunction                                          | MM7.1          | 1<br>Specification of carrier medium charac<br>teristics – Manufacturer's declaration                                                                                                                                                                                         |  |  |
| TM11   | Tracking by unau<br>thorised scanning<br>of UID                        | MM8.1          | 1<br>Introduce proximity technology as de<br>fined by ISO/IEC14443                                                                                                                                                                                                            |  |  |
| TM12   | Lack of fallback<br>solution in the<br>event of malfunc<br>tion        | MM9.1          | 1<br>Fallback solution for carrier medium<br>malfunction – Introduction of appropri<br>ate fallback solutions                                                                                                                                                                 |  |  |

**Table 11–10 Safeguards for the "electronic season ticket" entitlement on a "secure chip card"** 

### **11.2.3.2 Residual risks when utilising the "secure chip card" carrier medium**

For technical and commercial reasons, it is not always possible to eliminate threats completely using safeguards. In such cases a certain risk remains.

The residual risk should be determined and documented as part of the planning of the actual implementation.

### **11.2.3.3 Safeguards when utilising the "multi-application card" carrier medium**

Conditions particular to this case

If interoperability has to be assured technically, then the "electronic season ticket" entitlement is normally issued on a "multi-application card" carrier medium.

Furthermore, in this application scenario it is assumed that entitlements of product type "electronic season ticket" will be loaded at a later stage onto carrier media of type "multiapplication card", which are already in the customers' possession. This means that – assuming it is not yet there – the appropriate application will also have to be loaded later onto the card.

When using an existing "multi-application card", it must always be assumed that other applications and entitlements may already exist on the card. These other applications and entitlements may originate from different entities who have not necessarily agreed on common rules of usage and behaviour.

The entitlement and, where relevant, the application are loaded on at the sales point, a vending machine or via the Internet, provided a suitable reader is available.

Checking in and out is necessary only if interoperability is required when using the entitlement, so as to facilitate invoicing between the service providers.

In systems with barriers, access to and from the blocked-off area is by means of the carrier medium and entitlement.

#### Definition of safeguards

In the following table, safeguards are assigned to the threats in [Table 11–8.](#page-148-1) These safeguards are described in Section [8.4.](#page-66-1)

| Threat |                                                                                     | Safeguard                   | Safeguard                                                                                                                                                                                                                                                                                                                                                                              |
|--------|-------------------------------------------------------------------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TC1    | Lack of compati<br>bility between<br>interfaces in car<br>rier medium and<br>reader | MS1.3<br>MR1.3              | 1<br>Introduction of interface tests and ap<br>proval procedures – Certification                                                                                                                                                                                                                                                                                                       |
| TC2    | Eavesdropping                                                                       | MS2.2<br>MS3.2              | 1<br>Ensuring the confidentiality of commu<br>nication between carrier medium and<br>reader in order to prevent eavesdrop<br>ping – Mutual implicit authentication<br>during transmission<br>2<br>Introduction of contact-less interface as<br>defined by ISO/IEC14443                                                                                                                 |
| TM1    | Unauthorised<br>scanning of enti<br>tlement                                         | MM1.3                       | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection                                                                                                                                                                                                                                                                              |
| TM2    | Unauthorised<br>overwriting / ma<br>nipulation of enti<br>tlement                   | MM1.3<br>MM11a.3<br>MM11b.3 | 2<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection<br>3<br>Loading new entitlements – Securing<br>the authenticity and integrity of the enti<br>tlement – Complex symmetric authenti<br>cation concept with session key nego<br>tiation<br>4<br>Loading new entitlements – Securing<br>the confidentiality of the entitlement – |

<span id="page-153-0"></span>

| Threat |                                                                        | Safeguard               | Safeguard                                                                                                                                                                                                                                                                               |
|--------|------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        |                                                                        |                         | Complex symmetric authentication con<br>cept with session key negotiation                                                                                                                                                                                                               |
| TM3    | Cloning of me<br>dium including<br>entitlement                         | MM1.3<br>MM2.3          | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection<br>2<br>Protection against cloning of carrier<br>medium with entitlement – Advanced<br>protection against the cloning of carrier<br>medium and data content                   |
| TM4    | Emulation of ap<br>plication or enti<br>tlement                        | MM1.2<br>MM3.2          | 1<br>Hardware and software access protec<br>tion (read and write access) – Specific<br>access protection<br>2<br>Protection against emulation – Emula<br>tion protection                                                                                                                |
| TM5    | Unauthorised<br>scanning of per<br>sonal data                          | MM1.2<br>MM4.2          | 1<br>Hardware and software access protec<br>tion (read and write access) – Specific<br>access protection<br>2<br>Protection of personal data against re<br>trieval and overwriting/manipulation –<br>Specific access protection for personal<br>data                                    |
| TM6    | Unauthorised<br>overwriting / ma<br>nipulation of per<br>sonal data    | MM1.2<br>MM4.2<br>MM6.2 | 1<br>Hardware and software access protec<br>tion (read and write access) – Specific<br>access protection<br>2<br>Protection of personal data against re<br>trieval and overwriting/manipulation –<br>Specific access protection for personal<br>data<br>3<br>Separation of applications |
| TM7    | Unauthorised<br>scanning of cal<br>culation data                       | MM1.3<br>MM5.3          | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection<br>2<br>Protection of calculation data against<br>retrieval and overwriting/manipulation –<br>Access and manipulation protection in<br>the case of interoperability           |
| TM8    | Unauthorised<br>overwriting / ma<br>nipulation of cal<br>culation data | MM1.3<br>MM5.3          | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection<br>2<br>Protection of calculation data against<br>retrieval and overwriting/manipulation –<br>Access and manipulation protection in<br>the case of interoperability           |
| TM9    | Protection of ad<br>ditional applica<br>tions and entitle<br>ments     | MM6.3<br>MM10a.3        | 1<br>Separation of applications – Secure<br>separation of applications<br>2<br>Loading new applications – Securing<br>the authenticity and integrity of applica-                                                                                                                        |

<span id="page-154-0"></span>

| Threat |                                                                 | Safeguard          | Safeguard                                                                                                                                                                      |
|--------|-----------------------------------------------------------------|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        |                                                                 | MM10b.3<br>MM11a.3 | tions – Implementation of a reloading<br>mechanism as defined by ISO 7816-13<br>with SM                                                                                        |
|        |                                                                 | MM11b.3            | 3<br>Loading new applications – Securing<br>the confidentiality of applications – Im<br>plementation of a reloading mechanism<br>as defined by ISO 7816-13 with SM             |
|        |                                                                 |                    | 4<br>Loading new entitlements – Securing<br>the authenticity and integrity of entitle<br>ments – Complex symmetric authenti<br>cation concept with session key nego<br>tiation |
|        |                                                                 |                    | 5<br>Loading new entitlements – Securing<br>the confidentiality of entitlements –<br>Complex symmetric authentication con<br>cept with session key negotiation                 |
| TM10   | Carrier medium<br>malfunction                                   | MM7.1              | 1<br>Specification of carrier medium charac<br>teristics – Manufacturer's declaration                                                                                          |
| TM11   | Tracking by unau<br>thorised scanning<br>of UID                 | MM8.1              | 1<br>Introduce proximity technology as de<br>fined by ISO/IEC14443                                                                                                             |
| TM12   | Lack of fallback<br>solution in the<br>event of malfunc<br>tion | MM9.1              | 1<br>Fallback solution for carrier medium<br>malfunction – Introduction of appropri<br>ate fallback solutions                                                                  |

#### **Table 11–11 Safeguards for the "electronic season ticket" entitlement on a "multiapplication card"**

### **11.2.3.4 Residual risks when utilising the "multi-application card" carrier medium**

For technical and commercial reasons, it is not always possible to eliminate threats completely using safeguards. In such cases a certain risk remains.

The residual risk should be determined and documented as part of the planning of the actual implementation.

### **11.2.3.5 Safeguards when utilising the "NFC mobile device" carrier medium**

### Conditions particular to this case

The issuing of the "NFC mobile device" carrier medium type together with an entitlement is impossible to depict for reasons of cost and for operative reasons. In this application scenario we have therefore assumed that entitlements of product type "electronic season ticket" will be loaded at a later stage onto carrier media of type "NFC mobile device", which are already in the possession of customers. This means that – assuming it is not yet there – the relevant application will also have to be loaded into the secure memory of the NFC mobile device.

When an existing "NFC mobile device" is being used, it must always be assumed that other applications and entitlements may already exist on the carrier medium. These other applications and entitlements may originate from different entities who have not necessarily agreed on common rules of usage and behaviour.

The entitlement and, where relevant, the application are loaded on over-the-air, at a sales point or at a vending machine.

In systems with barriers, access to and from the blocked-off area is by means of the carrier medium and entitlement.

Definition of safeguards

In the following table, safeguards are assigned to the threats in [Table 11–8.](#page-148-1) These safeguards are described in Section [8.4.](#page-66-1)

| Threat |                                                                                     | Safeguard                   | Safeguard                                                                                                                                                                                                                                                                                                                                                                      |
|--------|-------------------------------------------------------------------------------------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TC1    | Lack of compati<br>bility between<br>interfaces in car<br>rier medium and<br>reader | MS1.3<br>MR1.3              | 1<br>Introduction of interface tests and ap<br>proval procedures – Certification                                                                                                                                                                                                                                                                                               |
| TC2    | Eavesdropping                                                                       | MS2.2<br>MS3.2              | 1<br>Ensuring the confidentiality of commu<br>nication between carrier medium and<br>reader in order to prevent eavesdrop<br>ping – Mutual implicit authentication<br>during transmission<br>2<br>Introduction of contact-less interface as<br>defined by ISO/IEC14443                                                                                                         |
| TM1    | Unauthorised<br>scanning of enti<br>tlement                                         | MM1.3                       | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection                                                                                                                                                                                                                                                                      |
| TM2    | Unauthorised<br>overwriting / ma<br>nipulation of enti<br>tlement                   | MM1.3<br>MM11a.3<br>MM11b.3 | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection<br>2<br>Loading new entitlements – Securing<br>the authenticity and integrity of the enti<br>tlement – Complex authentication con<br>cept.<br>3<br>Loading new entitlements – Securing<br>the confidentiality of the entitlement –<br>Complex authentication concept |
| TM3    | Cloning of me<br>dium including<br>entitlement                                      | MM1.3<br>MM2.3              | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection<br>2<br>Protection against cloning of carrier<br>medium with entitlement – Advanced<br>protection against the cloning of carrier<br>medium and data content                                                                                                          |
| TM4    | Emulation of ap<br>plication or enti                                                | MM1.2                       | 1<br>Hardware and software access protec<br>tion (read and write access) – Specific                                                                                                                                                                                                                                                                                            |

<span id="page-156-0"></span>

| Threat |                                                                        | Safeguard                                         | Safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------|------------------------------------------------------------------------|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        | tlement                                                                | MM3.2                                             | access protection<br>2<br>Protection against emulation – Emula<br>tion protection                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| TM5    | Unauthorised<br>scanning of per<br>sonal data                          | MM1.2<br>MM4.2                                    | 1<br>Hardware and software access protec<br>tion (read and write access) – Specific<br>access protection<br>2<br>Protection of personal data against re<br>trieval and overwriting/manipulation –<br>Specific access protection for personal<br>data                                                                                                                                                                                                                                                                                                                                                               |
| TM6    | Unauthorised<br>overwriting / ma<br>nipulation of per<br>sonal data    | MM1.2<br>MM4.2<br>MM6.2                           | 1<br>Hardware and software access protec<br>tion (read and write access) – Specific<br>access protection<br>2<br>Protection of personal data against re<br>trieval and overwriting/manipulation –<br>Specific access protection for personal<br>data<br>3<br>Separation of applications                                                                                                                                                                                                                                                                                                                            |
| TM7    | Unauthorised<br>scanning of cal<br>culation data                       | MM1.3<br>MM5.3                                    | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection<br>2<br>Protection of calculation data against<br>retrieval and overwriting/manipulation –<br>Access and manipulation protection in<br>the case of interoperability                                                                                                                                                                                                                                                                                                                                      |
| TM8    | Unauthorised<br>overwriting / ma<br>nipulation of cal<br>culation data | MM1.3<br>MM5.3                                    | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection<br>2<br>Protection of calculation data against<br>retrieval and overwriting/manipulation –<br>Access and manipulation protection in<br>the case of interoperability                                                                                                                                                                                                                                                                                                                                      |
| TM9    | Protection of ad<br>ditional applica<br>tions and entitle<br>ments     | MM6.3<br>MM10a.3<br>MM10b.3<br>MM11a.3<br>MM11b.3 | 1<br>Separation of applications – Secure<br>separation of applications<br>2<br>Loading new applications – Securing<br>the authenticity and integrity of applica<br>tions – Implementation of a reloading<br>mechanism as defined by ISO 7816-13<br>with SM<br>3<br>Loading new applications – Securing<br>the confidentiality of applications – Im<br>plementation of a reloading mechanism<br>as defined by ISO 7816-13 with SM<br>4<br>Loading new entitlements – Securing<br>the authenticity and integrity of entitle<br>ments – Complex symmetric authenti<br>cation concept with session key nego<br>tiation |

<span id="page-157-0"></span>

| Threat |                                                                 | Safeguard | Safeguard                                                                                                                                                      |
|--------|-----------------------------------------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        |                                                                 |           | 5<br>Loading new entitlements – Securing<br>the confidentiality of entitlements –<br>Complex symmetric authentication con<br>cept with session key negotiation |
| TM10   | Carrier medium<br>malfunction                                   | MM7.1     | 1<br>Specification of carrier medium charac<br>teristics – Manufacturer's declaration                                                                          |
| TM11   | Tracking by unau<br>thorised scanning<br>of UID                 | MM8.1     | 1<br>Introduce proximity technology as de<br>fined by ISO/IEC14443                                                                                             |
| TM12   | Lack of fallback<br>solution in the<br>event of malfunc<br>tion | MM9.1     | 1<br>Fallback solution for carrier medium<br>malfunction – Introduction of appropri<br>ate fallback solutions                                                  |

#### **Table 11–12 Safeguards for the "electronic season ticket" entitlement on an "NFC mobile device"**

### **11.2.3.6 Residual risks when utilising the "NFC mobile device" carrier medium**

For technical and commercial reasons, it is not always possible to eliminate threats completely using safeguards. In such cases a certain risk remains.

The residual risk should be determined and documented as part of the planning of the actual implementation.

## **11.3 The "Interoperable entitlement with automatic fare calculation" application scenario**

### **11.3.1 Determining the protection demand category**

The following conditions apply to the "Interoperable entitlement with AFC" application scenario and must be taken into consideration when determining the protection demand:

- 1 High commercial value (€10 to more than €1000)
- 2 Personal data
- 3 Interoperability between the entities must be assured technically:
	- a Sales data
	- b Usage data
	- c Calculation data
- 4 These tickets are used constantly, and the medium is probably carried around all the time between uses as well.
- 5 They may be combined with other application scenarios and products. The product can be combined with lower-value products in the same application area. When determining the protection demand it must be borne in mind that this scenario may be endangered by other product implementations.

<span id="page-158-0"></span>The "Interoperable entitlement with AFC" product is issued on a "multi-application card" carrier medium, or loaded onto existing "multi-application card" or "NFC mobile device" carrier media. Only these cases will be examined in further detail in the following.

On the basis of the criteria discussed in Section [8.2.5](#page-59-1), the application scenario can be allocated to the following protection demand categories:

| Security target |                                                                          | Protection<br>demand<br>category | Criteria for allocating to protection demand category                                                                                                                                         |  |  |  |
|-----------------|--------------------------------------------------------------------------|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|
| SS1             | Technical<br>compatibility                                               | 1                                | All of the system components are from the same sup<br>plier. The supplier ensures that they are compatible.                                                                                   |  |  |  |
|                 |                                                                          | 2                                | The system has to function with components from a<br>small number of defined suppliers. The system man<br>ager or a system integrator ensures compatibility.                                  |  |  |  |
|                 |                                                                          |                                  | Open system that has to function with components<br>from any company in the market.                                                                                                           |  |  |  |
|                 |                                                                          | 3                                | System and carrier media are normally acquired by<br>offering out for public tender.                                                                                                          |  |  |  |
|                 |                                                                          |                                  | Malfunction affects only a few customers.                                                                                                                                                     |  |  |  |
| SS2             | Fallback solu<br>tion in the<br>event of mal<br>function                 | 1                                | Malfunctions of a large number of media are not to be<br>expected. It is assumed that the system will remain<br>sufficiently available.                                                       |  |  |  |
|                 |                                                                          | 2                                | Malfunction affects many customers.                                                                                                                                                           |  |  |  |
|                 |                                                                          | 3                                | Malfunction affects a large proportion of customers.                                                                                                                                          |  |  |  |
|                 | Intuitive,<br>fault-tolerant<br>operation                                | 1                                | A few customers cannot operate it intuitively.                                                                                                                                                |  |  |  |
| SS3             |                                                                          | 2                                | Many customers cannot operate it intuitively.                                                                                                                                                 |  |  |  |
|                 |                                                                          | 3                                | A large proportion of customers cannot operate it intui<br>tively.                                                                                                                            |  |  |  |
|                 | Protection of<br>personal data<br>(including<br>personal us<br>age data) | 1                                | Customer's reputation is damaged / Data is lost.                                                                                                                                              |  |  |  |
| SI1             |                                                                          |                                  | Customer's social existence is damaged / Data be<br>comes known to third parties.                                                                                                             |  |  |  |
|                 |                                                                          | 2                                | If person-related invoicing information or payment de<br>tails stored in the system are stolen or manipulated,<br>the customer may suffer considerable commercial and<br>social consequences. |  |  |  |
|                 |                                                                          | 3                                | Customer's physical existence is damaged / Data is<br>misused.                                                                                                                                |  |  |  |
| SI2             | Protection of<br>entitlements                                            | 1                                | Predicted product-related loss of sales through coun<br>terfeiting, damage or manipulation <1%                                                                                                |  |  |  |
|                 |                                                                          | 2                                | Predicted product-related loss of sales through coun<br>terfeiting, damage or manipulation <3%                                                                                                |  |  |  |
|                 |                                                                          | 3                                | Predicted product-related loss of sales through coun                                                                                                                                          |  |  |  |

| Security target |                                                       | Protection<br>demand<br>category | Criteria for allocating to protection demand category                                                                                                                                      |  |  |  |
|-----------------|-------------------------------------------------------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|
|                 |                                                       |                                  | terfeiting, damage or manipulation >3%                                                                                                                                                     |  |  |  |
|                 |                                                       |                                  | From the point of view of an attacker, the expense of<br>counterfeiting must be well below the value of the enti<br>tlement (> €500). This can be prevented using level 3<br>safeguards.   |  |  |  |
|                 | Protection of                                         | 1                                | Data becomes known to third parties.                                                                                                                                                       |  |  |  |
| SI3             | logistical data<br>(anonymised                        | 2                                | Data is lost.                                                                                                                                                                              |  |  |  |
|                 | usage data)                                           | 3                                | Data is misused.                                                                                                                                                                           |  |  |  |
|                 |                                                       | 1                                |                                                                                                                                                                                            |  |  |  |
|                 |                                                       | 2                                |                                                                                                                                                                                            |  |  |  |
|                 | Reliable in                                           |                                  | Data is misused, modified, etc.                                                                                                                                                            |  |  |  |
| SI4             | voicing                                               | 3                                | Only relevant if interoperability is required:                                                                                                                                             |  |  |  |
|                 |                                                       |                                  | In a system involving multiple entities who do not trust<br>one another, the possibility of invoicing fraud between<br>the entities cannot be discounted.                                  |  |  |  |
| SI5             | Protection of<br>applications<br>and entitle<br>ments | 1                                | Applications are issued by the same application issuer<br>and entitlements by the same product owner.                                                                                      |  |  |  |
|                 |                                                       | 2                                | Applications are issued by different application issuers<br>and entitlements by different product owners. The enti<br>ties trust one another.                                              |  |  |  |
|                 |                                                       |                                  | Applications are issued by different application issuers<br>and entitlements by different product owners. The enti<br>ties do not trust one another.                                       |  |  |  |
|                 |                                                       | 3                                | When loading the entitlement onto multi-application<br>cards or NFC mobile devices, it must always be as<br>sumed that applications from other entities will be on<br>the customer medium. |  |  |  |
|                 | Data minimi                                           | 1                                | Not relevant for carrier medium.                                                                                                                                                           |  |  |  |
| SP3             | zation                                                | 2                                |                                                                                                                                                                                            |  |  |  |
|                 |                                                       | 3                                |                                                                                                                                                                                            |  |  |  |
| SP4             | Protection                                            | 1                                | Customer's reputation is damaged.                                                                                                                                                          |  |  |  |
|                 | against the<br>creation of                            | 2                                | Customer's social existence is damaged.                                                                                                                                                    |  |  |  |
|                 | movement<br>profiles                                  | 3                                | Customer's physical existence is damaged.                                                                                                                                                  |  |  |  |

**Table 11–13 Protection demand for the "Interoperable entitlement with AFC" application scenario** 

## <span id="page-160-0"></span>**11.3.2 Relevant threats**

|        |                                                                                         | Carrier medium  |                        |                               |                         |          |
|--------|-----------------------------------------------------------------------------------------|-----------------|------------------------|-------------------------------|-------------------------|----------|
| Threat |                                                                                         | Smart<br>Ticket | Secure<br>chip<br>card | Multi<br>applica<br>tion card | NFC<br>mobile<br>device | Comments |
| TC1    | Lack of compatibility<br>between the inter<br>faces of the carrier<br>medium and reader | -               | -                      | 3                             | 3                       |          |
| TC2    | Eavesdropping                                                                           | -               | -                      | 3                             | 3                       |          |
| TM1    | Unauthorised scan<br>ning of entitlement                                                | -               | -                      | 3                             | 3                       |          |
| TM2    | Unauthorised over<br>writing / manipulation<br>of entitlement                           | -               | -                      | 3                             | 3                       |          |
| TM3    | Cloning of medium<br>including entitlement                                              | -               | -                      | 3                             | 3                       |          |
| TM4    | Emulation of applica<br>tion or entitlement                                             | -               | -                      | 3                             | 3                       |          |
| TM5    | Unauthorised scan<br>ning of personal data                                              | -               | -                      | 3                             | 3                       |          |
| TM6    | Unauthorised over<br>writing / manipulation<br>of personal data                         | -               | -                      | 3                             | 3                       |          |
| TM7    | Unauthorised scan<br>ning of calculation<br>data                                        | -               | -                      | 3                             | 3                       |          |
| TM8    | Unauthorised over<br>writing / manipulation<br>of calculation data                      | -               | -                      | 3                             | 3                       |          |
| TM9    | Protection of addi<br>tional applications<br>and entitlements                           | -               | -                      | 3                             | 3                       |          |
| TM10   | Carrier medium mal<br>function                                                          | -               | -                      | 1                             | 1                       |          |
| TM11   | Tracking by unauthor<br>ised scanning of UID                                            | -               | -                      | 1                             | 1                       |          |

The following table lists the threats specific to this application scenario:

<span id="page-161-0"></span>

|        |                                                              | Carrier medium  |                        |                               |                         |          |
|--------|--------------------------------------------------------------|-----------------|------------------------|-------------------------------|-------------------------|----------|
| Threat |                                                              | Smart<br>Ticket | Secure<br>chip<br>card | Multi<br>applica<br>tion card | NFC<br>mobile<br>device | Comments |
| TM12   | Lack of fallback solu<br>tion in the event of<br>malfunction | -               | -                      | 1                             | 1                       |          |

| Table 11–14 | Relevant threats in the "Interoperable entitlement with AFC" applica |
|-------------|----------------------------------------------------------------------|
|             | tion scenario                                                        |

### <span id="page-161-1"></span>**11.3.3 Definition of specific safeguards**

This section defines specific safeguards on the basis of the relevant threats described in the section above. The threats listed will be discussed for the following use cases:

|                                                    | Carrier medium  |                        |                               |                         |                                                                                             |
|----------------------------------------------------|-----------------|------------------------|-------------------------------|-------------------------|---------------------------------------------------------------------------------------------|
| Use case                                           | Smart<br>Ticket | Secure<br>chip<br>card | Multi<br>applica<br>tion card | NFC<br>mobile<br>device | Comments                                                                                    |
| Identification when<br>registering and<br>ordering | -               | -                      | -                             | -                       |                                                                                             |
| Carrier medium<br>initialisation                   | -               | -                      | +                             | -                       |                                                                                             |
| Application loading                                | -               | -                      | +                             | +                       |                                                                                             |
| Entitlement loading                                | -               | -                      | +                             | +                       | Pre-configured NFC mo<br>bile devices may also be<br>available from the product<br>provider |
| Loading new enti<br>tlements                       | -               | -                      | +                             | +                       |                                                                                             |
| Delivery                                           | -               | -                      | +                             | +                       | Pre-configured NFC mo<br>bile devices may also be<br>available from the product<br>provider |
| Check-in                                           |                 |                        | +                             | +                       |                                                                                             |
| Check-out                                          | -               | -                      | +                             | +                       |                                                                                             |
| Entitlement check                                  | -               | +                      | +                             | +                       |                                                                                             |
| Blocking                                           | -               | +                      | +                             | +                       |                                                                                             |
| Key management                                     | -               | +                      | +                             | +                       |                                                                                             |

**Table 11–15 Use cases relevant to the "Interoperable entitlement withcalculation AFC" application scenario** 

<span id="page-162-0"></span>The following sub-sections will define safeguards for each carrier medium, on the basis of the threats described and the relevant use cases.

### **11.3.3.1 Safeguards when utilising the "multi-application card" carrier medium**

### Conditions particular to this case

The "Interoperable entitlement with AFC" product is normally issued on a "multi-application card" carrier medium.

Furthermore, in this application scenario it is assumed that entitlements of product type "Interoperable entitlement with AFC" will be loaded at a later stage onto carrier media of type "multi-application card", which are already in the customers' possession. This means that – assuming it is not yet there – the appropriate application will also have to be loaded later onto the card.

When using an existing "multi-application card", it must always be assumed that other applications and entitlements may already exist on the card. These other applications and entitlements may originate from different entities who have not necessarily agreed on common rules of usage and behaviour.

The entitlement and, where relevant, the application are loaded on at the sales point, a vending machine or via the Internet, provided a suitable reader is available.

When using this entitlement, checking in and checking out are necessary so as to facilitate invoicing between the service providers.

In systems with barriers, access to and from the blocked-off area is by means of the carrier medium and entitlement.

### Definition of safeguards

In the following table, safeguards are assigned to the threats in [Table 11–14.](#page-161-1) These safeguards are described in Section [8.4.](#page-66-1)

| Threat |                                                                                     | Safeguard      | Safeguard                                                                                                                                                                                                                                                               |
|--------|-------------------------------------------------------------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TC1    | Lack of compati<br>bility between<br>interfaces in car<br>rier medium and<br>reader | MS1.3<br>MR1.3 | 1<br>Introduction of interface tests and ap<br>proval procedures – Certification                                                                                                                                                                                        |
| TC2    | Eavesdropping                                                                       | MS2.3<br>MS3.3 | 1<br>Ensuring the confidentiality of commu<br>nication between carrier medium and<br>reader in order to prevent eavesdrop<br>ping – Mutual, dynamic authentication<br>during transmission<br>2<br>Introduction of contact-less interface as<br>defined by ISO/IEC14443. |
| TM1    | Unauthorised<br>scanning of enti<br>tlement                                         | MM1.3          | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection                                                                                                                                                               |
| TM2    | Unauthorised<br>overwriting / ma                                                    | MM1.3          | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad                                                                                                                                                                                           |

<span id="page-163-0"></span>

| Threat |                                                                        | Safeguard               | Safeguard                                                                                                                                                                                                                                                                                        |
|--------|------------------------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        | nipulation of enti<br>tlement                                          | MM11a.3<br>MM11b.3      | vanced access protection<br>2<br>Loading new entitlements – Securing<br>the authenticity and integrity of the enti<br>tlement – Complex authentication con<br>cept.<br>3<br>Loading new entitlements – Securing<br>the confidentiality of the entitlement –<br>Complex authentication concept    |
| TM3    | Cloning of me<br>dium including<br>entitlement                         | MM1.3<br>MM2.3          | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection<br>2<br>Protection against cloning of carrier<br>medium with entitlement – Advanced<br>protection against the cloning of carrier<br>medium and data content                            |
| TM4    | Emulation of ap<br>plication or enti<br>tlement                        | MM1.3<br>MM3.3          | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection<br>2<br>Protection against emulation – Ad<br>vanced emulation protection                                                                                                               |
| TM5    | Unauthorised<br>scanning of per<br>sonal data                          | MM1.3<br>MM4.3          | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection<br>2<br>Protection of personal data against re<br>trieval and overwriting/manipulation –<br>Advanced access protection for per<br>sonal data                                           |
| TM6    | Unauthorised<br>overwriting / ma<br>nipulation of per<br>sonal data    | MM1.3<br>MM4.3<br>MM6.3 | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection<br>2<br>Protection of personal data against re<br>trieval and overwriting/manipulation –<br>Advanced access protection for per<br>sonal data<br>3<br>Secure separation of applications |
| TM7    | Unauthorised<br>scanning of cal<br>culation data                       | MM1.3<br>MM5.3          | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection<br>2<br>Protection of calculation data against<br>retrieval and overwriting/manipulation –<br>Access and manipulation protection in<br>the case of interoperability                    |
| TM8    | Unauthorised<br>overwriting / ma<br>nipulation of cal<br>culation data | MM1.3<br>MM5.3          | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection<br>2<br>Protection of calculation data against<br>retrieval and overwriting/manipulation –<br>Access and manipulation protection in                                                    |

<span id="page-164-0"></span>

| Threat |                                                                    | Safeguard                                         | Safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------|--------------------------------------------------------------------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        |                                                                    |                                                   | the case of interoperability                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| TM9    | Protection of ad<br>ditional applica<br>tions and entitle<br>ments | MM6.3<br>MM10a.3<br>MM10b.3<br>MM11a.3<br>MM11b.3 | 1<br>Separation of applications – Secure<br>separation of applications<br>2<br>Loading new applications – Securing<br>the authenticity and integrity of applica<br>tions – Implementation of a reloading<br>mechanism as defined by ISO 7816-13<br>with SM Loading new applications –<br>Securing the confidentiality of applica<br>tions – Implementation of a reloading<br>mechanism as defined by ISO 7816-13<br>with SM<br>3<br>Loading new entitlements – Securing<br>the authenticity and integrity of entitle<br>ments – Complex authentication con<br>cept<br>4<br>Loading new entitlements – Securing<br>the confidentiality of entitlements –<br>Complex authentication concept |
| TM10   | Carrier medium<br>malfunction                                      | MM7.1                                             | 1<br>Specification of carrier medium charac<br>teristics – Manufacturer's declaration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| TM11   | Tracking by unau<br>thorised scanning<br>of UID                    | MM8.1                                             | 1<br>Introduce proximity technology as de<br>fined by ISO/IEC14443                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| TM12   | Lack of fallback<br>solution in the<br>event of malfunc<br>tion    | MM9.1                                             | 1<br>Fallback solution for carrier medium<br>malfunction – Introduction of appropri<br>ate fallback solutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

**Table 11–16 Safeguards for a "Interoperable entitlement with AFC" on a "multiapplication card"** 

### **11.3.3.2 Residual risks when utilising the "multi-application card" carrier medium**

For technical and commercial reasons, it is not always possible to eliminate threats completely using safeguards. In such cases a certain risk remains.

The residual risk should be determined and documented as part of the planning of the actual implementation.

### **11.3.3.3 Safeguards when utilising the "NFC mobile device" carrier medium**

Conditions particular to this case

The issuing of the "NFC mobile device" carrier medium type together with an entitlement is impossible to depict for reasons of cost and for operative reasons. In this application scenario we have therefore assumed that entitlements of product type "Interoperable entitlement with AFC" will be loaded at a later stage onto carrier media of type "NFC mobile device", which are already in the possession of the customer. This means that – assuming it is not yet there – the relevant application will also have to be loaded into the secure memory of the NFC mobile device.

When an existing "NFC mobile device" is being used, it must always be assumed that other applications and entitlements may already exist on the carrier medium. These other applications and entitlements may originate from different entities who have not necessarily agreed on common rules of usage and behaviour.

The entitlement and, where relevant, the application are loaded on over-the-air, at a sales point or at a vending machine.

In systems with barriers, access to and from the blocked-off area is by means of the carrier medium and entitlement.

#### Definition of safeguards

In the following table, safeguards are assigned to the threats in [Table 11–14.](#page-161-1) These safeguards are described in Section [8.4.](#page-66-1)

| Threat |                                                                                     | Safeguard                   | Safeguard                                                                                                                                                                                                                                                                                                                                                                      |
|--------|-------------------------------------------------------------------------------------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TC1    | Lack of compati<br>bility between<br>interfaces in car<br>rier medium and<br>reader | MS1.3<br>MR1.3              | 1<br>Introduction of interface tests and ap<br>proval procedures – Certification                                                                                                                                                                                                                                                                                               |
| TC2    | Eavesdropping                                                                       | MS2.3<br>MS3.3              | 1<br>Ensuring the confidentiality of commu<br>nication between carrier medium and<br>reader in order to prevent eavesdrop<br>ping – Mutual, dynamic authentication<br>during transmission<br>2<br>Introduction of contact-less interface as<br>defined by ISO/IEC14443                                                                                                         |
| TM1    | Unauthorised<br>scanning of enti<br>tlement                                         | MM1.3                       | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection                                                                                                                                                                                                                                                                      |
| TM2    | Unauthorised<br>overwriting / ma<br>nipulation of enti<br>tlement                   | MM1.3<br>MM11a.3<br>MM11b.3 | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection<br>2<br>Loading new entitlements – Securing<br>the authenticity and integrity of the enti<br>tlement – Complex authentication con<br>cept.<br>3<br>Loading new entitlements – Securing<br>the confidentiality of the entitlement –<br>Complex authentication concept |
| TM3    | Cloning of me<br>dium including<br>entitlement                                      | MM1.3<br>MM2.3              | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection<br>2<br>Protection against cloning of carrier<br>medium with entitlement – Advanced<br>protection against the cloning of carrier                                                                                                                                     |

<span id="page-166-0"></span>

| Threat |                                                                        | Safeguard                                         | Safeguard                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------|------------------------------------------------------------------------|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        |                                                                        |                                                   | medium and data content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| TM4    | Emulation of ap<br>plication or enti<br>tlement                        | MM1.3<br>MM3.3                                    | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection<br>2<br>Protection against emulation – Ad<br>vanced emulation protection                                                                                                                                                                                                                                                                                                                                         |
| TM5    | Unauthorised<br>scanning of per<br>sonal data                          | MM1.3<br>MM4.3                                    | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection<br>2<br>Protection of personal data against re<br>trieval and overwriting/manipulation –<br>Advanced access protection for per<br>sonal data                                                                                                                                                                                                                                                                     |
| TM6    | Unauthorised<br>overwriting / ma<br>nipulation of per<br>sonal data    | MM1.3<br>MM4.3<br>MM6.3                           | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection<br>2<br>Protection of personal data against re<br>trieval and overwriting/manipulation –<br>Advanced access protection for per<br>sonal data<br>3<br>Secure separation of applications                                                                                                                                                                                                                           |
| TM7    | Unauthorised<br>scanning of cal<br>culation data                       | MM1.3<br>MM5.3                                    | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection<br>2<br>Protection of calculation data against<br>retrieval and overwriting/manipulation –<br>Access and manipulation protection in<br>the case of interoperability                                                                                                                                                                                                                                              |
| TM8    | Unauthorised<br>overwriting / ma<br>nipulation of cal<br>culation data | MM1.3<br>MM5.3                                    | 1<br>Hardware and software access protec<br>tion (read and write access) – Ad<br>vanced access protection<br>2<br>Protection of calculation data against<br>retrieval and overwriting/manipulation –<br>Access and manipulation protection in<br>the case of interoperability                                                                                                                                                                                                                                              |
| TM9    | Protection of ad<br>ditional applica<br>tions and entitle<br>ments     | MM6.3<br>MM10a.3<br>MM10b.3<br>MM11a.3<br>MM11b.3 | 1<br>Separation of applications – Secure<br>separation of applications<br>2<br>Loading new applications – Securing<br>the authenticity and integrity of applica<br>tions – Implementation of a reloading<br>mechanism as defined by ISO 7816-13<br>with SM<br>3<br>Loading new applications – Securing<br>the confidentiality of applications – Im<br>plementation of a reloading mechanism<br>as defined by ISO 7816-13 with SM<br>4<br>Loading new entitlements – Securing<br>the authenticity and integrity of entitle- |

<span id="page-167-0"></span>

| Threat |                                                                 | Safeguard | Safeguard                                                                                                                                                         |
|--------|-----------------------------------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        |                                                                 |           | ments – Complex authentication con<br>cept<br>5<br>Loading new entitlements – Securing<br>the confidentiality of entitlements –<br>Complex authentication concept |
| TM10   | Carrier medium<br>malfunction                                   | MM7.1     | 1<br>Specification of carrier medium charac<br>teristics – Manufacturer's declaration                                                                             |
| TM11   | Tracking by unau<br>thorised scanning<br>of UID                 | MM8.1     | 1<br>Introduce proximity technology as de<br>fined by ISO/IEC14443                                                                                                |
| TM12   | Lack of fallback<br>solution in the<br>event of malfunc<br>tion | MM9.1     | 1<br>Fallback solution for carrier medium<br>malfunction – Introduction of appropri<br>ate fallback solutions                                                     |

#### **Table 11–17 Safeguards for a "Interoperable entitlement with AFC" on an "NFC mobile device"**

### **11.3.3.4 Residual risks when utilising the "NFC mobile device" carrier medium**

For technical and commercial reasons, it is not always possible to eliminate threats completely using safeguards. In such cases a certain risk remains.

The residual risk should be determined and documented as part of the planning of the actual implementation.

# <span id="page-168-0"></span>**12 Reference system "VDV Kernapplikation"**

The specification of the system solution VDV Kernapplikation was finalized in 2004. First implementations have been introduced in operations with several service providers in 2005. These systems support the application scenarios "electronic season ticket" and "Interoperable entitlement with AFC". Therefore the statements from chapter [8.4.1](#page-67-2) concerning existing installations apply for VDV Kernapplikation.

The existing implementations of VDV Kernapplikation deviate in some details from the examples given in chapter [10](#page-105-1) and chapter [11:](#page-134-1)

- 1 VDV KA doesn't employ specific safeguards against eavesdropping when transmitting entitlements over the contact-less interface as requested in MS2. KA allows a strict separation of entitlements and data related to a person. Personal data won't be transmitted together with an entitlement. In VDV KA the security target "Protection of the electronic entitlement" is reached even if the entitlement should be openly available. The following safeguards have been put in place to ensure this:
	- a Every entitlement is protected against manipulation by a MAC-mechanism.
	- b Loading, changing or deleting of an entitlement always requires a successful authentication between a valid carrier medium and the reader.
	- c The usage of an entitlement at the station or in the vehicle also requires a successful authentication between the carrier medium and the reader.

These measures do not only prevent manipulation but also emulation and copying of an entitlement onto another carrier media.

- 2 Asymmetric authentication between terminal and carrier media according to RSA uses keys of 1024 bits. The root key has a length of min. 1984 bits; the Sub-CA-Keys are using 1536 bits.
- 3 Symmetric authentication uses the TDES algorithm with keys of 112 bits.
- 4 MAC-protection is using a Retail-MAC based on TDES with keys of 112 bits.

A formal, detailed evaluation of VDV KA was not performed so far. From the current perspective the deviations are regarded as not critical. However, it is requested to introduce compliance to [ALGK\_BSI] with the next step of the system evolution.

# <span id="page-169-0"></span>**13 List of references**

### [RIKCHA]

Federal Office for Information Security: RFID – Security Aspects and Prospective Applications of RFID Systems, [https://www.bsi.bund.de/cln\\_174/ContentBSI/EN/publications/](https://www.bsi.bund.de/cln_174/ContentBSI/EN/publications/%0Brfid/RIKCHA_en_htm.html) [rfid/RIKCHA\\_en\\_htm.html](https://www.bsi.bund.de/cln_174/ContentBSI/EN/publications/%0Brfid/RIKCHA_en_htm.html), download from Sept. 15th 2009

#### [GSHB]

Federal Office for Information Security: IT Basic Protection Manual, [https://www.bsi.bund.de/](https://www.bsi.bund.de/%0Bcln_174/ContentBSI/grundschutz/intl/intl.html) [cln\\_174/ContentBSI/grundschutz/intl/intl.html,](https://www.bsi.bund.de/%0Bcln_174/ContentBSI/grundschutz/intl/intl.html) download from Sept. 15th 2009

#### [ISO 24014]

International Organization for Standardization: ISO 24014-1:2007 Public transport - Interoperable Fare Management System - Part 1: Architecture, [http://www.iso.org/iso/iso\\_catalogue.htm,](http://www.iso.org/iso/iso_catalogue.htm) download from Sept. 15th 2008

#### [IOPTA]

DIN EN15320:2008-02 Identifikationskartensysteme - Landgebundene Transportanwendungen - Interoperable Anwendungen für den öffentlichen Verkehr – Rahmenwerk (German) (Interoperable Public Transport Application - IOPTA),

<http://www.beuth.de/langanzeige/DIN+EN+15320/de/97592959.html>, download from Sept. 15th 2008

#### [VDV\_KM]

Verband Deutscher Verkehrsunternehmen (VDV): Spezifikation des Kundenmediums der VDV-Kernapplikation (German)

#### [ISO 7816-13]

International Organization for Standardization: ISO 7816-13 Identification Cards - Integrated Circuit Cards - Part 13: Commands for application management in a multi-application environment, [http://www.iso.org/iso/iso\\_catalogue.htm](http://www.iso.org/iso/iso_catalogue.htm), download from Sept. 15th 2008

#### [ALGK\_BSI]

Federal Office for Information Security: Technische Richtlinie Kryptographische Verfahren: Empfehlungen und Schlüssellängen (BSI TR-02102, German), [https://www.bsi.bund.de/](https://www.bsi.bund.de/cln_174/ContentBSI/Publikationen/TechnischeRichtlinien/tr02102/index_htm.html) [cln\\_174/ContentBSI/Publikationen/TechnischeRichtlinien/tr02102/index\\_htm.html,](https://www.bsi.bund.de/cln_174/ContentBSI/Publikationen/TechnischeRichtlinien/tr02102/index_htm.html) download from Sept. 15th 2009

#### [TR\_eCARD]

Federal Office for Information Security: Technische Richtlinie für die eCard-Projekte der Bundesregierung (BSI TR-03116, German), [https://www.bsi.bund.de/cln\\_164/ContentBSI/](https://www.bsi.bund.de/cln_164/ContentBSI/%0BPublikationen/TechnischeRichtlinien/tr03116/index_htm.html) [Publikationen/TechnischeRichtlinien/tr03116/index\\_htm.html,](https://www.bsi.bund.de/cln_164/ContentBSI/%0BPublikationen/TechnischeRichtlinien/tr03116/index_htm.html) download from Sept. 15th 2009

#### [BSI\_PICC\_TestSpec]

Federal Office for Information Security: Conformity Tests for Official Electronic ID Documents (formerly: ePassport Conformity Testing (TR-ePass)) (BSI TR-03105), Part 2 "Test Plan for ICAO Compliant MRTD with Secure Contactless Integrated Circuit" - Version 2.01.1, [https://www.bsi.bund.de/cln\\_164/ContentBSI/Publikationen/TechnischeRichtlinien/tr03105/in](https://www.bsi.bund.de/cln_164/ContentBSI/Publikationen/TechnischeRichtlinien/tr03105/index_htm.html) [dex\\_htm.html,](https://www.bsi.bund.de/cln_164/ContentBSI/Publikationen/TechnischeRichtlinien/tr03105/index_htm.html) download from Sept. 15th 2009

### [BSI\_PCD\_TestSpec]

Federal Office for Information Security: Conformity Tests for Official Electronic ID Documents (formerly: ePassport Conformity Testing (TR-ePass)) (BSI TR-03105), Part 4 "Test plan for ICAO compliant Proximity Coupling Device (PCD) on Layer 2-4" - Version 2.01.1, [https://www.bsi.bund.de/cln\\_164/ContentBSI/Publikationen/TechnischeRichtlinien/tr03105/in](https://www.bsi.bund.de/cln_164/ContentBSI/Publikationen/TechnischeRichtlinien/tr03105/index_htm.html) [dex\\_htm.html,](https://www.bsi.bund.de/cln_164/ContentBSI/Publikationen/TechnischeRichtlinien/tr03105/index_htm.html) download from Sept. 15th 2009

### [NFCIP2]

International Organization for Standardization: [ISO/IEC 21481:2005](http://standards.iso.org/ittf/PubliclyAvailableStandards/c040261_ISO_IEC_21481_2005(E).zip) Information technology - Telecommunications and information exchange between systems - Near Field Communication Interface and Protocol -2 (NFCIP-2), [http://www.iso.org/iso/iso\\_catalogue.htm](http://www.iso.org/iso/iso_catalogue.htm), download from Sept. 15th 2008

### [HW\_PP1]

Federal Office for Information Security: Smartcard IC Platform Protection Profile BSI-PP-0002-2001 Version 1.0, [https://www.bsi.bund.de/cae/servlet/contentblob/480416/](https://www.bsi.bund.de/cae/servlet/contentblob/480416/%0BpublicationFile/29278/ssvgpp01_pdf.pdf) [publicationFile/29278/ssvgpp01\\_pdf.pdf,](https://www.bsi.bund.de/cae/servlet/contentblob/480416/%0BpublicationFile/29278/ssvgpp01_pdf.pdf) download from Sept. 15th 2009

### [HW\_PP2]

Federal Office for Information Security: Security IC Platform Protection Profile BSI-PP-0035- 2007 Version 1.0, [https://www.bsi.bund.de/cae/servlet/contentblob/480302/publicationFile/](https://www.bsi.bund.de/cae/servlet/contentblob/480302/publicationFile/%0B29309/pp0035b_pdf.pdf) [29309/pp0035b\\_pdf.pdf](https://www.bsi.bund.de/cae/servlet/contentblob/480302/publicationFile/%0B29309/pp0035b_pdf.pdf), download from Sept. 15th 2009

# <span id="page-171-0"></span>**14 List of abbreviations**

| CICO    | Check-in / Check-out - Concept for validation of entitlements<br>and collection of calculation data. The passenger actively in<br>forms the system about the start and the end of his journey by<br>using his customer media at readers installed at the platform or<br>in the vehicle. |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DoS     | Denial of Service                                                                                                                                                                                                                                                                       |
| ECC     | Elliptic Curve Cryptography                                                                                                                                                                                                                                                             |
| EFS     | Electronic Ticket (Elektronischer Fahrschein)                                                                                                                                                                                                                                           |
| eID     | Electronic Identity                                                                                                                                                                                                                                                                     |
| ePA     | Elektronischer Personalausweis (German identity card)- May be<br>able to assume the function of the eID in the context of these<br>Guidelines.                                                                                                                                          |
| IFM     | Interoperable electronic fare management                                                                                                                                                                                                                                                |
| KA / CA | Kernapplikation / Core Application - Interoperable concept for<br>automated fare calculation by VDV                                                                                                                                                                                     |
| NFC     | Near Field Communication                                                                                                                                                                                                                                                                |
| NMD     | NFC Mobile Device, can be used as passive RF carrier medium<br>or control in "PCD-mode" the communication over the contact<br>less interface                                                                                                                                            |
| ÖPV     | Public Transport (Öffentlicher Personenverkehr)                                                                                                                                                                                                                                         |
| OTA     | Over-The-Air - Technical concept that supports the configura<br>tion of mobile devices over the mobile network                                                                                                                                                                          |
| PA      | Personalausweis – the German identity card                                                                                                                                                                                                                                              |
| RF      | Radio Frequency                                                                                                                                                                                                                                                                         |
| RFID    | Radio Frequency Identification                                                                                                                                                                                                                                                          |
| SAM     | Secure Authentication Module                                                                                                                                                                                                                                                            |
| UID     | Unique Identifier - A unique, non-changeable code belonging to<br>a chip                                                                                                                                                                                                                |
| UPS     | Uninterruptible Power Supply                                                                                                                                                                                                                                                            |
| VDV     | Association of German Transport Undertakings - In German:<br>Verband Deutscher Verkehrunternehmen                                                                                                                                                                                       |
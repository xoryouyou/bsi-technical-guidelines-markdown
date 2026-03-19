# Technical Guideline BSI TR-03184-2 Information Security for Space Systems 

Part 2: Ground Segment Version: 1.0 Date: 12.07.2025 

## Change history 

_Table 1: Change history_ 

|**_Version_**|**_Date_**|**_Description_**|
|---|---|---|
|1.0|12.07.2025|Firstpublication|
||||
|Revision cycle:|2|yearly|



Federal Office for Information Security P.O. Box 20 03 63 53133 Bonn weltraum.grundsatz@bsi.bund.de Internet: https://www.bsi.bund.de © Federal Office for Information Security 2021 

List of authors 

## List of authors 

The participants of the expert group "Information Security for Space Systems" initiated by the BSI in 2021 were involved in the development of the document “. 

_Table 2: List of authors_ 

|**_Name_**|**_Organisation_**|
|---|---|
|Dr. Johanna Niecknig|Federal Office for Information Security|
|Wendel Lohmer|Federal Office for Information Security|
|Florian Göhler|Federal Office for Information Security|
|Rabea Harnisch|Federal Office for Information Security|
|Katharina Schwab|Federal Office for Information Security|
|Vanessa Schwickart|Federal Office for Information Security|
|David Zabala Gepp|Federal Office for Information Security|
|Niclas Görgen|Federal Office of Civil Protection and Disaster Assistance|
|Stefanie Grundner|Panaglobo GbR|
|Manuel Hoffmann|Information Security Consulting Hoffmann|
|Niels Lerch|Niels Lerch IT-Beratung|
|Maximilian Roth|Airbus Defence and Space GmbH|
|Sascha Fankhänel|Jade Hochschule Wilhelmshaven|
|Andreas Ebhardt|DLR GfR mbH; Spaceopal GmbH|
|Aris Patronis|DLR GfR mbH|
|Christoph Möbius|CGI Deutschland B.V. & Co. KG|
|Dr. Björn Appel|INFODAS GmbH|
|Justus Bach|INFODAS GmbH|
|Dr. André Kubelka-Lange|OHB Digital Connect GmbH|



For technical quality assurance, the document was reviewed by: 

_Table 3: List of other parties involved in the creation of the Technical Guideline_ 

|**_Name_**|**_Organisation_**|
|---|---|
|Wim Fleischhauer|Rheinmetall Electronics GmbH|
|André Penzien|Rheinmetall Electronics GmbH|
|Daniel Kreschner|OHB System AG|
|Stefan Langhammer|OHB Digital Connect GmbH|
|Dr. Stephan Recher|CGI Deutschland B.V. & Co. KG|
|Sebastian Kasten|CGI Deutschland B.V. & Co. KG|
|Jens Ender|CGI Deutschland B.V. & Co. KG|
|Tarsicio López Delgado|Rivada Space Networks GmbH|



Federal Office for Information Security 

3 

Contents 

|Alexandra Gerling|TÜVIT|
|---|---|
|Matthias Petsch|TÜVIT|
|Serif Falay|IABG|



Federal Office for Information Security 

4 

Foreword by the Head of Department Protection of Classified Information and Cryptography 

## Foreword by the Head of Department Protection of Classified Information and Cryptography 

Since 2021, the Federal Office for Information Security (BSI) has maintained an interdisciplinary working group made up of experts from industry, administration and research, which deals with the cyber security of space systems. This working group has since become part of the "Cybersecurity in Space" expert group of the Alliance for Cybersecurity. 

The rapidly growing number of satellites and the expansion of a global network of ground infrastructures have significantly increased the vulnerability of satellite missions to targeted cyber-attacks. This considerably heightens the risk of successful attacks on individual satellites or entire constellations and requires a systematic analysis of possible attack vectors as well as a comprehensive assessment of potential damage scenarios, including ground segments. Particularly in view of the increasing strategic importance of satellite communication links for business and industry, it is imperative that the ground segment is regarded as an integral part of critical infrastructures and protected accordingly. 

This Technical Guideline "Information Security for Space Systems Part 2: Ground Segment" extends a continuously growing series of documents dedicated to the cyber security of space systems. Like the previous publications, this document is designed as a practical recommendation and detailed guide resulting in a comprehensive table that systematically assigns security measures for various identified threats. The recommendations, aspects and methods in this Technical Guideline are also intended to raise awareness of information security and its various forms among those responsible in this area to a high level of awareness. 

Our sincere thanks go to all members of the expert group "Cybersecurity in Space" and all other participants for their commitment to creating this Technical Guideline in proven quality through joint work with the BSI and to maintaining it in the future as well. 

## Dr. Günther Welsch 

Head of Classified Information Security and Cryptography Department 

Contents 

## Contents 

|Contents|Contents|
|---|---|
|List of abbreviations ................................................................................................................................................................................. 7||
|Terms .............................................................................................................................................................................................................. 8||
|1|Introduction ..................................................................................................................................................................................... 11|
||1.1<br>Objective of the document .............................................................................................................................................. 11|
||1.2<br>Structure of the document .............................................................................................................................................. 12|
|2|Description of operating ground segment .......................................................................................................................... 13|
|3|Application notes ........................................................................................................................................................................... 15|
||3.1<br>Scope of the Technical Guideline ................................................................................................................................. 15|
||3.2<br>Application of the Technical Guideline ..................................................................................................................... 16|
||3.2.1<br>Introduction .................................................................................................................................................................... 16|
||3.2.2<br>Procedure model for applying the TR .................................................................................................................. 16|
||3.2.3<br>Additional notes ............................................................................................................................................................. 18|
|4|Structure analysis ........................................................................................................................................................................... 20|
|5|Definition of protection needs ................................................................................................................................................. 22|
||5.1<br>Mission characteristics ...................................................................................................................................................... 22|
||5.2<br>Defining the security level ............................................................................................................................................... 22|
||5.3<br>Threats ..................................................................................................................................................................................... 23|
|6|Risk treatment ................................................................................................................................................................................. 25|
||6.1<br>Selection of suitable measures ....................................................................................................................................... 25|
||6.2<br>Security measures ............................................................................................................................................................... 25|
||6.3<br>Scenario modelling based on mission characteristics ......................................................................................... 26|
||6.3.1<br>Scenario 1: Incorrect transmission of an update to the on-board software ......................................... 26|
||6.3.2<br>Scenario 2: Leakage of sensitive data from a satellite model ...................................................................... 27|
||6.3.3<br>Scenario 3: Sabotage of the transmission and reception equipment of a ground station .............. 28|
|7|Cryptographic notes ..................................................................................................................................................................... 30|
|8|Outlook .............................................................................................................................................................................................. 32|
|9|Bibliography ..................................................................................................................................................................................... 33|



Federal Office for Information Security 

6 

List of abbreviations 

## List of abbreviations 

_Table 4: List of abbreviations_ 

|**_Abbreviation_**|**_Meaning_**|
|---|---|
|||
|BM|Securitymeasure(German: Bewältigungsmaßnahme)|
|BSI|Federal Office for Information Security|
|CCSDS|Consultative Committee for Space Data Systems|
|COTS|Commercial-off-the-shelf|
|DA|Official instruction|
|ECSS|European Cooperation for Space Standardization|
|EGSE|Electrical Ground Support Equipment|
|ESA|European Space Agency|
|G|Threat(German: Gefährdung)|
|GP|Businessprocess(German: Geschäftsprozess)|
|ISL|Inter-Satellite-Link|
|KDF|KeyDerivation Funktion|
|MGSE|Mechanical Ground Support Equipment|
|NIST|National Institute of Standards and Technology|
|OBSw|On-Board Software|
|OPS|Operations|
|SAT|Satellite|
|SAT ASW|Application-specific satellite softwareplatform andpayload|
|SAT GNS|Satellite Global Navigation System|
|SLE|Space Link Extension|
|TR|Technicalguideline(German: Technische Richtlinie)|
|TTC|Telemetry,Trackingand Command|
|VPN|Virtualprivate network|
|VS|Classified information(German: Verschlusssache)|
|WAN|Wide Area Network|



Terms 

## Terms 

_Table 5: List of terms used_ 

|**_Term_**|**_Description_**|
|---|---|
|Access (to system)|Access refers to the use of IT systems, system components and<br>networks. Access authorisations therefore allow a person to use<br>certain resources such as IT systems or system components and<br>networks.|
|Access (to data)|Access refers to the use of information or data. Access authorisations<br>are used to regulate which persons are authorised to use information,<br>data or IT applications or to carry out transactions within the scope<br>of their functions or IT applications.|
|Access (to site)|Admission refers to access to demarcated areas such as rooms or<br>protected areas on a site. Access authorisations therefore allow<br>people to enter certain environments, for example a site, a building<br>or defined rooms in a building.|
|Actor|An actor is a person acting within a system. The actor interacts with<br>other actors and with the infrastructure of the system.|
|Application|The information domain includes not only the processes but also the<br>programs that support the execution of these processes. In the life<br>cycle of satellite infrastructures, these include general applications<br>and services (e.g. e-mail service or data exchange service) as well as<br>space specific applications and services (e.g. analysis tools, EGSE,<br>simulators) and applications, components, devices and services<br>located on board the satellite(e.g.platform, payload,SAT controller).|
|Applied Threat|An applied threat is a threat that has a concrete effect on an object<br>via a vulnerability. A threat only becomes an applied threat to an<br>object through an existingvulnerability.|
|Attack|An attack is a deliberate form of endangerment, namely an<br>unwanted or unauthorised act with the aim of gaining an advantage<br>or harminga thirdparty.|
|Business Process|A business process is a set of logically linked individual activities<br>(tasks, workflows) that are carried out in order to achieve a specific<br>business or operationalgoal.|
|Classified Information|Classified information is information that must be kept secret in the<br>public interest. Classified information can exist in any form.<br>Examples include documents, audio or video files, data streams, but<br>also the spoken word. Classified information may only be disclosed<br>topersons who need to know it in order to fulfil their duties.|
|Ground Segment|The ground segment comprises all systems and components used for<br>communication with the space segment. The term includes the<br>operating ground segment, the user ground segment and the<br>antenna facilities.|
|Ground Station|A ground station refers to a station for the observation, monitoring,<br>or telemetryof satellites.|
|Information Security|Information security aims to protect information. Information can<br>be stored on paper, in IT systems or in human memory. The security<br>objectives or core values of information security are confidentiality,<br>integrity and availability. Many users include further core values in<br>their considerations.|



Federal Office for Information Security 

8 

Terms 

|**_Term_**|**_Description_**|
|---|---|
|Infrastructure|An infrastructure comprises all the physical and technical facilities of<br>a system.|
|IT- Infrastructure|IT-Infrastructures are technical facilities that are used for<br>information processing and form a self-contained functional unit.<br>Typical IT infrastructures are servers, clients, mobile phones,<br>smartphones, tablets, IoT components, routers, switches and<br>firewalls.|
|IT-System|An IT system comprises an IT infrastructure and the procedures for<br>its deployment, monitoring, control, operation, utilisation and<br>protection.|
|Keying (Key Injection)|Keying refers to the process of loading cryptographic key material<br>into crypto devices.|
|Launch Ground Segment|The launch ground segment are services and infrastructure that are<br>necessary for the launch. This includes the launch segment (on- and<br>off-shore)as well as landingfacilities for rocket stages.|
|Manipulation<br>(Tamper)|An unauthorised action on a system to cause a change in data and/or<br>intended behaviour.|
|Operator|In the context of this document, this term refers to the system<br>operator of a space system.|
|Operating Ground Segment|The operating ground segment comprises all components of the<br>ground segment that are necessary for the operation and<br>safeguarding of flight operations. This includes TTC ground stations<br>and antenna stations, as well as infrastructure operated as a service<br>for the above-mentionedpurpose.|
|Process|Processes describe how the components of a system (infrastructure<br>and actors)should interact so that the system fulfils its tasks.|
|Restricted Zone|Restricted zones are special forms of security areas with higher access<br>restrictions and security measures. They are usually located within<br>the securityarea.|
|Risk|The possibility that a threat becoming effective causes damage to<br>information, IT systems or business processes. The assessment is<br>based on the expected probability of occurrence and the extent of<br>damage that is caused in case of the damage event.|
|Risk Treatment|Risk treatment refers to the process of selecting and implementing<br>measures that have an impact on risks.<br>The aim is to lower the probability of the risk and/or reduce the<br>potential damage through suitable measures; see Security Measure.<br>Risk treatment typically falls into one of the following groups:<br>Risk Prevention<br>Risk Reduction/Control<br>Risk Acceptance<br>Risk Transfer|
|Risk Management|Risk management refers to all activities relating to the strategic and<br>operational handling of risks, i.e. all activities to identify,<br>analyse/assess, manage and monitor/control risks for an institution.<br>The aim of risk management is to reduce risks to an acceptable level.|
|Security Area|Security areas are areas to which only certain groups of people have<br>access. Access must be restricted by physical, logical and/or<br>organisational measures in order to regulate the presence of<br>employees as well as external serviceproviders and visitors.|



Federal Office for Information Security 

9 

TermsIntroduction 

|**_Term_**|**_Description_**|
|---|---|
|Security Control,<br>Countermeasure|A security measure is employed for risk treatment. It describes the<br>type and nature of the measure which has a direct impact on<br>identified risks. The security measure must be adapted to the project<br>with respect to how it is implemented, in order to achieve<br>appropriate effectiveness.|
|Security Level|The security level is determined by defining protection needs. It is<br>used to prioritise appropriate security measures. It generally has the<br>followingcharacteristics: normal,high,veryhigh.|
|Security Measure,<br>Safeguard, Measure|A security measure (or simply measure) refers to all actions that serve<br>to control and counteract security risks. This includes organisational<br>as well as personnel, technical or infrastructural security measures.<br>Securitymeasures serve to fulfil securityrequirements.|
|Security Requirement<br>(Control)|Security requirements are requirements for the organisational,<br>personnel, infrastructural and technical areas, the fulfilment of<br>which is necessary or contributes to increasing information security.<br>A security requirement therefore describes what has to be done to<br>achieve a certain level of information security. How the<br>requirements can be fulfilled in a specific case is specified in the<br>corresponding security measures. In the English-speaking world, the<br>term ‘control’ is often used for securityrequirements.|
|Space Infrastructure|The term space infrastructure covers all terrestrial and orbital<br>infrastructures (e.g. satellites, control centres, ground stations)<br>associated with the various functional phases of space systems, such<br>as operation and use, control, manufacture and aspects of protection.<br>The entire life cycle is considered.|
|Space Segment|The space segment includes all components that are located in space,<br>arepart of a mission and/or are required to fulfil the mission.|
|Space System|Space system summarises all segments of a space mission; space and<br>ground segments are to be considered as a combined system.|
|System|A system consists of various components (infrastructure and actors)<br>that interact with each other (according to processes) in order to<br>fulfil certain tasks.|
|Threat Actor, Attacker|An actor becomes a threat actor when there is motivation,<br>justification and opportunity for negative actions. Attackers can also<br>act on behalf of thirdparties who want togain advantages.|
|Threat|A threat is generally a circumstance or event that can cause damage.<br>The damage relates to the availability, integrity or confidentiality of<br>information.|
|User Ground Segment|The user ground segment refers to the services and infrastructure<br>that are relevant for the user or the use of thepayload.|
|Vulnerability|A vulnerability is a security-relevant error in a system or an<br>institution. The causes can lie in the design, the algorithms used, the<br>implementation, the configuration, the operation or the<br>organisation. A vulnerability can lead to a threat becoming effective<br>and an institution or system being damaged. Through a<br>vulnerability, an object (an institution or a system) becomes<br>susceptible to threats.|



Federal Office for Information Security 

10 

{PRIVATE & PERSONAL} 

Introduction 

## 1 Introduction 

Space technology is constantly advancing and the number of applications and players is steadily increasing. We mainly rely on satellite services in areas such as communication, navigation, monitoring the earth's surface and also in areas where precise time signals are used for synchronisation. With the increasing number of satellites and a global network of ground stations, the threats and possible effects of attacks are also growing. This applies to the entire space system, including the ground segment, space segment and communication links. The ground segment - the terrestrial infrastructure responsible for monitoring, control and data processing - requires special attention. Due to the diverse networking and different interfaces, this segment represents the primary point of attack for cyber operations against space systems. 

Ground stations often serve several missions at the same time. This makes them more attractive to a potential attacker, as he can inflict the greatest possible damage at this point. A basic distinction can be made between operating ground segments and user ground segments. This document deals with the protection of operating ground segments. 

The Technical Guideline (TR) is recommended by the BSI for considering the information security of ground segments and can be applied for each protection need category, i.e. for normal, high and very high protection requirements. The protection need category is taken into account by an appropriate design and implementation of the security measures. 

The TR is aimed at both contractors and clients. It is based on the IT-Grundschutz Methodology in accordance with BSI Standard 200-2 [1]. This means that the TR is also compliant with ISO 27001/27002 [2]. However, the use of the IT-Grundschutz Methodology is not mandatory for the use of the TR; it can also be used with other ISO 27001/27002-compliant approaches. 

In comparison with the ‘IT-Grundschutz-Profile for Space Systems Part 2: Ground Segment - Minimum Protection over the Entire Life Cycle’ [3] the TR allows for a deepening and detailing of the requirements for the ground segment. It builds on the findings of the 'IT-Grundschutz-Profile for Space Systems Part 2: Ground Segment' [3], identifies and addresses the risks and explains the differences in the business processes (BP) in relation to the protection requirements with concrete application examples and scenarios. 

In conjunction with ‘TR-03184 Information Security for Space Systems Part 1: Space Segment’ [4] this results in a seamless consideration of the security requirements of the space segment and ground segment in the same way and depth. 

## 1.1 Objective of the document 

The objective of the TR is to establish an appropriate standard of information security in aerospace; it can be part of a statement of work. To this end, the document provides a catalogue of applications, threats and security measures (BMs) and relates these to each other. 

This approach facilitates the implementation of information security. Those responsible for the respective business processes can use this document to analyse the applications relevant to them, identify risks and derive BMs. 

The result is a list for the implementation of risk-mitigating BMs. 

For the considerations analogous to the IT-Grundschutz-Profile, six business processes, based on the life phases according to ECSS [5], are considered relevant, i.e.: 

- Business process 0: General IT infrastructure, 

- Business process 1: Conception and design, 

- Business process 2: Manufacturing, 

- Business process 3: Preparation of operations, 

{PRIVATE & PERSONAL} 

Introduction 

- Business process 4: Operation, 

- Business process 5: Decommissioning. 

## 1.2 Structure of the document 

After a chapter on the basics, in which the structure of an operating ground segment and some elementary terms are explained, Chapter 3 provides information on the application and delimitation of the TR. Chapter 3.2 guides the user of the TR through the process of utilising the results in order to extract project-specific requirements. Chapter 4 presents the applications considered. Chapter 5 discusses security objectives and threats. Chapter 6 introduces the security measures and assigns them to the threats (categorised by business processes/applications). Selected scenarios are explained to help with the application of the resulting ‘assignment table’. Cryptographic notes are presented in Chapter 7 and Chapter 8 provides the reader with a brief outlook. The complete tables on threats, security measures and the assignment table can be found in the appendix to this document ‘Threats and Security Measures’. 

Federal Office for Information Security 

12 

{PRIVATE & PERSONAL} 

Description of operating ground segment 

## 2 Description of operating ground segment 

The operating ground segment comprises all components of a space system that are necessary for tracking and commanding the spacecraft from the ground. This enables the operation of the payloads and the actual execution of the mission tasks. 

Figure 1 shows the division of a space system into space and ground segments used in this TR. The communication links are assigned to the space segment so that the antenna tips of the ground station represent the interface between the space and ground segment. 


![](markdown/tr/BSI-TR-03184_EN/BSI-TR-03184_EN.pdf-0013-05.png)


_Figure 1: System boundaries and interfaces_ 

The operating ground segment consists of one or more ground control stations and one or more TTC antenna stations. Antennas and ground control stations are connected via a local or wide area network and do not have to be located at the same site. Depending on the mission requirements, parts of the ground segment can also be mobile. 

The aim of TTC communication is to establish a secure connection between the satellite control centre and the satellite platform. The operating ground segment and/or the antenna stations may be provided by external service providers ‘as-a-service’. 

The tasks of the operating ground segment are: 

- Manoeuvre planning, incl. course recommendations, e.g. from the Space Situational Awareness Centre and consideration of space weather; 

Federal Office for Information Security 

13 

{PRIVATE & PERSONAL} 

Description of operating ground segment 

- Safeguarding communication with the space segment for telemetry, tracking and command (TTC): 

   - **Telemetry** for the data received at the operating ground segment, 

   - **Tracking** for monitoring the orbit of a spacecraft and distance measurement via special sensors of a TTC ground station, e.g. radar or radio location. Tracking is one of the special functions that distinguishes the TTC ground station from a normal ground station (downlink only, possibly also uplink). 

   - **Command** for the data sent by the operating ground segment and 

- 

- 

- 

   - Control of the antennas; 

   - Monitoring of the operational status and orbit; 

   - Safeguarding the mission objective; 

- Providing and management of interfaces, e.g. to external providers of ground station networks and services, or for information on mission planning. 

Federal Office for Information Security 

14 

{PRIVATE & PERSONAL} 

Application notes 

## 3 Application notes 

## 3.1 Scope of the Technical Guideline 

The elements considered in this TR are marked in green in Figure 2. The description of the applications listed therein can be found in Chapter 4. All elements of the space segment are covered in the ITGrundschutz-Profile for Space Infrastructures [3] and are therefore not part of the information domain in this document. The communication links between the space segment and the operating ground segment were also assigned to the space segment, resulting in the ground station antennas as the interface between the space segment and the ground segment. Direct communication between spacecrafts (inter-satellite link, ISL) is also assigned to the space segment in this consideration. 

In addition, the user ground segment and associated processes are not taken into account in order to allow a sharp and meaningful differentiation of the Technical Guideline. However, the IT-Grundschutz Methodology in general and the knowledge gained from the Technical Guideline can be transferred accordingly by the user in order to obtain a holistic protection concept. 


![](markdown/tr/BSI-TR-03184_EN/BSI-TR-03184_EN.pdf-0015-06.png)


_Figure 2: Structure and elements of the operating ground segment_ 

The scope of consideration does not include: 

- Space segment and the assigned development, test and launch processes on the ground, 

- Interfaces between the operating ground segment and external service providers (e.g. Space Situational Awareness), 

- In the user ground segment: 

   - Communication with the payload, 

   - Processing of received payload data, 

   - Customer management, user administration and similar services. 

However, manufacturers and operators of an operating ground segment are required to ensure that a comparable security level can also be demonstrated in these systems by the operator. 

Federal Office for Information Security 

15 

{PRIVATE & PERSONAL} 

Application notes 

## 3.2 Application of the Technical Guideline 

## 3.2.1 Introduction 

This chapter shows how this Technical Guideline is applied. The process for implementing the TR is described by way of example, from analysing the existing IT landscape to selecting suitable measures and adapting them to protection needs and criticality. 

The TR can be applied to existing systems in order to subsequently improve information security. It can also be used for systems that are still being planned in order to integrate security measures into the design as early as possible (security-by-design). Early consideration and implementation of information security ensures a high level of effectiveness and is generally more cost-efficient than subsequent implementation. 

The TR follows a risk-based approach. It focuses on components in the operating ground segment that are not covered by the IT-Grundschutz Compendium. A generic risk analysis was carried out for these components as part of the annex documents and recommendations for mitigation are given, see Annex ‘Threats and Security Measures’. The recommendations of the IT-Grundschutz Compendium [6] should be followed for cross-sectional IT components. 

The TR provides targeted assistance for identifying threats and gives recommendations for risk mitigation. For this purpose, possible threats are considered and mitigated by BMs on an application-related basis. The security measures to be adapted by the project help the user in formulating project-specific requirements. This requires mission- or project-specific customisation (tailoring). The threats described must be fully examined by the user and the recommended BMs must be applied and designed in such a way that the risks of all identified threats are reduced to an acceptable level. 

The plausibility of the threat for the project-specific application is checked, as well as an unconsidered delta that has yet to be defined by the project. The design/implementation of the security measure is determined by risk, the probability of occurrence, the resulting damage and the economic efficiency. 

## 3.2.2 Procedure model for applying the TR 

The TR is based on the IT-Grundschutz Profile Part 2: Ground Segment [3]. The BSI recommends the prior application of the profile. The following steps are described there in detail: 

- **Assessment of the IT landscape.** The comprehensive identification of all IT systems, IT applications and IT components is essential. This is done as part of the structure analysis. This can involve the mapping to the applications in the annex to the "IT-Grundschutz Profile for Space Infrastructures" [7]. 

- **Defining protection needs** : As part of the definition of protection needs, the protection needs of the individual IT components are determined. This is derived from the underlying business processes. 

- - **Assignment of the IT-Grundschutz modules:** The IT-Grundschutz profile provides a generic assignment of modules to the components of the operating ground segment. 

The following necessary steps are covered in the Technical Guideline: 

**Identification of relevant threats:** As there are no tailored modules for the operating ground segment comparable to the IT-Grundschutz Compendium, the identification of threats follows the definition of protection needs. Threats relevant to the system under consideration are identified on the basis of the documented system structure. The list of threats presented in the appendix ‘Threats and Security Measures’ can serve as a basis for this. 

Furthermore, it must be verified whether additional threats exist for the particular application case (e.g., based on project-specific features). 

Federal Office for Information Security 

16 

{PRIVATE & PERSONAL} 

Application notes 

- **Risk analysis.** The risks for the operation of the ground station are derived from the threats. Potential risks must be identified and evaluated. The IT-Grundschutz Methodology[1] can be applied here. 

- **Risk treatment:** Depending on the individual assessment, additional measures can be taken to mitigate the risks. Recommendations for BMs can be found in the appendix ‘Threats and Security Measures’. 

When applying this methodology, several procedures are carried out for each business process identified in the structure analysis. 


![](markdown/tr/BSI-TR-03184_EN/BSI-TR-03184_EN.pdf-0017-05.png)


_Figure 3: Procedure (workflow) for the methodology_ 

In Figure 3, the procedures ‘Identify relevant application’, ‘Identify relevant threat’, ‘Perform risk assessment’ and ‘Identify and assign security measure’ have a decision-making character. The procedure 

1 In particular, the BSI 200-3 risk management standard [10]. 

Federal Office for Information Security 

17 

{PRIVATE & PERSONAL} 

Application notes 

‘Complete project documentation accordingly’ is used to document all decisions that are intended to promote the flow of communication and transparency. The procedure ‘Carry out risk assessment’ and the use of appropriate methods is the responsibility of the user and his risk management; the description of this procedure is not part of the TR. 

The first step of the proposed methodology starts with the ‘Identification of relevant application’ procedure for the respective BP (see section 1.1). In this procedure, the user checks for the BP whether the applications identified in the TR apply, and adapts them for the specific project. Applications that have been identified as ‘not relevant’ in the BP under consideration must be documented accordingly and can be discarded. Applications that do exist, but are missing within the scope of the TR must be identified, added and taken into consideration. 

The procedure ‘Determination of the qualitative design of the security measure’ and the documentation form the conclusion of the methodology and of the figure and initiate further process sequences for implementation by the user. 

After the ‘Identification of relevant application’, the second step is the procedure ‘Identification of relevant threats’. The threats for the project-specific applications in the BP must be identified and added by the user of this TR, or can be edited as not applicable. The documentation follows the same procedure as before. 

Subsequently, the ‘Perform risk assessment’ procedure follows. It is mandatory to carry out a standardised risk assessment (e.g. as per ISO 27005 [8], 31010 [9] or BSI-Standard 200-3 [10]) of the identified threat(s). 

Each BP should be considered individually, as the respective risks differ with respect to infrastructure, personnel and processes. The BPs can run in parallel, but also consecutively, and the rating (or possibly ‘the level of categorisation’) of the security objectives in the BPs can differ from one another. 

After the ‘Risk assessment’, the fourth step in the ‘Identify and assign security measures’ procedure is to assign the security measures to the threats. The user (for each BP) must check whether all threats have been identified and which security measure(s) reduce the risk of a threat; these must be assigned to the threat accordingly. If security measures have been identified as ‘not relevant’ for an application, they can be discarded after appropriate documentation. Relevant security measures that are missing in the TR must be identified, added and taken into consideration. 

In the fifth step, the procedure ‘Determining the qualitative design of the security measure’ must be used to check whether the proposed security measure(s) are sufficient to mitigate the threat in accordance with the risk assessment, or how these security measure(s) are to be designed/implemented. 

Risk management methods must be applied to check whether all threats have been considered and whether any residual risk can or must be accepted. 

## 3.2.3 Additional notes 

The implementation of the TR is an ongoing process. The structure analysis and implementation of the measures must be continuously reviewed and adapted. Changes in the IT landscape, new threats and the state of the art must be taken into account here. 

The perspective on the implementation and/or the perspective on the information security management system differs between the process of manufacturing and the process of operation. With regard to the planning and manufacturing phase, the focus of information security is on the product. Here, information security must be implemented in the product - operating ground segment - or the individual increments. For this reason, the system is planned, manufactured and configured accordingly. Appropriate product documentation with regard to information security must be created in the context of its deployment, e.g. as part of project work. 

When the product - operating ground segment - is transferred to operations, information security must be considered from an organisational perspective. The requirements, processes and guidelines must be implemented and continuously improved in accordance with the Plan-Do-Check-Act procedure. 

Federal Office for Information Security 

18 

{PRIVATE & PERSONAL} 

Application notes 

For the realisation of the TR, some of the information security documentations from BSI Standard 200-2 [1] must be created. This includes the structure analysis and the definition of protection needs. In addition, the risk analysis that may be necessary must be documented. The BSI's list ‘Übersicht konsolidierte DA im ITGrundschutz” des BSI [11] provides an overview of the documents to be created (in German). 

This TR provides the user with a scheme for identifying risks and assigning security measures based on the structure analysis of a typical operating ground segment. 

Federal Office for Information Security 

19 

{PRIVATE & PERSONAL} 

Structure analysis 

## 4 Structure analysis 

Below, the applications considered in this TR are described. In comparison to the list of applications in the BSI document ‘IT-Grundschutz Profile for the Ground Segment‘ [3], the considerations are limited to the applications that are not sufficiently covered in the IT-Grundschutz modules. The ‘Business process 0: General IT infrastructure’ is therefore not explicitly examined, some applications of this business process can be found in other business processes. 


![](markdown/tr/BSI-TR-03184_EN/BSI-TR-03184_EN.pdf-0020-04.png)


_Figure 4: Relationship between business processes and applications_ 

The assignment of the applications to the business processes is shown in Figure 4. 

Note: Applications can be assigned to several business processes. The following applications are considered: 

A101 On-Board Software Management Procedures and tools for managing, testing and installing the OBSw. 

A102 Antenna applications Applications for controlling the antenna and the necessary TTC operations. 

A103 Antenna 

The antenna as infrastructure including hardware and processes. 

Federal Office for Information Security 

20 

{PRIVATE & PERSONAL} 

Structure analysis 

## A104 Education 

Central system for the provision of educational and training materials, organising, monitoring and documenting the training of operators and maintenance personnel. 

## A105 Satellite model 

Model of the satellite remaining on the ground. 

## A106 Operations 

Tools that ensure operations. Ground control systems, administration of security keys for satellite communication, flight dynamics, TTC operations, etc. 

## A214 Soft-/Hardware Test Tools 

Software/hardware test tools comprise all tools for testing software/hardware. These can be stationary or portable tools. Examples are networkable oscilloscopes or digital multimeters. Depending on the application, only the software or the entire device can be considered as a unit. This is contingent on the hardware employed (COTS or Embedded). 

## A215 Simulators 

Simulators are both hardware- and software-based simulation environments. These can be used for testing, training and mission purposes. The exact scope must be defined by the project. 

To ensure that results, assessments, and changes to the structure analysis are comprehensible and can be checked later and by third parties, it is important that they are carefully documented, see [11]. 

Federal Office for Information Security 

21 

{PRIVATE & PERSONAL} 

Definition of protection needs 

## 5 Definition of protection needs 

## 5.1 Mission characteristics 

The following key characteristics were identified for the evaluation of a mission: 

- Mission type 

- Orbit or Earth orbit 

- Constellation size 

- Stakeholder/Purpose and 

- Infrastructure 

The mission type defines the requirements for the overall system. Examples of mission types are Earth observation, navigation or communication. The mission type has a direct influence on all subsequent factors. The mission characteristics under consideration subsequently form the basis for an appropriate definition of protection needs. 


![](markdown/tr/BSI-TR-03184_EN/BSI-TR-03184_EN.pdf-0022-11.png)


_Figure 5: Mission characteristics_ 

Figure 5 **Fehler! Verweisquelle konnte nicht gefunden werden.** shows which mission characteristics are used to carry out a case study for the project to be implemented. For this purpose, mission type, orbit, constellation size, stakeholders/purpose and infrastructure must be combined according to the requirements. From this, various requirements can be developed and the systems’ protection needs determined, see also Chapter 11 Mission characteristics of the IT-Grundschutz Profile for Space Systems Part 2: Ground Segment [3]. 

## 5.2 Defining the security level 

The IT-Grundschutz Methodology in accordance with BSI Standard 200-2 [1] can be used to determine the protection needs. This chapter is also based on this. 

There are helpful standardisation initiatives, overviews and frameworks aimed at identifying and mitigating cybersecurity threats in space systems, such as.: 

- The Aerospace Corporation - Space Attack Research and Tactic Analysis (SPARTA) [12] 

- ECSS (ECSS-Q-ST-80-10C DIR1) [5] 

- CCSDS (Security Threats against Space Missions) [13] 

- ESA - Space Attacks and Countermeasures Engineering Shield (SPACE-Shield) [14] 

- Mitre Corporation - Adversarial Tactics, Techniques, and Common Knowledge (ATT&CK) [15] 

- ISO 27001 [2] 

- NIST Cybersecurity Framework [16] 

Federal Office for Information Security 

22 

{PRIVATE & PERSONAL} 

Definition of protection needs 

The security level of the measures to be implemented should correspond to the protection needs of the information and processes to be protected. In order to carry out an assessment, the security objectives of confidentiality, integrity and availability are classified into protection need categories. This assessment should be considered application-specific for each business process and agreed upon between the client and contractor. 

It should be noted that the protection needs of the security objectives can be assessed differently depending on the business process due to different parameters in the infrastructure, personnel, processes and goals, as the following example illustrates using the business processes ‘Preparation for operation’ and ‘Operation’: 

## Example: 

Applications that are used for training in preparation for operation may have different requirements in terms of security objectives than applications that are required during operation. In training, simulations are used to command and control the satellite and monitor the orbit. If these simulation environments fail, training units cannot be carried out, there is no direct impact on the mission. Errors in the simulation system are tolerable, downtime has no impact and repair/recovery can be attempted within a reasonable period of time. 

The protection needs of a mission as a whole affect all applications, systems, networks, rooms and buildings required for the mission. The protection needs can differ in the individual life phases and processes and must be adapted or checked accordingly, e.g. the availability of a system in GP204 ‘Integration and testing’ is not of high priority. The failure of a test system does not usually cause major damage, even if the system is unavailable for several days. The situation is different for systems that are required for productive operation. In this case, even a failure lasting a few hours can cause significant damage. Depending on the project status, other type of information may become relevant in the same GP, which may have different protection needs. 

The protection needs may change as the GP progresses. For example, during the ‘operation’ GP, availability is generally a high-priority feature required for the business purpose. The protection needs must therefore be checked and adapted to the conditions of the actual GP accordingly. 

Simulation programmes are also employed during operations for orbital determination, collision avoidance, etc. However, if decisions have to be made on the basis of a simulation and these are not available, the impact on the mission can be considerable. 

A comparison of the protection needs defined in the example is shown in Figure 6. 

|**Preparation for operation**|**Preparation for operation**|**Preparation for operation**||||**Operation**|**Operation**||
|---|---|---|---|---|---|---|---|---|
|**Simulator**|normal|high|very<br>high||**Simulator**|normal|high|very<br>high|
|Confidentiality|X||||Confidentiality||X||
|Integrity|X||||Integrity|||X|
|Availability|X||||Availability|||X|



_Figure 6: Exemplary determination of protection requirements for operational preparation and operation_ 

## 5.3 Threats 

Based on the assumptions and experience of the authors and the content of the IT-Grundschutz, the relevant threats to the security objectives of confidentiality, integrity and availability are identified in the appendix to this document ‘Threats and Security Measures’. 

Federal Office for Information Security 

23 

{PRIVATE & PERSONAL} 

Definition of protection needs 

The elementary threats of the IT-Grundschutz Compendium are checked, adapted and completed with regard to their relevance for the operating ground segment. 

Federal Office for Information Security 

24 

{PRIVATE & PERSONAL} 

Risk treatment 

## 6 Risk treatment 

The risk of the individual threats is determined by evaluating the probability of occurrence and the potential level of damage; for the procedure, see also BSI Standard 200-3 ‘Risk analysis“ [10]. 

With the help of the BMs assigned to each threat, the risk can be reduced. There are usually several BMs assigned to a threat. A BM can reduce the risk for one or more threats. 

The protection requirements of a target object can change depending on the GP, current situation, framework conditions, etc.; see also Chapter 5. The implementation of the BM must therefore be adapted to the individual protection requirements of the target object and the BM must be translated into corresponding security requirements. 

A list of all the BMs considered can be found in the separate appendix ‘Threats and Security Measures’. 

## 6.1 Selection of suitable measures 

This TR provides a preselection of BMs that can be used to mitigate a threat. However, the quality of the measures is determined by the respective project according to the need for protection. 

Important criteria for the selection of suitable BMs are: 

**Effectiveness of the security measures:** Does the BM actually reduce the risk? Is the BM technically and organisationally effective? 

**Economic efficiency:** How high is the cost of implementation and maintenance? Is the BM economically justifiable (cost-benefit ratio)? 

**Legal and regulatory requirements:** Are there any legal requirements, standards or guidelines that enforce or prohibit the selection of certain BMs, or that have already led to certain BMs being considered in advance? Are there specifications that influence the way a BM is implemented? 

**Acceptance and user-friendliness:** Is the BM easy to implement and use? Does the BM affect employee productivity? 

**Scalability:** Can the BM grow with the company? Is the BM equipped to deal with future threats? **Interoperability and integration:** Can the BM be integrated into existing systems and processes? Does it cause compatibility problems? Are there functional overlaps between several already implemented or planned BMs? 

## 6.2 Security measures 

Security measures are all measures that can directly minimise a risk. One or more BMs can be assigned to a threat. The BM describes what must be implemented, not the way in which something is implemented. 

If BMs are not applicable in the specific project, explanatory documentation is required. A risk assessment and alternative security measures must be described. BMs already intended for other threats may also have an indirect effect on other threats under certain circumstances. 

The occurrence of damage cannot be completely ruled out if the BMs are assigned. An appropriate assignment and design of the measures can reduce the probability of occurrence or the impact. 

A BM can be assigned to a threat if the influence of the measure has a direct effect on the risk posed by the threat in question. If an entity is added to the causal chain for the effect, the measure no longer has a direct effect. In the case of the threat of unauthorised access to a room, the BMs that affect the room have an effect, not those for the building. At IT level, a security measure directly protects the software. No influence of possible hardware is considered - analogously, this must be considered the other way round. 

Federal Office for Information Security 

25 

{PRIVATE & PERSONAL} 

Risk treatment 

The appendix ‘Threats and Security Measures’ contains an assignment table in which the BMs are generically assigned to the threats - categorised according to the business processes. This assignment must be checked when applied to the requirements of the project and the protection needs. 

## 6.3 Scenario modelling based on mission characteristics 

The requirements for the elements of the operating ground segment are defined by the respective mission. Parameters such as the security objectives and orbit of the satellites to be controlled or the frequency of contact with the satellites are important here. For this purpose, important parameters can be linked, as shown in Figure 6, in order to model missions and derive protection requirements from them. 

The type of mission influences both the orbit to be used and the size of the constellation. This results in the frequency of contact, which in turn allows conclusions to be drawn about the required number of ground stations. If frequent contact is required and the satellites do not necessarily have to be controlled by the user, ground stations can be used ‘as a service’. In this case, the service providers must be selected according to the protection requirements. Specifications for compliance with the protection requirements of the provider must be defined and regularly audited. Purpose and infrastructure are also factors that define the quality of the implementation of measures. 

Selected scenarios are used below to illustrate how vulnerabilities can potentially be exploited. The scenarios are also intended to support the qualitative assessment of the BM. For this purpose, an application in a selected business process that is exposed to a specific threat is considered. Each scenario shows which attacks are possible and how they can be defended against by various BMs. The scenarios only contain selected BMs; they do not describe the effectiveness of all assigned BMs. They illustrate measures that minimise the probability of occurrence of the scenario described as far as possible. 

The following scenarios are considered: 

- Scenario 1: Incorrect transmission of an update to the on-board software 

- Scenario 2: Leakage of sensitive data from a satellite model 

- Scenario 3: Sabotage of the transmitting and receiving equipment of a ground station 

## 6.3.1 Scenario 1: Incorrect transmission of an update to the on-board software 

Table 6 explains the affected business process, the application under consideration, the threat under consideration and the BMs described for scenario 1. 

_Table 6: Summary of scenario 1_ 

|**_Application_**|**_A102 On-Board-Software_**|
|---|---|
|Possible affected business processes|Operation|
|Threat|G02 Loss of integrity of information|
|Security measures for G02|BM5 Integrity check of the software supply chain<br>BM14 Use the checksum verification method<br>BM54 Use encrypted communication<br>BM56 Integrity check of sent/received information|
|Cause|Technical failure|



## **Affected business processes/risk description** 

In the business process operation, a technical malfunction disrupts the management of the on-board software, which leads to on-board software that deviates from the specification being installed on a satellite. 

Federal Office for Information Security 

26 

{PRIVATE & PERSONAL} 

Risk treatment 

## **Persons involved** 

Since this is a technical malfunction, no specific group of people can be attributed as the trigger. 

## **Description of the scenario** 

On-board software is typically developed by or on behalf of the satellite manufacturer and provided to the operator upon completion so that the operator can transmit the software to the satellite using on-board software management tools. 

The integrity of the software is exposed to the risk of integrity loss during all transmissions: 

- At the manufacturer: defective transmission from the development system to the transport media (data storage device) to be used for transferring the software to the satellite operator. 

- During transport: Damage to the data storage device. 

- At the satellite operator: defective transmission from the data storage device to the management system. 

- During transmission from the ground segment to the satellite. 

## **Effect of the security measures** 

BM5, BM14 and BM54 use cryptographic and organisational measures to effectively protect the integrity of data. The cryptographic measures in this case are the use of hash functions or checksum verification that allow a recipient to check the integrity of information. The organisational measures include physical protection against manipulation, e.g. sealed letters/transport containers, personal handover and auditing of suppliers. 

## 6.3.2 Scenario 2: Leakage of sensitive data from a satellite model 

Table 7 explains the affected business process, the application under consideration, the threat under consideration and the BMs described for scenario 2. 

_Table 7: Summary of scenario 2_ 

|**_Application_**|**_A106 Satellite model_**|
|---|---|
|Possible affected business processes|Manufacturing (integration and testing), operation (on-board<br>software management))|
|Threat|G04 Interception of Information / Espionage|
|Security measures for G04|BM33 Supervised presence of visitors/external personnel in a<br>restricted zone<br>BM42 Keeping documents and media under lock and key<br>BM54 Use encrypted communication|
|Cause|Intention|



## **Affected business processes/risk description** 

The satellite model is accessed in the manufacturing or operation business process with the aim of obtaining sensitive data that can be used for further attacks in the future. 

## **Persons involved** 

An actor gains access to information in order to use it for their own purposes. 

## **Description of the scenario** 

A person infiltrating the company (e.g. external service provider) accesses the satellite model without authorisation. Through direct interaction with the model, the person gains access to sensitive data such as 

Federal Office for Information Security 

27 

{PRIVATE & PERSONAL} 

Risk treatment 

the specification of the structure of telecommands or the internal structure of the satellite. In addition, the physical characteristics of the model - if it is an operational model (‘flight model’) - allow conclusions to be drawn about other technical characteristics, such as energy requirements or special hardware components. This information can subsequently be used by a hostile party to carry out attacks on the satellite mission. 

## **Effect of the security measures** 

BM33 ensures that the infiltrated person can only operate in company areas where a satellite model is located if accompanied at all times. This makes it more difficult for the person to interact with the model unnoticed and effectively reduces the risk of attack. 

BM42 ensures that sensitive media, such as the satellite model, are stored separately and securely. If the model is stored in safes, the person cannot access it and the risk of attack is effectively reduced. 

BM54 makes it difficult for the person to access the sensitive information, since all interfaces only exchange data in encrypted form. However, BM54 cannot prevent the person from accessing components of the model that process decrypted data. 

## 6.3.3 Scenario 3: Sabotage of the transmission and reception equipment of a ground station 

Table 8 explains the affected business process, the application under consideration, the threat under consideration and the BMs described for scenario 3. 

_Table 8: Summary of scenario 3_ 

|**_Application_**|**_A103 Antenna_**|
|---|---|
|Possible affected business processes|Operation|
|Threat|G20 Vandalism|
|Security measures for G20|BM1 Setting up a security area/restricted zone<br>BM32 Transport of hardware/documents by trustworthy<br>personnel<br>BM33 Supervised presence of visitors/external personnel in a<br>restricted zone|
|Cause|Intention|



## **Affected business processes/risk description** 

During the business process operation, an antenna is damaged by sabotage with the aim of preventing the tracking and commanding of satellites. 

## **Persons involved** 

Attacks of this kind can be carried out by people on the company premises or by kinetic remote effects such as projectiles or drones. Potential attackers include hostile states, terrorist groups, competitors or activists. Similar attacks can also be realised through interventions in the supply chain, but this vector is not considered as part of this example scenario. 

## **Description of the scenario** 

In this scenario, the attacker has gained access to the site where the target object is located. This can be done, for example, by pretending to be someone else or by registering as a day visitor for maintenance purposes. 

Within the site, the attacker can enter the immediate vicinity of the antenna due to inadequate access controls and cause physical damage. Alternatively, the attacker can use projectiles or drones to cause physical damage if flying objects can approach the antenna. 

Federal Office for Information Security 

28 

{PRIVATE & PERSONAL} 

Risk treatment 

## **Effect of the security measures** 

BM1 makes it more difficult to carry out the attack described, as the placement of the antenna within a restricted zone with additional access controls represents an effective barrier to physical interaction with the antenna. It should be noted here that the perimeter protection must not only regulate access by people, but also the penetration of hostile technology as flying objects. 

BM32 is primarily relevant for the risk of an attack via the supply chain and is not considered further in this example scenario. 

Federal Office for Information Security 

29 

{PRIVATE & PERSONAL} 

Cryptographic notes 

## 7 Cryptographic notes 

The cryptographic concept for securing a space system must be defined depending on the planned mission, although some aspects are usually the same for almost all missions. The concept must be adapted to the threat scenario, the functional requirements, the protection requirements and the elements of the planned system.[2] 

End-to-end security from satellite control centre to space segment is required, since external control, with all its possible consequences, is assumed to be the maximum possible damage (total loss). 

End-to-end security is enforced by using an encryption device (which can protect the integrity and authenticity of information in addition to confidentiality) in the space segment and the operating ground segment. This is how the TTC Link can be protected. 

In addition, the communication link between the satellite control centre and the ground station (SLE link) should also be protected. However, this is less security-relevant, since in case of failure and disruption of a ground station antenna, another ground station antenna can potentially be used. To protect the public network connection from the satellite control centre to the ground station, it is recommended to use certified VPN products (e.g. Common Criteria) for the SLE link that meet the intended purpose and regulatory requirements. 

The security requirements of the payload communication channel differ significantly from mission to mission; the minimum requirement is the protection of confidentiality/authenticity/integrity. A missionspecific risk analysis must also be carried out for the payload in order to determine the quality of the measures. It should be noted that the undetected compromise of asymmetric key material generally only allows active cryptographic attacks on the confidentiality of data, while the undetected compromise of symmetric keys also enables passive (and therefore much more difficult to detect) attacks. 

Loading the keys into the satellite is another critical aspect, as this may not take place in an environment controlled by the customer or the satellite operator. Residual risks can be reduced by using asymmetric procedures for key agreement between the ground segment and the space segment, as, for example, only active attacks are possible even in the event of a compromise, as described above. However, the authenticity of the key material should also be protected in this case. 

Particularly with symmetric systems, it should be noted that through appropriate use of Key Derivation Functions (KDFs), the requirement for the amount of key material to be provided can be significantly reduced. 

Space systems usually require the storage and protection of long-term keys on the ground for the entire lifetime of the system or at least individual satellites of the system. This should be taken into account when designing the system. 

There are approved algorithms, mechanisms, procedures and protocols that are recommended by the BSI; these are described in Technical Guideline TR-02102-1 [17]. Deviations from this should be agreed on with the client. The BSI requirements may go beyond those described above, especially for high levels of protection. Therefore, in this case in particular, the BSI must be contacted at an early stage. 

Furthermore, protection against quantum cryptographic attacks must always be provided. This is particularly important when using asymmetric cryptographic methods. Information and requirements on suitable procedures, key lengths etc. can be found in TR-02102-1 [17] and also in the relevant publications of the BSI [18]. 

> 2  If the project requires the implementation of cryptographic procedures for the operating ground segment, this chapter is mandatory. In addition, it can be specified that a cryptographic concept certifiable by the BSI must be implemented, in that case the Technical Guideline TR-02102-1 [17] is to be applied. 

Federal Office for Information Security 

30 

{PRIVATE & PERSONAL} 

Cryptographic notes 

Due to the usually long development and lifetime of space systems, it is strongly recommended, for all protection levels, to go beyond what is established in TR-02102-1 [17] and to select cryptographic primitives and key lengths of correspondingly higher value. 

Furthermore, due to these long timeframes, it must be possible to change the cryptographic methods used. 

This so-called crypto-agility of the system (particularly of the space segment) must be provided for, whereby the authenticity of software/firmware updates must be secured with PQ-suitable cryptographic mechanisms. The mechanism or security anchor for replacing the firmware/software does not have to be modifiable. 

Random number generators must be used to generate cryptographic keys and other necessary random numbers. The BSI has identified requirements for the quality of random numbers, and their use is recommended. A specification of functionality classes of random number generators is contained in the documents AIS 20 [19] and AIS 31 [20] or the joint mathematical-technical annex [21] and [22]. 

A PTG.3 or DRG.4 generator should be used. (From a PTG.2 compliant random number generator, a random number generator that meets the requirements of functionality class PTG.3 can be constructed through suitable cryptographic post-processing.) For high security levels, two such generators must be appropriately combined for redundancy reasons. Additional information on random number generators and the aforementioned requirements can be found in Technical Guideline TR-02102-1 [17]. 

Federal Office for Information Security 

31 

{PRIVATE & PERSONAL} 

Outlook 

## 8 Outlook 

This document is subject to regular review in order to be able to react to new technologies, use cases and risks. The continuous improvement of the guideline and its application notes is also a pursued goal. In a subsequent version of this TR, for example, it is planned to summarise the identified BMs in categories. The BSI welcomes suggestions and proposals for improvement in all aspects of this TR. 

The creation of further TRs is planned. 

Federal Office for Information Security 

32 

{PRIVATE & PERSONAL} 

Bibliography 

## 9 Bibliography 

- [1] Federal Office for Information Security, BSI-Standard 200-2: IT-Grundschutz-Methodology, 2017. 

- [2] ISO - International Organization for Standardization, ISO/IEC 27001:2022 Information technology – Security techniques – Information security management systems – Requirements, 2022. 

- [3] Federal Office for Information Security, IT Grundschutz-Profile for Space Systems Part 2: Ground Segment - Minimum Protection for the Entire Lifecycle, 2024. 

- [4] Federal Office for Informaton Security, TR-03184 Information Security for Space Systems Part 1: Space Segment. 

- [5] European Cooperation for Space Standardization, ECSS-Q-ST-80-10C DIR1, 2023. 

- [6] Bundesamt für Sicherheit in der Informationstechnik, IT-Grundschutz-Compendium, 2023. 

- [7] IT Grundschutz-Profile for Space Infrastructures Part 1: Space Segment - Minimum Protection for the Entire Lifecycle, 2022. 

- [8] ISO - International Standardization Organization, ISO/IEC 27005:2022 Information technology — Security techniques — Information security risk management, 2022. 

- [9] ISO - International Standardization Organization, ISO.IEC 31010:2019 – Risk management – Risk assessment techniques, 2019. 

- [10]  Federal Office for Information Security , BSI-Standard 200-3 Risk Analysis based on IT-Grundschutz, 2017. 

- [11]  Bundesamt für Sicherheit in der Informationstechnik, „Übersicht konsolidierte DA im ITGrundschutz - Stand Kompendium 2023,“ 27 06 2024. [Online]. Available: https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Drafts/Community_Draft/ Uebersicht_DA-IT-Grundschutz_Kompendium_2023.html. [Zugriff am 30 05 2025]. 

- [12]  The Aerospace Corporation, „Space Attack Research and Tactic Analysis (SPARTA),“ 09 02 2024. [Online]. Available: https://sparta.aerospace.org. 

- [13]  The Consultative Committee for Space Data Systems, „Security Threats against Space Missions,“ 2022. [Online]. Available: https://public.ccsds.org/Pubs/350x1g3.pdf. 

- [14]  ESA, „Space Attacks and Countermeasures Engineering Shield (SPACE-Shield),“ [Online]. Available: https://spaceshield.esa.int. [Zugriff am 09 02 2024]. 

- [15]  Mitre Corporation, „Adversarial Tactics, Techniques, and Common Knowledge (ATT&CK),“ [Online]. Available: https://attack.mitre.org. [Zugriff am 02 09 2024]. 

- [16]  NIST, „Cybersecurity Framework,“ [Online]. Available: https://www.nist.gov/cyberframework. [Zugriff am 28 04 2025]. 

- [17]  Federal Office for Information Security, TR-02102 Cryptographic Mechanisms: Recommendations and Key Lengths, 2025. 

- [18]  Federal Office for Information Security, „Quantum Technologies and Quantum-Safe Cryptography,“ [Online]. Available: https://www.bsi.bund.de/EN/Themen/Unternehmen-undOrganisationen/Informationen-und-Empfehlungen/Quantentechnologien-und-Post-Quanten- 

Federal Office for Information Security 

33 

{PRIVATE & PERSONAL} 

Bibliography 

Kryptografie/quantentechnologien-und-post-quanten-kryptografie_node.html. [Zugriff am 28 04 2025]. 

- [19]  Federal Office for Information Security, AIS 20 Functionality classes and evaluation methodology for deterministic random number generators, 2013. 

- [20]  Federal Office for Information Security, AIS 31 Functionality classes and evaluation methodology for physical random number generators, 2011. 

- [21]  W. Schindler, Functionality Classes and Evaluation Methodology for Deterministic Random Number Generators. Version 2.0, 02.12.1999. 

- [22]  W. S. W. Killmann, A proposal for: Functionality classes and evaluation methodology for true (physical) random number generators, Version 3.1, 25.09.2001, 2001. 

Federal Office for Information Security 

34 


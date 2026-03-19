Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

Federal Office for Information Security 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

Federal Office for Information Security 

P.O.B 20 03 63 D-53133 Bonn (Germany) Phone.: +49 22899 9582-0 

E-Mail: tresor@bsi.bund.de 

Internet: https://www.bsi.bund.de 

© Federal Office for Information Security (BSI) 2020 

Federal Office of Information Security 

2 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

## Inhalt 

|1|Introduction|5|
|---|---|---|
|1.1|Purpose|5|
|2|Scope of Document|7|
|2.1|Assessment Framework|8|
|2.2|Document Overview|9|
|3|Assessment Approach|10|
|3.1|Assessment Pre-Requisites|10|
|3.2|Strictness of Assessment Criteria|10|
|3.2.1|Requirements|10|
|3.2.2|Assessment Criteria|11|
|3.3|Structure of the Assessment Criteria|11|
|3.4|Assessment Stages and Assessor Activities|12|
|3.4.1|Usage of a Certified TR-ESOR (V1.2.1 or later) Product in Combination with a||
||Preservation Service Provider (PSP)|13|
|3.4.2|Identification of Assessment Criteria|13|
|4|Structure of Assessment Criteria and Report Template|14|
|5|Assessment Criteria for Risk Assessment|15|
|6|Assessment criteria for Policies and Practices|16|
|6.1|Preservation Service Practice Statement|16|
|6.2|Terms and Conditions|20|
|6.3|Information Security Policy|24|
|6.4|Preservation profiles|25|
|6.5|Preservation evidence policy|34|
|6.6|Signature validation policy|43|
|6.7|Subscriber agreement|44|
|7|Assessment criteria for PSP Management and Operation|46|
|7.1|Internal organization|46|
|7.2|Human resources|47|
|7.3|Asset management|48|
|7.4|Access control|49|
|7.5|Cryptographic controls|50|



Federal Office of Information Security 

3 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|7.6|Physical and environmental security|56|
|---|---|---|
|7.7|Operation security|57|
|7.8|Network security|58|
|7.9|Incident management|60|
|7.10|Collection of evidence|61|
|7.11|Business continuity management|63|
|7.12|TSP termination and termination plans|64|
|7.13|Compliance|65|
|7.14|Cryptographic monitoring|66|
|7.15|Augmentation of preservation evidences|69|
|7.16|Export-Import package|71|
|8|Operational and notification protocols|76|
|8.1|Preservation protocol|76|
|8.2|Notification protocol|91|
|9|Preservation process|93|
|9.1|Storage of preserved data and evidences|93|
|9.2|Preservation evidences|95|
|9.3|Preservation of digital signatures|98|
|10|Assessment criteria for Annex A (normative): Qualified preservation service for QES||
||as defined by article 34 the Regulation (EU) No 910/2014|105|
|11|References|109|
|11.1|Normative References|109|
|11.2|Informative References|111|
|Keywords and Abbreviations||113|



## **Table of Figures** 

Figure 1: ETSI Assessment Framework ............................................................................... 8 Figure 2: Structure of Assessment Criteria and Report Template...................................... 14 

## **Table List** 

Table 2 Types of (qualified) Trust Services ......................................................................... 7 Table 3: Normative References ........................................................................................ 111 Table 4: Informative References ...................................................................................... 112 Table 5:  Keywords and Abbreviations ............................................................................ 115 

Federal Office of Information Security 

4 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

## **1 Introduction** 

## **1.1 Purpose** 

Trust services, as specified in Regulation (EU) No 910/2014 **[eIDAS]** (short: eIDAS), shall give participants of electronic commerce confidence in the security of these trust services. This confidence is expected to result from a set of procedures, processes and security measures, the Trust Service Provider (TSP) has established in order to minimize the operational and financial threats and risks associated. 

eIDAS distinguishes two trust levels with respect to trust services and providers of trust services: 

- normal trust services and trust service providers (TSP) and 

- **qualified** trust services and trust service providers ( **QTSPs** ) that need to fulfil additional legal requirements and are subject to periodical independent third party conformity assessments by accredited conformity assessment bodies (CAB). 

(Q)TSP means TSP or QTSP. 

Especially **qualified** trust services and QTSPs will fulfil such high expectations of participants. 

**[ETSI TS 119 511]** defines policy requirements for operation and management practices of a TSP, which provides long-term preservation of digital signatures or general data using digital signature techniques. **[ETSI TS 119 511]** does not specify **how** the requirements can be assessed by an independent party and what kind of information and documents shall be the subject of such a conformity assessment. **[ETSI TS 119 511]** refers to **[ETSI EN 319 403]** “Requirements for Conformity Assessment Bodies Assessing Trust Service Providers”, which is applicable to CABs and which supplements the international standard **[ISO/IEC 17065]** , which accredited CABs must fulfil. **[ETSI EN 319 403]** poses general requirements on CABs assessing (qualified) trust services and does neither distinguish between different trust services nor define dedicated assessment criteria for the application of standards like **[ETSI EN 319 401]** or standards for dedicated trust services of the ETSI EN 319 4x1 series. 

More specifically, **[ETSI TS 119 511]** extends the general requirements of **[ETSI 319 401]** for a TSP, which provides long-term preservation of digital signatures or general data using digital signature techniques. 

If the **[ETSI EN 319 401]** defines general requirements on the TSP’s public documentation, including the TSP’s management and operation, the **[ETSI TS 119 511]** defines specific requirements to documentation and policies relating to the preservation service (e.g. Preservation Service Practice Statement, Preservation Evidence Policy, etc.) including technical and operational requirements relating to the preservation service (e.g. Preservation 

5 

Federal Office of Information Security 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

Profiles, Preservation Protocol, Notification Protocol, etc.). 

Assessment criteria, derived one-by-one from **[ETSI TS 119 511]** requirements, are neither intended nor included. 

In summary, neither the TSP specific standards (ETSI EN 319 4x1) nor the CAB specific standard **[ETSI EN 319 403]** provides dedicated assessment criteria for an application for the conformity assessment of TSP. 

The document **[ASS 319 401],** further on also called Part 1, has the goal to bridge this gap with respect to **[ETSI EN 319 401]** . 

The present document, further on also called Part 2 and referenced by **[Ass 119 511]** , has the goal to bridge this gap with respect to **[ETSI TS 119 511]** . It specifies assessment criteria to be used by accredited conformity assessment bodies (CAB) to assess the conformity of (qualified) trust service providers ((Q)TSPs) against the standard **[ETSI TS 119 511]** . 

The conformity assessment of Part 1 SHALL be performed before the conformity assessment of Part 2 or in parallel. 

6 

Federal Office of Information Security 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

## **2 Scope of Document** 

These assessment criteria are the module for conformity assessment of TSPs that fulfils the requirements of **[ETSI TS 119 511]** . Other modules, applicable for the conformity assessment of TSP with specific other trust services may be drafted in the future. The assessment criteria are directly derived from the policy requirements given by **[ETSI TS 119 511]** . CAB shall apply all criteria set out in **[ETSI TS 119 511]** to be conformant to this document. 

There exist further parts of assessment criteria based on **[ETSI EN 319 401]** and beside **[ETSI TS 119 511]** for other specific trust services. Such assessment criteria will always be additional to those set out in Part 1 and Part 2. Currently, e.g. the following norms and specifications are available to specific types of (qualified) trust services as defined in **[eIDAS]** : 

|**Type of (Qualified) Trust Service**|**Related Norms and Technical**|
|---|---|
||**Specifications**|
|creation of qualified certificates for electronic<br>signatures or electronic seals|<br>ETSI EN 319 411-2 together with ETSI EN<br>319 411-1|
|creation of qualified certificates for web site<br>authentication|<br>ETSI EN 319 411-2 together with ETSI EN<br>319 411-1|
|creation of qualified electronic time stamps|ETSI EN 319 421|
|validation of qualified electronic signature and<br>seals|<br>ETSI TS 119 441|
|electronic registered delivery|ETSI EN 319 521 and ETSI EN 319 531|
|signing service|ETSI TS 119 431-1 and ETSI TS 119 431-<br>2|
|preservation service|ETSI TS 119 511 and ETSI TS 119 512|



## **Table 1 Types of (qualified) Trust Services** 

**Not** addressed in this document are organisational activities of the CAB and its assessors like contract gathering aspects and project management, assessor qualification and audit planning, reporting specific aspects or non-conformity tracking. These aspects are in the scope of **[ISO/IEC 17065]** and **[ETSI EN 319 403]** which are normative to the CAB. 

There are also **not** addressed requirements of **[ETSI EN 319 401]** , which is the base and a prerequisite of an assessment of a (qualified) TSP. This document relates to the specific assessment criteria for a TSP providing long-term preservation of digital signatures or general data using digital signature techniques. 

Federal Office of Information Security 

7 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

## **2.1 Assessment Framework** 

Derived assessment criteria are embedded in the European regulatory framework. On EUlevel, each TSP underlies especially the eIDAS regulation **[eIDAS]** and the General Data Protection Regulation (GDPR). Conformity Assessment Bodies (CAB) shall comply also with **[EU regulation 765/2008]** . Furthermore, EU implementing acts and national trust service laws apply to both. The ETSI series related to trusted services apply to TSPs in the same way, as related ISO and ETSI norms and standards or specifications apply to CABs. The following figure sketches hierarchy of documented regulatory framework and shows the relation to a Preservation Service Provider (as an example of a TSP) and a CAB as acting entities. The assessment criteria are applicable to CAB only. 


![](markdown/tr/Assessment-Handbuch_ETSI_319_511/Assessment-Handbuch_ETSI_319_511.pdf-0008-03.png)


**Figure 1: ETSI Assessment Framework** 

**[ETSI EN 319 401]** specifies general policy requirements on the operation and management practices of a TSP regardless of the service the TSP provides. 

Subordinated **[ETSI EN 319 411-1]** or **[ETSI TS 119 511]** specify specific policy requirements, depending on the specific service of the TSP. So, other than **[ETSI EN 319 401]** , only those norms and specifications from ETSI series apply, which are required for the specific type of trust service. As an example, **[ETSI EN 319 411-1]** applies to TSPs issuing certificates for natural or legal persons. In the same way, **[ETSI TS 119 511]** applies to Preservation Service Providers. 

The regulatory framework for CABs is based on **[ISO/IEC 17065]** as an accreditation norm, amended by **[ETSI EN 319 403]** . 

The assessment requirements are then based on the standards, so that the Preservation TSP has to be conformant with **[ETSI EN 319 401]** and **[ETSI TS 119 511]** , providing longterm preservation of digital signatures or general data using digital signature techniques. 

Federal Office of Information Security 

8 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

## **2.2 Document Overview** 

The following **chapter 3** specifies the assessment approach. It gives the frame for applying the criteria found in the following chapters. 

In **chapter 4,** the present document describes the structure and explains the content of the tables, which contain norm requirements together with detailed assessment criteria. The last column provides space to fill in observations, verdicts and findings, as a result of an assessment. 

Subsequent **chapters 5 to 7** define the assessment criteria for conformity assessment against **[ETSI TS 119 511]** , following its document structure. 

The assessment criteria are written in such a way that the present document (or the respective parts of it) could be used as **template** for the documentation of the results of a conformity assessment. An utilisation of the tables within a spreadsheet might be helpful for an actual assessment. 

Federal Office of Information Security 

9 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

## **3 Assessment Approach** 

## **3.1 Assessment Pre-Requisites** 

For demonstrating conformance to **[ETSI TS 119 511]** all mandatory assessment criteria in this document shall be applied. 

Pre-requisites for such a conformance assessment are the following aspects: 

- Because **[ETSI TS 119 511]** extends **[ETSI EN 319 401]** , it is necessary for the CAB to **assess** the assessment criteria of **[ETSI EN 319 401]** (usually during the **[ETSI TS 119 511]** assessment, but also possibly beforehand). 

- Due to the public nature of the provided preservation services, the Preservation Service Provider (PSP) has to **document** its implementing practices, together with legal terms and conditions. These documents target public audiences, who can be any party relying on the provided preservation services. With those documents, the PSP shows, what and how it is doing to fulfil the applicable norm requirements, here of **[ETSI TS 119 511]** . 

- The TSP has to **implement** all preservation service practices laid down in its publicly **1** available documents. Clearly, its implementation must fully conform to its own public documents. 

The CAB will assess the TSP as an organisation with its documentation and its implemented preservation services, based on the assessment criteria from the present document. The main task of the assessor is to determine if all mandatory assessment criteria are fulfilled. In this case conformance to **[ETSI TS 119 511]** is implied. 

Before starting a conformity assessment a contract between the accredited CAB and the PSP needs to be established. Further pre-requisites on the assessment process result from the accreditation of the CAB against **[ISO/IEC 17065]** and **[ETSI EN 319 403]** (e.g. audit team, assessment plan). They are out of scope of the present document, which focusses on the assessment activities itself and – in detail – on the expected results. 

## **3.2 Strictness of Assessment Criteria** 

For a better understanding of the strictness of the assessment criteria within this document it is necessary to clearly separate between the two different types of rules to be followed: 

- “Requirements” are applicable to TSPs/PSPs and directly originate from the related ETSI documents ( **ETSI EN 319 401** , **[ETSI TS 119 511],** etc.). 

- The assessment “criteria” are applicable to the CAB and its assessors and mainly derived from those ETSI documents applicable to TSPs/PSPs. 

## **3.2.1 Requirements** 

Requirements from TSP/PSP related ETSI documents use the modal verbs terminology of ETSI Drafting Rules, clause 3.2 (Verbal forms for the expression of provisions): "shall", "shall not", "should", "should not", "may", "need not", "will", "will not", "can" and "cannot". 

Whenever the assessor identifies a “shall” requirement not being fulfilled by a TSP, a **non-** 

> 1 Mandatory public documents of the PSP are its PSPS and terms & conditions. 10 

Federal Office of Information Security 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

**conformity (NC)** results. Such a NC may result in a stop of business for the TSP/PSP. Any decision about the severeness of non-conformities is up to the CAB, the assessor is working for and resides outside the scope of this document. Likewise, if a “should” requirement is unfulfilled by a TSP, a **recommendation (R)** results and further assessment activities by the CAB are necessary. 

A "should" requires from the TSP either to fulfil the requirement exactly as it is specified or respective test material or explanations should demonstrate the specified behaviour to make evident that it`s equivalent to the requirements and to the required security levels. Remark: not related to the strictness are so called **potentials for improvement (PI),** an assessor may identify. These PIs are only informative to the TSP. 

## **3.2.2 Assessment Criteria** 

Regarding the assessment criteria, this document uses the following three major classes of assessment criteria (cf. [RFC 2119]) 

- MAY: These criteria are just hints or optional activities of the assessor. These criteria will not result in mandatory assessment activities. 

- SHOULD: These criteria are strong recommendations. Respective assessment activities should be performed by the assessor. Alternatively, the assessor explains why he or she uses a different approach and why this activity assures the same assessment result as the original activity. 

- SHALL (or synonymously MUST): These are strict criteria. It is not allowed to use different assessment activities. 

The strictness of the assessment criteria applicable to the CAB and its assessors is to be specified by the applicable accreditation and certification scheme and resides outside the scope of this document. 

## **3.3 Structure of the Assessment Criteria** 

The order of the assessment criteria follows the document structure (chapters, sections) of norm **[ETSI TS 119 511]** . For each individual norm requirement, assessment criteria are derived for either stage 1 document assessment or/and stage 2 on-site assessment, as applicable. A conformant design of the provided preservation services, laid-out in the PSP documents (stage 1), is a pre-requisite for starting to audit the actual implementation on-site (stage 2). 

Norm chapters address specific aspects, a (Q)PSP and/or its preservation service(s) need to fulfil. Such aspects range 

- from sole **document** related requirements, which the documents of a (Q)PSP need to conform with; 

Federal Office of Information Security 

11 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

- through requirements related to **organisational** structure and processes and its procedures; 

- down to **infrastructural** requirements, both physical and logical (i.e. building infrastructure and IT infrastructure). 

Such a broad range of aspects is due to the overarching nature of “policy” requirements. A reason for such an approach are current **information security management practices.** To handle security, the purpose of business and applied processes need to be understood. Then immanent risks in the type of business and processes (to be implemented) need to be identified and treated assuring an acceptable level of security. Such treatment is structured along security measures. There are four generic types of **security measures:** 

- **Physical** security measures, 

- **Organisational** security measures, 

- **Personnel** related security measures, and 

- **Technology** related security measures. 

In a similar way, all assessment criteria are related to both, **functional and security aspects,** often at the same time and regardless of being related to (Q)TSP documentation and/or to actual implementation of provided trust service(s). The basic nature of trust services is trust, so functional aspects like the generation of certificates or signatures are actually security functions, using cryptography and implementing security objectives as integrity, confidentiality or authenticity. A sharp distinction between functional and security aspects is, therefore, at least difficult, if not impossible. The assessment must consider functional and security aspects always at the same time. 

## **3.4 Assessment Stages and Assessor Activities** 

The **assessment** of a (Q)TSP/(Q)PSP is performed by an accredited CAB on the basis of **[EN 319 403]** and split into two stages (see also **[ETSI EN 319 403]** ): 

- **Stage 1** – Document Assessment: the CAB assesses the documentation of the (Q)TSP for conformance with the requirements laid out in the applicable ETSI standard(s); 

- **Stage 2** – On Site Assessment **[2]** (Audit): the CAB assesses the (Q)TSP management, organisation, processes, documentation, facilities and infrastructures on site, i.e. at the (Q)TSP premises, for conformance with the requirements laid out in the applicable ETSI standard(s). 

At each stage, the CAB assessment includes **analytic, conclusive and reporting activities.** So the CAB assessor will 

- analyse documents, 

- ask questions and perform interviews, 

- inspect and has an eye on-site. 

> 2 Pre-assessment condition: see **[EN 319 403]** , chapter 7.4.5.3: In every case, the document review (stage 1) shall be completed prior to the commencement of audit, stage 2. 12 

Federal Office of Information Security 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

Based on this the assessor: 

- wants to understand the organisation and its services, 

- identifies potential gaps or non-conformities, 

- concludes whether the (Q)TSP/(Q)PSP fulfils its requirements, and finally 

- prepares a report on its findings and observations. 

The assessment criteria require from the assessor to perform certain activities and to check the expected results, with respect to the requirements. Per stage, the assessor describes the observations during his or her activity and gives per criterion a verdict (either “OK” or “not OK”). Also, he or she includes (negative) findings, expressed as non-conformities, recommendations or potentials for improvement. 

The assessor must document all results of assessor activities. For this the tables in chapter 5 to 7 SHOULD be used as a template for logging. Finally, an assessment report SHALL be written. See **[ETSI TS 119 403-3]** for details. 

## **3.4.1 Usage of a Certified TR-ESOR (V1.2.1 or later) Product in Combination with a Preservation Service Provider (PSP)** 

If the PSP claims to use a certified **TR-ESOR product [TR-ESOR] of version V1.2.1 or higher** and the claimed **[TR-ESOR]** certified product is in fact deployed for providing this service, proved e.g. by comparing the digital fingerprint of relevant executables, then the assessment result of the equivalent **[ETSI TS 119 511]** - test case is substituted by the TRESOR-certification result and this **[ETSI TS 119 511]** - assessment test step SHALL be omitted. 

## **3.4.2 Identification of Assessment Criteria** 

Each assessment criterion relates to a norm requirement identified by its unique identifier: 

<the 3 letters REQ> - < the clause number> - <2 digit number - incremental> 

Specific criterions are splitted into documentation related (stage 1) and implementation related aspects (stage 2, audit). Normally, stage 2 related criteria base on the results of stage 1 assessment. Some aspects are only relevant for stage 1, like some detailed content of the terms and conditions. Those will **not** be addressed in stage 2. Nevertheless, most aspects from stage 1 need to be mirrored and/or inspected on-site during stage 2. 

Federal Office of Information Security 

13 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

## **4 Structure of Assessment Criteria and Report Template** 

The following figure describes the structure and content of the tables used for assessment criteria as contained in chapter 5 to 7. The tables could be utilised as a template for a reporting of the assessment, as well. For that purpose, the use of a customised spreadsheet is advisable. 


![](markdown/tr/Assessment-Handbuch_ETSI_319_511/Assessment-Handbuch_ETSI_319_511.pdf-0014-03.png)


## **Figure 2: Structure of Assessment Criteria and Report Template** 

Notes and auditor guidance may origin from the norm itself or may be additional to that. 

If it is quoted from norm, the text in the table is set in _slanted_ format. 

The content of the column “Notes/auditor/Guidance” in the Figure 2: "Structure of Assessment Criteria and Report Template” is informative. 

Assessment criteria request assessor activities per each TSP requirement. Usually, the criteria text starts with a standard sentence and is followed by the specific assessor activities (indicated by hyphens “-“), and – in case – further detailed (indicated by plus signs “+”). Example **OVR-6.4-01** : 

## “See **[ASS 119 511]** , **OVR-6.1-03** . 

_The assessor shall check if the PSP_ 

- has _supported at least one preservation profile pursuant to OVR-6.2-03_ 

## _**or**_ 

- _stated which_ _**[TR-ESOR]** certified product of version 1.2.1 or higher is used for providing the service and this requirement by this PSP”_ 

Federal Office of Information Security 

14 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

## **5 Assessment Criteria for Risk Assessment** 

_NOTE: See ISO/IEC 27005 [i.5] for guidance on information security risk management as part of an information security management system._ 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-5-01_**|_The requirements specified in_**_ETSI_**|See<br>**[ETSI EN 319 401]**<br>and<br>**[ASS 319 401].**|The assessor shall assess the document<br>[PSPS] and verify  that  the PSP<br>- fulfils the requirements defined in**[ASS 319**<br>**401, REQ-5-01]**through**[ASS 319 401,**<br>**REQ-5-05]**concerning stage 1<br>or<br>- shows his valid and successful conformity<br>assessment report of its PSPS pursuant to<br>**[ETSI EN 319 401],**performed by a<br>conformity assessment body, which is<br>accredited in accordance with**[eIDAS]**as<br>competent.|<br> <br> <br> <br> <br> <br> <br>|Only applicable if no valid and successful conformity<br>assessment report of the PSP and its PSPS pursuant to<br>**[ETSI EN 319 401]**exists:<br>The assessor shall assess the PSP on-site and verify<br>that the PSP:<br>- fulfils the requirements defined in**[Ass 319401,**<br>**REQ-5-01]**through**[ASS 319401, REQ-5-05]**<br>concerning stage 2.|<br> <br> <br> <br>|||
||**_EN 319 401_**_[1], clause 5 shall apply._||||||||
||||||||||



15 

Federal Office of Information Security 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

## **6 Assessment criteria for Policies and Practices** 

## **6.1 Preservation Service Practice Statement** 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.1-01_**|_The requirements specified in_|<br> <br> <br> <br>See<br>**[ETSI EN 319**<br>**401]**<br>and<br>**[ASS 319 401].**|<br>The assessor shall assess the document [PSPS]<br>and verify that the PSP:<br>- fulfils the requirements defined in**[ASS**<br>**319401, REQ-6.1-01]**through**[ASS 319401,**<br>**REQ-6.1-12]**concerning stage 1,<br>or<br>- shows his valid and successful conformity<br>assessment report of its PSPS pursuant to**[ETSI**<br>**EN 319 401],**performed by a conformity<br>assessment body, which is accredited in<br>accordance with**[eIDAS] **as competent.|<br> <br> <br> <br> <br> <br> <br>|Only applicable if no valid and successful<br>conformity assessment report of the PSP and its<br>PSPS pursuant to**[ETSI EN 319 401]**exists.<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- fulfils the requirements defined in**[Ass 319401,**<br>**REQ-6.1-01]**through**[ASS 319401, REQ-6.1-**<br>**12]**concerning stage 2.|<br> <br> <br> <br>|||
||**_ETSI EN 319 401_**_[1], clause_||||||||
||_6.1 shall apply._||||||||
||||||||||
||||||||||
||_In addition, the following_||||||||
||_particular requirements apply:_||||||||
||||||||||
|**_OVR-6.1-02_**|_The_<br>_preservation_<br>_service_|<br> <br> <br> <br> <br>|The assessor shall assess the provided public<br>PSP documents and verify that<br>- the PSP listed or referenced (e.g. via OID)<br>supported preservation service policies<br>- and briefly described them.|<br>|not applicable||||
||_provider (PSP) should list or_||||||||
||_make reference to (e.g. through_||||||||
||_OIDs), and briefly describe the_||||||||
||_supported preservation service_||||||||
||_policies in its preservation_||||||||
||_servicepractice statement_||||||||
|**_OVR-6.1-03_**|_The PSP shall list in its_|<br> <br>|The assessor shall assess the provided public<br>[PSPS] and verify that:<br>- the set of supported preservation profiles,<br>which are provided for the preservation service,<br>are documented.|<br> <br>|The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- implemented the preservation profiles as<br>documented in [PSPS].<br>See also **[ASS 119 511]**, **OVR-6.4-01**et seq..|<br>|||
||_preservation service practice_||||||||
||_statement_<br>_the_<br>_supported_||||||||
||_preservation profiles._||||||||
||||||||||



16 

Federal Office for Information Security 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.1-04_**|_The PSP shall state in its_|<br> <br>|The assessor shall assess the provided public<br>[PSPS] and verify:<br>- the preservation goals are defined and<br>- how theyare achieved bythe service.|<br>|not applicable||||
||_preservation service practice_||||||||
||_statement how the preservation_||||||||
||_goals are achieved._||||||||
|**_OVR-6.1-05_**|_The PSP shall define in its_|<br> <br> <br> <br> <br>|The assessor shall assess the provided public<br>[PSPS] and verify that:<br>- it is defined how the process for the provision<br>of<br>preservation<br>services<br>achieves<br>the<br>availability requirements for<br>+ submitted data objects (SubDO) and<br>+ associatedpreservation evidences.|<br> <br>|The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- implemented the processes of:<br>+ provisioning the availability of the submitted<br>data objects and<br>+ provisioning the associated preservation<br>evidences.|<br> <br>|||
||_preservation service practice_||||||||
||_statement how the availability_||||||||
||_of the submitted data objects_||||||||
||_(SubDO) and the associated_||||||||
||_preservation_<br>_evidences_<br>_is_||||||||
||_achieved._||||||||
|**_OVR-6.1-06_**|_The PSP shall identify in its_|<br> <br> <br> <br> <br> <br>|The assessor shall assess the document [PSPS]<br>and verify that the PSP:<br>- identified all external organisations supporting<br>the PSP service<br>- named all obligations applicable to these<br>external organisations with contract and<br>- included in those obligations all applicable<br>policies and practices.|<br> <br> <br>|The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- names all external organisations, which support<br>the PSP service<br>- uses the services of these external organisations<br>as described in the preservation service practice<br>statement.|<br> <br> <br>|||
||_preservation service practice_||||||||
||_statement the obligations of all_||||||||
||_external_<br>_organisations_||||||||
||_supporting the preservation_||||||||
||_service services including the_||||||||
||_applicable_<br>_policies_<br>_and_||||||||
||_practices._||||||||
||||||||||



Federal Office for Information Security 

17 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.1-07_**|_[WST] The PSP shall state in_|<br> <br> <br> <br>See<br>**OVR-6.1-05.**|Only applicable in case of [WST]:<br>The assessor shall assess the document [PSPS]<br>and verify that the PSP:<br>- described the process of requesting export-<br>import package(s) clearly,<br>**or**<br>- stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in use for providing<br>the service and this requirement by this PSP.|<br> <br> <br> <br>|Only applicable in case of WST:<br>If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify:<br>- the process of requesting export-import<br>package(s)<br>- that the PSP implemented the export-import<br>package(s)as documented.|<br> <br> <br> <br> <br> <br> <br>|||
||_its_<br>_preservation_<br>_service_||||||||
||_practice statement the details_||||||||
||_on the process of requesting_||||||||
||_export-import package(s)._||||||||
||||||||||



Federal Office for Information Security 

18 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.1-08_**|_[WST] The PSP shall specify in_|<br> <br> <br> <br> <br>_EXAMPLE_<br>_1:_<br>_Whether_<br>_the_<br>_package_<br>_is_<br>_encrypted or not._|<br> <br> <br> <br>Only applicable in case of [WST]:<br>The assessor shall assess the document [PSPS]<br>and verify that the PSP:<br>- specified the production methods of the<br>export-import package(s), e.g. file type, data<br>structure,<br>integrity<br>or/and<br>confidentiality<br>protection,<br>**or**<br>- stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing<br>the preservation service and this requirement by<br>this PSP.|<br> <br> <br> <br> <br> <br> <br>|Only applicable in case of WST:<br>If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that:<br>- the production methods for export-import<br>package(s),e.g. pursuant to<br>•<br>**[TS 119 512, Annex G]**or<br>•<br>**[TR-ESOR-M.3, clause 2.5]**<br>are implemented and workingas documented.|<br> <br> <br> <br> <br> <br>|||
||_its_<br>_preservation_<br>_service_||||||||
||_practice_<br>_statement_<br>_the_||||||||
||_production methods of the_||||||||
||_export-import package(s), see_||||||||
||_clause 7.16._||||||||
||||||||||
|**_OVR-6.1-09_**|_[WST] The PSP shall specify in_|<br> <br> <br> <br>_EXAMPLE_<br>_2:_<br>_Whether the data_<br>_is_<br>_deleted_<br>_or_<br>_transferred_<br>_to_<br>_another place._|<br> <br> <br> <br>Only applicable in case of [WST]:<br>The assessor shall assess the document [PSPS]<br>and verify that the PSP:<br>- described what happens to the data at the end<br>of the preservation period,<br>**or**<br>- stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing<br>the service and this requirement by this PSP.|<br> <br> <br>|Only applicable in case of WST:<br>If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify:<br>- that what happens to the data at the end of the<br>preservationperiod,takesplace as documented.|<br> <br> <br> <br> <br>|||
||_its_<br>_preservation_<br>_service_||||||||
||_practice_<br>_statement_<br>_what_||||||||
||_happens to the data at the end_||||||||
||_of the preservation period._||||||||
||||||||||



Federal Office for Information Security 

19 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

## **6.2 Terms and Conditions** 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.2-01_**|_The requirements specified in_|<br> <br> <br>See<br>**[ETSI EN 319**<br>**401]**<br>and<br>**[ASS 319 401].**|<br>The assessor shall assess the document [T&C]<br>and verify that the PSP:<br>-  fulfils the requirements defined in**[ASS 319**<br>**401, REQ-6.2-01]**through**[ASS 319 401,**<br>**REQ-6.2-06]**concerning stage 1,<br>or<br>- shows his valid and successful conformity<br>assessment report of the PSP and its PSPS<br>pursuant to**[ETSI EN 319 401],**performed by<br>a conformity assessment body, which is<br>accredited in accordance with**[eIDAS]**as<br>competent.|<br> <br>|Only applicable if no valid and successful<br>conformity assessment report of the PSP and its<br>PSPS pursuant to**[ETSI EN 319 401]**exists.<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- fulfils the requirements defined in**[ASS 319**<br>**401, REQ-6.2-01]**through**[ASS 319 401, REQ-**<br>**6.2-06]**concerning stage 2.|<br> <br> <br>|||
||**_ETSI EN 319 401_**_[1], clause_||||||||
||_6.2 shall apply._||||||||
||||||||||
||_In addition, the following_||||||||
||_particular requirements apply:_||||||||
||||||||||
|**_OVR-6.2-02_**|_The PSP shall list in the terms_|<br> <br>|The assessor shall assess the document [T&C]<br>and verify that the PSP:<br>- listed all the preservation policies it supports.||not applicable||||
||_and_<br>_conditions_<br>_all_<br>_the_||||||||
||_preservation service policies it_||||||||
||_supports._||||||||
|**_OVR-6.2-03_**|_The PSP shall state where to_|<br> <br> <br>See**OVR-6.4-**<br>**01.**|The assessor shall assess the document [T&C]<br>and verify that the PSP:<br>- stated where to find information on the<br>supportedpreservationprofiles.||not applicable||||
||_find_<br>_information_<br>_on_<br>_the_||||||||
||_supported_<br>_preservation_||||||||
||_profiles._||||||||



Federal Office for Information Security 

20 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.2-04_**|_[CONDITIONAL] When the_||If the preservation submitter takes a role in the<br>preservation process,<br>the assessor shall assess the document [T&C]<br>and verify that the PSP:<br>+ pointed out under which conditions this will<br>be done and<br>+ stated more precisely in particular which are<br>the responsibilities taken by the preservation<br>service and the ones that shall be taken by the<br>submitter.|<br> <br> <br>|If the preservation submitter takes a role in the<br>preservation process,<br>the assessor shall assess the PSP on-site and verify<br>that the PSP:<br>+ identifies its preservation submitters,<br>+ shows their role in the preservation process,<br>+ shows  the conditions and responsibilities for the<br>PSP and its submitters.<br>The assessor shall<br>- cause the PSP to show one or more example(s)<br>and<br>- compare the descriptions in [T&C] with the<br>productionprocesses.|<br> <br> <br>|||
||_preservation submitter is_||||||||
||_allowed to take a role in the_||||||||
||_preservation process (e.g._||||||||
||_providing needed validation_||||||||
||_data), the PSP shall describe_||||||||
||_in its terms and conditions_||||||||
||_under which conditions this_||||||||
||_can be done, and specify in_||||||||
||_particular which are the_||||||||
||_responsibilities taken by the_||||||||
||_preservation service and the_||||||||
||_ones that shall be taken by the_||||||||
||_submitter._||||||||
||||||||||
|**_OVR-6.2-05_**|_[WST] The PSP shall state in_|_EXAMPLE 1:_<br>_The request can_<br>_be done via_<br>_email or a_<br>_registered mail._|Only applicable in case of [WST]:<br>The assessor shall assess the document [T&C]<br>and verify that the PSP:<br>- described in its Terms and Conditions how<br>the request for an export-import package can<br>be done,<br>**or**<br>- stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing<br>the service and this requirement bythis PSP.|<br> <br>|not applicable||||
||_its terms and conditions how_||||||||
||_the request for an export-_||||||||
||_import package can be done._||||||||
||||||||||



Federal Office for Information Security 

21 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.2-06_**|_[PDS] The PSP shall state in_|<br>_EXAMPLE 2):_<br>_Whether to send_<br>_a_<br>_failure_<br>_indication_<br>_or_<br>_not._<br>_EXAMPLE 3)_<br>_Whether to_<br>_abort the_<br>_preservation_<br>_request or to_<br>_continue with_<br>_the incomplete_<br>_validation_<br>_information._|<br> <br> <br>Only applicable in case of [PDS]:<br>The assessor shall assess the document [T&C]<br>and verify that the PSP:<br>- described its process/strategy for each<br>preservation profile, which belongs to the<br>preservation service of digital signatures<br>[PDS], when the preservation service is unable<br>to collect and verify all the validation data.<br>The assessor shall verify that the PSP<br>- described the process / strategy including a<br>failure indication or the preservation of<br>validation information, which can be collected,<br>**or**<br>- stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing<br>the service and this requirement by this PSP.|<br> <br> <br>|Only applicable in case of [PDS]:<br>If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows the process / strategy for each<br>preservation profile, which belongs to the<br>preservation service of digital signatures [PDS],<br>when the preservation service is unable to collect<br>and verify all the validation data.<br>The assessor shall cause the PSP to show one or<br>more example(s) of failure indications or<br>preserved validation information.<br>The assessor shall compare the process /<br>strategy/examples for each preservation profile<br>including a failure indication or the preservation<br>of validation information, it can collect, with the<br>description in the[T&C]of the PSP.|<br> <br> <br> <br> <br> <br>|||
||_its terms and conditions the_||||||||
||_strategy that it will follow_||||||||
||_when it is unable to collect and_||||||||
||_verify all the validation data._||||||||
||||||||||



Federal Office for Information Security 

22 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.2-07_**|_[CONDITIONAL] When the_|<br>_NOTE: The PSP_<br>_has no way of_<br>_knowing_<br>_to_<br>_which document_<br>_the hash values_<br>_correspond and_<br>_even if it really_<br>_corresponds to a_<br>_hash value of a_<br>_concrete_<br>_hash_<br>_computation._|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>If applicable,<br>the assessor shall assess the document [T&C]<br>and verify that the PSP:<br>- described that the PSP is not liable for<br>guaranteeing that the new hash values, in case<br>that the preservation submitter is allowed to<br>provide hash values within a hash tree renewal,<br>correspond to the original hash values of the<br>hash tree.|<br> <br> <br> <br> <br> <br>|If applicable,<br>the assessor shall assess the PSP on-site and verify<br>that the preservation submitter:<br>- allows to provide hash values which might be<br>used in a hash tree renewal or not.<br>The assessor shall compare the result on-site with<br>the description in the [T&C] of the PSP.|<br> <br> <br>|||
||_preservation submitter is_||||||||
||_allowed to provide hash values_||||||||
||_which might be used in a hash-_||||||||
||_tree renewal, the PSP shall_||||||||
||_state in its terms and_||||||||
||_conditions that the PSP is not_||||||||
||_liable for guaranteeing that_||||||||
||_the new hash values_||||||||
||_correspond to the original_||||||||
||_hashvalues of the hash tree._||||||||
|**_OVR-6.2-08_**|_[CONDITIONAL] When the_||If applicable,<br>the assessor shall assess the document [T&C]<br>and verify that the PSP:<br>- described that the preservation is only on the<br>submitted objects and that the PSP allows a<br>proof of existence of the hashed object only as<br>long as the hash algorithm, used by the<br>submitter, is strong enough, if the preservation<br>submitter is allowed to provide hash values of<br>objects to preserve, and not the object itself.|<br> <br> <br> <br> <br> <br>|If applicable,<br>the assessor shall assess the PSP on-site and verify<br>that the PSP:<br>- allows the submitter to provide hash values of<br>objects to preserve, and not the object itself.<br>The assessor shall compare the result on-site with<br>the description in the [T&C] of the PSP.|<br> <br>|||
||_preservation submitter is_||||||||
||_allowed to provide hash values_||||||||
||_of objects to preserve, and not_||||||||
||_the object itself, the PSP shall_||||||||
||_state in its terms and_||||||||
||_conditions that the_||||||||
||_preservation is only on the_||||||||
||_submitted objects and that this_||||||||
||_allows a proof of the existence_||||||||
||_of the hashed object only as_||||||||
||_long as the hash algorithm is_||||||||
||_strong enough._||||||||



Federal Office for Information Security 

23 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**6.3**<br>**Information Security Policy**|**6.3**<br>**Information Security Policy**|**6.3**<br>**Information Security Policy**|**6.3**<br>**Information Security Policy**|**6.3**<br>**Information Security Policy**|||||
|---|---|---|---|---|---|---|---|---|
|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.3-01_**|_The requirements specified in_|See<br>**[ETSI EN 319**<br>**401]**<br>and<br>**[ASS 319 401].**|<br>The assessor shall assess the document [IS-<br>Policy] and verify that the PSP:<br>- fulfils the requirements defined in**[ASS 319**<br>**401, REQ-6.3-01]**through**[ASS 319 401,**<br>**REQ-6.3-09]**concerning stage 1,<br>**or**<br>- shows his valid and successful conformity<br>assessment report of the PSP and its PSPS<br>pursuant to**[ETSI EN 319 401],**performed by<br>a conformity assessment body, which is<br>accredited in accordance with**[eIDAS]**as<br>competent.||Only applicable if no valid and successful<br>conformity assessment report of the PSP and its<br>PSPS pursuant to**[ETSI EN 319 401]**exists.<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- fulfils the requirements defined in**[ASS**<br>**319401, REQ-6.3-01]**through**[ASS 319401,**<br>**REQ-6.3-09]**concerning stage 2.|<br> <br>|||
||**_ETSI EN 319 401_**_[1], clause_||||||||
||_6.3 shall apply._||||||||
||||||||||



Federal Office for Information Security 

24 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**6.4**<br>**Preservation profiles**|**6.4**<br>**Preservation profiles**||||||||
|---|---|---|---|---|---|---|---|---|
|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.4-01_**|_A preservation service shall_|See also**OVR-6.2-03**.|See**[ASS 119 511]**,**OVR-6.1-03**.<br>The assessor shall check if the PSP<br>-has supported at least one preservation<br>profile pursuant to OVR-6.1-03,<br>**or**<br>- stated which**[TR-ESOR]**certified<br>product of version V1.2.1 or higher is used<br>for providing the service and this<br>requirement by this PSP.|<br> <br>|If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- support at least one preservation profile for each<br>preservation service.|<br> <br> <br> <br> <br>|||
||_support at least one_||||||||
||_preservation profile._||||||||
||||||||||
|**_OVR-6.4-02_**|_A preservation service may_||See**[ASS 119 511]**,**OVR-6.1-03**.||See**[ASS 119 511]**,**OVR-6.4-01**.||||
||_support more than one_||||||||
||_preservationprofile._||||||||
|**_OVR-6.4-03_**|_A preservation profile shall be_||REMARK: This requirement is fulfilled,<br>if requirement OVR-6.4-04 a) is fulfilled.<br>No additional stage 1 assessment activity<br>is required.||REMARK: This requirement is fulfilled, if<br>requirement OVR-6.4-04 a) is fulfilled. No<br>additional stage 2 assessment activity is required.||||
||_uniquely identified._||||||||
||||||||||
|**_OVR-6.4-04_**|_Apreservationprofile:_||||||||



25 

Federal Office for Information Security 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.4-04_**|_Shall contain the identifier_|See also**[ASS 119**<br>**511]**,**OVR-6.4-03**.|The assessor shall assess the document<br>[PSPS] and verify that the PSP:<br>- included the identifier syntax for each<br>preservation profile,<br>**or**<br>the assessor shall check if the PSP<br>- stated, which**[TR-ESOR]**certified<br>product of version V1.2.1 or higher is<br>used for providing the service and this<br>requirement bythis PSP.|<br>|If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- identifies each installed preservation profile<br>pursuant to_OVR-6.2-03_with an unique identifier.|<br> <br> <br> <br> <br> <br>|||
|**_a)_**|_which uniquely identifies the_||||||||
||_preservation profile._||||||||
||||||||||
|**_OVR-6.4-04_**|_Shall contain the supported_|_EXAMPLE 1:_<br>_In case the hash of the_<br>_data can be provided,_<br>_the list of accepted_<br>_hash functions._<br>_EXAMPLE 2:_<br>_In case of [PDS], the_<br>_supported digital_<br>_signature formats._|The assessor shall assess the preservation<br>profiles and verify that the PSP:<br>- described the supported input formats<br>and<br>additional<br>output<br>formats,<br>if<br>applicable, in each preservation profile or<br>in a documentation referenced by the<br>preservation profile (e.g.**[TR-ESOR-E]**)<br>**or**<br>- stated which**[TR-ESOR]**certified<br>product of version V1.2.1 or higher is used<br>for providing the service and this<br>requirement by this PSP.|<br> <br> <br> <br> <br> <br> <br>|If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- supports the input and additional output formats,<br>if applicable, for each preservation profile as<br>documented in the profile.|<br> <br> <br> <br> <br> <br>|||
|**_b)_**|_operations of the preservation_||||||||
||_protocol. For each operation it:_||||||||
||1<br>_Shall contain the_||||||||
||_supported input_||||||||
||_formats._||||||||
||2<br>_[CONDITIONAL]_||||||||
||_Shall contain_||||||||
||_additional output_||||||||
||_formats, in case other_||||||||
||_output is supported_||||||||
||_that is different from_||||||||
||_the supported input_||||||||
||_format and_||||||||
||_preservation evidence_||||||||
||_format._||||||||



26 

Federal Office for Information Security 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.4-04_**|_Shall contain a set of_|<br>_NOTE 1:_<br>_The preservation_<br>_service policy is not_<br>_covered here._<br>_NOTE 2:_<br>_While the current_<br>_version of the present_<br>_standard assumes that_<br>_a human-readable_<br>_policy document is_<br>_present, future_<br>_versions of the present_<br>_standard may refer to_<br>_a machine-readable_<br>_policy specifications,_<br>_if applicable._|The assessor shall assess the preservation<br>profiles and verify that the PSP:<br>- described for each preservation profile<br>the applicable technical policies, the<br>reference to the preservation evidence<br>policy and conditionally the reference to<br>the<br>signature<br>validation<br>policy,<br>if<br>applicable<br>in<br>case<br>of<br>[PDS]<br>or<br>[PDS+PGD].|<br> <br> <br> <br> <br> <br>|The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- supports the applicable technical policies for<br>each preservation profile as documented in the<br>profile.|<br> <br>|||
|**_c)_**|_applicable technical policies._||||||||
||_The set of policies_||||||||
||•<br>_Shall contain the_||||||||
||_reference to the_||||||||
||_preservation evidence_||||||||
||_policy as defined in_||||||||
||_clause 6.5._||||||||
||•<br>_[PDS][PDS+PGD]_||||||||
||_[CONDITIONAL]_||||||||
||_Shall contain the_||||||||
||_reference to the_||||||||
||_signature validation_||||||||
||_policy as defined in_||||||||
||_clause 6.6, in case the_||||||||
||_client does not provide_||||||||
||_the validation data._||||||||
|**_OVR-6.4-04_**|_Shall contain the validity_|<br>|The assessor shall assess the preservation<br>profiles and verify that the PSP:<br>- described the validity period for each<br>preservation profile, which:<br>+ includes the description of the point in<br>time when the preservation profile has<br>become or will become active and<br>+ may include the description of the point<br>in time until which each preservation<br>profile is active, if applicable.|<br> <br> <br> <br> <br>|The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- implemented the validity period for each<br>preservation profile as described in the profile.<br>The assessor shall compare given validity periods,<br>if more than one is applicable, of each<br>preservation profile with a description in the<br>profile.|<br> <br> <br> <br>|||
|**_d)_**|_period of the profile. The_||||||||
||_validity period:_||||||||
||1. _Shall contain the point_||||||||
||_in time from which on_||||||||
||_the preservation_||||||||
||_profile has become or_||||||||
||_will become active._||||||||
||2. _May contain a point in_||||||||
||_time until which the_||||||||
||_preservation profile is_||||||||
||_active._||||||||



Federal Office for Information Security 

27 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.4-04_**|_Shall contain the preservation_||The assessor shall assess the preservation<br>profiles and verify that the PSP:<br>- included the preservation storage model<br>in each preservation profile.||The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- supports the preservation storage model for each<br>preservation profile as documented in the profile.<br>The assessor shall compare the supported storage<br>model of each preservation profile with the<br>description in theprofile.|<br> <br> <br> <br>|||
|**_e)_**|_storage model (WST, WTS or_||||||||
||_WOS)._||||||||
||||||||||
|**_OVR-6.4-04_**|_Shall contain the preservation_||The assessor shall assess the preservation<br>profiles and verify that the PSP:<br>- included the preservation goals, like<br>PDS, PGD or AUG or a combination of<br>them, in each preservation profile.||The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- supports the preservation goals for each<br>preservation profile as described or referenced in<br>the [PSPS] or [T&C] of the PSP.<br>The assessor shall compare the provided method<br>for each preservation profile with the description<br>in theprofile.|<br> <br> <br> <br>|||
|**_f)_**|_goals (PDS, PGD, AUG or a_||||||||
||_combination of them)._||||||||
||||||||||
|**_OVR-6.4-04_**|_Shall contain all supported_||The assessor shall assess the preservation<br>profiles and verify that the PSP:<br>- described the supported evidence<br>formats for each preservation profile.||The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows the supported evidence formats for each<br>preservation profile.<br>The assessor shall compare the generated<br>evidence formats for each preservation profile<br>with the descriptionprovided in theprofile.|<br> <br> <br>|||
|**_g)_**|_evidence formats._||||||||
||||||||||



Federal Office for Information Security 

28 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.4-04_**|_May contain a specification_||If applicable , the assessor shall assess the<br>preservation profiles and verify that the<br>PSP:<br>- pointed out the specification for each<br>preservation profile,|<br> <br>|If applicable, the assessor shall assess the PSP on-<br>site and verify that the PSP:<br>- shows the publicly available specification for<br>each preservation profile,<br>The assessor shall compare the given specification<br>for each preservation profile with the description<br>in theprofile.|<br> <br>|||
|**_h)_**|_which can be used to refer to a_||||||||
||_publicly available specification_||||||||
||_in which the preservation_||||||||
||_profile is described._||||||||
||||||||||
|**_OVR-6.4-04_**|_May contain an identifier_||If applicable, the assessor shall assess the<br>preservation profiles and verify that the<br>PSP:<br>- pointed out an identifier, which refers to<br>a publicly available specification in which<br>the preservation scheme related to the<br>profile is described, for each preservation<br>profile.|<br> <br>|If applicable, the assessor shall assess the PSP on-<br>site and verify that the PSP:<br>- shows the identifier for each preservation<br>scheme, if used, and<br>- shows the reference to the publicly available<br>specification in which the preservation scheme<br>related to the profile as described.|<br> <br>|||
|**_j)_**|_which can be used to refer to a_||||||||
||_publicly available specification_||||||||
||_in which the preservation_||||||||
||_scheme related to the profile is_||||||||
||_described._||||||||
||||||||||
|**_OVR-6.4-05_**|_[WTS] For a preservation_||Only applicable in case of [WTS]:<br>The assessor shall assess the preservation<br>profiles and verify that the PSP:<br>- described the preservation evidence<br>retention period for each preservation<br>profile, which belongs to a preservation<br>service with temporary storage [WTS].||Only applicable in case of [WTS]:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows the preservation evidence retention period<br>for each preservation profile, which belongs to a<br>preservation service with temporary storage<br>[WTS].<br>The assessor shall compare the given<br>preservation evidence retention period for each<br>preservation profile with the description in the<br>profile.|<br> <br> <br>|||
||_service with temporary storage,_||||||||
||_the preservation profile shall_||||||||
||_contain the preservation_||||||||
||_evidence retention period, i.e._||||||||
||_the time period during which_||||||||
||_the asynchronously produced_||||||||
||_preservation evidence can be_||||||||
||_retrieved from the preservation_||||||||
||_service by the preservation_||||||||
||_client._||||||||
||||||||||



Federal Office for Information Security 

29 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.4-06_**|_[WTS][WOS] For a_||Only applicable in case of [WTS][WOS]:<br>The assessor shall assess the preservation<br>profiles and verify that the PSP:<br>- described the expected evidence<br>duration, if used, for each preservation<br>profile, which belongs to a preservation<br>service with temporary storage or without<br>storage_[WTS] [WOS]_.||Only applicable in case of [WTS][WOS]:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows the expected evidence duration, if used,<br>for each preservation profile and<br>- shows that this/these expected evidence<br>duration(s) belong(s) to a preservation service<br>with temporary storage_[WTS]_or without storage<br>_[WOS]_, if used.<br>The assessor shall compare the given expected<br>evidence duration for each preservation profile<br>with the description in theprofile.|<br> <br> <br> <br>|||
||_preservation service with_||||||||
||_temporary storage or without_||||||||
||_storage, the preservation_||||||||
||_profile should contain the_||||||||
||_expected evidence duration._||||||||
||||||||||



Federal Office for Information Security 

30 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.4-07_**|_[WTS][WOS] The expected_||Only applicable in case of [WTS][WOS]:<br>The assessor shall assess the preservation<br>profiles and verify that the PSP:<br>- based the expected evidence duration on<br>the estimation of the suitability of<br>cryptographic algorithms.<br>This shall be described for each<br>preservation profile, which belongs to the<br>preservation service with temporary<br>storage or without storage_[WTS]_ _[WOS]_,<br>if it is used.|<br> <br>|Only applicable in case of [WTS][WOS]:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows the expected evidence duration on the<br>estimation of the suitability of cryptographic<br>algorithms<br>and<br>- shows that this/these expected evidence<br>duration(s) belong(s) to a preservation service<br>with temporary storage or without storage_[WTS]_<br>_[WOS]_, if used.<br>The assessor shall compare the given date of<br>change including the new value for each<br>preservation profile with the description in the<br>profile.|<br> <br> <br> <br>|||
||_evidence duration shall be_||||||||
||_based on the estimation of the_||||||||
||_suitability of cryptographic_||||||||
||_algorithms._||||||||
||||||||||



Federal Office for Information Security 

31 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.4-08_**|_[WTS][WOS] The expected_|_Note 3: Cryptographic_<br>_suites_<br>_recommendations_<br>_defined in_**_ETSI TS_**<br>**_119 312_**_[i.5] can be_<br>_superseded by_<br>_national_<br>_recommendations._|<br>Only applicable in case of [WTS][WOS]:<br>The assessor shall assess the preservation<br>profiles and verify that the PSP:<br>- described the expected evidence duration<br>based on the estimation of the suitability of<br>cryptographic algorithms pursuant to<br>**[ETSI TS 119 312]**.<br>See also**[ASS 119 511]**,**OVR-6.4-06**&<br>**OVR-6.4-10**.|<br> <br> <br>|Only applicable in case of [WTS][WOS]:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows the expected evidence duration based on<br>the estimation of the suitability of cryptographic<br>algorithms pursuant to**[ETSI TS 119 312]**for<br>each preservation profile,.<br>The assessor shall compare the given expected<br>evidence validation including the estimation of<br>the suitability of cryptographic algorithms<br>pursuant to**[ETSI TS 119 312]**for each<br>preservation profile with the description in the<br>profile.<br>See also**[ASS 119 511]**, **OVR-6.4-10**.|<br> <br> <br> <br> <br> <br> <br> <br>|||
||_evidence duration should be_||||||||
||_based on_**_ETSI TS 119 312_**||||||||
||_[i.5]._||||||||
||||||||||
|**_OVR-6.4-09_**|_The supported preservation_|Note: See also**OVR-**<br>**6.2-03.**|The assessor shall assess the preservation<br>profiles and verify that the PSP:<br>- described where the supported<br>preservation profiles are online available.||The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows where the supported preservation<br>profiles and the preservation profiles, that has<br>been supported, are online available.<br>The PSP presents it live to the assessor at stage 2<br>audit.||||
||_profiles shall be available_||||||||
||_online._||||||||
||||||||||
|**_OVR-6.4-10_**|_A preservation service shall_||See**[ASS 119 511]**,**OVR-6.4-09**and the<br>assessor shall assess the document [PSPS]<br>and verify that the PSP:<br>- described where the preservation<br>profiles, that have been supported, are<br>online available.|<br>|See**[ASS 119 511]**,**OVR-6.4-09**.||||
||_make publicly available all the_||||||||
||_preservation profiles it supports_||||||||
||_or that it has supported._||||||||
||||||||||



Federal Office for Information Security 

32 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.4-11_**|_[WST] The same preservation_||Only applicable in case of [WST]:<br>The assessor shall assess the document<br>[PSPS] and verify that the PSP:<br>- described, that the same preservation<br>profile applies during the whole<br>preservation period for preservation<br>service with storage [WST].||Only applicable in case of [WST]:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows that the same preservation profile applies<br>during the whole preservation period for<br>preservation service with storage [WST].<br>The PSP presents at least one example to the<br>assessor to show that the mechanism works.|<br> <br> <br>|||
||_profile shall apply during the_||||||||
||_whole preservation period._||||||||
||||||||||
|**_OVR-6.4-12_**|_[WTS] The same preservation_||Only applicable in case of [WTS]:<br>The assessor shall assess the document<br>[PSPS] and verify that the PSP:<br>- described, that the same preservation<br>profile apply during the whole<br>preservation evidence retention period for<br>preservation service with temporary<br>storage [WTS].||Only applicable in case of [WTS]:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows that the same preservation profile apply<br>during the whole preservation evidence retention<br>period for preservation service with temporary<br>storage [WTS].<br>The PSP presents at least one example to the<br>assessor to show that the mechanism works.|<br> <br> <br> <br>|||
||_profile shall apply during the_||||||||
||_whole preservation evidence_||||||||
||_retention period._||||||||
||||||||||
|**_OVR-6.4-13_**|_The preservation profile should_||The assessor shall assess the document<br>[PSPS] and verify that the PSP:<br>- described that the preservation profile<br>was not changed and will not be changed<br>and that the dynamic aspects (e.g. the<br>preservation evidence policy or signature<br>validation policy) are specified outside the<br>preservation profile (e.g. the preservation<br>evidence policy or signature validation<br>policy), if applicable.|<br> <br> <br> <br> <br> <br> <br>|The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows that the preservation profile was not<br>changed and will not be changed and that the<br>dynamic aspects (e.g. the preservation evidence<br>policy or signature validation policy) are specified<br>outside the preservation profile (e.g. the<br>preservation<br>evidence<br>policy<br>or<br>signature<br>validation policy).<br>The PSP presents at least one example of a<br>preservation<br>profile<br>and<br>dynamic<br>aspects<br>specified outside,if applicable.|<br> <br> <br> <br> <br> <br> <br> <br>|||
||_not change over time, thus all_||||||||
||_dynamic aspects should be_||||||||
||_specified outside the_||||||||
||_preservation profile (e.g. the_||||||||
||_preservation evidence policy or_||||||||
||_signature validation policy)._||||||||
||||||||||



Federal Office for Information Security 

33 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.4-14_**|_The preservation evidence_|_EXAMPLE 4:_<br>_The preservation_<br>_evidence policy can_<br>_change if the used TSA_<br>_changes or when the_<br>_applied cryptographic_<br>_algorithms change._|<br>The assessor shall assess the document<br>[PSPS] and verify that the PSP:<br>- described where all applicable versions<br>of preservation evidence policies and<br>signature validation policies related to the<br>preservation profile are online available<br>with the clear explanation which version<br>applied at what time.||The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows where all applicable versions of the<br>preservation evidence policies and signature<br>validation policies related to the preservation<br>profile are online available.<br>The PSP presents its clearly described<br>explanation which version applied at what time<br>on the stage 2 on-site audit.||||
||_policies or signature validation_||||||||
||_policies referenced by the_||||||||
||_preservation profile may_||||||||
||_change over time. However, all_||||||||
||_versions related to a specific_||||||||
||_preservation profile shall be_||||||||
||_publicly available, and it shall_||||||||
||_be clear which version applied_||||||||
||_at which time._||||||||



## **6.5 Preservation evidence policy** 

Federal Office for Information Security 

34 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.5-01_**|_The preservation evidence_||The<br>assessor<br>shall<br>assess<br>each<br>preservation evidence policy and verify<br>that the PSP:<br>- described the preservation evidence<br>policy or policies for each preservation<br>profile.<br>The PSP may describe the preservation<br>evidence policy in a human readable<br>form.|<br> <br> <br>|The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows the preservation evidence policy or<br>policies referenced in each preservation profile.<br>The assessor shall cause the PSP to show at least<br>one example for each preservation evidence<br>policy.|<br>|||
||_policy which is referenced by_||||||||
||_the preservation profile (see_||||||||
||**_OVR-6.4-04_**_) may be in human_||||||||
||_readable form._||||||||
||||||||||
|**_OVR-6.5-02_**|_[CONDITIONAL] If there are_||If applicable,<br>the assessor shall assess each preservation<br>evidence policy and verify that the PSP:<br>- described which version takes<br>precedence, if different formats or<br>languages of the preservation evidence<br>policy exist.||If applicable,<br>the assessor shall assess the PSP on-site and verify<br>that the PSP:<br>- shows how the prior version of the preservation<br>evidence policy is demonstrated, if different<br>formats or languages exist.|<br>|||
||_different formats or languages_||||||||
||_of the preservation evidence_||||||||
||_policy, the PSP shall state_||||||||
||_which version takes_||||||||
||_precedence._||||||||
||||||||||



35 

Federal Office for Information Security 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.5-03_**|_The preservation evidence_||The<br>assessor<br>shall<br>assess<br>each<br>preservation evidence policy and verify<br>that the PSP:<br>- described the preservation evidence<br>policy, which contains the description of:<br>+ how the preservation evidence is created<br>and<br>+ the used cryptographic algorithms.<br>See also**[ASS 119 511]**,**OVR-6.5-04**.<br>**or**<br>- stated which**[TR-ESOR]**certified<br>product of version V1.2.1 or higher is used<br>for providing the service and this<br>requirement by this PSP.|<br> <br> <br> <br> <br> <br>|If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows the description of how the preservation<br>evidence is created in the preservation evidence<br>policy or policies referenced by a preservation<br>profile and<br>in the productive process the assessor verifies that<br>- the description of how the preservation evidence<br>is created is fulfilled in practice and<br>- the cryptographic algorithms, used in practice,<br>exist and are comparable with the description in<br>the preservation evidence policy or policies of the<br>PSP.<br>The assessor shall make the PSP show at least one<br>example of a description in the preservation<br>evidence policy and one created preservation<br>evidence for each preservation evidence policy,<br>which shall be checked by the assessor on the base<br>of the preservation evidence policy.<br>See also **[ASS 119 511]**, **OVR-6.5-04**.|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|||
||_policy shall contain the_||||||||
||_description of how the_||||||||
||_preservation evidence is_||||||||
||_created including and which_||||||||
||_cryptographic algorithms are_||||||||
||_used._||||||||
||||||||||



36 

Federal Office for Information Security 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.5-04_**|_The cryptographic algorithms_|_NOTE:_<br>_Cryptographic suites_<br>_recommendations_<br>_defined in_**_ETSI TS_**<br>**_119 312_**_[i.5] can be_<br>_superseded by_<br>_national_<br>_recommendations._|The<br>assessor<br>shall<br>assess<br>each<br>preservation evidence policy and verify<br>that the PSP:<br>- chosen the cryptographic algorithms in<br>the preservation evidence policy or<br>policies based on the cryptographic suites<br>recommendations defined in**[ETSI TS**<br>**119 312]**for each preservation profile.<br>**or**<br>if the standard**[ETSI TS 119 312]**is not<br>used, the assessor shall compare the<br>described cryptographic algorithms with<br>national recommendations.<br>**or**<br>- stated which**[TR-ESOR]**certified<br>product of version V1.2.1 or higher is<br>used for providing the service and this<br>requirement bythis PSP.|<br> <br> <br> <br> <br> <br> <br> <br>|If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise,<br>the assessor shall assess the PSP on-site and verify<br>that the PSP:<br>- uses cryptographic algorithms according to the<br>preservation<br>evidence<br>policy<br>or<br>policies<br>referenced by a preservation profile defined by<br>standard<br>**[ETSI TS 119 312]**<br>or<br>national<br>recommendations.<br>The assessor shall cause the PSP to show at least<br>one example of a preservation evidence for each<br>preservation evidence policy.<br>The assessor shall compare the cryptographic<br>algorithms for each preservation evidence shown<br>for each preservation profile with the description<br>in thepreservation evidencepolicyof the PSP.|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|||
||_used should be chosen_||||||||
||_according to TS 119 312 [i.5]._||||||||
||||||||||



Federal Office for Information Security 

37 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.5-05_**|_The preservation evidence_||The<br>assessor<br>shall<br>assess<br>each<br>preservation evidence policy and verify<br>that the PSP:<br>- described in its preservation evidence<br>policy referenced by a preservation<br>profile, which trust service providers<br>(TSP) are used by the preservation service,<br>if used.<br>The assessor shall also validate, that the<br>PSP described in its preservation<br>evidence policy, referenced by a<br>preservation profile, what and how the<br>trust service providers (TSP) are used by<br>thepreservation service.|<br> <br> <br> <br> <br>|The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows whether and how a trust service provider<br>(TSP) is used by the preservation service for each<br>preservation evidence policy.<br>The assessor shall cause the PSP to show at least<br>one example for each used trust service provider<br>for each preservation evidence policy.<br>The assessor shall compare the given details of<br>how the used trust service provider (TSP) is used<br>by the preservation service with the description<br>in the preservation evidence policy.|<br> <br> <br> <br> <br>|||
||_policy shall contain the_||||||||
||_description of which trust_||||||||
||_service providers (e.g. digital_||||||||
||_signature creation service or_||||||||
||_time stamping authorities,_||||||||
||_certificate status authorities)_||||||||
||_may be used by the_||||||||
||_preservation service._||||||||
||||||||||



Federal Office for Information Security 

38 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.5-06_**|_The preservation evidence_|Note: See also**OVR-**<br>**7.5-02.**|The<br>assessor<br>shall<br>assess<br>each<br>preservation evidence policy and verify<br>that the PSP:<br>- described how the preservation<br>evidence can be validated, including<br>+ the trust anchors to validate the digital<br>signatures within the preservation<br>evidence and<br>+ the trust anchors to validate the time-<br>stamps within the preservation evidence.|<br>|The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- pointed out in each used preservation evidence<br>policy, how the preservation evidence can be<br>validated including the trust anchors needed to<br>validate the digital signatures and/or time-stamps<br>within the preservation evidence and<br>- shows examples of verification reports.<br>The PSP presents at least one preservation<br>evidence verification report of each preservation<br>evidence policy as an example to the assessor on<br>stage 2 on-site audit.<br>The assessor shall compare the implementation<br>of the validation of the preservation evidence and<br>the details of the used trust anchors during the<br>validation of the preservation evidence by the<br>PSP with the description in the preservation<br>evidencepolicyof the PSP.|<br> <br> <br> <br> <br> <br> <br> <br>|||
||_policy shall contain how the_||||||||
||_preservation evidence can be_||||||||
||_validated, including_||||||||
||•<br>_Which trust anchors_||||||||
||_can be used to_||||||||
||_validate digital_||||||||
||_signatures within the_||||||||
||_preservation_||||||||
||_evidence._||||||||
||•<br>_Which trust anchors_||||||||
||_can be used to_||||||||
||_validate time-stamps_||||||||
||_within the_||||||||
||_preservation_||||||||
||_evidence._||||||||
||||||||||



Federal Office for Information Security 

39 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.5-07_**|_[WST][WTS] The preservation_|<br>_NOTE 2:_<br>_See clause 7.15 on_<br>_requirements on_<br>_preservation evidence_<br>_augmentation._|<br>Only applicable in case of [WST], [WTS]:<br>The<br>assessor<br>shall<br>assess<br>each<br>preservation evidence policy and verify<br>that the PSP:<br>- stated in its preservation evidence<br>policy how evidence is augmented and<br>- described the resulting format of the<br>augmented evidence<br>**or**<br>- stated which**[TR-ESOR]**certified<br>product is used for providing the service<br>and this requirement by this PSP.|<br> <br>|Only applicable in case of [WST], [WTS]:<br>If the claimed**[TR-ESOR]**certified product is in<br>fact deployed for providing the service (checked<br>e.g. by comparing the digital fingerprint of the<br>relevant executables), stage 2 will not be<br>executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows how evidence is augmented for each<br>preservation evidence policy of the preservation<br>services (see also**OVR-7.15-01**and**OVR-7.15-**<br>**02**)<br>- shows augmented preservation evidences for<br>each preservation evidence policy referenced by a<br>preservation profile.<br>The assessor shall compare the process and result<br>of the augmentation of the preservation evidence<br>for each preservation evidence policy with the<br>description in thepreservation evidencepolicy.|<br> <br> <br> <br> <br> <br> <br><br> <br> <br>|||
||_service evidence policy shall_||||||||
||_state how evidence is_||||||||
||_augmented._||||||||
||||||||||



Federal Office for Information Security 

40 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.5-08_**|_The preservation evidence_||The<br>assessor<br>shall<br>assess<br>each<br>preservation evidence policy and verify<br>that the PSP:<br>- described in its preservation evidence<br>policy the format of the preservation<br>evidence<br>**or**<br>- stated which**[TR-ESOR]**certified<br>product of version V1.2.1 or higher is used<br>for providing the service and this<br>requirement by this PSP.|<br> <br> <br> <br> <br> <br>|If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables<br>or by inspecting suitable samples), stage 2 will not<br>be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows for each preservation evidence policy the<br>description of the format of the preservation<br>evidence and<br>- shows examples of preservation evidences.<br>The PSP presents at least for each preservation<br>evidence policy examples of preservation<br>evidences to the assessor on stage 2 on-site audit,<br>which the assessor compares with the<br>description(s) of the preservation evidence in the<br>preservation evidencepolicyorpolicies.|<br> <br> <br> <br> <br> <br> <br> <br>|||
||_policy shall describe the_||||||||
||_format of the preservation_||||||||
||_evidence._||||||||
||||||||||



Federal Office for Information Security 

41 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.5-09_**|_The preservation evidence_|<br>|The<br>assessor<br>shall<br>assess<br>each<br>preservation evidence policy and verify<br>that the PSP:<br>- stated if and how the evidence contains<br>explicit information of the applicable<br>preservation<br>service,<br>preservation<br>evidence policy or preservation profile.|<br> <br> <br> <br>|The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows which and how information about<br>preservation service, preservation evidence policy<br>or preservation profile are contained in the<br>evidence (at least one example of each<br>preservation evidence policy), if applicable, and<br>- shows at least one preservation evidence with<br>these information, if applicable.<br>The assessor shall compare the information in the<br>preservation evidence with the description in the<br>preservation evidencepolicy.|<br> <br> <br> <br> <br> <br> <br>|||
||_policy shall state if and, in this_||||||||
||_case, how the evidence_||||||||
||_contains explicit information_||||||||
||_of the applicable_||||||||
||−<br>_Preservation service,_||||||||
||−<br>_Preservation evidence_||||||||
||_policy, or_||||||||
||−<br>_Preservation profile._||||||||
||||||||||



Federal Office for Information Security 

42 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**6.6**<br>**Signature validation policy**|**6.6**<br>**Signature validation policy**|**6.6**<br>**Signature validation policy**|**6.6**<br>**Signature validation policy**|**6.6**<br>**Signature validation policy**|||||
|---|---|---|---|---|---|---|---|---|
|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.6-01_**|_The signature validation policy_||If applicable,<br>the assessor shall assess at least one signature<br>validation policy and verify that the PSP:<br>- described the signature validation policy for<br>at least one preservation profile in a human<br>readable form.||If applicable,<br>the assessor shall assess the PSP on-site and verify<br>that the PSP:<br>- shows at least one signature validation policy in<br>a human readable form, referenced by the<br>preservation profile.|<br> <br>|||
||_contained in the preservation_||||||||
||_profile (see_**_OVR-6.4-04_**_) may_||||||||
||_be in human readable form._||||||||
||||||||||
|**_OVR-6.6-02_**|_[CONDITIONAL] If there are_||If applicable,<br>the assessor shall assess each signature<br>validation policy and verify that the PSP:<br>- described which version takes precedence, if<br>different formats or languages of the signature<br>validation policy exist.||If applicable,<br>the assessor shall assess the PSP on-site and verify<br>that the PSP:<br>- shows how the prior version of the signature<br>validation policy is demonstrated, if different<br>formats or languages of the signature validation<br>policyexist.|<br> <br> <br>|||
||_different formats or languages_||||||||
||_of the signature validation_||||||||
||_policy, the PSP shall state_||||||||
||_which version takes_||||||||
||_precedence._||||||||
||||||||||
|**_OVR-6.6-03_**|_[CONDITIONAL] If present in_|<br>|If applicable,<br>the assessor shall assess each signature<br>validation policy and verify that the PSP:<br>- described how the validation material is<br>selected (e.g. trust anchors, validation model<br>(chain/shell), etc.).||If applicable,<br>the assessor shall assess the PSP on-site and verify<br>that the PSP:<br>- shows how the validation material (e.g. trust<br>anchors, validation model (chain/shell), etc.) of<br>each signature validation policy is selected.<br>The assessor shall compare the implementation of<br>the selection of the validation material with the<br>description in each signature validationpolicy.|<br> <br> <br> <br>|||
||_the preservation profile, the_||||||||
||_signature validation policy_||||||||
||_shall state the strategy to how_||||||||
||_the validation material is_||||||||
||_selected, e.g. trust anchors,_||||||||
||_validation model (chain/shell),_||||||||
||_etc._||||||||
||||||||||



Federal Office for Information Security 

43 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

## **6.7 Subscriber agreement** 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.7-01_**|_The PSP shall provide a_||The assessor shall assess the document<br>subscriber agreement and verify that the PSP:<br>- pointed out the acceptance of the terms and<br>conditions.||not applicable||||
||_subscriber agreement, which_||||||||
||_shall include an acceptance of_||||||||
||_the terms and conditions._||||||||
|**_OVR-6.7-02_**|_[CONDITIONAL] If the_||If applicable,<br>the assessor shall assess the document<br>subscriber agreement and verify that the PSP:<br>- described whether and how the subscriber<br>would like to be notified, if a notification<br>protocol is used.||If applicable,<br>the assessor shall assess the PSP on-site and verify<br>that the PSP:<br>- shows whether and how the subscriber will be<br>notified, if a notification protocol is used.<br>The assessor shall compare the notification<br>process with the subscriber agreement of the PSP.|<br> <br> <br>|||
||_preservation service provides_||||||||
||_a notification protocol, the_||||||||
||_PSP shall state in the_||||||||
||_subscriber agreement whether_||||||||
||_and how the subscriber would_||||||||
||_like to be notified._||||||||
||||||||||
|**_OVR-6.7-03_**|_[CONDITIONAL] If the_||If applicable,<br>the assessor shall assess the document<br>subscriber agreement and verify that the PSP:<br>- described, that the subscriber agreement will<br>be updated each time in a way to notify the<br>subscriber is removed or added, if the<br>notification protocol is used.<br>The assessor may compare older versions of<br>the subscriber agreement with the current<br>version.|<br> <br> <br>|See**OVR-6.7-02.**||||
||_preservation service provides_||||||||
||_a notification protocol, the_||||||||
||_PSP shall update the_||||||||
||_subscriber agreement each_||||||||
||_time a way to notify the_||||||||
||_subscriber is removed or_||||||||
||_added._||||||||
||||||||||



Federal Office for Information Security 

44 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-6.7-04_**|_[WTS][WST] The PSP shall_||Only applicable in case of [WST], [WTS]:<br>The assessor shall assess the document<br>subscriber agreement and verify that the PSP:<br>- described who has the right to access to POs<br>including the SubDOs and preservation<br>evidences.||Only applicable in case of [WST], [WTS]:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows who has the right to access to POs<br>including<br>the<br>SubDOs<br>and<br>preservation<br>evidences.<br>The assessor shall compare the access rights,<br>customised in practice, with the description of<br>the rights to access in the subscriber agreement.|<br> <br>|||
||_state in the subscriber_||||||||
||_agreement who has the right to_||||||||
||_access to POs including the_||||||||
||_SubDOs and preservation_||||||||
||_evidences._||||||||
||||||||||
|**_OVR-6.7-05_**|_[WTS][WST] The PSP shall_||Only applicable in case of [WST], [WTS]:<br>The assessor shall assess the document<br>subscriber agreement and verify that the PSP:<br>- described who has the right to request traces<br>on the actions related to the POs.||Only applicable in case of [WST], [WTS]:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows who has the right to request traces on the<br>actions related to the POs.<br>The assessor shall compare the access rights,<br>customised in practice, with the description of<br>the rights to request traces in the subscriber<br>agreement.|<br>|||
||_state in the subscriber_||||||||
||_agreement who has the right to_||||||||
||_request traces on the actions_||||||||
||_related to the POs._||||||||
||||||||||



45 

Federal Office for Information Security 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

## **7 Assessment criteria for PSP Management and Operation** 

## **7.1 Internal organization** 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-7.1-01_**|_The requirements specified in_|<br> <br>See<br>**[ETSI EN 319**<br>**401]**<br>and<br>**[ASS 319 401].**|<br>The assessor shall assess the  documentation of<br>the PSP and verify that the PSP:<br>- fulfils the requirements defined in<br>**[ASS 319401, REQ-7.1.1-01]**through<br>**[ASS 319401, REQ-7.1.1-07]**and<br>**[ASS 319401, REQ-7.1.2-01]**concerning<br>stage 1,<br>or<br>- shows his valid and successful conformity<br>assessment report of the PSP and its PSPS<br>pursuant to**[ETSI EN 319 401],**performed by<br>a conformity assessment body, which is<br>accredited in accordance with**[eIDAS]**as<br>competent.|<br>|Only applicable if no valid and successful<br>conformity assessment report of the PSP and its<br>PSPS pursuant to**[ETSI EN 319 401]**exists.<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- fulfils the requirements defined in<br>**[ASS 319401, REQ-7.1.1-01]**through<br>**[ASS 319401, REQ-7.1.1-07]**and<br>**[ASS 319401, REQ-7.1.2-01]**concerning<br>stage 2.|<br> <br> <br>|||
||**_ETSI EN 319 401_**_[1], clause_||||||||
||_7.1 shall apply._||||||||
||||||||||



46 

Federal Office for Information Security 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**7.2**<br>**Human resources**|**7.2**<br>**Human resources**|**7.2**<br>**Human resources**|**7.2**<br>**Human resources**|**7.2**<br>**Human resources**|||||
|---|---|---|---|---|---|---|---|---|
|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-7.2-01_**|_The requirements specified in_|<br> <br>See<br>**[ETSI EN 319**<br>**401]**<br>and<br>**[ASS 319 401].**|<br>The assessor shall assess the  documentation of<br>the PSP and verify that the PSP:<br>- fulfils the requirements defined in<br>**[ASS 319401, REQ-7.2-01]**through<br>**[ASS 319401, REQ-7.2-17]**concerning<br>stage 1,<br>or<br>- shows his valid and successful conformity<br>assessment report of the PSP and its PSPS<br>pursuant to**[ETSI EN 319 401],**performed by<br>a conformity assessment body, which is<br>accredited in accordance with**[eIDAS]**as<br>competent.|<br>|Only applicable if no valid and successful<br>conformity assessment report of the PSP and its<br>PSPS pursuant to**[ETSI EN 319 401]**exists.<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>-<br>fulfils<br>the<br>requirements<br>defined<br>in<br>[**ASS 319401, REQ-7.2-01]**<br>through<br>**[ASS 319401, REQ-7.2-17]**concerning stage 2.|<br> <br> <br> <br> <br>|||
||**_ETSI EN 319 401_**_[1], clause_||||||||
||_7.2 shall apply._||||||||
||||||||||



Federal Office for Information Security 

47 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**7.3**<br>**Asset management**|**7.3**<br>**Asset management**|**7.3**<br>**Asset management**|**7.3**<br>**Asset management**|**7.3**<br>**Asset management**|||||
|---|---|---|---|---|---|---|---|---|
|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-7.3-01_**|_The requirements specified in_|<br> <br>See<br>**[ETSI EN 319**<br>**401]**<br>and<br>**[ASS 319 401].**|<br>The assessor shall assess the  documentation of<br>the PSP and verify that the PSP:<br>- fulfils the requirements defined in<br>**[ASS 319401, REQ-7.3.1-01]**through<br>**[ASS 319401, REQ-7.3.1-02]**and<br>**[ASS 319401, REQ-7.3.2-01]**concerning<br>stage 1,<br>or<br>- shows his valid and successful conformity<br>assessment report of the PSP and its PSPS<br>pursuant to**[ETSI EN 319 401],**performed by<br>a conformity assessment body, which is<br>accredited in accordance with**[eIDAS]**as<br>competent.||Only applicable if no valid and successful<br>conformity assessment report of the PSP and its<br>PSPS pursuant to**[ETSI EN 319 401]**exists.<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- fulfils the requirements defined in<br>**[ASS 319401, REQ-7.3.1-01]**through<br>**[ASS 319401, REQ-7.3.1-02]**and<br>**[ASS 319401, REQ-7.3.2-01]**concerning<br>stage 2.|<br> <br>|||
||**_ETSI EN 319 401_**_[1], clause_||||||||
||_7.3 shall apply_||||||||
||||||||||



Federal Office for Information Security 

48 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

## **7.4 Access control** 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-7.4-01_|_The requirements specified in_|<br> <br>See<br>**[ETSI EN 319**<br>**401]**<br>and<br>**[ASS 319 401].**|<br>The assessor shall assess the  documentation of<br>the PSP and verify that the PSP:<br>- fulfils the requirements defined in<br>**[ASS 319 401, REQ-7.4-01]**through<br>**[ASS 319 401,** **REQ-7.4-10]**concerning<br>stage 1,<br>or<br>**-**shows his valid and successful conformity<br>assessment report of the PSP and its PSPS<br>pursuant to [**ETSI EN 319 401]**, performed by<br>a conformity assessment body, which is<br>accredited in accordance with [**eIDAS]**as<br>competent.|<br>|Only applicable if no valid and successful<br>conformity assessment report of the PSP and its<br>PSPS pursuant to**[ETSI EN 319 401]**exists.<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- fulfils the requirements defined in<br>**[ASS 319401, REQ-7.4-01]**through<br>**[ASS 319401, REQ-7.4-10]**concerning stage 2.|<br> <br> <br>|||
||**_ETSI EN 319 401_**_[1], clause_||||||||
||_7.4 shall apply._||||||||
||||||||||



Federal Office for Information Security 

49 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**7.5**<br>**Cryptographic controls**|**7.5**<br>**Cryptographic controls**|**7.5**<br>**Cryptographic controls**|**7.5**<br>**Cryptographic controls**|**7.5**<br>**Cryptographic controls**|**7.5**<br>**Cryptographic controls**|**7.5**<br>**Cryptographic controls**|**7.5**<br>**Cryptographic controls**|**7.5**<br>**Cryptographic controls**|
|---|---|---|---|---|---|---|---|---|
|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-7.5-01_**|_The requirements specified in_|<br> <br>See<br>**[ETSI EN 319**<br>**401]**<br>and<br>**[ASS 319 401].**|<br>The assessor shall assess the  documentation of<br>the PSP and verify that the PSP:<br>- fulfils the requirements defined in<br>**[ASS 319 401, REQ-7.5-01]**concerning<br>stage 1,<br>or<br>**-**shows his valid and successful conformity<br>assessment report of the PSP and its PSPS<br>pursuant to [**ETSI EN 319 401]**, performed by<br>a conformity assessment body, which is<br>accredited in accordance with [**eIDAS]**as<br>competent.|<br>|Only applicable if no valid and successful<br>conformity assessment report of the PSP and its<br>PSPS pursuant to**[ETSI EN 319 401]**exists.<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- fulfils the requirements defined in<br>**[ASS 319401, REQ-7.5-01]**concerning stage 2.|<br> <br> <br>|||
||**_ETSI EN 319 401_**_[1], clause_||||||||
||_7.5 shall apply._||||||||
||||||||||



50 

Federal Office for Information Security 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-7.5-02_**|_The PSP shall insure that the_|<br> <br>_NOTE:_<br>_In the_<br>_EU context, one_<br>_or more_<br>_preservation_<br>_profiles may use_<br>_Qualified TSAs._<br>See<br>**[ASS 119 511]**<br>**OVR-6.5-05**,<br>**OVR-6.5-06**<br>and<br>**OVR-6.1-06.**|The assessor shall assess the documentation of<br>the PSP (e.g. document [PSPS] or preservation<br>evidence policy) and verify that the PSP:<br>- described for each preservation evidence<br>policy, that the time-stamps used in the<br>preservation process come from a time stamping<br>authority (TSA) which follows state-of-the-art<br>practices for…<br>+ policy and security requirements for trust<br>service providers issuing time-stamps<br>**or**<br>- stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing<br>the service and this requirement by this PSP.<br>The assessor shall verify that the PSP described<br>in the preservation evidence policy applicable<br>TSAs, which are conform to**[ETSI EN 319**<br>**421]**for each preservation profile.|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- has used time-stamps in the preservation process<br>from a time stamping authority (TSA) which<br>follows state-of-the-art practices for policy and<br>security requirements for trust service providers<br>issuing time-stamp, in particular conform to<br>**[ETSI EN 319 421]**, for each preservation<br>evidence  policy.<br>The assessor shall cause the PSP to show at least<br>one received example of created time-stamps<br>from a state-of-the-art trust service provider<br>conform to**[ETSI EN 319 421]**for each<br>preservation evidence policy referenced by a<br>preservation profile.<br>The assessor shall compare the identified TSAs<br>with the description in the preservation evidence<br>policy of the PSP for each preservation evidence<br>policy.|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|||
||_time-stamps used in_||||||||
||_preservation process come_||||||||
||_from a TSA that follows state-_||||||||
||_of-the-art practices for policy_||||||||
||_and security requirements for_||||||||
||_trust service providers_||||||||
||_issuing time-stamps. In_||||||||
||_particular the TSA should_||||||||
||_conform to_**_ETSI EN 319 421_**||||||||
||_[i.11]._||||||||
||||||||||



51 

Federal Office for Information Security 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-7.5-03_**|_The PSP should only use in_||The assessor shall assess the documentation of<br>the PSP (e.g. the preservation evidence policy)<br>and verify that the PSP:<br>- described that the used time-stamps are<br>verifiable using CRLs or OCSP responses<br>which include a reason code in case of the<br>revocation of a public key certificate, if<br>applicable<br>**or**<br>- stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing<br>the service and this requirement by this PSP.|<br> <br> <br> <br> <br> <br> <br>|If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- has used time-stamps, which are verifiable using<br>CRLs or OCSP responses with a reason code in<br>case of revocation of a public key certificate, if<br>applicable.<br>The assessor shall cause the PSP to show at least<br>one example of a time-stamp with its verification<br>report for each preservation evidence policy.<br>The assessor shall compare the details about the<br>distribution point of the time-stamps with the<br>description in the [PSPS] of the PSP, if applicable.|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|||
||_preservation process time-_||||||||
||_stamps that are verifiable_||||||||
||_using CRLs or OCSP_||||||||
||_responses which include a_||||||||
||_'reason code' in case of the_||||||||
||_revocation of a public key_||||||||
||_certificate._||||||||
||||||||||
||||||||||
||||||||||



52 

Federal Office for Information Security 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-7.5-04_**|_[CONDITIONAL] When PSP_|<br>Note: See**OVR-**<br>**6.1-06, OVR-**<br>**7.5-04.**|If applicable,<br>the assessor shall assess the  documentation of<br>the PSP and verify that the PSP:<br>- described which signing certificate from which<br>provider according to which standard (**[ETSI**<br>**EN 319 411-1]**or**[ETSI EN 319 411-2]**) is<br>used to signs (part of) preservation evidences.|<br> <br> <br> <br>|If applicable,<br>the assessor shall assess the PSP on-site and verify<br>that the PSP:<br>- has used a signing certificate from a provider,<br>which is**[ETSI EN 319 411-1]**or**[ETSI EN 319**<br>**411-2]**conform, to sign (part of) preservation<br>evidences.<br>The assessor shall cause the PSP to show at least<br>one example of a signing certificate from a<br>trustworthy CA for a signed preservation evidence<br>and the signature for each preservation evidence<br>policy.<br>The assessor shall compare the signing certificate<br>and its provider with the description in the<br>preservation evidence policy of the PSP and<br>check,whether the CA is trustworthy.|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|||
||_signs (part of) a preservation_||||||||
||_evidence, the PSP should_||||||||
||_select a signing certificate_||||||||
||_issued by a trustworthy CA_||||||||
||_that implements_**_ETSI EN_**||||||||
||**_319 411-1_**_[i.9] or_**_ETSI EN_**||||||||
||**_319 411-2_**_[i.10]._||||||||
||||||||||
|**_OVR-7.5-05_**|_[CONDITIONAL] When PSP_||REMARK: This requirement is only applicable,<br>if the PSP signs (part of) preservation evidences.<br>When this requirement is applicable, the<br>following requirements OVR-7.5-05 a) and<br>OVR-7.5-05 b) has to be fulfilled. No additional<br>stage 1 assessment activityis required.|<br> <br> <br> <br>|REMARK: This requirement is only applicable, if<br>the PSP signs (part of) preservation evidences.<br>When this requirement is applicable, the<br>following requirements OVR-7.5-05 a) and OVR-<br>7.5-05 b) has to be fulfilled. No additional stage 2<br>assessment activityis required.|<br> <br> <br>|||
||_signs (part of) a preservation_||||||||
||_evidence, the PSP private_||||||||
||_signing key shall be held and_||||||||
||_used within a cryptographic_||||||||
||_module which;_||||||||



53 

Federal Office for Information Security 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-7.5-05 a)_**|_Is a trustworthy system which_|<br> <br>|If applicable,<br>the assessor shall assess the documentation of<br>the PSP and verify that the PSP:<br>- described which cryptographic module for the<br>private key of the signing certificate, is used and<br>- described on which standard/norm or<br>national/international evaluation criteria the<br>cryptographic module is accorded.|<br> <br> <br> <br> <br>|If applicable,<br>the assessor shall assess the PSP on-site and verify<br>that the PSP:<br>- has used a cryptographic module for the private<br>key of its signing certificate which is according to<br>EAL 4 or higher in accordance with**[ISO/IEC**<br>**15408]**or equivalent national or international<br>recognized evaluation criteria.<br>The assessor shall compare the cryptographic<br>module and its evaluation with the description in<br>the [PSPS] of the PSP.|<br> <br> <br> <br> <br> <br> <br>|||
||_is assured to EAL 4 or higher_||||||||
||_in accordance with_**_ISO/IEC_**||||||||
||**_15408_**_[3], or equivalent_||||||||
||_national or internationally_||||||||
||_recognized evaluation_||||||||
||_criteria for IT security. This_||||||||
||_shall be to a security target_||||||||
||_or protection profile which_||||||||
||_meets the requirements of the_||||||||
||_present document, based on a_||||||||
||_risk analysis and taking into_||||||||
||_account physical and other_||||||||
||_non-technical security_||||||||
||_measures; or_||||||||
|**_OVR-7.5-05 b)_**|_Meets the requirements_||If applicable,<br>the assessor shall assess the documentation of<br>the PSP and verify that the PSP:<br>- described, that its cryptographic module for<br>the private key of the signing certificate meets<br>the requirements identified in**[ISO/IEC 19790]**<br>or**[FIPS PUB 140-2]**,level 3.|<br> <br> <br>|If applicable,<br>the assessor shall assess the PSP on-site and verify<br>that the PSP:<br>- has used a cryptographic module for the private<br>key of the signing certificate which meets the<br>requirements identified in**[ISO/IEC 19790]**or<br>**[FIPS PUB 140-2]**level 3.|<br> <br> <br>|||
||_identified in_**_ISO/IEC 19790_**||||||||
||_[4] or_**_FIPS PUB 140-2_**_[5],_||||||||
||_level 3._||||||||
||||||||||
|**_OVR-7.5-06_**|_[CONDITIONAL] When PSP_|<br>|If applicable,<br>see**[ASS 119 511]**,**OVR-7.5-05 a)**.||If applicable,<br>see**[ASS 119 511]**,**OVR-7.5-05 a)**.||||
||_signs (part of) a preservation_||||||||
||_evidence, the secure_||||||||
||_cryptographic device_||||||||
||_required by_**_OVR-7.5-05_**||||||||
||_should be as per_**_OVR-7.5-05_**||||||||
||**_a)_**_._||||||||



54 

Federal Office for Information Security 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_OVR-7.5-07_**|_[CONDITIONAL] When PSP_||If applicable,<br>the assessor shall assess the documentation of<br>the PSP and verify that the PSP:<br>- described how the integrity and confidentiality<br>of the private signing keys is ensured, when<br>signing certificates and backup copies of the<br>private signing keys are used.|<br> <br> <br> <br>|If applicable,<br>the assessor shall assess the PSP on-site and verify<br>that the PSP:<br>- shows how the integrity and confidentiality of<br>the private signing keys is ensured, if signing<br>certificates and backup copies of the private<br>signing keys are used.|<br> <br> <br> <br>|||
||_signs (part of) a preservation_||||||||
||_evidence, any backup copies_||||||||
||_of the PSP private signing_||||||||
||_keys shall be protected to_||||||||
||_ensure its integrity and_||||||||
||_confidentiality by the_||||||||
||_cryptographic module before_||||||||
||_being stored outside that_||||||||
||_device._||||||||



55 

Federal Office for Information Security 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**7.6**<br>**Physical and environmental security**|**7.6**<br>**Physical and environmental security**|**7.6**<br>**Physical and environmental security**|**7.6**<br>**Physical and environmental security**|**7.6**<br>**Physical and environmental security**|||||
|---|---|---|---|---|---|---|---|---|
|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-7.6-01_|_The requirements specified in_|<br> <br>See<br>**[ETSI EN 319**<br>**401]**<br>and<br>**[ASS 319 401].**|<br>The assessor shall assess the documentation of<br>the PSP and verify that the PSP:<br>- fulfils the requirements defined in<br>**[ASS 319401, REQ-7.6-01]**through<br>**[ASS 319401, REQ-7.6-05]**concerning<br>stage 1,<br>or<br>- shows his valid and successful conformity<br>assessment report of the PSP and its PSPS<br>pursuant to**[ETSI EN 319 401],**performed by<br>a conformity assessment body, which is<br>accredited in accordance with**[eIDAS]**as<br>competent.|<br>|Only applicable if no valid and successful<br>conformity assessment report of the PSP and its<br>PSPS pursuant to**[ETSI EN 319 401]**exists.<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- fulfils the requirements defined in<br>**[ASS 319401, REQ-7.6-01]**through<br>**[ASS 319401, REQ-7.6-05]**concerning stage 2.|<br> <br> <br>|||
||**_ETSI EN 319 401_**_[1], clause_||||||||
||_7.6 shall apply._||||||||
||||||||||
||||||||||



56 

Federal Office for Information Security 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**7.7**<br>**Operation security**|**7.7**<br>**Operation security**|**7.7**<br>**Operation security**|**7.7**<br>**Operation security**|**7.7**<br>**Operation security**|||||
|---|---|---|---|---|---|---|---|---|
|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-7.7-01_|_The requirements specified in_|<br> <br>See<br>**[ETSI EN 319**<br>**401]**<br>and<br>**[ASS 319 401].**|<br>The assessor shall assess the  documentation of<br>the PSP and verify that the PSP:<br>- fulfils the requirements defined in<br>**[ASS 319401, REQ-7.7-01]**through<br>**[ASS 319401, REQ-7.7-09]**concerning<br>stage 1,<br>or<br>- shows his valid and successful conformity<br>assessment report of the PSP and its PSPS<br>pursuant to**[ETSI EN 319 401],**performed by<br>a conformity assessment body, which is<br>accredited in accordance with**[eIDAS]**as<br>competent.|<br>|Only applicable if no valid and successful<br>conformity assessment report of the PSP and its<br>PSPS pursuant to**[ETSI EN 319 401]**exists.<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- fulfils the requirements defined in<br>**[ASS 319401, REQ-7.7-01]**through<br>**[ASS 319401, REQ-7.7-09]**concerning stage 2.|<br> <br> <br>|||
||**_ETSI EN 319 401_**_[1], clause_||||||||
||_7.7 shall apply._||||||||
||||||||||



57 

Federal Office for Information Security 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

## **7.8 Network security** 

_NOTE: See clause 13 of ISO/IEC 27002:2013 [i.3] for guidance._ 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-7.8-01_|_The requirements specified in_|<br> <br>See<br>**[ETSI EN 319**<br>**401]**<br>and<br>**[ASS 319 401].**|<br>The assessor shall assess the  documentation of<br>the PSP and verify that the PSP:<br>- fulfils the requirements defined in<br>**[ASS 319401, REQ-7.8-01]**through<br>**[ASS 319401, REQ-7.8-15]**concerning<br>stage 1,<br>or<br>- shows his valid and successful conformity<br>assessment report of the PSP and its PSPS<br>pursuant to**[ETSI EN 319 401],**performed by<br>a conformity assessment body, which is<br>accredited in accordance with**[eIDAS]**as<br>competent.||Only applicable if no valid and successful<br>conformity assessment report of the PSP and its<br>PSPS pursuant to**[ETSI EN 319 401]**exists.<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- fulfils the requirements defined in<br>**[ASS 319401, REQ-7.8-01]**through<br>**[ASS 319401, REQ-7.8-14]**concerning stage 2.|<br> <br>|||
||**_ETSI EN 319 401_**_[1], clause_||||||||
||_7.8 shall apply._||||||||
||||||||||



58 

Federal Office for Information Security 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-7.8-02_|_[WST] The preservation_||Only applicable in case of [WST]:<br>The assessor shall assess the documentation of<br>the PSP (e.g. [PSPS] or [T&C]) and verify that<br>the PSP:<br>- described the integration of the preservation<br>service in the IT environment and the<br>implementation of the preservation service in<br>such a way that all storage access by the<br>preservation client changing the content of the<br>storage cannot bypass the preservation service.|<br>|Only applicable in case of [WST]:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- integrated and implemented the preservation<br>service in such a way that all storage access by<br>the preservation client changing the content of<br>the storage cannot bypass the preservation<br>service.<br>The assessor shall compare the integration and<br>implementation of the preservation service with<br>the description in the [PSPS] or [T&C] of the<br>PSP.||||
||_service shall be integrated in_||||||||
||_the IT environment_||||||||
||_implemented in such a way_||||||||
||_that all storage access by the_||||||||
||_preservation client changing_||||||||
||_the content of the storage_||||||||
||_cannot bypass the_||||||||
||_preservation service._||||||||
||||||||||



59 

Federal Office for Information Security 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**7.9**<br>**Incident management**|**7.9**<br>**Incident management**|**7.9**<br>**Incident management**|**7.9**<br>**Incident management**|**7.9**<br>**Incident management**|||||
|---|---|---|---|---|---|---|---|---|
|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-7.9-01_|_The requirements specified in_|<br> <br>See<br>**[ETSI EN 319**<br>**401]**<br>and<br>**[ASS 319 401].**|<br>The assessor shall assess the documentation of<br>the PSPS and verify that the PSP:<br>- fulfils the requirements defined in<br>**[ASS 319401, REQ-7.9-01]**through<br>**[ASS 319401, REQ-7.9-12]**concerning<br>stage 1,<br>or<br>- shows his valid and successful conformity<br>assessment report of the PSP and its PSPS<br>pursuant to**[ETSI EN 319 401],**performed by<br>a conformity assessment body, which is<br>accredited in accordance with**[eIDAS]**as<br>competent.||Only applicable if no valid and successful<br>conformity assessment report of the PSP and its<br>PSPS pursuant to**[ETSI EN 319 401]**exists.<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- fulfils the requirements defined in<br>**[ASS 319401, REQ-7.9-01]**through<br>**[ASS 319401, REQ-7.9-12]**concerning stage 2.|<br> <br>|||
||**_ETSI EN 319 401_**_[1], clause_||||||||
||_7.9 shall apply_||||||||
||||||||||



60 

Federal Office for Information Security 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

## **7.10 Collection of evidence** 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-7.10-01_|_The requirements specified in_|<br> <br>See<br>**[ETSI EN 319**<br>**401]**<br>and<br>**[ASS 319 401].**|<br>The assessor shall assess the documentation of<br>the PSP and verify that the PSP:<br>- fulfils the requirements defined in<br>**[ASS 319401, REQ-7.10-01]**through<br>**[ASS 319401, REQ-7.10-08]**concerning<br>stage 1,<br>or<br>- shows his valid and successful conformity<br>assessment report of the PSP and its PSPS<br>pursuant to**[ETSI EN 319 401],**performed by<br>a conformity assessment body, which is<br>accredited in accordance with**[eIDAS]**as<br>competent.|<br>|Only applicable if no valid and successful<br>conformity assessment report of the PSP and its<br>PSPS pursuant to**[ETSI EN 319 401]**exists.<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- fulfils the requirements defined in<br>**[ASS 319401, REQ-7.10-01]**through<br>**[ASS 319401, REQ-7.10-08]**concerning stage 2.|<br> <br> <br> <br>|||
||**_ETSI EN 319 401_**_[1], clause_||||||||
||_7.10 shall apply._||||||||
||||||||||



61 

Federal Office for Information Security 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-7.10-02_|_The preservation service_||The assessor shall assess the documentation of<br>the PSP (e.g. [PSPS] or [T&C]) and verify that<br>the PSP:<br>- described the event logs process of the<br>preservation service<br>**or**<br>- stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing<br>the service and this requirement by this PSP.|<br> <br> <br>|If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- implemented the event logs process.<br>The assessor shall cause the PSP to show at least<br>one example of an event log for each preservation<br>evidence policy.<br>The assessor shall compare the event logs<br>process in practice with the description in the<br>[PSPS]or[T&C]of the PSP.|<br> <br> <br> <br> <br> <br> <br>|||
||_shall implement event logs to_||||||||
||_establish information needed_||||||||
||_for later proofs._||||||||
||||||||||



62 

Federal Office for Information Security 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**7.11**<br>**Business continuity management**|**7.11**<br>**Business continuity management**|**7.11**<br>**Business continuity management**|**7.11**<br>**Business continuity management**|**7.11**<br>**Business continuity management**|||||
|---|---|---|---|---|---|---|---|---|
|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-7.11-01_|_The requirements specified in_|<br> <br>See<br>**[ETSI EN 319**<br>**401]**<br>and<br>**[ASS 319 401].**|<br>The<br>assessor<br>shall<br>assess<br>the<br>(public)<br>documentation of the PSP and verify that the<br>PSP:<br>- fulfils the requirements defined in<br>**[ASS 319401, REQ-7.11-01]**through<br>**[ASS 319401, REQ-7.11-02]**concerning<br>stage 1,<br>or<br>- shows his valid and successful conformity<br>assessment report of the PSP and its PSPS<br>pursuant to**[ETSI EN 319 401],**performed by<br>a conformity assessment body, which is<br>accredited in accordance with**[eIDAS]**as<br>competent.|<br>|Only applicable if no valid and successful<br>conformity assessment report of the PSP and its<br>PSPS pursuant to**[ETSI EN 319 401]**exists.<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- fulfils the requirements defined in<br>**[ASS 319401, REQ-7.11-01]**through<br>**[ASS 319401, REQ-7.11-02]**concerning stage 2.|<br> <br> <br>|||
||**_ETSI EN 319 401_**_[1], clause_||||||||
||_7.11 shall apply._||||||||
||||||||||



63 

Federal Office for Information Security 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**7.12**<br>**TSP **|**termination and termination plans**|**termination and termination plans**|**termination and termination plans**|**termination and termination plans**|||||
|---|---|---|---|---|---|---|---|---|
|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-7.12-01_|_The requirements specified in_|<br> <br>See<br>**[ETSI EN 319**<br>**401]**<br>and<br>**[ASS 319 401].**|<br>The<br>assessor<br>shall<br>assess<br>the<br>(public)<br>documentation of the PSP including a<br>termination plan and verify that the PSP:<br>- fulfils the requirements defined in<br>**[ASS 319401, REQ-7.12-01]**through<br>**[ASS 319401, REQ-7.12-11]**concerning<br>stage 1,<br>or<br>- shows his valid and successful conformity<br>assessment report of the PSP and its PSPS<br>pursuant to**[ETSI EN 319 401],**performed by<br>a conformity assessment body, which is<br>accredited in accordance with**[eIDAS]**as<br>competent.|<br> <br>|Only applicable if no valid and successful<br>conformity assessment report of the PSP and its<br>PSPS pursuant to**[ETSI EN 319 401]**exists.<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- fulfils the requirements defined in<br>**[ASS 319401, REQ-7.12-01]**through<br>**[ASS 319401, REQ-7.12-11]**concerning stage 2.|<br> <br> <br> <br>|||
||**_ETSI EN 319 401_**_[1], clause_||||||||
||_7.12 shall apply._||||||||
||||||||||
|_OVR-7.12-02_|_[WST] The termination plan_||Only applicable in case of [WST]:<br>The assessor shall assess the termination plan<br>and verify that the PSP:<br>- described what happens with the stored POs at<br>the termination of thepreservation service.|<br>|not applicable||||
||_shall include what happens_||||||||
||_with the stored POs at the_||||||||
||_termination of the_||||||||
||_preservation service._||||||||
||||||||||



64 

Federal Office for Information Security 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

## **7.13 Compliance** 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-7.13-01_|_The requirements specified in_|<br>See<br>**[ETSI EN 319**<br>**401]**<br>and<br>**[ASS 319 401].**|<br>The<br>assessor<br>shall<br>assess<br>the<br>(public)<br>documentation of the  PSP and verify that the<br>PSP:<br>- fulfils the requirements defined in<br>**[ETSI EN 319401, REQ-7.13-01]**through<br>**[ETSI EN 319401, REQ-7.13-05]**concerning<br>stage 1,<br>or<br>- shows his valid and successful conformity<br>assessment report of the PSP and its PSPS<br>pursuant to**[ETSI EN 319 401],**performed by<br>a conformity assessment body, which is<br>accredited in accordance with**[eIDAS]**as<br>competent.<br>If sector-specific legal requirements exist (e.g.<br>**[EGovG]**,**[eIDAS]**), the assessor shall verify<br>that these requirements are fulfilled by the PSP.<br>In case of preservation services in public sector<br>in Germany § 6**[EGovG**] requires, that the<br>implemented preservation product shall be<br>state-of-the-art by fulfilling the BSI-TR-03125<br>**[TR_ESOR]**.<br>The eIDAS Regulation is fulfilled by**[TR-**<br>**ESOR]**version 1.2.1 and all higher versions.|<br> <br> <br>|Only applicable if no valid and successful<br>conformity assessment report of the PSP and its<br>PSPS pursuant to**[ETSI EN 319 401]**exists.<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- fulfils the requirements defined in<br>**[ETSI EN 319401, REQ-7.13-01]**through<br>**[ETSI EN 319401, REQ-7.13-05]**concerning<br>stage 2.<br>In case of public sector in Germany, the assessor<br>shall verify that the claimed**[TR-ESOR]**certified<br>product is in fact deployed for providing the<br>service (checked e.g. by comparing the digital<br>fingerprint of the relevant executables).|<br> <br> <br> <br> <br> <br>|||
||**_ETSI EN 319 401_**_[1],_||||||||
||_clause 7.13 shall apply._||||||||
||||||||||



65 

Federal Office for Information Security 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

## **7.14 Cryptographic monitoring** 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-7.14-01_|_For every supported_|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>Note: See**OVR-6.5-**<br>**03, OVR-6.5-04,**<br>**OVR-6.5-07.**|The<br>assessor<br>shall<br>assess<br>the<br>(public)<br>documentation of the PSP (e.g. preservation<br>evidence<br>policy<br>or<br>a<br>public<br>document<br>referenced by it (e.g.**[ETSI TS 119 512]**or<br>**[TR-ESOR]**)) and verify that the PSP:<br>- described for each preservation profile, that the<br>PSP<br>monitors<br>the<br>strength<br>of<br>every<br>cryptographic algorithms that were used in the<br>connection with the preservation profile and<br>- described the case, when one of the used<br>algorithms or parameters is thought to become<br>less secure or the validity of a relevant<br>certificate is going to expire.<br>In this case, the PSP shall  update the related<br>preservation evidence policy  to handle newly<br>submitted PO<br>**or**<br>- stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing<br>the service and this requirement by this PSP.|<br> <br> <br> <br> <br> <br>|If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>-  implemented a monitoring to the strength of<br>every cryptographic algorithms that have been<br>used in connection with each preservation profile<br>and<br>- implemented, that the related preservation<br>evidence policy will be updated, when the used<br>algorithms or parameters are thought to become<br>less secure or the validity of relevant certificate is<br>going to expire.<br>The assessor shall compare the monitoring with<br>the description in the preservation evidence policy<br>of the PSP for each preservation evidence policy<br>referenced byapreservationprofile.|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|||
||_active_<br>_preservation_||||||||
||_profile, the TSP shall_||||||||
||_monitor the strength of_||||||||
||_every_<br>_cryptographic_||||||||
||_algorithm that was used_||||||||
||_in connection with this_||||||||
||_profile. In case, one of_||||||||
||_the used algorithms or_||||||||
||_parameters is thought to_||||||||
||_become less secure or_||||||||
||_the validity of a relevant_||||||||
||_certificate is going to_||||||||
||_expire, it shall either_||||||||
||_update_<br>_the_<br>_related_||||||||
||_preservation_<br>_evidence_||||||||
||_policy or create a new_||||||||
||_preservation profile to_||||||||
||_handle newly submitted_||||||||
||_POs._||||||||
||||||||||



66 

Federal Office for Information Security 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-7.14-02_|_[WST]_|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>See**[ETSI TS 119**<br>**511]**,**OVR-6.5-07**.|Only applicable in case of [WST]:<br>The<br>assessor<br>shall<br>assess<br>the<br>(public)<br>documentation of the PSP (e.g. preservation<br>evidence<br>policy<br>or<br>a<br>public<br>document<br>referenced by it (e.g.**[ETSI TS 119 512]**or<br>**[TR-ESOR]**)) and verify that the PSP:<br>- described the augmentation of the preservation<br>evidence, when one of the algorithms or<br>parameters, which were used in a preservation<br>evidence, is thought to become less secure or the<br>validity of a relevant certificate is going to<br>expire<br>**or**<br>- stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing<br>the service and this requirement by this PSP.<br>In this case, the PSP shall point out, that the<br>preservation evidence is going to be augmented<br>by the preservation service according to a new<br>preservation<br>evidence<br>policy<br>during<br>the<br>preservation period.|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|Only applicable in case of [WST]:<br>If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>-<br>implemented<br>an<br>augmentation<br>by<br>the<br>preservation<br>service<br>according<br>to<br>a<br>new<br>preservation<br>evidence<br>policy<br>during<br>the<br>preservation period, if one of the used algorithms<br>or parameters is thought to become less secure or<br>the validity of a relevant certificate is going to<br>expire and<br>- shows at least one augmented preservation<br>evidence according to each preservation evidence<br>policy related to the preservation profile.<br>The assessor shall compare the augmentation<br>process and the augmented preservation evidence<br>with the requirements and description in the<br>preservation evidencepolicyof the PSP.|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|||
||_[CONDITIONAL]_<br>_If_||||||||
||_one of the algorithms or_||||||||
||_parameters which were_||||||||
||_used in a preservation_||||||||
||_evidence, is thought to_||||||||
||_become less secure or_||||||||
||_the validity of a relevant_||||||||
||_certificate is going to_||||||||
||_expire, the preservation_||||||||
||_evidence_<br>_shall_<br>_be_||||||||
||_augmented_<br>_by_<br>_the_||||||||
||_preservation_<br>_service_||||||||
||_according to a new_||||||||
||_version_<br>_of_<br>_the_||||||||
||_preservation_<br>_evidence_||||||||
||_policy_<br>_during_<br>_the_||||||||
||_preservation period._||||||||
||||||||||
||||||||||



67 

Federal Office for Information Security 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-7.14-03_|_For the evaluation of the_|<br> <br> <br>_NOTE_<br>_2:_<br>_Cryptographic suites_<br>_recommendations_<br>_defined in_**_ETSI TS_**<br>**_119 312_**_[i.5] can be_<br>_superseded_<br>_by_<br>_national_<br>_recommendations._<br>See<br>**[ETSI TS 119**<br>**511]**,**OVR-6.5-04**.|<br> <br> <br> <br> <br>The<br>assessor<br>shall<br>assess<br>the<br>(public)<br>documentation (e.g. preservation evidence<br>policy or a public document referenced by it<br>(e.g.**[ETSI TS 119 512]**or**[TR-ESOR]**)) and<br>verify that the PSP:<br>- described that the monitoring and the<br>augmentation consider algorithms according to<br>**[ETSI TS 119 312]**<br>or<br>national<br>recommendations<br>**or**<br>- stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing<br>the service and this requirement by this PSP.<br>The assessor shall verify the description in the<br>preservation<br>evidence<br>policy<br>of<br>the<br>cryptographic algorithms for each preservation<br>evidence policy, see also**[ASS 119 511]**,**OVR-**<br>**7.14-01**&**OVR-7.14-02**.|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- implemented the monitoring and augmentation<br>on base of algorithms according to**[ETS TS 119**<br>**312]**or national recommendations.<br>The assessor shall cause the PSP to show at least<br>one example of an augmented preservation<br>evidence for each preservation evidence policy for<br>each profile.<br>See also**[ASS 119 511]**,**OVR-7.14-01**&**OVR-**<br>**7.14-02**.|<br> <br> <br> <br> <br> <br> <br> <br> <br>|||
||_cryptographic_||||||||
||_algorithms_<br>_in_<br>**_OVR-_**||||||||
||**_7.14.01_**<br>_and_<br>**_OVR-_**||||||||
||**_7.14.02_**_,_**_ETSI TS 119_**||||||||
||**_312_**_[i.5] should be_||||||||
||_considered._||||||||
||||||||||



68 

Federal Office for Information Security 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

## **7.15 Augmentation of preservation evidences** 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-7.15-01_|_[WST] During the_|<br>See<br>**[ETSI TS 119 511]**,<br>**OVR-6.5-07.**|Only applicable in case of [WST]:<br>the assessor shall assess the (public)<br>documentation of the PSP (e.g. the<br>preservation evidence policy or a public<br>document referenced by it (e.g.**[ETSI TS**<br>**119 512]**or**[TR-ESOR]**)) and verify that<br>the PSP:<br>- described how the PSP makes sure that<br>the preservation evidence can be used to<br>achieve the corresponding preservation<br>goal during the preservation period, like<br>•<br>the use of a certified**[TR-**<br>**ESOR]**conform product of<br>version V1.2.1 or higher or<br>•<br>the use of another accepted<br>augmentation method with a<br>detailed description in the<br>preservation evidence policy<br>and an offering of an<br>appropriate test system)<br>or<br>- stated which**[TR-ESOR]**certified<br>product is used for providing the service<br>and this requirement bythis PSP.|<br> <br> <br> <br> <br> <br> <br>|Only applicable in case of [WST]:<br>If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables,<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- makes sure during the preservation period that<br>the preservation evidence can be used to achieve<br>the corresponding goal, like the use of a certified<br>**[TR-ESOR]**conform product<br>or<br>- had implemented the usage of another accepted<br>augmentation method with a detailed description<br>in the preservation evidence policy and<br>- is able to offer an appropriate test system to the<br>assessor.|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|||
||_preservation period, the_||||||||
||_preservation service shall_||||||||
||_make sure that the_||||||||
||_preservation evidence can_||||||||
||_be used to achieve the_||||||||
||_corresponding preservation_||||||||
||_goal._||||||||
||||||||||



69 

Federal Office for Information Security 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-7.15-02_|_[WTS] During the_|<br>_NOTE 1: This can be_<br>_jeopardized in case a_<br>_cryptographic_<br>_algorithm cannot be_<br>_trusted anymore or_<br>_revocation information_<br>_cannot be received_<br>_anymore._|Only applicable in case of [WTS]:<br>the assessor shall assess the (public)<br>documentation of the PSP (e.g. the<br>preservation evidence policy or a public<br>document referenced by it (e.g.**[ETSI TS**<br>**119 512]**or**[TR-ESOR]**)) and verify that<br>the PSP:<br>- described how the PSP  ensures that the<br>preservation evidence can be used to<br>achieve the corresponding preservation<br>goal during the preservation evidence<br>retention period, like<br>•<br>the use of a certified**[TR-**<br>**ESOR]**conform product of<br>version V1.2.1 or higher or<br>•<br>the use of another accepted<br>augmentation method with a<br>detailed description in the<br>[PSPS] and an offer of an<br>appropriate test system to the<br>assessor.|<br> <br> <br> <br> <br> <br> <br> <br>|Only applicable in case of [WTS]:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- ensures during the preservation evidence<br>retention period that the preservation evidence can<br>be used to achieve the corresponding goal, by<br>•<br>using a certified**[TR-ESOR]**conform<br>product or<br>•<br>using another accepted augmentation<br>method with a detailed description in<br>the preservation evidence policy and an<br>offer of an appropriate  test system to<br>the assessor.|<br> <br>|||
||_preservation evidence_||||||||
||_retention period, the_||||||||
||_preservation service shall_||||||||
||_make sure that the_||||||||
||_preservation evidence can_||||||||
||_be used to achieve the_||||||||
||_corresponding preservation_||||||||
||_goal._||||||||
||||||||||



Federal Office for Information Security 

70 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-7.15-03_|_[WST] [WTS] The_|_NOTE 2: In case of a_<br>_digital signature,_<br>_augmentation can be_<br>_done by incorporating_<br>_to a digital signature_<br>_information to maintain_<br>_the validity of that_<br>_signature as there are_<br>_e.g. time stamps,_<br>_validation data..._<br>_NOTE 3: In case of an_<br>_evidence record,_<br>_augmentation can be_<br>_done by time stamp_<br>_renewal or hash tree_<br>_renewal according to_<br>**_IETF RFC 4998_**_[i.20]_<br>_or_**_IETF RFC 6283_**<br>_[i.23]._<br>See**[ASS 119 511]**,<br>**OVR-6.5-07**,**OVR-**<br>**7.15-01**, **OVR-7.15-02**.|Only applicable in case of [WTS], [WST]:<br>the assessor shall assess the (public)<br>documentation of the PSP (e.g. each<br>preservation evidence policy or a public<br>document referenced by it (e.g.**[ETSI TS**<br>**119 512]**or**[TR-ESOR]**)) and verify that<br>the PSP:<br>- stated out in its preservation  evidence<br>policy how the preservation evidence is<br>augmented<br>or<br>- stated which**[TR-ESOR]**certified<br>product of version V1.2.1 or higher is<br>used for providing the service and this<br>requirement by this PSP.|<br> <br> <br> <br> <br>|Only applicable in case of [WTS], [WST]:<br>If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows, how evidence is augmented for each<br>preservation evidence policy in practice (see also<br>**OVR-7.15-01**and**OVR-7.15-02**),<br>-shows augmented preservation evidences for<br>each preservation evidence policy referenced by a<br>preservation profile,<br>- shows that it is possible to start an augmentation<br>process, if required.<br>The assessor shall compare the process and result<br>of the augmentation of the preservation evidence<br>for each preservation evidence policy with the<br>description in thepreservation evidencepolicy.|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|||
||_preservation service shall_||||||||
||_augment the preservation_||||||||
||_evidences before they_||||||||
||_cannot be used anymore to_||||||||
||_achieve the corresponding_||||||||
||_preservation goal, to make_||||||||
||_sure that_**_OVR-7.15-01_**_or_||||||||
||**_OVR-7.15-02_**_is fulfilled._||||||||
||||||||||



## **7.16 Export-Import package** 

Federal Office for Information Security 

71 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-7.16-01_|_[WST] The PSP shall allow_|<br>_NOTE 1: The export-_<br>_import package can be_<br>_used to move the_<br>_preserved data from one_<br>_preservation service to_<br>_another preservation_<br>_service._<br>_NOTE 2: The present_<br>_document does not give_<br>_any information on the_<br>_exact format of the_<br>_export-import package._<br>_See_**_ETSI TS 119 512_**<br>_[i.13] for a possible_<br>_structure._|<br>Only applicable in case of [WST]:<br>The assessor shall assess the (public)<br>documentation of the PSP and verify that<br>the PSP:<br>- described how the clients can request an<br>export-import package containing the<br>preserved data, the evidences and all<br>information needed to validate the<br>evidences and<br>- described the structure of the format of<br>an<br>import-export<br>package<br>(e.g.<br>**[ETSI TS 119 512]**)<br>**or**<br>- stated which**[TR-ESOR]**certified<br>product of version V1.2.1 or higher is<br>used for providing the service and this<br>requirement bythis PSP.|<br> <br> <br> <br> <br> <br> <br>|Only applicable in case of [WST]:<br>If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- implemented how the clients can request an<br>import-export package,<br>- implemented production methods for export-<br>import package(s), containing the preserved data,<br>the evidences and all information needed to<br>validate the evidences, working as documented.|<br> <br> <br> <br> <br> <br> <br>|||
||_the preservation client or_||||||||
||_another authorized_||||||||
||_preservation service to_||||||||
||_request the export-import_||||||||
||_package(s), containing the_||||||||
||_preserved data, the_||||||||
||_evidences and all_||||||||
||_information needed to_||||||||
||_validate the evidences._||||||||
||||||||||



Federal Office for Information Security 

72 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-7.16-02_|_[WST] The PSP should use_|_EXAMPLE 1:_<br>_The export-import_<br>_package(s) as described_<br>_in_**_ETSI TS 119 512_**<br>_[i.13]._<br>_EXAMPLE 2:_<br>_The export-import_<br>_package(s) according to_<br>**_TR-ESOR-M3_**_[i.27],_<br>_clause 2.5_|<br> <br>Only applicable in case of [WST]:<br>See**[ASS 119 511]**,**OVR-7.16-01**.<br>The assessor shall assess the (public)<br>documentation of PSP and verify that the<br>PSP:<br>- described the standardised format for the<br>export-import package(s), used,<br>- and described the structure of the format<br>of<br>an<br>import-export<br>package<br>(e.g.<br>**[ETSI TS 119 512]**), if applicable<br>**or**<br>- stated which**[TR-ESOR]**certified<br>product of version V1.2.1 or higher is<br>used for providing the service and this<br>requirement by this PSP.|<br> <br> <br> <br>|Only applicable in case of [WST]:<br>If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site,<br>cause the PSP to show at least one example of an<br>export-import package for each preservation<br>evidence policy<br>and verify that the PSP:<br>- implemented a standardised format for the<br>export-import package(s) as stated in the<br>documentation of PSP.<br>•<br>In both cases, the assessor shall test the<br>interoperability of the produced<br>preservation evidences, in case of**[TR-**<br>**ESOR]**by using the open source tool<br>ERVerifyTool, accessible at<br>https://github.com/ervta/ERVerifyTool.|<br> <br> <br> <br> <br> <br> <br>|||
||_standardised format for the_||||||||
||_export-import package(s)._||||||||
||||||||||



Federal Office for Information Security 

73 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-7.16-03_|_[WST] The export-import_|See also<br>**PRP-8.1-01.**|Only applicable in case of [WST]:<br>The assessor shall assess the (public)<br>documentation of the PSP and verify that<br>the PSP:<br>- described to which authorized legal or<br>natural person or preservation client.<br>Export-import<br>package(s)<br>may<br>be<br>delivered<br>**or**<br>- stated which**[TR-ESOR]**certified<br>product of version V1.2.1 or higher is<br>used for providing the service and this<br>requirement by this PSP.|<br> <br> <br> <br>|Only applicable in case of [WST]:<br>If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows that the delivery of the preservation<br>package(s) only takes place in case of a successful<br>authorization of the legal or natural person or<br>preservation client.<br>The assessor shall cause the PSP to show at<br>least one example of an_export-import package_<br>for each preservation evidence policy in<br>connection with an authorized person and<br>with an unauthorized person.|<br> <br> <br> <br> <br> <br> <br>|||
||_package shall only be_||||||||
||_delivered to an authorized_||||||||
||_legal or natural person or_||||||||
||_preservation client._||||||||
||||||||||



Federal Office for Information Security 

74 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-7.16-04_|_[WST] The PSP shall keep_||Only applicable in case of [WST]:<br>The assessor shall assess the (public)<br>documentation of the  PSP and verify that<br>the PSP:<br>- described how the PSP keeps records of<br>all<br>released<br>export-import<br>packages<br>including a date and a criteria that has<br>been used to select the set of preservation<br>objects to be included in the export-import<br>package<br>**or**<br>- stated which**[TR-ESOR]**certified<br>product of version V1.2.1 or higher is<br>used for providing the service and this<br>requirement bythis PSP.|<br> <br> <br> <br> <br> <br> <br> <br> <br>|Only applicable in case of [WST]:<br>If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows how the kept records of all released<br>export-import packages are implemented. They<br>shall include the date of the event and the criteria<br>that has been used to select the set of preservation<br>objects to be included in the export-import<br>package.|<br> <br> <br> <br> <br> <br> <br> <br> <br>|||
||_records of all released_||||||||
||_export-import packages_||||||||
||_including:_||||||||
||||||||||
|_OVR-7.16-04 1)_|_the date of the event_||See**[ASS 119 511]**, **OVR-7.16-04.**||See**[ASS 119 511]**, **OVR-7.16-04**.||||
|_OVR-7.16-04 2)_|_the criteria that has been_||See**[ASS 119 511]**,**OVR-7.16-04**.||See**[ASS 119 511]**,**OVR-7.16-04**.||||
||_used to select the set of_||||||||
||_preservation objects to be_||||||||
||_included in the export-_||||||||
||_importpackage _||||||||



75 

Federal Office for Information Security 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

## **8 Operational and notification protocols** 

## **8.1 Preservation protocol** 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
||||||||||
|_PRP-8.1-01_|_The communication channel_||The<br>assessor<br>shall<br>assess<br>the<br>(public)<br>documentation of the PSP and verify that the PSP:<br>- described how the communication channel<br>between the preservation client and the PSP is<br>secured including a description how the<br>confidentiality of the data is ensured (i.e. the PSP<br>shall offer a way to be authenticated by the<br>client)<br>**or**<br>- stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing the<br>service and this requirement by this PSP.|<br> <br> <br>|If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- implemented a secure communication channel<br>between the preservation client and itself<br>including a method to ensures the confidentiality<br>of the data.<br>The assessor shall cause the PSP to show at least<br>one example of each communication process<br>between the preservation client and the<br>preservation service.<br>The assessor shall compare the implementation<br>of the communication channel with the<br>description in the documentation of the PSP.|<br> <br> <br> <br>|||
||_between the preservation_||||||||
||_client and the PSP shall be_||||||||
||_secured, i.e. the PSP shall_||||||||
||_offer a way to be_||||||||
||_authenticated by the client_||||||||
||_and the confidentiality of the_||||||||
||_data shall be ensured._||||||||
||||||||||



76 

Federal Office for Information Security 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
||||||||||
|_PRP-8.1-02_|_The preservation protocol as_||The<br>assessor<br>shall<br>assess<br>the<br>(public)<br>documentation of the PSP and verify that the PSP:<br>- described which preservation protocol has been<br>used.<br>- fulfils the requirement exactly as it is specified<br>or<br>- explained why its provided service uses another<br>approach and why the results equally fulfil the<br>requirements and the required resulting security<br>level<br>**or**<br>- stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing the<br>service and this requirement by this PSP.|<br> <br> <br> <br> <br> <br> <br> <br>|If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>-<br>shows<br>which<br>preservation<br>protocol<br>is<br>implemented<br>- fulfils the requirement exactly as it is specified<br>or<br>- can demonstrate with respective test cases the<br>specified behaviour<br>- explains why its provided service uses another<br>approach and why the results fulfil the<br>requirements and the resulting security level<br>required.|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|||
||_defined in_**_ETSI TS 119 512_**||||||||
||_[i.13] should be used._||||||||
||||||||||



Federal Office for Information Security 

77 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
||||||||||
|_PRP-8.1-03_|_The protocols shall be_||The<br>assessor<br>shall<br>assess<br>the<br>(public)<br>documentation of the PSP and verify that the PSP:<br>- described how the preservation protocol is<br>protected against unauthorized usage<br>or<br>- stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing the<br>service and this requirement by this PSP.|<br> <br>|If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows how the preservation protocol is protected<br>against unauthorized usage.<br>The assessor shall cause the PSP to show at least<br>one example of each preservation protocol,<br>which is used.<br>The assessor shall compare the implementation<br>of the communication channel with the<br>description in the documentation of the PSP.|<br> <br> <br> <br> <br>|||
||_protected against_||||||||
||_unauthorised usage._||||||||
||||||||||



Federal Office for Information Security 

78 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
||||||||||
|_PRP-8.1-04_|_A preservation service shall_|_EXAMPLE 1_<br>_1:RetrieveInfo_<br>_as defined in_<br>**_ETSI TS 119_**<br>**_512_**_[i.13] to_<br>_retrieve_<br>_information on_<br>_preservation_<br>_profiles_|<br> <br>The<br>assessor<br>shall<br>assess<br>the<br>(public)<br>documentation of the PSP and verify that the PSP:<br>- described that the preservation service allows to<br>retrieve information about the currently and<br>previously supported preservation profiles.<br>The PSP may refer in the [PSPS] to a publicly<br>published document, which describes detailed<br>how the information can be retrieved from the<br>preservation service (e.g.**[ETSI TS 119 512]**or<br>**[TR-ESOR-E]**and**[TR-ESOR-E-Appendix]**)<br>or<br>- stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing the<br>service and this requirement by this PSP.|<br> <br> <br> <br>|If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows how the information about currently and<br>previously supported preservation profiles are<br>retrieved.<br>The assessor shall verify that the information can<br>be retrieved, e.g. by invoking the corresponding<br>RetrieveInfo call or by inspecting corresponding<br>logfiles,as documented.|<br> <br> <br> <br> <br> <br> <br> <br> <br>|||
||_allow to retrieve information_||||||||
||_about the currently and_||||||||
||_previously supported_||||||||
||_preservation profiles._||||||||
||||||||||



Federal Office for Information Security 

79 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
||||||||||
|_PRP-8.1-05_|_A preservation service shall_|_EXAMPLE 2:_<br>_The_<br>_preservation_<br>_object_<br>_identifier can_<br>_later be used_<br>_to retrieve_<br>_preservation_<br>_object(s)_<br>_(PO(s)) and/or_<br>_traces or to_<br>_delete PO(s)_<br>_or to update_<br>_preservation_<br>_object_<br>_containers_<br>_(asynchronous_<br>_mode)_<br>_EXAMPLE 3:_<br>_PreservePO as_<br>_defined in_<br>**_ETSI TS 119_**<br>**_512_** _[i.12]._|<br> <br> <br>The<br>assessor<br>shall<br>assess<br>the<br>(public)<br>documentation of the  PSP and verify that the<br>PSP:<br>- described that the preservation service allows<br>one or more submission data objects (SubDO) to<br>be preserved under a specific preservation profile<br>and to receive back either a preservation object<br>identifier or to retrieve back immediately a<br>preservation evidence (synchronous mode).<br>The PSP may refer in the documentation of the<br>PSP to a publicly published document, which<br>describes detailed how the data objects can be<br>preserved and received back from the<br>preservation service (e.g. see**[ETSI TS 119 512]**<br>or**[TR-ESOR-E]**and**[TR-ESOR-E-Appendix**])<br>or<br>- stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing the<br>service and this requirement by this PSP.|<br> <br> <br> <br> <br> <br> <br> <br> <br>|If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows how the preservation service allows the<br>submission data objects (SubDO) to be preserved<br>for each preservation profile and<br>- shows how the preservation object identifier can<br>be received back or how a preservation evidence<br>can be retrieved back immediately (synchronous<br>mode).<br>The assessor shall verify that the submission of<br>data objects is possible, e.g. by invoking the<br>corresponding PreservePO call or by inspecting<br>corresponding log files as documented.<br>The assessor shall cause the PSP to show the<br>description how the data objects can be preserved<br>and retrieved back.|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|||
||_allow one or more_||||||||
||_submission data objects_||||||||
||_(SubDO) to be preserved_||||||||
||_under a specific preservation_||||||||
||_profile, and to receive back_||||||||
||_either a preservation object_||||||||
||_identifier or to receive back_||||||||
||_immediately a preservation_||||||||
||_evidence (synchronous_||||||||
||_mode)._||||||||
||||||||||



Federal Office for Information Security 

80 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
||||||||||
|_PRP-8.1-06_|_A preservation service may_|_EXAMPLE 4:_<br>_RetrieveTrace_<br>_as defined in_<br>**_ETSI TS 119_**<br>**_512_**_[i.13]._|If applicable,<br>the<br>assessor<br>shall<br>assess<br>the<br>(public)<br>documentation of the   PSP and verify that the<br>PSP:<br>- described how the preservation service allows to<br>get traces of all the operations related to a specific<br>preservation object identifier, if applicable.<br>The PSP may refer in the documentation of the<br>PSP to a publicly published document, which<br>describes detailed how the traces can be get from<br>the preservation service (e.g. see<br>**[ETSI TS 119 512]**)<br>or<br>- stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing the<br>service and this requirement by this PSP.|<br> <br> <br> <br> <br>|If applicable,<br>if the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows how the preservation service allows to get<br>traces.<br>If applicable, the assessor shall verify that the<br>retrieval of traces is possible, e.g. by invoking the<br>corresponding RetrieveTrace call or by inspecting<br>corresponding log files, as documented.<br>The assessor shall cause the PSP to show the<br>description how toget traces.|<br> <br> <br> <br> <br> <br> <br> <br>|||
||_allow to get the traces of all_||||||||
||_operations related to a_||||||||
||_specific preservation object_||||||||
||_identifier._||||||||
||||||||||



Federal Office for Information Security 

81 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
||||||||||
|_PRP-8.1-07_|_A preservation service may_|_EXAMPLE 5:_<br>_Search as_<br>_defined in_<br>**_ETSI TS 119_**<br>**_512_**_[i.13]._|If applicable,<br>the<br>assessor<br>shall<br>assess<br>the<br>(public)<br>documentation of the  PSP and verify that the<br>PSP:<br>- described how the preservation service allows to<br>search for specific preservation objects and<br>retrieve a set of preservation object identifiers,<br>which can be used in other operations, if<br>applicable.<br>The PSP may refer in the documentation of the<br>PSP to a publicly published document, which<br>describes detailed how the preservation service<br>allows to search and to retrieve (e.g. see**[ETSI TS**<br>**119 512].**|<br> <br> <br> <br> <br> <br> <br> <br> <br>|If applicable,<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows how the preservation service allows to<br>search for specific preservation objects and to<br>retrieve a set of preservation object identifiers.<br>The assessor shall verify that searching for<br>specific preservation objects and retrieving a set<br>of preservation object identifiers is possible, e.g.<br>by invoking the corresponding search call or by<br>inspecting<br>corresponding<br>log<br>files,<br>as<br>documented.<br>The assessor shall cause the PSP to show the<br>description how to search for and retrieve<br>preservation object identifiers.|<br> <br> <br> <br> <br> <br> <br>|||
||_allow to search for specific_||||||||
||_preservation objects and_||||||||
||_retrieve a set of preservation_||||||||
||_object identifiers, which can_||||||||
||_be used in other operations,_||||||||
||_like for example_**_PRP-8.1-05_**_._||||||||
||||||||||



Federal Office for Information Security 

82 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
||||||||||
|_PRP-8.1-08_|_A preservation service may_|<br> <br>_EXAMPLE 6:_<br>_ValidateEvide_<br>_nce as defined_<br>_in_**_ETSI TS_**<br>**_119 512_**_[i.12]._|If applicable,<br>the<br>assessor<br>shall<br>assess<br>the<br>(public)<br>documentation of the  PSP and verify that the<br>PSP:<br>- described how the preservation service allows to<br>submit to the preservation service a preservation<br>evidence and a sequence of POs to which the<br>evidence corresponds, in order to validate the<br>evidence and to retrieve back preservation<br>evidence validation report.<br>The PSP may refer in the documentation of the<br>PSP to a publicly published document, which<br>describes detailed how the preservation service<br>allows submitting evidences and POs (e.g. see<br>**[ETSI TS 119 512], [TR-ESOR-E]**and**[TR-**<br>**ESOR-E-Appendix]**)<br>or<br>- stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing the<br>service and this requirement by this PSP.|<br> <br> <br> <br> <br> <br> <br>|If applicable,<br>If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows how the preservation service allows<br>submitting preservation evidences and sequences<br>of POs in order to validate the evidence and to<br>receive back a preservation evidence validation<br>report.<br>The assessor shall verify that the preservation<br>service can validate whether the submitted<br>preservation<br>evidence<br>corresponds<br>to<br>the<br>submitted sequence of POs and can return a<br>preservation evidence validation report.<br>The assessor shall cause the PSP to show for each<br>preservation evidence policy at least one example<br>including an event log with the results for the<br>validatingof apreservation evidence.|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|||
||_allow to submit to the_||||||||
||_preservation service a_||||||||
||_preservation evidence and a_||||||||
||_sequence of POs to which the_||||||||
||_evidence corresponds, in_||||||||
||_order to validate the evidence_||||||||
||_and to receive back a_||||||||
||_preservation evidence_||||||||
||_validation report._||||||||
||||||||||



Federal Office for Information Security 

83 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
||||||||||
|_PRP-8.1-09_|_[CONDITIONAL]: If the_||If applicable,<br>the<br>assessor<br>shall<br>assess<br>the<br>(public)<br>documentation of the  PSP and verify that the<br>PSP:<br>- described how the search functionality for<br>specific preservation objects include a filter<br>functionality to which the preservation object<br>(identifiers) shall correspond,<br>or<br>- stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing the<br>service and this requirement by this PSP.|<br> <br>|If applicable and<br>if the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- implemented a search functionality for specific<br>preservation<br>objects<br>including<br>a<br>filter<br>functionality to which the preservation object<br>(identifiers) shall correspond as described in<br>preservation profile.<br>The assessor shall cause the PSP to show for<br>each preservation evidence policy at least one<br>example of a successful invocation of the Search<br>call or a corresponding event log with the results<br>for searchingsuchpreservation objects.|<br> <br> <br> <br> <br> <br> <br> <br>|||
||_preservation service allows_||||||||
||_to search for specific_||||||||
||_preservation objects, it may_||||||||
||_include a filter functionality_||||||||
||_to which the preservation_||||||||
||_object (identifiers) shall_||||||||
||_correspond._||||||||
||||||||||



Federal Office for Information Security 

84 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
||||||||||
|_PRP-8.1-10_|_[WST] A preservation service_|<br>_NOTE 1: POs_<br>_can also_<br>_contain_<br>_evidences_<br>_EXAMPLE 7:_<br>_RetrievePO as_<br>_defined in_<br>**_ETSI TS 119_**<br>**_512_**_[i.12]._|<br>Only applicable in case of [WST]:<br>The<br>assessor<br>shall<br>assess<br>the<br>(public)<br>documentation of the  PSP and verify that the<br>PSP:<br>- described how the preservation service allows to<br>retrieves evidences and/or preservation objects<br>(POs).<br>The PSP may refer in the documentation of the<br>PSP to a publicly published document, which<br>describes detailed how the preservation service<br>allows to retrieve evidences and/or POs from<br>preservation services with storage (e.g. see**[ETSI**<br>**TS 119 512], [TR-ESOR-E]**and**[TR-ESOR-E-**<br>**Appendix]**).<br>or<br>- stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing the<br>service and this requirement bythis PSP|<br> <br> <br> <br> <br> <br> <br> <br> <br>|Only applicable in case of [WST]:<br>If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows that the preservation service has<br>implemented a retrieval functionality to retrieve<br>evidences and/or preservation objects (POs).<br>The assessor shall cause the PSP to show at least<br>one example including an event log with the<br>results for retrieving one preservation evidence<br>and/or one PO for each preservation evidence<br>policy, as documented.|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|||
||_with storage shall allow to_||||||||
||_retrieve evidences and/or_||||||||
||_preservation objects (POs)._||||||||
||||||||||



85 

Federal Office for Information Security 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
||||||||||
|_PRP-8.1-11_|_[WST] A preservation service_|<br> <br> <br>|Only applicable in case of [WST]:<br>The<br>assessor<br>shall<br>assess<br>the<br>(public)<br>documentation of the  PSP and verify that the<br>PSP:<br>- described how the preservation service allows to<br>delete stored POs,<br>- described the case of deletion of the preservation<br>evidence, then the corresponding SubDO has to be<br>deleted as well and<br>- described the case of deletion before expiry of<br>the preservation period.<br>The PSP may refer in the documentation of the<br>PSP to a publicly published document, which<br>describes detailed how the preservation service<br>allows to delete evidences and/or POs for<br>preservation services with storage (e.g. see**[ETSI**<br>**TS 119 512], [TR-ESOR-E]**and**[TR-ESOR-E-**<br>**Appendix]**)<br>or<br>- stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing the<br>service and this requirement by this PSP.|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|Only applicable in case of [WST]:<br>If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- also shows the case that the corresponding<br>SubDO is deleted, when a preservation evidence<br>is deleted.<br>The assessor shall cause the PSP to show at least<br>one example including an event log with the<br>results for deleting a stored PO including the<br>deletion of the corresponding subDO.<br>The assessor shall verify different cases:<br>•<br>deletion within preservation period –<br>deletion is only possible with provided<br>reason as justification,<br>•<br>deletion after the preservation period has<br>expired – deletion is possible with and<br>without reason asjustification.|<br> <br> <br> <br> <br> <br> <br> <br> <br>|||
||_with storage shall allow to_||||||||
||_delete stored POs. In case the_||||||||
||_deletion of the preservation_||||||||
||_evidence the corresponding_||||||||
||_SubDO shall be deleted as_||||||||
||_well. The preservation_||||||||
||_service shall assure that_||||||||
||_stored POs can only be_||||||||
||_deleted before expiry of the_||||||||
||_preservation period when the_||||||||
||_delete request will be_||||||||
||_submitted together with a_||||||||
||_justification. The_||||||||
||_preservation service shall log_||||||||
||_any DeletePO requests and_||||||||
||_the accompanying_||||||||
||_justifications._||||||||
||||||||||



86 

Federal Office for Information Security 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
||||||||||
|_PRP-8.1-12_|_[WST] The preservation_|<br> <br>_EXAMPLE 8:_<br>_DeletePO as_<br>_defined in_<br>**_ETSI TS 119_**<br>**_512_**_[i.12]._|Only applicable in case of [WST]:<br>The<br>assessor<br>shall<br>assess<br>the<br>(public)<br>documentation of the PSP and verify that the PSP:<br>- described, that it is assured that stored POs can<br>only be deleted before the end of the preservation<br>period when the delete request will be submitted<br>together with a justification, and<br>- described, that it is assured that any submitted<br>justification will be logged together with the<br>information of the deletion request.<br>The PSP may refer in the documentation of the<br>PSP to a publicly published document, which<br>describes detailed how the preservation service<br>allows to delete evidences and/or POs before the<br>end of the preservation period (e.g. see**[ETSI TS**<br>**119 512], [TR-ESOR-E]**and**[TR-ESOR-E-**<br>**Appendix]**)<br>or<br>- stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing the<br>service and this requirement by this PSP.|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|Only applicable in case of [WST]:<br>If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows the preservation service assures that the<br>stored POs can only be deleted before the end of<br>the preservation period when the delete request<br>will be submitted together with a justification and<br>- shows that any submitted justification will be<br>logged together with the information of the<br>deletion request.<br>The assessor shall cause the PSP to show at least<br>one example of a deletion request before the end<br>of the preservation period when the delete request<br>will be submitted together with a justification and<br>one example without a justification together with<br>the result in the event logs for each preservation<br>evidencepolicy,as documented.|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|||
||_service shall assure that_||||||||
||_stored POs can only be_||||||||
||_deleted before the end of the_||||||||
||_preservation period when the_||||||||
||_delete request will be_||||||||
||_submitted together with a_||||||||
||_justification. Any submitted_||||||||
||_justification shall be logged_||||||||
||_together with the information_||||||||
||_of the deletion request._||||||||
||||||||||



Federal Office for Information Security 

87 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
||||||||||
|_PRP-8.1-13_|_[WST] A preservation service_|<br>_EXAMPLE 9:_<br>_Search as_<br>_defined in_<br>**_ETSI TS 119_**<br>**_512_**_[i.12]_|Only applicable in case of [WST]:<br>The<br>assessor<br>shall<br>assess<br>the<br>(public)<br>documentation of the PSP and verify that the PSP:<br>- described, how the preservation service allows<br>to request a set of preservation object identifiers,<br>and<br>- described, if the set of preservation object<br>identifiers<br>included<br>a<br>filter<br>(see<br>also<br>**[ETSI TS 119 511], PRP-8.1-07**) to which the<br>preservation<br>object<br>identifier<br>has<br>to<br>be<br>correspond.<br>The PSP may refer in the documentation of the<br>PSP to a publicly published document, which<br>describes detailed how the preservation service<br>allows requesting a set of preservation object<br>identifiers for preservation services with storage<br>(e.g.**[ETSI TS 119 512]**).|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|Only applicable in case of [WST]:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- shows how the preservation service allows to<br>request a set of preservation object identifiers, if<br>applicable, and<br>- shows the filter to which the preservation object<br>identifiers has to be correspond.<br>The assessor shall cause the PSP to show at least<br>one example of the set of preservation object<br>identifiers including with the filter (see also<br>**[ETSI TS 119 511], PRP-8.1-07**) and with an<br>event log with the results, as documented.<br>The assessor shall cause the PSP to show the<br>description how to request a set of preservation<br>object identifiers.|<br> <br> <br> <br> <br> <br> <br> <br> <br>|||
||_with storage should allow to_||||||||
||_request a set of preservation_||||||||
||_object identifiers, which can_||||||||
||_be used to retrieve or delete_||||||||
||_POs as in_**_PRP-8.1-05_**_and_||||||||
||**_PRP-8.1-06_**_._||||||||
||||||||||



Federal Office for Information Security 

88 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
||||||||||
|_PRP-8.1-14_|_[WST] A preservation service_|<br>_EXAMPLE_<br>_10:_<br>_UpdatePOC_<br>_as defined in_<br>**_ETSI TS 119_**<br>**_512_**_[i.12]._<br>_NOTE 2: An_<br>_update_<br>_functionality_<br>_allows to_<br>_provide a new_<br>_version of a_<br>_SubDO. It can_<br>_completely or_<br>_partly replace_<br>_the original_<br>_version. All_<br>_versions are_<br>_kept, but one_<br>_is marked as_<br>_the latest one._|Only applicable in case of [WST]:<br>The<br>assessor<br>shall<br>assess<br>the<br>(public)<br>documentation of the PSP and verify that the PSP:<br>- described, how a new version of an already<br>submitted POC might be created for preservation<br>service with storage.<br>The PSP may refer in the documentation of the<br>PSP] to a publicly published document, which<br>describes<br>the<br>notation<br>of<br>versioning<br>for<br>preservation services with storage (e.g. see**[ETSI**<br>**TS 119 512], [TR-ESOR-E]**and**[TR-ESOR-E-**<br>**Appendix]**),<br>or<br>- stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing the<br>service and this requirement by this PSP.|<br> <br> <br> <br> <br> <br> <br> <br> <br>|Only applicable in case of [WST]:<br>If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- implemented the update functionality in order to<br>create a new version of an already submitted POC<br>for each preservation evidence policy, if<br>applicable.<br>The assessor shall verify that the PSP only accepts<br>for an already submitted POC one new version at<br>the same time.<br>The assessor shall cause the PSP to show at least<br>one example of the updated preservation object<br>with a new version and an event log with the<br>corresponding results for each preservation<br>evidencepolicy,as documented.|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|||
||_with storage may allow to_||||||||
||_provide a new version of an_||||||||
||_already submitted POC. The_||||||||
||_newly provided version may_||||||||
||_be specified only by the_||||||||
||_difference to the previous_||||||||
||_version._||||||||
||||||||||



Federal Office for Information Security 

89 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
||||||||||
|_PRP-8.1-15_|_[WTS] A preservation service_|<br>_NOTE 3:_<br>_Since the_<br>_evidences are_<br>_produced_<br>_asynchronousl_<br>_y and can be_<br>_used for a_<br>_number of_<br>_SubDOs, they_<br>_are available_<br>_during a time_<br>_period as_<br>_specified in_<br>_the_<br>_preservation_<br>_profile._<br>_EXAMPLE 11:_<br>_RetrievePO as_<br>_defined in_<br>**_ETSI TS 119_**<br>**_512_** _[i.12]._|<br> <br>Only applicable in case of [WTS]:<br>The<br>assessor<br>shall<br>assess<br>the<br>(public)<br>documentation of the PSP and verify that the PSP:<br>- described for preservation service with<br>temporary storage [WTS] that the retrieved<br>preservation<br>evidence<br>has<br>been<br>produced<br>asynchronously and<br>- described how the preservation service allows to<br>retrieve preservation evidences that have been<br>asynchronously produced by the preservation<br>service|<br> <br> <br> <br> <br> <br> <br>|Only applicable in case of [WTS]:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- implemented the preservation service with<br>temporary storage [WTS], which allows to<br>retrieve the preservation evidences, produced<br>asynchronously.<br>The assessor shall cause the PSP to show at least<br>one example of retrieved preservation evidence,<br>produced<br>asynchronously,<br>for<br>preservation<br>service with temporary storage by invoking the<br>retrieval function calls or inspecting log files.|<br> <br> <br> <br> <br> <br> <br>|||
||_with a temporary storage_||||||||
||_shall allow to retrieve_||||||||
||_preservation evidences that_||||||||
||_have been asynchronously_||||||||
||_produced by the preservation_||||||||
||_service._||||||||
||||||||||



Federal Office for Information Security 

90 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

## **8.2 Notification protocol** 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-8.2-01_|_The preservation service may_|<br>_NOTE 1: The_<br>_way, how this_<br>_notification is_<br>_done is out of_<br>_the scope of this_<br>_policy._|If applicable,<br>the assessor shall assess the document<br>Subscriber Agreement and verify that the PSP:<br>- described, if the preservation service supports<br>a notification protocol or not.|<br>|If applicable,<br>the assessor shall assess the PSP on-site and verify<br>that the PSP:<br>-  implemented a notification protocol or not.||||
||_define a notification protocol_||||||||
||_in order to be able to send_||||||||
||_messages or information to_||||||||
||_its subscribers._||||||||
||||||||||
|_OVR-8.2-02_|_[CONDITONAL] When the_|<br>|If applicable,<br>the assessor shall assess the document<br>Subscriber Agreement and verify that the PSP:<br>- described, in case a preservation evidence<br>policy is considered to become insecure, how<br>the preservation service notify its subscribers<br>about the security concerns that are specific for<br>that preservation evidence policy.|<br> <br> <br> <br>|If applicable,<br>the assessor shall assess the PSP on-site and verify<br>that the PSP:<br>- implemented the notification process to its<br>subscribers as described, for the case, when a<br>preservation evidence policy is considered to<br>become insecure.|<br> <br> <br>|||
||_preservation service provides_||||||||
||_a notification protocol, in_||||||||
||_case a preservation evidence_||||||||
||_policy referenced in an active_||||||||
||_preservation profile is_||||||||
||_considered to become_||||||||
||_insecure, the preservation_||||||||
||_service shall notify its_||||||||
||_subscribers, possibly using_||||||||
||_the corresponding profile,_||||||||
||_about the security concerns_||||||||
||_that are specific for that_||||||||
||_preservation evidencepolicy._||||||||



Federal Office for Information Security 

91 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-8.2-03_|_[CONDITONAL] When the_|<br> <br>|If applicable:<br>The assessor shall assess the document<br>Subscriber Agreement and verify that the PSP:<br>- described, that in case there are changes in<br>references elements that have an influence on<br>the specific profile, the PSP  notifies its<br>subscribers with a recommendation of the use<br>of, at least, one alternative or updated<br>preservation evidence policy.<br>See also **[ASS 119 511]**, **OVR-8.2-02**.|<br> <br> <br> <br> <br>|If applicable:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- implemented a notification process to its<br>subscribers with recommendation of the use of, at<br>least, one alternative or updated preservation<br>evidence policy, when there are changes in<br>references elements that have an influence on the<br>specific profile,.<br>See also **[ASS 119 511]**, **OVR-8.2-02**.|<br> <br> <br> <br> <br>|||
||_preservation service provides_||||||||
||_a notification protocol, in_||||||||
||_case there are changes in_||||||||
||_references elements that have_||||||||
||_an influence on the specific_||||||||
||_profile, the PSP shall notify_||||||||
||_its subscribers possibly using_||||||||
||_this profile._||||||||
||||||||||



Federal Office for Information Security 

92 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

## **9 Preservation process** 

## **9.1 Storage of preserved data and evidences** 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-9.1-01_|_[WOS] [WTS] A preservation_||Only applicable in case of [WOS], [WTS]:<br>The<br>assessor<br>shall<br>assess<br>the<br>(public)<br>documentation of the PSP and verify that the<br>PSP:<br>- described the time period for the storage of the<br>data to bepreserved.|<br> <br>|Only applicable in case of [WOS], [WTS]:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- implemented a time period for the storage of the<br>data to be preserved that is not longer than the time<br>period needed to create the evidence.|<br> <br>|||
||_service without storage or_||||||||
||_with temporary storage_||||||||
||_should not store the data to_||||||||
||_be preserved after the_||||||||
||_evidence has been created._||||||||
||||||||||
|_OVR-9.1-02_|_[WOS]_||Only applicable in case of [WOS], [WTS]:<br>The assessor shall assess the document [T&C]<br>and verify that the PSP:<br>- described the reasons why it stores the data to<br>be preserved after the evidence has be created.|<br>|Only applicable in case of [WOS], [WTS]:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- implemented the reasons for storing the data to<br>be preserved after the evidence has be created as<br>stated in the [T&C].|<br> <br>|||
||_[WTS][CONDITIONAL] A_||||||||
||_preservation service without_||||||||
||_storage or with temporary_||||||||
||_storage which stores the data_||||||||
||_to be preserved after the_||||||||
||_evidence has be created_||||||||
||_should state the reasons for_||||||||
||_doing so in its terms and_||||||||
||_conditions._||||||||



Federal Office for Information Security 

93 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-9.1-03_|_[WTS] A preservation service_||Only applicable in case of [WTS]:<br>See**[ASS 119 511]**,**OVR-9.1-01**applied to<br>preservation evidence instead of data stored.||Only applicable in case of [WTS]:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- implemented a time period for the storage of the<br>evidences that is not longer than the time allowed<br>to retrieve the evidence as stated in the<br>documentation of the SPS.<br>See also**[ASS 119 511]**, **OVR-9.1-01**.|<br> <br> <br>|||
||_with temporary storage shall_||||||||
||_not store the evidence for a_||||||||
||_time period longer than the_||||||||
||_time indicated in the_||||||||
||_preservation practice_||||||||
||_statement._||||||||
||||||||||



Federal Office for Information Security 

94 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

## **9.2 Preservation evidences** 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-9.2-01_|_[CONDITIONAL] If the_||If applicable,<br>the<br>assessor<br>shall<br>assess<br>the<br>(public)<br>documentation of the PSP and verify that the<br>PSP:<br>- described which time-stamp token is used and<br>that it is conform to [**IETF RFC 3161]**and<br>updated by [**IETF RFC 5816]**<br>_or_<br>- stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing<br>the service and this requirement by this PSP.|<br> <br> <br> <br>|If applicable and<br>If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- uses time-stamp tokens for the preservation<br>service, which are conform to**[IETF RFC 3161]**<br>and updated by**[IETF RFC 5816]**.<br>The assessor shall cause the PSP to show at least<br>one example of a time-stamp token for each<br>preservation evidencepolicy,as documented.|<br> <br> <br> <br> <br> <br> <br>|||
||_preservation service uses a_||||||||
||_time-stamp token it shall_||||||||
||_conform to_**_IETF RFC3161_**||||||||
||_[i.23] and updated by_**_RFC_**||||||||
||**_5816_**_[i.18]._||||||||
||||||||||
|_OVR-9.2-02_|_[CONDITIONAL] If the_||If applicable,<br>the<br>assessor<br>shall<br>assess<br>the<br>(public)<br>documentation of the  PSP and verify that the<br>PSP:<br>- described, that the time-stamping protocol and<br>time-stamp token profiles, used, conform to<br>**[ETSI EN 319 422]**.|<br> <br>|If applicable and<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- implemented the time-stamping protocol and<br>time-stamp token profiles as in**[ETSI EN 319**<br>**422]**.|<br> <br>|||
||_preservation service uses a_||||||||
||_time-stamp token it should_||||||||
||_conform to the time-stamping_||||||||
||_protocol and time-stamp_||||||||
||_token profiles as defined_||||||||
||**_ETSI EN 319 42_**_2 [i.11]._||||||||
||||||||||



95 

Federal Office for Information Security 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-9.2-03_|_[CONDITIONAL] If the_||If applicable,<br>the<br>assessor<br>shall<br>assess<br>the<br>(public)<br>documentation of the PSP and verify that the<br>PSP:<br>- described that the used evidence record is<br>conform to**[IETF RFC 4998]**or**[IETF RFC**<br>**6283]**<br>_or_<br>-stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing<br>the service and this requirement bythis PSP.|<br> <br> <br> <br> <br>|If applicable and<br>If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- implemented the evidence record conform to<br>**[IETF RFC 4998]**or**[IETF RFC 6283]**.|<br> <br> <br> <br> <br>|||
||_preservation service uses an_||||||||
||_evidence record it shall_||||||||
||_conform to_**_IETF RFC 4998_**||||||||
||_[i.25] or_**_IETF RFC 6283_**||||||||
||_[i.27]._||||||||
||||||||||
|_OVR-9.2-04_|_[CONDITIONAL] If the_|_NOTE: The_<br>_evidence policy_<br>_is referenced by_<br>_the preservation_<br>_profile. If the_<br>_preservation_<br>_profile is known_<br>_from the context,_<br>_the evidence_<br>_policy is known_<br>_as well._|<br>If applicable,<br>the<br>assessor<br>shall<br>assess<br>the<br>(public)<br>documentation of the PSP and verify that the<br>PSP:<br>- described what happened, if the preservation<br>evidence policy cannot be identified from the<br>context.|<br> <br> <br>|If applicable,<br>the assessor shall assess the PSP on-site and verify<br>that the PSP:<br>- implemented a process, if the preservation<br>evidence policy cannot be identified from the<br>context. In this case, the PSP should include the<br>preservation evidence policy directly in the<br>preservation evidence.<br>The assessor shall cause the PSP to show, at<br>least, one example of a preservation evidence<br>policyincluded directlyin thepreservation.|<br> <br> <br> <br>|||
||_preservation evidence policy_||||||||
||_cannot be identified from the_||||||||
||_context, the preservation_||||||||
||_evidence policy should be_||||||||
||_included directly in the_||||||||
||_preservation evidence._||||||||
||||||||||



96 

Federal Office for Information Security 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-9.2-05_|_[CONDITIONAL] If the_||If applicable,<br>the<br>assessor<br>shall<br>assess<br>the<br>(public)<br>documentation of the PSP and verify that the<br>PSP:<br>- described the use of cryptographically<br>methods to protect the included preservation<br>evidence policy in the preservation evidence.<br>See also**OVR-9.2-04.**|<br> <br> <br>|If applicable,<br>the assessor shall assess the PSP on-site and verify<br>that the PSP:<br>- implemented cryptographically methods to<br>protect the included preservation evidence policy<br>in the preservation evidence.<br>See also**OVR-9.2-04.**|<br> <br>|||
||_preservation evidence policy_||||||||
||_is included in the_||||||||
||_preservation evidence, it_||||||||
||_should be cryptographically_||||||||
||_protected._||||||||
||||||||||



Federal Office for Information Security 

97 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

## **9.3 Preservation of digital signatures** 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-9.3-01_|_[PDS][PDS+PGD]_|<br>|Only applicable in case of [PDS] [PDS+PGD] :<br>The assessor shall assess (public) the<br>documentation of the PSP and verify that the<br>PSP:<br>- described what efforts to collect and verify<br>the validation data according to a signature<br>validation policy are done.<br>or<br>-stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing<br>the service and this requirement by this PSP.||Only applicable in case of [PDS] [PDS+PGD]<br>and<br>If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant<br>executables), stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- implemented efforts to collect and verify the<br>validation data according to a signature<br>validationpolicy,as documented.||||
||_[CONDITIONAL] If the_||||||||
||_validation data is not_||||||||
||_submitted by the preservation_||||||||
||_client, the preservation_||||||||
||_service shall make its best_||||||||
||_efforts to collect and verify_||||||||
||_the validation data according_||||||||
||_to the signature validation_||||||||
||_policy supported by the_||||||||
||_preservation profile) see_||||||||
||_clause 6.6)._||||||||
||||||||||



Federal Office for Information Security 

98 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-9.3-02_|_[PDS][PDS+PGD]_|<br>|Only applicable in case of [PDS] [PDS+PGD] :<br>The assessor shall assess (public) the<br>documentation of the PSP and verify that the<br>PSP:<br>- described the verification process verifying<br>the signature validation data, if the validation<br>data is submitted by the preservation client.<br>The process shall include that the verification<br>of the submitted data is according to the<br>signature validation policy supported by the<br>preservation profile and that the submitted<br>validation data is appropriate. Otherwise, the<br>PSP described that the PSP collects and<br>verifies the appropriate validation data.<br>or<br>-stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing<br>the service and this requirement by this PSP.|<br> <br>|Only applicable in case of [PDS] [PDS+PGD]<br>and<br>If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant<br>executables), stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- implemented the verification process for<br>submitted validation data by the preservation<br>client.<br>When the validation data is submitted by the<br>preservation client, the verification process has to<br>include the verification of the validation data<br>according to the signature validation policy<br>supported by the preservation profile and the<br>verification that the submitted verification data is<br>appropriate. If the submitted validation data is<br>not submitted, then it should be possible to<br>collect and verify the appropriate validation data.<br>The assessor cause the PSP to show, at least, one<br>example for presenting the validation process,<br>described before for each signature validation<br>policysupported bythepreservationprofile.|<br> <br> <br> <br> <br> <br>|||
||_[CONDITIONAL] If the_||||||||
||_validation data is submitted_||||||||
||_by the preservation client, the_||||||||
||_preservation service should_||||||||
||_verify the submitted_||||||||
||_validation data according to_||||||||
||_the signature validation_||||||||
||_policy supported by the_||||||||
||_preservation profile (see_||||||||
||_clause 6.6), and verify that_||||||||
||_the submitted validation data_||||||||
||_is appropriate, otherwise it_||||||||
||_should collect and verify the_||||||||
||_appropriate validation data._||||||||
||||||||||



Federal Office for Information Security 

99 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-9.3-03_|_[PDS] To extend the ability_|<br> <br>NOTE 1: A proof<br>of existence of a<br>detached<br>signature<br>provides also a<br>proof of existence<br>of the signed data<br>at as long<br>algorithms, e.g.<br>the hash function<br>used in the<br>original signature<br>is resistant<br>against collision<br>attacks.|<br> <br> <br>Only applicable in case of [PDS] :<br>The assessor shall assess the (public)<br>documentation of the PSP and verify that the<br>PSP:<br>- described how the preservation service<br>provides (at a minimum) a proof of existence<br>of the signature and of the validation data<br>needed to validate the signature using digital<br>signature techniques.<br>or<br>-stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing<br>the service and this requirement bythis PSP.|<br>|Only applicable in case of [PDS]  :<br>If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant<br>executables), stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- implemented (at a minimum) a proof of<br>existence of the signature and of the validation<br>data needed to validate the signature using digital<br>signature techniques, as documented.|<br>|||
||_to validate a digital signature_||||||||
||_and to maintain its validity_||||||||
||_status, the preservation_||||||||
||_service shall, at the_||||||||
||_minimum, provide a proof of_||||||||
||_existence of the signature and_||||||||
||_of the validation data needed_||||||||
||_to validate the signature_||||||||
||_using digital signature_||||||||
||_techniques (digital_||||||||
||_signatures, time-stamps,_||||||||
||_evidence records)._||||||||
||||||||||



Federal Office for Information Security 

100 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-9.3-04_|_[PDS+PGD] To extend the_|<br> <br>NOTE 2: The<br>present<br>document gives<br>no restrictions<br>on the way the<br>preservation<br>service obtains<br>the validation<br>data needed to<br>validate the<br>signature.<br>EXAMPLE: The<br>preservation<br>service can use<br>an internal or<br>external<br>validation<br>service to obtain<br>the needed<br>validation data,<br>or just apply an<br>appropriate<br>time-stamp and<br>perform an<br>X.509 validation<br>of the signer’s<br>certification<br>path.|<br> <br>Only applicable in case of [PDS+PGD] :<br>The assessor shall assess the (public)<br>documentation of the PSP and verify that the<br>PSP:<br>- described how the preservation service<br>provides a proof of existence of the signature,<br>the signed data and the validation data needed<br>to validate the signature<br>or<br>-stated which**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is used for providing<br>the service and this requirement by this PSP<br>See also**[ASS 119 511]**,**OVR-0.3-03**.||Only applicable in case of [PDS+PGD] :<br>If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables<br>or by inspecting suitable samples), stage 2 will<br>not be executed.<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- implemented a proof of existence of the signed<br>data, as documented.<br>See also**[ASS 119 511]**,**OVR-0.3-03**.||||
||_ability to validate a digital_||||||||
||_signature and to maintain its_||||||||
||_validity status, the_||||||||
||_preservation service shall, on_||||||||
||_one side, provide a proof of_||||||||
||_existence of the signature and_||||||||
||_of the validation data needed_||||||||
||_to validate the signature and_||||||||
||_on the other side a proof of_||||||||
||_existence of the signed data._||||||||
||||||||||



Federal Office for Information Security 

101 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-9.3-05_|_[PDS][PDS+PGD]_|<br>|Only applicable in case of [PDS] [PDS+PGD] :<br>The assessor shall assess the (public)<br>documentation of the PSP and verify that the<br>PSP:<br>- described, if the preservation service, in case<br>of a detached signature, allows to the<br>subscribers to provide only a hash value of the<br>signed data instead of the signed data.||Only applicable in case of [PDS] [PDS+PGD] :<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- implemented, in case of a detached signature,<br>how the subscribers are able to use a hash value<br>of the signed data instead of the signed data, as<br>documented.<br>The assessor shall cause the PSP to show at least<br>one example of the hashed signed data.||||
||_[CONDITIONAL] In the case_||||||||
||_of a detached signature, the_||||||||
||_preservation service may_||||||||
||_allow the subscriber to_||||||||
||_provide only a hash value of_||||||||
||_the signed data instead of the_||||||||
||_signed data itself._||||||||
||||||||||
|_OVR-9.3-06_|_[PDS][PDS+PGD]_||Only applicable in case of [PDS] [PDS+PGD] :<br>The assessor shall assess the (public)<br>documentation of the PSP and verify that the<br>PSP:<br>- described the identifiers of the supported hash<br>functions for each preservation profile.<br>See also**[ASS 119 511]**,**OVR-6.1-03**&**OVR-**<br>**9.3-05**.|<br>|Only applicable in case of [PDS] [PDS+PGD] :<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- implemented, in case of a detached signature<br>and if the preservation service allows the<br>subscribers to provide only a hash value of the<br>signed data, the identifiers of the supported hash<br>functions in the preservation profile, as<br>documented.<br>See also**[ASS 119 511]**,**OVR-6.4-01**et. seq. &<br>**OVR-9.3-05.**||||
||_[CONDITIONAL] In case of_||||||||
||_a detached signature and if_||||||||
||_the preservation service_||||||||
||_allows the subscriber to_||||||||
||_provide only a hash value of_||||||||
||_the signed data, the PSP_||||||||
||_shall indicate in the_||||||||
||_preservation profile the_||||||||
||_identifiers of the hash_||||||||
||_functions that can be used._||||||||
||||||||||



Federal Office for Information Security 

102 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-9.3-07_|_[PDS][PDS+PGD]_|<br>NOTE 3: In this<br>case, the<br>preservation<br>service is only<br>responsible for<br>the preservation<br>of the submitted<br>hash value<br>(associated with<br>a hash function<br>identifier).|Only applicable in case of [PDS] [PDS+PGD] :<br>The assessor shall assess the (public)<br>documentation of the PSP and verify that the<br>PSP:<br>- described how the preservation service treats<br>the hash value (associated with a hash function<br>identifier) as a general data linked somehow to<br>the signatures, since it has no way of knowing<br>if the hash value really corresponds to the<br>signed data.<br>See also**[ASS 119 511]**,**OVR-9.3-05**.|<br>|Only applicable in case of [PDS] [PDS+PGD] :<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- implemented the process that the preservation<br>service treats the hash value (associated with a<br>hash function identifier) as a general data linked<br>somehow to the signatures, since it has no way<br>knowing if the hash value really corresponds to<br>the signed data, as documented.<br>The assessor shall cause the PSP to show at least<br>one example presenting the process.<br>See also**[ASS 119 511]**,**OVR-9.3-05**.||||
||_[CONDITIONAL] In case of_||||||||
||_a detached signature and if_||||||||
||_the preservation service_||||||||
||_allows the subscriber to_||||||||
||_provide only a hash value of_||||||||
||_the signed data, the_||||||||
||_preservation service shall_||||||||
||_treat the hash value_||||||||
||_(associated with a hash_||||||||
||_function identifier) as a_||||||||
||_general data linked somehow_||||||||
||_to the signature, since it has_||||||||
||_no way of knowing if the_||||||||
||_hash value really_||||||||
||_corresponds to the signed_||||||||
||_data._||||||||



Federal Office for Information Security 

103 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|<br>**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_OVR-9.3-08_|_[PDS][PDS+PGD]_||Only applicable in case of [PDS] [PDS+PGD] :<br>The assessor shall assess the (public)<br>documentation of the PSP and verify that the<br>PSP:<br>- described how the hash function identifier<br>and its length, included in the submitted<br>preservation objects, are verified with the<br>supported hash functions and their lengths in<br>the preservation profile.<br>See also**[ASS 119 511]**,**OVR-9.3-05**.||Only applicable in case of [PDS] [PDS+PGD] :<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- implemented a comparison of the hash function<br>identifier included in the submitted preservation<br>object and its length with the in the preservation<br>profile supported hash functions and theirs<br>lengths, as documented.<br>See also**[ASS 119 511]**,**OVR-9.3-05**.||||
||_[CONDITIONAL] In case of_||||||||
||_a detached signature and if_||||||||
||_the preservation service_||||||||
||_allows the subscriber to_||||||||
||_provide only a hash value of_||||||||
||_the signed data, the_||||||||
||_preservation service shall_||||||||
||_verify that the submitted_||||||||
||_preservation object contains_||||||||
||_hash function identifiers that_||||||||
||_are in accordance with the_||||||||
||_identifiers of the hash_||||||||
||_functions listed in the_||||||||
||_preservation profile and that_||||||||
||_each hash value has a length_||||||||
||_in accordance with the_||||||||
||_associated hash function_||||||||
||_identifier._||||||||



Federal Office for Information Security 

104 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

## **10 Assessment criteria for Annex A (normative): Qualified preservation service for QES as defined by article 34 the Regulation (EU) No 910/2014** 

_NOTE 1: This clause aims at providing requirements for a preservation service allowing it to fulfil the requirement of Regulation (EU) No 910/2014 [i.1] for qualified preservation service for qualified electronic signature and or seals (QES)_ 

_NOTE 2: A qualified preservation service is only mentioned for the preservation of QES, not for the preservation of general data. However, nothing forbids such a service to preserve also other data._ 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor Guidance_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
||||**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|OVR-A-01|_[PDS] [PDS+PGD] All_||Only applicable in case of [PDS]<br>[PDS+PGD] :<br>See above||Only applicable in case of [PDS] [PDS+PGD] :<br>See above||||
||_requirements from_||||||||
||_clause 5 to 9 shall_||||||||
||_apply._||||||||
||||||||||
||_In addition:_||||||||
||||||||||
||||||||||



105 

Federal Office for Information Security 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor Guidance_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
||||**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|OVR-A-02|_[PDS] [PDS+PGD]_|_NOTE 3:_<br>_As long as the corresponding_<br>_EU Member State (EUMS)_<br>_trusted list is provided the_<br>_information of historical_<br>_services is included and_<br>_publicly available._<br>_NOTE 4:_<br>_CID (EU) 2015/1505 [i.3]_<br>_defines the technical_<br>_specifications and formats_<br>_relating to EUMS trusted lists_<br>_pursuant to Article 22(5) of_<br>_Regulation (EU) No 910/2014_<br>_[i.2]._|Only applicable in case of [PDS]<br>[PDS+PGD] :<br>The assessor shall assess the(public)<br>documentation of the PSP and verify that<br>the PSP:<br>- described how the PSP preserves the<br>qualified status of the CA (e.g. preserving<br>the appropriate TL) that has issued the<br>qualified certificate or is used to sign the<br>general data until the end of the<br>preservation period.|<br> <br> <br> <br> <br> <br> <br>|Only applicable in case of [PDS] [PDS+PGD] :<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- implemented a preservation process of the<br>qualified status of the CA (e.g. preserving the<br>appropriate TL), that issued the qualified<br>certificate [PDS] or was used as the issuer of the<br>signing certificate (to sign the general data<br>[PDS+PGD]), as documented.<br>The assessor shall cause the PSP to show at least<br>one example of the preserved information about<br>the status of the qualified certificate.|<br> <br> <br> <br> <br> <br> <br>|||
||_The preservation_||||||||
||_service shall preserve_||||||||
||_all information needed_||||||||
||_to check the_||||||||
||_qualification status of_||||||||
||_the electronic signature_||||||||
||_or seal that would not_||||||||
||_be publicly available_||||||||
||_until the end of the_||||||||
||_preservation period._||||||||
||||||||||



106 

Federal Office for Information Security 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor Guidance_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
||||**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|OVR-A-03|_[PDS] [PDS+PGD]_||Only applicable in case of [PDS]<br>[PDS+PGD] :<br>The assessor shall assess the (public)<br>documentation of the PSP and verify that<br>the PSP:<br>- verifies the EU qualified status of time-<br>stamping authority provided by a qualified<br>TSA by using the appropriate TL, if a<br>qualified time stamp is required<br>or<br>-stated<br>which<br>**[TR-ESOR]**<br>certified<br>product of version V1.2.1 or higher is used<br>for providing the service and this<br>requirement by this PSP.|<br> <br> <br> <br> <br> <br> <br> <br>|Only applicable in case of [PDS] [PDS+PGD] :<br>If the claimed**[TR-ESOR]**certified product of<br>version V1.2.1 or higher is in fact deployed for<br>providing the service (checked e.g. by comparing<br>the digital fingerprint of the relevant executables),<br>stage 2 will not be executed.<br>Otherwise:<br>The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- implemented the use of qualified time-stamps<br>provided by a qualified TSA, as documented.<br>If this is the case, the assessor shall inspect at least<br>one example of requesting a qualified time-stamp<br>provided by a qualified TSA and of demonstrating<br>the verification of the time-stamping authority<br>including the use of the appropriate TL.|<br> <br> <br> <br> <br> <br> <br> <br> <br>|||
||_Time-stamps used_||||||||
||_within the preservation_||||||||
||_evidence should be_||||||||
||_provided by a qualified_||||||||
||_TSA._||||||||
||||||||||



Federal Office for Information Security 

107 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor Guidance_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
||||**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|OVR-A-04|_The preservation_|<br>EXAMPLE 1:<br>The<br>PKI<br>certificate<br>corresponding to an electronic<br>seal that is applied to a receipt<br>returned to the client after<br>submitting<br>data<br>to<br>the<br>preservation service.<br>EXAMPLE 2:<br>The<br>PKI<br>certificate<br>corresponding<br>to<br>an<br>SSL<br>certificate<br>used<br>when<br>connecting to the preservation<br>service.<br>EXAMPLE 3:<br>The certificate of a TSA service<br>uniquely<br>used<br>by<br>the<br>preservation service.<br>EXAMPLE 4:<br>In case, no PKI public key<br>technology is used to identify<br>the preservation service, an<br>indicator expressed by a URI<br>which<br>uniquely<br>and<br>unambiguously identifies the<br>preservation service.|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>The assessor shall assess the(public)<br>documentation of the PSP and verify that<br>the PSP:<br>- described one service identifier as<br>defined in 5.5.3 of**[ETSI TS 119 612]**for<br>its preservation service, which allows to<br>uniquely and unambiguously identify the<br>service within a EUMS trusted list.|<br> <br> <br> <br> <br>|The assessor shall assess the PSP on-site and<br>verify that the PSP:<br>- implemented one service identifier as defined in<br>5.5.3 of**[ETSI TS 119 612]**for its preservation<br>service.<br>The assessor shall verify whether the service<br>identifier used from the PSP is identical to the<br>entries of the applicable EUMS trusted list3.|<br> <br> <br> <br>|||
||_service shall have one_||||||||
||_service digital identifier_||||||||
||_as defined in 5.5.3 of_||||||||
||**_ETSI TS 119 612_**_[2]_||||||||
||_which allows to_||||||||
||_uniquely and_||||||||
||_unambiguously identify_||||||||
||_the service within an_||||||||
||_EUMS trusted list_.||||||||
||||||||||



> 3 This check will fail in case of an initial conformity assessment and will be reconsidered in subsequent audits. 

Federal Office for Information Security 

108 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

## **11 References** 

## **11.1 Normative References** 

References are either specific (identified by the date of publication and/or edition number or version number) or non-specific. For specific references only the cited version applies. For non-specific references the latest version of the referenced document (including any amendments) applies. Referenced documents, which are not found to be publicly available in the expected location, might be found at https://docbox.etsi.org/Reference. The following referenced documents are necessary for the application of the present document. 

|**_Reference_**|**_Document Title, Version / Date_**|
|---|---|
|ASS 319 401|BSI Criteria for Assessing:_Criteria for Assessing Trust Service Providers_<br>_against ETSI Policy Requirements, Part 1: Assessment Criteria for all TSP -_<br>_ETSI EN319 401_.|
|ASS 119 511|BSI Criteria for Assessing:_Criteria for Assessing Trust Service Providers_<br>_against ETSI Policy Requirements, Part 2: Assessment Criteria providing long-_<br>_term preservation of digital signatures or general data using digital signature_<br>_techniques- ETSI TS 119 511_.|
|EGovG|Act to promote electronic government (E-Government Act – EgovG), last<br>changed at 20.11.2019, https://www.gesetze-im-<br>internet.de/englisch_egovg/index.html|
|ETSI EN 319 403|ETSI EN 319 403 V2.2.2 (2015-08):_Electronic Signatures and Infrastructures_<br>_(ESI); Trust Service Provider Conformity Assessment - Requirements for_<br>_conformity assessment bodies assessing Trust Service Providers._|
|ETSI EN 319 421|ETSI EN 319 421 V1.1.1 (2016-03):_Electronic Signatures and Infrastructures_<br>_(ESI); Policy and Security Requirements for Trust Service Providers issuing_<br>_Time-Stamps._|
|ETSI EN 319 422|ETSI EN 319 422 V1.1.1 (2016-03):_Electronic Signatures and Infrastructures_<br>_(ESI); Time-stamping protocol and time-stamp token profiles._|
|ETSI TS 119 312|_ETSI TS 119 312: Electronic Signatures and Infrastructures (ESI);_<br>_Cryptographic Suites._|
|ETSI TS 119 403-3|TS 119 403-3 V1.1.1 (2019-03):_Trust Service Provider Conformity Assessment;_<br>_Part 3: Additional Requirements for Conformity Assessment Bodies assessing_<br>_EU qualified trust service providers._|



Federal Office for Information Security 

109 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Document Title, Version / Date_**|
|---|---|
|ETSI TS 119 511|ETSI TS 119 511 V1.1.1 (2019-006):_Electronic Signatures and Infrastructures_<br>_(ESI); Policy and security requirements for trust service providers providing_<br>_long-term preservation of digital signatures or general data using digital_<br>_signature techniques._|
|ETSI TS 119 512|ETSI TS 119 512 V1.1.1 (2020-01):_Electronic Signatures and Infrastructures_<br>_(ESI); Protocols for trust service providers providing long-term data_<br>_preservation services._|
|ETSI TS119 612|ETSI TS119 612: _Electronic Signatures and Infrastructures (ESI); Trusted Lists._|
|FIPSPUB 140-2|FIPSPUB 140-2: _Security Requirements for Cryptographic Modules._|
|IETF RFC 3161|IETF RFC 3161:_Internet X.509 Public Key Infrastructure Time-Stamp Protocol_<br>_(TSP)._|
|IETF RFC 4998|IETF RFC 4998:_Evidence Record Syntax (ERS)._|
|IETF RFC 5816|IETF RFC 5816:_ESSCertIDv2 Update for RFC 3161_|
|IETF RFC 6283|IETF RFC 4998:_Extensible Markup Language Evidence Record Syntax_<br>_(XMLERS)._|
|ISO/IEC 15408|ISO/IEC 15408:_Information technology -- Security techniques -- Evaluation_<br>_criteria for IT security._|
|ISO/IEC 17065|ISO/IEC 17065:2012:_Conformity assessment -- Requirements for bodies_<br>_certifying products, processes and services._|
|ISO/IEC 19790|ISO/IEC 19790:_Information technology -- Security techniques -- Security_<br>_requirements for cryptographic modules._|
|TR-ESOR|BSI Technical Guideline 03125:_Preservation of Evidence of_<br>_Cryptographically Signed Documents (on base of the eIDAS-Regulation and_<br>_ETSI Preservation Standards)_, V1.2.1 and later versions,<br>NOTE:<br>Available in English at https://www.bsi.bund.de/EN/tr-esor, in<br>German at https://www.bsi.bund.de/tr-esor.|
|TR-ESOR-E|BSITechnical Guideline03125:_Preservation of Evidence of Cryptographically_<br>_Signed Documents: Annex TR-ESOR-E_<br>_Concretisation of the Interfaces on the Basis of the eCard-APIM.ramework, V1.2.1_<br>_and later versions._|
|TR-ESOR-E-<br>Appendix|BSITechnical Guideline03125:_TR-ESOR-E-Annex: Grobkonzept des BSI-_<br>_TS119512-S.4-Transformators._|



Federal Office for Information Security 

110 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Reference_**|**_Document Title, Version / Date_**|
|---|---|
|TR-ESOR-M.3|BSITechnical Guideline03125:_Preservation of Evidence of Cryptographically_<br>_Signed Documents: Annex TR-ESOR-M.3 ArchiSig-Module, V1.2.1 and later_<br>_versions._|



**Table 2: Normative References** 

## **11.2 Informative References** 

References are either specific (identified by the date of publication and/or edition number or version number) or non-specific. For specific references only the cited version applies. For non-specific references the latest version of the referenced document (including any amendments) applies. The following referenced documents are not necessary for the application of the present document but they assist the user with regard to a particular subject area. 

|**_Reference_**|**_Document Title, Version / Date_**|
|---|---|
|eIDAS<br>(_Regulation_<br>_(EU) No 910/2014)_|_Regulation (EU) No 910/2014 of the European Parliament and of the Council of 23_<br>_July 2014 on electronic identification and trust services for electronic transactions in_<br>_the internal market and repealing Directive 1999/93/EC_. OJ L 257, 28.8.2014, p. 73-<br>114.|
|ETSI EN 319 401|ETSI EN 319 401 V2.2.1 (2018-04):_Electronic Signatures and Infrastructures (ESI);_<br>_General Policy Requirements for Trust Service Providers._|
|ETSI EN 319 411-1|ETSI EN 319 411-1 V1.1.1 (2016-02):_Electronic Signatures and Infrastructures_<br>_(ESI); Policy and security requirements for Trust Service Providers issuing_<br>_certificates; Part 1: General requirements._|
|ETSI EN 319 411-2|ETSI EN 319 411-2 V2.1.1 (2016-02):_Electronic Signatures and Infrastructures_<br>_(ESI); Policy and security requirements for Trust Service Providers issuing_<br>_certificates; Part 2: Requirements for trust service providers issuing EU qualified_<br>_certificates_|
|ISO 27001|ISO/IEC 27001:2013:_Information technology - Security techniques - Information_<br>_security management systems – Requirements._|
|ISO 27002|ISO/IEC 27002:2013:_Information technology - Security techniques - Code of practice_<br>_for information security management._|



Federal Office for Information Security 

111 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Document Title, Version / Date_**|
|---|---|
|Regulation (EC) No<br>765/2008|_Regulation (EC) No 765/2008 of the European Parliament and of the Council of 9 July_<br>_2008 setting out the requirements for accreditation and market surveillance relating_<br>_to the marketing of products and repealing Regulation (EEC) No 339/93._|



## **Table 3: Informative References** 

Federal Office for Information Security 

112 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

## Keywords and Abbreviations 

|**_Abbreviation _**|**_Keyword_**|
|---|---|
|[ABC]|for: document ABC|
|AUG|Augmentation|
|CA|Certificate Authority|
|ETSI EN 319 411-2|ETSI EN 319 411-2 V2.1.1 (2016-02):_Electronic Signatures and Infrastructures_<br>_(ESI); Policy and security requirements for Trust Service Providers issuing_<br>_certificates; Part 2: Requirements for trust service providers issuing EU qualified_<br>_certificates_|
|CAB|Conformity Assessment Body|
|CRL|Certificate Revocation List|
|eIDAS|REGULATION (EU) No 910/2014 OF THE EUROPEAN PARLIAMENT AND OF<br>THE COUNCIL of 23 July 2014 on electronic identification and trust service for<br>electronic transactions in the internal market and repealing Directive 1999/93/EC|
|et. seq.|et sequence|
|EU|European Union|
|EUMS|European Union Member State|
|GDPR|General Data Protection Regulation|
|IS-Policy|Information Security Policy (see e.g.**[EN 319 401]**, chapter 6.3.)|
|IT|Information Technology|
|NC|Non-Conformity|
|OCSP|Online Certificate Status Protocol|
|OID|Object Identifier|
|OVR|Overall|
|PDS|Preservation of Digital Signature|



Federal Office for Information Security 

113 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Abbreviation _**|**_Keyword_**|
|---|---|
|PGD|Preservation of General Data|
|PI|Potential for Improvement|
|PO|Preservation Object|
|POC|Preservation Object Container|
|PRP|Preservation Service Protocol|
|PSP|Preservation Service Provider|
|PSPS|Preservation Service Practice Statement|
|QES|Qualified Electronic Signature or qualified electronic seal|
|QTSP|Qualified Trust Service Provider|
|(Q)TPS|TSP or QTSP|
|QPSP|Qualified Preservation Service Provider|
|(Q)TPS|TSP or QTSP|
|QPSP|Qualified Preservation Service Provider|
|(Q)PSP|PSP or QPSP|
|R|Recommendation|
|SSL|Secure Sockets Layer|
|SubDO|Submission Data Object|
|T&C|Terms and Conditions|
|TL|Trusted List|
|TR-ESOR|DE: Technische Richtlinie zur Beweiserhaltung kryptographisch signierter<br>Dokumente<br>EN: Technical Guideline for Preservation of Evidence of Cryptographically Signed<br>Documents|
|TSA|Time-Stamping Authority|



Federal Office for Information Security 

114 

Part 2: Assessment Criteria providing long-term preservation of digital signatures or general data using digital signature techniques – ETSI TS 119 511 

|**_Abbreviation _**|**_Keyword_**|
|---|---|
|TSP|Trust Service Provider|
|TS-Policy|Trust Service Policy|
|TSPS|Trust Service Practice Statement (see e.g.**[EN 319 401]**, chapter 6.1.)|
|UTC|Coordinated Universal Time|
|WOS|Without Storage|
|WST|With Storage|
|WTS|With Temporary Storage|



## **Table 4:  Keywords and Abbreviations** 

115 

Federal Office for Information Security 


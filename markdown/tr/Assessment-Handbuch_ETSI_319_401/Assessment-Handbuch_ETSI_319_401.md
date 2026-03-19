Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

Federal Office for Information Security P.O.B. 20 03 63 D-53133 Bonn (Germany) Phone: +49 228 99 9582-0 E-mail: tresor@bsi.bund.de Internet: https://www.bsi.bund.de © Federal Office for Information Security (BSI) 2019 

Federal Office for Information Security 

## **Table of Contents** 

## Inhalt 

|1|Introduction|5|
|---|---|---|
|1.1|Purpose|5|
|2|Scope of Document|5|
|2.1|Assessment Framework|6|
|2.2|Document Overview|7|
|3|Assessment Approach|9|
|3.1|Assessment Pre-Requisites|9|
|3.2|Strictness of Assessment Criteria|9|
|3.2.1|Requirements|9|
|3.2.2|Assessment Criteria|10|
|3.3|Structure of the Assessment Criteria|10|
|3.4|Assessment Stages and Assessor Activities|11|
|3.4.1|Identification of Assessment Criteria|12|
|4|Structure of Assessment Criteria and Report Template|13|
|5|Assessment Criteria for Risk Assessment|14|
|6|Assessment criteria for Policies and Practices|17|
|6.1|Trust Service Practice Statement|17|
|6.2|Terms and Conditions|20|
|6.3|Information Security Policy|23|
|7|Assessment criteria for TSP Management and Operations|26|
|7.1|Internal organization|26|
|7.1.1|Organization reliability|26|
|7.1.2|Segregation of duties|30|
|7.2|Human resources|30|
|7.3|Asset management|37|
|7.3.1|General requirements|37|
|7.3.2|Media handling|38|
|7.4|Access control|38|
|7.5|Cryptographic controls|42|
|7.6|Physical and environmental security|42|
|7.7|Operation security|45|
|7.8|Network security|49|
|7.9|Incident management|55|
|7.10|Collection of evidence|60|
|7.11|Business continuity management|64|
|7.12|TSP termination and termination plans|65|
|7.13|Compliance|73|
|8|Appendix|75|
|9|References|76|



Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|9.1|Normative References|76|
|---|---|---|
|9.2|Informative References|78|
|10|Keywords and Abbreviations|80|



## **Table of Figures** 

Figure 2: ETSI Assessment Framework .................................................................................. 7 Figure 3: Structure of Assessment Criteria and Report Template ......................................... 13 

## **Table List** 

Table 1: Types of (qualified) Trust Services ........................................................................... 6 Table 2: Normative References ............................................................................................. 77 Table 3: Informative References ............................................................................................ 79 Table 4:   Keywords and Abbreviations ................................................................................ 81 

Federal Office for Information Security 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

## **1 Introduction** 

## **1.1 Purpose** 

Trust services, as specified in Regulation (EU) No 910/2014 **[eIDAS]** (short: eIDAS), shall give participants of electronic commerce confidence in the security of these trust services. This confidence is expected to result from a set of procedures, processes and security measures, the TSP has established in order to minimize the operational and financial threats and risks associated. 

eIDAS distinguishes two trust levels with respect to trust services and providers of trust services: 

- (normal) trust services and trust service providers (TSP) and 

- **qualified** trust services and trust service providers ( **QTSPs** ), that need to fulfil additional legal requirements and are subject to periodical independent third party conformity assessments by accredited conformity assessment bodies (CAB). 

## (Q)TSP means TSP or QTSP. 

Especially **qualified** trust services and QTSPs will fulfil such high expectations of participants. 

**[ETSI EN 319 401]** defines general policy requirements for operation and management practices of a TSP regardless the service it provides. **[ETSI EN 319 401]** does not specify **how** the requirements can be assessed by an independent party and what kind of information and documents shall be subject of such a conformity assessment. **[ETSI EN 319 401]** refers to **[ETSI EN 319 403]** “Requirements for Conformity Assessment Bodies Assessing Trust Service Providers”, which is applicable to CABs and which supplements the international standard **[ISO/IEC 17065]** , which accredited CABs must fulfil. **[ETSI EN 319 403]** poses general requirements on CABs assessing (qualified) trust services and does neither distinguish between different trust services nor define dedicated assessment criteria for the application of standards like **[ETSI EN 319 401]** or standards for dedicated trust services of the ETSI EN 310 4x1 series. 

More specifically, **[ETSI EN 319 401]** defines general requirements on the TSP’s public documentation (e.g. the Trust Service Practice Statement and the Terms and Conditions) and on the TSP management and operation (e.g. human resources, asset management, access control, physical and environmental security, operation and network security). Assessment criteria, derived one-byone from **[ETSI EN 319 401]** requirements, are neither intended nor included. 

In summary, neither the TSP specific standards (ETSI EN 319 4x1) nor the CAB specific standard **[ETSI EN 319 403]** provide dedicated assessment criteria for application for the conformity assessment of TSP. The present document has the goal to bridge this gap with respect to **[ETSI EN 319 401]** . It specifies assessment criteria to be used by accredited conformity assessment bodies (CAB) to assess the conformity of qualified trust service providers ((Q)TSPs) against the standard **[ETSI EN 319 401]** . 

## **2 Scope of Document** 

This **Part 1** of the assessment criteria is the first module for a conformity assessment of TSPs that fulfils the requirements of **[ETSI EN 319 401]** . The assessment criteria are directly derived from the general policy requirements given by **[ETSI EN 319 401]** . CAB shall apply all criteria set out in Part 1 to be conformant to this document. 

In addition to Part 1, 

5 

Federal Office for Information Security 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

there exist further parts of assessment criteria based on **[ETSI EN 319 401]** for other specific trust services. Such assessment criteria will always be additional to those set out in Part 1. Currently, e.g. the following norms and specifications are available to specific types of (qualified) trust services as defined in **[eIDAS]** : 

|**_Type of (Qualified) Trust Service_**|**_Related Norms and Technical Specifications_**|
|---|---|
|creation of qualified certificates for electronic<br>signatures or electronic seals|<br>ETSI EN 319 411-2 together with ETSI EN 319<br>411-1|
|creation of qualified certificates for web site<br>authentication|<br>ETSI EN 319 411-2 together with ETSI EN 319<br>411-1|
|creation of qualified electronic time stamps|ETSI EN 319 421|
|validation of qualified electronic signature and<br>seals|<br>ETSI TS 119 441|
|electronic registered delivery|ETSI EN 319 521 and ETSI EN 319 531|
|signing service|ETSI TS 119 431-1 and ETSI TS 119 431-2|
|preservation service|ETSI TS 119 511 and ETSI TS 119 512|



## **Table 1: Types of (qualified) Trust Services** 

**Not** addressed in this Part 1 are organisational activities of the CAB and its assessors like contract gathering aspects and project management, assessor qualification and audit planning, reporting specific aspects or non-conformity tracking. These aspects are in the scope of **[ISO/IEC 17065]** and **[ETSI EN 319 403]** which are normative to the CAB. 

## **2.1 Assessment Framework** 

Derived assessment criteria are embedded in the European regulatory framework. On EU-level, each TSP underlies especially the eIDAS regulation **[eIDAS]** and the General Data Protection Regulation (GDPR). Conformity Assessment Bodies (CAB) shall comply also with **[EU regulation 765/2008]** . Furthermore, EU implementing acts and national trust service laws apply to both. The ETSI series related to trusted services apply to TSPs in the same way, as related to ISO and ETSI norms and standards or specifications apply to CABs. The following figure sketches hierarchy of documented regulatory framework and shows the relation to a Preservation Service Provider (as an example of a TSP) and a CAB as acting entities. The assessment criteria are applicable to CAB only. 

6 

Federal Office for Information Security 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 


![](markdown/tr/Assessment-Handbuch_ETSI_319_401/Assessment-Handbuch_ETSI_319_401.pdf-0007-01.png)


**Figure 1: ETSI Assessment Framework** 

**[ETSI EN 319 401]** specifies general policy requirements on the operation and management practices of a TSP regardless of the service the TSP provides. 

Subordinated **[ETSI EN 319 411-1]** or **[ETSI TS 119 511]** specify specific policy requirements, depending on the specific service of the TSP. So, other than **[ETSI EN 319 401]** , only those norms and specifications from ETSI series apply, which are required for the specific type of trust service. As an example, **[ETSI EN 319 411-1]** applies to TSPs issuing certificates for natural or legal persons. In the same way, **[ETSI TS 119 511]** applies to Preservation Service Providers. 

The regulatory framework for CABs is based on **[ISO/IEC 17065]** as accreditation norm, amended by **[ETSI EN 319 403]** . 

The assessment requirements are then based on the standards, the TSP has to conform to. For example, the“Policy and Security Requirements for Trust Service Providers e.g. providing long-term Preservation of digital Signatures or general Data using digital Signature Techniques” are based on **[ETSI EN 319 401]** and **[ETSI TS 119 511]** . 

## **2.2 Document Overview** 

The following **chapter 3** specifies the assessment approach. It gives the frame for applying the criteria found in the following chapters. 

In **chapter 4,** the present document describes the structure and explains the content of the tables, which contain norm requirements together with detailed assessment criteria. The last column provides space to fill in observations, verdicts and finding, as a result of an assessment. 

Federal Office for Information Security 

7 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

Subsequent **chapters 5 to 7** define the assessment criteria for conformity assessment against **[ETSI EN 319 401],** following its document structure. 

The assessment criteria are written in such a way that the present document (or the respective parts of it) could be used as **template** for the documentation of the results of a conformity assessment. An utilisation of the tables within a spreadsheet might be helpful for an actual assessment. 

Federal Office for Information Security 

8 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

## **3 Assessment Approach** 

## **3.1 Assessment Pre-Requisites** 

For demonstrating conformance to **[ETSI EN 319 401]** all assessment criteria in this document shall be applied. 

Pre-requisites for such a conformance assessment are the following aspects: 

- Due to the public nature of the provided trust services, the TSP has to **document** its implementing practices, together with legal terms and conditions. These documents target public audiences, who can be any party relying on the provided trust services. With those documents, the TSP shows, what and how it is doing to fulfil the applicable norm requirements, here **[ETSI EN 319 401]** . 

- The TSP has to **implement** all trust service practices laid down in its publicly **1** available documents. Clearly, its implementation must fully conform to its own public documents. 

The CAB will assess the TSP as an organisation with its documentation and its implemented trust services based on the assessment criteria from the present document. The main task of the assessor is to determine if all mandatory assessment criteria are fulfilled. In this case conformance to **[ETSI EN 319 401]** is implied. 

Before starting a conformity assessment, a contract between the accredited CAB and the TSP needs to be established. Further pre-requisites on the assessment process result from the accreditation of the CAB against **[ISO/IEC 17065]** and **[ETSI EN 319 403]** (e.g. audit team, assessment plan). They are out of scope of the present document, which focusses on the assessment activities itself and – in detail – on the expected results. 

## **3.2 Strictness of Assessment Criteria** 

For a better understanding of the strictness of the assessment criteria within this document, it is necessary to clearly separate between the two different types of rules to be followed: 

- “Requirements” are applicable to TSPs and directly originate from the related ETSI documents ( **[ETSI EN 319 401]** , **[ETSI EN 319 411-1]** , etc.). 

- The assessment “criteria” are applicable to the CAB and its assessors and mainly derived from those ETSI documents applicable to TSPs. 

## **3.2.1 Requirements** 

Requirements from TSP related ETSI documents use the modal verbs terminology of ETSI Drafting Rules, clause 3.2 (Verbal forms for the expression of provisions): "shall", "shall not", "should", "should not", "may", "need not", "will", "will not", "can" and "cannot". 

Whenever the assessor identifies a “shall” requirement not being fulfilled by a TSP, a **nonconformity (NC)** results. Such a NC may result in a stop of business for the TSP. Any decision about the severeness of non-conformities is up to the CAB, the assessor is working for and resides outside the scope of this document. 

1 

Mandatory public documents of the TSP are its TSPS and terms & conditions. 

Federal Office for Information Security 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

Likewise, if a “SHOULD” requirement is unfulfilled by a TSP, a **recommendation (R)** results and further audits by the CAB are necessary. 

A “SHOULD” requires from the TSP either to fulfil the requirement exactly as it is specified or respective test cases should demonstrate the specified behaviour to make evident that it`s equivalent to the requirements and to the required security levels. 

Remark: not related to the strictness are so called **potentials for improvement (PI),** an assessor may identify. These PI are only informative to the TSP. 

## **3.2.2 Assessment Criteria** 

Regarding the assessment criteria, this document uses the following three major classes of assessment criteria (cf. [RFC 2119]) 

- MAY: These criteria are just hints or optional activites of the assessor. These criteria will not result in mandatory assessment activities. 

- SHOULD: These criteria are strong recommendations. Respective assessment activities should be performed by the assessor. Alternatively, the assessor explains why he or she uses a different approach and why this activity assures the same assessment result as the original activity. 

- SHALL (or synonymously MUST): These are strict criteria. It is not allowed to use different assessment activities. 

The strictness of the assessment criteria applicable to the CAB and its assessors is to be specified by the applicable accreditation and certification scheme and resides outside the scope of this document. 

## **3.3 Structure of the Assessment Criteria** 

The order of the assessment criteria follows the document structure (chapters, sections) of norm **[ETSI EN 319 401]** . For each individual norm requirement, assessment criteria are derived for either stage 1 document assessment or/and stage 2 on-site assessment, as applicable. A conformant design of the provided trust services, laid-out in the TSP documents (stage 1) is a pre-requisite for starting to audit the actual implementation on-site (stage 2). 

Norm chapters address specific aspects, a (Q)TSP and/or its trust service(s) need to fulfil. Such aspects range 

- from sole **document** related requirements, which the documents of a (Q)TSP need to conform with; 

- through requirements related to **organisational** structure and processes and its procedures; 

- down to **infrastructural** requirements, both physical and logical (i. e. building infrastructure and IT infrastructure). 

Such a broad range of aspects is due to the overarching nature of “policy” requirements. A reason for such an approach are current **information security management practices.** To handle security, the purpose of business and applied processes need to be understood. Then immanent risks in the type of business and processes (to be implemented) need to be identified and treated assuring an acceptable level of security. Such treatment is structured along security measures. There are four generic types of **security measures:** 

- **Physical** security measures, 

Federal Office for Information Security 

10 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

- **Organisational** security measures, 

- **Personnel** related security measures, and 

- **Technology** related security measures. 

In a similar way, all assessment criteria are related to both, **functional and security aspects,** often at the same time and regardless of being related to (Q)TSP documentation and/or to actual implementation of provided trust service(s). The basic nature of trust service is trust, so functional aspects like the generation of certificates or signatures are actually security functions, using cryptography and implementing security objectives as integrity, confidentiality or authenticity. A sharp distinction between functional and security aspects is therefore at least difficult, if not impossible. The assessment must consider functional and security aspects always at the same time. 

## **3.4 Assessment Stages and Assessor Activities** 

The **assessment** of a (Q)TSP is performed by an accredited CAB on the basis of **[EN 319 403]** and split into two stages (see also **[ETSI EN 319 403]** ): 

- **Stage 1** – Document Assessment: the CAB assesses the documentation of the (Q)TSP for conformance with the requirements laid out in the applicable ETSI standard(s); 

- **Stage 2** – On Site Assessment **2** (Audit): the CAB assesses the (Q)TSP management, organisation, processes, documentation, facilities and infrastructures on site, i.e. at the (Q)TSP premises, for conformance with the requirements laid out in the applicable ETSI standard(s). 

At each stage, the CAB assessment includes **analytic, conclusive and reporting activities.** So the CAB assessor will 

- analyse documents, 

- ask questions and perform interviews, 

- Inspect and has an eye on-site. 

Based on this the assessor: 

- wants to understand the organisation and its services, 

- identifies potential gaps or non-conformities, 

- concludes whether the (Q)TSP fulfils its requirements, and finally 

- prepares a report on its findings and observations. 

The assessment criteria require from the assessor to perform certain activities and to check the expected results, with respect to the requirements. Per stage, the assessor describes the observations during his or her activity and gives per criterion a verdict (either “OK” or “not OK”). Also, he or she includes (negative) findings, expressed as non-conformities, recommendations or potentials for improvement. 

The assessor must document all results of assessor activities. For this, the tables in chapter 5 to 7 SHOULD be used as a template for logging. Finally, an assessment report SHALL be written. See 

> 2 Pre-assessment condition: see **[EN 319 403]** , chapter 7.4.5.3: In every case, the document review (stage 1) shall be completed prior to the commencement of audit, stage 2. 

Federal Office for Information Security 

11 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

## **[ETSI TS 119 403-3]** for details. 

## **3.4.1 Identification of Assessment Criteria** 

Each assessment criterion relates to a norm requirement identified by its unique identifier: 

<the 3 letters REQ> - < the clause number> - <2 digit number - incremental> 

Specific criterions are splitted into documentation related (stage 1) and implementation related aspects (stage 2, audit). Normally, stage 2 related criteria base on the results of stage 1 assessment. Some aspects are only relevant for stage 1, like some detailed content of the terms and conditions. Those will **not** be addressed in stage 2. Nevertheless, most aspects from stage 1 need to be mirrored and/or inspected on-site during stage 2. 

Trust Service specific aspects are out of scope of the present document. Nevertheless, for **[ETSI EN 319 401]** assessments, the assessor has **to tune** his or her activities to the specific trust services provided by (Q)TSP. Such an obvious case is a trust service, where no specific ETSI norm or specification is available. Then, the assessor needs to include trust service specific assessment activities in addition to **[ETSI EN 319 401]** . 

Federal Office for Information Security 

12 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

## **4 Structure of Assessment Criteria and Report Template** 

The following figure describes the structure and content of the tables used for assessment criteria as contained in chapter 5 to 7. The tables could be utilised as a template for a reporting of the assessment, as well. For that purpose, the use of a customised spreadsheet is advisable. 


![](markdown/tr/Assessment-Handbuch_ETSI_319_401/Assessment-Handbuch_ETSI_319_401.pdf-0013-03.png)


**Figure 2: Structure of Assessment Criteria and Report Template** 

Notes and auditor guidance may origin from the norm itself or may be additional to that. 

If the text is quoted from norm, the text in the table is set in _slanted_ format. 

The content of the column “Notes/auditor/Guidance” in the Figure 2: "Structure of Assessment Criteria and Report Template” is informative. 

Assessment criteria request assessor activities per each TSP requirement. Usually, the criteria text starts with a standard sentence and is followed by the specific assessor activities (indicated by hyphens “-“), and – in case – further detailed (indicated by plus signs “+” or “+”). 

Example _REQ-6.1-01_ : 

_The assessor shall assess the provided public TSP documents and verify, that_ 

- _the TSP  documented the set of:_ 

- _+ policies_ 

- _+ practices_ 

for the trust services it is providing 

- _the chosen policies and practices are appropriate for the provided trust  services._ 

Federal Office for Information Security 

13 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

## **5 Assessment Criteria for Risk Assessment** 

NOTE: See **ISO/IEC 27005** [i.5] for guidance on information security risk management as part of an information security management system. 

Federal Office for Information Security 

14 

Assessment criteria for TSP Management and Operations 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-5-01_**|_The TSP_**_shall_**_carry out a risk_|<br> <br> <br>|The assessor shall assess the document [TSPS]<br>and verify that the TSP:<br>- stated that the TSP carries out a risk<br>assessment to identify, analyse and evaluate<br>trust service risks taking into account business<br>and technical issues.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  documented the results of a risk assessment,<br>including business and technical aspects.||||
||_assessment to identify, analyse_||||||||
||_and evaluate trust service_||||||||
||_risks taking into account_||||||||
||_business and technical issues._||||||||
||||||||||
|**_REQ-5-02_**|_The TSP_**_shall_**_select the_|<br> <br> <br> <br> <br> <br>|The assessor shall assess the document [TSPS]<br>and verify that the TSP:<br>- stated that the TSP selects appropriate risk<br>treatment measures based on risk assessment<br>results, ensuring a level of security<br>commensurate to the degree of risk.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  implemented the selected risk treatment<br>measures (based on risk assessment results),<br>which are sufficient to reach an acceptable level<br>of security.||||
||_appropriate risk treatment_||||||||
||_measures, taking account of_||||||||
||_the risk assessment results._||||||||
||_The risk treatment measures_||||||||
||_shall ensure that the level of_||||||||
||_security is commensurate to_||||||||
||_the degree of risk._||||||||
|**_REQ-5-03_**|_The TSP_**_shall_**_determine all_||The assessor shall assess the document [TSPS]<br>and verify that the TSP:<br>- determined all security requirements and<br>operational procedures necessary to fully<br>implement its risk treatment measures and<br>the assessor shall check,<br>- that these requirements and procedures are<br>completely documented in the [TSPS] and the<br>information security policy.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- implemented a set of determined security<br>requirements and operational procedures, which<br>are sufficient to implement the chosen risk<br>treatment measures and which are documented in<br>the [IS-Policy] and [TSPS].||||
||_security requirements and_||||||||
||_operational procedures that_||||||||
||_are necessary to implement_||||||||
||_the risk treatment measures_||||||||
||_chosen, as documented in the_||||||||
||_information security policy_||||||||
||_and the trust service practice_||||||||
||_statement (see clause 6)._||||||||
||||||||||
|**_REQ-5-04_**|_The risk assessment shall be_||The assessor shall assess the document [TSPS]<br>and verify that the TSP:<br>- stated that the TSP regularly reviews and<br>revises its risk assessment.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has kept the risk assessment up to date.||||
||_regularly reviewed and_||||||||
||_revised_||||||||
||||||||||



Bundesamt für Sicherheit in der Informationstechnik 

15 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-5-05_**|_The TSP's management shall_||The assessor shall assess the document [TSPS]<br>and verify that the TSP:<br>- stated that the TSP management approves its<br>risk assessment and accepts identified residual<br>risks.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- management approved the risk assessment and<br>accepted the identified residual risks.||||
||_approve the risk assessment_||||||||
||_and accept the residual risk_||||||||
||_identified._||||||||
||||||||||



16 

Federal Office for Information Security 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

## **6 Assessment criteria for Policies and Practices** 

## **6.1 Trust Service Practice Statement** 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-6.1-01_**|_The TSP s_**_hall_**_specify the set_|<br> <br>|The assessor shall assess the provided public<br>TSP documents and verify that<br>- the TSP documented the set of:<br>+ policies,<br>+ practices<br>for the trust services it is providing,<br>- the chosen policies and practices are<br>appropriateforprovided trust services.||not applicable**3**||||
||_of policies and practices_||||||||
||_appropriate for the trust_||||||||
||_services it is providing._||||||||
||||||||||
|**_REQ-6.1-02_**|_The set of policies and_|<br> <br> <br>|REMARK: This requirement is fulfilled, if all<br>derived requirements REQ-6.1-03 to REQ-6.1-<br>11 are fulfilled. No additional stage 1<br>assessment activity is required.||REMARK: This requirement is fulfilled, if all<br>derived requirements REQ-6.1-03 to REQ-6.1-11<br>are fulfilled. No additional stage 2 assessment<br>activity is required.||||
||_practices_**_shall_**_be approved by_||||||||
||_management, published and_||||||||
||_communicated to_||||||||
||_employees_<br>_and_<br>_external_||||||||
||_parties as relevant._||||||||
||||||||||



> 3 Implementation of applied set of policies and practices is assessed through the assessment of all other **[ETSI EN 319 401]** requirements. 

Federal Office for Information Security 

17 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-6.1-03_**|_In particular:_|<br> <br>_NOTE: The_<br>_present document_<br>_makes no_<br>_requirement as to_<br>_the structure of_<br>_the trust service_<br>_practice_<br>_statement._|<br> <br>The assessor shall assess the document [TSPS]<br>and verify that the TSP:<br>-  included its practices and procedures used to<br>address all the requirements identified for the<br>applicable TSP policy,<br>- clarified which policy or policies the TSP<br>follows and what the relations between<br>practices and procedures and the policy or<br>policies are.<br>Remark:The trust service policy contains all<br>(mandatory) rules applicable for the specific<br>Trust Service and defines the nominal<br>conditions. The TSPS describes<br>implementation of the policy, i. e. how the TSP<br>fulfils the TSPpolicy.||not applicable||||
||_The TSP_**_shall_**_have a_||||||||
||_statement of the practices and_||||||||
||_procedures used to address_||||||||
||_all the requirements identified_||||||||
||_for the applicable TSP's_||||||||
||_policy._||||||||
||||||||||
||||||||||
|**_REQ-6.1-04_**|_The TSP's trust service_||The assessor shall assess the document [TSPS]<br>and verify that the TSP:<br>- identified all external organisations<br>supporting the TSP service,<br>- named all obligations applicable to these<br>organisations and<br>- included in those obligations all applicable<br>policies and practices.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- named all external organisations,<br>- identified all obligations of external<br>organisations within contract,<br>- uses the services of these external organisations<br>as described in the trust service practice<br>statement.<br>See also **[ASS 319401, REQ-7.1.1-07].**||||
||_practice statement_**_shall_**||||||||
||_identify the obligations of all_||||||||
||_external organizations_||||||||
||_supporting the TSP's services_||||||||
||_including the applicable_||||||||
||_policies and practices._||||||||
||||||||||



Federal Office for Information Security 

18 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-6.1-05_**|_The TSP_**_shall_**_make available_||The assessor shall assess the document [TSPS]<br>and verify that the TSP:<br>- stated that the TSP<br>+ makes available its [TSPS] to subscribers<br>and relying parties, ++including other<br>documentation, which are necessary to assess<br>conformance to the service policy and<br>++describing how the [TSPS] is made<br>available to subscribers and relying parties.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  published its [TSPS] and related public<br>documents e.g. on its website.<br>The assessor shall verify,<br>-that the [TSPS] and the other information can be<br>retrieved.||||
||_to subscribers and relying_||||||||
||_parties its practice statement,_||||||||
||_and other relevant_||||||||
||_documentation, as necessary_||||||||
||_to assess conformance to the_||||||||
||_service policy._||||||||
||||||||||
|**_REQ-6.1-06_**|_The TSP s_**_hall_**_have a_||The assessor shall assess the document [TSPS]<br>and verify that the TSP:<br>- has a management body with overall<br>responsibility for the TSP and<br>- with final authority for approving the [TSPS].||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- management body has:<br>+ an appointment certificate, appointing overall<br>responsibility and<br>+ final authority for approving the [TSPS],<br>- management bodyapproved the[TSPS].||||
||_management body with_||||||||
||_overall responsibility for the_||||||||
||_TSP with final authority for_||||||||
||_approving the TSP's practice_||||||||
||_statement._||||||||
||||||||||
|**_REQ-6.1-07_**|_The TSP's management_**_shall_**||The assessor shall assess the document [TSPS]<br>and verify that the TSP:<br>- stated that the TSP management implements<br>thepractices.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- fully implemented the [TSPS].||||
||_implement the practices._||||||||
||||||||||
|**_REQ-6.1-08_**|_The TSP_**_shall_**_define a review_||The assessor shall assess the document [TSPS]<br>and verify that the TSP:<br>– stated that the TSP<br>+ defined a review process for the [TSPS] and<br>+ included responsibilities for the [TSPS]<br>maintenance.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- defined a review process for the [TSPS],<br>- assigned personnel for reviewing and<br>maintaining [TSPS],<br>- performed [TSPS] reviews in the past, if<br>applicable.||||
||_process for the practices_||||||||
||_including responsibilities for_||||||||
||_maintaining the TSP's_||||||||
||_practice statement._||||||||
||||||||||
|**_REQ-6.1-09_**|_The TSP_**_shall_**_notify notice of_||The assessor shall assess the document [TSPS]<br>and verify that the TSP:<br>- stated that the TSP will notify its stakeholders<br>(subscribers, relying parties) about intended<br>changes in the[TSPS].||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- notified intended changes of [TSPS], if<br>applicable.||||
||_changes it intends to make in_||||||||
||_its practice statement._||||||||
||||||||||



Federal Office for Information Security 

19 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-6.1-10_**|_The TSP_**_shall_**_, following_||The assessor shall assess the document [TSPS]<br>and verify that the TSP:<br>- stated that the TSP<br>+ will approve changed [TSPS] and<br>+ make the revised [TSPS] immediately<br>available to subscribers and relying parties.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- published newly approved [TSPS], e.g. on its<br>website, if applicable.||||
||_approval as in REQ-6.1-06_||||||||
||_above, make the revised TSP's_||||||||
||_practice statement_||||||||
||_immediately available as_||||||||
||_required under REQ-6.1-05_||||||||
||_above._||||||||
|**_REQ-6.1-11_**|_The TSP_**_shall_**_state in its_||The assessor shall assess the document [TSPS]<br>and verify that the TSP:<br>- stated its provisions made for termination of<br>service.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- provisions made in [TSPS] for termination of<br>service are implemented according7.12.||||
||_practices the provisions made_||||||||
||_for termination of service (see_||||||||
||_clause 7.12)._||||||||
|**6.2**<br>**Terms andConditions**|||||||||
|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-6.2-01_**|_The TSP_**_shall_**_make the terms_||The assessor shall assess the document [T&C]<br>and verify that the TSP:<br>- stated where [T&C] are available to all<br>subscribers and relying parties.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- made available [T&C] related to each trust<br>service policy, e.g. on its website, in the current<br>version(s).||||
||_and conditions regarding its_||||||||
||_services available to all_||||||||
||_subscribers and relying_||||||||
||_parties._||||||||
|**_REQ-6.2-02_**|_The terms and conditions_**_shall_**|<br>|REMARK: This requirement is fulfilled, if all<br>derived requirements REQ-6.2-02, a) to REQ-<br>6.2-02, k) are fulfilled. No additional stage 1<br>assessment activityis required.||REMARK: This requirement is fulfilled, if all<br>derived requirements REQ-6.2-02, a) to REQ-<br>6.2-02, k) are fulfilled. No additional stage 2<br>assessment activityis required.||||
||_at least specify for each trust_||||||||
||_service policy supported by the_||||||||
||_TSP thefollowing:_||||||||
|**_REQ-6.2-02, a)_**|_the trust service policy being_||The assessor shall assess the document [T&C]<br>and verify that the TSP:<br>- named the applied trust servicepolicy.||not applicable||||
||_applied;_||||||||
||||||||||



## **6.2 Terms and Conditions** 

Federal Office for Information Security 

20 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-6.2-02, b_**_)_|_any limitations on the use of_|_EXAMPLE 1:_<br>_The expected_<br>_life-time of_<br>_public key_<br>_certificates._|The assessor shall assess the document [T&C]<br>and verify that the TSP:<br>- included any limitations on the use of the<br>service.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- implementation of trust services matches the<br>limitations on the use of trust service given in<br>[T&C]||||
||_the service provided including_||||||||
||_the limitation for damages_||||||||
||_arising from the_||||||||
||_use of services exceeding such_||||||||
||_limitations;_||||||||
|**_REQ-6.2-02, c)_**|_the subscriber's obligations, if_||The assessor shall assess the document [T&C]<br>and verify that the TSP:<br>- included subscriber's obligations, if<br>applicable||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>– implemented  the subscriber obligations,<br>included in [T&C], which are sufficient from a<br>security point of view.||||
||_any;_||||||||
||||||||||
|**_REQ-6.2-02, d_**_)_|_information for parties relying_|_EXAMPLE 2:_<br>_How to verify_<br>_the trust service_<br>_token, any_<br>_possible_<br>_limitations on_<br>_the validity_<br>_period_<br>_associated with_<br>_the trust service_<br>_token._|The assessor shall assess the document [T&C]<br>and verify that the TSP:<br>- included information for parties relying on<br>the trust service||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- implementation of trust services matches the<br>information for parties relying on the trust<br>service given in [T&C].||||
||_on the trust service;_||||||||
||||||||||
|**_REQ-6.2-02, e)_**|_the period of time during_||The assessor shall assess the document [T&C]<br>and verify that the TSP:<br>- stated the period of time during which TSP<br>event logs are retained.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- retains TSP event logs for the period of time<br>given in[T&C].||||
||_which TSP's event logs are_||||||||
||_retained;_||||||||
||||||||||
|**_REQ-6.2-02, f)_**|_limitations of liability;_||The assessor shall assess the document [T&C]<br>and verify that the TSP:<br>- stated the limitations of liability.||not applicable||||
||||||||||
|**_REQ-6.2-02, g)_**|_the applicable legal system;_||The assessor shall assess the document [T&C]<br>and verify that the TSP:<br>- referred the applicable legal system.||not applicable||||
||||||||||
||||||||||



Federal Office for Information Security 

21 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|---|
||||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||||||||||
|**_REQ-6.2-02, h)_**|_procedures for complaints and_|||The assessor shall assess the document [T&C]<br>and verify that the TSP:<br>- included procedures for complaints and<br>dispute settlement.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- implemented its procedures for complaints and<br>dispute settlement.||||
||_dispute settlement;_|||||||||
|||||||||||
|**_REQ-6.2-02, i)_**|_whether the TSP's trust service_|||The assessor shall assess the document [T&C]<br>and verify that the TSP:<br>- has a conformance statement.||not applicable||||
||_has been assessed to be_|||||||||
||_conformant with the trust_|||||||||
||_service policy, and if so_|||||||||
||_through which conformity_|||||||||
||_assessment scheme;_|||||||||
|**_REQ-6.2-02, j)_**|_the TSP's contact information;_|||The assessor shall assess the document [T&C]<br>and verify that the TSP:<br>-gave contact information.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- contact information in[T&C]is correct||||
||_and_|||||||||
|||||||||||
|**_REQ-6.2-02, k_**_)_|_any undertaking regarding_|||The assessor shall assess the document [T&C]<br>and verify that the TSP:<br>- stated the availability of TSP services||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- implemented means to assure availability of<br>TSP service according [T&C]||||
||_availability._|||||||||
|||||||||||
|**_REQ-6.2-03_**|_Subscribers and parties_|||The assessor shall assess the TSP public<br>available resources for gathering precise terms<br>and conditions applicable to subscribers and<br>relying parties. Also the assessor may assess<br>whether [T&C] are available beforehand<br>contracting.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- implemented means to assure the availability of<br>information of precise terms and conditions for<br>the subscribers and relying partiesbefore<br>entering in a contractual relationship||||
||_relying on the trust service_|||||||||
||**_shall_**_be informed of precise_|||||||||
||_terms and conditions,_|||||||||
||_including the items listed_|||||||||
||<br>_above,  _|<br>_before entering into a_||||||||
||<br>_contractual relationship._|||||||||
|**_REQ-6.2-04_**|_Terms and conditions_**_shall_**_be_|||The assessor shall assess the TSP public<br>available resources<br>whether [T&C] are available through a<br>durable means of communication.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- made [T&C] available through a durable means<br>of communication.<br>The assessor shall verify,<br>-that the [T&C] can be retrieved through a<br>durable means of communication.||||
||_made available through a_|||||||||
||_durable means of_|||||||||
||_communication._|||||||||
|||||||||||



Federal Office for Information Security 

22 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-6.2-05_**|_Terms and conditions_**_shall_**_be_||The assessor shall assess the document [T&C]<br>and verify that the TSP:<br>- uses in [T&C] a for contractual partners (i.e.<br>subscriber)readilyunderstandable language||not applicable||||
||_available in a readily_||||||||
||_understandable language._||||||||
||||||||||
|**_REQ-6.2-06_**|_Terms and conditions_**_may_**_be_||No assessment activity is required.||No assessment activity is required.||||
||_transmitted electronically._||||||||
|**6.3**<br>**InformationSecurity Policy**|||||||||
|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-6.3-01_**|_The TSP_**_shall_**_define an_|_NOTE 1: See_<br>_clause 5.1.1 of_<br>**_ISO/IEC_**<br>**_27002:2013_**<br>_[i.3] for_<br>_guidance._|The assessor shall assess the document [TSPS]<br>and verify that the TSP:<br>- stated the existence of a management<br>approved [IS-Policy], defining the TSPs<br>approach to manage information security.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- management approves [IS-Policy],<br>- information security management is in<br>accordance with [IS-Policy].||||
||_information security policy_||||||||
||_which is approved by_||||||||
||_management and which sets_||||||||
||_out the organization's_||||||||
||_approach to managing its_||||||||
||_information security._||||||||
|**_REQ-6.3-02_**|_Changes to the information_||The assessor shall assess the document [TSPS]<br>and verify that the TSP:<br>- stated that changes of the [IS-Policy] will be<br>communicated to subscribers, relying parties,<br>assessment bodies, supervisory or other<br>regulatory bodies.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  communicates changes of [IS-Policy], e.g. on<br>its website, if applicable.||||
||_security policy_**_shall_**_be_||||||||
||_communicated to third parties,_||||||||
||_where applicable. This_||||||||
||_includes subscribers, relying_||||||||
||_parties, assessment bodies,_||||||||
||_supervisory or other_||||||||
||_regulatory bodies._||||||||
||_Inparticular:_||||||||



Federal Office for Information Security 

23 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-6.3-03_**|_A TSP's information security_||The assessor shall assess the document [IS-<br>Policy] and verify that the TSP:<br>- stated that the security controls and operating<br>procedures for TSP facilities, systems and<br>information assets providing the service are<br>documented, implemented and maintained.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  implemented and maintains the security<br>controls and operating procedures for TSP<br>facilities, systems and information assets<br>providing the service as stated in the [IS-Policy],<br>-  communicates the [IS-Policy] to all impacted<br>employees.||||
||_policy_**_shall_**_be  documented,_||||||||
||_implemented and maintained_||||||||
||_including the security controls_||||||||
||_and operating procedures for_||||||||
||_TSP's facilities, systems and_||||||||
||_information assets providing_||||||||
||_the services._||||||||
|**_REQ-6.3-04_**|_The TSP_**_shall_**_publish and_|_NOTE 1: See_<br>_clause 5.1.1 of_<br>**_ISO/IEC_**<br>**_27002:2013_**<br>_[i.3] for_<br>_guidance._|not applicable||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  communicates the [IS-Policy] to all impacted<br>employees.||||
||_communicate the information_||||||||
||_security policy to all_||||||||
||_employees who are impacted_||||||||
||_by it._||||||||
||||||||||
|**_REQ-6.3-05_**|_The TSP_**_shall_**_retain overall_|<br>|The assessor shall assess the document [IS-<br>Policy] and verify that the TSP:<br>- stated that overall responsibility for<br>conformance with the procedures prescribed in<br>its [IS-Policy], even when the TSP<br>functionality is outsourced, is retained by the<br>TSP,<br>- defined the outsourcer’s liability.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  included in its contracts with outsourcers that<br>overall responsibility for conformance with the<br>procedures of [IS-Policy] is retained by the TSP.||||
||_responsibility for conformance_||||||||
||_with the procedures prescribed_||||||||
||_in its information security_||||||||
||_policy, even when the TSP's_||||||||
||_functionality is undertaken by_||||||||
||_outsourcers._||||||||
||||||||||
|**_REQ-6.3-06_**|_TSP_**_shall_**_define the_||The assessor shall assess the document [IS-<br>Policy] and verify that the TSP:<br>- defined the outsourcers’ liability.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- contractually agreed outsourcer liabilities,<br>-  contractually agreed with the outsourcers that<br>the outsourcers implement any controls required<br>bythe TSP.||||
||_outsourcers' liability and_||||||||
||_ensure that outsourcer are_||||||||
||_bound to implement any_||||||||
||_controls required by the TSP._||||||||
||||||||||



Federal Office for Information Security 

24 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-6.3-07_**|_The TSP's information security_||The assessor shall assess the document [IS-<br>Policy] and verify that the TSP:<br>- stated that<br>+the [IS-Policy] and the inventory of assets for<br>information security at planned intervals or in<br>case of significant changes are regularly<br>reviewed and<br>+ the TSP system configurations for changes<br>violating the security policies are regularly<br>checked.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has regularly reviewed its [IS-Policy],<br>- has kept its [IS-Policy] up to date, ensuring<br>continuing suitability, adequacy and<br>effectiveness,<br>- has management approval of [IS-Policy], if<br>changes impact on the level of security provided,<br>- has regularly checked TSP system<br>configurations for changes violating the security<br>policies.|<br>|||
||_policy and inventory of assets_||||||||
||_for information security (see_||||||||
||_clause 7.3)_**_shall_**_be reviewed_||||||||
||_at planned intervals or if_||||||||
||_significant changes occur to_||||||||
||_ensure their continuing_||||||||
||_suitability, adequacy and_||||||||
||_effectiveness._||||||||
||||||||||
|**_REQ-6.3-08_**|_Any changes that will impact_||not applicable||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has management approval of [IS-Policy], if<br>changes impact on the level of security provided.||||
||_on the level of security_||||||||
||_provided_**_shall_**_be approved by_||||||||
||_the management body referred_||||||||
||_to in REQ-6.1-07._||||||||
|**_REQ-6.3-09_**|_The configuration of the TSPs_||The assessor shall assess the document [IS-<br>Policy] and verify that the TSP:<br>- stated that the TSP regularly checks TSP<br>system configurations for changes violating the<br>security policies.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has regularly checked TSP system<br>configurations for changes violating the security<br>policies.||||
||_systems_**_shall_**_be regularly_||||||||
||_checked for changes which_||||||||
||_violate the TSPs security_||||||||
||_policies._||||||||
||||||||||
|**_REQ-6.3-10_**|_The maximum interval_|<br>_NOTE 2:_<br>_Further specific_<br>_recommendation_<br>_s are given in_<br>_the CA/Browser_<br>_Forum network_<br>_security guide_<br>_[i.7],_<br>_item 1._|The assessor shall assess the document [TSPS]<br>and verify that the TSP:<br>- stated the maximum interval between two<br>checks of the TSP system configurations<br>violating the security policies.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has _not_ exceeded in the past the maximum<br>interval between two checks of the TSP system<br>configurations violating the security policies, as<br>specified by [TSPS].||||
||_between two checks_**_shall_**_be_||||||||
||_documented in the trust service_||||||||
||_practice_||||||||
||_statement._||||||||
||||||||||



25 

Federal Office for Information Security 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

## **7 Assessment criteria for TSP Management and Operations** 

## **7.1 Internal organization** 

## **7.1.1 Organization reliability** 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-7.1.1-01_**|_The TSP organization_**_shall_**||REMARK: This requirement is fulfilled, if all<br>derived requirements REQ-7.1.1-02 to REQ-<br>7.1.1-07 are fulfilled. No additional stage 1<br>assessment activityis required.||REMARK: This requirement is fulfilled, if all<br>derived requirements REQ-7.1.1-02 to REQ-<br>7.1.1-07 are fulfilled. No additional stage 2<br>assessment activityis required.||||
||_be reliable._||||||||
||_In particular:_||||||||
||||||||||



26 

Federal Office for Information Security 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-7.1.1-02_**|_Trust service practices under_|NOTE: See<br>following EU<br>directives:<br>-**[Directive**<br>**2000/43/EC]**<br>against<br>discrimination<br>on grounds of<br>race and ethnic<br>origin.<br>-**[Directive**<br>**2004/113/EC]**<br>equal treatment<br>for men and<br>women in the<br>access to and<br>supply of goods<br>and services.<br>-**[Directive**<br>**Proposal**<br>**(COM(2008)46**<br>**2)]**against<br>discrimination<br>based on age,<br>disability, sexual<br>orientation and<br>religion or belief<br>beyond the<br>workplace.|<br> <br>The assessor shall assess the document [TSPS]<br>and verify that the TSP:<br>- has only non-discriminatory trust service<br>practices.||not applicable||||
||_which the TSP operates_**_shall_**||||||||
||_be non-discriminatory._||||||||
||||||||||



Federal Office for Information Security 

27 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-7.1.1-03_**|_The TSP_**_should_**_make its_||The assessor shall assess the document [TSPS]<br>and verif, that the TSP:<br>- stated that the TSP makes its services<br>accessible, if an applicant falls within the<br>declared field of operation and agrees to fulfil<br>the obligations as stated in [T&C].||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- makes its services accessible, if an applicant<br>falls within the declared field of operation and<br>agrees to fulfil the obligations as stated in [T&C]||||
||_services accessible to all_||||||||
||_applicants whose activities_||||||||
||_fall within its declared field_||||||||
||_of operation and that agree_||||||||
||_to abide by their obligations_||||||||
||_as specified in the TSP's_||||||||
||_terms and conditions._||||||||
|**_REQ-7.1.1-04_**|_The TSP_**_shall_**_maintain_|_NOTE:_<br>_- For liability of_<br>_TSPs operating_<br>_in EU, see_<br>_article 13 of the_<br>_Regulation (EU)_<br>_No 910/2014_<br>_[i.2]._<br>- As a member<br>state example,<br>see § 10 of<br>German Trust<br>Service Act<br>**[VDG]**<br>**(German:**<br>Vertrauensdienst<br>egesetz).|<br>The assessor shall assess the document [TSPS]<br>and verify that the TSP:<br>- stated that the TSP maintains sufficient<br>financial resources and/or obtain appropriate<br>liability insurance, in accordance with national<br>law, to cover liabilities arising from its<br>operations and/or activities.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  documented evidence of appropriate liability<br>insurance and<br>- maintains sufficient financial resources.||||
||_sufficient financial resources_||||||||
||_and/or obtain appropriate_||||||||
||_liability insurance, in_||||||||
||_accordance with applicable_||||||||
||_law, to cover liabilities_||||||||
||_arising from its operations_||||||||
||_and/or activities._||||||||
||||||||||
|**_REQ-7.1.1-05_**|_The TSP_**_shall_**_have the_||The assessor shall assess the document [TSPS]<br>and verify that the TSP:<br>- stated his financial stability and that operation<br>of required resources conforms to his "policy".||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has the necessary financial means to operate the<br>trust services in conformity with its policy,<br>- presents evidence, which could be (the yearly)<br>financial statement.||||
||_financial stability and_||||||||
||_resources required to operate_||||||||
||_in conformity with this policy._||||||||
||||||||||



Federal Office for Information Security 

28 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-7.1.1-06_**|_The TSP_**_shall_**_have policies_||The assessor shall assess the documents<br>[TSPS] and [TSPolicy] and verify that the TSP:<br>- has policies and procedures for the resolution<br>of complaints and disputes received from<br>customers or other relying parties about the<br>provisioning of the services or any other<br>related matters.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- implemented an effective and timely complaint<br>management.||||
||_and procedures for the_||||||||
||_resolution of complaints and_||||||||
||_disputes received from_||||||||
||_customers or other relying_||||||||
||_parties about the_||||||||
||_provisioning of the services_||||||||
||_or any other related matters._||||||||
|**_REQ-7.1.1-07_**|_The TSP_**_shall_**_have a_||The assessor shall assess the documents<br>[TSPS] and [TSPolicy] and verify that the TSP:<br>- has a documented agreement and contractual<br>relationship in place where the provisioning of<br>services involves subcontracting, outsourcing<br>or other third party arrangements.<br>See also **[ASS 319401, REQ-6.1-04].**||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  documented agreement and contractual<br>relationship in place toallparties involved in the<br>provisioning of services.<br>See also**[ASS 319401, REQ-6.1-04].**||||
||_documented agreement and_||||||||
||_contractual relationship in_||||||||
||_place where the provisioning_||||||||
||<br>_of services involves_||||||||
||_subcontracting, outsourcing_||||||||
||_or other third party_||||||||
||_arrangements._||||||||



Federal Office for Information Security 

29 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**7.1.2**<br>**Segregation of duties**|**7.1.2**<br>**Segregation of duties**||||||||
|---|---|---|---|---|---|---|---|---|
|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
|**_REQ-7.1.2-01_**|_Conflicting duties and areas_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP has segregated conflicting<br>duties and areas of responsibilities and with<br>that<br>- reduced opportunities for unauthorized or<br>unintentional modification or misuse of the<br>TSP assets.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  effectively implemented the segregation of<br>conflicting duties and areas of responsibilities.||||
||_of responsibility_**_shall_**_be_||||||||
||_segregated to reduce_||||||||
||_opportunities for_||||||||
||_unauthorized or_||||||||
||_unintentional modification or_||||||||
||_misuse of the TSP's assets._||||||||
||||||||||
|**7.2**<br>**Human resources**|||||||||
|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage_**<br>**_1_**|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
|**_REQ-7.2-01_**|_The TSP_**_shall_**_ensure that_|<br>_NOTE 1: See_<br>_clauses 6.1.1_<br>_and 7 of_<br>**_ISO/IEC_**<br>**_27002:2013_**<br>_[i.3] for_<br>_guidance._|REMARK: This requirement is fulfilled, if all<br>derived requirements REQ-7.2-02 to REQ-7.2-<br>17 are fulfilled. No additional stage 1<br>assessment activity is required.||REMARK: This requirement is fulfilled, if all<br>derived requirements REQ-7.2-02 to REQ-7.2-17<br>are fulfilled. No additional stage 2 assessment<br>activity is required.||||
||_employees and contractors_||||||||
||_support the trustworthiness of_||||||||
||_the TSP's operations._||||||||
||_In particular:_||||||||
||||||||||
||||||||||



Federal Office for Information Security 

30 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**<br>|**_Verdict Stage_**<br>~~**_1_**~~|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
|**_REQ-7.2-02_**|_The TSP_**_shall_**_employ staff_||The assessor shall assess the document [TSPS]<br>and verify that the TSP:<br>- stated that the TSP only employs staff (and<br>subcontractors)<br>+ with necessary expertise, reliability,<br>experience, and qualifications related to the<br>supported business processes, information<br>security (and its management) as well as data<br>privacy and document control,<br>+ who are trained regarding security and<br>personal data protection rules<br>as appropriate for the offered services and the<br>job function||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has appointed only qualified, well trained<br>personnel in the specific trusted roles for the<br>provided services including information security<br>and personal data protection requirements.||||
||_and, if applicable,_||||||||
||_subcontractors, who possess_||||||||
||_the necessary expertise,_||||||||
||_reliability, experience, and_||||||||
||_qualifications and who have_||||||||
||_received training regarding_||||||||
||_security and personal data_||||||||
||_protection rules as_||||||||
||_appropriate for the offered_||||||||
||_services and the job function._||||||||
||||||||||
|**_REQ-7.2-03_**|_TSP personnel_**_should_**_be_||The assessor shall assess the document [TSPS]<br>and verify that the TSP:<br>- stated that the TSP has minimum<br>requirements regarding formal training and/or<br>experience for its TSP personnel,<br>- assures at least yearly update trainings on<br>new threats and current security practices.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has assured sufficient formal training and/or<br>experience of its TSP personnel,<br>- has necessary evidences of trainings and/or<br>experience.||||
||_able to fulfil the requirement_||||||||
||_of "expert knowledge,_||||||||
||_experience and_||||||||
||_qualifications" through_||||||||
||_formal training and_||||||||
||_credentials, or actual_||||||||
||_experience, or a combination_||||||||
||_of the two._||||||||



Federal Office for Information Security 

31 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**<br>|**_Verdict Stage_**<br>~~**_1_**~~|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
|**_REQ-7.2-04_**|_This_**_should_**_include regular_|_NOTE 2:_<br>_Personnel_<br>_employed by a_<br>_TSP include_<br>_individual_<br>_personnel_<br>_contractually_<br>_engaged in_<br>_performing_<br>_functions_<br>_in support of the_<br>_TSP's services._<br>_Personnel who_<br>_can be involved_<br>_in monitoring_<br>_the TSP's_<br>_services need_<br>_not_<br>_be TSP's_<br>_personnel._|<br>The assessor shall assess the document [TSPS]<br>and verify that the TSP:<br>- stated that the TSP assures at least yearly<br>update trainings on new threats and current<br>security practices.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has assured sufficient formal training and/or<br>experience of its TSP personnel,<br>- has evidences of yearly update trainings on new<br>threats and current security practices for its TSP<br>personnel.||||
||_(at least every 12 months)_||||||||
||_updates on new threats and_||||||||
||_current security practices._||||||||
||||||||||
|**_REQ-7.2-05_**|_Appropriate disciplinary_|_NOTE 3: See_<br>_clause 7.2.3 of_<br>**_ISO/IEC_**<br>**_27002:2013_**<br>_[i.3] for_<br>_guidance._|The assessor shall assess the document [TSPS]<br>and verify that the TSP:<br>- stated that the TSP has appropriate<br>disciplinary sanctions applied to personnel<br>violating TSP policies or procedures.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  effectively implemented appropriate<br>disciplinary sanctions applied to personnel<br>violating TSP policies or procedures<br>- has evidence of existing cases of TSP policy or<br>procedure violations,– if any–.||||
||_sanctions_**_shall_**_be applied to_||||||||
||_personnel violating TSP's_||||||||
||_policies or procedures._||||||||
||||||||||



Federal Office for Information Security 

32 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**<br>|**_Verdict Stage_**<br>~~**_1_**~~|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
|**_REQ-7.2-06_**|_Security roles and_|_._|The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- documented defined security roles and<br>responsibilities from [IS-Policy] in<br>job descriptions (or equivalent) and makes<br>them internally available to related personnel.||not applicable||||
||_responsibilities, as specified_||||||||
||_in the TSP's information_||||||||
||_security policy,_**_shall_**_be_||||||||
||_documented in job_||||||||
||_descriptions or in documents_||||||||
||_available to all concerned_||||||||
||_personnel._||||||||
|**_REQ-7.2-07_**|_Trusted roles, on which the_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- clearly identifies its trusted roles on which the<br>securityof the TSP operation relies||not applicable||||
||_security of the TSP's_||||||||
||_operation is dependent,_**_shall_**||||||||
||_be clearly identified._||||||||
||||||||||
|**_REQ-7.2-08_**|_Trusted roles_**_shall_**_be named_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP management clearly<br>named to person its trusted roles on which the<br>securityof the TSP operation relies||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has evidence, showing that personnel trusted<br>roles were named by management||||
||_by the management._||||||||
||||||||||
|**_REQ-7.2-09_**|_Trusted roles_**_shall_**_be_|_NOTE 4: See_<br>_clause 7.2.1 of_<br>**_ISO/IEC_**<br>**_27002:2013_**<br>_[i.3] for further_<br>_guidance on_<br>_management_<br>_responsibilities_<br>_in establishing_<br>_roles and_<br>_responsibilities._|The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- assures acceptance of trusted roles by both,<br>management and person responsible to fulfil||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has evidence, showing named personnel and<br>management have accepted trusted roles and<br>responsibilities||||
||_accepted by the management_||||||||
||_and the person to fulfil the_||||||||
||_role._||||||||
||||||||||



Federal Office for Information Security 

33 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**<br>|**_Verdict Stage_**<br>~~**_1_**~~|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
|**_REQ-7.2-10_**|_TSP's personnel (both_|<br> <br>_._|The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- has job descriptions of TSP personnel<br>(temporary and permanent), which are<br>conformant to the [IS-Policy]:<br>+ following principles of 'segregation of duties'<br>and 'least privilege' and<br>+ matching position sensitivity with duties,<br>access levels, background screening, training<br>and awareness.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  documented for each person involved in TSP<br>functions a job description appointed toand<br>agreed by the person (temporary or permanent<br>worker),<br>-  specified necessary position requirements,<br>considering experience, expertise, skills, training<br>and awareness,<br>-  specified the position tasks, responsibilities<br>and duties as well as privileges and access levels<br>conformant with the TSPs role concept||||
||_temporary and permanent)_||||||||
||**_shall_**_have job descriptions_||||||||
||_defined from the view point of_||||||||
||<br>_roles fulfilled with_||||||||
||_segregation of duties and_||||||||
||_least privilege (see clause_||||||||
||_7.1.2), determining position_||||||||
||_sensitivity based on the duties_||||||||
||_and access levels,_||||||||
||_background screening and_||||||||
||_employee training and_||||||||
||_awareness._||||||||
|**_REQ-7.2-11_**|_Where appropriate, job_|_NOTE 5: See_<br>_clause 7.2.1 of_<br>**_ISO/IEC_**<br>**_27002:2013_**<br>_[i.3] for further_<br>_guidance on_<br>_management_<br>_responsibilities_<br>_in establishing_<br>_roles and_<br>_responsibilities._|The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- has job descriptions of TSP personnel<br>(temporary and permanent), which are<br>separating general functions from TSP’s<br>specific functions added by skills and<br>experience requirements||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has documented evidences, that each person<br>(temporary or permanent, with either general or<br>TSP’s special functions) fulfils his or her<br>position skills and experience requirements||||
||_descriptions_**_shall_**||||||||
||_differentiate between general_||||||||
||_functions and TSP's specific_||||||||
||_functions. These should_||||||||
||_include skills and experience_||||||||
||_requirements._||||||||
||||||||||



Federal Office for Information Security 

34 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**<br>|**_Verdict Stage_**<br>~~**_1_**~~|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
|**_REQ-7.2-12_**|_Personnel_**_shall_**_exercise_|<br>_NOTE 6: See_<br>_clause 7.2.1 of_<br>**_ISO/IEC_**<br>**_27002:2013_**<br>_[i.3] for further_<br>_guidance on_<br>_management_<br>_responsibilities_<br>_in establishing_<br>_roles and_<br>_responsibilities._|The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>-  designed its administrative and management<br>procedures and processes in line with the TSP's<br>information security management procedures.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has documented evidence showing that its<br>personnel exercises administrative and<br>management procedures as specified are in line<br>with the TSP's information security management<br>procedures.||||
||_administrative and_||||||||
||_management procedures and_||||||||
||_processes that are in line with_||||||||
||_the TSP's information_||||||||
||_security  management_||||||||
||_procedures._||||||||
||||||||||
|**_REQ-7.2-13_**|_Managerial personnel_**_shall_**||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the managerial personnel of the TSP:<br>- has sufficient experience or training related to<br>provided trust services,<br>- is familiar with security procedures for<br>personnel with security responsibilities,<br>- has sufficient experienced with information<br>security and risk assessment.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has documented evidence showing its<br>managerial personnel is capable to carry out<br>management functions by fulfilling defined job<br>prerequisites.||||
||_possess experience or_||||||||
||_training with respect to the_||||||||
||_trust service that is provided,_||||||||
||_familiarity with security_||||||||
||_procedures for personnel_||||||||
||_with security responsibilities_||||||||
||_and experience with_||||||||
||_information security and risk_||||||||
||_assessment sufficient to carry_||||||||
||_out managementfunctions._||||||||
|**_REQ-7.2-14_**|_All TSP's personnel in trusted_|<br>_NOTE 7: See_<br>_clause 6.1.2 of_<br>**_ISO/IEC_**<br>**_27002:2013_**<br>_[i.3] for_<br>_guidance._|The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- assigns only TSP personnel to trusted roles, if<br>they are free from conflict of interest regarding<br>impartialityof TSP operations.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has effective means assuring freedom from<br>conflict of interest of its TSP personnel in trusted<br>roles.||||
||_roles_**_shall_**_be free from_||||||||
||_conflict of interest that might_||||||||
||_prejudice the impartiality of_||||||||
||_the TSP's operations._||||||||
||||||||||



35 

Federal Office for Information Security 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**<br>|**_Verdict Stage_**<br>~~**_1_**~~|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
|**_REQ-7.2-15_**|_Trusted roles_**_shall i_**_nclude_|<br> <br> <br>_NOTE 8: This_<br>{REMARK:<br>system<br>administrators’<br>responsibilitiy}<br>_includes_<br>_recovery of the_<br>_system._<br>_NOTE 9:_<br>_Additional_<br>_application_<br>_specific roles_<br>_can be required_<br>_for particular_<br>_trust services._|The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- documented that the trusted roles include the<br>following (with responsibilities:<br>+ Security Officers (administer the<br>implementation of the security practices),<br>+ System Administrators (install, configure,<br>maintain and recover TSP trustworthy<br>systems),<br>+ System Operators (operate the TSP<br>trustworthy systems and perform system<br>backups of it),<br>+ System Auditors (view archives and audit<br>logs of the TSP trustworthy systems)||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has documented evidence, that following<br>trusted roles are assigned to TSP personnel<br>+ Security Officers,<br>+ System Administrators,<br>+ System Operators,<br>+ System Auditors,<br>-  equipped assigned personnel with authority to<br>fulfil their responsibilities.||||
||_roles that involve the_||||||||
||_following responsibilities:_||||||||
||_a) Security Officers: Overall_||||||||
||_responsibility for_||||||||
||_administering the_||||||||
||_implementation of the_||||||||
||_security practices._||||||||
||_b) System Administrators:_||||||||
||_Authorized to install,_||||||||
||_configure and maintain the_||||||||
||_TSP's trustworthy systems for_||||||||
||_service management._||||||||
||_c) System Operators:_||||||||
||_Responsible for operating the_||||||||
||_TSP's trustworthy systems on_||||||||
||_a day-to-day basis._||||||||
||_Authorized to perform system_||||||||
||_backup._||||||||
||_d) System Auditors:_||||||||
||_Authorized to view archives_||||||||
||_and audit logs of the TSP's_||||||||
||_trustworthy systems._||||||||
|**_REQ-7.2-16_**|_TSP's personnel_**_shall_**_be_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- documented that<br>+senior management responsible for security<br>formally appoints TSP personnel to trusted<br>roles<br>- applies the principle of 'least privilege' when<br>accessingor configuringaccessprivileges.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has documented evidence, that senior<br>management responsible for security has<br>formally appointed all TSP personnel to their<br>trusted roles,<br>- enforces the principle of 'least privilege' when<br>accessing or configuring access privileges.||||
||_formally appointed to trusted_||||||||
||_roles by senior management_||||||||
||_responsible for security_||||||||
||_requiring the principle of_||||||||
||_"least privilege" when_||||||||
||_accessing or when_||||||||
||_configuring access privileges._||||||||
||||||||||



36 

Federal Office for Information Security 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage_**<br>~~**_1_**~~|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
|**_REQ-7.2-17_**|_Personnel_**_shall_**_not have_|_NOTE 10: In_<br>_some countries_<br>_it is not possible_<br>_for TSP to_<br>_obtain_<br>_information on_<br>_past convictions_<br>_without the_<br>_collaboration of_<br>_the candidate_<br>_employee._|The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP doesnotallow personnel<br>to access trusted function before all necessary<br>checks are positively completed, i.e. passed.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- effectively protects trusted functions from<br>access of personnelnothaving successfully<br>completed all necessary checks,<br>- denies personnel to have access to trusted<br>functions, if one or more of all necessary checks<br>failed.||||
||_access to the trusted_||||||||
||_functions until the necessary_||||||||
||_checks are completed._||||||||
||||||||||



## **7.3 Asset management** 

## **7.3.1 General requirements** 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-7.3.1-01_**|_The TSP_**_shall_**_ensure an_|_NOTE 1: See_<br>_clause 8 of_<br>**_ISO/IEC_**<br>**_27002:2013_**<br>_[i.3] for_<br>_guidance._|The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP appropriately protects its<br>assets by applying security requirements and<br>operational procedures in-line with risk<br>treatment measures.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  implemented security requirements and<br>operational procedures to appropriately protects<br>its assets.||||
||_appropriate level of_||||||||
||_protection of its assets_||||||||
||_including information assets._||||||||
||_In particular:_||||||||
||||||||||



Federal Office for Information Security 

37 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-7.3.1-02_**|_The TSP_**_shall_**_maintain an_|_NOTE 2: See_<br>_clause 8.1.1 of_<br>**_ISO/IEC_**<br>**_27002:2013_**<br>_[i.3] for_<br>_guidance._|The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ maintains an inventory of all information<br>assets<br>+ classifies these information assets<br>conformant with the results from risk<br>assessment.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  identified and correctly classifiedallrelevant<br>assets,<br>- has its information asset inventory up-to-date,<br>- uses a classification scheme conformant to the<br>risk assessment results.||||
||_inventory of all information_||||||||
||_assets and shall assign a_||||||||
||<br>_classification consistent with_||||||||
||_the risk assessment._||||||||
||||||||||
|**7.3.2**<br>**Media handling**|||||||||
|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
|**_REQ-7.3.2-01_**|_All media_**_shall_**_be handled_|_NOTE 3: See_<br>_clause 8.3 of_<br>**_ISO/IEC_**<br>**_27002:2013_**<br>_[i.3] for_<br>_guidance._|The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ has procedures for secure handling of any<br>(data storage) media in place conformant with<br>the information classification scheme<br>requirements,<br>+ assures secure media disposal after need, if<br>containingsensitive data.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  trained its TSP personnel regarding secure<br>handling of (all different types of) classified<br>media,<br>-  effective means to dispose media containing<br>sensitive data.||||
||_securely in accordance with_||||||||
||_requirements of the_||||||||
||_information classification_||||||||
||_scheme. Media containing_||||||||
||_sensitive data shall be_||||||||
||_securely disposed of when no_||||||||
||_longer required._||||||||
||||||||||



## **7.3.2 Media handling** 

## **7.4 Access control** 

## _NOTE: See clause 8 of_ _**ISO/IEC 27002:2013** [i.3] for guidance._ 

Federal Office for Information Security 

38 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**<br>|**_Verdict Stage_**<br>~~**_1_**~~|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
|**_REQ-7.4-01_**|_The TSP's system access_||REMARK: This requirement is fulfilled, if all<br>derived requirements REQ-7.4-02 to REQ-7.4-<br>10 are fulfilled. No additional stage 1<br>assessment activityis required.||REMARK: This requirement is fulfilled, if all<br>derived requirements REQ-7.4-02 to REQ-7.4-10<br>are fulfilled. No additional stage 2 assessment<br>activityis required.||||
||**_shall_**_be limited to authorized_||||||||
||_individuals._||||||||
||_Inparticular:_||||||||
|**_REQ-7.4-02_**|_Controls (e.g. firewalls)_**_shall_**||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP uses controls like firewalls<br>to protect the TSP internal network domains<br>from unauthorised access also by subscribers<br>and thirdparties.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- enforces access control via e.g. by firewalls in<br>order to protect its internal network domains on a<br>need to have basis,<br>- applies a hardening concept to its network<br>components.||||
||_protect the TSP's internal_||||||||
||_network domains from_||||||||
||_unauthorized access_||||||||
||_including access by_||||||||
||_subscribers and third parties._||||||||
||||||||||
|**_REQ-7.4-03_**|_Firewalls_**_should_**_also be_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP’s firewalls block<br>unnecessary protocols and accesses.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has implemented firewall rules allowingonly<br>necessary protocols and accesses.||||
||_configured to prevent all_||||||||
||_protocols and accesses not_||||||||
||<br>_required for the operation of_||||||||
||_the TSP._||||||||
|**_REQ-7.4-04_**|_The TSP_**_shall_**_administer_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP administers user access of<br>following trusted roles: operators,<br>administrators and system auditors.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has documented evidence thatonlynecessary<br>user accounts are set-up and are based on the<br>TSP role concept,<br>- segregates duties for the following trusted roles:<br>operators, administrators and system auditors,<br>especially by  'approval for granting access rights<br>to a person' from 'set-up or adjustment of a user<br>account'.|<br>|||
||_user access of operators,_||||||||
||_administrators and system_||||||||
||<br>_auditors._||||||||
||||||||||
|**_REQ-7.4-05_**|_The administration_**_shall_**||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+has a user account management and<br>+ keeps user accounts up-to-date||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- operates a user account management, assuring<br>up-to-date user accounts and access rules.||||
||_include user account_||||||||
||_management and timely_||||||||
||_modification or removal of_||||||||
||_access._||||||||
||||||||||



Federal Office for Information Security 

39 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**<br>|**_Verdict Stage_**<br>~~**_1_**~~|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
|**_REQ-7.4-06_**|_Access to information and_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP grants access to<br>information and application system functions<br>conformant to the access controlpolicy.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has an access control policy in-line with the<br>[IS-Policy] and its role concept,<br>- has effective 'access restrictions' to information<br>and application system functions.||||
||_application system functions_||||||||
||**_shall_**_be restricted in_||||||||
||_accordance with the access_||||||||
||_control policy._||||||||
||||||||||
|**_REQ-7.4-07_**|_The TSP's system_**_shall_**||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+provides sufficient computer security controls<br>for the separation of trusted roles,<br>+ separates security administration from<br>operation functions,<br>+ restricts and controls use of system utility<br>programs-||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- technically enforces trusted role separation<br>(security administration, operation),<br>- allowsonlynecessary roles for the use of<br>system utility programs.||||
||_provide sufficient computer_||||||||
||_security controls for the_||||||||
||_separation of trusted roles_||||||||
||_identified in TSP's practices,_||||||||
||<br>_including the separation of_||||||||
||_security administration and_||||||||
||_operation functions._||||||||
||_Particularly, use of system_||||||||
||_utility programs shall be_||||||||
||_restricted and controlled._||||||||
|**_REQ-7.4-08_**|_TSP's personnel_**_shall_**_be_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP allows only identified and<br>authenticated personnel to have access to<br>critical applications related to the service.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has implemented a system user concept,<br>requiring successful user identification &<br>authentication before granting access to service<br>critical applications,<br>- monitors failed user identification &<br>authentication and limits the number of<br>consecutive false log-ins(account blocking).||||
||_identified and authenticated_||||||||
||_before using critical_||||||||
||_applications related to the_||||||||
||_service._||||||||
||||||||||



Federal Office for Information Security 

40 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**<br>|**_Verdict Stage_**<br>~~**_1_**~~|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
|**_REQ-7.4-09_**|_TSP's personnel_**_shall_**_be_|_EXAMPLE: By_<br>_retaining event_<br>_logs._|The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- documented that the TSP’s  personnel are<br>accountable for their activities||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has documented evidence that the TSP’s<br>personnel is accountable for their TSP service<br>related activities<br>- has documented such cases, where TSP’s<br>personnel was to be disciplined,– if any–||||
||_accountable for their_||||||||
||_activities._||||||||
||||||||||
|**_REQ-7.4-10_**|_Sensitive data_**_shall_**_be_|_NOTE 1: See_<br>_clause 9 of_<br>**_ISO/IEC_**<br>**_27002:2013_**<br>_[i.3] for_<br>_guidance._<br>_NOTE 2:_<br>_Further_<br>_recommendation_<br>_s regarding_<br>_authentication_<br>_are given in the_<br>_CA/Browser_<br>_Forum network_<br>_security guide_<br>_[i.7], clause 2._|The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP assures that storage<br>information objects, which contain(ed)<br>sensitive data, are only allowed to be re-used<br>e.g. after data deletion, if sensitive data will not<br>be disclosed to unauthorised users.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  implemented technical means to erase sensitive<br>data contained in storage information objects<br>beforeunauthorised users may be allowed to re-<br>use these storage information objects,<br>- can present (test) evidence of the effectiveness<br>of chosen technical means.||||
||_protected against being_||||||||
||_revealed through re-used_||||||||
||_storage objects (e.g. deleted_||||||||
||_files) being accessible to_||||||||
||<br>_unauthorized users._||||||||
||||||||||



Federal Office for Information Security 

41 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

## **7.5 Cryptographic controls** 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**<br>|**_Verdict Stage_**<br>~~**_1_**~~|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
|**_REQ-7.5-01_**|_Appropriate security controls_|<br>_NOTE: See_<br>_clause 10 of_<br>**_ISO/IEC_**<br>**_27002:2013_**<br>_[i.3] for_<br>_guidance._|The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- documented that the TSP manages<br>cryptographic means (keys, devices)<br>throughout their whole lifecycle.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- safeguards cryptographic credentials as well as<br>HSMs, smart cards etc. throughout the whole<br>lifecycle,<br>- covering all lifecycle phases of<br>+ devices: typical are purchase, handling and<br>storage, installation, generation, start-up,<br>operation, key-change, re-assignment with key-<br>erase, maintenance, repair, end-of-use and<br>disposal and<br>+ keys: typical are generation, transfer and<br>storage, usage, cloning, certification, distribution,<br>end-of-use and erase or deletion||||
||**_shall_**_be in place for the_||||||||
||_management of any_||||||||
||_cryptographic keys and any_||||||||
||_cryptographic devices_||||||||
||_throughout their lifecycle._||||||||
||||||||||



## **7.6 Physical and environmental security** 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**<br>|**_Verdict Stage_**<br>~~**_1_**~~|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
|**_REQ-7.6-01_**|_The TSP_**_shall_**_control_|_NOTE 1: See_<br>_clause 11 of_<br>**_ISO/IEC_**<br>**_27002:2013_**<br>_[i.3] for_<br>_guidance._|REMARK: This requirement is fulfilled, if all<br>derived requirements REQ-7.6-02 to REQ-7.6-<br>05 are fulfilled. No additional stage 1<br>assessment activity is required.||REMARK: This requirement is fulfilled, if all<br>derived requirements REQ-7.6-02 to REQ-7.6-05<br>are fulfilled. No additional stage 2 assessment<br>activity is required.||||
||_physical access to_||||||||
||_components of the TSP's_||||||||
||_system whose security is_||||||||
||_critical to the_||||||||
||_provision of its trust services_||||||||
||_and minimize risks related to_||||||||
||_physical security._||||||||
||_Inparticular:_||||||||



Federal Office for Information Security 

42 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**<br>|**_Verdict Stage_**<br>~~**_1_**~~|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
|**_REQ-7.6-02_**|_Physical access to_|<br>_NOTE 2:_<br>_Criticality is_<br>_identified_<br>_through risk_<br>_assessment, or_<br>_through_<br>_application_<br>_security_<br>_requirements, as_<br>_requiring a_<br>_security_<br>_protection._|<br>The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP limits physical access to<br>TSP system components being security critical<br>only to authorised individuals, either by risk<br>assessment or by component specification (e.g.<br>via guidance documentation).||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- grants physical access to security critical TSP<br>systems only to personnel being authorised on a<br>need-to-have basis.||||
||_components of the TSP's_||||||||
||_system whose security is_||||||||
||_critical to the provision of its_||||||||
||_trust services_**_shall_**_be limited_||||||||
||_to authorized individuals._||||||||
||||||||||
|**_REQ-7.6-03_**|_Controls_**_shall_**_be_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+implements controls helping to avoid loss,<br>damage or compromise of physically protected<br>assets,<br>+ implements business continuity controls to<br>avoid intolerable interruption of physically<br>protected business activities.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has effective controls in place to protect assets<br>from loss, damage or compromise,<br>- has a business continuity management in place<br>limiting potential interruption of business<br>activities to the inevitable.||||
||_implemented to avoid loss,_||||||||
||_damage or compromise of_||||||||
||_assets and interruption to_||||||||
||_business activities._||||||||
||||||||||
|**_REQ-7.6-04_**|_Controls_**_shall_**_be_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP implements controls<br>helping to avoid compromise or theft of<br>physically protected information or<br>informationprocessingfacilities.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has effective controls in place to protect<br>information and information processing facilities<br>from compromise or theft.||||
||_implemented to avoid_||||||||
||_compromise or theft of_||||||||
||_information and information_||||||||
||_processing facilities._||||||||
||||||||||



Federal Office for Information Security 

43 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage_**<br>~~**_1_**~~|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
|**_REQ-7.6-05_**|_Components that are critical_|_NOTE 3: See_<br>**_ISO/IEC_**<br>**_27002:2013_**<br>_[i.3], clause 11.1_<br>_for guidance on_<br>_secure areas._|<br>The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- documented that the TSP locates all security<br>critical TSP system components in a protected<br>security perimeter with physical protection<br>against intrusion, controls on access through<br>the security perimeter and alarms to detect<br>intrusion.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- does store and operateallsecurity critical TSP<br>system componentsexclusivelywithin physical<br>security zones (minimum: second zone) having<br>limited access only to authorised personnel,<br>- has implemented sufficient physical means to<br>protect this security zone along with the 'onion<br>principle', including means for<br>+ prevention (typical are enforced doors,<br>windows and walls, ceilings and floors, use of<br>sluices, access control systems following<br>'knowledge', 'possession' and 'property', visible<br>company badges, guards at check-points),<br>+ detection (typical are cameras for video<br>surveillance, sensors for movement, infra-red<br>sensors, door and window contact sensors,<br>reliable alarming system put through guards and<br>external security services or even police),<br>+ response (check, if enough resources are<br>available throughout 7x24, esp. night and<br>weekends, sufficient response time, specific<br>contracts with external security services,<br>frequency of practices alarms, contracts with<br>alarm system provider)<br>- has carefully taken measures to protect access<br>even in the case of an emergency (typical to<br>consider are paramedic services, fire ladders,<br>emergencyexits or fire alarms)||||
||_for the secure operation of_||||||||
||_the trust service_**_shall_**_be_||||||||
||_located in a protected_||||||||
||<br>_security perimeter with_||||||||
||_physical protection against_||||||||
||_intrusion, controls on access_||||||||
||_through the security_||||||||
||_perimeter and alarms to_||||||||
||_detect intrusion._||||||||
||||||||||



Federal Office for Information Security 

44 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**7.7**<br>**Operation security**|**7.7**<br>**Operation security**||||||||
|---|---|---|---|---|---|---|---|---|
|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage_**<br>~~**_1_**~~|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
|**_REQ-7.7-01_**|_The TSP_**_shall u_**_se_|_NOTE 1: See_<br>_clause 12 of_<br>**_ISO/IEC_**<br>**_27002:2013_**<br>_[i.3] for_<br>_guidance._<br>_NOTE 2: See_<br>_clause 14 of_<br>**_ISO/IEC_**<br>**_27002:2013_**<br>_[i.3] for_<br>_guidance on_<br>_systems_<br>_acquisition,_<br>_development_<br>_and_<br>_maintenance._<br>_NOTE 3: See_<br>_clause 15 of_<br>**_ISO/IEC_**<br>**_27002:2013_**<br>_[i.3] for_<br>_guidance on_<br>_supplier_<br>_relationship._|REMARK: This requirement is fulfilled, if all<br>derived requirements REQ-7.7-02 to REQ-7.7-<br>09 are fulfilled. No additional stage 1<br>assessment activity is required.||REMARK: This requirement is fulfilled, if all<br>derived requirements REQ-7.7-02 to REQ-7.4-09<br>are fulfilled. No additional stage 2 assessment<br>activity is required.||||
||_trustworthy systems and_||||||||
||_products that are protected_||||||||
||_against modification and_||||||||
||_ensure_||||||||
||_the technical security and_||||||||
||_reliability of the processes_||||||||
||_supported by them._||||||||
||_In particular:_||||||||
||||||||||



45 

Federal Office for Information Security 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**<br>|**_Verdict Stage_**<br>~~**_1_**~~|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
|**_REQ-7.7-02_**|_An analysis of security_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP assures a 'security by<br>design' approach for the development of its<br>TSP system architecture and applications.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has documented evidence of its security<br>requirements being input to the development of<br>its TSP systems during the system requirements<br>definition and design phase,<br>- has contractually bound its system suppliers to<br>implement the security requirements.||||
||_requirements_**_shall_**_be carried_||||||||
||_out at the design and_||||||||
||_requirements specification_||||||||
||_stage of any systems_||||||||
||_development project_||||||||
||_undertaken by the TSP or on_||||||||
||_behalf of the TSP to ensure_||||||||
||_that security is built into IT_||||||||
||_systems._||||||||
|**_REQ-7.7-03_**|_Change control procedures_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ maintains a change control process,<br>+ defines changes of any operational software<br>as:<br>++ releases,<br>++ modifications or<br>++ emergency software fixes, like security<br>patches,<br>+ includes changes of security policy<br>implementingsystem configurations||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- installed segregated duties according to a<br>change control for releases, modification and<br>emergency software fixes, e.g.:<br>+ suggest, document and implement a change, +<br>approval to implement a change , if<br>implementation (i.e. software development or<br>change of network architecture) is necessary,<br>+ testing of a(n implemented) change,<br>+ approval (to deploy) a change,<br>+ deploy a change||||
||**_shall_**_be applied for releases,_||||||||
||_modifications and emergency_||||||||
||_software fixes of any_||||||||
||_operational software and_||||||||
||_changes to the configuration_||||||||
||_which applies the TSP's_||||||||
||_security policy._||||||||
||||||||||
|**_REQ-7.7-04_**|_The procedures_**_shall_**_include_|_NOTE 4: See_<br>_clause 14 of_<br>**_ISO/IEC_**<br>**_27002:2013_**<br>_[i.3] for_<br>_guidance._|The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP maintains a change control<br>process that documents changes||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has documented evidence of its TSP software<br>and configuration changes||||
||_documentation of the_||||||||
||_changes._||||||||
||||||||||



46 

Federal Office for Information Security 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**<br>|**_Verdict Stage_**<br>~~**_1_**~~|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
|**_REQ-7.7-05_**|_The integrity of TSP's_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+strictly regulates deployment (installation) of<br>software; only authorised software is allowed<br>to be installed,<br>+ does malware scans on a continuous basis<br>and on demand always with recent malware<br>signatures.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  implemented malware scanners for DMZ,<br>network, and all servers and all clients, online or<br>stand-alone, if reasonable and possible,<br>- has durable and timely distribution channels for<br>malware signature updates,<br>- has at minimumtwodifferent types of scanners<br>in use, whenever information can be accessed<br>online, e.g. for e-mails different scanner on e-<br>mail server and on client,<br>- has segregation of duties for the roles 'system<br>operation' and 'system administration'||||
||_systems and information_||||||||
||**_shall_**_be protected against_||||||||
||_viruses, malicious and_||||||||
||_unauthorized software._||||||||
||||||||||
|**_REQ-7.7-06_**|_Media used within the TSP's_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+applies a secure media handling regulation<br>addressing potential media damage, theft,<br>disclosure or obsolescence (i.e. loss of<br>information due to ageing effects of the media<br>like),<br>+ uses typical media as there are e.g.: CDs,<br>DVDs, Blue Rays, USB-Sticks or USB-Drives,<br>hard-drives, SD-Cards and variants, and in<br>some cases even access (smart) cards or video<br>tapes.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has categorised media according to its<br>information classification scheme<br>- has protected data against disclosure by strong<br>encryption, especially if media are transferred to<br>physical security zones with a lower security<br>level or even to the outside of a building,<br>- has procedures for secure storage of and access<br>to media,<br>- assures authenticity of media before their use<br>REMARK:for obsolescence and deterioration of<br>media,see_REQ-7.7-07_||||
||_systems_**_shall_**_be securely_||||||||
||_handled to protect media_||||||||
||_from damage, theft,_||||||||
||_unauthorized access and_||||||||
||_obsolescence._||||||||
||||||||||



Federal Office for Information Security 

47 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**<br>|**_Verdict Stage_**<br>~~**_1_**~~|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
|**_REQ-7.7-07_**|_Media management_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+protects against information loss or data<br>corruption due to obsolescence or deterioration<br>of storage media by monitoring media lifetime<br>and handling requirements based on known<br>industry standards:<br>++ environmental requirements like humidity,<br>light sensitivity,<br>++ life time expectations due to aging effects,<br>++ balancing with time for records to be<br>retained,<br>+prepares back-upcopies,if necessary.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has continuously monitored the need for<br>protection of media against obsolescence and<br>deterioration; this includes to know minimum<br>life period of time (time of durability) of all used<br>types of media,<br>- has assured safe and secure handling and<br>storage of media,<br>- has measures in place to replace or substitute<br>mediabeforeobsolescence or deterioration may<br>take place,<br>- has back-up copies available, if necessary||||
||_procedures_**_shall_**_protect_||||||||
||_against obsolescence and_||||||||
||_deterioration of media within_||||||||
||_the period of time that_||||||||
||_records are required to be_||||||||
||_retained._||||||||
||||||||||
|**_REQ-7.7-08_**|_Procedures_**_shall_**_be_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+specified procedures for all trusted and<br>administrative roles who take part in the<br>provision of the service.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  specified and implemented procedures for all<br>trusted and administrative roles to ensure:<br>+ the technical security and<br>+ reliability<br>of the processes supported by the TSP<br>trustworthy products and systems.||||
||_established and implemented_||||||||
||_for all trusted and_||||||||
||_administrative roles that_||||||||
||_impact on the provision of_||||||||
||_services._||||||||
||||||||||



Federal Office for Information Security 

48 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage_**<br>~~**_1_**~~|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
|**_REQ-7.7-09_**|_The TSP_**_shall_**_specify and_|<br> <br>_NOTE 5:_<br>_Further specific_<br>_recommendation_<br>_s are given in_<br>_the CA/Browser_<br>_Forum network_<br>_security guide_<br>_[i.7], item 1 l._|The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+specifies and applies following patching<br>procedures:<br>++onlyreliable security patches are to be<br>applied and in a timely manner,<br>++nosecurity patching if the result is an<br>introduction of additional vulnerabilities or<br>instabilities worsening the situation of the TSP,<br>++ skipped security patching needs to be<br>reasoned and documented.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  applied its own security patching procedures,<br>including testing of their reliability with the TSP<br>trusted system<br>-  applied security patches in a timely manner<br>-  documented evidences of reasons for not<br>installing security patches||||
||_apply procedures for_||||||||
||_ensuring that:_||||||||
||_a) security patches are_||||||||
||_applied within a reasonable_||||||||
||_time after they come_||||||||
||_available;_||||||||
||_b) security patches are not_||||||||
||_applied if they introduce_||||||||
||<br>_additional vulnerabilities or_||||||||
||_instabilities that outweigh the_||||||||
||_benefits of applying them;_||||||||
||_and_||||||||
||_c) the reasons for not_||||||||
||_applying any security patches_||||||||
||_are documented._||||||||
|**7.8**<br>**Network security**<br>_NOTE: See clause 13 of_**_ISO/IEC 27002:2013_**_[i.3] for guidance._|||||||||
|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-7.8-01_**|_The TSP_**_shall_**_protect its_||REMARK: This requirement is fulfilled, if all<br>derived requirements REQ-7.8-02 to REQ-7.8-<br>15 are fulfilled. No additional stage 1<br>assessment activityis required.||REMARK: This requirement is fulfilled, if all<br>derived requirements REQ-7.8-02 to REQ-7.8-15<br>are fulfilled. No additional stage 2 assessment<br>activityis required.||||
||_network and systems from_||||||||
||_attack._||||||||
||_Inparticular:_||||||||



## **7.8 Network security** 

## _NOTE: See clause 13 of_ _**ISO/IEC 27002:2013** [i.3] for guidance._ 

Federal Office for Information Security 

49 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-7.8-02_**|_The TSP_**_shall_**_segment its_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>- applies a multi-zone concept for its different<br>IT networks and systems (office LAN,<br>development and testing, production, DMZ,<br>and stand-alone with galvanic separation to<br>other networks),<br>+ matches the level of security per each zone<br>with the results of the risk assessment,<br>+ reflects functional, logical and physical<br>aspects to derive security controls.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  tailored its systems and network addressing at<br>minimum:<br>+ front-end, publicly available, e.g. E-Mail or<br>Web Server or OCSP Responder,<br>+ back-end with e.g. data bases,<br>+ production network with applications,<br>+ office LAN with clients,<br>+ network management,<br>+ separation of domains e.g. via VLAN, with use<br>of switches, routers and firewalls,<br>+ back-up systems and networks,<br>+ stand-alone systems e.g. for root certification,<br>+physicalprotection||||
||_systems into networks or_||||||||
||_zones based on risk_||||||||
||_assessment considering_||||||||
||_functional, logical, and_||||||||
||_physical (including location)_||||||||
||_relationship between_||||||||
||_trustworthy systems and_||||||||
||_services._||||||||
||||||||||
|**_REQ-7.8-03_**|_The TSP_**_shall_**_apply the same_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ applies the same security controls to systems<br>co-located in the same zone.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  implemented the same security controls to all<br>systems co-located in the same security zone.||||
||_security controls to all_||||||||
||_systems co-located in the_||||||||
||_same zone._||||||||
||||||||||
|**_REQ-7.8-04_**|_The TSP_**_shall_**_restrict access_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ establishes access and communication rules<br>based on technical procedures allowing only<br>necessary interaction between network security<br>zones and with outside / internet.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  implemented the documented TSP access and<br>communication rules,<br>-  performs regular internal audits of the TSP<br>network and systems against defined access and<br>communication rules.||||
||_and communications between_||||||||
||_zones to those necessary for_||||||||
||_the operation of theTSP._||||||||
||||||||||



50 

Federal Office for Information Security 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-7.8-05_**|_The TSP_**_shall_**_explicitly_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+hardens the TSP network and systems by<br>deactivating (or forbidding) connections, ports,<br>protocols, services and applications not<br>necessaryfor TSP operation.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  implemented the documented TSP hardening<br>rules,<br>-  performs regular internal auditing of the TSP<br>network and systems against defined hardening<br>rules.||||
||_forbid or deactivate not_||||||||
||_needed connections and_||||||||
||_services._||||||||
||||||||||
|**_REQ-7.8-06_**|_The TSP_**_shall_**_review the_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>-  stated that the TSP<br>+performs regular reviews for its set of access,<br>communication and hardening rules for<br>network securityzones and systems.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  performs regular reviews of its documented<br>access, communication and hardening rules for<br>the network security zones and systems.||||
||_established rule set on a_||||||||
||_regular basis._||||||||
||||||||||
|**_REQ-7.8-07_**|_The TSP_**_shall_**_keep all_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ operatesallsystems that are critical to the<br>TSP operationsolelyin secure zone(s).||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  identifiedallsystems, which are critical to the<br>TSP operation,<br>-  clearly assigned all these systems to and kept<br>them in their securityzone(s).||||
||_systems that are critical to_||||||||
||_the TSP's operation in one or_||||||||
||<br>_more secured zone(s) (e.g._||||||||
||_Root CA systems see ETSI_||||||||
||<br>_EN 319 411-1[i.9])._||||||||



51 

Federal Office for Information Security 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-7.8-08_**|_The TSP_**_shall_**_separate_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ uses dedicated IT networks for:<br>++ TSP’s operational network (for<br>development, testing and production),<br>++ administration of IT systems,<br>++ galvanic separated networks, if necessary<br>(e.g. root CA system),<br>+ assures a reasonable separation of these<br>networks.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  a network topology chosen with<br>+ a separate operation network (for development,<br>testing and production),<br>++ that has its own administration network,<br>++ which is supported by the network<br>communication rules.||||
||_dedicated network for_||||||||
||_administration of IT systems_||||||||
||_and TSP's_||||||||
||_operational network._||||||||
||||||||||
|**_REQ-7.8-09_**|_The TSP_**_shall_**_not use_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ uses systems for administration of the<br>security policy implementationnotfor other<br>purposes.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-strictly limitsuse of administration systems for<br>security policy implementation,<br>- applies hardening rules enforcing this limitation<br>of use.||||
||_systems used for_||||||||
||_administration of the security_||||||||
||<br>_policy implementation for_||||||||
||_other purposes._||||||||
||||||||||
|**_REQ-7.8-10_**|_The TSP_**_shall_**_separate the_|<br>|The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ separates its IT production systems for<br>provides TSP’s services from development and<br>testing systems.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has a network topology chosen,<br>+ which separates production from development<br>and testing,<br>+ which is supported by the network<br>communication rules.||||
||_production systems for the_||||||||
||_TSP's services from systems_||||||||
||_used in_||||||||
||_development and testing (e.g._||||||||
||_development, test and staging_||||||||
||_systems)._||||||||
||||||||||



52 

Federal Office for Information Security 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-7.8-11_**|_The TSP_**_shall_**_establish_|<br>|The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ assures identification of end points,before<br>establishing communication between distinct<br>trustworthy systems,<br>+onlyuses trusted channels, logically<br>separated from other communication channels,<br>+ protects communication data integrity and<br>confidentiality.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  implemented:<br>+ identified and authenticated trusted channels,<br>++ using encryption and<br>++ integrity protection<br>for the communication between distinct<br>trustworthy systems.||||
||_communication between_||||||||
||_distinct trustworthy systems_||||||||
||_only through_||||||||
||_trusted channels that are_||||||||
||_logically distinct from other_||||||||
||_communication channels and_||||||||
||_provide assured_||||||||
||<br>_identification of its end points_||||||||
||_and protection of the channel_||||||||
||_data from modification or_||||||||
||_disclosure._||||||||
|**_REQ-7.8-12_**|_If a high level of availability_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ uses redundant external network connection,<br>ifhigh level of availability of the trust services<br>is required.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  implemented a durable redundant external<br>network connection, if necessary,<br>- has periodic failure tests of its external network<br>connection.||||
||_of external access to the trust_||||||||
||_service is required, the_||||||||
||_external network connection_||||||||
||**_shall_**_be redundant to ensure_||||||||
||_availability of the services in_||||||||
||<br>_case of a singlefailure._||||||||
|**_REQ-7.8-13_**|_The TSP_**_shall_**_undergo or_|_NOTE 1: See_<br>_item 4c of the_<br>_CA/Browser_<br>_Forum network_<br>_security guide_<br>_[i.7] for_<br>_guidance_<br>_regarding the_<br>_time period._|The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ performsorundergoes periodic vulnerability<br>scans on public and private IP addresses of the<br>TSP,<br>+ assures necessary skills, tools, proficiency,<br>code of ethics and independence of the person<br>or entity performing and documenting each<br>vulnerability scan performed.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  performed or underwent periodic vulnerability<br>scans on relevant public and private IP addresses<br>- has documented evidence of:<br>+ the results of vulnerability scans (reports),<br>+ necessary skills, tools, proficiency, code of<br>ethics and independence of person or entity who<br>or which has performed the scans,<br>-  fixed those identified vulnerabilities, which<br>provide an unacceptable level of risk for the TSP.||||
||_perform a regular_||||||||
||_vulnerability scan on public_||||||||
||_and private IP addresses_||||||||
||_identified by the TSP and_||||||||
||<br>_record evidence that each_||||||||
||_vulnerability scan was_||||||||
||_performed by a person or_||||||||
||_entity with the skills, tools,_||||||||
||_proficiency, code of ethics,_||||||||
||_and independence necessary_||||||||
||_toprovide a reliable report._||||||||



53 

Federal Office for Information Security 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-7.8-14_**|_The TSP_**_shall_**_undergo a_|_NOTE 2: See_<br>_item 4d of the_<br>_CA/Browser_<br>_Forum network_<br>_security guide_<br>_[i.7] for_<br>_guidance_<br>_regarding the_<br>_time period._|The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ undergoes regular penetration tests of the<br>TSP systems (to perform by TSP itself isnot<br>sufficient)<br>+ assures testing:<br>++ at set-up,<br>++ after upgradesormodifications of<br>infrastructureorapplications.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  underwent regular penetration tests of the TSP<br>systems,<br>- has documented evidence of the penetration test<br>results (reports),<br>-  fixed those identified weaknesses, which<br>provide anin-acceptable level of risk for the TSP.||||
||_penetration test on the TSP's_||||||||
||_systems at set up and after_||||||||
||_infrastructure or application_||||||||
||_upgrades or modifications_||||||||
||_that the TSP determines are_||||||||
||_significant._||||||||
||||||||||
|**_REQ-7.8-15_**|_The TSP_**_shall_**_record_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ assures necessary skills, tools, proficiency,<br>code of ethics and independence of the person<br>or entity performing and documenting each<br>penetration testperformed.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  documented evidence of skills, tools,<br>proficiency, code of ethics and independence of<br>the person or entity who or which has performed<br>the tests.||||
||_evidence that_||||||||
||_eachpenetration test was_||||||||
||_performed by a person or_||||||||
||_entity with the skills, tools,_||||||||
||_proficiency, code of ethics,_||||||||
||_and independence necessary_||||||||
||_toprovide a reliable report._||||||||



54 

Federal Office for Information Security 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**7.9**<br>**Incident management**|**7.9**<br>**Incident management**||||||||
|---|---|---|---|---|---|---|---|---|
|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-7.9-01_**|_System activities concerning_|_NOTE 1: See_<br>_clause 16 of_<br>**_ISO/IEC_**<br>**_27002:2013_**<br>_[i.3] for_<br>_guidance._|REMARK: This requirement is fulfilled, if all<br>derived requirements REQ-7.9-02 to REQ-7.9-<br>12 are fulfilled. No additional stage 1<br>assessment activity is required.||REMARK: This requirement is fulfilled, if all<br>derived requirements REQ-7.9-02 to REQ-7.9-12<br>are fulfilled. No additional stage 2 assessment<br>activity is required.|<br>|||
||_access to IT systems, use of_||||||||
||_IT systems, and service_||||||||
||_requests_**_shall_**_be_||||||||
||_monitored._||||||||
||_Inparticular:_||||||||
|**_REQ-7.9-02_**|_Monitoring activities_**_should_**||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ only monitors system activitiesnecessaryto<br>identify potential security violation,<br>+ protects collected information from<br>unauthorised access or manipulation,<br>+ analyses collected information only for the<br>purpose to identifyorprove securitybreaches.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  established a monitoring process with<br>segregated duties (system operation and<br>administration separate from information<br>collection and analysis),<br>- has a monitoring concept with strict rules for<br>collecting and analysing information and further<br>use.||||
||_take account of the sensitivity_||||||||
||_of any information collected_||||||||
||_or analysed._||||||||
||||||||||
|**_REQ-7.9-03_**|_Abnormal system activities_|_NOTE 2:_<br>_Abnormal_<br>_network system_<br>_activities can_<br>_comprise_<br>_(external)_<br>_network scans_<br>_orpacket drops._|The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ applies technical and organisational means to<br>detect abnormal system activities like intrusion<br>into the TSP network,<br>+ reports detections as alarms.|<br>|The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  implemented a detection system to identify<br>abnormal system activities like port scans, packet<br>drops or mass online requests (i.e. denial-of-<br>service attacks) or unsuccessful log-ins,<br>- has documented evidence of reported alarms, –<br>if any–||||
||_that indicate a potential_||||||||
||_security violation, including_||||||||
||_intrusion into the TSP's_||||||||
||_network,_**_shall_**_be detected_||||||||
||_and reported as alarms._||||||||
||||||||||



55 

Federal Office for Information Security 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-7.9-04_**|_The TSP IT systems_**_shall_**||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ monitors with its IT systems following<br>events:<br>++ start-up and shutdown of logging functions,<br>++ availability and utilisation (i.e. current load)<br>of needed services.|<br>|The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  implemented (and has evidence of) monitoring<br>of following events:<br>+ start and stop of logging functions,<br>+ service availability and network utilisation<br>(current load).||||
||_monitor the following events:_||||||||
||_a) start-up and shutdown of_||||||||
||_the logging functions; and_||||||||
||_b) availability and utilization_||||||||
||_of needed services with the_||||||||
||_TSP's network._||||||||
||||||||||
|**_REQ-7.9-05_**|_The TSP_**_shall_**_act in a timely_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ responds in a timely and co-ordinated<br>manner to incidents,<br>+ limits the impact of breaches of security.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  defined the procedures, roles and<br>responsibilities of an incident response team to<br>limit the potential impact in case of a serious<br>incident,<br>- has sufficient trusted role personnel (alarm<br>team) available throughout whole service hours<br>of the TSP.||||
||_and co-ordinated manner in_||||||||
||_order to respond quickly to_||||||||
||_incidents and to limit the_||||||||
||_impact of breaches of_||||||||
||_security._||||||||
||||||||||
|**_REQ-7.9-06_**|_The TSP_**_shall_**_appoint_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ appoints trusted role personnel to analyse<br>alerts for their security relevance (i.e. if the<br>alarms may be serious incidents) and follow-up<br>those incidents,includingreporting.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  appointed trusted role personnel (alarm team)<br>to follow up on alerts potentially critical security<br>events,<br>-  documented evidences of identified incidents,<br>– if any –.||||
||_trusted role personnel to_||||||||
||_follow up on alerts of_||||||||
||_potentially critical security_||||||||
||_events and ensure that_||||||||
||_relevant incidents are_||||||||
||_reported in line with the_||||||||
||_TSP'sprocedures._||||||||



56 

Federal Office for Information Security 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-7.9-07_**|_The TSP_**_shall_**_establish_|<br> <br>_NOTE 3: TSPs_<br>_operating within_<br>_the European_<br>_Union can_<br>_contact the_<br>_appropriate_<br>_supervisory_<br>_body and/or_<br>_other competent_<br>_authorities for_<br>_further guidance_<br>_on implementing_<br>_notification_<br>_procedures as_<br>_per article 19.2_<br>_of Regulation_<br>_(EU) No_<br>_910/2014[i.2]._|<br> <br> <br>The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ establishes notification procedures in line<br>with applicable regulatory rules,<br>+ notifies any breach of security or integrity<br>loss, that has a significant impact on the trust<br>service providedorpersonal data maintained,<br>+ assuresallaffected parties are notified,<br>+ assures a notification within 24 hours after<br>breach identification.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  established a notification procedure for<br>security breaches or loss of integrity with<br>significant impact on the provided trust services,<br>-  appointed a notification team allowing<br>notification within 24 hours after identification<br>or the breach,<br>- has maintained a list of 'appropriate parties'<br>who, in principle, may have to be notified,<br>- has documented evidences of past notifications,<br>– if any.|<br>|||
||_procedures to notify the_||||||||
||_appropriate parties in line_||||||||
||_with the applicable_||||||||
||_regulatory rules of any_||||||||
||_breach of security or loss of_||||||||
||_integrity that has a_||||||||
||_significant impact on the_||||||||
||_trust service provided and on_||||||||
||<br>_the personal data maintained_||||||||
||<br>_therein within 24 hours of the_||||||||
||_breach  being identified._||||||||
||||||||||
|**_REQ-7.9-08_**|_Where the breach of security_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ notifies also a natural or legal person of a<br>security breach or loss of integrity, if the<br>breach is likely to adversely affect this person,<br>+ notifies these people without undue delay<br>(i.e. as soon as possible).||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  included in its notification procedure to notify<br>also adversely affected natural or legal people of<br>a security breach,<br>- is capable to notify those people without undue<br>delay<br>- has documented evidences of past notifications,<br>– if any –.||||
||_or loss of integrity is likely to_||||||||
||_adversely affect a natural or_||||||||
||_legal person to whom the_||||||||
||_trusted service has been_||||||||
||_provided, the TSP_**_shall_**_also_||||||||
||_notify the natural or legal_||||||||
||_person of the breach of_||||||||
||_security or loss of integrity_||||||||
||_without undue delay._||||||||



57 

Federal Office for Information Security 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-7.9-09_**|_The TSP's systems_**_shall_**_be_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ monitors its systemsandaudit logs (or<br>regularly reviews the latter) to identify<br>evidence of malicious activity,<br>+ implements automatic mechanisms to<br>process audit logs and to alert personnel of<br>possible critical securityevents.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  implemented monitoring of TSP systems for<br>malicious activity,<br>- has automated audit log analysis and alerting<br>appointed personnel of possible critical security<br>events (i.e. incidents).||||
||_monitored including the_||||||||
||_monitoring or regular review_||||||||
||_of audit logs to identify_||||||||
||_evidence of malicious activity_||||||||
||<br>_implementing automatic_||||||||
||_mechanisms to process the_||||||||
||_audit logs and alert_||||||||
||_personnel of possible critical_||||||||
||_security events._||||||||
|**_REQ-7.9-10_**|_The TSP_**_shall_**_address any_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ addresses critical vulnerabilities within 48<br>hours after discoverybythe TSP.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  appointed a notification team allowing to<br>address critical vulnerabilities within 48 hours<br>after discovery by the TSP.||||
||_critical vulnerability not_||||||||
||_previously addressed by the_||||||||
||_TSP, within a period of 48_||||||||
||_hours after its discovery._||||||||
||||||||||



58 

Federal Office for Information Security 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-7.9-11_**|_For any vulnerability, given_|_EXAMPLE: The_<br>_TSP can_<br>_determine that_<br>_the vulnerability_<br>_does not require_<br>_remediation_<br>_when the cost of_<br>_the_<br>_potential impact_<br>_does not_<br>_warrant the cost_<br>_of mitigation._<br>_NOTE 4:_<br>_Further_<br>_recommendation_<br>_s are given in_<br>_the CA/Browser_<br>_Forum network_<br>_security guide_<br>_[i.7] item 4f)._|<br>The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ mitigates critical vulnerabilities, if this is cost<br>effective in comparison to the impact,<br>+eithercreates and implements a plan to<br>mitigate the vulnerability,<br>+ordocuments factual reasons not to<br>remediate the vulnerability.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  planned and implemented mitigation of those<br>critical vulnerabilities, which are cost effective<br>compared to the potential impact,<br>-  documented reasons of any vulnerabilities not<br>remediated.||||
||_the potential impact, the TSP_||||||||
||**_shall [_**_CHOICE]:_||||||||
||_- create and implement a_||||||||
||_plan to mitigate the_||||||||
||_vulnerability; or_||||||||
||_- document the factual basis_||||||||
||<br>_for the TSP's determination_||||||||
||_that the vulnerability does_||||||||
||<br>_not require_||||||||
||_remediation._||||||||
||||||||||
|**_REQ-7.9-12_**|_Incident reporting and_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+assures, that the reporting of incidentsandthe<br>incident response procedures are used to<br>minimise factual damage from security<br>incidents and malfunctions.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  implemented its incident reporting and incident<br>response procedures<br>+ to keep the time, damage may occur from<br>incident, as short as possibleand<br>+ to limit damage to the inevitable by containing<br>the incident, avoiding spread-out of malicious<br>activity or infection to further TSP systems and<br>networks or subscribers or other relying parties||||
||_response procedures_**_shall_**_be_||||||||
||_employed in such a way that_||||||||
||_damage from security_||||||||
||_incidents and malfunctions_||||||||
||<br>_are minimized._||||||||
||||||||||



59 

Federal Office for Information Security 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

## **7.10 Collection of evidence** 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor Guidance_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
||||**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-7.10-01_**|_The TSP_**_shall r_**_ecord and_|<br>_NOTE:_<br>_See requirement REQ-7.13-_<br>_05._<br>See**[ISO-15489]**.<br>See**[TR-ESOR]**.|REMARK: This requirement is<br>fulfilled, if all derived<br>requirements REQ-7.10-02 to<br>REQ-7.10-08 are fulfilled. No<br>additional stage 1 assessment<br>activity is required.||REMARK: This requirement is fulfilled, if all<br>derived requirements REQ-7.10-02 to REQ-7.10-<br>08 are fulfilled. No additional stage 2 assessment<br>activity is required.||||
||_keep accessible for an_||||||||
||_appropriate period of time,_||||||||
||_including after the activities_||||||||
||_of the TSP have ceased, all_||||||||
||_relevant information_||||||||
||_concerning data issued and_||||||||
||_received by the TSP, in_||||||||
||_particular, for the_||||||||
||_purpose of providing_||||||||
||_evidence in legal proceedings_||||||||
||_and for the purpose of_||||||||
||_ensuring continuity of the_||||||||
||_service._||||||||
||_Inparticular:_||||||||



60 

Federal Office for Information Security 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor Guidance_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
||||**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-7.10-02_**|_The confidentiality and_|<br>See: Clauses<br>8.2, 9 & 10 of**[ISO/IEC**<br>**27002**]<br>and chap. 6.2-6.3, 8.3 -8.5 ,<br>9.5 and 9.9 of**[ISO-15489]**<br>and**[TR-ESOR]**<br>for guidance.|The assessor shall assess the<br>documents [TSPS] and [IS-Policy]<br>and<br>verify<br>that<br>the<br>TSP:<br>- stated that the TSP<br>+<br>protects<br>confidentiality<br>and<br>integrity of its currentandarchived<br>records, which are related to the<br>operation of services,<br>+ defined clear asks,<br>responsibilities and processes<br>regarding management of<br>electronic records.|<br> <br> <br> <br> <br>|The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  categorised its records related to the operation<br>of services according to the information<br>classification scheme,<br>-  implemented appropriate measures to observe<br>and monitor retention periods and deletion<br>policies,<br>-  defined appropriate confidentiality and<br>deletion classes,<br>-  defined an appropriate measures to ensure<br>confidentiality and integrity for the defined<br>retention period,<br>-  applied security measures to current and<br>archived records in line with the applicable<br>information classification,<br>- enforces confidentiality and integrity of its<br>records regardless of whether the information is<br>onpaper or in electronic form.||||
||_integrity of current and_||||||||
||_archived records concerning_||||||||
||_operation of services_**_shall_**_be_||||||||
||_maintained._||||||||
||||||||||
|**_REQ-7.10-03_**|_Records concerning the_|<br> <br>See Clauses 9, 12.3, 18.1.3<br>of**[ISO/IEC 27002]**and<br>chap. 9.6-9.9 of<br>**[ISO 15489]**for guidance.|The assessor shall assess the<br>documents [TSPS], [TSPolicy] and<br>[IS-Policy] and verify that the<br>TSP:<br>- stated that the TSP<br>+ assures completenessand<br>confidentiality of its archived<br>records,<br>+ applies its disclosed business<br>practices to archived records.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  implemented a procedure to assure<br>completeness and negotiability4of archived<br>records, even in the case, (parts of) archived<br>records will be taken out of the archive (for<br>further processing) or if moved to other (or final)<br>archive(s)<br>-  applied to its paper archive physical security<br>measures, e.g. access control and, if electronic<br>records are archived, logical security measures to<br>the IT archive system|<br>|||
||_operation of services_**_shall_**_be_||||||||
||_completely and confidentially_||||||||
||_archived in accordance with_||||||||
||_disclosed business practices._||||||||
||||||||||



4 Data / documents are "negotiable" if they (and the associated signatures and verification data) are available and exchangable in formats that a typical user can read and 

61 

Federal Office for Information Security 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor Guidance_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
||||**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-7.10-04_**|_Records concerning the_|<br>See<br>Clause 9 & 18.1 of<br>**[ISO/IEC 27002]**, chap. 9.7<br>of**[ISO-15489]**,<br>BSI TR03125 (main<br>document**[TR-ESOR]**&<br>annex F**[TR-ESOR-F]**) and<br>K15, K19 of**[DIN31644]**for<br>guidance.|<br>The assessor shall assess the<br>documents [TSPS], [TSPolicy] and<br>[IS-Policy] and verify that the<br>TSP:<br>- stated that the TSP<br>+ follows judicial demands for the<br>purpose of legal proceedings and<br>provides (current or archived)<br>records related to the correctness<br>of operation of the services.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  established a formalised response procedure to<br>judicial demands for handing over (current or<br>archived) records as evidence for its corrects<br>operation of the services for use in legal<br>proceedings,<br>-  established appropriate measures to ensure<br>access on records in negotiable and usable format<br>or structure, able to make integrity evident<br>against 3rdparties,<br>-  established appropriate measures to preserve<br>negotiability and availability for the defined<br>retentionperiods.||||
||_operation of services_**_shall_**_be_||||||||
||_made available if required_||||||||
||_for the purposes of providing_||||||||
||_evidence of the correct_||||||||
||_operation of the services for_||||||||
||_the purpose of legal_||||||||
||_proceedings._||||||||
||||||||||
|**_REQ-7.10-05_**|_The precise time of_|See Clause 10 of**[ISO/IEC-**<br>**27002]**for guidance.|The assessor shall assess the<br>documents [TSPS], [TSPolicy] and<br>[IS-Policy] and verify that the<br>TSP:<br>- stated that the TSP<br>+ records the precise time of<br>following significant TSP events:<br>++ environmental,<br>++ key management,<br>++ clock synchronisation.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  implemented (by automated means) to assign<br>precise time into audit logs for significant TSP<br>events (environment, clock sync, key<br>management).||||
||_significant TSP's_||||||||
||_environmental, key_||||||||
||_management, access, clock_||||||||
||_synchronization events_**_shall_**||||||||
||_be recorded._||||||||
||||||||||



interpret at the time of use thus at least until the end of the retention period with typical standard IT equipment, and in doing so consistency with the original is guaranteed and that authenticity and integrity can be make evident only by the self-contained data/document. 

62 

Federal Office for Information Security 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor Guidance_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
||||**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-7.10-06_**|_The time used to record_||The assessor shall assess the<br>documents [TSPS], [CP] and [IS-<br>Policy] and verify that the TSP:<br>- stated that the TSP<br>+ synchronises time (to record<br>significant events in audit logs)<br>with UTC at minimum once a day||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  assured - at minimum - daily sync of event<br>time for audit logs with UTC time source.||||
||_events as required in the_||||||||
||_audit log shall be_||||||||
||_synchronized with UTC at_||||||||
||_least once a day_||||||||
||||||||||
|**_REQ-7.10-07_**|_Records concerning services_|See<br>Clause 8+9 of**[ISO15489]**<br>and<br>**[TR-ESOR]**for guidance.|The assessor shall assess the<br>documents [TSPS] and [IS-Policy]<br>and verify that the TSP:<br>- stated that the TSP<br>+holds records as legal evidence<br>for {the correctness of} TSP<br>services as long as specified in the<br>[T&C].||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  implemented an appropriate management for<br>the relevant electronic records,<br>-  implemented an appropriate preservation of<br>evidence of electronic records.||||
||**_shall_**_be held for a period of_||||||||
||_time as appropriate for_||||||||
||_providing necessary legal_||||||||
||_evidence and as notified in_||||||||
||_the TSP's terms and_||||||||
||_conditions (see clause 6.3)._||||||||
||||||||||
|**_REQ-7.10-08_**|_The events shall be logged in_|<br> <br> <br> <br> <br>_EXAMPLE: This can be_<br>_achieved,_<br>_for_<br>_example,_<br>_through the use of write-only_<br>_media, a record of each_<br>_removable media used and_<br>_the use of off-site backup or_<br>_by parallel storage of the_<br>_information at_<br>_several (e.g. 2 or 3)_<br>_independent sites._<br>See also BSI TR-03125<br>(**[TR-ESOR])**forguidance.|<br> <br> <br> <br> <br> <br>The assessor shall assess the<br>documents [TSPS] and [IS-Policy]<br>and verify that the TSP:<br>- stated that the TSP<br>+ describes how the TSP prevents<br>the deletion or destruction of the<br>logging data within the period of<br>time that they are required to be<br>held.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  implemented an appropriate measures to<br>prevent the deletion or destruction of the logging<br>data within the period of time that they are<br>required to be held.||||
||_a way that they cannot be_||||||||
||_easily deleted or destroyed_||||||||
||_(except if_||||||||
||_reliably transferred to long-_||||||||
||_term media) within the period_||||||||
||_of time that they are required_||||||||
||_to be held._||||||||
||||||||||



63 

Federal Office for Information Security 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

## **7.11 Business continuity management** 

|**_Reference_**|**_Norm Requirement_**|**_Notes /_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Auditor_**|**_(document assessment)_**||**_(on-site assessment)_**||||
|||**_Guidance_**|||||||
||||||||||
|**_REQ-7.11-01_**|_The TSP shall define and_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ defines and maintains a continuity plan to<br>enact in case of a disaster.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has kept its continuity plan up-to-date by, at<br>minimum, yearly reviews and revisions and in<br>case of substantial changes (e.g. new services,<br>use of new technologies, change of shareholders,<br>change of organisational structure, new<br>outsourcing partners, moving of TSP critical<br>infrastructure or systems to other sites).||||
||_maintain a continuity plan to_||||||||
||_enact in case of a disaster._||||||||
||||||||||
|**_REQ-7.11-02_**|_In the event of a disaster,_|<br> <br>_NOTE 1: See_<br>_clause 17 of_<br>**_ISO/IEC_**<br>**_27002:2013_**<br>_[i.3] for_<br>_guidance in the_<br>_event of a_<br>_disaster._<br>_NOTE 2: Other_<br>_disaster_<br>_situations_<br>_include failure_<br>_of critical_<br>_components of a_<br>_TSP's_<br>_trustworthy_<br>_system,_<br>_including_<br>_hardware and_<br>_software_|<br>The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ considers compromise scenarios, e.g. of<br>private signing keys, in its continuity plan,<br>+ states provisioned restoration time,<br>+ remediates recurrence of disaster causes, e.g.<br>by a security vulnerability.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  assigned roles of the emergency, disaster and<br>recovery teams to personnel<br>- performs regular testing of its alarming,<br>response and recovery procedures at minimum<br>once a year<br>-  documented evidence of disasters from past –<br>if any – with<br>+ a description of disaster,<br>+ enacted continuity plan,<br>+ effective restoration times,<br>+ root cause analysis and<br>+ remediation measures preventing from<br>recurrence of such disaster, if applicable.||||
||_including compromise of a_||||||||
||_private signing key or_||||||||
||_compromise of some other_||||||||
||_credential of the TSP,_||||||||
||_operations shall be restored_||||||||
||_within the delay established_||||||||
||_in the continuity plan, having_||||||||
||_addressed any cause for the_||||||||
||_disaster which may recur_||||||||
||_(e.g. a security vulnerability)_||||||||
||_with appropriate remediation_||||||||
||_measures._||||||||
||||||||||



64 

Federal Office for Information Security 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

## **7.12 TSP termination and termination plans** 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-7.12-01_**|_Potential disruptions to_|Conditional in<br>Germany: See<br>**[VDG]**/**[VDV]**<br>for guidance.|REMARK: This requirement is fulfilled, if all<br>derived requirements REQ-7.12-02 to REQ-<br>7.12-11 are fulfilled. No additional stage 1<br>assessment activity is required.||REMARK: This requirement is fulfilled, if all<br>derived requirements REQ-7.12-02 to REQ-7.12-<br>11 are fulfilled. No additional stage 2 assessment<br>activity is required.||||
||_subscribers and relying_||||||||
||_parties shall be minimized as_||||||||
||_a result of the cessation of_||||||||
||_the TSP's services, and in_||||||||
||_particular continued_||||||||
||_maintenance of information_||||||||
||_required to verify the_||||||||
||_correctness of trust_||||||||
||_services shall be provided._||||||||
||_Inparticular:_||||||||



65 

Federal Office for Information Security 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-7.12-02_**|_The TSP shall have an up-to-_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+reviews and revises its termination plan:<br>++ on a yearly basis and<br>++ in case of substantial changes to the TSP<br>organisation, service or system.<br>Conditional in Germany: According to German<br>legislation, the assessor shall verify that<br>qualified TSPs issuing qualified certificates<br>assure following in specific:<br>The termination plan considers following<br>termination scenarios:<br>a) termination of service (regular case)<br>b) revocation of its qualification status<br>c) application for opening insolvency<br>proceedings, if service provision will not be<br>continued according to**[VDG],**article 16<br>paragraph 1.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has kept its termination plan up-to-date by, at<br>minimum, yearly reviews and revisionsandin<br>case of substantial changes (e.g. new services,<br>use of new technologies, change of shareholders,<br>change of organisational structure, new<br>outsourcing partners, moving of TSP critical<br>infrastructure or systems to other sites).<br>Conditional in Germany: According to German<br>legislation, the assessor shall verify that qualified<br>TSPs has implemented a proper measures<br>according to**[VDG],**article 16 paragraph 1.||||
||_date termination plan._||||||||
||||||||||
||_Before the TSP terminates its_||||||||
||<br>_services at least the following_||||||||
||_procedures apply:_||||||||
||||||||||



66 

Federal Office for Information Security 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-7.12-03_**|_Before the TSP terminates its_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ informsallsubscribers, other entities like<br>relying parties, TSPs and e.g. supervisory<br>bodies, with which the TSP has agreements or<br>other form of established relationsbefore<br>termination of its TSP services.<br>Conditional in Germany: According to German<br>legislation, the assessor shall verify that<br>qualified TSPs fulfil the requirements<br>according to**[VDG],**article 16 paragraph 2):<br>1. National Supervisory Body<br>“Bundesnetzagentur” is to be notified about<br>intended termination of qualified certification<br>service without undue delay<br>2 Subscriber (and subject) of qualified<br>certificates are to be informed of planned<br>termination of qualified certification services<br>and hand-over of qualified certificates as far as<br>possible no less than two months beforehand<br>accordingto**[VDG],**article 16paragraph 2.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- established termination proceduresassuring<br>that:<br>+allsubscribers and other relying parties (with<br>which the TSP has agreements or other form of<br>established relations) will be informedbefore<br>termination of TSP services, e.g. via mail, e-mail<br>or other way.<br>Conditional in Germany: According to German<br>legislation, the assessor shall verify that qualified<br>TSPs has implemented a proper measures<br>according to**[VDG],**article 16 paragraph 2.||||
||_services, the TSP shall inform_||||||||
||_the following of the_||||||||
||<br>_termination: all subscribers_||||||||
||_and other entities with which_||||||||
||_the TSP has agreements or_||||||||
||_other form of_||||||||
||<br>_established relations, among_||||||||
||<br>_which relying parties, TSPs_||||||||
||_and relevant authorities such_||||||||
||_as supervisory_||||||||
||_bodies._||||||||
||||||||||
|**_REQ-7.12-04_**|_Before the TSP terminates its_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ informs other relying parties before<br>termination of its TSP services.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  established termination proceduresassuring<br>that:<br>+allother relying parties will be informedbefore<br>termination of TSP services, e.g. via mail, e-mail<br>or other way.||||
||_services, the TSP shall make_||||||||
||_the information of the_||||||||
||<br>_termination available to_||||||||
||_other relying parties._||||||||
||||||||||



67 

Federal Office for Information Security 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**<br>|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**|||||
|||||||||||
|**_REQ-7.12-05_**|_Before the TSP terminates its_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ applies following procedures in case of<br>termination of service:<br>++ terminate authorisation of all subcontractors<br>involved inissuingtrust service tokens.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has termination proceduresassuringthat:<br>+ authorisations ofallsubcontractors involved in<br>issuanceof trust service tokens will be<br>terminatednolater than the termination date.|||||
||_services, the TSP shall_|||||||||
||_terminate authorization of all_|||||||||
||<br>_subcontractors to act on_|||||||||
||_behalf of the TSP in carrying_|||||||||
||<br>_out any functions relating to_|||||||||
||<br>_the process of issuing_|||||||||
||_trust service tokens._|||||||||



68 

Federal Office for Information Security 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**<br>|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**|||||
|||||||||||
|**_REQ-7.12-06_**|_Before the TSP terminates its_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ applies following procedures in case of<br>termination of service:<br>++ transfer obligations to a reliable third party<br>for maintainingallinformation necessary to<br>provide evidences of the TSP operation for a<br>reasonable period of time, if applicable.<br>Conditional in Germany: According to German<br>legislation, the assessor shall verify that<br>qualified TSPs issuing qualified certificates or<br>providing qualified time stamps assure the<br>following in specific:<br>Obligations for maintaining<br>- all issued qualified certificates,<br>- together with related certificate signer<br>certificates,<br>- its signer certificates for time stamps and<br>- revocation status information<br>are to be transferred either to a different<br>qualified TSP or to the National Supervisory<br>Body “Bundesnetzagentur”<br>according to**[VDG],**article 16 paragraph 1,<br>esp. no. 1 and 2.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has termination proceduresassuringthat:<br>+allinformation necessary to provide evidences<br>of the TSP operation will be securely transferred<br>to a reliable party such that it is protected from<br>disclosure and manipulation.<br>Conditional in Germany: According to German<br>legislation, the assessor shall verify that qualified<br>TSPs has implemented a proper measures<br>according. to**[VDG],**article 16 paragraph 1.|||||
||_services, the TSP shall_|||||||||
||_transfer obligations to a_|||||||||
||<br>_reliable party for maintaining_|||||||||
||<br>_all information necessary to_|||||||||
||_provide evidence of the_|||||||||
||_operation of the TSP for a_|||||||||
||_reasonable period, unless it_|||||||||
||<br>_can be demonstrated that the_|||||||||
||_TSP does not hold any such_|||||||||
||_information._|||||||||
|||||||||||



69 

Federal Office for Information Security 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**<br>|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**|||||
|||||||||||
|**_REQ-7.12-07_**|_Before the TSP terminates its_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ applies following procedures in case of<br>termination of service:<br>++ destroy or withdraw from use the TSP<br>private keys and backup copies (retrieval shall<br>not bepossible).||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has termination proceduresassuringthat:<br>+ TSP private keys and their backup copies<br>cannotbe retrieved after destruction or<br>withdrawal from use.|||||
||_services, the TSP's private_|||||||||
||_keys, including backup_|||||||||
||<br>_copies,_|||||||||
||_shall be destroyed, or_|||||||||
||<br>_withdrawn from use, in a_|||||||||
||_manner such that the private_|||||||||
||_keys cannot be retrieved._|||||||||
|||||||||||
|**_REQ-7.12-08_**|_Before the TSP terminates its_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ applies following procedures in case of<br>termination of service:<br>++ transfer of provision of trust services for its<br>existing customers to another TSP, where this<br>ispossible.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has termination proceduresassuringthat:<br>+ arrangements are made with another TSP, so<br>that provision of trust services for its existing<br>customers can be transferred, where this is<br>possible.|||||
||_services, where possible TSP_|||||||||
||_should make arrangements to_|||||||||
||<br>_transfer provision of trust_|||||||||
||_services for its existing_|||||||||
||_customers to another TSP._|||||||||
|||||||||||
|**_REQ-7.12-09_**|_The TSP shall have an_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ has arrangements in place, covering costs for<br>termination as far as possible according to its<br>termination plan also in the case of e.g.<br>bankruptcy.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has documented evidence for up-to-date and<br>effective arrangements (e.g. insurance, guarantee<br>from an independent third party = patronage)<br>covering costs for termination of service e.g. in<br>case of TSP bankruptcy.|||||
||_arrangement to cover the_|||||||||
||_costs to fulfil these minimum_|||||||||
||_requirements in case the TSP_|||||||||
||_becomes bankrupt or for_|||||||||
||_other reasons is unable to_|||||||||
||_cover the costs by itself, as_|||||||||
||_far as possible within the_|||||||||
||_constraints of applicable_|||||||||
||_legislation regarding_|||||||||
||_bankruptcy._|||||||||



Federal Office for Information Security 

70 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**<br>|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**|||||
|||||||||||
|**_REQ-7.12-10_**|_The TSP shall state in its_||The assessor shall assess the document [TSPS]<br>and verify that the TSP:<br>- states in the [TSPS] its provisions regarding:<br>+ notification of affected entities,<br>+ transfer of TSP obligations to other parties.<br>Conditional in Germany: According to German<br>legislation, the assessor shall verify that<br>qualified TSPs issuing qualified certificates or<br>providing qualified time stamps assure the<br>following in specific:<br>a) National Supervisory Body<br>“Bundesnetzagentur” is to be notified about<br>intended termination of qualified certification<br>service without undue delay acc. article 4<br>paragraph 3**[VDV]**. Subscriber (and subject)<br>of qualified certificates are to be informed of<br>planned termination of qualified certification<br>services and hand-over of qualified certificates<br>as far as possible no less than two months<br>beforehand acc. Article 16 paragraph 2**[VDG]**.<br>b) Obligations for maintaining<br>- all issued qualified certificates,<br>- together with related certificate signer<br>certificates,<br>- its signer certificates for time stamps and, and<br>- revocation status information<br>are to be transferred either to a different<br>qualified TSP or to the National Supervisory<br>Body “Bundesnetzagentur” according to article<br>**[VDG], **16paragraph 1,esp. no. 1 and 2**.**|<br> <br> <br>|The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has termination proceduresassuringthat:<br>+ TSP private keys and their backup copies can<br>notbe retrieved after destruction or withdrawal<br>from use.<br>Conditional in Germany: According to German<br>legislation, the assessor shall verify that qualified<br>TSPs has implemented a proper measures<br>according to**[VDG],**article 16 paragraph 1.|||||
||_practices the provisions made_|||||||||
||_for termination of service._|||||||||
||<br>_This shall include: a)_|||||||||
||_notification of affected_|||||||||
||<br>_entities; and_|||||||||
||_b) transferring the TSP's_|||||||||
||_obligations to other parties._|||||||||
|||||||||||



Federal Office for Information Security 

71 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**<br>|**_Verdict Stage_**<br>**_2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|**_REQ-7.12-11_**|_The TSP shall maintain or_|<br>|The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ either maintains by itself its obligations to<br>make available its public keys or its trust<br>service tokens to relying parties for a<br>reasonable period of time {after the<br>termination of service}<br>+ or transfers these obligations to a reliable<br>party.<br>Conditional in Germany: According to German<br>legislation, the assessor shall verify that<br>qualified TSPs issuing qualified certificates or<br>providing qualified time stamps assure the<br>following in specific:<br>Either the qualified TSP maintains itself or<br>transfers its obligations to make available<br>- its certificate signer certificates,<br>- its signer certificates for time stamps.<br>If the obligations are transferred, this will be<br>either to a different qualified TSP or to the<br>National Supervisory Body<br>“Bundesnetzagentur” according to**[VDG],**<br>article 16paragraph 1,esp. no. 1 and 2.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has durable means to make available its public<br>keys or its trust service tokens for a reasonable<br>period of time (after the termination of service)<br>- either maintains its obligations by itself or is<br>prepared to make arrangements to transfer these<br>obligations to a reliable party<br>Conditional in Germany: According to German<br>legislation, the assessor shall verify that qualified<br>TSPs has implemented a proper measures<br>according. to**[VDG],**article 16 paragraph 1.||||
||_transfer to a reliable party its_||||||||
||_obligations to make available_||||||||
||_its public key or its trust_||||||||
||_service tokens to relying_||||||||
||_parties for a reasonable_||||||||
||_period._||||||||
||||||||||



Federal Office for Information Security 

72 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

## **7.13 Compliance** 

|**_Reference_**|**_Norm Requirement_**|**_Notes / Auditor_**|**_Stage 1 Assessment criteria_**|**_Verdict Stage 1_**|**_Stage 2 Assessment criteria_**|**_Verdict Stage 2_**|**_Observations_**|**_Findings_**|
|---|---|---|---|---|---|---|---|---|
|||**_Guidance_**|**_(document assessment)_**||**_(on-site assessment)_**||||
||||||||||
|_REQ-7.13-01_|_The TSP shall ensure that it_||REMARK: This requirement is fulfilled, if all<br>derived requirements REQ-7.13-02 to REQ-<br>7.13-05 are fulfilled. No additional stage 1<br>assessment activityis required.||REMARK: This requirement is fulfilled, if all<br>derived requirements REQ-7.13-02 to REQ-7.13-<br>05 are fulfilled. No additional stage 2 assessment<br>activityis required.||||
||_operates in a legal and_||||||||
||_trustworthy manner._||||||||
||_Inparticular:_||||||||
|_REQ-7.13-02_|_The TSP shall provide_||The assessor shall assess the documents<br>[TSPS] and verify that the TSP:<br>-  stated in its [TSPS] how it meets the<br>applicable legal requirements.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has up-to-date knowledge of its applicable legal<br>requirements and<br>- has sufficient measures inplace to complywith||||
||_evidence on how it meets the_||||||||
||_applicable legal_||||||||
||_requirements._||||||||
||||||||||
|_REQ-7.13-03_|_Trust services provided and_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ provides its trust services such that they are<br>accessible for people with disabilities.||The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>-  made its trust services accessible for people<br>with disabilities, e.g.:<br>+ web-sites display (at least on demand) content<br>in text format instead of pictures,<br>+ e-mails are in such format that typical<br>applications (e.g. outlook), maybe supported by<br>plug-ins, can be used to non-visually read the<br>contained information (e.g. by voice reader),<br>-  tested the accessibility||||
||_end user products used in the_||||||||
||_provision of those services_||||||||
||_shall be made accessible for_||||||||
||_persons with disabilities,_||||||||
||_where feasible.._||||||||
||||||||||
|_REQ-7.13-04_|_Applicable standards on_||The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>stated that the TSP<br>-  took ETSI EN 301 549 as an accessibility<br>standard or a correspondingstandard.||not applicable||||
||_accessibility such as ETSI_||||||||
||_EN 301 549 [i.10] should be_||||||||
||_taken into account._||||||||
||||||||||



Federal Office for Information Security 

73 

## Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

|_REQ-7.13-05_|_Appropriate technical and_|_NOTE: TSPs_<br>_operating in_<br>_Europe are_<br>_required to_<br>_ensure that_<br>_personal data is_<br>_processed in_<br>_accordance with_<br>_Directive_<br>_95/46/EC [i.1]_<br>_until 25 May_<br>_2018, and from_<br>_25 May 2018 in_<br>_accordance with_<br>_Regulation_<br>_(EU) 2016/679_<br>_[i.12] that_<br>_repeals the_<br>_Directive_<br>_95/46/EC. In_<br>_this respect,_<br>_authentication_<br>_for a service_<br>_online concerns_<br>_processing of_<br>_only those_<br>_identification_<br>_data which are_<br>_adequate,_<br>_relevant and not_<br>_excessive to_<br>_grant access to_<br>_that service_<br>_online._|<br> <br> <br>The assessor shall assess the documents<br>[TSPS], [TSPolicy] and [IS-Policy] and verify<br>that the TSP:<br>- stated that the TSP<br>+ applies technical and organisational measures<br>to meet data protection requirements, at<br>minimum protection:<br>++ against unauthorised or unlawful processing<br>of personal data and<br>++ against accidental loss or destruction of, or<br>damage to, personal data.|<br>|The assessor shall assess the TSP on-site and<br>verify that the TSP:<br>- has technical and organisational measures for<br>data protection which are sufficient to:<br>+ abide unauthorised or unlawful processing of<br>personal data, esp. through legitimate<br>authorisation of personal data related processes,<br>roles and applications (software),<br>+ assure integrity and availability of personal<br>data.||||
|---|---|---|---|---|---|---|---|---|
||_organizational measures_||||||||
||_shall be taken against_||||||||
||_unauthorized or unlawful_||||||||
||_processing of personal data_||||||||
||_and against accidental loss_||||||||
||_or destruction of, or damage_||||||||
||_to, personal data._||||||||
||||||||||



Federal Office for Information Security 

74 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

## **8 Appendix** 

75 

Federal Office for Information Security 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

## **9 References** 

## **9.1 Normative References** 

References are either specific (identified by the date of publication and/or edition number or version number) or non-specific. For specific references, only the cited version applies. For non-specific references, the latest version of the referenced document (including any amendments) applies. 

Referenced documents, which are not found to be publicly available in the expected location, might be found at https://docbox.etsi.org/Reference. The following referenced documents are necessary for the application of the present document. 

|**_Reference_**|**_Document Title, Version / Date_**|
|---|---|
|ASS 319 401|BSI Criteria for Assessing: Criteria for Assessing Trust Service Providers against ETSI<br>Policy Requirements, Part 1: Assessment Criteria for all TSP - ETSI EN 319 401.|
|ETSI EN 319 401|ETSI EN 319 401 V2.2.1 (2018-04), Electronic Signatures and Infrastructures (ESI);<br>General Policy Requirements for Trust Service Providers.|
|ETSI EN 319 403|ETSI EN 319 403 V2.2.2 (2015-08), Electronic Signatures and Infrastructures (ESI); Trust<br>Service Provider Conformity Assessment - Requirements for conformity assessment bodies<br>assessing Trust Service Providers.|
|ETSI TS 119 403-3|TS 119 403-3 V1.1.1 (2019-03), Requirements for Conformity Assessment Bodies<br>assessing QTSP against eIDAS.|
|ISO/IEC 17065|ISO/IEC 17065:2012: Conformity assessment -- Requirements for bodies certifying<br>products, processes and services.|
|eIDAS<br>[eIDAS<br>(Regulation<br>(EU)<br>No<br>910/2014))|Regulation (EU) No 910/2014 of the European Parliament and of the Council of 23 July<br>2014 on electronic identification and trust services for electronic transactions in the internal<br>market and repealing Directive 1999/93/EC. OJ L 257, 28.8.2014, p. 73-114.|
|Directive 2000/43/EC|Council Directive 2000/43/EC of 29 June 2000 implementing the principle of equal<br>treatment between persons irrespective of racial or ethnic origin, 29.6.2000.|
|Directive 2004/113/EC|COUNCIL DIRECTIVE 2004/113/EC of 13 December 2004 - implementing the principle<br>of equal treatment between men and women in the access to and supply of goods and<br>services, 13.12.2004.|
|Directive<br>Proposal<br>(COM(2008)462)|Proposal for a Council Directive on implementing the principle of equal treatment between<br>persons irrespective of religion or belief, disability, age or sexual orientation {SEC(2008)<br>2180} {SEC(2008) 2181} /* COM/2008/0426 final - CNS 2008/0140 */, 2.7.2008.|



76 

Federal Office for Information Security 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**_Reference_**|**_Document Title, Version / Date_**|
|---|---|
|VDG|Vertrauensdienstegesetz<br>(VDG),<br>18.07.2017,<br>https://www.gesetze-im-<br>internet.de/vdg/BJNR274510017.html.|
|VDV|Vertrauensdiensteverordnung,  15.02.2019,<br>https://dejure.org/BGBl/2019/BGBl._I_S._114.|



## **Table 2: Normative References** 

Federal Office for Information Security 

77 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

## **9.2 Informative References** 

References are either specific (identified by the date of publication and/or edition number or version number) or non-specific. For specific references, only the cited version applies. For non-specific references, the latest version of the referenced document (including any amendments) applies. 

The following referenced documents are not necessary for the application of the present document but they assist the user with regard to a particular subject area. 

|**_Reference_**|**_Document Title, Version / Date_**|
|---|---|
|DIN31644|DIN 31644 (2012-04), Information and documentation - Criteria for trustworthy digital<br>archives, 04.2012, https://www.beuth.de/de/norm/din-31644/147058907.|
|Directive 95/46/EC|Directive 95/46/EC of the European Parliament and of the Council of 24 October 1995 on<br>the protection of individuals with regard to the processing of personal data and on the free<br>movement of such data.|
|Regulation (EU) 2016/679|Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April<br>2016 on the protection of natural persons with regard to the processing of personal data<br>and on the free movement of such data,and repealingDirective95/46/EC.|
|ETSI EN 319 411-1|ETSI EN 319 411-1 V1.2.2 (2018-04), Electronic Signatures and Infrastructures (ESI);<br>Policy and security requirements for Trust Service Providers issuing certificates; Part 1:<br>General requirements.|
|ETSI EN 319 411-2|ETSI EN 319 411-2 V2.2.2 (2018-04), Electronic Signatures and Infrastructures (ESI);<br>Policy and security requirements for Trust Service Providers issuing certificates; Part 2:<br>Requirements for trust service providers issuing EU qualified certificates.|
|ETSI EN 319 421|ETSI EN 319 421 V1.1.1 (2016-03), Electronic Signatures and Infrastructures (ESI); Policy<br>and Security Requirements for Trust Service Providers issuing Time-Stamps.|
|ETSI TS 119 511|ETSI TS 119 511 V1.1.1 (2019-06, Electronic Signatures and Infrastructures (ESI); Policy<br>and security requirements for trust service providers providing long-term preservation of<br>digital signatures or general data using digital signature techniques.|
|ETSI TS 119 512|ETSI TS 119 512 V1.1.1 (2019-07), Electronic Signatures and Infrastructures (ESI); Policy<br>and security requirements for trust service providers providing long-term data preservation<br>services.|
|ISO-15489|ISO 15489-1 (2016): Information and documentation — Records management — Part 1:<br>Concepts and principles.|
|ISO 27001|ISO/IEC 27001 (2013): Information technology - Security techniques - Information<br>security management systems – Requirements.|



Federal Office for Information Security 

78 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

|**_Reference_**|**_Document Title, Version / Date_**|
|---|---|
|ISO 27002|ISO/IEC 27002 (2013): Information technology - Security techniques - Code of practice<br>for information security management.|
|ISO 27005|ISO/IEC 27005 (2011): Information technology - Security techniques - Information<br>security risk management.|
|TR-ESOR|BSI Technical Guideline 03125: Preservation of Evidence of Cryptographically Signed<br>Documents – TR-ESOR.<br>NOTE:<br>Available in English athttps://www.bsi.bund.de/EN/tr-esor, in German at<br>https://www.bsi.bund.de/tr-esor.|
|TR-ESOR-F|BSI Technical Guideline 03125:_Preservation of Evidence of Cryptographically Signed_<br>_Documents: Annex TR-ESOR-F Formats, V1.2.2._|



## **Table 3: Informative References** 

Federal Office for Information Security 

79 

Criteria for Assessing Trust Service Providers against ETSI Policy Requirements 

## **10 Keywords and Abbreviations** 

|**_Abbreviation_**|**_Keyword_**|
|---|---|
|[ABC]|for: document ABC|
|CA|Certificate Authority|
|CAB|ConformityAssessment Body|
|eIDAS|REGULATION (EU) No 910/2014 OF THE<br>EUROPEAN PARLIAMENT AND OF THE<br>COUNCIL of 23 July 2014 on electronic<br>identification and trust service for electronic<br>transactions in the internal market and repealing<br>Directive 1999/93/EC|
|EU|European Union|
|GDPR|General Data Protection Regulation|
|IS-Policy|Information Security Policy (see e.g.**EN 319**<br>**401**, chapter 6.3)|
|IT|Information Technology|
|TSPolicy|Trust Service Policy|
|NC|Non-Conformity|
|OCSP|Online Certificate Status Protocol|
|QTSP|Qualified Trust Service Provider|
|(Q)TPS|TSP or QTSP|
|QPSP|Qualified Preservation Service Provider|
|(Q)PSP|PSP orQPSP|
|T&C|Terms and Conditions, EN 319 401, chapter 6.2|
|TR-ESOR|DE: DE: Technische Richtlinie zur<br>Beweiserhaltung kryptographisch signierter<br>Dokumente<br>EN: Preservation of Evidence of<br>CryptographicallySigned Documents|
|TSPS|Trust Service Practice Statement, EN 319 401,<br>chapter 6.1|
|UTC|Coordinated Universal Time|



Federal Office for Information Security 

80 

Part 1: Assessment Criteria for all TSP – ETSI EN 319 401 

## **Table 4:   Keywords and Abbreviations** 

Federal Office for Information Security 

81 


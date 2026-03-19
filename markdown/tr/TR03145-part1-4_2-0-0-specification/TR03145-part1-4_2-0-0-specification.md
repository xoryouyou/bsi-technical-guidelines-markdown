## Inspection Specification BSI TR03145-TS 

Part 1: Generic requirements for a Certification Authority in a Public Key Infrastructure with security level 'high', Version 2.0.0 

Part 4: Specific requirements for a Certification Authority in a Public Key Infrastructure for the Extended Access Control of the German Official Travel Documents according to BSI TR-03110, Version 2.0.0 

Version 2.0.0 

12.12.2025 

Federal Office for Information Security P.O. Box 20 03 63 53133 Bonn Tel.: +49 22899 9582-0 E-Mail: eID@bsi.bund.de Internet: https://www.bsi.bund.de © Federal Office for Information Security 2025 

1 Introduction 

## Table of Contents 

|1|Introduction....................................................................................................................................................................................... 5|Introduction....................................................................................................................................................................................... 5|
|---|---|---|
||1.1|Scope and structure of this document......................................................................................................................... 5|
||1.2|Concept and approach of the Inspection Specification........................................................................................ 5|
||1.2.1|Assignments.................................................................................................................................................................. 7|
||1.2.2|Notation.......................................................................................................................................................................... 7|
||1.3|Scope of the Audit................................................................................................................................................................. 7|
|2|General requirements for Certification Authorities.......................................................................................................... 9||
||2.1|Cryptographic measures.................................................................................................................................................... 9|
||2.2|Certification practice statement and certificate policy management........................................................... 10|
||2.2.1|Certificate policy management........................................................................................................................... 11|
||2.2.2|Certification practice statement management............................................................................................. 15|
||2.2.3|Requirements for relying parties and subscribers of the CA.................................................................. 17|
||2.3|Information security policy............................................................................................................................................ 18|
||2.4|Asset classification and management......................................................................................................................... 20|
||2.5|Human resources security............................................................................................................................................... 21|
||2.6|Physical and environmental security......................................................................................................................... 23|
||2.7|Operational security........................................................................................................................................................... 26|
||2.8|Access control....................................................................................................................................................................... 29|
||2.9|System acquisition, development and maintenance........................................................................................... 32|
||2.10|Business continuity management................................................................................................................................ 33|
||2.11|Monitoring, conformance and compliance............................................................................................................. 35|
||2.12|Audit journal security and archiving.......................................................................................................................... 35|
||2.13|Controlled CA termination............................................................................................................................................. 41|
|3|Key life cycle management ........................................................................................................................................................ 43||
||3.1|CA key life cycle management ....................................................................................................................................... 43|
||3.1.1|CA key generation..................................................................................................................................................... 44|
||3.1.2|CA key storage, backup, and recovery.............................................................................................................. 46|
||3.1.3|CA public key distribution .................................................................................................................................... 48|
||3.1.4|CA key usage............................................................................................................................................................... 48|
||3.1.5|CA key archival and destruction......................................................................................................................... 50|
||3.1.6|CA key compromise................................................................................................................................................. 51|
||3.2|Subject key life cycle management.............................................................................................................................. 52|
||3.2.1|Subject key generation and distribution......................................................................................................... 53|
||3.2.2|Subject key storage, backup and recovery...................................................................................................... 57|
||3.2.3|Hardware token life cycle management (if supported)............................................................................. 60|
||3.2.4|Subject key archival and destruction (if supported)................................................................................... 63|



Federal Office for Information Security 

3 

1 Introduction 

|4|Certificate life cycle management .......................................................................................................................................... 65|Certificate life cycle management .......................................................................................................................................... 65|
|---|---|---|
||4.1|Subject registration ............................................................................................................................................................. 65|
||4.2|Certificate renewal (if supported)................................................................................................................................. 68|
||4.3|Certificate rekey ................................................................................................................................................................... 71|
||4.4|Certificate issuance............................................................................................................................................................. 72|
||4.5|Certificate distribution...................................................................................................................................................... 75|
||4.5.1|Directory Service (if supported).......................................................................................................................... 76|
||4.6|Certificate changeover (if supported)......................................................................................................................... 77|
||4.7|Certificate revocation........................................................................................................................................................ 80|
||4.8|Certificate suspension (if supported).......................................................................................................................... 85|
||4.9|Revocation status information service....................................................................................................................... 89|
||4.10|Validation Model................................................................................................................................................................. 92|
|Bibliography.............................................................................................................................................................................................. 93|||



Federal Office for Information Security 

4 

1 Introduction 

## 1 Introduction 

The document at hand serves as the inspection specification for an auditor concerning a Certification Authority (CA) in a Public Key Infrastructure (PKI) with security level 'high'. This document contains lists for coordinating checks and actions to be undertaken by an auditor and thus, provides a structured approach to check if a Certification Authority in a Public Key Infrastructure fulfils all requirements for a secure CA operation as defined in (BSI-TR-03145-1). 


![](markdown/tr/TR03145-part1-4_2-0-0-specification/TR03145-part1-4_2-0-0-specification.pdf-0005-03.png)



![](markdown/tr/TR03145-part1-4_2-0-0-specification/TR03145-part1-4_2-0-0-specification.pdf-0005-04.png)


(RFC2119). Irrespective of capitalisation (ISO27099). 

## 1.1 Scope and structure of this document 

The document at hand represents the inspection specification for the following parts of the Secure CA Operation series (BSI-TR-03145): 

- (BSI-TR-03145-1) Generic requirements for a Certification Authority in a Public Key 

   - . 

- (BSI-TR-03145-4) fic requirements for a Certification Authority in a Public Key Infrastructure for the Extended Access Control of the German Official Travel Documents according to (BSI-TR-03110) 

If necessary, the generic requirements of (BSI-TR-03145-1) are adapted to a specific application context in a separate Technical Guideline but as part of the superior Secure CA Operation series. Thereby, an application specific Technical Guideline of the Secure CA Operation series defines only the differences between the generic and the application specific requirements. That means that for a requirement of an application specific Technical Guideline the following three cases exist: 

- a) the application specific requirement is a refinement of the corresponding, generic requirement from (BSI-TR-03145-1). 

- b) the application specific requirement is a supplement to the generic requirements of (BSI-TR-031451) addressed by (BSI-TR-03145-1). 

- c) the application specific requirement declares a generic requirement from (BSI-TR-03145-1) not applicable to that specific application context. 

In order to be compliant with such an application specific part, a CA SHALL completely fulfil all application specific requirements as well as all requirements from (BSI-TR-03145-1) unless explicitly declared not applicable in the application specific part. This means that in this case the CA SHALL fulfil 

- all refined requirements according to a), 

- all new requirements according to b), 

- all generic requirements from (BSI-TR-03145-1) except those explicitly declared not applicable according to c) or already superseded according to a). 

In order to allow the parallel usage of the document at hand and the corresponding Technical Guideline/Guidelines, this document mainly follows the structure of the corresponding version of (BSI-TR03145). Furthermore, the notation of the requirements from (BSI-TR-03145) and from the application specific Technical Guideline/Guidelines is re-used here. 

## 1.2 Concept and approach of the Inspection Specification 

This chapter describes the usage and notations of the document at hand in detail. 

Federal Office for Information Security 

5 

1 Introduction 

The inspection specification is presented in table form. These tables are divided into 2 parts which are highlighted in cyan and gray, respectively. 

The first part of the table is highlighted in cyan. This part describes and structures the actions that SHALL be performed by an auditor in order to check compliance of a CA with (BSI-TR-03145-1) and the corresponding application-specific part, if applicable. This first part of the table includes the following columns from left to right which cover all requirements for the secure CA operation according to the corresponding Technical Guideline/Guidelines: 

- 1st : refers to the requirement which is covered by this action. 

- TR-Part : specifies the part of the Secure CA Operation series the referred 

- requirement stems om (BSI-TR-03145-1). In this case, this action has to be performed by an auditor in any case. Other values correspond to application 4 (BSI-TR-03145-4). If the entry corresponds to an application specific 

- part this action has to be performed only if the CA has to be checked according to that particular application specific Technical Guideline. 


![](markdown/tr/TR03145-part1-4_2-0-0-specification/TR03145-part1-4_2-0-0-specification.pdf-0006-05.png)


: describes the action that SHALL be performed by an auditor. 

- 3rd 

The second part of the table is highlighted in gray and SHALL be filled in by the auditor to ensure and document a structured inspection of a CA. These 3 columns correspond to the actions, which an auditor SHALL perform during the inspection of a CA. The order of the actions by the auditor correspond to the order of the columns from left to right: 

- 4th : The auditor SHALL identify the parts of documentation provided by the CA, which deal with the requirements and the inspection actions defined in the underlying row. All documents used by the auditor for the specific action SHALL be listed. 

- 5th previous column, the auditor SHALL identify and document the measures which are provided by the CA in order to implement the requirements that are addressed by the first the underlying row. Those documented measures SHALL be inspected and evaluated during the inspection of the CA. 

- 6 : This column SHALL contain the verdict of the auditor concerning the completeness and effectiveness of the measures that are implemented by the CA in order to fulfil the requirements that are addressed by the first underlying row. 

The auditor SHALL state the verdict by marking one of the three given options. 

Note: For the sake of transparency and accountability, the auditor SHALL give reasons for the verdict . column 3 and 4), the auditor SHALL note questions and remarks which showed up during this step in the corresponding column. These questions and remarks SHALL be checked by the auditor during the inspection at the CA. Of course, if additional questions occur during the inspection of the CA, they SHALL be noted and checked by the auditor as well. Only if all questions and remarks of one row are checked (completeness) and are evaluated with a positive result by the auditor (effectiveness), the requirement is covered by the CA and the auditor can give a positive verdict. 

There are different background colours in the tables below that represent the following case: 

- Yellow: These parts refer directly to the section and paragraphs of (ISO27099) and its corresponding requirements that need to be checked by the auditor 

- Orange:  These parts describe the audit requirements referring to  (BSI-TR-03145-4) 

Federal Office for Information Security 

6 

1 Introduction 

## 1.2.1 Assignments 

Several requirements contain assignments. For these assignments, the CA MUST clearly define which specific security measures, information or time periods are applicable and used to fulfil the requirement. Assignments represent cases in which own solutions may be added. 

For all assignments, the auditor SHALL note the assigned values in the audit report. For example, for requirement 4.7.A2 the auditor SHALL note in the audit report how many hours the completion of the revocation process takes at most, e.g. 36 hours. 

## 1.2.2 Notation 

The following notation is used in this document: 


![](markdown/tr/TR03145-part1-4_2-0-0-specification/TR03145-part1-4_2-0-0-specification.pdf-0007-06.png)


by the auditor. 


![](markdown/tr/TR03145-part1-4_2-0-0-specification/TR03145-part1-4_2-0-0-specification.pdf-0007-08.png)


the underlying evaluation. Subsequently the auditor has to check the selected case. 

Further, nested notation are also used. For example: 

a) case A (i) aspect A1 (ii) aspect A2 (iii) aspect A3 b) case B aspect B1 

If case A is valid, the auditor has to check the aspects A1, A2, and A3. Otherwise B1 has to be checked. 

## 1.3 Scope of the Audit 

Part 1 of (BSI-TR-03145) defines requirements for the secure operation of a single CA in a PKI. This CA SHALL be uniquely identified in its own certificate as subject. Furthermore, its relationship within the PKI SHALL be clearly specified. This SHALL consist of a complete description of: 


![](markdown/tr/TR03145-part1-4_2-0-0-specification/TR03145-part1-4_2-0-0-specification.pdf-0007-15.png)



![](markdown/tr/TR03145-part1-4_2-0-0-specification/TR03145-part1-4_2-0-0-specification.pdf-0007-16.png)



![](markdown/tr/TR03145-part1-4_2-0-0-specification/TR03145-part1-4_2-0-0-specification.pdf-0007-17.png)


all CAs the PKI consists of whereas these CAs are all uniquely identified in their certificate as subject, 

- the PKI hierarchy, and 

all other PKI components or services that may be relevant for the security of the CA, such as for example Registration Authority, Directory Service or CRL Signer (if supported). 

However, an audit according to Part 1 or other application specific parts MAY be performed for more than one single CA within the same PKI or for all CAs within the same PKI. The scope of the audit SHALL be described by means of the following table: 

|No.|Question|Declarations of the<br>auditor|
|---|---|---|
|1|Has this audit been performed for a single CA?|☐Yes<br>☐No|
|2|For which part of the (BSI-TR-03145) series has this audit been<br>performed?|☐Part 1<br>☐Part 4|



Federal Office for Information Security 

7 

1 Introduction 

|No.|Question|Question|Declarations of the|
|---|---|---|---|
||||auditor|
|3|Based on which version of the Technical Guide this audit has been<br>performed (e.g. BSI TR-03145-1 Version 2.0.0)?|||
|4|Description of the audited CA.<br>Note:If more than one single CA is in the scope of the audit (see question<br>1 above), this question has to be answered once for each CA that is in the<br>scope of the audit.|||
||4a|How is the audited CA identified in their certificate as subject<br>(e.g. Root-CA-01)?||
||4b|What is the type of the audited CA?|☐root-CA<br>☐sub-CA|
|5|.<br>Note:If more than one single CA is in the scope of the audit (see<br>question 1 above), this question may have to be answered more than<br>once depending on the audit scope.|||
||5a|List all CAs as identified in their certificate as subject the PKI<br>consists of.||
||5b|Briefly describe the PKI hierarchy.||
||5c|Are there other PKI components or services that may be<br>relevant for the security of the CA, such as for example<br>Registration Authority, Directory Service or CRL Signer?|☐No<br>☐Yes<br>If Yes, which ones:|



If more than one CA is in the scope of the audit, an auditor SHALL evaluate all these CAs (and their relationships) and SHALL document the audit results in the inspection specification. For example, may apply to all CAs in the scope of the audit or may differ. The same scope of the audit or may differ. The audit report SHALL clearly reflect these differences or similarities . 

Federal Office for Information Security 

8 

2 General requirements for Certification Authorities 

## 2 General requirements for Certification Authorities 

## 2.1 Cryptographic measures 

The use of inappropriate cryptographic algorithms or parameters facilitates the compromise of certificates, signatures, hashes or encryption. Therefore, the CA shall ensure that appropriate cryptographic algorithms and parameters are used. The algorithms and parameters shall comply with the current state of the art and shall be based on well-known Technical Guidelines and standards such as for example (BSI-TR-03116), (BSI-TR-02102). 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|2.1A1|1|Check that the CA ensures that the cryptographic<br>algorithms and their parameters comply with the<br>newest editions of the following documents:<br>[assignment: technical guidelines or standards for<br>cryptographic algorithms and recommended key<br>lengths].<br>Check that this document is appropriate for the<br>business case of the CA.<br>Check that the CA ensures to check the cryptographic<br>algorithms and their parameters referring to the<br>newest editions:<br>(i) Each time a cryptographic algorithm is newly<br>implemented.<br>(ii) When an incident of a used algorithm becomes<br>public.<br>(iii) Regularly, in a period of [assignment: number<br>of days, weeks or months].|||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

9 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
||4|Check that the CA ensures that the cryptographic|||☐Pass|
|||algorithms and their parameters comply with the|||☐Fail|
|||||||
|||newest editions of (BSI-TR-03116-2).|||☐Not applicable|
|||||||
|||Check that the CA ensures to check the cryptographic||||
|||||||
|||algorithms and their parameters referring to the||||
|||newest editions:||||
|||(i) Each time a cryptographic algorithm is newly||||
|||implemented.||||
|||(ii) When an incident of a used algorithm becomes||||
|||public.||||
|||(iii) Regularly, in a period of [assignment: number||||
|||of days, weeks or months].||||



## 2.2 Certification practice statement and certificate policy management 

This Section refers to Section 7.2 of (ISO27099) and addresses requirements concerning both, Certificate Policy and Certification Practice Statement. With respect to Certificate Policy and Certification Practice Statement, the following requirements apply: 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|||||||
|2.2A1|1,<br>4|Check that CP and CPS are part of the documentation<br>which is maintained within the ISMS.|||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

10 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|||||||
|2.2A2|1,<br>4|Check that the CPs and CPSs within the PKI are<br>compliant.<br>If the audited CA is issuing certificates to a CA, check<br>that the audited CA ensures that CP and CPS of the<br>subscribing CA are consistent with its own CP and CPS.<br>If the audited CA is a subscribing CA (i.e. the CA to be<br>certified is not a Root-CA), check that the audited CA<br>ensures that its own CP and CPS are consistent with CP<br>and CPS of the issuing CA.|<br>||☐Pass<br>☐Fail<br>☐Not applicable|



## 2.2.1 Certificate policy management 

Control procedures referenced in this Section refer to Section 7.2.1 of (ISO27099). In order to provide an adequate Certificate Policy, the following control procedures SHALL be fulfilled as requirements: 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(1) from|1,|Check that the final authority, responsible for defining|||☐Pass|
|Section||and approving certificate policies is clearly defined.|||☐Fail|
||4|||||
|7.2.1|||||☐Not applicable|
|||||||
|||||||
|(4) from|1,|Check that the CA maintains procedures for keeping|||☐Pass|
|Section||the affected parties informed of any changes to its|||☐Fail|
||4|||||
|7.2.1||certificate policies and makes this available to the|||☐Not applicable|
|||affected parties.||||
|||||||



Federal Office for Information Security 

11 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(6) from|1,|Check that Certificate policies are approved by the CA|||☐Pass|
|Section||in accordance to section 7.2.1 (6) of ISO 27099.|||☐Fail|
||4|||||
|7.2.1|||||☐Not applicable|
|||||||
|||||||
|(7) from|1,|Check that the CA makes available  its certificate|||☐Pass|
|Section||policies to all appropriate subscribers and relying|||☐Fail|
||4|||||
|7.2.1||parties.|||☐Not applicable|
|||||||
|2.2.1A1|1,<br>4|person of the CA.|||☐Pass<br>☐Fail<br>☐Not applicable|
|2.2.1A2|1|Check that the key and certificate management life cycle<br>processes of the CA are specified comprehensively in the<br>Check that at least the following aspects are covered:<br>•<br>reference to a document owner for CP related<br>issues<br>•<br>unique document identification for further<br>reference, i.e. by exact document title, version and<br>unique policy identifier<br>for<br>reference in<br>certificates issued by the CA<br>•<br>limitations concerning subscribers of the PKI (e.g.<br>company or administration specific PKIs)<br>•<br>application context of the PKI<br>•<br>description of subscriber registration procedures<br>including specification of registration data,<br>requirements<br>for<br>data<br>transmission,<br>and<br>description of verification procedures of the CA<br>or RA|<br>||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

12 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|||•<br>subscriber obligations (e.g. requirements on<br>subscriber<br>key<br>stores<br>and<br>application<br>environment)<br>•<br>specification of certificate profiles<br>•<br>validation model of the PKI, need of certificate<br>validation by checking signature and fingerprints<br>•<br>certificate<br>revocation<br>procedures<br>including<br>revocation reasons, revocation authorization,<br>revocation<br>application<br>mechanisms<br>(if<br>supported)<br>•<br>certificate status information services<br>`o`<br>CRLs (if supported)<br>`o`<br>OCSP (if supported)<br>•<br>directory service (if supported)<br>•<br>key lifecycle security measures<br>•<br>certificate renewal procedures (if supported)<br>•<br>CA termination<br>•<br>CP update procedures||||
||4|Check that the key and certificate management life cycle|<br>||☐Pass|
|||processes of the CA are specified comprehensively in the|||☐Fail|
|||||||
||||||☐Not applicable|
|||||||
|||Check that at least the following aspects are covered:||||
|||•<br>reference to a document owner for CP related||||
|||issues||||



Federal Office for Information Security 

13 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|||•<br>unique document identification for further||||
|||reference, i.e. by exact document title, version and||||
|||unique policy identifier<br>for<br>reference in||||
|||certificates issued by the CA||||
|||•<br>limitations concerning subscribers of the PKI (e.g.||||
|||company or administration specific PKIs)||||
|||•<br>application context of the PKI||||
|||•<br>description of subscriber registration procedures||||
|||including specification of registration data,||||
|||requirements<br>for<br>data<br>transmission,<br>and||||
|||description of verification procedures of the CA||||
|||or RA||||
|||•<br>subscriber obligations (e.g. requirements on||||
|||subscriber<br>key<br>stores<br>and<br>application||||
|||environment)||||
|||•<br>specification of certificate profiles and request||||
|||format||||
|||•<br>validation model of the PKI, need of certificate||||
|||validation by checking signature and fingerprints||||
|||•<br>certificate<br>revocation<br>procedures<br>including||||
|||revocation reasons, revocation authorization,||||
|||revocation<br>application<br>mechanisms<br>(if||||
|||supported)||||
|||•<br>certificate status information services||||
|||`o`<br>CRLs (if supported)||||
|||`o`<br>OCSP (if supported)||||



Federal Office for Information Security 

14 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|||•<br>directory service (if supported)||||
|||•<br>key lifecycle security measures||||
|||•<br>CA termination||||
|||•<br>CP update procedures||||



## 2.2.2 Certification practice statement management 

Control procedures referenced in this Section refer to Section 7.2.2 of (ISO27099). In order to provide an adequate Certification practice statement, the following control procedures SHALL be fulfilled as requirements: 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(1) from|1,|described in|||☐Pass|
|Section||is fully compliant with the requirements|||☐Fail|
||4|||||
|7.2.2||of the CP.|||☐Not applicable|
|||||||
|||||||
|(2) from|1,|Check that the CA ensures that a CPS is in place,|||☐Pass|
|Section||describing at least the requirements as defined in|||☐Fail|
||4|||||
|7.2.2||section 7.2.2 (2) of ISO 27099. The auditor must check|||☐Not applicable|
|||each requirement listed in section 7.2.2 (2), thus the||||
|||||||
|||enumeration (a), (b), (c) is substituted by (i), (ii), (iii)||||
|||||||
|||according to this TS.||||
|||||||
|(3) from|1,|Check that the CA has a review and approval process|||☐Pass|
|Section||for its CPS, including any changes.|||☐Fail|
||4|||||
|7.2.2|||||☐Not applicable|
|||Check that the responsibilities for maintaining the CPS||||
|||||||
|||are clearly defined.||||
|||||||



Federal Office for Information Security 

15 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(4) from|1,|Check that the CA provides its CPS to all appropriate|||☐Pass|
|Section||parties.|||☐Fail|
||4|||||
|7.2.2|||||☐Not applicable|
|||||||
|||||||
|(5) from|1,|Check that the CA ensures to revise its CPS according|||☐Pass|
|Section||to the requirements as defined in section 7.2.2 (5) of ISO|||☐Fail|
||4|||||
|7.2.2||27099.|||☐Not applicable|
|||||||
|(6) from|1,|Check that the CA provides revisions to the CA's CPS to|||☐Pass|
|Section||all appropriate parties.|||☐Fail|
||4|||||
|7.2.2|||||☐Not applicable|
|||||||
|||||||
|(7) from|1,|of all|||☐Pass|
|Section||controls as defined in section 7.2.2 (7) of ISO 27099. All|||☐Fail|
||4|||||
|7.2.2||controls shall be checked by the auditor, thus the|||☐Not applicable|
|||enumeration from (a) to (f) of section 7.2.2 (7) is||||
|||||||
|||substituted by (i) to (vi) according to this TS.||||
|||||||
|(8) from|1,||||☐Pass|
|Section|||||☐Fail|
||4|||||
|7.2.2|||||☐Not applicable|
|||||||
|(9) from|1,||||☐Pass|
|Section|||||☐Fail|
||4|(i) is defined by the CA,||||
|7.2.2|||||☐Not applicable|
|||(ii) approved by management of the CA,||||
|||||||
|||(iii) published and communicated to employees||||
|||and relevant external parties.||||
|(11) from|<br>1,|Check that the CA remains responsible for writing and|||☐Pass|
|Section||maintaining the CPS, in case the CA delegates some of|||☐Fail|
||4|||||
|7.2.2||its services or functions to separate component service|||☐Not applicable|
|||providers.||||
|||||||



Federal Office for Information Security 

16 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|2.2.2A1|1,<br>4|Check that the CPS includes a reference to a document<br>owner responsible for the document management.|||☐Pass<br>☐Fail<br>☐Not applicable|
|2.2.2A2|1,<br>4|Check that CPS includes a section with document<br>identification of the CPS for further reference, i.e. by<br>exact document title, version and unique policy<br>identifier of the CP which the CPS is corresponding to.|||☐Pass<br>☐Fail<br>☐Not applicable|
|2.2.2A3|1,<br>4|Check that the CPS documents all security measures<br>and server and network configurations.|||☐Pass<br>☐Fail<br>☐Not applicable|



## 2.2.3 Requirements for relying parties and subscribers of the CA 

Control procedures referenced in this Section refer to Section 7.2.3 of (ISO27099). Concerning requirements for relying parties and subscribers of the CA, the following control procedures SHALL be fulfilled as requirements: 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(1) from|1,|Check that requirement according to section 7.2.3 (1) of|||☐Pass|
|Section||ISO 27099 is fulfilled.|||☐Fail|
||4|||||
|7.2.3|||||☐Not applicable|
|||||||
|||||||
|(2) from|1,|Check that requirement of to section 7.2.3 (2) of ISO|||☐Pass|
|Section||27099 is fulfilled.|||☐Fail|
||4|||||
|7.2.3|||||☐Not applicable|
|||||||
|||||||
|(6) from|1,|Check that the subscriber agreement specifies the|||☐Pass|
|Section||requirements for notification of the CA concerning any|||☐Fail|
||4|||||
|7.2.3||event that affects the certificate validity.|||☐Not applicable|
|||||||



Federal Office for Information Security 

17 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|2.2.3A1|1,<br>4|Check that the CA makes each version of its Terms and<br>Conditions available to its subscribers and relying<br>parties.|||☐Pass<br>☐Fail<br>☐Not applicable|
|2.2.3A2|1,<br>4|Conditions is uniquely identifiable, e.g. by a unique<br>version number contained in the text.|||☐Pass<br>☐Fail<br>☐Not applicable|
|2.2.3A3|1,<br>4|Check that the CA oblige the subscribers and advise the<br>relying parties, e.g. within its CP or Terms and<br>Conditions, to validate the CA certificate and the<br>subscriber certificates.|||☐Pass<br>☐Fail<br>☐Not applicable|
|2.2.3A4|1,<br>4|Check that the dissemination of Terms and Conditions<br>is protected from manipulation.|||☐Pass<br>☐Fail<br>☐Not applicable|



## 2.3 Information security policy 

Control procedures referenced in this Section refer to Section 7.3 of (ISO27099). Concerning the information security the following control procedures SHALL be fulfilled as requirements: 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(1) from|1,|Check that an information security policy document|||☐Pass|
|Section||fulfils all the requirements as defined in section 7.3 (1)|||☐Fail|
||4|||||
|7.3||of ISO 27099. The auditor must check each|||☐Not applicable|
|||requirement listed in section 7.3 (1) of ISO 27099||||
|||||||
|||separately, thus the enumeration (a), (b) of ISO 27099 is||||
|||substituted by (i), (ii) of this TS.||||



Federal Office for Information Security 

18 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(3) from|1,|Check that the information security policy includes at|||☐Pass|
|Section||least the points according to section 7.3 (3) of ISO|||☐Fail|
||4|||||
|7.3||27099. Each of the bullet points must be checked by the|||☐Not applicable|
|||auditor thus the enumeration of (a) to (f) of section 7.3.||||
|||||||
|||(3) is substituted by (i) to (vi) according to this TS.||||
|(4) from|1,|Check that requirement defined in section 7.3 (4) of|||☐Pass|
|Section||ISO27099 is fulfilled.|||☐Fail|
||4|||||
|7.3|||||☐Not applicable|
|||||||
|||||||
|(5) from|1,|Check that the requirements as defined in section 7.3|||☐Pass|
|Section||(5) of ISO 27099 is fulfilled.|||☐Fail|
||4|||||
|7.3|||||☐Not applicable|
|||||||
|||||||
|(6) from|1,|Check that there exists a risk management system and|||☐Pass|
|Section||all requirements according to section 7.3 (6) of ISO|||☐Fail|
||4|||||
|7.3||27099 are fulfilled.|||☐Not applicable|
|||||||
|(7) from|1,|Check that requirement 7.3 (7) of ISO 27099 is fulfilled.|||☐Pass|
|Section|||||☐Fail|
||4|||||
|7.3|||||☐Not applicable|
|||||||
|(12) from|<br>1,|If the CA outsources the management and control of all|||☐Pass|
|Section||or some of its information systems, networks or|||☐Fail|
||4|||||
|7.3||desktop environment check that all security|||☐Not applicable|
|||requirements of section 7.3 (12) of ISO 27099 are met.||||
|||||||
|(13) from|<br>1,|If the CA chooses to delegate a portion of the CA roles|||☐Pass|
|Section||and respective functions to another party, check that|||☐Fail|
||4|||||
|7.3||requirement in section 7.3 (13) of ISO 27099 is fulfilled.|||☐Not applicable|
|||||||
|(14) from|<br>1,|Check that processes operated by subcontractors are|||☐Pass|
|Section||subject to applicable requirements from this document.|||☐Fail|
||4|||||
|7.3|||||☐Not applicable|
|||||||
|||||||



Federal Office for Information Security 

19 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(15) from|<br>1,|Check that requirement 7.3 (15) of ISO 27099 is fulfilled.|||☐Pass|
|Section|||||☐Fail|
||4|||||
|7.3|||||☐Not applicable|
|||||||
|2.3A1|1,<br>4|Check that the CA implements and adheres to its<br>information security policy.|||☐Pass<br>☐Fail<br>☐Not applicable|



## 2.4 Asset classification and management 

Control procedures referenced in this Section refer to Section 7.4 of (ISO27099). The following control procedures SHALL be fulfilled as requirements: 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(1) from|1,|Check that for all CA assets owners are identified and|||☐Pass|
|Section||responsibility for the maintenance of appropriate|||☐Fail|
||4|||||
|7.4||controls are assigned.|||☐Not applicable|
|||||||
|(2) from|1,|Check the requirements of section 7.4 (2) of ISO 27099|||☐Pass|
|Section||are implemented.|||☐Fail|
||4|||||
|7.4|||||☐Not applicable|
|||||||
|||||||
|(3) from|1,|Check that the requirement from section 7.4 (3) of ISO|||☐Pass|
|Section||27099 is fulfilled.|||☐Fail|
||4|||||
|7.4|||||☐Not applicable|
|||||||
|||||||
|||||||
|(4) from|1,|Check that the procedures according to section 7.4 (4)|||☐Pass|
|Section||of ISO 27099 are defined.|||☐Fail|
||4|||||
|7.4|||||☐Not applicable|
|||||||
|||||||



Federal Office for Information Security 

20 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(5) from|1,|Check that procedures for the management of|||☐Pass|
|Section||removable computer media are as defined in section|||☐Fail|
||4|||||
|7.4||7.4. (5) of ISO 27099. The auditor must check each listed|||☐Not applicable|
|||requirement of section 7.4 (5), thus the enumeration||||
|||||||
|||from (a) to (c) of ISO 27099 is substituted by||||
|||enumeration (i) to (iii) as defined in this TS.||||
|(6) from|1,|Check that all requirements for storage devices as|||☐Pass|
|Section||defined in section 7.4 (6) of ISO 27099 are fulfilled.|||☐Fail|
||4|||||
|7.4|||||☐Not applicable|
|||||||
|||||||
|||||||
|(7) from|1,|If applicable, check that the CA implements procedures|||☐Pass|
|Section||for the archiving of information on subscribers and|||☐Fail|
||4|||||
|7.4||their certificates sufficient for the certificate renewal,|||☐Not applicable|
|||re-keying, and update processes.||||
|||||||



## 2.5 Human resources security 

Control procedures referenced in this Section refer to Section 7.5 of (ISO27099). Concerning the trustworthiness of personnel, the following control procedures SHALL be fulfilled as requirements: 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(1) from|1,|Check that it is ensured that the selected CA employs|||☐Pass|
|Section||personnel having the necessary knowledge, experience|||☐Fail|
||4|||||
|7.5||and skills to carry out the work.|||☐Not applicable|
|||||||



Federal Office for Information Security 

21 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(2) from|1,|Check that the security roles and responsibilities, as|||☐Pass|
|Section||specified in the organization's security policy, are|||☐Fail|
||4|||||
|7.5||documented.|||☐Not applicable|
|||||||
|||Check that trusted roles, on which the security of the||||
|||CA's operation is dependent, are clearly identified.||||
|(3) from|1,|Check that trusted roles at least include roles that|||☐Pass|
|Section||involve the following responsibilities as defined in|||☐Fail|
||4|||||
|7.5||section 7.5 (3) from ISO 27099. The auditor must check|||☐Not applicable|
|||each listed responsibility defined in section 7.5 (3), thus||||
|||||||
|||the enumeration of (a) to (h) of ISO 27099 is substituted||||
|||||||
|||by (i) to (viii) according to this TS.||||
|(4) from|1,|Check that all requirements in section 7.5 (4) as defined|||☐Pass|
|Section||in ISO 27099 is fulfilled.|||☐Fail|
||4|||||
|7.5|||||☐Not applicable|
|||||||
|||||||
|||||||
|(5) from|1,|Check that an individual`s trusted status has been|||☐Pass|
|Section||approved before granting access to systems/facilities or|||☐Fail|
||4|||||
|7.5||performing actions that require trusted status.|||☐Not applicable|
|||||||
|(6) from|1,|Check that contractors who perform trusted roles|||☐Pass|
|Section||undergo the same background checks and personal|||☐Fail|
||4|||||
|7.5||management procedures as employees.|||☐Not applicable|
|||||||
|||||||
|(8) from|1,|Check that a disciplinary process exists and be followed|||☐Pass|
|Section||as defined in section 7.5 (8) of ISO 27099.|||☐Fail|
||4|||||
|7.5|||||☐Not applicable|
|||||||
|||||||



Federal Office for Information Security 

22 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(9) from|1,|Check that CA ensures to take appropriate timely|||☐Pass|
|Section||action as defined in section 7.5 (9) of ISO 27099.|||☐Fail|
||4|||||
|7.5|||||☐Not applicable|
|||||||
|||||||
|(11) from|<br>1,|Check that requirement 7.5 (11) of ISO 27099 is fulfilled.|||☐Pass|
|Section|||||☐Fail|
||4|||||
|7.5|||||☐Not applicable|
|||||||
|2.5A1|1,<br>4|Check that the responsibilities bound to the roles at the<br>CA and RA, and the boundaries of each of these<br>responsibilities are well-defined in order to enable a<br>clear structure in staff organization at the CA and RA.|||☐Pass<br>☐Fail<br>☐Not applicable|



## 2.6 Physical and environmental security 

Control procedures referenced in this Section refer to Section 7.6 of (ISO27099). Concerning the physical and environmental security, the following control procedures SHALL be fulfilled as requirements: 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(3) from|1,|Check that access to the building or site housing CA|||☐Pass|
|Section||operations is restricted as defined in section 7.6 (3) of|||☐Fail|
||4|||||
|7.6||ISO 27099.|||☐Not applicable|
|||||||
|||||||
|(4) from|1,|Check that physical barriers are in place (e.g. solid walls|||☐Pass|
|Section||that extend from real floor to real ceiling) are in place|||☐Fail|
||4|||||
|7.6||to prevent unauthorised access and environmental|||☐Not applicable|
|||contamination to the CA's certificate manufacturing||||
|||||||
|||facility.||||
|||||||



Federal Office for Information Security 

23 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(5) from|1,|Check that physical barriers and protection against|||☐Pass|
|Section||radiant emission (e.g. Faraday cage) and the|||☐Fail|
||4|||||
|7.6||requirements as defined in section 7.6 (5) of ISO 27099|||☐Not applicable|
|||are in place.||||
|||||||
|(8) from|1,|Check that access to CA operational facilities is secured|||☐Pass|
|Section||according to section 7.6 (8) of ISO 27099.|||☐Fail|
||4|||||
|7.6|||||☐Not applicable|
|||||||
|||||||
|(10) from|<br>1,|Check that all entrance and leavings of personal to CAs|||☐Pass|
|Section||operational facilities is locked according to ISO 27099|||☐Fail|
||4|||||
|7.6||section 7.6 (10).|||☐Not applicable|
|||||||
|(11) from|<br>1,|Check that visitors to CA facilities are supervised and|||☐Pass|
|Section||records are taken as defined in section 7.6 (11) of ISO|||☐Fail|
||4|||||
|7.6||27099.|||☐Not applicable|
|||||||
|(12) from|<br>1,|Check that, the restrictions on personal of third party|||☐Pass|
|Section||support service are enforced as defined in section 7.6|||☐Fail|
||4|||||
|7.6||(12) from ISO 27099.|||☐Not applicable|
|||||||
|||||||
|(13) from|<br>1,|Check that access rights to CA facilities are regularly|||☐Pass|
|Section||updated and reviewed.|||☐Fail|
||4|||||
|7.6|||||☐Not applicable|
|||||||
|||||||
|(14) from|<br>1,||||☐Pass|
|Section||identified as critical to the security of its operations are|||☐Fail|
||4|||||
|7.6||within a physically secure boundary that physically|||☐Not applicable|
|||restricts access by unauthorised personnel.||||
|||||||
|(17) from|<br>1,|Check that the requirement (17) of section 7.6 from ISO|||☐Pass|
|Section||27099 is fulfilled.|||☐Fail|
||4|||||
|7.6|||||☐Not applicable|
|||||||
|||||||



Federal Office for Information Security 

24 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(20) from|<br>1,|Check that all requirements of storage media as defined|||☐Pass|
|Section||in section 7.6 (20) of ISO 27099 are implemented.|||☐Fail|
||4|||||
|7.6|||||☐Not applicable|
|||||||
|||||||
|(21) from|<br>1,|Check that the CA implements the controls as defined|||☐Pass|
|Section||in section 7.6 (21) of ISO 27099.|||☐Fail|
||4|||||
|7.6|||||☐Not applicable|
|||||||
|||||||
|(24) from|<br>1,|Check that procedures as defined in section 7.6 (24) of|||☐Pass|
|Section||ISO 27099 are place.|||☐Fail|
||4|||||
|7.6|||||☐Not applicable|
|||||||
|||||||
|(25) from|<br>1,|Check that physical access to the secure cryptographic|||☐Pass|
|Section||device is only possible under multiple controls, which|||☐Fail|
||4|||||
|7.6||are limited to authorised entities. .|||☐Not applicable|
|||||||
|2.6A1|1,<br>4|Check that physical access to CA facilities is limited to<br>authorized individuals.<br>For virtualised environments, check that the CA<br>software is isolated from other software and access is<br>limited to authorized individuals.|||☐Pass<br>☐Fail<br>☐Not applicable|
|2.6A2|1,<br>4|Check that security levels are defined for the premises<br>of the CA, CA facilities, supplying facilities and/or parts<br>of them.<br>Check that the access to the security levels is defined by<br>an access list and is reviewed regularly.<br>Check that the physical protection is ensured by clearly<br>defined security perimeters for the defined security<br>levels.|<br> <br>||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

25 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|2.6A3|1,<br>4|Check that all premises shared with external<br>organizations are outside of the security perimeters.|||☐Pass<br>☐Fail<br>☐Not applicable|
|2.6A4|1,<br>4|Check that continuous power supply is ensured for all<br>critical processes by an uninterruptible power supply<br>(UPS) system.|||☐Pass<br>☐Fail<br>☐Not applicable|



## 2.7 Operational security 

Control procedures referenced in this Section refer to Section 7.7 of (ISO27099). The following control procedures SHALL be fulfilled as requirements: 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(1) from|1,|Check that the CA operating procedures are|||☐Pass|
|Section||documented and maintained for each functional area.|||☐Fail|
||4|||||
|7.7|||||☐Not applicable|
|||||||
|||||||
|(2) from|1,|Check that formal management responsibilities and|||☐Pass|
|Section||procedures exist as defined in section 7.7 (2) according|||☐Fail|
||4|||||
|7.7||to ISO 27099.|||☐Not applicable|
|||||||
|(3) from|1,|Check that the requirements according to section 7.7|||☐Pass|
|Section||(3) of ISO 27099 is fulfilled.|||☐Fail|
||4|||||
|7.7|||||☐Not applicable|
|||||||
|||||||
|(4) from|1,|Check that the requirements on development and|||☐Pass|
|Section||testing facilities are as defined in section 7.7 (4) from|||☐Fail|
||4|||||
|7.7||ISO 27099.|||☐Not applicable|
|||||||



Federal Office for Information Security 

26 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(5) from|1,|Check that capacity demands are monitored, and|||☐Pass|
|Section||projections of future capacity requirements are made|||☐Fail|
||4|||||
|7.7||to ensure that adequate processing power and storage|||☐Not applicable|
|||are available.||||
|||||||
|(6) from|1,|Check that acceptance criteria for new information|||☐Pass|
|Section||systems, upgrades and new versions are established|||☐Fail|
||4|||||
|7.7||and that suitable tests of the system carried out prior to|||☐Not applicable|
|||acceptance.||||
|||||||
|(7) from|1,|Check that detection and prevention controls against|||☐Pass|
|Section||malware and viruses are implemented and check that|||☐Fail|
||4|||||
|7.7||appropriate awareness programmes are in place as|||☐Not applicable|
|||defined in section 7.7 (7) of ISO 27099.||||
|||||||
|(8) from|1,|Check that all requirements on incident reporting|||☐Pass|
|Section||procedures and documentations are existing and|||☐Fail|
||4|||||
|7.7||implemented as defined in section 7.7 (8) from ISO|||☐Not applicable|
|||27099.||||
|||||||
|(9) from|1,|Check that reactions by the CA are planted in case|||☐Pass|
|Section||security relevant algorithms or processes are|||☐Fail|
||4|||||
|7.7||broken/insecure as defined in section 7.7 (9) of ISO|||☐Not applicable|
|||27099.||||
|||||||
|(10) from|<br>1,|Check that the CA ensures timely, appropriate reaction|||☐Pass|
|Section||to incidents.|||☐Fail|
||4|||||
|7.7|||||☐Not applicable|
|||||||
|||||||
|(11) from|<br>1,|Check that users of CA systems with trusted roles are|||☐Pass|
|Section||required to note and report observed or suspected|||☐Fail|
||4|||||
|7.7||security weaknesses in, or threats to, systems or|||☐Not applicable|
|||services to ensure an appropriate response to a security||||
|||||||
|||incident.||||



Federal Office for Information Security 

27 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(12) from|<br>1,|Check that procedures exist and are followed as|||☐Pass|
|Section||defined in section 7.7 (12) of ISO 27099.|||☐Fail|
||4|||||
|7.7|||||☐Not applicable|
|||||||
|||||||
|(13) from|<br>1,|Check that procedures exist and are followed as|||☐Pass|
|Section||defined in section 7.7 (13) according to ISO 27099.|||☐Fail|
||4|||||
|7.7|||||☐Not applicable|
|||||||
|||||||
|(14) from|<br>1,|Check that a formal problem management process|||☐Pass|
|Section||exists that fulfils the requirements as defined in section|||☐Fail|
||4|||||
|7.7||7.7 (14) of ISO 27099.|||☐Not applicable|
|||||||
|(15) from|<br>1,|Check that the CA ensures that any security breach|||☐Pass|
|Section||results in an appropriate countermeasure to limit the|||☐Fail|
||4|||||
|7.7||impact in a timely and coordinated manner.|||☐Not applicable|
|||||||
|2.7A1|1|Check that an analysis of the estimated usage of the CA<br>services is done before setting-up the technical<br>infrastructure.<br>Check that the performance of the technical<br>infrastructure is sufficient for the requirements and<br>scalable without interrupting the continuous<br>operation.|||☐Pass<br>☐Fail<br>☐Not applicable|
||4|Check that the CA provides a degree of availability of|||☐Pass|
|||its services towards its subscribers tailored appropriate|||☐Fail|
|||||||
|||to the interval of certificate issuing.|||☐Not applicable|
|||||||
|||||||
|2.7A2|1,<br>4|Check that written procedures exist for all operational<br>CA processes, including the information of the<br>associated roles.|||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

28 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|2.7A3|1,<br>4|Check that persons who are involved in the registration<br>process of applicants are not involved in the certificate<br>generation process or vice versa.|||☐Pass<br>☐Fail<br>☐Not applicable|
|2.7A4|1,<br>4|Check that the CA employs sufficient personnel for all<br>critical services.|||☐Pass<br>☐Fail<br>☐Not applicable|
|2.7A5|1,<br>4|Check that penetration testing is conducted regularly,<br>in a period of [assignment: number of days, weeks or<br>months].|||☐Pass<br>☐Fail<br>☐Not applicable|
|2.7A6|1|Check that the CA defines the maximal tolerable<br>downtime of each service.<br>Check that the CA tailors the services appropriately.|||☐Pass<br>☐Fail<br>☐Not applicable|
||4|Check that the CA defines the maximal tolerable|||☐Pass|
|||downtime of each service.|||☐Fail|
|||||||
||||||☐Not applicable|
|||Check that the CA tailors the services appropriately.||||
|||||||
|||Particularly check that the service treating the||||
|||suspension of certificates shall ensure to process||||
|||inquiries and updates within [assignment: number of||||
|||hours] hours.||||



## 2.8 Access control 

Control procedures referenced in this Section refer to Section 7.8 of (ISO27099). 

Federal Office for Information Security 

29 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(1) from|1,|Check that the access control requirements are|||☐Pass|
|Section 7.8||defined and documented in an access control|||☐Fail|
||4|||||
|||policy which should include at least the criteria|||☐Not applicable|
|||||||
|||defined in section 7.8 (1) of ISO 27099. The auditor||||
|||shall check each requirement, thus the||||
|||enumeration (a) to (d) from section 7.8 (1) is||||
|||substituted by (i) to (iv) of this TS.||||
|(2) from|1,|Check that there is a formal, trusted procedure for|||☐Pass|
|Section 7.8||registering and deregistering users of the CA's|||☐Fail|
||4|||||
|||information systems and services.|||☐Not applicable|
|||||||
|||||||
|(3) from|1,|Check that section 7.8 (3) of ISO 27099 is followed.|||☐Pass|
|Section 7.8|||||☐Fail|
||4|||||
||||||☐Not applicable|
|||||||
|(5) from|1,|Check that reviewing of access right for user with|||☐Pass|
|Section 7.8||trusted roles is done as defined in section 7.8 (5)|||☐Fail|
||4|||||
|||from ISO 27099.|||☐Not applicable|
|||||||
|||||||
|(10) from|1,|Check that controls for network protection for the|||☐Pass|
|Section 7.8||internal CA<br>network domain is in place in|||☐Fail|
||4|||||
|||accordance with ISO 27099 section 7.8 (10).|||☐Not applicable|
|||||||
|||||||
|(11) from|1,|Check that all requirements as defined in section|||☐Pass|
|Section 7.8||7.8 (11) of ISO 27099 are fulfilled.|||☐Fail|
||4|||||
||||||☐Not applicable|
|||||||
|||||||
|(13) from|1,|Check that all local network components are kept|||☐Pass|
|Section 7.8||inside a secure area and their configurations are|||☐Fail|
||4|||||
|||regularly audited for conformance, as specified in|||☐Not applicable|
|||||||
|||section 7.8. (13) of ISO 27099.||||



Federal Office for Information Security 

30 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(15) from|1,|Check that the CA monitors access to its system to|||☐Pass|
|Section 7.8||detect unauthorized access as defined in section 7.8|||☐Fail|
||4|||||
|||(15) of ISO 27099.|||☐Not applicable|
|||||||
|||||||
|||||||
|(16) from|1,|Check that all requirements according to section|||☐Pass|
|Section 7.8||7.8 (16) of ISO 27099 are fulfilled.|||☐Fail|
||4|||||
||||||☐Not applicable|
|||||||
|(17) from|1,||||☐Pass|
|Section 7.8||configured as defined in section 7.8 (17) of ISO|||☐Fail|
||4|||||
|||27099.|||☐Not applicable|
|||||||
|||||||
|(18) from|1,|Check that operating system patches and updates|||☐Pass|
|Section 7.8||are applied as defined in section 7.8 (18) of ISO|||☐Fail|
||4|||||
|||27099.|||☐Not applicable|
|||||||
|||||||
|(19) from|1,|Check that access to CA systems requires a|||☐Pass|
|Section 7.8||protected log-on process.|||☐Fail|
||4|||||
||||||☐Not applicable|
|||||||
|(20) from|1,|Check that all requirements according to section|||☐Pass|
|Section 7.8||7.8 (20) of ISO 27099 are fulfilled.|||☐Fail|
||4|||||
||||||☐Not applicable|
|||||||
|||||||
|(21) from|1,|Check that uses of system utility programmes are|||☐Pass|
|Section 7.8||restricted to authorized personnel and are tightly|||☐Fail|
||4|||||
|||controlled as defined in section 7.8 (21) of ISO|||☐Not applicable|
|||||||
|||27099.||||
|(23) from|1,|Check that the CA servers used for certificate|||☐Pass|
|Section 7.8||manufacturer is configured as defined in section|||☐Fail|
||4|||||
|||7.8 (23) of ISO 27099.Check that this covers|||☐Not applicable|
|||||||
|||configuration and settings as defined in ISO 27099,||||
|||section 7.8 (23).||||



Federal Office for Information Security 

31 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(25) from|1,|Before using critical applications, check that CA|||☐Pass|
|Section 7.8||personal is successfully identified and|||☐Fail|
||4|||||
|||authenticated according section 7.8 (25) of ISO|||☐Not applicable|
|||||||
|||27099.||||
|(26) from|1,|Check that requirement for sensitive systems (e.g.|||☐Pass|
|Section 7.8||root CA) according to section 7.8 (26) as defined in|||☐Fail|
||4|||||
|||ISO 27099 is fulfilled.|||☐Not applicable|
|||||||
|||||||
|2.8A1|1,<br>4|Check that staff employed by the CA does not have<br>access to any service for which they are not<br>explicitly authorized to use.|||☐Pass<br>☐Fail<br>☐Not applicable|



## 2.9 System acquisition, development and maintenance 

Control procedures referenced in this Section refer to Section 7.9 of (ISO27099). The following control procedures SHALL be fulfilled as requirements: 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(2) from|1,|Check that software testing and change control|||☐Pass|
|Section||procedures exist and are followed as defined in section|||☐Fail|
||4|||||
|7.9||7.9 (2) of ISO 27099.|||☐Not applicable|
|||||||
|(3) from|1,|Check that change control procedures are in place and|||☐Pass|
|Section||followed for the hardware, network component and|||☐Fail|
||4|||||
|7.9||system configuration changes.|||☐Not applicable|
|||||||
|(5) from|1,|Check that, after operating system changes have|||☐Pass|
|Section||occurred, that they are reviewed and tested.|||☐Fail|
||4|||||
|7.9|||||☐Not applicable|
|||||||
|||||||



Federal Office for Information Security 

32 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|2.9A1|1,<br>4|Check that Test PKI operations are operated strictly<br>separated from productive PKI operations.|||☐Pass<br>☐Fail<br>☐Not applicable|
|2.9A2|1,<br>4|Check that a productive CA does not issue test<br>certificates.|||☐Pass<br>☐Fail<br>☐Not applicable|



## 2.10 Business continuity management 

Control procedures referenced in this Section refer to Section 7.10 of (ISO27099). Concerning business continuity management the following control procedures SHALL be fulfilled as requirements: 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(1) from|1,|Check that all requirements from section 7.10 (1) of ISO<br>27099 are followed.|||☐Pass|
|Section|||||☐Fail|
||4|||||
|7.10|||||☐Not applicable|
|||||||
|(2) from|1,|Check that the CA has a business continuity plan to|||☐Pass|
|Section|||||☐Fail|
||4|||||
|7.10||manner following interruption to, or failure of, critical|||☐Not applicable|
|||CA processes that shall include all the points outlined||||
|||||||
|||in section 7.10 (2) from ISO 27099. The auditor shall||||
|||check each requirement listed in section 7.10 (2) of ISO||||
|||27099 , thus the enumeration (a) to (j) from section 7.10||||
|||(2) is substituted by (i) to (x) of this TS.||||
|(3) from|1,|Check that the CA's business continuity plans cover all|||☐Pass|
|Section||critical components (i.e. hardware, software and keys)|||☐Fail|
||4|||||
|7.10||and include measures for recovering from the|||☐Not applicable|
|||compromise or loss of CAprivate keys. These measures||||
|||||||



Federal Office for Information Security 

33 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|||a), b) as defined in section 7.10.(3) of ISO 27099 may be||||
|||applied.||||
|(4) from|1,|Check that all requirements for backup copies of|||☐Pass|
|Section||essential business information according to section|||☐Fail|
||4|||||
|7.10||7.10 (4) of ISO 27099 applies.|||☐Not applicable|
|||||||
|(6) from|1,||||☐Pass|
|Section||procedures for securing its facility to the fullest extent|||☐Fail|
||4|||||
|7.10||possible during the period of time following a disaster|||☐Not applicable|
|||and prior to restoring a secure environment either at||||
|||||||
|||the original site or a remote site.||||
|(9) from|1,|Check the effectiveness of business continuity plans by|||☐Pass|
|Section||carrying out regular reviews and updates in accordance|||☐Fail|
||4|||||
|7.10||with section 7.10. (9) of ISO 27099.|||☐Not applicable|
|||||||
|2.10A1|1,<br>4|Check that the CA ensures that after an incident the<br>security vulnerability, which caused the incident, is<br>fixed or sufficiently mitigated.<br>Check that afterwards a timely restart of the services is<br>processed.|||☐Pass<br>☐Fail<br>☐Not applicable|
|2.10A2|1,<br>4|Check that for each defined role there is at least one<br>substitute to limit negative effects on the process-flow<br>conducted at the CA if an individual is unavailable to<br>fulfil his or her role.|||☐Pass<br>☐Fail<br>☐Not applicable|
|2.10A3|1,<br>4|Check that data regarding CA operation is backed-up.<br>Check that this backup ensures the operation of the CA<br>in case of an emergency.|||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

34 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|||Check that at least the backups of critical data are<br>realized physically separated from regular operations.||||



## 2.11 Monitoring, conformance and compliance 

Control procedures referenced in this Section refer to Section 7.11 of (ISO27099). The following control procedures SHALL be fulfilled as requirements: 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(4) from|1,|Check those records that are relevant for monitoring|||☐Pass|
|Section||and conformance are protected from loss, destruction,|||☐Fail|
||4|||||
|7.11||and falsification.|||☐Not applicable|
|||||||
|(6) from|1,||||☐Pass|
|Section||review to ensure it is in accordance with its CPS.|||☐Fail|
||4|||||
|7.11|||||☐Not applicable|
|||||||
|||||||
|(8) from|1,|Check that procedures for CA system usage have been|||☐Pass|
|Section||established as defined in section 7.11 (8) of ISO 27099.|||☐Fail|
||4|||||
|7.11|||||☐Not applicable|
|||Check that alerting mechanisms are implemented to||||
|||||||
|||detect both unauthorized access and unauthorized||||
|||modification attempts.||||



## 2.12 Audit journal security and archiving 

Control procedures referenced in this Section refer to Section 7.12 of (ISO27099). Concerning the archiving and tracking of relevant events, the following control procedures SHALL be fulfilled as requirements: 

Federal Office for Information Security 

35 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(1) from|1,|Check that the CA generates automatic (electronic) and|||☐Pass|
|Section||manual audit logs as stated and required by the|||☐Fail|
||4|||||
|7.12||certificate policy.|||☐Not applicable|
|||||||
|(2) from|1,|Check that all journey entries must include date and|||☐Pass|
|Section||time of the entry and check that all elements as|||☐Fail|
||4|||||
|7.12||mentioned in section 7.12 (2) from ISO 27099 are|||☐Not applicable|
|||included in the journey, if relevant. The auditor must||||
|||||||
|||check all listed requirements of section 7.12 (2)||||
|||separately, thus the enumeration from (a) to (c) of ISO||||
|||27099 is substituted by (i) to (iii) according to this TS.||||
|(3) from|1,|Check that all the archived audit logs are secured as|||☐Pass|
|Section||defined in section 7.12 (3) of ISO 27099.|||☐Fail|
||4|||||
|7.12|||||☐Not applicable|
|||||||
|||||||
|(4) from|1,|Check that the CA implements an audit trail with the|||☐Pass|
|Section||purpose to identify evidence of any malicious activities.|||☐Fail|
||4|||||
|7.12|||||☐Not applicable|
|||Check that the roles and responsibilities for regularly||||
|||||||
|||monitoring and reviewing these audit logs are clearly||||
|||defined.||||
|(8) from|1|Check that the CA logs (or require that the RA records)|||☐Pass|
|Section||the certificate application information. Check that this|||☐Fail|
|||||||
|7.12||includes all the points as defined in section 7.12 (8) of|||☐Not applicable|
|||ISO 27099. The auditor shall check each points of||||
|||||||
|||section 7.12. (8) separately , thus the enumeration (a)||||
|||(h) is substituted by (i) to (viii) according to this TS.||||
|||||||
||4|Check that the CA logs (or require that the RA records)|||☐Pass|
|||the certificate application information.|||☐Fail|
|||||||
||||||☐Not applicable|
|||||||



Federal Office for Information Security 

36 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|||Check that this includes:||||
|||(i) the method of identification applied, and||||
|||-your-||||
|||requirements;||||
|||(ii)<br>identification and registration data as defined||||
|||in the corresponding CP;||||
|||(iii)<br>identity of entity accepting the application as||||
|||defined in the corresponding CP;||||
|||(iv)<br>validation of identification documents as||||
|||defined in the corresponding CP;||||
|||(v)<br>name of receiving CA or submitting RA;||||
|||(vi)||||
|||agreement;||||
|||(vii)||||
|||keep records containing personal data and||||
|||pass this information to specified third||||
|||parties, and publication of certificates.||||
|(9) from|1|Check that the CA logs all certificate life cycle|||☐Pass|
|Section||management related events as defined in section 7.12|||☐Fail|
|||||||
|7.12||(9) from ISO 27099. The auditor shall check each|||☐Not applicable|
|||certificate life cycle event as listed in section 7.12. (9)||||
|||||||
|||from ISO 27099 separately, thus the enumeration of (a)||||
|||to (j) of ISO 27099 is substituted by (i) to (x) as defined in||||
|||the TS.||||
||4|Check that the CA logs certificate life cycle|||☐Pass|
|||management related events according to section 7.12.|||☐Fail|
|||||||
|||(9) of ISO 27099.|||☐Not applicable|
|||||||
|||Check that this includes:||||
|||(i) certificate requests;||||



Federal Office for Information Security 

37 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|||(ii) rekey requests;||||
|||(iii)<br>submissions of public keys for certification;||||
|||(iv)<br>change of registration information of an||||
|||entity;||||
|||(v)<br>generation and distribution of certificates;||||
|||(vi)||||
|||(vii)<br>requests for certificate revocation or||||
|||suspension;||||
|||(viii) revocation of a certificate that has been||||
|||issued by the CA;||||
|||(ix)<br>certificate suspension requests (if supported);||||
|||(x)<br>certificate suspension and reactivation (if||||
|||supported);||||
|||(xi)<br>generation and issuance of certificate||||
|||revocation lists (if supported).||||
|(11) from|<br>1,|Check that audit logs do not record the private keys in|||☐Pass|
|Section||any form (e.g. plaintext or enciphered).|||☐Fail|
||4|||||
|7.12|||||☐Not applicable|
|||||||
|||||||
|(12) from|<br>1,|Check that CA computer system clock requirement as|||☐Pass|
|Section||defined in 7.12 (12) of ISO 27099 is fulfilled.|||☐Fail|
||4|||||
|7.12|||||☐Not applicable|
|||||||
|||||||
|(14) from|<br>1,|Check that the length of time for audit log retention is|||☐Pass|
|Section||follows section 7.12 (14) from ISO 27099.|||☐Fail|
||4|||||
|7.12|||||☐Not applicable|
|||||||
|||||||
|(15) from|<br>1,|Check that the CA retains audit log data for the|||☐Pass|
|Section||specified period as defined in section 7.12 (15) of ISO|||☐Fail|
||4|||||
|7.12||27099.|||☐Not applicable|
|||||||



Federal Office for Information Security 

38 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(18) from|<br>1,|Check that audit logs are reviewed in accordance with|||☐Pass|
|Section||the practices established in the CPS.|||☐Fail|
||4|||||
|7.12|||||☐Not applicable|
|||||||
|||||||
|(19) from|<br>1,|Check that the review of current and archived audit|||☐Pass|
|Section||logs is done as defined in section 7.12 (19) of ISO 27099|||☐Fail|
||4|||||
|7.12||and check that all requirements mentioned in this|||☐Not applicable|
|||section applies.||||
|||||||
|2.12A1|1|Check that the CA logs CA key life cycle management<br>related events.<br>Check that this includes:<br>•<br>CA key generation;<br>•<br>manual installation of cryptographic keys (if<br>supported);<br>•<br>CA key back-up (if supported);<br>•<br>CA key storage;<br>•<br>CA key recovery (if supported);<br>•<br>CA key escrow activities (if supported);<br>•<br>CA key usage;<br>•<br>CA key archival (if supported);<br>•<br>CA key revocation (if supported);<br>•<br>CA key destruction;<br>•<br>identity of the entity authorizing a key<br>management operation;|||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

39 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|||•<br>identity of the entities handling any keying<br>material (such as key components or keys stored<br>in portable devices or media);<br>•<br>custody of keys and of devices or media holding<br>keys.||||
|2.12A2|1,<br>4|Check that audit trail data is append-only.|||☐Pass<br>☐Fail<br>☐Not applicable|
|2.12A3|1,<br>4|Check that the CA ensures that a complete set of<br>information concerning a certificate is archived.<br>Check that this set of information is<br>•<br>clearly and a priori defined,<br>•<br>stored for an a priori defined, appropriate time,<br>and<br>•<br>unambiguously be referred to a certificate.|||☐Pass<br>☐Fail<br>☐Not applicable|
|2.12A4|1|Check that the set of information to be archived and<br>the period of time for keeping the archived<br>Conditions.<br>Check that for each event to be archived, the event<br>time is recorded precisely.|||☐Pass<br>☐Fail<br>☐Not applicable|
||4|Check that the set of information to be archived and|||☐Pass|
|||the period of time for keeping the archived|||☐Fail|
|||||||
|||CP.|||☐Not applicable|
|||||||
|||Check that for each event to be archived, the event||||
|||time is recorded precisely.||||



Federal Office for Information Security 

40 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|2.12A5|1,<br>4|Check that the archived set of information, the<br>mapping onto certificates and to the registered<br>subscribers is sufficient for all applicable processes of<br>certificate renewal, re-keying and update.|||☐Pass<br>☐Fail<br>☐Not applicable|



## 2.13 Controlled CA termination 

Control procedures referenced in this Section refer to Section 7.15.9 of (ISO27099). Concerning the cessation of operation of a CA, the following control procedures SHALL be fulfilled as requirements: 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(1) from|1,|Check that a termination plan has been established|||☐Pass|
|Section||which includes all points from ISO 27099, 7.15.9. (1).|||☐Fail|
||4|||||
|7.15.9|||||☐Not applicable|
|||||||
|||||||
|(5) from|1,|Check that a termination plan has been developed to|||☐Pass|
|Section||minimise disruption. This should include notification|||☐Fail|
||4|||||
|7.15.9||to subscribers, preserving records, transferring business|||☐Not applicable|
|||to a reliable successor.||||
|||||||
|(7) from|1|Check that the CA makes certificate status information|||☐Pass|
|Section||(including certificate revocation lists and other|||☐Fail|
|||||||
|7.15.9||certificate status mechanisms) available to relevant|||☐Not applicable|
|||entities (e.g. subscribers and relying parties or their||||
|||||||
|||agents, i.e. CVSPs) using mechanism in accordance with||||
|||the CP.||||
||4|Not applicable to CAs affected by (BSI-TR-03145-4)|||☐Pass|
||||||☐Fail|
|||||||
||||||☐Not applicable<br>x|



Federal Office for Information Security 

41 

2 General requirements for Certification Authorities 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(8) from|1,|Check that the CA has a plan for the case of business|||☐Pass|
|Section||termination, that at least includes the points as defined|||☐Fail|
||4|||||
|7.15.9||in section 7.15.9 (8) from ISO 27099. The auditor shall|||☐Not applicable|
|||check each separately, thus the enumeration of 7.15.9||||
|||||||
|||(8) (a) to (e) is substituted by (i) to (v) as defined by this||||
|||TS.||||
|(9) from|1|Check that the CA ensures to inform all stakeholders|||☐Pass|
|Section||prior to its business termination.|||☐Fail|
|||||||
|7.15.9|||||☐Not applicable|
|||||||
||4|Check that sub-CA informs subscribers, subjects and|||☐Pass|
|||||||
|||the root-CA as well as other entities the sub-CA has|||☐Fail|
|||||||
|||agreements with about successor instances (i.e. third|||☐Not applicable|
|||party service providers) prior to its termination. Check||||
|||that the process of the CA termination is described in||||
|||||||
||4|Check that the CA ensures that if a subscriber of a CA|||☐Pass|
|||declares the termination of its business within the PKI,|||☐Fail|
|||||||
|||the subscriber is suspended by its CA at the termination|||☐Not applicable|
|||date.||||
||4|Check that the CA ensures that if a subscriber of a CA|||☐Pass|
|||declares the termination of its business within the PKI,|||☐Fail|
|||||||
|||the last certificate which will be issued for that|||☐Not applicable|
|||subscriber does not have the end of validity beyond the||||
|||termination date.||||
|2.13A1|1,<br>4|If no successor instance for a transition period is<br>defined and guaranteed for the case of CA termination,<br>check that the CA has a guaranteed plan for an<br>alternative secure termination of all services.|||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

42 

3 Key life cycle management 

## 3 Key life cycle management 

## 3.1 CA key life cycle management 


![](markdown/tr/TR03145-part1-4_2-0-0-specification/TR03145-part1-4_2-0-0-specification.pdf-0043-03.png)


, in particular its own private key, is 

maintained securely during the whole key life cycle. 

Please mark, if the CA uses separate key pairs with corresponding certificates to sign certificates, revocation lists and to issue OCSP signers 

## ☐ No 

## ☐ Yes 

If Yes, please mark for what the separate key pairs and corresponding certificates are used by the CA (multiple selection possible) 

☐ signing certificates 

- ☐ signing CRLs 

- ☐ issuing OCSP signers 

☐ others:____________________ 

If more than one single CA is in the scope of the audit this may have to be specified for each individual CA. 

Note that the requirements from this Section apply to all of the CA key pairs. 


![](markdown/tr/TR03145-part1-4_2-0-0-specification/TR03145-part1-4_2-0-0-specification.pdf-0043-16.png)


|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|3.1A1|1|Check that private keys of the CA are generated and<br>handled in a certified security device compliant with<br>[assignment: Security Level 2 according to (KLSR),<br>(ISO15408), equivalent, appropriate application specific<br>requirements] ensuring the claimed security features,<br>includingtamper resistance,mitigation of side|||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

43 

3 Key life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|||channels, suitable access control, random number<br>generator and security of cryptographic operations.<br>Check that appropriate access control ensures that the<br>keys are not accessible from outside.||||
||4|Check that private keys of the CA are generated, held,|||☐Pass|
|||used and deleted in a security device following the|||☐Fail|
|||||||
|||requirements of the Certificate Policy of the Root-CA|||☐Not applicable|
|||ensuring the claimed security features, including||||
|||tamper resistance, mitigation of side channels, suitable||||
|||access control, random number generator and security||||
|||of cryptographic operations.||||
|3.1A2|1,<br>4|Check that private keys of the CA are handled (e.g.<br>generated, stored, used or recovered) only by personnel<br>in trusted roles.|||☐Pass<br>☐Fail<br>☐Not applicable|



## 3.1.1 CA key generation 

Control procedures referenced in this Section refer to Section 7.13.1 of (ISO27099). procedures SHALL be fulfilled as requirements: 


![](markdown/tr/TR03145-part1-4_2-0-0-specification/TR03145-part1-4_2-0-0-specification.pdf-0044-04.png)


following control 

|Require-||Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|||||Explanations by|
||||||the Auditor|
|(3) from|1|Check that  the requirements for CA keys generation is|||☐Pass|
|Section||done as defined in section 7.13.1 (3) of ISO 27099.|||☐Fail|
|||||||
|7.13.1|||||☐Not applicable|
|||||||
||4|Check that the CA key pair generation is performed by|||☐Pass|
|||||||
|||trustworthy personnel during a key ceremony in a|||☐Fail|
|||||||
|||four-eyesprinciple under the attendance of the key|||☐Not applicable|



Federal Office for Information Security 

44 

3 Key life cycle management 

|Require-||Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|||||Explanations by|
||||||the Auditor|
|||responsible officer in a physically secured||||
|||environment.||||
|(4) from|1,|Check that generation requirements of its own key pair|||☐Pass|
|Section||by the CA are implemented and followed as defined in|||☐Fail|
||4|||||
|7.13.1||section 7.13.1 (4).|||☐Not applicable|
|||||||
|(5) from|1|Check that the CA generates keys as defined in section|||☐Pass|
|Section||7.13.1 (5) of ISO 27099. The auditor shall check each|||☐Fail|
|||||||
|7.13.1||listed requirement of section 7.13.1 (5) of ISO 27099|||☐Not applicable|
|||separately, thus the enumeration (a) to (d) of ISO 27099||||
|||||||
|||is substituted by (i) to (iv) according to this TS.||||
||4|Not applicable to CAs affected by (BSI-TR-03145-4)|||☐Pass|
||||||☐Fail|
|||||||
||||||☐Not applicable<br>x|
|(7) from|1,|Check that the operation of the user software and|||☐Pass|
|Section||cryptographic hardware is tested before going into|||☐Fail|
||4|||||
|7.13.1||production.|||☐Not applicable|
|||||||
|(10) from|<br>1,|Check that the cryptographic hardware used by the CA|||☐Pass|
|Section||is stored and used in a secure location that is only|||☐Fail|
||4|||||
|7.13.1||accessible to authorised personnel.|||☐Not applicable|
|||||||
|(12) from|<br>1,||||☐Pass|
|Section||installation, removal, servicing, repair is carried out by|||☐Fail|
||4|||||
|7.13.1||at least two authorized personnel.|||☐Not applicable|
|||||||
|3.1.1A1|1|Check that the generation of a new key pair and the<br>corresponding CA certificate is done at least<br>[assignment: number of days more than 2] days before<br>the private key usage period of the previous CA<br>certificate ends.|||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

45 

3 Key life cycle management 

|Require-||Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|||||Explanations by|
||||||the Auditor|
||4|Check that the generation of a new key pair and the|||☐Pass|
|||corresponding CA certificate is done according to the|||☐Fail|
|||||||
|||deadlines defined in the corresponding CP.|||☐Not applicable|
|||||||



## 3.1.2 CA key storage, backup, and recovery 


![](markdown/tr/TR03145-part1-4_2-0-0-specification/TR03145-part1-4_2-0-0-specification.pdf-0046-03.png)


Control procedures referenced in this Section refer to Section 7.13.2 of (ISO27099). control procedures SHALL be fulfilled as requirements: 

following 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by the|
||||||Auditor|
|(2) from|1,|If<br>all the requirements|||☐Pass|
|Section||as defined in section 7.13.2 (2) of ISO 27099 must be|||☐Fail|
||4|||||
|7.13.2||applied. The auditor must check all listed requirements|||☐Not applicable|
|||of section 7.13.2 (2) separately, thus the enumeration||||
|||||||
|||from (a) to (c) of ISO 27099 is substituted by (i) to (iii)||||
|||according to this TS.||||
|(5) from|1,|Check that the recovery of the CA's keys is carried out|||☐Pass|
|Section||in a manner that is as secure as the backup process.|||☐Fail|
||4|||||
|7.13.2|||||☐Not applicable|
|||||||
|||||||
|(7) from|1,||||☐Pass|
|Section||and used in a secure site, with access limited to|||☐Fail|
||4|||||
|7.13.2||authorized personnel. Check that all requirements of|||☐Not applicable|
|||section 7.13.2 (7) are fulfilled. The auditor must check||||
|||||||
|||all listed requirements of section 7.13.2 (7) separately,||||
|||thus the enumeration from (a) to (e) of ISO 27099 is||||
|||substituted by (i) to (v) according to this TS.||||



Federal Office for Information Security 

46 

3 Key life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by the|
||||||Auditor|
|(8) from|1,|Check that the handling of CA cryptographic hardware|||☐Pass|
|Section||is performed as defined in section 7.13.2 (8) of ISO|||☐Fail|
||4|||||
|7.13.2||27099.|||☐Not applicable|
|||||||
|3.1.2A1|1|Check that backups of the CA keys are made|||☐Pass<br>☐Fail<br>☐Not applicable|
||4|Check that the root-CA makes backups of its keys.|||☐Pass|
||||||☐Fail|
|||Check that the requirements defined in (KLSR) for the||||
||||||☐Not applicable|
|||corresponding security level are fulfilled by the CA for||||
|||||||
|||the backups of its keys (this includes sub-CAs, if||||
|||backups are supported by this sub-CA).||||
|3.1.2A2|1,<br>4|If private keys of the CA are stored outside the security<br>device (e.g. as backup), check that the private keys are<br>processed with the same level of protection as defined<br>by requirement3.1A1.|||☐Pass<br>☐Fail<br>☐Not applicable|
|3.1.2A3|1,<br>4|Check that any storage media containing backups of<br>private keys is encrypted and secured against non-<br>authorized usage.<br>Check that the storage media is located in a physically<br>and logically highly secured area.<br>Check that access to this area is restricted to an<br>appropriate set of persons which is clearly defined by<br>their roles.<br>Check that the number of authorized persons is<br>restricted, while ensuring staff availability to carry out<br>these tasks.|||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

47 

3 Key life cycle management 

## **3.1.3 CA public key distribution** 


![](markdown/tr/TR03145-part1-4_2-0-0-specification/TR03145-part1-4_2-0-0-specification.pdf-0048-02.png)


Control procedures referenced in this Section refer to Section 7.13.3 of (ISO27099). procedures SHALL be fulfilled as requirements: 

public key, the following control 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(1) from|1,|Check that provides a mechanism for validating the|||☐Pass|
|Section||authenticity and integrity of its public key as defined in|||☐Fail|
||4|||||
|7.13.3||section 7.13.3 (1).|||☐Not applicable|
|||||||
|||Check that for subsequent and subordinate CA public||||
|||keys are validated according to section 7.13.3 (1).||||
|||If applicable, check that the CA issues a link certificate||||
|||for its new public key before the expiration of its||||
|||current public key.||||
|||||||
|(5) from|1,|Check that any new CA public key is made available to|||☐Pass|
|Section||relying parties.|||☐Fail|
||4|||||
|7.13.3|||||☐Not applicable|
|||||||
|||||||
|3.1.3A1|1,<br>4|Check that the public key fingerprint of a CA certificate<br>is disseminated to the relying parties on a different<br>channel than the corresponding CA certificate.|||☐Pass<br>☐Fail<br>☐Not applicable|



## 3.1.4 CA key usage 


![](markdown/tr/TR03145-part1-4_2-0-0-specification/TR03145-part1-4_2-0-0-specification.pdf-0048-07.png)


Control procedures referenced in this Section refer to Section 7.13.4 of (ISO27099). be fulfilled as requirements: 

following control procedures SHALL 

Federal Office for Information Security 

48 

3 Key life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(1) from|1,|Check that the activation of the CA private signing key|||☐Pass|
|Section||is performed as defined in section 7.13.4 (1) from ISO|||☐Fail|
||4|||||
|7.13.4||27099.|||☐Not applicable|
|||||||
|(2) from|1|Check that the activation of the CA private key is|||☐Pass|
|Section||performed using multifactor authentication (e.g. smart|||☐Fail|
|||||||
|7.13.4||card and password, biometric and password).|||☐Not applicable|
|||||||
||4|Check that the activation of the CA private key is|||☐Pass|
|||performed using multifactor authentication using|||☐Fail|
|||||||
|||hardware tokens (e.g. smart card and password or PIN).|||☐Not applicable|
|||||||
|(3) from|1,|Check that the CA signing key(s) used to generate|||☐Pass|
|Section||certificates or issue revocation status information, are|||☐Fail|
||4|||||
|7.13.4||not used for any other purpose.|||☐Not applicable|
|||||||
|(5) from|1,|Check that the CA ceases to use a key pair at the end of|||☐Pass|
|Section||its defined operational lifetime, or when the private|||☐Fail|
||4|||||
|7.13.4||key has been compromised or is suspected to have|||☐Not applicable|
|||been compromised.||||
|||||||
|3.1.4A1|1,<br>4|Check that the private key is only set active for the<br>period necessary. Check that the private key is<br>deactivated if one of following cases occurs:<br>•<br>the key is intended not to be used until a fixed<br>date, e.g. for disseminating the new certificate<br>before it will be used;<br>•<br>the key is no longer in use because a new private<br>key has been activated;<br>•<br>it is obvious that the key will not be used for a<br>period of [assignment: number of days, weeks or<br>months] due to a special use case.|||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

49 

3 Key life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|3.1.4A2|1|Check that for the activation of the key material,<br>hardware tokens (e.g. smart cards) are used.|||☐Pass<br>☐Fail<br>☐Not applicable|
||4|Not applicable to CAs affected by (BSI-TR-03145-4)|||☐Pass|
||||||☐Fail|
|||||||
||||||☐Not applicable<br>x|



## 3.1.5 CA key archival and destruction 


![](markdown/tr/TR03145-part1-4_2-0-0-specification/TR03145-part1-4_2-0-0-specification.pdf-0050-03.png)


Control procedures referenced in this Section refer to Section 7.13.5 of (ISO27099). procedures SHALL be fulfilled as requirements: 

following control 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(1) from|1,|Where CA private keys are archived, check that the|||☐Pass|
|Section||requirement of section 7.15.3 (1) of ISO 27099 is|||☐Fail|
||4|||||
|7.13.5||fulfilled.|||☐Not applicable|
|||||||
|(3) from|1,|Check that authorisation to destroy a CA's private key,|||☐Pass|
|Section||and the method of destruction (e.g. hardware token|||☐Fail|
||4|||||
|7.13.5||surrender, hardware token destruction or key|||☐Not applicable|
|||||||
|||||||
|(4) from|1,||||☐Pass|
|Section||key are destroyed so that the private key cannot be|||☐Fail|
||4|||||
|7.13.5||recovered as defined in section 7.13.5 (4) of ISO 27099.|||☐Not applicable|
|||||||
|(5) from|1,|Check that in case a CA cryptographic device is being|||☐Pass|
|Section||permanently removed from service, all keys that have|||☐Fail|
||4|||||
|7.13.5||been used for cryptographic purpose shall be erased|||☐Not applicable|
|||||||
|||||||



Federal Office for Information Security 

50 

3 Key life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|||from the device in use as defined in section 7.13.5 (5) of||||
|||ISO 27099.||||
|(6) from|1,|Check that the CAs private key and all backups are|||☐Pass|
|Section||destroyed in the way as described in section 7.13.5 (6) of|||☐Fail|
||4|||||
|7.13.5||ISO 27099.|||☐Not applicable|
|||||||
|(7) from|1,|Check that the destruction of CA keys follows the|||☐Pass|
|Section||requirements as described in section 7.13.5 (7) of ISO|||☐Fail|
||4|||||
|7.13.5||27099.|||☐Not applicable|
|||||||
|(9) from|1,|Check that algorithms and key length for key|||☐Pass|
|Section||encryption of keys held outside HSM meets the|||☐Fail|
||4|||||
|7.13.5||requirements of section 7.13.5 (9) of ISO 27099.|||☐Not applicable|
|||||||
|3.1.5A1|1,<br>4|Check that archived public keys are only used when<br>historical evidence requires validation.|||☐Pass<br>☐Fail<br>☐Not applicable|



## 3.1.6 CA key compromise 


![](markdown/tr/TR03145-part1-4_2-0-0-specification/TR03145-part1-4_2-0-0-specification.pdf-0051-03.png)


Control procedures referenced in this Section refer to 7.13.6 of (ISO27099). be fulfilled as requirements: 

following control procedures SHALL 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(1) from|1,|describe|||☐Pass|
|Section||the compromise or suspected compromise of a CA's|||☐Fail|
||4|||||
|7.13.6||private keys as a disaster.|||☐Not applicable|
|||||||
|(2) from|1,|Check that disaster recovery procedures as defined in|||☐Pass|
|Section||section 7.13.6 (2) of ISO 27099 exists.|||☐Fail|
||4|||||
|7.13.6|||||☐Not applicable|
|||||||
|||||||



Federal Office for Information Security 

51 

3 Key life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|||Check that details of recovery as defined in section||||
|||7.13.6 (2) of ISO 27099 are part of the recovery plan.||||



## 3.2 Subject key life cycle management 

This section specifies requirements concerning the life cycle of subject keys and refers to Section 7.14 of (ISO27099). Concerning the secure handling of subject keys throughout the whole subject key life cycle, the following requirements apply: 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|3.2A1|1,<br>4|Check that the requirements on hard- and/or software<br>to be used for handling (e.g. key generation or storage)<br>of subject keys are specified by the CA in its Terms and<br>Conditions.|||☐Pass<br>☐Fail<br>☐Not applicable|
|3.2A2|1,<br>4|Check that the CA defines in its Terms and Conditions<br>the subscriber (and where applicable subject)<br>environment in order<br>to prevent unauthorized access to or alteration of<br>subject keys.|||☐Pass<br>☐Fail<br>☐Not applicable|
|3.2A3|1,<br>4|Check that the CA defines in its Terms and Conditions<br>subscriber (and where applicable subject) obligations<br>subject key operations|||☐Pass<br>☐Fail<br>☐Not applicable|
|3.2A4|1,<br>4|Check that the CA specifies in its CP requirements and<br>limitations for the usage of subject keys.|||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

52 

3 Key life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|||Check that all certificates issued by this CA contain<br>information on the subject key usage correspondingly<br>(cf. KeyUsage according to (RFC5280)).<br>Check that the CA defines in its Terms and Conditions<br>the obligations for subscribers (and where applicable of<br>subjects) concerning the usage of subject keys.||||
|3.2A5|1,<br>4|Check that subject private keys are handled (e.g.<br>generated, stored, used or recovered) only by trusted<br>individuals|||☐Pass<br>☐Fail<br>☐Not applicable|



## 3.2.1 Subject key generation and distribution 

There are two alternative ways how the subject key pair can be generated and provided: 

- The subject key pair is generated at the subject's premise and the public key is provided by the subject or subscriber during the identification and registration process to the issuing CA. This alternative is addressed in subsection 3.2.1.1. 

- The CA generates a key pair on behalf of the subject, issues the corresponding certificate and delivers it to the subject or subscriber in a secure manner. Requirements for this alternative are described in subsection 3.2.1.2. 

Despite of which alternative is chosen for subject key generation and distribution, the following requirement applies: 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|3.2.1A1|1,<br>4|Check that the CA implements mechanisms to<br>correctly assign the subject's public key to the<br>registration data.|||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

53 

3 Key life cycle management 

## 3.2.1.1 Subject keys provided by subscriber (if supported) 

Please mark, if subject key generation by the subscriber is supported by the CA: 

## ☐ Yes 

## ☐ No 

If subject key generation by the subscriber is supported by the CA, the following requirements concerning the subject key generation apply: 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|3.2.1.1A1|1,<br>4|Check that the CA determines the security level of the<br>supported subscriber applications by considering a risk<br>analysis of the business case and if applicable of legal<br>requirements.<br>Check that for subscriber applications with security<br>level 'high', as e.g. Sub-CAs or qualified electronic<br>signatures, the CA demands the usage of cryptographic<br>modules (HSM or token) for the handling of subject<br>keys, in particular for key generation and key storage,.<br>Check that for subscriber applications with lower<br>security level, the CA at least demands from<br>subscribers to adopt the following security measures:<br>use of virus protection, use of software firewall,<br>installation of operating system security updates when<br>they occur, [assignment: additional security measures]|||☐Pass<br>☐Fail<br>☐Not applicable|
|3.2.1.1A2|1|Check that the registration data is clearly defined by<br>the CA and contains the public key of the subject and<br>all subject attributes that are necessary for the<br>registration process.<br>Check that at least the public key and the subject|||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

54 

3 Key life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|||avoid alteration and to provide proof of possession of<br>the private key.<br>Check that the CA verifies this signature.||||
||4|Check that the registration data is clearly defined by|||☐Pass|
|||the CA and contains the public key of the subject and|||☐Fail|
|||||||
|||all subject attributes that are necessary for the|||☐Not applicable|
|||registration process.||||
|||Check that certificate requests comply with the||||
|||corresponding CP.||||
|3.2.1.1A3|1,<br>4|Check that the CA validates if the subject key pair<br>fulfils the cryptographic requirements.<br>Check that the CA refuses the certificate request and<br>does not generate a corresponding certificate if these<br>requirements are not fulfilled.|||☐Pass<br>☐Fail<br>☐Not applicable|



## 3.2.1.2 Subject keys provided by the CA (if supported) 

Control procedures referenced in this Section refer to Section 7.14.1 of (ISO27099). 

Please mark, if subject key generation by the CA on behalf of the subject is supported by the CA: 

## ☐ Yes 

## ☐ No 

Note that (BSI-TR-03145-4) does not allow that the subject key is generated by the CA and disseminated to the subscriber. 

If subject key generation by the CA on behalf of the subject is supported the following control procedures SHALL be fulfilled as requirements: 

Federal Office for Information Security 

55 

3 Key life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(2) from|1|Check that subject key generation follows the|||☐Pass|
|Section||requirements as defined in section 7.14.1 (2) of ISO|||☐Fail|
|||||||
|7.14.1||27099.|||☐Not applicable|
|||||||
|(3) from|1|Check that subject key generation performed by the CA|<br>||☐Pass|
|Section||fulfils the requirement as defined in section 7.14.1 (3) of|||☐Fail|
|||||||
|7.14.1||ISO 27099.|||☐Not applicable|
|||||||
|(4) from|1|Check that requirement 7.14.1 (4) from ISO 27099 is|||☐Pass|
|Section||fulfilled.|||☐Fail|
|||||||
|7.14.1|||||☐Not applicable|
|||||||
|||||||
|(5) from|1|Check that the CA's subject key generation process|||☐Pass|
|Section||fulfils the requirements as defined in section 7.14.1 (5)|||☐Fail|
|||||||
|7.14.1||of ISO 27099.|||☐Not applicable|
|||||||
|(6) from|1|Check that the securely key delivery of subject key|||☐Pass|
|Section||pair(s) by the CA is done and all requirements as|||☐Fail|
|||||||
|7.14.1||defined in section 7.14.1 (6) from ISO 27099 are|||☐Not applicable|
|||fulfilled. Check that the key pair is disseminated only||||
|||||||
|||to the subject.||||
|3.2.1.2A1|1|Check that the CA describes the key dissemination<br>procedure in its Terms and Conditions.|||☐Pass<br>☐Fail<br>☐Not applicable|
|3.2.1.2A2|1|Check that the CA determines the security level of the<br>supported subscriber applications by considering a risk<br>analysis of the business case and if applicable of legal<br>requirements.<br>Check that for subscriber applications with security<br>level 'high', as e.g. Sub-CAs or qualified electronic<br>signatures, the CA demands the usage of a certified<br>securitydevice compliant with[assignment: Security|||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

56 

3 Key life cycle management 

|Require-<br>|TR-<br>|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment<br>|Part||||Explanations by|
||||||the Auditor|
||<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|Level 2 according to (KLSR), (ISO15408), equivalent,<br>appropriate application specific requirements] for the<br>handling of subject keys, in particular for key<br>generation and key storage. Check that an appropriate<br>access control ensures that the keys are not accessible<br>from outside.<br>Check that for subscriber applications with lower<br>security level, the CA at least demands from<br>subscribers to adopt the following security measures:<br>use of virus protection, use of software firewall,<br>installation of operating system security updates when<br>they occur, [assignment: additional security measures].||||
|3.2.1.2A3|1<br> <br> <br> <br>|Check if the private key has been provided to the<br>subscriber and is not needed anymore for key storage,<br>recovery, or back-up services, that the CA destroys this<br>private key, including any copies, without undue delay.|||☐Pass<br>☐Fail<br>☐Not applicable|



## 3.2.2 Subject key storage, backup and recovery 

Concerning the secure storage, backup or recovery of subject keys, the following requirements apply: 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|3.2.2A1|1,<br>4|If private keys of subscribers/subjects are stored<br>outside the security device (e.g. as backup), check that<br>the private keys are processed with the same level of<br>protection as defined in Section 3.2.1.|||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

57 

3 Key life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|3.2.2A2|1,<br>4|Check that any storage media containing backups of<br>private keys are encrypted and secured against non-<br>authorized usage.|||☐Pass<br>☐Fail<br>☐Not applicable|



## 3.2.2.1 Subject key storage, backup and recovery services provided by CA (if supported) 

Control procedures referenced in this Section refer to Section 7.14.2 of (ISO27099). 

Please mark, if subject key storage, backup or recovery services are supported by the CA[1] : 

## ☐ Yes 

## ☐ No 

Note that (BSI-TR-03145-4) does not allow subject key storage, backup and recovery services provided by the CA. 

If the CA provides key storage, backup or recovery services of subject keys, the following control procedures SHALL be fulfilled as requirements: 

|Require-<br>|TR-<br>|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment<br>|Part||||Explanations by|
||||||the Auditor|
|(1) from|1<br>|Check that storing of CA private keys meets all the|||☐Pass|
|Section|<br>|<br>requirements as defined in section 7.14.2 of ISO|||☐Fail|
|||||||
|7.14.2||27099.|||☐Not applicable|
|||||||
|(2) from|1<br> <br> <br>|Check that, if the CA generates signing key pair (s) on|||☐Pass|
|Section||<br>behalf of a subscriber, the requirement of ISO 27099,|||☐Fail|
|||||||
|7.14.2||section 7.14.2 (2) is fulfilled.|||☐Not applicable|
|||||||
|(3) from|1<br> <br>|If the CA (or trusted service provider for key storage)|||☐Pass|
|Section||<br>generates public/private signing key pairs on behalf|||☐Fail|
|||||||
|7.14.2|||||☐Not applicable|
|||||||



## 1 Subject key storage, backup or recovery services by the CA are not supported by CAs within a CVCA PKI. 

Federal Office for Information Security 

58 

3 Key life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|||of a subscriber, check that the requirements of||||
|||section 7.14.2 (3) of ISO 27099 are met.||||
|(4) from|1|Check that all requirements as defined in section|||☐Pass|
|Section||<br>7.14.2 (4) of ISO 27099 are fulfilled.|||☐Fail|
|||||||
|7.14.2|||||☐Not applicable|
|||||||
|(5) from|1|If the CA provides key storage, backup and recovery|||☐Pass|
|Section||<br>on behalf of the subject, check that controls as|||☐Fail|
|||||||
|7.14.2||defined in section 7.14.2 (5) of ISO 27099 exists.|||☐Not applicable|
|||||||
|(6) from|1|If the CA provides subject key archival check that|||☐Pass|
|Section||<br>requirement of section 7.14.2 (6) of ISO 27099 is|||☐Fail|
|||||||
|7.14.2||fulfilled.|||☐Not applicable|
|||||||
|(7) from|1|If the CA provides key recovery, check that the|||☐Pass|
|Section||<br>requirement as defined in section 7.14.2 (7) applies.|||☐Fail|
|||||||
|7.14.2|||||☐Not applicable|
|||||||
|(8) from|1|If the CA provides key recovery, check that the CA|||☐Pass|
|Section||<br>sends notification to the subscriber as defined in|||☐Fail|
|||||||
|7.14.2||section 7.14.2 (8) of ISO 27099.|||☐Not applicable|
|||||||
|(10) from|<br>1|If the CA provides subject (confidentiality) key|||☐Pass|
|Section||<br>storage, check that all copies and fragments of the|||☐Fail|
|||||||
|7.14.2||subject's private key are destroyed at the end of its|||☐Not applicable|
|||life cycle.||||
|||||||
|3.2.2.1A1|1|Check that any storage media containing backups of<br>private keys is located in a physically and logically<br>highly secured area.<br>Check that access to this area is restricted to an<br>appropriate set of persons which is clearly defined by<br>their roles.|||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

59 

3 Key life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|||Check that the number of authorized persons is<br>restricted, while ensuring staff availability to carry out<br>these tasks.||||



## 3.2.3 Hardware token life cycle management (if supported) 

Control procedures referenced in this Section refer to Section 7.14.3 of (ISO27099). 

Please mark, if supported by the CA[2] : 

☐ Yes 

## ☐ No 

Note that (BSI-TR-03145-4) does not allow he subscriber. 

If Hardware token lifecycle management is provided by the CA, the following control procedures SHALL be fulfilled as requirements: 

|Require-<br>|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment<br>|Part||||Explanations by|
||||||the Auditor|
|(2) from|1|For transport of hardware token between the card|||☐Pass|
|Section||manufacturer and the card issuer check that|||☐Fail|
|||||||
|7.14.3||requirement 7.14.3 (2) of ISO 27099 is fulfilled.|||☐Not applicable|
|||||||
|(5) from|1|Check that hardware tokens are securely stored and|||☐Pass|
|Section||under inventory control while under the control of the|||☐Fail|
|||||||
|7.14.3||card issuer.|||☐Not applicable|
|||||||
|(6) from|1|Check that the requirements as defined in section|||☐Pass|
|Section||7.14.3 (6) of ISO 27099 are fulfilled.|||☐Fail|
|||||||
|7.14.3|||||☐Not applicable|
|||||||
|||||||



2 The generation and dissemination of a personalized token by the CA is not supported by CAs within a CVCA PKI. 

Federal Office for Information Security 

60 

3 Key life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(7) from|1|Check that hardware token personalization follows<br>the processes and procedures and that all<br>requirements as defined in section 7.14.3 (7) of ISO<br>27099 are fulfilled. The auditor must check all listed<br>requirements of section 7.14.3 (7) separately, thus the<br>enumeration from (a) to (f) of ISO 27099 is substituted<br>by (i) to (vi) according to this TS.|||☐Pass|
|Section|||||☐Fail|
|||||||
|7.14.3|||||☐Not applicable|
|||||||
|||||||
|||||||
|(8) from|1|Check that the card bureau or CA (or RA) logs hardware|||☐Pass|
|Section||<br>token preparation and personalization in an audit log.|||☐Fail|
|||||||
|7.14.3|||||☐Not applicable|
|||||||
|(11) from|<br>1|Check that all requirements defined in section 7.14.3|||☐Pass|
|Section||(11) of ISO 27099 are fulfilled.|||☐Fail|
|||||||
|7.14.3|||||☐Not applicable|
|||||||
|(12) from|<br>1|Check that the requirements for the initial activation|||☐Pass|
|Section||data for hardware tokens as defined in section 7.14.3|||☐Fail|
|||||||
|7.14.3||(12) are fulfilled.|||☐Not applicable|
|||||||
|(14) from|<br>1|Check that the subject is provided with a mechanism|||☐Pass|
|Section||<br>that protects the access to the card data including the|||☐Fail|
|||||||
|7.14.3||private keys stored on the hardware token during use|||☐Not applicable|
|||by the subscriber (i.e. PIN access control mechanism||||
|||||||
|||cardholder verification method).||||



Federal Office for Information Security 

61 

3 Key life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(15) from|<br>1|Check that the subject private keys on the hardware|||☐Pass|
|Section||<br>token are not be exported to application for|||☐Fail|
|||||||
|7.14.3||cryptographic functions, such as signing..|||☐Not applicable|
|||||||
|(19) from|<br>1|Check that processes and procedures for replacing lost|||☐Pass|
|Section||<br>or damaged hardware tokens are in existence and being|||☐Fail|
|||||||
|7.14.3||followed.|||☐Not applicable|
|||||||
|3.2.3A1|1|Check that the CA ensures that the hardware token<br>(cryptographic hardware) is appropriate to the security<br>requirements of the certificates throughout its life<br>cycle and as defined in the CP.|||☐Pass<br>☐Fail<br>☐Not applicable|
|3.2.3A2|1|Check that the CA correctly assigns the hardware token<br>and the public key from the hardware token to the|||☐Pass<br>☐Fail<br>☐Not applicable|
|3.2.3A3|1|Check that the CA describes the dissemination<br>procedure for hardware tokens in its Terms and<br>Conditions.|||☐Pass<br>☐Fail<br>☐Not applicable|
|3.2.3A4|1|Check that the CA uses the registered subscriber data to<br>ensure that the hardware token is disseminated to the<br>correct subscriber.|||☐Pass<br>☐Fail<br>☐Not applicable|
|3.2.3A5|1|Check that the subscriber is obliged by the CA's Terms<br>and Conditions to inform the CA when detecting a<br>compromise of the PIN code during the activation<br>procedure.<br>Check that in this case the affected certificate is<br>revoked.|||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

62 

3 Key life cycle management 

## 3.2.4 Subject key archival and destruction (if supported) 

Control procedures referenced in this Section are based upon Section 7.13.5 of (ISO27099) . 

Please mark, if archival or storage services of subject keys are provided by the CA[3] : 

☐ Yes 

## ☐ No 

Note that (BSI-TR-03145-4) does not allow archival, storage and destruction services provided by the CA. 

If the CA provides archival or storage services of subject keys, the following requirements concerning the archival and destruction of subject keys apply: 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|3.2.4A1|1|Check that subject private keys are archived with the<br>same or a greater level of security as keys currently in<br>use.|||☐Pass<br>☐Fail<br>☐Not applicable|
|3.2.4A2|1|Check that archived keys are only used when historical<br>evidence requires validation.|||☐Pass<br>☐Fail<br>☐Not applicable|
|3.2.4A3|1|private key has to be destroyed (e.g. hardware token<br>surrender, hardware token destruction or key<br>overwrite).|||☐Pass<br>☐Fail<br>☐Not applicable|
|3.2.4A4|1|private key are destroyed such that the private key<br>cannot be retrieved.|||☐Pass<br>☐Fail<br>☐Not applicable|
|3.2.4A5|1|Check that the CA destroys the subject private key and<br>all the backups after revocation or regular end of<br>validity of the corresponding subject certificate.|||☐Pass<br>☐Fail<br>☐Not applicable|



3 Subject key archival or storage by the CA are not supported by CAs within a CVCA PKI. 

Federal Office for Information Security 

63 

3 Key life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|3.2.4A6|1|Check that destruction of subject keys is undertaken in<br>a physically secured environment by authorized and<br>trusted personnel under the principles of multiple<br>control.|||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

64 

4 Certificate life cycle management 

## 4 Certificate life cycle management 

In this section the requirements for the different tasks of a CA during the certificate life cycle are specified. 

## 4.1 Subject registration 

Control procedures referenced in this Section refer to Section 7.15.1 of (ISO27099). Concerning the subject registration the following control procedures SHALL be fulfilled as requirements: 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(1) from|1,|Check that the CA verifies or requires that the RA|||☐Pass|
|Section||verifies the credentials of a subject as defined in|||☐Fail|
||4|||||
|7.15.1||section 7.15.1 (1).|||☐Not applicable|
|||||||
|(2) from|1,|Check that the CA or RA verifies the accuracy of the|||☐Pass|
|Section||information included in the certificate request|||☐Fail|
||4|||||
|7.15.1||submitted by the requesting entity in accordance|||☐Not applicable|
|||with the CP.||||
|||||||
|(3) from|1,|Check that the CA or RA checks the certificate request|||☐Pass|
|Section||for errors or omissions in accordance with the CP.|||☐Fail|
||4|||||
|7.15.1|||||☐Not applicable|
|||||||
|||||||
|(4) from|1,|The CA must check that the end entity signing|||☐Pass|
|Section||request is submitted securely and fulfils the|||☐Fail|
||4|||||
|7.15.1||requirements as defined in section 7.15.1 (4).|||☐Not applicable|
|||||||
|(5) from|1,|Check that encryption and access controls are used as|||☐Pass|
|Section||defined in section 7.15.1 (5) of ISO 27099.|||☐Fail|
||4|||||
|7.15.1|||||☐Not applicable|
|||||||
|||||||
|(6) from|1,|Check that the CA or RA, at the point of registration,|||☐Pass|
|Section||informs the subject or subscriber about the terms and|||☐Fail|
||4|||||
|7.15.1|||||☐Not applicable|
|||||||



Federal Office for Information Security 

65 

4 Certificate life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|||condition about using the certificates as defined in||||
|||section 7.15.1 (6) of ISO 27099.||||
|(7) from|1,|Check that the identification and authentication of a|||☐Pass|
|Section||subject is done first, before issuing certificate, as|||☐Fail|
||4|||||
|7.15.1||defined in section 7.15.1 (7) of ISO 27099.|||☐Not applicable|
|||||||
|(8) from|1,|Check that the RA or CA keeps registration and|||☐Pass|
|Section||related administrative data as defined in section|||☐Fail|
||4|||||
|7.15.1||7.15.1 (8) of ISO 27099.|||☐Not applicable|
|||||||
|(10) from|<br>1,||||☐Pass|
|Section||agreement to the terms and conditions.|||☐Fail|
||4|||||
|7.15.1|||||☐Not applicable|
|||||||
|||||||
|(11) from|<br>1,|Check that the CA (or RA) records the success or|||☐Pass|
|Section||failure of the registration event in an audit log.|||☐Fail|
||4|||||
|7.15.1|||||☐Not applicable|
|||||||
|||||||
|(12) from|<br>1,|Check that the CA stores the certificate enrolment|||☐Pass|
|Section||data in a database, that follows the requirements as|||☐Fail|
||4|||||
|7.15.1||defined in section 7.15.1 (12) of ISO 27099.|||☐Not applicable|
|||||||
|(13) from|<br>1,|Check that the CA or RA ensures that the|||☐Pass|
|Section||'Identification and registration' process is secure. In|||☐Fail|
||4|||||
|7.15.1||particular, check that all transfers of registration and|||☐Not applicable|
|||identification data, whether inside or outside the CA||||
|||||||
|||or RA, are protected against eavesdropping and||||
|||manipulation.||||
|4.1A1|1,<br>4|Check that the formal process-flow including the<br>interfaces for requesting the registration and/or<br>providing information by the subscriber are clearly<br>defined and verified by the CA or RA.|||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

66 

4 Certificate life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|4.1A2|1,<br>4|Check that the CA obliges subscribers to notify the CA<br>immediately about any change of their registration<br>data.<br>Check that the CA requires a confirmation from the<br>subscriber that the registration data is still valid at<br>least every [assignment: number of months] months.|||☐Pass<br>☐Fail<br>☐Not applicable|
|4.1A3|1,<br>4|Check that the CA verifies the information<br>identifying the subscribers and the physical existence<br>directly or indirectly using appropriate measures.<br>Check that the physical address or other appropriate<br>attributes for contact are verified.|||☐Pass<br>☐Fail<br>☐Not applicable|
|4.1A4|1,<br>4|Check that the CA defines clearly the set of<br>information identifying the subscriber.<br>If the subject differs from the subscriber, check that<br>additional information (e.g. evidence of legitimation<br>to act on behalf of subject) are provided and checked.<br>In case of a physical person associated with a legal<br>person, check that this association is verified.|||☐Pass<br>☐Fail<br>☐Not applicable|
|4.1A5|1,<br>4|Check that the CA checks its database to determine if<br>a subject has registered before so that multiple<br>identities of a subject are linked within the<br>registration database and can be suspended at once or<br>prevented totally if required by the Terms and<br>Conditions.|||☐Pass<br>☐Fail<br>☐Not applicable|
|4.1A6|1|Check that the CA ensures, that the requesting subject<br>is identified unambiguously before starting the<br>certificate generation process.|||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

67 

4 Certificate life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
||4|Check that the CA ensures, that the requesting subject|||☐Pass|
|||is identified unambiguously before starting the|||☐Fail|
|||||||
|||certificate generation process.|||☐Not applicable|
|||||||
|||Check that the CA verifies certificate requests as||||
|||specified in the corresponding CP.||||
|||Check in particular, that the CA validates the||||
|||signatures on certificate requests for successive||||
|||certificate.||||



## 4.2 Certificate renewal (if supported) 

Control procedures referenced in this Section refer to Section 7.15.2 of (ISO27099). 

Please mark, if certificate renewal is provided by the CA 

## ☐ Yes 

## ☐ No 

Note that (BSI-TR-03145-4) does not allow renewal of certificates. 

If certificate renewal is provided the following control procedures SHALL be fulfilled as requirements: 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(2) from|1|Check that the CA ensures that the requirements on|||☐Pass|
|Section||secure submission of renewal request is done as|||☐Fail|
|||||||
|7.15.2||defined section 7.15.2 (2) of ISO 27099.|||☐Not applicable|
|||||||



Federal Office for Information Security 

68 

4 Certificate life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(3) from|1|Check that the CA issues a new certificate using|||☐Pass|
|Section||all|||☐Fail|
|||||||
|7.15.2||the requirements of section 7.15.2 (3) of ISO 27099 are|||☐Not applicable|
|||fulfilled.||||
|||||||
|||Check in particular, that the CA does not issue new||||
|||certificate if the points defined in section 7.15.2 (3) of||||
|||ISO 27099 are valid.  The auditor must check all listed||||
|||requirements of section 7.15.2 (3) separately, thus the||||
|||enumeration from (a) to (c) of ISO 27099 is substituted||||
|||by (i) to (iii) according to this TS.||||
|(4) from|1|Check that the CA or the RA processes the certificate|||☐Pass|
|Section||renewal data as defined in section 7.15.2 (4) of ISO|||☐Fail|
|||||||
|7.15.2||27099.|||☐Not applicable|
|||||||
|(5) from|1|Check that the CA verifies the existence and validity|||☐Pass|
|Section||of the certificate to be renewed.|||☐Fail|
|||||||
|7.15.2|||||☐Not applicable|
|||Check that renewal is not permitted unless the||||
|||||||
|||existing certificate status is live (i.e. not revoked or||||
|||suspended).||||
|(6) from|1|Check that the CA or the RA verifies that the|||☐Pass|
|Section||requirements as defined in section 7.15.2 (6) of ISO|||☐Fail|
|||||||
|7.15.2||27099 is fulfilled.|||☐Not applicable|
|||||||
|(8) from|1|Check that the CA records the renewal actions in an|||☐Pass|
|Section||audit log.|||☐Fail|
|||||||
|7.15.2|||||☐Not applicable|
|||||||
|||||||
|(9) from|1|Check that the certificate renewal request is checked|||☐Pass|
|Section||for errors or omissions by the CA or RA.|||☐Fail|
|||||||
|7.15.2|||||☐Not applicable|
|||||||
|||||||



Federal Office for Information Security 

69 

4 Certificate life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(12) from|<br>1|Check that the new certificate is made available to the|||☐Pass|
|Section||end entity by the issuing CA in accordance with the|||☐Fail|
|||||||
|7.15.2||requirements of the corresponding CP.|||☐Not applicable|
|||||||
|(13) from|<br>1|Check that the CA defines Terms and Conditions in|||☐Pass|
|Section||which cases renewal may be allowed|||☐Fail|
|||||||
|7.15.2|||||☐Not applicable|
|||||||
|||||||
|(14) from|<br>1|Check that all requirements as defined in section|||☐Pass|
|Section||7.15.2 (14) of ISO 27099 are fulfilled.|||☐Fail|
|||||||
|7.15.2|||||☐Not applicable|
|||||||
|||||||
|4.2A1|1|Check that the CA checks carefully, if the renewal of a<br>certificate is necessary.<br>Check that the need for a renewal instead of re-<br>keying demanded by the business case is balanced<br>with the security risk of the weakened key pair, the<br>validity period of the certificate and the used<br>algorithms. In case of doubt, check that re-keying of<br>the certificate is done.|||☐Pass<br>☐Fail<br>☐Not applicable|
|4.2A2|1|For the case of expiring certificates, check that the CA<br>defines in the CP and/or CPS that a request for the<br>renewal of a certificate SHALL be submitted at least<br>[assignment: number of days or weeks] before the<br>previous certificate expires.<br>Check that the CA is able to generate the new<br>certificate within the defined timeframe.|||☐Pass<br>☐Fail<br>☐Not applicable|
|4.2A3|1|Check that the CA defines clearly in its Terms and<br>Conditions in which cases renewal may be allowed.|||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

70 

4 Certificate life cycle management 

## 4.3 Certificate rekey 

Control procedures referenced in this Section refer to Section 7.15.3 of (ISO27099). 

Note that (BSI-TR-03145-4) does only allow the rekeying of CV certificates but not the rekeying of MDS certificates. 

Concerning rekeying of a certificate the following control procedures SHALL be fulfilled as requirements: 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(1) from|1,|Check that the CA ensures that the rekeying request is|||☐Pass|
|Section||secure transmitted and authenticated as defined in|||☐Fail|
||4|||||
|7.15.3||section 7.15.3 (1).|||☐Not applicable|
|||||||
|(2) from|1,|Check that the requirement as defined in section|||☐Pass|
|Section||7.15.3 (2) of ISO 27099 is fulfilled.|||☐Fail|
||4|||||
|7.15.3|||||☐Not applicable|
|||||||
|||||||
|(3) from|1,|Check that the CA or the RA checks the certificate|||☐Pass|
|Section||rekey request for errors or omissions.|||☐Fail|
||4|||||
|7.15.3|||||☐Not applicable|
|||||||
|||||||
|(5) from|1,|Check that prior to the rekeying of existing|||☐Pass|
|Section||certificates all the requirements as listed in section|||☐Fail|
||4|||||
|7.15.3||7.15.3 (5) of ISO 27099 are verified. The auditor must|||☐Not applicable|
|||check all listed requirements of section 7.15.3 (5)||||
|||||||
|||separately, thus the enumeration from (a) to (f) of ISO||||
|||27099 is substituted by (i) to (vi) according to this TS.||||
|(8) from|1,|Check that the CA defines the terms and conditions|||☐Pass|
|Section||under which rekeying may be permitted.|||☐Fail|
||4|||||
|7.15.3|||||☐Not applicable|
|||||||
|||||||
|4.3A1|1|For the case of expiring certificates, check that the CA<br>defines in the CP and/or CPS that a request for the<br>rekeyingof a certificate SHALL be submitted at least|||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

71 

4 Certificate life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|||[assignment: number of days or weeks] before the<br>previous certificate expires.<br>Check that the CA is able to generate the new<br>certificate within the defined timeframe.||||
||4|Check that for the case of expiring certificates, the CA|||☐Pass|
|||defines in the CP and/or CPS that a request for the|||☐Fail|
|||||||
|||rekeying of a certificate is submitted according to the|||☐Not applicable|
|||||||
|||Check that the CA is able to generate the new||||
|||certificate within the defined timeframe.||||
|4.3A2|1,<br>4|Check that the CA enforces the use of a newly<br>generated key pair.|||☐Pass<br>☐Fail<br>☐Not applicable|



## 4.4 Certificate issuance 

Control procedures referenced in this Section refer to Section 7.15.4 of (ISO27099). Concerning certificate issuance the following control procedure SHALL be fulfilled as requirement: 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(4) from|1|Check that the requirement of section 7.15.4 (4) of ISO|||☐Pass|
|Section||27099 is fulfilled.|||☐Fail|
|||||||
|7.15.4|||||☐Not applicable|
|||||||
||4|Not applicable to CAs affected by (BSI-TR-03145-4)|||☐Pass|
|||||||
||||||☐Fail|
|||||||
||||||☐Not applicable<br>x|



Federal Office for Information Security 

72 

4 Certificate life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|4.4A1|1,<br>4|Check that the CA does not allow issuance of identical<br>certificate attributes for two different key pairs.|||☐Pass<br>☐Fail<br>☐Not applicable|
|4.4A2|1|Check that certificates include the following<br>attributes:<br>•<br>to (RFC5280)),<br>•<br>name of the subscriber or the identifiable<br>subject,<br>•<br>additional relevant attributes of the CA or<br>subject/subscriber,<br>•<br>public key corresponding to the private key<br>under the subscriber control,<br>•<br>period of validity,<br>•<br>the certificate serial number,<br>•<br>the electronic signature of the issuing<br>authority,<br>•<br>limitation of the scope of the certificate,<br>•<br>limitations on transactions,<br>•<br>information about the cryptographic<br>algorithms of the issuing authority's signature<br>and of the public key of the subscriber.<br>Check that these attributes are verified by the CA.|||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

73 

4 Certificate life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
||4|Check that certificates (german:|||☐Pass|
|||Berechtigungszertifikate) include the following|||☐Fail|
||||<br>|||
|||attributes:|||☐Not applicable|
|||||||
|||•<br>Certificate Authority Reference ,||||
|||•<br>Certificate Holder Reference ,||||
|||•<br>type of certificate,||||
|||•<br>public key corresponding to the private key||||
|||under the subscriber control,||||
|||•<br>period of validity,||||
|||•<br>the sequence number of the certificate,||||
|||•<br>the electronic signature of the issuing||||
|||authority,||||
|||•<br>access rights||||
|||•<br>certificate extensions (if applicable).||||
|||Check that these attributes are verified by the CA.||||
||4|Check that MDS Certificates include the following|||☐Pass|
|||attributes:|||☐Fail|
|||||||
||||||☐Not applicable|
|||•<br>Distinguished Name of Issuer,||||
|||||||
|||•<br>Distinguished Name of Subject,||||
|||•<br>public key corresponding to the private key||||
|||under the subscriber control,||||
|||•<br>period of validity,||||
|||•<br>the certificate serial number,||||



Federal Office for Information Security 

74 

4 Certificate life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|||•<br>the electronic signature of the issuing||||
|||authority,||||
|||•<br>certificate extensions (if applicable).||||
|||Check that these attributes are verified by the CA.||||
|4.4A3|1,<br>4|Check that the CA is able for all disseminated<br>certificates to associate unambiguously a certificate to<br>the subject the respective certificate has been<br>disseminated to.|||☐Pass<br>☐Fail<br>☐Not applicable|
|4.4A4|1|Check that the CA differentiates between private key<br>usage and validity period of the public key.|||☐Pass<br>☐Fail<br>☐Not applicable|
||4|Not applicable to CAs affected by (BSI-TR-03145-4)|||☐Pass|
||||||☐Fail|
|||||||
||||||☐Not applicable<br>x|



## 4.5 Certificate distribution 

Control procedures referenced in this Section refer to Section 7.15.5 of (ISO27099). Concerning the distribution of certificates, the following control procedures SHALL be fulfilled as requirements: 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(1) from|1,|Check that the CA makes the issued certificates|||☐Pass|
|Section||available to relevant parties as defined in section|||☐Fail|
||4|||||
|7.15.5||7.15.5 (1) of ISO 27099.|||☐Not applicable|
|||||||



Federal Office for Information Security 

75 

4 Certificate life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(2) from|1,|Check that only authorized CA personal is allowed to|||☐Pass|
|Section||administer its repository or to administer alternative|||☐Fail|
||4|||||
|7.15.5||distribution mechanisms.|||☐Not applicable|
|||||||
|(3) from|1,|Check that requirement of section 7.15.5 (3) is|||☐Pass|
|Section||fulfilled.|||☐Fail|
||4|||||
|7.15.5|||||☐Not applicable|
|||||||
|||||||



## 4.5.1 Directory Service[4] (if supported) 

If a directory service is supported, then following requirements apply: 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|4.5.1A1|1|Check that the Directory Service provides a<br>searchable repository that contains all certificates<br>that are issued by this CA and their certificate status<br>information.|||☐Pass<br>☐Fail<br>☐Not applicable|
||4|Check that the CA provides a searchable repository|||☐Pass|
|||that contains all certificates that are issued by this CA|||☐Fail|
|||||||
|||and their certificate status information.|||☐Not applicable|
|||||||
|4.5.1A2|1|Check that the publication of a certificate, i.e. the<br>delay between issuance of a certificate and its<br>availability on the directory service to all relying<br>parties, is at most [assignment: number of<br>hours/days].|||☐Pass<br>☐Fail<br>☐Not applicable|



4 For a certification according to (BSI-TR-03145-4) the requirements ascribed to a directory service SHALL be fulfilled by a non-public repository which is operated and maintained by the CA. 

Federal Office for Information Security 

76 

4 Certificate life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
||4|Not applicable to CAs affected by (BSI-TR-03145-4)|||☐Pass|
||||||☐Fail|
|||||||
||||||☐Not applicable<br>x|
|4.5.1A3|1,<br>4|Check that the Directory Service provides secure<br>communication and adequate controls in order to<br>prevent unauthorized entities from adding,<br>modifying, or deleting repository entries.<br>Check that the exact control mechanisms is part of<br>the respective CPS.|||☐Pass<br>☐Fail<br>☐Not applicable|
|4.5.1A4|1|Check that the Directory Service grants access to all<br>relevant information to the relying parties.|||☐Pass<br>☐Fail<br>☐Not applicable|
||4|Check that the Repository is not publicly accessible.|||☐Pass|
||||||☐Fail|
|||||||
||||||☐Not applicable|



## 4.6 Certificate changeover (if supported) 

Please mark, if the root-CA uses link certificates 

☐ Yes 

## ☐ No 

## ☐ Not applicable[5] 

Note that concerning (BSI-TR-03145-4) the requirements from this Section are mandatory for certificate changeover within a CVCA PKI, except MDS certificates within the CVCA-eID PKI. 

If a certificate changeover by means of link certificates is supported by a root-CA, the following requirements apply: 

## 5 e.g., because the audited CA is a sub-CA 

Federal Office for Information Security 

77 

4 Certificate life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|4.6A1|1,<br>4|Check for a root-CA changeover, that the root-CA<br>generates two certificates: a self-signed successor<br>certificate and a link certificate.<br>Check that the link certificate contains the public key<br>and the attributes of the successor certificate and is<br>signed with the private key of the currently valid<br>root-CA certificate.<br>If the root-CA implements a directory service, check<br>that these two certificates are published on the root-<br>integrity and authenticity of the successor root-CA<br>certificate.|||☐Pass<br>☐Fail<br>☐Not applicable|
|4.6A2|1|Check that the root-CA changeover is performed with<br>a preloading phase of at least [assignment: number of<br>days/months].<br>Check that the successor certificate of the CA is<br>generated accordingly to that preloading phase<br>before its validity starts.<br>Check that during this preloading phase the successor<br>certificate and the link certificate, if supported, are<br>securely distributed to all relying parties.|<br>||☐Pass<br>☐Fail<br>☐Not applicable|
||4|Not applicable to CAs affected by (BSI-TR-03145-4)|||☐Pass|
||||||☐Fail|
|||||||
||||||☐Not applicable<br>x|



Concerning the secure transition from a CA certificate to the succeeding CA certificate the following requirements apply for both, root-CA and sub-CA: 

Federal Office for Information Security 

78 

4 Certificate life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|4.6A3|1|Check that a CA changeover is performed with an<br>overlap time of at least [assignment: number of<br>days/months] up to at most [assignment: number of<br>days/months] in order to ensure a secure transition<br>from the current to the successor CA certificate.<br>Check that the overlap time starts at the same time as<br>the validity of the successor certificate starts.|||☐Pass<br>☐Fail<br>☐Not applicable|
||4|Check that the CA changeover is performed with an|||☐Pass|
||||||☐Fail|
|||||||
|||to ensure a secure transition from the current to the|||☐Not applicable|
|||successor CA certificate.||||
|||Check that the overlap time starts at the same time as||||
|||the validity of the successor certificate starts.||||
|4.6A4|1,<br>4|Check that after expiration of the overlap time, the<br>private key including backup keys of the current CA<br>certificate are securely deleted.|||☐Pass<br>☐Fail<br>☐Not applicable|
|4.6A5|1,<br>4|Check that the CA uses its newest private key for<br>issuing certificates.<br>issuing certificates, once a successor certificate<br>becomes valid.<br>Check that at any point in time there is exactly one<br>private key in usage for issuing certificates.|||☐Pass<br>☐Fail<br>☐Not applicable|
|4.6A6|1|Check that the CA uses its newest private key for<br>signing its Certificate Revocation List.|||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

79 

4 Certificate life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|||signing CRLs, once a successor certificate becomes<br>valid.<br>Check that at any point in time there is only one<br>p<br>6||||
||4|Not applicable to CAs affected by (BSI-TR-03145-4)|||☐Pass|
||||||☐Fail|
|||||||
||||||☐Not applicable<br>x|
|4.6A7|4|Check that the CA provides an appropriate process|||☐Pass|
|||for re-keying of a certificate if the process is|||☐Fail|
|||||||
|||requested by the subscriber or started by the CA.|||☐Not applicable|
|||||||
|||Check that the CA ensures that the request is||||
|||processed in a timely manner.||||



## 4.7 Certificate revocation 

Control procedures referenced in this Section refer to Section 7.15.6 of (ISO27099). 

Note that only MDS certificates within the CVCA-eID PKI are revoked. Therefore, the requirements in this section apply to MDS certificates within the CVCA-eID PKI only. 

Concerning the revocation of certificates the following control procedures SHALL be fulfilled as requirements: 

> 6 Note that although the CRL is always signed with the newest private key of the CA, the CRL can include revoked certificates that are issued by this CA with its newest private key as well as revoked certificates that are issued by this CA with one of its earlier private keys. 

Federal Office for Information Security 

80 

4 Certificate life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(1) from|1,|Check that the CA provides a means to facilitated|||☐Pass|
|Section||secure and authenticated revocation as defined in|||☐Fail|
||4|||||
|7.15.6||section 7.15.6 (1) of ISO 27099.|||☐Not applicable|
|||||||
|(2) from|1,|Check that the CA ensures that the revocation request|||☐Pass|
|Section||is securely submitted.|||☐Fail|
||4|||||
|7.15.6|||||☐Not applicable|
|||Check that the revocation request is from an||||
|||||||
|||authorised entity.||||
|(4) from|1,|Check that all certificate revocation requests and|||☐Pass|
|Section||outcomes are recorded in an audit log as defined in|||☐Fail|
||4|||||
|7.15.6||section 7.15.6 (4) of ISO 27099.|||☐Not applicable|
|||||||
|(6) from|1,|Even if certificate renewal is supported, check that a|||☐Pass|
|Section||revoked certificate is never reinstated|||☐Fail|
||4|||||
|7.15.6|||||☐Not applicable|
|||||||
|||||||
|(7) from|1,|Check that the CA ensures a notification of a subject|||☐Pass|
|Section||or subscriber is done in case of certificate revocation|||☐Fail|
||4|||||
|7.15.6||as defined in section 7.15.6 (7) of ISO 27099.|||☐Not applicable|
|||||||
|(8) from|1,|Check that the system hosting the revocation|||☐Pass|
|Section||information fulfils the requirements as defined in|||☐Fail|
||4|||||
|7.15.6||section 7.15.6 (8) of ISO 27099. Check that the CA|||☐Not applicable|
|||analyses the risk of a system failure and attacks||||
|||||||
|||against the system, taking the assumed traffic into||||
|||account.||||
|(9) from|1,|Check that the revocation information is secured as|||☐Pass|
|Section||defined in section 7.15.6 (9) of ISO 27099.|||☐Fail|
||4|||||
|7.15.6|||||☐Not applicable|
|||||||
|||||||



Federal Office for Information Security 

81 

4 Certificate life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|(10) from|<br>1|Check that the CA maintains controls to revoke|||☐Pass|
|Section||certificates and publish appropriate information|||☐Fail|
|||||||
|7.15.6||about the revoked certificates.|||☐Not applicable|
|||||||
||4|Check that the CA maintains controls to revoke MDS|||☐Pass|
|||certificates and publish appropriate information|||☐Fail|
|||||||
|||about revoked MDS certificates.|||☐Not applicable|
|||||||
|4.7A1|1,<br>4|Check if a legitimate revocation request is received<br>that the CRL, OCSP responder (if supported), or other<br>certificate status information mechanisms are<br>updated by the CA in the respective time frames<br>specified within the CP.|||☐Pass<br>☐Fail<br>☐Not applicable|
|4.7A2|1,<br>4|Check that the complete revocation process (i.e. the<br>delay between a revocation request or report and the<br>availability of the revocation status information to all<br>relying parties) is at most [assignment: number of<br>hours] hours.|||☐Pass<br>☐Fail<br>☐Not applicable|
|4.7A3|1,<br>4|Check that certificate status information are backed<br>up to a physically separated server to avoid the loss of<br>data.|||☐Pass<br>☐Fail<br>☐Not applicable|
|4.7A4|1,<br>4|Check that the integrity of the revocation<br>information, both of the original and the back-ups,<br>are secured by appropriate cryptographic measures.|||☐Pass<br>☐Fail<br>☐Not applicable|
|4.7A5|1,<br>4|Check that the service processing the revocation of<br>certificates ensures the processing of inquiries and<br>updates within [assignment: number of hours] hours.|||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

82 

4 Certificate life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|4.7A6|1,<br>4|Check that the CA provides a service receiving the<br>revocation or suspension request by subscribers or<br>third parties.<br>Check that this service is available as required by the<br>application context or business case, respectively.|||☐Pass<br>☐Fail<br>☐Not applicable|
|4.7A7|1,<br>4|Check that the CA documents and archives each<br>revocation request and actually performed revocation<br>in a comprehensible way. Check that this<br>documentation and archiving includes at least:<br>•<br>entity that applied for revocation of a<br>certificate,<br>•<br>name of revoked subject if present and<br>known at time of revocation,<br>•<br>serial number of revoked certificate if present<br>and known at time of revocation,<br>•<br>reasonable evidence for the legitimacy of the<br>revoking party,<br>•<br>date and time of revocation,<br>•<br>date and time of invalidity, and<br>•<br>revocation reason.|<br>||☐Pass<br>☐Fail<br>☐Not applicable|
|4.7A8|1,<br>4|a new certificate for this subject has to be requested<br>following the process of initial application.|||☐Pass<br>☐Fail<br>☐Not applicable|
|4.7A9|1,<br>4|the CA creates new certificates for the subject with a<br>new key pair.|||☐Pass<br>☐Fail<br>☐Not applicable|



Federal Office for Information Security 

83 

4 Certificate life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by|
||||||the Auditor|
|4.7A10|4|Check that revocation lists of MDS certificates are|||☐Pass|
|||backed up to a physically separated server to avoid|||☐Fail|
|||||||
|||the loss of data.|||☐Not applicable|
|||||||
|4.7A11|4|Check that the integrity of the revocation|||☐Pass|
|||information is secured by appropriate means.|||☐Fail|
|||||||
||||||☐Not applicable|
|||||||
|4.7A12|4|Check that the service processing the revocation of|||☐Pass|
|||certificates ensures the processing of inquiries and|||☐Fail|
|||||||
||||||☐Not applicable|
|||||||
|4.7A13|4|Check that the CA documents and archives each|||☐Pass|
|||revocation request and actually performed revocation|||☐Fail|
||||<br>|||
|||in a comprehensible way.|||☐Not applicable|
|||||||
|||Check that this documentation and archiving||||
|||includes at least:||||
|||• entity that applied for revocation of a||||
|||certificate,||||
|||• name of revoked subject if present and||||
|||known at time of revocation,||||
|||• serial number of revoked certificate if present||||
|||and known at time of revocation,||||
|||• reasonable evidence for the legitimacy of the||||
|||revoking party,||||
|||• date and time of revocation,||||
|||• date and time of invalidity, and||||
|||• revocation reason.||||



Federal Office for Information Security 

84 

4 Certificate life cycle management 

## 4.8 Certificate suspension (if supported) 

Control procedures referenced in this Section refer to Section 7.15.7 of (ISO27099). 

Please mark if the CA supports suspension of 

☐ subscribers 

- ☐ certificates 

- ☐ both 

## ☐ none 

Note that concerning (BSI-TR-03145-4) the suspension of subscribers SHALL be provided by CAs within the CVCA-PKI. 

If suspension is supported by the CA, the following control procedures SHALL be fulfilled as requirements: 

|Requirement|TR-Part|Inspection|CA Documentation|Measures|Verdict and Explanations|
|---|---|---|---|---|---|
|||||identified by|by the Auditor|
|||||auditor||
|(1) from Section|1,|Check that the CA defines and implements a process|||☐Pass|
|7.15.7||for suspension requests as defined in section 7.15.7 (1)|||☐Fail|
||4|||||
|||of ISO 27099. Check that the security and authenticity|||☐Not applicable|
|||||||
|||of the suspension request is ensured as defined in||||
|||section 7.15.7 (1) of ISO 27099.  The auditor must check||||
|||all listed requirements of section 7.15.7 (1) separately,||||
|||thus the enumeration from (a) to (c) of ISO 27099 is||||
|||substituted by (i) to (iii) according to this TS.||||
|(2) from Section|1,|Check that the CA requirement according to section|||☐Pass|
|7.15.7||7.15.7 (2) of ISO 27099 is fulfilled.|||☐Fail|
||4|||||
||||||☐Not applicable|
|||||||
|(3) from Section|1,|Check that notification by the CA or RA is done as|||☐Pass|
|7.15.7||defined in section 7.15.7 (3) of ISO 27099.|||☐Fail|
||4|||||
||||||☐Not applicable|
|||||||



Federal Office for Information Security 

85 

4 Certificate life cycle management 

|Requirement|TR-Part|Inspection|CA Documentation|Measures|Verdict and Explanations|
|---|---|---|---|---|---|
|||||identified by|by the Auditor|
|||||auditor||
|(4) from Section|1,|Check that requests for certificate suspension are|||☐Pass|
|7.15.7||processed and validated in accordance with CP's|||☐Fail|
||4|||||
|||requirements.|||☐Not applicable|
|||||||
|||||||
|(5) from Section|1|Check that the CA updates the certificate revocation|||☐Pass|
|7.15.7||list (CRL) as defined in section 7.15.7 (5) of ISO 27099.|||☐Fail|
|||||||
||||||☐Not applicable|
|||Check that changes in certificate status are completed||||
|||||||
|||in a time frame determined by the CP.||||
||4|Check that the CA updates the suspension status|||☐Pass|
|||information when a certificate is suspended.|||☐Fail|
|||||||
||||||☐Not applicable|
|||||||
|(9) from Section|1,|Check that requirement as defined in section 7.15.7 (9)|||☐Pass|
|7.15.7||is fulfilled.|||☐Fail|
||4|||||
||||||☐Not applicable|
|||||||
||4|Check that the CA updates the suspension status|||☐Pass|
|||information upon the lifting of a certificate suspension|||☐Fail|
|||||||
|||in accordance with the CA's CP.|||☐Not applicable|
|||||||
|(10) from Section|1,|Check that the CA verifies, or requires the RA to verify,|||☐Pass|
|7.15.7||the identity and authority of the entity requesting the|||☐Fail|
||4|||||
|||lifting of a certificate suspension.|||☐Not applicable|
|||||||
|||||||
|(13) from Section|1|Check that in case a legitimate suspension request is|||☐Pass|
|7.15.7||received the suspension status information must be|||☐Fail|
|||||||
|||handled as defined in section 7.15.7 (13) of ISO 27099.|||☐Not applicable|
|||||||
|||||||
||4|Check that the CA processes and updates the|||☐Pass|
|||suspension status information in a period of|||☐Fail|
|||||||
|||[assignment: number of hours] hours in case of a|||☐Not applicable|
|||suspension.||||



Federal Office for Information Security 

86 

4 Certificate life cycle management 

|Requirement|TR-Part|Inspection|CA Documentation|Measures|Verdict and Explanations|
|---|---|---|---|---|---|
|||||identified by|by the Auditor|
|||||auditor||
|(14) from Section|1|Check that requirement according section 7.15.7 (14) of|||☐Pass|
|7.15.7||ISO 27099 is fulfilled.|||☐Fail|
|||||||
||||||☐Not applicable|
|||||||
||4|Check that the CA ensures that the suspension status|||☐Pass|
|||information is secured against failure, attacks and|||☐Fail|
|||||||
|||unauthorized modification.|||☐Not applicable|
|||||||
|||Check that the CA analyses the risk of a server failure||||
|||and attacks against the server.||||
|||Check that the IT infrastructure is deployed||||
|||redundantly, if neccessary.||||
|(15) from Section|1,|Check that the system hosting the suspension status|||☐Pass|
|7.15.7||information is protected against both system failure|||☐Fail|
||4|||||
|||and attacks.|||☐Not applicable|
|||||||
|||||||
|||Check that the CA analyses the risk of system failures as||||
|||well as attacks against the system as defined in section||||
|||7.15.7 (15) of ISO 27099.||||
|4.8A1|1|Check that certificate suspension entries remain on the<br>CRL until the expiration of the underlying certificate or<br>the expiration of the suspension, whichever is first.<br>Check if the CP specifies a maximum number for how<br>often the certificate status may be suspended and a<br>maximum time-period for the suspension status. In<br>this case, check that the CA complies to its CP.|||☐Pass<br>☐Fail<br>☐Not applicable|
||4|Not applicable to CAs affected by (BSI-TR-03145-4)|||☐Pass|
||||||☐Fail|
|||||||
||||||☐Not applicable<br>x|
|4.8A2|1|Check that the complete suspension process (i.e. the<br>delaybetween a suspension request or report and the|||☐Pass<br>☐Fail|



Federal Office for Information Security 

87 

4 Certificate life cycle management 

|Requirement|TR-Part|Inspection|CA Documentation|Measures|Verdict and Explanations|
|---|---|---|---|---|---|
|||||identified by|by the Auditor|
|||||auditor||
|||availability of the suspension status information to all<br>relying parties) is at most [assignment: number of<br>minutes] minutes.|||☐Not applicable|
||4|Check that the complete suspension process (i.e. the|||☐Pass|
|||delay between a suspension request or report and the|||☐Fail|
|||||||
|||availability of the suspension status information) is at|||☐Not applicable|
|||most [assignment: number of minutes] minutes.||||
|4.8A3|4|Check that the CA ensures that suspended subscribers|||☐Pass|
|||will not receive any certificates as long as the|||☐Fail|
|||||||
|||suspension is active.|||☐Not applicable|
|||||||
|4.8A4|4|Check that the CA defines an appropriate procedure for|||☐Pass|
|||the suspension started by an authorized subscriber|||☐Fail|
|||||||
|||suspension.|||☐Not applicable|
|||||||
|||Check that the involved parties and suspension reasons||||
|||are clearly defined.||||
|||Check that the CA ensures:||||
|||(i) the identification of persons/institutions with||||
|||legitimate claim to apply for suspension of a||||
|||subscriber: the subscriber/certificate holder,||||
|||[assignment: list of further||||
|||persons/institutions],||||
|||(ii) the identification of reasons for a suspension:||||
|||private key of certificate compromised,||||
|||incorrect information on certificate, security||||
|||incident on the IT systems of the certificate||||
|||holder/subscriber, subscriber not fulfilling||||
|||Terms and Conditions of the CA, [assignment:||||
|||other reasons for suspension],||||



Federal Office for Information Security 

88 

4 Certificate life cycle management 

|Requirement|TR-Part|Inspection|CA Documentation|Measures|Verdict and Explanations|
|---|---|---|---|---|---|
|||||identified by|by the Auditor|
|||||auditor||
|||(iii) [assignment: the transmission path and record||||
|||of the suspension],||||
|||(iv) [assignment: additional requirements for a||||
|||successful suspension],||||
|||(v) The suspension of a subscriber may only be||||
|||cancelled, if the cause for the suspension has||||
|||been solved.||||
|4.8A5|4|Check that the CA ensures that suspension information|||☐Pass|
|||are up-to-date and accessible by the registration and|||☐Fail|
|||||||
|||the certification processes as well.|||☐Not applicable|
|||||||



## 4.9 Revocation status information service 

Control procedures referenced in this Section refer to Section 7.15.8 of (ISO27099). 

Please mark, how revocation status information are provided by the CA (multiple selection possible) 

☐ CRL 

☐ OCSP 

☐ others:____________________ 

Note that concerning (BSI-TR-03145-4) only MDS certificates within the CVCA-eID PKI are revoked. Therefore, the requirements in this section apply to MDS certificates within the CVCA-eID PKI only. 

Concerning the revocation status information service the following control procedure SHALL be fulfilled as requirements: 

Federal Office for Information Security 

89 

4 Certificate life cycle management 

|Require-|TR-|Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|Part||||Explanations by the|
||||||Auditor|
|(1) from|1,|Check that the CA makes certificate status|||☐Pass|
|Section||information available to all relevant parties via an|||☐Fail|
||4|||||
|7.15.8||mechanism as defined in section 7.15.8 (1) of ISO|||☐Not applicable|
|||27099.||||
|||||||
|(2) from|1,|If CRLs are used:|||☐Pass|
|Section|||||☐Fail|
||4|Check that the CA digitally signs each CRL so that all||||
|7.15.8|||||☐Not applicable|
|||requirements of section 7.15.8 (2) of ISO 27099 are||||
|||||||
|||fulfilled.||||
|(3) from|1,|If CRLs are used:|||☐Pass|
|Section|||||☐Fail|
||4|Check that the CA issues CRLs at regular intervals as||||
|7.15.8|||||☐Not applicable|
|||defined in section 7.15.8 (3) of ISO 27099.||||
|||||||
|||||||
|(4) from|1,|If CRLs are used:|||☐Pass|
|Section|||||☐Fail|
||4|Check that at a minimum, that a CRL entry||||
|7.15.8|||||☐Not applicable|
|||identifying the revocation of certificates remains on||||
|||||||
|||||||
|||Check if a retrospective view of a certificate status, at||||
|||a given point in time, is required. If this is the case,||||
|||check that CRL entries are held beyond the life of a||||
|||certificate validity period to prove its validity at the||||
|||time of use.||||
|(5) from|1|If CRLs are used:|||☐Pass|
|Section|||||☐Fail|
|||If certificate suspension is used, check that the||||
|7.15.8|||||☐Not applicable|
|||requirements according to section 7.15.8 (5) of ISO||||
|||||||
|||27099 are fulfilled.||||
||4|Not applicable to CAs affected by (BSI-TR-03145-4)|||☐Pass|
||||||☐Fail|
|||||||



Federal Office for Information Security 

90 

4 Certificate life cycle management 

||||||☐Not applicable<br>x|
|---|---|---|---|---|---|
|(6) from|1,|If CRLs are used:|||☐Pass|
|Section|||||☐Fail|
||4|Check that the CRL are retained and archived as||||
|7.15.8|||||☐Not applicable|
|||defined in section 7.15.8 (6) of ISO 27099.||||
|||||||
|||||||
|(7) from|1,|If CRLs are used:|||☐Pass|
|Section|||||☐Fail|
||4|Check that all requirements of section 7.15.8 (7) of ISO||||
|7.15.8|||||☐Not applicable|
|||27099 are fulfilled, when issuing CRLs.||||
|||||||
|||||||
|(9) from|1|If online certificate status mechanisms (e.g. OCSP) are|||☐Pass|
|Section||used:|||☐Fail|
|||||||
|7.15.8|||||☐Not applicable|
|||Check that all response messages are digitally signed||||
|||||||
|||and include all required data  as defined  within the||||
|||underlying  CP.||||
||4|Not applicable to CAs affected by (BSI-TR-03145-4)|||☐Pass|
||||||☐Fail|
|||||||
||||||☐Not applicable<br>x|
|(10) from|<br>1|If online certificate status mechanisms (e.g. OCSP) are|||☐Pass|
|Section||used:|||☐Fail|
|||||||
|7.15.8|||||☐Not applicable|
|||Check that the requirements as defined in 7.15.8 (10)||||
|||||||
|||of ISO 27099 are fulfilled.||||
||4|Not applicable to CAs affected by (BSI-TR-03145-4)|||☐Pass|
||||||☐Fail|
|||||||
||||||☐Not applicable<br>x|
|4.9A1|1|Check that the CA ensures that that the revocation<br>information is continuously available and accessible<br>to the relying parties.|||☐Pass<br>☐Fail<br>☐Not applicable|
||4|Check that the CA ensurs that the status information|||☐Pass|
|||of certificates or subscribers is continuously available|||☐Fail|
|||||||
|||and accessible to the relevant parties.|||☐Not applicable|
|||||||



Federal Office for Information Security 

91 

4 Certificate life cycle management 

|4.9A2|1,<br>4|Check that the CA ensures that the provided<br>revocation information is up to date.|||☐Pass<br>☐Fail<br>☐Not applicable|
|---|---|---|---|---|---|
|4.9A3|1,<br>4|Check that the Servers hosting the maintained<br>revocation information are hardened against failure<br>and attacks.<br>Check that the hardening against failure and attacks<br>is based on the risk analysis.|||☐Pass<br>☐Fail<br>☐Not applicable|



## 4.10 Validation Model 

Concerning the validation model the following requirements apply: 

|Require-||Inspection|CA Documentation|Measures identified by auditor|Verdict and|
|---|---|---|---|---|---|
|ment|||||Explanations by the|
||||||Auditor|
|4.10A1|1,<br>4|Check that within the whole PKI in which the CA is<br>active, one validation model is consistently applied.<br>Check that the CA ensures a consistent application of<br>the validation model for all of its operations such that<br>the validity periods of all certificates in a certificate<br>chain are chosen according to the chosen validation<br>model.|||☐Pass<br>☐Fail<br>☐Not applicable|
|4.10A2|1|Check that the Shell Model is used. If the CA uses a<br>different validation model, check that the CA justifies<br>its reasons.|||☐Pass<br>☐Fail<br>☐Not applicable|
||4|Check that the Shell Model is used.|||☐Pass|
||||||☐Fail|
|||||||
||||||☐Not applicable|



Federal Office for Information Security 

92 

Bibliography 

## Bibliography 

BSI-TR-02102. _Bundesamt für Sicherheit in der Informationstechnik: Kryptographische Verfahren: Empfehlungen und Schlüssellängen_ . kein Datum. 

- BSI-TR-03107. _Bundesamt für Sicherheit in der Informationstechnik: Elektronische Identitäten und Vertrauensdienste im E-Government, Teil 1: Vretrauensniveau und Mechanismen_ . kein Datum. 

- BSI-TR-03110. „Bundesamt für Sicherheit in der Informationstechnik: Advanced Security Mechanisms for Machine Readable Travel Documents and eIDAS token.“ kein Datum. 

BSI-TR-03116. _Bundesamt für Sicherheit in der Informationstechnik: Kryptographische Vorgaben für Projekte der Bundesregierung_ . kein Datum. 

- BSI-TR-03116-2. „Bundesamt für Sicherheit in der Informationstechnik: Kryptographische Vorgaben gür Projekte der Bundesregierung, Teil 2: Hoheitliche und eID-Dokumente.“ kein Datum. 

BSI-TR-03145. „Bundesamt für Sicherheit in der Informationstechnik: Secure CA operation.“ kein Datum. 

- BSI-TR-03145-1. „Bundesamt für Sicherheit in der Informationstechnik: Secure CA operation, Part 1: Generic requirements for a Certification Authority in a Public Key Infrastructure with security level 'high'.“ kein Datum. 

- BSI-TR-03145-4. „Bundesamt für Sicherheit in der Informationstechnik: Secure CA operation.“ Part 4: Specific requirements for a Certification Authority in a Public Key Infrastructure for the Extended Access Control of the German Official Travel Documents according to BSI TR-03110. 

- BSI-TR-03145-5. „Bundesamt für Sicherheit in der Informationstechnik: Secure CA operation.“ Part 5: Specific requirements for a Public Key Infrastructure for Technical Security Systems. 

ETSI102042. „ETSI TS 102 042: Policy requirements for certification authorities issuing public key certificates.“ kein Datum. 

ISO15408. „ISO/IEC 15408: Information technology -- Security techniques -- Evaluation criteria for IT security .“ kein Datum. 

ISO27001. „ISO/IEC 27001: Information security management systems — Requirements.“ 2022. 

ISO27099. „ISO/IEC 27099: Information technology — Public key infrastructure — Practices and policy framework.“ 2022. 

KLSR. „Bundesamt für Sicherheit in der Informationstechnik: Key Lifecycle Security Requirements.“ kein Datum. 

RFC2119. _Bradner, S.: Key words for use in RFCs to Indicate Requirement Levels_ . https://datatracker.ietf.org/doc/html/rfc2119: IETF, kein Datum. 

RFC5280. _Cooper, D.; Santesson, S.; Farrell, S.; Boeyen, S.; Housley, R.; Polk, W.: RFC5280 Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile_ . https://datatracker.ietf.org/doc/html/rfc5280: IETF, kein Datum. 

Federal Office for Information Security 

93 


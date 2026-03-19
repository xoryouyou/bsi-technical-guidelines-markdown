BSI Technical Guideline TR-03121-3 

## Biometrics for Public Sector Applications 

Part 3: Application Profiles, Function Modules and Processes 

Volume 1: Border Control (BCL) 

Version 7.0 

Federal Office for Information Security PO Box 20 03 63 53133 Bonn E-Mail: trbiometrics@bsi.bund.de Internet: https://bsi.bund.de © Federal Office for Information Security 2025 

BSI Technical Guideline TR-03121-3 

Federal Office for Information Security 

iii 

Table of Contents 

## Table of Contents 

|1|Volume Border Control ................................................................................................................. 1|
|---|---|
|2|Application Profiles ....................................................................................................................... 2|
|2.1|Application Profile Manual Border Control ............................................................................. 2|
|2.2|Application Profile Facial Image Acquisition System Manual Border Control ............................. 3|
|2.3|Application Profile Mobile Manual Border Control .................................................................. 4|
|2.4|Application Profile Semi-Mobile Manual Border Control ......................................................... 5|
|2.5|Application Profile Automated Border Control (Face-Verification Only) ................................... 6|
|2.6|Application Profile Self-Service System ................................................................................... 8|
|2.7|Application Profile Biometric Matching Systems ..................................................................... 9|
|3|Partial Application Processes ........................................................................................................ 12|
|3.1|PAP ACQ-FI-SV-5: Supervised Facial Image Acquisition System ............................................. 12|
|3.2|PAP ACQ-FI-SV-4: Supervised Facial Image Acquisition ......................................................... 13|
|3.3|PAP ACQ-FI-USV-1: Unsupervised Facial Image Acquisition with Prequalification .................. 15|
|3.4|PAP VER-FI-ALL-1: Facial Image Verification ........................................................................ 16|
|3.5|PAP ACQ-FI-AUTO-1: Automated Facial Image Acquisition ................................................... 17|
|3.6|PAP ACQ-FPS-SV-1: Supervised Acquisition Single Slap ......................................................... 19|
|3.7|PAP ACQ-FPS-USV-1: Unsupervised Acquisition Slap ............................................................ 22|
|3.8|PAP ID-1: CIR Identification ................................................................................................. 24|
|3.9|PAP ASS-B-USV-1: Assess Unsupervised Acquired Biometrics ................................................ 24|
|3.10|PAP EVA-ID-wCIR-1: Identification Evaluation Workflow for BMS with Identification Capability|
||and with Verification Capability ............................................................................................ 25|
|3.11|PAP EVA-VER-wCIR-1: Verification Evaluation Workflow for BMS with Identification Capability|
||and with Verification Capability ............................................................................................ 30|
|3.12|PAP EVA-VER-nCIR-1: Verification Evaluation Workflow for BMS without Identification Capabi|
||lity ....................................................................................................................................... 35|
|3.13|PAP UPD-B-EES-1: Update EES Reference Biometrics ............................................................ 41|
|4|Function Modules ........................................................................................................................ 47|
|4.1|FM Category Acquisition Hardware ....................................................................................... 47|
|4.2|FM Category Acquisition Software ........................................................................................ 52|
|4.3|FM Category Biometric Image Processing .............................................................................. 55|
|4.4|FM Category Quality Assessment .......................................................................................... 56|
|4.5|FM Category Presentation Attack Detection .......................................................................... 62|
|4.6|FM Category Compression .................................................................................................... 65|
|4.7|FM Category Operation ........................................................................................................ 66|
|4.8|FM Category User Interface .................................................................................................. 68|
|4.9|FM Category Reference Storage ............................................................................................. 71|
|4.10|FM Category Biometric Comparison ..................................................................................... 72|
|4.11|FM Category Logging ............................................................................................................ 73|
|4.12|FM Category Coding ............................................................................................................. 76|
|4.13|FM Category Evaluation ....................................................................................................... 78|
||List of Abbreviations .................................................................................................................... 79|



Federal Office for Information Security 

iv 

Table of Contents 

Bibliography ................................................................................................................................ 81 

Federal Office for Information Security 

v 

List of Figures 

## List of Figures 

2.1. Overview Process of Manual Border Control ................................................................................... 2 2.2. Overview Process of Facial Image Acquisition System at MBC Border Crossing ................................. 4 2.3. Overview Process of Semi-Mobile Manual Border Control ............................................................... 5 2.4. Overview Process of ABC (Face-Verification Only) Border Crossing .................................................. 7 2.5. Overview Process of Self-Service System Usage ............................................................................... 8 2.6. Overall BMS Process .................................................................................................................... 10 3.1. Supervised Facial Image Acquisition System: Overall Process ......................................................... 13 3.2. Partial Application Process Task "Capture Live Facial Image" ......................................................... 13 3.3. Partial Application Process "Supervised Facial Image Acquisition" .................................................. 14 3.4. Partial Application Process Task "Capture Live Facial Image" ......................................................... 15 3.5. Partial Application Process "Unsupervised Facial Image Acquisition with Prequalification" .............. 16 3.6. Partial Application Process Task "Capture Live Facial Image" ......................................................... 16 3.7. Partial Application Process "Facial Image Verification" .................................................................. 17 3.8. Partial Application Process "Automated Facial Image Acquisition" .................................................. 18 3.9. Partial Application Process Task "Capture Live Facial Image" ......................................................... 19 3.10.Partial Application Process "Supervised Acquisition Slap" .............................................................. 19 3.11.Partial Application Process Task "Capture Slap Supervised" ............................................................ 21 3.12.Partial Application Process Task "Capture Plain Fingerprint Supervised" ......................................... 22 3.13.Partial Application Process "Unsupervised Acquisition Slap" .......................................................... 22 3.14.Partial Application Process Task "Capture Slap Unsupervised" ........................................................ 24 3.15.Partial Application Process "CIR Identification" ............................................................................. 24 3.16.Partial Application Process "Assess Unsupervised Acquired Biometrics" .......................................... 25 3.17.Overall Identification Workflow ................................................................................................... 28 3.18.Evaluation Workflow for Identification ......................................................................................... 28 3.19.Use of Operator Decisions as a Background Filter .......................................................................... 30 3.20.Overall Verification Workflow with CIR ........................................................................................ 33 3.21.Verification Evaluation Workflow with Connected Identity Register .............................................. 33 3.22.Use of Operator Decisions as a Background Filter .......................................................................... 35 3.23.Overall Verification Workflow without CIR .................................................................................. 38 3.24.Verification Evaluation Workflow without Connected Identity Register ......................................... 39 

Federal Office for Information Security 

vi 

List of Figures 

3.25.Use of Operator Decisions as a Background Filter .......................................................................... 41 3.26.Partial Application Process "Update CIR Reference Biometrics" ...................................................... 42 3.27.Partial Application Process Task "EES Biometric Update Facial Images" .......................................... 43 3.28.Partial Application Process Task "EES Biometric Update Fingerprints" ............................................ 43 4.1. Example: In the sketch beta1 is lower than or equal 45° and beta2 is lower than or equal 135°. The struc tural observability is therefore given. ............................................................................................ 67 

Federal Office for Information Security 

vii 

List of Figures 

Federal Office for Information Security 

viii 

1 Volume Border Control 

## 1 Volume Border Control 

BSI TR-03121, Volume 1 Border Control (BCL), covers the biometric processes of border control. Thereby, en rolment of the biometric subject's biometric characteristics as well as identification and verification of bio metric subjects' identities with the help of biometric characteristics are subprocesses of the general border control processes. Biometric characteristics used in border control processes are facial images (FIs) and plain fingerprints (FPs). 

In addition to the requirements of this technical guideline further standards SHALL be applied: 

- [BIB_ISO_39794_FINGER] 

- [BIB_ISO_39794_FACE] 

- [BIB_ISO_19794_FINGER] 

- [BIB_ISO_19794_FACE] 

The ISO/IEC 39794 series succeeds the ISO/IEC 19794 series of international standards for biometric data interchange formats. The following transition time table has been defined: 

- The ISO/IEC 19794-4 and -5 SHOULD be readable, despite the introduction of the ISO/IEC 39794 series; 

- From 2030-01-01 on, passport issuers SHALL use the tagged binary data formats specified in ISO/IEC 39794-4 and -5 for encoding biometric data. However, document reader SHOULD be able to process the ISO/IEC 39794 series from 2026-01-01 on. 

Federal Office for Information Security 

1 

2 Application Profiles 

## 2 Application Profiles 

The following sections specify the Application Profiles of this Volume. The processes specified by the Appli cation Profiles of this Volume support a number of border control configurations. 

## 2.1 Application Profile Manual Border Control 

This Application Profile specifies the requirements for Manual Border Control (MBC) systems equipped with a facial image acquisition system and a fingerprint acquisition system. 

## 2.1.1 Mandatory Process 

The following subsections specify the overall process of the biometric operations of the MBC and the bio metric border control checks required per border control use case at the MBC. 

## 2.1.1.1 Overview Process 

Figure 2.1 depicts the general biometric process of the MBC. The ad hoc process depicted is for illustration purpose only. 

At the MBC the border guard assesses alphanumeric and biometric candidate lists. In case true matches are identified, the border guard takes the necessary actions such as guiding the traveller to the second line or linking existing records. The border guard acquires missing biometric modalities or assesses the biometric modalities acquired unsupervised at a downstream system. In addition, the border guard assesses biometric verification results. 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0010-10.png)


**----- Start of picture text -----**<br>
FM COD-FP-VER<br>FM CMP-FP-VER<br>Verify live<br>Fingerprints<br>against eMRTD<br>FM COD-FI-VER<br>FM CMP-FI-VER<br>PAP Supervised  Verify live<br>Facial Image  Facial Image<br>Acquisition System against eMRTD<br>Yes<br>acquired biometric Prior downstream characteristics unsupervised  No Facial ImageAcquire live  if applicable for traveller in use case if applicable for traveller in use case<br>available? Any restriction for FI acquisition  Yes<br>Start Yes No Any restriction for FP acquisition present?present? No Acquire live Fingerprints PAP Verication Evaluation  if applicable for traveller in use caseagainst CIR(s)Fingerprints Verify live  Identify live in PAP CIR IdenticationCIR(s) identication verifcation / Assess results Discard biometric and/or results?characteristics No Default End<br>Yes Workow For BMS<br>Without<br>PAP Supervised Acquisition Single Slap Identication Capability against CIR(s)Facial Image Verify live  PAP Assess Unsupervised Acquired Biometrics<br>Evaluation<br>Workow<br>Assess<br>Unsupervised<br>Biometrics<br>Process may be interrupted at any point by the border  Send traveller to second line<br>guard<br>**----- End of picture text -----**<br>


**Figure 2.1.** Overview Process of Manual Border Control 

## 2.1.2 Mandatory Function Modules 

All Function Modules which SHALL be applied for this Application Profile are listed in Table 2.1. All listed Function Modules (separated by commas) are REQUIRED for this Application Profile unless specified other wise. Function Modules separated by slash are alternatives to each other. Function Modules in brackets are RECOMMENDED. 

|**Module Category**|**Required Function Modules**|
|---|---|
|Acquisition Hardware|FM AH-FP-OPT|
|Acquisition Software|FM AS-FP-MF,<br>FM AS-FP-SLP|
|Biometric Image Processing|FM BIP-FP-APP|



Federal Office for Information Security 

2 

2 Application Profiles 

|**Module Category**|**Required Function Modules**|
|---|---|
|Quality Assessment|FM QA-FP-APP|
|Presentation Attack Detec<br>tion|FM PAD-FP-APP1|
|Compression|FM COM-FI-GENERIC,<br>FM COM-FI-BCL,<br>FM COM-FP-WSQ,<br>FM COM-FP-BCL|
|Operation|FM O-ALL-LNK|
|User Interface|FM UI-FI-OP,<br>FM UI-FP-OP|
|Reference Storage|FM REF-FP-EES,<br>FM REF-FI-EES|
|Biometric Comparison|FM CMP-FI-VER,<br>FM CMP-FP-VER|
|Logging|FM LOG-ALL-GENERIC,<br>FM LOG-ALL-BCL,<br>FM LOG-FI-GENERIC,<br>FM LOG-FP-GE<br>NERIC|
|Coding|FM COD-ALL-BCL,<br>FM COD-FI-VER (for FI verification logging),<br>FM COD-FI-EES (for FI<br>data to CS EES),<br>FM COD-FP-EES (for FP data to CS EES),<br>FM COD-FP-VER|
|Evaluation|-|



**Table 2.1** Required Function Modules for Application Profile Manual Border Control 

## 2.1.3 Mandatory Application Profiles 

For the acquisition of facial images, the Application Profile Facial Image Acquisition System Manual Border Control SHALL be applied by this Application Profile. 

## 2.1.4 Mandatory Partial Application Processes 

All Partial Application Processes and Tasks which SHALL be applied for this Application Profile are listed in Table 2.2. All listed Processes (separated by commas) are REQUIRED for this Application Profile unless specified otherwise. Processes separated by slash are alternatives to each other. 

|**No.**|**Required Partial Application Process**|
|---|---|
|1|PAP ASS-B-USV-1: Assess Unsupervised Acquired Biometrics|
|2|PAP ID-1: CIR Identification|
|3|PAP EVA-VER-nCIR-1: Verification Evaluation Workflow for BMS without Identification Capability|
|4|PAP ACQ-FPS-SV-1: Supervised Acquisition Single Slap|



**Table 2.2** Required Partial Application Processes Application Profile Manual Border Control 

## 2.2 Application Profile Facial Image Acquisition System Manual Border Control 

This Application Profile specifies a facial image acquisition system for manual border control booths. The facial image acquisition system is used to automatically acquire or manually capture facial images for enrol ment, verification or identification purposes. 

## 2.2.1 Mandatory Process 

The following subsection specifies the overall process of the biometric operations of a facial image acquisition system used at the MBC. 

## 2.2.1.1 Overview Process 

Figure 2.2 depicts the general biometric process of the facial image acquisition system. Note, that PAP ACQFI-SV-5: Supervised Facial Image Acquisition System is used here. 

Federal Office for Information Security 

3 

2 Application Profiles 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0012-01.png)


**----- Start of picture text -----**<br>
Acquire live<br>Facial Image<br>Start End<br>PAP Supervised Facial Image Acquisition System<br>**----- End of picture text -----**<br>


**Figure 2.2.** Overview Process of Facial Image Acquisition System at MBC Border Crossing 

## 2.2.2 Mandatory Function Modules 

All Function Modules which SHALL be applied for this Application Profile are listed in Table 2.3. All listed Function Modules (separated by commas) are REQUIRED for this Application Profile unless specified other wise. Function Modules separated by slash are alternatives to each other. Function Modules in brackets are RECOMMENDED. 

|**Module Category**|**Required Function Modules**|
|---|---|
|Acquisition Hardware|FM AH-FI-ICS,<br>FM AH-FI-BCL|
|Acquisition Software|FM AS-FI-ICS,<br>FM AS-FI-ICS3|
|Biometric Image Processing|FM BIP-FI-APP|
|Quality Assessment|FM QA-FI-PRE,<br>FM QA-FI-GENERIC,<br>FM QA-FI-BCL|
|Presentation Attack Detection|-|
|Compression|FM COM-FI-GENERIC,<br>FM COM-FI-BCL|
|Operation|FM O-ALL-USV,<br>FM O-FI-ALL,<br>FM O-FI-DC|
|User Interface|FM UI-FI-BSJ|
|Reference Storage|-|
|Biometric Comparison|-|
|Logging|FM LOG-ALL-BCL,<br>FM LOG-FI-GENERIC|
|Coding|FM COD-ALL-EES,<br>FM COD-FI-GENERIC|
|Evaluation|-|



**Table 2.3** Required Function Modules for Application Profile Facial Image Acquisition Manual Border Control 

## 2.2.3 Mandatory Partial Application Processes 

All Partial Application Processes and Tasks which SHALL be applied for this Application Profile are listed in Table 2.4. All listed Processes (separated by commas) are REQUIRED for this Application Profile unless specified otherwise. Processes separated by slash are alternatives to each other. 

|**No.**|**Required Partial Application Process**|
|---|---|
|1|PAP ACQ-FI-SV-5: Supervised Facial Image Acquisition System|
|2|PAP ACQ-FI-AUTO-1: Automated Facial Image Acquisition|



**Table 2.4** Required Partial Application Processes Application Profile Facial Image Acquisition Manual Border Control 

## 2.3 Application Profile Mobile Manual Border Control 

This Application Profile specifies the requirements for a mobile manual border control with handheld devices. It will be amended in a future version of this Technical Guideline (TR). 

Federal Office for Information Security 

4 

2 Application Profiles 

## 2.4 Application Profile Semi-Mobile Manual Border Control 

This Application Profile specifies the requirements for semi-mobile MBC systems equipped with a facial image camera and a fingerprint acquisition system. 

## 2.4.1 Mandatory Process 

Figure 2.3 depicts the acquisition process at the semi-mobile manual border control. Semi-mobile equip ment is meant to be portable (e.g. placed within in a suit-case), but is not hand-held. 

In general, the biometric data of the biometric subject SHALL be captured sequentially. Depending on the use case it is required to acquire fingerprints and / or a facial image of the biometric subject. For all acquisitions enrolment quality SHALL be used in order to simplify the over all processes (e.g. a facial image that has been used for a verification is not needed to be recaptured for an enrolment). 

In the end the acquired biometrics are used for enrolment, verifications and / or identifications within one or multiple Central Indentity Registers (CIRs). 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0013-07.png)


**----- Start of picture text -----**<br>
PAP Supervised<br>Acquisition<br>Single Slap<br>Acquire 4 Flat<br>Fingerprints<br>Facial<br>Enrolment in  Verication  Image  Identication<br>CIR against CIR Verication  within CIR<br>Facial Image  against (e)MRTD<br>Start Acquisition  End<br>required Acquire Facial<br>Image with<br>Digital Camera<br>PAP Supervised<br>Facial Image<br>Acquisition<br>**----- End of picture text -----**<br>


**Figure 2.3.** Overview Process of Semi-Mobile Manual Border Control 

## 2.4.2 Mandatory Function Modules 

All Function Modules which SHALL be applied for this Application Profile are listed in Table 2.5. All listed Function Modules (separated by commas) are REQUIRED for this Application Profile unless specified other wise. Function Modules separated by slash are alternatives to each other. Function Modules in brackets are RECOMMENDED. 

|**Module Category**|**Required Function Modules**|
|---|---|
|Acquisition Hardware|FM AH-FI-DC,<br>FM AH-FP-OPT|
|Acquisition Software|FM AS-FI-DC,<br>FM AS-FP-MF,<br>FM AS-FP-SLP|
|Biometric Image Processing|FM BIP-FI-APP,<br>FM BIP-FP-APP|
|Quality Assessment|FM QA-FI-GENERIC,<br>FM QA-FI-BCL,<br>FM QA-FP-APP|
|Presentation Attack Detection|FM PAD-FP-APP1|
|Coding|FM COD-ALL-BCL,<br>FM COD-ALL-EES,<br>FM COD-FI-GENERIC,<br>FM<br>COD-FI-EES,<br>FM COD-FP-EES|
|Compression|FM COM-FI-GENERIC,<br>FM COM-FI-BCL,<br>FM COM-FP-BCL,<br>FM<br>COM-FP-WSQ|
|Operation|FM O-FI-ALL,<br>FM O-FI-DC,<br>FM O-FP-ALL|
|User Interface|FM UI-FI-OP,<br>FM UI-FP-OP|
|Reference Storage|-|



Federal Office for Information Security 

5 

2 Application Profiles 

|**Module Category**|**Required Function Modules**|
|---|---|
|Biometric Comparison|-|
|Logging|FM LOG-ALL-GENERIC,<br>FM LOG-ALL-BCL,<br>FM LOG-FI-GENERIC,<br>FM LOG-FP-GENERIC|
|Evaluation|-|



**Table 2.5** Required Function Modules for Application Profile Semi-Mobile Manual Border Control 

## 2.4.3 Mandatory Partial Application Processes 

All Partial Application Processes and Tasks which SHALL be applied for this Application Profile are listed in Table 2.6. All listed Processes (separated by commas) are REQUIRED for this Application Profile unless specified otherwise. Processes separated by slash are alternatives to each other. 

|**No.**|**Required Partial Application Process**|
|---|---|
|1|PAP ACQ-FI-SV-4: Supervised Facial Image Acquisition|
|2|PAP ACQ-FPS-SV-1: Supervised Acquisition Single Slap|



**Table 2.6** Required Partial Application Processes Application Profile Semi-Mobile Manual Border Control 

## 2.5 Application Profile Automated Border Control (Face-Verification Only) 

This Application Profile specifies the requirements for integrated two-step man trap Automated Border Con trol (ABC) (Face-Verification Only) which are equipped with a facial image acquisition system inside the man trap and a document reader at the entrance of the system. 

## 2.5.1 Mandatory Process 

The following subsections specify the overall process of biometric operations of the ABC (Face-Verification Only) and the biometric border control checks required per border control use case at the ABC (Face-Verifi cation Only). 

Note, this is an one modality system with a facial image camera for face verification with Presentation Attack Detection (PAD) only. The acquired images in this system do not have enrolment quality. 

## 2.5.1.1 Overview Process 

Figure 2.4 depicts the general biometric process of the ABC (Face-Verification Only). 

If the candidate's facial image is not available or an PAD alarm is triggered, the situation MUST be checked by a border guard. 

Also, if any verification fails, the situation MUST be checked by a border guard. 

Federal Office for Information Security 

6 

2 Application Profiles 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0015-01.png)


**----- Start of picture text -----**<br>
Situation has to be<br>checked by a border<br>guard<br>No No<br>Acquire Facial  Yes Verication  Yes<br>Image Process<br>Start Facial Image  Default End<br>All verications<br>available AND no<br>successful?<br>PAD alarm?<br>PAP Unsupervised Facial Image  PAP Facial Image<br>Acquisition with Prequalication Verication<br>**----- End of picture text -----**<br>


**Figure 2.4.** Overview Process of ABC (Face-Verification Only) Border Crossing 

## 2.5.2 Mandatory Function Modules 

All Function Modules which SHALL be applied for this Application Profile are listed in Table 2.7. All listed Function Modules (separated by commas) are REQUIRED for this Application Profile unless specified other wise. Function Modules separated by slash are alternatives to each other. Function Modules in brackets are RECOMMENDED. 

|**Module Category**|**Required Function Modules**|
|---|---|
|Acquisition Hardware|FM AH-FI-EGT,<br>FM AH-FI-ICS|
|Acquisition Software|FM AS-FI-ICS|
|Biometric Image Processing|FM BIP-FI-APP|
|Quality Assessment|FM QA-FI-PRE|
|Presentation Attack Detec<br>tion|FM PAD-FI-APP|
|Compression|FM COM-FI-GENERIC,<br>FM COM-FI-BCL|
|Operation|FM O-ALL-USV,<br>FM O-FI-DC|
|User Interface|FM UI-FI-OP,<br>FM UI-FI-BSJ|
|Reference Storage|-|
|Biometric Comparison|FM CMP-FI-VER|
|Logging|FM LOG-ALL-GENERIC,<br>FM LOG-ALL-BCL,<br>FM LOG-FI-GENERIC|
|Coding|FM COD-ALL-BCL,<br>FM COD-FI-GENERIC,<br>FM COD-FI-VER (for FI verification logging),<br>FM COD-FI-EES (for FI data to Central System EES (CS EES))|
|Evaluation|-|



**Table 2.7** Required Function Modules for Application Profile Automated Border Control 

## 2.5.3 Mandatory Partial Application Processes 

All Partial Application Processes and Tasks which SHALL be applied for this Application Profile are listed in Table 2.8. All listed Processes (separated by commas) are REQUIRED for this Application Profile unless specified otherwise. Processes separated by slash are alternatives to each other. 

|**No.**|**Required Partial Application Process**|
|---|---|
|1|PAP ACQ-FI-USV-1: Unsupervised Facial Image Acquisition with Prequalification|
|2|PAP VER-FI-ALL-1: Facial Image Verification|



Federal Office for Information Security 

7 

2 Application Profiles 

## **No. Required Partial Application Process** 

3 PAP EVA-VER-nCIR-1: Verification Evaluation Workflow for BMS without Identification Capability 

**Table 2.8** Required Partial Application Processes Application Profile Automated Border Control 

## 2.6 Application Profile Self-Service System 

This Application Profile specifies the requirements for self-service systems (SSSs) equipped with a facial image acquisition system, a fingerprint acquisition system and a document reader. 

## 2.6.1 Mandatory Process 

The following subsections specify the overall process of the biometric operations of the SSS and the biometric border control checks required per border control use case at the SSS. 

## 2.6.1.1 Overview Process 

Figure 2.5 depicts the general biometric process of the SSS. 

A live facial image of the biometric subject is acquired. In some of the use cases the acquisition of the finger prints is started in parallel. In case an applicable biometric modality could not be acquired from the biometric subject, the following process steps requiring this modality are skipped and the next border control step is the MBC. 

Afterwards, the verification of the live facial image is carried out against the reference facial image on the Electronic Machine Readable Travel Document (eMRTD) and the evaluation workflow is started. In some use cases fingerprint verifications against CIRs (e.g. CS EES or Visa Information System (VIS)) are performed in parallel. If the verification against a CIR failed, an identification is performed within the same system which SHALL be multimodal if possible. The retrieval of the identification results SHALL never block the release message to the biometric subject to proceed to the next border control system. 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0016-12.png)


**----- Start of picture text -----**<br>
PAP Verication Evaluation Workow For<br>PAP Automated Facial Image Acquisition BMS Without Identication Capability<br>Movement traveller (Freedom of  Facial ImageAcquire live  Evaluation Workow<br>and FI acquisition<br>already conducted)<br>OR (FI and FP<br>acquistion already  FP age restriction<br>conducted)? traveller has applies OR  PAP Unsupervised Acquisition Slap Freedom of  PAP CIR Identication For previously failed Verications against CIR(s) only<br>Freedom of  Movement<br>Movement? traveller?<br>Start YesNo YesNo Acquire live Fingerprints traveller to next border control systemGuide YesNo against CIR(s)Fingerprints Verify live  Identify live in CIR(s) Default End<br>traveller to next border control systemGuide against eMRTDFacial Image Verify live<br>FM COD-FI-VER<br>FM CMP-FI-VER<br>**----- End of picture text -----**<br>


**Figure 2.5.** Overview Process of Self-Service System Usage 

## 2.6.2 Mandatory Function Modules 

All Function Modules which SHALL be applied for this Application Profile are listed in Table 2.9. All listed Function Modules (separated by commas) are REQUIRED for this Application Profile unless specified other wise. Function Modules separated by slash are alternatives to each other. Function Modules in brackets are RECOMMENDED. 

|**Module Category**|**Required Function Modules**|
|---|---|
|Acquisition Hardware|FM AH-ALL-SSS,<br>FM AH-FI-ICS,<br>FM AH-FI-BCL,<br>FM AH-FI-SSS,<br>FM AH-FP-OPT,<br>FM AH-FP-SSS|
|Acquisition Software|FM AS-FI-ICS,<br>FM AS-FI-ICS3,<br>FM AS-FP-MF,<br>FM AS-FP-SLP|
|Biometric Image Processing|FM BIP-FI-APP,<br>FM BIP-FP-APP|



Federal Office for Information Security 

8 

2 Application Profiles 

|**Module Category**|**Required Function Modules**|
|---|---|
|Quality Assessment|FM QA-FI-GENERIC,<br>FM QA-FI-BCL,<br>FM QA-FP-APP|
|Presentation Attack Detec<br>tion|FM PAD-FI-APP,<br>FM PAD-FP-APP1|
|Compression|FM COM-FI-GENERIC,<br>FM COM-FI-BCL,<br>FM COM-FP-WSQ,<br>FM COM-FP-BCL,<br>FM<br>COM-CCTV-JPG|
|Operation|FM O-ALL-USV,<br>FM O-FI-ALL,<br>FM O-FI-DC,<br>FM O-FP-ALL|
|User Interface|FM UI-FI-BSJ,<br>FM UI-FP-BSJ|
|Reference Storage|-|
|Biometric Comparison|FM CMP-FI-VER,<br>FM CMP-FP-VER|
|Logging|FM LOG-ALL-GENERIC,<br>FM LOG-ALL-BCL,<br>FM LOG-FI-GENERIC,<br>FM LOG-FP-GE<br>NERIC|
|Coding|FM COD-ALL-BCL,<br>FM COD-FI-VER (for FI verification logging),<br>FM COD-FI-EES (for<br>FI data to CS EES),<br>FM COD-FP-EES (for FP data to CS EES)|
|Evaluation|-|



**Table 2.9** Required Function Modules for Application Profile Self-Service System 

## 2.6.3 Mandatory Partial Application Processes 

All Partial Application Processes and Tasks which SHALL be applied for this Application Profile are listed in Table 2.10. All listed Processes (separated by commas) are REQUIRED for this Application Profile unless specified otherwise. Processes separated by slash are alternatives to each other. 

|**No.**|**Required Partial Application Process**|
|---|---|
|1|PAP ACQ-FPS-USV-1: Unsupervised Acquisition Slap|
|2|PAP ACQ-FI-AUTO-1: Automated Facial Image Acquisition|
|3|PAP ID-1: CIR Identification|
|4|PAP EVA-VER-nCIR-1: Verification Evaluation Workflow for BMS without Identification Capability|



**Table 2.10** Required Partial Application Processes Application Profile Self-Service System 

## 2.7 Application Profile Biometric Matching Systems 

This Application Profile specifies requirements for a Biometric Matching System (BMS). 

## 2.7.1 Mandatory Process 

The following subsections specify the overall process of the BMS as well as different evaluation workflows. 

## 2.7.1.1 Overview Process 

Figure 2.6 depicts the overall BMS process. 

Federal Office for Information Security 

9 

2 Application Profiles 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0018-01.png)


**----- Start of picture text -----**<br>
Evaluation of biometric accuracy<br>performance necessary<br>Perform<br>Verication<br>Perform<br>Identication<br>Evaluation of biometric accuracy<br>performance necessary<br>Calling System<br>Verication<br>BMS<br>Identication<br>**----- End of picture text -----**<br>


**Figure 2.6.** Overall BMS Process 

## 2.7.1.2 Evaluation Worflows 

The outcome of a biometric verification (match vs. non-match)[1] or identification (candidate list) is only relia ble if the corresponding error rates are quantified and monitored. In order to enable a competent authority to evaluate false and true match rates and to configure the BMS comparison thresholds, the Application Profile specifies evaluation workflows which SHALL be executed in parallel for requests received by the BMS or made available to the BMS, unless the main working processes would be impaired in times of high load. 

Note, the specifications of evaluation workflows do not distinguish between the type of biometric modality and are generic. Thus, they SHALL be applied to measure biometric performance of fingerprint, facial image and multimodal verification and identification depending on the used biometric modalities of the relevant system. 

The evaluation workflows enable a competent authority... 

- ... to continuously monitor biometric accuracy in terms of security and usability of the system. 

- ... to precisely reconfigure comparison thresholds in order to meet defined security or usability targets. 

- ... to assess the biometric performance of new comparison algorithms or updates of deployed comparison algorithms prior to deployment. 

- ... to determine thresholds for deploying new or updated algorithms in order to meet defined security and usability targets. 

- ... to evaluate and compare new quality algorithms or updates of deployed quality algorithms. 

- ... to determine quality thresholds for biometric modalities to be included or excluded in a BMS to meet the defined accuracy targets. 

- 1 The term "biometric match" is ambiguous and could literally mean both "biometric recognition/compa rison" or "biometric conformity/hit/equivalence". In the European Regulations and Implementing Acts, it appears being used for both meanings. For the sake of clarity, "match" will only correspond to a hit in the biometric recognition in the following, unless used within the fixed term "biometric matching system", where it is used in the sense of "recognition". 

Federal Office for Information Security 

10 

2 Application Profiles 

- ... to evaluate and compare comparison algorithms to attribute type specific performance differences, e.g. sex or age. 

The process specified by PAP EVA-ID-wCIR-1: Identification Evaluation Workflow for BMS with Identifi cation Capability and with Verification Capability SHALL be executed if an identification request is received. 

The process specified by PAP EVA-VER-wCIR-1: Verification Evaluation Workflow for BMS with Identifi cation Capability and with Verification Capability SHALL be executed if a verification request is received and the BMS does not offer an identification capability. 

The process specified by PAP EVA-VER-nCIR-1: Verification Evaluation Workflow for BMS without Iden tification Capability SHALL be executed if a verification request is received and the BMS does offer an iden tification capability. 

## 2.7.2 Mandatory Function Modules 

All Function Modules which SHALL be applied for this Application Profile are listed in Table 2.11. All listed Function Modules (separated by commas) are REQUIRED for this Application Profile unless specified other wise. Function Modules separated by slash are alternatives to each other. Function Modules in brackets are RECOMMENDED. 

|**Module Category**|**Required Function Modules**|
|---|---|
|Acquisition Hardware|-|
|Acquisition Software|-|
|Biometric Image Processing|-|
|Quality Assessment|FM QA-FI-GENERIC,<br>FM QA-FI-BCL,<br>FM QA-FP-APP|
|Presentation Attack Detection|-|
|Compression|FM COM-FI-GENERIC|
|Operation|-|
|User Interface|-|
|Reference Storage|-|
|Biometric Comparison|FM CMP-FI-VER,<br>FM CMP-FP-VER|
|Logging|Will be amended in a future version of this TR.|
|Coding|-|
|Evaluation|Will be amended in a future version of this TR.|



**Table 2.11** Required Function Modules for Application Profile Biometric Matching System Control 

## 2.7.3 Mandatory Partial Application Processes 

All Partial Application Processes and Tasks which SHALL be applied for this Application Profile are listed in Table 2.12. All listed Processes (separated by commas) are REQUIRED for this Application Profile unless specified otherwise. Processes separated by slash are alternatives to each other. 

**No. Required Partial Application Process** 

- 1 PAP EVA-ID-wCIR-1: Identification Evaluation Workflow for BMS with Identification Capability and with Verificati on Capability / PAP EVA-VER-wCIR-1: Verification Evaluation Workflow for BMS with Identification Capability and with Verification Capability / PAP EVA-VER-nCIR-1: Verification Evaluation Workflow for BMS without Identificati on Capability 

**Table 2.12** Required Partial Application Processes Application Profile Automated Border Control 

Federal Office for Information Security 

11 

3 Partial Application Processes 

## 3 Partial Application Processes 

The Partial Application Processes (PAPs) specified by the following sections provide process specifications of basic biometric processes, e.g. the acquisition, identification or verification of biometrics or the evaluation processes for verification and identification. The PAPs are referenced by the relevant Application Profiles and are part of the overall processes specified therein. 

A PAP MAY also be a task. A task is a process which functions as a generic reusable building block which is used by another PAP and is not referenced by an Application Profile directly. 

The specific Function Modules that SHALL be implemented in the processes of this chapter are specified by the relevant Application Profiles. 

## 3.1 PAP ACQ-FI-SV-5: Supervised Facial Image Acquisition System 

This Partial Application Process specifies a facial image acquisition system to automatically acquire or manu ally capture facial images for enrolment, verification or identification purposes. Note, that the PAP ACQ-FIAUTO-1: Automated Facial Image Acquisition is used here. 

## 3.1.1 Process 

The facial image acquisition system consists of two main processes, whereby the automated acquisition is REQUIRED in all application scenarios while the manual mode is 

- OPTIONAL for devices that are subject to TR volume German Identity Documents (GID) 

- REQUIRED for other devices, especially in the context of TR volume Border Control (BCL). 

- The overall process is depicted in Figure 3.1: 

1. The operator triggers the automatic acquisition of a facial image for enrolment or for verification/iden tification. The operator SHALL also have the option to manually trigger the acquisition. The operator re views the acquired facial image and the results of the software based Quality Assessment (QA). The opera tor SHALL have the option to manually crop and de-rotate the image. In case the manual review revealed bad quality of the facial image, the operator MAY discard the facial image in order to acquire a new facial image. The operator releases the image for further processing. 

2. The operator triggers the manual acquisition of a facial image for enrolment or for verification/identifi cation. The operator manually configures the camera system to the body height of the biometric subject (or triggers automatic height configuration). Next, the operator triggers the capture of a facial image of the biometric subject. The operator reviews the results of the software based QA. The operator SHALL have the option to manually crop and de-rotate the image. In case the manual review revealed bad quality of the facial image, the operator MAY discard the facial image in order to acquire a new facial image. The operator releases the image for further processing. 

To support the two processes, the system provides the following two service modes via its interface, refer to Section 3.1.1.1: 

1. _automated mode_ 

In this mode, the system obtains a request from the calling application to acquire an image by a certain quality level (enrolment, verification/identification quality). The system executes the required process au tonomously and returns the final image to the calling application. Thereby, the system handles the pro cess execution, e.g. configuration of the camera system to the height of the biometric subject, mandatory repetitions due to quality issues, QA, automatic capture of the facial image etc. The system SHALL imple ment the processes specified by the PAP ACQ-FI-AUTO-1: Automated Facial Image Acquisition for the automated mode. This service mode is REQUIRED in all application scenarios. 

2. _manual mode_ 

In this mode, the system acts as a capture device for the calling application. The calling application sends atomic requests to the system, e.g. to adjust the system to the height of the biometric subject, to switch on the lighting or to capture a facial image. This service mode is OPTIONAL in the application context German Identity Documents (GID). 

Federal Office for Information Security 

12 

3 Partial Application Processes 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0021-01.png)


**----- Start of picture text -----**<br>
Retry Capture?<br>Yes No<br>Process End<br>Automated Operation Mode without Image<br>PAP Automated Facial Image Acqusition<br>Automated  No Yes (Best) Image Show No Yes Release Facial<br>Facial Image  with QA-Results  Image<br>Acquisition Image(s) Captured? to Operator Operator Accepts  Default End<br>Automated Trigger Manual Capture by  Manual Cropping &  Image?<br>Operator De-Rotation<br>Correction by<br>Start Acquisitionon Manual/ Automated Decision  previously selectedOperation Mode(Re-)Start  Switch to Manual Operation ModeManual Operation Mode Operation ModeAutomated Switch to  QA-FI-GENERIC,QA-FI-<VL> Assess Quality ofFacial Image Operator<br>Manual Trigger<br>Manual<br>Note that within the application context German Identity Documents (GID), the  Show Capture by Operator Task: Capture<br>support of a manual mode is optional. Live Feed Live Facial  Cropping &<br>to Operator Image De-Rotation of<br>Facial Image<br>Trigger Manual<br>Adjustment of<br>Camera System to Illumination or Body Height,  PAP Task Capture Live Facial Image BIP-FI-<VL><br>Focus Point<br>**----- End of picture text -----**<br>


**Figure 3.1.** Supervised Facial Image Acquisition System: Overall Process 

## 3.1.1.1 Interface Requirements 

If High Level Biometric Services (HLBS) is used by the system, the "Service Definition Facial Image Acquisition System" of Part 2, Volume 2 of this Technical Guideline SHALL be implemented. 

## 3.1.2 PAP Task ACQ-FI-1: Capture Live Facial Image 

Figure 3.2 depicts the basic process of a live facial image capture. If the image acquisition is not supervised PAD SHALL be performed[1] . In case of supervised image acquisition PAD is OPTIONAL. 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0021-07.png)


**----- Start of picture text -----**<br>
FM PAD-FI-*<br>Perform PAD<br>OPTIONAL in<br>supervised case<br>No Yes<br>Is acquisition  Yes No<br>supervised?<br>PAD functionality<br>available and<br>congured to be<br>used?<br>Retrieve image<br>from hardware<br>Start End<br>**----- End of picture text -----**<br>


**Figure 3.2.** Partial Application Process Task "Capture Live Facial Image" 

## 3.2 PAP ACQ-FI-SV-4: Supervised Facial Image Acquisition 

## 3.2.1 Process 

The facial image acquisition process, refer to Figure 3.3, described by this section requires a supervised si tuation. Note, that the PAP Task ACQ-FI-1: Capture Live Facial Image is used here. The biometric subject's facial image is captured using live enrolment equipment (including a digital camera within a photo studio setup) operated by an operator[2] . 

- 1 Note that the requirement for PAD in supervised settings might be subject to transitional arrangements. The final obligation is regulated through the selection of mandatory Function Modules within the respec tive Application Profiles. 

- 2 See ISO/IEC 19794-5, Annex B for "Best practices for Face Images" 

Federal Office for Information Security 

13 

3 Partial Application Processes 

In case the acquisition system detects a face, the facial image capture SHALL be performed automatically. An alternative automatic mode is the automatic facial image capture after a fixed time interval. However, the operator SHALL also have the option to perform the capture manually. For that the automatic capture, which is performed when a face is detected or after a fixed time interval, is disabled. An immediately performed cropping and de-rotation of the face and software quality assessment for the captured facial image ensures its biometric usability. If the quality assessment succeeds positively, the image SHALL be shown to the operator. If the quality is assessed as insufficient and the timeout has not exceeded yet, the system SHALL recapture. If the operator has captured manually, the image SHALL be shown to the operator in any case. In case the timeout has exceeded, the system SHALL identify the best captured facial image and show this image to the operator. The operator SHALL have the option to correct the cropping and de-rotation on the shown image manually. The operator SHALL also have the option to accept the captured facial image. The image is then release to the calling application. This is also the case, if the quality has been assessed as insufficient by the system. In the negative case, the facial image SHALL be discarded, the timeout is reset and a recapture is performed. 

If the timeout exceeds and no facial image has been captured (neither with sufficient nor with insufficient quality), the process terminates without releasing an image. It is the operator's decision to restart the acquisi tion process or to perform other actions. 

The process SHALL be supervised by an operator. 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0022-04.png)


**----- Start of picture text -----**<br>
No FM QA-FI-GENERIC Process End<br>with insufcient Facial Image(s)  Yes Best Image of Identify without Image<br>quality captured  captured Facial<br>before timeout? Images<br>QA-FI-GENERIC, Manual Cropping &<br>Timeout exceeded PAP Task Capture Live Facial Image BIP-FI-<VL> QA-FI-<VL> Sufcient Quality or Operator  Correction by De-Rotation<br>Captured  Operator Operator accepts<br>Manually? Image?<br>Start to OperatorLive FeedShow  Manual Capture by Face found or Operator Task: CaptureLive Facial Image Rotate to FaceCrop & De- Facial ImageQuality of CapturedAssess No Yes with QA-Results (Best) Image to OperatorShow  No Yes Release Facial Image Default End<br>Reset Timeout<br>**----- End of picture text -----**<br>


**Figure 3.3.** Partial Application Process "Supervised Facial Image Acquisition" 

## 3.2.1.1 Interface Requirements 

If HLBS is used by the system, the "Service Definition Basic Facial Image Acquisition System" of Part 2, Volume 2 of this Technical Guideline SHALL be implemented. 

## 3.2.2 PAP Task ACQ-FI-1: Capture Live Facial Image 

Figure 3.4 depicts the basic process of a live facial image capture. If the image acquisition is not supervised PAD SHALL be performed[3] . In case of supervised image acquisition PAD is OPTIONAL. 

> 3 Note that the requirement for PAD in supervised settings might be subject to transitional arrangements. The final obligation is regulated through the selection of mandatory Function Modules within the respec tive Application Profiles. 

Federal Office for Information Security 

14 

3 Partial Application Processes 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0023-01.png)


**----- Start of picture text -----**<br>
FM PAD-FI-*<br>Perform PAD<br>OPTIONAL in<br>supervised case<br>No Yes<br>Is acquisition  Yes No<br>supervised?<br>PAD functionality<br>available and<br>congured to be<br>used?<br>Retrieve image<br>from hardware<br>Start End<br>**----- End of picture text -----**<br>


**Figure 3.4.** Partial Application Process Task "Capture Live Facial Image" 

## 3.3 PAP ACQ-FI-USV-1: Unsupervised Facial Image Acquisition with Prequalification 

The facial image acquisition process described by this section applies to unsupervised acquisition situations. The full process of image acquisition and the prequalification of the live facial image is presented in Figu re 3.5. Note, that the PAP Task ACQ-FI-1: Capture Live Facial Image is used here. 

The following steps SHALL be performed. Live image data is captured with respect to FM Category Acqui sition Hardware, FM Category Acquisition Software, FM Category Biometric Image Processing and FM Category Quality Assessment. Prequalification (as defined by FM QA-FI-PRE) ensures that only images of sufficient quality are taken. Live image data MAY be compressed according to FM Category Compression. 

If the image quality is not sufficient and the specified timeout is not reached and no PAD alarm is triggered, the following SHALL be done: The captured image SHALL be added to a sorted list (sorted by image quality) and a new image SHALL be captured. 

This process will finish in one of the following conditions: 

- If the image quality is sufficient and the specified timeout is not reached and no PAD alarm is triggered, the acquired image SHALL be returned. 

- If the timeout is reached and the sorted image list is not empty, the best quality image from the image list SHALL be returned. Otherwise if the list is empty no image SHALL be returned. 

- If a PAD alarm is triggered, the PAD alarm message and the acquired image SHALL be returned to the calling application and displayed to the operator. 

The timeout SHALL be configurable. 

All gathered information is logged and coded according to FM Category Coding and FM Category Logging. 

During the complete transaction of acquisition an operator SHOULD ensure that the biometric subject does not try to illegally bypass the system by using presentation attack instruments or other mechanisms. By me ans of FM Category Presentation Attack Detection the operator SHALL receive a warning when the PAD subsystem detects a spoofing attack. 

Federal Office for Information Security 

15 

3 Partial Application Processes 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0024-01.png)


**----- Start of picture text -----**<br>
Add image to sorted<br>list (sorted by image<br>quality)<br>FM UI-FI-BSJ<br>Guide<br>biometric subject to distance rangeenter optimal  PAP Task Capture Live Facial Image FM QA-FI-PRE BIP-FI-<VL><br>Timeout? No PAD alarm triggered? No<br>Start Yes No subject to present Guide biometric its face congure camera system biometric subjectto body height of Automatically distance of biometricsubject to camera Estimatesystem Biometric subject inYes from live streamCapture image  Yes No Pre-Qualicationof Image Image quality Yes De-Rotatation of Facial ImageCropping &  End<br>optimal distance  sufcient?<br>FM AS-FI-ICS3 range?<br>Sorted image list  No Get Image of<br>empty? best quality<br>Yes<br>**----- End of picture text -----**<br>


**Figure 3.5.** Partial Application Process "Unsupervised Facial Image Acquisition with Prequalification" 

## 3.3.1 Interface Requirements 

If HLBS is used by the system, the "Service Definition Facial Image Acquisition System" of Part 2, Volume 2 of this Technical Guideline SHALL be implemented. 

## 3.3.2 PAP Task ACQ-FI-1: Capture Live Facial Image 

Figure 3.6 depicts the basic process of a live facial image capture. If the image acquisition is not supervised PAD SHALL be performed[4] . In case of supervised image acquisition PAD is OPTIONAL. 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0024-07.png)


**----- Start of picture text -----**<br>
FM PAD-FI-*<br>Perform PAD<br>OPTIONAL in<br>supervised case<br>No Yes<br>Is acquisition  Yes No<br>supervised?<br>PAD functionality<br>available and<br>congured to be<br>used?<br>Retrieve image<br>from hardware<br>Start End<br>**----- End of picture text -----**<br>


**Figure 3.6.** Partial Application Process Task "Capture Live Facial Image" 

## 3.4 PAP VER-FI-ALL-1: Facial Image Verification 

Figure 3.7 depicts the basic process of a facial image varification in an unsupervised scenario. The verification SHALL be performed according to FM Category Biometric Comparison. 

The facial image of the biometric subject is verified against the reference facial image on the eMRTD chip. If the biometric subject is a Third-Country National (TCN), verification against applicable CIRs is carried out additionally. 

Also, the evaluation workflow is carried out in order to determine the biometric performance of the deployed comparison algorithm. 

> 4 Note that the requirement for PAD in supervised settings might be subject to transitional arrangements. The final obligation is regulated through the selection of mandatory Function Modules within the respec tive Application Profiles. 

Federal Office for Information Security 

16 

3 Partial Application Processes 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0025-01.png)


**----- Start of picture text -----**<br>
No<br>Verify<br>CIR Verication  Yes Live Facial<br>necessary? Image against<br>CIR(s)<br>FM COD-FI-<br>VER<br>Verify<br>Live Facial<br>Image against<br>eMRTD<br>Start Default End<br>FM COD-FI-<br>VER<br>Evaluation<br>Workow<br>PAP Verication<br>Evaluation<br>Workow for<br>BMS Without<br>Identication<br>Capability<br>**----- End of picture text -----**<br>


**Figure 3.7.** Partial Application Process "Facial Image Verification" 

## 3.5 PAP ACQ-FI-AUTO-1: Automated Facial Image Acquisition 

The facial image acquisition process described by this section applies to acquisition processes where the facial image is acquired automatically, refer to Figure 3.8. Note, that the PAP Task ACQ-FI-1: Capture Live Facial Image is used here. 

An acquisition system SHALL be used that works with an integrated quality assessment Function Module (see FM Category Quality Assessment). The requirements of FM Category Acquisition Hardware, FM Category Acquisition Software and FM Category Biometric Image Processing SHALL apply. The process SHALL use the following steps: 

1. The biometric subject SHALL be guided to present its face. 

2. The camera system SHALL be automatically configured for the body height of the person. 

3. Multiple faces in the acquisition image area SHALL be detected. Note, the detection SHALL be carried out all the time while the acquisition is ongoing until the facial image is captured. 

4. If multiple faces are detected, a guidance SHALL advice the biometric subject to appear alone in front of the acquisition system. 

5. The distance of the biometric subject to the camera system SHALL be determined. 

6. If the biometric subject is not in the optimal capture range, a guidance SHALL advice the biometric subject to enter the optimal distance range. 

7. If a facial image can not be captured within a configured timeout, e.g. the biometric subject does not look in the camera or disappears from the system, the acquisition processes ends. The timeout SHALL be configurable. 

Federal Office for Information Security 

17 

3 Partial Application Processes 

8. The facial image of the biometric subject SHALL be captured. The image SHALL then be cropped and derotated to the face. 

9. The quality of the facial image SHALL be assessed according to the specific Function Module in FM Category Quality Assessment. 

10. If the quality is not sufficient and the timeout is not exceeded, a new facial image is captured. The timer for the timeout SHALL start with the retrieval of the first facial image from the capture system. 

11. If the quality is sufficient, the facial image is released for the calling application. 

12. If the timeout is exceeded and no image is of sufficient quality, the best facial image is selected among the captured images according to the specific Function Module in FM Category Quality Assessment and the image SHALL be released for the calling application. 

13. With optimal conditions (bona fide) the overall facial image acquisition process SHALL NOT exceed the following time limits: 

   - a. For devices that are subject to TR volume Border Control (BCL), the overall facial image acquisition process SHALL NOT exceed ten seconds. In case the system is not required to perform a PAD (e.g. supervised scenario) the overall facial image acquisition process SHALL NOT exceed seven seconds. 

   - b. For devices that are subject to TR volume German Identity Documents (GID), the overall facial image acquisition process SHALL NOT exceed thirty seconds (including PAD and, if applicable, excluding background replacement). 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0026-09.png)


**----- Start of picture text -----**<br>
Timeout exceeded?<br>No Yes<br>FM UI-FI-BSJ<br>This timeout SHALL start with the retrieval of the rst facial image<br>Guide from the hardware. The timeout SHALL be congurable.<br>In contrast to the other  Biometric Subject to<br>a separate timeout runs  Enter Optimal<br>FM UI-FI-BSJ here. The timeout SHALL be congurable. FM AS-FI-ICS3 Distance Range PAP Task Capture Live Facial Image BIP-FI-<VL> FM QA-FI-GENERIC,FM QA-FI-<VL> FM QA-FI-GENERIC,FM QA-FI-<VL><br>No No<br>Start Present its FaceSubject to Biometric Guide System to Body Height of Biometric SubjectCongure Camera Automatically to Camera SystemBiometric Subject Distance of Estimate Adjust Illumination & Focus PointAutomatically Biometric Subject Yes Task: Capture Live Facial Image De-Rotatation of Facial ImageCropping &  Assess Quality Sufcient Quality?Yes Captured Facial Best Facial Image of IdentiyImages Default End<br>in Optimal<br>Distance Range?<br>FM AS-FI-ICS3 FM UI-FI-BSJ<br>Multiple Faces<br>detected? Guide<br>Detect Yes Biometric<br>Multiple Faces in  Subject to Appear<br>Acquisition Area Alone in Front of the<br>No Camera Restart Acquistion Process<br>No Yes<br>Facial Image  End<br>acquired?<br>Main Process<br>Multiple Faces Detector<br>**----- End of picture text -----**<br>


**Figure 3.8.** Partial Application Process "Automated Facial Image Acquisition" 

## 3.5.1 Interface Requirements 

If HLBS is used by the system, the "Service Definition Facial Image Acquisition System" of Part 2, Volume 2 of this Technical Guideline SHALL be implemented. 

## 3.5.2 PAP Task ACQ-FI-1: Capture Live Facial Image 

Figure 3.9 depicts the basic process of a live facial image capture. If the image acquisition is not supervised PAD SHALL be performed[5] . In case of supervised image acquisition PAD is OPTIONAL. 

- 5 Note that the requirement for PAD in supervised settings might be subject to transitional arrangements. The final obligation is regulated through the selection of mandatory Function Modules within the respec tive Application Profiles. 

Federal Office for Information Security 

18 

3 Partial Application Processes 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0027-01.png)


**----- Start of picture text -----**<br>
FM PAD-FI-*<br>Perform PAD<br>OPTIONAL in<br>supervised case<br>No Yes<br>Is acquisition  Yes No<br>supervised?<br>PAD functionality<br>available and<br>congured to be<br>used?<br>Retrieve image<br>from hardware<br>Start End<br>**----- End of picture text -----**<br>


**Figure 3.9.** Partial Application Process Task "Capture Live Facial Image" 

## 3.6 PAP ACQ-FPS-SV-1: Supervised Acquisition Single Slap 

## 3.6.1 Process 

Figure 3.10 depicts the supervised acquisition process of a slap. 

At first the operator flags the missing fingers of the hand of the biometric subject. (Alternative: The operator flags the missing fingers of both hands of the biometric subject.) 

The biometric subject SHALL be guided to place the hand correctly on the scanner and the slap SHALL be captured. Note, that the Section 3.6.2 is used here. 

If already slaps of both hands were acquired, the process SHALL end here. Otherwise the operator SHALL decide if he likes to capture the slap of the other hand, too. 

The process SHALL be supervised by an operator. 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0027-10.png)


**----- Start of picture text -----**<br>
Two slaps acquired? Yes<br>The Guide<br>operator ags  biometric Capture Slap  No<br>missing ngers  subject to place hand  Supervised No<br>of hand on scanner<br>Start End<br>Yes Operator decides:<br>Capture Slap of<br>Note: The selection of missing ngers MAY other hand?<br>also be performed for both hands here. So this task  PAP Task<br>SHALL be omitted in case of acquiring the second slap, if  Capture Slap<br>the operator already agged the missing ngers of both  Supervised<br>hands during the rst run. It is NOT REQUIRED to<br>support both variants.<br>**----- End of picture text -----**<br>


**Figure 3.10.** Partial Application Process "Supervised Acquisition Slap" 

## 3.6.1.1 Interface Requirements 

If HLBS is used by the system, the "Service Definition Fingerprint Acquisition" of Part 2, Volume 2 of this Technical Guideline SHALL be implemented. 

## 3.6.2 PAP Task ACQ-FPS-SV-1: Capture Slap Supervised 

Figure 3.11 depicts the basic process for a plain supervised slap capture. A plain slap capture can be part of more complex acquisition processes, e.g. a ten finger acquisition by the 4-1-4-1 capture sequence. The plain slap capture is subsequently described in detail. The quality assessment is conducted according to the requi rements of the applicable FM Category Quality Assessment. Note, that the PAP Task ACQ-FPP-SV-2: Cap ture Plain Fingerprint Supervised is used here. 

Federal Office for Information Security 

19 

3 Partial Application Processes 

If the biometric subject is physically not capable to place all fingers of the slap on the capture hardware at the same time to achieve a slap image of good quality, the operator can decide to capture each finger of the slap in single finger capture mode. This SHALL be possible during the entire process. Hereby, single finger capture mode refers to the PAP Task ACQ-FPP-SV-2: Capture Plain Fingerprint Supervised as described below. 

1. The counter variable for the number of attempts for capturing the current slap SHALL be initialized as _i_ = 1. 

2. The slap image SHALL be retrieved from hardware. While the image is retrieved from hardware, PAD SHALL be performed. Note: The operator SHALL have the option to manually conduct the capture of sla p(s). 

3. The fingerprints SHALL be segmented and each fingerprint SHALL be quality assessed. 

   - a. In case the quality of the fingerprints meets the quality requirements defined in the corresponding QA Function Module, the captured slap and the set of segmented fingerprints and parameter data (e.g. quality values) SHALL be temporarily stored. 

   - b. In case the quality requirements for one or more fingerprints of the slap are not met, the capture SHALL be repeated up to two times (i.e. the acquisition of a single slap consists of a maximum of three capture attempts). The counter SHALL be set to _i_ = _i_ + 1. 

4. A uniqueness check SHALL be conducted for the captured slap image to detect the capture of wrong fin gers, e.g. due to interchanged hands or multiple acquisition of the same hand or finger. Note, that it is RE COMMENDED to conduct the uniqueness check as early as possible after a fingerprint image is available. 

   - a. In case 

      - the comparison of any fingerprint of the current slap with any previously accepted fingerprint of a previous slap or 

      - the comparison of any fingerprint of the current slap with another fingerprint of the current slap 

      - is successful, the uniqueness check SHALL raise a warning. 

   - b. In case the comparisons of all fingerprints of the current slap with all fingerprints of previous slaps are not successful, the uniqueness check SHALL NOT show a warning. 

5. Generally, a slap classifier SHALL be used for the captured slap image to detect the capture of the wrong slap. It SHALL be configurable to switch the classifier off or in evaluation mode (logging of the result wi thout showing the result/warning to the operator). Note, that the slap classifier is only required for 4 finger slaps. Other acquisitions currently do not require the corresponding FM. 

   - a. If the result of the classification concludes that the acquired slap mismatches the expected slap, a warning SHALL be reported. 

   - b. If the result of the classification concludes that the acquired slap matches the expected slap, no warning SHALL be reported. 

If the quality check of the third capture attempt fails (counter _i_ is set to 3), the best of the captured slaps SHALL be identified according to the corresponding QA Function Module and temporarily stored along with the corresponding information. 

The process SHALL be supervised by an operator. 

At the end of the process the operator decides on one of the three options: 

1. Use the acquired slap. 

2. Recapture the current slap. The counter SHALL be reset to _i_ = 1. 

3. Restart the total slap acquisition workflow. 

The operator SHALL have the following veto options: 

- Select none of the captured slaps despite sufficient quality. 

- Select a slap of insufficient quality from the acquisition process. 

At any point of the process the operator MAY decide to acquire any finger of the slap individually. 

Federal Office for Information Security 

20 

3 Partial Application Processes 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0029-01.png)


**----- Start of picture text -----**<br>
Discard<br>all Previously  Set i = 1<br>The operator SHALL have the option to  Acquired Images Case B: The operator  Case A: The<br>manually conduct the capture of slap(s) decides to recapture the  operator decides<br>FM QA-FP-APP Here, no sufcient  Show acquired FP images and results of PAD, uniqueness check and slap classication current slap.FM UI-FP-OP Case B to use the acquired slap<br>from hardwareRetrieve slap  Slap quality sufcient? quality implies i=3 4 Finger Slap captured?<br>Initialize variable Assess Quality of Yes Uniqueness  No Show all acquired  Case A Default End<br>Start i = 1 Slap Check information to<br>No FM QA-FP-APP FM AS-FP-SLP the operator<br>Perform PAD Yes<br>Set i = i + 1 No i = 3? Yes of Captured SlapsBest SlapIdentiy Classify Slap Case C: The operator decides to restart the total slap acquisition workow. Case CRestart total slap acquisition workow<br>This is only relevant for<br>application proles where 4<br>nger slaps are expected.<br>Acquire each<br>nger(s) of slap in<br>In case difculties occur in the process  single nger<br>(e.g. biometric subject is not capable to  acquisition mode<br>place ngers of slap on scanner) switch<br>to single nger acquisition mode.<br>PAP Task Capture Plain<br>Finger Supervised<br>**----- End of picture text -----**<br>


**Figure 3.11.** Partial Application Process Task "Capture Slap Supervised" 

## 3.6.2.1 PAP Task ACQ-FPP-SV-2: Capture Plain Fingerprint Supervised 

Figure 3.12 depicts the basic supervised capture process for a plain fingerprint capture. A plain fingerprint capture can be part of more complex acquisition processes, e.g. a ten finger acquisition by the 4-1-4-1 capture process. The plain fingerprint capture is described in detail subsequently. The quality assessment is conducted according to the requirements of the applicable FM Category Quality Assessment. 

1. The counter variable for the number of attempts for capturing the current fingerprints SHALL be initia lized as _i_ = 1. 

2. The fingerprint image SHALL be retrieved from hardware. While the image is retrieved from hardware, PAD SHALL be performed. Note: The operator SHALL have the option to manually conduct the capture of fingerprint(s). 

3. The fingerprint SHALL be quality assessed and the captured fingerprint and parameter data (e.g. quality values) SHALL be temporarily stored. 

4. In case the quality requirements for the fingerprint are not met, the capture SHALL be repeated up to two times (i.e. the acquisition of a finger consists of a maximum of three capture attempts). The counter SHALL be set to _i_ = _i_ + 1. 

5. A uniqueness check SHALL be conducted for the captured fingerprint image to detect the capture of wrong fingers, e.g. due to interchanged hands or multiple acquisition of the same hand or finger. Note: It is RE COMMENDED to conduct the uniqueness check as early as possible after a fingerprint image is available. 

   - a. In case the comparison of the current fingerprint with any previously captured fingerprint is success ful, the uniqueness check SHALL report a warning. 

   - b. In case the comparison of the current fingerprint with any previously captured fingerprint is not suc cessful, the uniqueness check SHALL NOT report a warning. 

6. The acquired finger prints and the results of PAD, QA and uniqueness check SHALL be displayed to the operator. 

If the quality check of the third capture attempt fails (counter _i_ is set to 3), the best of the captured fingerprint images SHALL be identified according to the corresponding QA Function Module and temporarily stored along with the corresponding information. 

The process SHALL be supervised by an operator. 

At the end of the process the operator decides on one of the three options: 

1. Use the acquired fingerprint. 

2. Recapture the current fingerprint. The counter SHALL be reset to _i_ = 1. 

3. Restart the Figure 3.12 acquisition workflow. 

The operator SHALL have the following veto options: 

- Select none of the captured fingerprints despite sufficient quality. 

Federal Office for Information Security 

21 

3 Partial Application Processes 

- Select a fingerprint of insufficient quality from the acquisition process. 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0030-02.png)


**----- Start of picture text -----**<br>
Discard<br>all previously  Set i = 1<br>acquired images Case A: The<br>Case B: The operator  operator decides to<br>The operator SHALL  decides to recapture the  use the acquired<br>have the option to  current nger. ngerprint image.<br>manually conduct the capture of ngerprint(s) Note: The captured ngerprint SHALL be compared with each already accepted ngerprint of the current<br>Retrieve  FM QA-FP-APP acquistion process. However, it is RECOMMENDED to conduct the uniqueness check as early as possible after a new ngerprint is available. FM UI-FP-OP Case B<br>ngerprint from hardware Fingerprint quality sufcient? Show acquired<br>Initialize variablei = 1 Assess quality of ngerprint Yes Uniqueness check results of PAD, FP images and QA and uniq.  Case A<br>Start No FM QA-FP-APP check Default End<br>Perform PAD<br>Case C<br>Set i = i +1 No Yes Identiy best ngerprint Case C: The operator decides to  Restart total<br>i = 3? restart the total ngerprint acquisition workow. acquisition ngerprint workow<br>**----- End of picture text -----**<br>


**Figure 3.12.** Partial Application Process Task "Capture Plain Fingerprint Supervised" 

## 3.7 PAP ACQ-FPS-USV-1: Unsupervised Acquisition Slap 

Figure 3.13 depicts the unsupervised acquisition process for slaps: 

1. It SHALL be checked if all fingers of the desired slap are available, if not the process SHALL end. 

2. The biometric subject SHALL be guided to place the hand on the scanner. 

3. The slap SHALL be captured. Note, that the PAP Task ACQ-FPS-USV-1: Capture Slap Unsupervised is used here. In parallel the surveillance images SHALL be captured, too. 

4. If not four fingers were acquired: Acquired finger images and associated surveillance images SHALL be discarded. 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0030-10.png)


**----- Start of picture text -----**<br>
FM AH-ALL-SSS,<br>FM COM-CCTV-JPG<br>FM UI-FP-BSJ<br>Capture of<br>All Fingers of Slap  Surveillance  Four Fingerprints<br>available? Images acquired?<br>Guide<br>Yes Biometric Yes<br>Subject to place<br>Hand on Scanner Discard<br>Start No No acquired End<br>Capture Slap<br>Fingerprints and<br>Unsupervised associated<br>Surveillance Images<br>FM AS-FP-MF PAP Task<br>Capture Slap<br>Unsupvervised<br>**----- End of picture text -----**<br>


**Figure 3.13.** Partial Application Process "Unsupervised Acquisition Slap" 

## 3.7.1 Interface Requirements 

If HLBS is used by the system, the "Service Definition Fingerprint Acquisition System" of Part 2, Volume 2 of this Technical Guideline SHALL be implemented. 

## 3.7.2 PAP Task ACQ-FPS-USV-1: Capture Slap Unsupervised 

Figure 3.14 depicts the basic process for a plain unsupervised slap capture. A plain slap capture can be part of more complex acquisition processes, e.g. a ten finger acquisition by the 4-1-4-1 capture sequence. The plain unsupervised slap capture is subsequently described in detail. The quality assessment is conducted according to the requirements of the applicable FM Category Quality Assessment. 

In a uniqueness check, each segmented fingerprint of the current slap SHALL be compared with each already accepted fingerprint of the current acquisition process. Note, this is only required in case more than one slap is captured within the acquisition process. 

Federal Office for Information Security 

22 

3 Partial Application Processes 

1. The slap image SHALL be retrieved from hardware. The timer for timeout SHALL be configurable and SHALL start right away with beginning of the whole process. Note, that this timeout can also occur before performing PAD respectively before retrieving slap from hardware. 

   - a. If the Pre-Qualification is insufficient and timeout has exceeded, the acquisition process, described in this chapter, SHALL continue as follows: 

      - i. In case no slap has been captured, it SHALL end without an acquired slap. 

      - ii. In case at least one slap has been captured, the best one SHALL be identified and the acquisition process SHALL end afterwards. 

   - b. If the Pre-Qualification is insufficient and timeout has not exceeded, the retrieval of an image SHALL be retried. 

2. If the hardware returns a PAD alarm, the acquisition process SHALL end. Note, that the relevant informa tion described in Section 4.5 SHALL be stored before ending the acquisition process. 

3. QA SHALL be conducted. In case the quality of the fingerprints meet the quality requirements defined in the corresponding Section 4.4, the captured slap and the set of segmented fingerprints and parameter data (e.g. quality values) SHALL be temporarily stored. 

   - a. In case the quality requirements for one or more fingerprints of the slap are not met, the capture SHALL be repeated if the timeout is not reached. 

   - b. In case the timeout is reached and no slap image of sufficient quality was captured, the best slap image according to the corresponding QA Function Module SHALL be stored with the set of segmented fin gerprints and parameter data (e.g. quality values). 

4. The uniqueness check SHALL be conducted. If the uniqueness check fails, all captured images SHALL be discarded and the capture process SHALL be repeated from the beginning, but if the uniqueness check fails for the second time for the same slap, the acquisition process, described in this chapter, SHALL end without an acquired slap and a warning message SHALL be returned to the calling application, which SHALL be shown to the operator. 

5. With optimal conditions (bona fide) the overall slap capture process SHALL NOT exceed ten seconds. 

6. Generally, a slap classifier SHALL be used for the captured slap image to detect the capture of the wrong slap. It SHALL be configurable to switch the classifier off or in evaluation mode (logging of the result wi thout showing the result/warning to the operator). Note, that the slap classifier is only required for 4 finger slaps. Other acquisitions currently do not require the corresponding FM. 

   - a. If the result of the classification concludes that the acquired slap mismatches the expected slap, a warning SHALL be shown to the biometric subject, all captured images SHALL be discarded and the capture process SHALL be repeated from the beginning. The number of allowed retries SHALL be con figurable. 

   - b. If the result of the classification concludes that the acquired slap mismatches the expected slap and the image is transferred to the calling process, a warning SHALL be reported and shown to the operator. The operator decides whether the slap will be recaptured or the process continuous with the current slap. 

   - c. If the result of the classification concludes that the acquired slap matches the expected slap, no warning SHALL be reported. 

Federal Office for Information Security 

23 

3 Partial Application Processes 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0032-01.png)


**----- Start of picture text -----**<br>
about Detected Slap Warning Message ClassicationDisplay all Captured DiscardImages<br>Warning Message Sequence Errorabout Detected Display all Captured DiscardImages No Sequence Error Occurred<br>beforehand and the<br>Fingerprint Matches<br>FM PAD-FP-* The Uniqueness Check SHALL be  One Fingerprint beforehandAcquired<br>Executed if at least One Different  Classify Slap<br>Perform PAD Fingerprint has been Acquired beforehand FM QA-FP-APP<br>No Yes Yes<br>Start Timer for Timeout Pre-Qualication Insufcient Uniqueness Check Else Assess Quality ofSlap Yes No No<br>Start Timeout Exceeded?Yes No Guidance for PuttingCorrect Slap on ScannerDisplay from HardwareRetrieve Slap  Second Sequence Error Occured Sufcient Quality?Is Slap of  4 Finger Slap? Detected and Retry(The Number of Allowed Retries Congurable.)Incorrect Slap SHALL be Allowed? Default End<br>FM UI-FP-BSJ FM AH-FP-*,FM AS-FP-* Any Slaps  FM QA-FP-APP<br>Captured?<br>Yes Identiy<br>Best Slap of<br>Captured Slaps<br>No<br>**----- End of picture text -----**<br>


**Figure 3.14.** Partial Application Process Task "Capture Slap Unsupervised" 

## 3.8 PAP ID-1: CIR Identification 

Figure 3.15 depicts the process of a CIR identification. 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0032-05.png)


**----- Start of picture text -----**<br>
FM COD-FP-<Application Specic><br>Execute<br>ngerprint<br>identication in<br>CIR<br>FM COD-FP-<Application Specic><br>No No<br>Execute multi-<br>Yes Yes modal<br>identication in<br>CIR<br>Start Default End<br>At least one  Facial image<br>ngerprint  available?<br>available?<br>FM COD-FI-<Application Specic><br>**----- End of picture text -----**<br>


**Figure 3.15.** Partial Application Process "CIR Identification" 

## 3.9 PAP ASS-B-USV-1: Assess Unsupervised Acquired Biometrics 

Figure 3.16 depicts the process of assessment of unsupervised acquired biometrics by an operator. 

Federal Office for Information Security 

24 

3 Partial Application Processes 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0033-01.png)


**----- Start of picture text -----**<br>
Withdraw both<br>(FP+FI) OR<br>Also if available, classication results,  withdraw FI and FI<br>multiperson detection results, etc. SHALL  was acquired at an<br>be displayed. unsupervised  Discard all data<br>system<br>Display Operator<br>Display  all biometric  decision about  no withdrawal<br>surveillance data data including  withdrawal of<br>PAD result biometrics Withdraw FP<br>Start Default End<br>Discard FP data<br>Withdraw FI and FI<br>was acquired at a<br>supervised system<br>Discard FI data<br>**----- End of picture text -----**<br>


**Figure 3.16.** Partial Application Process "Assess Unsupervised Acquired Biometrics" 

## 3.10 PAP EVA-ID-wCIR-1: Identification Evaluation Workflow for BMS with Identification Capability and with Verification Capability 

This Partial Application Process specifies how the evaluation of biometric identification SHALL be carried out for biometric matching systems with identification and verification capability. 

Our notation and exposition in this section closely follows the ISO-standard. 

## 3.10.1 Identification Results and Identification Errors 

The goal of _(algorithmic) identification_ is to identify a subject by means of a given _(biometric) sample_ (for in stance, a facial image) inside a register that contains _(biometric) reference templates_ of a set of individuals. In a typical algorithmic setting, the outcome of an identification process is based on the computation of numerical scores that are meant to quantify the resemblance between the given sample and the reference (templates) from the register. The algorithm then outputs a _candidate list_ that contains all those subjects from the register for which the corresponding numerical score exceeds a pre-defined threshold. In particular, the algorithm can return an empty list (no matching subject was found in the register), or a list which only contains a single subject. 

An identification is also known as a (1: _n_ comparison), since a single probe sample is compared to a set of _n_ references, as opposed to the _verification setting_ where we compare a single probe sample with a single reference sample. Accordingly, verification is also referred to as 1:1 comparison. 

We now discuss the expected outcome of an identification process. First of all, if a subject _P_ is enrolled in the register, then we expect that the identification system returns a candidate list _CL_ which contains the subject _P_ . We denote this expected _true-positive identification result_ by _P 2 CL_ . If, on the other hand, the identification system returns a candidate list that lacks the subject _P_ , although _P_ is enrolled in the register, then this is considered to be an erroneous result, namely a _false-negative identification (FNI)_ result. 

Analogously, let us consider the case where the subject _P_ is not enrolled in the register. Obviously, in this case _P_ cannot be on the returned candidate list. In this case we would expect that the algorithm returns an empty candidate list, denote by _CL_ = _;_ . This is a _true-negative identification_ result. If, on the other hand, the identification system returns a non-empty candidate list, then it wrongly claims that _P_ is contained in the register. This erroneous event is referred to as a _false-positive identification (FPI)_ result. 

In order to analyse the quality of the identification system it is important to approximate the probabilities for these two types of erroneous results. Indeed, without any kind of knowledge about the range of these two probabilities, the results of the identification system are more or less meaningless. To this end, we introduce 

Federal Office for Information Security 

25 

3 Partial Application Processes 

appropriate empirical rates to control the quality of the identification results. But before we do this, let us summarise our setting in the following table: 

||**P enrolled**|**P not enrolled**|
|---|---|---|
|Expected Result|_P 2 CL_|_CL_=_;_|
|Erroneous Result|_P 2 CL_|_CL _=_;_|



**Table 3.1** Identification Results 

## 3.10.2 Introduction to the Error Rates 

An identification (1: _n_ comparison) consists of _n_ successive comparisons between the current probe template and _n_ references templates, where _n_ usually denotes all reference templates enrolled in the identity register. Each match is added to a candidate list. Under the assumption that the BMS supports deduplication, i.e. at most one mated template is among the _n_ reference templates, two different initial situations for each identification are possible: 

- The identity register contains one _mated_ (or _related_ ) reference to the current probe. This event is denoted as _R_ in the context of identifications. 

- The identity register contains only _non-mated_ (or _unrelated_ ) references to the current probe. This event is denoted as _R_[¹] in the context of identifications. 

In identifications with registers containing one mated reference, i.e. in case of event _R_ , the following outcomes are possible: 

- The mated reference is correctly returned in the candidate list. This event is denoted as _IR_ . 

- The mated reference is not included in the returned candidate list. This event is denoted as _I_[¹] _R_ . Since the mated reference was among the _n_ references for identification, this is a _false-negative-identification_ error (event _R ^ I_[¹] _R_ ). 

In identifications with registers containing only non-mated references, i.e. in case of event _R_[¹] , the following outcomes are possible: 

- The candidate list is empty. This event is denoted as _I;_ . Since the mated reference was not among the _n_ references for identification, this is the correct outcome. 

- The candidate list is not empty. This event is denoted as _I_ ¹ _;_ . Since the mated reference was not among the ¹ 

- _n_ references for identification, this is a _false-positive-identification_ (event _R_[¹] _^ I;_ ). 

## 3.10.2.1 Calculation of the Error Rates for Identification 

In the following context of identification evaluation, _jRj_ and _jR_[¹] _j_ denote the counts of the events _R_ and _R_[¹] , respectively; i.e. _jRj_ is the number of identifications with a probe, where the identity register contains one mated reference, and _jR_[¹] _j_ is the number of identifications, where the identity register does not contain a mated ¹ ¹ reference. The quantities _jI_[¹] _Rj_ , _jR ^ I_[¹] _Rj_ , _jI_[¹] _;j_ and _jR_[¹] _^ I_[¹] _;j_ are defined accordingly as counts of the corresponding events. 

The following definitions of the error rates are in accordance to [BIB_ISO_19795-1:2021]. 

## 3.10.2.1.1 False-Negative Identification-Rate 

The false-negative identification-rate (false-negative-identification-rate (FNIR)) is defined as the fraction of identifications not returning the mated reference as candidate among the conducted identifications with re gisters including a mated reference: 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0034-19.png)


This quantity can be measured under laboratory conditions, but the daily application may lack the certain information, whether the mated reference was contained among the _n_ references for identification (i.e. whe ther the identification represents event _jRj_ or event _jR_[¹] _j_ ) and whether the correct mated reference is returned in the candidate list (i.e. whether the identification result represent event _IR_ or _I_[¹] _R_ ). Therefore, the calculation 

Federal Office for Information Security 

26 

3 Partial Application Processes 

of the FNIR SHOULD only use identifications, where the mated reference is assumed to be contained in the identity register and to be known, e.g. by comparison of associated identity information or by an operator decision as described in Section 3.10.3.3. In this case, an estimate of the FNIR can be calculated using the fol lowing approximation and by estimating the count _jI_[¹] _Rj_ by the number of cases, in which the assumed mated reference is not returned in the candidate list.[6] 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0035-02.png)


where _N_ FNIR is the number of identifications performed to determine the FNIR. 

## 3.10.2.1.2 False-Positive Identification-Rate 

The false-positive identifications-rate (false-positive-identification-rate (FPIR)) is defined as the fraction of identifications returning a non-empty candidate list among the conducted identifications which did not in clude a comparison with the mated reference:[7] 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0035-06.png)


This quantity can be measured under laboratory conditions, but the daily application may lack the certain information, whether the mated reference is contained among the _n_ references for identification (i.e. whether the identification represents event _jRj_ or event _jR_[¹] _j_ ). Therefore, the calculation of the FPIR SHOULD use only identifications, where the mated reference is assumed to be not contained in the identity register. If the mated reference is assumed to be known, e.g. by comparison of associated identity information or by an operator decision as described in Section 3.10.3.3, it can be (temporarily) excluded from the identity register for eva luation purposes.[8] 

Under the assumption that multiple references do not refer to the same biometric subject in the identity re gister and that the true mated reference is excluded in nearly all _N_ FPIR identifications ( _jR_[¹] _j ¼ N_ FPIR), the FPIR can be calculated as the fraction of identifications returning at least one candidate among the identifications with excluded mated reference: 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0035-09.png)


where _N_ FPIR is the number of identifications performed to determine the FPIR. 

## 3.10.3 Identification Evaluation Workflow for BMS 

The identification evaluation workflow can be triggered by both a verification request and an identification request and uses the biometric probe and, in case of a verification request, the reference from the request for evaluation. Depending on the biometric algorithm, the templates may be generated either explicitly prior to the comparison or implicitly during the comparison. 

- 6 Ideally, the addition of non-mated references in the register should have no influence on the occurrence of mated references in the candidate list. If this property can be assumed for an identification algorithm, a minimal register containing only the mated reference can be used to evaluate the FNIR. 

- 7 The FPIR is not affected by the results of comparisons between mated templates. 

- 8 Ideally, the inclusion of a mated reference in the register should have no influence on the occurrence of non-mated references in the candidate list. If this property can be assumed for an identification algorithm, the mated reference does not need to be excluded from the register; instead it can be simply ignored in the candidate list. 

Federal Office for Information Security 

27 

3 Partial Application Processes 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0036-01.png)


**----- Start of picture text -----**<br>
FM Categories<br>No LOG, COD, CMP<br>Send<br>Request<br>comparison<br>received<br>result to calling<br>application<br>Yes Generate Compare current<br>probe and<br>template<br>reference<br>Start End<br>Explicit feature<br>extraction? Evaluation<br>workow<br>Identity Register<br>**----- End of picture text -----**<br>


**Figure 3.17.** Overall Identification Workflow 

This Partial Application Process allows to determine the error rates (FNIRs and FPIRs) of BMS for identification purpose. 

## 3.10.3.1 Overall Process 

The overall process is comprised of two workflows: 

- Either a verification workflow, which compares the presented candidate (probe) and reference, or an iden tification workflow, which compares the presented candidate (probe) with all references from the identity register. After execution of the verification or identification workflow, respectively, the result is returned to the calling application.[9] 

- The evaluation workflow which conducts identifications with the presented probe by the algorithms de ployed and under evaluation. 

Figure 3.17 shows a general overview over the complete process within the BMS. Note, that the process "Evaluation workflow" is detailed in the following subsection. The probe data (and reference data in case of a verification request) are received or made available to the BMS. Templates are generated and the compari son is performed and logged according to FM Category Logging. Identification and evaluation logging data SHALL be linked by means of the provided transaction identifiers. Note, that the evaluation workflow MAY be scheduled to reduce system load at peak times. Templates MAY be cached to execute the evaluation workflow while low load is on the system. 

## 3.10.3.2 Evaluation Workflow 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0036-10.png)


**----- Start of picture text -----**<br>
Identication<br>with current<br>probe using<br>multiple settings<br>Start End<br>FM Categories<br>LOG, COD<br>**----- End of picture text -----**<br>


**Figure 3.18.** Evaluation Workflow for Identification 

- 9 The confidence in the assumed identity of the reference presented for verification is typically quite high, in particular, in case of a positive outcome. Therefore, these references from verification requests can be used to set up the identity registers used for the evaluation process. 

Federal Office for Information Security 

28 

3 Partial Application Processes 

An overview of the evaluation workflow is given in Figure 3.18. The evaluation workflow executes an iden tification with the current probe from the current (verification or identification) request. The result of the identification is logged according to FM Category Coding and FM Category Logging. The identification and evaluation SHALL be conducted for each modality available separately and for the multimodal identification if multiple modalities are supplied in the initial (verification or identification) request. The evaluation work flow SHALL be an automatic process without manual processing. 

In detail, the following process SHALL be executed in the evaluation workflow for identification: 

1. A probe (sample or template) with one or more biometric modalities is received. 

2. If not already conducted in a previous step, e.g. in a verification evaluation workflow, QA MAY be conduc ted according to FM Category Quality Assessment. 

3. To enhance the quality of the calculation, measures SHOULD be taken to ensure that a mated reference is contained in the register for the following identifications; exemplary measures are listed in Sec tion 3.10.3.3. The following steps are REQUIRED to calculate the FNIR: 

   - a. The score for the comparison of the current probe against the (assumed) mated reference from the identity register (genuine comparison) is obtained for the current identification setup under evalua tion. If this score is already available, e.g. due to a previous comparison between both templates, this result MAY be reused if the algorithms coincided. In particular for the calculation of a Detection Error Trade-Off (DET) curve, where the threshold profile is the only varying parameter, scores need to be obtained just once for each probe-reference-pair. 

   - b. If the resulting score is below the threshold value for the identification under evaluation, the amount of false-negative-identifications _jI_[¹] _Rj_ is counted up. 

   - c. The amount of identifications for FNIR evaluation, _N_ FNIR, is counted up. 

   - d. In addition to the evaluation of the identification workflow in the current setup, steps 3(a) to 3(c) SHOULD be performed using other comparison algorithms and/or other threshold profiles. Note that for each algorithm (or deviating threshold profile), separate counts are REQUIRED. 

   - e. The FNIRs for each setup under evaluation can be calculated by the fraction of both counts according to Equation 3.1. 

4. To enhance the quality of the calculation, measures SHOULD be taken to ensure that a mated reference is not contained in the register for the following identifications; exemplary measures are listed in Sec tion 3.10.3.3. The following steps are REQUIRED to calculate the FPIR: 

   - a. An identification is run, comparing the current probe template against all (assumed) non-mated refe rence templates from the identity register (imposter comparisons). If a comparison score exceeds the current threshold profile, the candidate is set on the candidate list. 

   - b. If at least one candidate is returned during an identification, the amount of false-positive-identificati ons, _jI_ ¹ _Rj_ , is counted up. 

   - c. At the end of each identification, the amount of identifications for FPIR evaluation, _N_ FPIR, is counted up. 

   - d. In addition to the evaluation of the identification workflow in the current setup, steps 4(a) to 4(c) SHOULD be performed using other identification algorithms under evaluation or other threshold pro files. It should be noted that... 

      - ... for each setup under evaluation (register, algorithm, threshold profile), separate counts are RE QUIRED. 

      - ... the FPIRs depends on the number _n_ of references in the identity register and thus, the calculation of the FPIRs (for a given algorithm) SHOULD NOT combine identifications with considerably vary ing register sizes _n_ (e.g. due to amendments to the register), 

      - ... for the calculation of a DET curve, i.e. FPIRs for varying threshold values, the identification needs to be performed just on (using a low threshold profile) and the resulting scores can be checked against all required threshold values (greater or equal than the threshold used in the identification operati on) without successive reproduction of the comparison scores. 

Federal Office for Information Security 

29 

3 Partial Application Processes 

   - e. The FPIR for each setup under evaluation is calculated by the fraction of both corresponding counts according to Equation 3.4. 

5. The results SHALL be logged according to FM Category Coding and FM Category Logging. 

## 3.10.3.3 Optional Measures to Enhance the Quality of the Evaluation 

For the assumptions made above to calculate the error rates, it is essential to ensure, that the correct mated reference template is (or is not) contained in the pool of reference templates. Following implementations MAY be used to achieve this goal: 

- For the accuracy evaluation of identifications or verifications using only one biometric modality, a pre ceding verification based on another biometric modality could give insight about the true nature (ma ted or non-mated) of the relation between probe and reference. As false-non-matches (or respectively fal se-matches) for different biometric modalities are independent, this does not introduce a bias. This is only possible if more biometric modalities are transmitted for the probe and are available for the references than required for the evaluation. Additionally, it MUST be ensured that the accuracy provided by verification of another modality is sufficiently high to prevent from introducing errors. 

- Further insight about the true nature (mated or non-mated) of the relation between probe and reference can be obtained by operator decisions from the main-workflow. Any non-match appearing during the border control process will require further inspection by an operator. The final decision entered by the operator can be used as additional information. If the operator ends this inspection by deciding on a true-non-match, the probe-reference pair SHOULD be excluded in evaluation workflows requiring mated pairs. Thus, the evaluation workflow itself will still be completely automatic, though its start SHALL be delayed until the main border control process is terminated, see Figure 3.19. 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0038-07.png)


**----- Start of picture text -----**<br>
Operator overrules<br>the verication and<br>decides on a false-<br>match Current probe-<br>reference-pair is<br>excluded from the<br>evaluation<br>workow.<br>Manual<br>inspection of the<br>Operator is<br>optional<br>Verication results in a match Current probe-reference-pair<br>will be used in<br>Operator does not  evaluation<br>overrule the  workow Border Control<br>Main verication verication<br>Process is<br>during border<br>Start control workow Operator decides ona false-non-match Current probe- terminated by theoperator decision End<br>reference-pair<br>will be used in<br>evaluation<br>Verication results workow<br>in a non-match<br>Manual<br>inspection of the<br>Operator is<br>mandatory<br>Current probe-<br>reference-pair is<br>excluded from the<br>Operator decides on evaluation<br>a true-non-match workow.<br>**----- End of picture text -----**<br>


**Figure 3.19.** Use of Operator Decisions as a Background Filter 

## 3.11 PAP EVA-VER-wCIR-1: Verification Evaluation Workflow for BMS with Identification Capability and with Verification Capability 

This Partial Application Process specifies how the evaluation of biometric verification SHALL be carried out for biometric matching systems with identification and verification capability. 

## 3.11.1 Introduction to the Error Rates 

Biometric verifications and identifications are based on single algorithmic comparisons between a probe and a reference template, quantifying the resemblance between each pair of templates by a numerical score. The 

Federal Office for Information Security 

30 

3 Partial Application Processes 

binary result of a comparison (match or non-match) depends on whether this numerical score exceeds a preset threshold value. 

A verification consist of a single 1:1 comparison between one probe template and one reference template. Therefore, two scenarios are possible for the incoming probe and reference templates: 

- Probe and reference are _mated_ (or _related_ ), i.e. belong to the biometric characteristic of the same biometric subject. In the following context of verifications, this event is denoted as _R_ . 

- Probe and reference are _non-mated_ (or _unrelated_ ), i.e. do not belong to the same biometric characteristic of the same biometric subject. In the following context of verifications, this event is denoted as _R_[¹] . 

A verification-threshold-value is set, so that two results for the biometric comparison are possible: 

- If the score is above or equal to the threshold, the result of the comparison is a _match_ . In the following context of verifications, this event is denoted as _M_ . 

- If the score is below the threshold, the result of the comparison is a _non-match_ . In the following context of verifications, this event is denoted as _M_[¹] . 

As a consequence, four different scenarios between income and outcome are possible in a verification: 

- Probe and reference are _mated_ and the verification returns a _match_ . This is a correct result ( _true-match_ ) and denoted as _R ^ M_ . 

- Probe and reference are _mated_ and the verification returns a _non-match_ . This is an error referred to as _fal se-non-match_ and denoted as _R ^ M_[¹] . 

- Probe and reference are _non-mated_ and the verification returns a _match_ . This is an error referred to as _fal se-match_ and denoted as _R_[¹] _^ M_ . 

- Probe and reference are _non-mated_ and the verification returns a _non-match_ . This is a correct result ( _truenon-match_ ) and denoted as _R_[¹] _^ M_[¹] . 

A false-match is usually security related, as access might be granted to an imposter. Therefore, an acceptable false-match-rate (FMR) needs to be predefined depending on the application and a strict obedience SHALL be monitored. A false-non-match can be related to a denial of access for a genuine user. This error is usually not security related, though a low false-non-match-rate (FNMR) is important to ensure a high performance, usability and acceptance by the users of the application. 

## 3.11.1.1 Calculation of the Error Rates for Verification 

In the following context of verification evaluation, _jRj_ denotes the amount of comparisons between mated templates for a set of _N_ independent comparisons. The quantities _jR_[¹] _j_ , _jM j_ , _jM_[¹] _j_ , _jR ^ M j_ , _jR ^ M_[¹] _j_ , _jR_[¹] _^ M j_ , _jR_[¹] _^ M_[¹] _j_ are defined accordingly as counts of the corresponding events. This implies _N_ = _jRj_ + _jR_[¹] _j_ = _jM j_ + _jM_[¹] _j_ . 

The following definitions of the error rates are in accordance to [BIB_ISO_19795-1:2021]. 

## 3.11.1.1.1 False-Non-Match-Rate (FNMR) 

The FNMR is defined as the fraction of comparisons returning a non-match among the comparisons between mated images: 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0039-19.png)


Under laboratory conditions, _R_ is known, i.e. whether two images are mated, thus _jR ^ M_[¹] _j_ can be measured and the FNMR exactly calculated. Though the evaluation within the daily application lacks information about whether or not two images are truly mated, thus _R_ is unknown. Therefore, the FNMR needs to be approxi mated: 

Federal Office for Information Security 

31 

3 Partial Application Processes 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0040-01.png)


where _N_ FNMR is the number of verifications performed to determine the false-non-match-rate (FNMR). 

Here, both quantities _jM_[¹] _j_ and _N_ FNMR can be measured. The approximation in Equation 3.6 holds if _jR_[¹] _j ¿ jRj ) jRj ¼ N_ FNMR, thus the amount of true-non-matches is negligible to the amount of false-nonmatches. Therefore, the calculation of the FNMR SHOULD only use verifications, where the reference and probe can be assumed to be mated, e.g. by comparison of associated identity information or by an operator decision as described in Section 3.11.2.2.[10] 

## 3.11.1.1.2 False-Match-Rate (FMR) 

The FMR is defined as the fraction of comparisons returning a match among the comparisons between nonmated images: 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0040-06.png)


Under laboratory conditions, _R_[¹] is known, i.e. whether two images are non-mated, thus _jR_[¹] _^ M j_ can be mea sured and the FMR exactly calculated. Though the evaluation within the daily application lacks information about whether or not two images are truely mated, thus _R_[¹] is unknown. Therefore, FMR needs to be approxi mated: 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0040-08.png)


where _N_ FMR is the number of identifications performed to determine the false-match-rate (FMR). 

Here, both quantities _jM j_ and _N_ FMR can be measured. The approximation in Equation 3.8 holds if _jRj ¿ jR_[¹] _j ) jR_[¹] _j ¼ N_ FMR, thus the amount of true-matches is negligible to the amount of false-matches. The refore, the calculation of the FMR SHOULD only use verifications, where the reference and probe are assumed to be non-mated. 

## 3.11.2 Verification Evaluation Workflow for BMS with Connected Identity Register 

The verification evaluation workflow is triggered by a verification request and uses the biometric probe and reference from the request for evaluation. Depending on the biometric algorithm, the templates may be ge nerated either explicitly prior to the comparison or implicitly during the comparison. 

> 10 Non-mated images could occur due to imposters or due to accidentally changed documents within travel groups. 

Federal Office for Information Security 

32 

3 Partial Application Processes 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0041-01.png)


**----- Start of picture text -----**<br>
FM Categories<br>No LOG, COD, CMP<br>Send<br>Request<br>comparison<br>received<br>result to calling<br>application<br>Yes Generate Compare current<br>probe and<br>template<br>reference<br>Start End<br>Explicit feature<br>extraction? Evaluation<br>workow<br>Identity Register<br>**----- End of picture text -----**<br>


**Figure 3.20.** Overall Verification Workflow with CIR 

Figure 3.20 shows a general overview over the complete verification workflow within the BMS. Note, that the process "Evaluation workflow" is detailed in the following subsection and Figure 3.21. The reference and probe data are received or made available to the BMS. Templates are generated and the comparison is performed and logged according to FM Category Logging. Verification and evaluation logging data SHALL be linked by means of the provided transaction identifiers. 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0041-04.png)


**----- Start of picture text -----**<br>
Quality<br>Assessment<br>FM Category QA RECOMMENDED<br>Compare<br>current reference<br>and probe using<br>multiple settings<br>FM Categories<br>LOG, COD, CMP<br> n Zero-Effort<br>Imposter<br>Comparisons<br>Start End<br>The number of<br>FM Categories  comparisons n<br>LOG, COD, CMP and m SHALL be<br>congurable.<br>Identity Register<br>m Attribute<br>Imposter<br>Comparisons<br>The number of<br>FM Categories  comparisons n<br>LOG, COD, CMP and m SHALL be<br>congurable.<br>Identity Register<br>**----- End of picture text -----**<br>


**Figure 3.21.** Verification Evaluation Workflow with Connected Identity Register 

Federal Office for Information Security 

33 

3 Partial Application Processes 

## 3.11.2.1 Evaluation Workflow 

An overview over the evaluation workflow is given in Figure 3.21. The evaluation workflow itself SHALL be comprised of three main tasks: 

- recommended QA of the current probe and reference image 

- comparison of the current probe with the current reference using an additional comparison algorithm, which was not used for the normal verification, or varying threshold profiles 

- control-verifications of the current probe with non-mated reference templates 

In detail, the following process SHALL be executed in the evaluation workflow for verification: 

1. A probe template and the mated reference template are received. 

2. QA for evaluation purposes MAY be conducted according to FM Category Quality Assessment. 

3. To enhance the quality of the calculation, measures SHOULD be taken to exclude non-mated comparisons in the following genuine comparisons. Exemplary measures are listed in Section 3.11.2.2. The following steps are REQUIRED to calculate the FNMR: 

   - a. The current probe is compared against the current (assumed mated) reference (genuine comparison) to obtain a score. If this score is already available, e.g due to a previous comparison between both tem plates, this result MAY be reused if the algorithms coincided. In particular, for the calculation of a De tection-Error-Tradeoff curve, where the threshold profile is the only varying parameter, scores need to be obtained just once for each probe-template-pair. 

   - b. If the score is below the threshold profile under evaluation, the amount of non-matches ( _M_[¹] ) is counted up. 

   - c. The amount of total comparisons ( _N_ FNMR) is counted up. 

   - d. In addition to the setup of the standard verification workflow, other comparison algorithms and/or other threshold profiles SHALL be evaluated here. Note that for each algorithm (or deviating threshold profile), the non-matches SHALL be counted separately. 

   - e. The FNMR based on the yet evaluated data can be calculated for each setup according to Equation 3.6. 

4. To enhance the quality of the calculation, measures SHOULD be taken to exclude mated comparisons in the following impostor comparisons. Exemplary measures are listed in Section 3.11.2.2. The following steps are REQUIRED to calculate FMR as follows: 

   - a. Comparisons of the current probe with a sufficiently large amount of _n_ templates in a pool of nonmated references from the identity register are conducted without respect to similiar attributes (zero effort). It SHALL be ensured that the pool neither contains the mated reference to the probe nor mul tiple references of the same biometric subject. 

   - b. For each comparison, _N_ FMR is increased by 1. 

   - c. For each comparison score exceeding the current threshold profile under evaluation, the (false) match counter _jM j_ is increased by 1. As all templates without restriction are used, these are the "zero-ef fort"-counts. 

   - d. The FMRs for probe-reference-pairs coinciding in certain attributes SHALL be accessed by separated counts for matches and comparisons when one of the following attributes coincides: 

      - i. Age groups 

      - ii. Sex 

      - iii. Nationality 

      - iv. Document Issuer of Identity Document 

Additional attributes MAY be evaluated. 

- e. The FMRs for the zero-effort and all attributes based on the yet evaluated data can be calculated ac cording to Equation 3.8. 

Federal Office for Information Security 

34 

3 Partial Application Processes 

5. The results are logged according to FM Category Coding and FM Category Logging. 

## 3.11.2.2 Optional Measures to Enhance the Quality of the Evaluation 

For the assumptions made above to calculate the error rates, it is essential to ensure, that the correct mated reference template is (or is not) contained in the pool of reference templates. Following implementations MAY be used to achieve this goal: 

- For the accuracy evaluation of identifications or verifications using only one biometric modality, a pre ceding verification based on another biometric modality could give insight about the true nature (ma ted or non-mated) of the relation between probe and reference. As false-non-matches (or respectively fal se-matches) for different biometric modalities are independent, this does not introduce a bias. This is only possible if more biometric modalities are transmitted for the probe and are available for the references than required for the evaluation. Additionally, it MUST be ensured that the accuracy provided by verification of another modality is sufficiently high to prevent from introducing errors. 

- Further insight about the true nature (mated or non-mated) of the relation between probe and reference can be obtained by operator decisions from the main-workflow. Any non-match appearing during the border control process will require further inspection by an operator. The final decision entered by the operator can be used as additional information. If the operator ends this inspection by deciding on a true-non-match, the probe-reference pair SHOULD be excluded in evaluation workflows requiring mated pairs. Thus, the evaluation workflow itself will still be completely automatic, though its start SHALL be delayed until the main border control process is terminated, see Figure 3.22. 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0043-06.png)


**----- Start of picture text -----**<br>
Operator overrules<br>the verication and<br>decides on a false-<br>match Current probe-<br>reference-pair is<br>excluded from the<br>evaluation<br>workow.<br>Manual<br>inspection of the<br>Operator is<br>optional<br>Verication results in a match Current probe-reference-pair<br>will be used in<br>Operator does not  evaluation<br>overrule the  workow Border Control<br>Main verication verication<br>Process is<br>during border<br>Start control workow Operator decides ona false-non-match Current probe- terminated by theoperator decision End<br>reference-pair<br>will be used in<br>evaluation<br>Verication results workow<br>in a non-match<br>Manual<br>inspection of the<br>Operator is<br>mandatory<br>Current probe-<br>reference-pair is<br>excluded from the<br>Operator decides on evaluation<br>a true-non-match workow.<br>**----- End of picture text -----**<br>


**Figure 3.22.** Use of Operator Decisions as a Background Filter 

## 3.12 PAP EVA-VER-nCIR-1: Verification Evaluation Workflow for BMS without Identification Capability 

This Partial Application Process specifies how the evaluation of biometric verification SHALL be carried out for biometric matching systems without identification capability. 

## 3.12.1 Introduction to the Error Rates 

Biometric verifications and identifications are based on single algorithmic comparisons between a probe and a reference template, quantifying the resemblance between each pair of templates by a numerical score. The binary result of a comparison (match or non-match) depends on whether this numerical score exceeds a preset threshold value. 

Federal Office for Information Security 

35 

3 Partial Application Processes 

A verification consist of a single 1:1 comparison between one probe template and one reference template. Therefore, two scenarios are possible for the incoming probe and reference templates: 

- Probe and reference are _mated_ (or _related_ ), i.e. belong to the biometric characteristic of the same biometric subject. In the following context of verifications, this event is denoted as _R_ . 

- Probe and reference are _non-mated_ (or _unrelated_ ), i.e. do not belong to the same biometric characteristic of the same biometric subject. In the following context of verifications, this event is denoted as _R_[¹] . 

A verification-threshold-value is set, so that two results for the biometric comparison are possible: 

- If the score is above or equal to the threshold, the result of the comparison is a _match_ . In the following context of verifications, this event is denoted as _M_ . 

- If the score is below the threshold, the result of the comparison is a _non-match_ . In the following context of verifications, this event is denoted as _M_[¹] . 

As a consequence, four different scenarios between income and outcome are possible in a verification: 

- Probe and reference are _mated_ and the verification returns a _match_ . This is a correct result ( _true-match_ ) and denoted as _R ^ M_ . 

- Probe and reference are _mated_ and the verification returns a _non-match_ . This is an error referred to as _fal se-non-match_ and denoted as _R ^ M_[¹] . 

- Probe and reference are _non-mated_ and the verification returns a _match_ . This is an error referred to as _fal se-match_ and denoted as _R_[¹] _^ M_ . 

- Probe and reference are _non-mated_ and the verification returns a _non-match_ . This is a correct result ( _truenon-match_ ) and denoted as _R_[¹] _^ M_[¹] . 

A false-match is usually security related, as access might be granted to an imposter. Therefore, an acceptable false-match-rate (FMR) needs to be predefined depending on the application and a strict obedience SHALL be monitored. A false-non-match can be related to a denial of access for a genuine user. This error is usually not security related, though a low false-non-match-rate (FNMR) is important to ensure a high performance, usability and acceptance by the users of the application. 

## 3.12.1.1 Calculation of the Error Rates for Verification 

In the following context of verification evaluation, _jRj_ denotes the amount of comparisons between mated templates for a set of _N_ independent comparisons. The quantities _jR_[¹] _j_ , _jM j_ , _jM_[¹] _j_ , _jR ^ M j_ , _jR ^ M_[¹] _j_ , _jR_[¹] _^ M j_ , _jR_[¹] _^ M_[¹] _j_ are defined accordingly as counts of the corresponding events. This implies _N_ = _jRj_ + _jR_[¹] _j_ = _jM j_ + _jM_[¹] _j_ . 

The following definitions of the error rates are in accordance to [BIB_ISO_19795-1:2021]. 

## 3.12.1.1.1 False-Non-Match-Rate (FNMR) 

The FNMR is defined as the fraction of comparisons returning a non-match among the comparisons between mated images: 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0044-18.png)


Under laboratory conditions, _R_ is known, i.e. whether two images are mated, thus _jR ^ M_[¹] _j_ can be measured and the FNMR exactly calculated. Though the evaluation within the daily application lacks information about whether or not two images are truly mated, thus _R_ is unknown. Therefore, the FNMR needs to be approxi mated: 

Federal Office for Information Security 

36 

3 Partial Application Processes 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0045-01.png)


where _N_ FNMR is the number of verifications performed to determine the FNMR. 

Here, both quantities _jM_[¹] _j_ and _N_ FNMR can be measured. The approximation in Equation 3.10 holds if _jR_[¹] _j ¿ jRj ) jRj ¼ N_ FNMR, thus the amount of true-non-matches is negligible to the amount of false-nonmatches. Therefore, the calculation of the FNMR SHOULD only use verifications, where the reference and probe can be assumed to be mated, e.g. by comparison of associated identity information or by an operator decision as described in Section 3.12.2.2.[11] 

## 3.12.1.1.2 False-Match-Rate (FMR) 

The FMR is defined as the fraction of comparisons returning a match among the comparisons between nonmated images: 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0045-06.png)


Under laboratory conditions, _R_[¹] is known, i.e. whether two images are non-mated, thus _jR_[¹] _^ M j_ can be mea sured and the FMR exactly calculated. Though the evaluation within the daily application lacks information about whether or not two images are truely mated, thus _R_[¹] is unknown. Therefore, FMR needs to be approxi mated: 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0045-08.png)


where _N_ FMR is the number of identifications performed to determine the FMR. 

Here, both quantities _jM j_ and _N_ FMR can be measured. The approximation in Equation 3.12 holds if _jRj ¿ jR_[¹] _j ) jR_[¹] _j ¼ N_ FMR, thus the amount of true-matches is negligible to the amount of false-matches. The refore, the calculation of the FMR SHOULD only use verifications, where the reference and probe are assumed to be non-mated. 

## 3.12.2 Verification Evaluation Workflow for BMS without Connected Identity Register 

The overall verification process is comprised of two workflows: 

- the verification workflow which compares the presented candidate (probe) with a reference and returns the result to the calling application 

- the evaluation workflow which conducts the comparisons with algorithms under evaluation, executes im poster control-verifications for accuracy evaluation and may evaluate the quality of biometric modalities by quality algorithms under evaluation 

> 11 Non-mated images could occur due to imposters or due to accidentally changed documents within travel groups. 

Federal Office for Information Security 

37 

3 Partial Application Processes 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0046-01.png)


**----- Start of picture text -----**<br>
The number of cached<br>Quality  reference templates n<br>Assessment shall be congurable.<br>≤ n reference<br>Compare Cache templates cached<br>reference and<br>current reference<br>probe template using<br>template<br>multiple settings<br>Start End<br>> n reference<br>n templates cached Delete<br>Zero-Effort  oldest reference<br>Imposter  template<br>the number of  Comparisons<br>comparisons n<br>SHALL be<br>congurable Reference Template<br>Cache<br>**----- End of picture text -----**<br>


**Figure 3.23.** Overall Verification Workflow without CIR 

Figure 3.23 shows a general overview over the complete verification workflow within the BMS. Note, that the process "Evaluation workflow" is detailed in the following subsection and Figure 3.24. The reference and probe data are received or made available to the BMS. Templates are generated and the comparison is performed and logged according to FM Category Logging. Verification and evaluation logging data SHALL be linked by means of the provided transaction identifiers. 

Federal Office for Information Security 

38 

3 Partial Application Processes 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0047-01.png)


**----- Start of picture text -----**<br>
Send verication<br>request<br>Compare current<br>Send comparison<br>Generate  reference and<br>result to calling<br>templates current probe<br>application<br>template<br>Start Default End<br>FM Categories<br>Evaluation<br>LOG, COD, CMP<br>workow<br>Reference Template<br>Cache<br>Delete templates<br>older than t hours<br>continuously<br>Calling System<br>Triggered by External Call<br>Scheduled Process<br>**----- End of picture text -----**<br>


**Figure 3.24.** Verification Evaluation Workflow without Connected Identity Register 

## 3.12.2.1 Evaluation Workflow 

An overview over the evaluation workflow is given in Figure 3.24. The evaluation workflow itself SHALL be comprised of three main tasks: 

- recommended QA of the current probe and reference image 

- comparison of the current probe with the current reference using an additional comparison algorithm, which was not used for the normal verification, or varying threshold profiles 

- control-verifications of the current probe with non-mated reference templates 

In detail, the following process SHALL be executed in the evaluation workflow for verification: 

1. A probe template and the mated reference template are recieved. 

2. QA for evaluation purposes MAY be conducted according to FM Category Quality Assessment. 

3. To enhance the quality of the calculation, measures SHOULD be taken to exclude non-mated comparisons in the evaluation. Exemplary measures are listed in Section 3.12.2.2. The following steps are REQUIRED to calculate the FNMR: 

   - a. The current probe is compared against the current (assumed mated) reference (genuine comparison) to obtain a score. If this score is already available, e.g due to a previous comparison between both tem plates, this result MAY be reused if the algorithms coincided. In particular for the calculation of a De 

Federal Office for Information Security 

39 

3 Partial Application Processes 

tection-Error-Tradeoff curve, where the threshold profile is the only varying parameter, scores need to be obtained just once for each probe-template-pair. 

   - b. If the score is below the threshold profile under evaluation, the amount of non-matches ( _M_[¹] ) is counted up. 

   - c. The amount of total comparisons ( _N_ FNMR) is counted up. 

   - d. In addition to the setup of the standard verification workflow, other comparison algorithms and/or other threshold profiles SHALL be evaluated here. Note that for each algorithm (or deviating threshold profile), the non-matches SHALL be counted separately. 

   - e. The FNMR based on the yet evaluated data can be calculated for each setup according to Equati on 3.10. 

4. It is RECOMMENDED to take measures to exclude mated comparisons in the following evaluation steps (e.g. in analogy to Section 3.12.2.2) as the current probe template from the verification process is assumed to be compared against non-mated reference templates (imposter comparisons) to calculate the FMR as follows: 

   - a. Comparisons of the current probe with a sufficiently large amount of _n_ templates in a pool of cached non-mated references are conducted without respect to similiar attributes (zero effort). The pool SHALL NOT contain the mated reference to the probe or multiple references of the same biometric subject. 

   - b. For each comparison, _N_ FMR is increased by 1. 

   - c. For each comparison score exceeding the current threshold profile under evaluation, the (false) match counter _jM j_ is increased by 1. As all templates without restriction are used, these are the "zero-ef fort"-counts. 

   - d. The FMRs for probe-reference-pairs coinciding in certain attributes MAY be accessed by separated counts for matches and comparisons when one of the following attributes coincides: 

      - i. Age groups 

      - ii. Sex 

      - iii. Nationality 

iv. Document Issuer of Identity Document 

Additional attributes MAY be evaluated. 

   - e. The cache is updated: 

      - The reference mated to the current probe SHALL be added to the cache after the imposter compa risons. It SHALL be ensured, that no reference of this biometric subject is already contained in the cache, e.g. by using the alphanumeric data from the identity document corresponding to the images. 

      - The oldest reference in the cache SHALL be deleted, if more than _n_ references are currently stored in the cache. This maximum amount _n_ of references in the cache SHALL be configurable. 

      - Additionally, cached references SHALL be deleted after a configurable time _t_ in accordance with the applicable data protection regulations. 

   - f. The FMRs for the zero-effort and all attributes based on the yet evaluated data can be calculated ac cording to Equation 3.12. 

5. The results are logged according to FM Category Coding and FM Category Logging. 

## 3.12.2.2 Optional Measures to Enhance the Quality of the Evaluation 

For the assumptions made above to calculate the error rates, it is essential to ensure, that the correct mated reference template is (or is not) contained in the pool of reference templates. Following implementations MAY be used to achieve this goal: 

- For the accuracy evaluation of identifications or verifications using only one biometric modality, a pre ceding verification based on another biometric modality could give insight about the true nature (ma 

Federal Office for Information Security 

40 

3 Partial Application Processes 

ted or non-mated) of the relation between probe and reference. As false-non-matches (or respectively fal se-matches) for different biometric modalities are independent, this does not introduce a bias. This is only possible if more biometric modalities are transmitted for the probe and are available for the references than required for the evaluation. Additionally, it MUST be ensured that the accuracy provided by verification of another modality is sufficiently high to prevent from introducing errors. 

- Further insight about the true nature (mated or non-mated) of the relation between probe and reference can be obtained by operator decisions from the main-workflow. Any non-match appearing during the border control process will require further inspection by an operator. The final decision entered by the operator can be used as additional information. If the operator ends this inspection by deciding on a true-non-match, the probe-reference pair SHOULD be excluded in evaluation workflows requiring mated pairs. Thus, the evaluation workflow itself will still be completely automatic, though its start SHALL be delayed until the main border control process is terminated, see Figure 3.25. 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0049-03.png)


**----- Start of picture text -----**<br>
Operator overrules<br>the verication and<br>decides on a false-<br>match Current probe-<br>reference-pair is<br>excluded from the<br>evaluation<br>workow.<br>Manual<br>inspection of the<br>Operator is<br>optional<br>Verication results in a match Current probe-reference-pair<br>will be used in<br>Operator does not  evaluation<br>overrule the  workow Border Control<br>Main verication verication<br>Process is<br>during border<br>Start control workow Operator decides ona false-non-match Current probe- terminated by theoperator decision End<br>reference-pair<br>will be used in<br>evaluation<br>Verication results workow<br>in a non-match<br>Manual<br>inspection of the<br>Operator is<br>mandatory<br>Current probe-<br>reference-pair is<br>excluded from the<br>Operator decides on evaluation<br>a true-non-match workow.<br>**----- End of picture text -----**<br>


**Figure 3.25.** Use of Operator Decisions as a Background Filter 

## 3.13 PAP UPD-B-EES-1: Update EES Reference Biometrics 

This PAP it not used yet and is only part of this TR due to temporary reasons. 

Figure 3.26 depicts the update process of reference biometrics in a CIR (here: CS EES) by live acquired images. Note, that the PAP Task UPD-FP-EES-1: EES Biometric Update Fingerprints and Section 3.13.1 are used here. 

The process specified here SHALL only be executed if all prior verifications of the biometric subject were successful or, if a verification failed, an operator has qualified the prior verification result as false non-match. 

Federal Office for Information Security 

41 

3 Partial Application Processes 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0050-01.png)


**----- Start of picture text -----**<br>
Application specic:<br>Task Update EES Facial Image<br>or<br>Task Update VIS Facial Image<br>Update CIR<br>Reference<br>Yes Facial Images<br>No<br>New Facial Image<br>for CIR captured?<br>Start End<br>No<br>New Fingerprint for<br>CIR captured?<br>Yes Update CIR<br>Reference<br>Fingerprints<br>Application specic:<br>Task Update EES Fingerprints<br>or<br>Task Update VIS Fingerprints<br>**----- End of picture text -----**<br>


**Figure 3.26.** Partial Application Process "Update CIR Reference Biometrics" 

## 3.13.1 PAP Task UPD-FI-EES-1: EES Biometric Update Facial Images 

Figure 3.27 depicts the update process of reference facial images in the CS EES by live acquired facial images. 

For the process decision of expired Entry-Exit System (EES) reference facial images, the following rule SHALL be applied. An EES reference facial image SHALL be considered as expired if one of the following statements hold true for the EES reference facial image: 

- if the age of biometric subject was _less than or equal to 12 years_ at the create timestamps of the EES reference facial image and the time range between the EES reference facial image create timestamps and the current date is _greater than 1 year_ 

- if the age of biometric subject was _greater than 12 years_ at the create timestamps of the EES reference facial image and the time range between the EES reference image create timestamps and the current date is _greater than 3 years_ 

For the process decision of whether the EES reference facial images is superior in terms of quality to the live facial image, the FM QA-FI-GENERIC and FM QA-FI-BCL SHALL be applied. 

Federal Office for Information Security 

42 

3 Partial Application Processes 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0051-01.png)


**----- Start of picture text -----**<br>
EES reference  EES reference<br>Biometric subject provided new  image indication "Chip image"  EES reference  indication "Low facial image<br>Travel Document? present? image expired? quality" present?<br>No No No No<br>Start Yes Yes refer to specication by PAP text Yes Yes Default End<br>FP verication<br>successful OR<br>(verication not<br>possible due to not<br>matching available<br>live ngers to<br>reference ngers  FM COD-FI-EES<br>AND FI verifcation  Live FI of sufcient<br>successful) quality?<br>Yes Yes Update EES<br>reference FI by<br>live FI<br>No No<br>FM QA-FI-GENERIC,<br>FM QA-FI-<VL><br>**----- End of picture text -----**<br>


**Figure 3.27.** Partial Application Process Task "EES Biometric Update Facial Images" 

## 3.13.2 PAP Task UPD-FP-EES-1: EES Biometric Update Fingerprints 

Figure 3.28 depicts the update process of reference fingerprints in the CS EES by live acquired fingerprints. For the decision on the conditions and fingerprint update actions, the process in Figure 3.28 SHALL be ap plied. 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0051-05.png)


**----- Start of picture text -----**<br>
Update<br>EES reference<br>ngerprints<br>Start End<br>The decision<br>table of the task<br>text SHALL be<br>followed.<br>**----- End of picture text -----**<br>


**Figure 3.28.** Partial Application Process Task "EES Biometric Update Fingerprints" 

An update of EES reference fingerprint SHALL be conducted according to Table 3.2. In addition, a reasoning for the specified update rules will be amended in a next version of this Technical Guideline. 

Note, that the following constraints have to be met by the update rules from a legislative point of view: 

- Right and left hand fingerprint images SHALL never be stored simultaneously in the CS EES. 

- If at least one finger of the right hand is available, the right hand slap SHALL be used, even if only one finger is available and four fingers of the left hand would be available. 

- A "best of" slap SHALL NOT be created, i.e. a slap stored with single fingers acquired in different acquisition processes. 

In addition, the following constraint is set: 

- The quality of a fingerprint image is considered as sufficient if the quality score of the relevant finger excels a threshold. Update of fingerprints above the threshold SHALL NOT affect the update rules. 

- As many fingerprint images as possible of suitable quality SHALL be enrolled in the EES. 

- Information about the status of the missing fingers SHOULD be as accurate as possible. 

For the decision whether the EES reference fingerprints are of better quality compared to the live fingerprint, the FM QA-FP-APP SHALL be applied. 

Federal Office for Information Security 

43 

3 Partial Application Processes 

||||**Right Hand Fingerprints**|**Right Hand Fingerprints**|||
|---|---|---|---|---|---|---|
||||**no fingerprint stored in EES**||**at least one fingerprint stored in**<br>**EES**||
||||**at least one**<br>**live fingerprint**<br>**available12**|**no live finger**<br>**print available**|**at least one**<br>**live fingerprint**<br>**available13**|**no live finger**<br>**print available**|
|Left Hand Fin<br>gerprints|no fingerprint<br>stored in EES|at least one<br>live fingerprint<br>available|1. add live right<br>fingers to EES<br>Traveller File|2.<br>**•**<br>update EES<br>reference<br>right fingers'<br>missing rea<br>son<br>**•**<br>add live left<br>fingers to<br>EES Travel<br>ler File|3. if more live<br>right fingers are<br>available than<br>EES Traveller<br>File right fin<br>gers OR (the<br>bad quality<br>flag for any<br>EES Traveller<br>File right fin<br>gers is set AND<br>the same live<br>right finger<br>as bad quality<br>EES Traveller<br>File fingers are<br>available AND<br>all live right<br>fingers are of<br>better or same<br>quality than the<br>EES Traveller<br>File right fin<br>gers AND not<br>less live right<br>hand finger<br>prints are avail<br>able than EES<br>Traveller File<br>right fingers):<br>replace EES<br>Traveller File<br>right fingers by<br>live right fin<br>gers|4.<br>**•**<br>delete EES<br>Traveller File<br>right fingers<br>and add live<br>right fingers'<br>missing rea<br>son<br>**•**<br>add live left<br>fingers to EES<br>Traveller File|
|||no live finger<br>print available||5.<br>**•**<br>update EES<br>Traveller<br>File right<br>fingers' mis<br>sing reason<br>**•**<br>update EES<br>Traveller<br>File left fin<br>gers' missing<br>reason||6. if all live right<br>fingers marked<br>as permanent<br>ly missing: dele<br>te EES Traveller<br>File right fingers<br>and add live left<br>fingers' missing<br>reason.|



- 12 Note, if no EES reference fingerprint is stored and at least one right live fingerprint is available, the acqui sition of a left hand fingerprint SHALL NOT happen as it is not required for any purpose. Thus, no distinc tion between the case of _at least one live fingerprint available_ and _no live fingerprint available_ for left hand fingerprints is required 

- 13 Note, if at least one right EES reference fingerprint is stored and at least one right live fingerprint is avail able, the acquisition of a left hand fingerprint SHALL NOT happen as it is not required for any purpose. Thus, no distinction between the case of _at least one live fingerprint available_ and _no live fingerprint avail able_ for left hand fingerprints is required 

Federal Office for Information Security 

44 

3 Partial Application Processes 

||||**Right Hand Fingerprints**|**Right Hand Fingerprints**|||
|---|---|---|---|---|---|---|
||||**no fingerprint stored in EES**||**at least one fingerprint stored in**<br>**EES**||
||||**at least one**<br>**live fingerprint**<br>**available12**|**no live finger-**<br>**print available**|**at least one**<br>**live fingerprint**<br>**available13**|**no live finger-**<br>**print available**|
||at least one fin<br>gerprint stored<br>in EES|at least one<br>live fingerprint<br>available|7.<br>**•**<br>delete EES<br>Traveller<br>File left fin<br>gers<br>**•**<br>add live<br>right fingers<br>to EES Tra<br>veller File|8.<br>**•**<br>update EES<br>Traveller<br>File right<br>fingers' mis<br>sing reasons<br>**•**<br>do number 3<br>with live left<br>hand finger<br>prints and<br>left EES Tra<br>veller File<br>fingers ins<br>tead|By EU-regulation, CS EES never<br>stores left and right hand finger<br>prints at the same time.||
|||no live finger<br>print available||9.<br>**•**<br>update EES<br>Traveller<br>File right<br>fingers' mis<br>sing reason<br>**•**<br>if all live left<br>fingers mar<br>ked as per<br>manently<br>missing: de<br>lete EES Tra<br>veller File<br>left fingers<br>and add live<br>left fingers'<br>missing rea<br>son|||



**Table 3.2** Decision Table EES Reference Fingerprint Update 

## 3.13.2.1 Annotations to Decision Table 3.2 

The following annotations explain the reasoning behind the decision table. Each annotation refers to the cell of the decision table by its number. 

1. If no fingerprints of the right hand are enrolled, though currently available, they SHALL be enrolled. 

2. The reason for fingerprint images missing in the EES might change, e.g. from temporary missing fingers to permanently missing fingers. Therefore, an update is REQUIRED even if no fingerprint images can be ac quired. If no fingerprint images of the right hand are available, the left hand SHALL be used for enrolment. 

- 12 Note, if no EES reference fingerprint is stored and at least one right live fingerprint is available, the acqui sition of a left hand fingerprint SHALL NOT happen as it is not required for any purpose. Thus, no distinc tion between the case of _at least one live fingerprint available_ and _no live fingerprint available_ for left hand fingerprints is required 

- 13 Note, if at least one right EES reference fingerprint is stored and at least one right live fingerprint is avail able, the acquisition of a left hand fingerprint SHALL NOT happen as it is not required for any purpose. Thus, no distinction between the case of _at least one live fingerprint available_ and _no live fingerprint avail able_ for left hand fingerprints is required 

Federal Office for Information Security 

45 

3 Partial Application Processes 

3. Following the aim to store as many fingerprint images of sufficient quality of the right hand as possible in the EES. 

- 

- 4. 

5. If no fingerprint images of the right hand are available, the left hand SHALL be enrolment. As only fin gerprints of one hand must be enrolled in the EES, the right hand fingerprints SHALL be deleted and the missing reasons saved. 

6. If no fingerprints of any hand are currently available, an update SHALL NOT be done as it would delete the currently enrolled fingerprint images. The only exception is the case, where all fingers of the right hand are now permanently missing. In this case, the fingerprint images of the right hand SHALL be deleted in the EES, as they can no longer be used for traveller verification. In this case, at least the reasons for the missing left fingers SHALL be enrolled. 

7. Following the legal requirements, that the fingers of the right hand SHALL always be enrolled if possible. 

## - 8. 

9. If no fingerprints of any hand are currently available, an update SHALL NOT be done as it would delete the currently enrolled fingerprint images. The only exception is the case, where all fingers of the left hand are now permanently missing. In this case, the fingerprint images of the left hand SHALL be deleted in the EES, as they can no longer be used for traveller verification. In this case, at least the reasons for the missing right fingers SHALL be enrolled. 

Federal Office for Information Security 

46 

4 Function Modules 

## 4 Function Modules 

This chapter lists all Function Modules for the defined Application Profiles. 

## 4.1 FM Category Acquisition Hardware 

Devices that are used for digitising physical, representable biometric characteristics are called Acquisition Hardware (AH). Digital cameras to capture images of the face, fingerprint sensors, or signature tablets can be named as examples. 

## 4.1.1 FM AH-ALL-SSS 

This Function Module describes the requirements for SSSs that are used to obtain digitised facial images and fingerprints. 

## 4.1.1.1 Requirements 

## 4.1.1.1.1 General Requirements 

- An environment surveillance camera system SHALL supervise the area around the SSS. 

   - The camera images SHALL allow to identify whether more than one person was in range of the SSS during the capture of the fingerprints. 

   - The surveillance camera system SHALL capture an image of the surrounding area at the moment of each finger capture attempt. The face of the biometric subject using the fingerprint scanner SHALL be visible in the image of the surveillance camera. 

   - The images SHALL be cached locally on the SSS. 

   - A maximum of 100 ms SHALL be allowed to elapse between the fingerprint capture attempt image and the capture of the surveillance camera system. 

   - For the fingerprint image selected in the acquisition process, the corresponding surveillance image SHALL be made available from the cache. 

   - A colour camera SHALL be used for the environment surveillance. 

   - The camera SHALL be capable to capture images with a resolution of at least 1280 x 720 pixels. 

- A camera system SHALL closely supervise the fingerprint capture system. 

   - The camera image is intended to identify whether presentation attack instruments are applied to the fingerprint capture system. 

   - The camera system SHALL capture an image of the fingerprint acquisition area at the moment of each finger capture attempt. 

   - The images SHALL be cached locally on the SSS. 

   - A maximum of 100 ms SHALL be allowed to elapse between the fingerprint capture attempt image and the capture of the surveillance camera system. 

   - A colour camera SHALL be used for the fingerprint capture surveillance. 

   - The camera SHALL be capable to capture images with a resolution of at least 1280 x 720 pixels. 

- In case the biometric subject leaves the corridor in front of the SSS system, the running SSS process SHALL be stopped. The corridor is defined by a distance of 100 cm in front of the SSS and the width of the SSS. Note, this requirement does not mandate a dedicate hardware sensor to enable the detection of leaving. The detection MAY also happen in software based on the surveillance images. In this case, the requirement does not affect any additional hardware. 

## 4.1.1.2 Recommendations 

In case the biometric subject is approaching close to the maximum allowed distance of the SSS the biometric subject SHOULD be warned. 

Federal Office for Information Security 

47 

4 Function Modules 

## 4.1.2 FM AH-FI-BCL 

This Function Module describes the requirements for systems where a digitised facial image is obtained. Note, the distance between camera system and biometric subject is defined as the geometrical optical-path length between the forehead of the biometric subject and the active camera system's optic. The optical-path MAY, for example, follow a straight line from forehead to optic, or be rerouted by using mirrors so that the biometric subject can stand closer to the device. 

## 4.1.2.1 Requirements 

- The system MAY measure the distance between the biometric subject and the camera system. 

- The camera system SHALL capture images in colour. 

- The system SHALL allow high quality acquisitions independently from the environmental light situation. 

- The camera system SHALL at least allow to acquire facial images compliant to this Technical Guideline of biometric subject which have a body height in range of 140 cm to 200 cm if standing upright in front of the camera system. 

- If the biometric subject is standing at 60 cm distance to the camera system, the minimum physical reso lution of the camera system SHALL allow to crop the full frontal facial image of the biometric subject to 1600 x 1200 pixels with an allowed deviation of maximum negative 10 %. 

- The camera system SHALL capture sharp full frontal images with minimized distortion of biometric sub jects which 

   - stand upright 40 cm to 100 cm[1] in front of the camera system and 

   - look frontal. 

- Biometric subjects with a distance of less than 40 cm or more than 100 cm SHALL NOT be captured. 

- If the biometric subject is in the capture area of maximum 100 cm and minimum 40 cm distance to the camera system, the camera installation SHALL be able to capture an image according to the definition of "full frontal" (see [BIB_ISO_19794_FACE][2] ) on a hardware level. Especially an image capturing at "Frankfurt Horizon" SHALL be possible for all biometric subjects within the defined range of body height. 

## 4.1.3 FM AH-FI-DC 

This Function Module describes the requirements for facial image cameras and physical setups that are used to obtain facial images. 

## 4.1.3.1 Requirements 

- The camera SHALL be able to capture a full frontal facial image of the person if the person is looking straight to the camera. The minimum physical resolution of the camera SHALL allow a cropping of the captured facial image to 1200 x 1600 pixels without any upscaling. Note, this requirement is OPTIONAL for scenarios where only a facial verification is performed. 

- Adequate image quality to meet the requirements of [BIB_ISO_19794_FACE][3] SHALL be provided. 

- The physical and environmental conditions for capturing facial images, such as the positioning of the ca mera, proper lighting of the face and a uniform background as described in [BIB_ISO_19794_FACE] and [BIB_ICAO_TR_Portrait_Quality] SHALL be complied with. It is RECOMMENDED to use a uniform back ground in grey (i.e. R=G=B) between #A1A1A1 and #E1E1E1. 

- The camera system SHALL be able to capture images in colour (24 bit sRGB). Note, this requirement is OP TIONAL for scenarios where only a facial verification is performed. 

> 1 Note, that the physical construction of the system may not allow the biometric subject to stand at the maximum distance. 

> 2 The ISO/IEC 39794 series might be relevant here. 

> 3 

> The ISO/IEC 39794 series might be relevant here. 

Federal Office for Information Security 

48 

4 Function Modules 

- The requirements for focal length (depending on the size of the camera sensor) as described in [BIB_I CAO_TR_Portrait_Quality] (chapters 5.2.1 and 5.2.2) SHALL be complied with. Wide-angle settings MUST NOT be used. 

## 4.1.4 FM AH-FI-EGT 

This Function Module describes the requirements for e-gate scenarios where a digitised facial image is obtai ned. 

## 4.1.4.1 Requirements 

- The camera system SHALL cover at least a range of 140 cm to 200 cm of a person's body height (if standing in front of the camera system). 

- The minimum physical resolution of the captured facial image SHALL be at least 600 x 800 pixels without any upscaling. 

- The camera system SHALL be designed to be placed in the moving direction of the biometric subject (side ways attached camera units which require a rotation of the moving person SHALL NOT be used). 

- Biometric subjects SHALL be captured within a typical range of at least 200 cm with sufficient sharpness and with minimized distortion of the captured face. 

## 4.1.4.2 Recommendations 

- The physical resolution of the captured facial image is RECOMMENDED to be 1200 x 1600 pixels without any upscaling. 

- It is RECOMMENDED that at a distance of 70 cm before the end of the gate (typically the exit door), the necessary rotation of the person requires less than 15 degrees. 

## 4.1.5 FM AH-FI-ICS 

This Function Module describes the requirements for integrated camera systems that are used to obtain digi tised facial images. 

## 4.1.5.1 Requirements 

- The camera SHALL be able to capture a frontal image of the person if the person is looking straight to the camera. 

- The camera system SHALL use diffuse lighting which SHALL adapt to the environmental light conditions for a uniform illumination of the biometric subject's face to ensure the capture of a well-exposed facial image; mirroring effects of glasses SHALL be avoided. 

- The camera system SHALL provide a feedback screen for displaying the camera live acquisition image (di gital mirror). If the biometric subject is looking straight to the feedback screen the viewing direction of the person SHALL be frontal. The feedback SHALL include guidance to help the biometric subject for correct positioning in front of the camera. 

- The system SHALL allow high quality acquisitions independently from the environmental light situation that can usually be found in the environment in question. 

- The camera system SHALL guarantee the sharpness of the captured image within the designated capture area. 

- The camera system SHALL minimise the distortion of the captured face within the whole capture area. 

- The minimum physical resolution of the captured facial image SHALL be at least 1200 x 1600 pixels without any upscaling. Note, this requirement is OPTIONAL for scenarios where only a facial verification is perfor med. 

- The camera system SHALL be able to capture images in colour (24 bit sRGB). Note, this requirement is OP TIONAL for scenarios where only a facial verification is performed. 

Federal Office for Information Security 

49 

4 Function Modules 

- The requirements for focal length (depending on the size of the camera sensor) as described in [BIB_I CAO_TR_Portrait_Quality] (chapters 5.2.1 and 5.2.2) SHALL be complied with. Wide-angle settings MUST NOT be used. 

## 4.1.6 FM AH-FI-SSS 

This Function Module describes the requirements for SSS scenarios where a digitised facial image is obtained. 

## 4.1.6.1 Requirements 

The camera system SHALL NOT require the biometric subject to rotate its standing position while interacting with the graphical user interface in order to look straight to the camera system. 

## 4.1.7 FM AH-FP-OPT 

This Function Module describes the requirements for optical high quality fingerprint scanners (single finger and multi finger). 

## 4.1.7.1 Requirements 

- For the acquisition of the fingerprints, optical sensors using the principal of frustrated total reflection or direct contact (the imaging system is the sensor surface, typically separated by a transparent protection layer) according to the certification requirements of [BIB_ISO_19794_FINGER][4] (especially this means a resolution of 500 ppi or 1000 ppi) SHALL be used exclusively. 

- For the acquisition of the fingerprints, only devices are permitted which meet the following requirements (in analogy to [BIB_EBTS/F]). Notwithstanding, a capturing area of at minimum 16 mm width and 20 mm height is REQUIRED (deviating from table F 1 in [BIB_EBTS/F]) for single finger scanners. 

## 4.1.7.1.1 Grey Scale Linearity 

When measuring a stepped series of uniform target reflectance patches ("step tablet") that substantially covers the scanner's grey range, the average value of each patch SHALL be within 7.65 grey levels of a linear, least squares regression line fitted between target reflectance patch values (independent variable) and scanner out put grey levels of 8 bit resolution (dependent variable). 

## 4.1.7.1.2 Resolution and Geometrical Accuracy 

Resolution: The scanner's final output fingerprint image SHALL have a resolution, in both sensor detector row and column directions, in the range: ( _R ¡_ 0 _:_ 01 _R_ ) to ( _R_ + 0 _:_ 01 _R_ ). The magnitude of _R_ is either 500 ppi or 1000 ppi; a scanner MAY be certified at either one or both of these resolution levels. The scanner's true optical resolution SHALL be greater than or equal to _R_ . 

Across-Bar geometric accuracy: When scanning a 1.0 cy/mm, multiple parallel bar target, in both vertical bar and horizontal bar orientations, the absolute value of the difference ( _D_ ) between the actual distance across parallel target bars ( _X_ ), and the corresponding distance measured in the image ( _Y_ ) SHALL NOT exceed the following values for at least 99 % of the tested cases in each print block measurement area and in each of the two directions: 

- for 500 ppi scanners: 

   - _D ·_ 0 _:_ 0007, for 0 _:_ 00 _< X ·_ 0 _:_ 07 and 

   - _D ·_ 0 _:_ 01 _X_ , for 0 _:_ 07 _· X ·_ 1 _:_ 50 

- for 1000 ppi scanners: 

   - _D ·_ 0 _:_ 0005, for 0 _:_ 00 _< X ·_ 0 _:_ 07 and 

   - _D ·_ 0 _:_ 0071 _X_ , for 0 _:_ 07 _· X ·_ 1 _:_ 50 

where _D_ = _jY ¡ Xj_ , _X_ = actual target distance, _Y_ = measured image distance ( _D; X; Y_ are in inches). 

Along-Bar geometric accuracy: When scanning a 1.0 cy/mm, multiple parallel bar target, in both vertical bar and horizontal bar orientations, the maximum difference in the horizontal or vertical direction, respectively, 

- 4 The ISO/IEC 39794 series might be relevant here. 

Federal Office for Information Security 

50 

4 Function Modules 

between the locations of any two points within a 1.5 inch segment of a given bar image, SHALL be less than 0.016 inches for at least 99 % of the tested cases in each print block measurement area and in each of the two orthogonal directions. 

## 4.1.7.1.3 Contrast Transfer Function 

The spatial frequency response SHALL be measured using a binary grid target (Ronchi-Grating), denoted as contrast transfer function (CTF) measurement. When measuring the bar CTF, it SHALL meet or exceed the minimum modulation values defined by equation Equation 4.1 or equation Equation 4.2, in both the de tector's row and detector's column directions, and over any region of the scanner's field of view. CTF values computed from equations Equation 4.1 and Equation 4.2 for nominal test frequencies are given in the fol lowing table. None of the CTF modulation values measured at specification spatial frequencies SHALL exceed 1.05. The output bar target image SHALL NOT exhibit any significant amount of aliasing. It is NOT REQUIRED that the bar target contains the exact frequencies listed in Table 4.1, however, the target does need to cover the listed frequency range and contain bar patterns close to each of the listed frequencies. 

The following equations are used to obtain the minimum acceptable CTF modulation values when using bar targets that contain frequencies not listed in Table 4.1: 

- 500 ppi scanner, for f = 1.0 to 10.0 cy/mm: 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0059-06.png)


- 1000 ppi scanner, for f = 1.0 to 20.0 cy/mm: 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0059-08.png)


For a given bar target, the specification frequencies include all of the bar frequencies which that target has in the range 1 to 10 cy/mm (500 ppi scanner) or 1 to 20 cy/mm (1000 ppi scanner). 

|**Frequency [cy/mm]**|**Minimum Modulation for 500 ppi**<br>**scanners**|**Minimum Modulation for**<br>**1000 ppi scanners**|**Maximum Modulation**|
|---|---|---|---|
|1.0|0.948|0.957|1.05|
|2.0|0.869|0.904|1.05|
|3.0|0.791|0.854|1.05|
|4.0|0.713|0.805|1.05|
|5.0|0.636|0.760|1.05|
|6.0|0.559|0.716|1.05|
|7.0|0.483|0.675|1.05|
|8.0|0.408|0.636|1.05|
|9.0|0.333|0.598|1.05|
|10.0|0.259|0.563|1.05|
|12.0|---|0.497|1.05|
|14.0|---|0.437|1.05|
|16.0|---|0.382|1.05|
|18.0|---|0.332|1.05|
|20.0|---|0.284|1.05|



**Table 4.1** Minimum and Maximum Modulation 

## 4.1.7.1.4 Signal-to-Noise Ratio and the Grey–Level Uniformity 

The white signal-to-noise ratio (SNR) and black SNR SHALL each be greater than or equal to 125.0, in at least 97 % of respective cases, within each measurement area. 

The grey level uniformity is defined for the three following cases: 

Federal Office for Information Security 

51 

4 Function Modules 

- Adjacent row, column uniformity: At least 99 % of the average grey levels between every two adjacent quar ter-inch long rows and 99 % between every two adjacent quarter-inch long columns, within each imaged area, SHALL NOT differ by more than 1.0 grey levels when scanning a uniform low reflectance target, and SHALL NOT differ by more than 2.0 grey levels when scanning a uniform high reflectance target. 

- Pixel to pixel uniformity: For at least 99.9 % of all pixels within every independent 0.25 inch by 0.25 inch area located within each imaged area, individual pixel's grey level SHALL NOT vary from the average by more than 22.0 grey levels, when scanning a uniform high reflectance target, and SHALL NOT vary from the average by more than 8.0 grey levels, when scanning a uniform low reflectance target. 

- Small area uniformity: For every two independent 0.25 inch by 0.25 inch areas located within each imaged area, the average grey levels of the two areas SHALL NOT differ by more than 12.0 grey levels when scanning a uniform high reflectance target, and SHALL NOT differ by more than 3.0 grey levels when scanning a uniform low reflectance target. 

## 4.1.7.1.5 Grey Scale Range of Fingerprint Images 

A fingerprint scanner operating at 500 ppi or 1000 ppi, SHALL perform the following sets of live scans: 

- For a standard roll and plain finger live scanner: capture a complete set of fingerprints from each of 10 sub jects; i.e. 10 rolls (all 5 fingers from each hand), 2 plain thumb impressions, and 2 plain 4-finger impressions. 

- For a palm scanner component of a live scan system: capture left and right palms from each of 10 subjects. 

- For an identification flat live scanner: capture left and right 4-finger plain impressions and dual thumb plain impressions from each of 10 subjects. 

Within the histogram of each image all grey values with at least 5 Pixels in this image are counted. The histo gram SHALL show no break and no other artefact. At least 80 % of the captured individual fingerprint images SHALL have a grey scale dynamic range of at least 200 grey levels, and at least 99% SHALL have a dynamic range of at least 128 grey levels. 

## 4.1.8 FM AH-FP-SSS 

This Function Module describes the requirements for SSS scenarios where digitised fingerprints are obtained. 

## 4.1.8.1 Requirements 

- The spatial configuration of the fingerprint acquisition system SHALL be optimal for primary right hand acquisition. 

- The spatial configuration of the fingerprint acquisition system SHALL allow the acquisition of left hands. 

- During the fingerprint acquisition process multiple persons within the reach of the fingerprint acquisition system of the SSS SHALL be detected. 

- The multiple person detection result SHALL be cached locally on the SSS. 

## 4.1.8.2 Recommendation 

Measures SHOULD be taken to make the fingerprint acquisition system apparent to the biometric subject as the active part of the SSS to interact with in the moment where an acquisition of fingerprints is foreseen. 

## 4.2 FM Category Acquisition Software 

The Function Module category Acquisition Software (AS) contains all functionality regarding image proces sing for biometric purposes. Therefore, these Function Modules usually contains device driver software for the acquisition hardware or, in general, software that is very close to the physical hardware such as firmware. Furthermore, colour management and image enhancement mechanisms are part of this software layer. 

## 4.2.1 FM AS-FI-DC 

This Function Module describes the requirements and interfaces for acquisition software used for facial image cameras in order to obtain digitised images. 

Federal Office for Information Security 

52 

4 Function Modules 

## 4.2.1.1 Requirements 

- In regard to the application scenario an adequate resolution of the camera SHALL be chosen to acquire a facial image of at least 1200 x 1600 pixels with an inter eye distance of at least 120 pixels. 

- The images SHALL be captured and stored in colour (24 bit sRGB). Note, this requirement is OPTIONAL for scenarios where only a facial verification is performed. 

- In normal mode of operation, no compression artefacts SHALL be detectable in the image. 

## 4.2.1.2 Recommendations 

- The image data SHOULD be provided without any compression or with lossless compression. If the acqui sition device does not support a lossless mode, the image MAY alternatively be provided with the minimal level of compression possible. 

- Acquisition software that supports calibration procedures for the respective digital camera SHOULD be used (in particular colour management). 

## 4.2.2 FM AS-FI-ICS 

This Function Module describes the requirements and interfaces for acquisition software used for integrated camera systems in order to obtain digitised facial images. 

## 4.2.2.1 Requirements 

- The acquisition software of the camera system SHALL provide uncompressed image data for further pro cessing. 

- The selected resolution within the camera settings (e.g. configurable via camera firmware SHALL be at least 1200 x 1600 pixels. Note, this requirement is OPTIONAL for scenarios where only a facial verification is performed. 

- The integrated camera system SHALL have the diffuse lighting activated within software. 

- The capture of images in colour (24 bit sRGB) SHALL be selected. Note, this requirement is OPTIONAL for scenarios where only a facial verification is performed. 

## 4.2.3 FM AS-FI-ICS3 

This Function Module describes the requirements and interfaces for acquisition software used for integrated camera systems in order to obtain digitised facial images. 

## 4.2.3.1 Requirements 

- The acquisition software of the camera system SHALL detect whether multiple faces are presented to the camera system simultaneously in the capture area. 

- The acquisition software of the camera system SHALL detect whether a face which is presented to the ca mera system completely leaves the capture area. The process SHALL then terminate after a configurable timeout. 

## 4.2.4 FM AS-FP-MF 

This Function Module describes the requirements and interfaces for acquisition software for multi finger scanners. 

## 4.2.4.1 Requirements 

- The image provided by acquisition software SHALL meet the criteria of fingerprints as descri bed in [BIB_ISO_19794_FINGER][5] . The requirements according to the certification requirements of [BIB_ISO_19794_FINGER] SHALL be met. In particular the resolution of the fingerprint scanner SHALL ful fill the requirements for acquisition setting levels 31 and 41 of [BIB_ISO_19794_FINGER]. 

- 5 The ISO/IEC 39794 series might be relevant here. 

Federal Office for Information Security 

53 

4 Function Modules 

- For the acquisition process, a pre-qualification of the fingerprints to prefer high quality SHALL be used. The activation of the acquisition SHALL occur automatically. The capture SHOULD prefer the highest quality image of a sequence. 

- This functionality MAY be part of the hardware firmware and MAY NOT be available as separate software component. 

- The thresholds of the pre-qualification for performing a capture SHALL be documented by the vendor. 

- If the acquisition software allows multiple thresholds for pre-qualification, it SHALL be configurable by the system administrator. 

- In case further requirements demand for an export of the uncompressed fingerprint image data BMP SHALL be used as image format. 

## 4.2.4.2 Recommendations 

In order to prevent unwanted duplicate acquisitions of the same fingers or slaps, the software SHOULD start the acquisition process not before the fingers from a previous acquisition have been removed from the sensor surface. 

## 4.2.5 FM AS-FP-SF 

This Function Module describes the requirements and interfaces for acquisition software for single finger scanners. 

## 4.2.5.1 Requirements 

- The image provided by acquisition software SHALL meet the criteria of fingerprints as descri bed in [BIB_ISO_19794_FINGER][6] . The requirements according to the certification requirements of [BIB_ISO_19794_FINGER] SHALL be met. 

- For the acquisition process, a pre-qualification of the fingerprints to prefer high quality SHALL be used. The activation of the acquisition SHALL occur automatically. The capture SHOULD prefer the highest quality image of a sequence. This functionality MAY be part of the hardware firmware and MAY NOT be available as separate software component. 

- The thresholds of the pre-qualification for performing a capture SHALL be documented by the vendor. 

- If the acquisition software allows multiple thresholds for pre-qualification, it SHALL be configurable by the system administrator. 

- In case further requirements demand for an export of the uncompressed fingerprint image data BMP SHALL be used as image format. 

## 4.2.5.2 Recommendations 

In order to prevent unwanted duplicate acquisitions of the same finger, the software SHOULD start the ac quisition process not before the finger from a previous acquisition has been removed from the sensor surface. 

## 4.2.6 FM AS-FP-SLP 

This Function Module describes the requirements and interfaces for acquisition software for four finger slap scanners running in slap acquisition mode. 

## 4.2.6.1 Requirements 

- It SHALL be classified by software whether the left or right hand slap has been acquired. Thumb slap clas sification is NOT REQUIRED. This MAY be achieved by using the acquired fingerprint images or with the help of further sensors or images (e.g. surveillance) if available. Direct hardware-based detection MAY also be used, as long as the results are logged. 

> 6 The ISO/IEC 39794 series might be relevant here. 

Federal Office for Information Security 

54 

4 Function Modules 

- The classification SHALL have a performance of at least 99% i.e. 99% of all left hand slaps SHALL be correctly classified as left hand slaps and 99% of all right hand slaps SHALL be correctly classified as right hand slaps. 

- In case the classification can return more than two possible results, e.g. "left", "right", or "unknown", a clas sification threshold SHALL be configurable. 

- It SHALL be configurable to switch the classification off or to only use the classification result information for evaluation purposes. 

## 4.3 FM Category Biometric Image Processing 

The Function Module Biometric Image Processing (BIP) provides the extraction of all relevant biometric in formation from the data which is provided by the acquisition hardware or the acquisition software layer. Thus, a proprietary data block is transformed to a digital image of a biometric characteristic. In general, specific image processing for biometric characteristics is addressed here. 

## 4.3.1 FM BIP-FI-APP 

This Function Module describes requirements and interfaces for biometric image processing with respect to the output of (integrated) camera systems to obtain a facial image that fulfils the requirements. 

## 4.3.1.1 Requirements 

- The colour depth SHALL be 24 bit sRGB. Note, this requirement is OPTIONAL for scenarios where only a facial verification is performed. 

- The face SHALL be fully visible in the foreground of the provided image. 

- The minimum distance between both eyes for capture positions of the biometric subject in the preferred area of the camera range SHALL be 120 pixels. 

- The face SHALL be cropped and de-rotated from the overall scene in the captured image. Post processing of the image orientation in regard to pitch and jaw (see [BIB_ISO_19794_FACE][7] ) SHALL NOT be done. 

- The size of the face within the image SHALL be according to the geometric requirements of [BIB_ISO_19794_FACE] and QA category of this TR. 

## 4.3.2 FM BIP-FP-APP 

This Function Module describes requirements and interfaces for the biometric image processing to provide up to four single finger images for the subsequent reference storage or biometric comparison. 

## 4.3.2.1 Requirements 

- The resolution of the fingerprint image has to be 500 ppi or 1000 ppi corresponding to the certification requirements of [BIB_ISO_19794_FINGER][8] and, therefore, MAY differ from the scan resolution. 

- Depending on the call, as many individual fingerprints as requested SHALL be extracted from the input image and provided as single fingerprints. 

Note: Segmentation for single finger scanners is OPTIONAL. 

For this segmentation process, the following requirements SHALL be fulfilled: 

   - ability to accept fingerprints which are rotated in the same direction up to 45 degrees 

   - in the same direction rotated fingerprints have to be corrected to be vertical 

   - segment the first part over the finger (fingertip) 

   - segmentation has to occur on uncompressed data 

- 7 The ISO/IEC 39794 series might be relevant here. 8 The ISO/IEC 39794 series might be relevant here. 

Federal Office for Information Security 

55 

4 Function Modules 

- Fingerprint images SHALL NOT be upscaled. If the targeted system or database requires fingerprint images of higher size than captured the fingerprint image SHALL be evenly surrounded with white pixels to reach the desired size. 

## 4.4 FM Category Quality Assessment 

The Function Module Quality Assessment contains all kinds of mechanisms and procedures to check the qua lity of the biometric data or to select the best quality data out of multiple instances. 

## 4.4.1 FM QA-FI-GENERIC 

This Function Module describes requirements and interfaces for software that is used for quality assessment of digital images to ensure compliance with [BIB_ISO_19794_FACE][9] . 

## 4.4.1.1 Requirements 

## 4.4.1.1.1 General Requirements 

The QA module is used for the software-based automatic check of the conformance of the picture to [BIB_ISO_19794_FACE] after the digitisation. Thereby, the geometric properties of the picture as well as the digital parameters of the image are analysed and rated. 

The standard which is relevant for the quality of facial images [BIB_ISO_19794_FACE] hierarchically describes requirements for the facial images. In the following, full frontal images are expected. 

The QA module SHALL analyse and evaluate all of the quality components listed in Table 4.2. For the com ponents marked with "M", the quality values SHALL be provided while quality values for the components marked with "O" MAY be provided in the defined format according to the respective components. 

A component is fulfilled if its calculated value is in the given threshold boundaries. 

Based on the results of all provided quality components the QA module SHALL reject or approve the picture. The total result is true if every single quality component is fulfilled. 

The QA module SHALL provide an interface for conformance testing where a single image can be processed and the calculated values and configuration data are returned. The image type to process depends on the image type requirements of the application profile to implement. 

The QA module SHOULD operate on cropped images retrieved from the image processing according to FM Category Biometric Image Processing. 

|**ID**|**Component**|**ISO-Ref., compare**<br>**[BIB_ISO_19794_FACE]**|**Mandatory / Optional**|**Unit/Range**|
|---|---|---|---|---|
|Pose of the head|||||
|1.1|Yaw, neck axis|7.2.2|O|Degrees|
|1.2|Pitch, ear axis|7.2.2|O|Degrees|
|1.3|Roll, nose axis|7.2.2|M|Degrees|
|Facial|expression||||
|2.1|Neutral expression|7.2.3|O|Arbitrary units|
|2.2|Mouth closed|7.2.3|M|Arbitrary units|
|2.3|No raised eyebrows|7.2.3|O|Arbitrary units|
|Eyes|||||
|3.1|Eyes open|7.2.3|O|Arbitrary units|
|3.2|No occlusion (glasses,<br>hair, eye patch)|7.2.11 7.2.12|O|Arbitrary units|



> 9 The ISO/IEC 39794 series might be relevant here. 

Federal Office for Information Security 

56 

4 Function Modules 

|**ID**|**Component**|**ISO-Ref., compare**<br>**[BIB_ISO_19794_FACE]**|**Mandatory / Optional**|**Unit/Range**|
|---|---|---|---|---|
|3.3|Eyes looking to the ca<br>mera|7.2.3|O|Arbitrary units|
|Background|||||
|4.1|Uniformity (plainness,<br>no textures, colour)|7.2.6 A.2.4.3|O|Arbitrary units|
|4.2|No shadows|7.2.6 A.2.4.2|O|Arbitrary units|
|4.3|No further people / ob<br>jects|7.2.4 A2.3|O|Arbitrary units|
|Geometry|||||
|5.1|Image height|8.3.5 A.3.1.1 A.3.2.1|M|In pixel|
|5.2|Image width|8.3.4 A.3.1.1 A.3.2.1|M|In pixel|
|5.3|Ratio: Head width /<br>image width|8.3.4|M|As ratio between 0 and 1|
|5.4|Ratio: Head height /<br>image height|8.3.5|M|As ratio between 0 and 1|
|5.5|Vertical position of the<br>face|8.3.3|M|As ratio between 0 and 1|
|5.6|Horizontally centred<br>face|8.3.2|M|As ratio between 0 and 1|
|5.7|Eye distance|8.4.1 A3.1.1|M|In pixel|
|Subject lighting|||||
|6.1|Equally distributed<br>lighting|7.2.7|O|Arbitrary units|
|6.2|No shadows over the<br>face nor in the eye-so<br>ckets|7.2.8 7.2.9|O|Arbitrary units|
|6.3|No hot spots on skin|7.2.10|O|Arbitrary units|
|6.4|No effects on glasses|7.2.11|O|Arbitrary units|
|Photographic requirements|||||
|7.1|Proper exposure|7.3.2|M|Arbitrary units|
|7.2|Focus and depth of field|7.3.3|M|Arbitrary units|
|7.3|No unnatural colours|7.3.4|O|Arbitrary units|
|7.4|No red eyes|7.3.4|O|Arbitrary units|
|7.5|Colour space|7.4.2.3|M|According to<br>[BIB_ISO_19794_FACE] using<br>Decimal notation (e.g. "1" for<br>RGB-24bit, "2" for YUV422 or<br>"3" for 8bit-grey scale and "0"<br>for_unknown_or errors)|
|7.6|Grey scale density and<br>colour saturation|7.4.2.1 7.4.2.2|M|Counted numbers of intensi<br>ty values existing within the<br>image|



**Table 4.2** Mapping of Relevant Quality Components 

Federal Office for Information Security 

57 

4 Function Modules 

## 4.4.1.1.2 Identification of the Best Capture 

When multiple facial images and their corresponding set of quality metrics are present, the best capture of the list SHALL be identified in an automated manner as described in the following[10] : 

1. If exactly one facial image conforms to more mandatory components than all other images, this image is chosen. 

2. If more than one facial image is conform to more mandatory components than all other facial images, the facial image fulfilling the most optional components SHALL be chosen. 

3. If more than one facial image is conform to more mandatory and optional components than all other facial images, the most recent facial image within this selection SHALL be chosen. If no timestamp is available, a random selection MAY be applied among the facial images fulfilling the most components. 

## 4.4.2 FM QA-FI-BCL 

This Function Module describes requirements and interfaces for software that is used for quality assessment of digital images within the context of border control to ensure compliance with [BIB_ISO_19794_FACE][11] . 

## 4.4.2.1 Requirements 

The threshold requirements of Table 4.3 SHALL be in place within the context of border control. These thres holds relate to the generic quality components of FM QA-FI-GENERIC. 

|**ID**|**Component**|**Minimum**|**Maximum**|**Unit/Range**|
|---|---|---|---|---|
|1.1|Yaw, neck axis|-5|5|Degrees|
|1.2|Pitch, ear axis|-5|5|Degrees|
|1.3|Roll, nose axis|-8|8|Degrees|
|5.1|Image height|800|1600|In pixel|
|5.2|Image width|600|1200|In pixel|
|5.3|Ratio: Head width / image width|0,5|0,75|As ratio between 0 and 1|
|5.4|Ratio: Head height / image height|0,6|0,9|As ratio between 0 and 1|
|5.5|Vertical position of the face|0,3|0,5|As ratio between 0 and 1|
|5.6|Horizontally centred face|0,45|0,55|As ratio between 0 and 1|
|5.7|Eye distance|120|-|In pixel|



**Table 4.3** Quality Threshold Requirements for Facial Images for Border Control 

## 4.4.3 FM QA-FI-PRE 

This Function Module describes quality requirements for a digital live facial image that is used for automated face recognition (pre-qualification). 

## 4.4.3.1 Requirements 

- Pre-qualification of captured live facial images from the acquisition stream SHALL be used. Images SHALL be ranked according to the conducted pre-qualification and passed to the subsequent stage as indicated by the rank. 

- Pre-qualification SHALL be conducted at least according to the following components, refer to [BIB_ISO_19794_FACE][12] : 

   - pose of the head 

- 10 Note that this is a description of the automated selection of the best capture among a list of facial images. Operators may always decide otherwise during the process (veto). 

- 11 The ISO/IEC 39794 series might be relevant here. 

- 12 

- The ISO/IEC 39794 series might be relevant here. 

Federal Office for Information Security 

58 

4 Function Modules 

   - illumination of the face 

   - position of the eyes 

- The pre-qualification result SHALL depend only on the provided live-captured facial image. In particular, the pre-qualification SHALL be independet of any other biometric sample that might be extracted from other sources, e.g. eMRTD, etc. 

## 4.4.4 FM QA-FP-APP 

This Function Module describes requirements for the quality assessment of plain or rolled fingerprints inclu ding quality assessment of single fingerprint, respectively slap and selection of the best quality image out of multiple instances. 

## 4.4.4.1 Requirements 

## 4.4.4.1.1 Quality Algorithm 

As quality algorithm, the latest version of NIST Fingerprint Image Quality 2.2 (NFIQ2.2) [BIB_NFIQ2.2] SHALL be used, and therefore, images with 1000 ppi SHALL be resampled to 500 ppi before application of NFIQ2.2. Note, that the resampled image SHALL be used for NFIQ2.2 only. As resulting quality value, the output value of NFIQ2.2 in the integer range of [0,100] SHALL be used. In the case of failure, the returned error code 255 indicates that a computation was not successful and the resulting quality value SHALL be returned as the result, as described in Section 4.11.1. 

## 4.4.4.1.2 Quality Evaluation Process for a Slap or Single Fingerprint 

In case a single captured fingerprint, respectively slap is passed, the QA SHALL be performed as described in the following. Beforehand, the fingerprints of the passed capture SHALL be segmented (considering missing fingers). Note, that in verification applications, a QA is not conducted. Thus, every slap capture is considered sufficient and no thresholds are specified here. Skipping the QA is expected to accelerate the overall process. OPTIONALLY, a QA can be performed. 

1. For each segmented fingerprint _FA;j_ of a passed capture _A_ , a quality value _QA;j_ is calculated with _j 2_ 1 _; :::;_ 10 (up to 4 fingers in one slap) representing the specific finger code according to [BIB_ISO_19794_FINGER][13] . 

2. The resulting quality value is compared with the defined threshold _THj_ for this finger. The application specific thresholds as defined in the following section apply. 

3. In case all of the fingerprint qualities reach the specified threshold (i.e. _8j; QA;j ¸ THj_ ), the Boolean infor mation _b_ = 1 indicates a successful capture. 

4. In case one or more fingerprints do not reach the threshold (i.e. _9j; QA;j < THj_ ), the Boolean information _b_ = 0 indicates insufficient quality of the capture. 

5. For the segmented fingerprint _FA;j_ the corresponding parameter set _PA;j_ is compiled and returned. 

6. As a result of the QA process, the following values are returned to the calling process: 

   - a. the Boolean information _b_ 

   - b. the parameter set _PA_ = _QA;j; :::; QA;l_ with _j; l 2_ 1 _; :::;_ 10 representing the specific finger code 

## 4.4.4.1.3 Identification of the Best Capture out of Multiple Captures 

When multiple captures _Ai; i 2_ 1 _; :::; n_ and their corresponding set of segmented fingerprints _FAi;j_ with _j 2_ 1 _; :::;_ 10 representing the specific finger code according to [BIB_ISO_19794_FINGER][14] are passed, the best of the captures SHALL be identified as described in the following section: 

1. For each segmented fingerprint _FAi;j_ of a passed capture _Ai_ , the quality value _QAi;j_ is calculated with re presenting the specific finger code according to [BIB_ISO_19794_FINGER]. 

- 13 The ISO/IEC 39794 series might be relevant here. 14 The ISO/IEC 39794 series might be relevant here. 

Federal Office for Information Security 

59 

4 Function Modules 

2. The captures are ranked according to the quality values of the fingerprints according to the following (lexicographical) order. The highest ranked capture is considered as the capture yielding the best quality. 

   - a. for left/right four-finger slaps, the order is as follows: 

      - i. index finger (highest priority) 

      - ii. middle finger 

      - iii. ring finger 

      - iv. little finger (lowest priority) 

Example 1: Two Slaps of a right hand. Middle finger, ring finger and little finger of the first slap have a better quality than the middle finger, ring finger and little finger of the second slap, but the quality of the index finger is better in the second slap. Consequently, the second slap SHALL be taken. 

Example 2: Three Slaps of a left hand. The quality of the index finger and the middle finger is the same in all three slaps, but the quality of the ring finger is better in the first slap. So the first slap SHALL be taken, no matter how high or low the quality of the little finger is in any slap. 

- b. for thumb slaps, the order is as follows: 

   - i. right thumb (highest priority) 

   - ii. left thumb (lowest priority) 

- c. for index finger slaps: 

   - i. In contrast to the other two slap types, the best capture of index finger slaps is a set of the best captures of each index finger as indicated by the following two options. 

If each index finger yields sufficient quality in at least one of the already conducted captures, the index fingers of sufficient quality are accepted and the total index finger slap capture is considered as of sufficient quality. 

If not both index fingers yield at least once sufficient quality in a capture, the best image for each index finger is returned as the best capture and the slap captured is considered as of insufficient quality. 

      - ii. If for a single slap both index fingers yield to sufficient quality, those two index fingers SHALL be selected even if an index finger of another slap yield to better quality. 

   - d. for rolled single finger captures: 

      - i. Of the set of captured images obtained in the process beforehand, which are not annotated by a hardware reported issue, the capture with the highest quality value is considered as the best image. 

      - ii. If the set of captured images obtained in the process beforehand on does only contain images which are annotated by hardware reported issues, the capture with the highest quality value of the entire set is considered as the best image. 

      - iii. In case several captures yield to the same highest quality value, the last (temporal) of highest quality captures is considered as the best image. 

3. As a result of the QA process, the following values are returned: 

   - a. the identifier _i_ representing the capture yielding the best quality 

   - b. the parameter set _PA_ = _QAi;j; QAi;l_ with _j; l 2_ 1 _; :::_ 10. 

## 4.4.4.1.4 Thresholds for Plain Fingerprints for Enrolment Purposes 

The following thresholds as indicated in Table 4.4 apply when fingerprints are captured plain for enrolment purposes. Note, the thresholds in Table 4.4 do not apply to plain captured fingerprint in enrolment scenarios where the plain fingerprints are captured for control purpose of rolled fingerprints. In that case, thresholds as indicated in Table 4.5 apply for the plain fingerprints. 

Federal Office for Information Security 

60 

4 Function Modules 

|**Finger Position**|**Finger Code**|**NFIQ2.2 Threshold**|
|---|---|---|
|Right thumb|1|30|
|Right index finger|2|30|
|Right middle finger|3|20|
|Right ring finger|4|10|
|Right little finger|5|10|
|Left thumb|6|30|
|Left index finger|7|30|
|Left middle finger|8|20|
|Left ring finger|9|10|
|Left little finger|10|10|



**Table 4.4** Thresholds for Plain Fingerprints for Enrolment Purposes 

## 4.4.4.1.5 Thresholds for Plain Control Fingerprints and Fingerprints used for Identification Searches 

The following thresholds as indicated in Table 4.5 apply when fingerprints are captured plain for the purpose of control slaps (used for comparison with rolled prints) or for use in identification searches. Note, the thres holds in Table 4.5 do apply to plain captured fingerprint in enrolment scenarios where the plain fingerprints are captured for control purpose of rolled fingerprints. 

|**Finger Position**|**Finger Code**|**NFIQ2.2 Threshold**|
|---|---|---|
|Right thumb|1|20|
|Right index finger|2|20|
|Right middle finger|3|20|
|Right ring finger|4|10|
|Right little finger|5|10|
|Left thumb|6|20|
|Left index finger|7|20|
|Left middle finger|8|20|
|Left ring finger|9|10|
|Left little finger|10|10|



**Table 4.5** Thresholds for Plain Control /Identification Fingerprints 

## 4.4.4.1.6 Thresholds for Rolled Fingerprints 

The following thresholds as indicated in Table 4.6 apply when fingerprints are captured rolled for enrolment purposes. 

|**Finger Position**|**Finger Code**|**NFIQ2.2 Threshold**|
|---|---|---|
|Right thumb|1|20|
|Right index finger|2|15|
|Right middle finger|3|15|
|Right ring finger|4|10|
|Right little finger|5|5|
|Left thumb|6|20|
|Left index finger|7|15|



Federal Office for Information Security 

61 

4 Function Modules 

|**Finger Position**|**Finger Code**|**NFIQ2.2 Threshold**|
|---|---|---|
|Left middle finger|8|15|
|Left ring finger|9|10|
|Left little finger|10|5|



**Table 4.6** Thresholds for Rolled Fingerprints 

## 4.5 FM Category Presentation Attack Detection 

The objective of the Function Module Presentation Attack Detection is to avoid presentations with the goal to subvert an enrolment, verification of identification process. 

## 4.5.1 FM PAD-FI-APP 

This Function Module describes requirements for PAD in the context of the acquisition of facial images. This Function Module is especially relevant for use cases where no direct observation of the acquisition process by an operator is possible (e.g. in SSS scenarios). 

## 4.5.1.1 Requirements 

## 4.5.1.1.1 General Requirements 

The capture subsystem SHALL contain a PAD subsystem detecting spoofing attempts using artefacts by which an attacker is trying to establish a different biometric characteristic as biometric sample in the enrolment, verification or identification process. 

The PAD subsystem MAY consist of hardware and software (e.g. the used camera system MAY have additional sensors designed for this purpose). 

The PAD subsystem SHALL be able to detect different artefact classes listed in the following: 

- Complete artefacts (covering the whole or nearly the whole face of the attacker), either built from one piece or from multiple pieces. 

- Partial artefacts (covering only parts of the attacker's face, such as artefacts covering the chin only), either built from one piece or from multiple pieces. 

The PAD subsystem SHALL be able to detect all well-known artefact material types listed in the following: 

- Photographs printed on paper with different thicknesses and structures of paper and different structures of printing (colouring, etc.). 

- Photographs displayed on electronic devices (e.g. phones, tablets, laptops, etc.) where different methods of displaying might be used. 

- Videos displayed on electronic devices, especially showing motion of the biometric subject. 

- Photographs printed on fabrics with different thicknesses and structures of the fabrics and different me thods of printing (flock print, silk screening, etc.). 

- 3D masks in big (size of a face) and small (smaller than a normal face) sizes and different thicknesses based on, 

   - Paper 

   - Casted silicon 

   - 3D-printer 

   - Latex 

On top of the listed attack classes and materials, additional attack classes MAY be detected by the PAD sub system: 

- Makeup (normal or professional) 

- Additional artefacts beyond the imitation of faces, such as glasses etc. 

Federal Office for Information Security 

62 

4 Function Modules 

Under optimal testing conditions, the PAD subsystem SHALL feature a false-alarm-rate of 2% maximum when tested with bona fide biometric subjects. This rate is monitored via logfiles analysis within the operational environment. If this rate is significantly exceeded, any certification that may have been issued might be reevaluated (depending on application context)[15] . 

Also, the detection subsystem SHALL be adequate to the usage setting in correspondence with the security requirements in question. The performance MAY be described by a risk analysis for every considered attack type. The current version of [BIB_ISO_PAD_3] SHALL be taken into account. 

## 4.5.1.1.2 Integration Requirements 

The PAD subsystem SHALL be independent of the regular capture subsystem, i.e. it SHALL NOT inhibit captu ring image data in case of a suspected attack. It SHALL signal its detection results in the form of a PAD score to the calling application. The score SHALL be a normalized `double` in the range [0,1] using at least ten uniformly distributed interim values, where 0 indicates bona fide and 1 presentation attack. A binary score SHALL NOT be used (e.g. True or False, 1 or 0). Detailed information about the PAD (results) SHALL be logged as described in Section 4.12. The technical information including the result value and description of the mapping between technical result and interpretation SHALL be stored additionally, if they are provided. 

Even if the Function Module is used within a comparison scenario, the detection result SHALL be signalled in any case, independent from any biometric comparison score. Also, the omission of the detection result SHALL be signalled in any case. 

The PAD result SHALL correspond to the chosen facial image. 

Note that a facial image SHALL be taken independently of a possible PAD alarm. 

## 4.5.1.1.3 Maintenance Requirements 

As new technologies and new attack mechanisms are developed over time, the PAD subsystem SHALL be regularly updated and re-evaluated. 

## 4.5.1.1.4 Certification Requirements 

To ensure comparable performance of presentation attack detection subsystems, the system SHALL be certi fied 

- either under the Common Criteria Agreement according to the Protection Profile "BSI-CC-PP-0118-2022: Common Criteria Protection Profile - Biometric Mechanisms Protection Profile (BMPP), Version 2.0, base PP and at least the functional package PAD" 

- or according to BSI TR-03122: Conformance Test Specification for Technical Guideline TR-03121 - Bio metrics for Public Sector Applications, respectively this technical guideline. 

## 4.5.2 FM PAD-FP-APP1 

This Function Module describes requirements for PAD in the context of the acquisition of biometric charac teristics of fingerprints. 

## 4.5.2.1 Requirements 

## 4.5.2.1.1 General Requirements 

The capture system SHALL contain a PAD subsystem according to [BIB_ISO_PAD_1] detecting spoofing at tempts using artefacts by which an attacker is trying to establish a different biometric characteristic as probe in the verification or identification process. 

The PAD subsystem MAY consist of hardware and software (e.g. the used fingerprint scanner MAY have addi tional sensors designed for this purpose). 

According to the used fingerprint scanner, PAD subsystem SHALL be able to detect artefact classes listed in the following: 

- 15 Note that during certification a relaxed false-alarm-rate is tested. The requirement of the rate specified in this Function Module is tested on operational collected data only. 

Federal Office for Information Security 

63 

4 Function Modules 

- Fingertips, created in different thicknesses 

- Single fingers (massive) 

The PAD subsystem SHALL be able to detect all typical artefact material types listed in the following: 

- Artefacts created from different kinds of silicon 

- Artefacts created from different kinds of latex 

- Artefacts created from different kinds of gelatine 

- Artefacts created from different kinds of wood glue 

- Artefacts created from different kinds of window painting 

- Artefacts created from different kinds of paper 

each in different colourings. 

Under optimal testing conditions, the PAD subsystem SHALL feature a false-alarm-rate of 2% maximum when tested with bona fide biometric subjects with generally good quality fingerprints. This rate is monitored via logfiles analysis within the operational environment. If this rate is significantly exceeded, any certification that may have been issued might be re-evaluated (depending on application context)[16] . 

Also, the detection subsystem SHALL be adequate to the usage setting in correspondence with the security requirements in question. The performance MAY be described by a risk analysis for every considered attack type. The current version of [BIB_ISO_PAD_3] SHALL be taken into account. 

The PAD SHALL be conducted both in supervised acquisition scenarios, e.g. in a counter scenario, and in un supervised acquisition scenarios, e.g. in SSS scenarios. Thereby, the PAD SHALL be conducted for all acquisi tion purposes, e.g. enrolment, identification and verification. 

## 4.5.2.1.2 Integration Requirements 

The PAD subsystem SHALL be independent of the regular capture subsystem. 

It SHALL signal its detection results in the form of a PAD score for each finger individually. Additionally, an overall result SHALL be returned to the calling application. 

The score for each finger SHALL be a normalized as `double` in the range [0,1] using at least ten uniformly distributed interim values, where 0 indicates bona fide and 1 presentation attack. A binary score SHALL NOT be used (e.g. True or False, 1 or 0). The PAD subsystem SHALL additionally provide detailed information about the scores of the PAD. 

The overall result SHALL be a Boolean value (e.g. True or False). The value SHALL be true, if any of the fingers individual result triggers a PAD alarm. 

Even if the Function Module is used within a comparison scenario, the detection result SHALL be signalled in any case, independent from any biometric comparison score. Also, the omission of the detection result SHALL be signalled in any case. 

The PAD result SHALL correspond to the respective finger capture attempt. 

Note, that an image of the fingerprint or slap in question SHALL be acquired independently of a possible PAD alarm. 

## 4.5.2.1.3 Maintenance Requirements 

As new technologies and new attack mechanisms are developed over time, the PAD subsystem SHALL be updated and checked whenever necessary, so it stays capable against old and new attacks and attack types. 

## 4.5.2.1.4 Certification Requirements 

To ensure comparable performance of presentation attack detection subsystems, the system SHALL be certi fied either under the Common Criteria Agreement according to one of following Protection Profiles: 

- 16 Note that during certification a relaxed false-alarm-rate is tested. The requirement of the rate specified in this Function Module is tested on operational collected data only. 

Federal Office for Information Security 

64 

4 Function Modules 

- BSI-CC-PP-0063-2010: Fingerprint Spoof Detection Protection Profile (FSDPP) 

- BSI-CC-PP-0062-2010: Fingerprint Spoof Detection Protection Profile based on Organisational Security Policies (FSDPP_OSP) 

- BSI-CC-PP-0118-2022: Common Criteria Protection Profile - Biometric Mechanisms Protection Profile (BMPP), Version 2.0, base PP and at least the functional package PAD 

or according to BSI TR-03122: Conformance Test Specification for Technical Guideline TR-03121 - Biometrics for Public Sector Applications, respectively this technical guideline. Note that the PAD certification according to BSI TR-03122 is preliminary and still subject to amendments. Anticipating certification under this Function Modul MAY only be realised with the permission of the Federal Ministry of the Interior and Community and upon consultation with the Federal Office for Information Security. 

## 4.6 FM Category Compression 

The objective of the Function Module Compression (COM) is to keep the biometric data within a feasible size without losing too much quality for a biometric verification or identification. 

## 4.6.1 FM COM-CCTV-JPG 

This Function Module describes requirements and interfaces for the compression of surveillance images. 

## 4.6.1.1 Requirements 

- The compression method for surveillance images SHALL be JPEG (compare [BIB_ISO_10918-1]). Multiple lossy compressions SHALL NOT take place. 

- The compression ratio SHALL be configurable. 

- The image resolution SHALL be at least 1280 x 720 pixels. 

## 4.6.2 FM COM-FI-GENERIC 

The following requirements are generic and apply to all Function Modules (FMs) regarding compression of facial images. 

## 4.6.2.1 Requirements 

Multiple lossy compressions of the facial image data SHALL NOT take place with the exception of the initial capture by a digital camera whenever that camera does not support uncompressed image capture. 

## 4.6.3 FM COM-FI-BCL 

This Function Module describes requirements and interfaces for the compression of live images used within the context of border control. 

## 4.6.3.1 Requirements 

## 4.6.3.1.1 General Requirements 

For conformance testing the software component encapsulating the compression SHALL provide an interface that accepts predefined test data instead of performing the regular process. 

## 4.6.3.2 Compression Requirements 

|**Property**|**Value**|
|---|---|
|Compression method (Image format)|JPEG 2000 (compare [BIB_ISO_15444]) or JPEG (compare|
||[BIB_ISO_10918-1])|
|Multiple lossy compressions|not allowed|
|Maximum compression ratio|20:1|
|Minimum file size|-|



Federal Office for Information Security 

65 

4 Function Modules 

|**Property**|**Value**|
|---|---|
|Maximum file size|375 kB|



**Table 4.7** Compression Requirements for Facial Images for Border Control 

## 4.6.4 FM COM-FP-BCL 

This Function Module describes requirements and interfaces for the compression of fingerprint images con tained in [BIB_ANSI_NIST_2011:2015] files within the context of border control. 

## 4.6.4.1 Requirements 

The NIST file size after compression SHALL have a maximum file size of 5332 kB for EES purposes (base64 encoded). The equivalent binary file SHAll have a maximum size of 3999 kB. [BIB_EES_ICD] 

The NIST file size after compression SHALL have a maximum file size of 3000 kB for Schengen Information System (SIS) purposes. 

## 4.6.5 FM COM-FP-WSQ 

This Function Module describes requirements and interfaces for the compression of fingerprint images by Wavelet Scalar Quantisation (WSQ) method. 

## 4.6.5.1 Requirements 

WSQ SHALL be used as compression method for fingerprint images. A bit rate of 0.75 SHALL be used as compression parameter. This is equivalent to a compression factor of approximately 15:1[17] (according to [BIB_ISO_19794_FINGER][18] ). The implementation of the used WSQ algorithm SHALL be certified by the FBI and SHALL be referenced by the respective certificate number (coded in the WSQ header). The certified WSQ implementation SHALL be version 3.1 and SHALL base on NBIS Version 5.0. Multiple lossy compressions SHALL NOT take place. 

## 4.7 FM Category Operation 

Within the Function Module Operation (O), the working process is specified for the respective operator. All steps that have to be executed are described sequentially and in more detail. This also includes descriptions of how to proceed in error cases. 

## 4.7.1 FM O-ALL-LNK 

This Function Module describes requirements to be observed by the operator who handles the identification process. 

## 4.7.1.1 Requirements 

## 4.7.1.1.1 Organisational Requirements 

- The operator SHALL determine whether the identification was positive by means of manually assessing the returned candidate list. 

- If multiple identities of the biometric subject are revealed by the identification, the operator SHALL assure the identities are linked in the Automated Biometric Identification System (ABIS) for deduplication pur pose. 

## 4.7.2 FM O-ALL-USV 

This Function Module describes requirements to be observed by the responsible operator of the unsupervised acquisition process of biometric characteristics. 

- 17 For estimation of compression factor it is allowed to crop to the minimum size containing the fingerprint defined if a sensor is used with a larger capturing area than this minimum. 

- 18 The ISO/IEC 39794 series might be relevant here. 

Federal Office for Information Security 

66 

4 Function Modules 

## 4.7.2.1 Requirements 

## 4.7.2.1.1 General Organisational Requirements 

During operating hours the device SHALL be (potentially) visible to an authority employee. Curtains, doors or similar SHALL NOT be used during operating hours. The installation in the visible area is intended to prevent manipulation of the device, as well as vandalism. Note that this requirement does not necessitate that an aut hority employee watches the device permanently. 

## 4.7.2.1.2 Additional Organisational Requirements within the application context German Identity Documents (GID) 

For devices which are subject to the TR volume German Identity Documents the following requirements apply additionally: 

The device SHALL be set up in such a way that the capture process can be permanently observed by an official during opening hours. The installation in the observable area is intended to prevent counterfeits and misuse of the device. Note, the usage of monitoring technology (exclusively) is not sufficient to fulfil this requirement. 

The delivery of the device SHALL be accompanied by product documentation that has to indicate the condi tions for installation in the authorities. 

The device SHALL NOT have side panels. The device SHALL NOT prevent the biometric subject from entering the capture area from either side. 

For devices which use a physical back panel the following requirements apply additionally: 

The frontal obstruction angle beta1 at the nasion of the biometric subject looking at the device SHALL NOT exceed 45°. The biometric subject is positioned as close as possible to the camera unit so that an image com pliant with the components of FM QA-FI-GID can still be captured. The frontal obstruction angle is calcula ted using the outermost edges of the device in the area 20 cm below and above the height of the "Frankfurt Horizon" of a biometric subject which has a body height in the range of 140 cm to 200 cm. The "Frankfurt Horizon" is a plane which is uniquely defined for each biometric subject by the following three points: the inferior margin of the left orbit and the superior margin of each ear canal. 

In a similar way the backward obstruction angle beta2 at the nasion of the biometric subject looking at the device SHALL NOT exceed 135°. The backward obstruction angle is calculated using the outermost edges of the back panel in the area 20 cm below and above the height of the "Frankfurt Horizon" of a biometric subject which has a body height in the range of 140 cm to 200 cm. 


![](markdown/tr/TR-03121-3_1_Biometrics_7_0/TR-03121-3_1_Biometrics_7_0.pdf-0075-12.png)


**Figure 4.1.** Example: In the sketch beta1 is lower than or equal 45° and beta2 is lower than or equal 135°. The structural observability is there fore given. 

Federal Office for Information Security 

67 

4 Function Modules 

## 4.7.2.2 Recommendations 

## 4.7.2.2.1 Organisational Recommendations within the application context Border Control (BCL) 

For devices which are subject to the TR volume Border Control the following requirement is recommended additionally: 

The operator SHOULD assure that only one person was in near distance of the biometric capture devices. The operator MAY be assisted in this requirement, e.g. by corresponding sensors. This is typically used in conjunc tion with additional video surveillance. 

## 4.7.3 FM O-FI-ALL 

This Function Module describes requirements to be observed by the operator who handles the facial image acquisition process. This includes the full working process. 

## 4.7.3.1 Requirements 

The operator SHALL be responsible for an adequate cleanliness of all capture hardware components. 

## 4.7.3.2 Recommendations 

OPTIONALLY, the operator can use the photo guideline. 

## 4.7.4 FM O-FI-DC 

This Function Module describes requirements to be observed by the operator who handles the facial image acquisition process with a digital camera. 

## 4.7.4.1 Requirements 

- The operator SHALL ensure that different environmental lighting conditions caused by direct or indirect sunlight and different seasons of the year SHALL NOT influence the proper and uniform lighting of the captured facial image. 

- Direct and cross irradiation of lighting SHALL be avoided by the operator. 

## 4.7.5 FM O-FP-ALL 

This Function Module describes requirements to be observed by the operator who handles the acquisition process of fingerprint images. 

## 4.7.5.1 Requirements 

## 4.7.5.1.1 Operation of Devices 

- The operator SHALL be responsible for an adequate cleanliness of all capture hardware components. Fin gerprint scanners SHALL be cleaned regularly to provide good probe images. 

- The fingerprint scanner SHALL be regularly calibrated (e.g. once a day), if the used fingerprint scanner tech nology requires such a calibration. The operator SHALL ensure that the sensor platen is clean before cali bration to reduce the risk of ghost images. 

## 4.7.5.1.2 Environmental Requirements 

- The operator SHALL ensure that different environmental lighting conditions caused by direct or indirect sunlight and different seasons of the year SHALL NOT influence the scanner capture process. 

- Direct and cross irradiation of lighting on the sensor platen SHALL be avoided completely. 

## 4.8 FM Category User Interface 

It is the task of the User Interface (UI) to display and visualise the respective information that is obtained from the underlying Function Modules. 

Federal Office for Information Security 

68 

4 Function Modules 

## 4.8.1 FM UI-FI-BSJ 

This Function Module describes requirements for the user interface of facial image acquisition shown to the biometric subject. 

## 4.8.1.1 Requirements 

If PAD was conducted: Neither the PAD result nor PAD score SHALL be displayed to the person whose facial image is acquired. In a supervised acquisition scenario the process operator MAY be responsible for screen po sitioning, so that the PAD result or the PAD score is not displayed to the person whose facial image is acquired. 

If the acquisition system is required to have a feedback screen for the facial image acquisition within a specific application context, or if the vendor decided to implement a feedback screen although it is OPTIONAL in the respective application context, the following requirements SHALL be fulfilled: 

- The acquisition system SHALL show a digital mirror or physical mirror image to the biometric subject to guide it for the correct positioning in front of the camera. 

- The acquisition system SHALL show user guidance information to help the biometric subject with the cor rect positioning in front of the camera when one of the following conditions is met: 

   - The biometric subject is too close to or too far away from the camera. 

   - The biometric subject is too far left or right to the camera. 

   - The biometric subject is too high or low and the camera is not able to compensate this with a vertical adjustment. 

   - The biometric subject is in too much movement. 

   - The biometric subject is not facing frontally to the camera. 

   - The eyes of the biometric subject are closed. 

   - The mouth of the biometric subject is opened. 

   - Multiple faces are detected in front of the camera. 

## 4.8.1.2 Recommendations 

- An indicator showing the capture status SHOULD be displayed to the biometric subject. 

- Graphics (e.g. buttons or pictograms) SHOULD use a uniform colour palette without utilizing clashing co lours. 

## 4.8.2 FM UI-FI-OP 

This Function Module describes requirements for the user interface of the software displaying the result of the quality assessment and verification (if performed) of facial images to the operator. 

## 4.8.2.1 Requirements 

- The current evaluated picture SHALL be displayed to the operator for the enrolment. 

- All components evaluated with the current value and threshold as well as their relation: OK/NOK for every component SHALL be displayed to the operator for the enrolment. 

- The summarised result OK/NOK for the current picture SHALL be displayed to the operator for the enrol ment. 

- The provision of the veto power for the operator SHALL be shown to the operator for the enrolment: 

   - enforcement of OK for obvious reasons (e.g. disability) 

   - enforcement of OK without obvious reasons 

   - enforcement of NOK to overrule software based quality assessment 

- If PAD has been performed and a presentation attack alarm has been raised, a warning with the overall result SHALL be displayed to the operator. All facial images within an acquisition where at least one facial 

Federal Office for Information Security 

69 

4 Function Modules 

image caused a PAD alarm SHALL be displayed to the operator. Those facial images for which a PAD alarm is present SHALL be highlighted (e.g. by a red frame). In cases where the execution of PAD is MANDATORY and no PAD result is available, the operator SHALL be informed of the missing PAD result. 

If verifications are performed[19] : 

- Visual feedback of the verification process SHALL be provided for the operator. At least both images (live and reference) and the (Boolean) result of the verification SHALL be displayed to the operator. 

- If the verification fails, then the operator SHALL get access to at least one complete and coherent set of biometric samples and verification results corresponding to a single verification attempt. For instance, in case of verification of a live-captured facial image against a facial image from chip (Data Group 2) and CIR, such a complete set would consist of the live-captured facial image, the facial image extracted from chip, the facial image stored in the CIR, and both corresponding verification results of the live-captured facial image against the facial image from chip and the CIR image. 

## 4.8.3 FM UI-FP-BSJ 

This Function Module describes requirements for the user interface of the biometric subject for fingerprint acquisitions. The user interface MAY be e.g. monitors, buttons, pictograms or status lights. 

## 4.8.3.1 Requirements 

The following requirements SHALL be met for the user interface: 

- An indicator showing the capture status and an indication when the capture process has finished SHALL be displayed to the biometric subject. The capture status SHALL include: Where to place the fingers, an indication of the scanning process and the feedback in case of mispositioning of fingers. 

- In an unsupervised scenario a visualisation which fingerprint or hand to place on the sensor SHALL be given, whereby in the case of a supervised scenario the visualisation MAY be given. 

If PAD was conducted: Neither the PAD result nor PAD score SHALL be displayed to the person whose finger prints are acquired. In a supervised acquisition scenario the process operator MAY be responsible for screen positioning, so that the PAD result or the PAD score is not displayed to the person whose fingerprints are acquired. 

## 4.8.3.2 Recommendations 

The following recommendations SHOULD be met for the user interface: 

- Graphics (e.g. buttons or pictograms) SHOULD use a uniform colour palette without utilizing clashing co lours. 

- The acquisition process SHOULD be displayed as real time feedback to the biometric subject (e.g. with the help of a feedback monitor). 

## 4.8.4 FM UI-FP-OP 

This Function Module describes requirements for the user interface of the software displaying the live feed back and results of the fingerprint acquisition, QA and control verification of fingerprint images to the ope rator. 

## 4.8.4.1 Requirements 

- The user interface SHALL signal which fingerprints are expected for the current slap or fingerprint acqui sition such that the operator can guide the biometric subject to place the correct fingers on the fingerprint scanner. 

- Visual feedback of the fingerprint acquisition at least displaying of the final images SHALL be provided to the operator. 

> 19 This is only the case if the application profile defines verification processes explicitly. 

Federal Office for Information Security 

70 

4 Function Modules 

- If a uniqueness check error occurs, the fingers involved in the unexpected successful comparisons SHALL be pictorially displayed to the operator and in case of a slap image, only the affected finger(s) SHALL be marked in the displayed image. In case a control verification was attempted and no successful comparison occurred during the control verification, a warning SHALL be displayed to the operator that the control verification was not successful. 

- The segmented single fingerprints SHALL be visualised to the operator to identify potential failures in seg mentation. This can be realised by displaying the result containing up to ten segmented single fingerprints. In case the amount of captured fingerprints mismatches with the amount of expected fingers a warning SHALL be displayed to the operator. 

- If a slap acquisition is in place and a slap classifier is in use (and activated not only for evaluation purpose), a warning SHALL be displayed to the operator when the classification result mismatches with the expected slap of the current acquisition. 

- If PAD has been performed and a presentation attack alarm has been raised, a warning SHALL be displayed to the operator and displayed for each finger individually. An overall result SHALL also be displayed addi tionally. In cases where the execution of PAD is MANDATORY and no PAD result is available, the operator SHALL be informed of the missing PAD result. 

- The indication of the quality level SHALL be displayed to the operator. 

- The provision of the veto power for the operator SHALL be shown to the operator for the enrolment: 

   - enforcement of OK for obvious reasons (e.g. disability) 

   - enforcement of OK without obvious reasons 

   - enforcement of NOK to overrule software based quality assessment 

## 4.8.4.2 Recommendations 

A live view from the fingerprint scanner SHOULD be displayed to the operator during the fingerprint acquisi tion. This also includes live information, e.g. about the correct positioning of fingers on the fingerprint scan ner or about the current quality level, that supports the operator guiding the biometric subject. 

The user interface SHOULD show a graphical representation of the fingerprints that are expected for the cur rent slap or fingerprint acquisition. 

## 4.8.5 FM UI-FP-VER 

This Function Module describes requirements for the user interface of the operator for verification of finger print images. 

## 4.8.5.1 Requirements 

Visual feedback of the verification process SHALL be provided for the operator. At least the (Boolean) result of the verification SHALL be displayed to the operator. 

## 4.8.5.2 Recommendations 

- A visualization which fingerprint / hand to place on the sensor SHOULD be displayed. 

- An indicator showing the capture status SHOULD be displayed to the biometric subject. 

- An indication when the capture process has finished or the capture process is to be retried. 

- Information about the successful or failed verification process SHOULD be displayed. 

- Graphics SHOULD avoid multiple colours or harsh contrast. 

## 4.9 FM Category Reference Storage 

The objective of the Function Module Reference Storage (REF) is to store biometric data in a way that it can be used for reference purposes later on. 

Federal Office for Information Security 

71 

4 Function Modules 

## 4.9.1 FM REF-FI-EES 

This Function Module describes requirements how facial images are stored as reference data in the EES. 

## 4.9.1.1 Requirements 

The acquired facial image data SHALL be stored in the CS EES if enrolment or update of facial images is re quired by the relevant use case. 

## 4.9.2 FM REF-FP-EES 

This Function Module describes requirements how fingerprint images are stored as reference data in the EES. 

## 4.9.2.1 Requirements 

The acquired fingerprint data SHALL be stored in the CS EES if enrolment or update of fingerprints is required by the relevant use case. 

## 4.10 FM Category Biometric Comparison 

The Function Module Biometric Comparison (CMP) encloses the mechanisms and algorithms to verify or identify an identity based on a 1:1 or 1: _n_ biometric comparison between reference data and a current biometric probe (usually a live presented image) regardless of where the reference is stored (e.g. passport, identity card, ABIS, database, ...). 

It is RECOMMENDED that the verifications conducted during uniqueness checks comply with this FM. 

## 4.10.1 FM CMP-FI-VER 

This Function Module contains requirements for the verification of an identity in relation to a stored reference facial image. 

## 4.10.1.1 Requirements 

## 4.10.1.1.1 Requirements on the Algorithm Performance 

The following requirements SHALL be met for a face verification algorithm: 

- The face verification algorithm SHALL be configured at a security level (threshold) guaranteeing an FMR of at most 0.1 % (1:1000) (0.01 %, 1:10,000 is RECOMMENDED ) in conjunction with an FNMR less than 2 %. 

- The threshold SHALL be configurable by the system administrator to allow for stricter settings when ne cessary. 

- Furthermore, the overall system has to be calibrated for the security level set within this specific scenario of verification. The vendor of the verification algorithm has to provide calibration data based on the actual verification performance. 

- The output of the algorithm SHALL be a comparison score[20] and the result of the verification (the achieved FMR and an indication whether the threshold has been reached) depending on the chosen security level (threshold) of the algorithm. 

To ensure the validity of proclaimed values, a vendor SHALL provide test results that support the designated claim. The following requirements apply to those test results: 

- The vendor SHALL provide a DET curve of the algorithm performance. 

- Such performance SHALL be on the basis of images of comparable characteristic (e.g. images in size and resolution and pose variation of a typical Electronic Passport deployment). 

## 4.10.1.1.2 Requirements on the System Performance 

The following requirements SHALL be met for the system performance (including failure to enrol (FTE) and failure to aquire (FTA) rates): 

- 20 Typically a vendor-specific uncalibrated raw score 

Federal Office for Information Security 

72 

4 Function Modules 

The false reject rate (FRR) SHALL be less than 4 % at an false accept rate (FAR) of at most 0.1 %. 

## 4.10.2 FM CMP-FP-VER 

This Function Module contains requirements for the verification of an identity in relation to stored reference fingerprint images. 

## 4.10.2.1 Requirements 

## 4.10.2.1.1 Requirements on the Algorithm Performance 

The following requirements SHALL be met for a fingerprint verification algorithm: 

- The fingerprint verification algorithm has to be configured at a security level (threshold) guaranteeing an FMR of 0.1 % (1:1000) in conjunction with an FNMR less than 2 %. 

- The threshold SHALL be configurable by the system administrator to allow for stricter settings when ne cessary. 

- Furthermore, the overall system has to be calibrated for the security level set within this specific scenario of verification. The vendor of the verification algorithm has to provide calibration data based on the actual verification performance. 

- The output of the algorithm SHALL be a comparison score[21] and the result of the verification (the achieved FMR and an indication whether the threshold has been reached) depending on the chosen security level (threshold) of the algorithm. 

To ensure the validity of proclaimed values, a vendor SHALL provide test results that support the designated claim. The following requirements apply to those test results: 

- The vendor SHALL provide a DET curve of the algorithm performance. 

- Such performance SHALL be on the basis of images of comparable characteristic (e.g. images in size and resolution and pose variation of a typical Electronic Passport deployment). 

## 4.10.2.1.2 Requirements on the System Performance 

The following requirements SHALL be met for the system performance (including FTE) and FTA rates): 

The FRR SHALL be less than 4 % at an FAR of 0.1 %. 

## 4.11 FM Category Logging 

The Function Module Logging (LOG) contains logging requirements. The requirements of this chapter and the requirements of the schema of information to log apply both. 

## 4.11.1 FM LOG-ALL-GENERIC 

The Function Module Logging contains requirements as to which data has to be logged for a specific appli cation. 

## 4.11.1.1 Requirements 

- A transaction SHALL cover all information concerning one single biometric subject. Created IDs SHALL be unique globally. During the biometric process all data SHALL be gathered or created by the application. 

- Each transaction SHALL contain the generic process information about the system that are defined in `ty pe.transaction` . The exact semantic for the location of station is profile-dependent. See the specific profile for a refined definition. If the transaction is dependent or derived from another transaction the ID of the reference SHALL be set. 

- In case of abnormal termination of the transaction or any of its sub-processes, the error code SHALL be log ged. The vendor SHALL provide a detailed list of all error codes used with complete semantic descriptions. 

> 21 Typically a vendor-specific uncalibrated raw score 

Federal Office for Information Security 

73 

4 Function Modules 

- During the transaction performed enrolment processes SHALL be logged as `Enrolment` . In cases where the central system replies directly with enrolment status information the submit time SHALL be recorded. If any control verification is performed during enrolment the result SHALL be contained. 

- For identification processes the data defined in `Identification` SHALL be recorded. The list of candidates SHALL be contained if detailed scoring information is provided by the central system. 

- A verification processes SHALL be recorded based on the `Verification` element. Per verification all perfor med comparisons SHALL be included. For each comparison the vendor specific score as well as the thres hold SHALL be contained. 

## 4.11.2 FM LOG-ALL-BCL 

The Function Module Logging contains requirements as to which data has to be logged for the application of border control. 

## 4.11.2.1 Requirements 

In case a record is stored externally, the external reference SHALL be defined giving information about the actual location of the data. For this purpose the `externalReference` attribute of the `bio:BinaryRecord` element SHALL be used.There SHALL NOT be data within the respective record of the log when the external reference is used. 

In order to allocate border control logs to their respective application profile the element `ApplicationProfile` SHALL be filled as described in Table 4.8. 

|**Application Profile within TR**|**ApplicationProfile-Element**|
|---|---|
|Application Profile Manual Border Control|`BCL_ManualBorderControl`|
|Application Profile Semi-Mobile Manual Border Control|`BCL_SemiMobileManualBorderControl`|
|Application Profile Automated Border Control (Face-Verifi|`BCL_AutomatedBorderControlFaceVerfication`|
|cation Only)||
|Application Profile Self-Service System|`BCL_SelfServiceSystem`|
|**Table 4.8**Mapping Logs to Application Profiles||



Logging for Application Profile Manual Border Control and Application Profile Semi-Mobile Manual Bor der Control SHALL be done with the `bcl-log` element as root containing only the following sub-elements (besides the already required elements and attributes by the XML-schema itself): 

- gathered elements of `MultiModalProcess` , `FaceAcquisition` , `FaceDelivery` , `FingerAcquisition` and/or `Finger Delivery` (depending on which acquisition and/or delivery processes have been performed beforehand) 

- `Verification` (of chip facial image against live facial image, if not performed before and result(s) of verifi cation(s) using live fingerprints and live facial image against CIRs) 

- `Identification` (result(s) of identification(s) within CIRs) 

Logging for Application Profile Automated Border Control (Face-Verification Only) SHALL be done with the `bcl-log` (or `MultiModalProcess` if system is designed to have down stream process at Application Profile Manual Border Control or Application Profile Semi-Mobile Manual Border Control) element as root con taining only the following sub-elements (besides the already required elements and attributes by the XMLschema itself): 

- `FaceAcquisition` (live facial image) 

- `FaceDelivery` (chip facial image) 

- `Verification` (of chip facial image against live facial image and result(s) of verification(s) against CIRs) 

Logging for Application Profile Self-Service System SHALL be done with the `MultiModalProcess` element as root containing only the following sub-elements (besides the already required elements and attributes by the XML-schema itself): 

- `FaceAcquisition` (live facial image) 

- `FaceDelivery` (chip facial image) 

Federal Office for Information Security 

74 

4 Function Modules 

- `Verification` (of chip facial image against live facial image and result(s) of verification(s) againstCIRs) 

## 4.11.2.2 Recommendations 

It is RECOMMENDED to store the images of the fingerprints and the facial image not only in the application specific container (e.g. EES-ANSI-NIST) record within the log, but also as separated records (e.g. in JPEG, BMP, WSQ). Thereby, the log-reading applications are able to parse the images easier, as they only need knowledge about the syntax of the BSI TR-03121 log schema. 

## 4.11.3 FM LOG-FI-GENERIC 

This Function Module describes requirements and interfaces for the logging of information regarding facial images for all profiles. 

## 4.11.3.1 Requirements 

- Within a transaction for each facial image acquisition or delivery performed for enrolment, verification or identification, all data defined in `FaceAcquisition` (of which some MAY be contained within a `Multi ModalProcess` ) or `FaceDelivery` SHALL be collected, if available. 

- During an acquisition process, the available details for all captures SHALL be logged. 

- If a veto was put by the operator the type of veto (OK/NOK) SHALL be set. 

- Detailed quality information SHALL be logged at least for the selected facial image. The overall result MAY be omitted if it is undefined. For each component the identifier, upper and lower value bound as well as the upper and lower threshold bound SHALL be included if available. When more than one facial image is present, all face quality elements SHALL reference to the corresponding record element. 

- For each performed PAD the detailed PAD quality values accompanied by identifiers, upper and lower value bounds and upper and lower threshold bounds SHALL be collected. 

- If a user interface is available during the acquisition process, the displayed information, e.g. an indication of a PAD alert or live feedback screen SHALL be logged. 

- In case of abnormal termination of the facial image acquisition process or any of its sub-processes, the error code SHALL be logged. The vendor SHALL provide a detailed list of all error codes used with complete semantic descriptions. In the special case that image acquisition is canceled, logging of information is only expected in the border control domain. 

## 4.11.4 FM LOG-FP-GENERIC 

This Function Module describes requirements and interfaces for the logging of information regarding finger print images for all profiles. 

## 4.11.4.1 Requirements 

- Within a transaction for each fingerprint acquisition or delivery performed for enrolment, verification, control verification or identification, all data defined in `FingerAcquisition` (of which some MAY be contai ned within a `MultiModalProcess` ) or `FingerDelivery` SHALL be collected, if available. If a fingerprint could not be acquired, the reason for each missing finger SHALL be logged. 

- For each capture process of a dedicated fingerprint or slap, all available information SHALL be logged. In case of multiple captures for a finger or slap the number of the capture details for which slap was selected as the best capture SHALL be specified. Within the finger capture the reference to the corresponding record of the probe SHALL be set. Further the details of each during the capture performed attempt SHALL be pro vided, including the reference to the corresponding record if available. In case of an unacceptable capture attempt the reason for rejection of this capture attempt SHALL be selected. If the rejection reason is `other` an error code detailing the reason of rejection SHALL be set. 

- If a veto was put by the operator the type of veto (OK/NOK) SHALL be set. 

- For the best capture attempt, detailed quality information about the result SHALL be logged. For all other capture attempts quality information, if calculated during the process, SHOULD be logged. For each finger or slap within a capture the quality result value and the threshold SHALL be presented within a range from 

Federal Office for Information Security 

75 

4 Function Modules 

0 to 100 when available. If an overall quality value can be estimated by the quality assessment algorithm it SHALL be specified. 

- If a slap classification is performed during the acquisition process, the details SHALL be logged as `Finger ClassifierInformation` . This includes the classification results, information about the configured threshold of the algorithm and whether the classifier has been used in evaluation mode. 

- When a uniqueness check is performed, the results SHALL be collected. If the FMR is known, the security level for the uniqueness check SHALL be contained. The log SHALL specify all detected duplicate fingers. 

- For each performed PAD the detailed PAD quality values accompanied by identifiers, upper and lower va lue bounds and upper and lower threshold bounds SHALL be collected. In case the probe is a slap and a PAD result is expected for each individual finger of the slap, the finger code SHALL be defined and PAD information SHALL be present for each finger. 

- If a user interface is available during the acquisition process, the displayed information, e.g. an indication of a PAD alert or live feedback screen SHALL be logged. 

- In unsupervised acquisition scenarios all available surveillance information SHALL be stored for each cor responding capture attempt. The surveillance image contained within a record SHALL be linked to the fin gerprint capture attempt. 

- It SHALL be logged if multiple persons have been detected or not during the fingerprint acquisition process or single capture attempts. 

- When the acquisition process is performed with the presence of a configured timeout the corresponding value SHALL be specified in milliseconds. The logging of the configured value SHALL be independent from the occurrence of a timeout. 

- If a control verification is performed (e.g. for rolled vs flat fingerprints or for fingerprints acquired at a SSS vs fingerprints acquired at the counter) all available information SHALL be logged within a `Verification` element. 

- In case of abnormal termination of the fingerprint acquisition process or any of its sub-processes, the error code SHALL be logged. Errors during the fingerprint segmentation or uniqueness check SHALL be specified additionally by their corresponding error element. The vendor SHALL provide a detailed list of all error codes used with complete semantic descriptions. In the special case that image acquisition is canceled, log ging of information is only expected in the border control domain. 

- Information about the configured pixel density in dpi (dots-per-inch) of the fingerprint scanner SHALL be contained in `FingerAcquisition/Hardware/ConfigurationInformation` using _PixelDensity_ as type. 

## 4.12 FM Category Coding 

This Function Module Coding (COD) contains the procedures to encode quality data as well as biometric data in defined formats. Interoperability is provided by means of standard compliant coding. 

## 4.12.1 FM COD-ALL-BCL 

This Function Module describes requirements and interfaces for the overall coding of biometric and biogra phic data used within the context of border control. 

## 4.12.1.1 Requirements 

- The logging data as defined by the FM of the FM Category Logging SHALL be encoded as XML according to the schema definition as `bcl-log` element. The XML encoding is defined by the XML schema definition in the file „bcl6v1.xsd“ and referenced schema files. 

- Optional attributes and elements of the schema SHALL be considered as far as possible (e.g. error codes only need to be logged, in case an error occurred; an acquisition element is only required, in case an acquisition process has at least been started). 

- All log data SHALL be encoded as far as it is available throughout the acquisition process (e.g. fingerprint quality data is encoded if and only if fingerprint capture was performed). 

Federal Office for Information Security 

76 

4 Function Modules 

## 4.12.2 FM COD-ALL-EES 

This Function Module describes requirements and interfaces for the coding of general information according to EES-ANSI-NIST transactions. 

## 4.12.2.1 Requirements 

The general coding SHALL be conformant to the current version of the [BIB_EES_ICD] in the binary format. Some required EES-ANSI-NIST data fields (e.g. biographic information) may not be available for the acquisi tion system (see Table 4.9) . In order to keep the schema conformance during the entire process, these fields SHALL be filled with conformant placeholders. These placeholders SHALL be replaced as soon as possible with the actual values by the calling application. 

|**Record Type**|**Mnemonic**|**Field Name**|
|---|---|---|
|1|PRY|Priority|
|1|ORI|Originating Agency Identifier|
|10|SRC|Source Agency|
|14|SRC|Source Agency|



**Table 4.9** Potential EES-ANSI-NIST Fields for Placeholders 

## 4.12.3 FM COD-FI-GENERIC 

This Function Module describes requirements for the coding used during the acquisition process of facial images. 

## 4.12.3.1 Requirements 

All results of the acquisition or delivery process SHALL be encoded in XML as `FaceAcquisition` or `FaceDelivery` . 

The XML encoding is defined by the XML schema definition in `biotypes6v1.xsd` for all volumes. 

## 4.12.4 FM COD-FI-EES 

This Function Module describes requirements for the coding used within the context of border control. 

## 4.12.4.1 Requirements 

- The coding for facial images SHALL be conformant to the current version of the [BIB_EES_ICD] in accor dance with [BIB_EES_ICD] in the binary format. 

- The minimum image resolution SHALL be 600 x 800 pixels. 

- The maximum image resolution SHALL be 1200 x 1600 pixels. 

## 4.12.5 FM COD-FI-VER 

This Function Module describes requirements for the coding used during the verification process of facial images. 

## 4.12.5.1 Requirements 

The result data of the verification process is collected from different components. The verification and the evaluation work flow return separate logging data: 

- All results of the verification work flow SHALL be encoded in XML according to the schema definition as `Verification` within bcl-log element. 

- All results of the evaluation work flow SHALL be encoded in XML according to the schema definition as fi-bcl-eval element. 

The XML encoding is defined by the XML schema definition in "bcl6v1.xsd". Examples can be found in "bcllog.xml" and "fi-bcl-eval.xml". 

Federal Office for Information Security 

77 

4 Function Modules 

## 4.12.6 FM COD-FP-EES 

This Function Module describes requirements for the coding used to send fingerprint images to the CS EES. 

## 4.12.6.1 Requirements 

The coding for fingerprint images SHALL be conformant to the current version of the [BIB_EES_ICD] in ac cordance with [BIB_EES_ICD] in the binary format. 

## 4.12.7 FM COD-FP-VER 

This Function Module describes requirements for the coding used during the verification process of finger print images. 

## 4.12.7.1 Requirements 

The result data of the verification process is collected from different components. The verification and the evaluation work flow return separate logging data: 

- All results of the verification work flow SHALL be encoded in XML as `Verification` within "bcl-log". 

- All results of the evaluation work flow SHALL be encoded in XML as "fp-bcl-eval". 

The XML encoding is defined by the XML schema definition in "bcl6v1.xsd". Examples can be found in "bcllog.xml" and "fp-bcl-eval.xml". 

## 4.13 FM Category Evaluation 

Will be amended in a future version of this TR. 

Federal Office for Information Security 

78 

List of Abbreviations 

## List of Abbreviations 

|**Abbreviation**|**Description**|
|---|---|
|ABC|Automated Border Control|
|ABIS|Automated Biometric Identification System|
|AH|Acquisition Hardware|
|AS|Acquisition Software|
|BCL|Border Control|
|BIP|Biometric Image Processing|
|BMS|Biometric Matching System|
|CIR|Central Identity Register|
|CMP|Biometric Comparison|
|COD|Coding|
|COM|Compression|
|CS EES|Central System EES|
|CTF|contrast transfer function|
|DET|Detection Error Trade-Off|
|EES|Entry-Exit System|
|eMRTD|Electronic Machine Readable Travel Document|
|FAR|false accept rate|
|FI|facial image|
|FM|Function Module|
|FMR|false-match-rate|
|FNIR|false-negative-identification-rate|
|FNMR|false-non-match-rate|
|FP|fingerprint|
|FPIR|false-positive-identification-rate|
|FRR|false reject rate|
|FTA|failure to aquire|
|FTE|failure to enrol|
|HLBS|High Level Biometric Services|
|LOG|Logging|
|MBC|Manual Border Control|
|NFIQ2.2|NIST Fingerprint Image Quality 2.2|
|O|Operation|
|PAD|Presentation Attack Detection|
|PAP|Partial Application Process|
|QA|Quality Assessment|
|REF|Reference Storage|
|SIS|Schengen Information System|
|SNR|signal-to-noise ratio|
|SSS|self-service system|



Federal Office for Information Security 

79 

List of Abbreviations 

|**Abbreviation**|**Description**|
|---|---|
|TCN|Third-Country National|
|TR|Technical Guideline|
|UI|User Interface|
|VIS|Visa Information System|
|WSQ|Wavelet Scalar Quantisation|



Federal Office for Information Security 

80 

Bibliography 

## Bibliography 

- [BIB_ANSI_NIST_2011:2015] _ANSI/NIST-ITL 1-2011: Update 2015, American National Standard for Infor mation Systems – Data Format for the Interchange of Fingerprint, Facial & Other Biometric Informa tion ANSI/NIST-ITL 1-2011 NIST Special Publication 500-290 Edition 3, available at: http://dx.doi.or g/10.6028/NIST.SP.500-290e3._ 

- [BIB_EBTS/F] _FBI Electronic Biometric Transmission Specification Version 11, Appendix F, April 2021._ 

- [BIB_EES_ICD] _eu-LISA EES Interface Control Document, Version 00_07_06_errata2, 2025, 27.06.2025._ 

- [BIB_EES_ICD] _eu-LISA EES Interface Control Document, Annex 05 - NIST Fields, Version 00_07_06_errata2, 2025, 27.06.2025._ 

- [BIB_ICAO_TR_Portrait_Quality] _ICAO Technical Report: Portrait Quality (Reference Facial Images for MRTD), version 1.0, April 2018._ 

- [BIB_ISO_10918-1] _ISO/IEC 10918-1:1994 "Information technology – Digital compression and coding of conti nuous-tone still images: Requirements and guidelines"._ 

- [BIB_ISO_15444] _ISO/IEC 15444-1:2004 "Information technology – JPEG 2000 image coding system: Core coding system"._ 

- [BIB_ISO_19794_FACE] _ISO/IEC 19794-5:2005 "Information technology – Biometric data interchange formats – Part 5: Face image data"._ 

- [BIB_ISO_19794_FINGER] _ISO/IEC 19794-4:2005 "Information technology – Biometric data interchange formats – Part 4: Finger image data"._ 

- [BIB_ISO_19795-1:2021] _ISO/IEC 19795-1:2021 "Information technology — Biometric performance testing and reporting — Part 1: Principles and framework"._ 

- [BIB_ISO_39794_FACE] _ISO/IEC 39794-5:2019, Information technology – Extensible biometric data interchange formats – Part 5: Face image data._ 

- [BIB_ISO_39794_FINGER] _ISO/IEC 39794-4:2019, Information technology – Extensible biometric data interch ange formats – Part 4: Finger image data._ 

- [BIB_ISO_PAD_1] _ISO/IEC 30107-1:2023 "Information technology – Biometric presentation attack detection – Part 1: Framework"._ 

- [BIB_ISO_PAD_3] _ISO/IEC 30107-3:2023 "Information technology – Biometric presentation attack detection – Part 3: Testing and reporting"._ 

- [BIB_NFIQ2.2] _NIST Fingerprint Image Quality 2.2._ 

Federal Office for Information Security 

81 

Bibliography 

Federal Office for Information Security 

82 


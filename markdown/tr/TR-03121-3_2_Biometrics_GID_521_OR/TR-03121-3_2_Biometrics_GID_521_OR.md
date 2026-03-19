BSI Technical Guideline TR-03121-3 

## Biometrics for Public Sector Applications 

Part 3: Application Profiles, Function Modules and Processes 

Volume 2: Enrolment Scenarios for Identity Documents 

Version 5.2.1 

Federal Office for Information Security PO Box 20 03 63 53133 Bonn E-Mail: TRBiometrics@bsi.bund.de Internet: https://bsi.bund.de © Federal Office for Information Security 2022 

BSI Technical Guideline TR-03121-3 

Federal Office for Information Security 

iii 

Table of Content 

## Table of Content 

|1|Volume Enrolment Scenarios of Identity Documents ...................................................................... 1|
|---|---|
|2|Application Profiles ....................................................................................................................... 2|
|2.1|Application Profile German Electronic Passport ...................................................................... 2|
|2.2|Application Profile German Identity Card ............................................................................... 8|
|2.3|Application Profile German Electronic Residence Permit ....................................................... 14|
|3|Partial Application Processes ........................................................................................................ 21|
|3.1|PAP ACQ-FI-SV-1: Supervised Facial Image Acquisition by Scanned Image ............................. 21|
|3.2|PAP ACQ-FP2P-SV-2: Supervised Acquisition of Two Plain Fingerprints on Single-Finger Hard|
||ware for Enrolment .............................................................................................................. 21|
|3.3|PAP ACQ-FP2P-SV-1: Supervised Acquisition of Two Plain Fingerprints on Multi-Finger Hard|
||ware for Enrolment .............................................................................................................. 23|
|3.4|PAP ACQ-FP2P-USV-2: Unsupervised Acquisition of Two Plain Fingerprints on Single-Finger|
||Hardware for Enrolment ...................................................................................................... 26|
|3.5|PAP ACQ-FP2P-USV-1: Unsupervised Acquisition of Two Plain Fingerprints on Multi-Finger|
||Hardware for Enrolment ...................................................................................................... 28|
|4|Function Modules ........................................................................................................................ 31|
|4.1|FM Category Acquisition Hardware ....................................................................................... 31|
|4.2|FM Category Acquisition Software ........................................................................................ 35|
|4.3|FM Category Biometric Image Processing .............................................................................. 36|
|4.4|FM Category Quality Assessment .......................................................................................... 37|
|4.5|FM Category Presentation Attack Detection .......................................................................... 44|
|4.6|FM Category Compression .................................................................................................... 47|
|4.7|FM Category Operation ........................................................................................................ 48|
|4.8|FM Category User Interface .................................................................................................. 49|
|4.9|FM Category Reference Storage ............................................................................................. 52|
|4.10|FM Category Biometric Comparison ..................................................................................... 52|
|4.11|FM Category Logging ............................................................................................................ 53|
|4.12|FM Category Coding ............................................................................................................. 60|
|4.13|FM Category Evaluation ....................................................................................................... 64|
||List of Abbreviations .................................................................................................................. 143|
||Bibliography .............................................................................................................................. 144|



Federal Office for Information Security 

iv 

List of figures 

## List of figures 

2.1. Overview Process Biometric Application German ePass .................................................................. 2 2.2. Facial Image Acquisition Process by Scan of Photograph ................................................................. 3 2.3. Facial Image Acquisition Process by an Unsupervised Self-Service System ........................................ 4 2.4. Facial Image Acquisition Process in Studio Set-up by Official ........................................................... 4 2.5. Facial Image Acquisition Process by Digital Transmission of the Photograph .................................... 5 2.6. Fingerprint Acquisition by Supervised Live Enrolment .................................................................... 6 2.7. Fingerprint Acquisition Process by Unsupervised Self-Service Live Enrolment .................................. 6 2.8. Overview Process Biometric Application German Identity Card ....................................................... 8 2.9. Facial Image Acquisition Process by Scan of Photograph ................................................................. 9 2.10.Facial Image Acquisition Process by an Unsupervised Self-Service System ...................................... 10 2.11.Facial Image Acquisition Process in Studio Set-up by Official ......................................................... 10 2.12.Facial Image Acquisition Process by Digital Transmission of the Photograph .................................. 11 2.13.Fingerprint Acquisition by Supervised Live Enrolment .................................................................. 12 2.14.Fingerprint Acquisition Process by Unsupervised Self-Service Live Enrolment ................................ 12 2.15.Overview Process Biometric Application German Electronic Residence Permit ............................... 14 2.16.Facial Image Acquisition Process by Scan of Photograph ............................................................... 15 2.17.Facial Image Acquisition Process by an Unsupervised Self-Service System ...................................... 16 2.18.Facial Image Acquisition Process in Studio Set-up by Official ......................................................... 16 2.19.Facial Image Acquisition Process by Digital Transmission of the Photograph .................................. 17 2.20.Fingerprint Acquisition by Supervised Live Enrolment .................................................................. 18 2.21.Fingerprint Acquisition Process by Unsupervised Self-Service Live Enrolment ................................ 18 3.1. Partial Application Process "Supervised Facial Image Acquisition by Scanned Image" ...................... 21 3.2. Partial Application Process "Supervised Acquisition of Two Plain Fingerprints on Single-Finger Hard ware for Enrolment" .................................................................................................................... 22 3.3. Partial Application Process Task "Capture Plain Fingerprint Supervised" ......................................... 23 3.4. Partial Application Process "Supervised Acquisition of Two Plain Fingerprints on Multi-Finger Hard ware for Enrolment" .................................................................................................................... 24 3.5. Partial Application Process Task "Capture Slap Supervised" ............................................................ 25 3.6. Partial Application Process Task "Capture Plain Fingerprint Supervised" ......................................... 26 3.7. Partial Application Process "Unsupervised Acquisition of Two Plain Fingerprints on Single-Finger Hardware for Enrolment" ............................................................................................................. 27 3.8. Partial Application Process Task "Capture Plain Fingerprint Unsupervised" ..................................... 28 

Federal Office for Information Security 

v 

List of figures 

3.9. Partial Application Process "Unsupervised Acquisition of Two Plain Fingerprints on Multi-Finger Hard ware for Enrolment" .................................................................................................................... 29 3.10.Partial Application Process Task "Capture Slap Unsupervised" ........................................................ 30 4.1. Example Heat Map ....................................................................................................................... 68 4.2. Example Box Plot ......................................................................................................................... 69 4.3. Example Scatter Plot .................................................................................................................... 70 4.4. Example Line Plot ........................................................................................................................ 71 4.5. Example Histogram Plot ............................................................................................................... 72 4.6. Example Histogram with Empirical Cumulative Distribution Function ........................................... 73 4.7. Example Bar Plot ......................................................................................................................... 74 4.8. Example Horizontal Stacked Bar Plot ............................................................................................ 75 4.9. Example Vertical Stacked Bar Plot ................................................................................................ 75 4.10.Example Grouped Bar Plot ........................................................................................................... 76 4.11.Example Table with Alternation Background Colour ..................................................................... 76 4.12.Example Line Plot Number of Acquisition Processes ..................................................................... 85 4.13.Example Histogram Finger Identification Process Duration ........................................................... 87 4.14.Example Stacked Bar Plot Global Identification Process Result ....................................................... 90 4.15.Example Histogram Finger Identification Candidate’s Achieved FMR ............................................. 91 4.16.Example Histogram Number of Applications ................................................................................ 92 4.17.Example Stacked Bar Plot Global Single Verification Process Result ................................................ 93 4.18.Example Histogram Single Verification Achieved FMR .................................................................. 94 4.19.Example Histogram Single Verification Process Duration .............................................................. 96 4.20.Heat Map Facial Image Acquisitions by Software ........................................................................... 98 4.21.Heat Map Facial Image Acquisitions by Hardware ......................................................................... 99 4.22.Example Stacked Bar Plot Total Facial Image Quality ................................................................... 100 4.23.Example Stacked Bar Plot Acceptability of Facial Images by Quality Metrics .................................. 101 4.24.Example Stacked Bar Plot Total Central Facial Image Quality ....................................................... 103 4.25.Example Stacked Bar Plot Central Acceptability of Facial Images by Quality Metrics ...................... 104 4.26.Heat Map Finger Acquisitions by Software .................................................................................. 106 4.27.Heat Map Finger Acquisitions by Hardware ................................................................................. 107 4.28.Example Stacked Bar Plot Number of Finger Captures ................................................................. 108 4.29.Example Heat Map Number of Finger Captures by Time .............................................................. 110 

Federal Office for Information Security 

vi 

List of figures 

4.30.Example Stacked Bar Plot Number of Finger Captures by Finger Plot ............................................ 111 4.31.Example Stacked Bar Rejection Reasons of Finger Capture Attempts ............................................. 112 4.32.Example Stacked Bar Rejection Reasons of Finger Capture Attempts by Finger .............................. 113 4.33.Example Stacked Bar Success Rate of Finger Capture Attempts ..................................................... 114 4.34.Example Stacked Bar Success Rate of Finger Capture Attempts by Finger ...................................... 116 4.35.Example Histogram Number of Finger Capture Attempts per Applicant ........................................ 117 4.36.Example Stacked Bar Plot Relative Finger Quality Assessment Errors ............................................ 118 4.37.Example Histogram NFIQ 2.0 Fingerprint Image Quality .............................................................. 119 4.38.Example Box Plot NFIQ 2.0 Fingerprint Image Quality Finger Comparison ................................... 120 4.39.Example Histogram Finger Capture Duration per Finger .............................................................. 122 4.40.Example Box Plot Finger Capture Duration Comparison .............................................................. 123 4.41.Example Stacked Bar Plot Relative Frequencies of Applicants with a Missing Finger ....................... 124 4.42.Example Stacked Bar Plot Relative Frequencies Missing Finger Reason ......................................... 125 4.43.Example Histogram Number of Missing Fingers .......................................................................... 126 4.44.Example Stacked Bar Plot Relative Frequencies Missing Fingers ................................................... 127 4.45.Example Stacked Bar Finger Acquisitions With Sequence Errors ................................................... 128 4.46.Example Histogram Number of Sequence Errors ......................................................................... 129 4.47.Example Stacked Bar Finger Acquisitions With Segmentation Errors ............................................ 130 4.48.Example Stacked Bar Uniqueness Check Errors per Finger Acquisition .......................................... 131 4.49.Example Stacked Bar Finger Duplicates ....................................................................................... 131 4.50.Example Stacked bar plot finger quality errors ............................................................................ 133 4.51.Example Histogram NFIQ 2.0 Fingerprint Image Quality .............................................................. 134 4.52.Example Box plot NFIQ 2.0 fingerprint image quality comparison by finger .................................. 135 4.53.Example Stacked Bar Plot Fingerprint Capture Allowed ............................................................... 136 4.54.Example Stacked Bar Plot Fingerprint Exclude Option ................................................................. 138 4.55.Example Stacked Bar Finger Acquisitions with Presentation Attack Detection ............................... 140 4.56.Example Histogram Number of Presentation Attack Detection Scores .......................................... 142 

Federal Office for Information Security 

vii 

List of figures 

Federal Office for Information Security 

viii 

1 Volume Enrolment Scenarios of Identity Documents 

## 1 Volume Enrolment Scenarios of Identity Documents 

This document defines Application Profiles for the enrolment of biometric data for specific Identity Docu ments, namely the electronic Passport, the German Identity Card and the German Electronic Residence Per mit. 

Note, that with this version only certifications valid until April 30, 2025 will be issued. 

Federal Office for Information Security 

1 

2 Application Profiles 

## 2 Application Profiles 

## 2.1 Application Profile German Electronic Passport 

The following Application Profile describes the biometric application process for a German Electronic Passport (ePass). 

The requirements for the application of a German ePass are determined by the [BIB_PassG], which mandates biometric characteristics to be included in the chip of the German Electronic Passport. These requirements are based on the EU regulation 2252/2004, refer to [BIB_EC_2252/2004]. 

By legal requirements, the inclusion of a facial image is mandatory, the inclusion of fingerprints for persons up to the age of six is not allowed but is mandatory for applicants older than six. 

## 2.1.1 Mandatory Process 

For the application of a German electronic passport a facial image as well as two fingerprints of the applicant have to be captured electronically[1] . This is done in accordance with FM Category Acquisition Hardware, FM Category Acquisition Software and FM Category Biometric Image Processing. 

The resulting biometric data of the facial image and fingerprints can be reduced in size by lossy compression. However, multiple lossy compressions SHALL NOT be allowed. For facial images software-based quality as surance SHALL be conducted on the processed and compressed image data. For fingerprints, the compression SHALL be performed after the quality assurance process. The facial image and the fingerprint images as well as additional quality information, which is connected to the biometric data, SHALL be coded and then passed to the calling application. 

Hereby, the facial image SHALL be passed to the calling application in two different encoding formats: The applying formats that SHALL be used for storing the facial image in the passport and for storing in a local re ference storage ("Passregister", [BIB_PassG], §21), are stated within FM REF-FI-GID, FM REF-FI-CHIP. FM COD-FI-GID contains general details on the XML encodings. The software-based quality assurance SHALL be conducted on basis of the processed and compressed images for storage in the chip of the passport. 

## 2.1.1.1 Overview Process 

Figure 2.1 depicts the biometric overview process of an application for a German ePass. The process depicted is for illustration purpose only. Note, that the following sections will detail this process for fingerprint and facial image acquisition. 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0010-12.png)


**----- Start of picture text -----**<br>
Acquire<br>Fingerprint<br>Images<br>Start End<br>Acquire Facial<br>Image<br>**----- End of picture text -----**<br>


**Figure 2.1.** Overview Process Biometric Application German ePass 

> 1 Furthermore a signature is captured, but this is not part of the description within TR Biometrics. 

Federal Office for Information Security 

2 

2 Application Profiles 

## 2.1.1.2 Facial Image Acquisition Process 

The facial image acquisition application system SHALL implement one ore more of the processes defined by the following subsections: 

1. scan-of-photograph process 

2. live-enrolment process 

3. BSI [BIB_TR-03146] digital-transmission process 

In any case, a quality assurance module (software) SHALL be used in the facial image acquisition process. In case a facial image is deemed non-compliant by the quality assurance module, the official SHALL make a final decision regarding exceptions (based on legal rules) for further processing. 

The final facial image SHALL be transferred to the calling application twice in different formats, refer to FM Category Biometric Image Processing, one image to be stored within the passport chip, and the other facial image to be stored within the local reference storage ("Passregister", refer to [BIB_PassG] §21). The software-ba sed quality assurance SHALL be conducted on basis of the processed and compressed images for storage in the chip of the passport. 

## 2.1.1.2.1 Scan-of-Photograph Process 

The facial image MAY be acquired by scanning a photograph which the applicant hands over to the official. 

The photograph SHALL be compliant with the requirements for biometric images [BIB_ISO_FACE]. The offi cial manually verifies whether the photograph depicts the applicant. After the official visually inspected the facial image with the help of a photo guideline and, if needed, with the help of a photo template the facial image SHALL be scanned, refer to FM QA-FI-PT and FM QA-FI-PG. Afterwards, the facial image SHALL be processed by the quality assurance module (software). 

Figure 2.2 depicts the facial image acquisition process by scanning a photograph which the applicant hands over to the official. The process is defined in detail by PAP ACQ-FI-SV-1: Supervised Facial Image Acquisition by Scanned Image. 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0011-12.png)


**----- Start of picture text -----**<br>
Acquire Facial<br>Image<br>Start End<br>**----- End of picture text -----**<br>


PAP Supervised Facial Image Acquisition by Scanned Image 

**Figure 2.2.** Facial Image Acquisition Process by Scan of Photograph 

## 2.1.1.2.2 Live Enrolment Process 

The facial image MAY be acquired live at a self-service system (SSS) or in a studio set-up by the official. 

## **Self-Service System** 

Figure 2.3 depicts the overall facial image self-service acquisition process at the SSS and the counter. 

The facial image is acquired at the SSS. The official at the counter retrieves the acquired facial image. 

The official SHALL verify the acquired facial image is of the applicant at the counter. The software based qua lity metrics SHALL be displayed to the official. The official SHALL decide to accept or reject the facial image, i.e. he MAY follow the quality software decision or MAY overrule a negative software Quality Assessment (QA) or MAY reject the facial image despite a positive software QA . 

Section 4.5.2 only applies for SSS but not until May 2025. 

Federal Office for Information Security 

3 

2 Application Profiles 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0012-01.png)


**----- Start of picture text -----**<br>
FM PAD-FI-APP1<br>(not until May 2025)<br>Acquire Facial<br>Image<br>Start<br>facial image<br>acquistion data<br>Reject Image<br>End<br>no no<br>acquired facial applicant by identity of imageVerifiy yes Assurance Results to DisplayQuality Offical Acquired Facial Assessment of Operator Image yes Release Image<br>Facial image  Accept image?<br>depicts applicant?<br>Self-Service System<br>Counter<br>**----- End of picture text -----**<br>


**Figure 2.3.** Facial Image Acquisition Process by an Unsupervised Self-Service System 

## **Studio Set-Up** 

Figure 2.4 depicts the overall facial image acquisition process in a studio set-up by an official, refer to FM AH-FI-DC for the studio set-up requirements. 

The facial image is acquired by the official with a digital camera. The software based quality metrics SHALL be determined and be displayed to the official. The official SHALL decide to accept or reject the facial image, i.e. the quality software decision MAY be followed or MAY be overruled in case of a negative software QA. In addition, the official MAY reject the facial image despite a positive software QA. 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0012-06.png)


**----- Start of picture text -----**<br>
FM AH-FI-DC<br>FM AS-FI-DC<br>Capture Facial<br>Image With<br>Camera<br>FM QA-FI-GID<br>Accept image?<br>Assess Display Operator<br>Quality of  Assurance Quality  Assessment of  yes Release Image<br>Captured Facial Results to  Acquired Facial<br>Start Image Offical Image End<br>no<br>Studio Set-Up<br>Offical<br>Counter<br>**----- End of picture text -----**<br>


**Figure 2.4.** Facial Image Acquisition Process in Studio Set-up by Official 

## 2.1.1.2.3 BSI TR-03146 Digital-Transmission Process 

The facial image MAY be transmitted to the counter by a photographer. 

Federal Office for Information Security 

4 

2 Application Profiles 

Figure 2.5 depicts the facial image acquisition process whereby the facial image acquisition is conducted detached from the counter office and is electronically transferred to the official counter. 

The image SHALL be acquired and compressed according to FM Category Acquisition Hardware, FM Cate gory Acquisition Software, FM Category Biometric Image Processing and FM Category Compression befo re transferring. The electronic transmission of the image SHALL comply to [BIB_TR-03146]. In order to gua rantee the connection between the facial image and the respective applicant, a manual verification SHALL be conducted by the official. In the successful case, the facial image SHALL be checked by the quality software. Finally, the operator SHALL have the option to give a veto in order to overrule the QA software decision. 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0013-03.png)


**----- Start of picture text -----**<br>
Photographer<br>Reject Image<br>Facial Image<br>no no<br>Start acquired facial applicant by  identity ofimageVerifiy Verified? yes retrieved facial Quality of Assessimage Results to OfficalDisplay Quality Assurance  Acquired Facial Assessment of Operator Image Accept image? yes Release Image End<br>FM QA-FI-GID<br>Counter<br>**----- End of picture text -----**<br>


**Figure 2.5.** Facial Image Acquisition Process by Digital Transmission of the Photograph 

## 2.1.1.3 Fingerprint Acquisition Process 

The fingerprint acquisition application system SHALL implement one or more of the following live-enrol ment processes defined in the following subsections: 

1. supervised live-enrolment process 

2. unsupervised self-service live-enrolment process 

## 2.1.1.3.1 Supervised Live Enrolment Process 

The fingerprint images MAY be acquired by a supervised acquisition process at the counter of the official. 

Figure 2.6 depicts the fingerprint acquisition process by a supervised acquisition at the counter of the offi cial. Depending on the type of fingerprint scanner at the counter, the detailed process is defined either detai led by PAP ACQ-FP2P-SV-2: Supervised Acquisition of Two Plain Fingerprints on Single-Finger Hardware for Enrolment or PAP ACQ-FP2P-SV-1: Supervised Acquisition of Two Plain Fingerprints on Multi-Finger Hardware for Enrolment. 

Federal Office for Information Security 

5 

2 Application Profiles 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0014-01.png)


**----- Start of picture text -----**<br>
FM FP-PAD-APP<br>Acquire<br>Fingerprint<br>Images<br>Start End<br>**----- End of picture text -----**<br>


PAP Supervised Acquisition of Two Plain Fingers on Single-Finger Hardware for Enrolment OR PAP Supervised Acquisition of Two Plain Fingers on Multi-Finger Hardware for Enrolment 

**Figure 2.6.** Fingerprint Acquisition by Supervised Live Enrolment 

## 2.1.1.3.2 Unsupervised Self-Service Live Enrolment Process 

The fingerprint images MAY be acquired by a unsupervised acquisition process at a SSS. 

Figure 2.7 depicts the overall fingerprint acquisition process at the SSS and the counter. 

The fingerprint is acquired at the SSS. The official at the counter retrieves the acquired fingerprints. 

The applicant’s fingerprints which have been acquired at the SSS SHALL additionally be acquired at the offi cial’s desk for verification according to FM Category Biometric Comparison. A verification comparison with the previously enrolled fingerprints at the SSS SHALL be conducted. Thereby, it is ensured that the legitimated applicant’s fingerprints have been captured at the live enrolment self-service station. In case the verification fails, the fingerprint enrolment SHALL be repeated at the official’s desk. 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0014-09.png)


**----- Start of picture text -----**<br>
PAP Unsupervised Acquisition of Two Finger Plain on Single-Finger Hardware for Enrolment OR<br>PAP Unsupervised Acquisition of Two Plain Fingers on Multi-Finger Hardware for Enrolment<br>Acquire<br>Fingerprint<br>Image<br>Start<br>FM FP-PAD-APP<br>fingerprint<br>acquistion data<br>no fingerprints and Discard  fingerprints and Discard<br>reacquire at  reacquire at<br>counter counter<br>yes Offical decides to<br>retry verification?<br>no no<br>Conduct Control Verfication results to OfficalDisplay PAD  Verification  yes Assurance Results of SSS to OfficalDisplay Quality  Fingerprint ImageAssessment of Acquired Operator  Accept  yes Release Image Default End<br>successful AND  fingerprints?<br>The finger  attack detected?no presentation<br>acquired at the<br>SSS SHALL be verified. FM CMP-FP-VER, FM FP-PAD-APP From SSS aquisition and aquisition for control verification<br>Self-Service System<br>Counter<br>**----- End of picture text -----**<br>


**Figure 2.7.** Fingerprint Acquisition Process by Unsupervised Self-Service Live Enrolment 

Federal Office for Information Security 

6 

2 Application Profiles 

## 2.1.2 Relevant Standards and Conditions 

In addition to the legal requirements (see above), further basic directives and standards SHALL be applicable: 

- [BIB_ICAO_9303] 

- [BIB_ISO_FINGER] 

- [BIB_ISO_FACE] 

## 2.1.3 Mandatory Function Modules 

All Function Modules which SHALL be applied for the Application Profile are presented in Table 2.1 where by slash-separated entries denote alternative Function Modules and comma-separated entries denote requi rements for all specified Function Modules. 

|**Module Category**|**Required Function Modules**|
|---|---|
|Acquisition Hardware|FM AH-FI-FBS (for scan-of-photograph process) /<br>FM AH-FI-DC (for live-enrol<br>ment process using digital cameras) /<br>FM AH-FI-ICS,<br>FM AH-FI-SSS2 (for live-en<br>rolment process using self-service systems)<br>FM AH-FP-OPT (for Fingerprint Acqui<br>sition)|
|Acquisition Software|FM AS-FI-FBS/<br>FM AS-FI-DC ,<br>FM AS-FP-SF/<br>FM AS-FP-MF|
|Biometric Image Processing|FM BIP-FI-FBS/<br>FM BIP-FI-GID ,<br>FM BIP-FP-APP|
|Quality Assessment|FM QA-FI-PG,<br>FM QA-FI-PT,<br>FM QA-FI-GENERIC,<br>FM QA-FI-GID ,<br>FM QA-<br>FP-APP|
|Presentation Attack Detection|FM PAD-FP-APP,<br>FM PAD-FI-APP1 (only applies for SSS but not until May 2025)|
|Compression|FM COM-FI-JP2,<br>FM COM-FI-JPG ,<br>FM COM-FP-WSQR|
|Operation|FM O-ALL-USV ,<br>FM O-FI-ALL ,<br>FM O-FI-DC,<br>FM O-FI-FBS ,<br>FM O-FP-ALL|
|User Interface|FM UI-FI-OP,<br>FM UI-FI-BSJ ,<br>FM UI-FP-OP,<br>FM UI-FP-BSJ|
|Reference Storage|FM REF-FP-CHIP ,<br>FM REF-FI-GID,<br>FM REF-FI-CHIP|
|Biometric Comparison|FM CMP-FP-VER (for control verifications if using a self-service system for finger<br>print acquisition)|
|Logging|FM LOG-ALL-GENERIC,<br>FM LOG-ALL-GID ,<br>FM LOG-FI-GENERIC,<br>FM LOG-<br>FI-GID ,<br>FM LOG-FP-GENERIC,<br>FM LOG-FP-GID|
|Coding|FM COD-ALL-GID,<br>FM COD-FI-GID,<br>FM COD-FP-GID|
|Evaluation|FM EVA-ALL-GID ,<br>FM EVA-FI-GID ,<br>FM EVA-FP-GID|



**Table 2.1** Required Function Modules Application Profile German Electronic Passport 

## 2.1.4 Mandatory Partial Application Processes 

All Partial Application Processes which SHALL be applied for the Application Profile are presented in Ta ble 2.2 whereby slash-separated entries denote alternative Partial Application Processes and comma-separa ted entries denote requirements for all specified Partial Application Processes. 

|**No.**|**Required Partial Application Process**|
|---|---|
|12|PAP ACQ-FI-SV-1: Supervised Facial Image Acquisition by Scanned Image|
|2|PAP ACQ-FP2P-SV-2: Supervised Acquisition of Two Plain Fingerprints on Single-Finger Hard<br>ware for Enrolment/<br>PAP ACQ-FP2P-SV-1: Supervised Acquisition of Two Plain Fingerprints on<br>Multi-Finger Hardware for Enrolment|



- 2 Note, as alternative the defined processes of the application profile are allowed. However, for these no dedicated Partial Application Processes exist. 

Federal Office for Information Security 

7 

2 Application Profiles 

|**No.**|**Required Partial Application Process**|
|---|---|
|3|PAP ACQ-FP2P-USV-2: Unsupervised Acquisition of Two Plain Fingerprints on Single-Finger<br>Hardware for Enrolment/<br>PAP ACQ-FP2P-USV-1: Unsupervised Acquisition of Two Plain Finger<br>prints on Multi-Finger Hardware for Enrolment (if a SSS is deployed)|



**Table 2.2** Required Partial Application Processes Application Profile German Electronic Passport 

## 2.2 Application Profile German Identity Card 

The following Application Profile describes the biometric application process for a German Identity Card. 

The requirements for the application of an electronic German Identity Card are determined by the [BIB_PAuswG], which mandates biometric characteristics to be included in the chip of the German Identity Card. By legal requirements, the inclusion of a facial image is mandatory, the inclusion of fingerprints for persons up to the age of six is not allowed. The inclusion of fingerprints for applicants older than six years is mandatory since 02.08.2021. 

## 2.2.1 Mandatory Process 

For the application of a German Identity Card a facial image as well as two fingerprints (optional) of the appli cant have to be captured electronically[3] . This is done in accordance with FM Category Acquisition Hardware, FM Category Acquisition Software and FM Category Biometric Image Processing. 

The resulting biometric data of the facial image and fingerprints can be reduced in size by lossy compression. However, multiple lossy compressions SHALL NOT be allowed. For facial images software-based quality as surance SHALL be conducted on the processed and compressed image data. For fingerprints, the compression SHALL be performed after the quality assurance process. The facial image and the fingerprint images as well as additional quality information, which is connected to the biometric data, SHALL be coded and then passed to the calling application. 

Hereby, the facial image SHALL be passed to the calling application in two different encoding formats: The first format SHALL be used for storing the facial image in the passport, the second format SHALL be used for storing in a local reference storage ("Personalausweisregister", [BIB_PAuswG], §23), refer to FM COM-FIJPG, FM COM-FI-JP2 and FM COD-FI-GID for details on the encodings etc. The software-based quality assurance SHALL be conducted on basis of the processed and compressed images for storage on the chip of the identity card. 

## 2.2.1.1 Overview Process 

Figure 2.8 depicts the biometric overview process of an application for a German Identity Card. The process depicted is for illustration purpose only. Note, that the following section will detail this process for fingerprint and facial image acquisition. 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0016-12.png)


**----- Start of picture text -----**<br>
Fingerprint<br>acquisition  no<br>allowed and<br>application<br>consents finger<br>acquisition OR<br>aquisition is<br>mandatory? yes Acquire<br>Fingerprint<br>Images<br>Start End<br>Acquire Facial<br>Image<br>**----- End of picture text -----**<br>


**Figure 2.8.** Overview Process Biometric Application German Identity Card 

- 3 Furthermore a signature is captured, too, but this is not part of the description within TR Biometrics. 

Federal Office for Information Security 

8 

2 Application Profiles 

## 2.2.1.2 Facial Image Acquisition Process 

The facial image acquisition application system SHALL implement one ore more of the processes defined by the following subsections: 

1. scan-of-photograph process 

2. live-enrolment process 

3. BSI [BIB_TR-03146] digital-transmission process 

In any case, a quality assurance module (software) SHALL be used in the facial image acquisition process. In case a facial image is deemed non-compliant by the quality assurance module, the official SHALL make a final decision regarding exceptions (based on legal rules) for further processing. 

The final facial image SHALL be transferred to the calling application twice in different formats, one image to be stored within the passport chip, and the other facial image to be stored within the local reference storage ("Passregister", refer to [BIB_PAuswG] §23). The software-based quality assurance SHALL be conducted on basis of the processed and compressed images for storage on the chip of the identity card. 

## 2.2.1.2.1 Scan-of-Photograph Process 

The facial image MAY be acquired by scanning a photograph which the applicant hands over to the official. 

The photograph SHALL be compliant with the requirements for biometric images [BIB_ISO_FACE]. The offi cial manually verifies whether the photograph depicts the applicant. After the official visually inspected the facial image with the help of a photo guideline and, if needed, with the help of a photo template the facial image SHALL be scanned, refer to FM QA-FI-PT and FM QA-FI-PG. Afterwards, the facial image SHALL be processed by the quality assurance module (software). 

Figure 2.9 depicts the facial image acquisition process by scanning a photograph which the applicant hands over to the official. The process is defined in detail by PAP ACQ-FI-SV-1: Supervised Facial Image Acquisition by Scanned Image. 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0017-12.png)


**----- Start of picture text -----**<br>
Acquire Facial<br>Image<br>Start End<br>**----- End of picture text -----**<br>


PAP Supervised Facial Image Acquisition by Scanned Image 

**Figure 2.9.** Facial Image Acquisition Process by Scan of Photograph 

## 2.2.1.2.2 Live Enrolment Process 

The facial image MAY be acquired live at a SSS or in a studio set-up by the official. 

## **Self-Service System** 

Figure 2.10 depicts the overall facial image self-service acquisition process at the SSS and the counter. 

The facial image is acquired at the SSS. The official at the counter retrieves the acquired facial image. 

The official SHALL verify the acquired facial image is of the applicant at the counter. The software based qua lity metrics SHALL be displayed to the official. The official SHALL decide to accept or reject the facial image, i.e. he MAY follow the quality software decision or MAY overrule a negative software QA or MAY reject the facial image despite a positive software QA. 

Section 4.5.2 only applies for SSS but not until May 2025. 

Federal Office for Information Security 

9 

2 Application Profiles 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0018-01.png)


**----- Start of picture text -----**<br>
FM PAD-FI-APP1<br>(not until May 2025)<br>Acquire Facial<br>Image<br>Start<br>facial image<br>acquistion data<br>Reject Image<br>End<br>no no<br>acquired facial applicant by identity of imageVerifiy yes Assurance Results to DisplayQuality Offical Acquired Facial Assessment of Operator Image yes Release Image<br>Facial image  Accept image?<br>depicts applicant?<br>Self-Service System<br>Counter<br>**----- End of picture text -----**<br>


**Figure 2.10.** Facial Image Acquisition Process by an Unsupervised Self-Service System 

## **Studio Set-Up** 

Figure 2.11 depicts the overall facial image acquisition process in a studio set-up by an official, refer to FM AH-FI-DC for the studio set-up requirements. 

The facial image is acquired by the official with a digital camera. The software based quality metrics SHALL be determined and be displayed to the official. The official SHALL decide to accept or reject the facial image, i.e. the quality software decision MAY be followed or MAY be overruled in case of a negative software QA. In addition, the official MAY reject the facial image despite a positive software QA. 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0018-06.png)


**----- Start of picture text -----**<br>
FM AH-FI-DC<br>FM AS-FI-DC<br>Capture Facial<br>Image With<br>Camera<br>FM QA-FI-GID<br>Accept image?<br>Assess Display Operator<br>Quality of  Assurance Quality  Assessment of  yes Release Image<br>Captured Facial Results to  Acquired Facial<br>Start Image Offical Image End<br>no<br>Studio Set-Up<br>Offical<br>Counter<br>**----- End of picture text -----**<br>


**Figure 2.11.** Facial Image Acquisition Process in Studio Set-up by Official 

## 2.2.1.2.3 BSI TR-03146 Digital-Transmission Process 

The facial image MAY be transmitted to the counter by a photographer. 

Federal Office for Information Security 

10 

2 Application Profiles 

Figure 2.12 depicts the facial image acquisition process whereby the facial image acquisition is conducted detached from the counter office and is electronically transferred to the official counter. 

The image SHALL be acquired and compressed according to FM Category Acquisition Hardware, FM Cate gory Acquisition Software, FM Category Biometric Image Processing and FM Category Compression befo re transferring. The electronic transmission of the image SHALL comply to [BIB_TR-03146]. In order to gua rantee the connection between the facial image and the respective applicant, a manual verification SHALL be conducted by the official. In the successful case, the facial image SHALL be checked by the quality software. Finally, the operator SHALL have the option to give a veto in order to overrule the QA software decision. 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0019-03.png)


**----- Start of picture text -----**<br>
Photographer<br>Reject Image<br>Facial Image<br>no no<br>Start acquired facial applicant by  identity ofimageVerifiy Verified? yes retrieved facial Quality of Assessimage Results to OfficalDisplay Quality Assurance  Acquired Facial Assessment of Operator Image Accept image? yes Release Image End<br>FM QA-FI-GID<br>Counter<br>**----- End of picture text -----**<br>


**Figure 2.12.** Facial Image Acquisition Process by Digital Transmission of the Photograph 

## 2.2.1.3 Fingerprint Acquisition Process 

The fingerprint acquisition application system SHALL implement one or more of the following live-enrol ment processes defined in the following subsections: 

1. supervised live-enrolment process 

2. unsupervised self-service live-enrolment process 

## 2.2.1.3.1 Supervised Live Enrolment Process 

The fingerprint images MAY be acquired by a supervised acquisition process at the counter of the official. 

Figure 2.13 depicts the fingerprint acquisition process by a supervised acquisition at the counter of the offi cial. Depending on the type of fingerprint scanner at the counter, the detailed process is defined either detai led by PAP ACQ-FP2P-SV-2: Supervised Acquisition of Two Plain Fingerprints on Single-Finger Hardware for Enrolment or PAP ACQ-FP2P-SV-1: Supervised Acquisition of Two Plain Fingerprints on Multi-Finger Hardware for Enrolment. 

Federal Office for Information Security 

11 

2 Application Profiles 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0020-01.png)


**----- Start of picture text -----**<br>
FM FP-PAD-APP<br>Acquire<br>Fingerprint<br>Images<br>Start End<br>**----- End of picture text -----**<br>


PAP Supervised Acquisition of Two Plain Fingers on Single-Finger Hardware for Enrolment OR PAP Supervised Acquisition of Two Plain Fingers on Multi-Finger Hardware for Enrolment 

**Figure 2.13.** Fingerprint Acquisition by Supervised Live Enrolment 

## 2.2.1.3.2 Unsupervised Self-Service Live Enrolment Process 

The fingerprint images MAY be acquired by a unsupervised acquisition process at a SSS. 

Figure 2.14 depicts the overall fingerprint acquisition process at the SSS and the counter. 

The fingerprint is acquired at the SSS. The official at the counter retrieves the acquired fingerprints. 

The applicant’s fingerprints which have been acquired at the SSS SHALL additionally be acquired at the offi cial’s desk for verification according to FM Category Biometric Comparison. A verification comparison with the previously enrolled fingerprints at the SSS SHALL be conducted. Thereby, it is ensured that the legitimated applicant’s fingerprints have been captured at the live enrolment self-service station. In case the verification fails, the fingerprint enrolment SHALL be repeated at the official’s desk. 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0020-09.png)


**----- Start of picture text -----**<br>
PAP Unsupervised Acquisition of Two Finger Plain on Single-Finger Hardware for Enrolment OR<br>PAP Unsupervised Acquisition of Two Plain Fingers on Multi-Finger Hardware for Enrolment<br>Acquire<br>Fingerprint<br>Image<br>Start<br>FM FP-PAD-APP<br>fingerprint<br>acquistion data<br>no fingerprints and Discard  fingerprints and Discard<br>reacquire at  reacquire at<br>counter counter<br>yes Offical decides to<br>retry verification?<br>no no<br>Conduct Control Verfication results to OfficalDisplay PAD  Verification  yes Assurance Results of SSS to OfficalDisplay Quality  Fingerprint ImageAssessment of Acquired Operator  Accept  yes Release Image Default End<br>successful AND  fingerprints?<br>The finger  attack detected?no presentation<br>acquired at the<br>SSS SHALL be verified. FM CMP-FP-VER, FM FP-PAD-APP From SSS aquisition and aquisition for control verification<br>Self-Service System<br>Counter<br>**----- End of picture text -----**<br>


**Figure 2.14.** Fingerprint Acquisition Process by Unsupervised Self-Service Live Enrolment 

Federal Office for Information Security 

12 

2 Application Profiles 

## 2.2.2 Relevant Standards and Conditions 

In addition to the legal requirements (see above), further basic directives and standards SHALL be applicable: 

- [BIB_ICAO_9303] 

- [BIB_ISO_FINGER] 

- [BIB_ISO_FACE] 

## 2.2.3 Mandatory Function Modules 

All Function Modules which SHALL be applied for the Application Profile are presented in Table 2.3 where by slash-separated entries denote alternative Function Modules and comma-separated entries denote requi rements for all specified Function Modules. 

|**Module Category**|**Required Function Modules**|
|---|---|
|Acquisition Hardware|FM AH-FI-FBS (for scan-of-photograph process) /<br>FM AH-FI-DC (for live-enrol<br>ment process using digital cameras) /<br>FM AH-FI-ICS,<br>FM AH-FI-SSS2 (for live-en<br>rolment process using self-service systems)<br>FM AH-FP-OPT (for Fingerprint Acqui<br>sition)|
|Acquisition Software|FM AS-FI-FBS/<br>FM AS-FI-DC,<br>FM AS-FP-SF/<br>FM AS-FP-MF|
|Biometric Image Processing|FM BIP-FI-FBS/<br>FM BIP-FI-GID,<br>FM BIP-FP-APP|
|Quality Assessment|FM QA-FI-PG,<br>FM QA-FI-PT,<br>FM QA-FI-GENERIC,<br>FM QA-FI-GID,<br>FM QA-<br>FP-APP|
|Presentation Attack Detection|FM PAD-FP-APP,<br>FM PAD-FI-APP1 (only applies for SSS but not until May 2025)|
|Compression|FM COM-FI-JP2,<br>FM COM-FI-JPG,<br>FM COM-FP-WSQR|
|Operation|FM O-ALL-USV,<br>FM O-FI-ALL,<br>FM O-FI-DC,<br>FM O-FI-FBS,<br>FM O-FP-ALL|
|User Interface|FM UI-FI-OP,<br>FM UI-FI-BSJ,<br>FM UI-FP-OP,<br>FM UI-FP-BSJ|
|Reference Storage|FM REF-FP-CHIP,<br>FM REF-FI-GID,<br>FM REF-FI-CHIP|
|Biometric Comparison|FM CMP-FP-VER (for control verifications if using a self-service system for finger<br>print acquisition)|
|Logging|FM LOG-ALL-GENERIC,<br>FM LOG-ALL-GID,<br>FM LOG-FI-GENERIC,<br>FM LOG-<br>FI-GID,<br>FM LOG-FP-GENERIC,<br>FM LOG-FP-GID|
|Coding|FM COD-ALL-GID,<br>FM COD-FI-GID,<br>FM COD-FP-GID|
|Evaluation|FM EVA-ALL-GID,<br>FM EVA-FI-GID,<br>FM EVA-FP-GID|



**Table 2.3** Required Function Modules Application Profile German Identity Card 

## 2.2.4 Mandatory Partial Application Processes 

All Partial Application Processes which SHALL be applied for the Application Profile are presented in Ta ble 2.4 whereby slash-separated entries denote alternative Partial Application Processes and comma-separa ted entries denote requirements for all specified Partial Application Processes. 

|**No.**|**Required Partial Application Process**|
|---|---|
|14|PAP ACQ-FI-SV-1: Supervised Facial Image Acquisition by Scanned Image|
|2|PAP ACQ-FP2P-SV-2: Supervised Acquisition of Two Plain Fingerprints on Single-Finger Hard<br>ware for Enrolment/<br>PAP ACQ-FP2P-SV-1: Supervised Acquisition of Two Plain Fingerprints on<br>Multi-Finger Hardware for Enrolment|



- 4 Note, as alternative the defined processes of the application profile are allowed. However, for these no dedicated Partial Application Processes exist. 

Federal Office for Information Security 

13 

2 Application Profiles 

|**No.**|**Required Partial Application Process**|
|---|---|
|3|PAP ACQ-FP2P-USV-2: Unsupervised Acquisition of Two Plain Fingerprints on Single-Finger<br>Hardware for Enrolment/<br>PAP ACQ-FP2P-USV-1: Unsupervised Acquisition of Two Plain Fin<br>gerprints on Multi-Finger Hardware for Enrolment (if a SSS is deployed)|



**Table 2.4** Required Partial Application Processes Application Profile German Identity Card 

## 2.3 Application Profile German Electronic Residence Permit 

The following Application Profile describes the application for a German Electronic Residence Permit. 

The requirements for the application of a German Electronic Residence Permit are determined by the [BIB_AufenthG], which mandates biometric characteristics to be included in the chip of the German Electro nic Residence Permit. These requirements are based on [BIB_EC_1030_2002]. 

By legal requirements, the inclusion of a facial image is mandatory, the inclusion of fingerprints for persons up to the age of six is not allowed but is mandatory for applicants older than six. 

## 2.3.1 Mandatory Process 

For the application of a German Electronic Residence Permit a facial image as well as two fingerprints of the applicant have to be captured electronically[5] . This is done in accordance with FM Category Acquisition Hardware, FM Category Acquisition Software and FM Category Biometric Image Processing. 

The resulting biometric data of the facial image and fingerprints can be reduced in size by lossy compression. However, multiple lossy compressions SHALL NOT be allowed. For facial images software-based quality as surance SHALL be conducted on the processed and compressed image data. For fingerprints, the compression SHALL be performed after the quality assurance process. The facial image and the fingerprint images as well as additional quality information, which is connected to the biometric data, SHALL be coded and then passed to the calling application. 

## 2.3.1.1 Overview Process 

Figure 2.15 depicts the biometric overview process of an application for a German Residence Permit. The process depicted is for illustration purpose only. Note, that the following section will detail this process for fingerprint and facial image acquisition. 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0022-12.png)


**----- Start of picture text -----**<br>
Acquire<br>Fingerprint<br>Images<br>Start End<br>Acquire Facial<br>Image<br>**----- End of picture text -----**<br>


**Figure 2.15.** Overview Process Biometric Application German Electronic Residence Permit 

## 2.3.1.2 Facial Image Acquisition Process 

The facial image acquisition application system SHALL implement one ore more of the processes defined by the following subsections: 

1. scan-of-photograph process 

- 5 Furthermore a signature is captured, too, but this is not part of the description within TR Biometrics. 

Federal Office for Information Security 

14 

2 Application Profiles 

2. live-enrolment process 

3. BSI [BIB_TR-03146] digital-transmission process 

In any case, a quality assurance module (software) in the facial image acquisition process SHALL be used. In case a facial image is deemed non-compliant by the quality assurance module, the official SHALL make a final decision regarding exceptions (based on legal rules) for further processing. 

## 2.3.1.2.1 Scan-of-Photograph Process 

The facial image MAY be acquired by scanning a photograph which the applicant hands over to the official. 

The photograph SHALL be compliant with the requirements for biometric images [BIB_ISO_FACE]. The offi cial manually verifies whether the photograph depicts the applicant. After the official visually inspected the facial image with the help of a photo guideline and, if needed, with the help of a photo template the facial image SHALL be scanned, refer to FM QA-FI-PT and FM QA-FI-PG. Afterwards, the facial image SHALL be processed by the quality assurance module (software). 

Figure 2.16 depicts the facial image acquisition process by scanning a photograph which the applicant hands over to the official. The process is defined in detail by PAP ACQ-FI-SV-1: Supervised Facial Image Acquisition by Scanned Image. 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0023-08.png)


**----- Start of picture text -----**<br>
Acquire Facial<br>Image<br>Start End<br>**----- End of picture text -----**<br>


PAP Supervised Facial Image Acquisition by Scanned Image 

**Figure 2.16.** Facial Image Acquisition Process by Scan of Photograph 

## 2.3.1.2.2 Live Enrolment Process 

The facial image MAY be acquired live at a SSS or in a studio set-up by the official. 

## **Self-Service System** 

Figure 2.17 depicts the overall facial image self-service acquisition process at the SSS and the counter. 

The facial image is acquired at the SSS. The official at the counter retrieves the acquired facial image. 

At the counter, the official SHALL verify the acquired facial image is of the applicant at the counter. The soft ware based quality metrics SHALL be displayed to the official. The official SHALL decide to accept or reject the facial image, i.e. he MAY follow the quality software decision or MAY overrule a negative software QA or MAY reject the facial image despite a positive software QA. 

Section 4.5.2 only applies for SSS but not until May 2025. 

Federal Office for Information Security 

15 

2 Application Profiles 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0024-01.png)


**----- Start of picture text -----**<br>
FM PAD-FI-APP1<br>(not until May 2025)<br>Acquire Facial<br>Image<br>Start<br>facial image<br>acquistion data<br>Reject Image<br>End<br>no no<br>acquired facial applicant by identity of imageVerifiy yes Assurance Results to DisplayQuality Offical Acquired Facial Assessment of Operator Image yes Release Image<br>Facial image  Accept image?<br>depicts applicant?<br>Self-Service System<br>Counter<br>**----- End of picture text -----**<br>


**Figure 2.17.** Facial Image Acquisition Process by an Unsupervised Self-Service System 

## **Studio Set-Up** 

Figure 2.18 depicts the overall facial image acquisition process in a studio set-up by an official, refer to FM AH-FI-DC for the studio set-up requirements. 

The facial image is acquired by the official with a digital camera. The software based quality metrics SHALL be determined and be displayed to the official. The official SHALL decide to accept or reject the facial image, i.e. the quality software decision MAY be followed or MAY be overruled in case of a negative software QA. In addition, the official MAY reject the facial image despite a positive software QA. 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0024-06.png)


**----- Start of picture text -----**<br>
FM AH-FI-DC<br>FM AS-FI-DC<br>Capture Facial<br>Image With<br>Camera<br>FM QA-FI-GID<br>Accept image?<br>Assess Display Operator<br>Quality of  Assurance Quality  Assessment of  yes Release Image<br>Captured Facial Results to  Acquired Facial<br>Start Image Offical Image End<br>no<br>Studio Set-Up<br>Offical<br>Counter<br>**----- End of picture text -----**<br>


**Figure 2.18.** Facial Image Acquisition Process in Studio Set-up by Official 

## 2.3.1.2.3 BSI TR-03146 Digital-Transmission Process 

The facial image MAY be transmitted to the counter by a photographer. 

Federal Office for Information Security 

16 

2 Application Profiles 

Figure 2.19 depicts the facial image acquisition process whereby the facial image acquisition is conducted detached from the counter office and is electronically transferred to the official counter. 

The image SHALL be acquired and compressed according to FM Category Acquisition Hardware, FM Cate gory Acquisition Software, FM Category Biometric Image Processing and FM Category Compression befo re transferring. The electronic transmission of the image SHALL comply to [BIB_TR-03146]. In order to gua rantee the connection between the facial image and the respective applicant, a manual verification SHALL be conducted by the official. In the successful case, the facial image SHALL be checked by the quality software. Finally, the operator SHALL have the option to give a veto in order to overrule the QA software decision. 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0025-03.png)


**----- Start of picture text -----**<br>
Photographer<br>Reject Image<br>Facial Image<br>no no<br>Start acquired facial applicant by  identity ofimageVerifiy Verified? yes retrieved facial Quality of Assessimage Results to OfficalDisplay Quality Assurance  Acquired Facial Assessment of Operator Image Accept image? yes Release Image End<br>FM QA-FI-GID<br>Counter<br>**----- End of picture text -----**<br>


**Figure 2.19.** Facial Image Acquisition Process by Digital Transmission of the Photograph 

## 2.3.1.3 Fingerprint Acquisition Process 

The fingerprint acquisition application system SHALL implement one or more of the following live-enrol ment processes defined in the following subsections: 

1. supervised live-enrolment process 

2. unsupervised self-service live-enrolment process 

## 2.3.1.3.1 Supervised Live Enrolment Process 

The fingerprint images MAY be acquired by a supervised acquisition process at the counter of the official. 

Figure 2.20 depicts the fingerprint acquisition process by a supervised acquisition at the counter of the offi cial. Depending on the type of fingerprint scanner at the counter, the detailed process is defined either detai led by PAP ACQ-FP2P-SV-2: Supervised Acquisition of Two Plain Fingerprints on Single-Finger Hardware for Enrolment or PAP ACQ-FP2P-SV-1: Supervised Acquisition of Two Plain Fingerprints on Multi-Finger Hardware for Enrolment. 

Federal Office for Information Security 

17 

2 Application Profiles 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0026-01.png)


**----- Start of picture text -----**<br>
FM FP-PAD-APP<br>Acquire<br>Fingerprint<br>Images<br>Start End<br>**----- End of picture text -----**<br>


PAP Supervised Acquisition of Two Plain Fingers on Single-Finger Hardware for Enrolment OR PAP Supervised Acquisition of Two Plain Fingers on Multi-Finger Hardware for Enrolment 

**Figure 2.20.** Fingerprint Acquisition by Supervised Live Enrolment 

## 2.3.1.3.2 Unsupervised Self-Service Live Enrolment Process 

The fingerprint images MAY be acquired by a unsupervised acquisition process at a SSS. 

Figure 2.21 depicts the overall fingerprint acquisition process at the SSS and the counter. 

The fingerprint is acquired at the SSS. The official at the counter retrieves the acquired fingerprints. 

The applicant’s fingerprints which have been acquired at the SSS SHALL additionally be acquired at the offi cial’s desk for verification according to FM Category Biometric Comparison. A verification comparison with the previously enrolled fingerprints at the SSS SHALL be conducted. Thereby, it is ensured that the legitimated applicant’s fingerprints have been captured at the live enrolment self-service station. In case the verification fails, the fingerprint enrolment SHALL be repeated at the official’s desk. 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0026-09.png)


**----- Start of picture text -----**<br>
PAP Unsupervised Acquisition of Two Finger Plain on Single-Finger Hardware for Enrolment OR<br>PAP Unsupervised Acquisition of Two Plain Fingers on Multi-Finger Hardware for Enrolment<br>Acquire<br>Fingerprint<br>Image<br>Start<br>FM FP-PAD-APP<br>fingerprint<br>acquistion data<br>no fingerprints and Discard  fingerprints and Discard<br>reacquire at  reacquire at<br>counter counter<br>yes Offical decides to<br>retry verification?<br>no no<br>Conduct Control Verfication results to OfficalDisplay PAD  Verification  yes Assurance Results of SSS to OfficalDisplay Quality  Fingerprint ImageAssessment of Acquired Operator  Accept  yes Release Image Default End<br>successful AND  fingerprints?<br>The finger  attack detected?no presentation<br>acquired at the<br>SSS SHALL be verified. FM CMP-FP-VER, FM FP-PAD-APP From SSS aquisition and aquisition for control verification<br>Self-Service System<br>Counter<br>**----- End of picture text -----**<br>


**Figure 2.21.** Fingerprint Acquisition Process by Unsupervised Self-Service Live Enrolment 

Federal Office for Information Security 

18 

2 Application Profiles 

## 2.3.2 Relevant Standards and Conditions 

In addition to the legal requirements (see above), further basic directives and standards SHALL be applicable: 

- [BIB_ICAO_9303] 

- [BIB_ISO_FINGER] 

- [BIB_ISO_FACE] 

## 2.3.3 Mandatory Function Modules 

All Function Modules which SHALL be applied for the Application Profile are presented in Table 2.5 where by slash-separated entries denote alternative Function Modules and comma-separated entries denote requi rements for all specified Function Modules. 

|**Module Category**|**Required Function Modules**|
|---|---|
|Acquisition Hardware|FM AH-FI-FBS (for scan-of-photograph process) /<br>FM AH-FI-DC (for live-enrol<br>ment process using digital cameras) /<br>FM AH-FI-ICS,<br>FM AH-FI-SSS2 (for live-en<br>rolment process using self-service systems)<br>FM AH-FP-OPT (for Fingerprint Acqui<br>sition)|
|Acquisition Software|FM AS-FI-FBS/<br>FM AS-FI-DC,<br>FM AS-FP-SF/<br>FM AS-FP-MF|
|Biometric Image Processing|FM BIP-FI-FBS/<br>FM BIP-FI-GID,<br>FM BIP-FP-APP|
|Quality Assessment|FM QA-FI-PG,<br>FM QA-FI-PT,<br>FM QA-FI-GENERIC,<br>FM QA-FI-GID,<br>FM QA-<br>FP-APP|
|Presentation Attack Detection|FM PAD-FP-APP,<br>FM PAD-FI-APP1 (only applies for SSS but not until May 2025)|
|Compression|FM COM-FI-JPG,<br>FM COM-FP-WSQR|
|Operation|FM O-ALL-USV,<br>FM O-FI-ALL,<br>FM O-FI-DC,<br>FM O-FI-FBS,<br>FM O-FP-ALL|
|User Interface|FM UI-FI-OP,<br>FM UI-FI-BSJ,<br>FM UI-FP-OP,<br>FM UI-FP-BSJ|
|Reference Storage|FM REF-FP-CHIP,<br>FM REF-FI-CHIP|
|Biometric Comparison|FM CMP-FP-VER (for control verifications if using a self-service system for finger<br>print acquisition)|
|Logging|FM LOG-ALL-GENERIC,<br>FM LOG-ALL-GID,<br>FM LOG-FI-GENERIC,<br>FM LOG-<br>FI-GID,<br>FM LOG-FP-GENERIC,<br>FM LOG-FP-GID|
|Coding|FM COD-ALL-GID,<br>FM COD-FI-GID,<br>FM COD-FP-GID|
|Evaluation|FM EVA-ALL-GID,<br>FM EVA-FI-GID,<br>FM EVA-FP-GID|



**Table 2.5** Required Function Modules Application Profile German Electronic Residence Permit 

## 2.3.4 Mandatory Partial Application Processes 

All Partial Application Processes which SHALL be applied for the Application Profile are presented in Ta ble 2.6 whereby slash-separated entries denote alternative Partial Application Processes and comma-separa ted entries denote requirements for all specified Partial Application Processes. 

|**No.**|**Required Partial Application Process**|
|---|---|
|16|PAP ACQ-FI-SV-1: Supervised Facial Image Acquisition by Scanned Image|
|2|PAP ACQ-FP2P-SV-2: Supervised Acquisition of Two Plain Fingerprints on Single-Finger Hard<br>ware for Enrolment/<br>PAP ACQ-FP2P-SV-1: Supervised Acquisition of Two Plain Fingerprints on<br>Multi-Finger Hardware for Enrolment|



> 6 Note, as alternative the defined processes of the application profile are allowed. However, for these no dedicated Partial Application Processes exist. 

Federal Office for Information Security 

19 

2 Application Profiles 

|**No.**|**Required Partial Application Process**|
|---|---|
|3|PAP ACQ-FP2P-USV-2: Unsupervised Acquisition of Two Plain Fingerprints on Single-Finger<br>Hardware for Enrolment/<br>PAP ACQ-FP2P-USV-1: Unsupervised Acquisition of Two Plain Fin<br>gerprints on Multi-Finger Hardware for Enrolment (if a SSS is deployed)|



**Table 2.6** Required Partial Application Processes Application Profile German Electronic Residence Permit 

Federal Office for Information Security 

20 

3 Partial Application Processes 

## 3 Partial Application Processes 

The Partial Application Process (PAP) specified by the following sections provide process specifications of basic biometric processes, e.g. the acquisition, identification or verification of biometrics or the evaluation processes for verification and identification. The processes are referenced by the relevant Application Profiles and are part of the overall processes specified by the relevant Application Profiles. 

A PAP MAY also be a task. A task is a process which functions as a generic reusable building block which is used by another PAP and is not referenced by an Application Profile directly. 

The specific Function Modules that SHALL be implemented in the processes of this chapter are specified by the relevant Application Profiles. 

## 3.1 PAP ACQ-FI-SV-1: Supervised Facial Image Acquisition by Scanned Image 

The facial image acquisition process described by this section applies to supervised acquisition situations whe re the facial image is acquired by an operator scanning a printed image, refer to Figure 3.1. 

A photo taken and printed by a photographer is provided by the biometric subject. At first, a visual check SHALL be performed by the operator, refer to Section 4.7 and Section 4.4. The operator SHALL manually verify whether the photo depicts the biometric subject. Depending on the result of the visual inspection, the photo is rejected or accepted for further processing. In the successful case, the image SHALL be digitised with a scanner by the operator, refer to Section 4.1, Section 4.2 and Section 4.3, and be compressed, refer to 

Section 4.6. Afterwards, the scanned image SHALL be subject to quality assessment, refer to Section 4.4. Finally, the operator SHALL have the option, to give a veto in order to overrule the QA software decision. 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0029-09.png)


**----- Start of picture text -----**<br>
Visual inspection  Biometric subject<br>result positive? is depicted on theprovided photo? Operator accepts<br>image?<br>Yes Yes Assess quality  Operator  Yes<br>Visual inspection Scan Image of image decision Release Image<br>Start End<br>No No<br>No<br>FM QA-FI-PG  FM QA-FI-GENERIC, FM QA-FI-PT,<br>FM QA-FI-PT FM QA-FI-GID FM QA-FI-PG<br>Reject Image<br>**----- End of picture text -----**<br>


**Figure 3.1.** Partial Application Process "Supervised Facial Image Acquisition by Scanned Image" 

In addition to the check by QA software, the operator MAY verify the geometric features of the image using a photo template (one for adults and one for children), refer to Section 4.4. If the operator gives a veto (veto equals yes) a negative software decision of the quality assessment SHALL be overruled and the facial image SHALL be released. The operator SHALL in addition have the option to reject an image despite a positive software QA decision. 

The process SHALL be supervised by an operator. 

## 3.2 PAP ACQ-FP2P-SV-2: Supervised Acquisition of Two Plain Fingerprints on Single-Finger Hardware for Enrolment 

Figure 3.2 depicts the acquisition process for two finger enrolment on single finger hardware. Note, that the PAP Task ACQ-FPP-SV-2: Capture Plain Fingerprint Supervised is used here. 

The process SHALL be supervised by an operator. 

Federal Office for Information Security 

21 

3 Partial Application Processes 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0030-01.png)


**----- Start of picture text -----**<br>
PAP Task<br>Capture Plain<br>Finger<br>Note: The selection of missing fingers MAY  PAP Task  Supervised<br>also be performed for both hands here. In this<br>Capture Plain<br>case, the task "Select missing fingers of left<br>hand" SHALL be omited. It is NOT REQUIRED to support both variants. Finger Supervised PAD Warning to Display Official Capture Plain Finger (outcome finger of pervious capture)<br>At least one right<br>hand finger<br>available? yes<br>Select  yes Capture Plain  no<br>missing fingers  Finger (right<br>of right hand hand finger) The counter i<br>Start PAD Warning  SHALL be inialized<br>no present for right  with 3.<br>hand finger?<br>Note: If the captured finger did not yield to sufficient quality,<br>at least one aditional finger of the same hand in order of<br>priority SHOULD be captured. If none of the captured fingers<br>yield to sufficient quality, the finger with the highest quality<br>score SHALL be accepted. The finger to capture SHOULD be<br>Display<br>Capture Plain Finger (outcome finger  selected by the following ordered priority: index, thumb, middle<br>PAD Warning to<br>of pervious capture) Offical finger, ring finger.<br>At least one left<br>yes hand finger available?<br>Note: The finger acquired in  no Capture Plain  yes Select<br>Finger (left hand  missing fingers<br>this step SHALL be different from the already accepted  PAD Warning  finger) of left hand<br>finger. The finger to capture present for left  no<br>SHOULD be selected by  PAP Task  hand finger?<br>the following ordered  Capture Plain<br>priority: index, thumb,  Finger<br>middle finger, ring finger.  Supervised<br>If none of the fingers yield<br>to sufficient quality, the  All fingers of one The counter i  PAP Task<br>finger with the highest  hand are missing  SHALL be inialized  Capture Plain<br>quality score is accepted.  and at least two  with 3. Finger<br>If fingers have already been fingers of the  Supervised<br>captured before hand, they  other hand are<br>can be reused in this step  available?<br>to avoid multiple captures<br>of the same finger. no<br>yes End<br>no<br>Capture Plain Finger (additional finger  yes Display  Capture Plain Finger (outcome finger<br>PAD Warning to<br>from existing hand) Offical of pervious capture)<br>PAD Warning<br>present for<br>additional finger?<br>**----- End of picture text -----**<br>


**Figure 3.2.** Partial Application Process "Supervised Acquisition of Two Plain Fingerprints on Single-Finger Hardware for Enrolment" 

## 3.2.1 PAP Task ACQ-FPP-SV-2: Capture Plain Fingerprint Supervised 

Figure 3.3 depicts the basic supervised capture sequence for a plain fingerprint capture. A plain fingerprint capture can be part of more complex acquisition processes, e.g. a ten finger acquisition by the 4-1-4-1 capture sequence. The plain fingerprint capture is described in detail subsequently. The quality assessment is conduc ted according to the requirements of the applicable FM Category Quality Assessment. 

1. The counter variable for the number of attempts for capturing the current slap SHALL be initialized as _i_ = 0. 

2. The fingerprint image SHALL be retrieved from hardware. 

3. The fingerprint SHALL be assessed and the captured fingerprint and parameter data (e.g. quality values) SHALL be temporarily stored. 

4. In case the quality requirements for the fingerprint is not met, the capture SHALL be repeated up to two times (i.e. the acquisition of a finger consists of a maximum of three capture attempts). The counter SHALL be set to _i_ = _i_ + 1. 

5. A sequence check SHALL be conducted for the captured fingerprint image to detect the capture of wrong fingers, e.g. due to interchanged hands or multiple acquisition of the same hand or finger. Note: It is RE COMMENDED to conduct the sequence check as early as possible after a fingerprint image is available. 

Federal Office for Information Security 

22 

3 Partial Application Processes 

- a. In case the comparison of the current fingerprint with any previously captured fingerprint is success ful, the sequence check SHALL report an error. 

- b. In case the comparison of the current fingerprint with any previously captured fingerprint is not suc cessful, the sequence check SHALL NOT report an error. 

If the quality check of the third capture attempt fails (counter _i_ is set to 3), the best of the captured fingerprint images SHALL be identified according to the corresponding QA Function Module and temporarily stored along with the corresponding information. 

The process SHALL be supervised by an operator. 

At the end of the process the operator decides on one of the three options: 

1. Use the acquired fingerprint. 

2. Recapture the current fingerprint. The counter SHALL be reset to _i_ = 1. 

3. Restart the total fingerprint acquisition workflow. 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0031-09.png)


**----- Start of picture text -----**<br>
Discard<br>all previously  Set i = 1<br>acquired images<br>FM FP-QA<br>Case A:The<br>Identifiy best fingerprint Case B: The operator decides to recapture the  operator decides to use the acquired<br>current finger. fingerprint image.<br>Fingerprint is of  FM UI-FP-OP Case B<br>Perform PAD insufficient quality<br>and i = 3<br>Start Initialize variablei = 1 Retrieve  Assess quality of fingerprint insufficient qualityFingerprint is of and i < 3sufficient qualityFingerprint is of Sequence check FP images and Show acquired results of PAD and sequence check Case C Case A Default End<br>fingerprint from<br>hardware Case C: The operator decides to<br>Note: The captured fingerprint SHALL be compared with each already accepted fingerprint of the current acquistion process. restart the total fingerprint acquisition workflow.<br>However, it is RECOMMENDED to conduct the sequence  Restart total<br>Set i = i +1 check as early as possible after a new fingerprint is available. acquisition fingerprint<br>workflow<br>**----- End of picture text -----**<br>


**Figure 3.3.** Partial Application Process Task "Capture Plain Fingerprint Supervised" 

## 3.3 PAP ACQ-FP2P-SV-1: Supervised Acquisition of Two Plain Fingerprints on Multi-Finger Hardware for Enrolment 

Figure 3.4 depicts the acquisition process for two finger enrolment on multi finger hardware. Note, that the PAP Task ACQ-FPS-SV-1: Capture Slap Supervised is used here. 

The process SHALL be supervised by an operator. 

Federal Office for Information Security 

23 

3 Partial Application Processes 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0032-01.png)


**----- Start of picture text -----**<br>
Execute PAP<br>Supervised<br>Acquisition of Two<br>Plain Fingers on<br>Single-Finger<br>Hardware for  Both index fingers<br>no Enrolment are of sufficient<br>quality?<br>Select yes Capture Slap  yes<br>missing fingers  Supervised<br>of both hands (index fingers)<br>Start Both index fingers no Default End<br>are available?<br>Capture Plain Fingerprint<br>(alternative finger(s))<br>PAP Task<br>Capture Slap<br>Supervised<br>Note: The fingers to capture SHALL be selected by the following<br>ordered priority (right, then left hand) thumb, middle finger, ring<br>finger. If a finger did not yield to sufficient quality, at least one<br>additional finger in order of their priority SHALL be captured until<br>sufficient quality is yield for a finger or the operator stops<br>acquisition of further available fingers. If none of the captured<br>fingers yield to sufficient quality, the finger with the highest quality<br>score is accepted. If two fingers yield same quality values, the<br>finger with the higher priority is accepted.<br>**----- End of picture text -----**<br>


**Figure 3.4.** Partial Application Process "Supervised Acquisition of Two Plain Fingerprints on Multi-Finger Hardware for Enrolment" 

## 3.3.1 PAP Task ACQ-FPS-SV-1: Capture Slap Supervised 

Figure 3.5 depicts the basic process for a plain supervised slap capture. A plain slap capture can be part of more complex acquisition processes, e.g. a ten finger acquisition by the 4-1-4-1 capture sequence. The plain slap capture is subsequently described in detail. The quality assessment is conducted according to the requi rements of the applicable FM Category Quality Assessment. Note, that the PAP Task ACQ-FPP-SV-2: Cap ture Plain Fingerprint Supervised is used here. 

If the biometric subject is physically not capable to place all fingers of the slap on the capture hardware at the same time to achieve a good quality image, the operator can decide to capture each finger of the slap in single finger capture mode. This SHALL be possible during the entire process. Hereby, single finger capture mode refers to the PAP Task ACQ-FPP-SV-2: Capture Plain Fingerprint Supervised as described below. 

1. The counter variable for the number of attempts for capturing the current slap SHALL be initialized as _i_ = 1. 

2. The slap image SHALL be retrieved from hardware. While the image is retrieved from hardware, presen tation attack detection (PAD) SHALL be performed. 

3. The fingerprints SHALL be segmented and each SHALL be assessed. 

   - a. In case the quality of the fingerprints meets the quality requirements defined in the corresponding QA Function Module, the captured slap and the set of segmented fingerprints and parameter data (e.g. quality values) SHALL be temporarily stored. 

   - b. In case the quality requirements for one or more fingerprints of the slap are not met, the capture SHALL be repeated up to two times (i.e. the acquisition of a single slap consists of a maximum of three capture attempts). The counter SHALL be set to _i_ = _i_ + 1. 

4. A sequence check SHALL be conducted for the captured slap image to detect the capture of wrong fingers, e.g. due to interchanged hands or multiple acquisition of the same hand or finger. Note, that it is RECOM MENDED to conduct the sequence check as early as possible after a fingerprint image is available. 

Federal Office for Information Security 

24 

3 Partial Application Processes 

   - a. In case the comparison of any fingerprint of the current slap with any previously accepted fingerprint of a previous slap is successful, the sequence check SHALL show a warning. 

   - b. In case the comparisons of all fingerprints of the current slap with all fingerprints of previous slaps are not successful, the sequence check SHALL NOT show a warning. 

5. Generally, a slap classifier SHALL be used for the captured slap image to detect the capture of the wrong slap. It SHALL be configurable to switch the classifier off or in evaluation mode (logging of the result wi thout showing the result/error to the operator). Note, that the slap classifier is only required for 4 finger slaps. Other acquisitions currently do not require the corresponding FM. 

   - a. If the result of the classification concludes that the acquired slap mismatches the expected slap, an error SHALL be thrown. 

   - b. If the result of the classification concludes that the acquired slap matches the expected slap, no error SHALL be thrown. 

If the quality check of the third capture attempt fails (counter _i_ is set to 3), the best of the captured slaps SHALL be identified according to the corresponding QA Function Module and temporarily stored along with the corresponding information. 

The process SHALL be supervised by an operator. 

At the end of the process the operator decides on one of the three options: 

1. Use the acquired slap. 

2. Recapture the current slap. The counter SHALL be reset to _i_ = 1. 

3. Restart the total slap acquisition workflow. 

At any point of the process the operator MAY decide to acquire any finger of the slap individually. 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0033-13.png)


**----- Start of picture text -----**<br>
Discard<br>all Previously  Set i = 1<br>Acquired Images<br>FM AS-FP-SLP<br>FM QA-FP Case B: The operator<br>decides to recapture the<br>Here, no  Classify Slap current slap.<br>Start Initialize variablei = 1 Perform PAD Assess Quality of Slap quality ANDinsufficientSlap is of i < 3 No Slap is of sufficientquality Yes sufficient qualityimplies i=3 Sequence Check Yes No FM UI-FP-OPFP images and seq. check and Show acquired results of PAD,  Case B Case A: The operator decidesto use the acquired slapCase A Default End<br>In case difficulties occur in  from hardwareRetrieve slap  Yes No Best SlapIdentifiy 4 Finger Slap? slap class. Case C<br>the process (e.g. biometric  of Captured Slaps<br>subject is not capable to placefingers of slap on scanner) switch to single finger acquisition mode. Set i = i + 1 FM QA-FP Case C: The operator decides to restart the total slap acquisition workflow. Restart total slap acquisition workflow<br>PAP Task Capture Plain Finger<br>Acquire each Supervised<br>finger(s) of slap in<br>single finger<br>acquisition mode<br>**----- End of picture text -----**<br>


**Figure 3.5.** Partial Application Process Task "Capture Slap Supervised" 

## 3.3.1.1 PAP Task ACQ-FPP-SV-2: Capture Plain Fingerprint Supervised 

Figure 3.3 depicts the basic supervised capture sequence for a plain fingerprint capture. A plain fingerprint capture can be part of more complex acquisition processes, e.g. a ten finger acquisition by the 4-1-4-1 capture sequence. The plain fingerprint capture is described in detail subsequently. The quality assessment is conduc ted according to the requirements of the applicable FM Category Quality Assessment. 

1. The counter variable for the number of attempts for capturing the current slap SHALL be initialized as _i_ = 0. 

2. The fingerprint image SHALL be retrieved from hardware. 

3. The fingerprint SHALL be assessed and the captured fingerprint and parameter data (e.g. quality values) SHALL be temporarily stored. 

Federal Office for Information Security 

25 

3 Partial Application Processes 

4. In case the quality requirements for the fingerprint is not met, the capture SHALL be repeated up to two times (i.e. the acquisition of a finger consists of a maximum of three capture attempts). The counter SHALL be set to _i_ = _i_ + 1. 

5. A sequence check SHALL be conducted for the captured fingerprint image to detect the capture of wrong fingers, e.g. due to interchanged hands or multiple acquisition of the same hand or finger. Note: It is RE COMMENDED to conduct the sequence check as early as possible after a fingerprint image is available. 

   - a. In case the comparison of the current fingerprint with any previously captured fingerprint is success ful, the sequence check SHALL report an error. 

   - b. In case the comparison of the current fingerprint with any previously captured fingerprint is not suc cessful, the sequence check SHALL NOT report an error. 

If the quality check of the third capture attempt fails (counter _i_ is set to 3), the best of the captured fingerprint images SHALL be identified according to the corresponding QA Function Module and temporarily stored along with the corresponding information. 

The process SHALL be supervised by an operator. 

At the end of the process the operator decides on one of the three options: 

1. Use the acquired fingerprint. 

2. Recapture the current fingerprint. The counter SHALL be reset to _i_ = 1. 

3. Restart the total fingerprint acquisition workflow. 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0034-11.png)


**----- Start of picture text -----**<br>
Discard<br>all previously  Set i = 1<br>acquired images<br>FM FP-QA<br>Case A:The<br>Identifiy best fingerprint Case B: The operator decides to recapture the  operator decides to use the acquired<br>current finger. fingerprint image.<br>Fingerprint is of  FM UI-FP-OP Case B<br>Perform PAD insufficient quality<br>and i = 3<br>Start Initialize variablei = 1 Retrieve  Assess quality of fingerprint insufficient qualityFingerprint is of and i < 3sufficient qualityFingerprint is of Sequence check FP images and Show acquired results of PAD and sequence check Case C Case A Default End<br>fingerprint from<br>hardware Case C: The operator decides to<br>Note: The captured fingerprint SHALL be compared with each already accepted fingerprint of the current acquistion process. restart the total fingerprint acquisition workflow.<br>However, it is RECOMMENDED to conduct the sequence  Restart total<br>Set i = i +1 check as early as possible after a new fingerprint is available. acquisition fingerprint<br>workflow<br>**----- End of picture text -----**<br>


**Figure 3.6.** Partial Application Process Task "Capture Plain Fingerprint Supervised" 

## 3.4 PAP ACQ-FP2P-USV-2: Unsupervised Acquisition of Two Plain Fingerprints on Single-Finger Hardware for Enrolment 

Figure 3.7 depicts the unsupervised acquisition process for two finger enrolment on single finger hardware. Note, that the PAP Task ACQ-FPP-USV-1: Capture Plain Fingerprint Unsupervised as defined below is used here. 

Note, in case the acquisition system is equipped with two single-fingerprint scanners, the simultaneous ac quisition of two fingers with equal finger type from different hands (e.g. both index fingers) SHALL be allowed. 

Note, in case a supervised acquisition at a supervised downstream system is possible, the implementation of the unsupervised process MAY only include the flow of sufficient quality acquisitions and abort in case suffi cient quality is not yield. In this situation, the acquisition SHALL be conducted at the downstream supervised system. 

Federal Office for Information Security 

26 

3 Partial Application Processes 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0035-01.png)


**----- Start of picture text -----**<br>
Biometric subject indicates  No or only one right hand finger with<br>that the fingerprint is  unsufficient quality has already been<br>physically temorary OR  FM QA-FP-APP captured AND at least on finger of<br>permanently impossible to  the right hand has not already been<br>capture? tried to be captured?<br>Yes<br>Guide bio-<br>metric subject to  No Capture Fingerprint Unsupervised  Quality  No<br>place right hand  (right hand finger) Assessment<br>finger on scanner<br>Start<br>Yes<br>The finger to capture SHALL be selected by<br>the following ordered priority: index, thumb,  No or only one left hand finger with<br>middle finger, ring finger. In case a finger is  unsufficient quality has already<br>not available or is of unsufficient quality, the  been captured AND at least on<br>next finger of the order list SHALL be chosen. FM QA-FP-APP finger of the left hand has not<br>already been tried to be captured?<br>Yes<br>Guide bio-<br>metric subject to  No Capture Fingerprint Unsupervised Quality  No<br>place left hand  (left hand finger) Assessment<br>finger on scanner<br>Yes<br>Biometric subject indicates that the fingerprint is<br>physically temorary or permanently impossible to<br>capture?<br>Note: The fingerprint acquired in this step SHALL be different from the<br>No already accepted fingerprints. The finger to capture SHALL be selected by the following ordered priority: index, thumb, middle finger, ring finger.<br>If a fingerprint did not yield to sufficient quality, at least on<br>All fingers of one additional finger in order of priority SHALL be captured until sufficient<br>hand are missing  Yes End quality is yield for a fingerprint. This fingerprint SHALL be accepted. If<br>AND at least one  none of the fingerprints yield to sufficient quality, the fingerprint with<br>finger of the  the highest quality score SHALL be accepted. If fingerprints have<br>other hand has  already been captured before hand, they can be reused in this step to<br>not been skipped  Capture Fingerprint Unsupervised  avoid multiple captures of the same fingerprint.<br>due to physically  (additional finger from existing hand)<br>impossibility to<br>capture?<br>**----- End of picture text -----**<br>


**Figure 3.7.** Partial Application Process "Unsupervised Acquisition of Two Plain Fingerprints on Single-Finger Hardware for Enrolment" 

## 3.4.1 PAP Task ACQ-FPP-USV-1: Capture Plain Fingerprint Unsupervised 

Figure 3.8 depicts the basic process for a plain unsupervised fingerprint capture. A plain fingerprint capture can be part of more complex acquisition processes, e.g. a ten finger acquisition. The plain unsupervised fin gerprint capture is subsequently described in detail. The QA is conducted according to the requirements of the applicable Section 4.4. 

1. The fingerprint image SHALL be retrieved from hardware. 

2. The fingerprint SHALL be assessed. 

   - a. The PAD SHALL be carried out. 

   - b. The sequence check SHALL be conducted. 

      - i. If the sequence check fails for the first time for a finger: 

The captured image SHALL be discarded. 

A warning message that a sequence error was detected SHALL be displayed to the user. 

Federal Office for Information Security 

27 

3 Partial Application Processes 

The capture SHALL be repeated. 

   - ii. If the sequence check fails for the second time for the same finger, the acquisition process, described in this chapter, SHALL end without an acquired fingerprint. 

   - iii. If the sequence check yields to no error, the QA SHALL be conducted. 

- c. In case the quality of the fingerprint meets the quality requirements defined in the corresponding Section 4.4, the captured fingerprint and parameter data (e.g. quality values) SHALL be temporarily 

- stored. 

- d. QA SHALL be conducted within 300 ms. 

- e. Slap classification SHALL be performed, if configured and SHALL be conducted within 300 ms. Slap classification MAY be done for evaluation purpose only. 

- f. In case the timeout is reached and no fingerprint image of sufficient quality was captured, the best fingerprint image according to the corresponding QA Function Module and corresponding parameter data (e.g. quality values) SHALL be stored. 

- g. In case the quality requirements for the fingerprint is not met, the capture SHALL be repeated if the timeout is not reached. The timeout SHALL start with the try of retrieval of the first fingerprint image from hardware and SHALL be configurable. 

- h. With optimal conditions (bona fide) the overall fingerprintt capture process SHALL NOT exceed five seconds. 

If a second sequence error occurs, an error message SHALL be returned to the calling process. 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0036-11.png)


**----- Start of picture text -----**<br>
guidance to put correct finger on scannerDisplay  warning message that a sequence error was detectedDisplay all Captured DiscaredImages<br>no sequence error FM QA-FP<br>occurred<br>FM PAD-FP beforehand and the fingerprint  Identifiy<br>matches one  Best Fingerprint<br>fingerprint  Fingerprint is of  of Captured<br>acquired  insufficient  Fingerprints<br>Perform PAD beforehand timeout  exceededquality and<br>Fingerprint is of<br>Sequence  else Assess Quality  sufficient quality<br>Check of Fingerprint<br>Start Default End<br>fingerprint fromRetrieve  second sequence error occured The timeout SHALL be configurable. The<br>hardware start of the timeout<br>The sequence check SHALL be executed if at least one  Fingerprint is of insufficient  SHALL be the start of retrieval of the<br>different fingerprint has  quality and  first finger from<br>been acquired beforehand timeout has not  hardware.<br>FM AH-FP, FM exceeded<br>AS-FP<br>**----- End of picture text -----**<br>


**Figure 3.8.** Partial Application Process Task "Capture Plain Fingerprint Unsupervised" 

## 3.5 PAP ACQ-FP2P-USV-1: Unsupervised Acquisition of Two Plain Fingerprints on Multi-Finger Hardware for Enrolment 

Figure 3.9 depicts the unsupervised acquisition process for two finger enrolment on multi finger hardware. Note, that the PAP Task ACQ-FPS-USV-1: Capture Slap Unsupervised is used here. The sequence is described in detail subsequently: 

1. Acquire right index finger, left index finger (as two-finger slap). 

2. In case of insufficient index finger quality, alternative finger(s) SHOULD be acquired for each index finger of insufficient quality. First further fingers from the right hand SHALL be acquired in single-finger mode (if any available), then further fingers from the left hand. Further fingers are considered in the following order: thumb, middle finger, ring finger. The index fingers are not recaptured. 

3. In any case, at least one further finger (if available) for each hand SHALL be acquired if the index finger does not fulfil the quality requirements. Note, the fingers to capture SHOULD be selected by the following 

Federal Office for Information Security 

28 

3 Partial Application Processes 

ordered priority (right, then left hand) thumb, middle finger, ring finger. If a fingerprint did not yield to sufficient quality, additional fingers in order of their priority SHALL be captured until sufficient quality is yield for a fingerprint or the operator stops acquisition of further available fingers (at least one alternative finger SHALL be captured). If none of the captured fingerprints yield to sufficient quality, the fingerprint with the highest quality score is accepted. If two fingerprints yield same quality values, the fingerprint with the higher priority is accepted. 

Note, in case a supervised acquisition at a supervised downstream system is possible, the implementation of the unsupervised process MAY only include the flow of sufficient quality acquisitions and abort in case suffi cient quality is not yield. In this situation, the acquisition SHALL be conducted at the downstream supervised system. 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0037-03.png)


**----- Start of picture text -----**<br>
PAP Task<br>Capture Slap<br>Unsupervised Capture Plain Fingerprint Unsupervised<br>(alternative finger(s))<br>Both index fingers no<br>available?<br>Guide bio-<br>metric subject yes Capture Slap<br>Unsupervised<br>to place both index<br>(index fingers) yes<br>fingers on scanner<br>Start Default End<br>Both index finger<br>no are of sufficient<br>quality? Note: The fingers to capture SHOULD be selected by the following<br>ordered priority (right, then left hand) thumb, middle finger, ring finger. If a<br>fingerprint did not yield to sufficient quality, additional fingerprints in<br>order of their priority SHALL be captured until sufficient quality is yield for<br>i.e. ask for the capture of the fingers but give  a finger or the operator stops acquisition of further available fingers (at<br>the option to skip by naming the option  Execute "PAP  least one alternative finger SHALL be captured). If none of the captured<br>"finger(s) physically temporary or permanently  Unsupervised  fingerprints yield to sufficient quality, the fingerprint with the highest<br>impossible to capture" Two Finger  quality score is accepted. If two fingerprints yield same quality values, the<br>Enrolment on  fingerprint from the finger with the higher priority is accepted.<br>Single Finger<br>Hardware"<br>**----- End of picture text -----**<br>


**Figure 3.9.** Partial Application Process "Unsupervised Acquisition of Two Plain Fingerprints on Multi-Finger Hardware for Enrolment" 

## 3.5.1 PAP Task ACQ-FPS-USV-1: Capture Slap Unsupervised 

Figure 3.10 depicts the basic process for a plain unsupervised slap capture. A plain slap capture can be part of more complex acquisition processes, e.g. a ten finger acquisition by the 4-1-4-1 capture sequence. The plain unsupervised slap capture is subsequently described in detail. The quality assessment is conducted according to the requirements of the applicable FM Category Quality Assessment. 

In a sequence check, each segmented finger of the current slap SHALL be compared with each already accepted finger of the current acquisition process. Note, this is only required in case more than one slap is captured within the acquisition process. 

1. The slap image SHALL be retrieved from hardware. 

2. The fingerprints SHALL be segmented and each SHALL be assessed. 

   - a. The PAD SHALL be carried out. 

   - b. The sequence check SHALL be conducted. 

Federal Office for Information Security 

29 

3 Partial Application Processes 

- i. If the sequence check fails, the captured image SHALL be discarded and the capture repeated, but if the sequence check fails for the second time for the same finger, the acquisition process, described in this chapter, SHALL end without an acquired slap. 

ii. If the sequence check yields to no error, the quality assessment SHALL be conducted. 

- c. In case the quality of the fingerprints meet the quality requirements defined in the corresponding Section 4.4, the captured slap and the set of segmented fingerprints and parameter data (e.g. quality 

- values) SHALL be temporarily stored. 

- d. In case the timeout is reached and no slap image of sufficient quality was captured, the best slap image according to the corresponding QA Function Module SHALL be stored with the set of segmented fin gerprints and parameter data (e.g. quality values). 

- e. In case the quality requirements for one or more fingerprints of the slap are not met, the capture SHALL be repeated if the timeout is not reached. The timeout SHALL start with the try of retrieval of the first slap image from hardware and SHALL be configurable. 

- f. With optimal conditions (bona fide) the overall finger slap capture process SHALL NOT exceed ten seconds. 

- g. Generally, a slap classifier SHALL be used for the captured slap image to detect the capture of the wrong slap. It SHALL be configurable to switch the classifier off or in evaluation mode (logging of the result without showing the result/error to the operator). Note, that the slap classifier is only required for 4 finger slaps. Other acquisitions currently do not require the corresponding FM. 

   - i. If the result of the classification concludes that the acquired slap mismatches the expected slap, an error SHALL be thrown. 

   - ii. If the result of the classification concludes that the acquired slap matches the expected slap, no error SHALL be thrown. 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0038-10.png)


**----- Start of picture text -----**<br>
FM UI-FP-BSJ<br>slap on scannerto put correct guidanceDisplay  all captured Discardimages no sequence error occurred  FM QA-FP-APP<br>beforehand and at<br>least one finger<br>matches one<br>finger of a  Slap is of  Identifiy<br>different slap  insufficient  Best Slap of<br>FM AH-FP-OPT, FM PAD-FP-APP beforehandacquired  timeout  exceededquality and  Captured Slaps<br>FM AH-FP-SSS<br>Slap is of<br>sufficient quality<br>HardwareSlap from Retrieve Perform PAD Sequence Check else Assess Quality of Slap Classify Slap timeout exceeded and correct slap and potentially incorrect slap acquired or<br>Start acquired Default End<br>second sequence  FM AS-FP-SLP<br>The sequence check SHALL be executed if at least one different slap has been acquired beforehand. error occured insufficient potentially (Slap is of quality or  The timeout SHALL be configurable. The start ofthe timeout SHALL be<br>incorrect slap  the start of retrieval of<br>Timeout has not acquired) and exceeded the first slap from hardware.<br>**----- End of picture text -----**<br>


**Figure 3.10.** Partial Application Process Task "Capture Slap Unsupervised" 

Federal Office for Information Security 

30 

4 Function Modules 

## 4 Function Modules 

This chapter lists all the Function Modules (FMs) for the defined Application Profiles. 

## 4.1 FM Category Acquisition Hardware 

Devices that are used for digitising physical, representable biometric characteristics are called Acquisition Hardware (AH). Scanners for capturing photographs, digital cameras to capture images of the face, fingerprint sensors, or signature tablets can be named as examples. 

## 4.1.1 FM AH-FI-FBS 

This function block describes the requirements and interfaces in particular for flat bed scanners that are used to scan photos for enrolment purposes. 

## 4.1.1.1 Requirements 

- The minimum physical resolution of the scanner SHALL be 300 ppi. 

- Adequate image quality to meet the requirements of [BIB_ISO_FACE] SHALL be provided. 

## 4.1.2 FM AH-FI-DC 

This Function Module describes the requirements for digital cameras and physical setup that are used to obtain facial biometrics. 

## 4.1.2.1 Requirements 

- The minimum physical resolution of the camera SHALL allow a cropping of an image to 1600x1200 pixels without any up-scaling. 

- Adequate image quality to meet the requirements of [BIB_ISO_FACE] SHALL be provided. 

- The physical and environmental conditions for capturing facial photos, such as the positioning of the ca mera, proper lighting of the face and a uniform background as described in [BIB_ISO_FACE] SHALL be complied with. 

## 4.1.3 FM AH-FI-ICS 

This Function Module describes the requirements for integrated camera systems that are used to obtain digi tised facial images. 

## 4.1.3.1 Requirements 

- The camera SHALL be able to capture a frontal image of the person if the person is looking straight to the camera. 

- The camera system SHALL use diffuse lighting which SHALL adapt to the environmental light conditions for a uniform illumination of the biometric subject's face to ensure the capture of a well-exposed facial image; mirroring effects of glasses SHALL be avoided. 

- The system SHALL allow high quality acquisitions independently from the environmental light situation that can usually be found in the environment in question. 

- The camera system SHALL guarantee the sharpness of the captured image within the designated capture area. 

- The camera system SHALL minimise the distortion of the captured face within the whole capture area. 

- The minimum physical resolution of the captured facial image SHALL be at least 1200 x 1600 pixels without any up-scaling. Note, this requirement is not MANDATORY for scenarios where only a facial verification is performed. 

- The camera system SHALL be able to capture images in colour (24 bit RGB). Note, this requirement is not MANDATORY for scenarios where only a facial verification is performed. 

Federal Office for Information Security 

31 

4 Function Modules 

## 4.1.3.2 Recommendations 

The camera system MAY provide a feedback screen for displaying the camera live acquisition image (digital mirror). If the biometric subject is looking straight to the feedback screen the viewing direction of the person SHALL be frontal. The feedback SHALL include guidance to help the biometric subject for correct positioning in front of the camera. 

## 4.1.4 FM AH-FI-SSS2 

This Function Module describes the requirements for self-service systems scenarios where a digitised facial image is obtained. Note, the distance between camera system and biometric subject is defined as the horizontal distance between the forehead of the biometric subject to the active camera system's optic. 

## 4.1.4.1 Requirements 

- The system MAY measure the distance between the biometric subject and the camera system. 

- The camera system SHALL NOT require the biometric subject to rotate its standing position while interac ting with the graphical user interface in order to look straight to the camera system. 

- The camera system SHALL at least allow to acquire facial images compliant to this Technical Guideline of biometric subject which have a body height in range of 140 cm to 200 cm if standing upright in front of the camera system. 

- If the biometric subject is standing at maximum in 130 cm[1] distance to the camera system, the minimum physical resolution of the camera system SHALL allow to crop the full frontal facial image of the biometric subject to 640 x 480 pixels with an allowed deviation of maximum negative 10 %. 

- The camera system SHALL at least capture sharp full frontal images with minimized distortion of biometric subjects which 

   - stand upright 70 cm in front of the camera system to 120 cm[2] back of the camera system and 

   - look frontal. 

- If the biometric subject is in the capture area of maximum 120 cm distance to the camera system, the camera installation SHALL be able to capture an image according to the definition of "full frontal" (see [BIB_ISO_FACE]) on a hardware level. Especially an image capturing at "Frankfurt Horizon" SHALL be pos sible for all biometric subjects within the defined range of body height. 

## 4.1.5 FM AH-FP-OPT 

This Function Module describes the requirements for high quality fingerprint scanners (single finger and mul ti finger). 

## 4.1.5.1 Requirements 

- For the acquisition of the fingerprints, optical sensors using the principal of frustrated total reflection or direct contact (the imaging system is the sensor surface, typically separated by a transparent protection layer) according to the certification requirements of [BIB_ISO_FINGER] (especially this means a resolution of 500 ppi or 1000 ppi) SHALL be used exclusively. 

- For the acquisition of the fingerprints, only devices are permitted which meet the following requirements (in analogy to [BIB_EBTS/F]). Notwithstanding, a capturing area of at minimum 16 mm width and 20 mm height is REQUIRED (deviating from table F 1 in [BIB_EBTS/F]) for single finger scanners. 

## 4.1.5.1.1 Grey Scale Linearity 

When measuring a stepped series of uniform target reflectance patches ("step tablet") that substantially covers the scanner's grey range, the average value of each patch SHALL be within 7.65 grey levels of a linear, least 

> 1 Note, that the physical construction of the system may not allow the biometric subject to stand at the maximum distance. 

> 2 Note, that the physical construction of the system may not allow the biometric subject to stand at the maximum distance. 

Federal Office for Information Security 

32 

4 Function Modules 

squares regression line fitted between target reflectance patch values (independent variable) and scanner out put grey levels of 8 bit resolution (dependent variable). 

## 4.1.5.1.2 Resolution and Geometrical Accuracy 

Resolution: The scanner's final output fingerprint image SHALL have a resolution, in both sensor detector row and column directions, in the range: ( _R ¡_ 0 _:_ 01 _R_ ) to ( _R_ + 0 _:_ 01 _R_ ). The magnitude of _R_ is either 500 ppi or 1000 ppi; a scanner MAY be certified at either one or both of these resolution levels. The scanner's true optical resolution SHALL be greater than or equal to _R_ . 

Across-Bar geometric accuracy: When scanning a 1.0 cy/mm, multiple parallel bar target, in both vertical bar and horizontal bar orientations, the absolute value of the difference ( _D_ ) between the actual distance across parallel target bars ( _X_ ), and the corresponding distance measured in the image ( _Y_ ) SHALL NOT exceed the following values for at least 99 % of the tested cases in each print block measurement area and in each of the two directions: 

- for 500 ppi scanners: 

_D ·_ 0 _:_ 0007, for 0 _:_ 00 _< X ·_ 0 _:_ 07 and 

   - _D ·_ 0 _:_ 01 _X_ , for 0 _:_ 07 _· X ·_ 1 _:_ 50 

- for 1000 ppi scanners: 

   - _D ·_ 0 _:_ 0005, for 0 _:_ 00 _< X ·_ 0 _:_ 07 and 

   - _D ·_ 0 _:_ 0071 _X_ , for 0 _:_ 07 _· X ·_ 1 _:_ 50 

where _D_ = _jY ¡ Xj_ , _X_ = actual target distance, _Y_ = measured image distance ( _D; X; Y_ are in inches). 

Along-Bar geometric accuracy: When scanning a 1.0 cy/mm, multiple parallel bar target, in both vertical bar and horizontal bar orientations, the maximum difference in the horizontal or vertical direction, respectively, between the locations of any two points within a 1.5 inch segment of a given bar image, SHALL be less than 0.016 inches for at least 99 % of the tested cases in each print block measurement area and in each of the two orthogonal directions. 

## 4.1.5.1.3 Contrast Transfer Function 

The spatial frequency response SHALL be measured using a binary grid target (Ronchi-Grating), denoted as contrast transfer function (CTF) measurement. When measuring the bar CTF, it SHALL meet or exceed the minimum modulation values defined by equation Equation 4.1 or equation Equation 4.2, in both the de tector's row and detector's column directions, and over any region of the scanner's field of view. CTF values computed from equations Equation 4.1 and Equation 4.2 for nominal test frequencies are given in the fol lowing table. None of the CTF modulation values measured at specification spatial frequencies SHALL exceed 1.05. The output bar target image SHALL NOT exhibit any significant amount of aliasing. It is NOT REQUIRED that the bar target contains the exact frequencies listed in Table 4.1, however, the target does need to cover the listed frequency range and contain bar patterns close to each of the listed frequencies. 

The following equations are used to obtain the minimum acceptable CTF modulation values when using bar targets that contain frequencies not listed in Table 4.1: 

- 500 ppi scanner, for f = 1.0 to 10.0 cy/mm: 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0041-17.png)


- 1000 ppi scanner, for f = 1.0 to 20.0 cy/mm: 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0041-19.png)


For a given bar target, the specification frequencies include all of the bar frequencies which that target has in the range 1 to 10 cy/mm (500 ppi scanner) or 1 to 20 cy/mm (1000 ppi scanner). 

|**Frequency [cy/mm]**|**Minimum Modulation for 500 ppi**<br>**scanners**|**Minimum Modulation for**<br>**1000 ppi scanners**|**Maximum Modulation**|
|---|---|---|---|
|1.0|0.948|0.957|1.05|



Federal Office for Information Security 

33 

4 Function Modules 

|**Frequency [cy/mm]**|**Minimum Modulation for 500 ppi**<br>**scanners**|**Minimum Modulation for**<br>**1000 ppi scanners**|**Maximum Modulation**|
|---|---|---|---|
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

## 4.1.5.1.4 Signal-to-Noise Ratio and the Grey–Level Uniformity 

The white signal-to-noise ratio (SNR) and black SNR SHALL each be greater than or equal to 125.0, in at least 97 % of respective cases, within each measurement area. 

The grey level uniformity is defined for the three following cases: 

- Adjacent row, column uniformity: At least 99 % of the average grey levels between every two adjacent quar ter-inch long rows and 99 % between every two adjacent quarter-inch long columns, within each imaged area, SHALL NOT differ by more than 1.0 grey levels when scanning a uniform low reflectance target, and SHALL NOT differ by more than 2.0 grey levels when scanning a uniform high reflectance target. 

- Pixel to pixel uniformity: For at least 99.9 % of all pixels within every independent 0.25 inch by 0.25 inch area located within each imaged area, individual pixel's grey level SHALL NOT vary from the average by more than 22.0 grey levels, when scanning a uniform high reflectance target, and SHALL NOT vary from the average by more than 8.0 grey levels, when scanning a uniform low reflectance target. 

- Small area uniformity: For every two independent 0.25 inch by 0.25 inch areas located within each imaged area, the average grey levels of the two areas SHALL NOT differ by more than 12.0 grey levels when scanning a uniform high reflectance target, and SHALL NOT differ by more than 3.0 grey levels when scanning a uniform low reflectance target. 

## 4.1.5.1.5 Grey Scale Range of Fingerprint Images 

A fingerprint scanner operating at 500 ppi or 1000 ppi, SHALL perform the following sets of live scans: 

- For a standard roll and plain finger live scanner: capture a complete set of fingerprints from each of 10 sub jects; i.e. 10 rolls (all 5 fingers from each hand), 2 plain thumb impressions, and 2 plain 4-finger impressions. 

- For a palm scanner component of a live scan system: capture left and right palms from each of 10 subjects. 

- For an identification flat live scanner: capture left and right 4-finger plain impressions and dual thumb plain impressions from each of 10 subjects. 

Within the histogram of each image all grey values with at least 5 Pixels in this image are counted. The histo gram SHALL show no break and no other artefact. At least 80 % of the captured individual fingerprint images SHALL have a grey scale dynamic range of at least 200 grey levels, and at least 99% SHALL have a dynamic range of at least 128 grey levels. 

Federal Office for Information Security 

34 

4 Function Modules 

## 4.2 FM Category Acquisition Software 

Acquisition Software (AS) contains all functionality regarding image processing except for biometric purposes. Therefore, this Function Module usually contains device driver software for the acquisition hardware or, in general, software that is very close to the physical hardware such as firmware. Furthermore, colour manage ment and image enhancement mechanisms are part of this software layer. 

## 4.2.1 FM AS-FI-FBS 

This function block describes the requirements and interfaces of Acquisition Software in particular for flat bed scanners that are used for the provisioning of digitised application form for the application of a German Identity Document. 

## 4.2.1.1 Requirements 

The image data SHALL be provided without any compression in Windows Bitmap Format Version 3. 

## 4.2.1.2 Recommendations 

Acquisition Software that supports calibration procedures for the respective scanner SHOULD be used (in particular colour management). 

## 4.2.2 FM AS-FI-DC 

This function block describes the requirements and interfaces for acquisition software used for digital cameras in order to obtain digitised images. 

## 4.2.2.1 Requirements 

- In regard to the application scenario an adequate resolution of the camera SHALL be chosen to acquire a facial image of at least 1200 x 1600 pixels with an inter eye distance of at least 120 pixels. 

- The images SHALL be captured and stored in colour (24 bit RGB). Note, this requirement is not MANDA TORY for scenarios where only a facial verification is performed. 

- The image data SHOULD be provided without any compression in one of the following image formats: Windows Bitmap Format Version 3, JPEG Lossless, DNG (in combination with JPEG Lossless). 

- If the acquisition device does not support a lossless mode, the image MAY alternatively be provided in JPEG mode with the minimal level of compression possible. 

- In normal mode of operation, no compression artefacts SHALL be detectable in the image. 

## 4.2.2.2 Recommendations 

Acquisition software that supports calibration procedures for the respective digital camera SHOULD be used (in particular colour management). 

## 4.2.3 FM AS-FP-SF 

This Function Module describes the requirements and interfaces for acquisition software for single finger scanners. 

## 4.2.3.1 Requirements 

- The image provided by acquisition software SHALL meet the criteria of fingerprints as described in [BIB_ISO_FINGER]. The requirements according to the certification requirements of [BIB_ISO_FINGER] are in force. 

- For the acquisition process, a pre-qualification of the fingerprints to prefer high quality SHALL be used. The activation of the acquisition SHALL occur automatically and SHALL have a configurable timeout, which starts together with the activation. The capture SHOULD prefer the highest quality image of a sequence, at least the last captured image (after timeout) of a sequence. This functionality MAY be part of the hardware firmware and MAY NOT be available as separate software component. 

Federal Office for Information Security 

35 

4 Function Modules 

- If the sensor was not able to capture an image (e.g. because no finger was placed on it), it is OPTIONAL to return an image after timeout. In this case, an adequate error code SHALL be returned. 

## 4.2.3.2 Recommendations 

In order to prevent unwanted duplicate acquisitions of the same finger, the software SHOULD start the ac quisition process not before the finger from a previous acquisition has been removed from the sensor surface. 

## 4.2.4 FM AS-FP-MF 

This Function Module describes the requirements and interfaces for acquisition software for multi finger scanners. 

## 4.2.4.1 Requirements 

- The image provided by acquisition software SHALL meet the criteria of fingerprints as described in [BIB_ISO_FINGER]. The requirements according to the certification requirements of [BIB_ISO_FINGER] are mandatory. 

- For the acquisition process, a pre-qualification of the fingerprints to prefer high quality SHALL be used. The activation of the acquisition SHALL occur automatically and SHALL have a configurable timeout, which starts together with the activation. The capture SHOULD prefer the highest quality image of a sequence, at least the last captured image (after time-out) of a sequence. 

- This functionality MAY be part of the hardware firmware and MAY NOT be available as separate software component. 

- The thresholds of the pre-qualification for performing a capture SHALL be documented by the vendor. 

- If the acquisition software allows multiple thresholds for pre-qualification, it SHALL be configurable by the system administrator. 

- In case further requirements demand for an export of the uncompressed fingerprint image data BMP SHALL be used as image format. 

- If the sensor was not able to capture an image (e.g. because no finger was placed on it), it is OPTIONAL to return an image after timeout. In this case, an adequate error code SHALL be returned. 

## 4.2.4.2 Recommendations 

In order to prevent unwanted duplicate acquisitions of the same fingers or slaps, the software SHOULD start the acquisition process not before the fingers from a previous acquisition have been removed from the sensor surface. 

## 4.3 FM Category Biometric Image Processing 

The Function Module Biometric Image Processing (BIP) provides the extraction of all relevant biometric in formation from the data which is provided by the acquisition hardware or the acquisition software layer. Thus, a proprietary data block is transformed to a digital image of a biometric characteristic. In general, specific image processing for biometric characteristics is addressed here. 

## 4.3.1 FM BIP-FI-FBS 

This function block describes requirements and interfaces for Biometric Image Processing with respect to the output of flat bed scanners to obtain a facial image for enrolment purposes. 

## 4.3.1.1 Requirements 

As a result of the image processing of this module, a facial image SHALL be generated that is compliant to the requirements of full frontal images specified in [BIB_ISO_FACE]. As a precondition, the input photograph SHALL fulfil the requirements of [BIB_ISO_FACE] as well and the photograph must be positioned on the ap plication form in a correct manner. 

Federal Office for Information Security 

36 

4 Function Modules 

Basically, the facial image processing SHALL enclose the cropping to the facial image. In the following, the requirements for the image cropping are specified: 

- The size of the facial image SHALL be 3.5 cm x 4.5 cm (width x height) with an image resolution of 300 ppi i.e. 413 pixels width, 531 pixels height and with a tolerance of +/- 10 pixels. 

- The colour depth SHALL be 24 bit RGB (for colour and black-and-white pictures) or 8 bit grey scale (just for black-and-white-pictures). 

## 4.3.2 FM BIP-FI-GID 

This function block describes requirements and interfaces for Biometric Image Processing with respect to the output of digital cameras to obtain a facial image that fulfils the ICAO requirements for travel documents. 

## 4.3.2.1 Requirements 

As a result of the image processing of this module, a facial image SHALL be generated that is compliant to the requirements of full frontal images specified in [BIB_ISO_FACE]. 

Basically, the facial image processing SHALL enclose the cropping to the facial image. In the following, the requirements for the image cropping are specified: 

- The size of the facial image SHALL be 3.5 cm x 4.5 cm (width x height) with an image resolution of 300 ppi i.e. 413 pixels width, 531 pixels height and with a tolerance of +/- 10 pixels. 

- The colour depth SHALL be 24 bit RGB (for colour and black-and-white pictures) or 8 bit grey scale (just for black-and-white-pictures). 

## 4.3.3 FM BIP-FP-APP 

This Function Module describes requirements and interfaces for the biometric image processing to provide up to four single finger images for the subsequent reference storage or biometric comparison. 

## 4.3.3.1 Requirements 

- The resolution of the fingerprint image has to be 500 ppi corresponding to the certification requirements of [BIB_ISO_FINGER] and, therefore, MAY differ from the scan resolution. 

- Depending on the call, as many individual fingerprints as requested SHALL be extracted from the input image and provided as single fingerprints. 

Note: Segmentation for single finger scanners is OPTIONAL. 

For this segmentation process, the following requirements SHALL be fulfilled: 

   - ability to accept fingerprints which are rotated in the same direction up to 45 degrees 

   - in the same direction rotated fingerprints have to be corrected to be vertical 

   - segment the first part over the finger (fingertip) 

   - segmentation has to occur on uncompressed data 

- Fingerprint images SHALL NOT be upscaled. If the targeted system or database requires fingerprint images of higher size than captured the fingerprint image SHALL be evenly surrounded with white pixels to reach the desired size. 

## 4.4 FM Category Quality Assessment 

The Function Module Quality Assessment contains all kinds of mechanisms and procedures to check the qua lity of the biometric data or to select the best quality data out of multiple instances. 

## 4.4.1 FM QA-FI-PG 

This function block describes requirements for a photo guideline that is used for Quality Assessment. 

Federal Office for Information Security 

37 

4 Function Modules 

## 4.4.1.1 Recommendations 

If the QA is to be performed by a person, visual tools like a photo guideline MAY be used for support. 

If the visual check is conducted with the photo guideline, it always SHALL be done even if the checks with the photo template and/or the QA software will be performed afterwards. A recent picture is required according to [BIB_ISO_FACE] . 

If these basic criteria are not met, the image SHALL be rejected without any further checks by the software or the photo template. 

In the case of the photo guideline, the following criteria SHALL be described, preferably using sample images for compliant and non compliant images (compare [BIB_ISO_FACE] ): 

- frontal pose 

- neutral expression 

- mouth closed 

- eyes open 

- no occlusion (glasses, hair, eye patch) 

- eyes looking to the camera 

- background uniformity (plainness, no textures, colour) 

- no shadows 

- no head coverings 

- no further people / objects 

- equally distributed lighting 

- no shadows over the face 

- no shadows in the eye sockets 

- no hot spots on skin 

- no effects from glasses 

- correct exposure 

- correct contrast 

- focus and depth of field 

- no unnatural colours 

- no red eyes 

## 4.4.2 FM QA-FI-PT 

This function block describes requirements for a photo template that is used for QA. 

## 4.4.2.1 Requirements 

The photo template SHALL be used to determine if the geometric requirements of [BIB_ISO_FACE] are ful filled (e.g. format, the height of the face and the centred alignment of the face). For this purpose, the photo template SHALL be placed on the image (physically or digitally) and SHALL be checked by the official. 

For the photo template at least the following criteria out of [BIB_ISO_FACE] SHALL be supported. 

- image height 

- image width 

- head height 

- eye positions 

Federal Office for Information Security 

38 

4 Function Modules 

## **•** centred horizontally 

For images of children under the age of 10, different requirements for the height of the head and the area of the eyes MAY be used. That is why a special photo template for children SHALL exist to check the acceptability of the image. 

For the images of infants and babies younger than 6 years, additional tolerances concerning the pose of the head, the facial expression and the line of sight MAY be allowed, compared to those already described by the photo template for children. 

## 4.4.3 FM QA-FI-GENERIC 

This Function Module describes requirements and interfaces for software that is used for quality assessment of digital images to ensure compliance with [BIB_ISO_FACE]. 

## 4.4.3.1 Requirements 

## 4.4.3.1.1 General Requirements 

The QA module is used for the software-based automatic check of the conformance of the picture to [BIB_ISO_FACE] after the digitisation. Thereby, the geometric properties of the picture as well as the digital parameters of the image are analysed and rated. 

The standard which is relevant for the quality of facial images [BIB_ISO_FACE] hierarchically describes requi rements for the facial images. In the following, full frontal images are expected. 

The QA module SHALL analyse and evaluate all of the quality criteria listed in Table 4.2. For the criteria marked with "M", the quality values SHALL be provided while quality values for the criteria marked with "O" MAY be provided in the defined format according to the respective criteria. 

A criterion is fulfilled if its calculated value is in the given threshold boundaries. 

Based on the results of all provided quality criteria the QA module SHALL reject or approve the picture. The total result is true if every single quality criteria is fulfilled. 

The QA module SHALL provide an interface for conformance testing where a single image (JPEG or JPEG2000 encoded) can be processed and the calculated values and configuration data are returned. The image type to process depends on the image type requirements of the application profile to implement. 

The QA module SHOULD operate on cropped images retrieved from the image processing according to FM Category Biometric Image Processing. 

|**ID**|**Criterion**|**ISO-Ref., compare**<br>[BIB_ISO_FACE]|**Mandatory / Optional**|**Unit/Range**|
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
|3.3|Eyes looking to the ca<br>mera|7.2.3|O|Arbitrary units|



Federal Office for Information Security 

39 

4 Function Modules 

|**ID**|**Criterion**|**ISO-Ref., compare**<br>[BIB_ISO_FACE]|**Mandatory / Optional**|**Unit/Range**|
|---|---|---|---|---|
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
|7.5|Colour space|7.4.2.3|M|According to [BIB_ISO_FACE]<br>using Decimal notation (e.g.<br>"1" for RGB-24bit, "2" for<br>YUV422 or "3" for 8bit-grey<br>scale)|
|7.6|Grey scale density and<br>colour saturation|7.4.2.1 7.4.2.2|M|Counted numbers of intensi<br>ty values existing within the<br>image|



**Table 4.2** Mapping of Relevant Quality Criteria 

## 4.4.3.1.2 Requirements Identification of the Best Capture 

When multiple captures of facial images and their corresponding set of quality metrics are passed, the best capture of the captures SHALL be identified as described in the following: 

1. If exactly one facial image conforms to more mandatory criteria than all other images, this image is chosen. 

2. If no image is conform to more mandatory criteria than all other images, the last temporal image with the most fulfilled mandatory criteria is chosen among the facial images fulfilling the most criteria. If no 

Federal Office for Information Security 

40 

4 Function Modules 

temporal information is available, a random selection SHALL be applied among the facial images fulfilling the most criteria 

## 4.4.4 FM QA-FI-GID 

This Function Module describes requirements and interfaces for software that is used for quality assessment of digital images within the context of enrolment scenarios for identity documents to ensure compliance with [BIB_ISO_FACE]. 

## 4.4.4.1 Requirements 

The threshold requirements of Table 4.3 SHALL be in place within the context of enrolment scenarios for identity documents. These thresholds relate to the generic quality criteria of FM QA-FI-GENERIC. 

|**ID**|**Criterion**|**Minimum**|**Maximum**|**Unit/Range**|
|---|---|---|---|---|
|Image for passport chip (GID), ratio 45:35|||||
|1.1|Yaw, neck axis|-5|5|Degrees|
|1.2|Pitch, ear axis|-5|5|Degrees|
|1.3|Roll, nose axis|-8|8|Degrees|
|5.1|Image height|521|541|In pixel|
|5.2|Image width|403|423|In pixel|
|5.3|Ratio: Head width / image width|0,5|0,75|As ratio between 0 and 1|
|5.4|Ratio: Head height / image height|0,6|0,9|As ratio between 0 and 1|
|5.5|Vertical position of the face|0,3|0,5|As ratio between 0 and 1|
|5.6|Horizontally centred face|0,45|0,55|As ratio between 0 and 1|
|5.7|Eye distance|90|-|In pixel|



**Table 4.3** Quality Threshold Requirements for Facial Images for Enrolment Scenarios for Identity Documents 

## 4.4.5 FM QA-FP-APP 

This Function Module describes requirements for the quality assessment of plain or rolled fingerprints inclu ding quality assessment of single fingerprint, respectively slap and selection of the best quality image out of multiple instances. 

## 4.4.5.1 Requirements 

## 4.4.5.1.1 Quality Algorithm 

As quality algorithm NFIQ 2.0 [BIB_NFIQ2.0] SHALL be used. As resulting quality value, the output value of NFIQ 2.0 in the integer range of [0,100] SHALL be used. In the case of failure, the returned value 255 indicates that a computation was not successful. In this case, the value SHALL be returned as dedicated error code. 

## 4.4.5.1.2 Quality Evaluation Process for a Slap or Single Fingerprint 

In case a single captured fingerprint, respectively slap is passed, the QA SHALL be performed as described in the following. Beforehand, the fingerprints of the passed capture SHALL be segmented (considering missing fingers). Note, that in verification applications, a QA is not conducted. Thus, every slap capture is considered sufficient and no thresholds are specified here. Skipping the QA is expected to accelerate the overall process. OPTIONALLY, a QA can be performed. 

1. For each segmented fingerprint _FA;j_ of a passed capture _A_ , a quality value _QA;j_ is calculated with _j 2_ 1 _; :::;_ 10 (up to 4 fingers in one slap) representing the specific finger code according to [BIB_ISO_FIN GER]. 

2. The resulting quality value is compared with the defined threshold _THj_ for this finger. The application specific thresholds as defined in the following section apply. 

Federal Office for Information Security 

41 

4 Function Modules 

3. In case all of the fingerprint qualities reach the specified threshold (i.e. _8j; QA;j ¸ THj_ ), the boolean infor mation _b_ = 1 indicates a successful capture. 

4. In case one or more fingerprints do not reach the threshold (i.e. _9j; QA;j < THj_ ), the boolean information _b_ = 0 indicates insufficient quality of the capture. 

5. For the segmented fingerprint _FA;j_ the corresponding parameter set _PA;j_ is compiled and returned. 

6. As a result of the QA process, the following values are returned to the calling process: 

   - a. the boolean information _b_ 

   - b. the parameter set _PA_ = _QA;j; :::; QA;l_ with _j; l 2_ 1 _; :::;_ 10 representing the specific finger code 

## 4.4.5.1.3 Identification of the Best Capture out of Multiple Captures 

When multiple captures _Ai; i 2_ 1 _; :::; n_ and their corresponding set of segmented fingerprints _FAi;j_ with _j 2_ 1 _; :::;_ 10 representing the specific finger code according to [BIB_ISO_FINGER] are passed, the best of the captures SHALL be identified as described in the following section: 

1. For each segmented fingerprint _FAi;j_ of a passed capture _Ai_ , the quality value _QAi;j_ is calculated with re presenting the specific finger code according to [BIB_ISO_FINGER]. 

2. The captures are ranked according to the quality values of the fingerprints according to the following (lexicographical) order. The highest ranked capture is considered as the capture yielding the best quality. 

   - a. for left/right four-finger slaps, the order is as follows: 

      - i. index finger (highest priority) 

      - ii. middle finger 

      - iii. ring finger 

iv. little finger (lowest priority) 

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

Federal Office for Information Security 

42 

4 Function Modules 

      - i. Of the set of captured images obtained in the process beforehand, which are not annotated by a hardware reported issue, the capture with the highest quality value is considered as the best image. 

      - ii. If the set of captured images obtained in the process beforehand on does only contain images which are annotated by hardware reported issues, the capture with the highest quality value of the entire set is considered as the best image. 

      - iii. In case several captures yield to the same highest quality value, the last (temporal) of highest quality captures is considered as the best image. 

3. As a result of the QA process, the following values are returned: 

   - a. the identifier _i_ representing the capture yielding the best quality 

   - b. the parameter set _PA_ = _QAi;j; QAi;l_ with _j; l 2_ 1 _; :::_ 10. 

## 4.4.5.1.4 Thresholds for Plain Fingerprints for Enrolment Purposes 

The following thresholds as indicated in Table 4.4 apply when fingerprints are captured plain for enrolment purposes. Note, the thresholds in Table 4.4 do not apply to plain captured fingerprint in enrolment scenarios where the plain fingerprints are captured for control purpose of rolled fingerprints. In that case, thresholds as indicated in Table 4.5 apply for the plain fingerprints. 

|**Finger Position**|**Finger Code**|**NFIQ 2.0 Threshold**|
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

## 4.4.5.1.5 Thresholds for Plain Control Fingerprints and Fingerprints used for Identification Searches 

The following thresholds as indicated in Table 4.5 apply when fingerprints are captured plain for the purpose of control slaps (used for comparison with rolled prints) or for use in identification searches. Note, the thres holds in Table 4.5 do apply to plain captured fingerprint in enrolment scenarios where the plain fingerprints are captured for control purpose of rolled fingerprints. 

|**Finger Position**|**Finger Code**|**NFIQ 2.0 Threshold**|
|---|---|---|
|Right thumb|1|20|
|Right index finger|2|20|
|Right middle finger|3|20|
|Right ring finger|4|10|
|Right little finger|5|10|
|Left thumb|6|20|
|Left index finger|7|20|
|Left middle finger|8|20|



Federal Office for Information Security 

43 

4 Function Modules 

|**Finger Position**|**Finger Code**|**NFIQ 2.0 Threshold**|
|---|---|---|
|Left ring finger|9|10|
|Left little finger|10|10|



**Table 4.5** Thresholds for Plain Control /Identification Fingerprints 

## 4.4.5.1.6 Thresholds for Rolled Fingerprints 

The following thresholds as indicated in Table 4.6 apply when fingerprints are captured rolled for enrolment purposes. 

|**Finger Position**|**Finger Code**|**NFIQ 2.0 Threshold**|
|---|---|---|
|Right thumb|1|20|
|Right index finger|2|15|
|Right middle finger|3|15|
|Right ring finger|4|10|
|Right little finger|5|5|
|Left thumb|6|20|
|Left index finger|7|15|
|Left middle finger|8|15|
|Left ring finger|9|10|
|Left little finger|10|5|



**Table 4.6** Thresholds for Rolled Fingerprints 

## 4.5 FM Category Presentation Attack Detection 

The objective of the Function Module presentation attack detection is to avoid presentations with the goal to subvert an enrolment, verification of identification process. 

## 4.5.1 FM PAD-FP-APP 

This Function Module describes requirements for PAD in the context of the acquisition of biometric charac teristics of fingerprints. This Function Module is especially relevant for use cases where no direct observation of the acquisition process by an operator is possible (e.g. in SSS scenarios). 

## 4.5.1.1 Requirements 

## 4.5.1.1.1 General Requirements 

The capture system SHALL contain a PAD subsystem according to [BIB_ISO_PAD_1] detecting spoofing at tempts using artefacts by which an attacker is trying to establish a different biometric characteristic as probe in the verification or identification process. 

The PAD subsystem MAY consist of hardware and software (e.g. the used fingerprint scanner MAY have addi tional sensors designed for this purpose). 

According to the used fingerprint scanner, PAD subsystem SHALL be able to detect artefact classes listed in the following: 

- Fingertips, created in different thicknesses 

- Single fingers (massive) 

- Complete hands (massive) 

- Artefacts with two to four fingers (massive) 

The PAD subsystem SHALL be able to detect all typical artefact material types listed in the following: 

Federal Office for Information Security 

44 

4 Function Modules 

- Artefacts created from different kinds of silicon, in different colouring 

- Artefacts created from different kinds of latex, in different colouring 

- Artefacts created from different kinds of gelatine, in different colouring 

- Artefacts created from different kinds of wood glue, in different colouring 

- Artefacts created from different kinds of window painting, in different colouring 

Also, the detection subsystem SHALL be adequate to the usage setting in correspondence with the security requirements in question. The performance MAY be described by a risk analysis for every considered attack type. The current version of [BIB_ISO_PAD_3] SHALL be taken into account. 

The PAD SHALL be conducted both in supervised acquisition scenarios, e.g. in a counter scenario, and in un supervised acquisition scenarios, e.g. in SSS scenarios. Thereby, the PAD SHALL be conducted for all acquisi tion purposes, e.g. enrolment, identification and verification. 

## 4.5.1.1.2 Integration Requirements 

The PAD subsystem SHALL be independent of the regular capture subsystem. 

It SHALL signal its detection results in the form of a PAD for each finger individually. An overall result to the calling application SHALL also be applied additionally. 

The score SHALL be a normalized `double` in the range [0,...,1] using at least ten uniformly distributed interim values, where 1 indicates bona fide and 0 presentation attack. A binary score SHALL NOT be used (e.g. True or False, 1 or 0). It SHALL additionally provide detailed information about the scores of the PAD. 

OPTIONAL, if the Function Module is used within a comparison scenario, it is allowed to only signal the de tection result in conjunction with a match (comparison decision stating that the biometric probe and the bio metric reference are from the same source) to the operator. 

The PAD result SHALL correspond to the respective finger capture attempt. 

Note that an image of the fingerprint or slap in question SHALL be taken independently of a possible PAD alarm. 

## 4.5.1.1.3 Maintenance Requirements 

As new technologies and new attack mechanisms are developed over time, the PAD subsystem SHALL be updated and checked whenever necessary, so it stays capable agianst old and new attacks and attack types. 

## 4.5.1.1.4 Certification Requirements 

To ensure comparable performance of presentation attack detection subsystems, the system SHALL be certi fied under the Common Criteria Agreement according to one of following Protection Profiles: 

- BSI-CC-PP-0063-2010: Fingerprint Spoof Detection Protection Profile (FSDPP) 

- BSI-CC-PP-0062-2010: Fingerprint Spoof Detection Protection Profile based on Organisational Security Policies (FSDPP_OSP) 

## 4.5.1.1.5 Transitional Rules 

The following transition rules are defined for the requirements of this Function Module. 

- The requirements of this Function Module only apply to devices and software put into operation after No vember 1, 2020. 

- However, this transition rule ends by November 1, 2024: By November 1, 2024, all devices and software SHALL apply to the requirements of this Function Module. 

- From November 1, 2020 to November 1, 2024, only software updates are allowed for non-certified PAD devices for which the PAD requirement holds. 

Federal Office for Information Security 

45 

4 Function Modules 

## 4.5.2 FM PAD-FI-APP1 

This Function Module describes requirements for PAD in the context of the acquisition of facial biometrics. This Function Module is especially relevant for use cases where no direct observation of the acquisition pro cess by an operator is possible (e.g. in self-service scenarios). 

## 4.5.2.1 Requirements 

## 4.5.2.1.1 General Requirements 

The capture subsystem SHALL contain a PAD subsystem detecting spoofing attempts using artefacts by which an attacker is trying to establish a different biometric characteristic as probe in the verification or identifica tion process. 

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

Also, the detection subsystem SHALL be adequate to the usage setting in correspondence with the security requirements in question. The performance MAY be described by a risk analysis for every considered attack type. The current version of [BIB_ISO_PAD_3] SHALL be taken into account. 

## 4.5.2.1.2 Integration Requirements 

The PAD subsystem SHALL be independent of the regular capture subsystem, i.e. it SHALL NOT inhibit cap turing image data in case of a suspected attack. It SHALL signal its detection results in the form of a PAD score to the calling application. The score SHALL be a normalized `double` in the range [0,...,1] using at least ten uniformly distributed interim values, where 1 indicates bona fide and 0 presentation attack. A binary score SHALL NOT be used (e.g. True or False, 1 or 0). It SHALL additionally provide detailed information about the results of the PAD. 

Federal Office for Information Security 

46 

4 Function Modules 

If the Function Module is used within a comparison scenario, it MAY only signal the detection result in con junction with a match (comparison decision stating that the biometric probe and the biometric reference are from the same source). In any case, the omission of the detection result SHALL be signalled. 

The PAD result SHALL correspond to the chosen facial image. 

## 4.5.2.1.3 Maintenance Requirements 

As new technologies and new attack mechanisms are developed over time, the PAD subsystem SHALL be regularly updated and reevaluated. 

## 4.5.2.2 Transition Rules 

The requirements of this module do not apply until May 2025. 

## 4.6 FM Category Compression 

The objective of the Function Module Compression (COM) is to keep the biometric data within a feasible size without losing too much quality for a biometric verification or identification. 

## 4.6.1 FM COM-FI-JP2 

This function block describes requirements and interfaces for the compression of photos using the JPEG 2000 format for reference storage usable for enrolment, verification, and identification purposes. 

## 4.6.1.1 Requirements 

The compression method for facial images SHALL be JPEG 2000 (compare [BIB_ISO_15444]). The compression SHALL result in a constant file size of 15 kB[3] with a tolerance of +/- 5%. A well-known implementation of JPEG 2000 SHALL be used. 

Within the Compression Module multiple lossy compressions SHALL NOT be allowed. 

For conformance testing the compression module SHALL provide an interface that accepts predefined test data instead of performing the regular process. 

## 4.6.2 FM COM-FI-JPG 

This function block describes requirements and interfaces for the compression of photos using the JPEG for mat for reference storage. 

## 4.6.2.1 Requirements 

The compression method for facial images SHALL be JPEG (compare [BIB_ISO_10918-1]). The compression algorithm SHALL be parametrized in such a way that the application specific requirements as listed in Ta ble 4.7 are met by the resulting compressed image. Within the Compression Module multiple lossy compres sions SHALL NOT be allowed. 

|**Minimum File Size**|**Recommended Compression Ratio**|
|---|---|
|Small size image (531x413 pixel)||
|25 KiB|20:1|
|Medium size image (800x600 pixel)||
|35 KiB|20:1|
|Standard size image (1600x1200 pixel)||
|100 KiB|20:1|



**Table 4.7** Requirements to Compression Using JPEG Format 

For conformance the implementation encapsulating the compression has to provide an interface that accepts predefined test data instead of performing the regular process. 

> 3 1 kB equals 1024 bytes 

Federal Office for Information Security 

47 

4 Function Modules 

## 4.6.3 FM COM-FP-WSQR 

This Function Module describes requirements and interfaces for the compression of fingerprint images by Wavelet Scalar Quantisation (WSQ) method for reference storage on electronic chips. 

## 4.6.3.1 Requirements 

WSQ SHALL be used as compression method for fingerprint images. A bit rate of 0.75 SHALL be used as compression parameter. This is equivalent to a compression factor of approximately 1:15[4] (according to [BIB_ISO_FINGER]). The implementation of the used WSQ algorithm SHALL be certified by the FBI and SHALL be referenced by the respective certificate number (coded in the WSQ header). The certified WSQ im plementation SHALL be version 3.1 and SHALL base on NBIS Version 5.0. Within the Function Module Com pression multiple lossy compressions SHALL NOT be allowed. 

The resulting image file of a fingerprint SHALL NOT exceed the maximum size of 18 kB. 

If the resulting image file compressed with the above-named bit rate is larger than the defined maximum size, for this particular case a stronger compression SHALL be used. Therefore, an iterative process SHALL be applied, which results in an image file smaller or equal to the maximum size, yet differs at least 1 kB from the maximum size. Therefore the result is between or equal 17 and 18 kB. 

## 4.7 FM Category Operation 

Within the Function Module Operation (O), the working process is specified for the respective operator. All steps that have to be executed are described sequentially and in more detail. This also includes descriptions of how to proceed in error cases. 

## 4.7.1 FM O-ALL-USV 

This Function Module describes requirements to be observed by the operator who handles the unsupervised acquisition process of biometric characteristics. 

## 4.7.1.1 Requirements 

## 4.7.1.1.1 Organisational Requirements 

The operator SHALL check that the acquired digital image belongs to the biometric subject. 

## 4.7.1.2 Recommendations 

## 4.7.1.2.1 Organisational Recommendations 

The operator SHOULD assure that only one person was in near distance of the biometric capture devices. The operator MAY be assisted in this requirement, e.g. by corresponding sensors. This is typically used in conjunc tion with additional video surveillance. 

## 4.7.2 FM O-FI-ALL 

This Function Module describes requirements to be observed by the operator who handles the facial image acquisition process. This includes the full working process. 

## 4.7.2.1 Requirements 

- If the software based QA rejects the image, the operator SHALL have the option to give a veto in order to release the image despite a negative software decision and vice versa. 

- The operator SHALL be responsible for an adequate cleanliness of all capture hardware components. 

## 4.7.2.2 Recommendations 

OPTIONALLY, the operator can use the photo guideline. 

- 4 For estimation of compression factor it is allowed to crop to the minimum size containing the fingerprint defined if a sensor is used with a larger capturing area than this minimum. 

Federal Office for Information Security 

48 

4 Function Modules 

## 4.7.3 FM O-FI-DC 

This Function Module describes requirements to be observed by the operator who handles the facial image acquisition process with a digital camera. 

## 4.7.3.1 Requirements 

- The operator SHALL ensure that different environmental lighting conditions caused by direct or indirect sunlight and different seasons of the year SHALL NOT influence the proper and uniform lighting of the captured facial image. 

- Direct and cross irradiation of lighting SHALL be avoided by the operator. 

## 4.7.4 FM O-FI-FBS 

This Function Module describes requirements to be observed by the operator who handles the facial image acquisition process with a flat bet scanner. 

## 4.7.4.1 Requirements 

- The operator SHALL be responsible for a clean scanning surface so that adequate image results can be ob tained in the following. 

- The operator SHALL consider the photo guideline. 

- The person on the photo SHALL be doubtlessly identified by the operator. 

## 4.7.4.2 Recommendations 

OPTIONALLY, the operator can use the photo template. 

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

## 4.8.1 FM UI-FI-OP 

This Function Module describes requirements for the user interface of the software displaying the result of the quality assessment and verification of facial images to the operator. 

Federal Office for Information Security 

49 

4 Function Modules 

## 4.8.1.1 Requirements 

The following SHALL be shown to the operator for the enrolment: 

- displaying of the current evaluated picture 

- displaying of all criteria evaluated with the current value and threshold as well as their relation: OK/NOK for every criterion 

- displaying of the summarised result OK/NOK for the current picture 

- provision of the veto power for the operator 

   - enforcement of OK for obvious reasons (e.g. disability) 

   - enforcement of OK without obvious reasons 

   - enforcement of NOK to overrule software based quality assessment 

The following SHALL be shown to operator for the verification: 

- Visual feedback of the verification process SHALL be provided for the operator. At least both images (live and reference) and the (boolean) result of the verification SHALL be displayed to the operator. 

- If the verification fails, then the operator SHALL get access to at least one complete and coherent set of bio metric samples and verification results corresponding to a single verification attempt. For instance, in case of verification of a live-captured facial image against a facial image from chip (Data Group 2) and Central Identity Register (CIR), such a complete set would consist of the live-captured facial image, the facial image extracted from chip, the facial image stored in the CIR, and both corresponding verification results of the live-captured facial image against the facial image from chip and the CIR image. 

## 4.8.2 FM UI-FI-BSJ 

This Function Module describes requirements for the user interface of facial image acquisition shown to the biometric subject. 

## 4.8.2.1 Requirements 

In case the acquisition system is required by another[5] Function Module to have a feedback screen for the facial acquisition, the following requirements SHALL be fulfilled: 

- The acquisition system SHALL show a digital or physical mirror image to the biometric subject to guide it for the correct positioning in front of the camera. 

- The acquisition system SHALL show user guidance information to help the biometric subject with the cor rect positioning in front of the camera when one of the following conditions is met: 

   - The biometric subject is too close to or too far away from the camera. 

   - The biometric subject is too far left or right to the camera. 

   - The biometric subject is too high or low and the camera is not able to compensate this with a vertical adjustment. 

   - The biometric subject is in too much movement. 

   - The biometric subject is not facing frontally to the camera. 

   - The eyes of the biometric subject are closed. 

   - The mouth of the biometric subject is opened. 

   - Multiple faces were detected in front of the camera. 

- 5 If no Function Module of the Application Profile to implement requires a feedback screen, there is no need to implement the requirements within this section. 

Federal Office for Information Security 

50 

4 Function Modules 

## 4.8.2.2 Recommendations 

- An indicator showing the capture status SHOULD be displayed to the biometric subject. 

- Graphics (e.g. buttons or pictograms) SHOULD use a uniform colour palette without utilizing clashing co lours. 

## 4.8.3 FM UI-FP-OP 

This Function Module describes requirements for the user interface of the software displaying the live feed back and results of the fingerprint acquisition, QA and control verification of fingerprint images to the ope rator. 

## 4.8.3.1 Requirements 

- The user interface SHALL signal which fingerprints are expected for the current slap or fingerprint acqui sition such that the operator can guide the biometric subject to place the correct fingers on the fingerprint scanner. 

- Visual feedback of the fingerprint acquisition at least displaying of the final images SHALL be provided to the operator. 

- If a control verification or sequence check error occurs, the fingers involved in the unexpected successful comparisons SHALL be displayed to the operator and in case of a slap image only the affected finger(s) SHALL be marked in the displayed image. In case a control verification was attempted and no successful comparison occurred during the control verification, a warning SHALL be displayed to the operator that the control verification was not successful. 

- The segmented single fingerprints SHALL be visualised to the operator to identify potential failures in seg mentation. This can be realised by displaying the result containing up to ten segmented single fingerprints. In case the amount of captured fingerprints mismatches with the amount of expected fingers a warning SHALL be displayed to the operator. 

- If a slap acquisition is in place and a slap classifier is in use (and activated not only for evaluation purpose), a warning SHALL be displayed to the operator when the classification result mismatches with the expected slap of the current acquisition. 

- If PAD was performed and a presentation attack was detected, a warning SHALL be displayed to the operator and displayed for each finger individually. An overall result SHALL also be displayed additionally. 

- The indication of the quality level SHALL be displayed to the operator. 

- The provision of the veto power for the operator SHALL be shown to the operator for the enrolment: 

   - enforcement of OK for obvious reasons (e.g. disability) 

   - enforcement of OK without obvious reasons 

   - enforcement of NOK to overrule software based quality assessment 

## 4.8.3.2 Recommendations 

A live view from the fingerprint scanner SHOULD be displayed to the operator during the fingerprint acquisi tion. This also includes live information, e.g. about the correct positioning of fingers on the fingerprint scan ner or about the current quality level, that supports the operator guiding the biometric subject. 

The user interface SHOULD show a graphical representation of the fingerprints that are expected for the cur rent slap or fingerprint acquisition. 

## 4.8.4 FM UI-FP-BSJ 

This Function Module describes requirements for the user interface of the biometric subject for fingerprint acquisitions. 

## 4.8.4.1 Requirements 

The following requirements SHALL be met for the user interface: 

Federal Office for Information Security 

51 

4 Function Modules 

- An indicator showing the capture status and an indication when the capture process has finished SHALL be displayed to the biometric subject. The capture status SHALL include: Where to place the fingers, an indication of the scanning process and the feedback in case of mispositioning of fingers. 

- A visualization which fingerprint or hand to place on the sensor SHALL be given. 

If PAD was conducted: Neither the PAD result nor PAD score SHALL be displayed to the person whose finger prints are acquired. In a supervised acquisition scenario the process operator MAY be responsible for screen positioning, so that the PAD result or the PAD score is not displayed to the person whose fingerprints are acquired. 

## 4.8.4.2 Recommendations 

The following recommendations SHOULD be met for the user interface: 

- Graphics (e.g. buttons or pictograms) SHOULD use a uniform colour palette without utilizing clashing co lours. 

- The acquisition process SHOULD be displayed as real time feedback to the biometric subject (e.g. with the help of a feedback monitor). 

## 4.9 FM Category Reference Storage 

The objective of the Function Module Reference Storage (REF) is to store biometric data in a way that it can be used for reference purposes later on. 

## 4.9.1 FM REF-FP-CHIP 

This function block describes requirements how fingerprint images are stored as reference data in context of electronic chips. 

## 4.9.1.1 Requirements 

According to the ICAO document Doc 9303 the data is put on the chip. 

## 4.9.2 FM REF-FI-GID 

This function block describes requirements how facial images are stored as reference data in context of Ger man identity documents. 

## 4.9.2.1 Requirements on Facial Images for Local Reference Storages 

According to §21 [BIB_PassG] and §23 [BIB_PAuswG] the data SHALL be stored within the local reference storage. The image data SHALL be stored according to FM COM-FI-JPG. 

## 4.9.3 FM REF-FI-CHIP 

This function block describes requirements how facial images are stored as reference data in context of elec tronic chips. 

## 4.9.3.1 Requirements on Chip Facial Images 

According to the [BIB_ICAO_9303] and the FM COM-FI-JP2 the data SHALL be put on the chip. 

## 4.10 FM Category Biometric Comparison 

The Function Module Biometric Comparison (CMP) encloses the mechanisms and algorithms to verify or identify an identity based on a 1:1 or 1: _n_ biometric comparison between reference data and a current biometric probe (usually a live presented image) regardless of where the reference is stored (e.g. passport, identity card, Automated Biometric Identification System (ABIS), database, ...). 

It is RECOMMENDED that the verifications conducted during sequence checks comply with this FM. 

Federal Office for Information Security 

52 

4 Function Modules 

## 4.10.1 FM CMP-FP-VER 

This Function Module contains requirements for the verification of an identity in relation to stored reference fingerprint images. 

## 4.10.1.1 Requirements 

## 4.10.1.1.1 Requirements on the Algorithm Performance 

The following requirements SHALL be met for a fingerprint verification algorithm: 

- The fingerprint verification algorithm has to be configured at a security level (threshold) guaranteeing a false-match-rate (FMR) of 0.1 % (1:1000) in conjunction with a false-non-match-rate (FNMR) less than 2 %. 

- The threshold SHALL be configurable to allow for stricter settings when necessary. 

- Furthermore, the overall system has to be calibrated for the security level set within this specific scenario of verification. The vendor of the verification algorithm has to provide calibration data based on the actual verification performance. 

- The output of the algorithm SHALL be a comparison score[6] and the result of the verification (the achieved FMR and an indication whether the threshold has been reached) depending on the chosen security level (threshold) of the algorithm. 

To ensure the validity of proclaimed values, a vendor SHALL provide test results that support the designated claim. The following requirements apply to those test results: 

- The vendor SHALL provide a Detection Error Trade-Off (DET) curve of the algorithm performance. 

- Such performance SHALL be on the basis of images of comparable characteristic (e.g. images in size and resolution and pose variation of a typical ePassport deployment). 

## 4.10.1.1.2 Requirements on the System Performance 

The following requirements SHALL be met for the system performance (including failure to enrol (FTE)) and failure to aquire (FTA) rates): 

The false reject rate (FRR) SHALL be less than 4 % at a false accept rate (FAR) of 0.1 %. 

## 4.11 FM Category Logging 

The Function Module Logging (LOG) contains logging requirements. The requirements of this chapter and the requirements of the schema of information to log apply both. 

## 4.11.1 FM LOG-ALL-GENERIC 

The Function Module Logging contains requirements as to which data has to be logged for a specific appli cation. 

## 4.11.1.1 Requirements 

- A transaction SHALL cover all information concerning one single biometric subject. Created IDs (except the transaction UUID) only need to be unique locally within one transaction, as usually only one transaction is stored per XML-file. However, for scenarios where multiple transactions are collected within one XMLfile, the created IDs SHALL be unique globally. 

- During the biometric process all available data SHALL be gathered / created by the application. 

- generic process information: 

> 6 Typically a vendor-specific uncalibrated raw score 

Federal Office for Information Security 

53 

4 Function Modules 

   - name of the implemented application profile (e.g. BCL_ManualBorderControl) if suitable (for scheme version 4v7) 

   - a globally unique Transaction ID conforming to [BIB_RFC4122] Version 1 UUID specification 

   - global start time of the transaction (timestamp of the beginning of the biometric process as defined by the application profile[7] ) 

   - global end time of the transaction (timestamp of the end of the biometric process as defined by the ap plication profile) 

   - fully qualified host name (or if not available any other locally unique identifier serving as host name) of the station 

   - type of station (e.g. stationary/mobile) 

   - location of station (The exact semantic of this value is profile-dependent. See the specific profile for a refined definition.) 

   - the software used in this transaction (biometric component), at least with the following identifiers 

      - vendor name 

      - software name 

      - version number (Using a version numbering scheme which allows for proper lexicographic ordering is highly recommended) 

      - optional configuration information 

   - error code (optional) detailing any abnormal termination of the process 

   - a transaction reference if this transaction is dependent or derived from another transaction (reference to Transaction ID) 

- information about any identification processes performed during this transaction: 

   - start time of the identification process (i.e. beginning of capturing biometric data) 

   - submit time of the identification process (i.e. when the captured data is submitted to the backend system for identification) 

   - end time of the identification process (i.e. when the results from the backend system are available or the process terminated with a timeout) 

   - a list of modalities used for identification 

   - the result of the identification 

   - the count of candidates available 

   - for each candidate: 

      - the rank of the candidate 

      - score and threshold information 

   - an error code in case of abnormal termination of the identification process 

- information about any enrolment processes performed during this transaction: 

> 7 For example this may be the moment in time when the operator has started the process by clicking on "start acquisition". 

Federal Office for Information Security 

54 

4 Function Modules 

   - start time of the enrolment process (i.e. beginning of capturing biometric data) 

   - optional submit time of the enrolment process (i.e. when the captured data is submitted to the backend for identification). This element SHALL be present in cases where the central system replies directly with enrolment status information. 

   - end time of the enrolment process (e.g. when the process terminated with a timeout) 

   - a list of modalities used for enrolment 

   - the enrolment status (i.e. whether the subject was enrolled successfully) 

   - an error code in case of abnormal termination of the enrolment process 

   - information about any control verifications performed during enrolment 

- information about any verification processes performed during this transaction 

   - start time of the verification process (i.e. beginning of capturing biometric data) 

   - end time of the verification process 

   - information about the references used for this verification processes (image type, position codes) 

   - the verification result 

   - for each verification: 

      - the verification result 

      - for each comparison: the result of the comparison, the duration of the comparison process, detailed scoring and threshold information and an error code in case of abnormal termination of the compa rison process 

      - an error code in case of abnormal termination of the verification process 

- information about the records collected in this transaction: 

   - unique ID of record 

   - size of record 

   - type of record (encoding format) 

   - purpose of the record (enrolment, identification, verification) 

The vendor SHALL provide a detailed list of error codes used with complete semantic descriptions. 

## 4.11.2 FM LOG-ALL-GID 

This Function Module block describes additional requirements and interfaces for the logging of process in formation for the application of German Identity Documents. 

## 4.11.2.1 Requirements 

The following additional data SHALL be gathered during the biometric process: 

- Information whether fingerprint are legally allowed to be captured (i.e. person not under age) 

- Information about the applicant’s choice of not including fingerprints in the document 

The location shall be logged by the “Behördenkennziffer” (BHKZ). 

## 4.11.3 FM LOG-FP-GENERIC 

This Function Module describes requirements and interfaces for the logging of information regarding finger print images for all profiles. 

## 4.11.3.1 Requirements 

Within a transaction for each set of fingerprints used for enrolment / verification / identification, all available data items SHALL be collected 

Federal Office for Information Security 

55 

4 Function Modules 

- name of the implemented application profile (e.g. BCL_ManualBorderControl) if suitable (for scheme ver sion 4v7) 

- the purpose of the acquisition (enrolment, identification, verification) 

- the overall result for the acquisition process (for scheme version 4v7) 

- start time of the fingerprint acquisition process 

- end time of the fingerprint acquisition process 

- the time out if configured (for scheme version 4v7) 

- software components used in this fingerprint acquisition process 

- hardware components used in this fingerprint acquisition process 

- the finger capture mode (plain, rolled, contactless) 

- information about missing fingers (in relation to the requirement of the profile) 

- information for each capture process for a dedicated fingerprint of the slap, detailing: 

   - fingerprint or slap code 

   - duration of the capture 

   - information whether this capture satisfies the quality requirements of the profile 

   - count of single capture attempts performed for this fingerprint of the slap 

   - the capture number of the selected fingerprint or slap in case of multiple acquisitions 

   - results from the control verification process for each finger (when comparing a rolled image against a finger extracted from a control slap) 

   - reference to the selected probe 

   - for each capture attempt, detailing: 

      - whether this was an acceptable capture attempt (from the application software perspective, indepen dent of the quality assessment) 

      - the duration of the capture attempt 

      - in case of an unacceptable capture attempt: the reason for rejecting this capture attempt and an error code detailing the reason for rejection (SHOULD be present when acceptableCapture is false, it SHALL be present when the rejection reason is "other") 

- For the best capture attempt, detailed quality information about the result SHALL be logged. For all other capture attempts detailed quality information, if calculated during the process, SHOULD be logged: 

   - information about the quality assessment software 

   - duration of quality assessment 

   - detailed quality values in the range 0-100 

   - fingerprint or slap code 

   - any error code in case of abnormal termination of the quality assessment 

- for the acquisition of slaps: finger classifier information, detailing: 

   - information about the slap classifier algorithm 

   - information whether the classifier has been used in evaluation mode 

   - classification result 

   - information about the configured threshold of the algorithm 

- uniqueness check information, detailing: 

Federal Office for Information Security 

56 

4 Function Modules 

   - information about the uniqueness check algorithm 

   - the configured security level (only required, if known) 

   - information about potential duplicates including finger codes and detailed scoring information 

   - any error code in case of abnormal termination of the uniqueness check 

- information about PAD data during the capture: 

   - information about the PAD subsystem 

   - the overall PAD assessment result 

   - for each probe: 

      - the PAD result 

      - detailed PAD quality values accompanied by identifiers, upper and lower value bounds and upper and lower threshold bounds 

- an error code in case of abnormal termination of the fingerprint acquisition process 

- information about the user interface: 

   - an indication of a displayed PAD alert if PAD was performed during the acquisition process, the PAD result was at least once detected and displayed to the operator during the acquisition process 

   - an indication that a live feedback screen was available to the biometric subject if alive feedback screen was available to the biometric subject 

the vendor SHALL provide a detailed list of error codes used with complete semantic descriptions 

## 4.11.4 FM LOG-FP-GID 

This function block describes the requirements for the logging of fingerprint quality information data used within application for German Identity Documents. 

## 4.11.4.1 Requirements 

## 4.11.4.1.1 Central Reference Algorithms 

For the assessment of the fingerprint quality information data, the document producer SHALL apply a cen tral reference quality algorithm to all incoming fingerprints. Alternative or additional reference algorithms (comparators or quality algorithms) MAY be defined by the technical responsible authority. 

The output of the quality algorithm shall be encoded in XML according to the „fp-gid-eval“ record structure, according to FM COD-ALL-GID. 

## 4.11.4.1.2 Collection of Data for the Central Statistics 

The document producer is responsible for the data collection for the central statistics. 

The following data SHALL be collected from each application: 

- authority identification number 

- all quality information from the application according to FM Category Logging, in particular 

   - information about the quality assessment software 

   - duration of quality assessment 

   - detailed quality values in the range 0-100 

   - fingerprint or slap code 

   - any error code in case of abnormal termination of the quality assessment 

Additionally, the data of the reference algorithms, as described above, SHALL be stored in the central statistics. 

Federal Office for Information Security 

57 

4 Function Modules 

The storage scheme SHALL be devised by the given types of the corresponding XML encoding, it shall be able to reproduce the complete content of the originally received „fp-gid-eval“. 

## 4.11.4.1.3 Export of Data from the Central Statistics 

As an export format, the given „fp-gid-eval“ record structure, according to FM Category Coding, sorted by authority identification number, SHALL be used. 

## 4.11.4.1.4 Omission of Person-Related Data 

No person-related data SHALL be saved for QA statistics. 

## 4.11.4.1.5 Storage Duration and Deletion of Data from the Central Statistics 

The data of the central statistics SHALL be stored for a duration of 36 months. Data of the central statistics, which are older than 36 months, SHALL be deleted monthly. 

## 4.11.5 FM LOG-FI-GENERIC 

This Function Module describes requirements and interfaces for the logging of information regarding facial images for all profiles. 

## 4.11.5.1 Requirements 

Within a transaction for each facial image used for enrolment / verification / identification, all available data items SHALL be collected 

- name of the implemented application profile (e.g. BCL_ManualBorderControl) if suitable (for scheme ver sion 4v7) 

- the overall result for the acquisition process (for scheme version 4v7) 

- the purpose of the acquisition (enrolment, identification, verification) 

- start time of the facial acquisition process 

- end time of the facial acquisition process 

- the time out if configured (for scheme version 4v7) 

- software used in this facial acquisition process 

- hardware used in this facial acquisition process 

- the source of the facial image under consideration 

- the count of face captures performed 

- for each face capture: 

   - if a veto was put by the operator: the type of veto (OK/NOK) 

   - the operation mode (if information is available) 

   - the vertical position of the camera (if information is available, for scheme version 4v7) 

   - the illumination level (if information is available, for scheme version 4v7) 

   - the focus distance (if information is available, for scheme version 4v7) 

- for the selected capture, detailed quality information about the result, detailing: 

   - information about the quality assessment software 

   - duration of quality assessment 

   - detailed quality values accompanied by: 

Federal Office for Information Security 

58 

4 Function Modules 

      - identifiers 

      - upper and lower value bounds, if available 

      - upper and lower threshold bounds, if available 

   - any error code in case of abnormal termination of the quality assessment 

- information about PAD data during the capture: 

   - information about the PAD subsystem 

   - the overall PAD assessment result 

   - for each probe: 

      - the PAD result 

      - detailed PAD quality values accompanied by identifiers, upper and lower value bounds and upper and lower threshold bounds 

- information about the user interface: 

   - an indication of a displayed PAD alert if PAD was performed during the acquisition process, the PAD result was at least once detected and displayed to the operator during the acquisition process 

   - an indication that a live feedback screen was available to the biometric subject if a live feedback screen was available to the biometric subject 

- an error code in case of abnormal termination of the facial acquisition process 

the vendor SHALL provide a detailed list of error codes used with complete semantic descriptions 

## 4.11.6 FM LOG-FI-GID 

This function block describes the best practice for the logging of photo quality information data used during application for German Identity Documents. 

## 4.11.6.1 Requirements 

## 4.11.6.1.1 Central Reference Algorithms 

For the assessment of the photo quality information data, the document producer SHALL apply a central re ference quality algorithm to all incoming facial images. Alternative or additional reference algorithms (com parators or quality algorithms) MAY be defined by the technical responsible authority. 

The output of the quality algorithm SHALL be encoded in XML according to the „ph-gid-eval“ record struc ture, according to FM COD-ALL-GID. 

## 4.11.6.1.2 Collection of Data for the Central Statistics 

The document producer is responsible for the data collection for the central statistics. 

The following SHALL be collected from each application. 

- authority identification number 

- all quality information from the application, in particular 

   - information about the quality assessment software 

   - duration of quality assessment 

   - detailed quality values accompanied by 

   - identifiers 

   - upper and lower value bounds 

   - upper and lower threshold bounds 

   - any error code in case of abnormal termination of the quality assessment 

Federal Office for Information Security 

59 

4 Function Modules 

Additionally, the data of the reference algorithms, as described above, SHALL be stored in the central statistics. 

The output of the quality algorithm SHALL be encoded in XML according to the „ph-gid-eval“ record struc ture, according to FM COD-ALL-GID. 

## 4.11.6.1.3 Export of Data from the Central Statistics 

As an export format, the given „ph-gid-eval“ record structure according to FM COD-ALL-GID, sorted by authority identification number, SHALL be used. 

## 4.11.6.1.4 Omission of Person-Related Data 

No person-related data SHALL be saved for QA statistics. 

## 4.11.6.1.5 Storage Duration and Deletion of Data from the Central Statistics 

The data of the central statistics SHALL be stored for a duration of 36 months. Data of the central statistics, which are older than 36 months, SHALL be deleted monthly. 

## 4.12 FM Category Coding 

This Function Module Coding (COD) contains the procedures to encode quality data as well as biometric data in defined formats. Interoperability is provided by means of standard compliant coding. 

## 4.12.1 FM COD-ALL-GID 

This function block describes requirements and interfaces for the overall coding of biometric data used within the context of the German Identity Documents. 

## 4.12.1.1 Requirements 

- The logging data as defined by the Section 4.11 SHALL be encoded as XML according to the schema defini tion as `gid-app` element. The XML encoding is defined by the XML schema definition in the file "gid4v6.xsd" and referenced schema files. Note that the corresponding XML schemata are always published together with the Technical Guideline (TR) and can be obtained from the same location. 

- Optional attributes and elements of the schema SHALL be considered as far as possible (e.g. error codes only need to be logged, in case an error occurred; an acquisition element is only required, in case an acquisition process has at least been started). 

- All log data SHALL be encoded as far as it is available throughout the acquisition process (e.g. fingerprint quality data is encoded if and only if fingerprint capture was performed). 

- The biometric data containers SHALL be embedded in the XML log ( `Record` element). 

## 4.12.2 FM COD-FP-GID 

This function block describes requirements and interfaces for the coding of fingerprint images used for app lication of German Identity Documents. 

## 4.12.2.1 Requirements 

The biometric data (zero, one or two fingers) SHALL be coded as a Biometric Information Template (BIT) ac cording to [BIB_ISO_19785-3]. The BIT SHALL contain at least the fields header version, Biometric Data Block (BDB) Format Owner, BDB Format Type, BDB Biometric Type, and BDB Biometric Subtype in the header and BDB data according to [BIB_ISO_FINGER]. The field for finger image quality information defined in [ISO_FIN GER] SHALL be occupied with the result of the quality evaluation algorithm (of the selected fingerprint). The BIT SHALL be encoded Base64 and stored in the output XML data. 

Note, it SHALL be the task of the document producer to combine the BIT into the data group 3 according to [BIB_ICAO_9303]. 

Federal Office for Information Security 

60 

4 Function Modules 

## 4.12.2.2 Working Example 

This working example ( Table 4.8) gives an overview how a WSQ image (containing the finger image) MAY be extracted by the application from the BIT. The BIT is composed of the Biometric Header Template (BHT) and the BDB containing the general record header, the finger image header record, and the finger image data. In the example "??" is representing a placeholder for a byte and `<WSQ>` is representing a placeholder for the actual fingerprint image). 

|**Tag**|**Length**|**Value**|||||
|---|---|---|---|---|---|---|
|7F60|var.|BIT|||||
|||**Tag**|**Length**|**Value**|||
|||A1|var.|**Biometric Header Template**|||
|||||**Tag**|**Length**|**Value**|
|||||80|02|0101<br>CBEFF_patron_header_version|
|||||81|01|08<br>CBEFF_BDB_biometric_type|
|||||82|01|??<br>CBEFF_BDB_biometric_subtype|
|||||87|02|0101<br>CBEFF_BDB_format_owner (ISO/IEC JTC 1 SC<br>37-Biometrics)|
|||||88|02|0007<br>CBEFF_BDB_format_type (ISO/IEC JTC 1 SC 37-<br>Biometrics)|
||||**Tag**|**Length**|**Value**||
||||5F2E|var.|**CBEFF BDB**||
||||||**General Record Header**||
||||||46495200<br>Format Identifier (Finger Image Record (FIR))||
||||||30313000<br>Version Number (“010”)||
||||||32+ 1 * (14 bytes + Data length)<br>Record Length (6 bytes)||
||||||?? ??<br>Capture device ID (2 bytes, Vendor specified)||
||||||001F (Level 31) or 0029 (Level 41)<br>Image Acquisition Level||
||||||01<br>Number of fingers||
||||||01<br>Scale units||
||||||01F4<br>Scan resolution (horizontal) (500ppi)||



Federal Office for Information Security 

61 

4 Function Modules 

|**Tag**|**Length**|**Value**|||||
|---|---|---|---|---|---|---|
||||||01F4<br>Scan resolution (vertical) (500ppi)||
||||||01F4<br>Image resolution (horizontal)||
||||||01F4<br>Image resolution (vertical)||
||||||08<br>Pixel depth||
||||||02<br>Image compression algorithm (WSQ)||
||||||0000<br>Reserved||
||||||**Finger Image Header Record**||
||||||?? ?? ?? ??<br>Length of finger data block||
||||||07<br>Finger position (e.g. left index finger)||
||||||01<br>Count of views||
||||||01<br>View number||
||||||??<br>Finger image quality||
||||||00<br>Impression type||
||||||?? ??<br>Horizontal line length||
||||||?? ??<br>Vertical line|length|
||||||00<br>Reserved||
||||||**Finger Image Data**||
||||||`<WSQ>`||



**Table 4.8** Example for a Data Element containing a WSQ Image 

As an example the following BIT in hexadecimal representation is presumed ( representing a placeholder with variable length, ?? representing a placeholder for a byte, and WSQ representing a placeholder for the actual fingerprint image): 

```
7F 60 $$ A1 $$ 80 02 01 01 81 01 08 82 01 ?? 87 02 01 01 88 02 00 07 5F 2E 46 49 52 00 30 31 30
 00 ?? ?? ?? ?? ?? ?? ?? ?? 00 1F 01 01 01 F4 01 F4 01 F4 01 F4 08 02 00 00 ?? ?? ?? ?? 07 01
 01 ?? 00 ?? ?? ?? ?? 00 WSQ
```

Federal Office for Information Security 

62 

4 Function Modules 

## 4.12.2.2.1 Requirements on XML Encoding 

The following section specifies requirements for data coding for the purpose of sending the fingerprint images to the document producer. 

- The XML-element `FingerAcquisition` SHALL occur at least once for applicants older than 6 years applying for: 

   - Resindence Permit. 

   - Passport. 

   - Identity Card (from 2. August 2021). 

- The XML-element `FingerAcquisition` SHALL NOT occur for applicants younger than 6 years. 

- The XML-element `FingerAcquisition/Records` MAY be missing e.g. if fingers are physically impossible to acquire. 

- The XML-element `FingerAcquisition/Records` SHALL occur at maximum once in one of the `FingerAcquiss tion` XML-elements. 

- The XML-element `FingerAcquisition/Records/XMLRecord` SHALL NOT be used. 

- The XML-element `FingerAcquisition/Records/Record` SHALL occur at least once and at maximum two times. 

- The XML-attribute `FingerAcquisition/Records/Record/@type` SHALL be _icao-cbeff-bit-bdb-19794-4_ 

- The XML-element `FingerAcquisition/Records/Record/Data` SHALL occur exactly once per record. 

## 4.12.3 FM COD-FI-GENERIC 

This function block describes requirements for the coding used during the acquisition process of facial images. 

## 4.12.3.1 Requirements 

All results of the acquisition process SHALL be encoded in XML as `FaceAcquisition` . 

The XML encoding is defined by the XML schema definition in `biotypes4v7.xsd` for volumes BCL and IMA or `biotypes4v6.xsd` . 

## 4.12.4 FM COD-FI-GID 

This function block describes requirements and interfaces for the coding of facial images used for application of German Identity Documents. 

## 4.12.4.1 Requirements on Chip Facial Images 

The biometric data (face) SHALL be coded as a BIT according to [BIB_ISO_19785-3]. The BIT SHALL contain at least the fields header version, BDB Format Owner, BDB Format Type, BDB Biometric Type, and BDB Bio metric Subtype in the header and BDB data according to [BIB_ISO_FACE] containing a Full Frontal JPEG 2000 image, refer to FM Category Compression. The BIT SHALL be encoded Base64 and stored in the output XML data. 

## 4.12.4.2 Requirements on Facial Images for Local Reference Storage 

The biometric data (facial image) SHALL be encoded as JPG image, refer to FM Category Compression. 

## 4.12.4.3 Requirements on XML Encoding 

The following section specifies requirements for data coding for the purpose of sending the facial image to the document producer. 

- The XML-element `FaceAcquisition` SHALL occurs once. 

- The XML-element `FaceAcquisition/Records` SHALL occur once. 

- The XML-element `FaceAcquisition/Records/XMLRecord` SHALL NOT be used. 

Federal Office for Information Security 

63 

4 Function Modules 

- The XML-element `FaceAcquisition/Records/Record` SHALL occur once. 

- The XML-element `FaceAcquisition/Records/Record/@type` SHALL be _icao-cbeff-bit-bdb-19794-5_ . 

- The XML-element `FaceAcquisition/Records/Record/Data` SHALL occur once. 

## 4.13 FM Category Evaluation 

This Function Module Evaluation contains methods and interfaces which are used in the scope of evaluation based on the specified log data of this Technical Guideline. 

## 4.13.1 FM EVA-ALL-GENERIC 

This Function Module defines general requirements for evaluations realized by plots, graphics and tables. 

## 4.13.1.1 Requirements 

The general requirements for plots, graphics, tables etc. defined in this module SHALL apply for all evaluations if not overruled by evaluation specific requirements. 

## 4.13.1.2 Representation of Component Information 

If an evaluation specification requires to use information of an XML-element of type `type.component` , e.g. for a software or hardware, a string concatenation of its child elements `Vendor` , `Name` , `Version` and `FirmwareVersion` SHALL be used to represent the XML-element of type `type.component` . If a child element is empty, this child element SHALL be excluded from the string representation. 

If the child element `ConfigurationInformation` is used for the application, the configuration information SHALL be added to the string representation if reasonable for the specific evaluation e.g. if the configuration parameter may influence the aspects addressed by the specific evaluation. 

The elements of the string representation SHALL be separated by “,”. 

## 4.13.1.3 Number and Date Formatting 

The following applies for all numbers in plots, graphics and tables: 

- The “.” or a blank SHALL be used as thousands separator. 

- The “,” SHALL be used as decimal separator. 

- Small numerics, i.e. smaller than 10 _[¡]_[4] , SHOULD be denoted in scientific notation e.g. 5 _;_ 34 _¢_ 10 _[¡]_[7] . 

- Large numerics, i.e. bigger than 10[6] , SHOULD be denoted in scientific notation or by reasonable abbrevia tions e.g. “M” for million. 

- Decimal fractions SHOULD be rounded to not more than two digits. 

- Relative frequencies SHALL be noted as decimal. 

The following applies for all numbers in tables: 

Leading zeros in the table body’s cells SHOULD be omitted for decimal fractions e.g. “.34” instead of “0.34”. 

The following applies for all dates in plots, graphics and tables: 

- The order of date components SHALL be (year, month, day). Note, that not all components are required. 

- Day, month and year components SHALL be numeric. 

- The “.” SHALL be used as separator between numeric components. 

- Leading zeros SHALL be used to fill up numeric months and days to two digits. 

- Years SHALL be presented by four digits. 

## 4.13.1.4 Use of Colours 

The following requirements apply for colours used in plots and graphics: 

Federal Office for Information Security 

64 

4 Function Modules 

- The used colours SALL be consistent over all plots and graphics generated. Colours SHALL be consistent over variable types, i.e. the same colour schema SHALL be used for the same variable type in different plots and graphics. 

- Colours commonly connoted with specific attributes SHALL be used only in coherence to the coloured object’s meaning e.g. a plot or graphic object indicating an error fraction SHALL NOT be coloured green. 

- If no need to use more than one colour in a plot or graphic, e.g. to distinguish different types of plot elements by colour or to emphasis the denotation of an element by colour, the default colour SHOULD be black. 

If more than one colour is used in a plot, a meaningful legend SHALL explain the applied colour schema. 

Two RECOMMENDED colour palettes for e.g. line colours or stacked bar plot partitions are given in Table 4.9. 

|**Palette 1 Hex Colour Codes**|**Palette 2 RGB Colour Codes**|
|---|---|
|#3E647D|255, 200, 25|
|#7B92A8|242, 133, 2|
|#82C0E9|196, 0, 70|
|#2D6D66|137, 13, 72|
|#BFA19C|0, 184, 242|
|#008BBC|7, 120, 165|
|#97B6B0|0, 79,128|
|#D7D29E|116, 185, 23|
|#1A476F|35, 97, 78|
|#90353B|107, 117, 129|
|#9C8847||
|#938DD2||
|#6E8E84||
|#C10534||
|#CAC27E||



**Table 4.9** Recommended Colour Palettes 

## 4.13.1.5 Definitions of Terms 

The term "Geographic Region" SHALL be defined according to [BIB_UN REGIO]. 

## 4.13.1.6 Trimmed Values 

For trimming of values the following applies: 

- Trimming of values SHALL only be allowed for input variables of plots and graphics to e.g. remove outliers. 

- Trimming of values SHALL NOT be allowed for any kind of variables in table presentation, especially in lookup tables. 

- In case plot input variables have been trimmed, the trimming method and parameters as well as the number of excluded observation SHALL be denoted as remark at the resulting plot or graphic. 

- Trimming in context of this document refers to omitting the visualisation of the trimmed data e.g. for a box plot, the median and quartiles of the box SHALL still be calculated based on the total data but not on the trimmed data. However, the trimmed data points SHALL NOT be depicted in the box plot as outliers. 

## 4.13.1.7 Plots, Graphics and Table in General 

The following applies for all plots, graphics and tables: 

- An explanatory description for each plot, graphic and table SHALL be given within a generated report. 

Federal Office for Information Security 

65 

4 Function Modules 

- Every plot, graphic or table SHALL have a meaningful caption or heading. 

- If finger codes are used, they SHALL be explained at the plot, graphic or table e.g. by a label or footnote. 

- The units of axis, cell values and other metrics SHALL be denoted either at each value or annotated as e.g. footnote or label of axis, rows, columns. 

## 4.13.1.8 Plots and Graphics in General 

The following applies for all plots and graphics: 

- Every axis of a plot or graphic SHALL have a meaningful labelling. 

- If not specifically defined by the plot definition, plot axis and their labels SHALL be scaled and chosen meaningfully. 

- Every plot with multiple colours or other means of coding to distinguish elements SHALL have a mea ningful legend explaining the coding. 

- If an axis range is defined on an interval, e.g. [0,1] or [0,100], the respective axis SHALL be scaled for the full interval e.g. quality scores (0 to 100) or relative frequencies (0 to 1). 

## 4.13.1.9 Plots and Graphic Types 

The following plot and graphic types MAY be used by evaluation modules. The subsequent general plot and graphic requirement applies if not otherwise specified by the specific evaluation. 

## 4.13.1.9.1 Pie Charts 

It is RECOMMENDED to use stacked bar plots instead of pie charts. 

## 4.13.1.9.2 Heat Map 

A heat map depicts the values of a matrix by colours. Thereby, the following applies: 

The matrix cell values SHALL be mapped to a colour via two steps. Step 1 SHALL map every cell value to a value in the range [0,1]. Step 2 SHALL map every value within the range [0,1] to a heat colour. The exact computation SHALL be conducted in the following way: 

- Step 0 

   - If negative cell values are given in the relevant matrix, Step 0 SHALL be executed before the other Steps 1 and 2. 

   - Step 0 SHALL subtract from every cell value the minimum value of the column (case 1), the row (case 2) or of the whole matrix (case 3). In this way all values are mapped to non-negative numbers. Then all the other computations SHALL build on the non-negative cell values. 

- Step 1 

   - The matrix SHALL depict the values of the cells relatively to a given maximum value. Three types of modalities are possible: The cell values colours can orientate on 

      - the maximum value in their column (case 1) or 

      - the maximum value in their row (case 2) or 

      - the maximum value of the entire matrix (case 3). 

   - Which of the possible cases SHALL be considered is defined in the specifications of this Technical Gui deline for the respective heat map by the "Colour" attribute. It SHALL be visible to the viewer of heat map if the maximum of the columns, the rows or the entire table is considered. This can be done by a legend to the plot or a footnote. 

   - Every cell value SHALL be divided by … 

Federal Office for Information Security 

66 

4 Function Modules 

      - the maximal value of the column (case 1) 

      - the maximal value of the row (case 2) 

      - the maximal value of the hole matrix (case 3) 

   - In this way every cell SHALL be mapped to a value in the range [0,1]. Every maximal value SHALL be mapped to the value 1. Please note that this computation SHALL only be used to compute the heat map colour and SHALL NOT be used to label the cells itself (except for the case that it is the same value). 

- Step 2: The values derived in Step 1 SHALL be mapped to a colour following the mapping defined in Ta ble 4.10. Every maximal value of the column (case 1), of the row (case 2) or of the entire matrix (case 3) SHALL be coloured in `#FF0000` . Note, multiple maxima MAY be possible. 

|**ID**|**Value Interval**|**Corresponding Colour of the Heat Map Cell**|
|---|---|---|
|1|[0, 0.05]|#FFFFE6|
|2|(0.05, 0.1]|#FFFFB3|
|3|(0.1, 0.15]|#FFFF80|
|4|(0.15, 0.2]|#FFFF4D|
|5|(0.2, 0.25]|#FFFF19|
|6|(0.25, 0.3]|#FFFF00|
|7|(0.3, 0.35]|#FFED00|
|8|(0.35, 0.4]|#FFDB00|
|9|(0.4, 0.45]|#FFC800|
|10|(0.45, 0.5]|#FFB600|
|11|(0.5, 0.55]|#FFA400|
|12|(0.55, 0.6]|#FF9200|
|13|(0.6, 0.65]|#FF8000|
|14|(0.65, 0.7]|#FF6D00|
|15|(0.7, 0.75]|#FF5B00|
|16|(0.75, 0.8]|#FF4900|
|17|(0.8, 0.85]|#FF3700|
|18|(0.85, 0.9]|#FF2400|
|19|(0.9, 0.95]|#FF1200|
|20|(0.95, 1]|#FF0000|



**Table 4.10** Heat Map Colours 

An exemplary heat map is depicted in Figure 4.1. In this example the colours of the cells are derived relatively to the maximum value of the matrix (case 3) which occurs in the fourth row and the fourth column of the matrix. 

Federal Office for Information Security 

67 

4 Function Modules 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0076-01.png)


**Figure 4.1.** Example Heat Map 

## 4.13.1.9.3 Box Plot 

A box plot depicts distributions by central distribution metrics. Thereby, the following applies: 

- The lower whisker SHALL be at maximum within a 1.5 inter quartile range from the lowest quartile and the higher whisker shall be within a 1.5 inter quartile range from the highest quartile. 

- Outliers SHOULD be depicted as black filled dots with 33% transparency. 

- An exemplary box plot is depicted in Figure 4.2. 

Federal Office for Information Security 

68 

4 Function Modules 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0077-01.png)


**Figure 4.2.** Example Box Plot 

## 4.13.1.9.4 Scatter Plot 

A scatter plot depicts two dimensional data points on an X- and Y-axis. Thereby, the following applies: Data points SHALL be depicted as filled dots with 33% transparency. 

An exemplary scatter plot is depicted in Figure 4.3. 

Federal Office for Information Security 

69 

4 Function Modules 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0078-01.png)


**Figure 4.3.** Example Scatter Plot 

## 4.13.1.9.5 Line Plot 

A line plot depicts two dimensional data points on an X- and Y-axis. Thereby, the following applies: 

- Data points SHALL be connected by straight lines. 

- Data points SHALL be visible i.e. not only the line shall be depicted. 

An exemplary line plot is depicted in Figure 4.4. 

Federal Office for Information Security 

70 

4 Function Modules 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0079-01.png)


**Figure 4.4.** Example Line Plot 

## 4.13.1.9.6 Histogram 

A histogram is composed of vertical columns plotted on a graph for which the following applies: 

- Histograms SHALL be based on continuous variables. 

- It is RECOMMENDED that there is no space between adjacent columns. 

- The X-axis labels SHALL be single values or a range of value descriptions, i.e. bin names. 

- The height of each individual column SHALL indicate the size of the group defined by the column bin. 

- The Y-axis SHALL be located at the left hand side of the histogram. 

- The median of the input variable SHALL be indicated by a red solid vertical line. 

- The mean of the input variable SHALL be indicated by a red dashed vertical line. 

- If the number of bins is not defined by the evaluation, the number of bins SHOULD be calculated by Scott's formula, refer to Equation 4.3, or Sturges' formula, refer to Equation 4.4. Whereby _k_ denotes the number of bins, _¾_ the standard deviation of the input data and n the number of data points. 

- If the data is of type integer the number of bins _k_ SHALL NOT be greater than the range of the data plus one e.g. the minimum data point is -5 and the maximum data point is 64, the number of bins SHALL NOT be greater than 70. 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0079-14.png)



![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0079-15.png)



![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0079-16.png)


An exemplary histogram is depicted in Figure 4.5. 

Federal Office for Information Security 

71 

4 Function Modules 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0080-01.png)


**Figure 4.5.** Example Histogram Plot 

## 4.13.1.9.7 Histogram with Empirical Cumulative Distribution Function 

A histogram with empirical cumulative distribution function is a histogram with an empirical Cumulative Distribution Function (CDF) added to the base histogram plot. All requirements for histograms apply. In ad dition, the following applies: 

- The CDF SHALL be plotted as step function. 

- No additional X-axis for the CDF SHALL be added to the base histogram. 

- An additional Y-axis for the CDF SHALL be added to the base histogram on the right hand side, the histo gram Y-axis SHALL be on the left hand side. 

- The CDF Y-axis SHALL be scaled from 0 to 1 by 0.1 steps. 

It is RECOMMENDED to colour the CDF and its Y-axis in red. 

An exemplary histogram with empirical CDF is depicted in Figure 4.6. 

Federal Office for Information Security 

72 

4 Function Modules 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0081-01.png)


**Figure 4.6.** Example Histogram with Empirical Cumulative Distribution Function 

## 4.13.1.10 Bar Plot 

A bar plot is composed of vertical or horizontal bars plotted on a graph for which the following applies: 

- The bars SHALL be labelled. 

- A bar label SHALL represent a categorical variable. 

- The height of a bar SHALL indicate the size of the group defined by the bar label. 

- An exemplary bar plot is depicted in Figure 4.7. 

Federal Office for Information Security 

73 

4 Function Modules 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0082-01.png)


**Figure 4.7.** Example Bar Plot 

## 4.13.1.11 Stacked Bar Plot 

A stacked bar plot is a bar plot whose columns are partitioned by the relative frequencies of a variable. The following applies for stacked bar plots: 

- Partitions SHALL be separated by different colours. 

- If multiple bars are present, the order of partitions SHALL be consistent across all bars. 

It is RECOMMENDED to add an axis for both, relative frequencies and absolute frequencies. 

An example horizontal stacked bar plot is depicted in Figure 4.8, an example vertical stacked bar plot is depicted in Figure 4.9. 

Federal Office for Information Security 

74 

4 Function Modules 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0083-01.png)


**Figure 4.8.** Example Horizontal Stacked Bar Plot 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0083-03.png)


**Figure 4.9.** Example Vertical Stacked Bar Plot 

## 4.13.1.12 Grouped Bar Plot 

A grouped bar plot displays two variables on the X-axis by grouping the bars for the instances of one variable for every instance of the other variable. It is comparable to a stacked bar plot, where the sub-bars are not stacked but grouped next to each other. The following applies for grouped bar plots: 

- Bars within a group SHALL be separated by different colours. 

- If multiple bar-groups are present, the order of partitions SHALL be consistent across all groups. 

Federal Office for Information Security 

75 

4 Function Modules 

An example for a grouped bar plot is displayed in Figure 4.10. 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0084-02.png)


**Figure 4.10.** Example Grouped Bar Plot 

## 4.13.1.13 Table Types 

For all table types defined subsequently, the following applies: 

- Input data for table representation SHALL never be trimmed by any means. 

- Rows SHALL be visually separated, e.g. by alternating background colour. 

An example table is depicted by Figure 4.11. 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0084-09.png)


**Figure 4.11.** Example Table with Alternation Background Colour 

Federal Office for Information Security 

76 

4 Function Modules 

## 4.13.1.14 Lookup Tables 

A lookup table is designated to convey the exact values of a plot or graphic to the viewer. The following applies: 

- Only the aggregated or processed absolute or relative data which is the direct input for a plot or graphic SHALL be present in the lookup table if not specified otherwise. 

- A plot or graphic SHALL be reproducible, in terms of required data, only by using its corresponding lookup table. 

## 4.13.1.14.1 Lookup Tables Heat Map 

For lookup tables for heat maps the following applies: 

- It is RECOMMENDED to separate relative and absolute frequencies in separated lookup tables. 

- Row and column sums, means and medians SHALL be present for the absolute frequency table. 

- Total sum, mean and median SHALL be present for the absolute frequency table. 

The lookup table for absolute frequencies is defined by the table definition in Table 4.11. 

|**Attribute**|**Value**|
|---|---|
|Name|Heat map absolute frequencies lookup table|
|Purpose|Presenting absolute frequencies and distribution summaries of the input data for a given<br>heat map broken down by the heat map’s dimensions.|
|Row Labelling|The row dimension of the heat map.|
|Column Labelling|The column dimension of the heat map.|
|Cell|The absolute frequency of the heat map’s figure of interest.|
|Miscellaneous|The column and row sum, median and mean shall be present in the lookup table.|



**Table 4.11** Heat Map Absolute Frequency Lookup Table Definition 

An exemplary heat map lookup table for absolute frequencies is depicted in Table 4.12. 

|||**Var1**||||||
|---|---|---|---|---|---|---|---|
|||**Val1.1**|**Val1.2**|**Val1.3**|**Row Sum**|**Row Mean**|**Row Median**|
||Val2.1|Count 4|Count 5|Count 6|Sum Val2.2|Mean Val2.2|Median Val2.2|
||Val2.2|Count 7|Count 8|Count 9|Sum Val2.3|Mean Val2.3|Median Val2.3|
||Val2.3|Count 10|Count 11|Count 12|Sum Val2.4|Mean Val2.4|Median Val2.4|
||Val2.4|Count 1|Count 2|Count 3|Sum Val2.1|Mean Val2.1|Median Val2.1|
||Column Sum|Sum Val1.1|Sum Val1.2|Sum Val1.3|Total Sum|||
||Column Mean|Mean Val1.1|Mean Val1.2|Mean Val1.3||Total Mean||
||Column Medi<br>an|Median Val1.1|Median Val1.2|Median Val1.3|||Total Median|



**Table 4.12** Example Heat Map Lookup Table Absolute Frequencies 

The lookup table for relative frequencies is defined by the table definition in Table 4.13. 

|**Attribute**|**Value**|
|---|---|
|Name|Heat map absolute frequencies lookup table|
|Purpose|Presenting relative frequencies and distribution summaries of the input data for a given heat<br>map broken down by the heat map’s dimensions.|
|Row Labelling|The row dimension of the heat map.|
|Column Labelling|The column dimension of the heat map.|



Federal Office for Information Security 

77 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Cell|The relative frequency of the heat map’s figure of interest.|



**Table 4.13** Heat Map Absolute Frequency Lookup Table Definition 

An exemplary heat map lookup table for relative frequency is depicted in Table 4.14. 

|||**Var1**|||
|---|---|---|---|---|
|||Val1.1|Val1.2|Val1.3|
|Var2|Val2.1|Share 4|Share 5|Share 6|
||Val2.2|Share 1|Share 2|Share 3|



**Table 4.14** Example Heat Map Lookup Table for Relative Frequencies 

## 4.13.1.14.2 Lookup Table Histogram 

For lookup tables for histograms the following applies: 

- For every bin, its name, value and cumulative probability SHALL be present in the lookup table. 

- Mean and median SHALL be listed in the lookup table. 

- The sum of the input variable SHALL be listed at the end of the lookup table. 

The lookup table for histograms is defined by the table definition in Table 4.15. 

|**Attribute**|**Value**|
|---|---|
|Name|Histogram lookup table|
|Purpose|Presenting relative frequencies and distribution summaries of the input data for a given his<br>togram as well as cumulative probabilities.|
|Row Labelling|The bin variable of the histogram. Median and Mean shall be present.|
|Column Labelling|**•**<br>a column representing the absolute frequencies of the bin<br>**•**<br>a column representing the relative frequencies of the bin<br>**•**<br>a column representing the empirical cumulative probability of the bin|
|Cell|The relative, absolute frequencies or cumulative probability of the histogram’s figure of inte<br>rest.|
|Miscellaneous|The absolute sum of the histogram’s figure of interest shall be present in the lookup table.|



**Table 4.15** Histogram Lookup Table Definition 

An exemplary histogram lookup table is depicted in Table 4.16. 

|**Bin**|**Absolute Bin Value**|**Relative Bin Value**|**Empirical Cumulative Probability**|
|---|---|---|---|
|Bin name 1|Bin value 1|Relative Bin value 1|Cumulative probability 1|
|Bin name 2|Bin value 2|Relative Bin value 2|Cumulative probability 2|
|...|...|...|...|
|Bin name_n_|Bin value_n_|Relative Bin value_n_|Cumulative probability_n_|
|Bin name_n-1_|Bin value_n-1_|Relative Bin value_n-1_|Cumulative probability_n-1_|
|Median|Median value|||
|Mean|Mean value|||
|**Sum**|Sum value|1||



**Table 4.16** Example Histogram Lookup Table 

## 4.13.1.14.3 Lookup Table Stacked Bar Plot 

For lookup tables for stacked bar plots the following applies: 

Federal Office for Information Security 

78 

4 Function Modules 

- For every bar, its absolute and relative frequencies SHALL be present. 

- It is RECOMMENDED to separate absolute and relative frequencies in separate lookup tables. 

- The sum of the values of the intra and inter bar variables SHALL be present in the absolute count lookup table. 

- The total sum of counts SHALL be present in the absolute count lookup table. 

Note, a stacked bar plot MAY have only a single stacked bar. In this case, no inter bar variable exists and row and sum columns SHALL be omitted. 

The lookup table for absolute frequency stacked bar plot lookup table is defined by the table definition in Table 4.17. 

|**Attribute**|**Value**|
|---|---|
|Name|Absolute frequency stacked bar plot lookup table|
|Purpose|Presenting absolute frequencies and sums of the input data for a given stacked bar plot.|
|Row Labelling|**•**<br>The stacked bar plot’s intra bar variable.<br>**•**<br>A column sum row.|
|Column Labelling|**•**<br>The stacked bar plot’s inter bar variable.<br>**•**<br>A row sum column.|
|Cell|The absolute frequencies of figure of interest for the stacked bar plot’s partitions.|
|Miscellaneous|The absolute sum of the stacked bar plot’s figure of interest shall be present in the lookup<br>table.|



**Table 4.17** Absolute Frequency Stacked Bar Plot Lookup Table Definition 

An exemplary absolute frequency stacked bar plot lookup table is depicted in Table 4.18. 

|||**Inter Bar Variable**|**Inter Bar Variable**||||
|---|---|---|---|---|---|---|
|||**Val1.1**|**Val1.2**|**Val1.3**|**Val1.4**||
|**Inter Bar Variable**|**Val2.1**|Count|Count|Count|Count|Sum Val2.1|
||**Val2.2**|Count|Count|Count|Count|Sum Val2.2|
||**Val2.3**|Count|Count|Count|Count|Sum Val2.3|
||**Val2.4**|Count|Count|Count|Count|Sum Val2.4|
||**Val2.5**|Count|Count|Count|Count|Sum Val2.1|
||**Sum**|Sum Val1.1|Sum Val1.2|Sum Val1.3|Sum Val1.4|Total Sum|



**Table 4.18** Example Absolute Frequency Stacked Bar Plot Lookup Table 

The lookup table for relative frequency stacked bar plot lookup table is defined by the table definition in Table 4.19. 

|**Attribute**|**Value**|
|---|---|
|Name|Relative frequency stacked bar plot lookup table|
|Purpose|Presenting relative frequencies of the input data for a given stacked bar plot.|
|Row Labelling|The stacked bar plot’s intra bar variable.|
|Column Labelling|The stacked bar plot’s inter bar variable.|
|Cell|The relative frequencies of figure of interest for the stacked bar plot’s partitions.|



**Table 4.19** Relative Frequency Stacked Bar Plot Lookup Table Definition 

An exemplary relative frequency stacked bar plot lookup table is depicted in Table 4.20. 

Federal Office for Information Security 

79 

4 Function Modules 

|||**Inter Bar Variable**|||
|---|---|---|---|---|
|||Val1.1|Val1.2|Val1.3|
|Intra Bar Variable|Val2.1|Share 1|Share 2|Share 3|
||Val2.2|Share 4|Share 5|Share 6|



**Table 4.20** Example Relative Frequency Stacked Bar Plot Lookup Table 

## 4.13.1.14.4 Lookup Table for Box Plots 

For lookup tables for box plots the following applies: For every box, its minimum, first and third quartile, median, mean and maximum SHALL be present. 

The lookup table for box plots is defined by the table definition in Table 4.21. 

|**Attribute**|**Value**|
|---|---|
|Name|Box plots lookup table|
|Purpose|Presenting the distribution metrics for each box of the box plot.|
|Row Labelling|The box group variable.|
|Column Labelling|The distribution metrics.|
|Cell|The value of the distribution metric for the relevant box group.|



**Table 4.21** Box Plot Lookup Table Definition 

An exemplary box plot lookup table is depicted in Table 4.22. 

|||**Distribution Metric**|**Distribution Metric**|||||
|---|---|---|---|---|---|---|---|
|||Min.|1. Qu.|Median|Mean|3. Qu.|Max|
|Box Descriptor Variable|Box1 name|val|val|val|val|val|val|
||Box2 name|val|val|val|val|val|val|



**Table 4.22** Example Box Plot Lookup Table 

## 4.13.1.14.5 Top and Bottom Tables 

A top or bottom table is a table, ordered by a set of value columns. The following applies: 

- “Value columns” SHALL be columns of the table which shall be considered and which are decisive for the ordering of the rows. 

- A fixed number of rows SHALL be present. If the number of rows to display is not defined by the evaluation, the default number SHALL be 20 rows. 

- In case of a top table, the table SHALL be ordered descending regarding the considered set of value columns and the row with the highest order SHALL be the first row of the table. In case of a bottom table, the table SHALL be ordered ascending by the set of value columns and the row with the lowest order SHALL be the first row of the table. 

- The ordering SHALL be conducted in the order of the value columns defined in the respective evaluation. In case of ties, the next value column of the set SHALL be evaluated. 

- If ties can not be resolved, the rank for same ranked rows SHALL be equal. The rank SHALL continue in the original order for following rows. 

- In case relative frequencies are in the set of value columns, a goodness indicator SHALL be present to esti mate the meaningfulness of the relative frequency i.e. the denominator of the relative frequency SHALL be the goodness estimator. 

- A rank column SHALL be present giving the rank of the record according to the ordering by the value columns. 

Federal Office for Information Security 

80 

4 Function Modules 

- The value columns SHALL be highlighted in the table header and a remark SHALL denote which columns are used for the ordering. 

- The ordering SHALL be unambiguous so that it is clear in which ordering the different rows appear in the table. This MAY be realised by ordering the rows by a name column. If the rows differ only by the name the rank SHALL be equal for all of those rows. 

The top and bottom table is defined by the table definition in Table 4.23. 

|**Attribute**|**Value**|
|---|---|
|Name|Top and bottom table|
|Purpose|Presenting records with lowest and highest rank according to a set of variables.|
|Row Labelling|The records.|
|Column Labelling|The records variables.|
|Cell|The value of the record variable for the given record.|



**Table 4.23** Top and Bottom Table Definition 

An exemplary top table is depicted in Table 4.24. 

|**Rank**|**Goodness Esti**<br>**mator**|**Value Co**<br>**lumn 1**|**Value Co**<br>**lumn 2**|**Value Co**<br>**lumn 3**|**Column 4**|**Column 5**|**Column 6**|
|---|---|---|---|---|---|---|---|
|1|891|val|val|val|val|val|val|
|2|753|val|val|val|val|val|val|



**Table 4.24** Example Top Table 

An exemplary bottom table is depicted in Table 4.25. 

|**Rank**|**Goodness Esti**<br>**mator**|**Value Co**<br>**lumn 1**|**Value Co**<br>**lumn 2**|**Value Co**<br>**lumn 3**|**Column 4**|**Column 5**|**Column 6**|
|---|---|---|---|---|---|---|---|
|82|4|val|val|val|val|val|val|
|81|27|val|val|val|val|val|val|



**Table 4.25** Example Bottom Table 

## 4.13.1.14.6 Component Usage Table 

A component usage table presents the type and usage period of components of interest. Components can be hardware or software components. The following applies: 

- The first and last day of operation in the reporting period SHALL be present. 

- Component descriptors SHALL be present i.e. the triple vendor, name and version of the component. 

- The number of occurrences and number of locations using the component in the reporting period SHALL be present. 

The component usage table is defined by the table definition in Table 4.26. 

|**Attribute**|**Value**|
|---|---|
|Name|Component usage table|
|Purpose|Allowing to investigate the type and number of used components in the reporting period as well<br>as investigating the first and last day of operation of the components in the report period.|
|Row Labelling|The components|



Federal Office for Information Security 

81 

4 Function Modules 

- **Attribute Value** Columns **•** A consecutive numbering column, starting with 1 **•** Vendor, name, version and firmware version of the component **•** First day of operation in the reporting period **•** Last day of operation in the reporting period **•** Number of occurrences **•** Number of distinct locations with at last one occurrence of the component 

- Data Source **•** The component usage table always refers to XML nodes of type `type.component` **•** An available location or host data field shall be used to calculate the number of distinct locati ons or hosts which used the component at least once in the reporting period. 

- **•** An XML node `StartTime` must be used for period filtering and calculation of first and last day of operation 

- Miscellaneous The table shall be ordered by the number of occurrences. 

   - An available location or host data field shall be used to calculate the number of distinct locati ons or hosts which used the component at least once in the reporting period. 

**Table 4.26** Component Usage Table Definition 

An exemplary component usage table is depicted in Table 4.27. 

||**Vendor**|**Name**|**Version**|**Firmware**<br>**Version**|**First Day of**<br>**Operation**|**Last Day of**<br>**Operation**|**Number of Oc**<br>**currences**|**Number of**<br>**Locations**|
|---|---|---|---|---|---|---|---|---|
|**1.**|XYZ|XYZ2|1.2|12 Test|03.01.1999|04.01.1999|744|32|
|**2.**|XYZ|XYZ1|3.2|6.4.2|01.01.1999|06.01.1999|345|12|



**Table 4.27** Example Component Usabe Table 

## 4.13.1.14.7 Threshold Configuration Table 

A threshold configuration table presents the configured threshold of a component. The following applies: 

- The first and last day of operation in the reporting period SHALL be present. 

- Component descriptors SHALL be present i.e. the triple vendor, name and version of the component. 

- The number of occurrences and number of locations using the component in the reporting period SHALL be present. 

The component usage table is defined by the table definition in Table 4.28. 

|**Attribute**|**Value**|
|---|---|
|Name|Threshold Configuration table|
|Purpose|Allowing to investigate the configured thresholds in the report period.|
|Row Labelling|configured thresholds|
|Columns|**•**<br>A consecutive numbering column, starting with 1<br>**•**<br>Vendor, name, version and firmware version of the component<br>**•**<br>The first day the configuration was logged in the reporting period<br>**•**<br>The last day the configuration was logged in the reporting period<br>**•**<br>The optional ID to note the ID of the corresponding measurement.<br>**•**<br>Configured lower bound of the possible range<br>**•**<br>Configured upper bound of the possible range<br>**•**<br>Number of occurrences<br>**•**<br>Number of distinct locations with at last one occurrence of the component|



Federal Office for Information Security 

82 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Data Source|**•**<br>The threshold configuration table refers to XML nodes of type`type.configuration.parame`<br>`ters`,`type.value.with.threshold`,`type.finger.quality.integer`and a XML node of type<br>`type.component`on the same hierarchy level or the first node of type`type.component`on a hig<br>her level.<br>**•**<br>The column “Lower Bound” refers to XML nodes`tmin`<br>**•**<br>The column “Upper Bound” refers to XML nodes`tmax`<br>**•**<br>An available location or host data field SHALL be used to calculate the number of distinct locati<br>ons or hosts which used the component at least once in the reporting period.<br>**•**<br>An XML node`StartTime`must be used for period filtering and calculation of first and last day of<br>operation<br>**•**<br>Note, that depending on the context a component may have several threshold for different me<br>asurements configured e.g. a face image quality component may evaluate a facial image on se<br>veral different indicators or different thresholds are configured for different fingers. In those ca<br>ses, an optional ID column SHALL be used to note the ID of the corresponding measurement, fin<br>ger code etc.<br>**•**<br>Note, if only a threshold is specified and no upper and lower bounds, a single threshold column<br>SHALL replace the lower and upper bound columns.|
|Miscellaneous|The table SHALL be ordered by the number of occurrences.|



**Table 4.28** Threshold Configuration Table Definition 

An exemplary threshold configuration table is depicted in Table 4.29. 

||**Ven**<br>**dor**|**Na**<br>**me**|**Version**|**Firmware**<br>**Version**|**First Day of**<br>**Configurati**<br>**on**|**Last Day of**<br>**Configurati**<br>**on**|**ID**|**Lower**<br>**bound**|**Upper**<br>**bound**|**Number of**<br>**Occurrences**|**Number**<br>**of Locati**<br>**ons**|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**1**|XYZ|XYZ2|1.2|12 Test|03.01.1999|04.01.1999|1.1|0|60|744|32|
|**2**|XYZ|XYZ1|3.2|6.4.2|01.01.1999|06.01.1999|1.2|0.4|1|345|12|



**Table 4.29** Example Threshold Configuration Table 

## 4.13.1.14.8 Lookup Table for Line Plots 

For lookup tables for line plots the following applies: 

- For every line, its absolute and relative frequencies SHALL be present. If there is only one line in the plot there SHALL be no relative frequencies. 

- It is RECOMMENDED to separate absolute and relative frequencies in separate lookup tables. 

- The sum of the X-axis and Y-axis variable SHALL be present in the absolute count lookup table. 

- The total sum of counts SHALL be present in the absolute count lookup table. 

The absolute frequency line plot lookup table is defined by the table definition in Table 4.30. 

|**Attribute**|**Value**|
|---|---|
|Name|Absolute frequency line plot lookup table|
|Purpose|Presenting absolute frequencies and sums of the input data for a given line plot.|
|Row Labelling|**•**<br>The stacked line plot’s Y-axis variable.<br>**•**<br>A row called “Sum” which shows all the sums of the values of each column.|
|Column Labelling|**•**<br>The stacked line plot’s X-axis variable.<br>**•**<br>A column called “Sum” which shows all the sums of the values of each row.|
|Cell|The absolute frequencies of figure of interest for the line plots data points.|
|Miscellaneous|The absolute sum of the line plot’s figure of interest SHALL be present in the lookup ta<br>ble.|



**Table 4.30** Absolute Frequency Line Plot Lookup Table Definition 

Federal Office for Information Security 

83 

4 Function Modules 

An exemplary absolute frequency line plot lookup table is depicted in Table 4.31. 

|||**X-Axis Variable**|||||
|---|---|---|---|---|---|---|
|||**Val1.1**|**Val1.2**|**Val1.3**|**Val1.4**|**Sum**|
|**Y-Axis Variable**|**Val2.1**|Count|Count|Count|Count|Sum Val2.1|
||**Val2.2**|Count|Count|Count|Count|Sum Val2.2|
||**Val2.3**|Count|Count|Count|Count|Sum Val2.3|
||**Val2.4**|Count|Count|Count|Count|Sum Val2.4|
||**Val2.5**|Count|Count|Count|Count|Sum Val2.1|
||**Sum**|Sum Val1.1|Sum Val1.2|Sum Val1.3|Sum Val1.4|Total Sum|



**Table 4.31** Example Absolute Frequency Line Plot Lookup Table 

The lookup table for relative frequency line plot lookup table is defined by the table definition in Table 4.32. 

|**Attribute**|**Value**|
|---|---|
|Name|Relative frequency stacked line plot lookup table|
|Purpose|Presenting relative frequencies of the input data for a given line plot.|
|Row Labelling|The line plot’s X-axis variable.|
|Column Labelling|The line plot’s Y-axis variable.|
|Cell|The relative frequencies of a figure of interest for the line plot’s partitions.|



**Table 4.32** Relative Frequency Line Plot Lookup Table Definition 

An exemplary relative frequency line plot lookup table is depicted in Table 4.33. 

|||**X-Axis Variable**|||
|---|---|---|---|---|
|||**Val1.1**|**Val1.2**|**Val1.3**|
|**Y-Axis Variable**|**Val2.1**|Share 1|Share 2|Share 3|
||**Val2.2**|Share 4|Share 5|Share 6|



**Table 4.33** Example Relative Frequency Line Plot Lookup Table 

## 4.13.2 FM EVA-ALL-PROCESS 

This functional module defines general process evaluations which are not directly related to a biometric mo dality. 

## 4.13.2.1 Requirements 

The evaluations defined by this module SHALL be provided if the application specific EVA-ALL module re quires them. 

## 4.13.2.2 Number of Acquisition Processes 

|**Attribute**|**Value**|
|---|---|
|ID|ALL-PROCESS-1|
|Name|Number of acquisition processes|
|Purpose|This evaluation SHALL deliver insights into the number of acquisition processes.|
|Plots|Line Plot (<br>Table 4.35)|
|Tables|Lookup table for line plot (<br>Table 4.35)|



**Table 4.34** Evaluation Number of Acquisition Processes 

Federal Office for Information Security 

84 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Name|Line plot of number of acquisition processes|
|Purpose|This line plot depicts the number of acquisition processes by type.|
|Type|Line plot|
|X-Axis|Time, calendar weeks if yearly report, days if monthly report.|
|Y-Axis|Number of processes|
|Data Source|**•**<br>The number of XML nodes`FingerAcquisition`for Y-axis if relevant for the application pro<br>file, if finger acquisition is conducted in the domain<br>**•**<br>The number of XML nodes`FaceAcquisition`for Y-axis if relevant for the application profile,<br>if face acquisition is conducted in the domain<br>**•**<br>The number of XML nodes`IrisAcquisition`for Y-axis if relevant for the application profile,<br>if iris acquisition is conducted in the domain<br>**•**<br>The XML node`FingerAcquisition/StartTime`for period filtering and X-axis, if finger ac<br>quisition is not conducted in the domain, face or iris element SHALL be used to extract the<br>start time|
|Example Visualisation|Figure 4.12|



**Table 4.35** Line Plot Number of Acquisition Processes 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0093-03.png)


**Figure 4.12.** Example Line Plot Number of Acquisition Processes 

## 4.13.2.3 Identification Process Duration 

|**Attribute**|**Value**|
|---|---|
|ID|ALL-PROCESS-2|



Federal Office for Information Security 

85 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Name|Identification process duration|
|Purpose|This evaluation SHALL deliver insights into the duration of identification processes. Thereby, e.g. the<br>detection of identifications with long duration is of interest.|
|Facet|**•**<br>Modalities used for identification<br>**•**<br>identification System|
|Plots|Histogram (<br>Table 4.37)|
|Tables|**•**<br>Lookup table for histogram (<br>Table 4.37)<br>**•**<br>Top and bottom table (<br>Table 4.42)|



**Table 4.36** Evaluation Identification Duration 

|**Attribute**|**Value**|
|---|---|
|Name|Histogram identification process duration|
|Purpose|This histogram depicts the distribution of the identification process duration. Thereby, e.g.<br>the detection of outliers is of interest.|
|Type|Histogram with Cumulative Distribution Function|
|X-Axis|Identification duration|
|Y-Axis 1|Frequency of identification processes|
|Y-Axis 2|Axis for empirical cumulative distribution function scaled from 0 to 1.|
|Trimming|The input data of the histograms SHALL be trimmed by the respective 95% percentile.|
|Data Source|**•**<br>distribution of time difference between XML-Nodes<br>`/Identification/SubmitTime`and`Identification/EndTime`in XML-node<br>**•**<br>XML-node`Identification/StartTime`for period filtering<br>**•**<br>XML-attribute`Identification/@system`for facet<br>**•**<br>XML-node`Identification/Modalities`for facet|
|Example Visualisation|Figure 4.13|



**Table 4.37** Histogram Finger Identification Process Duration 

Federal Office for Information Security 

86 

4 Function Modules 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0095-01.png)


**Figure 4.13.** Example Histogram Finger Identification Process Duration 

|**Attribute**|**Value**|
|---|---|
|Name|Top and bottom table locations by identification process duration median|
|Purpose|Presenting locations with lowest and highest rank according to the identification processes du<br>ration median|
|Row|The finger acquisition location.|
|Columns|**•**<br>Median of identification process duration of the location (`EndTime`-`SubmitTime`)<br>**•**<br>Number of identification process at the location as goodness estimator|
|Miscellaneous|**•**<br>value column for ordering is the median of identification duration median<br>**•**<br>ascending order (the lower, the better)|
|Data Source|**•**<br>An XML-node with location or host information for location column. This data may also be<br>located in sources external to this Technical Guideline.<br>**•**<br>XML-nodes`Identification/SubmitTime`and`Identification/EndTime`for the median<br>duration calculation<br>**•**<br>XML-node`Identification/StartTime`for period filtering<br>**•**<br>Attributable`Identification/@system`for facet<br>**•**<br>XML-node`Identification/Modalities`for facet|



**Table 4.38** Top and Bottom Locations by Finger Identification Process Duration 

Federal Office for Information Security 

87 

4 Function Modules 

## 4.13.2.4 Identification Candidate Count 

|**Attribute**|**Value**|
|---|---|
|ID|ALL-PROCESS-3|
|Name|Identification candidate count|
|Purpose|This evaluation shall deliver insights into the number of candidates of an identification processes.|
|Facet|**•**<br>Modalities used for identification<br>**•**<br>Identification System|
|Plots|Histogram (<br>Table 4.40) per finger|
|Tables|**•**<br>Lookup table for histogram (<br>Table 4.40) per finger<br>**•**<br>Top and bottom table (<br>Table 4.41)|



**Table 4.39** Evaluation Identification Candidate Count 

|**Attribute**|**Value**|
|---|---|
|Name|Stacked bar plot relative frequencies of global identification candidate count|
|Purpose|This stacked bar plot shall deliver insights into how many candidates are returned on identi<br>fications.|
|Type|Stacked Bar Plot (horizontal)|
|X-Axis|Relative frequencies of candidate counts.|
|Data Source|**•**<br>distribution XML-Nodes`Identification/CandidateCount`for X-axis.<br>**•**<br>XML-node`Identification/StartTime`for period filtering<br>**•**<br>XML-attribute system of XML-node`Identification`for facet<br>**•**<br>XML-node`Identification/Modalities`for facet|



**Table 4.40** Stacked Bar Plot Global Identification Candidate Count 

|**Attribute**|**Value**|
|---|---|
|Name|Top and bottom table locations by average candidate count.|
|Purpose|Presenting locations with lowest and highest rank according to the average identification candi<br>date count.|
|Row|The identification location.|
|Columns|**•**<br>Average candidate count of successful identification processes at the location (Value)<br>**•**<br>Number of successful identification process at the location as goodness estimator|
|Miscellaneous|ascending order (the lower, the better)|
|Data Source|**•**<br>An XML-node with location or host information for location column. This data may also be<br>located in sources external to this Technical Guideline.<br>**•**<br>XML-nodes`Identification/Result`for filtering only successful identification processes<br>**•**<br>XML-nodes`Identification/CandidateCount`for calculation of average candidate count<br>per location<br>**•**<br>XML-node`Identification/StartTime`for period filtering<br>**•**<br>XML-attribute`Identification/@system`for facet<br>**•**<br>XML-node`Identification/Modalitie`s for facet|



**Table 4.41** Top and Bottom Locations by Average Identification Candidate Count 

Federal Office for Information Security 

88 

4 Function Modules 

## 4.13.2.5 Identification Process Result 

|**Attribute**|**Value**|
|---|---|
|ID|ALL-PROCESS-4|
|Name|Identification process result|
|Purpose|This evaluation SHALL deliver insights into the result of identification processes. Thereby, e.g. the detec<br>tion of identifications with high number of hits is of interest.|
|Facet|**•**<br>Modalities used for identification<br>**•**<br>Identification System|
|Plots|**•**<br>Stacked Bar Plot (<br>Table 4.43)<br>**•**<br>Histogram (<br>Table 4.45)|
|Tables|**•**<br>Lookup table for stacked bar plot (<br>Table 4.43)<br>**•**<br>Lookup table for histogram (<br>Table 4.45)<br>**•**<br>Top and bottom table for Identification Process Result (<br>Table 4.44)<br>**•**<br>Threshold Configuration Table<br>**•**<br>use XML-node`Identification/System`for component information if present. If this informati<br>on is not present or only part of the information is available for the table, omit the corresponding co<br>lumns.<br>**•**<br>use XML-node Verification`Identification/Candidates/Candidate/AchievedFMR`or if not exis<br>ting`RawScore`for threshold information|



**Table 4.42** Evaluation Identification Process Result 

|**Attribute**|**Value**|
|---|---|
|Name|Stacked bar plot global identification result|
|Purpose|This stacked bar plot SHALL deliver insights into how frequently an identification is success<br>fully on a global scope.|
|Type|Stacked Bar Plot (horizontal)|
|X-Axis|Relative frequencies of identification results.|
|Data Source|**•**<br>distribution XML-Nodes`Identification/Result`for X-axis.<br>**•**<br>XML-node`Identification/StartTime`for period filtering<br>**•**<br>XML-attribute`Identification/@system`for facet<br>**•**<br>XML-node`Identification/Modalities`for facet|
|Example Visualisation|Figure 4.14|



**Table 4.43** Stacked Bar Plot Global Identification Process Result 

Federal Office for Information Security 

89 

4 Function Modules 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0098-01.png)


**Figure 4.14.** Example Stacked Bar Plot Global Identification Process Result 

|**Attribute**|**Value**|
|---|---|
|Name|Top and bottom table locations by successful identification result.|
|Purpose|Presenting locations with lowest and highest rank according to the identification processes re<br>sult successful|
|Row|The finger acquisition location.|
|Columns|**•**<br>Relative frequencies of successful identification processes at the location (Value)<br>**•**<br>Number of identification process at the location as goodness estimator|
|Miscellaneous|ascending order (the lower, the better)|
|Data Source|**•**<br>An XML-node with location or host information for location column. This data may also be<br>located in sources external to this Technical Guideline.<br>**•**<br>XML-nodes`Identification/Result`for value column<br>**•**<br>XML-node`Identification/StartTime`for period filtering<br>**•**<br>XML-attribute`Identification/@system`for facet<br>**•**<br>XML-node`Identification/Modalities`for facet|



**Table 4.44** Top and Bottom Locations by Identification Process Result 

|**Attribute**|**Value**|
|---|---|
|Name|Histogram identification candidate’s achieved FMR|
|Purpose|This histogram depicts the distribution of the identification candidate’s achieved FMR. Thereby, e.g.<br>the detection of unusual distribution characteristics is of interest.|
|Type|Histogram with Cumulative Distribution Function|
|X-Axis|Identification candidate’s achieved FMR|
|Y-Axis 1|Frequency of identifications|
|Y-Axis 2|Axis for empirical cumulative distribution function scaled from 0 to 1.|
|Miscellaneous|If the applied threshold is equal over all candidates, the threshold SHALL be added as vertical line to<br>the histogram.|



Federal Office for Information Security 

90 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Data Source|**•**<br>XML-nodes`Identification/Candidates/Candidate/AchievedFMR`<br>**•**<br>XML-attribute`Identification/Candidates/Candidate/AchievedFMR/@threshold`<br>**•**<br>XML-node`Identification/StartTime`for period filtering<br>**•**<br>XML-attribute`Identification/@system`for facet<br>**•**<br>XML-node`Identification/Modalities`for facet|
|Example Visualisati<br>on|Figure 4.15|



**Table 4.45** Histogram Finger Identification Candidate’s Achieved FMR 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0099-03.png)


**Figure 4.15.** Example Histogram Finger Identification Candidate’s Achieved FMR 

## 4.13.2.6 Applications by Time 

|**Attribute**|**Value**|
|---|---|
|ID|ALL-PROCESS-5|
|Name|Applications by time|
|Purpose|This evaluation shall deliver insights into the number of applications. Thereby, e.g. the detection of time<br>periods with low and high number of applications is of interest and the distribution of application num<br>bers over a given time frame.|
|Plots|Histogram (<br>Table 4.47)|
|Tables|Lookup table for histogram (<br>Table 4.47)|



**Table 4.46** Histogram Applications by Time 

|**Attribute**|**Value**|
|---|---|
|Name|Number of applications over time|
|Purpose|This histogram depicts the number of applications over a given time period to recognize<br>e.g. periods of low and high number of applications.|
|Type|Histogram with Cumulative Distribution Function|



Federal Office for Information Security 

91 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|X-Axis|Time, bin size shall be one calendar week for yearly report and one day for monthly report|
|Y-Axis 1|Number of applications|
|Y-Axis 2|Axis for empirical cumulative distribution function scaled from 0 to 1.|
|Data Source|**•**<br>Count of applications with existing TR-03121 logging data in considered time frame<br>**•**<br>`/StartTime`|
|Miscellaneous|The mean shall not be indicated by a vertical line.|
|Example Visualisation|Figure 4.16|



**Table 4.47** Histogram Number of Applications 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0100-03.png)


**Figure 4.16.** Example Histogram Number of Applications 

## 4.13.2.7 Single Verification Process Result 

|**Attribute**|**Value**|
|---|---|
|ID|ALL-PROCESS-6|
|Name|Verification process results|
|Purpose|This evaluation shall deliver insights into the result of verification processes. Thereby, e.g. the global re<br>lative frequency of failed verifications is of interest.|
|Facet|**•**<br>Modalities used for verification<br>**•**<br>Identification System|
|Plots|**•**<br>Stacked Bar Plot (<br>Table 4.49)<br>**•**<br>Histogram (<br>Table 4.50)|



Federal Office for Information Security 

92 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Tables|**•**<br>Lookup table for stacked bar plot (<br>Table 4.49)<br>**•**<br>Lookup table for histogram (<br>Table 4.50)<br>**•**<br>Top and bottom table for (<br>Table 4.48)<br>**•**<br>Threshold Configuration Table<br>**•**<br>use XML-node Verification`Verification/Software`for component information<br>**•**<br>use XML-node`Verification/SingleVerification/Comparison/AchievedFMR`or if not exis<br>ting`RawScore`for threshold information|



**Table 4.48** Evaluation Single Verification Process Result 

|**Attribute**|**Value**|
|---|---|
|Name|Stacked bar plot global verification result|
|Purpose|This stacked bar plot shall deliver insights into how frequently a verification is successfully<br>on a global scope.|
|Type|Stacked Bar Plot (horizontal)|
|X-Axis|Relative frequencies of verification results.|
|Data Source|**•**<br>distribution XML attribute`Verification/@result`for X-axis.<br>**•**<br>XML-node`Verification/StartTime`for period filtering<br>**•**<br>XML-attribute`Verification/@system`for facet<br>**•**<br>XML-node`Verification/Modalities`for facet|
|Example Visualisation|Figure 4.17|



**Table 4.49** Stacked Bar Plot Global Single Verification Process Result 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0101-05.png)


**Figure 4.17.** Example Stacked Bar Plot Global Single Verification Process Result 

|**Attribute**|**Value**|
|---|---|
|Name|Histogram verification achieved FMR|
|Purpose|This histogram depicts the distribution of the verification’s achieved FMR. Thereby, e.g. the de<br>tection of unusual distribution characteristics is of interest.|
|Type|Histogram with Cumulative Distribution Function|
|X-Axis|Verification achieved FMR|



Federal Office for Information Security 

93 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Y-Axis 1|Frequency of verifications|
|Y-Axis 2|Axis for empirical cumulative distribution function scaled from 0 to 1.|
|Data Source|**•**<br>XML-nodes`Verification/SingleVerification/Comparison/AchievedFMR`<br>**•**<br>XML-attribute`Verification/SingleVerification/Comparison/AchievedFMR/@thres`<br>`hold`<br>**•**<br>XML-node`Verification/StartTime`for period filtering<br>**•**<br>XML-attribute`Verification/@system`for facet<br>**•**<br>XML-node`Verification/Modalities`for facet|
|Example Visualisation|Figure 4.18|



**Table 4.50** Histogram Single Verification Achieved FMR 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0102-03.png)


**Figure 4.18.** Example Histogram Single Verification Achieved FMR 

## 4.13.2.8 Single Verification Process Duration 

|**Attribute**|**Value**|
|---|---|
|ID|ALL-PROCESS-7|
|Name|Verification process duration|
|Purpose|This evaluation SHALL deliver insights into the duration of verification processes. Thereby, e.g. the de<br>tection of verification with long duration is of interest.|
|Facet|**•**<br>Modalities used for verification<br>**•**<br>Verification System|



Federal Office for Information Security 

94 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Plots|Histogram (<br>Table 4.52) per verification system and modalities used|
|Tables|**•**<br>Lookup table for histogram (<br>Table 4.52) per verification system and modalities used<br>**•**<br>Top and bottom table (<br>Table 4.53) per verification system and modalities used.|



**Table 4.51** Evaluation Single Verification Process Duration 

|**Attribute**|**Value**|
|---|---|
|Name|Histogram verification process duration|
|Purpose|This histogram depicts the distribution of the verification process duration. Thereby, e.g. the<br>detection of outliers is of interest.|
|Type|Histogram with Cumulative Distribution Function|
|X-Axis|Verification duration|
|Y-Axis 1|Frequency of verification processes|
|Y-Axis 2|Axis for empirical cumulative distribution function scaled from 0 to 1.|
|Trimming|The input data of the histograms SHALL be trimmed by the respective 95% percentile.|
|Data Source|**•**<br>distribution of time difference between XML-Nodes<br>`/Verification/StartTime and Verification/EndTime in XML-node`<br>**•**<br>XML-node`Verification/StartTime`for period filtering<br>**•**<br>XML-attribute`Verification/@system`for facet<br>**•**<br>XML-node`Verification/Modalities`for facet|
|Example Visualisation|Figure 4.19|



**Table 4.52** Histogram Single Verification Process Duration 

Federal Office for Information Security 

95 

4 Function Modules 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0104-01.png)


**Figure 4.19.** Example Histogram Single Verification Process Duration 

|**Attribute**|**Value**|
|---|---|
|Name|Top and bottom table locations by verification process duration median|
|Purpose|Presenting locations with lowest and highest rank according to the verification processes durati<br>on median|
|Row|The finger acquisition location.|
|Columns|**•**<br>Median of verification process duration of the location (`EndTime`-`StartTime`)<br>**•**<br>Number of verification process at the location as goodness estimator|
|Miscellaneous|**•**<br>value column for ordering is the median of verification duration median<br>**•**<br>ascending order (the lower, the better)|
|Data Source|**•**<br>An XML-node with location or host information for location column. This data may also be<br>located in sources external to this Technical Guideline.<br>**•**<br>XML-nodes`Verification/StartTime`and`Verification/EndTime`for the median durati<br>on calculation<br>**•**<br>XML-node`Verification/StartTime`for period filtering<br>**•**<br>XML-attribute`Verification/@system`for facet<br>**•**<br>XML-node`Verification/Modalities`for facet|



**Table 4.53** Top and Bottom Locations by Single Verification Process Duration 

## 4.13.3 FM EVA-ALL-GID 

This functional module defines general evaluations for the German Identity Documents application profiles. 

Federal Office for Information Security 

96 

4 Function Modules 

## 4.13.3.1 Requirements 

The evaluations specified by this module SHALL be provided for the German Identity Documents application profiles. In addition all evaluation defined by Table 4.54 SHALL be provided. The requirements by EVA-ALLGENERIC SHALL apply. 

|**ID**|**Remark**|
|---|---|
|ALL-PROCESS-1|_none_|
|ALL-PROCESS-5|_none_|
|ALL-PROCESS-6|For control verification in self -service scenarios.|
|ALL-PROCESS-7|For control verification in self -service scenarios.|



**Table 4.54** Required Evaluations EVA-ALL-GID 

## 4.13.4 FM EVA-FI-GENERIC 

This functional module defines requirements for the evaluation of facial image acquisitions. 

## 4.13.4.1 Requirements 

The evaluations defined by this module SHALL be provided if the application specific EVA-FI module requires them. 

## 4.13.4.2 Facial Image Capture Components 

|**Attribute**|**Value**|
|---|---|
|ID|FI-GENERIC-1|
|Name|Software version of facial image capture|
|Purpose|This evaluation SHALL give insights in the used software for capturing facial images during the report<br>period.|
|Plots|**•**<br>Heat Map facial image acquisition software usage (Table 2)<br>**•**<br>Heat Map facial image hardware usage (Table 3)|
|Tables|**•**<br>Lookup table for heat maps (<br>Table 4.56 and<br>Table 4.57)<br>**•**<br>Component Usage Tables for<br>**•**<br>software of facial image acquisition`FaceAcquisition/Software`<br>**•**<br>hardware of facial image acquisition`FaceAcquisition/Hardware`|



**Table 4.55** Evaluation Facial Image Capture Component 

|**Attribute**|**Value**|
|---|---|
|Name|Heat map of the number of facial image acquisitions by software version|
|Purpose|This heat map depicts the distributions of the number of facial image acquisitions by software<br>version over a given period to recognize e.g. new software versions and their introduction pha<br>se.|
|Type|Heat Map|
|Row Labelling|The facial image acquisition software version|
|Column Labelling|Time, calender week if yearly report, day if monthly report|
|Cells|The frequency of facial image acquisitions with the given software version|
|Data Source|**•**<br>The number of XML nodes`FaceAcquisition`for the cell counts<br>**•**<br>The XML nodes`FaceAcquisition/Software`for the row dimension<br>**•**<br>XML node`FaceAcquisition/StartTime`for period filtering and the column dimension|
|Colours|Maximum: “column wise” (case 1)|



Federal Office for Information Security 

97 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Example Visualisation|Figure 4.20|



**Table 4.56** Heat Map Facial Image Acquisitions by Software 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0106-03.png)


**Figure 4.20.** Heat Map Facial Image Acquisitions by Software 

|**Attribute**|**Value**|
|---|---|
|Name|Heat map of the number of facial image acquisitions by hardware version|
|Purpose|This heat map depicts the distributions of the number of facial image acquisitions by hardware<br>version over a given period to recognize e.g. detect new hardware versions and their introduc<br>tion phase.|
|Type|Heat Map|
|Row Labelling|The facial image acquisition hardware version|
|Column Labelling|Time, calendar week if yearly report, day if monthly report|
|Cells|The count of facial image acquisitions with the relevant hardware version|
|Data Source|**•**<br>The number of XML nodes`FaceAcquisition`for the cell counts<br>**•**<br>The XML nodes`FaceAcquisition/Hardware`for the row dimension<br>**•**<br>XML node`FaceAcquisition/StartTime`for period filtering and the column dimension|
|Colours|Maximum: “column wise” (case 1)|
|Example Visualisation|Figure 4.21|



**Table 4.57** Heat Map Facial Image Acquisitions by Hardware 

Federal Office for Information Security 

98 

4 Function Modules 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0107-01.png)


**Figure 4.21.** Heat Map Facial Image Acquisitions by Hardware 

## 4.13.4.3 Facial Image Acceptability 

|**Attribute**|**Value**|
|---|---|
|ID|FI-GENERIC-2|
|Name|Facial image acceptability|
|Purpose|This evaluation SHALL give insights in the acceptability of facial images. Thereby it can be measured if<br>the percentage of acceptable images is reasonable.|
|Plots|**•**<br>Stacked Bar Plot (<br>Table 4.59)<br>**•**<br>Stacked Bar Plot (<br>Table 4.60)|
|Tables|**•**<br>Lookup table for stacked bar plot (<br>Table 4.59)<br>**•**<br>Lookup table for stacked bar plot (<br>Table 4.60)<br>**•**<br>Top and bottom table (<br>Table 4.61)<br>**•**<br>Threshold Configuration Table<br>**•**<br>`FaceAcquisition/FaceQuality/Software`for component information<br>**•**<br>`FaceAcquisition/FaceQuality/qa`for threshold information.|



**Table 4.58** Evaluation Facial Image Acceptability 

|**Attribute**|**Value**|
|---|---|
|Name|Stacked bar plot of the total acceptability of facial images in the reporting period|



Federal Office for Information Security 

99 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Purpose|This stacked bar plot SHALL give insights in the total acceptability of the facial images. Thereby, it<br>SHALL e.g. be measured if the total quality of the images is reasonable.|
|Type|Stacked Bar Plot (horizontal)|
|X-Axis|Relative percentage of acceptable and unacceptable facial images.|
|Miscellaneous|**•**<br>An image is acceptable if it fulfils all quality criteria defined by the function module<br>FM QA-<br>FI-GENERIC.<br>**•**<br>If any quality criteria is not fulfilled, the facial image's total acceptability SHALL be nominated<br>as unacceptable.|
|Data Source|**•**<br>XML-attribute`bio:FaceQuality/@total`for the X-axis calculation<br>**•**<br>XML node`FaceAcquisition/StartTime`for period filtering|
|Example Visualisation|Figure 4.22|



**Table 4.59** Stacked Bar Plot Total Facial Image Quality 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0108-03.png)


**Figure 4.22.** Example Stacked Bar Plot Total Facial Image Quality 

|**Attribute**|**Value**|
|---|---|
|Name|Stacked bar plot acceptability of facial images by quality criteria.|
|Purpose|This plot SHALL give insights in the distribution of results for different facial image quality crite<br>ria. This information can give insight in which aspects have to be addressed for future technology<br>improvements.|
|Y-Axis|Relative percentage of facial images which are acceptable and unacceptable for each quality crite<br>ria.|
|X-Axis|The facial image quality criteria (<br>FM QA-FI-GENERIC)|
|Data Sources|**•**<br>XML-attribute`FaceAcquisition/FaceQuality/qa/@result`,`FaceAcquisition/FaceQua`<br>`lity/qa/@tmin`,`FaceAcquisition/FaceQuality/qa/@tmax`for the Y-axis<br>**•**<br>XML-attribute`FaceAcquisition/FaceQuality/qa/@id`<br>for the X-axis<br>**•**<br>XML node`FaceAcquisition/StartTime`for period filtering|
|Example Visualisation|Figure 4.23|



**Table 4.60** Stacked Bar Plot Acceptability of Facial Images by Quality Metrics 

Federal Office for Information Security 

100 

4 Function Modules 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0109-01.png)


**Figure 4.23.** Example Stacked Bar Plot Acceptability of Facial Images by Quality Metrics 

|**Attribute**|**Value**|
|---|---|
|Name|Top and bottom table locations by total acceptability of facial images|
|Purpose|Presenting locations with lowest and highest rank according to total facial image quality|
|Row Labelling|The facial image acquisition location.|
|Columns|**•**<br>Relative frequencies of results of facial image total acceptability<br>**•**<br>Number of facial image acquisitions at the location as goodness estimator|
|Miscellaneous|**•**<br>ascending order (the lower, the better)<br>**•**<br>An image is acceptable if it fulfils all quality criteria defined by<br>FM QA-FI-GENERIC.<br>**•**<br>If any quality criteria is not fulfilled, the image’s total acceptability is unacceptable.|
|Data Source|**•**<br>XML-attributes`FaceAcquisition/FaceQuality/qa/@result`,`FaceAcquisition/FaceQua`<br>`lity/qa/@tmin`,`FaceAcquisition/FaceQuality/qa/@tmax`<br>**•**<br>XML-attribute`FaceAcquisition/FaceQuality/qa/@id`to determine whether criteria is man<br>datory<br>**•**<br>XML node`FaceAcquisition/StartTime`for period filtering<br>**•**<br>An XML-node with location or host information for location column. This data may also be lo<br>cated in sources external to this Technical Guideline.|



**Table 4.61** Top and Bottom Locations by Total Acceptability of Facial Images 

## 4.13.5 FM EVA-FI-CENTRAL 

This functional module defines requirements for the evaluation of facial image acquisitions on central systems different from acquisition clients based on the XML-element “ph-gid-eval”. 

Federal Office for Information Security 

101 

4 Function Modules 

## 4.13.5.1 Requirements 

The evaluations defined by this module SHALL be provided if the application specific EVA-FI module requires them. For each quality algorithm deployed at the central side, the evaluations defined by this module SHALL be made provided. 

## 4.13.5.2 Facial Image Central Acceptability 

|**Attribute**|**Value**|
|---|---|
|ID|FI-CENTRAL-1|
|Name|Facial image acceptability|
|Purpose|This evaluation SHALL give insights in the acceptability of facial images. Thereby it can be measured if<br>the percentage of acceptable images is reasonable.|
|Plots|**•**<br>Stacked Bar Plot (<br>Table 4.63)<br>**•**<br>Stacked Bar Plot (<br>Table 4.64)|
|Tables|**•**<br>Lookup table for stacked bar plot (<br>Table 4.63)<br>**•**<br>Lookup table for stacked bar plot (<br>Table 4.64)<br>**•**<br>Threshold Configuration Table<br>**•**<br>`FaceQualityAssurance/FaceQuality/Software`for component information<br>**•**<br>`FaceQualityAssurance/FaceQuality/qa`for threshold information.|



**Table 4.62** Evaluation Facial Image Central Acceptability 

|**Attribute**|**Value**|
|---|---|
|Name|Stacked bar plot of the total acceptability of facial images in the reporting period|
|Purpose|This stacked bar plot SHALL give insights in the total acceptability of the facial images. Thereby, it<br>SHALL e.g. be measured if the total quality of the images is reasonable.|
|Type|Stacked Bar Plot (horizontal)|
|X-Axis|Relative percentage of acceptable and unacceptable facial images.|
|Miscellaneous|**•**<br>An image is acceptable if it fulfils all mandatory quality criteria defined by the function module<br>FM QA-FI-GENERIC.<br>**•**<br>If any mandatory quality criteria is not fulfilled, the facial image’s total acceptability SHALL be<br>nominated as unacceptable.|
|Data Source|**•**<br>XML-attributes`FaceQualityAssurance/FaceQuality/qa/@result`,`FaceQualityAssuran`<br>`ce/FaceQuality/qa/@tmin`,`FaceQualityAssurance/FaceQuality/qa/@tmax`for the X-axis<br>calculation<br>**•**<br>XML node`StartTime`for period filtering|
|Example Visualisation|Figure 4.24|



**Table 4.63** Stacked Bar Plot Total Central Facial Image Quality 

Federal Office for Information Security 

102 

4 Function Modules 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0111-01.png)


**Figure 4.24.** Example Stacked Bar Plot Total Central Facial Image Quality 

|**Attribute**|**Value**|
|---|---|
|Name|Stacked bar plot acceptability of facial images by quality criteria.|
|Purpose|This plot SHALL give insights in the distribution of results for different facial image quality criteria.<br>This information can give insight in which aspects have to be addressed for future technology im<br>provements.|
|Y-Axis|Relative frequencies of results of quality criteria.|
|X-Axis|The facial image quality criteria (<br>FM QA-FI-GENERIC)|
|Data Sources|**•**<br>XML-attribute`FaceQualityAssurance/FaceQuality/qa/@result`,`FaceQualityAssuran`<br>`ce/FaceQuality/qa/@tmin`,`FaceQualityAssurance/FaceQuality/qa/@tmax`for the Y-axis<br>**•**<br>XML-attribute`FaceAcquisition/FaceQuality/qa/@id`<br>for the X-axis<br>**•**<br>XML node`StartTime`for period filtering|
|Example Visualisation|Figure 4.25|



**Table 4.64** Stacked Bar Plot Central Acceptability of Facial Images by Quality Metrics 

Federal Office for Information Security 

103 

4 Function Modules 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0112-01.png)


**Figure 4.25.** Example Stacked Bar Plot Central Acceptability of Facial Images by Quality Metrics 

## 4.13.6 FM EVA-FI-GID 

This functional module defines facial image evaluations for the German Identity Documents application pro files. 

## 4.13.6.1 Requirements 

The evaluations specified by this module SHALL be provided. In addition all evaluation defined by Table 4.65 SHALL be provided. 

|**ID**|**Remark**|
|---|---|
|FI-CENTRAL-*|_none_|
|FI-GENERIC-*|_none_|



**Table 4.65** Required Evaluations EVA-FI-GID 

## 4.13.7 FM EVA-FP-GENERIC 

This functional module defines requirements for the evaluation of fingerprint acquisitions. 

## 4.13.7.1 Requirements 

The evaluations defined by this module SHALL be provided if the application specific EVA-FP module requires them. The evaluations related to Finger Capture Attempts SHALL be provided if finger capture attempts occur in the relevant application profile. 

Federal Office for Information Security 

104 

4 Function Modules 

## 4.13.7.2 Finger Capture Components 

|**Attribute**|**Value**|**Value**|
|---|---|---|
|ID|FP-GENERIC-1||
|Name|Software and hardware version of finger capture||
|Purpose|This evaluation SHALL give insights in the used software and hardware for capturing fingers during<br>the report period.||
|Plots|**•**<br>Heat Map finger acquisition software usage (<br>Table 4.67)<br>**•**<br>Heat Map finger hardware usage (<br>Table 4.68)||
|Tables|**•**<br>Lookup table for heat maps<br>Table 4.67 and<br>Table 4.68)<br>**•**<br>Component Usage Tables for<br>**•**<br>software of finger acquisition XML node`FingerAcquisition/Software/`<br>**•**<br>hardware of finger acquisition XML node`FingerAcquisition/Hardware/`||
|**Table 4.66**Evaluation Finger Capture Component|||
|**Attribute**||**Value**|
|Name||Heat map of the number of finger acquisitions by software version|
|Purpose||This heat map depicts the distributions of the number of finger acquisitions by software versi<br>on and time to recognize e.g. new software versions and their introduction phase.|
|Type||Heat Map|
|Row Labelling||The finger acquisition software version|
|Column Labelling||Time, calendar week if yearly report, day if monthly report|
|Cells||The frequency of finger acquisitions with the given software version|
|Data Source||**•**<br>The number of XML nodes`FingerAcquisition`for the cell counts<br>**•**<br>The XML nodes`FingerAcquisition/Software`for the row dimension<br>**•**<br>XML node`FingerAcquisition/StartTime/`for period filtering and the column dimensi<br>on|
|Colours||Maximum: “column wise” (case 1)|
|Example Visualisation||Figure 4.26|



**Table 4.67** Heat Map Finger Acquisitions by Software 

Federal Office for Information Security 

105 

4 Function Modules 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0114-01.png)


**Figure 4.26.** Heat Map Finger Acquisitions by Software 

|**Attribute**|**Value**|
|---|---|
|Name|Heat map of the number of finger acquisitions by hardware version|
|Purpose|This heat map depicts the distributions of the number of finger acquisitions by hardware version<br>over a given period to recognize e.g. detect new hardware versions and their introduction phase.|
|Type|Heat Map|
|Row Labelling|The finger acquisition hardware version|
|Column Labelling|Time, calendar week if yearly report, day if monthly report|
|Cells|The count of finger acquisitions with the relevant hardware version|
|Data Source|**•**<br>The number of XML nodes`FingerAcquisition`for the cell counts<br>**•**<br>The XML nodes`FingerAcquisition/Hardware/Version`for the row dimension<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering and the column dimension|
|Colours|Maximum: “column wise” (case 1)|
|Example Visualisation|Figure 4.27|



**Table 4.68** Heat Map Finger Acquisitions by Hardware 

Federal Office for Information Security 

106 

4 Function Modules 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0115-01.png)


**Figure 4.27.** Heat Map Finger Acquisitions by Hardware 

## 4.13.7.3 Number of Finger Captures 

|**Attribute**|**Value**|
|---|---|
|ID|FP-GENERIC-2|
|Name|Number of finger captures|
|Purpose|This evaluation SHALL give insights in the number of captures needed to digitise a finger. Thereby, e.g.<br>the detection of digitization problems is of interest.|
|Plots|Stacked Bar Plot (<br>Table 4.70)|
|Tables|**•**<br>Lookup table for stacked bar plot (<br>Table 4.70)<br>**•**<br>Top and bottom table (<br>Table 4.71)|
|Facet|Finger capture mode|



**Table 4.69** Evaluation Number of Finger Captures 

|**Attribute**|**Value**|
|---|---|
|Name|Stacked bar plot for the number of necessary captures for finger digitalization|
|Purpose|This stacked bar plot depicts the number of finger captures needed to digitise a finger for a given<br>period to recognize e.g. global high number of necessary attempts to capture a finger.|
|Type|Stacked Bar Plot (horizontal)|
|X-Axis|Relative frequencies of the observed counts of finger captures needed to digitise a finger.|
|Miscellaneous|At maximum a count of nine SHALL be depicted. All exceeding counts SHALL be summarised in a<br>single category (only for plot, not for lookup table).|



Federal Office for Information Security 

107 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Data Source|**•**<br>XML-attribute`FingerAcquisition/FingerCapture/@count`for the X-axis<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering<br>**•**<br>XML node`FingerAcquisition/FingerCaptureMod`e for facet|
|Example Visualisation|Figure 4.28|



**Table 4.70** Stacked Bar Plot Number of Finger Captures 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0116-03.png)


**Figure 4.28.** Example Stacked Bar Plot Number of Finger Captures 

|**Attribute**|**Value**|
|---|---|
|Name|Top and bottom table locations with high number of finger captures|
|Purpose|Presenting locations with lowest and highest rank according to the mean of needed finger capture<br>per finger.|
|Row Labelling|The finger acquisition location.|
|Columns|**•**<br>Mean of number of captures per finger capture (Value)<br>**•**<br>Number of FingerAcquisition/FingerCapture as goodness estimator column|
|Miscellaneous|**•**<br>value column for ordering is the mean of number of captures per finger capture<br>**•**<br>ascending order (the lower, the better)|
|Data Source|**•**<br>XML-attribute`FingerAcquisition/FingerCapture/@count`for mean<br>**•**<br>number of`FingerAcquisition`as goodness estimator column<br>**•**<br>An XML-node with location or host information for location column. This data may also be lo<br>cated in sources external to this Technical Guideline.<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering<br>**•**<br>XML node`FingerAcquisition/FingerCaptureMode`for facet|



**Table 4.71** Top and Bottom Locations by Finger Capture Count Mean 

## 4.13.7.4 Number of Finger Captures by Time 

|**Attribute**|**Value**|
|---|---|
|ID|FP-GENERIC-3|
|Name|Number of finger captures by time|



Federal Office for Information Security 

108 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Purpose|This evaluation shall give insights in the number captures needed to digitise a finger over a period. The<br>reby, e.g. the detection of permanent or temporary shifts over time in the number of needed captures<br>shall be detected.|
|Facet|Finger capture mode|
|Plots|Heat Map (<br>Table 4.73)|
|Tables|Absolute and relative lookup tables for heat map (<br>Table 4.73)|



**Table 4.72** Evaluation Number of Finger Captures by Time 

|**Attribute**|**Value**|
|---|---|
|Name|Heat map of the number of finger captures by time|
|Purpose|This heat map depicts the distributions of the number of finger captures needed over a given pe<br>riod to recognize e.g. permanent or temporary shifts in the needed number of finger captures<br>over time.|
|Type|Heat map|
|Row Labelling|The observed counts of finger captures needed to digitise a finger.|
|Column Labelling|Time, calendar week if yearly report, day if monthly report|
|Data Source|**•**<br>XML-attribute`FingerAcquisition/FingerCapture/@count`for the row dimension<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering and the column dimension<br>**•**<br>XML node`FingerAcquisition/FingerCaptureMode`for facet|
|Colours|Maximum: “column wise”(case 1)|
|Miscellaneous|At maximum a count of nine shall be depicted in the row dimension. All exceeding counts shall<br>be summarised in a single category (only for plot, not for lookup table).|
|Example Visualisation|Figure 4.29|



**Table 4.73** Heat Map Number of Finger Captures by Time 

Federal Office for Information Security 

109 

4 Function Modules 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0118-01.png)


**Figure 4.29.** Example Heat Map Number of Finger Captures by Time 

## 4.13.7.5 Number of Finger Captures by Finger 

|**Attribute**|**Value**|
|---|---|
|ID|FP-GENERIC-4|
|Name|Number of finger captures by finger|
|Purpose|This evaluation SHALL give insights in the number of needed finger captures by finger. Thereby, e.g. the<br>detection of fingers with low and high numbers of needed finger captures is of interest.|
|Facet|Finger capture mode|
|Plots|Stacked bar plot (<br>Table 4.75)|
|Tables|Absolute and relative lookup table for stacked bar plot (<br>Table 4.75)|



**Table 4.74** Evaluation Number of Finger Captures by Finger 

|**Attribute**|**Value**|
|---|---|
|Name|Stacked bar plot of the number of finger captures by finger|
|Purpose|This stacked bar plot depicts the number of finger captures by finger to e.g. identify fingers with<br>low or high number of finger captures.|
|Type|Stacked Bar Plot (vertical)|
|X-Axis|Finger code|
|Y-Axis|Relative frequency of the number of captures scaled from 0 to 1.|



Federal Office for Information Security 

110 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Data Source|**•**<br>XML-attribute`FingerAcquisition/FingerCapture/@count`for the Y-axis<br>**•**<br>XML-attribute`FingerAcquisition/FingerCapture/@fc`for the X-axis<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering<br>**•**<br>XML node`FingerAcquisition/FingerCaptureMode`for facet|
|Example Visualisation|Figure 4.30|



**Table 4.75** Stacked Bar Plot Number of Finger Captures by Finger 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0119-03.png)


**Figure 4.30.** Example Stacked Bar Plot Number of Finger Captures by Finger Plot 

## 4.13.7.6 Rejection Reasons of Finger Capture Attempts 

|**Attribute**|**Value**|
|---|---|
|ID|FP-GENERIC-5|
|Name|Rejection reasons of finger capture attempts|
|Purpose|This evaluation shall give insights in the rejection reasons of finger capture attempts needed to digitise a<br>finger. Thereby, e.g. the detection of specific sensor problems is of interest.|
|Plots|Stacked Bar Plot (Table 12)|
|Tables|Lookup table for stacked bar plot (Table 12)|
|Facet|Finger capture mode|



**Table 4.76** Evaluation Rejection Reason of Finger Capture Attempts 

Federal Office for Information Security 

111 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Name|Stacked bar plot for the rejection reasons of finger capture attempts|
|Purpose|This stacked bar plot depicts the rejection reasons of finger capture attempts occurred for a given period<br>to recognize e.g. globally unusual balances of sensor errors.|
|Type|Stacked Bar Plot (horizontal)|
|X-Axis|Relative frequencies of finger capture rejection reasons.|
|Miscellaneous|If the rejection reason is “other”, the error code shall be used as value in addition e.g. “other, Error Code<br>5”.|
|Data Source|**•**<br>XML-attributes`FingerAcquisition/FingerCapture/FingerCaptureAttempt/@ rejectionRe`<br>`ason`and<br>`FingerAcquisition/FingerCapture/FingerCaptureAttempt/@errorCode`for the X-axis<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering<br>**•**<br>XML node`FingerAcquisition/FingerCaptureMode`for facet|
|Example Visuali<br>sation|Figure 4.31|



**Table 4.77** Stacked Bar Rejection Reasons of Finger Capture Attempts 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0120-03.png)


**Figure 4.31.** Example Stacked Bar Rejection Reasons of Finger Capture Attempts 

## 4.13.7.7 Rejection Reasons of Finger Capture Attempts by Finger 

|**Attribute**|**Value**|
|---|---|
|ID|FP-GENERIC-6|
|Name|Rejection Reasons of finger capture attempts by finger|
|Purpose|This evaluation SHALL give insights in the rejection reasons of finger capture attempts by finger needed<br>to digitise a finger. Thereby, e.g. the detection of fingers with specific sensor problems is of interest.|
|Plots|Stacked Bar Plot (<br>Table 4.79)|
|Tables|Lookup table for stacked bar plot (<br>Table 4.79)|
|Facet|Finger capture mode|



**Table 4.78** Evaluation Rejection Reason of Finger Capture Attempts by Finger 

Federal Office for Information Security 

112 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Name|Stacked bar plot for the rejection reasons of finger capture attempts by finger|
|Purpose|This stacked bar plot depicts the rejection reasons of finger capture attempts occurred for a given period<br>to recognize e.g. globally unusual balances of sensor errors.|
|Type|Stacked Bar Plot (vertical)|
|X-Axis|Finger code|
|Y-Axis|Relative frequencies of finger capture rejection reasons. If the rejection reason is “other”, the error code<br>SHALL be used as value in addition e.g. “other, Error Code 5”.|
|Miscellaneous|If the rejection reason is “other”, the error code SHALL be used as value in addition e.g. “other, Error<br>Code 5”.|
|Data Source|**•**<br>XML-attributes`FingerAcquisition/FingerCapture/FingerCaptureAttempt/@rejectionRea`<br>`sonand` `FingerAcquisition/FingerCapture/FingerCaptureAttempt/@errorCode`for the X-axis<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering<br>**•**<br>XML-attribute`FingerAcquisition/FingerCapture@fc`for the X-axis<br>**•**<br>XML node`FingerAcquisition/FingerCaptureMode`for facet|
|Example Visuali<br>sation|Figure 4.32|



**Table 4.79** Stacked Bar Rejection Reasons of Finger Capture Attempts by Finger 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0121-03.png)


**Figure 4.32.** Example Stacked Bar Rejection Reasons of Finger Capture Attempts by Finger 

Federal Office for Information Security 

113 

4 Function Modules 

## 4.13.7.8 Success Rate of Finger Capture Attempts 

|**Attribute**|**Value**|
|---|---|
|ID|FP-GENERIC-7|
|Name|Success rate of finger capture attempts|
|Purpose|This evaluation shall give insights in the global success rate of finger capture attempts needed to digitise<br>a finger. Thereby, the detection of global problems is of interest.|
|Plots|Stacked Bar Plot (<br>Table 4.81)|
|Tables|**•**<br>Lookup table for stacked bar plot (<br>Table 4.81)<br>**•**<br>Top and bottom table (<br>Table 4.82)|
|Facet|Finger capture mode|



**Table 4.80** Evaluation Success Rate of Finger Capture Attempts 

|**Attribute**|**Value**|
|---|---|
|Name|Stacked bar plot for the success rate of finger capture attempts|
|Purpose|This stacked bar plot depicts the global success rate of finger capture attempts occurred for a given peri<br>od to recognize e.g. global high number of failed capture attempts.|
|Type|Stacked Bar Plot (horizontal)|
|X-Axis|Relative frequencies of successful and not successful finger captures.|
|Data Source|**•**<br>XML-attribute`FingerAcquisition/FingerCapture/FingerCaptureAttempt/@ acceptable`<br>`Capture`for the X-axis<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering<br>**•**<br>XML node`FingerAcquisition/FingerCaptureMode`for facet|
|Example Visuali<br>sation|Figure 4.33|



**Table 4.81** Stacked Bar Success Rate of Finger Capture Attempts 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0122-06.png)


**Figure 4.33.** Example Stacked Bar Success Rate of Finger Capture Attempts 

|**Attribute**|**Value**|
|---|---|
|Name|Top and bottom table locations by success rate of finger capture attempts|



Federal Office for Information Security 

114 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Purpose|Presenting locations with lowest and highest rank according to the success rate of finger capture at<br>tempts.|
|Row Labelling|The finger acquisition location.|
|Columns|**•**<br>Success rate of finger capture attempts of the location (Value)<br>**•**<br>Number of finger capture attempts of the location as goodness estimator|
|Miscellaneous|**•**<br>value column for ordering is the success rate of finger capture attempts<br>**•**<br>descending order (the higher, the better)|
|Data Source|**•**<br>An XML-node with location or host information for location column. This data may also be located<br>in sources external to this Technical Guideline.<br>**•**<br>XML-attribute`FingerAcquisition/FingerCapture/FingerCaptureAttempt/@ acceptable`<br>`Capture`for the success rate<br>**•**<br>the number of XML nodes`FingerAcquisition/FingerCapture/FingerCaptureAttempt`for the<br>success rate and goodness estimator column<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering<br>**•**<br>XML node`FingerAcquisition/FingerCaptureMode`for facet|



**Table 4.82** Top and Bottom Locations by Success Rate of Finger Capture Attempts 

## 4.13.7.9 Success Rate of Finger Capture Attempts by Finger 

|**Attribute**|**Value**|
|---|---|
|ID|FP-GENERIC-8|
|Name|Success rate of finger capture attempts by finger|
|Purpose|This evaluation SHALL give insights in the success rate by finger of finger capture attempts needed to<br>digitise the specific finger. Thereby, the detection of specific fingers with digitisation problems is of inte<br>rest.|
|Plots|Stacked Bar Plot (<br>Table 4.84)|
|Tables|Lookup table for stacked bar plot (<br>Table 4.84)|
|Facet|Finger capture mode|



**Table 4.83** Evaluation Success Rate of Finger Capture Attempts by Finger 

|**Attribute**|**Value**|
|---|---|
|Name|Stacked bar plot for the success rate of finger capture attempts by finger|
|Purpose|This stacked bar plot depicts the success rate by finger of finger capture attempts occurred for a given<br>period to recognize e.g. fingers with high number of failed capture attempts.|
|Type|Stacked Bar Plot (vertical)|
|X-Axis|Finger code|
|Y-Axis|Relative frequencies of successful and not successful finger captures.|
|Data Source|**•**<br>XML-attribute`FingerAcquisition/FingerCapture/FingerCaptureAttempt/@acceptableCap`<br>`ture`for the Y-axis<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering<br>**•**<br>XML-attribute`FingerAcquisition/FingerCapture/@fc`for the X-axis<br>**•**<br>XML node`FingerAcquisition/FingerCaptureMode`for facet|
|Example Visuali<br>sation|Figure 4.34|



**Table 4.84** Stacked Bar Success Rate of Finger Capture Attempts by Finger 

Federal Office for Information Security 

115 

4 Function Modules 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0124-01.png)


**Figure 4.34.** Example Stacked Bar Success Rate of Finger Capture Attempts by Finger 

## 4.13.7.10 Number of Finger Captures per Applicant 

|**Attribute**|**Value**|
|---|---|
|ID|FP-GENERIC-9|
|Name|Number of finger capture per Applicant|
|Purpose|This evaluation SHALL give insights in the number finger captures per applicant. Thereby, e.g. the sha<br>re of applicants with very high number of captures is of interest.|
|Plots|Histogram (<br>Table 4.86)|
|Tables|Lookup table for histogram (<br>Table 4.86)|



**Table 4.85** Number of Finger Captures per Applicant 

|**Attribute**|**Value**|
|---|---|
|Name|Histogram number of finger captures per applicant|
|Purpose|This histogram depicts the number of finger captures per applicant for a given time period to re<br>cognize e.g. groups of applicants with high number of finger captures.|
|Type|Histogram with Cumulative Distribution Function|
|X-Axis|Number of captures per applicant|



Federal Office for Information Security 

116 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Y-Axis 1|Number of applicants|
|Y-Axis 2|Axis for empirical cumulative distribution function scaled from 0 to 1.|
|Data Source|**•**<br>distribution of the sum of the XML-attributes`FingerAcquisition/FingerCapture/@count`<br>per applicant<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering|
|Miscellaneous|The mean SHALL NOT be indicated by a vertical line.|
|Example Visualisation|Figure 4.35|



**Table 4.86** Histogram Number of Finger Capture Attempts per Applicant 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0125-03.png)


**Figure 4.35.** Example Histogram Number of Finger Capture Attempts per Applicant 

## 4.13.7.11 NFIQ 2.0 Fingerprint Image Quality 

|**Attribute**|**Value**|
|---|---|
|ID|FP-GENERIC-10|
|Name|NFIQ 2.0 fingerprint image quality|
|Purpose|This evaluation SHALL give insights in the NFIQ 2.0 fingerprint image quality. Thereby, e.g. the detection<br>of fingers with quality below defined thresholds is of interest.|
|Plots|**•**<br>Stacked Bar Plot (<br>Table 4.88)<br>**•**<br>Histogram (<br>Table 4.89) per finger<br>**•**<br>Box plot (<br>Table 4.90)|



Federal Office for Information Security 

117 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Tables|**•**<br>Lookup table for stacked bar plot (<br>Table 4.88)<br>**•**<br>Lookup table for histogram (<br>Table 4.89) per finger<br>**•**<br>Lookup table for box plot (<br>Table 4.90)<br>**•**<br>Top and bottom table (<br>Table 4.91)<br>**•**<br>Threshold Configuration Table<br>**•**<br>`FingerAcquisition/FingerQuality/Software`for component information<br>**•**<br>`FingerAcquisition/FingerQuality/fp`for threshold information.|



**Table 4.87** Evaluation NFIQ 2.0 Fingerprint Image Quality 

|**Attribute**|**Value**|
|---|---|
|Name|Stacked bar plot finger quality errors|
|Purpose|This figure depicts a stacked bar plot of the relative frequencies of finger quality assessments with<br>and without errors. Thereby, e.g. the detection of high numbers of fingers which no quality was<br>measured for is of interest.|
|Type|Stacked bar plot (horizontal)|
|X-Axis|Relative frequencies of the finger quality assessments without error and with error (by error code).|
|Miscellaneous|Note, that the bar segment of fingers with error code SHALL be further segmented by the error<br>code values itself. If the rejection reason is “other”, the error code SHALL be used as value in additi<br>on e.g. “other, Error Code 5”.|
|Data Source|**•**<br>counts of XML nodes`FingerAcquisition/FingerQuality/`with and without`FingerAcqui`<br>`sition/FingerQuality/ErrorCodes`<br>**•**<br>XML-nodes`FingerAcquisition/FingerQuality/ErrorCode`<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering|
|Example Visualisation|Figure 4.36|



**Table 4.88** Stacked Bar Plot Relative Finger Quality Assessment Errors 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0126-05.png)


**Figure 4.36.** Example Stacked Bar Plot Relative Finger Quality Assessment Errors 

|**Attribute**|**Value**|
|---|---|
|Name|Histogram NFIQ 2.0 fingerprint image quality per finger|



Federal Office for Information Security 

118 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Purpose|This histogram depicts the distribution of NFIQ 2.0 fingerprint image quality for a single finger.<br>Thereby, e.g. the share of fingers below the finger’s threshold is of interest.|
|Type|Histogram with Cumulative Distribution Function|
|X-Axis|NFIQ 2.0 score scaled from 0 to 100|
|Y-Axis 1|Number of fingers|
|Y-Axis 2|Axis for empirical cumulative distribution function scaled from 0 to 1.|
|Facet|Finger Code|
|Miscellaneous|**•**<br>The histogram SHALL only depict the quality distribution for a single finger. No histogram wi<br>thout facet grouping.<br>**•**<br>A vertical line SHALL indicate the threshold for the finger. The line SHALL be annotated with<br>the numeric threshold and the relative number of fingers below the threshold.|
|Data Source|**•**<br>distribution of XML attribute`FingerAcquisition/FingerQuality/fp/@result`<br>**•**<br>XML-attribute`FingerAcquisition/FingerQuality/fp/@fc`for finger filtering<br>**•**<br>XML-attribute<br>`FingerAcquisition/FingerQuality/fp/@threshold`for threshold of finger<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering|
|Example Visualisation|Figure 4.37|



**Table 4.89** Histogram NFIQ 2.0 Fingerprint Image Quality 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0127-03.png)


**Figure 4.37.** Example Histogram NFIQ 2.0 Fingerprint Image Quality 

Federal Office for Information Security 

119 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Name|Box plot NFIQ 2.0 fingerprint image quality comparison by finger|
|Purpose|This figure depicts box plots of the distributions of NFIQ 2.0 fingerprint image quality for multiple<br>fingers. Thereby, e.g. the fingers with unusual distribution characteristics SHALL be identified.|
|Type|Box plot|
|X-Axis|Finger code|
|Y-Axis|NFIQ 2.0 score|
|Data Source|**•**<br>distribution of XML-attribute`FingerAcquisition/FingerQuality/fp/@result`for Y-axis<br>**•**<br>XML-attribute`FingerAcquisition/FingerQuality/fp/@fc`for X-axis<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering|
|Example Visualisation|Figure 4.38|



**Table 4.90** Box Plot NFIQ 2.0 Fingerprint Image Quality Finger Comparison 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0128-03.png)


**Figure 4.38.** Example Box Plot NFIQ 2.0 Fingerprint Image Quality Finger Comparison 

|**Attribute**|**Value**|
|---|---|
|Name|Top and bottom table locations by NFIQ 2.0 result|
|Purpose|Presenting locations with lowest and highest rank according to the NFIQ 2.0 results|
|Row Labelling|The finger acquisition location.|
|Columns|**•**<br>A column for the median of the NFIQ 2.0 results for each finger (value columns)<br>**•**<br>Number of total finger captures at the location as goodness estimator|



Federal Office for Information Security 

120 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Miscellaneous|**•**<br>The value column for ordering are the median NFIQ 2.0 columns. The order priority is as follows:<br>right index, left index, right thumb, left thumb, right middle, left middle, right ring, left ring, right<br>little, left little. Note that some fingers may not be available in the application.<br>**•**<br>Rank: descending order (the higher, the better)|
|Data Source|**•**<br>An XML-node with location or host information for location column. This data may also be loca<br>ted in sources external to this Technical Guideline.<br>**•**<br>distribution of XML-attribute`FingerAcquisition/FingerQuality/fp/@result`for median<br>**•**<br>XML-attribute`FingerAcquisition/FingerQuality/fp/@fc`for filtering the median columns<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering|



**Table 4.91** Top and Bottom Locations by NFIQ 2.0 Result 

## 4.13.7.12 Finger Capture Duration 

|**Attribute**|**Value**|
|---|---|
|ID|FP-GENERIC-11|
|Name|Finger capture duration|
|Purpose|This evaluation SHALL give insights in the duration of finger captures. Thereby, e.g. the detection of<br>fingers with long capture duration is of interest.|
|Plots|**•**<br>Histogram (<br>Table 4.93) per finger<br>**•**<br>Box plot (<br>Table 4.94)|
|Tables|**•**<br>Lookup table for histogram (<br>Table 4.93) per finger<br>**•**<br>Lookup table for box plot (<br>Table 4.94)<br>**•**<br>Top and bottom table (<br>Table 4.95)|



**Table 4.92** Evaluation Finger Capture Duration 

|**Attribute**|**Value**|
|---|---|
|Name|Histogram finger capture duration per finger|
|Purpose|This histogram depicts the distribution of the capture duration for a single finger. Thereby, e.g.<br>the detection of outliers is of interest.|
|Type|Histogram with Cumulative Distribution Function|
|X-Axis|Finger capture duration|
|Y-Axis 1|Number of fingers|
|Y-Axis 2|Axis for empirical cumulative distribution function scaled from 0 to 1.|
|Facet|Finger Code|
|Trimming|The input data of the histograms SHALL be trimmed by the respective 95% percentile.|
|Data Source|**•**<br>distribution of XML-attribute`FingerAcquisition/FingerCapture/@duration`<br>**•**<br>XML-attribute`FingerAcquisition/FingerCapture/@fc`for finger filtering<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering|
|Example Visualisation|Figure 4.39|



**Table 4.93** Histogram Finger Capture Duration per Finger 

Federal Office for Information Security 

121 

4 Function Modules 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0130-01.png)


**Figure 4.39.** Example Histogram Finger Capture Duration per Finger 

|**Attribute**|**Value**|
|---|---|
|Name|Box Plot Finger capture duration comparison by finger|
|Purpose|This figure depicts box plots of the distributions of finger capture durations for multiple fingers.<br>Thereby, e.g. fingers with unusual capture duration distribution characteristics SHALL be identi<br>fied.|
|Type|Box plot (vertical)|
|X-Axis|Finger code|
|Y-Axis|Finger capture duration|
|Miscellaneous|The boxes SHALL be ordered by their finger code.|
|Trimming|The input data of the boxes SHALL be trimmed by the respective 95% percentile. The percentile<br>SHALL be calculated for each box separately.|
|Data Source|**•**<br>distribution of XML-attribute`FingerAcquisition/FingerCapture/@duration`for Y-axis<br>**•**<br>XML-attribute`FingerAcquisition/FingerCapture/@fc`for X-axis<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering|
|Example Visualisation|Figure 4.40|



**Table 4.94** Box Plot Finger Capture Duration Comparison 

Federal Office for Information Security 

122 

4 Function Modules 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0131-01.png)


**Figure 4.40.** Example Box Plot Finger Capture Duration Comparison 

|**Attribute**|**Value**|
|---|---|
|Name|Top and bottom table locations by finger acquisition duration|
|Purpose|Presenting locations with lowest and highest rank according to the finger acquisition duration|
|Row Labelling|The finger acquisition location.|
|Columns|**•**<br>Median of finger acquisition duration at the location. The duration can be calculated by sub<br>tracting`StartTime`from`EndTime`.<br>**•**<br>Number of finger acquisitions at the location as goodness estimator|
|Miscellaneous|**•**<br>value column for ordering is the median of finger acquisition duration<br>**•**<br>ascending order (the lower, the better)|
|Data Source|**•**<br>An XML-node with location or host information for location column. This data may also be lo<br>cated in sources external to this Technical Guideline.<br>**•**<br>XML nodes`FingerAcquisition/StartTime`and<br>`FingerAcquisition/EndTime`for the median duration calculation<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering|



**Table 4.95** Top and Bottom Locations by Finger Acquisition Duration 

## 4.13.7.13 Missing Fingers 

|**Attribute**|**Value**|
|---|---|
|ID|FP-GENERIC-12|
|Name|Missing fingers|



Federal Office for Information Security 

123 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Purpose|This evaluation SHALL give insights in distribution of missing fingers.|
|Plots|**•**<br>Stacked bar plot (<br>Table 4.97)<br>**•**<br>Stacked bar plot (<br>Table 4.98)<br>**•**<br>Histograms (<br>Table 4.99, facet)<br>**•**<br>Stacked bar plots (<br>Table 4.100)|
|Tables|**•**<br>Lookup table for stacked bar plot (<br>Table 4.97)<br>**•**<br>Lookup table for stacked bar plot (<br>Table 4.98)<br>**•**<br>Lookup tables for histogram (<br>Table 4.99)<br>**•**<br>Lookup tables for stacked bar plot (<br>Table 4.100)<br>**•**<br>Top and bottom table (<br>Table 4.101)|



**Table 4.96** Evaluation Missing Fingers 

|**Attribute**|**Value**|
|---|---|
|Name|Stacked bar plot relative frequencies of applicants with at least one missing finger|
|Purpose|This figure depicts a stacked bar plot of the relative frequencies of applicants with at least one<br>missing finger. Thereby, e.g. globally unusually frequent numbers of applicants with missing fin<br>gers SHALL be detected.|
|Type|Stacked bar plot (horizontal)|
|X-Axis|Relative frequencies of applicants with at least on missing finger and no missing finger scaled<br>from 0 to 1.|
|Data Source|**•**<br>Number of processes with at least one and without any XML node`FingerAcquisition/Fin`<br>`gerMissing`<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering|
|Example Visualisation|Figure 4.41|



**Table 4.97** Stacked Bar Plot Relative Frequencies of Applicants with a Missing Finger 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0132-05.png)


**Figure 4.41.** Example Stacked Bar Plot Relative Frequencies of Applicants with a Missing Finger 

Federal Office for Information Security 

124 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Name|Stacked bar plot reason for missing fingers|
|Purpose|This figure depicts a stacked bar plot of the relative frequencies of missing fingers by reason for<br>finger missing. Thereby, e.g. the major reason for missing fingers SHALL be identified.|
|Type|Stacked bar plot (horizontal)|
|X-Axis|Relative frequencies of the number of missing fingers by reason for missing scaled from 0 to 1.|
|Data Source|**•**<br>counts of XML nodes`FingerAcquisition/FingerMissing`<br>**•**<br>XML-attribute`FingerAcquisition/FingerMissing/@reason`for bar partitioning<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering|
|Example Visualisation|Figure 4.42|



**Table 4.98** Stacked Bar Plot Relative Frequencies Missing Finger Reason 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0133-03.png)


**Figure 4.42.** Example Stacked Bar Plot Relative Frequencies Missing Finger Reason 

|**Attribute**|**Value**|
|---|---|
|Name|Histogram missing fingers|
|Purpose|This histogram depicts the distribution of missing fingers. Thereby, e.g. the detection of unex<br>pected high numbers of missing fingers is of interest.|
|Type|Histogram with Cumulative Distribution Function|
|X-Axis|Number of missing fingers per applicant|
|Y-Axis 1|Number of applicants|
|Y-Axis 2|Axis for empirical cumulative distribution function scaled from 0 to 1.|
|Facet|Reason for missing finger|
|Data Source|**•**<br>distribution of the number of XML nodes`FingerAcquisition/FingerMissing`per appli<br>cant<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering<br>**•**<br>XML-attribute`FingerAcquisition/FingerMissing/@reaso`n for facet|
|Example Visualisation|Figure 4.43|



**Table 4.99** Histogram Number of Missing Fingers 

Federal Office for Information Security 

125 

4 Function Modules 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0134-01.png)


**Figure 4.43.** Example Histogram Number of Missing Fingers 

|**Attribute**|**Value**|
|---|---|
|Name|Stacked bar plot missing finger relative frequencies by finger|
|Purpose|This figure depicts a stacked bar plot of the relative frequencies of missing fingers by finger. Ther<br>eby, e.g. fingers which are frequently missing SHALL be identified.|
|Type|Stacked bar plot (horizontal)|
|X-Axis|Finger Code|
|Y-Axis|Relative frequencies of the finger acquisitions with finger missing scaled from 0 to 1.|
|Facet|reason for missing finger|
|Data Source|**•**<br>counts of XML nodes`FingerAcquisition/FingerMissing`relative to counts of XML nodes<br>`FingerAcquisition`<br>**•**<br>XML-attribute`FingerAcquisition/FingerMissing/@fc`for bar partitioning<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering<br>**•**<br>XML-attribute`FingerAcquisition/FingerMissing/@reason`for facet|
|Example Visualisation|Figure 4.44|



**Table 4.100** Stacked Bar Plot Relative Frequencies Missing Fingers 

Federal Office for Information Security 

126 

4 Function Modules 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0135-01.png)


**Figure 4.44.** Example Stacked Bar Plot Relative Frequencies Missing Fingers 

|**Attribute**|**Value**|
|---|---|
|Name|Top and bottom table locations by relative frequencies of at least on missing finger per process|
|Purpose|Presenting locations with lowest and highest rank according to the relative frequencies of process<br>with at least one missing finger.|
|Row Labelling|The finger acquisition location.|
|Columns|**•**<br>Relative frequencies of finger acquisition processes with at least on missing finger (Value)<br>**•**<br>Number of finger acquisitions at the location as goodness estimator|
|Miscellaneous|ascending order (the lower, the better)|
|Data Source|**•**<br>Number of processes with and without existing XML nodes`FingerAcquisition/FingerMis`<br>`sing`. If no XML node exists this process SHALL count for processes without missing fingers<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering<br>**•**<br>An XML-node with location or host information for location column. This data may also be lo<br>cated in sources external to this Technical Guideline.|



**Table 4.101** Top and Bottom Locations by Relative Frequencies of at least one Missing Finger per Process 

## 4.13.7.14 Sequence Errors 

|**Attribute**|**Value**|
|---|---|
|ID|FP-GENERIC-13|
|Name|Sequence Errors|
|Purpose|This evaluation SHALL give insights in the distribution of sequence errors.|
|Plots|**•**<br>Histograms (<br>Table 4.104)<br>**•**<br>Stacked Bar Plot (<br>Table 4.103)|
|Tables|**•**<br>Lookup table for histograms (<br>Table 4.104)<br>**•**<br>Lookup table for stacked bar plot (<br>Table 4.103)|



**Table 4.102** Evaluation Sequence Errors 

|**Attribute**|**Value**|
|---|---|
|Name|Stacked bar plot for proportion of finger acquisition with sequence errors|



Federal Office for Information Security 

127 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Purpose|This stacked bar plot depicts the relative frequencies of finger acquisitions with and without se<br>quence errors to recognize e.g. globally unusual high number of acquisitions with sequence er<br>rors.|
|Type|Stacked Bar Plot (horizontal)|
|X-Axis|Relative frequencies of finger acquisitions with and without sequence errors.|
|Data Source|**•**<br>Number of processes with and without existing XML node`FingerAcquisition/Sequen`<br>`ceError`<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering|
|Example Visualisation|Figure 4.45|



**Table 4.103** Stacked Bar Finger Acquisitions With Sequence Errors 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0136-03.png)


**Figure 4.45.** Example Stacked Bar Finger Acquisitions With Sequence Errors 

|**Attribute**|**Value**|
|---|---|
|Name|Histogram number of sequence errors|
|Purpose|This histogram depicts the distribution of the number of sequence errors. Thereby, e.g. the de<br>tection of unexpected high numbers of sequence errors SHALL be possible.|
|Type|Histogram with Cumulative Distribution Function|
|X-Axis|Number of sequence errors|
|Y-Axis 1|Number of finger acquisitions with sequence errors|
|Y-Axis 2|Axis for empirical cumulative distribution function scaled from 0 to 1.|
|Data Source|**•**<br>XML node`FingerAcquisition/StartTime`for period filtering<br>**•**<br>distribution of XML nodes`FingerAcquisition/SequenceError`|
|Example Visualisation|Figure 4.46|



**Table 4.104** Histogram Number of Sequence Errors 

Federal Office for Information Security 

128 

4 Function Modules 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0137-01.png)


**Figure 4.46.** Example Histogram Number of Sequence Errors 

## 4.13.7.15 Segmentation Errors 

|**Attribute**|**Value**|
|---|---|
|ID|FP-GENERIC-14|
|Name|Segmentation Errors|
|Purpose|This evaluation SHALL give insights in the distribution of segmentation errors.|
|Plots|Stacked Bar Plot (<br>Table 4.106)|
|Tables|Lookup table for stacked bar plot (<br>Table 4.106)|



**Table 4.105** Evaluation Segmentation Errors 

|**Attribute**|**Value**|
|---|---|
|Name|Stacked bar plot for proportion of finger acquisition with segmentation errors|
|Purpose|This stacked bar plot depicts the relative frequencies of finger acquisitions with and without seg<br>mentation errors to recognize e.g. globally unusual high number of acquisitions with segmentati<br>on errors.|
|Type|Stacked Bar Plot (horizontal)|
|X-Axis|Relative frequencies of finger acquisitions with and without segmentation errors.|
|Data Source|**•**<br>Number processes with and without existing XML node`FingerAcquisition/Segmentatio`<br>`nError`<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering|



Federal Office for Information Security 

129 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Example Visualisation|Figure 4.47|



**Table 4.106** Stacked Bar Finger Acquisitions With Segmentation Errors 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0138-03.png)


**Figure 4.47.** Example Stacked Bar Finger Acquisitions With Segmentation Errors 

## 4.13.7.16 Uniqueness Checks 

|**Attribute**|**Value**|
|---|---|
|ID|FP-GENERIC-15|
|Name|Uniqueness Checks|
|Purpose|This evaluation SHALL give insights in the distribution of uniqueness checks.|
|Plots|**•**<br>Stacked Bar Plot (<br>Table 4.108)<br>**•**<br>Stacked Bar Plot (<br>Table 4.109)|
|Tables|**•**<br>Lookup table for stacked bar plots (<br>Table 4.109,<br>Table 4.108)<br>**•**<br>Top and bottom table (<br>Table 4.110)|



**Table 4.107** Evaluation Uniqueness Checks 

|**Attribute**|**Value**|
|---|---|
|Name|Stacked bar plot for proportion of finger acquisition with uniqueness check errors|
|Purpose|This stacked bar plot depicts the relative frequencies of finger acquisitions with and without uni<br>queness errors to recognize e.g. globally unusual high number of acquisitions with uniqueness er<br>rors.|
|Type|Stacked Bar Plot (horizontal)|
|X-Axis|Relative frequencies of finger acquisitions with and without uniqueness errors.|
|Data Source|**•**<br>Number of processes with and without existing XML node`FingerAcquisition/Uniquen`<br>`essCheck`. If no XML node exists or if it exists and its XML-attribute result is false, this process<br>SHALL count for processes without uniqueness check errors.<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering|
|Example Visualisation|Figure 4.48|



**Table 4.108** Stacked Bar Uniqueness Check Errors per Finger Acquisition 

Federal Office for Information Security 

130 

4 Function Modules 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0139-01.png)


**Figure 4.48.** Example Stacked Bar Uniqueness Check Errors per Finger Acquisition 

|**Attribute**|**Value**|
|---|---|
|Name|Stacked bar plot of relative frequencies of finger duplicates|
|Purpose|This stacked bar plot depicts the relative frequencies of finger duplicates for each finger code to re<br>cognize e.g. duplicates with unusual high number of occurrences.|
|Type|Stacked Bar Plot (horizontal)|
|X-Axis|Relative frequencies of duplicates|
|Y-Axis|Finger Code|
|Data Source|**•**<br>Distribution of XML node<br>`FingerAcquisition/UniquenessCheck/Duplicates/Duplicate`<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering|
|Example Visualisation|Figure 4.49|



**Table 4.109** Stacked Bar Finger Duplicates 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0139-05.png)


**Figure 4.49.** Example Stacked Bar Finger Duplicates 

Federal Office for Information Security 

131 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Name|Top and bottom table locations by number of uniqueness check errors|
|Purpose|Presenting locations with lowest and highest rank according to the number of uniqueness|
|Row Labelling|The finger acquisition location.|
|Columns|**•**<br>Relative frequencies of finger acquisition processes with uniqueness check errors of the location<br>(Value)<br>**•**<br>Number of finger acquisitions at the location as goodness estimator|
|Miscellaneous|**•**<br>value column for ordering is the relative frequencies of finger acquisitions with uniqueness<br>check error<br>**•**<br>ascending order (the lower, the better)|
|Data Source|**•**<br>Number of processes with and without existing XML node`FingerAcquisition/Uni`<br>`qunessCheck`. If no XML node exists or if it exists and its XML-attribute result is false, this pro<br>cess SHALL count for processes without uniqueness check errors.<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering|



**Table 4.110** Top and Bottom Locations by Number of Uniqueness Check Errors 

## 4.13.8 FM EVA-FP-CENTRAL 

This functional module defines requirements for the evaluation of fingerprint images in central systems dif ferent from acquisition clients based on the XML-element “fp-gid-eval”. 

## 4.13.8.1 Requirements 

The evaluations defined by this module SHALL be provided if the application specific EVA-FP module requires them. For each quality algorithm deployed at the central side, the evaluations defined by this module SHALL be made provided. 

## 4.13.8.2 NFIQ 2.0 Fingerprint Image Quality 

|**Attribute**|**Value**|
|---|---|
|ID|FP-CENTRAL-1|
|Name|NFIQ 2.0 fingerprint image quality|
|Purpose|This evaluation SHALL give insights in the NFIQ 2.0 fingerprint image quality. Thereby, e.g. the detection<br>of fingers with quality below defined thresholds is of interest.|
|Plots|**•**<br>Stacked bar plot (<br>Table 4.112)<br>**•**<br>Histogram (<br>Table 4.113) per finger<br>**•**<br>Box plot (<br>Table 4.114)|
|Tables|**•**<br>Lookup table for histogram (<br>Table 4.113) per finger<br>**•**<br>Lookup table for box plot (<br>Table 4.114)<br>**•**<br>Threshold Configuration Table<br>**•**<br>`FingerQualityAssurance/FingerQuality/Software`for component information<br>**•**<br>`FingerQualityAssurance/FingerQuality/fp`for threshold information.|



**Table 4.111** Evaluation NFIQ 2.0 Fingerprint Image Quality 

|**Attribute**|**Value**|
|---|---|
|Name|Stacked bar plot finger quality errors|
|Purpose|This figure depicts a stacked bar plot of the relative frequencies of finger quality assessments with<br>and without errors. Thereby, e.g. the detection of high numbers of fingers which no quality was me<br>asured for is of interest.|



Federal Office for Information Security 

132 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Type|Stacked bar plot (horizontal)|
|X-Axis|Relative frequencies of the finger quality assessments without error and with error (by error code).|
|Miscellaneous|Note, that the bar segment of fingers with error code SHALL be further segmented by the error code<br>values itself. If the rejection reason is “other”, the error code SHALL be used as value in addition e.g.<br>“other, Error Code 5”.|
|Data Source|**•**<br>counts of XML nodes`FingerQualityAssurance/FingerQuality/`with and without`Finger`<br>`QualityAssurance/FingerQuality/ErrorCodes`<br>**•**<br>XML-nodes`FingerQualityAssurance/FingerQuality/ErrorCode`<br>**•**<br>XML node`StartTime`for period filtering|
|Example Visualisation|Figure 4.50.|



**Table 4.112** Stacked Bar Plot Relative Finger Quality Assessment Errors 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0141-03.png)


**Figure 4.50.** Example Stacked bar plot finger quality errors 

|**Attribute**|**Value**|
|---|---|
|Name|Histogram NFIQ 2.0 fingerprint image quality per finger|
|Purpose|This histogram depicts the distribution of NFIQ 2.0 fingerprint image quality for a single finger. The<br>reby, e.g. the share of fingers below the finger’s threshold is of interest.|
|Type|Histogram with Cumulative Distribution Function|
|X-Axis|NFIQ 2.0 score scaled from 0 to 100|
|Y-Axis 1|Number of fingers|
|Y-Axis 2|Axis for empirical cumulative distribution function scaled from 0 to 1.|
|Facet|Finger Code|
|Miscellaneous|**•**<br>The histogram SHALL only depict the quality distribution for a single finger. No histogram wi<br>thout facet grouping.<br>**•**<br>A vertical line SHALL indicate the threshold for the finger. The line SHALL be annotated with the<br>numeric threshold and the relative number of fingers below the threshold.|



Federal Office for Information Security 

133 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Data Source|**•**<br>distribution of XML attribute`FingerQualityAssurance/FingerQuality/fp/@result`<br>**•**<br>XML-attribute`FingerQualityAssurance/FingerQuality/fp/@fc`for finger filtering<br>**•**<br>XML-attribute`FingerQualityAssurance/FingerQuality/fp/@threshold`for threshold of<br>finger<br>**•**<br>XML node`StartTime`for period filtering|
|Example Visualisation|Figure 4.51|



**Table 4.113** Histogram NFIQ 2.0 Fingerprint Image Quality 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0142-03.png)


**Figure 4.51.** Example Histogram NFIQ 2.0 Fingerprint Image Quality 

|**Attribute**|**Value**|
|---|---|
|Name|Box plot NFIQ 2.0 fingerprint image quality comparison by finger|
|Purpose|This figure depicts box plots of the distributions of NFIQ 2.0 fingerprint image quality for multiple<br>fingers. Thereby, e.g. the fingers with unusual distribution characteristics SHALL be identified.|
|Type|Box plot|
|X-Axis|Finger code|
|Y-Axis|NFIQ 2.0 score|
|Data Source|**•**<br>distribution of XML-attribute`FingerQualityAssurance/FingerQuality/fp/@result`for Y-<br>axis<br>**•**<br>XML-attribute`FingerQualityAssurance/FingerQuality/fp/@fc`for X-axis<br>**•**<br>XML node`StartTime`for period filtering|



Federal Office for Information Security 

134 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Example Visualisation|Figure 4.52|



**Table 4.114** Box Plot NFIQ 2.0 Fingerprint Image Quality Finger Comparison 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0143-03.png)


**Figure 4.52.** Example Box plot NFIQ 2.0 fingerprint image quality comparison by finger 

## 4.13.9 FM EVA-FP-GID 

This functional module defines fingerprint evaluations for the German Identity Documents application pro files. 

## 4.13.9.1 Requirements 

The evaluations specified by this module SHALL be provided. In addition all evaluation defined by Ta ble 4.115 SHALL be provided. 

|**ID**|**Remark**|
|---|---|
|FP-PAD-*|_none_|
|FP-CENTRAL-*|_none_|
|FP-GENERIC-*|_none_|



**Table 4.115** Required Evaluations EVA-FP-GID 

## 4.13.9.2 Fingerprint Capture Allowed 

|**Attribute**|**Value**|
|---|---|
|ID|FP-GID-1|



Federal Office for Information Security 

135 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Name|Fingerprint Capture Allowed|
|Purpose|This evaluation SHALL give insights in the distribution of applications regarding allowed fingerprint<br>captures.|
|Plots|Stacked bar plot (<br>Table 4.117)|
|Tables|**•**<br>Absolute and relative lookup table for stacked bar plot (<br>Table 4.117)<br>**•**<br>Top and bottom table (<br>Table 4.118)|



**Table 4.116** Evaluation Fingerprint Capture Allowed 

|**Attribute**|**Value**|
|---|---|
|Name|Stacked bar plot share of applications where fingerprint capture is allowed|
|Purpose|This stacked bar plot depicts the share of applications where fingerprint capture is allowed<br>and not allowed.|
|Type|Stacked Bar Plot (horizontal)|
|X-Axis|Relative frequency of values from fingerprint capture allowed logging field.|
|Data Source|**•**<br>XML-nodes`FingerprintCaptureAllowed`for X-axis shares<br>**•**<br>XML-node`StartTime`for period filtering|
|Example Visualisation|Figure 4.53|



**Table 4.117** Stacked Bar Plot Fingerprint Capture Allowed 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0144-05.png)


**Figure 4.53.** Example Stacked Bar Plot Fingerprint Capture Allowed 

|**Attribute**|**Value**|
|---|---|
|Name|Top and bottom table locations by fingerprint capture allowed|
|Purpose|Presenting locations with lowest and highest rank according to the share of allowed fingerprint<br>captures|
|Row|The finger acquisition location.|
|Columns|**•**<br>Share of applications with TRUE`FingerprintCaptureAllowed`field<br>**•**<br>Number of log files at the location as goodness estimator|



Federal Office for Information Security 

136 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Miscellaneous|**•**<br>value column for ordering is the share of applications with TRUE`FingerprintCaptureAl`<br>`lowed`<br>**•**<br>descending order (the higher, the better)|
|Data Source|**•**<br>An XML-node with location or host information for location column. This data may also be<br>located in sources external to this Technical Guideline.<br>**•**<br>XML-node`FingerprintCaptureAllowed`<br>**•**<br>XML-node`StartTime`for period filtering|



**Table 4.118** Top and Bottom Locations by Fingerprint Capture Allowed 

## 4.13.9.3 Fingerprint Exclude Option 

|**Attribute**|**Value**|
|---|---|
|ID|FP-GID-2|
|Name|Fingerprint Exclude Option|
|Purpose|This evaluation SHALL give insights in the distribution of applications regarding the fingerprint ex<br>clude option.|
|Plots|Stacked bar plot (<br>Table 4.120)|
|Tables|**•**<br>Absolute and relative lookup table for stacked bar plot (<br>Table 4.120)<br>**•**<br>Top and bottom table (<br>Table 4.121)|



**Table 4.119** Evaluation Fingerprint Exclude Option 

|**Attribute**|**Value**|
|---|---|
|Name|Stacked bar plot share of applications where fingerprint exclude option is TRUE|
|Purpose|This stacked bar plot depicts the share of applications where fingerprint exclude option is<br>TRUE and not allowed.|
|Type|Stacked Bar Plot (horizontal)|
|X-Axis|Relative frequency of values of fingerprint exclude option.|
|Data Source|**•**<br>XML-nodes`FingerprintExcludeOption`for X-axis shares<br>**•**<br>XML-node`StartTime`for period filtering|
|Example Visualisation|Figure 4.54|



**Table 4.120** Stacked Bar Plot Fingerprint Exclude Option 

Federal Office for Information Security 

137 

4 Function Modules 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0146-01.png)


**Figure 4.54.** Example Stacked Bar Plot Fingerprint Exclude Option 

|**Attribute**|**Value**|
|---|---|
|Name|Top and Bottom Locations by Fingerprint Exclude Option|
|Purpose|Presenting locations with lowest and highest rank according to the share of TRUE fingerprint<br>exclude option|
|Row|The finger acquisition location.|
|Columns|**•**<br>Share of applications with TRUE`FingerprintExcludeOption`field<br>**•**<br>Number of log files the location as goodness estimator|
|Miscellaneous|**•**<br>value column for ordering is the share of applications with TRUE`FingerprintExclude`<br>`Option`<br>**•**<br>ascending order (the lower, the better)|
|Data Source|**•**<br>An XML-node with location or host information for location column. This data may also be<br>located in sources external to this Technical Guideline.<br>**•**<br>XML-node`FingerprintExcludeOption`<br>**•**<br>XML-node`StartTime`for period filtering|



**Table 4.121** Top and Bottom Locations by Fingerprint Exclude Option 

## 4.13.9.4 Fingerprint Exclude Option vs. Fingerprint Capture Allowed 

|**Attribute**|**Value**|
|---|---|
|ID|FP-GID-3|
|Name|Fingerprint Exclude Option vs. Fingerprint Capture Allowed|
|Purpose|This evaluation SHALL give insights in the combination of Fingerprint Capture Allowed vs. Fingerprint<br>Exclude Option e.g. to detect misconfiguration (allowed FALSE, excluded TRUE)|
|Tables|**•**<br>Absolute and relative contingency table (<br>Table 4.123 and<br>Table 4.124)<br>**•**<br>Top and bottom table (<br>Table 4.125)|



**Table 4.122** Evaluation Fingerprint Exclude Option vs. Fingerprint Capture Allowed 

|**Attribute**|**Value**|
|---|---|
|Name|Absolute Contingency Table Fingerprint Exclude Option vs. Fingerprint Capture Allowed|
|Purpose|This table provides insights in the absolute frequencies of applications with different value combi<br>nations of Fingerprint Exclude Option and Fingerprint Capture Allowed.|



Federal Office for Information Security 

138 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Row Labelling|Value of Fingerprint Exclude Option|
|Column Labelling|Value of Fingerprint Capture Allowed|
|Cell|The cell SHALL be the absolute frequency of applications with the specific Fingerprint Exclude Op<br>tion and Fingerprint Capture Allowed combination.|
|Data Source|**•**<br>XML-node`FingerprintExcludeOption`<br>**•**<br>XML-node`FingerprintCaptureAllowed`<br>**•**<br>XML-node`StartTime`for period filtering|



**Table 4.123** Absolute Contingency Table Fingerprint Exclude Option vs. Fingerprint Capture Allowed 

|**Attribute**|**Value**|
|---|---|
|Name|Relative Contingency Table Fingerprint Exclude Option vs. Fingerprint Capture Allowed|
|Purpose|This table provides insights in the relative frequencies of applications with different value combi<br>nations of Fingerprint Exclude Option and Fingerprint Capture Allowed.|
|Row Labelling|Value of Fingerprint Exclude Option|
|Column Labelling|Value of Fingerprint Capture Allowed|
|Cell|The cell SHALL be the relative frequency of applications with the specific Fingerprint Exclude Op<br>tion and Fingerprint Capture Allowed combination.|
|Data Source|**•**<br>XML-node`FingerprintExcludeOption`<br>**•**<br>XML-node`FingerprintCaptureAllowed`<br>**•**<br>XML-node`StartTime`for period filtering|



**Table 4.124** Relative Contingency Table Fingerprint Exclude Option vs. Fingerprint Capture Allowed 

|**Attribute**|**Value**|
|---|---|
|Name|Top and bottom table locations by allowed but excluded fingerprints|
|Purpose|Presenting locations with lowest and highest rank according to the share of allowed but exclu<br>ded fingerprints flags.|
|Row|The finger acquisition location.|
|Columns|**•**<br>Share of applications with TRUE`FingerprintExcludeOption`field and TRUE`Finger`<br>`printCaptureAllowed`field<br>**•**<br>Number of applications process at the location as goodness estimator|
|Miscellaneous|**•**<br>value column for ordering is the share of applications with TRUE`FingerprintExclude`<br>`Option`field and TRUE`FingerprintCaptureAllowed`field<br>**•**<br>ascending order (the lower, the better)|
|Data Source|**•**<br>An XML-node with location or host information for location column. This data may also be<br>located in sources external to this Technical Guideline.<br>**•**<br>XML-node`FingerprintExcludeOption`<br>**•**<br>XML-node`FingerprintCaptureAllowed`<br>**•**<br>XML-node`StartTime`for period filtering|



**Table 4.125** Top and Bottom Locations by Allowed but Excluded Fingerprints 

## 4.13.10 FM EVA-FP-PAD 

This functional module defines requirements for the evaluation of presentation attack detection at fingerprint acquisitions. 

Federal Office for Information Security 

139 

4 Function Modules 

## 4.13.10.1 Requirements 

The evaluations defined by this module shall be provided if the application specific EVA-FP module requires them. 

## 4.13.10.2 Finger Presentation Attack Detection 

|**Attribute**|**Value**|
|---|---|
|ID|FP-PAD-1|
|Name|Presentation attack detection|
|Purpose|This evaluation shall give insights in the distribution of presentation attack detection results.|
|Plots|**•**<br>Histograms (<br>Table 4.130)<br>**•**<br>Stacked bar plot (<br>Table 4.127)|
|Tables|**•**<br>Lookup table for histograms (<br>Table 4.127)<br>**•**<br>Top and bottom tables (<br>Table 4.128,<br>Table 4.129)|



**Table 4.126** Evaluation Finger Presentation Attack Detection 

|**Attribute**|**Value**|
|---|---|
|Name|Stacked bar plot activation of presentation attack detection|
|Purpose|This stacked bar plot depicts the relative frequencies of finger acquisition processes with and wi<br>thout activated presentation attack detection e.g. to detect misconfigured hosts.|
|Type|Stacked Bar Plot (horizontal)|
|X-Axis|Relative frequencies of finger acquisition processes with and without presentation detection<br>enabled.|
|Data Source|**•**<br>Number of processes with and without existing`FingerAcquisition/PADInformation`<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering|
|Example Visualisation|Figure 4.55|



**Table 4.127** Stacked Bar Finger Acquisitions with Presentation Attack Detection 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0148-08.png)


**Figure 4.55.** Example Stacked Bar Finger Acquisitions with Presentation Attack Detection 

|**Attribute**|**Value**|
|---|---|
|Name|Top and bottom table locations with low and high presentation attack detection activation quote.|



Federal Office for Information Security 

140 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Purpose|Presenting locations with high and low activation of presentation attack detection functionality.|
|Row Labelling|The finger acquisition location.|
|Columns|**•**<br>Relative frequency of finger acquisition processes with a`FingerAcquisition/PADInformati`<br>`on`<br>**•**<br>Number of finger acquisitions as goodness estimator|
|Miscellaneous|**•**<br>value column for ordering is relative frequency of finger acquisition processes with a`Finger`<br>`Acquisition/PADInformation`<br>**•**<br>ascending order (the lower, the better)|
|Data Source|**•**<br>count of XML-node`FingerAcquistion/PADInformation/ProbePADInfo/`<br>**•**<br>count of XML-node`FingerAcquistion`<br>**•**<br>An XML-node with location or host information. This data may also be located in sources exter<br>nal to this Technical Guideline.<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering|



**Table 4.128** Top and Bottom Locations by Activation of Presentation Attack Detection 

|**Attribute**|**Value**|
|---|---|
|Name|Top and bottom table locations with low and high detected presentation attacks.|
|Purpose|Presenting locations with high and low relative numbers of detections of presentation attacks.|
|Row Labelling|The finger acquisition location.|
|Columns|**•**<br>Share of presentation attack detection probes with “detected” presentation attack detection.<br>**•**<br>Number of presentation attack detection probes as goodness estimator|
|Miscellaneous|**•**<br>value column for ordering is the share of “detected” results<br>**•**<br>ascending order (the lower, the better)|
|Data Source|**•**<br>XML-attribute`FingerAcquistion/PADInformation/ProbePADInfo/@total`for share of PAD<br>probes with “detected” result<br>**•**<br>An XML-node with location or host information. This data may also be located in sources exter<br>nal to this Technical Guideline.<br>**•**<br>XML node`FingerAcquisition/StartTime`for period filtering|



**Table 4.129** Top and Bottom Locations by Detected Presentation Attack Detection 

|**Attribute**<br>|**Value**|
|---|---|
|Name<br>|Histogram presentation attack detection scores|
|Purpose<br> <br>|This histogram depicts the distribution of presentation attack detection scores. Thereby, e.g. the de<br>tection of unexpected high numbers of low presentation attack detection results shall be possible.|
|Type<br>|Histogram with Cumulative Distribution Function|
|X-Axis<br>|Presentation attack detection score|
|Y-Axis 1<br>|Number of probes|
|Y-Axis 2<br>|Axis for empirical cumulative distribution function scaled from 0 to 1.|
|Facet<br><br><br>|**•**<br>Finger Code<br>**•**<br>PAD Subsystem<br>**•**<br>Finger Acquisition Hardware|



Federal Office for Information Security 

141 

4 Function Modules 

|**Attribute**|**Value**|
|---|---|
|Data Source|**•**<br>XML node`FingerAcquisition/StartTime`for period filtering<br>**•**<br>distribution of`XML-attribute FingerAcquisition/PADInformation/ProbePADInfo/pad/`<br>`@result`<br>**•**<br>XML-attribute`FingerAcquisition/FingerCapture/@fc`for facet<br>**•**<br>XML node`FingerAcquisition/PADInformation/PADSubsystem`for facet, child node values<br>concatenated<br>**•**<br>XML node`FingerAcquisition/Hardware`for facet, child node values concatenated|
|Example Visualisati<br>on|Figure 4.56|



**Table 4.130** Histogram Number of Presentation Attack Detection Scores 


![](markdown/tr/TR-03121-3_2_Biometrics_GID_521_OR/TR-03121-3_2_Biometrics_GID_521_OR.pdf-0150-03.png)


**Figure 4.56.** Example Histogram Number of Presentation Attack Detection Scores 

Federal Office for Information Security 

142 

List of Abbreviations 

## List of Abbreviations 

|**Abbreviation**|**Description**|
|---|---|
|ABIS|Automated Biometric Identification System|
|AH|Acquisition Hardware|
|AS|Acquisition Software|
|BDB|Biometric Data Block|
|BHT|Biometric Header Template|
|BIP|Biometric Image Processing|
|BIT|Biometric Information Template|
|CDF|Cumulative Distribution Function|
|CIR|Central Identity Register|
|CMP|Biometric Comparison|
|COD|Coding|
|COM|Compression|
|CTF|contrast transfer function|
|DET|Detection Error Trade-Off|
|ePass|Electronic Passport|
|FAR|false accept rate|
|FIR|Finger Image Record|
|FM|Function Module|
|FMR|false-match-rate|
|FNMR|false-non-match-rate|
|FRR|false reject rate|
|FTA|failure to aquire|
|FTE|failure to enrol|
|LOG|Logging|
|O|Operation|
|PAD|presentation attack detection|
|PAP|Partial Application Process|
|QA|Quality Assessment|
|REF|Reference Storage|
|SNR|signal-to-noise ratio|
|SSS|self-service system|
|TR|Technical Guideline|
|UI|User Interface|
|WSQ|Wavelet Scalar Quantisation|



Federal Office for Information Security 

143 

Bibliography 

## Bibliography 

- [BIB_AufenthG] _Aufenthaltsgesetz of 25. Feburary 2008 (BGBl. I S. 162), last changed by law from 12. July 2018 (BGBl. I S. 1147)._ 

- [BIB_EBTS/F] _FBI Electronic Biometric Transmission Specification Version 8, Appendix F, September 2007._ 

- [BIB_EC_1030_2002] _Regulation (EC) No 1030/2002 of 13 June 2002 laying down a uniform format for residence permits for third-country nationals._ 

- [BIB_EC_2252/2004] _Regulation (EC) No 2252/2004 of the European Parliament and of the Council of 13 Decem ber 2004 on standards for security features and biometrics in passports and travel documents issued by Member States._ 

- [BIB_ICAO_9303] _ICAO Document 9303, Machine Readable Travel Documents, 7th edition, 2016._ 

- [BIB_ISO_10918-1] _ISO/IEC 10918-1:1994 "Information technology – Digital compression and coding of conti nuous-tone still images: Requirements and guidelines"._ 

- [BIB_ISO_15444] _ISO/IEC 15444-1:2004 "Information technology – JPEG 2000 image coding system: Core coding system"._ 

- [BIB_ISO_19785-3] _ISO/IEC 19785-3:2007 "Information technology – Common Biometric Exchange Formats Framework – Part 3: Patron format specification"._ 

- [BIB_ISO_FACE] _ISO/IEC 19794-5:2005 "Information technology - Biometric data interchange formats – Part 5: Face image data"._ 

- [BIB_ISO_FINGER] _ISO/IEC 19794-4:2005 "Information technology - Biometric data interchange formats – Part 4: Finger image data"._ 

- [BIB_ISO_PAD_1] _ISO/IEC 30107-1:2016 "Information technology – Biometric presentation attack detection – Part 1: Framework"._ 

- [BIB_ISO_PAD_3] _ISO/IEC 30107-3:2017 "Information technology – Biometric presentation attack detection – Part 3: Testing and reporting"._ 

- [BIB_NFIQ2.0] _http://www.nist.gov/itl/iad/ig/development_nfiq_2.cfm, Source code from Apr 28, 2016._ 

- [BIB_PassG] _Paßgesetz of 19. April 1986 (BGBl. I S. 537), last change by Article 2 of law from 7. July 2017 (BGBl. I S. 2310)._ 

- [BIB_PAuswG] _Personalausweisgesetz of 18. Juni 2009 (BGBl. I S. 1346), last changed by Article 4 of law from 18. Juli 2017 (BGBl. I S. 2745)._ 

- [BIB_RFC4122] _RFC 4122: A Universally Unique IDentifier (UUID) URN Namespace._ 

- [BIB_TR-03146] _BSI TR-03146 Elektronische Bildübermittlung zur Beantragung hoheitlicher Dokumente (E-Bild hD), Version 1.0._ 

- [BIB_UN REGIO] _Standard Country or Area Codes for statistical Use, United Nations Department Of Economic and Social Affairs Statistics Division, 1999._ 

Federal Office for Information Security 

144 


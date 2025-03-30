![](_page_0_Picture_0.jpeg)

BSI Technical Guideline TR-03121-3

# Biometrics for Public Sector Applications

Part 3: Application Profiles, Function Modules and Processes

Volume 4: Alien Register Enrolment (ARE)

Version 6.0

Federal Office for Information Security P.O. Box 20 03 63 53133 Bonn E-Mail: trbiometrics@bsi.bund.de Internet: https://bsi.bund.de © Federal Office for Information Security 2023

## **Table of Contents**

| 1.    | Volume Alien Register Enrolment<br><br>1                                                                                   |
|-------|----------------------------------------------------------------------------------------------------------------------------|
| 1.1.  | System Overview<br><br>1                                                                                                   |
| 2.    | Application Profiles<br><br>2                                                                                              |
| 2.1.  | Application Profile Arrival Attestation Document<br><br>2                                                                  |
| 2.2.  | Application Profile Arrival Attestation Document in Special Situations<br><br>4                                            |
| 3.    | Partial Application Processes<br><br>8                                                                                     |
| 3.1.  | PAP ACQ-FI-SV-2: Supervised Facial Image Acquisition with CIR Lookup<br><br>8                                              |
| 3.2.  | PAP DEL-FI-SV-1: Supervised Facial Image Digital Delivery<br><br>9                                                         |
| 3.3.  | PAP ACQ-FP442-SV-2: Supervised Acquisition 4-4-2 for Enrolment without Fall-back Single Finger<br>Acquisition<br><br>10    |
| 3.4.  | PAP ACQ-FP4141-SV-2: Supervised Acquisition 4-1-4-1 for Enrolment without Fall-back Single<br>Finger Acquisition<br><br>12 |
| 3.5.  | PAP ACQ-FP10R-SV-1: Ten Finger Rolled Supervised Acquisition for Enrolment<br><br>14                                       |
| 4.    | Function Modules<br><br>17                                                                                                 |
| 4.1.  | FM Category Acquisition Hardware<br><br>17                                                                                 |
| 4.2.  | FM Category Acquisition Software<br><br>20                                                                                 |
| 4.3.  | FM Category Biometric Image Processing<br><br>23                                                                           |
| 4.4.  | FM Category Quality Assessment<br><br>24                                                                                   |
| 4.5.  | FM Category Presentation Attack Detection<br><br>31                                                                        |
| 4.6.  | FM Category Compression<br><br>33                                                                                          |
| 4.7.  | FM Category Operation<br><br>34                                                                                            |
| 4.8.  | FM Category User Interface<br><br>35                                                                                       |
| 4.9.  | FM Category Reference Storage<br><br>37                                                                                    |
| 4.10. | FM Category Biometric Comparison<br><br>37                                                                                 |
| 4.11. | FM Category Logging<br><br>38                                                                                              |
| 4.12. | FM Category Coding<br><br>40                                                                                               |
|       | List of Abbreviations<br><br>42                                                                                            |
|       | Bibliography<br><br>43                                                                                                     |

## **List of Figures**

| 1.1. | System Architecture Overview Alien Register Enrolment<br><br>1                                                                      |
|------|-------------------------------------------------------------------------------------------------------------------------------------|
| 2.1. | Process Overview Arrival Attestation Document<br><br>3                                                                              |
| 2.2. | Process Overview Arrival Attestation Document in Special Situations<br><br>5                                                        |
| 3.1. | Partial Application Process "Supervised Facial Image Acquisition Process with CIR Lookup"<br><br>8                                  |
| 3.2. | Partial Application Process "Supervised Facial Image Digital Delivery"<br><br>10                                                    |
| 3.3. | Partial Application Process "Supervised Acquisition 4-4-2 for Enrolment without Fall-back Single Fin<br>ger Acquisition"<br><br>10  |
| 3.4. | Partial Application Process Task "Capture Slap Supervised without Fall-back Single Finger Acquisiti<br>on"<br><br>12                |
| 3.5. | Partial Application Process "Supervised Acquisition 4-1-4-1 for Enrolment without Fall-back Single<br>Finger Acquisition"<br><br>12 |
| 3.6. | Partial Application Process Task "Capture Slap Supervised without Fall-back Single Finger Acquisiti<br>on"<br><br>14                |
| 3.7. | Partial Application Process "Ten Finger Rolled Supervised Acquisition for Enrolment"<br><br>14                                      |
| 3.8. | Partial Application Process Task "Capture Rolled Finger"<br><br>16                                                                  |

## <span id="page-4-0"></span>**1. Volume Alien Register Enrolment**

This document defines Application Profiles, Function Modules and Processes for the [Alien Register Enrolment](#page-45-1) [\(ARE\)](#page-45-1) of biometric data for Identity Documents of asylum seekers.

### <span id="page-4-1"></span>**1.1. System Overview**

The main components in this context consist of the [Central Indentity Registers \(CIRs\)](#page-45-2), the [Biometric Evalua](#page-45-3) [tion Authority \(BEA\)](#page-45-3) and the local registration authority as depicted in [Figure 1.1](#page-4-2). Any request for biometric and biographic data retrieval or storage is performed via the [CIRs, which connects and proxies further back](#page-45-2) ground systems. The [BEA](#page-45-3) represents the destination for log files documenting process in detail. The ap plicant appears in person at the local registration authority, where an operator controls the live enrolment equipment and guides the process.

<span id="page-4-2"></span>![](_page_4_Figure_5.jpeg)

![](_page_4_Figure_6.jpeg)

In the depicted architecture, the [CIRs](#page-45-2) comprises of the Central Register of Foreigners (operated by Federal Office of Administration) in conjunction with the [Automated Fingerprint Identification System \(AFIS\) \(ope](#page-45-4) rated by Federal Criminal Office). The [BEA](#page-45-3) is also operated by the Federal Office of Administration.

## <span id="page-5-0"></span>**2. Application Profiles**

The following sections specify the Application Profiles of this Volume.

### <span id="page-5-2"></span><span id="page-5-1"></span>**2.1. Application Profile Arrival Attestation Document**

The following Application Profile describes the application for an Arrival Attestation Document. [Function](#page-45-5) [Modules \(FMs\)](#page-45-5) may have additional transition rules for their requirements.

The requirements for the application and issuance of an Arrival Attestation Document are determined by national law [\[BIB\\_AsylG\]](#page-46-1) §63a according to [\[BIB\\_AKNV\]](#page-46-2).

By legal requirements, the enrolment of the applicant´s facial image and fingerprints (only for applicants 14 years of age or older) is mandatory. In addition to the issued document, the recorded information must be transferred to the Central Register of Foreigners (according to [\[BIB\\_AZRG\]](#page-46-3) §3 and [\[BIB\\_AZRGDV\]](#page-46-4) §5).

#### **2.1.1. Mandatory Process**

In general, two different scenarios exist, refer to [Figure 2.1](#page-6-0): One scenario is the pre-registration with storage of the applicant's biographic and biometric data in the [CIR.](#page-45-2) The issuance of the Arrival Attestation Document is performed at any registration office later on in a separate process by retrieving the already existing data from the [CIR](#page-45-2). In the other scenario, the process consists of both biographic and biometric data assessment and the immediate subsequent issuance of the document.

In any case, the main process SHALL begin with an initial identification request to the [CIR](#page-45-2). Up to ten plain fingerprints SHALL be captured from the applicant and sent to the [CIR in order to perform a biometric iden](#page-45-2) tification and check whether the applicant has already been registered upfront. The returned result is either empty or contains a set of identification results.

In case the identification fails, i.e. no record is returned from the [CIR](#page-45-2), a new data record for the applicant SHALL be created and subsequently sent to the [CIR](#page-45-2) for storage. For this purpose, rolled fingerprints SHALL be captured additionally. A biometric control verification (cross verification) with the previously captured plain fingerprints SHALL be used as [Quality Assessment \(QA\)](#page-45-6) in this process.

In case one or more facial images of the applicant are present in a retrieved record, they SHALL be assessed in regard to quality requirements and re-usability for the issuance of the Arrival Attestation Document. If no facial image is available from the [CIR,](#page-45-2) a high quality image SHALL be captured live by the operator using a facial image camera with subsequently applied [QA](#page-45-6). Note that this Application Profile allows for high quality digital cameras only, the use of webcams is not permitted within this application context.

The applicant´s biographic and biometric data including process and quality information are coded and passed to the calling application, which directs the data to the back-end system for enrolment.

<span id="page-6-0"></span>![](_page_6_Figure_1.jpeg)

**Figure 2.1.** Process Overview Arrival Attestation Document

#### **2.1.2. Relevant Standards and Conditions**

In addition to the legal requirements, further basic directives and standards are applicable.

- **•** [\[BIB\\_GSAT3\]](#page-46-5)
- **•** [\[BIB\\_ISO\\_FACE\]](#page-46-6)
- **•** [\[BIB\\_ISO\\_FINGER\]](#page-46-7)

#### **2.1.3. Mandatory Function Modules**

All Function Modules which SHALL be applied for this Application Profile are listed in [Table 2.1](#page-6-1). All listed Function Modules (separated by commas) are mandatory for this Application Profile unless specified other wise. Function Modules separated by slash are alternatives to each other. Function Modules in brackets are RECOMMENDED.

<span id="page-6-1"></span>

| Module Category               | Required Function Modules                          |
|-------------------------------|----------------------------------------------------|
| Acquisition Hardware          | FM AH-FI-DC                                        |
|                               | FM AH-FP-ALL /<br>FM AH-FP-OPT                     |
| Acquisition Software          | FM AS-FI-DC                                        |
|                               | FM AS-FP-MF, (<br>FM AS-FP-SLP ),<br>FM AS-FP-ROLL |
| Biometric Image Processing    | FM BIP-FI-DC-HQ                                    |
|                               | FM BIP-FP-APP                                      |
| Quality Assessment            | FM QA-FI-PG,<br>FM QA-FI-GENERIC,<br>FM QA-FI-ARE  |
|                               | FM QA-FP-APP                                       |
| Presentation Attack Detection | FM PAD-FP-APP                                      |
| Compression                   | FM COM-FI-GENERIC                                  |
|                               | FM COM-FI-JPG                                      |
|                               | FM COM-FP-WSQE                                     |
| Operation                     | FM O-FI-ALL                                        |
|                               | FM O-FI-DC                                         |
|                               | FM O-FP-ALL                                        |

| Module Category      | Required Function Modules             |
|----------------------|---------------------------------------|
| User Interface       | FM UI-FI-OP                           |
|                      | FM UI-FP-OP,<br>FM UI-FP-BSJ          |
| Reference Storage    | FM REF-FI-ARE                         |
|                      | FM REF-FP-ARE                         |
| Biometric Comparison | FM CMP-FP-CV                          |
| Logging              | FM LOG-ALL-GENERIC,<br>FM LOG-ALL-ARE |
|                      | FM LOG-FI-GENERIC                     |
|                      | FM LOG-FP-GENERIC                     |
| Coding               | FM COD-ALL-ARE                        |
|                      | FM COD-FI-GSAT3                       |
|                      | FM COD-FP-GSAT3                       |
| Evaluation           | -                                     |

**Table 2.1** Required Function Modules Application Profile Arrival Attestation Document

### **2.1.4. Mandatory Partial Application Processes**

All Partial Application Processes and Tasks which SHALL be applied for this Application Profile are listed in [Table 2.2](#page-7-1). All listed Processes (separated by commas) are mandatory for this Application Profile unless specified otherwise. Processes separated by slash are alternatives to each other.

<span id="page-7-1"></span>

| No. | Required Partial Application Process                                                                                                                                                                                          |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | PAP ACQ-FP10R-SV-1: Ten Finger Rolled Supervised Acquisition for Enrolment                                                                                                                                                    |
| 2   | PAP ACQ-FP442-SV-2: Supervised Acquisition 4-4-2 for Enrolment without Fall-back Single Finger Acquisition /<br>PAP ACQ-FP4141-SV-2: Supervised Acquisition 4-1-4-1 for Enrolment without Fall-back Single Finger Acquisition |
| 3   | PAP ACQ-FI-SV-2: Supervised Facial Image Acquisition with CIR Lookup                                                                                                                                                          |
| 4   | PAP DEL-FI-SV-1: Supervised Facial Image Digital Delivery                                                                                                                                                                     |

**Table 2.2** Required Partial Application Processes Application Profile Arrival Attention Document

### <span id="page-7-0"></span>**2.2. Application Profile Arrival Attestation Document in Special Situations**

The following Application Profile describes the application for an Arrival Attestation Document in special situations. A special situation is in place, e.g. when the number of applicants for an Arrival Attestation Docu ment is significantly higher than usual due to external events. Note that applications under this profile can only be used at particular (temporary) agencies in charge that are specifically approved for this special situa tion by the German Federal Ministry of the Interior.

Instead of the usual process (described in [Section 2.1](#page-5-2)), the capture of rolled fingerprints is neglected in favour of the capture of plain fingerprints, as described in [Section 3.3](#page-13-3) or [Section 3.4.](#page-15-0) [FMs](#page-45-5) may have additional transition rules for their requirements.

The requirements for the application and issuance of an Arrival Attestation Document are determined by national law [\[BIB\\_AsylG\]](#page-46-1) §63a according to [\[BIB\\_AKNV\]](#page-46-2).

By legal requirements, the enrolment of the applicant`s facial image and fingerprints (only for applicants 14 years of age or older) is mandatory. In addition to the issued document, the recorded information must be transferred to the Central Register of Foreigners (according to [\[BIB\\_AZRG\]](#page-46-3) §3 and [\[BIB\\_AZRGDV\]](#page-46-4) §5).

#### **2.2.1. Mandatory Process**

In general, two different scenarios exist, refer to [Figure 2.2](#page-8-0): One scenario is the pre-registration with storage of the applicant's biographic and biometric data in the [CIR.](#page-45-2) The issuance of the Arrival Attestation Document is performed at any registration office later on in a separate process by retrieving the already existing data from the [CIR](#page-45-2). In the other scenario, the process consists of both biographic and biometric data assessment and the immediate subsequent issuance of the document.

In any case, the main process SHALL begin with an initial identification request to the [CIR](#page-45-2). Up to ten plain fingerprints SHALL be captured from the applicant and sent to the [CIR in order to perform a biometric iden](#page-45-2) tification and check whether the applicant has already been registered upfront. The returned result is either empty or contains a set of identification results.

In case the identification fails, i.e. no record is returned from the [CIR](#page-45-2), a new data record for the applicant SHALL be created and subsequently sent to the [CIR](#page-45-2) for storage.

In case one or more facial images of the applicant are present in a retrieved record, they SHALL be assessed in regard to quality requirements and re-usability for the issuance of the Arrival Attestation Document. If no facial image is available from the [CIR](#page-45-2), a facial image SHALL be captured live by the operator using a facial image camera with subsequently applied [QA](#page-45-6).

Note that this Application Profile allows for digital cameras as well as for webcams. The requirements for focal length do not apply in this scenario (refer to [FM AH-FI-DC](#page-20-2) ).

The applicant´s biographic and biometric data including process and quality information are coded and passed to the calling application, which directs the data to the back-end system for enrolment.

<span id="page-8-0"></span>![](_page_8_Figure_9.jpeg)

**Figure 2.2.** Process Overview Arrival Attestation Document in Special Situations

#### **2.2.2. Relevant Standards and Conditions**

In addition to the legal requirements, further basic directives and standards are applicable.

- **•** [\[BIB\\_GSAT3\]](#page-46-5)
- **•** [\[BIB\\_ISO\\_FACE\]](#page-46-6)
- **•** [\[BIB\\_ISO\\_FINGER\]](#page-46-7)

#### **2.2.3. Mandatory Function Modules**

All Function Modules which SHALL be applied for this Application Profile are listed in [Table 2.3](#page-9-0). All listed Function Modules (separated by commas) are mandatory for this Application Profile unless specified other wise. Function Modules separated by slash are alternatives to each other. Function Modules in brackets are RECOMMENDED.

<span id="page-9-0"></span>

| Module Category               | Required Function Modules                         |
|-------------------------------|---------------------------------------------------|
| Acquisition Hardware          | FM AH-FI-DC                                       |
|                               | FM AH-FP-ALL /<br>FM AH-FP-OPT                    |
| Acquisition Software          | FM AS-FI-DC                                       |
|                               | FM AS-FP-MF, (<br>FM AS-FP-SLP )                  |
| Biometric Image Processing    | FM BIP-FI-DC-HQ                                   |
|                               | FM BIP-FP-APP                                     |
| Quality Assessment            | FM QA-FI-PG,<br>FM QA-FI-GENERIC,<br>FM QA-FI-ARE |
|                               | FM QA-FP-APP                                      |
| Presentation Attack Detection | (<br>FM PAD-FP-APP )                              |
| Compression                   | FM COM-FI-GENERIC                                 |
|                               | FM COM-FI-JPG                                     |
|                               | FM COM-FP-WSQE                                    |
| Operation                     | FM O-FI-ALL                                       |
|                               | FM O-FI-DC                                        |
|                               | FM O-FP-ALL                                       |
| User Interface                | FM UI-FI-OP                                       |
|                               | FM UI-FP-OP,<br>FM UI-FP-BSJ                      |
| Reference Storage             | FM REF-FI-ARE                                     |
|                               | FM REF-FP-ARE                                     |
| Biometric Comparison          | FM CMP-FP-CV                                      |
| Logging                       | FM LOG-ALL-GENERIC,<br>FM LOG-ALL-ARE             |
|                               | FM LOG-FI-GENERIC                                 |
|                               | FM LOG-FP-GENERIC                                 |
| Coding                        | FM COD-ALL-ARE                                    |
|                               | FM COD-FI-GSAT3                                   |
|                               | FM COD-FP-GSAT3                                   |
| Evaluation                    | -                                                 |

**Table 2.3** Required Function Modules Application Profile Arrival Attestation Document

#### **2.2.4. Mandatory Partial Application Processes**

All Partial Application Processes and Tasks which SHALL be applied for this Application Profile are listed in [Table 2.4](#page-10-0). All listed Processes (separated by commas) are mandatory for this Application Profile unless specified otherwise. Processes separated by slash are alternatives to each other.

<span id="page-10-0"></span>

| No. | Required Partial Application Process                                                                                                                                                                                          |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | PAP ACQ-FP442-SV-2: Supervised Acquisition 4-4-2 for Enrolment without Fall-back Single Finger Acquisition /<br>PAP ACQ-FP4141-SV-2: Supervised Acquisition 4-1-4-1 for Enrolment without Fall-back Single Finger Acquisition |
| 2   | PAP ACQ-FI-SV-2: Supervised Facial Image Acquisition with CIR Lookup                                                                                                                                                          |
| 3   | PAP DEL-FI-SV-1: Supervised Facial Image Digital Delivery                                                                                                                                                                     |

**Table 2.4** Required Partial Application Processes Application Profile Arrival Attention Document

## <span id="page-11-0"></span>**3. Partial Application Processes**

The [Partial Application Processes \(PAPs\)](#page-45-7) specified by the following sections provide process specifications of basic biometric processes, e.g. the acquisition, identification or verification of biometrics or the evaluation processes for verification and identification. The [PAPs](#page-45-7) are referenced by the relevant Application Profiles and are part of the overall processes specified therein.

A [PAP](#page-45-7) MAY also be a task. A task is a process which functions as a generic reusable building block which is used by another [PAP](#page-45-7) and is not referenced by an Application Profile directly.

The specific Function Modules that SHALL be implemented in the processes of this chapter are specified by the relevant Application Profiles.

### <span id="page-11-3"></span><span id="page-11-1"></span>**3.1. PAP ACQ-FI-SV-2: Supervised Facial Image Acquisition with CIR Lookup**

The facial image acquisition process described in this section SHALL be supervised. Also, the required [CIRs](#page-45-2) which MAY already contain a facial image of the biometric subject SHALL be available. Thus, two options of how an image of the biometric subject can be obtained are available, refer to [Figure 3.1](#page-11-2):

- 1. The biometric subject's facial image is captured by an operator using live enrolment equipment (including a facial image camera within a photo studio setup)[1](#page-11-4) . Note that the requirements regarding the facial image camera in use (digital camera, webcam, etc.) depend on the specific application context. Refer to cor responding Application Profile for further information.
- 2. One or more facial images of the biometric subject already exist in the [CIR](#page-45-2) and can be retrieved to be examined for re-use.

In the first case, a facial image of the biometric subject is taken live by the operator using a facial image camera. An immediately performed software [QA](#page-45-6) for the captured facial image ensures its biometric usability. If the [QA](#page-45-6) succeeds, the facial image is released to the calling software. If the quality is assessed as insufficient, the operator can recapture or has the option to put a veto in order to accept the captured facial image despite the negative software decision. In case of an overruling veto, the facial image is accepted and released to the calling application. In the negative case, the facial image is discarded and a re-capture is performed.

<span id="page-11-2"></span>![](_page_11_Figure_10.jpeg)

**Figure 3.1.** Partial Application Process "Supervised Facial Image Acquisition Process with CIR Lookup"

<span id="page-11-4"></span><sup>1</sup> See ISO/IEC 19794-5, Annex B for "Best practices for Face Images"

In case one or more facial images of the biometric subject are available in the [CIR,](#page-45-2) they can potentially be reused for the issuance of the document. In case the [CIR](#page-45-2) does provide information about the capture date or date of storing, only facial images SHALL be retrieved which are not older than six months by capture date or date of storing. The quality of each retrieved facial image SHALL be assessed by the software in regard to quality requirements and usability for the purpose of enrolment. Additionally, the best retrieved image SHALL be identified by the software [QA.](#page-45-6) After the images were processed by the software [QA](#page-45-6), they are displayed to the operating operator for selection via the [graphical user interface \(GUI\)](#page-45-8) of the software in order to be selected for release. Thereby, only those images are displayed which pass the [QA](#page-45-6) with a positive result and they SHALL be displayed in descending order of [QA](#page-45-6)-rating. Further, the best image SHALL be clearly marked and automatically pre-selected, so that the operator still needs to confirm the pre-selection of the image. In case none of the retrieved images are considered to be of sufficient quality a live facial image SHALL be captured (see first case).

The operator SHALL have the following veto options:

- **•** Select none of the retrieved facial images despite sufficient quality from the [CIR.](#page-45-2)
- **•** Select a facial image of insufficient quality from the acquisition process.

The process SHALL be supervised by an operator.

#### **3.1.1. Interface Requirements**

If [High Level Biometric Services \(HLBS\)](#page-45-9) is used by the system, "Service Definition Basic Facial Image Ac quisition System" of Part 2, Volume 2 of this Technical Guideline SHALL be implemented.

### <span id="page-12-1"></span><span id="page-12-0"></span>**3.2. PAP DEL-FI-SV-1: Supervised Facial Image Digital Delivery**

#### **3.2.1. Process**

The facial image delivery process, refer to [Figure 3.2](#page-13-1), described by this section requires a supervised situation performed by an operator [2](#page-12-2) .

After loading the captured facial image(s) into the operators application, an immediately performed cropping and de-rotation of the face software quality assessment for captured facial image(s) ensures its bio metric usability. Following a quality assessment the image(s) SHALL be shown to the operator. The system MAY identify the best captured facial image, show this image to the operator and preselect it. The operator SHALL have the option to correct the cropping and de-rotation on the shown image(s) manually. The operator SHALL also have the option to accept one of the captured facial image(s). The image is then released to the calling application. This is also the case, if the quality has been assessed as insufficient by the system.

In the case that the operator rejects the image(s) the process terminates without releasing an image. This is also the case, if the quality has been assessed as sufficient by the system.

Note, the facial image(s) captured SHALL be handled, transported and loaded into the operators application by the operators only. The biometric subject MUST NOT gain access to the facial image(s) at any time during this process.

<span id="page-12-2"></span><sup>2</sup> See ISO/IEC 19794-5, Annex B for "Best practices for Face Images"

<span id="page-13-1"></span>![](_page_13_Figure_1.jpeg)

**Figure 3.2.** Partial Application Process "Supervised Facial Image Digital Delivery"

#### **3.2.1.1. Interface Requirements**

If [HLBS](#page-45-9) is used by the system, the "Service Definition Facial Image Delivery System" of Part 2, Volume 2 of this Technical Guideline SHALL be implemented.

### <span id="page-13-3"></span><span id="page-13-0"></span>**3.3. PAP ACQ-FP442-SV-2: Supervised Acquisition 4-4-2 for Enrolment without Fall-back Single Finger Acquisition**

The capture process for the 4-4-2 enrolment scenario is shown in [Figure 3.3.](#page-13-2) Single finger acquisition as fallback is not allowed in this process. Note, that the [PAP Task ACQ-FPS-SV-2: Capture Slap Supervised without](#page-13-4) [Fall-back Single Finger Acquisition](#page-13-4) is used here. The 4-4-2 sequences are described in detail subsequently:

- 1. acquire right slap: index finger, middle finger, ring finger, little finger
- 2. acquire left slap: index finger, middle finger, ring finger, little finger
- 3. thumbs of both hands (simultaneously)

The process SHALL be supervised by an operator.

<span id="page-13-2"></span>![](_page_13_Figure_11.jpeg)

**Figure 3.3.** Partial Application Process "Supervised Acquisition 4-4-2 for Enrolment without Fall-back Single Finger Acquisition"

#### **3.3.1. Interface Requirements**

If [HLBS](#page-45-9) is used by the system, the "Service Definition Fingerprint Acquisition System" of Part 2, Volume 2 of this Technical Guideline SHALL be implemented.

#### <span id="page-13-4"></span>**3.3.2. PAP Task ACQ-FPS-SV-2: Capture Slap Supervised without Fall-back Single Finger Acquisition**

[Figure 3.4](#page-15-1) depicts the basic process for a plain supervised slap capture. A plain slap capture can be part of more complex acquisition processes, e.g. a ten finger acquisition by the 4-1-4-1 capture sequence. The plain slap capture is subsequently described in detail. The [QA](#page-45-6) is conducted according to the requirements of the applicable [FM Category Quality Assessment](#page-27-0).

- 1. The counter variable for the number of attempts for capturing the current slap SHALL be initialized as *i* = 1.
- 2. The slap image SHALL be retrieved from hardware. While the image is retrieved from hardware, [Presenta](#page-45-10) [tion Attack Detection \(PAD\)](#page-45-10) SHALL be performed. Note: The operator SHALL have the option to manually conduct the capture of slap(s).
- 3. The fingerprints SHALL be segmented and each SHALL be quality assessed.
	- a. In case the quality of the fingerprints meets the quality requirements defined in the corresponding [QA](#page-45-6) [FM,](#page-45-5) the captured slap and the set of segmented fingerprints and parameter data (e.g. quality values) SHALL be temporarily stored.
	- b. In case the quality requirements for one or more fingerprints of the slap are not met, the capture SHALL be repeated up to two times (i.e. the acquisition of a single slap consists of a maximum of three capture attempts). The counter SHALL be set to *i* = *i* + 1.
- 4. A uniqueness check SHALL be conducted for the captured slap image to detect capture of wrong fin gers, e.g. due to interchanged hands or multiple acquisition of the same hand finger. Note, that it is RE COMMENDED to conduct the uniqueness check as early as possible after a fingerprint image is available.

a. In case

- **•** the comparison of any fingerprint of the current slap with any previously accepted fingerprint of a previous slap or
- **•** the comparison of a fingerprint of the current slap with another finger print of the current slap

is successful, the uniqueness check SHALL show a warning.

- b. In case the comparisons of all fingers current slap with previous slaps are not suc cessful, the uniqueness check SHALL report no error.
- 5. Generally, a slap classifier SHALL[3](#page-14-0) be used for the captured slap image to detect the capture of the wrong slap. It SHALL be configurable to switch the classifier off or in evaluation mode (logging of result wi thout showing the result/error to the operator). Note, that the slap classifier is only required for 4 finger slaps. Other acquisitions currently do not require the corresponding [FM.](#page-45-5)
	- a. If the result of the classification concludes that the acquired slap mismatches the expected slap, an error SHALL be reported.
	- b. If the result of the classification concludes that the acquired slap matches the expected slap, no error SHALL be reported.

If the quality check of the third capture attempt fails (counter *i* is set to 3), the best of the captured slaps SHALL be identified according to the corresponding [QA](#page-45-6) Function Module and temporarily stored along with corresponding information.

The process SHALL be supervised by an operator.

At the end of the process the operator decides on one of the three options:

- 1. Use the acquired slap.
- 2. Recapture the current slap. The counter will be reset to *i* = 1.
- 3. Restart the total slap acquisition workflow.

<span id="page-14-0"></span><sup>3</sup> For Volume ARE, this is only RECOMMENDED.

<span id="page-15-1"></span>![](_page_15_Figure_1.jpeg)

**Figure 3.4.** Partial Application Process Task "Capture Slap Supervised without Fall-back Single Finger Acquisition"

### <span id="page-15-0"></span>**3.4. PAP ACQ-FP4141-SV-2: Supervised Acquisition 4-1-4-1 for Enrolment without Fall-back Single Finger Acquisition**

[Figure 3.5](#page-15-2) depicts the acquisition process for 4-1-4-1 the enrolment scenarios. Note, that the [PAP Task](#page-13-4) [ACQ-FPS-SV-2: Capture Slap Supervised without Fall-back Single Finger Acquisition](#page-13-4) is used here. The 4-1-4-1 sequence is described in detail subsequently:

- 1. capture right hand: index finger, middle finger, ring finger, little finger
- 2. capture right hand: thumb
- 3. capture left hand: index finger, middle finger, ring finger, little finger
- 4. capture left hand: thumb

The process SHALL be supervised by an operator.

<span id="page-15-2"></span>![](_page_15_Figure_10.jpeg)

**Figure 3.5.** Partial Application Process "Supervised Acquisition 4-1-4-1 for Enrolment without Fall-back Single Finger Acquisition"

#### **3.4.1. Interface Requirements**

If [HLBS](#page-45-9) is used by the system, the "Service Definition Fingerprint Acquisition System" of Part 2, Volume 2 of this Technical Guideline SHALL be implemented.

### **3.4.2. PAP Task ACQ-FPS-SV-2: Capture Slap Supervised without Fall-back Single Finger Acquisition**

[Figure 3.4](#page-15-1) depicts the basic process for a plain supervised slap capture. A plain slap capture can be part of more complex acquisition processes, e.g. a ten finger acquisition by the 4-1-4-1 capture sequence. The plain slap capture is subsequently described in detail. The [QA](#page-45-6) is conducted according to the requirements of the applicable [FM Category Quality Assessment](#page-27-0).

- 1. The counter variable for the number of attempts for capturing the current slap SHALL be initialized as *i* = 1.
- 2. The slap image SHALL be retrieved from hardware. While the image is retrieved from hardware, [PAD](#page-45-10) SHALL be performed. Note: The operator have the option to manually conduct capture of sla p(s).
- 3. The fingerprints SHALL be segmented and each SHALL be quality assessed.
	- a. In case the quality of the fingerprints meets the quality requirements defined in the corresponding [QA](#page-45-6) [FM,](#page-45-5) the captured slap and the set of segmented fingerprints and parameter data (e.g. quality values) SHALL be temporarily stored.
	- b. In case the quality requirements for one or more fingerprints of the slap are not met, the capture SHALL be repeated up to two times (i.e. the acquisition of a single slap consists of a maximum of three capture attempts). The counter SHALL be set to *i* = *i* + 1.
- 4. A uniqueness check SHALL be conducted for the captured slap image to detect capture of wrong fin gers, e.g. due to interchanged hands or multiple acquisition of the same hand finger. Note, that it is RE COMMENDED to conduct the uniqueness check as early as possible after a fingerprint image is available.
	- a. In case
		- **•** the comparison of any fingerprint of the current slap with any previously accepted fingerprint of a previous slap or
		- **•** the comparison of a fingerprint of the current slap with another finger print of the current slap

is successful, the uniqueness check SHALL show a warning.

- b. In case the comparisons of all fingers current slap with previous slaps are not suc cessful, the uniqueness check SHALL report no error.
- 5. Generally, a slap classifier SHALL[4](#page-16-0) be used for the captured slap image to detect the capture of the wrong slap. It SHALL be configurable to switch the classifier off or in evaluation mode (logging of result wi thout showing the result/error to the operator). Note, that the slap classifier is only required for 4 finger slaps. Other acquisitions currently do not require the corresponding [FM.](#page-45-5)
	- a. If the result of the classification concludes that the acquired slap mismatches the expected slap, an error SHALL be reported.
	- b. If the result of the classification concludes that the acquired slap matches the expected slap, no error SHALL be reported.

If the quality check of the third capture attempt fails (counter *i* is set to 3), the best of the captured slaps SHALL be identified according to the corresponding [QA](#page-45-6) Function Module and temporarily stored along with corresponding information.

The process SHALL be supervised by an operator.

At the end of the process the operator decides on one of the three options:

1. Use the acquired slap.

<span id="page-16-0"></span><sup>4</sup> For Volume ARE, this is only RECOMMENDED.

- 2. Recapture the current slap. The counter will be reset to *i* = 1.
- 3. Restart the total slap acquisition workflow.

<span id="page-17-1"></span>![](_page_17_Figure_3.jpeg)

**Figure 3.6.** Partial Application Process Task "Capture Slap Supervised without Fall-back Single Finger Acquisition"

### <span id="page-17-0"></span>**3.5. PAP ACQ-FP10R-SV-1: Ten Finger Rolled Supervised Acquisition for Enrolment**

[Figure 3.7](#page-17-2) depicts the acquisition process for ten rolled fingers. Note, that the [PAP Task ACQ-FPR-1: Cap](#page-17-3) [ture Rolled Fingerprint](#page-17-3) is used here. The sequence is described in detail subsequently:

- 1. The permanently and temporarily missing fingers are selected.
- 2. Each available finger is captured according to "Capture Rolled Fingerprint" process. In case the finger to be captured is permanently or temporarily missing (e.g. due to injury) or unable to be captured, the current capture is skipped.

<span id="page-17-2"></span>When all available fingers have been captured, the process finishes.

![](_page_17_Figure_10.jpeg)

**Figure 3.7.** Partial Application Process "Ten Finger Rolled Supervised Acquisition for Enrolment"

#### **3.5.1. Interface Requirements**

If [HLBS](#page-45-9) is used by the system, the "Service Definition Rolled Fingerprint Acquisition System" of Part 2, Volume 2 of this Technical Guideline SHALL be implemented.

### <span id="page-17-3"></span>**3.5.2. PAP Task ACQ-FPR-1: Capture Rolled Fingerprint**

[Figure 3.8 defines the basic sequence for a rolled fingerprint capture. The finger](#page-19-0) print capture can be part of more complex acquisition processes, e.g. a ten finger rolled acquisition. The basic sequence for a rolled fingerprint capture is described in detail subsequently. The [QA](#page-45-6) is conducted according to the requirements of the applicable [Section 4.4.](#page-27-0)

- 1. The counter variable for the number of attempts for capturing is initialized as *i* = 1.
- 2. The finger SHALL be placed on the fingerprint sensor with the guidance of the operator.
- 3. The rolled fingerprint images is retrieved from the acquisition hardware.
- 4. If the hardware reports an issue of the rolling process, the capture SHALL be repeated if i < 3. i is increased by 1.
- 5. If no hardware reported issue was found, [QA](#page-45-6) SHALL ensure proper quality of the captured fingerprint. Note, that the quality value of each capture attempt SHALL be logged according to [Section 4.11.4](#page-42-1).
	- a. In case the quality of the fingerprint meets the quality requirements defined in the corresponding [QA](#page-45-6) Function Module, the captured fingerprint and parameter data (e.g. quality values) are temporarily stored and the capture of the current finger finishes.
	- b. In case the quality requirements of the rolled fingerprint is not met, the capture SHALL be repeated if i < 3. i is increased by 1.
- 6. A uniqueness check SHALL be conducted for the captured fingerprint image to detect the capture of wrong fingers, e.g. due to interchanged hands or multiple acquisition of the same hand finger. Note: It is RE COMMENDED to conduct the uniqueness check as early as possible after a fingerprint image is available.
	- a. In case the comparison of current fingerprint with any previously captured is success ful, the uniqueness check SHALL report an alert.
	- b. In case the comparison of current fingerprint with any previously captured is not suc cessful, the uniqueness check SHALL NOT report an alert.
- 7. A control verification SHALL be conducted for each captured rolled image. Therefore, plain control slaps have to be captured in a workflow upfront. Note, it is RECOMMENDED to conduct the control verification as early as possible after a fingerprint image is available.
	- a. In case the comparison of the rolled finger and its corresponding plain finger is successful, the control verification is considered successful.
	- b. In case the comparison of the rolled finger and its plain finger is not successful and the rolled finger is successfully compared with any other plain finger, the control verification is considered not successful.
	- c. In case no successful comparison of the rolled finger and any plain occurs, control verifica tion is considered undetermined.
- 8. The capture SHALL be repeated up to two times because of hardware reported issues of the rolling process or quality issues. The operator SHALL be allowed to capture additional images if after the third attempt no fingerprint without hardware reported issue and sufficient quality was conducted.

If the quality check of the third capture attempt fails or the hardware reported an issue of the rolling process, the best of the previously captured images is identified according to the corresponding [QA](#page-45-6) Function Module and temporarily stored along with corresponding information. Note, that the quality value of each capture attempt SHALL be logged according to [Section 4.11.4.](#page-42-1)

<span id="page-19-0"></span>![](_page_19_Figure_1.jpeg)

**Figure 3.8.** Partial Application Process Task "Capture Rolled Finger"

## <span id="page-20-0"></span>**4. Function Modules**

This chapter lists all Function Modules for the defined Application Profiles.

### <span id="page-20-1"></span>**4.1. FM Category Acquisition Hardware**

Devices that are used for digitising physical, representable biometric characteristics are called [Acquisition](#page-45-11) [Hardware \(AH\).](#page-45-11) Digital cameras to capture images of the face, fingerprint sensors, or signature tablets can be named as examples.

#### <span id="page-20-2"></span>**4.1.1. FM AH-FI-DC**

This Function Module describes the requirements for facial image cameras and physical setups that are used to obtain facial images.

#### **4.1.1.1. Requirements**

- **•** The minimum physical resolution of the camera SHALL allow a cropping of an image to 1200 x 1600 pixels without any upscaling. Note, this requirement is OPTIONAL for scenarios where only a facial verification is performed.
- **•** Adequate image quality to meet the requirements of [\[BIB\\_ISO\\_FACE\]](#page-46-6) SHALL be provided.
- **•** The physical and environmental conditions for capturing facial images, such as the positioning of ca mera, proper lighting of the face and a uniform background as described in [\[BIB\\_ISO\\_FACE\]](#page-46-6) and [\[BIB\\_I](#page-46-8) [CAO\\_TR\\_Portrait\\_Quality\]](#page-46-8) SHALL be complied with. It is RECOMMENDED to use a uniform background in grey (i.e. R=G=B) between #A1A1A1 and #E1E1E1.
- **•** The camera system SHALL be able to capture images in colour (24 bit sRGB). Note, this requirement is OP TIONAL for scenarios where only a facial verification is performed.
- **•** The requirements for focal length (depending on the size of the camera sensor) as described in [\[BIB\\_I](#page-46-8) [CAO\\_TR\\_Portrait\\_Quality\]](#page-46-8) (chapters 5.2.1 and 5.2.2) SHALL be complied with. Wide-angle settings MUST NOT be used.

#### <span id="page-20-3"></span>**4.1.2. FM AH-FP-ALL**

This Function Module describes requirements for high quality fingerprint scanners (single finger and multi finger). In this set of requirements, one of the following certification SHALL be used:

- **•** FBI/CJIS Image Quality Specifications from [Electronic Biometric Transmission Specification \(EBTS\) Ap](#page-45-12) pendix F [\[BIB\\_EBTS/F\]](#page-46-9)
- **•** FBI/CJIS Biometric Specifications, [Personal Identity Verification \(PIV\) Image Quality Specification for Sing](#page-45-13) le Finger Capture Devices [\[BIB\\_PIV\]](#page-46-10)

Note, that the FBI certification allows for multiple types of fingerprint scanners e.g. capacitive and optical fingerprint scanners.

#### **4.1.2.1. Requirements**

For the acquisition of the fingerprints, only devices are permitted which meet the following requirements (in analogy to [\[BIB\\_EBTS/F\]](#page-46-9) and [\[BIB\\_PIV\]\)](#page-46-10).

- **•** Multi fingerprint scanners SHALL be certified according to [\[BIB\\_EBTS/F\]](#page-46-9) and the respective certificate SHALL be at hand.
- **•** Single fingerprint scanners SHALL be certified according to [\[BIB\\_EBTS/F\]](#page-46-9) or [\[BIB\\_PIV\]](#page-46-10) and the respective certificate SHALL be at hand.
- **•** For single singer scanners, a capturing area of at minimum 16 mm width and 20 mm height is REQUIRED (deviating from table F 1 in [\[BIB\\_EBTS/F\]](#page-46-9)).
- **•** The certificate according to [\[BIB\\_EBTS/F\]](#page-46-9) or [\[BIB\\_PIV\]](#page-46-10) SHOULD NOT be older than 5 years in order to ensure proper actuality. The certificate SHALL NOT be older than a maximum of 10 years.

### <span id="page-21-0"></span>**4.1.3. FM AH-FP-OPT**

This Function Module describes the requirements for optical high quality fingerprint scanners (single finger and multi finger).

#### **4.1.3.1. Requirements**

- **•** For the acquisition of the fingerprints, optical sensors using the principal of frustrated total reflection or direct contact (the imaging system is the sensor surface, typically separated by a transparent protection layer) according to the certification requirements of [\[BIB\\_ISO\\_FINGER\]](#page-46-7) (especially this means a resolution of 500 ppi or 1000 ppi) SHALL be used exclusively.
- **•** For the acquisition of the fingerprints, only devices are permitted which meet the following requirements (in analogy to [\[BIB\\_EBTS/F\]](#page-46-9)). Notwithstanding, a capturing area of at minimum 16 mm width and 20 mm height is REQUIRED (deviating from table F 1 in [\[BIB\\_EBTS/F\]\)](#page-46-9) for single finger scanners.

#### **4.1.3.1.1. Grey Scale Linearity**

When measuring a stepped series of uniform target reflectance patches ("step tablet") that substantially covers the scanner's grey range, the average value of each patch SHALL be within 7.65 grey levels of a linear, least squares regression line fitted between target reflectance patch values (independent variable) and scanner out put grey levels of 8 bit resolution (dependent variable).

#### **4.1.3.1.2. Resolution and Geometrical Accuracy**

Resolution: The scanner's final output fingerprint image SHALL have a resolution, in both sensor detector row and column directions, in the range: (*R ¡* 0*:*01*R*) to (*R* + 0*:*01*R*). The magnitude of *R* is either 500 ppi or 1000 ppi; a scanner MAY be certified at either one or both of these resolution levels. The scanner's true optical resolution SHALL be greater than or equal to *R*.

Across-Bar geometric accuracy: When scanning a 1.0 cy/mm, multiple parallel bar target, in both vertical bar and horizontal bar orientations, the absolute value of the difference (*D*) between the actual distance across parallel target bars (*X*), and the corresponding distance measured in the image (*Y*) SHALL NOT exceed the following values for at least 99 % of the tested cases in each print block measurement area and in each of the two directions:

**•** for 500 ppi scanners:

*D ·* 0*:*0007, for 0*:*00 *< X ·* 0*:*07 and

*D ·* 0*:*01*X*, for 0*:*07 *· X ·* 1*:*50

**•** for 1000 ppi scanners:

*D ·* 0*:*0005, for 0*:*00 *< X ·* 0*:*07 and

*D ·* 0*:*0071*X*, for 0*:*07 *· X ·* 1*:*50

where *D* = *jY ¡ Xj*, *X* = actual target distance, *Y* = measured image distance (*D; X; Y* are in inches).

Along-Bar geometric accuracy: When scanning a 1.0 cy/mm, multiple parallel bar target, in both vertical bar and horizontal bar orientations, the maximum difference in the horizontal or vertical direction, respectively, between the locations of any two points within a 1.5 inch segment of a given bar image, SHALL be less than 0.016 inches for at least 99 % of the tested cases in each print block measurement area and in each of the two orthogonal directions.

#### **4.1.3.1.3. Contrast Transfer Function**

The spatial frequency response SHALL be measured using a binary grid target (Ronchi-Grating), denoted as [contrast transfer function \(CTF\)](#page-45-14) measurement. When measuring the bar [CTF,](#page-45-14) it SHALL meet or exceed the minimum modulation values defined by equation [Equation 4.1](#page-22-0) or equation [Equation 4.2, in both the de](#page-22-1) tector's row and detector's column directions, and over any region of the scanner's field of view. [CTF](#page-45-14) values computed from equations [Equation 4.1](#page-22-0) and [Equation 4.2 for nominal test frequencies are given in the fol](#page-22-1) lowing table. None of the [CTF](#page-45-14) modulation values measured at specification spatial frequencies SHALL exceed 1.05. The output bar target image SHALL NOT exhibit any significant amount of aliasing. It is NOT REQUIRED that the bar target contains the exact frequencies listed in [Table 4.1,](#page-22-2) however, the target does need to cover the listed frequency range and contain bar patterns close to each of the listed frequencies.

The following equations are used to obtain the minimum acceptable [CTF](#page-45-14) modulation values when using bar targets that contain frequencies not listed in [Table 4.1](#page-22-2):

<span id="page-22-0"></span>**•** 500 ppi scanner, for f = 1.0 to 10.0 cy/mm:

$$CTF = 3.04105 \cdot 10^{-4} \cdot f^2 - 7.99095 \cdot 10^{-2} \cdot f + 1.02774 \tag{4.1}$$

<span id="page-22-1"></span>**•** 1000 ppi scanner, for f = 1.0 to 20.0 cy/mm:

$$CTF = -1.85487 \cdot 10^{-5} \cdot f^3 + 1.41666 \cdot 10^{-3} \cdot f^2 - 5.73701 \cdot 10^{-2} \cdot f + 1.01341 \tag{4.2}$$

For a given bar target, the specification frequencies include all of the bar frequencies which that target has in the range 1 to 10 cy/mm (500 ppi scanner) or 1 to 20 cy/mm (1000 ppi scanner).

<span id="page-22-2"></span>

| Frequency [cy/mm] | Minimum Modulation for 500 ppi<br>scanners | Minimum Modulation for<br>1000 ppi scanners | Maximum Modulation |
|-------------------|--------------------------------------------|---------------------------------------------|--------------------|
| 1.0               | 0.948                                      | 0.957                                       | 1.05               |
| 2.0               | 0.869                                      | 0.904                                       | 1.05               |
| 3.0               | 0.791                                      | 0.854                                       | 1.05               |
| 4.0               | 0.713                                      | 0.805                                       | 1.05               |
| 5.0               | 0.636                                      | 0.760                                       | 1.05               |
| 6.0               | 0.559                                      | 0.716                                       | 1.05               |
| 7.0               | 0.483                                      | 0.675                                       | 1.05               |
| 8.0               | 0.408                                      | 0.636                                       | 1.05               |
| 9.0               | 0.333                                      | 0.598                                       | 1.05               |
| 10.0              | 0.259                                      | 0.563                                       | 1.05               |
| 12.0              | ---                                        | 0.497                                       | 1.05               |
| 14.0              | ---                                        | 0.437                                       | 1.05               |
| 16.0              | ---                                        | 0.382                                       | 1.05               |
| 18.0              | ---                                        | 0.332                                       | 1.05               |
| 20.0              | ---                                        | 0.284                                       | 1.05               |

**Table 4.1** Minimum and Maximum Modulation

#### **4.1.3.1.4. Signal-to-Noise Ratio and the Grey–Level Uniformity**

The white [signal-to-noise ratio \(SNR\)](#page-45-15) and black [SNR](#page-45-15) SHALL each be greater than or equal to 125.0, in at least 97 % of respective cases, within each measurement area.

The grey level uniformity is defined for the three following cases:

- **•** Adjacent row, column uniformity: At least 99 % of the average grey levels between every two adjacent quar ter-inch long rows and 99 % between every two adjacent quarter-inch long columns, within each imaged area, SHALL NOT differ by more than 1.0 grey levels when scanning a uniform low reflectance target, and SHALL NOT differ by more than 2.0 grey levels when scanning a uniform high reflectance target.
- **•** Pixel to pixel uniformity: For at least 99.9 % of all pixels within every independent 0.25 inch by 0.25 inch area located within each imaged area, individual pixel's grey level SHALL NOT vary from the average by more than 22.0 grey levels, when scanning a uniform high reflectance target, and SHALL NOT vary from the average by more than 8.0 grey levels, when scanning a uniform low reflectance target.
- **•** Small area uniformity: For every two independent 0.25 inch by 0.25 inch areas located within each imaged area, the average grey levels of the two areas SHALL NOT differ by more than 12.0 grey levels when scanning a uniform high reflectance target, and SHALL NOT differ by more than 3.0 grey levels when scanning a uniform low reflectance target.

#### **4.1.3.1.5. Grey Scale Range of Fingerprint Images**

A fingerprint scanner operating at 500 ppi or 1000 ppi, SHALL perform the following sets of live scans:

- **•** For a standard roll and plain finger live scanner: capture complete set of fingerprints from each 10 sub jects; i.e. 10 rolls (all 5 fingers from each hand), 2 plain thumb impressions, and 2 plain 4-finger impressions.
- **•** For a palm scanner component of a live scan system: capture left and right palms from each of 10 subjects.
- **•** For an identification flat live scanner: capture left and right 4-finger plain impressions and dual thumb plain impressions from each of 10 subjects.

Within the histogram of each image all grey values with at least 5 Pixels in this are counted. The histo gram SHALL show no break and no other artefact. At least 80 % of the captured individual fingerprint images SHALL have a grey scale dynamic range of at least 200 grey levels, and at least 99% SHALL have a dynamic range of at least 128 grey levels.

### <span id="page-23-0"></span>**4.2. FM Category Acquisition Software**

The Function Module category [Acquisition Software \(AS\) contains all functionality regarding image proces](#page-45-16) sing for biometric purposes. Therefore, these Function Modules usually contains device driver software for the acquisition hardware or, in general, software that is very close to the physical hardware such as firmware. Furthermore, colour management and image enhancement mechanisms are part of this software layer.

#### <span id="page-23-1"></span>**4.2.1. FM AS-FI-DC**

This Function Module describes the requirements and interfaces for acquisition software used for facial image cameras in order to obtain digitised images.

#### **4.2.1.1. Requirements**

- **•** In regard to the application scenario an adequate resolution of the camera SHALL be chosen to acquire a facial image of at least 1200 x 1600 pixels with an inter eye distance of at least 120 pixels.
- **•** The images SHALL be captured and stored in colour (24 bit sRGB). Note, this requirement is OPTIONAL for scenarios where only a facial verification is performed.
- **•** In normal mode of operation, no compression artefacts SHALL be detectable in the image.

#### **4.2.1.2. Recommendations**

- **•** The image data SHOULD be provided without any compression or with lossless compression. If the acqui sition device does not support a lossless mode, the image MAY alternatively be provided with the minimal level of compression possible.
- **•** Acquisition software that supports calibration procedures for the respective digital camera SHOULD be used (in particular colour management).

#### <span id="page-24-0"></span>**4.2.2. FM AS-FP-MF**

This Function Module describes the requirements and interfaces for acquisition software for multi finger scanners.

#### **4.2.2.1. Requirements**

- **•** The image provided by acquisition software SHALL meet the criteria of fingerprints as described in [\[BIB\\_ISO\\_FINGER\]](#page-46-7). The requirements according to the certification requirements of [\[BIB\\_ISO\\_FINGER\]](#page-46-7) SHALL be met.
- **•** For the acquisition process, a pre-qualification of the fingerprints to prefer high quality SHALL be used. The activation of the acquisition SHALL occur automatically. The capture SHOULD prefer the highest quality image of a sequence.
- **•** This functionality MAY be part of the hardware firmware and MAY NOT be available as separate software component.
- **•** The thresholds of the pre-qualification for performing a capture SHALL be documented by the vendor.
- **•** If the acquisition software allows multiple thresholds for pre-qualification, it SHALL be configurable by the system administrator.
- **•** In case further requirements demand for an export of the uncompressed fingerprint image data BMP SHALL be used as image format.

#### **4.2.2.2. Recommendations**

In order to prevent unwanted duplicate acquisitions of the same fingers or slaps, the software SHOULD start the acquisition process not before the fingers from a previous acquisition have been removed from the sensor surface.

#### <span id="page-24-1"></span>**4.2.3. FM AS-FP-SLP**

This Function Module describes the requirements and interfaces for acquisition software for four finger slap scanners running in slap acquisition mode.

#### **4.2.3.1. Requirements**

- **•** It SHALL be classified by software whether the left or right hand slap has been acquired. Thumb clas sification is NOT REQUIRED. This MAY be achieved by using the acquired fingerprint images or with the help of further sensors or images (e.g. surveillance) if available.
- **•** The classification SHALL have a performance of at least 99% i.e. 99% of all left hand slaps SHALL be correctly classified as left hand slaps and 99% of all right hand slaps SHALL be correctly classified as right hand slaps.
- **•** In case the classification can return more than two possible results, e.g. "left", "right", or "unknown", a clas sification threshold SHALL be configurable.
- **•** It SHALL be configurable to switch the classification off or to only use the classification result information for evaluation purposes.

#### <span id="page-25-0"></span>**4.2.4. FM AS-FP-ROLL**

This Function Module describes the requirements and interfaces for Acquisition Software scanners sup porting rolled fingerprint capture.

#### **4.2.4.1. Requirements**

The acquisition software SHALL support the of rolled fingerprints. Therefore, following requi rements apply:

- 1. The captured fingerprint image SHALL depict the fingerprint from nail to nail.
- 2. The captured fingerprint image SHALL depict a faithful reproduction of the fingerprint, especially in the areas where the rolled fingerprint overlaps with the corresponding plain print.
- 3. Uniform Depiction
	- a. The captured fingerprint image SHALL NOT depict visible distortion or interruptions.
	- b. The captured fingerprint image SHALL NOT depict puzzle effects such that parts of the fingerprint image are displaced from their actual position.
- 4. Clear Depiction
	- a. The captured fingerprint image SHALL clearly depict friction ridges and ridge pattern.
	- b. The captured fingerprint image SHALL NOT depict blurring and smearing. Blurring also smea ring SHALL be detected by the acquisition software. If any blurring or smearing is detected, a warning SHALL be shown to the operator. The acquisition software NOT perform any correction con cerning the blurring and smearing.
	- c. If features exists for the given fingerprint:
		- i. The captured fingerprint image SHALL clearly depict features.
		- ii. If loop features exists for the given fingerprint: The captured fingerprint image SHALL clearly de pict loop features (core and delta).
	- d. The captured fingerprint image SHALL clearly depict existing features at the border zone of the image.
- 5. Complete Fingerprint
	- a. The captured fingerprint image SHALL depict the fingerprint's upper part.
	- b. The captured fingerprint image SHALL depict the fingerprint's core area with ridge lines.
	- c. If delta features exists for the given fingerprint: The captured fingerprint image SHALL depict fin gerprints delta features.
	- d. The captured fingerprint image SHALL depict the fingerprint's baseline (bottom area).
- 6. The captured fingerprint image SHALL be unrotated. Thus, the vertical axis of the fingerprint depicted in the captured image SHALL be in parallel with the fingerprint image's vertical axis.
- 7. The captured fingerprint image provided by Acquisition Software SHALL meet the criteria of fingerprints as described in [\[BIB\\_ISO\\_FINGER\].](#page-46-7) The requirements according to [Table 4.2](#page-25-1) are MANDATORY.
- 8. The acquisition software SHALL detect and provide information about issues while rolling a finger which affect the quality of captured fingerprint. Those information SHALL be considered as hardware repor ted issues in the capture process, see relevant [PAP](#page-45-7).

<span id="page-25-1"></span>

| Setting Level | Scan Resolution Pixels/Centi<br>meter (ppcm) | Scan Resolution Pi<br>xels/Inch (ppi) | Pixel Depth<br>(bits) | Dynamic Ran<br>ge (Grey Levels) | Certification |
|---------------|----------------------------------------------|---------------------------------------|-----------------------|---------------------------------|---------------|
| 31            | 197                                          | 500                                   | 8                     | 200                             | EFTS/F        |

| Setting Level | Scan Resolution Pixels/Centi<br>meter (ppcm) | Scan Resolution Pi<br>xels/Inch (ppi) | Pixel Depth<br>(bits) | Dynamic Ran<br>ge (Grey Levels) | Certification |
|---------------|----------------------------------------------|---------------------------------------|-----------------------|---------------------------------|---------------|
| 41            | 394                                          | 1000                                  | 8                     | 200                             | EFTS/F        |

**Table 4.2** Image Acquisition Settings Levels

### <span id="page-26-0"></span>**4.3. FM Category Biometric Image Processing**

The Function Module [Biometric Image Processing \(BIP\) provides the extraction of all relevant biometric in](#page-45-17) formation from the data which is provided by the acquisition hardware or the acquisition software layer. Thus, a proprietary data block is transformed to a digital image of a biometric characteristic. In general, specific image processing for biometric characteristics is addressed here.

### <span id="page-26-1"></span>**4.3.1. FM BIP-FI-DC-HQ**

This Function Module describes requirements and interfaces for Biometric Image Processing with respect to the output of digital cameras to obtain a high quality facial image that fulfils the ISO requirements.

#### **4.3.1.1. General Requirements**

As a result of the image processing of this module, a facial image SHALL be compliant to the requirements of full frontal images specified in [\[BIB\\_ISO\\_FACE\]](#page-46-6). The minimum distance between both eyes for capture positions of the applicant in the preferred area of the camera range SHALL be at least 120 pixel.

The image processing SHALL enclose cropping the facial image, resulting in images with a height/width ratio of 4:3. The general requirements for the image cropping in [Table 4.3](#page-26-2) SHALL apply to all images if no dedicate requirements are defined for a given use case in this Function Module. If the image is smaller than described in [Table 4.3](#page-26-2) it SHALL NOT be rescaled.

Depending on the requirements of the modules of [Section 4.12,](#page-43-0) multiple differently cropped versions of the image might be created at this step of image processing.

<span id="page-26-2"></span>

| Criterion    | Value | Unit  |
|--------------|-------|-------|
| Image height | 1600  | Pixel |
| Image width  | 1200  | Pixel |

**Table 4.3** Requirements for the Size of Facial Images

#### **4.3.1.2. Requirements GSAT Transactions**

Requirements in [Table 4.3](#page-26-2) SHALL NOT apply for [German Standard for AFIS Transactions Version 3 \(GSAT3\)](#page-45-18) transactions. The requirements in [Table 4.4](#page-26-3) SHALL apply to images used in [GSAT3](#page-45-18) transactions.If the image is smaller than described in [Table 4.4](#page-26-3) it SHALL NOT be rescaled.

Note, the requirements regarding the image resolution for [GSAT3](#page-45-18) transactions of [Table 4.4](#page-26-3) MAY be outdated. If the current version of [\[BIB\\_GSAT3\]](#page-46-5) requires a different resolution the image resolution of [\[BIB\\_GSAT3\]](#page-46-5) SHALL be applied instead.

<span id="page-26-3"></span>

| Criterion    | Value | Unit  |
|--------------|-------|-------|
| Image height | 800   | Pixel |
| Image width  | 600   | Pixel |

**Table 4.4** Requirements for the Size of Facial Images in GSAT Transactions

#### **4.3.1.3. Requirements on Printing**

If the image is also used for printing to the target size of 45mm x 35mm, it SHALL be cropped equidistantly from the original 4:3 aspect ratio.

Note that for the purpose of biometric processing, the 45:35 image SHALL NOT be considered any further.

#### <span id="page-27-1"></span>**4.3.2. FM BIP-FP-APP**

This Function Module describes requirements and interfaces for the biometric image processing to provide up to four single finger images for the subsequent reference storage or biometric comparison.

#### **4.3.2.1. Requirements**

- **•** The resolution of the fingerprint image has to be 500 ppi or 1000 ppi corresponding to the certification requirements of [\[BIB\\_ISO\\_FINGER\]](#page-46-7) and, therefore, MAY differ from the scan resolution.
- **•** Depending on the call, as many individual fingerprints as requested SHALL be extracted from the input image and provided as single fingerprints.

Note: Segmentation for single finger scanners is OPTIONAL.

For this segmentation process, the following requirements SHALL be fulfilled:

- **•** ability to accept fingerprints which are rotated in the same direction up to 45 degrees
- **•** in the same direction rotated fingerprints have to be corrected to be vertical
- **•** segment the first part over the finger (fingertip)
- **•** segmentation has to occur on uncompressed data
- **•** Fingerprint images SHALL NOT be upscaled. If the targeted system or database requires fingerprint images of higher size than captured the fingerprint image SHALL be evenly surrounded with white pixels to reach the desired size.

### <span id="page-27-0"></span>**4.4. FM Category Quality Assessment**

The Function Module [Quality Assessment contains all kinds of mechanisms and procedures to check the qua](#page-45-6) lity of the biometric data or to select the best quality data out of multiple instances.

#### <span id="page-27-2"></span>**4.4.1. FM QA-FI-GENERIC**

This Function Module describes requirements and interfaces for software that is used for quality assessment of digital images to ensure compliance with [\[BIB\\_ISO\\_FACE\].](#page-46-6)

#### **4.4.1.1. Requirements**

#### **4.4.1.1.1. General Requirements**

The [QA](#page-45-6) module is used for the software-based automatic check of the conformance of the picture to [\[BIB\\_ISO\\_FACE\]](#page-46-6) after the digitisation. Thereby, the geometric properties of the picture as well as the digital parameters of the image are analysed and rated.

The standard which is relevant for the quality of facial images [\[BIB\\_ISO\\_FACE\] hierarchically describes requi](#page-46-6) rements for the facial images. In the following, full frontal images are expected.

The [QA](#page-45-6) module SHALL analyse and evaluate all of the quality criteria listed in [Table 4.5](#page-28-0). For the criteria marked with "M", the quality values SHALL be provided while quality values for the criteria marked with "O" MAY be provided in the defined format according to the respective criteria.

A criterion is fulfilled if its calculated value is in the given threshold boundaries.

Based on the results of all provided quality criteria the [QA](#page-45-6) module SHALL reject or approve the picture. The total result is true if every single quality criteria is fulfilled.

The [QA](#page-45-6) module SHALL provide an interface for conformance testing where a single image can be processed and the calculated values and configuration data are returned. The image type to process depends on the image type requirements of the application profile to implement.

The [QA](#page-45-6) module SHOULD operate on cropped images retrieved from the image processing according to [FM](#page-26-0) [Category Biometric Image Processing.](#page-26-0)

<span id="page-28-0"></span>

| ID               | Criterion                                      | ISO-Ref., compare<br>[BIB_ISO_FACE] | Mandatory / Optional | Unit/Range               |
|------------------|------------------------------------------------|-------------------------------------|----------------------|--------------------------|
| Pose of the head |                                                |                                     |                      |                          |
| 1.1              | Yaw, neck axis                                 | 7.2.2                               | O                    | Degrees                  |
| 1.2              | Pitch, ear axis                                | 7.2.2                               | O                    | Degrees                  |
| 1.3              | Roll, nose axis                                | 7.2.2                               | M                    | Degrees                  |
|                  | Facial expression                              |                                     |                      |                          |
| 2.1              | Neutral expression                             | 7.2.3                               | O                    | Arbitrary units          |
| 2.2              | Mouth closed                                   | 7.2.3                               | M                    | Arbitrary units          |
| 2.3              | No raised eyebrows                             | 7.2.3                               | O                    | Arbitrary units          |
| Eyes             |                                                |                                     |                      |                          |
| 3.1              | Eyes open                                      | 7.2.3                               | O                    | Arbitrary units          |
| 3.2              | No occlusion (glasses,<br>hair, eye patch)     | 7.2.11 7.2.12                       | O                    | Arbitrary units          |
| 3.3              | Eyes looking to the ca<br>mera                 | 7.2.3                               | O                    | Arbitrary units          |
| Background       |                                                |                                     |                      |                          |
| 4.1              | Uniformity (plainness,<br>no textures, colour) | 7.2.6 A.2.4.3                       | O                    | Arbitrary units          |
| 4.2              | No shadows                                     | 7.2.6 A.2.4.2                       | O                    | Arbitrary units          |
| 4.3              | No further people / ob<br>jects                | 7.2.4 A2.3                          | O                    | Arbitrary units          |
| Geometry         |                                                |                                     |                      |                          |
| 5.1              | Image height                                   | 8.3.5 A.3.1.1 A.3.2.1               | M                    | In pixel                 |
| 5.2              | Image width                                    | 8.3.4 A.3.1.1 A.3.2.1               | M                    | In pixel                 |
| 5.3              | Ratio: Head width /<br>image width             | 8.3.4                               | M                    | As ratio between 0 and 1 |
| 5.4              | Ratio: Head height /<br>image height           | 8.3.5                               | M                    | As ratio between 0 and 1 |
| 5.5              | Vertical position of the<br>face               | 8.3.3                               | M                    | As ratio between 0 and 1 |
| 5.6              | Horizontally centred<br>face                   | 8.3.2                               | M                    | As ratio between 0 and 1 |
| 5.7              | Eye distance                                   | 8.4.1 A3.1.1                        | M                    | In pixel                 |
| Subject lighting |                                                |                                     |                      |                          |
| 6.1              | Equally distributed<br>lighting                | 7.2.7                               | O                    | Arbitrary units          |

| ID  | Criterion                                              | ISO-Ref., compare<br>[BIB_ISO_FACE] | Mandatory / Optional | Unit/Range                                                                                                                                                          |
|-----|--------------------------------------------------------|-------------------------------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 6.2 | No shadows over the<br>face nor in the eye-so<br>ckets | 7.2.8 7.2.9                         | O                    | Arbitrary units                                                                                                                                                     |
| 6.3 | No hot spots on skin                                   | 7.2.10                              | O                    | Arbitrary units                                                                                                                                                     |
| 6.4 | No effects on glasses                                  | 7.2.11                              | O                    | Arbitrary units                                                                                                                                                     |
|     | Photographic requirements                              |                                     |                      |                                                                                                                                                                     |
| 7.1 | Proper exposure                                        | 7.3.2                               | M                    | Arbitrary units                                                                                                                                                     |
| 7.2 | Focus and depth of field                               | 7.3.3                               | M                    | Arbitrary units                                                                                                                                                     |
| 7.3 | No unnatural colours                                   | 7.3.4                               | O                    | Arbitrary units                                                                                                                                                     |
| 7.4 | No red eyes                                            | 7.3.4                               | O                    | Arbitrary units                                                                                                                                                     |
| 7.5 | Colour space                                           | 7.4.2.3                             | M                    | According to [BIB_ISO_FACE]<br>using Decimal notation (e.g.<br>"1" for RGB-24bit, "2" for<br>YUV422 or "3" for 8bit-grey<br>scale and "0" for unknown or<br>errors) |
| 7.6 | Grey scale density and<br>colour saturation            | 7.4.2.1 7.4.2.2                     | M                    | Counted numbers of intensi<br>ty values existing within the<br>image                                                                                                |

**Table 4.5** Mapping of Relevant Quality Criteria

#### **4.4.1.1.2. Identification of the Best Capture**

When multiple facial images and their corresponding set of quality metrics are present, the best capture of the list SHALL be identified in an automated manner as described in the following[1](#page-29-1) :

- 1. If exactly one facial image conforms to more mandatory criteria than all other images, this image is chosen.
- 2. If more than one facial image is conform to more mandatory criteria than all other facial images, the facial image fulfilling the most optional criteria SHALL be chosen.
- 3. If more than one facial image is conform to more mandatory and optional criteria than all other facial images, the most recent facial image within this selection SHALL be chosen. If no timestamp is available, a random selection MAY be applied among the facial images fulfilling the most criteria.

#### <span id="page-29-0"></span>**4.4.2. FM QA-FI-ARE**

This Function Module describes requirements and interfaces for software that is used for quality assessment of digital images within the context of alien register enrolment to ensure compliance with [\[BIB\\_ISO\\_FACE\].](#page-46-6)

#### **4.4.2.1. Requirements**

The threshold requirements of [Table 4.6](#page-29-2) SHALL be in place within the context of alien register enrolment. These thresholds relate to the generic quality criteria of [FM QA-FI-GENERIC.](#page-27-2)

<span id="page-29-2"></span>

| ID                                           | Criterion      | Minimum | Maximum | Unit/Range |
|----------------------------------------------|----------------|---------|---------|------------|
| Image ratio 4:3 (Image height / image width) |                |         |         |            |
| 1.1                                          | Yaw, neck axis | -5      | 5       | Degrees    |

<span id="page-29-1"></span>1 Note that this is a description of the automated selection of the best capture among a list of facial images. Operators may always decide otherwise during the process (veto).

| ID  | Criterion                         | Minimum | Maximum | Unit/Range                                                                                                                                                        |
|-----|-----------------------------------|---------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.2 | Pitch, ear axis                   | -5      | 5       | Degrees                                                                                                                                                           |
| 1.3 | Roll, nose axis                   | -8      | 8       | Degrees                                                                                                                                                           |
| 5.1 | Image height                      | 800     | 1600    | In pixel                                                                                                                                                          |
| 5.2 | Image width                       | 600     | 1200    | In pixel                                                                                                                                                          |
| 5.3 | Ratio: Head width / image width   | 0,5     | 0,75    | As ratio between 0 and 1                                                                                                                                          |
| 5.4 | Ratio: Head height / image height | 0,6     | 0,9     | As ratio between 0 and 1                                                                                                                                          |
| 5.5 | Vertical position of the face     | 0,3     | 0,5     | As ratio between 0 and 1                                                                                                                                          |
| 5.6 | Horizontally centred face         | 0,45    | 0,55    | As ratio between 0 and 1                                                                                                                                          |
| 5.7 | Eye distance                      | 120     | -       | In pixel                                                                                                                                                          |
| 7.5 | Colour space                      | -       | -       | According to [BIB_ISO_FACE]<br>using Decimal notation (e.g. "1" for<br>RGB-24bit, "2" for YUV422 or "3"<br>for 8bit-grey scale and "0" for unk<br>nown or errors) |

**Table 4.6** Quality Threshold Requirements for Facial Images for Alien Register Enrolment

Please note, that for criterion 7.5 (Colour space) there still might be facial images from [CIR](#page-45-2) that are greyscale images.

#### <span id="page-30-0"></span>**4.4.3. FM QA-FI-PG**

This Function Module describes requirements for a photo guideline that is used for Quality Assessment.

#### **4.4.3.1. Recommendations**

If the [QA](#page-45-6) is to be performed by a person, visual tools like a photo guideline MAY be used for support.

If the visual check is conducted with the photo guideline, it always SHALL be done even if the checks with the photo template and/or the [QA](#page-45-6) software will be performed afterwards. A recent picture is required according to [\[BIB\\_ISO\\_FACE\]](#page-46-6) .

If these basic criteria are not met, the image SHALL be rejected without any further checks by the software or the photo template.

In the case of the photo guideline, the following criteria SHALL be described, preferably using sample images for compliant and non compliant images (compare [\[BIB\\_ISO\\_FACE\]](#page-46-6) ):

- **•** frontal pose
- **•** neutral expression
- **•** mouth closed
- **•** eyes open
- **•** no occlusion (glasses, hair, eye patch)
- **•** eyes looking to the camera
- **•** background uniformity (plainness, no textures, colour)
- **•** no shadows
- **•** no head coverings
- **•** no further people / objects
- **•** equally distributed lighting
- **•** no shadows over the face
- **•** no shadows in the eye sockets
- **•** no hot spots on skin
- **•** no effects from glasses
- **•** correct exposure
- **•** correct contrast
- **•** focus and depth of field
- **•** no unnatural colours
- **•** no red eyes

### <span id="page-31-0"></span>**4.4.4. FM QA-FP-APP**

This Function Module describes requirements for the quality assessment of plain or rolled fingerprints inclu ding quality assessment of single fingerprint, respectively slap and selection of the best quality image out of multiple instances.

#### **4.4.4.1. Requirements**

#### **4.4.4.1.1. Quality Algorithm**

As quality algorithm, the latest version of [NIST Fingerprint Image Quality 2.2 \(NFIQ2.2\)](#page-45-19) [\[BIB\\_NFIQ2.2\]](#page-46-11) SHALL be used, and therefore, images with 1000 ppi SHALL be resampled to 500 ppi before application of [NFIQ2.2](#page-45-19). Note, that the resampled image SHALL be used for [NFIQ2.2](#page-45-19) only. As resulting quality value, the output value of [NFIQ2.2](#page-45-19) in the integer range of [0,100] SHALL be used. In the case of failure, the returned error code 255 indicates that a computation was not successful and the resulting quality value SHALL be returned as the result, as described in [Section 4.11.1](#page-41-1).

#### **4.4.4.1.2. Quality Evaluation Process for a Slap or Single Fingerprint**

In case a single captured fingerprint, respectively slap is passed, the [QA](#page-45-6) SHALL be performed as described in the following. Beforehand, the fingerprints of the passed capture SHALL be segmented (considering missing fingers). Note, that in verification applications, a [QA](#page-45-6) is not conducted. Thus, every slap capture is considered sufficient and no thresholds are specified here. Skipping the [QA](#page-45-6) is expected to accelerate the overall process. OPTIONALLY, a [QA](#page-45-6) can be performed.

- 1. For each segmented fingerprint *FA;j* of a passed capture *A*, a quality value *QA;j* is calculated with *j 2* 1*; :::;* 10 (up to 4 fingers in one slap) representing the specific finger code according to [\[BIB\\_ISO\\_FIN](#page-46-7) [GER\].](#page-46-7)
- 2. The resulting quality value is compared with the defined threshold *T Hj* for this finger. The application specific thresholds as defined in the following section apply.
- 3. In case all of the fingerprint qualities reach the specified threshold (i.e. *8j; QA;j ¸ T Hj* ), the boolean infor mation *b* = 1 indicates a successful capture.
- 4. In case one or more fingerprints do not reach the threshold (i.e. *9j; QA;j < T Hj* ), the boolean information *b* = 0 indicates insufficient quality of the capture.
- 5. For the segmented fingerprint *FA;j* the corresponding parameter set *PA;j* is compiled and returned.
- 6. As a result of the [QA](#page-45-6) process, the following values are returned to the calling process:
	- a. the boolean information *b*
	- b. the parameter set *PA* = *QA;j ; :::; QA;l* with *j; l 2* 1*; :::;* 10 representing the specific finger code

#### **4.4.4.1.3. Identification of the Best Capture out of Multiple Captures**

When multiple captures *Ai ;i 2* 1*; :::; n* and their corresponding set of segmented fingerprints *FAi ;j* with *j 2* 1*; :::;* 10 representing the specific finger code according to [\[BIB\\_ISO\\_FINGER\]](#page-46-7) are passed, the best of the captures SHALL be identified as described in the following section:

- 1. For each segmented fingerprint *FAi ;j* of a passed capture *Ai* , the quality value *QAi ;j* is calculated with re presenting the specific finger code according to [\[BIB\\_ISO\\_FINGER\]](#page-46-7).
- 2. The captures are ranked according to the quality values of the fingerprints according to the following (lexicographical) order. The highest ranked capture is considered as the capture yielding the best quality.
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
- 3. As a result of the [QA](#page-45-6) process, the following values are returned:
- a. the identifier *i* representing the capture yielding the best quality
- b. the parameter set *PA* = *QAi;j ; QAi;l* with *j; l 2* 1*; :::*10.

#### **4.4.4.1.4. Thresholds for Plain Fingerprints for Enrolment Purposes**

The following thresholds as indicated in [Table 4.7](#page-33-0) apply when fingerprints are captured plain for enrolment purposes. Note, the thresholds in [Table 4.7](#page-33-0) do not apply to plain captured fingerprint in enrolment scenarios where the plain fingerprints are captured for control purpose of rolled fingerprints. In that case, thresholds as indicated in [Table 4.8](#page-33-1) apply for the plain fingerprints.

<span id="page-33-0"></span>

| Finger Position     | Finger Code | NFIQ2.2 Threshold |
|---------------------|-------------|-------------------|
| Right thumb         | 1           | 30                |
| Right index finger  | 2           | 30                |
| Right middle finger | 3           | 20                |
| Right ring finger   | 4           | 10                |
| Right little finger | 5           | 10                |
| Left thumb          | 6           | 30                |
| Left index finger   | 7           | 30                |
| Left middle finger  | 8           | 20                |
| Left ring finger    | 9           | 10                |
| Left little finger  | 10          | 10                |

**Table 4.7** Thresholds for Plain Fingerprints for Enrolment Purposes

#### **4.4.4.1.5. Thresholds for Plain Control Fingerprints and Fingerprints used for Identification Searches**

The following thresholds as indicated in [Table 4.8](#page-33-1) apply when fingerprints are captured plain for the purpose of control slaps (used for comparison with rolled prints) or use in identification searches. Note, the thres holds in [Table 4.8](#page-33-1) do apply to plain captured fingerprint in enrolment scenarios where the plain fingerprints are captured for control purpose of rolled fingerprints.

<span id="page-33-1"></span>

| Finger Position     | Finger Code | NFIQ2.2 Threshold |
|---------------------|-------------|-------------------|
| Right thumb         | 1           | 20                |
| Right index finger  | 2           | 20                |
| Right middle finger | 3           | 20                |
| Right ring finger   | 4           | 10                |
| Right little finger | 5           | 10                |
| Left thumb          | 6           | 20                |
| Left index finger   | 7           | 20                |
| Left middle finger  | 8           | 20                |
| Left ring finger    | 9           | 10                |
| Left little finger  | 10          | 10                |

**Table 4.8** Thresholds for Plain Control /Identification Fingerprints

#### **4.4.4.1.6. Thresholds for Rolled Fingerprints**

The following thresholds as indicated in [Table 4.9](#page-34-2) apply when fingerprints are captured rolled for enrolment purposes.

<span id="page-34-2"></span>

| Finger Position     | Finger Code | NFIQ2.2 Threshold |
|---------------------|-------------|-------------------|
| Right thumb         | 1           | 20                |
| Right index finger  | 2           | 15                |
| Right middle finger | 3           | 15                |
| Right ring finger   | 4           | 10                |
| Right little finger | 5           | 5                 |
| Left thumb          | 6           | 20                |
| Left index finger   | 7           | 15                |
| Left middle finger  | 8           | 15                |
| Left ring finger    | 9           | 10                |
| Left little finger  | 10          | 5                 |

**Table 4.9** Thresholds for Rolled Fingerprints

### <span id="page-34-0"></span>**4.5. FM Category Presentation Attack Detection**

The objective of the Function Module [Presentation Attack Detection](#page-45-10) is to avoid presentations with the goal to subvert an enrolment, verification of identification process.

#### <span id="page-34-1"></span>**4.5.1. FM PAD-FP-APP**

This Function Module describes requirements for [PAD](#page-45-10) in the context of acquisition biometric charac teristics of fingerprints.

#### **4.5.1.1. Requirements**

#### **4.5.1.1.1. General Requirements**

The capture system SHALL contain a [PAD](#page-45-10) subsystem according to [\[BIB\\_ISO\\_PAD\\_1\] detecting spoofing at](#page-46-12) tempts using artefacts by which an attacker is trying to establish a different biometric characteristic as probe in the verification or identification process.

The [PAD](#page-45-10) subsystem MAY consist of hardware and software (e.g. the used fingerprint scanner have addi tional sensors designed for this purpose).

According to the used fingerprint scanner, [PAD](#page-45-10) subsystem SHALL be able to detect artefact classes listed in the following:

- **•** Fingertips, created in different thicknesses
- **•** Single fingers (massive)

The [PAD](#page-45-10) subsystem SHALL be able to detect all typical artefact material types listed in the following:

- **•** Artefacts created from different kinds of silicon
- **•** Artefacts created from different kinds of latex
- **•** Artefacts created from different kinds of gelatine
- **•** Artefacts created from different kinds of wood glue
- **•** Artefacts created from different kinds of window painting

**•** Artefacts created from different kinds of paper

each in different colourings.

Under optimal testing conditions, the [PAD](#page-45-10) subsystem SHALL feature a false-alarm-rate of 2% maximum when tested with bona fide biometric subjects with generally good quality fingerprints. This rate is monitored via logfiles analysis within the operational environment. If this rate is significantly exceeded, any certification that may have been issued might be re-evaluated (depending on application context) [2](#page-35-0) .

Also, the detection subsystem SHALL be adequate to the usage setting in correspondence with the security requirements in question. The performance MAY be described by a risk analysis for every considered attack type. The current version of [\[BIB\\_ISO\\_PAD\\_3\]](#page-46-13) SHALL be taken into account.

The [PAD SHALL be conducted both in supervised acquisition scenarios, e.g. a counter scenario, and un](#page-45-10) supervised acquisition scenarios, e.g. in [self-service system \(SSS\)](#page-45-20) scenarios. Thereby, the [PAD SHALL be con](#page-45-10) ducted for all acquisition purposes, e.g. enrolment, identification and verification.

#### **4.5.1.1.2. Integration Requirements**

The [PAD](#page-45-10) subsystem SHALL be independent of the regular capture subsystem.

It SHALL signal its detection results in the form of a [PAD](#page-45-10) score for each finger individually. Additionally, an overall result SHALL be returned to the calling application.

The score for each finger SHALL be a normalized as double in the range [0,1] using at least ten uniformly distributed interim values, where 0 indicates bona fide and 1 presentation attack. A binary score SHALL NOT be used (e.g. True or False, 1 or 0). The [PAD](#page-45-10) subsystem SHALL additionally provide detailed information about the scores of the [PAD.](#page-45-10)

The overall result SHALL be a boolean value (e.g. True or False). The value SHALL be true, if any of the fingers individual result triggers a [PAD](#page-45-10) alarm.

Even if the Function Module is used within a comparison scenario, the detection result SHALL be signalled in any case, independent from any biometric comparison score. Also, the omission of the detection result SHALL be signalled in any case.

The [PAD](#page-45-10) result SHALL correspond to the respective finger capture attempt.

Note, that an image of the fingerprint or slap in question SHALL be acquired independently of a possible PAD alarm.

#### **4.5.1.1.3. Maintenance Requirements**

As new technologies and new attack mechanisms are developed over time, the [PAD](#page-45-10) subsystem SHALL be updated and checked whenever necessary, so it stays capable against old and new attacks and attack types.

#### **4.5.1.1.4. Certification Requirements**

To ensure comparable performance of presentation attack detection subsystems, the system SHALL be certi fied either under the Common Criteria Agreement according to one of following Protection Profiles:

- **•** BSI-CC-PP-0063-2010: Fingerprint Spoof Detection Protection Profile (FSDPP)
- **•** BSI-CC-PP-0062-2010: Fingerprint Spoof Detection Protection Profile based on Organisational Security Policies (FSDPP\_OSP)
- **•** BSI-CC-PP-0118-2022: Common Criteria Protection Profile Biometric Mechanisms Protection Profile (BMPP), Version 2.0, base PP and at least the functional package PAD

or according to BSI TR-03122: Conformance Test Specification for Technical Guideline TR-03121 - Biometrics for Public Sector Applications, respectively this technical guideline. Note that the PAD certification according

<span id="page-35-0"></span><sup>2</sup> Note that during certification a relaxed false-alarm-rate is tested. The requirement of the rate specified in this Function Module is tested on operational collected data only.

to BSI TR-03122 is preliminary and still subject to amendments. Anticipating certification under this Function Modul MAY only be realised with the permission of the Federal Ministry of the Interior and Community and upon consultation with the Federal Office for Information Security.

### <span id="page-36-6"></span><span id="page-36-0"></span>**4.6. FM Category Compression**

The objective of the Function Module [Compression \(COM\)](#page-45-21) is to keep the biometric data within a feasible size without losing too much quality for a biometric verification or identification.

### <span id="page-36-1"></span>**4.6.1. FM COM-FI-GENERIC**

The following requirements are generic and apply to all [FMs](#page-45-5) regarding compression of facial images.

#### **4.6.1.1. Requirements**

Multiple lossy compressions of the facial image data SHALL NOT take place with the exception of the initial capture by a digital camera whenever that camera does not support uncompressed image capture.

#### <span id="page-36-2"></span>**4.6.2. FM COM-FI-JPG**

This Function Module describes requirements and interfaces for the compression of images using the JPEG format for reference storage.

#### **4.6.2.1. Requirements**

The compression method for facial images SHALL be JPEG (compare [\[BIB\\_ISO\\_10918-1\]](#page-46-14)). The compression algorithm SHALL be parametrized in such a way that the application specific requirements as listed in [Ta](#page-36-4) [ble 4.10](#page-36-4) are met by the resulting compressed image. Multiple lossy compressions SHALL NOT take place.

<span id="page-36-4"></span>

| Minimum File Size                                 | Recommended Com<br>pression Ratio | Maximum Compressi<br>on Ratio |
|---------------------------------------------------|-----------------------------------|-------------------------------|
| Small size image (600x800 /622x800 pixel)         |                                   |                               |
| 35 KiB                                            | 5:1                               | 15:1                          |
| Standard size image (1200x1600 / 1244x1600 pixel) |                                   |                               |
| 100 KiB                                           | 5:1                               | 15:1                          |

**Table 4.10** Requirements to Compression Using JPEG Format

For conformance the implementation encapsulating the compression has to provide an interface that accepts predefined test data instead of performing the regular process.

### <span id="page-36-3"></span>**4.6.3. FM COM-FP-WSQE**

This Function Module describes requirements and interfaces for the compression of fingerprint images by [Wavelet Scalar Quantisation \(WSQ\)](#page-45-22) method.

#### **4.6.3.1. Requirements**

[WSQ](#page-45-22) SHALL be used as compression method for fingerprint images. A bit rate of 0.75 SHALL be used as compression parameter. This is equivalent to a compression factor of approximately 15:1[3](#page-36-5) (according to [\[BIB\\_ISO\\_FINGER\]\)](#page-46-7). The implementation of the used [WSQ](#page-45-22) algorithm SHALL be certified by the FBI and SHALL be referenced by the respective certificate number (coded in the [WSQ](#page-45-22) header). The certified [WSQ](#page-45-22) im plementation SHALL be version 3.1 and SHALL base on NBIS Version 5.0. Multiple lossy compressions SHALL NOT take place.

<span id="page-36-5"></span><sup>3</sup> For estimation of compression factor it is allowed to crop to the minimum size containing the fingerprint defined if a sensor is used with a larger capturing area than this minimum.

If the resulting effective compression rate *C* does not fulfil the requirement of [Equation 4.3](#page-37-4) for this particular case only a stronger or weaker compression *C* SHALL be used.

$$10:1 \ll = C \ll = 20:1\tag{4.3}$$

<span id="page-37-4"></span>Therefore, an iterative process SHALL be applied, which results in an image file with an effective compression rate within the defined range, refer to [Equation 4.3](#page-37-4).

<span id="page-37-5"></span>The effective compression rate SHALL be calculated by [Equation 4.4](#page-37-5) where *Swsq* is the size in bytes of the resulting [WSQ](#page-45-22) file and *Sraw* is the size in bytes of the raw fingerprint image.

$$C = \frac{S\_{raw}}{S\_{wsq}}\tag{4.4}$$

### <span id="page-37-0"></span>**4.7. FM Category Operation**

Within the Function Module [Operation \(O\),](#page-45-23) the working process is specified for the respective operator. All steps that have to be executed are described sequentially and in more detail. This also includes descriptions of how to proceed in error cases.

#### <span id="page-37-1"></span>**4.7.1. FM O-FI-ALL**

This Function Module describes requirements to be observed by the operator who handles the facial image acquisition process. This includes the full working process.

#### **4.7.1.1. Requirements**

- **•** If the software based [QA](#page-45-6) rejects the image, the operator SHALL have the option to give a veto in order to release the image despite a negative software decision and vice versa.
- **•** The operator SHALL be responsible for an adequate cleanliness of all capture hardware components.

#### **4.7.1.2. Recommendations**

OPTIONALLY, the operator can use the photo guideline.

#### <span id="page-37-2"></span>**4.7.2. FM O-FI-DC**

This Function Module describes requirements to be observed by the operator who handles the facial image acquisition process with a digital camera.

#### **4.7.2.1. Requirements**

- **•** The operator SHALL ensure that different environmental lighting conditions caused by direct or indirect sunlight and different seasons of the year SHALL NOT influence the proper and uniform lighting of the captured facial image.
- **•** Direct and cross irradiation of lighting SHALL be avoided by the operator.

#### <span id="page-37-3"></span>**4.7.3. FM O-FP-ALL**

This Function Module describes requirements to be observed by the operator who handles the acquisition process of fingerprint images.

#### **4.7.3.1. Requirements**

#### **4.7.3.1.1. Operation of Devices**

**•** The operator SHALL be responsible for an adequate cleanliness of all capture hardware components. Fin gerprint scanners SHALL be cleaned regularly to provide good probe images. **•** The fingerprint scanner SHALL be regularly calibrated (e.g. once a day), if the used tech nology requires such a calibration. The operator SHALL ensure that the sensor platen is clean before cali bration to reduce the risk of ghost images.

#### **4.7.3.1.2. Environmental Requirements**

- **•** The operator SHALL ensure that different environmental lighting conditions caused by direct or indirect sunlight and different seasons of the year SHALL NOT influence the scanner capture process.
- **•** Direct and cross irradiation of lighting on the sensor platen SHALL be avoided completely.

### <span id="page-38-0"></span>**4.8. FM Category User Interface**

It is the task of the [User Interface \(UI\)](#page-45-24) to display and visualise the respective information that is obtained from the underlying Function Modules.

#### <span id="page-38-1"></span>**4.8.1. FM UI-FI-OP**

This Function Module describes requirements for the user interface of the software displaying the result of the quality assessment and verification (if performed) of facial images to the operator.

#### **4.8.1.1. Requirements**

- **•** The current evaluated picture SHALL be displayed to the operator for the enrolment.
- **•** All criteria evaluated with the current value and threshold as well their relation: OK/NOK for every cri terion SHALL be displayed to the operator for the enrolment.
- **•** The summarised result OK/NOK for the current picture SHALL be displayed to operator enrol ment.
- **•** The provision of the veto power for the operator SHALL be shown to the operator for the enrolment:
	- **•** enforcement of OK for obvious reasons (e.g. disability)
	- **•** enforcement of OK without obvious reasons
	- **•** enforcement of NOK to overrule software based quality assessment
- **•** If [PAD](#page-45-10) was performed and a presentation attack was detected, a warning with the overall result SHALL be displayed to the operator. All facial images that have caused a PAD alarm SHALL be displayed to the operator as well. In addition, all facial images within an acquisition where at least one facial image caused a PAD alarm SHALL be displayed to the operator.

If verifications are performed[4](#page-38-3) :

- **•** Visual feedback of the verification process SHALL be provided for the operator. At least both images (live and reference) and the (Boolean) result of the verification SHALL be displayed to the operator.
- **•** If the verification fails, then the operator SHALL get access to at least one complete and coherent set of biometric samples and verification results corresponding to a single verification attempt. For instance, in case of verification of a live-captured facial image against a facial image from chip (Data Group 2) and [CIR](#page-45-2), such a complete set would consist of the live-captured facial image, the facial image extracted from chip, the facial image stored in the [CIR](#page-45-2), and both corresponding verification results of the live-captured facial image against the facial image from chip and the [CIR](#page-45-2) image.

#### <span id="page-38-2"></span>**4.8.2. FM UI-FP-BSJ**

This Function Module describes requirements for the user interface of the biometric subject for fingerprint acquisitions. The user interface MAY be e.g. monitors, buttons, pictograms or status lights.

<span id="page-38-3"></span><sup>4</sup> This is only the case if the application profile defines verification processes explicitly.

#### **4.8.2.1. Requirements**

The following requirements SHALL be met for the user interface:

- **•** An indicator showing the capture status and an indication when the capture process has finished SHALL be displayed to the biometric subject. The capture status SHALL include: Where to place the fingers, an indication of the scanning process and the feedback in case of mispositioning of fingers.
- **•** In an unsupervised scenario a visualisation which fingerprint or hand to place on the sensor SHALL be given, whereby in the case of a supervised scenario the visualisation MAY be given.

If [PAD](#page-45-10) was conducted: Neither the [PAD](#page-45-10) result nor [PAD](#page-45-10) score SHALL be displayed to the person whose finger prints are acquired. In a supervised acquisition scenario the process operator MAY be responsible for screen positioning, so that the [PAD](#page-45-10) result or the [PAD](#page-45-10) score is not displayed to the person whose fingerprints are acquired.

#### **4.8.2.2. Recommendations**

The following recommendations SHOULD be met for the user interface:

- **•** Graphics (e.g. buttons or pictograms) SHOULD use a uniform colour palette without utilizing clashing co lours.
- **•** The acquisition process SHOULD be displayed as real time feedback to the biometric subject (e.g. with the help of a feedback monitor).

#### <span id="page-39-0"></span>**4.8.3. FM UI-FP-OP**

This Function Module describes requirements for the user interface of software displaying live feed back and results of the fingerprint acquisition, [QA and control verification of fingerprint images to the ope](#page-45-6) rator.

#### **4.8.3.1. Requirements**

- **•** The user interface SHALL signal which fingerprints are expected for the current slap or fingerprint acqui sition such that the operator can guide the biometric subject to place the correct fingers on the fingerprint scanner.
- **•** Visual feedback of the fingerprint acquisition at least displaying of the final images SHALL be provided to the operator.
- **•** If a uniqueness check error occurs, the fingers involved in the unexpected successful comparisons SHALL be pictorially displayed to the operator and in case of a slap image, only the affected finger(s) SHALL be marked in the displayed image. In case a control verification was attempted and no successful comparison occurred during the control verification, a warning SHALL be displayed to the operator that the control verification was not successful.
- **•** The segmented single fingerprints SHALL be visualised to the operator identify potential failures in seg mentation. This can be realised by displaying the result containing up to ten segmented single fingerprints. In case the amount of captured fingerprints mismatches with the amount of expected fingers a warning SHALL be displayed to the operator.
- **•** If a slap acquisition is in place and a slap classifier is in use (and activated not only for evaluation purpose), a warning SHALL be displayed to the operator when the classification result mismatches with the expected slap of the current acquisition.
- **•** If [PAD](#page-45-10) was performed and a presentation attack was detected, a warning SHALL be displayed to the operator and displayed for each finger individually. An overall result SHALL also be displayed additionally.
- **•** The indication of the quality level SHALL be displayed to the operator.
- **•** The provision of the veto power for the operator SHALL be shown to the operator for the enrolment:
- **•** enforcement of OK for obvious reasons (e.g. disability)
- **•** enforcement of OK without obvious reasons
- **•** enforcement of NOK to overrule software based quality assessment

#### **4.8.3.2. Recommendations**

A live view from the fingerprint scanner SHOULD be displayed to operator during acquisi tion. This also includes live information, e.g. about the correct positioning of fingers on fingerprint scan ner or about the current quality level, that supports the operator guiding the biometric subject.

The user interface SHOULD show a graphical representation of the fingerprints that are expected for cur rent slap or fingerprint acquisition.

### <span id="page-40-0"></span>**4.9. FM Category Reference Storage**

The objective of the Function Module [Reference Storage \(REF\)](#page-45-25) is to store biometric data in a way that it can be used for reference purposes later on.

#### <span id="page-40-2"></span>**4.9.1. FM REF-FI-ARE**

This Function Module describes requirements how facial images are stored as reference data in the context of the Application Arrival Document.

#### **4.9.1.1. Requirements**

The facial image of an applicant SHALL be stored in the [CIR](#page-45-2) and made available immediately for further iden tification requests.

#### <span id="page-40-3"></span>**4.9.2. FM REF-FP-ARE**

This Function Module describes requirements how fingerprint images are stored as reference data within the context of the Application Arrival Document.

#### **4.9.2.1. Requirements**

The captured fingerprints of an applicant SHALL be stored in the [CIR](#page-45-2) and made available immediately for further identification requests.

### <span id="page-40-1"></span>**4.10. FM Category Biometric Comparison**

The Function Module [Biometric Comparison \(CMP\)](#page-45-26) encloses the mechanisms and algorithms to verify or identify an identity based on a 1:1 or 1:*n* biometric comparison between reference data and a current biometric probe (usually a live presented image) regardless of where the reference is stored (e.g. passport, identity card, [Automated Biometric Identification System \(ABIS\)](#page-45-27), database, ...).

It is RECOMMENDED that the verifications conducted during uniqueness checks comply with this [FM.](#page-45-5)

#### <span id="page-40-4"></span>**4.10.1. FM CMP-FP-CV**

This Function Module contains requirements for the control-verification of plain and rolled captured finger prints.

#### **4.10.1.1. Requirements**

A fingerprint verification algorithm SHALL be used for control-verification of the plain and rolled captured fingerprints intended for enrolment.

The used verification algorithm SHALL be configured at a security level (threshold) guaranteeing a maximum [false-match-rate \(FMR\)](#page-45-28) of at least 0,1 % (1/1000) at a [false-non-match-rate \(FNMR\)](#page-45-29) below 2 %. It SHALL be allowed to configure a threshold which allows stronger settings (lower [FMR](#page-45-28) and/or [FNMR\)](#page-45-29).

Furthermore, the overall system SHALL be calibrated for the security level set within this specific scenario of verification. The vendor of the verification algorithm SHALL provide calibration data based on the actual system performance.

Input data of the verification are the segmented plain and rolled captured fingerprints from the applicant. Output of the algorithm SHALL be a comparison score for both prints of each captured finger and the result of the verification depending on the configured threshold of the algorithm.

### <span id="page-41-3"></span><span id="page-41-0"></span>**4.11. FM Category Logging**

The Function Module [Logging \(LOG\)](#page-45-30) contains logging requirements. The requirements of this chapter and the requirements of the schema of information to log apply both.

#### <span id="page-41-1"></span>**4.11.1. FM LOG-ALL-GENERIC**

The Function Module Logging contains requirements as to which data has be logged for a specific appli cation.

#### **4.11.1.1. Requirements**

- **•** A transaction SHALL cover all information concerning one single biometric subject. Created IDs SHALL be unique globally. During the biometric process all data SHALL be gathered or created by the application.
- **•** Each transaction SHALL contain the generic process information about the system that are defined in ty pe.transaction. The exact semantic for the location of station is profile-dependent. See the specific profile for a refined definition. If the transaction is dependent or derived from another transaction the ID of the reference SHALL be set.
- **•** In case of abnormal termination the transaction or any its sub-processes, error code SHALL be log ged. The vendor SHALL provide a detailed list of all error codes used with complete semantic descriptions.
- **•** During the transaction performed enrolment processes SHALL be logged as Enrolment. In cases where the central system replies directly with enrolment status information the submit time SHALL be recorded. If any control verification is performed during enrolment the result SHALL be contained.
- **•** For identification processes the data defined in Identification SHALL be recorded. The list of candidates SHALL be contained if detailed scoring information is provided by the central system.
- **•** A verification processes SHALL be recorded based on the Verification element. Per verification all perfor med comparisons SHALL be included. For each comparison the vendor specific score as well thres hold SHALL be contained.

#### <span id="page-41-2"></span>**4.11.2. FM LOG-ALL-ARE**

This Function Module describes additional requirements and interfaces for the logging of process information for the application T TrArrival Attestation Document.

#### **4.11.2.1. Requirements**

All information about any existing facial images of the applicant in the [CIR](#page-45-2) SHALL be logged. This includes the number of images, whether an acceptable image is available and whether any of the acceptable images was used (information gathered within the FaceDelivery element). For each during the enrolment performed control verification the results SHALL be logged.

The location SHALL be logged by the name of the city or village where the biometric process takes place.

In order to allocate alien register enrolment logs to their respective application profile the element Applica tionProfile SHALL be filled as described in [Table 4.11.](#page-42-2)

<span id="page-42-2"></span>

| Application Profile within TR                                             | ApplicationProfile-Element                            |
|---------------------------------------------------------------------------|-------------------------------------------------------|
| Application Profile Arrival Attestation Document                          | ARE_ArrivalAttestationDocument                        |
| Application Profile Arrival Attestation Document in Special<br>Situations | ARE_ArrivalAttestationDocumentInSpecialSituati<br>ons |
|                                                                           |                                                       |

**Table 4.11** Mapping Logs to Application Profiles

### <span id="page-42-0"></span>**4.11.3. FM LOG-FI-GENERIC**

This Function Module describes requirements and interfaces for the logging of information regarding facial images for all profiles.

#### **4.11.3.1. Requirements**

- **•** Within a transaction for each facial image acquisition or delivery performed for enrolment, verification or identification, all data defined in FaceAcquisition (of which some MAY be contained within a MultiModa lAcquisition) or FaceDelivery SHALL be collected, if available.
- **•** During an acquisition process, the available details for all captures SHALL be logged.
- **•** If a veto was put by the operator the type of veto (OK/NOK) SHALL be set.
- **•** Detailed quality information SHALL be logged at least for the selected facial image. The overall result MAY be omitted if it is undefined. For each criterion the identifier, upper and lower value bound as well as the upper and lower threshold bound SHALL be included if available. When more than one facial image is present, all face quality elements SHALL reference to the corresponding record element.
- **•** For each performed [PAD](#page-45-10) the detailed [PAD](#page-45-10) quality values accompanied by identifiers, upper and lower value bounds and upper and lower threshold bounds SHALL be collected.
- **•** If a user interface is available during the acquisition process, the displayed information, e.g. an indication of a PAD alert or live feedback screen SHALL be logged.
- **•** In case of abnormal termination of the facial image acquisition process or any of its sub-processes, the error code SHALL be logged. The vendor SHALL provide a detailed list of all error codes used with complete semantic descriptions.

#### <span id="page-42-1"></span>**4.11.4. FM LOG-FP-GENERIC**

This Function Module describes requirements and interfaces for the logging of information regarding finger print images for all profiles.

#### **4.11.4.1. Requirements**

- **•** Within a transaction for each fingerprint acquisition or delivery performed for enrolment, verification, control verification or identification, all data defined in FingerAcquisition (of which some MAY be con tained within a MultiModalAcquisition) or FingerDelivery SHALL be collected, if available. If a fingerprint could not be acquired, the reason for each missing finger SHALL be logged.
- **•** For each capture process of a dedicated fingerprint or slap, all available information SHALL be logged. In case of multiple captures for a finger or slap the number of the capture details for which slap was selected as the best capture SHALL be specified. Within the finger capture the reference to the corresponding record of the probe SHALL be set. Further details of each during capture performed attempt pro vided, including the reference to the corresponding record if available. In case of an unacceptable capture attempt the reason for rejection of this capture attempt SHALL be selected. If the rejection reason is other an error code detailing the reason of rejection SHALL be set.
- **•** If a veto was put by the operator the type of veto (OK/NOK) SHALL be set.
- **•** For the best capture attempt, detailed quality information about the result SHALL be logged. For all other capture attempts quality information, if calculated during the process, SHOULD be logged. For each finger or slap within a capture the quality result value and the threshold SHALL be presented within a range from 0 to 100 when available. If an overall quality value can be estimated by the quality assessment algorithm it SHALL be specified.
- **•** If a slap classification is performed during the acquisition process, the details SHALL be logged as Finger ClassifierInformation. This includes the classification results, information about the configured threshold of the algorithm and whether the classifier has been used in evaluation mode.
- **•** When a uniqueness check is performed, the results SHALL be collected. If the FMR is known, the security level for the uniqueness check SHALL be contained. The log SHALL specify all detected duplicate fingers.
- **•** For each performed [PAD](#page-45-10) the detailed [PAD quality values accompanied by identifiers, upper and lower va](#page-45-10) lue bounds and upper and lower threshold bounds SHALL be collected. In case the probe is a slap and a [PAD](#page-45-10) result is expected for each individual finger of the slap, the finger code SHALL be defined and [PAD](#page-45-10) information SHALL be present for each finger.
- **•** If a user interface is available during the acquisition process, the displayed information, e.g. an indication of a [PAD](#page-45-10) alert or live feedback screen SHALL be logged.
- **•** In unsupervised acquisition scenarios all available surveillance information SHALL be stored for each cor responding capture attempt. The surveillance image contained within a record SHALL be linked to the fin gerprint capture attempt.
- **•** It SHALL be logged if multiple persons have been detected or not during the fingerprint acquisition process or single capture attempts.
- **•** When the acquisition process is performed with the presence of a configured timeout the corresponding value SHALL be specified in milliseconds. The logging of the configured value SHALL be independent from the occurrence of a timeout.
- **•** If a control verification is performed (e.g. for rolled vs flat fingerprints or for fingerprints acquired at a [SSS](#page-45-20) vs fingerprints acquired at the counter) all available information SHALL be logged within a Verification element.
- **•** In case of abnormal termination of the fingerprint acquisition process or any of its sub-processes, the error code SHALL be logged. Errors during the fingerprint segmentation or uniqueness check SHALL be specified additionally by their corresponding error element. The vendor SHALL provide a detailed list of all error codes used with complete semantic descriptions.
- **•** Information about the configured pixel density in dpi (dots-per-inch) of the fingerprint scanner SHALL be contained in FingerAcquisition/Hardware/ConfigurationInformation using *PixelDensity* as type.

### <span id="page-43-0"></span>**4.12. FM Category Coding**

This Function Module [Coding \(COD\)](#page-45-31) contains the procedures to encode quality data as well as biometric data in defined formats. Interoperability is provided by means of standard compliant coding.

#### <span id="page-43-1"></span>**4.12.1. FM COD-ALL-ARE**

This Function Module describes requirements and interfaces for the overall coding of biometric biogra phic data used within the context of the Arrival Attestation Document.

#### **4.12.1.1. Requirements on Biometric and Biographic Data Encoding for the Central Foreigners Register**

Biographic data and the facial image are delivered to the Central Foreigners Register in the compressed format as defined by [Section 4.6](#page-36-6) with further encoding.

#### **4.12.1.2. Requirements on Biometric and Biographic Data Encoding in GSAT 3**

In general the XML-based standard [\[BIB\\_GSAT3\]](#page-46-5) does apply for coding of both biometric and biographic data of an applicant and process related data. Depending on the biometric modality, the corresponding coding Function Module SHALL be considered. The current version of the [GSAT3](#page-45-18) SHALL be used.

#### **4.12.1.3. Requirements on Encoding Logging Data**

- **•** The logging data as defined by the [Section 4.11 SHALL be encoded as XML according to the schema defini](#page-41-3) tion as are-log element. The XML encoding is defined by the XML schema definition in the file "are5v1.xsd" and referenced schema files.
- **•** Optional attributes and elements of the schema SHALL be considered as far as possible (e.g. error codes only need to be logged, in case an error occurred; an acquisition element is only required, in case an acquisition process has at least been started).
- **•** All log data SHALL be encoded as far as it is available throughout the acquisition process (e.g. fingerprint quality data is encoded if and only if fingerprint capture was performed).
- **•** The [GSAT3](#page-45-18) transaction container SHALL be embedded in the XML log (XMLRecord element) for conformance testing of the encoding. Alternatively, the base64 encoded [GSAT3](#page-45-18) transaction container SHALL be embed ded in the XML log (BinaryRecord element).

#### <span id="page-44-0"></span>**4.12.2. FM COD-FI-GSAT3**

This Function Module describes requirements and interfaces for the coding of facial images according to the German Standard for [AFIS](#page-45-4) transactions in XML format.

#### **4.12.2.1. Requirements on Encoding**

For data format and encoding, the XML-based standard [\[BIB\\_GSAT3\]](#page-46-5) SHALL apply. The current version of [GSAT3](#page-45-18) SHALL be used.

#### <span id="page-44-1"></span>**4.12.3. FM COD-FP-GSAT3**

This Function Module describes requirements and interfaces for the coding of fingerprint images according to the German Standard for [AFIS](#page-45-4) transactions in XML format.

#### **4.12.3.1. Requirements on Encoding**

For data format and encoding, the XML-based standard [\[BIB\\_GSAT3\]](#page-46-5) SHALL apply. The current version of the [GSAT3](#page-45-18) SHALL be used.

Note, if all fingers are available, a total number of 14 fingerprint records (itl:PackageFingerprintImageRecord) is to be transferred (10 fingerprints plus 4 slap images of right hand, left hand, right thumb and left thumb), regardless of the setting in use (4-1-4-1 or 4-4-2).

### <span id="page-45-0"></span>**List of Abbreviations**

<span id="page-45-31"></span><span id="page-45-30"></span><span id="page-45-29"></span><span id="page-45-28"></span><span id="page-45-27"></span><span id="page-45-26"></span><span id="page-45-25"></span><span id="page-45-24"></span><span id="page-45-23"></span><span id="page-45-22"></span><span id="page-45-21"></span><span id="page-45-20"></span><span id="page-45-19"></span><span id="page-45-18"></span><span id="page-45-17"></span><span id="page-45-16"></span><span id="page-45-15"></span><span id="page-45-14"></span><span id="page-45-13"></span><span id="page-45-12"></span><span id="page-45-11"></span><span id="page-45-10"></span><span id="page-45-9"></span><span id="page-45-8"></span><span id="page-45-7"></span><span id="page-45-6"></span><span id="page-45-5"></span><span id="page-45-4"></span><span id="page-45-3"></span><span id="page-45-2"></span><span id="page-45-1"></span>

| Abbreviation | Description                                     |
|--------------|-------------------------------------------------|
| ABIS         | Automated Biometric Identification System       |
| AFIS         | Automated Fingerprint Identification System     |
| AH           | Acquisition Hardware                            |
| ARE          | Alien Register Enrolment                        |
| AS           | Acquisition Software                            |
| BEA          | Biometric Evaluation Authority                  |
| BIP          | Biometric Image Processing                      |
| CIR          | Central Identity Register                       |
| CMP          | Biometric Comparison                            |
| COD          | Coding                                          |
| COM          | Compression                                     |
| CTF          | contrast transfer function                      |
| EBTS         | Electronic Biometric Transmission Specification |
| FM           | Function Module                                 |
| FMR          | false-match-rate                                |
| FNMR         | false-non-match-rate                            |
| GSAT3        | German Standard for AFIS Transactions Version 3 |
| GUI          | graphical user interface                        |
| HLBS         | High Level Biometric Services                   |
| LOG          | Logging                                         |
| NFIQ2.2      | NIST Fingerprint Image Quality 2.2              |
| O            | Operation                                       |
| PAD          | Presentation Attack Detection                   |
| PAP          | Partial Application Process                     |
| PIV          | Personal Identity Verification                  |
| QA           | Quality Assessment                              |
| REF          | Reference Storage                               |
| SNR          | signal-to-noise ratio                           |
| SSS          | self-service system                             |
| UI           | User Interface                                  |
| WSQ          | Wavelet Scalar Quantisation                     |

## <span id="page-46-0"></span> **Bibliography**

- <span id="page-46-2"></span>[BIB\_AKNV] *Ankunftsnachweisverordnung.*
- <span id="page-46-1"></span>[BIB\_AsylG] *Asylgesetz of 02. September 2008 (BGBl. I S. 1798), last changed by law from 20. July 2017 (BGBl. I S. 2780).*
- <span id="page-46-3"></span>[BIB\_AZRG] *Allgemeine Verwaltungsvorschrift zum Gesetz über das Ausländerzentralregister und zur Verord nung zur Durchführung des Gesetzes über das Ausländerzentralregister of 26. October 2009.*
- <span id="page-46-4"></span>[BIB\_AZRGDV] *Verordnung zur Durchführung des Gesetzes über das Ausländerzentralregister of 17. May 1995 (BGBl. I S. 695), last changed by Art. 3 VO zur Umsetzung aufenthaltsrechtlicher Richtlinien der EU Arbeits migration of 1. August 2017 (BGBl. I S. 3066).*
- <span id="page-46-9"></span>[BIB\_EBTS/F] *FBI Electronic Biometric Transmission Specification Version 11, Appendix F, April 2021.*
- <span id="page-46-5"></span>[BIB\_GSAT3] *German Standard for AFIS transactions. XML schema files current version..*
- <span id="page-46-8"></span>[BIB\_ICAO\_TR\_Portrait\_Quality] *ICAO Technical Report: Portrait Quality (Reference Facial Images for MRTD), version 1.0, April 2018.*
- <span id="page-46-14"></span>[BIB\_ISO\_10918-1] *ISO/IEC 10918-1:1994 "Information technology – Digital compression and coding of conti nuous-tone still images: Requirements and guidelines".*
- <span id="page-46-6"></span>[BIB\_ISO\_FACE] *ISO/IEC 19794-5:2005 "Information technology - Biometric data interchange formats – Part 5: Face image data".*
- <span id="page-46-7"></span>[BIB\_ISO\_FINGER] *ISO/IEC 19794-4:2005 "Information technology - Biometric data interchange formats – Part 4: Finger image data".*
- <span id="page-46-12"></span>[BIB\_ISO\_PAD\_1] *ISO/IEC 30107-1:2016 "Information technology – Biometric presentation attack detection – Part 1: Framework".*
- <span id="page-46-13"></span>[BIB\_ISO\_PAD\_3] *ISO/IEC 30107-3:2017 "Information technology – Biometric presentation attack detection – Part 3: Testing and reporting".*
- <span id="page-46-11"></span>[BIB\_NFIQ2.2] *NIST Fingerprint Image Quality 2.2.*
- <span id="page-46-10"></span>[BIB\_PIV] *Personal Identity Verification (PIV) Image Quality Specification for Single Finger Capture Devices, FBI/ CJIS Biometric Specifications, 10 July 2006.*